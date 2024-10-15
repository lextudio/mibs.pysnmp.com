# SNMP MIB module (MEDIAHAWK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MEDIAHAWK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:20:47 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ConcurrentComputerCorporation_ObjectIdentity = ObjectIdentity
concurrentComputerCorporation = _ConcurrentComputerCorporation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457)
)
_MediaHawkVideoServer_ObjectIdentity = ObjectIdentity
mediaHawkVideoServer = _MediaHawkVideoServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1)
)
_MediaHawkVSVP_ObjectIdentity = ObjectIdentity
mediaHawkVSVP = _MediaHawkVSVP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2)
)
_MhvsVPVideo_ObjectIdentity = ObjectIdentity
mhvsVPVideo = _MhvsVPVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1)
)
_MhvsVPVideoTable_Object = MibTable
mhvsVPVideoTable = _MhvsVPVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    mhvsVPVideoTable.setStatus("mandatory")
_MhvsVPVideoEntry_Object = MibTableRow
mhvsVPVideoEntry = _MhvsVPVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1)
)
mhvsVPVideoEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPVideoIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPVideoEntry.setStatus("mandatory")


class _MhvsVPVideoIndex_Type(Integer32):
    """Custom type mhvsVPVideoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPVideoIndex_Type.__name__ = "Integer32"
_MhvsVPVideoIndex_Object = MibTableColumn
mhvsVPVideoIndex = _MhvsVPVideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 1),
    _MhvsVPVideoIndex_Type()
)
mhvsVPVideoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoIndex.setStatus("mandatory")
_MhvsVPVideoName_Type = DisplayString
_MhvsVPVideoName_Object = MibTableColumn
mhvsVPVideoName = _MhvsVPVideoName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 2),
    _MhvsVPVideoName_Type()
)
mhvsVPVideoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoName.setStatus("mandatory")
_MhvsVPVideoNumCopies_Type = Gauge32
_MhvsVPVideoNumCopies_Object = MibTableColumn
mhvsVPVideoNumCopies = _MhvsVPVideoNumCopies_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 3),
    _MhvsVPVideoNumCopies_Type()
)
mhvsVPVideoNumCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoNumCopies.setStatus("mandatory")
_MhvsVPVideoSize_Type = Integer32
_MhvsVPVideoSize_Object = MibTableColumn
mhvsVPVideoSize = _MhvsVPVideoSize_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 4),
    _MhvsVPVideoSize_Type()
)
mhvsVPVideoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoSize.setStatus("mandatory")
_MhvsVPVideoNumOpen_Type = Gauge32
_MhvsVPVideoNumOpen_Object = MibTableColumn
mhvsVPVideoNumOpen = _MhvsVPVideoNumOpen_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 5),
    _MhvsVPVideoNumOpen_Type()
)
mhvsVPVideoNumOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoNumOpen.setStatus("mandatory")


class _MhvsVPVideoStatus_Type(Integer32):
    """Custom type mhvsVPVideoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPVideoStatus_Type.__name__ = "Integer32"
_MhvsVPVideoStatus_Object = MibTableColumn
mhvsVPVideoStatus = _MhvsVPVideoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 6),
    _MhvsVPVideoStatus_Type()
)
mhvsVPVideoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPVideoStatus.setStatus("mandatory")
_MhvsVPVideoContentSpace_Type = Integer32
_MhvsVPVideoContentSpace_Object = MibTableColumn
mhvsVPVideoContentSpace = _MhvsVPVideoContentSpace_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 7),
    _MhvsVPVideoContentSpace_Type()
)
mhvsVPVideoContentSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoContentSpace.setStatus("mandatory")
_MhvsVPVideoIndexSpace_Type = Integer32
_MhvsVPVideoIndexSpace_Object = MibTableColumn
mhvsVPVideoIndexSpace = _MhvsVPVideoIndexSpace_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 2, 1, 8),
    _MhvsVPVideoIndexSpace_Type()
)
mhvsVPVideoIndexSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoIndexSpace.setStatus("mandatory")
_MhvsVPVideoInstTable_Object = MibTable
mhvsVPVideoInstTable = _MhvsVPVideoInstTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    mhvsVPVideoInstTable.setStatus("mandatory")
_MhvsVPVideoInstEntry_Object = MibTableRow
mhvsVPVideoInstEntry = _MhvsVPVideoInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1)
)
mhvsVPVideoInstEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPVideoInstVideoIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPVideoInstIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPVideoInstEntry.setStatus("mandatory")


class _MhvsVPVideoInstVideoIndex_Type(Integer32):
    """Custom type mhvsVPVideoInstVideoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPVideoInstVideoIndex_Type.__name__ = "Integer32"
_MhvsVPVideoInstVideoIndex_Object = MibTableColumn
mhvsVPVideoInstVideoIndex = _MhvsVPVideoInstVideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 1),
    _MhvsVPVideoInstVideoIndex_Type()
)
mhvsVPVideoInstVideoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstVideoIndex.setStatus("mandatory")
_MhvsVPVideoInstDiskIndex_Type = Integer32
_MhvsVPVideoInstDiskIndex_Object = MibTableColumn
mhvsVPVideoInstDiskIndex = _MhvsVPVideoInstDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 3),
    _MhvsVPVideoInstDiskIndex_Type()
)
mhvsVPVideoInstDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstDiskIndex.setStatus("mandatory")
_MhvsVPVideoInstNumOpen_Type = Gauge32
_MhvsVPVideoInstNumOpen_Object = MibTableColumn
mhvsVPVideoInstNumOpen = _MhvsVPVideoInstNumOpen_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 4),
    _MhvsVPVideoInstNumOpen_Type()
)
mhvsVPVideoInstNumOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstNumOpen.setStatus("mandatory")


class _MhvsVPVideoInstStatus_Type(Integer32):
    """Custom type mhvsVPVideoInstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPVideoInstStatus_Type.__name__ = "Integer32"
_MhvsVPVideoInstStatus_Object = MibTableColumn
mhvsVPVideoInstStatus = _MhvsVPVideoInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 5),
    _MhvsVPVideoInstStatus_Type()
)
mhvsVPVideoInstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPVideoInstStatus.setStatus("mandatory")
_MhvsVPVideoInstPath_Type = DisplayString
_MhvsVPVideoInstPath_Object = MibTableColumn
mhvsVPVideoInstPath = _MhvsVPVideoInstPath_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 6),
    _MhvsVPVideoInstPath_Type()
)
mhvsVPVideoInstPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstPath.setStatus("mandatory")


class _MhvsVPVideoInstIndex_Type(Integer32):
    """Custom type mhvsVPVideoInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPVideoInstIndex_Type.__name__ = "Integer32"
_MhvsVPVideoInstIndex_Object = MibTableColumn
mhvsVPVideoInstIndex = _MhvsVPVideoInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 7),
    _MhvsVPVideoInstIndex_Type()
)
mhvsVPVideoInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstIndex.setStatus("mandatory")
_MhvsVPVideoInstSize_Type = Integer32
_MhvsVPVideoInstSize_Object = MibTableColumn
mhvsVPVideoInstSize = _MhvsVPVideoInstSize_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 3, 1, 8),
    _MhvsVPVideoInstSize_Type()
)
mhvsVPVideoInstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPVideoInstSize.setStatus("mandatory")


class _MhvsVPVideoTrapGeneration_Type(Integer32):
    """Custom type mhvsVPVideoTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_MhvsVPVideoTrapGeneration_Type.__name__ = "Integer32"
_MhvsVPVideoTrapGeneration_Object = MibScalar
mhvsVPVideoTrapGeneration = _MhvsVPVideoTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 1, 4),
    _MhvsVPVideoTrapGeneration_Type()
)
mhvsVPVideoTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPVideoTrapGeneration.setStatus("mandatory")
_MhvsVPResources_ObjectIdentity = ObjectIdentity
mhvsVPResources = _MhvsVPResources_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2)
)
_MhvsVPResourcesMaxStreams_Type = Gauge32
_MhvsVPResourcesMaxStreams_Object = MibScalar
mhvsVPResourcesMaxStreams = _MhvsVPResourcesMaxStreams_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 1),
    _MhvsVPResourcesMaxStreams_Type()
)
mhvsVPResourcesMaxStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesMaxStreams.setStatus("mandatory")
_MhvsVPResourcesNumStreams_Type = Gauge32
_MhvsVPResourcesNumStreams_Object = MibScalar
mhvsVPResourcesNumStreams = _MhvsVPResourcesNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 2),
    _MhvsVPResourcesNumStreams_Type()
)
mhvsVPResourcesNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNumStreams.setStatus("mandatory")
_MhvsVPResourcesMaxBandwidth_Type = Gauge32
_MhvsVPResourcesMaxBandwidth_Object = MibScalar
mhvsVPResourcesMaxBandwidth = _MhvsVPResourcesMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 3),
    _MhvsVPResourcesMaxBandwidth_Type()
)
mhvsVPResourcesMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesMaxBandwidth.setStatus("mandatory")
_MhvsVPResourcesBandwidth_Type = Gauge32
_MhvsVPResourcesBandwidth_Object = MibScalar
mhvsVPResourcesBandwidth = _MhvsVPResourcesBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 4),
    _MhvsVPResourcesBandwidth_Type()
)
mhvsVPResourcesBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesBandwidth.setStatus("mandatory")
_MhvsVPResourcesVPTable_Object = MibTable
mhvsVPResourcesVPTable = _MhvsVPResourcesVPTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesVPTable.setStatus("mandatory")
_MhvsVPResourcesVPEntry_Object = MibTableRow
mhvsVPResourcesVPEntry = _MhvsVPResourcesVPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1)
)
mhvsVPResourcesVPEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesVPIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesVPEntry.setStatus("mandatory")


class _MhvsVPResourcesVPIndex_Type(Integer32):
    """Custom type mhvsVPResourcesVPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesVPIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesVPIndex_Object = MibTableColumn
mhvsVPResourcesVPIndex = _MhvsVPResourcesVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 1),
    _MhvsVPResourcesVPIndex_Type()
)
mhvsVPResourcesVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPIndex.setStatus("mandatory")
_MhvsVPResourcesVPMax_Type = Gauge32
_MhvsVPResourcesVPMax_Object = MibTableColumn
mhvsVPResourcesVPMax = _MhvsVPResourcesVPMax_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 2),
    _MhvsVPResourcesVPMax_Type()
)
mhvsVPResourcesVPMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPMax.setStatus("mandatory")
_MhvsVPResourcesVPUsed_Type = Gauge32
_MhvsVPResourcesVPUsed_Object = MibTableColumn
mhvsVPResourcesVPUsed = _MhvsVPResourcesVPUsed_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 3),
    _MhvsVPResourcesVPUsed_Type()
)
mhvsVPResourcesVPUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPUsed.setStatus("mandatory")
_MhvsVPResourcesVPNumStreams_Type = Gauge32
_MhvsVPResourcesVPNumStreams_Object = MibTableColumn
mhvsVPResourcesVPNumStreams = _MhvsVPResourcesVPNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 4),
    _MhvsVPResourcesVPNumStreams_Type()
)
mhvsVPResourcesVPNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPNumStreams.setStatus("mandatory")


class _MhvsVPResourcesVPStatus_Type(Integer32):
    """Custom type mhvsVPResourcesVPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesVPStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesVPStatus_Object = MibTableColumn
