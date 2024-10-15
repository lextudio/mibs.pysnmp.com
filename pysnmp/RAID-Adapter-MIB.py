# SNMP MIB module (RAID-Adapter-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAID-Adapter-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:27 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lsi_ObjectIdentity = ObjectIdentity
lsi = _Lsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3582)
)
_MegaRaid_ObjectIdentity = ObjectIdentity
megaRaid = _MegaRaid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3582, 1)
)
_MegaRaidMib_ObjectIdentity = ObjectIdentity
megaRaidMib = _MegaRaidMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1)
)
_AdapterTable_Object = MibTable
adapterTable = _AdapterTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adapterTable.setStatus("optional")
_AdapterEntry_Object = MibTableRow
adapterEntry = _AdapterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1)
)
adapterEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "adpAdapterNumber"),
)
if mibBuilder.loadTexts:
    adapterEntry.setStatus("optional")
_AdpAdapterNumber_Type = Integer32
_AdpAdapterNumber_Object = MibTableColumn
adpAdapterNumber = _AdpAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 1),
    _AdpAdapterNumber_Type()
)
adpAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpAdapterNumber.setStatus("optional")


class _NumLogicalDrives_Type(Integer32):
    """Custom type numLogicalDrives based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_NumLogicalDrives_Type.__name__ = "Integer32"
_NumLogicalDrives_Object = MibTableColumn
numLogicalDrives = _NumLogicalDrives_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 2),
    _NumLogicalDrives_Type()
)
numLogicalDrives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLogicalDrives.setStatus("optional")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibTableColumn
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 3),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("optional")
_BiosVersion_Type = DisplayString
_BiosVersion_Object = MibTableColumn
biosVersion = _BiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 4),
    _BiosVersion_Type()
)
biosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    biosVersion.setStatus("optional")
_DramSizeInMB_Type = Integer32
_DramSizeInMB_Object = MibTableColumn
dramSizeInMB = _DramSizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 5),
    _DramSizeInMB_Type()
)
dramSizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dramSizeInMB.setStatus("optional")


class _RebuildRateInPercent_Type(Integer32):
    """Custom type rebuildRateInPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RebuildRateInPercent_Type.__name__ = "Integer32"
_RebuildRateInPercent_Object = MibTableColumn
rebuildRateInPercent = _RebuildRateInPercent_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 6),
    _RebuildRateInPercent_Type()
)
rebuildRateInPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rebuildRateInPercent.setStatus("optional")


class _FlushInterval_Type(Integer32):
    """Custom type flushInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8,
              10)
        )
    )
    namedValues = NamedValues(
        *(("eightSec", 8),
          ("fourSec", 4),
          ("sixSec", 6),
          ("tenSec", 10),
          ("twoSec", 2))
    )


_FlushInterval_Type.__name__ = "Integer32"
_FlushInterval_Object = MibTableColumn
flushInterval = _FlushInterval_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 7),
    _FlushInterval_Type()
)
flushInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flushInterval.setStatus("optional")
_MaxConcurrentCmds_Type = Integer32
_MaxConcurrentCmds_Object = MibTableColumn
maxConcurrentCmds = _MaxConcurrentCmds_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 8),
    _MaxConcurrentCmds_Type()
)
maxConcurrentCmds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxConcurrentCmds.setStatus("optional")
_SpinupDelay_Type = Integer32
_SpinupDelay_Object = MibTableColumn
spinupDelay = _SpinupDelay_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 9),
    _SpinupDelay_Type()
)
spinupDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spinupDelay.setStatus("optional")
_SpinupCount_Type = Integer32
_SpinupCount_Object = MibTableColumn
spinupCount = _SpinupCount_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 10),
    _SpinupCount_Type()
)
spinupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spinupCount.setStatus("optional")
_AdpIOReadsPerSec_Type = Integer32
_AdpIOReadsPerSec_Object = MibTableColumn
adpIOReadsPerSec = _AdpIOReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 11),
    _AdpIOReadsPerSec_Type()
)
adpIOReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpIOReadsPerSec.setStatus("optional")
_AdpIOWritesPerSec_Type = Integer32
_AdpIOWritesPerSec_Object = MibTableColumn
adpIOWritesPerSec = _AdpIOWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 12),
    _AdpIOWritesPerSec_Type()
)
adpIOWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpIOWritesPerSec.setStatus("optional")
_AdpReadKBsPerSec_Type = Integer32
_AdpReadKBsPerSec_Object = MibTableColumn
adpReadKBsPerSec = _AdpReadKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 13),
    _AdpReadKBsPerSec_Type()
)
adpReadKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpReadKBsPerSec.setStatus("optional")
_AdpWriteKBsPerSec_Type = Integer32
_AdpWriteKBsPerSec_Object = MibTableColumn
adpWriteKBsPerSec = _AdpWriteKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 14),
    _AdpWriteKBsPerSec_Type()
)
adpWriteKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpWriteKBsPerSec.setStatus("optional")
_AdpReadFailuresPerSec_Type = Integer32
_AdpReadFailuresPerSec_Object = MibTableColumn
adpReadFailuresPerSec = _AdpReadFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 15),
    _AdpReadFailuresPerSec_Type()
)
adpReadFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpReadFailuresPerSec.setStatus("optional")
_AdpWriteFailuresPerSec_Type = Integer32
_AdpWriteFailuresPerSec_Object = MibTableColumn
adpWriteFailuresPerSec = _AdpWriteFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 16),
    _AdpWriteFailuresPerSec_Type()
)
adpWriteFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpWriteFailuresPerSec.setStatus("optional")


class _ScanChannels_Type(Integer32):
    """Custom type scanChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scanInProg", 3),
          ("scanOver", 1),
          ("startScan", 2))
    )


_ScanChannels_Type.__name__ = "Integer32"
_ScanChannels_Object = MibTableColumn
scanChannels = _ScanChannels_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 17),
    _ScanChannels_Type()
)
scanChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scanChannels.setStatus("optional")
_AdpBasePort_Type = DisplayString
_AdpBasePort_Object = MibTableColumn
adpBasePort = _AdpBasePort_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 18),
    _AdpBasePort_Type()
)
adpBasePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpBasePort.setStatus("optional")
_NumSCSIChannels_Type = Integer32
_NumSCSIChannels_Object = MibTableColumn
numSCSIChannels = _NumSCSIChannels_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 19),
    _NumSCSIChannels_Type()
)
numSCSIChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numSCSIChannels.setStatus("optional")
_NumFCLoops_Type = Integer32
_NumFCLoops_Object = MibTableColumn
numFCLoops = _NumFCLoops_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 20),
    _NumFCLoops_Type()
)
numFCLoops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numFCLoops.setStatus("optional")
_SubSystemID_Type = Integer32
_SubSystemID_Object = MibTableColumn
subSystemID = _SubSystemID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 21),
    _SubSystemID_Type()
)
subSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSystemID.setStatus("optional")
_SubSystemVendorID_Type = Integer32
_SubSystemVendorID_Object = MibTableColumn
subSystemVendorID = _SubSystemVendorID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 22),
    _SubSystemVendorID_Type()
)
subSystemVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subSystemVendorID.setStatus("optional")
_ProductName_Type = DisplayString
_ProductName_Object = MibTableColumn
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 23),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("optional")


