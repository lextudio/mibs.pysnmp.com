# SNMP MIB module (SONUS-ANNOUNCEMENT-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-ANNOUNCEMENT-RESOURCES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:51 2024
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

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusResourcesMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusResourcesMIBs")

(SonusBoolean,) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusBoolean")


# MODULE-IDENTITY

sonusAnnouncementResourcesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusAnnouncementResourcesMIBObjects_ObjectIdentity = ObjectIdentity
sonusAnnouncementResourcesMIBObjects = _SonusAnnouncementResourcesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1)
)
_SonusAnnSegStatTable_Object = MibTable
sonusAnnSegStatTable = _SonusAnnSegStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sonusAnnSegStatTable.setStatus("current")
_SonusAnnSegStatEntry_Object = MibTableRow
sonusAnnSegStatEntry = _SonusAnnSegStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1)
)
sonusAnnSegStatEntry.setIndexNames(
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"),
)
if mibBuilder.loadTexts:
    sonusAnnSegStatEntry.setStatus("current")
_SonusAnnSegStatSegId_Type = Integer32
_SonusAnnSegStatSegId_Object = MibTableColumn
sonusAnnSegStatSegId = _SonusAnnSegStatSegId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 1),
    _SonusAnnSegStatSegId_Type()
)
sonusAnnSegStatSegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegStatSegId.setStatus("current")
_SonusAnnSegStatLength_Type = Integer32
_SonusAnnSegStatLength_Object = MibTableColumn
sonusAnnSegStatLength = _SonusAnnSegStatLength_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 2),
    _SonusAnnSegStatLength_Type()
)
sonusAnnSegStatLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegStatLength.setStatus("current")
_SonusAnnSegStatVersion_Type = Integer32
_SonusAnnSegStatVersion_Object = MibTableColumn
sonusAnnSegStatVersion = _SonusAnnSegStatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 3),
    _SonusAnnSegStatVersion_Type()
)
sonusAnnSegStatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegStatVersion.setStatus("current")
_SonusAnnSegStatPreload_Type = SonusBoolean
_SonusAnnSegStatPreload_Object = MibTableColumn
sonusAnnSegStatPreload = _SonusAnnSegStatPreload_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 4),
    _SonusAnnSegStatPreload_Type()
)
sonusAnnSegStatPreload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegStatPreload.setStatus("current")