mhvsVPResourcesVPStatus = _MhvsVPResourcesVPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 5),
    _MhvsVPResourcesVPStatus_Type()
)
mhvsVPResourcesVPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPStatus.setStatus("mandatory")


class _MhvsVPResourcesVPConnected_Type(Integer32):
    """Custom type mhvsVPResourcesVPConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MhvsVPResourcesVPConnected_Type.__name__ = "Integer32"
_MhvsVPResourcesVPConnected_Object = MibTableColumn
mhvsVPResourcesVPConnected = _MhvsVPResourcesVPConnected_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 6),
    _MhvsVPResourcesVPConnected_Type()
)
mhvsVPResourcesVPConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPConnected.setStatus("mandatory")
_MhvsVPResourcesVPHostIndex_Type = Integer32
_MhvsVPResourcesVPHostIndex_Object = MibTableColumn
mhvsVPResourcesVPHostIndex = _MhvsVPResourcesVPHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 5, 1, 7),
    _MhvsVPResourcesVPHostIndex_Type()
)
mhvsVPResourcesVPHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesVPHostIndex.setStatus("mandatory")
_MhvsVPResourcesDiskTable_Object = MibTable
mhvsVPResourcesDiskTable = _MhvsVPResourcesDiskTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskTable.setStatus("mandatory")
_MhvsVPResourcesDiskEntry_Object = MibTableRow
mhvsVPResourcesDiskEntry = _MhvsVPResourcesDiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1)
)
mhvsVPResourcesDiskEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesDiskIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskEntry.setStatus("mandatory")


class _MhvsVPResourcesDiskIndex_Type(Integer32):
    """Custom type mhvsVPResourcesDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesDiskIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesDiskIndex_Object = MibTableColumn
mhvsVPResourcesDiskIndex = _MhvsVPResourcesDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 1),
    _MhvsVPResourcesDiskIndex_Type()
)
mhvsVPResourcesDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskIndex.setStatus("mandatory")
_MhvsVPResourcesDiskName_Type = DisplayString
_MhvsVPResourcesDiskName_Object = MibTableColumn
mhvsVPResourcesDiskName = _MhvsVPResourcesDiskName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 2),
    _MhvsVPResourcesDiskName_Type()
)
mhvsVPResourcesDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskName.setStatus("mandatory")
_MhvsVPResourcesDiskMax_Type = Gauge32
_MhvsVPResourcesDiskMax_Object = MibTableColumn
mhvsVPResourcesDiskMax = _MhvsVPResourcesDiskMax_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 3),
    _MhvsVPResourcesDiskMax_Type()
)
mhvsVPResourcesDiskMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskMax.setStatus("mandatory")
_MhvsVPResourcesDiskUsed_Type = Gauge32
_MhvsVPResourcesDiskUsed_Object = MibTableColumn
mhvsVPResourcesDiskUsed = _MhvsVPResourcesDiskUsed_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 4),
    _MhvsVPResourcesDiskUsed_Type()
)
mhvsVPResourcesDiskUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskUsed.setStatus("mandatory")
_MhvsVPResourcesDiskNumStreams_Type = Gauge32
_MhvsVPResourcesDiskNumStreams_Object = MibTableColumn
mhvsVPResourcesDiskNumStreams = _MhvsVPResourcesDiskNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 5),
    _MhvsVPResourcesDiskNumStreams_Type()
)
mhvsVPResourcesDiskNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskNumStreams.setStatus("mandatory")


class _MhvsVPResourcesDiskStatus_Type(Integer32):
    """Custom type mhvsVPResourcesDiskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesDiskStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesDiskStatus_Object = MibTableColumn
mhvsVPResourcesDiskStatus = _MhvsVPResourcesDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 6),
    _MhvsVPResourcesDiskStatus_Type()
)
mhvsVPResourcesDiskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskStatus.setStatus("mandatory")
_MhvsVPResourcesDiskMaxCapacity_Type = Integer32
_MhvsVPResourcesDiskMaxCapacity_Object = MibTableColumn
mhvsVPResourcesDiskMaxCapacity = _MhvsVPResourcesDiskMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 7),
    _MhvsVPResourcesDiskMaxCapacity_Type()
)
mhvsVPResourcesDiskMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskMaxCapacity.setStatus("mandatory")
_MhvsVPResourcesDiskUsedCapacity_Type = Integer32
_MhvsVPResourcesDiskUsedCapacity_Object = MibTableColumn
mhvsVPResourcesDiskUsedCapacity = _MhvsVPResourcesDiskUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 8),
    _MhvsVPResourcesDiskUsedCapacity_Type()
)
mhvsVPResourcesDiskUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskUsedCapacity.setStatus("mandatory")
_MhvsVPResourcesDiskMaxSysCapacity_Type = Integer32
_MhvsVPResourcesDiskMaxSysCapacity_Object = MibTableColumn
mhvsVPResourcesDiskMaxSysCapacity = _MhvsVPResourcesDiskMaxSysCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 9),
    _MhvsVPResourcesDiskMaxSysCapacity_Type()
)
mhvsVPResourcesDiskMaxSysCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskMaxSysCapacity.setStatus("mandatory")
_MhvsVPResourcesDiskUsedSysCapacity_Type = Integer32
_MhvsVPResourcesDiskUsedSysCapacity_Object = MibTableColumn
mhvsVPResourcesDiskUsedSysCapacity = _MhvsVPResourcesDiskUsedSysCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 6, 1, 10),
    _MhvsVPResourcesDiskUsedSysCapacity_Type()
)
mhvsVPResourcesDiskUsedSysCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskUsedSysCapacity.setStatus("mandatory")
_MhvsVPResourcesNetwTable_Object = MibTable
mhvsVPResourcesNetwTable = _MhvsVPResourcesNetwTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwTable.setStatus("mandatory")
_MhvsVPResourcesNetwEntry_Object = MibTableRow
mhvsVPResourcesNetwEntry = _MhvsVPResourcesNetwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1)
)
mhvsVPResourcesNetwEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesNetwType"),
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesNetwIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwEntry.setStatus("mandatory")


class _MhvsVPResourcesNetwIndex_Type(Integer32):
    """Custom type mhvsVPResourcesNetwIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesNetwIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwIndex_Object = MibTableColumn
mhvsVPResourcesNetwIndex = _MhvsVPResourcesNetwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 1),
    _MhvsVPResourcesNetwIndex_Type()
)
mhvsVPResourcesNetwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwIndex.setStatus("mandatory")
_MhvsVPResourcesNetwMax_Type = Gauge32
_MhvsVPResourcesNetwMax_Object = MibTableColumn
mhvsVPResourcesNetwMax = _MhvsVPResourcesNetwMax_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 3),
    _MhvsVPResourcesNetwMax_Type()
)
mhvsVPResourcesNetwMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwMax.setStatus("mandatory")
_MhvsVPResourcesNetwUsed_Type = Gauge32
_MhvsVPResourcesNetwUsed_Object = MibTableColumn
mhvsVPResourcesNetwUsed = _MhvsVPResourcesNetwUsed_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 4),
    _MhvsVPResourcesNetwUsed_Type()
)
mhvsVPResourcesNetwUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwUsed.setStatus("mandatory")
_MhvsVPResourcesNetwNumStreams_Type = Gauge32
_MhvsVPResourcesNetwNumStreams_Object = MibTableColumn
mhvsVPResourcesNetwNumStreams = _MhvsVPResourcesNetwNumStreams_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 5),
    _MhvsVPResourcesNetwNumStreams_Type()
)
mhvsVPResourcesNetwNumStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwNumStreams.setStatus("mandatory")


class _MhvsVPResourcesNetwType_Type(Integer32):
    """Custom type mhvsVPResourcesNetwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 6),
          ("codec", 5),
          ("dvb", 3),
          ("ip", 7),
          ("qam", 4))
    )


_MhvsVPResourcesNetwType_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwType_Object = MibTableColumn
mhvsVPResourcesNetwType = _MhvsVPResourcesNetwType_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 6),
    _MhvsVPResourcesNetwType_Type()
)
mhvsVPResourcesNetwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwType.setStatus("mandatory")
_MhvsVPResourcesNetwId_Type = DisplayString
_MhvsVPResourcesNetwId_Object = MibTableColumn
mhvsVPResourcesNetwId = _MhvsVPResourcesNetwId_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 7),
    _MhvsVPResourcesNetwId_Type()
)
mhvsVPResourcesNetwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwId.setStatus("mandatory")


class _MhvsVPResourcesNetwStatus_Type(Integer32):
    """Custom type mhvsVPResourcesNetwStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesNetwStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwStatus_Object = MibTableColumn
mhvsVPResourcesNetwStatus = _MhvsVPResourcesNetwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 7, 1, 8),
    _MhvsVPResourcesNetwStatus_Type()
)
mhvsVPResourcesNetwStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwStatus.setStatus("mandatory")
_MhvsVPResourcesSPTable_Object = MibTable
mhvsVPResourcesSPTable = _MhvsVPResourcesSPTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesSPTable.setStatus("mandatory")
_MhvsVPResourcesSPEntry_Object = MibTableRow
mhvsVPResourcesSPEntry = _MhvsVPResourcesSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1)
)
mhvsVPResourcesSPEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesSPIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesSPEntry.setStatus("mandatory")


class _MhvsVPResourcesSPIndex_Type(Integer32):
    """Custom type mhvsVPResourcesSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesSPIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesSPIndex_Object = MibTableColumn
mhvsVPResourcesSPIndex = _MhvsVPResourcesSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 1),
    _MhvsVPResourcesSPIndex_Type()
)
mhvsVPResourcesSPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPIndex.setStatus("mandatory")
_MhvsVPResourcesSPMax_Type = Gauge32
_MhvsVPResourcesSPMax_Object = MibTableColumn
mhvsVPResourcesSPMax = _MhvsVPResourcesSPMax_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 2),
    _MhvsVPResourcesSPMax_Type()
)
mhvsVPResourcesSPMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPMax.setStatus("mandatory")
_MhvsVPResourcesSPUsed_Type = Gauge32
_MhvsVPResourcesSPUsed_Object = MibTableColumn
mhvsVPResourcesSPUsed = _MhvsVPResourcesSPUsed_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 3),
    _MhvsVPResourcesSPUsed_Type()
)
mhvsVPResourcesSPUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPUsed.setStatus("mandatory")


class _MhvsVPResourcesSPStatus_Type(Integer32):
    """Custom type mhvsVPResourcesSPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesSPStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesSPStatus_Object = MibTableColumn
