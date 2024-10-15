# SNMP MIB module (CISCO-CDSTV-CS-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDSTV-CS-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:16 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalSec,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalSec")

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

ciscoCdstvCsStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743)
)
ciscoCdstvCsStatsMIB.setRevisions(
        ("2012-05-17 00:00",
         "2010-07-29 00:00",
         "2010-06-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoCdstvStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoCdstvStatsMIBNotifs = _CiscoCdstvStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 0)
)
_CiscoCdstvStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoCdstvStatsMIBObjects = _CiscoCdstvStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1)
)
_CiscoCdstvCacheStats_ObjectIdentity = ObjectIdentity
ciscoCdstvCacheStats = _CiscoCdstvCacheStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1)
)


class _CdstvCacheCapacity_Type(Unsigned32):
    """Custom type cdstvCacheCapacity based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdstvCacheCapacity_Type.__name__ = "Unsigned32"
_CdstvCacheCapacity_Object = MibScalar
cdstvCacheCapacity = _CdstvCacheCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 1),
    _CdstvCacheCapacity_Type()
)
cdstvCacheCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCacheCapacity.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCacheCapacity.setUnits("kilobytes")
_CdstvCacheLevel_Type = Gauge32
_CdstvCacheLevel_Object = MibScalar
cdstvCacheLevel = _CdstvCacheLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 2),
    _CdstvCacheLevel_Type()
)
cdstvCacheLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCacheLevel.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCacheLevel.setUnits("kilobytes")
_CdstvFillReceiveStreams_Type = Gauge32
_CdstvFillReceiveStreams_Object = MibScalar
cdstvFillReceiveStreams = _CdstvFillReceiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 3),
    _CdstvFillReceiveStreams_Type()
)
cdstvFillReceiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvFillReceiveStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvFillReceiveStreams.setUnits("stream count")
_CdstvFillStreamCommittedBW_Type = Gauge32
_CdstvFillStreamCommittedBW_Object = MibScalar
cdstvFillStreamCommittedBW = _CdstvFillStreamCommittedBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 4),
    _CdstvFillStreamCommittedBW_Type()
)
cdstvFillStreamCommittedBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvFillStreamCommittedBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvFillStreamCommittedBW.setUnits("kilobits")
_CdstvFillStreamActualBW_Type = Gauge32
_CdstvFillStreamActualBW_Object = MibScalar
cdstvFillStreamActualBW = _CdstvFillStreamActualBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 5),
    _CdstvFillStreamActualBW_Type()
)
cdstvFillStreamActualBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvFillStreamActualBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvFillStreamActualBW.setUnits("kilobits")
_CdstvDiskReadStreams_Type = Gauge32
_CdstvDiskReadStreams_Object = MibScalar
cdstvDiskReadStreams = _CdstvDiskReadStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 6),
    _CdstvDiskReadStreams_Type()
)
cdstvDiskReadStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvDiskReadStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvDiskReadStreams.setUnits("stream count")
_CdstvDiskReadBW_Type = Gauge32
_CdstvDiskReadBW_Object = MibScalar
cdstvDiskReadBW = _CdstvDiskReadBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 7),
    _CdstvDiskReadBW_Type()
)
cdstvDiskReadBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvDiskReadBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvDiskReadBW.setUnits("kilobits")
_CdstvCCPInfromVaultStreams_Type = Gauge32
_CdstvCCPInfromVaultStreams_Object = MibScalar
cdstvCCPInfromVaultStreams = _CdstvCCPInfromVaultStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 8),
    _CdstvCCPInfromVaultStreams_Type()
)
cdstvCCPInfromVaultStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInfromVaultStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInfromVaultStreams.setUnits("stream count")
_CdstvCCPInFromVaultStreamBW_Type = Gauge32
_CdstvCCPInFromVaultStreamBW_Object = MibScalar
cdstvCCPInFromVaultStreamBW = _CdstvCCPInFromVaultStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 9),
    _CdstvCCPInFromVaultStreamBW_Type()
)
cdstvCCPInFromVaultStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInFromVaultStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInFromVaultStreamBW.setUnits("kilobits")
_CdstvCCPInFromCacheStreams_Type = Gauge32
_CdstvCCPInFromCacheStreams_Object = MibScalar
cdstvCCPInFromCacheStreams = _CdstvCCPInFromCacheStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 10),
    _CdstvCCPInFromCacheStreams_Type()
)
cdstvCCPInFromCacheStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInFromCacheStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInFromCacheStreams.setUnits("stream count")
_CdstvCCPInFromCacheStreamBW_Type = Gauge32
_CdstvCCPInFromCacheStreamBW_Object = MibScalar
cdstvCCPInFromCacheStreamBW = _CdstvCCPInFromCacheStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 11),
    _CdstvCCPInFromCacheStreamBW_Type()
)
cdstvCCPInFromCacheStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInFromCacheStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInFromCacheStreamBW.setUnits("kilobits")
_CdstvCCPInFromStreamerStreamCount_Type = Gauge32
_CdstvCCPInFromStreamerStreamCount_Object = MibScalar
cdstvCCPInFromStreamerStreamCount = _CdstvCCPInFromStreamerStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 12),
    _CdstvCCPInFromStreamerStreamCount_Type()
)
cdstvCCPInFromStreamerStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInFromStreamerStreamCount.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInFromStreamerStreamCount.setUnits("stream count")


class _CdstvCCPInFromStreamerStreamBW_Type(Unsigned32):
    """Custom type cdstvCCPInFromStreamerStreamBW based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CdstvCCPInFromStreamerStreamBW_Type.__name__ = "Unsigned32"
