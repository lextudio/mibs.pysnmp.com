# SNMP MIB module (H320ENTIRY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H320ENTIRY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:49:38 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

h320EntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 221, 2)
)
h320EntityMIB.setRevisions(
        ("1998-08-01 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LineRates(Integer32, TextualConvention):
    status = "current"


class VideoFormats(Integer32, TextualConvention):
    status = "current"


class AudioTypes(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Capability_ObjectIdentity = ObjectIdentity
capability = _Capability_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 1)
)
_CapsH320Table_Object = MibTable
capsH320Table = _CapsH320Table_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1)
)
if mibBuilder.loadTexts:
    capsH320Table.setStatus("current")
_CapsH320Entry_Object = MibTableRow
capsH320Entry = _CapsH320Entry_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1)
)
capsH320Entry.setIndexNames(
    (0, "H320ENTIRY-MIB", "terminalIndex"),
)
if mibBuilder.loadTexts:
    capsH320Entry.setStatus("current")


class _TerminalIndex_Type(Integer32):
    """Custom type terminalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TerminalIndex_Type.__name__ = "Integer32"
_TerminalIndex_Object = MibTableColumn
terminalIndex = _TerminalIndex_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 1),
    _TerminalIndex_Type()
)
terminalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    terminalIndex.setStatus("current")
_CapsH320EntityLineRate_Type = LineRates
_CapsH320EntityLineRate_Object = MibTableColumn
capsH320EntityLineRate = _CapsH320EntityLineRate_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 2),
    _CapsH320EntityLineRate_Type()
)
capsH320EntityLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityLineRate.setStatus("current")
_CapsH320EntityVideoFormats_Type = VideoFormats
_CapsH320EntityVideoFormats_Object = MibTableColumn
capsH320EntityVideoFormats = _CapsH320EntityVideoFormats_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 3),
    _CapsH320EntityVideoFormats_Type()
)
capsH320EntityVideoFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityVideoFormats.setStatus("current")
_CapsH320EntityMaxVideoRate_Type = Integer32
_CapsH320EntityMaxVideoRate_Object = MibTableColumn
capsH320EntityMaxVideoRate = _CapsH320EntityMaxVideoRate_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 4),
    _CapsH320EntityMaxVideoRate_Type()
)
capsH320EntityMaxVideoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityMaxVideoRate.setStatus("current")
_CapsH320EntityAudioTypes_Type = AudioTypes
_CapsH320EntityAudioTypes_Object = MibTableColumn
capsH320EntityAudioTypes = _CapsH320EntityAudioTypes_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 5),
    _CapsH320EntityAudioTypes_Type()
)
capsH320EntityAudioTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityAudioTypes.setStatus("current")
_CapsH320EntityDataCaps_Type = Integer32
_CapsH320EntityDataCaps_Object = MibTableColumn
capsH320EntityDataCaps = _CapsH320EntityDataCaps_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 6),
    _CapsH320EntityDataCaps_Type()
)
capsH320EntityDataCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityDataCaps.setStatus("current")
_CapsH320EntityEncryp_Type = Integer32
_CapsH320EntityEncryp_Object = MibTableColumn
capsH320EntityEncryp = _CapsH320EntityEncryp_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 7),
    _CapsH320EntityEncryp_Type()
)
capsH320EntityEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntityEncryp.setStatus("current")
_CapsH320EntryRDC_Type = Integer32
_CapsH320EntryRDC_Object = MibTableColumn
capsH320EntryRDC = _CapsH320EntryRDC_Object(
    (1, 3, 6, 1, 3, 221, 2, 1, 1, 1, 8),
    _CapsH320EntryRDC_Type()
)
capsH320EntryRDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    capsH320EntryRDC.setStatus("current")
_CallStatus_ObjectIdentity = ObjectIdentity
callStatus = _CallStatus_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 2)
)
_CallStatusTable_Object = MibTable
callStatusTable = _CallStatusTable_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1)
)
if mibBuilder.loadTexts:
    callStatusTable.setStatus("current")
_CallStatusEntry_Object = MibTableRow
callStatusEntry = _CallStatusEntry_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    callStatusEntry.setStatus("current")


class _H320CurrentCallStatus_Type(Integer32):
    """Custom type h320CurrentCallStatus based on Integer32"""
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
        *(("connected", 3),
          ("connecting", 2),
          ("disconnected", 5),
          ("disconnecting", 4),
          ("idle", 1))
    )


_H320CurrentCallStatus_Type.__name__ = "Integer32"
_H320CurrentCallStatus_Object = MibTableColumn
h320CurrentCallStatus = _H320CurrentCallStatus_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 2),
    _H320CurrentCallStatus_Type()
)
h320CurrentCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CurrentCallStatus.setStatus("current")


class _H320CallSiteName_Type(DisplayString):
    """Custom type h320CallSiteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_H320CallSiteName_Type.__name__ = "DisplayString"