mhvsVPResourcesSPStatus = _MhvsVPResourcesSPStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 4),
    _MhvsVPResourcesSPStatus_Type()
)
mhvsVPResourcesSPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPStatus.setStatus("mandatory")


class _MhvsVPResourcesSPConnected_Type(Integer32):
    """Custom type mhvsVPResourcesSPConnected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MhvsVPResourcesSPConnected_Type.__name__ = "Integer32"
_MhvsVPResourcesSPConnected_Object = MibTableColumn
mhvsVPResourcesSPConnected = _MhvsVPResourcesSPConnected_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 5),
    _MhvsVPResourcesSPConnected_Type()
)
mhvsVPResourcesSPConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPConnected.setStatus("mandatory")
_MhvsVPResourcesSPHostIndex_Type = Integer32
_MhvsVPResourcesSPHostIndex_Object = MibTableColumn
mhvsVPResourcesSPHostIndex = _MhvsVPResourcesSPHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 8, 1, 6),
    _MhvsVPResourcesSPHostIndex_Type()
)
mhvsVPResourcesSPHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesSPHostIndex.setStatus("mandatory")
_MhvsVPResourcesDiskAttTable_Object = MibTable
mhvsVPResourcesDiskAttTable = _MhvsVPResourcesDiskAttTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttTable.setStatus("mandatory")
_MhvsVPResourcesDiskAttEntry_Object = MibTableRow
mhvsVPResourcesDiskAttEntry = _MhvsVPResourcesDiskAttEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1)
)
mhvsVPResourcesDiskAttEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesDiskAttDiskIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesDiskAttIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttEntry.setStatus("mandatory")


class _MhvsVPResourcesDiskAttDiskIndex_Type(Integer32):
    """Custom type mhvsVPResourcesDiskAttDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesDiskAttDiskIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesDiskAttDiskIndex_Object = MibTableColumn
mhvsVPResourcesDiskAttDiskIndex = _MhvsVPResourcesDiskAttDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1, 1),
    _MhvsVPResourcesDiskAttDiskIndex_Type()
)
mhvsVPResourcesDiskAttDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttDiskIndex.setStatus("mandatory")
_MhvsVPResourcesDiskAttVPIndex_Type = Integer32
_MhvsVPResourcesDiskAttVPIndex_Object = MibTableColumn
mhvsVPResourcesDiskAttVPIndex = _MhvsVPResourcesDiskAttVPIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1, 2),
    _MhvsVPResourcesDiskAttVPIndex_Type()
)
mhvsVPResourcesDiskAttVPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttVPIndex.setStatus("mandatory")
_MhvsVPResourcesDiskAttDir_Type = DisplayString
_MhvsVPResourcesDiskAttDir_Object = MibTableColumn
mhvsVPResourcesDiskAttDir = _MhvsVPResourcesDiskAttDir_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1, 3),
    _MhvsVPResourcesDiskAttDir_Type()
)
mhvsVPResourcesDiskAttDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttDir.setStatus("mandatory")


class _MhvsVPResourcesDiskAttStatus_Type(Integer32):
    """Custom type mhvsVPResourcesDiskAttStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesDiskAttStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesDiskAttStatus_Object = MibTableColumn
mhvsVPResourcesDiskAttStatus = _MhvsVPResourcesDiskAttStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1, 4),
    _MhvsVPResourcesDiskAttStatus_Type()
)
mhvsVPResourcesDiskAttStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttStatus.setStatus("mandatory")


class _MhvsVPResourcesDiskAttIndex_Type(Integer32):
    """Custom type mhvsVPResourcesDiskAttIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesDiskAttIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesDiskAttIndex_Object = MibTableColumn
mhvsVPResourcesDiskAttIndex = _MhvsVPResourcesDiskAttIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 9, 1, 5),
    _MhvsVPResourcesDiskAttIndex_Type()
)
mhvsVPResourcesDiskAttIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttIndex.setStatus("mandatory")
_MhvsVPResourcesNetwAttTable_Object = MibTable
mhvsVPResourcesNetwAttTable = _MhvsVPResourcesNetwAttTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10)
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttTable.setStatus("mandatory")
_MhvsVPResourcesNetwAttEntry_Object = MibTableRow
mhvsVPResourcesNetwAttEntry = _MhvsVPResourcesNetwAttEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1)
)
mhvsVPResourcesNetwAttEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesNetwAttFromType"),
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesNetwAttFromIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPResourcesNetwAttIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttEntry.setStatus("mandatory")


class _MhvsVPResourcesNetwAttFromType_Type(Integer32):
    """Custom type mhvsVPResourcesNetwAttFromType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 6),
          ("codec", 5),
          ("dvb", 3),
          ("ip", 7),
          ("qam", 4))
    )


_MhvsVPResourcesNetwAttFromType_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwAttFromType_Object = MibTableColumn
mhvsVPResourcesNetwAttFromType = _MhvsVPResourcesNetwAttFromType_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 1),
    _MhvsVPResourcesNetwAttFromType_Type()
)
mhvsVPResourcesNetwAttFromType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttFromType.setStatus("mandatory")


class _MhvsVPResourcesNetwAttFromIndex_Type(Integer32):
    """Custom type mhvsVPResourcesNetwAttFromIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesNetwAttFromIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwAttFromIndex_Object = MibTableColumn
mhvsVPResourcesNetwAttFromIndex = _MhvsVPResourcesNetwAttFromIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 2),
    _MhvsVPResourcesNetwAttFromIndex_Type()
)
mhvsVPResourcesNetwAttFromIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttFromIndex.setStatus("mandatory")


class _MhvsVPResourcesNetwAttToType_Type(Integer32):
    """Custom type mhvsVPResourcesNetwAttToType based on Integer32"""
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
        *(("atm", 6),
          ("codec", 5),
          ("disk", 2),
          ("dvb", 3),
          ("ip", 7),
          ("qam", 4),
          ("vp", 1))
    )


_MhvsVPResourcesNetwAttToType_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwAttToType_Object = MibTableColumn
mhvsVPResourcesNetwAttToType = _MhvsVPResourcesNetwAttToType_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 3),
    _MhvsVPResourcesNetwAttToType_Type()
)
mhvsVPResourcesNetwAttToType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttToType.setStatus("mandatory")
_MhvsVPResourcesNetwAttToIndex_Type = Integer32
_MhvsVPResourcesNetwAttToIndex_Object = MibTableColumn
mhvsVPResourcesNetwAttToIndex = _MhvsVPResourcesNetwAttToIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 4),
    _MhvsVPResourcesNetwAttToIndex_Type()
)
mhvsVPResourcesNetwAttToIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttToIndex.setStatus("mandatory")


class _MhvsVPResourcesNetwAttStatus_Type(Integer32):
    """Custom type mhvsVPResourcesNetwAttStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPResourcesNetwAttStatus_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwAttStatus_Object = MibTableColumn
mhvsVPResourcesNetwAttStatus = _MhvsVPResourcesNetwAttStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 5),
    _MhvsVPResourcesNetwAttStatus_Type()
)
mhvsVPResourcesNetwAttStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttStatus.setStatus("mandatory")


class _MhvsVPResourcesNetwAttIndex_Type(Integer32):
    """Custom type mhvsVPResourcesNetwAttIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPResourcesNetwAttIndex_Type.__name__ = "Integer32"
_MhvsVPResourcesNetwAttIndex_Object = MibTableColumn
mhvsVPResourcesNetwAttIndex = _MhvsVPResourcesNetwAttIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 6),
    _MhvsVPResourcesNetwAttIndex_Type()
)
mhvsVPResourcesNetwAttIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttIndex.setStatus("mandatory")
_MhvsVPResourcesNetwAttName_Type = DisplayString
_MhvsVPResourcesNetwAttName_Object = MibTableColumn
mhvsVPResourcesNetwAttName = _MhvsVPResourcesNetwAttName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 10, 1, 7),
    _MhvsVPResourcesNetwAttName_Type()
)
mhvsVPResourcesNetwAttName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttName.setStatus("mandatory")


class _MhvsVPResourcesTrapGeneration_Type(Integer32):
    """Custom type mhvsVPResourcesTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_MhvsVPResourcesTrapGeneration_Type.__name__ = "Integer32"
_MhvsVPResourcesTrapGeneration_Object = MibScalar
mhvsVPResourcesTrapGeneration = _MhvsVPResourcesTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 2, 11),
    _MhvsVPResourcesTrapGeneration_Type()
)
mhvsVPResourcesTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPResourcesTrapGeneration.setStatus("mandatory")
_MhvsVPStreams_ObjectIdentity = ObjectIdentity
mhvsVPStreams = _MhvsVPStreams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3)
)


class _MhvsVPStreamsTrapGeneration_Type(Integer32):
    """Custom type mhvsVPStreamsTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("openClose", 2),
          ("stateChange", 3))
    )


_MhvsVPStreamsTrapGeneration_Type.__name__ = "Integer32"
_MhvsVPStreamsTrapGeneration_Object = MibScalar
mhvsVPStreamsTrapGeneration = _MhvsVPStreamsTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 1),
    _MhvsVPStreamsTrapGeneration_Type()
)
mhvsVPStreamsTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPStreamsTrapGeneration.setStatus("mandatory")
_MhvsVPStreamsVideoTable_Object = MibTable
mhvsVPStreamsVideoTable = _MhvsVPStreamsVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoTable.setStatus("mandatory")
_MhvsVPStreamsVideoEntry_Object = MibTableRow
mhvsVPStreamsVideoEntry = _MhvsVPStreamsVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2, 1)
)
mhvsVPStreamsVideoEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsVideoSSEIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsVideoSIIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsVideoDiskIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsVideoVideoIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoEntry.setStatus("mandatory")


class _MhvsVPStreamsVideoSSEIndex_Type(Integer32):
    """Custom type mhvsVPStreamsVideoSSEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MhvsVPStreamsVideoSSEIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsVideoSSEIndex_Object = MibTableColumn
mhvsVPStreamsVideoSSEIndex = _MhvsVPStreamsVideoSSEIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2, 1, 1),
    _MhvsVPStreamsVideoSSEIndex_Type()
)
mhvsVPStreamsVideoSSEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoSSEIndex.setStatus("mandatory")


class _MhvsVPStreamsVideoSIIndex_Type(Integer32):
    """Custom type mhvsVPStreamsVideoSIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MhvsVPStreamsVideoSIIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsVideoSIIndex_Object = MibTableColumn
mhvsVPStreamsVideoSIIndex = _MhvsVPStreamsVideoSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2, 1, 2),
    _MhvsVPStreamsVideoSIIndex_Type()
)
mhvsVPStreamsVideoSIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoSIIndex.setStatus("mandatory")