_CdstvCCPInFromStreamerStreamBW_Object = MibScalar
cdstvCCPInFromStreamerStreamBW = _CdstvCCPInFromStreamerStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 13),
    _CdstvCCPInFromStreamerStreamBW_Type()
)
cdstvCCPInFromStreamerStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPInFromStreamerStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPInFromStreamerStreamBW.setUnits("kilobits")
_CdstvHTTPInStreams_Type = Gauge32
_CdstvHTTPInStreams_Object = MibScalar
cdstvHTTPInStreams = _CdstvHTTPInStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 14),
    _CdstvHTTPInStreams_Type()
)
cdstvHTTPInStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvHTTPInStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvHTTPInStreams.setUnits("stream count")
_CdstvHTTPInStreamBW_Type = Gauge32
_CdstvHTTPInStreamBW_Object = MibScalar
cdstvHTTPInStreamBW = _CdstvHTTPInStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 15),
    _CdstvHTTPInStreamBW_Type()
)
cdstvHTTPInStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvHTTPInStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvHTTPInStreamBW.setUnits("kilobits")
_CdstvActiveIngestStreams_Type = Gauge32
_CdstvActiveIngestStreams_Object = MibScalar
cdstvActiveIngestStreams = _CdstvActiveIngestStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 16),
    _CdstvActiveIngestStreams_Type()
)
cdstvActiveIngestStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveIngestStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveIngestStreams.setUnits("stream count")
_CdstvActiveIngestStreamBW_Type = Gauge32
_CdstvActiveIngestStreamBW_Object = MibScalar
cdstvActiveIngestStreamBW = _CdstvActiveIngestStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 1, 17),
    _CdstvActiveIngestStreamBW_Type()
)
cdstvActiveIngestStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveIngestStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveIngestStreamBW.setUnits("kilobits")
_CiscoCdstvStreamStats_ObjectIdentity = ObjectIdentity
ciscoCdstvStreamStats = _CiscoCdstvStreamStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2)
)
_CdstvActiveStreams_Type = Gauge32
_CdstvActiveStreams_Object = MibScalar
cdstvActiveStreams = _CdstvActiveStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 1),
    _CdstvActiveStreams_Type()
)
cdstvActiveStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveStreams.setUnits("stream count")
_CdstvActiveStreamBW_Type = Gauge32
_CdstvActiveStreamBW_Object = MibScalar
cdstvActiveStreamBW = _CdstvActiveStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 2),
    _CdstvActiveStreamBW_Type()
)
cdstvActiveStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveStreamBW.setUnits("kilobits")
_CdstvUniqueStreams_Type = Gauge32
_CdstvUniqueStreams_Object = MibScalar
cdstvUniqueStreams = _CdstvUniqueStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 3),
    _CdstvUniqueStreams_Type()
)
cdstvUniqueStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvUniqueStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvUniqueStreams.setUnits("stream count")
_CdstvUniqueStreamBW_Type = Gauge32
_CdstvUniqueStreamBW_Object = MibScalar
cdstvUniqueStreamBW = _CdstvUniqueStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 4),
    _CdstvUniqueStreamBW_Type()
)
cdstvUniqueStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvUniqueStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvUniqueStreamBW.setUnits("kilobits")
_CdstvCCPOutStreams_Type = Gauge32
_CdstvCCPOutStreams_Object = MibScalar
cdstvCCPOutStreams = _CdstvCCPOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 5),
    _CdstvCCPOutStreams_Type()
)
cdstvCCPOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPOutStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPOutStreams.setUnits("stream count")
_CdstvCCPOutStreamBW_Type = Gauge32
_CdstvCCPOutStreamBW_Object = MibScalar
cdstvCCPOutStreamBW = _CdstvCCPOutStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 6),
    _CdstvCCPOutStreamBW_Type()
)
cdstvCCPOutStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvCCPOutStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvCCPOutStreamBW.setUnits("kilobits")
_CdstvHTTPOutStreams_Type = Gauge32
_CdstvHTTPOutStreams_Object = MibScalar
cdstvHTTPOutStreams = _CdstvHTTPOutStreams_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 7),
    _CdstvHTTPOutStreams_Type()
)
cdstvHTTPOutStreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvHTTPOutStreams.setStatus("current")
if mibBuilder.loadTexts:
    cdstvHTTPOutStreams.setUnits("stream count")