_H320CallSiteName_Object = MibTableColumn
h320CallSiteName = _H320CallSiteName_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 3),
    _H320CallSiteName_Type()
)
h320CallSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallSiteName.setStatus("current")
_H320CallLineRate_Type = LineRates
_H320CallLineRate_Object = MibTableColumn
h320CallLineRate = _H320CallLineRate_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 4),
    _H320CallLineRate_Type()
)
h320CallLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallLineRate.setStatus("current")
_H320CallVideoInFormat_Type = VideoFormats
_H320CallVideoInFormat_Object = MibTableColumn
h320CallVideoInFormat = _H320CallVideoInFormat_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 5),
    _H320CallVideoInFormat_Type()
)
h320CallVideoInFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallVideoInFormat.setStatus("current")
_H320CallVideoOutFormat_Type = VideoFormats
_H320CallVideoOutFormat_Object = MibTableColumn
h320CallVideoOutFormat = _H320CallVideoOutFormat_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 6),
    _H320CallVideoOutFormat_Type()
)
h320CallVideoOutFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallVideoOutFormat.setStatus("current")
_H320CallAudioInFormat_Type = AudioTypes
_H320CallAudioInFormat_Object = MibTableColumn
h320CallAudioInFormat = _H320CallAudioInFormat_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 7),
    _H320CallAudioInFormat_Type()
)
h320CallAudioInFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallAudioInFormat.setStatus("current")
_H320CallAudioOutFormat_Type = AudioTypes
_H320CallAudioOutFormat_Object = MibTableColumn
h320CallAudioOutFormat = _H320CallAudioOutFormat_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 8),
    _H320CallAudioOutFormat_Type()
)
h320CallAudioOutFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallAudioOutFormat.setStatus("current")


class _H320CallData_Type(Integer32):
    """Custom type h320CallData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("t120", 1))
    )


_H320CallData_Type.__name__ = "Integer32"
_H320CallData_Object = MibTableColumn
h320CallData = _H320CallData_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 9),
    _H320CallData_Type()
)
h320CallData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallData.setStatus("current")


class _H320CallEncryp_Type(Integer32):
    """Custom type h320CallEncryp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h233", 1),
          ("other", 2))
    )


_H320CallEncryp_Type.__name__ = "Integer32"
_H320CallEncryp_Object = MibTableColumn
h320CallEncryp = _H320CallEncryp_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 10),
    _H320CallEncryp_Type()
)
h320CallEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallEncryp.setStatus("current")