class _MhvsVPStreamsVideoDiskIndex_Type(Integer32):
    """Custom type mhvsVPStreamsVideoDiskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPStreamsVideoDiskIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsVideoDiskIndex_Object = MibTableColumn
mhvsVPStreamsVideoDiskIndex = _MhvsVPStreamsVideoDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2, 1, 3),
    _MhvsVPStreamsVideoDiskIndex_Type()
)
mhvsVPStreamsVideoDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoDiskIndex.setStatus("mandatory")


class _MhvsVPStreamsVideoVideoIndex_Type(Integer32):
    """Custom type mhvsVPStreamsVideoVideoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPStreamsVideoVideoIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsVideoVideoIndex_Object = MibTableColumn
mhvsVPStreamsVideoVideoIndex = _MhvsVPStreamsVideoVideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 2, 1, 4),
    _MhvsVPStreamsVideoVideoIndex_Type()
)
mhvsVPStreamsVideoVideoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsVideoVideoIndex.setStatus("mandatory")
_MhvsVPStreamsNetwTable_Object = MibTable
mhvsVPStreamsNetwTable = _MhvsVPStreamsNetwTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3)
)
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwTable.setStatus("mandatory")
_MhvsVPStreamsNetwEntry_Object = MibTableRow
mhvsVPStreamsNetwEntry = _MhvsVPStreamsNetwEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3, 1)
)
mhvsVPStreamsNetwEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsNetwSSEIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsNetwSIIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPStreamsNetwNetwType"),
)
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwEntry.setStatus("mandatory")


class _MhvsVPStreamsNetwSSEIndex_Type(Integer32):
    """Custom type mhvsVPStreamsNetwSSEIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MhvsVPStreamsNetwSSEIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsNetwSSEIndex_Object = MibTableColumn
mhvsVPStreamsNetwSSEIndex = _MhvsVPStreamsNetwSSEIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3, 1, 1),
    _MhvsVPStreamsNetwSSEIndex_Type()
)
mhvsVPStreamsNetwSSEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwSSEIndex.setStatus("mandatory")


class _MhvsVPStreamsNetwSIIndex_Type(Integer32):
    """Custom type mhvsVPStreamsNetwSIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MhvsVPStreamsNetwSIIndex_Type.__name__ = "Integer32"
_MhvsVPStreamsNetwSIIndex_Object = MibTableColumn
mhvsVPStreamsNetwSIIndex = _MhvsVPStreamsNetwSIIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3, 1, 2),
    _MhvsVPStreamsNetwSIIndex_Type()
)
mhvsVPStreamsNetwSIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwSIIndex.setStatus("mandatory")


class _MhvsVPStreamsNetwNetwType_Type(Integer32):
    """Custom type mhvsVPStreamsNetwNetwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("atm", 6),
          ("codec", 5),
          ("dvb", 3),
          ("ip", 7),
          ("qam", 4))
    )


_MhvsVPStreamsNetwNetwType_Type.__name__ = "Integer32"
_MhvsVPStreamsNetwNetwType_Object = MibTableColumn
mhvsVPStreamsNetwNetwType = _MhvsVPStreamsNetwNetwType_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3, 1, 3),
    _MhvsVPStreamsNetwNetwType_Type()
)
mhvsVPStreamsNetwNetwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwNetwType.setStatus("mandatory")
_MhvsVPStreamsNetwNetwIndex_Type = Integer32
_MhvsVPStreamsNetwNetwIndex_Object = MibTableColumn
mhvsVPStreamsNetwNetwIndex = _MhvsVPStreamsNetwNetwIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 3, 3, 1, 4),
    _MhvsVPStreamsNetwNetwIndex_Type()
)
mhvsVPStreamsNetwNetwIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPStreamsNetwNetwIndex.setStatus("mandatory")
_MhvsVPMenu_ObjectIdentity = ObjectIdentity
mhvsVPMenu = _MhvsVPMenu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4)
)
_MhvsVPMenuTable_Object = MibTable
mhvsVPMenuTable = _MhvsVPMenuTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    mhvsVPMenuTable.setStatus("mandatory")
_MhvsVPMenuEntry_Object = MibTableRow
mhvsVPMenuEntry = _MhvsVPMenuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1)
)
mhvsVPMenuEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPMenuIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPMenuEntry.setStatus("mandatory")


class _MhvsVPMenuIndex_Type(Integer32):
    """Custom type mhvsVPMenuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPMenuIndex_Type.__name__ = "Integer32"
_MhvsVPMenuIndex_Object = MibTableColumn
mhvsVPMenuIndex = _MhvsVPMenuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1, 1),
    _MhvsVPMenuIndex_Type()
)
mhvsVPMenuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuIndex.setStatus("mandatory")
_MhvsVPMenuName_Type = DisplayString
_MhvsVPMenuName_Object = MibTableColumn
mhvsVPMenuName = _MhvsVPMenuName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1, 2),
    _MhvsVPMenuName_Type()
)
mhvsVPMenuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuName.setStatus("mandatory")
_MhvsVPMenuNumCopies_Type = Gauge32
_MhvsVPMenuNumCopies_Object = MibTableColumn
mhvsVPMenuNumCopies = _MhvsVPMenuNumCopies_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1, 3),
    _MhvsVPMenuNumCopies_Type()
)
mhvsVPMenuNumCopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuNumCopies.setStatus("mandatory")
_MhvsVPMenuNumOpen_Type = Gauge32
_MhvsVPMenuNumOpen_Object = MibTableColumn
mhvsVPMenuNumOpen = _MhvsVPMenuNumOpen_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1, 5),
    _MhvsVPMenuNumOpen_Type()
)
mhvsVPMenuNumOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuNumOpen.setStatus("mandatory")


class _MhvsVPMenuStatus_Type(Integer32):
    """Custom type mhvsVPMenuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPMenuStatus_Type.__name__ = "Integer32"
_MhvsVPMenuStatus_Object = MibTableColumn
mhvsVPMenuStatus = _MhvsVPMenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 2, 1, 6),
    _MhvsVPMenuStatus_Type()
)
mhvsVPMenuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPMenuStatus.setStatus("mandatory")
_MhvsVPMenuInstTable_Object = MibTable
mhvsVPMenuInstTable = _MhvsVPMenuInstTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3)
)
if mibBuilder.loadTexts:
    mhvsVPMenuInstTable.setStatus("mandatory")
_MhvsVPMenuInstEntry_Object = MibTableRow
mhvsVPMenuInstEntry = _MhvsVPMenuInstEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1)
)
mhvsVPMenuInstEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhvsVPMenuInstMenuIndex"),
    (0, "MEDIAHAWK-MIB", "mhvsVPMenuInstIndex"),
)
if mibBuilder.loadTexts:
    mhvsVPMenuInstEntry.setStatus("mandatory")


class _MhvsVPMenuInstMenuIndex_Type(Integer32):
    """Custom type mhvsVPMenuInstMenuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPMenuInstMenuIndex_Type.__name__ = "Integer32"
_MhvsVPMenuInstMenuIndex_Object = MibTableColumn
mhvsVPMenuInstMenuIndex = _MhvsVPMenuInstMenuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 1),
    _MhvsVPMenuInstMenuIndex_Type()
)
mhvsVPMenuInstMenuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuInstMenuIndex.setStatus("mandatory")
_MhvsVPMenuInstDiskIndex_Type = Integer32
_MhvsVPMenuInstDiskIndex_Object = MibTableColumn
mhvsVPMenuInstDiskIndex = _MhvsVPMenuInstDiskIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 3),
    _MhvsVPMenuInstDiskIndex_Type()
)
mhvsVPMenuInstDiskIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuInstDiskIndex.setStatus("mandatory")
_MhvsVPMenuInstNumOpen_Type = Gauge32
_MhvsVPMenuInstNumOpen_Object = MibTableColumn
mhvsVPMenuInstNumOpen = _MhvsVPMenuInstNumOpen_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 4),
    _MhvsVPMenuInstNumOpen_Type()
)
mhvsVPMenuInstNumOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuInstNumOpen.setStatus("mandatory")


class _MhvsVPMenuInstStatus_Type(Integer32):
    """Custom type mhvsVPMenuInstStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 1),
          ("disabled", 2),
          ("enabled", 6),
          ("failed", 4),
          ("quiesce", 3),
          ("standby", 5))
    )


_MhvsVPMenuInstStatus_Type.__name__ = "Integer32"
_MhvsVPMenuInstStatus_Object = MibTableColumn
mhvsVPMenuInstStatus = _MhvsVPMenuInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 5),
    _MhvsVPMenuInstStatus_Type()
)
mhvsVPMenuInstStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPMenuInstStatus.setStatus("mandatory")
_MhvsVPMenuInstPath_Type = DisplayString
_MhvsVPMenuInstPath_Object = MibTableColumn
mhvsVPMenuInstPath = _MhvsVPMenuInstPath_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 6),
    _MhvsVPMenuInstPath_Type()
)
mhvsVPMenuInstPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuInstPath.setStatus("mandatory")


class _MhvsVPMenuInstIndex_Type(Integer32):
    """Custom type mhvsVPMenuInstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_MhvsVPMenuInstIndex_Type.__name__ = "Integer32"
_MhvsVPMenuInstIndex_Object = MibTableColumn
mhvsVPMenuInstIndex = _MhvsVPMenuInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 3, 1, 7),
    _MhvsVPMenuInstIndex_Type()
)
mhvsVPMenuInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhvsVPMenuInstIndex.setStatus("mandatory")


class _MhvsVPMenuTrapGeneration_Type(Integer32):
    """Custom type mhvsVPMenuTrapGeneration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("on", 1)
    )


_MhvsVPMenuTrapGeneration_Type.__name__ = "Integer32"
_MhvsVPMenuTrapGeneration_Object = MibScalar
mhvsVPMenuTrapGeneration = _MhvsVPMenuTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 2, 4, 4),
    _MhvsVPMenuTrapGeneration_Type()
)
mhvsVPMenuTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhvsVPMenuTrapGeneration.setStatus("mandatory")
_MediaHawkVEMon_ObjectIdentity = ObjectIdentity
mediaHawkVEMon = _MediaHawkVEMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3)
)


class _MediaHawkVEMonAlive_Type(Integer32):
    """Custom type mediaHawkVEMonAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MediaHawkVEMonAlive_Type.__name__ = "Integer32"
_MediaHawkVEMonAlive_Object = MibScalar
mediaHawkVEMonAlive = _MediaHawkVEMonAlive_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 1),
    _MediaHawkVEMonAlive_Type()
)
mediaHawkVEMonAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaHawkVEMonAlive.setStatus("mandatory")
_MediaHawkDVBTable_Object = MibTable
mediaHawkDVBTable = _MediaHawkDVBTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2)
)
if mibBuilder.loadTexts:
    mediaHawkDVBTable.setStatus("mandatory")
_MediaHawkDVBEntry_Object = MibTableRow
mediaHawkDVBEntry = _MediaHawkDVBEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1)
)
mediaHawkDVBEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhDVBName"),
)
if mibBuilder.loadTexts:
    mediaHawkDVBEntry.setStatus("mandatory")