_CdstvHTTPOutStreamBW_Type = Gauge32
_CdstvHTTPOutStreamBW_Object = MibScalar
cdstvHTTPOutStreamBW = _CdstvHTTPOutStreamBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 8),
    _CdstvHTTPOutStreamBW_Type()
)
cdstvHTTPOutStreamBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvHTTPOutStreamBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvHTTPOutStreamBW.setUnits("kilobits")
_CdstvSessionSetupSuccess_Type = Counter32
_CdstvSessionSetupSuccess_Object = MibScalar
cdstvSessionSetupSuccess = _CdstvSessionSetupSuccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 9),
    _CdstvSessionSetupSuccess_Type()
)
cdstvSessionSetupSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvSessionSetupSuccess.setStatus("current")
_CdstvSessionSetupFailures_Type = Counter32
_CdstvSessionSetupFailures_Object = MibScalar
cdstvSessionSetupFailures = _CdstvSessionSetupFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 10),
    _CdstvSessionSetupFailures_Type()
)
cdstvSessionSetupFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvSessionSetupFailures.setStatus("current")
_CdstvSecondsSinceReference_Type = TimeIntervalSec
_CdstvSecondsSinceReference_Object = MibScalar
cdstvSecondsSinceReference = _CdstvSecondsSinceReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 11),
    _CdstvSecondsSinceReference_Type()
)
cdstvSecondsSinceReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvSecondsSinceReference.setStatus("current")
_CdstvStreamControlMessageQueueMax_Type = Unsigned32
_CdstvStreamControlMessageQueueMax_Object = MibScalar
cdstvStreamControlMessageQueueMax = _CdstvStreamControlMessageQueueMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 12),
    _CdstvStreamControlMessageQueueMax_Type()
)
cdstvStreamControlMessageQueueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvStreamControlMessageQueueMax.setStatus("current")
if mibBuilder.loadTexts:
    cdstvStreamControlMessageQueueMax.setUnits("elements")
_CdstvStreamControlMessageQueueSize_Type = Unsigned32
_CdstvStreamControlMessageQueueSize_Object = MibScalar
cdstvStreamControlMessageQueueSize = _CdstvStreamControlMessageQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 13),
    _CdstvStreamControlMessageQueueSize_Type()
)
cdstvStreamControlMessageQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvStreamControlMessageQueueSize.setStatus("current")
if mibBuilder.loadTexts:
    cdstvStreamControlMessageQueueSize.setUnits("elements")
_CdstvSkippedPlaylistElements_Type = Unsigned32
_CdstvSkippedPlaylistElements_Object = MibScalar
cdstvSkippedPlaylistElements = _CdstvSkippedPlaylistElements_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 14),
    _CdstvSkippedPlaylistElements_Type()
)
cdstvSkippedPlaylistElements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvSkippedPlaylistElements.setStatus("current")
if mibBuilder.loadTexts:
    cdstvSkippedPlaylistElements.setUnits("elements")
_CdstvStatsByContentTypeTable_Object = MibTable
cdstvStatsByContentTypeTable = _CdstvStatsByContentTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15)
)
if mibBuilder.loadTexts:
    cdstvStatsByContentTypeTable.setStatus("current")
_CdstvStatsByContentTypeEntry_Object = MibTableRow
cdstvStatsByContentTypeEntry = _CdstvStatsByContentTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1)
)
cdstvStatsByContentTypeEntry.setIndexNames(
    (0, "CISCO-CDSTV-CS-STATS-MIB", "cdstvContentType"),
)
if mibBuilder.loadTexts:
    cdstvStatsByContentTypeEntry.setStatus("current")