class _AdpSpeed_Type(Integer32):
    """Custom type adpSpeed based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("eightyMB", 5),
          ("fiveMB", 1),
          ("fortyMB", 4),
          ("oneHundredSixtyMB", 6),
          ("tenMB", 2),
          ("threeHundredTwentyMB", 7),
          ("twentyMB", 3),
          ("unAvailable", 20))
    )


_AdpSpeed_Type.__name__ = "Integer32"
_AdpSpeed_Object = MibTableColumn
adpSpeed = _AdpSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 1, 1, 24),
    _AdpSpeed_Type()
)
adpSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adpSpeed.setStatus("optional")
_LogicaldriveTable_Object = MibTable
logicaldriveTable = _LogicaldriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2)
)
if mibBuilder.loadTexts:
    logicaldriveTable.setStatus("optional")
_LogicaldriveEntry_Object = MibTableRow
logicaldriveEntry = _LogicaldriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1)
)
logicaldriveEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "ldAdapterNumber"),
    (0, "RAID-Adapter-MIB", "logicalDriveNumber"),
)
if mibBuilder.loadTexts:
    logicaldriveEntry.setStatus("optional")
_LdAdapterNumber_Type = Integer32
_LdAdapterNumber_Object = MibTableColumn
ldAdapterNumber = _LdAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 1),
    _LdAdapterNumber_Type()
)
ldAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldAdapterNumber.setStatus("optional")
_LogicalDriveNumber_Type = Integer32
_LogicalDriveNumber_Object = MibTableColumn
logicalDriveNumber = _LogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 2),
    _LogicalDriveNumber_Type()
)
logicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logicalDriveNumber.setStatus("optional")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
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
        *(("checkConsistency", 4),
          ("degraded", 1),
          ("initialize", 3),
          ("offLine", 0),
          ("optimal", 2))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 3),
    _Status_Type()
)
status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    status.setStatus("optional")
_SizeInMB_Type = Integer32
_SizeInMB_Object = MibTableColumn
sizeInMB = _SizeInMB_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 4),
    _SizeInMB_Type()
)
sizeInMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeInMB.setStatus("optional")


class _RaidLevel_Type(Integer32):
    """Custom type raidLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rAID0", 0),
          ("rAID1", 1),
          ("rAID3", 3),
          ("rAID5", 5))
    )


_RaidLevel_Type.__name__ = "Integer32"
_RaidLevel_Object = MibTableColumn
raidLevel = _RaidLevel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 5),
    _RaidLevel_Type()
)
raidLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raidLevel.setStatus("optional")


class _StripeSize_Type(Integer32):
    """Custom type stripeSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("eightKB", 8),
          ("fourKB", 4),
          ("oneKB", 1),
          ("oneTwentyEightKB", 128),
          ("sixteenKB", 16),
          ("sixtyFourKB", 64),
          ("thirtyTwoKB", 32),
          ("twoKB", 2))
    )


_StripeSize_Type.__name__ = "Integer32"
_StripeSize_Object = MibTableColumn
stripeSize = _StripeSize_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 6),
    _StripeSize_Type()
)
stripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stripeSize.setStatus("optional")


class _ReadPolicy_Type(Integer32):
    """Custom type readPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 2),
          ("normal", 0),
          ("readAhead", 1))
    )


_ReadPolicy_Type.__name__ = "Integer32"
_ReadPolicy_Object = MibTableColumn
readPolicy = _ReadPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 7),
    _ReadPolicy_Type()
)
readPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    readPolicy.setStatus("optional")


class _WritePolicy_Type(Integer32):
    """Custom type writePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("writeBack", 1),
          ("writeThru", 0))
    )


_WritePolicy_Type.__name__ = "Integer32"
_WritePolicy_Object = MibTableColumn
writePolicy = _WritePolicy_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 8),
    _WritePolicy_Type()
)
writePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    writePolicy.setStatus("optional")


class _CachePolicy_Type(Integer32):
    """Custom type cachePolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cachedIO", 0),
          ("directIO", 1))
    )


_CachePolicy_Type.__name__ = "Integer32"
_CachePolicy_Object = MibTableColumn
cachePolicy = _CachePolicy_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 9),
    _CachePolicy_Type()
)
cachePolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cachePolicy.setStatus("optional")


class _EnquiryString_Type(DisplayString):
    """Custom type enquiryString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_EnquiryString_Type.__name__ = "DisplayString"
_EnquiryString_Object = MibTableColumn
enquiryString = _EnquiryString_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 10),
    _EnquiryString_Type()
)
enquiryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enquiryString.setStatus("optional")


class _NumberOfSpans_Type(Integer32):
    """Custom type numberOfSpans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_NumberOfSpans_Type.__name__ = "Integer32"
_NumberOfSpans_Object = MibTableColumn
numberOfSpans = _NumberOfSpans_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 11),
    _NumberOfSpans_Type()
)
numberOfSpans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfSpans.setStatus("optional")


class _NumberOfStripes_Type(Integer32):
    """Custom type numberOfStripes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NumberOfStripes_Type.__name__ = "Integer32"
_NumberOfStripes_Object = MibTableColumn
numberOfStripes = _NumberOfStripes_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 12),
    _NumberOfStripes_Type()
)
numberOfStripes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfStripes.setStatus("optional")


class _CheckConsistencyOrInitializeProgress_Type(DisplayString):
    """Custom type checkConsistencyOrInitializeProgress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CheckConsistencyOrInitializeProgress_Type.__name__ = "DisplayString"
_CheckConsistencyOrInitializeProgress_Object = MibTableColumn
checkConsistencyOrInitializeProgress = _CheckConsistencyOrInitializeProgress_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 13),
    _CheckConsistencyOrInitializeProgress_Type()
)
checkConsistencyOrInitializeProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    checkConsistencyOrInitializeProgress.setStatus("optional")
_LdIOReadsPerSec_Type = Integer32
_LdIOReadsPerSec_Object = MibTableColumn
ldIOReadsPerSec = _LdIOReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 14),
    _LdIOReadsPerSec_Type()
)
ldIOReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldIOReadsPerSec.setStatus("optional")
_LdIOWritesPerSec_Type = Integer32
_LdIOWritesPerSec_Object = MibTableColumn
ldIOWritesPerSec = _LdIOWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 15),
    _LdIOWritesPerSec_Type()
)
ldIOWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldIOWritesPerSec.setStatus("optional")
_LdReadKBsPerSec_Type = Integer32
_LdReadKBsPerSec_Object = MibTableColumn
ldReadKBsPerSec = _LdReadKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 16),
    _LdReadKBsPerSec_Type()
)
ldReadKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldReadKBsPerSec.setStatus("optional")
_LdWriteKBsPerSec_Type = Integer32
_LdWriteKBsPerSec_Object = MibTableColumn
ldWriteKBsPerSec = _LdWriteKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 17),
    _LdWriteKBsPerSec_Type()
)
ldWriteKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWriteKBsPerSec.setStatus("optional")
_LdReadFailuresPerSec_Type = Integer32
_LdReadFailuresPerSec_Object = MibTableColumn
ldReadFailuresPerSec = _LdReadFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 18),
    _LdReadFailuresPerSec_Type()
)
ldReadFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldReadFailuresPerSec.setStatus("optional")
_LdWriteFailuresPerSec_Type = Integer32
_LdWriteFailuresPerSec_Object = MibTableColumn
ldWriteFailuresPerSec = _LdWriteFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 2, 1, 19),
    _LdWriteFailuresPerSec_Type()
)
ldWriteFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldWriteFailuresPerSec.setStatus("optional")
_PhysicaldriveTable_Object = MibTable
physicaldriveTable = _PhysicaldriveTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3)
)
if mibBuilder.loadTexts:
    physicaldriveTable.setStatus("optional")
_PhysicaldriveEntry_Object = MibTableRow
physicaldriveEntry = _PhysicaldriveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1)
)
physicaldriveEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "physAdapterNumber"),
    (0, "RAID-Adapter-MIB", "physChannel"),
    (0, "RAID-Adapter-MIB", "targetID"),
    (0, "RAID-Adapter-MIB", "lunNumber"),
)
if mibBuilder.loadTexts:
    physicaldriveEntry.setStatus("optional")


class _PhysAdapterNumber_Type(Integer32):
    """Custom type physAdapterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_PhysAdapterNumber_Type.__name__ = "Integer32"
_PhysAdapterNumber_Object = MibTableColumn
physAdapterNumber = _PhysAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 1),
    _PhysAdapterNumber_Type()
)
physAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physAdapterNumber.setStatus("optional")


class _PhysChannel_Type(Integer32):
    """Custom type physChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_PhysChannel_Type.__name__ = "Integer32"
_PhysChannel_Object = MibTableColumn
physChannel = _PhysChannel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 2),
    _PhysChannel_Type()
)
physChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physChannel.setStatus("optional")


class _TargetID_Type(Integer32):
    """Custom type targetID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_TargetID_Type.__name__ = "Integer32"
_TargetID_Object = MibTableColumn
targetID = _TargetID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 3),
    _TargetID_Type()
)
targetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    targetID.setStatus("optional")


class _State_Type(Integer32):
    """Custom type state based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              20)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("hotSpare", 6),
          ("nonDisk", 20),
          ("online", 3),
          ("ready", 1),
          ("rebuild", 5))
    )