class _MhDVBStatus_Type(Integer32):
    """Custom type mhDVBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MhDVBStatus_Type.__name__ = "Integer32"
_MhDVBStatus_Object = MibTableColumn
mhDVBStatus = _MhDVBStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 1),
    _MhDVBStatus_Type()
)
mhDVBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBStatus.setStatus("mandatory")


class _MhDVBName_Type(DisplayString):
    """Custom type mhDVBName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhDVBName_Type.__name__ = "DisplayString"
_MhDVBName_Object = MibTableColumn
mhDVBName = _MhDVBName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 2),
    _MhDVBName_Type()
)
mhDVBName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBName.setStatus("mandatory")
_MhDVBMTU_Type = Integer32
_MhDVBMTU_Object = MibTableColumn
mhDVBMTU = _MhDVBMTU_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 3),
    _MhDVBMTU_Type()
)
mhDVBMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBMTU.setStatus("mandatory")
_MhDVBReceivePackets_Type = Integer32
_MhDVBReceivePackets_Object = MibTableColumn
mhDVBReceivePackets = _MhDVBReceivePackets_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 4),
    _MhDVBReceivePackets_Type()
)
mhDVBReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBReceivePackets.setStatus("mandatory")
_MhDVBReceiveErrors_Type = Integer32
_MhDVBReceiveErrors_Object = MibTableColumn
mhDVBReceiveErrors = _MhDVBReceiveErrors_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 5),
    _MhDVBReceiveErrors_Type()
)
mhDVBReceiveErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBReceiveErrors.setStatus("mandatory")
_MhDVBTransmitPackets_Type = Integer32
_MhDVBTransmitPackets_Object = MibTableColumn
mhDVBTransmitPackets = _MhDVBTransmitPackets_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 6),
    _MhDVBTransmitPackets_Type()
)
mhDVBTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBTransmitPackets.setStatus("mandatory")
_MhDVBTransmitErrors_Type = Integer32
_MhDVBTransmitErrors_Object = MibTableColumn
mhDVBTransmitErrors = _MhDVBTransmitErrors_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 7),
    _MhDVBTransmitErrors_Type()
)
mhDVBTransmitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBTransmitErrors.setStatus("mandatory")
_MhDVBTransmitKBytesPerSec_Type = Integer32
_MhDVBTransmitKBytesPerSec_Object = MibTableColumn
mhDVBTransmitKBytesPerSec = _MhDVBTransmitKBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 2, 1, 8),
    _MhDVBTransmitKBytesPerSec_Type()
)
mhDVBTransmitKBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDVBTransmitKBytesPerSec.setStatus("mandatory")
_MediaHawkDisk_ObjectIdentity = ObjectIdentity
mediaHawkDisk = _MediaHawkDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3)
)
_MhDiskNumDisks_Type = Integer32
_MhDiskNumDisks_Object = MibScalar
mhDiskNumDisks = _MhDiskNumDisks_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 1),
    _MhDiskNumDisks_Type()
)
mhDiskNumDisks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskNumDisks.setStatus("mandatory")
_MhDiskKBytesPerSec_Type = Integer32
_MhDiskKBytesPerSec_Object = MibScalar
mhDiskKBytesPerSec = _MhDiskKBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 2),
    _MhDiskKBytesPerSec_Type()
)
mhDiskKBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskKBytesPerSec.setStatus("mandatory")
_MhDiskDrivesTable_Object = MibTable
mhDiskDrivesTable = _MhDiskDrivesTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3)
)
if mibBuilder.loadTexts:
    mhDiskDrivesTable.setStatus("mandatory")
_MhDiskDrivesEntry_Object = MibTableRow
mhDiskDrivesEntry = _MhDiskDrivesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1)
)
mhDiskDrivesEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhDiskDriveName"),
)
if mibBuilder.loadTexts:
    mhDiskDrivesEntry.setStatus("mandatory")


class _MhDiskDriveName_Type(DisplayString):
    """Custom type mhDiskDriveName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhDiskDriveName_Type.__name__ = "DisplayString"
_MhDiskDriveName_Object = MibTableColumn
mhDiskDriveName = _MhDiskDriveName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 1),
    _MhDiskDriveName_Type()
)
mhDiskDriveName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveName.setStatus("mandatory")
_MhDiskDriveReads_Type = Integer32
_MhDiskDriveReads_Object = MibTableColumn
mhDiskDriveReads = _MhDiskDriveReads_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 2),
    _MhDiskDriveReads_Type()
)
mhDiskDriveReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveReads.setStatus("mandatory")
_MhDiskDriveWrites_Type = Integer32
_MhDiskDriveWrites_Object = MibTableColumn
mhDiskDriveWrites = _MhDiskDriveWrites_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 3),
    _MhDiskDriveWrites_Type()
)
mhDiskDriveWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveWrites.setStatus("mandatory")
_MhDiskDriveReadKBytes_Type = Integer32
_MhDiskDriveReadKBytes_Object = MibTableColumn
mhDiskDriveReadKBytes = _MhDiskDriveReadKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 4),
    _MhDiskDriveReadKBytes_Type()
)
mhDiskDriveReadKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveReadKBytes.setStatus("mandatory")
_MhDiskDriveWriteKBytes_Type = Integer32
_MhDiskDriveWriteKBytes_Object = MibTableColumn
mhDiskDriveWriteKBytes = _MhDiskDriveWriteKBytes_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 5),
    _MhDiskDriveWriteKBytes_Type()
)
mhDiskDriveWriteKBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveWriteKBytes.setStatus("mandatory")
_MhDiskDriveReadKBytesPerSec_Type = Integer32
_MhDiskDriveReadKBytesPerSec_Object = MibTableColumn
mhDiskDriveReadKBytesPerSec = _MhDiskDriveReadKBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 6),
    _MhDiskDriveReadKBytesPerSec_Type()
)
mhDiskDriveReadKBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveReadKBytesPerSec.setStatus("mandatory")
_MhDiskDriveWriteKBytesPerSec_Type = Integer32
_MhDiskDriveWriteKBytesPerSec_Object = MibTableColumn
mhDiskDriveWriteKBytesPerSec = _MhDiskDriveWriteKBytesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 3, 1, 7),
    _MhDiskDriveWriteKBytesPerSec_Type()
)
mhDiskDriveWriteKBytesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhDiskDriveWriteKBytesPerSec.setStatus("mandatory")


class _MhContentMounted_Type(Integer32):
    """Custom type mhContentMounted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MhContentMounted_Type.__name__ = "Integer32"
_MhContentMounted_Object = MibScalar
mhContentMounted = _MhContentMounted_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 3, 4),
    _MhContentMounted_Type()
)
mhContentMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhContentMounted.setStatus("mandatory")
_MediaHawkEnvironment_ObjectIdentity = ObjectIdentity
mediaHawkEnvironment = _MediaHawkEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4)
)
_MhEnvironmentFanTable_Object = MibTable
mhEnvironmentFanTable = _MhEnvironmentFanTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 1)
)
if mibBuilder.loadTexts:
    mhEnvironmentFanTable.setStatus("mandatory")
_MhEnvironmentFanEntry_Object = MibTableRow
mhEnvironmentFanEntry = _MhEnvironmentFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 1, 1)
)
mhEnvironmentFanEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhEnvironmentFanLocation"),
)
if mibBuilder.loadTexts:
    mhEnvironmentFanEntry.setStatus("mandatory")


class _MhEnvironmentFanLocation_Type(DisplayString):
    """Custom type mhEnvironmentFanLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhEnvironmentFanLocation_Type.__name__ = "DisplayString"
_MhEnvironmentFanLocation_Object = MibTableColumn
mhEnvironmentFanLocation = _MhEnvironmentFanLocation_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 1, 1, 1),
    _MhEnvironmentFanLocation_Type()
)
mhEnvironmentFanLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentFanLocation.setStatus("mandatory")


class _MhEnvironmentFanStatus_Type(Integer32):
    """Custom type mhEnvironmentFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("working", 1)
    )


_MhEnvironmentFanStatus_Type.__name__ = "Integer32"
_MhEnvironmentFanStatus_Object = MibTableColumn
mhEnvironmentFanStatus = _MhEnvironmentFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 1, 1, 2),
    _MhEnvironmentFanStatus_Type()
)
mhEnvironmentFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentFanStatus.setStatus("mandatory")
_MhEnvironmentPowerSupplyTable_Object = MibTable
mhEnvironmentPowerSupplyTable = _MhEnvironmentPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 2)
)
if mibBuilder.loadTexts:
    mhEnvironmentPowerSupplyTable.setStatus("mandatory")
_MhEnvironmentPowerSupplyEntry_Object = MibTableRow
mhEnvironmentPowerSupplyEntry = _MhEnvironmentPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 2, 1)
)
mhEnvironmentPowerSupplyEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhEnvironmentPowerSupplyLocation"),
)
if mibBuilder.loadTexts:
    mhEnvironmentPowerSupplyEntry.setStatus("mandatory")


class _MhEnvironmentPowerSupplyLocation_Type(DisplayString):
    """Custom type mhEnvironmentPowerSupplyLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhEnvironmentPowerSupplyLocation_Type.__name__ = "DisplayString"
_MhEnvironmentPowerSupplyLocation_Object = MibTableColumn
mhEnvironmentPowerSupplyLocation = _MhEnvironmentPowerSupplyLocation_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 2, 1, 1),
    _MhEnvironmentPowerSupplyLocation_Type()
)
mhEnvironmentPowerSupplyLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentPowerSupplyLocation.setStatus("mandatory")


class _MhEnvironmentPowerSupplyStatus_Type(Integer32):
    """Custom type mhEnvironmentPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mising", -1),
          ("working", 1))
    )


_MhEnvironmentPowerSupplyStatus_Type.__name__ = "Integer32"
_MhEnvironmentPowerSupplyStatus_Object = MibTableColumn
mhEnvironmentPowerSupplyStatus = _MhEnvironmentPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 2, 1, 2),
    _MhEnvironmentPowerSupplyStatus_Type()
)
mhEnvironmentPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentPowerSupplyStatus.setStatus("mandatory")
_MhEnvironmentTemperatureTable_Object = MibTable
mhEnvironmentTemperatureTable = _MhEnvironmentTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 3)
)
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureTable.setStatus("mandatory")
_MhEnvironmentTemperatureEntry_Object = MibTableRow
mhEnvironmentTemperatureEntry = _MhEnvironmentTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 3, 1)
)
mhEnvironmentTemperatureEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhEnvironmentTemperatureLocation"),
)
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureEntry.setStatus("mandatory")