class _CdstvContentType_Type(Integer32):
    """Custom type cdstvContentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("legacyVod", 1),
          ("ndvrCommonCopy", 3),
          ("ndvrUniqueCopy", 2))
    )


_CdstvContentType_Type.__name__ = "Integer32"
_CdstvContentType_Object = MibTableColumn
cdstvContentType = _CdstvContentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 1),
    _CdstvContentType_Type()
)
cdstvContentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cdstvContentType.setStatus("current")
_CdstvActiveEgressCount_Type = Gauge32
_CdstvActiveEgressCount_Object = MibTableColumn
cdstvActiveEgressCount = _CdstvActiveEgressCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 2),
    _CdstvActiveEgressCount_Type()
)
cdstvActiveEgressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveEgressCount.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveEgressCount.setUnits("stream count")
_CdstvActiveEgressBW_Type = Gauge32
_CdstvActiveEgressBW_Object = MibTableColumn
cdstvActiveEgressBW = _CdstvActiveEgressBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 3),
    _CdstvActiveEgressBW_Type()
)
cdstvActiveEgressBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveEgressBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveEgressBW.setUnits("kilobits")
_CdstvActiveIngressCount_Type = Gauge32
_CdstvActiveIngressCount_Object = MibTableColumn
cdstvActiveIngressCount = _CdstvActiveIngressCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 4),
    _CdstvActiveIngressCount_Type()
)
cdstvActiveIngressCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveIngressCount.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveIngressCount.setUnits("fill count")
_CdstvActiveIngressBW_Type = Gauge32
_CdstvActiveIngressBW_Object = MibTableColumn
cdstvActiveIngressBW = _CdstvActiveIngressBW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 1, 2, 15, 1, 5),
    _CdstvActiveIngressBW_Type()
)
cdstvActiveIngressBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdstvActiveIngressBW.setStatus("current")
if mibBuilder.loadTexts:
    cdstvActiveIngressBW.setUnits("kilobits")
_CiscoCdstvStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoCdstvStatsMIBConform = _CiscoCdstvStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2)
)
_CiscoCdstvStatsMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoCdstvStatsMIBCompliances = _CiscoCdstvStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1)
)
_CiscoCdstvStatsMIBGroups_ObjectIdentity = ObjectIdentity
ciscoCdstvStatsMIBGroups = _CiscoCdstvStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2)
)

# Managed Objects groups

ciscoCdstvStatsMIBCacheObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 1)
)
ciscoCdstvStatsMIBCacheObjectGroup.setObjects(
      *(("CISCO-CDSTV-CS-STATS-MIB", "cdstvCacheCapacity"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCacheLevel"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillReceiveStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillStreamCommittedBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvFillStreamActualBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvDiskReadStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvDiskReadBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInfromVaultStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromVaultStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromCacheStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromCacheStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromStreamerStreamCount"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPInFromStreamerStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPInStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPInStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngestStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngestStreamBW"))
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBCacheObjectGroup.setStatus("current")

ciscoCdstvStatsMIBStreamObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 2)
)
ciscoCdstvStatsMIBStreamObjectGroup.setObjects(
      *(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"))
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBStreamObjectGroup.setStatus("deprecated")

ciscoCdstvStatsMIBStreamObjectGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 3)
)
ciscoCdstvStatsMIBStreamObjectGroup2.setObjects(
      *(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueMax"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueSize"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSkippedPlaylistElements"))
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBStreamObjectGroup2.setStatus("deprecated")

ciscoCdstvStatsMIBStreamObjectGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 2, 4)
)
ciscoCdstvStatsMIBStreamObjectGroup3.setObjects(
      *(("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvUniqueStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvCCPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreams"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvHTTPOutStreamBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupSuccess"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSessionSetupFailures"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSecondsSinceReference"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueMax"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvStreamControlMessageQueueSize"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvSkippedPlaylistElements"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveEgressCount"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveEgressBW"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngressCount"),
        ("CISCO-CDSTV-CS-STATS-MIB", "cdstvActiveIngressBW"))
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBStreamObjectGroup3.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoCdstvStatsMIBModuleCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBModuleCompliance.setStatus(
        "obsolete"
    )

ciscoCdstvStatsMIBModuleCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBModuleCompliance2.setStatus(
        "deprecated"
    )

ciscoCdstvStatsMIBModuleCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 743, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoCdstvStatsMIBModuleCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDSTV-CS-STATS-MIB",
    **{"ciscoCdstvCsStatsMIB": ciscoCdstvCsStatsMIB,
       "ciscoCdstvStatsMIBNotifs": ciscoCdstvStatsMIBNotifs,
       "ciscoCdstvStatsMIBObjects": ciscoCdstvStatsMIBObjects,
       "ciscoCdstvCacheStats": ciscoCdstvCacheStats,
       "cdstvCacheCapacity": cdstvCacheCapacity,
       "cdstvCacheLevel": cdstvCacheLevel,
       "cdstvFillReceiveStreams": cdstvFillReceiveStreams,
       "cdstvFillStreamCommittedBW": cdstvFillStreamCommittedBW,
       "cdstvFillStreamActualBW": cdstvFillStreamActualBW,
       "cdstvDiskReadStreams": cdstvDiskReadStreams,
       "cdstvDiskReadBW": cdstvDiskReadBW,
       "cdstvCCPInfromVaultStreams": cdstvCCPInfromVaultStreams,
       "cdstvCCPInFromVaultStreamBW": cdstvCCPInFromVaultStreamBW,
       "cdstvCCPInFromCacheStreams": cdstvCCPInFromCacheStreams,
       "cdstvCCPInFromCacheStreamBW": cdstvCCPInFromCacheStreamBW,
       "cdstvCCPInFromStreamerStreamCount": cdstvCCPInFromStreamerStreamCount,
       "cdstvCCPInFromStreamerStreamBW": cdstvCCPInFromStreamerStreamBW,
       "cdstvHTTPInStreams": cdstvHTTPInStreams,
       "cdstvHTTPInStreamBW": cdstvHTTPInStreamBW,
       "cdstvActiveIngestStreams": cdstvActiveIngestStreams,
       "cdstvActiveIngestStreamBW": cdstvActiveIngestStreamBW,
       "ciscoCdstvStreamStats": ciscoCdstvStreamStats,
       "cdstvActiveStreams": cdstvActiveStreams,
       "cdstvActiveStreamBW": cdstvActiveStreamBW,
       "cdstvUniqueStreams": cdstvUniqueStreams,
       "cdstvUniqueStreamBW": cdstvUniqueStreamBW,
       "cdstvCCPOutStreams": cdstvCCPOutStreams,
       "cdstvCCPOutStreamBW": cdstvCCPOutStreamBW,
       "cdstvHTTPOutStreams": cdstvHTTPOutStreams,
       "cdstvHTTPOutStreamBW": cdstvHTTPOutStreamBW,
       "cdstvSessionSetupSuccess": cdstvSessionSetupSuccess,
       "cdstvSessionSetupFailures": cdstvSessionSetupFailures,
       "cdstvSecondsSinceReference": cdstvSecondsSinceReference,
       "cdstvStreamControlMessageQueueMax": cdstvStreamControlMessageQueueMax,
       "cdstvStreamControlMessageQueueSize": cdstvStreamControlMessageQueueSize,
       "cdstvSkippedPlaylistElements": cdstvSkippedPlaylistElements,
       "cdstvStatsByContentTypeTable": cdstvStatsByContentTypeTable,
       "cdstvStatsByContentTypeEntry": cdstvStatsByContentTypeEntry,
       "cdstvContentType": cdstvContentType,
       "cdstvActiveEgressCount": cdstvActiveEgressCount,
       "cdstvActiveEgressBW": cdstvActiveEgressBW,
       "cdstvActiveIngressCount": cdstvActiveIngressCount,
       "cdstvActiveIngressBW": cdstvActiveIngressBW,
       "ciscoCdstvStatsMIBConform": ciscoCdstvStatsMIBConform,
       "ciscoCdstvStatsMIBCompliances": ciscoCdstvStatsMIBCompliances,
       "ciscoCdstvStatsMIBModuleCompliance": ciscoCdstvStatsMIBModuleCompliance,
       "ciscoCdstvStatsMIBModuleCompliance2": ciscoCdstvStatsMIBModuleCompliance2,
       "ciscoCdstvStatsMIBModuleCompliance3": ciscoCdstvStatsMIBModuleCompliance3,
       "ciscoCdstvStatsMIBGroups": ciscoCdstvStatsMIBGroups,
       "ciscoCdstvStatsMIBCacheObjectGroup": ciscoCdstvStatsMIBCacheObjectGroup,
       "ciscoCdstvStatsMIBStreamObjectGroup": ciscoCdstvStatsMIBStreamObjectGroup,
       "ciscoCdstvStatsMIBStreamObjectGroup2": ciscoCdstvStatsMIBStreamObjectGroup2,
       "ciscoCdstvStatsMIBStreamObjectGroup3": ciscoCdstvStatsMIBStreamObjectGroup3}
)