_State_Type.__name__ = "Integer32"
_State_Object = MibTableColumn
state = _State_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 4),
    _State_Type()
)
state.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    state.setStatus("optional")


class _ArrayPosition_Type(DisplayString):
    """Custom type arrayPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_ArrayPosition_Type.__name__ = "DisplayString"
_ArrayPosition_Object = MibTableColumn
arrayPosition = _ArrayPosition_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 5),
    _ArrayPosition_Type()
)
arrayPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayPosition.setStatus("optional")
_SizeMB_Type = Integer32
_SizeMB_Object = MibTableColumn
sizeMB = _SizeMB_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 6),
    _SizeMB_Type()
)
sizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sizeMB.setStatus("optional")


class _DeviceType_Type(Integer32):
    """Custom type deviceType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("asynchronousHigh", 11),
          ("asynchronousLow", 10),
          ("cDROM", 5),
          ("changer", 8),
          ("communication", 9),
          ("disk", 0),
          ("optical", 7),
          ("printer", 2),
          ("processor", 3),
          ("reservedLow", 12),
          ("scanner", 6),
          ("tape", 1),
          ("wORM", 4))
    )


_DeviceType_Type.__name__ = "Integer32"
_DeviceType_Object = MibTableColumn
deviceType = _DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 7),
    _DeviceType_Type()
)
deviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceType.setStatus("optional")


class _InquiryString_Type(DisplayString):
    """Custom type inquiryString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_InquiryString_Type.__name__ = "DisplayString"
_InquiryString_Object = MibTableColumn
inquiryString = _InquiryString_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 8),
    _InquiryString_Type()
)
inquiryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inquiryString.setStatus("optional")


class _ScsiLevel_Type(Integer32):
    """Custom type scsiLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sCSI1", 1),
          ("sCSI2", 2),
          ("sCSI3", 3),
          ("sCSI4", 4))
    )


_ScsiLevel_Type.__name__ = "Integer32"
_ScsiLevel_Object = MibTableColumn
scsiLevel = _ScsiLevel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 9),
    _ScsiLevel_Type()
)
scsiLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scsiLevel.setStatus("optional")
_MaximumQueueDepth_Type = Integer32
_MaximumQueueDepth_Object = MibTableColumn
maximumQueueDepth = _MaximumQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 10),
    _MaximumQueueDepth_Type()
)
maximumQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumQueueDepth.setStatus("optional")


class _RebuildProgress_Type(DisplayString):
    """Custom type rebuildProgress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_RebuildProgress_Type.__name__ = "DisplayString"
_RebuildProgress_Object = MibTableColumn
rebuildProgress = _RebuildProgress_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 11),
    _RebuildProgress_Type()
)
rebuildProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rebuildProgress.setStatus("optional")
_MediumErrors_Type = Integer32
_MediumErrors_Object = MibTableColumn
mediumErrors = _MediumErrors_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 12),
    _MediumErrors_Type()
)
mediumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediumErrors.setStatus("optional")


class _PhysSlotStatus_Type(Integer32):
    """Custom type physSlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PhysSlotStatus_Type.__name__ = "Integer32"
_PhysSlotStatus_Object = MibTableColumn
physSlotStatus = _PhysSlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 13),
    _PhysSlotStatus_Type()
)
physSlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physSlotStatus.setStatus("optional")


class _PhysSlotNumber_Type(Integer32):
    """Custom type physSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_PhysSlotNumber_Type.__name__ = "Integer32"
_PhysSlotNumber_Object = MibTableColumn
physSlotNumber = _PhysSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 14),
    _PhysSlotNumber_Type()
)
physSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physSlotNumber.setStatus("optional")
_OtherErrors_Type = Integer32
_OtherErrors_Object = MibTableColumn
otherErrors = _OtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 15),
    _OtherErrors_Type()
)
otherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otherErrors.setStatus("optional")


class _PhysTermination_Type(Integer32):
    """Custom type physTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              20)
        )
    )
    namedValues = NamedValues(
        *(("narrow", 1),
          ("notSupported", 20),
          ("wide", 0))
    )


_PhysTermination_Type.__name__ = "Integer32"
_PhysTermination_Object = MibTableColumn
physTermination = _PhysTermination_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 16),
    _PhysTermination_Type()
)
physTermination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physTermination.setStatus("optional")


class _PhysSpeed_Type(Integer32):
    """Custom type physSpeed based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("asynchronous", 1),
          ("eightyMB", 6),
          ("fiveMB", 2),
          ("fortyMB", 5),
          ("maximum", 0),
          ("notSupported", 20),
          ("oneHundredSixtyMB", 7),
          ("tenMB", 3),
          ("threeHundredTwentyMB", 8),
          ("twentyMB", 4))
    )


_PhysSpeed_Type.__name__ = "Integer32"
_PhysSpeed_Object = MibTableColumn
physSpeed = _PhysSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 17),
    _PhysSpeed_Type()
)
physSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    physSpeed.setStatus("optional")


class _LunNumber_Type(Integer32):
    """Custom type lunNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_LunNumber_Type.__name__ = "Integer32"
_LunNumber_Object = MibTableColumn
lunNumber = _LunNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 3, 1, 18),
    _LunNumber_Type()
)
lunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lunNumber.setStatus("optional")
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("optional")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1)
)
channelEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "chanAdapterNumber"),
    (0, "RAID-Adapter-MIB", "channel"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("optional")
_ChanAdapterNumber_Type = Integer32
_ChanAdapterNumber_Object = MibTableColumn
chanAdapterNumber = _ChanAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1, 1),
    _ChanAdapterNumber_Type()
)
chanAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanAdapterNumber.setStatus("optional")
_Channel_Type = Integer32
_Channel_Object = MibTableColumn
channel = _Channel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1, 2),
    _Channel_Type()
)
channel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channel.setStatus("optional")


class _Terminations_Type(Integer32):
    """Custom type terminations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("higher8Bits", 1),
          ("wideTerminations", 2))
    )


_Terminations_Type.__name__ = "Integer32"
_Terminations_Object = MibTableColumn
terminations = _Terminations_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1, 3),
    _Terminations_Type()
)
terminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    terminations.setStatus("optional")


class _ChannelStatus_Type(Integer32):
    """Custom type channelStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("quiet", 1))
    )


_ChannelStatus_Type.__name__ = "Integer32"
_ChannelStatus_Object = MibTableColumn
channelStatus = _ChannelStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1, 4),
    _ChannelStatus_Type()
)
channelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelStatus.setStatus("optional")


class _ChannelType_Type(Integer32):
    """Custom type channelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rAID", 1),
          ("sCSI", 0))
    )


_ChannelType_Type.__name__ = "Integer32"
_ChannelType_Object = MibTableColumn
channelType = _ChannelType_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 4, 1, 5),
    _ChannelType_Type()
)
channelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelType.setStatus("mandatory")
_FcDeviceTable_Object = MibTable
fcDeviceTable = _FcDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fcDeviceTable.setStatus("optional")
_FcDeviceEntry_Object = MibTableRow
fcDeviceEntry = _FcDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1)
)
fcDeviceEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "fcPhysAdapterNumber"),
    (0, "RAID-Adapter-MIB", "fcPhysChannel"),
    (0, "RAID-Adapter-MIB", "fcTargetId"),
)
if mibBuilder.loadTexts:
    fcDeviceEntry.setStatus("optional")


class _FcPhysAdapterNumber_Type(Integer32):
    """Custom type fcPhysAdapterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FcPhysAdapterNumber_Type.__name__ = "Integer32"
_FcPhysAdapterNumber_Object = MibTableColumn
fcPhysAdapterNumber = _FcPhysAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 1),
    _FcPhysAdapterNumber_Type()
)
fcPhysAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPhysAdapterNumber.setStatus("optional")


class _FcPhysChannel_Type(Integer32):
    """Custom type fcPhysChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FcPhysChannel_Type.__name__ = "Integer32"
_FcPhysChannel_Object = MibTableColumn
fcPhysChannel = _FcPhysChannel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 2),
    _FcPhysChannel_Type()
)
fcPhysChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcPhysChannel.setStatus("optional")


class _FcTargetId_Type(Integer32):
    """Custom type fcTargetId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FcTargetId_Type.__name__ = "Integer32"
_FcTargetId_Object = MibTableColumn
fcTargetId = _FcTargetId_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 3),
    _FcTargetId_Type()
)
fcTargetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcTargetId.setStatus("optional")