class _MhEnvironmentTemperatureLocation_Type(DisplayString):
    """Custom type mhEnvironmentTemperatureLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhEnvironmentTemperatureLocation_Type.__name__ = "DisplayString"
_MhEnvironmentTemperatureLocation_Object = MibTableColumn
mhEnvironmentTemperatureLocation = _MhEnvironmentTemperatureLocation_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 3, 1, 1),
    _MhEnvironmentTemperatureLocation_Type()
)
mhEnvironmentTemperatureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureLocation.setStatus("mandatory")
_MhEnvironmentTemperatureValue_Type = Integer32
_MhEnvironmentTemperatureValue_Object = MibTableColumn
mhEnvironmentTemperatureValue = _MhEnvironmentTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 3, 1, 2),
    _MhEnvironmentTemperatureValue_Type()
)
mhEnvironmentTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureValue.setStatus("mandatory")
_MhEnvironmentTemperatureRedLine_Type = Integer32
_MhEnvironmentTemperatureRedLine_Object = MibTableColumn
mhEnvironmentTemperatureRedLine = _MhEnvironmentTemperatureRedLine_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 4, 3, 1, 3),
    _MhEnvironmentTemperatureRedLine_Type()
)
mhEnvironmentTemperatureRedLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureRedLine.setStatus("mandatory")


class _MediaHawkVideoEngineHealth_Type(Integer32):
    """Custom type mediaHawkVideoEngineHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 3),
          ("red", 1),
          ("yellow", 2))
    )


_MediaHawkVideoEngineHealth_Type.__name__ = "Integer32"
_MediaHawkVideoEngineHealth_Object = MibScalar
mediaHawkVideoEngineHealth = _MediaHawkVideoEngineHealth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 5),
    _MediaHawkVideoEngineHealth_Type()
)
mediaHawkVideoEngineHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaHawkVideoEngineHealth.setStatus("mandatory")


class _MediaHawkArrayHealth_Type(Integer32):
    """Custom type mediaHawkArrayHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("green", 3),
          ("red", 1),
          ("yellow", 2))
    )


_MediaHawkArrayHealth_Type.__name__ = "Integer32"
_MediaHawkArrayHealth_Object = MibScalar
mediaHawkArrayHealth = _MediaHawkArrayHealth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 6),
    _MediaHawkArrayHealth_Type()
)
mediaHawkArrayHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaHawkArrayHealth.setStatus("mandatory")
_MediaHawkShutdown_Type = DisplayString
_MediaHawkShutdown_Object = MibScalar
mediaHawkShutdown = _MediaHawkShutdown_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 7),
    _MediaHawkShutdown_Type()
)
mediaHawkShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaHawkShutdown.setStatus("mandatory")
_MediaHawkDiskDisable_Type = DisplayString
_MediaHawkDiskDisable_Object = MibScalar
mediaHawkDiskDisable = _MediaHawkDiskDisable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 8),
    _MediaHawkDiskDisable_Type()
)
mediaHawkDiskDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaHawkDiskDisable.setStatus("mandatory")
_MediaHawkDiskEnable_Type = DisplayString
_MediaHawkDiskEnable_Object = MibScalar
mediaHawkDiskEnable = _MediaHawkDiskEnable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 3, 9),
    _MediaHawkDiskEnable_Type()
)
mediaHawkDiskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaHawkDiskEnable.setStatus("mandatory")
_MediaHawkVPMon_ObjectIdentity = ObjectIdentity
mediaHawkVPMon = _MediaHawkVPMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4)
)


class _MediaHawkVPMonAlive_Type(Integer32):
    """Custom type mediaHawkVPMonAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_MediaHawkVPMonAlive_Type.__name__ = "Integer32"
_MediaHawkVPMonAlive_Object = MibScalar
mediaHawkVPMonAlive = _MediaHawkVPMonAlive_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 1),
    _MediaHawkVPMonAlive_Type()
)
mediaHawkVPMonAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaHawkVPMonAlive.setStatus("mandatory")
_MhPartitionLastUnit_Type = Integer32
_MhPartitionLastUnit_Object = MibScalar
mhPartitionLastUnit = _MhPartitionLastUnit_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 2),
    _MhPartitionLastUnit_Type()
)
mhPartitionLastUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionLastUnit.setStatus("mandatory")
_MhPartitionCount_Type = Integer32
_MhPartitionCount_Object = MibScalar
mhPartitionCount = _MhPartitionCount_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 3),
    _MhPartitionCount_Type()
)
mhPartitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionCount.setStatus("mandatory")
_MhPartitionsTable_Object = MibTable
mhPartitionsTable = _MhPartitionsTable_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4)
)
if mibBuilder.loadTexts:
    mhPartitionsTable.setStatus("mandatory")
_MhPartitionsEntry_Object = MibTableRow
mhPartitionsEntry = _MhPartitionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1)
)
mhPartitionsEntry.setIndexNames(
    (0, "MEDIAHAWK-MIB", "mhPartitionName"),
)
if mibBuilder.loadTexts:
    mhPartitionsEntry.setStatus("mandatory")