class _H320CallRDC_Type(Integer32):
    """Custom type h320CallRDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h281FECC", 1),
          ("other", 2))
    )


_H320CallRDC_Type.__name__ = "Integer32"
_H320CallRDC_Object = MibTableColumn
h320CallRDC = _H320CallRDC_Object(
    (1, 3, 6, 1, 3, 221, 2, 2, 1, 1, 11),
    _H320CallRDC_Type()
)
h320CallRDC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h320CallRDC.setStatus("current")
_H221Stats_ObjectIdentity = ObjectIdentity
h221Stats = _H221Stats_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 3)
)
_H221StatsTable_Object = MibTable
h221StatsTable = _H221StatsTable_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1)
)
if mibBuilder.loadTexts:
    h221StatsTable.setStatus("current")
_H221StatsEntry_Object = MibTableRow
h221StatsEntry = _H221StatsEntry_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    h221StatsEntry.setStatus("current")
_H221InFrames_Type = Counter32
_H221InFrames_Object = MibTableColumn
h221InFrames = _H221InFrames_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 2),
    _H221InFrames_Type()
)
h221InFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221InFrames.setStatus("current")
_H221OutFrames_Type = Counter32
_H221OutFrames_Object = MibTableColumn
h221OutFrames = _H221OutFrames_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 3),
    _H221OutFrames_Type()
)
h221OutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221OutFrames.setStatus("current")
_H221InFrameErrs_Type = Counter32
_H221InFrameErrs_Object = MibTableColumn
h221InFrameErrs = _H221InFrameErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 4),
    _H221InFrameErrs_Type()
)
h221InFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221InFrameErrs.setStatus("current")
_H221FrameAlignmentErrs_Type = Counter32
_H221FrameAlignmentErrs_Object = MibTableColumn
h221FrameAlignmentErrs = _H221FrameAlignmentErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 5),
    _H221FrameAlignmentErrs_Type()
)
h221FrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221FrameAlignmentErrs.setStatus("current")
_H221MultiFrameAlignmentErrs_Type = Counter32
_H221MultiFrameAlignmentErrs_Object = MibTableColumn
h221MultiFrameAlignmentErrs = _H221MultiFrameAlignmentErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 6),
    _H221MultiFrameAlignmentErrs_Type()
)
h221MultiFrameAlignmentErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221MultiFrameAlignmentErrs.setStatus("current")
_H221ErrorPerformance_Type = Counter32
_H221ErrorPerformance_Object = MibTableColumn
h221ErrorPerformance = _H221ErrorPerformance_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 7),
    _H221ErrorPerformance_Type()
)
h221ErrorPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221ErrorPerformance.setStatus("current")
_H221BASErrs_Type = Counter32
_H221BASErrs_Object = MibTableColumn
h221BASErrs = _H221BASErrs_Object(
    (1, 3, 6, 1, 3, 221, 2, 3, 1, 1, 8),
    _H221BASErrs_Type()
)
h221BASErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h221BASErrs.setStatus("current")
_Events_ObjectIdentity = ObjectIdentity
events = _Events_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 4)
)
_H320EntityMIBConfs_ObjectIdentity = ObjectIdentity
h320EntityMIBConfs = _H320EntityMIBConfs_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 4)
)
_H320EntityMIBGroups_ObjectIdentity = ObjectIdentity
h320EntityMIBGroups = _H320EntityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 4, 1)
)
_H320EntityMIBCompl_ObjectIdentity = ObjectIdentity
h320EntityMIBCompl = _H320EntityMIBCompl_ObjectIdentity(
    (1, 3, 6, 1, 3, 221, 2, 4, 2)
)
capsH320Entry.registerAugmentions(
    ("H320ENTIRY-MIB",
     "callStatusEntry")
)
callStatusEntry.setIndexNames(*capsH320Entry.getIndexNames())
capsH320Entry.registerAugmentions(
    ("H320ENTIRY-MIB",
     "h221StatsEntry")
)
h221StatsEntry.setIndexNames(*capsH320Entry.getIndexNames())

# Managed Objects groups

h320CapsGroups = ObjectGroup(
    (1, 3, 6, 1, 3, 221, 2, 4, 1, 1)
)
h320CapsGroups.setObjects(
      *(("H320ENTIRY-MIB", "capsH320EntityLineRate"),
        ("H320ENTIRY-MIB", "capsH320EntityVideoFormats"),
        ("H320ENTIRY-MIB", "capsH320EntityMaxVideoRate"),
        ("H320ENTIRY-MIB", "capsH320EntityAudioTypes"),
        ("H320ENTIRY-MIB", "capsH320EntityDataCaps"),
        ("H320ENTIRY-MIB", "capsH320EntityEncryp"),
        ("H320ENTIRY-MIB", "capsH320EntryRDC"))
)
if mibBuilder.loadTexts:
    h320CapsGroups.setStatus("current")

h320CallStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 221, 2, 4, 1, 2)
)
h320CallStatusGroup.setObjects(
      *(("H320ENTIRY-MIB", "h320CurrentCallStatus"),
        ("H320ENTIRY-MIB", "h320CallSiteName"),
        ("H320ENTIRY-MIB", "h320CallLineRate"),
        ("H320ENTIRY-MIB", "h320CallVideoInFormat"),
        ("H320ENTIRY-MIB", "h320CallVideoOutFormat"),
        ("H320ENTIRY-MIB", "h320CallAudioInFormat"),
        ("H320ENTIRY-MIB", "h320CallAudioOutFormat"),
        ("H320ENTIRY-MIB", "h320CallData"),
        ("H320ENTIRY-MIB", "h320CallRDC"))
)
if mibBuilder.loadTexts:
    h320CallStatusGroup.setStatus("current")

h221StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 221, 2, 4, 1, 3)
)
h221StatsGroup.setObjects(
      *(("H320ENTIRY-MIB", "h221InFrames"),
        ("H320ENTIRY-MIB", "h221OutFrames"),
        ("H320ENTIRY-MIB", "h221InFrameErrs"),
        ("H320ENTIRY-MIB", "h221FrameAlignmentErrs"),
        ("H320ENTIRY-MIB", "h221MultiFrameAlignmentErrs"),
        ("H320ENTIRY-MIB", "h221ErrorPerformance"),
        ("H320ENTIRY-MIB", "h221BASErrs"))
)
if mibBuilder.loadTexts:
    h221StatsGroup.setStatus("current")


# Notification objects

h221TooManyErrors = NotificationType(
    (1, 3, 6, 1, 3, 221, 2, 4, 1)
)
h221TooManyErrors.setObjects(
    ("H320ENTIRY-MIB", "h221ErrorPerformance")
)
if mibBuilder.loadTexts:
    h221TooManyErrors.setStatus(
        "current"
    )

h320ConnectionEstablished = NotificationType(
    (1, 3, 6, 1, 3, 221, 2, 4, 2)
)
h320ConnectionEstablished.setObjects(
    ("H320ENTIRY-MIB", "h320CurrentCallStatus")
)
if mibBuilder.loadTexts:
    h320ConnectionEstablished.setStatus(
        "current"
    )

h320ConnectionTerminated = NotificationType(
    (1, 3, 6, 1, 3, 221, 2, 4, 3)
)
h320ConnectionTerminated.setObjects(
    ("H320ENTIRY-MIB", "h320CurrentCallStatus")
)
if mibBuilder.loadTexts:
    h320ConnectionTerminated.setStatus(
        "current"
    )


# Notifications groups

h320EventsGroup = NotificationGroup(
    (1, 3, 6, 1, 3, 221, 2, 4, 1, 4)
)
h320EventsGroup.setObjects(
      *(("H320ENTIRY-MIB", "h221TooManyErrors"),
        ("H320ENTIRY-MIB", "h320ConnectionEstablished"),
        ("H320ENTIRY-MIB", "h320ConnectionTerminated"))
)
if mibBuilder.loadTexts:
    h320EventsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

h221StatsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 221, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    h221StatsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H320ENTIRY-MIB",
    **{"LineRates": LineRates,
       "VideoFormats": VideoFormats,
       "AudioTypes": AudioTypes,
       "h320EntityMIB": h320EntityMIB,
       "capability": capability,
       "capsH320Table": capsH320Table,
       "capsH320Entry": capsH320Entry,
       "terminalIndex": terminalIndex,
       "capsH320EntityLineRate": capsH320EntityLineRate,
       "capsH320EntityVideoFormats": capsH320EntityVideoFormats,
       "capsH320EntityMaxVideoRate": capsH320EntityMaxVideoRate,
       "capsH320EntityAudioTypes": capsH320EntityAudioTypes,
       "capsH320EntityDataCaps": capsH320EntityDataCaps,
       "capsH320EntityEncryp": capsH320EntityEncryp,
       "capsH320EntryRDC": capsH320EntryRDC,
       "callStatus": callStatus,
       "callStatusTable": callStatusTable,
       "callStatusEntry": callStatusEntry,
       "h320CurrentCallStatus": h320CurrentCallStatus,
       "h320CallSiteName": h320CallSiteName,
       "h320CallLineRate": h320CallLineRate,
       "h320CallVideoInFormat": h320CallVideoInFormat,
       "h320CallVideoOutFormat": h320CallVideoOutFormat,
       "h320CallAudioInFormat": h320CallAudioInFormat,
       "h320CallAudioOutFormat": h320CallAudioOutFormat,
       "h320CallData": h320CallData,
       "h320CallEncryp": h320CallEncryp,
       "h320CallRDC": h320CallRDC,
       "h221Stats": h221Stats,
       "h221StatsTable": h221StatsTable,
       "h221StatsEntry": h221StatsEntry,
       "h221InFrames": h221InFrames,
       "h221OutFrames": h221OutFrames,
       "h221InFrameErrs": h221InFrameErrs,
       "h221FrameAlignmentErrs": h221FrameAlignmentErrs,
       "h221MultiFrameAlignmentErrs": h221MultiFrameAlignmentErrs,
       "h221ErrorPerformance": h221ErrorPerformance,
       "h221BASErrs": h221BASErrs,
       "events": events,
       "h320EntityMIBConfs": h320EntityMIBConfs,
       "h221TooManyErrors": h221TooManyErrors,
       "h320EntityMIBGroups": h320EntityMIBGroups,
       "h320CapsGroups": h320CapsGroups,
       "h320CallStatusGroup": h320CallStatusGroup,
       "h221StatsGroup": h221StatsGroup,
       "h320EventsGroup": h320EventsGroup,
       "h320ConnectionEstablished": h320ConnectionEstablished,
       "h320EntityMIBCompl": h320EntityMIBCompl,
       "h221StatsCompliance": h221StatsCompliance,
       "h320ConnectionTerminated": h320ConnectionTerminated}
)