class _FcLoopID_0_Type(Integer32):
    """Custom type fcLoopID_0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inLoop0", 1),
          ("inLoop1", 2),
          ("notInTheLoop", 255))
    )


_FcLoopID_0_Type.__name__ = "Integer32"
_FcLoopID_0_Object = MibScalar
fcLoopID_0 = _FcLoopID_0_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 4),
    _FcLoopID_0_Type()
)
fcLoopID_0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLoopID_0.setStatus("optional")


class _FcLoopID_1_Type(Integer32):
    """Custom type fcLoopID_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("inLoop0", 1),
          ("inLoop1", 2),
          ("notInTheLoop", 255))
    )


_FcLoopID_1_Type.__name__ = "Integer32"
_FcLoopID_1_Object = MibScalar
fcLoopID_1 = _FcLoopID_1_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 5),
    _FcLoopID_1_Type()
)
fcLoopID_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLoopID_1.setStatus("optional")


class _FcWwn_Type(DisplayString):
    """Custom type fcWwn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FcWwn_Type.__name__ = "DisplayString"
_FcWwn_Object = MibTableColumn
fcWwn = _FcWwn_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 6),
    _FcWwn_Type()
)
fcWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcWwn.setStatus("optional")


class _FcState_Type(Integer32):
    """Custom type fcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              20)
        )
    )
    namedValues = NamedValues(
        *(("failed", 4),
          ("hotspare", 6),
          ("nonDisk", 20),
          ("online", 3),
          ("ready", 1),
          ("rebuild", 5))
    )


_FcState_Type.__name__ = "Integer32"
_FcState_Object = MibTableColumn
fcState = _FcState_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 7),
    _FcState_Type()
)
fcState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fcState.setStatus("optional")


class _FcArrayPosition_Type(DisplayString):
    """Custom type fcArrayPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_FcArrayPosition_Type.__name__ = "DisplayString"
_FcArrayPosition_Object = MibTableColumn
fcArrayPosition = _FcArrayPosition_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 8),
    _FcArrayPosition_Type()
)
fcArrayPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcArrayPosition.setStatus("optional")
_FcSizeMB_Type = Integer32
_FcSizeMB_Object = MibTableColumn
fcSizeMB = _FcSizeMB_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 9),
    _FcSizeMB_Type()
)
fcSizeMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcSizeMB.setStatus("optional")


class _FcInquiryString_Type(DisplayString):
    """Custom type fcInquiryString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(29, 29),
    )


_FcInquiryString_Type.__name__ = "DisplayString"
_FcInquiryString_Object = MibTableColumn
fcInquiryString = _FcInquiryString_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 10),
    _FcInquiryString_Type()
)
fcInquiryString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcInquiryString.setStatus("optional")


class _FcScsiLevel_Type(Integer32):
    """Custom type fcScsiLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("sCSI1", 1),
          ("sCSI2", 2),
          ("sCSI3", 3),
          ("sCSI4", 4))
    )


_FcScsiLevel_Type.__name__ = "Integer32"
_FcScsiLevel_Object = MibTableColumn
fcScsiLevel = _FcScsiLevel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 11),
    _FcScsiLevel_Type()
)
fcScsiLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcScsiLevel.setStatus("optional")


class _FcRebuildProgress_Type(DisplayString):
    """Custom type fcRebuildProgress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 25),
    )


_FcRebuildProgress_Type.__name__ = "DisplayString"
_FcRebuildProgress_Object = MibTableColumn
fcRebuildProgress = _FcRebuildProgress_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 12),
    _FcRebuildProgress_Type()
)
fcRebuildProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcRebuildProgress.setStatus("optional")
_FcMediumErrors_Type = Integer32
_FcMediumErrors_Object = MibTableColumn
fcMediumErrors = _FcMediumErrors_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 13),
    _FcMediumErrors_Type()
)
fcMediumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcMediumErrors.setStatus("optional")
_FcOtherErrors_Type = Integer32
_FcOtherErrors_Object = MibTableColumn
fcOtherErrors = _FcOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 5, 1, 14),
    _FcOtherErrors_Type()
)
fcOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcOtherErrors.setStatus("optional")
_FcChannelTable_Object = MibTable
fcChannelTable = _FcChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fcChannelTable.setStatus("optional")
_FcChannelEntry_Object = MibTableRow
fcChannelEntry = _FcChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1)
)
fcChannelEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "fcChanAdapterNumber"),
    (0, "RAID-Adapter-MIB", "fcChannel"),
)
if mibBuilder.loadTexts:
    fcChannelEntry.setStatus("optional")
_FcChanAdapterNumber_Type = Integer32
_FcChanAdapterNumber_Object = MibTableColumn
fcChanAdapterNumber = _FcChanAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 1),
    _FcChanAdapterNumber_Type()
)
fcChanAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcChanAdapterNumber.setStatus("optional")
_FcChannel_Type = Integer32
_FcChannel_Object = MibTableColumn
fcChannel = _FcChannel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 2),
    _FcChannel_Type()
)
fcChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcChannel.setStatus("optional")
_FcLoopNumber_Type = Integer32
_FcLoopNumber_Object = MibTableColumn
fcLoopNumber = _FcLoopNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 3),
    _FcLoopNumber_Type()
)
fcLoopNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLoopNumber.setStatus("optional")


class _FcLoopStatus_Type(Integer32):
    """Custom type fcLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("quiet", 1))
    )


_FcLoopStatus_Type.__name__ = "Integer32"
_FcLoopStatus_Object = MibTableColumn
fcLoopStatus = _FcLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 4),
    _FcLoopStatus_Type()
)
fcLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcLoopStatus.setStatus("optional")
_FcNumberofDevices_Type = Integer32
_FcNumberofDevices_Object = MibTableColumn
fcNumberofDevices = _FcNumberofDevices_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 5),
    _FcNumberofDevices_Type()
)
fcNumberofDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcNumberofDevices.setStatus("optional")
_FcProcessorType_Type = Integer32
_FcProcessorType_Object = MibTableColumn
fcProcessorType = _FcProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 6, 1, 6),
    _FcProcessorType_Type()
)
fcProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcProcessorType.setStatus("optional")
_IoReadsPerSec_Type = Integer32
_IoReadsPerSec_Object = MibScalar
ioReadsPerSec = _IoReadsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 9),
    _IoReadsPerSec_Type()
)
ioReadsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioReadsPerSec.setStatus("optional")
_IoWritesPerSec_Type = Integer32
_IoWritesPerSec_Object = MibScalar
ioWritesPerSec = _IoWritesPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 10),
    _IoWritesPerSec_Type()
)
ioWritesPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ioWritesPerSec.setStatus("optional")
_ReadKBsPerSec_Type = Integer32
_ReadKBsPerSec_Object = MibScalar
readKBsPerSec = _ReadKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 11),
    _ReadKBsPerSec_Type()
)
readKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readKBsPerSec.setStatus("optional")
_WriteKBsPerSec_Type = Integer32
_WriteKBsPerSec_Object = MibScalar
writeKBsPerSec = _WriteKBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 12),
    _WriteKBsPerSec_Type()
)
writeKBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeKBsPerSec.setStatus("optional")
_ReadFailuresPerSec_Type = Integer32
_ReadFailuresPerSec_Object = MibScalar
readFailuresPerSec = _ReadFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 13),
    _ReadFailuresPerSec_Type()
)
readFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readFailuresPerSec.setStatus("optional")
_WriteFailuresPerSec_Type = Integer32
_WriteFailuresPerSec_Object = MibScalar
writeFailuresPerSec = _WriteFailuresPerSec_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 14),
    _WriteFailuresPerSec_Type()
)
writeFailuresPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    writeFailuresPerSec.setStatus("optional")
_EnclConfigurationTable_Object = MibTable
enclConfigurationTable = _EnclConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15)
)
if mibBuilder.loadTexts:
    enclConfigurationTable.setStatus("optional")
_EnclConfigurationEntry_Object = MibTableRow
enclConfigurationEntry = _EnclConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1)
)
enclConfigurationEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "enclNumber"),
)
if mibBuilder.loadTexts:
    enclConfigurationEntry.setStatus("optional")


class _EnclAdapterNumber_Type(Integer32):
    """Custom type enclAdapterNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_EnclAdapterNumber_Type.__name__ = "Integer32"