class _MhPartitionName_Type(DisplayString):
    """Custom type mhPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MhPartitionName_Type.__name__ = "DisplayString"
_MhPartitionName_Object = MibTableColumn
mhPartitionName = _MhPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 1),
    _MhPartitionName_Type()
)
mhPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionName.setStatus("mandatory")
_MhPartitionType_Type = DisplayString
_MhPartitionType_Object = MibTableColumn
mhPartitionType = _MhPartitionType_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 2),
    _MhPartitionType_Type()
)
mhPartitionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionType.setStatus("mandatory")
_MhPartitionState_Type = DisplayString
_MhPartitionState_Object = MibTableColumn
mhPartitionState = _MhPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 3),
    _MhPartitionState_Type()
)
mhPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionState.setStatus("mandatory")
_MhPartitionActiveReadCount_Type = Integer32
_MhPartitionActiveReadCount_Object = MibTableColumn
mhPartitionActiveReadCount = _MhPartitionActiveReadCount_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 4),
    _MhPartitionActiveReadCount_Type()
)
mhPartitionActiveReadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionActiveReadCount.setStatus("mandatory")
_MhPartitionActiveWriteCount_Type = Integer32
_MhPartitionActiveWriteCount_Object = MibTableColumn
mhPartitionActiveWriteCount = _MhPartitionActiveWriteCount_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 5),
    _MhPartitionActiveWriteCount_Type()
)
mhPartitionActiveWriteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionActiveWriteCount.setStatus("mandatory")
_MhPartitionTotalErrors_Type = Integer32
_MhPartitionTotalErrors_Object = MibTableColumn
mhPartitionTotalErrors = _MhPartitionTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 6),
    _MhPartitionTotalErrors_Type()
)
mhPartitionTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionTotalErrors.setStatus("mandatory")
_MhPartitionSliceSize_Type = Integer32
_MhPartitionSliceSize_Object = MibTableColumn
mhPartitionSliceSize = _MhPartitionSliceSize_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 7),
    _MhPartitionSliceSize_Type()
)
mhPartitionSliceSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionSliceSize.setStatus("mandatory")
_MhPartitionSizeKbytes_Type = Integer32
_MhPartitionSizeKbytes_Object = MibTableColumn
mhPartitionSizeKbytes = _MhPartitionSizeKbytes_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 8),
    _MhPartitionSizeKbytes_Type()
)
mhPartitionSizeKbytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionSizeKbytes.setStatus("mandatory")
_MhPartitionReaderMode_Type = DisplayString
_MhPartitionReaderMode_Object = MibTableColumn
mhPartitionReaderMode = _MhPartitionReaderMode_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 9),
    _MhPartitionReaderMode_Type()
)
mhPartitionReaderMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhPartitionReaderMode.setStatus("mandatory")
_MhPartitionWriterMode_Type = Integer32
_MhPartitionWriterMode_Object = MibTableColumn
mhPartitionWriterMode = _MhPartitionWriterMode_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 10),
    _MhPartitionWriterMode_Type()
)
mhPartitionWriterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhPartitionWriterMode.setStatus("mandatory")
_MhPartitionRestoreThrottle_Type = Integer32
_MhPartitionRestoreThrottle_Object = MibTableColumn
mhPartitionRestoreThrottle = _MhPartitionRestoreThrottle_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 11),
    _MhPartitionRestoreThrottle_Type()
)
mhPartitionRestoreThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhPartitionRestoreThrottle.setStatus("mandatory")
_MhPartitionProgressMeter_Type = DisplayString
_MhPartitionProgressMeter_Object = MibTableColumn
mhPartitionProgressMeter = _MhPartitionProgressMeter_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 12),
    _MhPartitionProgressMeter_Type()
)
mhPartitionProgressMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionProgressMeter.setStatus("mandatory")
_MhPartitionMemberCount_Type = Integer32
_MhPartitionMemberCount_Object = MibTableColumn
mhPartitionMemberCount = _MhPartitionMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 13),
    _MhPartitionMemberCount_Type()
)
mhPartitionMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionMemberCount.setStatus("mandatory")
_MhPartitionMemberDevices_Type = DisplayString
_MhPartitionMemberDevices_Object = MibTableColumn
mhPartitionMemberDevices = _MhPartitionMemberDevices_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 14),
    _MhPartitionMemberDevices_Type()
)
mhPartitionMemberDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionMemberDevices.setStatus("mandatory")
_MhPartitionStartRestore_Type = Integer32
_MhPartitionStartRestore_Object = MibTableColumn
mhPartitionStartRestore = _MhPartitionStartRestore_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 15),
    _MhPartitionStartRestore_Type()
)
mhPartitionStartRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhPartitionStartRestore.setStatus("mandatory")
_MhPartitionCancelRestore_Type = Integer32
_MhPartitionCancelRestore_Object = MibTableColumn
mhPartitionCancelRestore = _MhPartitionCancelRestore_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 16),
    _MhPartitionCancelRestore_Type()
)
mhPartitionCancelRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mhPartitionCancelRestore.setStatus("mandatory")
_MpPartitionErrorMask_Type = Integer32
_MpPartitionErrorMask_Object = MibTableColumn
mpPartitionErrorMask = _MpPartitionErrorMask_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 17),
    _MpPartitionErrorMask_Type()
)
mpPartitionErrorMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpPartitionErrorMask.setStatus("mandatory")
_MhPartitionHealth_Type = DisplayString
_MhPartitionHealth_Object = MibTableColumn
mhPartitionHealth = _MhPartitionHealth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 18),
    _MhPartitionHealth_Type()
)
mhPartitionHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionHealth.setStatus("mandatory")
_MhPartitionRestoreStatus_Type = DisplayString
_MhPartitionRestoreStatus_Object = MibTableColumn
mhPartitionRestoreStatus = _MhPartitionRestoreStatus_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 19),
    _MhPartitionRestoreStatus_Type()
)
mhPartitionRestoreStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionRestoreStatus.setStatus("mandatory")
_MhPartitionRestoreDate_Type = DateAndTime
_MhPartitionRestoreDate_Object = MibTableColumn
mhPartitionRestoreDate = _MhPartitionRestoreDate_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 20),
    _MhPartitionRestoreDate_Type()
)
mhPartitionRestoreDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionRestoreDate.setStatus("mandatory")
_MhPartitionMountPoint_Type = DisplayString
_MhPartitionMountPoint_Object = MibTableColumn
mhPartitionMountPoint = _MhPartitionMountPoint_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 21),
    _MhPartitionMountPoint_Type()
)
mhPartitionMountPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionMountPoint.setStatus("mandatory")
_MhPartitionFreeSpace_Type = Integer32
_MhPartitionFreeSpace_Object = MibTableColumn
mhPartitionFreeSpace = _MhPartitionFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 4, 1, 22),
    _MhPartitionFreeSpace_Type()
)
mhPartitionFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhPartitionFreeSpace.setStatus("mandatory")
_MhVPSubsystemHealth_Type = DisplayString
_MhVPSubsystemHealth_Object = MibScalar
mhVPSubsystemHealth = _MhVPSubsystemHealth_Object(
    (1, 3, 6, 1, 4, 1, 1457, 1, 4, 5),
    _MhVPSubsystemHealth_Type()
)
mhVPSubsystemHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mhVPSubsystemHealth.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mhvsVPStreamChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 50)
)
if mibBuilder.loadTexts:
    mhvsVPStreamChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesSPChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 51)
)
mhvsVPResourcesSPChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesSPStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesSPChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesVPChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 52)
)
mhvsVPResourcesVPChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesVPStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesVPChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesDiskChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 53)
)
mhvsVPResourcesDiskChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesDiskStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesDiskAttChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 54)
)
mhvsVPResourcesDiskAttChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesDiskAttStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesDiskAttChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesNetwChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 55)
)
mhvsVPResourcesNetwChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesNetwStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwChangedStatus.setStatus(
        ""
    )

mhvsVPResourcesNetwAttChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 56)
)
mhvsVPResourcesNetwAttChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPResourcesNetwAttStatus")
)
if mibBuilder.loadTexts:
    mhvsVPResourcesNetwAttChangedStatus.setStatus(
        ""
    )

mhvsVPVideoChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 57)
)
mhvsVPVideoChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPVideoStatus")
)
if mibBuilder.loadTexts:
    mhvsVPVideoChangedStatus.setStatus(
        ""
    )

mhvsVPVideoInstChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 58)
)
mhvsVPVideoInstChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPVideoInstStatus")
)
if mibBuilder.loadTexts:
    mhvsVPVideoInstChangedStatus.setStatus(
        ""
    )

mhvsVPMenuChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 59)
)
mhvsVPMenuChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPMenuStatus")
)
if mibBuilder.loadTexts:
    mhvsVPMenuChangedStatus.setStatus(
        ""
    )

mhvsVPMenuInstChangedStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 60)
)
mhvsVPMenuInstChangedStatus.setObjects(
    ("MEDIAHAWK-MIB", "mhvsVPMenuInstStatus")
)
if mibBuilder.loadTexts:
    mhvsVPMenuInstChangedStatus.setStatus(
        ""
    )

mhProcessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 101)
)
mhProcessStart.setObjects(
    ("MEDIAHAWK-MIB", "mediaHawkVEMonAlive")
)
if mibBuilder.loadTexts:
    mhProcessStart.setStatus(
        ""
    )

mhProcessTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 102)
)
mhProcessTermination.setObjects(
    ("MEDIAHAWK-MIB", "mediaHawkVEMonAlive")
)
if mibBuilder.loadTexts:
    mhProcessTermination.setStatus(
        ""
    )

vpProcessStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 103)
)
vpProcessStart.setObjects(
    ("MEDIAHAWK-MIB", "mediaHawkVPMonAlive")
)
if mibBuilder.loadTexts:
    vpProcessStart.setStatus(
        ""
    )

vpProcessTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 104)
)
vpProcessTermination.setObjects(
    ("MEDIAHAWK-MIB", "mediaHawkVPMonAlive")
)
if mibBuilder.loadTexts:
    vpProcessTermination.setStatus(
        ""
    )

vpPartitionStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 105)
)
vpPartitionStateChanged.setObjects(
    ("MEDIAHAWK-MIB", "mhPartitionState")
)
if mibBuilder.loadTexts:
    vpPartitionStateChanged.setStatus(
        ""
    )

mhEnvironmentFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 106)
)
mhEnvironmentFanFailure.setObjects(
    ("MEDIAHAWK-MIB", "mhEnvironmentFanStatus")
)
if mibBuilder.loadTexts:
    mhEnvironmentFanFailure.setStatus(
        ""
    )

mhEnvironmentPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 107)
)
mhEnvironmentPowerSupplyFailure.setObjects(
    ("MEDIAHAWK-MIB", "mhEnvironmentPowerSupplyStatus")
)
if mibBuilder.loadTexts:
    mhEnvironmentPowerSupplyFailure.setStatus(
        ""
    )

mhEnvironmentTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 1457, 0, 108)
)
mhEnvironmentTemperatureAlarm.setObjects(
    ("MEDIAHAWK-MIB", "mhEnvironmentTemperatureValue")
)
if mibBuilder.loadTexts:
    mhEnvironmentTemperatureAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MEDIAHAWK-MIB",
    **{"concurrentComputerCorporation": concurrentComputerCorporation,
       "mhvsVPStreamChangedStatus": mhvsVPStreamChangedStatus,
       "mhvsVPResourcesSPChangedStatus": mhvsVPResourcesSPChangedStatus,
       "mhvsVPResourcesVPChangedStatus": mhvsVPResourcesVPChangedStatus,
       "mhvsVPResourcesDiskChangedStatus": mhvsVPResourcesDiskChangedStatus,
       "mhvsVPResourcesDiskAttChangedStatus": mhvsVPResourcesDiskAttChangedStatus,
       "mhvsVPResourcesNetwChangedStatus": mhvsVPResourcesNetwChangedStatus,
       "mhvsVPResourcesNetwAttChangedStatus": mhvsVPResourcesNetwAttChangedStatus,
       "mhvsVPVideoChangedStatus": mhvsVPVideoChangedStatus,
       "mhvsVPVideoInstChangedStatus": mhvsVPVideoInstChangedStatus,
       "mhvsVPMenuChangedStatus": mhvsVPMenuChangedStatus,
       "mhvsVPMenuInstChangedStatus": mhvsVPMenuInstChangedStatus,
       "mhProcessStart": mhProcessStart,
       "mhProcessTermination": mhProcessTermination,
       "vpProcessStart": vpProcessStart,
       "vpProcessTermination": vpProcessTermination,
       "vpPartitionStateChanged": vpPartitionStateChanged,
       "mhEnvironmentFanFailure": mhEnvironmentFanFailure,
       "mhEnvironmentPowerSupplyFailure": mhEnvironmentPowerSupplyFailure,
       "mhEnvironmentTemperatureAlarm": mhEnvironmentTemperatureAlarm,
       "mediaHawkVideoServer": mediaHawkVideoServer,
       "mediaHawkVSVP": mediaHawkVSVP,
       "mhvsVPVideo": mhvsVPVideo,
       "mhvsVPVideoTable": mhvsVPVideoTable,
       "mhvsVPVideoEntry": mhvsVPVideoEntry,
       "mhvsVPVideoIndex": mhvsVPVideoIndex,
       "mhvsVPVideoName": mhvsVPVideoName,
       "mhvsVPVideoNumCopies": mhvsVPVideoNumCopies,
       "mhvsVPVideoSize": mhvsVPVideoSize,
       "mhvsVPVideoNumOpen": mhvsVPVideoNumOpen,
       "mhvsVPVideoStatus": mhvsVPVideoStatus,
       "mhvsVPVideoContentSpace": mhvsVPVideoContentSpace,
       "mhvsVPVideoIndexSpace": mhvsVPVideoIndexSpace,
       "mhvsVPVideoInstTable": mhvsVPVideoInstTable,
       "mhvsVPVideoInstEntry": mhvsVPVideoInstEntry,
       "mhvsVPVideoInstVideoIndex": mhvsVPVideoInstVideoIndex,
       "mhvsVPVideoInstDiskIndex": mhvsVPVideoInstDiskIndex,
       "mhvsVPVideoInstNumOpen": mhvsVPVideoInstNumOpen,
       "mhvsVPVideoInstStatus": mhvsVPVideoInstStatus,
       "mhvsVPVideoInstPath": mhvsVPVideoInstPath,
       "mhvsVPVideoInstIndex": mhvsVPVideoInstIndex,
       "mhvsVPVideoInstSize": mhvsVPVideoInstSize,
       "mhvsVPVideoTrapGeneration": mhvsVPVideoTrapGeneration,
       "mhvsVPResources": mhvsVPResources,
       "mhvsVPResourcesMaxStreams": mhvsVPResourcesMaxStreams,
       "mhvsVPResourcesNumStreams": mhvsVPResourcesNumStreams,
       "mhvsVPResourcesMaxBandwidth": mhvsVPResourcesMaxBandwidth,
       "mhvsVPResourcesBandwidth": mhvsVPResourcesBandwidth,
       "mhvsVPResourcesVPTable": mhvsVPResourcesVPTable,
       "mhvsVPResourcesVPEntry": mhvsVPResourcesVPEntry,
       "mhvsVPResourcesVPIndex": mhvsVPResourcesVPIndex,
       "mhvsVPResourcesVPMax": mhvsVPResourcesVPMax,
       "mhvsVPResourcesVPUsed": mhvsVPResourcesVPUsed,
       "mhvsVPResourcesVPNumStreams": mhvsVPResourcesVPNumStreams,
       "mhvsVPResourcesVPStatus": mhvsVPResourcesVPStatus,
       "mhvsVPResourcesVPConnected": mhvsVPResourcesVPConnected,
       "mhvsVPResourcesVPHostIndex": mhvsVPResourcesVPHostIndex,
       "mhvsVPResourcesDiskTable": mhvsVPResourcesDiskTable,
       "mhvsVPResourcesDiskEntry": mhvsVPResourcesDiskEntry,
       "mhvsVPResourcesDiskIndex": mhvsVPResourcesDiskIndex,
       "mhvsVPResourcesDiskName": mhvsVPResourcesDiskName,
       "mhvsVPResourcesDiskMax": mhvsVPResourcesDiskMax,
       "mhvsVPResourcesDiskUsed": mhvsVPResourcesDiskUsed,
       "mhvsVPResourcesDiskNumStreams": mhvsVPResourcesDiskNumStreams,
       "mhvsVPResourcesDiskStatus": mhvsVPResourcesDiskStatus,
       "mhvsVPResourcesDiskMaxCapacity": mhvsVPResourcesDiskMaxCapacity,
       "mhvsVPResourcesDiskUsedCapacity": mhvsVPResourcesDiskUsedCapacity,
       "mhvsVPResourcesDiskMaxSysCapacity": mhvsVPResourcesDiskMaxSysCapacity,
       "mhvsVPResourcesDiskUsedSysCapacity": mhvsVPResourcesDiskUsedSysCapacity,
       "mhvsVPResourcesNetwTable": mhvsVPResourcesNetwTable,
       "mhvsVPResourcesNetwEntry": mhvsVPResourcesNetwEntry,
       "mhvsVPResourcesNetwIndex": mhvsVPResourcesNetwIndex,
       "mhvsVPResourcesNetwMax": mhvsVPResourcesNetwMax,
       "mhvsVPResourcesNetwUsed": mhvsVPResourcesNetwUsed,
       "mhvsVPResourcesNetwNumStreams": mhvsVPResourcesNetwNumStreams,
       "mhvsVPResourcesNetwType": mhvsVPResourcesNetwType,
       "mhvsVPResourcesNetwId": mhvsVPResourcesNetwId,
       "mhvsVPResourcesNetwStatus": mhvsVPResourcesNetwStatus,
       "mhvsVPResourcesSPTable": mhvsVPResourcesSPTable,
       "mhvsVPResourcesSPEntry": mhvsVPResourcesSPEntry,
       "mhvsVPResourcesSPIndex": mhvsVPResourcesSPIndex,
       "mhvsVPResourcesSPMax": mhvsVPResourcesSPMax,
       "mhvsVPResourcesSPUsed": mhvsVPResourcesSPUsed,
       "mhvsVPResourcesSPStatus": mhvsVPResourcesSPStatus,
       "mhvsVPResourcesSPConnected": mhvsVPResourcesSPConnected,
       "mhvsVPResourcesSPHostIndex": mhvsVPResourcesSPHostIndex,
       "mhvsVPResourcesDiskAttTable": mhvsVPResourcesDiskAttTable,
       "mhvsVPResourcesDiskAttEntry": mhvsVPResourcesDiskAttEntry,
       "mhvsVPResourcesDiskAttDiskIndex": mhvsVPResourcesDiskAttDiskIndex,
       "mhvsVPResourcesDiskAttVPIndex": mhvsVPResourcesDiskAttVPIndex,
       "mhvsVPResourcesDiskAttDir": mhvsVPResourcesDiskAttDir,
       "mhvsVPResourcesDiskAttStatus": mhvsVPResourcesDiskAttStatus,
       "mhvsVPResourcesDiskAttIndex": mhvsVPResourcesDiskAttIndex,
       "mhvsVPResourcesNetwAttTable": mhvsVPResourcesNetwAttTable,
       "mhvsVPResourcesNetwAttEntry": mhvsVPResourcesNetwAttEntry,
       "mhvsVPResourcesNetwAttFromType": mhvsVPResourcesNetwAttFromType,
       "mhvsVPResourcesNetwAttFromIndex": mhvsVPResourcesNetwAttFromIndex,
       "mhvsVPResourcesNetwAttToType": mhvsVPResourcesNetwAttToType,
       "mhvsVPResourcesNetwAttToIndex": mhvsVPResourcesNetwAttToIndex,
       "mhvsVPResourcesNetwAttStatus": mhvsVPResourcesNetwAttStatus,
       "mhvsVPResourcesNetwAttIndex": mhvsVPResourcesNetwAttIndex,
       "mhvsVPResourcesNetwAttName": mhvsVPResourcesNetwAttName,
       "mhvsVPResourcesTrapGeneration": mhvsVPResourcesTrapGeneration,
       "mhvsVPStreams": mhvsVPStreams,
       "mhvsVPStreamsTrapGeneration": mhvsVPStreamsTrapGeneration,
       "mhvsVPStreamsVideoTable": mhvsVPStreamsVideoTable,
       "mhvsVPStreamsVideoEntry": mhvsVPStreamsVideoEntry,
       "mhvsVPStreamsVideoSSEIndex": mhvsVPStreamsVideoSSEIndex,
       "mhvsVPStreamsVideoSIIndex": mhvsVPStreamsVideoSIIndex,
       "mhvsVPStreamsVideoDiskIndex": mhvsVPStreamsVideoDiskIndex,
       "mhvsVPStreamsVideoVideoIndex": mhvsVPStreamsVideoVideoIndex,
       "mhvsVPStreamsNetwTable": mhvsVPStreamsNetwTable,
       "mhvsVPStreamsNetwEntry": mhvsVPStreamsNetwEntry,
       "mhvsVPStreamsNetwSSEIndex": mhvsVPStreamsNetwSSEIndex,
       "mhvsVPStreamsNetwSIIndex": mhvsVPStreamsNetwSIIndex,
       "mhvsVPStreamsNetwNetwType": mhvsVPStreamsNetwNetwType,
       "mhvsVPStreamsNetwNetwIndex": mhvsVPStreamsNetwNetwIndex,
       "mhvsVPMenu": mhvsVPMenu,
       "mhvsVPMenuTable": mhvsVPMenuTable,
       "mhvsVPMenuEntry": mhvsVPMenuEntry,
       "mhvsVPMenuIndex": mhvsVPMenuIndex,
       "mhvsVPMenuName": mhvsVPMenuName,
       "mhvsVPMenuNumCopies": mhvsVPMenuNumCopies,
       "mhvsVPMenuNumOpen": mhvsVPMenuNumOpen,
       "mhvsVPMenuStatus": mhvsVPMenuStatus,
       "mhvsVPMenuInstTable": mhvsVPMenuInstTable,
       "mhvsVPMenuInstEntry": mhvsVPMenuInstEntry,
       "mhvsVPMenuInstMenuIndex": mhvsVPMenuInstMenuIndex,
       "mhvsVPMenuInstDiskIndex": mhvsVPMenuInstDiskIndex,
       "mhvsVPMenuInstNumOpen": mhvsVPMenuInstNumOpen,
       "mhvsVPMenuInstStatus": mhvsVPMenuInstStatus,
       "mhvsVPMenuInstPath": mhvsVPMenuInstPath,
       "mhvsVPMenuInstIndex": mhvsVPMenuInstIndex,
       "mhvsVPMenuTrapGeneration": mhvsVPMenuTrapGeneration,
       "mediaHawkVEMon": mediaHawkVEMon,
       "mediaHawkVEMonAlive": mediaHawkVEMonAlive,
       "mediaHawkDVBTable": mediaHawkDVBTable,
       "mediaHawkDVBEntry": mediaHawkDVBEntry,
       "mhDVBStatus": mhDVBStatus,
       "mhDVBName": mhDVBName,
       "mhDVBMTU": mhDVBMTU,
       "mhDVBReceivePackets": mhDVBReceivePackets,
       "mhDVBReceiveErrors": mhDVBReceiveErrors,
       "mhDVBTransmitPackets": mhDVBTransmitPackets,
       "mhDVBTransmitErrors": mhDVBTransmitErrors,
       "mhDVBTransmitKBytesPerSec": mhDVBTransmitKBytesPerSec,
       "mediaHawkDisk": mediaHawkDisk,
       "mhDiskNumDisks": mhDiskNumDisks,
       "mhDiskKBytesPerSec": mhDiskKBytesPerSec,
       "mhDiskDrivesTable": mhDiskDrivesTable,
       "mhDiskDrivesEntry": mhDiskDrivesEntry,
       "mhDiskDriveName": mhDiskDriveName,
       "mhDiskDriveReads": mhDiskDriveReads,
       "mhDiskDriveWrites": mhDiskDriveWrites,
       "mhDiskDriveReadKBytes": mhDiskDriveReadKBytes,
       "mhDiskDriveWriteKBytes": mhDiskDriveWriteKBytes,
       "mhDiskDriveReadKBytesPerSec": mhDiskDriveReadKBytesPerSec,
       "mhDiskDriveWriteKBytesPerSec": mhDiskDriveWriteKBytesPerSec,
       "mhContentMounted": mhContentMounted,
       "mediaHawkEnvironment": mediaHawkEnvironment,
       "mhEnvironmentFanTable": mhEnvironmentFanTable,
       "mhEnvironmentFanEntry": mhEnvironmentFanEntry,
       "mhEnvironmentFanLocation": mhEnvironmentFanLocation,
       "mhEnvironmentFanStatus": mhEnvironmentFanStatus,
       "mhEnvironmentPowerSupplyTable": mhEnvironmentPowerSupplyTable,
       "mhEnvironmentPowerSupplyEntry": mhEnvironmentPowerSupplyEntry,
       "mhEnvironmentPowerSupplyLocation": mhEnvironmentPowerSupplyLocation,
       "mhEnvironmentPowerSupplyStatus": mhEnvironmentPowerSupplyStatus,
       "mhEnvironmentTemperatureTable": mhEnvironmentTemperatureTable,
       "mhEnvironmentTemperatureEntry": mhEnvironmentTemperatureEntry,
       "mhEnvironmentTemperatureLocation": mhEnvironmentTemperatureLocation,
       "mhEnvironmentTemperatureValue": mhEnvironmentTemperatureValue,
       "mhEnvironmentTemperatureRedLine": mhEnvironmentTemperatureRedLine,
       "mediaHawkVideoEngineHealth": mediaHawkVideoEngineHealth,
       "mediaHawkArrayHealth": mediaHawkArrayHealth,
       "mediaHawkShutdown": mediaHawkShutdown,
       "mediaHawkDiskDisable": mediaHawkDiskDisable,
       "mediaHawkDiskEnable": mediaHawkDiskEnable,
       "mediaHawkVPMon": mediaHawkVPMon,
       "mediaHawkVPMonAlive": mediaHawkVPMonAlive,
       "mhPartitionLastUnit": mhPartitionLastUnit,
       "mhPartitionCount": mhPartitionCount,
       "mhPartitionsTable": mhPartitionsTable,
       "mhPartitionsEntry": mhPartitionsEntry,
       "mhPartitionName": mhPartitionName,
       "mhPartitionType": mhPartitionType,
       "mhPartitionState": mhPartitionState,
       "mhPartitionActiveReadCount": mhPartitionActiveReadCount,
       "mhPartitionActiveWriteCount": mhPartitionActiveWriteCount,
       "mhPartitionTotalErrors": mhPartitionTotalErrors,
       "mhPartitionSliceSize": mhPartitionSliceSize,
       "mhPartitionSizeKbytes": mhPartitionSizeKbytes,
       "mhPartitionReaderMode": mhPartitionReaderMode,
       "mhPartitionWriterMode": mhPartitionWriterMode,
       "mhPartitionRestoreThrottle": mhPartitionRestoreThrottle,
       "mhPartitionProgressMeter": mhPartitionProgressMeter,
       "mhPartitionMemberCount": mhPartitionMemberCount,
       "mhPartitionMemberDevices": mhPartitionMemberDevices,
       "mhPartitionStartRestore": mhPartitionStartRestore,
       "mhPartitionCancelRestore": mhPartitionCancelRestore,
       "mpPartitionErrorMask": mpPartitionErrorMask,
       "mhPartitionHealth": mhPartitionHealth,
       "mhPartitionRestoreStatus": mhPartitionRestoreStatus,
       "mhPartitionRestoreDate": mhPartitionRestoreDate,
       "mhPartitionMountPoint": mhPartitionMountPoint,
       "mhPartitionFreeSpace": mhPartitionFreeSpace,
       "mhVPSubsystemHealth": mhVPSubsystemHealth}
)