class _SonusAnnSegStatNfsPath_Type(DisplayString):
    """Custom type sonusAnnSegStatNfsPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SonusAnnSegStatNfsPath_Type.__name__ = "DisplayString"
_SonusAnnSegStatNfsPath_Object = MibTableColumn
sonusAnnSegStatNfsPath = _SonusAnnSegStatNfsPath_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 1, 1, 5),
    _SonusAnnSegStatNfsPath_Type()
)
sonusAnnSegStatNfsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegStatNfsPath.setStatus("current")
_SonusAnnSegMemStatTable_Object = MibTable
sonusAnnSegMemStatTable = _SonusAnnSegMemStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    sonusAnnSegMemStatTable.setStatus("current")
_SonusAnnSegMemStatEntry_Object = MibTableRow
sonusAnnSegMemStatEntry = _SonusAnnSegMemStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1)
)
sonusAnnSegMemStatEntry.setIndexNames(
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemStatShelfIndex"),
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusAnnSegMemStatEntry.setStatus("current")
_SonusAnnSegMemStatShelfIndex_Type = Integer32
_SonusAnnSegMemStatShelfIndex_Object = MibTableColumn
sonusAnnSegMemStatShelfIndex = _SonusAnnSegMemStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 1),
    _SonusAnnSegMemStatShelfIndex_Type()
)
sonusAnnSegMemStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemStatShelfIndex.setStatus("current")
_SonusAnnSegMemStatSlotIndex_Type = Integer32
_SonusAnnSegMemStatSlotIndex_Object = MibTableColumn
sonusAnnSegMemStatSlotIndex = _SonusAnnSegMemStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 2),
    _SonusAnnSegMemStatSlotIndex_Type()
)
sonusAnnSegMemStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemStatSlotIndex.setStatus("current")
_SonusAnnSegMemStatNumSegs_Type = Integer32
_SonusAnnSegMemStatNumSegs_Object = MibTableColumn
sonusAnnSegMemStatNumSegs = _SonusAnnSegMemStatNumSegs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 3),
    _SonusAnnSegMemStatNumSegs_Type()
)
sonusAnnSegMemStatNumSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemStatNumSegs.setStatus("current")
_SonusAnnSegMemStatTotalBytes_Type = Integer32
_SonusAnnSegMemStatTotalBytes_Object = MibTableColumn
sonusAnnSegMemStatTotalBytes = _SonusAnnSegMemStatTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 4),
    _SonusAnnSegMemStatTotalBytes_Type()
)
sonusAnnSegMemStatTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemStatTotalBytes.setStatus("current")
_SonusAnnSegMemStatUsedBytes_Type = Integer32
_SonusAnnSegMemStatUsedBytes_Object = MibTableColumn
sonusAnnSegMemStatUsedBytes = _SonusAnnSegMemStatUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 2, 1, 5),
    _SonusAnnSegMemStatUsedBytes_Type()
)
sonusAnnSegMemStatUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemStatUsedBytes.setStatus("current")
_SonusAnnSegPlayStatTable_Object = MibTable
sonusAnnSegPlayStatTable = _SonusAnnSegPlayStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatTable.setStatus("current")
_SonusAnnSegPlayStatEntry_Object = MibTableRow
sonusAnnSegPlayStatEntry = _SonusAnnSegPlayStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1)
)
sonusAnnSegPlayStatEntry.setIndexNames(
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatShelfIndex"),
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatSlotIndex"),
    (0, "SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegPlayStatSegId"),
)
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatEntry.setStatus("current")
_SonusAnnSegPlayStatShelfIndex_Type = Integer32
_SonusAnnSegPlayStatShelfIndex_Object = MibTableColumn
sonusAnnSegPlayStatShelfIndex = _SonusAnnSegPlayStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 1),
    _SonusAnnSegPlayStatShelfIndex_Type()
)
sonusAnnSegPlayStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatShelfIndex.setStatus("current")
_SonusAnnSegPlayStatSlotIndex_Type = Integer32
_SonusAnnSegPlayStatSlotIndex_Object = MibTableColumn
sonusAnnSegPlayStatSlotIndex = _SonusAnnSegPlayStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 2),
    _SonusAnnSegPlayStatSlotIndex_Type()
)
sonusAnnSegPlayStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatSlotIndex.setStatus("current")
_SonusAnnSegPlayStatSegId_Type = Integer32
_SonusAnnSegPlayStatSegId_Object = MibTableColumn
sonusAnnSegPlayStatSegId = _SonusAnnSegPlayStatSegId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 3),
    _SonusAnnSegPlayStatSegId_Type()
)
sonusAnnSegPlayStatSegId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatSegId.setStatus("current")
_SonusAnnSegPlayStatVersion_Type = Integer32
_SonusAnnSegPlayStatVersion_Object = MibTableColumn
sonusAnnSegPlayStatVersion = _SonusAnnSegPlayStatVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 4),
    _SonusAnnSegPlayStatVersion_Type()
)
sonusAnnSegPlayStatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatVersion.setStatus("current")


class _SonusAnnSegPlayStatState_Type(Integer32):
    """Custom type sonusAnnSegPlayStatState based on Integer32"""
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
        *(("loaded", 2),
          ("loading", 1),
          ("notPresent", 0),
          ("updatePending", 3))
    )


_SonusAnnSegPlayStatState_Type.__name__ = "Integer32"
_SonusAnnSegPlayStatState_Object = MibTableColumn
sonusAnnSegPlayStatState = _SonusAnnSegPlayStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 5),
    _SonusAnnSegPlayStatState_Type()
)
sonusAnnSegPlayStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatState.setStatus("current")
_SonusAnnSegPlayStatDelOnceFree_Type = SonusBoolean
_SonusAnnSegPlayStatDelOnceFree_Object = MibTableColumn
sonusAnnSegPlayStatDelOnceFree = _SonusAnnSegPlayStatDelOnceFree_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 6),
    _SonusAnnSegPlayStatDelOnceFree_Type()
)
sonusAnnSegPlayStatDelOnceFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatDelOnceFree.setStatus("current")
_SonusAnnSegPlayStatUseCount_Type = Integer32
_SonusAnnSegPlayStatUseCount_Object = MibTableColumn
sonusAnnSegPlayStatUseCount = _SonusAnnSegPlayStatUseCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 7),
    _SonusAnnSegPlayStatUseCount_Type()
)
sonusAnnSegPlayStatUseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatUseCount.setStatus("current")
_SonusAnnSegPlayStatTotalPlays_Type = Counter64
_SonusAnnSegPlayStatTotalPlays_Object = MibTableColumn
sonusAnnSegPlayStatTotalPlays = _SonusAnnSegPlayStatTotalPlays_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 1, 3, 1, 8),
    _SonusAnnSegPlayStatTotalPlays_Type()
)
sonusAnnSegPlayStatTotalPlays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegPlayStatTotalPlays.setStatus("current")
_SonusAnnouncementResourcesMIBNotifications_ObjectIdentity = ObjectIdentity
sonusAnnouncementResourcesMIBNotifications = _SonusAnnouncementResourcesMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2)
)
_SonusAnnouncementResourcesMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusAnnouncementResourcesMIBNotificationsPrefix = _SonusAnnouncementResourcesMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0)
)
_SonusAnnouncementResourcesMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusAnnouncementResourcesMIBNotificationsObjects = _SonusAnnouncementResourcesMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1)
)
_SonusAresUnavailCount_Type = Integer32
_SonusAresUnavailCount_Object = MibScalar
sonusAresUnavailCount = _SonusAresUnavailCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1, 1),
    _SonusAresUnavailCount_Type()
)
sonusAresUnavailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAresUnavailCount.setStatus("current")
_SonusAnnSegMemFullCount_Type = Integer32
_SonusAnnSegMemFullCount_Object = MibScalar
sonusAnnSegMemFullCount = _SonusAnnSegMemFullCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 1, 2),
    _SonusAnnSegMemFullCount_Type()
)
sonusAnnSegMemFullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusAnnSegMemFullCount.setStatus("current")

# Managed Objects groups


# Notification objects

sonusAnnouncementFileNotFoundNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 1)
)
sonusAnnouncementFileNotFoundNotification.setObjects(
      *(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementFileNotFoundNotification.setStatus(
        "current"
    )

sonusAnnouncementFileFoundNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 2)
)
sonusAnnouncementFileFoundNotification.setObjects(
      *(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"),
        ("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementFileFoundNotification.setStatus(
        "current"
    )

sonusAnnouncementFileInvalidNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 3)
)
sonusAnnouncementFileInvalidNotification.setObjects(
      *(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementFileInvalidNotification.setStatus(
        "current"
    )

sonusAnnouncementFileValidNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 4)
)
sonusAnnouncementFileValidNotification.setObjects(
      *(("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatNfsPath"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementFileValidNotification.setStatus(
        "current"
    )

sonusAnnouncementSegmentLoadFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 5)
)
sonusAnnouncementSegmentLoadFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatSegId"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatVersion"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegStatLength"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAnnSegMemFullCount"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementSegmentLoadFailureNotification.setStatus(
        "current"
    )

sonusAnnouncementResUnavailRisingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 6)
)
sonusAnnouncementResUnavailRisingThresholdNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementResUnavailRisingThresholdNotification.setStatus(
        "current"
    )

sonusAnnouncementResUnavailFallingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 2, 5, 2, 0, 7)
)
sonusAnnouncementResUnavailFallingThresholdNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-ANNOUNCEMENT-RESOURCES-MIB", "sonusAresUnavailCount"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusAnnouncementResUnavailFallingThresholdNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-ANNOUNCEMENT-RESOURCES-MIB",
    **{"sonusAnnouncementResourcesMIB": sonusAnnouncementResourcesMIB,
       "sonusAnnouncementResourcesMIBObjects": sonusAnnouncementResourcesMIBObjects,
       "sonusAnnSegStatTable": sonusAnnSegStatTable,
       "sonusAnnSegStatEntry": sonusAnnSegStatEntry,
       "sonusAnnSegStatSegId": sonusAnnSegStatSegId,
       "sonusAnnSegStatLength": sonusAnnSegStatLength,
       "sonusAnnSegStatVersion": sonusAnnSegStatVersion,
       "sonusAnnSegStatPreload": sonusAnnSegStatPreload,
       "sonusAnnSegStatNfsPath": sonusAnnSegStatNfsPath,
       "sonusAnnSegMemStatTable": sonusAnnSegMemStatTable,
       "sonusAnnSegMemStatEntry": sonusAnnSegMemStatEntry,
       "sonusAnnSegMemStatShelfIndex": sonusAnnSegMemStatShelfIndex,
       "sonusAnnSegMemStatSlotIndex": sonusAnnSegMemStatSlotIndex,
       "sonusAnnSegMemStatNumSegs": sonusAnnSegMemStatNumSegs,
       "sonusAnnSegMemStatTotalBytes": sonusAnnSegMemStatTotalBytes,
       "sonusAnnSegMemStatUsedBytes": sonusAnnSegMemStatUsedBytes,
       "sonusAnnSegPlayStatTable": sonusAnnSegPlayStatTable,
       "sonusAnnSegPlayStatEntry": sonusAnnSegPlayStatEntry,
       "sonusAnnSegPlayStatShelfIndex": sonusAnnSegPlayStatShelfIndex,
       "sonusAnnSegPlayStatSlotIndex": sonusAnnSegPlayStatSlotIndex,
       "sonusAnnSegPlayStatSegId": sonusAnnSegPlayStatSegId,
       "sonusAnnSegPlayStatVersion": sonusAnnSegPlayStatVersion,
       "sonusAnnSegPlayStatState": sonusAnnSegPlayStatState,
       "sonusAnnSegPlayStatDelOnceFree": sonusAnnSegPlayStatDelOnceFree,
       "sonusAnnSegPlayStatUseCount": sonusAnnSegPlayStatUseCount,
       "sonusAnnSegPlayStatTotalPlays": sonusAnnSegPlayStatTotalPlays,
       "sonusAnnouncementResourcesMIBNotifications": sonusAnnouncementResourcesMIBNotifications,
       "sonusAnnouncementResourcesMIBNotificationsPrefix": sonusAnnouncementResourcesMIBNotificationsPrefix,
       "sonusAnnouncementFileNotFoundNotification": sonusAnnouncementFileNotFoundNotification,
       "sonusAnnouncementFileFoundNotification": sonusAnnouncementFileFoundNotification,
       "sonusAnnouncementFileInvalidNotification": sonusAnnouncementFileInvalidNotification,
       "sonusAnnouncementFileValidNotification": sonusAnnouncementFileValidNotification,
       "sonusAnnouncementSegmentLoadFailureNotification": sonusAnnouncementSegmentLoadFailureNotification,
       "sonusAnnouncementResUnavailRisingThresholdNotification": sonusAnnouncementResUnavailRisingThresholdNotification,
       "sonusAnnouncementResUnavailFallingThresholdNotification": sonusAnnouncementResUnavailFallingThresholdNotification,
       "sonusAnnouncementResourcesMIBNotificationsObjects": sonusAnnouncementResourcesMIBNotificationsObjects,
       "sonusAresUnavailCount": sonusAresUnavailCount,
       "sonusAnnSegMemFullCount": sonusAnnSegMemFullCount}
)