_EnclAdapterNumber_Object = MibTableColumn
enclAdapterNumber = _EnclAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 1),
    _EnclAdapterNumber_Type()
)
enclAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclAdapterNumber.setStatus("optional")


class _EnclNumber_Type(Integer32):
    """Custom type enclNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EnclNumber_Type.__name__ = "Integer32"
_EnclNumber_Object = MibTableColumn
enclNumber = _EnclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 2),
    _EnclNumber_Type()
)
enclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumber.setStatus("optional")


class _EnclChannel_Type(Integer32):
    """Custom type enclChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EnclChannel_Type.__name__ = "Integer32"
_EnclChannel_Object = MibTableColumn
enclChannel = _EnclChannel_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 3),
    _EnclChannel_Type()
)
enclChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclChannel.setStatus("optional")


class _EnclNumDeviceSlots_Type(Integer32):
    """Custom type enclNumDeviceSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EnclNumDeviceSlots_Type.__name__ = "Integer32"
_EnclNumDeviceSlots_Object = MibTableColumn
enclNumDeviceSlots = _EnclNumDeviceSlots_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 4),
    _EnclNumDeviceSlots_Type()
)
enclNumDeviceSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumDeviceSlots.setStatus("optional")


class _EnclNumFans_Type(Integer32):
    """Custom type enclNumFans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EnclNumFans_Type.__name__ = "Integer32"
_EnclNumFans_Object = MibTableColumn
enclNumFans = _EnclNumFans_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 5),
    _EnclNumFans_Type()
)
enclNumFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumFans.setStatus("optional")


class _EnclNumTempSensors_Type(Integer32):
    """Custom type enclNumTempSensors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EnclNumTempSensors_Type.__name__ = "Integer32"
_EnclNumTempSensors_Object = MibTableColumn
enclNumTempSensors = _EnclNumTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 6),
    _EnclNumTempSensors_Type()
)
enclNumTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumTempSensors.setStatus("optional")


class _EnclNumPowerSupplies_Type(Integer32):
    """Custom type enclNumPowerSupplies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EnclNumPowerSupplies_Type.__name__ = "Integer32"
_EnclNumPowerSupplies_Object = MibTableColumn
enclNumPowerSupplies = _EnclNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 7),
    _EnclNumPowerSupplies_Type()
)
enclNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumPowerSupplies.setStatus("optional")


class _EnclDoorLockStatus_Type(Integer32):
    """Custom type enclDoorLockStatus based on Integer32"""
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
        *(("locked", 2),
          ("notInstalled", 0),
          ("other", 3),
          ("unlocked", 1))
    )


_EnclDoorLockStatus_Type.__name__ = "Integer32"
_EnclDoorLockStatus_Object = MibTableColumn
enclDoorLockStatus = _EnclDoorLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 8),
    _EnclDoorLockStatus_Type()
)
enclDoorLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclDoorLockStatus.setStatus("optional")


class _EnclAudibleAlarm_Type(Integer32):
    """Custom type enclAudibleAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("audibleAlarm", 1),
          ("noAudibleAlarm", 0),
          ("other", 2))
    )


_EnclAudibleAlarm_Type.__name__ = "Integer32"
_EnclAudibleAlarm_Object = MibTableColumn
enclAudibleAlarm = _EnclAudibleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 9),
    _EnclAudibleAlarm_Type()
)
enclAudibleAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclAudibleAlarm.setStatus("optional")


class _EnclAlarmStatus_Type(Integer32):
    """Custom type enclAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1),
          ("other", 2))
    )


_EnclAlarmStatus_Type.__name__ = "Integer32"
_EnclAlarmStatus_Object = MibTableColumn
enclAlarmStatus = _EnclAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 10),
    _EnclAlarmStatus_Type()
)
enclAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclAlarmStatus.setStatus("optional")


class _EnclTemperatureScale_Type(Integer32):
    """Custom type enclTemperatureScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 0))
    )


_EnclTemperatureScale_Type.__name__ = "Integer32"
_EnclTemperatureScale_Object = MibTableColumn
enclTemperatureScale = _EnclTemperatureScale_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 11),
    _EnclTemperatureScale_Type()
)
enclTemperatureScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTemperatureScale.setStatus("optional")


class _EnclTotalPowerOnMins_Type(Integer32):
    """Custom type enclTotalPowerOnMins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EnclTotalPowerOnMins_Type.__name__ = "Integer32"
_EnclTotalPowerOnMins_Object = MibTableColumn
enclTotalPowerOnMins = _EnclTotalPowerOnMins_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 12),
    _EnclTotalPowerOnMins_Type()
)
enclTotalPowerOnMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTotalPowerOnMins.setStatus("optional")


class _EnclTotalPowerOnCycles_Type(Integer32):
    """Custom type enclTotalPowerOnCycles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EnclTotalPowerOnCycles_Type.__name__ = "Integer32"
_EnclTotalPowerOnCycles_Object = MibTableColumn
enclTotalPowerOnCycles = _EnclTotalPowerOnCycles_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 15, 1, 13),
    _EnclTotalPowerOnCycles_Type()
)
enclTotalPowerOnCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTotalPowerOnCycles.setStatus("optional")
_EnclFanTable_Object = MibTable
enclFanTable = _EnclFanTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 16)
)
if mibBuilder.loadTexts:
    enclFanTable.setStatus("optional")
_EnclFanEntry_Object = MibTableRow
enclFanEntry = _EnclFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 16, 1)
)
enclFanEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "enclNumberFan"),
    (0, "RAID-Adapter-MIB", "enclFanIndex"),
)
if mibBuilder.loadTexts:
    enclFanEntry.setStatus("optional")


class _EnclNumberFan_Type(Integer32):
    """Custom type enclNumberFan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EnclNumberFan_Type.__name__ = "Integer32"
_EnclNumberFan_Object = MibTableColumn
enclNumberFan = _EnclNumberFan_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 16, 1, 1),
    _EnclNumberFan_Type()
)
enclNumberFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumberFan.setStatus("optional")


class _EnclFanIndex_Type(Integer32):
    """Custom type enclFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclFanIndex_Type.__name__ = "Integer32"
_EnclFanIndex_Object = MibTableColumn
enclFanIndex = _EnclFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 16, 1, 2),
    _EnclFanIndex_Type()
)
enclFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclFanIndex.setStatus("optional")


class _EnclFanStatus_Type(Integer32):
    """Custom type enclFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              128)
        )
    )
    namedValues = NamedValues(
        *(("malfunction", 1),
          ("notInstalled", 2),
          ("operational", 0),
          ("unknown", 128))
    )


_EnclFanStatus_Type.__name__ = "Integer32"
_EnclFanStatus_Object = MibTableColumn
enclFanStatus = _EnclFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 16, 1, 3),
    _EnclFanStatus_Type()
)
enclFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclFanStatus.setStatus("optional")
_EnclPowerSupplyTable_Object = MibTable
enclPowerSupplyTable = _EnclPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 17)
)
if mibBuilder.loadTexts:
    enclPowerSupplyTable.setStatus("optional")
_EnclPowerSupplyEntry_Object = MibTableRow
enclPowerSupplyEntry = _EnclPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 17, 1)
)
enclPowerSupplyEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "enclNumberPower"),
    (0, "RAID-Adapter-MIB", "enclPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    enclPowerSupplyEntry.setStatus("optional")


class _EnclNumberPower_Type(Integer32):
    """Custom type enclNumberPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EnclNumberPower_Type.__name__ = "Integer32"
_EnclNumberPower_Object = MibTableColumn
enclNumberPower = _EnclNumberPower_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 17, 1, 1),
    _EnclNumberPower_Type()
)
enclNumberPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumberPower.setStatus("optional")


class _EnclPowerSupplyIndex_Type(Integer32):
    """Custom type enclPowerSupplyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnclPowerSupplyIndex_Type.__name__ = "Integer32"
_EnclPowerSupplyIndex_Object = MibTableColumn
enclPowerSupplyIndex = _EnclPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 17, 1, 2),
    _EnclPowerSupplyIndex_Type()
)
enclPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSupplyIndex.setStatus("optional")


class _EnclPowerSupplyStatus_Type(Integer32):
    """Custom type enclPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              128)
        )
    )
    namedValues = NamedValues(
        *(("malfunctionOFF", 3),
          ("malfunctionON", 2),
          ("notPresent", 4),
          ("operationalOFF", 1),
          ("operationalON", 0),
          ("present", 5),
          ("unknown", 128))
    )


_EnclPowerSupplyStatus_Type.__name__ = "Integer32"
_EnclPowerSupplyStatus_Object = MibTableColumn
enclPowerSupplyStatus = _EnclPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 17, 1, 3),
    _EnclPowerSupplyStatus_Type()
)
enclPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclPowerSupplyStatus.setStatus("optional")
_EnclTempSensorsTable_Object = MibTable
enclTempSensorsTable = _EnclTempSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 18)
)
if mibBuilder.loadTexts:
    enclTempSensorsTable.setStatus("optional")
_EnclTempSensorsEntry_Object = MibTableRow
enclTempSensorsEntry = _EnclTempSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 18, 1)
)
enclTempSensorsEntry.setIndexNames(
    (0, "RAID-Adapter-MIB", "enclNumberTemp"),
    (0, "RAID-Adapter-MIB", "enclTempSensorIndex"),
)
if mibBuilder.loadTexts:
    enclTempSensorsEntry.setStatus("optional")


class _EnclNumberTemp_Type(Integer32):
    """Custom type enclNumberTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EnclNumberTemp_Type.__name__ = "Integer32"
_EnclNumberTemp_Object = MibTableColumn
enclNumberTemp = _EnclNumberTemp_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 18, 1, 1),
    _EnclNumberTemp_Type()
)
enclNumberTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclNumberTemp.setStatus("optional")


class _EnclTempSensorIndex_Type(Integer32):
    """Custom type enclTempSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_EnclTempSensorIndex_Type.__name__ = "Integer32"
_EnclTempSensorIndex_Object = MibTableColumn
enclTempSensorIndex = _EnclTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 18, 1, 2),
    _EnclTempSensorIndex_Type()
)
enclTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTempSensorIndex.setStatus("optional")


class _EnclTemperature_Type(Integer32):
    """Custom type enclTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 245),
    )


_EnclTemperature_Type.__name__ = "Integer32"
_EnclTemperature_Object = MibTableColumn
enclTemperature = _EnclTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 18, 1, 3),
    _EnclTemperature_Type()
)
enclTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enclTemperature.setStatus("optional")
_RaidTraps_ObjectIdentity = ObjectIdentity
raidTraps = _RaidTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200)
)
_RtAdapterNumber_Type = Integer32
_RtAdapterNumber_Object = MibScalar
rtAdapterNumber = _RtAdapterNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1001),
    _RtAdapterNumber_Type()
)
rtAdapterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtAdapterNumber.setStatus("optional")
_RtLogicalDriveNumber_Type = Integer32
_RtLogicalDriveNumber_Object = MibScalar
rtLogicalDriveNumber = _RtLogicalDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1002),
    _RtLogicalDriveNumber_Type()
)
rtLogicalDriveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtLogicalDriveNumber.setStatus("optional")
_RtChannelNumber_Type = Integer32
_RtChannelNumber_Object = MibScalar
rtChannelNumber = _RtChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1003),
    _RtChannelNumber_Type()
)
rtChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtChannelNumber.setStatus("optional")
_RtTargetID_Type = Integer32
_RtTargetID_Object = MibScalar
rtTargetID = _RtTargetID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1004),
    _RtTargetID_Type()
)
rtTargetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtTargetID.setStatus("optional")
_RtOldDriveState_Type = DisplayString
_RtOldDriveState_Object = MibScalar
rtOldDriveState = _RtOldDriveState_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1005),
    _RtOldDriveState_Type()
)
rtOldDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtOldDriveState.setStatus("optional")
_RtNewDriveState_Type = DisplayString
_RtNewDriveState_Object = MibScalar
rtNewDriveState = _RtNewDriveState_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1006),
    _RtNewDriveState_Type()
)
rtNewDriveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtNewDriveState.setStatus("optional")
_RtSenseKey_Type = Integer32
_RtSenseKey_Object = MibScalar
rtSenseKey = _RtSenseKey_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1007),
    _RtSenseKey_Type()
)
rtSenseKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtSenseKey.setStatus("optional")
_RtASC_Type = Integer32
_RtASC_Object = MibScalar
rtASC = _RtASC_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1008),
    _RtASC_Type()
)
rtASC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtASC.setStatus("optional")
_RtASCQ_Type = Integer32
_RtASCQ_Object = MibScalar
rtASCQ = _RtASCQ_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1009),
    _RtASCQ_Type()
)
rtASCQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtASCQ.setStatus("optional")
_RtDriveVendor_Type = DisplayString
_RtDriveVendor_Object = MibScalar
rtDriveVendor = _RtDriveVendor_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1010),
    _RtDriveVendor_Type()
)
rtDriveVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtDriveVendor.setStatus("optional")
_RtEnclNumber_Type = Integer32
_RtEnclNumber_Object = MibScalar
rtEnclNumber = _RtEnclNumber_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1011),
    _RtEnclNumber_Type()
)
rtEnclNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEnclNumber.setStatus("optional")
_RtEnclTempSensorIndex_Type = Integer32
_RtEnclTempSensorIndex_Object = MibScalar
rtEnclTempSensorIndex = _RtEnclTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1012),
    _RtEnclTempSensorIndex_Type()
)
rtEnclTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEnclTempSensorIndex.setStatus("optional")
_RtEnclTemperature_Type = Integer32
_RtEnclTemperature_Object = MibScalar
rtEnclTemperature = _RtEnclTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1013),
    _RtEnclTemperature_Type()
)
rtEnclTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEnclTemperature.setStatus("optional")
_RtEnclFanIndex_Type = Integer32
_RtEnclFanIndex_Object = MibScalar
rtEnclFanIndex = _RtEnclFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1014),
    _RtEnclFanIndex_Type()
)
rtEnclFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEnclFanIndex.setStatus("optional")
_RtEnclPowerSupplyIndex_Type = Integer32
_RtEnclPowerSupplyIndex_Object = MibScalar
rtEnclPowerSupplyIndex = _RtEnclPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1015),
    _RtEnclPowerSupplyIndex_Type()
)
rtEnclPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtEnclPowerSupplyIndex.setStatus("optional")
_RtWWN_Type = DisplayString
_RtWWN_Object = MibScalar
rtWWN = _RtWWN_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1016),
    _RtWWN_Type()
)
rtWWN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtWWN.setStatus("optional")
_RtOldLoopID_Type = Integer32
_RtOldLoopID_Object = MibScalar
rtOldLoopID = _RtOldLoopID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1017),
    _RtOldLoopID_Type()
)
rtOldLoopID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtOldLoopID.setStatus("optional")
_RtNewLoopID_Type = Integer32
_RtNewLoopID_Object = MibScalar
rtNewLoopID = _RtNewLoopID_Object(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 1018),
    _RtNewLoopID_Type()
)
rtNewLoopID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtNewLoopID.setStatus("optional")

# Managed Objects groups


# Notification objects

rtConfigUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9001)
)
rtConfigUpdated.setObjects(
    ("RAID-Adapter-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtConfigUpdated.setStatus(
        ""
    )

rtPhysicalDriveStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9002)
)
rtPhysicalDriveStateChange.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateChange.setStatus(
        ""
    )

rtLogicalDriveStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9003)
)
rtLogicalDriveStateChange.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateChange.setStatus(
        ""
    )

rtInitializeStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9004)
)
rtInitializeStarted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeStarted.setStatus(
        ""
    )

rtInitializeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9005)
)
rtInitializeCompleted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeCompleted.setStatus(
        ""
    )

rtInitializeAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9006)
)
rtInitializeAborted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeAborted.setStatus(
        ""
    )

rtInitializeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9007)
)
rtInitializeFailed.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtInitializeFailed.setStatus(
        ""
    )

rtCheckConsistencyStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9008)
)
rtCheckConsistencyStarted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyStarted.setStatus(
        ""
    )

rtCheckConsistencyCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9009)
)
rtCheckConsistencyCompleted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyCompleted.setStatus(
        ""
    )

rtCheckConsistencyAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9010)
)
rtCheckConsistencyAborted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyAborted.setStatus(
        ""
    )

rtConsistencyCorrected = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9011)
)
rtConsistencyCorrected.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtConsistencyCorrected.setStatus(
        ""
    )

rtCheckConsistencyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9012)
)
rtCheckConsistencyFailed.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtCheckConsistencyFailed.setStatus(
        ""
    )

rtReconstructionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9013)
)
rtReconstructionStarted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionStarted.setStatus(
        ""
    )

rtReconstructionCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9014)
)
rtReconstructionCompleted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionCompleted.setStatus(
        ""
    )

rtReconstructionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9015)
)
rtReconstructionFailed.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"))
)
if mibBuilder.loadTexts:
    rtReconstructionFailed.setStatus(
        ""
    )

rtPredictiveFailuresExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9016)
)
rtPredictiveFailuresExceeded.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtDriveVendor"),
        ("RAID-Adapter-MIB", "rtSenseKey"),
        ("RAID-Adapter-MIB", "rtASC"),
        ("RAID-Adapter-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtPredictiveFailuresExceeded.setStatus(
        ""
    )

rtPredictiveFailuresFalse = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9017)
)
rtPredictiveFailuresFalse.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtDriveVendor"),
        ("RAID-Adapter-MIB", "rtSenseKey"),
        ("RAID-Adapter-MIB", "rtASC"),
        ("RAID-Adapter-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtPredictiveFailuresFalse.setStatus(
        ""
    )

rtCheckConditionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9018)
)
rtCheckConditionStatus.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtSenseKey"),
        ("RAID-Adapter-MIB", "rtASC"),
        ("RAID-Adapter-MIB", "rtASCQ"))
)
if mibBuilder.loadTexts:
    rtCheckConditionStatus.setStatus(
        ""
    )

rtNewDriveInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9019)
)
rtNewDriveInserted.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"))
)
if mibBuilder.loadTexts:
    rtNewDriveInserted.setStatus(
        ""
    )

rtBatteryMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9020)
)
rtBatteryMissing.setObjects(
    ("RAID-Adapter-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryMissing.setStatus(
        ""
    )

rtBatteryVolatageLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9021)
)
rtBatteryVolatageLow.setObjects(
    ("RAID-Adapter-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryVolatageLow.setStatus(
        ""
    )

rtBatteryTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9022)
)
rtBatteryTemperatureHigh.setObjects(
    ("RAID-Adapter-MIB", "rtAdapterNumber")
)
if mibBuilder.loadTexts:
    rtBatteryTemperatureHigh.setStatus(
        ""
    )

rtPhysicalDriveStateReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9023)
)
rtPhysicalDriveStateReady.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateReady.setStatus(
        ""
    )

rtPhysicalDriveStateOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9024)
)
rtPhysicalDriveStateOnline.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateOnline.setStatus(
        ""
    )

rtPhysicalDriveStateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9025)
)
rtPhysicalDriveStateFailed.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateFailed.setStatus(
        ""
    )

rtPhysicalDriveStateRebuild = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9026)
)
rtPhysicalDriveStateRebuild.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateRebuild.setStatus(
        ""
    )

rtPhysicalDriveStateHotspare = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9027)
)
rtPhysicalDriveStateHotspare.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtTargetID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtPhysicalDriveStateHotspare.setStatus(
        ""
    )

rtLogicalDriveStateOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9028)
)
rtLogicalDriveStateOffline.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateOffline.setStatus(
        ""
    )

rtLogicalDriveStateDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9029)
)
rtLogicalDriveStateDegraded.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateDegraded.setStatus(
        ""
    )

rtLogicalDriveStateOptimal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9030)
)
rtLogicalDriveStateOptimal.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateOptimal.setStatus(
        ""
    )

rtLogicalDriveStateInitialize = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9031)
)
rtLogicalDriveStateInitialize.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateInitialize.setStatus(
        ""
    )

rtLogicalDriveStateChkConsist = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9032)
)
rtLogicalDriveStateChkConsist.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtLogicalDriveNumber"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtLogicalDriveStateChkConsist.setStatus(
        ""
    )

rtEnclTemperatureOutofRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9033)
)
rtEnclTemperatureOutofRange.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclTempSensorIndex"),
        ("RAID-Adapter-MIB", "rtEnclTemperature"))
)
if mibBuilder.loadTexts:
    rtEnclTemperatureOutofRange.setStatus(
        ""
    )

rtEnclTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9034)
)
rtEnclTemperatureNormal.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclTempSensorIndex"),
        ("RAID-Adapter-MIB", "rtEnclTemperature"))
)
if mibBuilder.loadTexts:
    rtEnclTemperatureNormal.setStatus(
        ""
    )

rtEnclFanMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9035)
)
rtEnclFanMalfunction.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclFanIndex"))
)
if mibBuilder.loadTexts:
    rtEnclFanMalfunction.setStatus(
        ""
    )

rtEnclFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9036)
)
rtEnclFanOk.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclFanIndex"))
)
if mibBuilder.loadTexts:
    rtEnclFanOk.setStatus(
        ""
    )

rtEnclPowerSupplyMalfunction = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9037)
)
rtEnclPowerSupplyMalfunction.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclPowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    rtEnclPowerSupplyMalfunction.setStatus(
        ""
    )

rtEnclPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9038)
)
rtEnclPowerSupplyOk.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtChannelNumber"),
        ("RAID-Adapter-MIB", "rtEnclNumber"),
        ("RAID-Adapter-MIB", "rtEnclPowerSupplyIndex"))
)
if mibBuilder.loadTexts:
    rtEnclPowerSupplyOk.setStatus(
        ""
    )

rtFCLooplStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 3582, 1, 1, 200, 0, 9040)
)
rtFCLooplStateChange.setObjects(
      *(("RAID-Adapter-MIB", "rtAdapterNumber"),
        ("RAID-Adapter-MIB", "rtOldLoopID"),
        ("RAID-Adapter-MIB", "rtOldDriveState"),
        ("RAID-Adapter-MIB", "rtNewDriveState"))
)
if mibBuilder.loadTexts:
    rtFCLooplStateChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAID-Adapter-MIB",
    **{"lsi": lsi,
       "megaRaid": megaRaid,
       "megaRaidMib": megaRaidMib,
       "adapterTable": adapterTable,
       "adapterEntry": adapterEntry,
       "adpAdapterNumber": adpAdapterNumber,
       "numLogicalDrives": numLogicalDrives,
       "firmwareVersion": firmwareVersion,
       "biosVersion": biosVersion,
       "dramSizeInMB": dramSizeInMB,
       "rebuildRateInPercent": rebuildRateInPercent,
       "flushInterval": flushInterval,
       "maxConcurrentCmds": maxConcurrentCmds,
       "spinupDelay": spinupDelay,
       "spinupCount": spinupCount,
       "adpIOReadsPerSec": adpIOReadsPerSec,
       "adpIOWritesPerSec": adpIOWritesPerSec,
       "adpReadKBsPerSec": adpReadKBsPerSec,
       "adpWriteKBsPerSec": adpWriteKBsPerSec,
       "adpReadFailuresPerSec": adpReadFailuresPerSec,
       "adpWriteFailuresPerSec": adpWriteFailuresPerSec,
       "scanChannels": scanChannels,
       "adpBasePort": adpBasePort,
       "numSCSIChannels": numSCSIChannels,
       "numFCLoops": numFCLoops,
       "subSystemID": subSystemID,
       "subSystemVendorID": subSystemVendorID,
       "productName": productName,
       "adpSpeed": adpSpeed,
       "logicaldriveTable": logicaldriveTable,
       "logicaldriveEntry": logicaldriveEntry,
       "ldAdapterNumber": ldAdapterNumber,
       "logicalDriveNumber": logicalDriveNumber,
       "status": status,
       "sizeInMB": sizeInMB,
       "raidLevel": raidLevel,
       "stripeSize": stripeSize,
       "readPolicy": readPolicy,
       "writePolicy": writePolicy,
       "cachePolicy": cachePolicy,
       "enquiryString": enquiryString,
       "numberOfSpans": numberOfSpans,
       "numberOfStripes": numberOfStripes,
       "checkConsistencyOrInitializeProgress": checkConsistencyOrInitializeProgress,
       "ldIOReadsPerSec": ldIOReadsPerSec,
       "ldIOWritesPerSec": ldIOWritesPerSec,
       "ldReadKBsPerSec": ldReadKBsPerSec,
       "ldWriteKBsPerSec": ldWriteKBsPerSec,
       "ldReadFailuresPerSec": ldReadFailuresPerSec,
       "ldWriteFailuresPerSec": ldWriteFailuresPerSec,
       "physicaldriveTable": physicaldriveTable,
       "physicaldriveEntry": physicaldriveEntry,
       "physAdapterNumber": physAdapterNumber,
       "physChannel": physChannel,
       "targetID": targetID,
       "state": state,
       "arrayPosition": arrayPosition,
       "sizeMB": sizeMB,
       "deviceType": deviceType,
       "inquiryString": inquiryString,
       "scsiLevel": scsiLevel,
       "maximumQueueDepth": maximumQueueDepth,
       "rebuildProgress": rebuildProgress,
       "mediumErrors": mediumErrors,
       "physSlotStatus": physSlotStatus,
       "physSlotNumber": physSlotNumber,
       "otherErrors": otherErrors,
       "physTermination": physTermination,
       "physSpeed": physSpeed,
       "lunNumber": lunNumber,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "chanAdapterNumber": chanAdapterNumber,
       "channel": channel,
       "terminations": terminations,
       "channelStatus": channelStatus,
       "channelType": channelType,
       "fcDeviceTable": fcDeviceTable,
       "fcDeviceEntry": fcDeviceEntry,
       "fcPhysAdapterNumber": fcPhysAdapterNumber,
       "fcPhysChannel": fcPhysChannel,
       "fcTargetId": fcTargetId,
       "fcLoopID-0": fcLoopID_0,
       "fcLoopID-1": fcLoopID_1,
       "fcWwn": fcWwn,
       "fcState": fcState,
       "fcArrayPosition": fcArrayPosition,
       "fcSizeMB": fcSizeMB,
       "fcInquiryString": fcInquiryString,
       "fcScsiLevel": fcScsiLevel,
       "fcRebuildProgress": fcRebuildProgress,
       "fcMediumErrors": fcMediumErrors,
       "fcOtherErrors": fcOtherErrors,
       "fcChannelTable": fcChannelTable,
       "fcChannelEntry": fcChannelEntry,
       "fcChanAdapterNumber": fcChanAdapterNumber,
       "fcChannel": fcChannel,
       "fcLoopNumber": fcLoopNumber,
       "fcLoopStatus": fcLoopStatus,
       "fcNumberofDevices": fcNumberofDevices,
       "fcProcessorType": fcProcessorType,
       "ioReadsPerSec": ioReadsPerSec,
       "ioWritesPerSec": ioWritesPerSec,
       "readKBsPerSec": readKBsPerSec,
       "writeKBsPerSec": writeKBsPerSec,
       "readFailuresPerSec": readFailuresPerSec,
       "writeFailuresPerSec": writeFailuresPerSec,
       "enclConfigurationTable": enclConfigurationTable,
       "enclConfigurationEntry": enclConfigurationEntry,
       "enclAdapterNumber": enclAdapterNumber,
       "enclNumber": enclNumber,
       "enclChannel": enclChannel,
       "enclNumDeviceSlots": enclNumDeviceSlots,
       "enclNumFans": enclNumFans,
       "enclNumTempSensors": enclNumTempSensors,
       "enclNumPowerSupplies": enclNumPowerSupplies,
       "enclDoorLockStatus": enclDoorLockStatus,
       "enclAudibleAlarm": enclAudibleAlarm,
       "enclAlarmStatus": enclAlarmStatus,
       "enclTemperatureScale": enclTemperatureScale,
       "enclTotalPowerOnMins": enclTotalPowerOnMins,
       "enclTotalPowerOnCycles": enclTotalPowerOnCycles,
       "enclFanTable": enclFanTable,
       "enclFanEntry": enclFanEntry,
       "enclNumberFan": enclNumberFan,
       "enclFanIndex": enclFanIndex,
       "enclFanStatus": enclFanStatus,
       "enclPowerSupplyTable": enclPowerSupplyTable,
       "enclPowerSupplyEntry": enclPowerSupplyEntry,
       "enclNumberPower": enclNumberPower,
       "enclPowerSupplyIndex": enclPowerSupplyIndex,
       "enclPowerSupplyStatus": enclPowerSupplyStatus,
       "enclTempSensorsTable": enclTempSensorsTable,
       "enclTempSensorsEntry": enclTempSensorsEntry,
       "enclNumberTemp": enclNumberTemp,
       "enclTempSensorIndex": enclTempSensorIndex,
       "enclTemperature": enclTemperature,
       "raidTraps": raidTraps,
       "rtConfigUpdated": rtConfigUpdated,
       "rtPhysicalDriveStateChange": rtPhysicalDriveStateChange,
       "rtLogicalDriveStateChange": rtLogicalDriveStateChange,
       "rtInitializeStarted": rtInitializeStarted,
       "rtInitializeCompleted": rtInitializeCompleted,
       "rtInitializeAborted": rtInitializeAborted,
       "rtInitializeFailed": rtInitializeFailed,
       "rtCheckConsistencyStarted": rtCheckConsistencyStarted,
       "rtCheckConsistencyCompleted": rtCheckConsistencyCompleted,
       "rtCheckConsistencyAborted": rtCheckConsistencyAborted,
       "rtConsistencyCorrected": rtConsistencyCorrected,
       "rtCheckConsistencyFailed": rtCheckConsistencyFailed,
       "rtReconstructionStarted": rtReconstructionStarted,
       "rtReconstructionCompleted": rtReconstructionCompleted,
       "rtReconstructionFailed": rtReconstructionFailed,
       "rtPredictiveFailuresExceeded": rtPredictiveFailuresExceeded,
       "rtPredictiveFailuresFalse": rtPredictiveFailuresFalse,
       "rtCheckConditionStatus": rtCheckConditionStatus,
       "rtNewDriveInserted": rtNewDriveInserted,
       "rtBatteryMissing": rtBatteryMissing,
       "rtBatteryVolatageLow": rtBatteryVolatageLow,
       "rtBatteryTemperatureHigh": rtBatteryTemperatureHigh,
       "rtPhysicalDriveStateReady": rtPhysicalDriveStateReady,
       "rtPhysicalDriveStateOnline": rtPhysicalDriveStateOnline,
       "rtPhysicalDriveStateFailed": rtPhysicalDriveStateFailed,
       "rtPhysicalDriveStateRebuild": rtPhysicalDriveStateRebuild,
       "rtPhysicalDriveStateHotspare": rtPhysicalDriveStateHotspare,
       "rtLogicalDriveStateOffline": rtLogicalDriveStateOffline,
       "rtLogicalDriveStateDegraded": rtLogicalDriveStateDegraded,
       "rtLogicalDriveStateOptimal": rtLogicalDriveStateOptimal,
       "rtLogicalDriveStateInitialize": rtLogicalDriveStateInitialize,
       "rtLogicalDriveStateChkConsist": rtLogicalDriveStateChkConsist,
       "rtEnclTemperatureOutofRange": rtEnclTemperatureOutofRange,
       "rtEnclTemperatureNormal": rtEnclTemperatureNormal,
       "rtEnclFanMalfunction": rtEnclFanMalfunction,
       "rtEnclFanOk": rtEnclFanOk,
       "rtEnclPowerSupplyMalfunction": rtEnclPowerSupplyMalfunction,
       "rtEnclPowerSupplyOk": rtEnclPowerSupplyOk,
       "rtFCLooplStateChange": rtFCLooplStateChange,
       "rtAdapterNumber": rtAdapterNumber,
       "rtLogicalDriveNumber": rtLogicalDriveNumber,
       "rtChannelNumber": rtChannelNumber,
       "rtTargetID": rtTargetID,
       "rtOldDriveState": rtOldDriveState,
       "rtNewDriveState": rtNewDriveState,
       "rtSenseKey": rtSenseKey,
       "rtASC": rtASC,
       "rtASCQ": rtASCQ,
       "rtDriveVendor": rtDriveVendor,
       "rtEnclNumber": rtEnclNumber,
       "rtEnclTempSensorIndex": rtEnclTempSensorIndex,
       "rtEnclTemperature": rtEnclTemperature,
       "rtEnclFanIndex": rtEnclFanIndex,
       "rtEnclPowerSupplyIndex": rtEnclPowerSupplyIndex,
       "rtWWN": rtWWN,
       "rtOldLoopID": rtOldLoopID,
       "rtNewLoopID": rtNewLoopID}
)
