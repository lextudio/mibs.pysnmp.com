# SNMP MIB module (DATAFABRIC-MANAGER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DATAFABRIC-MANAGER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:17 2024
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

(netapp,) = mibBuilder.importSymbols(
    "NETWORK-APPLIANCE-MIB",
    "netapp")

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


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetappDataFabricManager_ObjectIdentity = ObjectIdentity
netappDataFabricManager = _NetappDataFabricManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 789, 3)
)
_DfmSerialNumber_Type = DisplayString
_DfmSerialNumber_Object = MibScalar
dfmSerialNumber = _DfmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 1),
    _DfmSerialNumber_Type()
)
dfmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmSerialNumber.setStatus("mandatory")
_DfmEventTable_Object = MibTable
dfmEventTable = _DfmEventTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11)
)
if mibBuilder.loadTexts:
    dfmEventTable.setStatus("mandatory")
_DfmEventEntry_Object = MibTableRow
dfmEventEntry = _DfmEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1)
)
dfmEventEntry.setIndexNames(
    (0, "DATAFABRIC-MANAGER-MIB", "dfmEventId"),
)
if mibBuilder.loadTexts:
    dfmEventEntry.setStatus("mandatory")
_DfmEventId_Type = Integer32
_DfmEventId_Object = MibTableColumn
dfmEventId = _DfmEventId_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 1),
    _DfmEventId_Type()
)
dfmEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventId.setStatus("mandatory")
_DfmEventSourceId_Type = Integer32
_DfmEventSourceId_Object = MibTableColumn
dfmEventSourceId = _DfmEventSourceId_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 2),
    _DfmEventSourceId_Type()
)
dfmEventSourceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventSourceId.setStatus("mandatory")


class _DfmEventSeverity_Type(Integer32):
    """Custom type dfmEventSeverity based on Integer32"""
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
        *(("critical", 5),
          ("emergency", 6),
          ("error", 4),
          ("information", 2),
          ("normal", 1),
          ("warning", 3))
    )


_DfmEventSeverity_Type.__name__ = "Integer32"
_DfmEventSeverity_Object = MibTableColumn
dfmEventSeverity = _DfmEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 3),
    _DfmEventSeverity_Type()
)
dfmEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventSeverity.setStatus("mandatory")
_DfmEventTimestamp_Type = Integer32
_DfmEventTimestamp_Object = MibTableColumn
dfmEventTimestamp = _DfmEventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 4),
    _DfmEventTimestamp_Type()
)
dfmEventTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventTimestamp.setStatus("mandatory")
_DfmEventName_Type = DisplayString
_DfmEventName_Object = MibTableColumn
dfmEventName = _DfmEventName_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 5),
    _DfmEventName_Type()
)
dfmEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventName.setStatus("mandatory")
_DfmEventMessage_Type = DisplayString
_DfmEventMessage_Object = MibTableColumn
dfmEventMessage = _DfmEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 6),
    _DfmEventMessage_Type()
)
dfmEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventMessage.setStatus("mandatory")
_DfmEventMessageDetails_Type = DisplayString
_DfmEventMessageDetails_Object = MibTableColumn
dfmEventMessageDetails = _DfmEventMessageDetails_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 7),
    _DfmEventMessageDetails_Type()
)
dfmEventMessageDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventMessageDetails.setStatus("mandatory")


class _DfmEventSourceTable_Type(Integer32):
    """Custom type dfmEventSourceTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("objects", 1),
          ("quotas", 2))
    )


_DfmEventSourceTable_Type.__name__ = "Integer32"
_DfmEventSourceTable_Object = MibTableColumn
dfmEventSourceTable = _DfmEventSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 8),
    _DfmEventSourceTable_Type()
)
dfmEventSourceTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventSourceTable.setStatus("mandatory")
_DfmEventSourceSerialNumber_Type = DisplayString
_DfmEventSourceSerialNumber_Object = MibTableColumn
dfmEventSourceSerialNumber = _DfmEventSourceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 9),
    _DfmEventSourceSerialNumber_Type()
)
dfmEventSourceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventSourceSerialNumber.setStatus("mandatory")
_DfmEventSourceProductId_Type = DisplayString
_DfmEventSourceProductId_Object = MibTableColumn
dfmEventSourceProductId = _DfmEventSourceProductId_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 11, 1, 10),
    _DfmEventSourceProductId_Type()
)
dfmEventSourceProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmEventSourceProductId.setStatus("mandatory")
_DfmObjectTable_Object = MibTable
dfmObjectTable = _DfmObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12)
)
if mibBuilder.loadTexts:
    dfmObjectTable.setStatus("mandatory")
_DfmObjectEntry_Object = MibTableRow
dfmObjectEntry = _DfmObjectEntry_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1)
)
dfmObjectEntry.setIndexNames(
    (0, "DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
)
if mibBuilder.loadTexts:
    dfmObjectEntry.setStatus("mandatory")
_DfmObjectId_Type = Integer32
_DfmObjectId_Object = MibTableColumn
dfmObjectId = _DfmObjectId_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 1),
    _DfmObjectId_Type()
)
dfmObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmObjectId.setStatus("mandatory")
_DfmObjectFullName_Type = DisplayString
_DfmObjectFullName_Object = MibTableColumn
dfmObjectFullName = _DfmObjectFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 2),
    _DfmObjectFullName_Type()
)
dfmObjectFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmObjectFullName.setStatus("mandatory")


class _DfmObjectType_Type(Integer32):
    """Custom type dfmObjectType based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("aggregate", 15),
          ("cmsJob", 14),
          ("config", 6),
          ("dataset", 19),
          ("directory", 12),
          ("disk", 30),
          ("dpPolicy", 22),
          ("dpSchedule", 23),
          ("dpThrottle", 24),
          ("fcSwitchPort", 11),
          ("group", 10),
          ("hbaPort", 13),
          ("host", 3),
          ("ifgrp", 33),
          ("interface", 16),
          ("lif", 34),
          ("lun", 9),
          ("mgmtStation", 2),
          ("network", 8),
          ("ossvDirectory", 25),
          ("port", 32),
          ("provPolicy", 28),
          ("qtree", 5),
          ("reportSchedule", 27),
          ("resourcePool", 21),
          ("schedule", 26),
          ("script", 17),
          ("scriptJob", 18),
          ("scriptSchedule", 31),
          ("storageService", 35),
          ("storageset", 20),
          ("unknown", 1),
          ("user", 7),
          ("vfilerTemplate", 29),
          ("volume", 4))
    )


_DfmObjectType_Type.__name__ = "Integer32"
_DfmObjectType_Object = MibTableColumn
dfmObjectType = _DfmObjectType_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 3),
    _DfmObjectType_Type()
)
dfmObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmObjectType.setStatus("mandatory")


class _DfmObjectStatus_Type(Integer32):
    """Custom type dfmObjectStatus based on Integer32"""
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
        *(("critical", 6),
          ("emergency", 7),
          ("error", 5),
          ("normal", 3),
          ("unknown", 1),
          ("unmanaged", 2),
          ("warning", 4))
    )


_DfmObjectStatus_Type.__name__ = "Integer32"
_DfmObjectStatus_Object = MibTableColumn
dfmObjectStatus = _DfmObjectStatus_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 4),
    _DfmObjectStatus_Type()
)
dfmObjectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmObjectStatus.setStatus("mandatory")
_DfmHostFullName_Type = DisplayString
_DfmHostFullName_Object = MibTableColumn
dfmHostFullName = _DfmHostFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 5),
    _DfmHostFullName_Type()
)
dfmHostFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmHostFullName.setStatus("mandatory")
_DfmCommentFields_Type = DisplayString
_DfmCommentFields_Object = MibTableColumn
dfmCommentFields = _DfmCommentFields_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 6),
    _DfmCommentFields_Type()
)
dfmCommentFields.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmCommentFields.setStatus("mandatory")
_DfmPhysicalHostId_Type = Integer32
_DfmPhysicalHostId_Object = MibTableColumn
dfmPhysicalHostId = _DfmPhysicalHostId_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 7),
    _DfmPhysicalHostId_Type()
)
dfmPhysicalHostId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmPhysicalHostId.setStatus("mandatory")
_DfmPhysicalHostFullName_Type = DisplayString
_DfmPhysicalHostFullName_Object = MibTableColumn
dfmPhysicalHostFullName = _DfmPhysicalHostFullName_Object(
    (1, 3, 6, 1, 4, 1, 789, 3, 12, 1, 8),
    _DfmPhysicalHostFullName_Type()
)
dfmPhysicalHostFullName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfmPhysicalHostFullName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dfmEvtSnapshotSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10001)
)
dfmEvtSnapshotSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapshotSpaceOk.setStatus(
        ""
    )

dfmEvtSnapshotFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10002)
)
dfmEvtSnapshotFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapshotFull.setStatus(
        ""
    )

dfmEvtVolumeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10011)
)
dfmEvtVolumeSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSpaceOk.setStatus(
        ""
    )

dfmEvtVolumeAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10012)
)
dfmEvtVolumeAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeAlmostFull.setStatus(
        ""
    )

dfmEvtVolumeFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10013)
)
dfmEvtVolumeFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeFull.setStatus(
        ""
    )

dfmEvtInodesUtilOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10021)
)
dfmEvtInodesUtilOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtInodesUtilOk.setStatus(
        ""
    )

dfmEvtInodesAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10022)
)
dfmEvtInodesAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtInodesAlmostFull.setStatus(
        ""
    )

dfmEvtInodesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10023)
)
dfmEvtInodesFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtInodesFull.setStatus(
        ""
    )

dfmEvtMgmtStNodeLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10031)
)
dfmEvtMgmtStNodeLimitOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStNodeLimitOk.setStatus(
        ""
    )

dfmEvtMgmtStNodeLimitNearlyReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10032)
)
dfmEvtMgmtStNodeLimitNearlyReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStNodeLimitNearlyReached.setStatus(
        ""
    )

dfmEvtMgmtStNodeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10033)
)
dfmEvtMgmtStNodeLimitReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStNodeLimitReached.setStatus(
        ""
    )

dfmEvtMgmtStPerfAdvisorFreeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10034)
)
dfmEvtMgmtStPerfAdvisorFreeSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStPerfAdvisorFreeSpaceOk.setStatus(
        ""
    )

dfmEvtMgmtStPerfAdvisorNotEnoughFreeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10035)
)
dfmEvtMgmtStPerfAdvisorNotEnoughFreeSpace.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStPerfAdvisorNotEnoughFreeSpace.setStatus(
        ""
    )

dfmEvtVolumeOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10036)
)
dfmEvtVolumeOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeOnline.setStatus(
        ""
    )

dfmEvtVolumeOfflineOrDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10037)
)
dfmEvtVolumeOfflineOrDestroyed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeOfflineOrDestroyed.setStatus(
        ""
    )

dfmEvtVolumeOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10038)
)
dfmEvtVolumeOffline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeOffline.setStatus(
        ""
    )

dfmEvtVolumeDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10039)
)
dfmEvtVolumeDestroyed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeDestroyed.setStatus(
        ""
    )

dfmEvtVolumeRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10040)
)
dfmEvtVolumeRestricted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeRestricted.setStatus(
        ""
    )

dfmEvtMgmtStLicenseNotExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10041)
)
dfmEvtMgmtStLicenseNotExpired.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStLicenseNotExpired.setStatus(
        ""
    )

dfmEvtMgmtStLicenseNearlyExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10042)
)
dfmEvtMgmtStLicenseNearlyExpired.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStLicenseNearlyExpired.setStatus(
        ""
    )

dfmEvtMgmtStLicenseExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10043)
)
dfmEvtMgmtStLicenseExpired.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStLicenseExpired.setStatus(
        ""
    )

dfmEvtMgmtStSchedulerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10049)
)
dfmEvtMgmtStSchedulerUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStSchedulerUp.setStatus(
        ""
    )

dfmEvtMgmtStSchedulerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10050)
)
dfmEvtMgmtStSchedulerDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStSchedulerDown.setStatus(
        ""
    )

dfmEvtMgmtStDatabaseUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10051)
)
dfmEvtMgmtStDatabaseUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStDatabaseUp.setStatus(
        ""
    )

dfmEvtMgmtStDatabaseDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10052)
)
dfmEvtMgmtStDatabaseDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStDatabaseDown.setStatus(
        ""
    )

dfmEvtMgmtStMonitorUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10053)
)
dfmEvtMgmtStMonitorUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStMonitorUp.setStatus(
        ""
    )

dfmEvtMgmtStMonitorDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10054)
)
dfmEvtMgmtStMonitorDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStMonitorDown.setStatus(
        ""
    )

dfmEvtMgmtStEventdUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10055)
)
dfmEvtMgmtStEventdUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStEventdUp.setStatus(
        ""
    )

dfmEvtMgmtStEventdDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10056)
)
dfmEvtMgmtStEventdDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStEventdDown.setStatus(
        ""
    )

dfmEvtMgmtStWatchdogUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10057)
)
dfmEvtMgmtStWatchdogUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStWatchdogUp.setStatus(
        ""
    )

dfmEvtMgmtStWatchdogDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10058)
)
dfmEvtMgmtStWatchdogDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStWatchdogDown.setStatus(
        ""
    )

dfmEvtMgmtStServerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10059)
)
dfmEvtMgmtStServerUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStServerUp.setStatus(
        ""
    )

dfmEvtMgmtStServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10060)
)
dfmEvtMgmtStServerDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStServerDown.setStatus(
        ""
    )

dfmEvtDisksSparesAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10061)
)
dfmEvtDisksSparesAvailable.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksSparesAvailable.setStatus(
        ""
    )

dfmEvtDisksNoSpares = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10062)
)
dfmEvtDisksNoSpares.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksNoSpares.setStatus(
        ""
    )

dfmEvtDisksNoneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10071)
)
dfmEvtDisksNoneFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksNoneFailed.setStatus(
        ""
    )

dfmEvtDisksSomeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10072)
)
dfmEvtDisksSomeFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksSomeFailed.setStatus(
        ""
    )

dfmEvtDisksReconstructNone = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10081)
)
dfmEvtDisksReconstructNone.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksReconstructNone.setStatus(
        ""
    )

dfmEvtDisksReconstructSome = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10082)
)
dfmEvtDisksReconstructSome.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDisksReconstructSome.setStatus(
        ""
    )

dfmEvtHostUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10091)
)
dfmEvtHostUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUp.setStatus(
        ""
    )

dfmEvtHostDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10092)
)
dfmEvtHostDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostDown.setStatus(
        ""
    )

dfmEvtHostReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10093)
)
dfmEvtHostReachable.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtHostReachable.setStatus(
        ""
    )

dfmEvtHostUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10094)
)
dfmEvtHostUnreachable.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUnreachable.setStatus(
        ""
    )

dfmEvtQtreeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10101)
)
dfmEvtQtreeSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeSpaceOk.setStatus(
        ""
    )

dfmEvtQtreeAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10102)
)
dfmEvtQtreeAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeAlmostFull.setStatus(
        ""
    )

dfmEvtQtreeFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10103)
)
dfmEvtQtreeFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeFull.setStatus(
        ""
    )

dfmEvtQtreeFilesOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10104)
)
dfmEvtQtreeFilesOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeFilesOk.setStatus(
        ""
    )

dfmEvtQtreeFilesAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10105)
)
dfmEvtQtreeFilesAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeFilesAlmostFull.setStatus(
        ""
    )

dfmEvtQtreeFilesFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10106)
)
dfmEvtQtreeFilesFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeFilesFull.setStatus(
        ""
    )

dfmEvtCpuUtilOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10111)
)
dfmEvtCpuUtilOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCpuUtilOk.setStatus(
        ""
    )

dfmEvtCpuTooBusy = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10112)
)
dfmEvtCpuTooBusy.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCpuTooBusy.setStatus(
        ""
    )

dfmEvtFansNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10121)
)
dfmEvtFansNormal.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFansNormal.setStatus(
        ""
    )

dfmEvtFansOneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10122)
)
dfmEvtFansOneFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFansOneFailed.setStatus(
        ""
    )

dfmEvtFansManyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10123)
)
dfmEvtFansManyFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFansManyFailed.setStatus(
        ""
    )

dfmEvtPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10131)
)
dfmEvtPowerSupplyOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtPowerSupplyOk.setStatus(
        ""
    )

dfmEvtPowerSupplyOneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10132)
)
dfmEvtPowerSupplyOneFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtPowerSupplyOneFailed.setStatus(
        ""
    )

dfmEvtPowerSupplyManyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10133)
)
dfmEvtPowerSupplyManyFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtPowerSupplyManyFailed.setStatus(
        ""
    )

dfmEvtTemperatureOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10141)
)
dfmEvtTemperatureOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTemperatureOk.setStatus(
        ""
    )

dfmEvtTemperatureHot = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10142)
)
dfmEvtTemperatureHot.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTemperatureHot.setStatus(
        ""
    )

dfmEvtNvramBatteryOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10151)
)
dfmEvtNvramBatteryOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryOk.setStatus(
        ""
    )

dfmEvtNvramBatteryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10152)
)
dfmEvtNvramBatteryLow.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryLow.setStatus(
        ""
    )

dfmEvtNvramBatteryDischarged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10153)
)
dfmEvtNvramBatteryDischarged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryDischarged.setStatus(
        ""
    )

dfmEvtNvramBatteryMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10154)
)
dfmEvtNvramBatteryMissing.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryMissing.setStatus(
        ""
    )

dfmEvtNvramBatteryOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10155)
)
dfmEvtNvramBatteryOld.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryOld.setStatus(
        ""
    )

dfmEvtNvramBatteryReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10156)
)
dfmEvtNvramBatteryReplace.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryReplace.setStatus(
        ""
    )

dfmEvtNvramBatteryUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10157)
)
dfmEvtNvramBatteryUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryUnknown.setStatus(
        ""
    )

dfmEvtNvramBatteryOverCharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10158)
)
dfmEvtNvramBatteryOverCharged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryOverCharged.setStatus(
        ""
    )

dfmEvtNvramBatteryFullyCharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10159)
)
dfmEvtNvramBatteryFullyCharged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNvramBatteryFullyCharged.setStatus(
        ""
    )

dfmEvtGlobalStatusOther = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10161)
)
dfmEvtGlobalStatusOther.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusOther.setStatus(
        ""
    )

dfmEvtGlobalStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10162)
)
dfmEvtGlobalStatusUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusUnknown.setStatus(
        ""
    )

dfmEvtGlobalStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10163)
)
dfmEvtGlobalStatusOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusOk.setStatus(
        ""
    )

dfmEvtGlobalStatusNonCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10164)
)
dfmEvtGlobalStatusNonCritical.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusNonCritical.setStatus(
        ""
    )

dfmEvtGlobalStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10165)
)
dfmEvtGlobalStatusCritical.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusCritical.setStatus(
        ""
    )

dfmEvtGlobalStatusNonRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10166)
)
dfmEvtGlobalStatusNonRecoverable.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtGlobalStatusNonRecoverable.setStatus(
        ""
    )

dfmEvtSnapMirrorOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10171)
)
dfmEvtSnapMirrorOff.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorOff.setStatus(
        ""
    )

dfmEvtSnapMirrorWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10172)
)
dfmEvtSnapMirrorWorking.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorWorking.setStatus(
        ""
    )

dfmEvtSnapMirrorNotScheduled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10173)
)
dfmEvtSnapMirrorNotScheduled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorNotScheduled.setStatus(
        ""
    )

dfmEvtSnapMirrorPossibleProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10174)
)
dfmEvtSnapMirrorPossibleProblem.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorPossibleProblem.setStatus(
        ""
    )

dfmEvtSnapMirrorNotWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10175)
)
dfmEvtSnapMirrorNotWorking.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorNotWorking.setStatus(
        ""
    )

dfmEvtSnapMirrorUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10176)
)
dfmEvtSnapMirrorUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorUnknown.setStatus(
        ""
    )

dfmEvtCfoSettingsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10181)
)
dfmEvtCfoSettingsEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoSettingsEnabled.setStatus(
        ""
    )

dfmEvtCfoSettingsNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10182)
)
dfmEvtCfoSettingsNotConfigured.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoSettingsNotConfigured.setStatus(
        ""
    )

dfmEvtCfoSettingsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10183)
)
dfmEvtCfoSettingsDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoSettingsDisabled.setStatus(
        ""
    )

dfmEvtCfoSettingsTakeoverDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10184)
)
dfmEvtCfoSettingsTakeoverDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoSettingsTakeoverDisabled.setStatus(
        ""
    )

dfmEvtCfoSettingsThisNodeDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10185)
)
dfmEvtCfoSettingsThisNodeDead.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoSettingsThisNodeDead.setStatus(
        ""
    )

dfmEvtCfoThisFilerCanTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10191)
)
dfmEvtCfoThisFilerCanTakeover.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoThisFilerCanTakeover.setStatus(
        ""
    )

dfmEvtCfoThisFilerCannotTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10192)
)
dfmEvtCfoThisFilerCannotTakeover.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoThisFilerCannotTakeover.setStatus(
        ""
    )

dfmEvtCfoThisFilerTakeover = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10193)
)
dfmEvtCfoThisFilerTakeover.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoThisFilerTakeover.setStatus(
        ""
    )

dfmEvtCfoThisFilerDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10194)
)
dfmEvtCfoThisFilerDead.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoThisFilerDead.setStatus(
        ""
    )

dfmEvtCfoPartnerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10201)
)
dfmEvtCfoPartnerOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoPartnerOk.setStatus(
        ""
    )

dfmEvtCfoPartnerMayBeDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10202)
)
dfmEvtCfoPartnerMayBeDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoPartnerMayBeDown.setStatus(
        ""
    )

dfmEvtCfoPartnerDead = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10203)
)
dfmEvtCfoPartnerDead.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoPartnerDead.setStatus(
        ""
    )

dfmEvtCfoInterconnectUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10211)
)
dfmEvtCfoInterconnectUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoInterconnectUp.setStatus(
        ""
    )

dfmEvtCfoInterconnectNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10212)
)
dfmEvtCfoInterconnectNotPresent.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoInterconnectNotPresent.setStatus(
        ""
    )

dfmEvtCfoInterconnectDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10213)
)
dfmEvtCfoInterconnectDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoInterconnectDown.setStatus(
        ""
    )

dfmEvtCfoInterconnectPartialFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10214)
)
dfmEvtCfoInterconnectPartialFailure.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCfoInterconnectPartialFailure.setStatus(
        ""
    )

dfmEvtSvdirDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10220)
)
dfmEvtSvdirDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSvdirDiscovered.setStatus(
        ""
    )

dfmEvtHostDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10221)
)
dfmEvtHostDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostDiscovered.setStatus(
        ""
    )

dfmEvtHostSystemIdChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10222)
)
dfmEvtHostSystemIdChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostSystemIdChanged.setStatus(
        ""
    )

dfmEvtHostNameChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10223)
)
dfmEvtHostNameChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostNameChanged.setStatus(
        ""
    )

dfmEvtOssvHostDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10224)
)
dfmEvtOssvHostDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtOssvHostDiscovered.setStatus(
        ""
    )

dfmEvtHostIdentityOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10225)
)
dfmEvtHostIdentityOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostIdentityOk.setStatus(
        ""
    )

dfmEvtHostIdentityConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10226)
)
dfmEvtHostIdentityConflict.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostIdentityConflict.setStatus(
        ""
    )

dfmEvtHostLoginOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10227)
)
dfmEvtHostLoginOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostLoginOk.setStatus(
        ""
    )

dfmEvtHostLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10228)
)
dfmEvtHostLoginFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostLoginFailed.setStatus(
        ""
    )

dfmEvtPrimaryHostDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10229)
)
dfmEvtPrimaryHostDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtPrimaryHostDiscovered.setStatus(
        ""
    )

dfmEvtMgmtStFreeSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10231)
)
dfmEvtMgmtStFreeSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStFreeSpaceOk.setStatus(
        ""
    )

dfmEvtMgmtStNotEnoughFreeSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10232)
)
dfmEvtMgmtStNotEnoughFreeSpace.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStNotEnoughFreeSpace.setStatus(
        ""
    )

dfmEvtMgmtStFileSystemFileSizeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10233)
)
dfmEvtMgmtStFileSystemFileSizeLimitReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStFileSystemFileSizeLimitReached.setStatus(
        ""
    )

dfmEvtConfigFileChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10241)
)
dfmEvtConfigFileChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtConfigFileChanged.setStatus(
        ""
    )

dfmEvtConfigGroupChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10242)
)
dfmEvtConfigGroupChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtConfigGroupChanged.setStatus(
        ""
    )

dfmEvtSnapMirrorDateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10261)
)
dfmEvtSnapMirrorDateOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDateOk.setStatus(
        ""
    )

dfmEvtSnapMirrorNearlyOutOfDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10262)
)
dfmEvtSnapMirrorNearlyOutOfDate.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorNearlyOutOfDate.setStatus(
        ""
    )

dfmEvtSnapMirrorOutOfDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10263)
)
dfmEvtSnapMirrorOutOfDate.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorOutOfDate.setStatus(
        ""
    )

dfmEvtSnapMirrorDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10264)
)
dfmEvtSnapMirrorDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDeleted.setStatus(
        ""
    )

dfmEvtSnapMirrorUndeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10265)
)
dfmEvtSnapMirrorUndeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorUndeleted.setStatus(
        ""
    )

dfmEvtSnapMirrorDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10266)
)
dfmEvtSnapMirrorDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDiscovered.setStatus(
        ""
    )

dfmEvtSnapMirrorModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10267)
)
dfmEvtSnapMirrorModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorModified.setStatus(
        ""
    )

dfmEvtNetworkOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10281)
)
dfmEvtNetworkOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNetworkOk.setStatus(
        ""
    )

dfmEvtNetworkTooLarge = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10282)
)
dfmEvtNetworkTooLarge.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNetworkTooLarge.setStatus(
        ""
    )

dfmEvtUserDiskSpaceQuotaOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10291)
)
dfmEvtUserDiskSpaceQuotaOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserDiskSpaceQuotaOk.setStatus(
        ""
    )

dfmEvtUserDiskSpaceQuotaAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10292)
)
dfmEvtUserDiskSpaceQuotaAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserDiskSpaceQuotaAlmostFull.setStatus(
        ""
    )

dfmEvtUserDiskSpaceQuotaFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10293)
)
dfmEvtUserDiskSpaceQuotaFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserDiskSpaceQuotaFull.setStatus(
        ""
    )

dfmEvtUserFilesQuotaOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10301)
)
dfmEvtUserFilesQuotaOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserFilesQuotaOk.setStatus(
        ""
    )

dfmEvtUserFilesQuotaAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10302)
)
dfmEvtUserFilesQuotaAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserFilesQuotaAlmostFull.setStatus(
        ""
    )

dfmEvtUserFilesQuotaFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10303)
)
dfmEvtUserFilesQuotaFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserFilesQuotaFull.setStatus(
        ""
    )

dfmEvtLunOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10311)
)
dfmEvtLunOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunOnline.setStatus(
        ""
    )

dfmEvtLunOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10312)
)
dfmEvtLunOffline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunOffline.setStatus(
        ""
    )

dfmEvtLunSnapshotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10313)
)
dfmEvtLunSnapshotOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunSnapshotOk.setStatus(
        ""
    )

dfmEvtLunSnapshotNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10314)
)
dfmEvtLunSnapshotNotPossible.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunSnapshotNotPossible.setStatus(
        ""
    )

dfmEvtLunHostClusterConfigOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10315)
)
dfmEvtLunHostClusterConfigOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunHostClusterConfigOk.setStatus(
        ""
    )

dfmEvtLunHostClusterConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10316)
)
dfmEvtLunHostClusterConfigError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLunHostClusterConfigError.setStatus(
        ""
    )

dfmEvtUserEmailAddressRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10321)
)
dfmEvtUserEmailAddressRejected.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtUserEmailAddressRejected.setStatus(
        ""
    )

dfmEvtUserEmailAddressOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10322)
)
dfmEvtUserEmailAddressOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtUserEmailAddressOk.setStatus(
        ""
    )

dfmEvtFCSwitchPortFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10331)
)
dfmEvtFCSwitchPortFaulty.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFCSwitchPortFaulty.setStatus(
        ""
    )

dfmEvtFCSwitchPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10332)
)
dfmEvtFCSwitchPortOffline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFCSwitchPortOffline.setStatus(
        ""
    )

dfmEvtFCSwitchPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10333)
)
dfmEvtFCSwitchPortOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFCSwitchPortOnline.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10334)
)
dfmEvtSnapvaultRelationshipCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipCreated.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10335)
)
dfmEvtSnapvaultRelationshipDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipDeleted.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10336)
)
dfmEvtSnapvaultRelationshipModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipModified.setStatus(
        ""
    )

dfmEvtSnapvaultReplicaDateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10337)
)
dfmEvtSnapvaultReplicaDateOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultReplicaDateOk.setStatus(
        ""
    )

dfmEvtSnapvaultReplicaNearlyOutOfDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10338)
)
dfmEvtSnapvaultReplicaNearlyOutOfDate.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultReplicaNearlyOutOfDate.setStatus(
        ""
    )

dfmEvtSnapvaultReplicaOutOfDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10339)
)
dfmEvtSnapvaultReplicaOutOfDate.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultReplicaOutOfDate.setStatus(
        ""
    )

dfmEvtSnapvaultBackupCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10340)
)
dfmEvtSnapvaultBackupCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultBackupCompleted.setStatus(
        ""
    )

dfmEvtSnapvaultBackupAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10341)
)
dfmEvtSnapvaultBackupAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultBackupAborted.setStatus(
        ""
    )

dfmEvtSnapvaultBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10342)
)
dfmEvtSnapvaultBackupFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultBackupFailed.setStatus(
        ""
    )

dfmEvtSnapvaultRestoreCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10343)
)
dfmEvtSnapvaultRestoreCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRestoreCompleted.setStatus(
        ""
    )

dfmEvtSnapvaultRestoreAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10344)
)
dfmEvtSnapvaultRestoreAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRestoreAborted.setStatus(
        ""
    )

dfmEvtSnapvaultRestoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10345)
)
dfmEvtSnapvaultRestoreFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRestoreFailed.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10346)
)
dfmEvtSnapvaultRelationshipDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipDiscovered.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipCreateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10347)
)
dfmEvtSnapvaultRelationshipCreateFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipCreateFailed.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipCreateAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10348)
)
dfmEvtSnapvaultRelationshipCreateAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipCreateAborted.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipDeleteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10349)
)
dfmEvtSnapvaultRelationshipDeleteFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipDeleteFailed.setStatus(
        ""
    )

dfmEvtSnapvaultRelationshipDeleteAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10350)
)
dfmEvtSnapvaultRelationshipDeleteAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapvaultRelationshipDeleteAborted.setStatus(
        ""
    )

dfmEvtTestAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10351)
)
dfmEvtTestAlarm.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTestAlarm.setStatus(
        ""
    )

dfmEvtUserDiskSpaceSoftLimitNotExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10361)
)
dfmEvtUserDiskSpaceSoftLimitNotExceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserDiskSpaceSoftLimitNotExceeded.setStatus(
        ""
    )

dfmEvtUserDiskSpaceSoftLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10362)
)
dfmEvtUserDiskSpaceSoftLimitExceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserDiskSpaceSoftLimitExceeded.setStatus(
        ""
    )

dfmEvtUserFilesSoftLimitNotExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10371)
)
dfmEvtUserFilesSoftLimitNotExceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserFilesSoftLimitNotExceeded.setStatus(
        ""
    )

dfmEvtUserFilesSoftLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10372)
)
dfmEvtUserFilesSoftLimitExceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"))
)
if mibBuilder.loadTexts:
    dfmEvtUserFilesSoftLimitExceeded.setStatus(
        ""
    )

dfmEvtHbaPortOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10373)
)
dfmEvtHbaPortOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHbaPortOnline.setStatus(
        ""
    )

dfmEvtHbaPortOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10374)
)
dfmEvtHbaPortOffline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHbaPortOffline.setStatus(
        ""
    )

dfmEvtHbaPortError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10375)
)
dfmEvtHbaPortError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHbaPortError.setStatus(
        ""
    )

dfmEvtSanHostLunChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10376)
)
dfmEvtSanHostLunChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSanHostLunChanged.setStatus(
        ""
    )

dfmEvtHostAgentUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10377)
)
dfmEvtHostAgentUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostAgentUp.setStatus(
        ""
    )

dfmEvtHostAgentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10378)
)
dfmEvtHostAgentDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostAgentDown.setStatus(
        ""
    )

dfmEvtHbaPortTrafficHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10379)
)
dfmEvtHbaPortTrafficHigh.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHbaPortTrafficHigh.setStatus(
        ""
    )

dfmEvtHbaPortTrafficOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10380)
)
dfmEvtHbaPortTrafficOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHbaPortTrafficOk.setStatus(
        ""
    )

dfmEvtSnapMirrorInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10381)
)
dfmEvtSnapMirrorInSync.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorInSync.setStatus(
        ""
    )

dfmEvtSnapMirrorOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10382)
)
dfmEvtSnapMirrorOutOfSync.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorOutOfSync.setStatus(
        ""
    )

dfmEvtSnapMirrorInitCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10383)
)
dfmEvtSnapMirrorInitCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorInitCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorInitAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10384)
)
dfmEvtSnapMirrorInitAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorInitAborted.setStatus(
        ""
    )

dfmEvtSnapMirrorInitFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10385)
)
dfmEvtSnapMirrorInitFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorInitFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10386)
)
dfmEvtSnapMirrorUpdateCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorUpdateCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorUpdateAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10387)
)
dfmEvtSnapMirrorUpdateAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorUpdateAborted.setStatus(
        ""
    )

dfmEvtSnapMirrorUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10388)
)
dfmEvtSnapMirrorUpdateFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorUpdateFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorBreakCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10389)
)
dfmEvtSnapMirrorBreakCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorBreakCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorBreakFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10390)
)
dfmEvtSnapMirrorBreakFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorBreakFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorResyncCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10391)
)
dfmEvtSnapMirrorResyncCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorResyncCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorResyncAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10392)
)
dfmEvtSnapMirrorResyncAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorResyncAborted.setStatus(
        ""
    )

dfmEvtSnapMirrorResyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10393)
)
dfmEvtSnapMirrorResyncFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorResyncFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorQuiesceCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10394)
)
dfmEvtSnapMirrorQuiesceCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorQuiesceCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorQuiesceAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10395)
)
dfmEvtSnapMirrorQuiesceAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorQuiesceAborted.setStatus(
        ""
    )

dfmEvtSnapMirrorQuiesceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10396)
)
dfmEvtSnapMirrorQuiesceFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorQuiesceFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorResumeCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10397)
)
dfmEvtSnapMirrorResumeCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorResumeCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorResumeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10398)
)
dfmEvtSnapMirrorResumeFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorResumeFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorAbortCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10399)
)
dfmEvtSnapMirrorAbortCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorAbortCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorAbortFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10400)
)
dfmEvtSnapMirrorAbortFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorAbortFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorDeleteCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10401)
)
dfmEvtSnapMirrorDeleteCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDeleteCompleted.setStatus(
        ""
    )

dfmEvtSnapMirrorDeleteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10402)
)
dfmEvtSnapMirrorDeleteFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDeleteFailed.setStatus(
        ""
    )

dfmEvtSnapMirrorDeleteAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10403)
)
dfmEvtSnapMirrorDeleteAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapMirrorDeleteAborted.setStatus(
        ""
    )

dfmEvtMgmtStLoadOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10411)
)
dfmEvtMgmtStLoadOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStLoadOk.setStatus(
        ""
    )

dfmEvtMgmtStLoadTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10412)
)
dfmEvtMgmtStLoadTooHigh.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStLoadTooHigh.setStatus(
        ""
    )

dfmEvtHostSnmpUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10422)
)
dfmEvtHostSnmpUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostSnmpUp.setStatus(
        ""
    )

dfmEvtHostSnmpDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10423)
)
dfmEvtHostSnmpDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostSnmpDown.setStatus(
        ""
    )

dfmEvtEnvEnclOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10432)
)
dfmEvtEnvEnclOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclOk.setStatus(
        ""
    )

dfmEvtEnvEnclFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10433)
)
dfmEvtEnvEnclFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclFailed.setStatus(
        ""
    )

dfmEvtEnvEnclFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10434)
)
dfmEvtEnvEnclFound.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclFound.setStatus(
        ""
    )

dfmEvtEnvEnclDissapeared = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10435)
)
dfmEvtEnvEnclDissapeared.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclDissapeared.setStatus(
        ""
    )

dfmEvtEnvEnclInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10436)
)
dfmEvtEnvEnclInactive.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclInactive.setStatus(
        ""
    )

dfmEvtEnvEnclActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10437)
)
dfmEvtEnvEnclActive.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEnvEnclActive.setStatus(
        ""
    )

dfmEvtAggregateSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10451)
)
dfmEvtAggregateSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateSpaceOk.setStatus(
        ""
    )

dfmEvtAggregateAlmostFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10452)
)
dfmEvtAggregateAlmostFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateAlmostFull.setStatus(
        ""
    )

dfmEvtAggregateFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10453)
)
dfmEvtAggregateFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateFull.setStatus(
        ""
    )

dfmEvtAggregateOvercommitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10461)
)
dfmEvtAggregateOvercommitOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateOvercommitOk.setStatus(
        ""
    )

dfmEvtAggregateAlmostOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10462)
)
dfmEvtAggregateAlmostOvercommitted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateAlmostOvercommitted.setStatus(
        ""
    )

dfmEvtAggregateOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10463)
)
dfmEvtAggregateOvercommitted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateOvercommitted.setStatus(
        ""
    )

dfmEvtVolumeCloneDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10471)
)
dfmEvtVolumeCloneDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeCloneDiscovered.setStatus(
        ""
    )

dfmEvtVolumeCloneDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10472)
)
dfmEvtVolumeCloneDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeCloneDeleted.setStatus(
        ""
    )

dfmEvtAggregateDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10481)
)
dfmEvtAggregateDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateDiscovered.setStatus(
        ""
    )

dfmEvtAggregateDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10482)
)
dfmEvtAggregateDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateDeleted.setStatus(
        ""
    )

dfmEvtTrapListenerFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10491)
)
dfmEvtTrapListenerFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTrapListenerFailed.setStatus(
        ""
    )

dfmEvtTrapListenerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10492)
)
dfmEvtTrapListenerOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTrapListenerOk.setStatus(
        ""
    )

dfmEvtHostColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10501)
)
dfmEvtHostColdStart.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostColdStart.setStatus(
        ""
    )

dfmEvtEmergencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10511)
)
dfmEvtEmergencyTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtEmergencyTrap.setStatus(
        ""
    )

dfmEvtAlertTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10521)
)
dfmEvtAlertTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAlertTrap.setStatus(
        ""
    )

dfmEvtCriticalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10531)
)
dfmEvtCriticalTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCriticalTrap.setStatus(
        ""
    )

dfmEvtErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10541)
)
dfmEvtErrorTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtErrorTrap.setStatus(
        ""
    )

dfmEvtWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10551)
)
dfmEvtWarningTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtWarningTrap.setStatus(
        ""
    )

dfmEvtNotificationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10561)
)
dfmEvtNotificationTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNotificationTrap.setStatus(
        ""
    )

dfmEvtInformationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10571)
)
dfmEvtInformationTrap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtInformationTrap.setStatus(
        ""
    )

dfmEvtIfAdminStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10581)
)
dfmEvtIfAdminStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtIfAdminStatusUp.setStatus(
        ""
    )

dfmEvtIfAdminStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10582)
)
dfmEvtIfAdminStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtIfAdminStatusDown.setStatus(
        ""
    )

dfmEvtIfAdminStatusTesting = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10583)
)
dfmEvtIfAdminStatusTesting.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtIfAdminStatusTesting.setStatus(
        ""
    )

dfmEvtIfAdminStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10584)
)
dfmEvtIfAdminStatusUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtIfAdminStatusUnknown.setStatus(
        ""
    )

dfmEvtScriptEmergency = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10591)
)
dfmEvtScriptEmergency.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptEmergency.setStatus(
        ""
    )

dfmEvtScriptCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10592)
)
dfmEvtScriptCritical.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptCritical.setStatus(
        ""
    )

dfmEvtScriptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10593)
)
dfmEvtScriptError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptError.setStatus(
        ""
    )

dfmEvtScriptWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10594)
)
dfmEvtScriptWarning.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptWarning.setStatus(
        ""
    )

dfmEvtScriptInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10595)
)
dfmEvtScriptInformation.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptInformation.setStatus(
        ""
    )

dfmEvtScriptNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10596)
)
dfmEvtScriptNormal.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptNormal.setStatus(
        ""
    )

dfmEvtScriptScheduleEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10597)
)
dfmEvtScriptScheduleEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptScheduleEnabled.setStatus(
        ""
    )

dfmEvtScriptScheduleDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10598)
)
dfmEvtScriptScheduleDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScriptScheduleDisabled.setStatus(
        ""
    )

dfmEvtAggrSnapReserveOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10601)
)
dfmEvtAggrSnapReserveOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggrSnapReserveOk.setStatus(
        ""
    )

dfmEvtAggrSnapReserveNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10602)
)
dfmEvtAggrSnapReserveNearlyFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggrSnapReserveNearlyFull.setStatus(
        ""
    )

dfmEvtAggrSnapReserveFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10603)
)
dfmEvtAggrSnapReserveFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggrSnapReserveFull.setStatus(
        ""
    )

dfmEvtVolumeSpaceReserveOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10611)
)
dfmEvtVolumeSpaceReserveOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSpaceReserveOk.setStatus(
        ""
    )

dfmEvtVolumeSpaceReserveNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10612)
)
dfmEvtVolumeSpaceReserveNearlyFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSpaceReserveNearlyFull.setStatus(
        ""
    )

dfmEvtVolumeSpaceReserveFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10613)
)
dfmEvtVolumeSpaceReserveFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSpaceReserveFull.setStatus(
        ""
    )

dfmEvtVolumeFirstSnapOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10621)
)
dfmEvtVolumeFirstSnapOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeFirstSnapOk.setStatus(
        ""
    )

dfmEvtVolumeNearlyNoFirstSnap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10622)
)
dfmEvtVolumeNearlyNoFirstSnap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNearlyNoFirstSnap.setStatus(
        ""
    )

dfmEvtVolumeNoFirstSnap = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10623)
)
dfmEvtVolumeNoFirstSnap.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNoFirstSnap.setStatus(
        ""
    )

dfmEvtVolumeNewSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10631)
)
dfmEvtVolumeNewSnapshot.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNewSnapshot.setStatus(
        ""
    )

dfmEvtVolumeSnapshotDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10632)
)
dfmEvtVolumeSnapshotDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSnapshotDeleted.setStatus(
        ""
    )

dfmEvtLocalFilerConfigStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10641)
)
dfmEvtLocalFilerConfigStatusOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLocalFilerConfigStatusOk.setStatus(
        ""
    )

dfmEvtLocalFilerConfigStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10642)
)
dfmEvtLocalFilerConfigStatusChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLocalFilerConfigStatusChanged.setStatus(
        ""
    )

dfmEvtFilerLoginOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10651)
)
dfmEvtFilerLoginOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerLoginOk.setStatus(
        ""
    )

dfmEvtFilerLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10652)
)
dfmEvtFilerLoginFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerLoginFailed.setStatus(
        ""
    )

dfmEvtNdmpStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10661)
)
dfmEvtNdmpStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpStatusUp.setStatus(
        ""
    )

dfmEvtNdmpStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10662)
)
dfmEvtNdmpStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpStatusDown.setStatus(
        ""
    )

dfmEvtFilerConfigPushStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10671)
)
dfmEvtFilerConfigPushStatusOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerConfigPushStatusOk.setStatus(
        ""
    )

dfmEvtFilerConfigPushStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10672)
)
dfmEvtFilerConfigPushStatusError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerConfigPushStatusError.setStatus(
        ""
    )

dfmEvtVfilerDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10681)
)
dfmEvtVfilerDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerDiscovered.setStatus(
        ""
    )

dfmEvtVfilerDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10682)
)
dfmEvtVfilerDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerDeleted.setStatus(
        ""
    )

dfmEvtVfilerRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10683)
)
dfmEvtVfilerRenamed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerRenamed.setStatus(
        ""
    )

dfmEvtVfilerStorageUnitAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10684)
)
dfmEvtVfilerStorageUnitAdded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerStorageUnitAdded.setStatus(
        ""
    )

dfmEvtVfilerStorageUnitRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10685)
)
dfmEvtVfilerStorageUnitRemoved.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerStorageUnitRemoved.setStatus(
        ""
    )

dfmEvtVfilerIpAddressAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10686)
)
dfmEvtVfilerIpAddressAdded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerIpAddressAdded.setStatus(
        ""
    )

dfmEvtVfilerIpAddressRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10687)
)
dfmEvtVfilerIpAddressRemoved.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerIpAddressRemoved.setStatus(
        ""
    )

dfmEvtVfilerHostingFilerLoginOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10688)
)
dfmEvtVfilerHostingFilerLoginOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerHostingFilerLoginOk.setStatus(
        ""
    )

dfmEvtVfilerHostingFilerLoginFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10689)
)
dfmEvtVfilerHostingFilerLoginFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerHostingFilerLoginFailed.setStatus(
        ""
    )

dfmEvtVolumeGrowthRateAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10691)
)
dfmEvtVolumeGrowthRateAbnormal.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeGrowthRateAbnormal.setStatus(
        ""
    )

dfmEvtVolumeGrowthRateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10692)
)
dfmEvtVolumeGrowthRateOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeGrowthRateOk.setStatus(
        ""
    )

dfmEvtQtreeGrowthRateAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10693)
)
dfmEvtQtreeGrowthRateAbnormal.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeGrowthRateAbnormal.setStatus(
        ""
    )

dfmEvtQtreeGrowthRateOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10694)
)
dfmEvtQtreeGrowthRateOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtQtreeGrowthRateOk.setStatus(
        ""
    )

dfmEvtSnapSchedModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10701)
)
dfmEvtSnapSchedModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapSchedModified.setStatus(
        ""
    )

dfmEvtSnapSchedSmConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10711)
)
dfmEvtSnapSchedSmConflict.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapSchedSmConflict.setStatus(
        ""
    )

dfmEvtSnapSchedSmOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10712)
)
dfmEvtSnapSchedSmOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapSchedSmOk.setStatus(
        ""
    )

dfmEvtSnapSchedSvConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10721)
)
dfmEvtSnapSchedSvConflict.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapSchedSvConflict.setStatus(
        ""
    )

dfmEvtSnapSchedSvOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10722)
)
dfmEvtSnapSchedSvOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapSchedSvOk.setStatus(
        ""
    )

dfmEvtTooManySnapshots = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10731)
)
dfmEvtTooManySnapshots.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtTooManySnapshots.setStatus(
        ""
    )

dfmEvtNotTooManySnapshots = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10732)
)
dfmEvtNotTooManySnapshots.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNotTooManySnapshots.setStatus(
        ""
    )

dfmEvtSnapDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10741)
)
dfmEvtSnapDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapDisabled.setStatus(
        ""
    )

dfmEvtSnapEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10742)
)
dfmEvtSnapEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapEnabled.setStatus(
        ""
    )

dfmEvtDatabaseBackupSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10751)
)
dfmEvtDatabaseBackupSucceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatabaseBackupSucceeded.setStatus(
        ""
    )

dfmEvtDatabaseBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10752)
)
dfmEvtDatabaseBackupFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatabaseBackupFailed.setStatus(
        ""
    )

dfmEvtDatabaseRestoreSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10753)
)
dfmEvtDatabaseRestoreSucceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatabaseRestoreSucceeded.setStatus(
        ""
    )

dfmEvtDatabaseRestoreFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10754)
)
dfmEvtDatabaseRestoreFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatabaseRestoreFailed.setStatus(
        ""
    )

dfmEvtMaxdirsizeReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10761)
)
dfmEvtMaxdirsizeReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMaxdirsizeReached.setStatus(
        ""
    )

dfmEvtMaxdirsizeNearlyReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10762)
)
dfmEvtMaxdirsizeNearlyReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMaxdirsizeNearlyReached.setStatus(
        ""
    )

dfmEvtSnapTooOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10771)
)
dfmEvtSnapTooOld.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapTooOld.setStatus(
        ""
    )

dfmEvtSnapNotTooOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10772)
)
dfmEvtSnapNotTooOld.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapNotTooOld.setStatus(
        ""
    )

dfmEvtRpmOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10781)
)
dfmEvtRpmOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtRpmOnline.setStatus(
        ""
    )

dfmEvtRpmUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10782)
)
dfmEvtRpmUnavailable.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtRpmUnavailable.setStatus(
        ""
    )

dfmEvtAggregateStateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10791)
)
dfmEvtAggregateStateFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateStateFailed.setStatus(
        ""
    )

dfmEvtAggregateStateOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10792)
)
dfmEvtAggregateStateOnline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateStateOnline.setStatus(
        ""
    )

dfmEvtAggregateStateOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10793)
)
dfmEvtAggregateStateOffline.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateStateOffline.setStatus(
        ""
    )

dfmEvtAggregateStateRestricted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10794)
)
dfmEvtAggregateStateRestricted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateStateRestricted.setStatus(
        ""
    )

dfmEvtDatasetCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10801)
)
dfmEvtDatasetCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetCreated.setStatus(
        ""
    )

dfmEvtDatasetDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10811)
)
dfmEvtDatasetDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDeleted.setStatus(
        ""
    )

dfmEvtDatasetModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10821)
)
dfmEvtDatasetModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetModified.setStatus(
        ""
    )

dfmEvtSnapshotCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10831)
)
dfmEvtSnapshotCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapshotCreated.setStatus(
        ""
    )

dfmEvtSnapshotFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10833)
)
dfmEvtSnapshotFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtSnapshotFailed.setStatus(
        ""
    )

dfmEvtDatasetProvisioningOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10841)
)
dfmEvtDatasetProvisioningOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProvisioningOk.setStatus(
        ""
    )

dfmEvtDatasetProvisioningFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10842)
)
dfmEvtDatasetProvisioningFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProvisioningFailed.setStatus(
        ""
    )

dfmEvtDatasetProtectionProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10851)
)
dfmEvtDatasetProtectionProtected.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionProtected.setStatus(
        ""
    )

dfmEvtDatasetProtectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10852)
)
dfmEvtDatasetProtectionFailure.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionFailure.setStatus(
        ""
    )

dfmEvtDatasetProtectionSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10853)
)
dfmEvtDatasetProtectionSuspended.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionSuspended.setStatus(
        ""
    )

dfmEvtDatasetProtectionLagError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10854)
)
dfmEvtDatasetProtectionLagError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionLagError.setStatus(
        ""
    )

dfmEvtDatasetProtectionLagWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10855)
)
dfmEvtDatasetProtectionLagWarning.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionLagWarning.setStatus(
        ""
    )

dfmEvtDatasetProtectionUninitialized = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10856)
)
dfmEvtDatasetProtectionUninitialized.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetProtectionUninitialized.setStatus(
        ""
    )

dfmEvtDatasetConformant = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10861)
)
dfmEvtDatasetConformant.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetConformant.setStatus(
        ""
    )

dfmEvtDatasetConforming = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10862)
)
dfmEvtDatasetConforming.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetConforming.setStatus(
        ""
    )

dfmEvtDatasetNonConformant = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10863)
)
dfmEvtDatasetNonConformant.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetNonConformant.setStatus(
        ""
    )

dfmEvtDatasetCloneSnapshotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10864)
)
dfmEvtDatasetCloneSnapshotFound.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetCloneSnapshotFound.setStatus(
        ""
    )

dfmEvtDatasetNoCloneSnapshotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10865)
)
dfmEvtDatasetNoCloneSnapshotFound.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetNoCloneSnapshotFound.setStatus(
        ""
    )

dfmEvtDatasetWriteCheckWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10866)
)
dfmEvtDatasetWriteCheckWarning.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetWriteCheckWarning.setStatus(
        ""
    )

dfmEvtDatasetWriteCheckOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10867)
)
dfmEvtDatasetWriteCheckOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetWriteCheckOk.setStatus(
        ""
    )

dfmEvtResourcePoolCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10871)
)
dfmEvtResourcePoolCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolCreated.setStatus(
        ""
    )

dfmEvtResourcePoolDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10881)
)
dfmEvtResourcePoolDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolDeleted.setStatus(
        ""
    )

dfmEvtResourcePoolModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10891)
)
dfmEvtResourcePoolModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolModified.setStatus(
        ""
    )

dfmEvtResourcePoolSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10901)
)
dfmEvtResourcePoolSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolSpaceOk.setStatus(
        ""
    )

dfmEvtResourcePoolSpaceNearlyFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10902)
)
dfmEvtResourcePoolSpaceNearlyFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolSpaceNearlyFull.setStatus(
        ""
    )

dfmEvtResourcePoolSpaceFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10903)
)
dfmEvtResourcePoolSpaceFull.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourcePoolSpaceFull.setStatus(
        ""
    )

dfmEvtDataProtectionPolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10911)
)
dfmEvtDataProtectionPolicyCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionPolicyCreated.setStatus(
        ""
    )

dfmEvtDataProtectionPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10921)
)
dfmEvtDataProtectionPolicyDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionPolicyDeleted.setStatus(
        ""
    )

dfmEvtDataProtectionPolicyModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10931)
)
dfmEvtDataProtectionPolicyModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionPolicyModified.setStatus(
        ""
    )

dfmEvtDataProtectionScheduleCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10941)
)
dfmEvtDataProtectionScheduleCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionScheduleCreated.setStatus(
        ""
    )

dfmEvtDataProtectionScheduleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10951)
)
dfmEvtDataProtectionScheduleDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionScheduleDeleted.setStatus(
        ""
    )

dfmEvtDataProtectionScheduleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10961)
)
dfmEvtDataProtectionScheduleModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionScheduleModified.setStatus(
        ""
    )

dfmEvtNdmpCredentialsGood = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10971)
)
dfmEvtNdmpCredentialsGood.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpCredentialsGood.setStatus(
        ""
    )

dfmEvtNdmpCredentialsBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10972)
)
dfmEvtNdmpCredentialsBad.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpCredentialsBad.setStatus(
        ""
    )

dfmEvtDataProtectionJobStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10981)
)
dfmEvtDataProtectionJobStarted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataProtectionJobStarted.setStatus(
        ""
    )

dfmEvtHostDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 10991)
)
dfmEvtHostDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostDeleted.setStatus(
        ""
    )

dfmEvtHostModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11001)
)
dfmEvtHostModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostModified.setStatus(
        ""
    )

dfmEvtResourceGroupCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11011)
)
dfmEvtResourceGroupCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourceGroupCreated.setStatus(
        ""
    )

dfmEvtResourceGroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11021)
)
dfmEvtResourceGroupDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourceGroupDeleted.setStatus(
        ""
    )

dfmEvtResourceGroupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11031)
)
dfmEvtResourceGroupModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtResourceGroupModified.setStatus(
        ""
    )

dfmEvtAlarmCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11041)
)
dfmEvtAlarmCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAlarmCreated.setStatus(
        ""
    )

dfmEvtAlarmDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11051)
)
dfmEvtAlarmDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAlarmDeleted.setStatus(
        ""
    )

dfmEvtAlarmModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11061)
)
dfmEvtAlarmModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAlarmModified.setStatus(
        ""
    )

dfmEvtNdmpCommunicationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11071)
)
dfmEvtNdmpCommunicationUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpCommunicationUp.setStatus(
        ""
    )

dfmEvtNdmpCommunicationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11081)
)
dfmEvtNdmpCommunicationDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNdmpCommunicationDown.setStatus(
        ""
    )

dfmEvtDatasetBackupCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11090)
)
dfmEvtDatasetBackupCompleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetBackupCompleted.setStatus(
        ""
    )

dfmEvtDatasetBackupAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11091)
)
dfmEvtDatasetBackupAborted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetBackupAborted.setStatus(
        ""
    )

dfmEvtDatasetBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11092)
)
dfmEvtDatasetBackupFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetBackupFailed.setStatus(
        ""
    )

dfmEvtFilerCommunicationOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11100)
)
dfmEvtFilerCommunicationOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerCommunicationOk.setStatus(
        ""
    )

dfmEvtFilerCommunicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11101)
)
dfmEvtFilerCommunicationFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtFilerCommunicationFailed.setStatus(
        ""
    )

dfmEvtLocalVfilerConfigStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11111)
)
dfmEvtLocalVfilerConfigStatusOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLocalVfilerConfigStatusOk.setStatus(
        ""
    )

dfmEvtLocalVfilerConfigStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11112)
)
dfmEvtLocalVfilerConfigStatusChanged.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtLocalVfilerConfigStatusChanged.setStatus(
        ""
    )

dfmEvtVfilerConfigPushStatusOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11113)
)
dfmEvtVfilerConfigPushStatusOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerConfigPushStatusOk.setStatus(
        ""
    )

dfmEvtVfilerConfigPushStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11114)
)
dfmEvtVfilerConfigPushStatusError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerConfigPushStatusError.setStatus(
        ""
    )

dfmEvtScheduledReportOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11121)
)
dfmEvtScheduledReportOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScheduledReportOk.setStatus(
        ""
    )

dfmEvtScheduledReportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11122)
)
dfmEvtScheduledReportFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtScheduledReportFailed.setStatus(
        ""
    )

dfmEvtReportScheduleEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11123)
)
dfmEvtReportScheduleEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtReportScheduleEnabled.setStatus(
        ""
    )

dfmEvtReportScheduleDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11124)
)
dfmEvtReportScheduleDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtReportScheduleDisabled.setStatus(
        ""
    )

dfmEvtHostRoleDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11131)
)
dfmEvtHostRoleDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostRoleDiscovered.setStatus(
        ""
    )

dfmEvtHostRoleDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11132)
)
dfmEvtHostRoleDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostRoleDeleted.setStatus(
        ""
    )

dfmEvtHostRoleModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11133)
)
dfmEvtHostRoleModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostRoleModified.setStatus(
        ""
    )

dfmEvtHostUsergroupDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11134)
)
dfmEvtHostUsergroupDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUsergroupDiscovered.setStatus(
        ""
    )

dfmEvtHostUsergroupDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11135)
)
dfmEvtHostUsergroupDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUsergroupDeleted.setStatus(
        ""
    )

dfmEvtHostUsergroupModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11136)
)
dfmEvtHostUsergroupModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUsergroupModified.setStatus(
        ""
    )

dfmEvtHostUserDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11137)
)
dfmEvtHostUserDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUserDiscovered.setStatus(
        ""
    )

dfmEvtHostUserDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11138)
)
dfmEvtHostUserDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUserDeleted.setStatus(
        ""
    )

dfmEvtHostUserModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11139)
)
dfmEvtHostUserModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostUserModified.setStatus(
        ""
    )

dfmEvtHostDomainUserModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11140)
)
dfmEvtHostDomainUserModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostDomainUserModified.setStatus(
        ""
    )

dfmEvtVolumeQuotaOvercommitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11151)
)
dfmEvtVolumeQuotaOvercommitOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeQuotaOvercommitOk.setStatus(
        ""
    )

dfmEvtVolumeQuotaAlmostOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11152)
)
dfmEvtVolumeQuotaAlmostOvercommitted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeQuotaAlmostOvercommitted.setStatus(
        ""
    )

dfmEvtVolumeQuotaOvercommitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11153)
)
dfmEvtVolumeQuotaOvercommitted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeQuotaOvercommitted.setStatus(
        ""
    )

dfmEvtDataExportOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11161)
)
dfmEvtDataExportOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataExportOk.setStatus(
        ""
    )

dfmEvtDataExportFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11162)
)
dfmEvtDataExportFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDataExportFailed.setStatus(
        ""
    )

dfmEvtDatasetMemberResized = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11171)
)
dfmEvtDatasetMemberResized.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberResized.setStatus(
        ""
    )

dfmEvtDatasetMemberResizeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11172)
)
dfmEvtDatasetMemberResizeFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberResizeFailed.setStatus(
        ""
    )

dfmEvtProvisioningPolicyCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11181)
)
dfmEvtProvisioningPolicyCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtProvisioningPolicyCreated.setStatus(
        ""
    )

dfmEvtProvisioningPolicyDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11182)
)
dfmEvtProvisioningPolicyDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtProvisioningPolicyDeleted.setStatus(
        ""
    )

dfmEvtProvisioningPolicyModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11183)
)
dfmEvtProvisioningPolicyModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtProvisioningPolicyModified.setStatus(
        ""
    )

dfmEvtVFilerTemplateCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11191)
)
dfmEvtVFilerTemplateCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVFilerTemplateCreated.setStatus(
        ""
    )

dfmEvtVFilerTemplateDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11192)
)
dfmEvtVFilerTemplateDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVFilerTemplateDeleted.setStatus(
        ""
    )

dfmEvtVFilerTemplateModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11193)
)
dfmEvtVFilerTemplateModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVFilerTemplateModified.setStatus(
        ""
    )

dfmEvtDatasetSpaceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11201)
)
dfmEvtDatasetSpaceOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetSpaceOk.setStatus(
        ""
    )

dfmEvtDatasetSpaceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11202)
)
dfmEvtDatasetSpaceWarning.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetSpaceWarning.setStatus(
        ""
    )

dfmEvtDatasetSpaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11203)
)
dfmEvtDatasetSpaceError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetSpaceError.setStatus(
        ""
    )

dfmEvtVolumeAutosized = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11211)
)
dfmEvtVolumeAutosized.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeAutosized.setStatus(
        ""
    )

dfmEvtVolumeSnapshotsAutoDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11221)
)
dfmEvtVolumeSnapshotsAutoDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeSnapshotsAutoDeleted.setStatus(
        ""
    )

dfmEvtVolumeNextSnapshotNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11231)
)
dfmEvtVolumeNextSnapshotNotPossible.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNextSnapshotNotPossible.setStatus(
        ""
    )

dfmEvtVolumeNextSnapshotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11232)
)
dfmEvtVolumeNextSnapshotPossible.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNextSnapshotPossible.setStatus(
        ""
    )

dfmEvtDatasetMemberDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11241)
)
dfmEvtDatasetMemberDestroyed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberDestroyed.setStatus(
        ""
    )

dfmEvtDatasetMemberDestroyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11242)
)
dfmEvtDatasetMemberDestroyFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberDestroyFailed.setStatus(
        ""
    )

dfmEvtMgmtStProvMgrNodeLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11262)
)
dfmEvtMgmtStProvMgrNodeLimitOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProvMgrNodeLimitOk.setStatus(
        ""
    )

dfmEvtMgmtStProvMgrNodeLimitNearlyReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11263)
)
dfmEvtMgmtStProvMgrNodeLimitNearlyReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProvMgrNodeLimitNearlyReached.setStatus(
        ""
    )

dfmEvtMgmtStProvMgrNodeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11264)
)
dfmEvtMgmtStProvMgrNodeLimitReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProvMgrNodeLimitReached.setStatus(
        ""
    )

dfmEvtMgmtStProtMgrNodeLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11265)
)
dfmEvtMgmtStProtMgrNodeLimitOk.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProtMgrNodeLimitOk.setStatus(
        ""
    )

dfmEvtMgmtStProtMgrNodeLimitNearlyReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11266)
)
dfmEvtMgmtStProtMgrNodeLimitNearlyReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProtMgrNodeLimitNearlyReached.setStatus(
        ""
    )

dfmEvtMgmtStProtMgrNodeLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11267)
)
dfmEvtMgmtStProtMgrNodeLimitReached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtMgmtStProtMgrNodeLimitReached.setStatus(
        ""
    )

dfmEvtDatasetNotMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11270)
)
dfmEvtDatasetNotMigrating.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetNotMigrating.setStatus(
        ""
    )

dfmEvtDatasetMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11271)
)
dfmEvtDatasetMigrating.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMigrating.setStatus(
        ""
    )

dfmEvtDatasetMigrateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11272)
)
dfmEvtDatasetMigrateFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMigrateFailed.setStatus(
        ""
    )

dfmEvtDatasetMigratedWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11273)
)
dfmEvtDatasetMigratedWithErrors.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMigratedWithErrors.setStatus(
        ""
    )

dfmEvtDatasetMigrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11274)
)
dfmEvtDatasetMigrated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMigrated.setStatus(
        ""
    )

dfmEvtDatasetRollbackWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11275)
)
dfmEvtDatasetRollbackWithErrors.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetRollbackWithErrors.setStatus(
        ""
    )

dfmEvtDatasetRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11279)
)
dfmEvtDatasetRollback.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetRollback.setStatus(
        ""
    )

dfmEvtVfilerNotMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11280)
)
dfmEvtVfilerNotMigrating.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerNotMigrating.setStatus(
        ""
    )

dfmEvtVfilerMigrating = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11281)
)
dfmEvtVfilerMigrating.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerMigrating.setStatus(
        ""
    )

dfmEvtVfilerMigrateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11282)
)
dfmEvtVfilerMigrateFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerMigrateFailed.setStatus(
        ""
    )

dfmEvtVfilerMigratedWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11283)
)
dfmEvtVfilerMigratedWithErrors.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerMigratedWithErrors.setStatus(
        ""
    )

dfmEvtVfilerMigrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11284)
)
dfmEvtVfilerMigrated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerMigrated.setStatus(
        ""
    )

dfmEvtVolumeOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11285)
)
dfmEvtVolumeOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeOverDeduplicated.setStatus(
        ""
    )

dfmEvtVfilerRollbackWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11286)
)
dfmEvtVfilerRollbackWithErrors.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerRollbackWithErrors.setStatus(
        ""
    )

dfmEvtVfilerRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11291)
)
dfmEvtVfilerRollback.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtVfilerRollback.setStatus(
        ""
    )

dfmEvtVolumeNearlyOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11292)
)
dfmEvtVolumeNearlyOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNearlyOverDeduplicated.setStatus(
        ""
    )

dfmEvtVolumeNotOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11293)
)
dfmEvtVolumeNotOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtVolumeNotOverDeduplicated.setStatus(
        ""
    )

dfmEvtAggregateOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11294)
)
dfmEvtAggregateOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateOverDeduplicated.setStatus(
        ""
    )

dfmEvtAggregateNearlyOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11295)
)
dfmEvtAggregateNearlyOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateNearlyOverDeduplicated.setStatus(
        ""
    )

dfmEvtAggregateNotOverDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11296)
)
dfmEvtAggregateNotOverDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtAggregateNotOverDeduplicated.setStatus(
        ""
    )

dfmEvtDatasetMemberDeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11297)
)
dfmEvtDatasetMemberDeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberDeduplicated.setStatus(
        ""
    )

dfmEvtDatasetMemberDeduplicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11298)
)
dfmEvtDatasetMemberDeduplicationFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberDeduplicationFailed.setStatus(
        ""
    )

dfmEvtDatasetMemberUndeduplicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11299)
)
dfmEvtDatasetMemberUndeduplicated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberUndeduplicated.setStatus(
        ""
    )

dfmEvtDatasetMemberUndeduplicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11300)
)
dfmEvtDatasetMemberUndeduplicationFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetMemberUndeduplicationFailed.setStatus(
        ""
    )

dfmEvtHostNfsServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11310)
)
dfmEvtHostNfsServiceStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostNfsServiceStatusUp.setStatus(
        ""
    )

dfmEvtHostNfsServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11371)
)
dfmEvtHostNfsServiceStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostNfsServiceStatusDown.setStatus(
        ""
    )

dfmEvtHostCifsServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11372)
)
dfmEvtHostCifsServiceStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostCifsServiceStatusUp.setStatus(
        ""
    )

dfmEvtHostCifsServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11373)
)
dfmEvtHostCifsServiceStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostCifsServiceStatusDown.setStatus(
        ""
    )

dfmEvtHostIscsiServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11374)
)
dfmEvtHostIscsiServiceStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostIscsiServiceStatusUp.setStatus(
        ""
    )

dfmEvtHostIscsiServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11375)
)
dfmEvtHostIscsiServiceStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostIscsiServiceStatusDown.setStatus(
        ""
    )

dfmEvtHostFcpServiceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11376)
)
dfmEvtHostFcpServiceStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostFcpServiceStatusUp.setStatus(
        ""
    )

dfmEvtHostFcpServiceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11377)
)
dfmEvtHostFcpServiceStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtHostFcpServiceStatusDown.setStatus(
        ""
    )

dfmEvtCommentFieldCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11378)
)
dfmEvtCommentFieldCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCommentFieldCreated.setStatus(
        ""
    )

dfmEvtCommentFieldModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11379)
)
dfmEvtCommentFieldModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCommentFieldModified.setStatus(
        ""
    )

dfmEvtCommentFieldDestroyed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11380)
)
dfmEvtCommentFieldDestroyed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCommentFieldDestroyed.setStatus(
        ""
    )

dfmEvtNfsPerClientStatsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11390)
)
dfmEvtNfsPerClientStatsEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNfsPerClientStatsEnabled.setStatus(
        ""
    )

dfmEvtNfsPerClientStatsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11391)
)
dfmEvtNfsPerClientStatsDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtNfsPerClientStatsDisabled.setStatus(
        ""
    )

dfmEvtCifsPerClientStatsEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11392)
)
dfmEvtCifsPerClientStatsEnabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCifsPerClientStatsEnabled.setStatus(
        ""
    )

dfmEvtCifsPerClientStatsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11393)
)
dfmEvtCifsPerClientStatsDisabled.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtCifsPerClientStatsDisabled.setStatus(
        ""
    )

dfmEvtDatasetDrStateReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11400)
)
dfmEvtDatasetDrStateReady.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStateReady.setStatus(
        ""
    )

dfmEvtDatasetDrStateFailingOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11401)
)
dfmEvtDatasetDrStateFailingOver.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStateFailingOver.setStatus(
        ""
    )

dfmEvtDatasetDrStateFailedOver = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11402)
)
dfmEvtDatasetDrStateFailedOver.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStateFailedOver.setStatus(
        ""
    )

dfmEvtDatasetDrStateFailoverError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11403)
)
dfmEvtDatasetDrStateFailoverError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStateFailoverError.setStatus(
        ""
    )

dfmEvtDatasetDrStatusNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11410)
)
dfmEvtDatasetDrStatusNormal.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStatusNormal.setStatus(
        ""
    )

dfmEvtDatasetDrStatusWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11411)
)
dfmEvtDatasetDrStatusWarning.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStatusWarning.setStatus(
        ""
    )

dfmEvtDatasetDrStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11412)
)
dfmEvtDatasetDrStatusError.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmPhysicalHostFullName"))
)
if mibBuilder.loadTexts:
    dfmEvtDatasetDrStatusError.setStatus(
        ""
    )

dfmEvtVserverDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11421)
)
dfmEvtVserverDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtVserverDiscovered.setStatus(
        ""
    )

dfmEvtVserverDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11422)
)
dfmEvtVserverDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtVserverDeleted.setStatus(
        ""
    )

dfmEvtVserverRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11423)
)
dfmEvtVserverRenamed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtVserverRenamed.setStatus(
        ""
    )

dfmEvtClusterDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11431)
)
dfmEvtClusterDiscovered.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtClusterDiscovered.setStatus(
        ""
    )

dfmEvtClusterRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11432)
)
dfmEvtClusterRenamed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtClusterRenamed.setStatus(
        ""
    )

dfmEvtClusterNodeAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11433)
)
dfmEvtClusterNodeAdded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtClusterNodeAdded.setStatus(
        ""
    )

dfmEvtClusterNodeRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11434)
)
dfmEvtClusterNodeRemoved.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtClusterNodeRemoved.setStatus(
        ""
    )

dfmEvtPortStatusUndef = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11435)
)
dfmEvtPortStatusUndef.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtPortStatusUndef.setStatus(
        ""
    )

dfmEvtPortStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11436)
)
dfmEvtPortStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtPortStatusUp.setStatus(
        ""
    )

dfmEvtPortStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11437)
)
dfmEvtPortStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtPortStatusDown.setStatus(
        ""
    )

dfmEvtPortStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11438)
)
dfmEvtPortStatusUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtPortStatusUnknown.setStatus(
        ""
    )

dfmEvtPortRoleChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11439)
)
dfmEvtPortRoleChange.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtPortRoleChange.setStatus(
        ""
    )

dfmEvtLifStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11440)
)
dfmEvtLifStatusUp.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtLifStatusUp.setStatus(
        ""
    )

dfmEvtLifStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11441)
)
dfmEvtLifStatusDown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtLifStatusDown.setStatus(
        ""
    )

dfmEvtLifStatusUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11442)
)
dfmEvtLifStatusUnknown.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtLifStatusUnknown.setStatus(
        ""
    )

dfmEvtLifMigrated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11443)
)
dfmEvtLifMigrated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtLifMigrated.setStatus(
        ""
    )

dfmEvtSpaceManagementJobStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11451)
)
dfmEvtSpaceManagementJobStarted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtSpaceManagementJobStarted.setStatus(
        ""
    )

dfmEvtSpaceManagementJobSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11452)
)
dfmEvtSpaceManagementJobSucceeded.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtSpaceManagementJobSucceeded.setStatus(
        ""
    )

dfmEvtSpaceManagementJobFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11453)
)
dfmEvtSpaceManagementJobFailed.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtSpaceManagementJobFailed.setStatus(
        ""
    )

dfmEvtStorageServiceCreated = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11461)
)
dfmEvtStorageServiceCreated.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceCreated.setStatus(
        ""
    )

dfmEvtStorageServiceModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11462)
)
dfmEvtStorageServiceModified.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceModified.setStatus(
        ""
    )

dfmEvtStorageServiceDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11463)
)
dfmEvtStorageServiceDeleted.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceDeleted.setStatus(
        ""
    )

dfmEvtStorageServiceDatasetProvisioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11464)
)
dfmEvtStorageServiceDatasetProvisioned.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceDatasetProvisioned.setStatus(
        ""
    )

dfmEvtStorageServiceDatasetDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11465)
)
dfmEvtStorageServiceDatasetDetached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceDatasetDetached.setStatus(
        ""
    )

dfmEvtStorageServiceDatasetAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 789, 3, 0, 11466)
)
dfmEvtStorageServiceDatasetAttached.setObjects(
      *(("DATAFABRIC-MANAGER-MIB", "dfmSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceSerialNumber"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSeverity"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventTimestamp"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessage"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventMessageDetails"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceTable"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectType"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmObjectStatus"),
        ("DATAFABRIC-MANAGER-MIB", "dfmEventSourceProductId"),
        ("DATAFABRIC-MANAGER-MIB", "dfmHostFullName"),
        ("DATAFABRIC-MANAGER-MIB", "dfmCommentFields"))
)
if mibBuilder.loadTexts:
    dfmEvtStorageServiceDatasetAttached.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATAFABRIC-MANAGER-MIB",
    **{"DisplayString": DisplayString,
       "netappDataFabricManager": netappDataFabricManager,
       "dfmEvtSnapshotSpaceOk": dfmEvtSnapshotSpaceOk,
       "dfmEvtSnapshotFull": dfmEvtSnapshotFull,
       "dfmEvtVolumeSpaceOk": dfmEvtVolumeSpaceOk,
       "dfmEvtVolumeAlmostFull": dfmEvtVolumeAlmostFull,
       "dfmEvtVolumeFull": dfmEvtVolumeFull,
       "dfmEvtInodesUtilOk": dfmEvtInodesUtilOk,
       "dfmEvtInodesAlmostFull": dfmEvtInodesAlmostFull,
       "dfmEvtInodesFull": dfmEvtInodesFull,
       "dfmEvtMgmtStNodeLimitOk": dfmEvtMgmtStNodeLimitOk,
       "dfmEvtMgmtStNodeLimitNearlyReached": dfmEvtMgmtStNodeLimitNearlyReached,
       "dfmEvtMgmtStNodeLimitReached": dfmEvtMgmtStNodeLimitReached,
       "dfmEvtMgmtStPerfAdvisorFreeSpaceOk": dfmEvtMgmtStPerfAdvisorFreeSpaceOk,
       "dfmEvtMgmtStPerfAdvisorNotEnoughFreeSpace": dfmEvtMgmtStPerfAdvisorNotEnoughFreeSpace,
       "dfmEvtVolumeOnline": dfmEvtVolumeOnline,
       "dfmEvtVolumeOfflineOrDestroyed": dfmEvtVolumeOfflineOrDestroyed,
       "dfmEvtVolumeOffline": dfmEvtVolumeOffline,
       "dfmEvtVolumeDestroyed": dfmEvtVolumeDestroyed,
       "dfmEvtVolumeRestricted": dfmEvtVolumeRestricted,
       "dfmEvtMgmtStLicenseNotExpired": dfmEvtMgmtStLicenseNotExpired,
       "dfmEvtMgmtStLicenseNearlyExpired": dfmEvtMgmtStLicenseNearlyExpired,
       "dfmEvtMgmtStLicenseExpired": dfmEvtMgmtStLicenseExpired,
       "dfmEvtMgmtStSchedulerUp": dfmEvtMgmtStSchedulerUp,
       "dfmEvtMgmtStSchedulerDown": dfmEvtMgmtStSchedulerDown,
       "dfmEvtMgmtStDatabaseUp": dfmEvtMgmtStDatabaseUp,
       "dfmEvtMgmtStDatabaseDown": dfmEvtMgmtStDatabaseDown,
       "dfmEvtMgmtStMonitorUp": dfmEvtMgmtStMonitorUp,
       "dfmEvtMgmtStMonitorDown": dfmEvtMgmtStMonitorDown,
       "dfmEvtMgmtStEventdUp": dfmEvtMgmtStEventdUp,
       "dfmEvtMgmtStEventdDown": dfmEvtMgmtStEventdDown,
       "dfmEvtMgmtStWatchdogUp": dfmEvtMgmtStWatchdogUp,
       "dfmEvtMgmtStWatchdogDown": dfmEvtMgmtStWatchdogDown,
       "dfmEvtMgmtStServerUp": dfmEvtMgmtStServerUp,
       "dfmEvtMgmtStServerDown": dfmEvtMgmtStServerDown,
       "dfmEvtDisksSparesAvailable": dfmEvtDisksSparesAvailable,
       "dfmEvtDisksNoSpares": dfmEvtDisksNoSpares,
       "dfmEvtDisksNoneFailed": dfmEvtDisksNoneFailed,
       "dfmEvtDisksSomeFailed": dfmEvtDisksSomeFailed,
       "dfmEvtDisksReconstructNone": dfmEvtDisksReconstructNone,
       "dfmEvtDisksReconstructSome": dfmEvtDisksReconstructSome,
       "dfmEvtHostUp": dfmEvtHostUp,
       "dfmEvtHostDown": dfmEvtHostDown,
       "dfmEvtHostReachable": dfmEvtHostReachable,
       "dfmEvtHostUnreachable": dfmEvtHostUnreachable,
       "dfmEvtQtreeSpaceOk": dfmEvtQtreeSpaceOk,
       "dfmEvtQtreeAlmostFull": dfmEvtQtreeAlmostFull,
       "dfmEvtQtreeFull": dfmEvtQtreeFull,
       "dfmEvtQtreeFilesOk": dfmEvtQtreeFilesOk,
       "dfmEvtQtreeFilesAlmostFull": dfmEvtQtreeFilesAlmostFull,
       "dfmEvtQtreeFilesFull": dfmEvtQtreeFilesFull,
       "dfmEvtCpuUtilOk": dfmEvtCpuUtilOk,
       "dfmEvtCpuTooBusy": dfmEvtCpuTooBusy,
       "dfmEvtFansNormal": dfmEvtFansNormal,
       "dfmEvtFansOneFailed": dfmEvtFansOneFailed,
       "dfmEvtFansManyFailed": dfmEvtFansManyFailed,
       "dfmEvtPowerSupplyOk": dfmEvtPowerSupplyOk,
       "dfmEvtPowerSupplyOneFailed": dfmEvtPowerSupplyOneFailed,
       "dfmEvtPowerSupplyManyFailed": dfmEvtPowerSupplyManyFailed,
       "dfmEvtTemperatureOk": dfmEvtTemperatureOk,
       "dfmEvtTemperatureHot": dfmEvtTemperatureHot,
       "dfmEvtNvramBatteryOk": dfmEvtNvramBatteryOk,
       "dfmEvtNvramBatteryLow": dfmEvtNvramBatteryLow,
       "dfmEvtNvramBatteryDischarged": dfmEvtNvramBatteryDischarged,
       "dfmEvtNvramBatteryMissing": dfmEvtNvramBatteryMissing,
       "dfmEvtNvramBatteryOld": dfmEvtNvramBatteryOld,
       "dfmEvtNvramBatteryReplace": dfmEvtNvramBatteryReplace,
       "dfmEvtNvramBatteryUnknown": dfmEvtNvramBatteryUnknown,
       "dfmEvtNvramBatteryOverCharged": dfmEvtNvramBatteryOverCharged,
       "dfmEvtNvramBatteryFullyCharged": dfmEvtNvramBatteryFullyCharged,
       "dfmEvtGlobalStatusOther": dfmEvtGlobalStatusOther,
       "dfmEvtGlobalStatusUnknown": dfmEvtGlobalStatusUnknown,
       "dfmEvtGlobalStatusOk": dfmEvtGlobalStatusOk,
       "dfmEvtGlobalStatusNonCritical": dfmEvtGlobalStatusNonCritical,
       "dfmEvtGlobalStatusCritical": dfmEvtGlobalStatusCritical,
       "dfmEvtGlobalStatusNonRecoverable": dfmEvtGlobalStatusNonRecoverable,
       "dfmEvtSnapMirrorOff": dfmEvtSnapMirrorOff,
       "dfmEvtSnapMirrorWorking": dfmEvtSnapMirrorWorking,
       "dfmEvtSnapMirrorNotScheduled": dfmEvtSnapMirrorNotScheduled,
       "dfmEvtSnapMirrorPossibleProblem": dfmEvtSnapMirrorPossibleProblem,
       "dfmEvtSnapMirrorNotWorking": dfmEvtSnapMirrorNotWorking,
       "dfmEvtSnapMirrorUnknown": dfmEvtSnapMirrorUnknown,
       "dfmEvtCfoSettingsEnabled": dfmEvtCfoSettingsEnabled,
       "dfmEvtCfoSettingsNotConfigured": dfmEvtCfoSettingsNotConfigured,
       "dfmEvtCfoSettingsDisabled": dfmEvtCfoSettingsDisabled,
       "dfmEvtCfoSettingsTakeoverDisabled": dfmEvtCfoSettingsTakeoverDisabled,
       "dfmEvtCfoSettingsThisNodeDead": dfmEvtCfoSettingsThisNodeDead,
       "dfmEvtCfoThisFilerCanTakeover": dfmEvtCfoThisFilerCanTakeover,
       "dfmEvtCfoThisFilerCannotTakeover": dfmEvtCfoThisFilerCannotTakeover,
       "dfmEvtCfoThisFilerTakeover": dfmEvtCfoThisFilerTakeover,
       "dfmEvtCfoThisFilerDead": dfmEvtCfoThisFilerDead,
       "dfmEvtCfoPartnerOk": dfmEvtCfoPartnerOk,
       "dfmEvtCfoPartnerMayBeDown": dfmEvtCfoPartnerMayBeDown,
       "dfmEvtCfoPartnerDead": dfmEvtCfoPartnerDead,
       "dfmEvtCfoInterconnectUp": dfmEvtCfoInterconnectUp,
       "dfmEvtCfoInterconnectNotPresent": dfmEvtCfoInterconnectNotPresent,
       "dfmEvtCfoInterconnectDown": dfmEvtCfoInterconnectDown,
       "dfmEvtCfoInterconnectPartialFailure": dfmEvtCfoInterconnectPartialFailure,
       "dfmEvtSvdirDiscovered": dfmEvtSvdirDiscovered,
       "dfmEvtHostDiscovered": dfmEvtHostDiscovered,
       "dfmEvtHostSystemIdChanged": dfmEvtHostSystemIdChanged,
       "dfmEvtHostNameChanged": dfmEvtHostNameChanged,
       "dfmEvtOssvHostDiscovered": dfmEvtOssvHostDiscovered,
       "dfmEvtHostIdentityOk": dfmEvtHostIdentityOk,
       "dfmEvtHostIdentityConflict": dfmEvtHostIdentityConflict,
       "dfmEvtHostLoginOk": dfmEvtHostLoginOk,
       "dfmEvtHostLoginFailed": dfmEvtHostLoginFailed,
       "dfmEvtPrimaryHostDiscovered": dfmEvtPrimaryHostDiscovered,
       "dfmEvtMgmtStFreeSpaceOk": dfmEvtMgmtStFreeSpaceOk,
       "dfmEvtMgmtStNotEnoughFreeSpace": dfmEvtMgmtStNotEnoughFreeSpace,
       "dfmEvtMgmtStFileSystemFileSizeLimitReached": dfmEvtMgmtStFileSystemFileSizeLimitReached,
       "dfmEvtConfigFileChanged": dfmEvtConfigFileChanged,
       "dfmEvtConfigGroupChanged": dfmEvtConfigGroupChanged,
       "dfmEvtSnapMirrorDateOk": dfmEvtSnapMirrorDateOk,
       "dfmEvtSnapMirrorNearlyOutOfDate": dfmEvtSnapMirrorNearlyOutOfDate,
       "dfmEvtSnapMirrorOutOfDate": dfmEvtSnapMirrorOutOfDate,
       "dfmEvtSnapMirrorDeleted": dfmEvtSnapMirrorDeleted,
       "dfmEvtSnapMirrorUndeleted": dfmEvtSnapMirrorUndeleted,
       "dfmEvtSnapMirrorDiscovered": dfmEvtSnapMirrorDiscovered,
       "dfmEvtSnapMirrorModified": dfmEvtSnapMirrorModified,
       "dfmEvtNetworkOk": dfmEvtNetworkOk,
       "dfmEvtNetworkTooLarge": dfmEvtNetworkTooLarge,
       "dfmEvtUserDiskSpaceQuotaOk": dfmEvtUserDiskSpaceQuotaOk,
       "dfmEvtUserDiskSpaceQuotaAlmostFull": dfmEvtUserDiskSpaceQuotaAlmostFull,
       "dfmEvtUserDiskSpaceQuotaFull": dfmEvtUserDiskSpaceQuotaFull,
       "dfmEvtUserFilesQuotaOk": dfmEvtUserFilesQuotaOk,
       "dfmEvtUserFilesQuotaAlmostFull": dfmEvtUserFilesQuotaAlmostFull,
       "dfmEvtUserFilesQuotaFull": dfmEvtUserFilesQuotaFull,
       "dfmEvtLunOnline": dfmEvtLunOnline,
       "dfmEvtLunOffline": dfmEvtLunOffline,
       "dfmEvtLunSnapshotOk": dfmEvtLunSnapshotOk,
       "dfmEvtLunSnapshotNotPossible": dfmEvtLunSnapshotNotPossible,
       "dfmEvtLunHostClusterConfigOk": dfmEvtLunHostClusterConfigOk,
       "dfmEvtLunHostClusterConfigError": dfmEvtLunHostClusterConfigError,
       "dfmEvtUserEmailAddressRejected": dfmEvtUserEmailAddressRejected,
       "dfmEvtUserEmailAddressOk": dfmEvtUserEmailAddressOk,
       "dfmEvtFCSwitchPortFaulty": dfmEvtFCSwitchPortFaulty,
       "dfmEvtFCSwitchPortOffline": dfmEvtFCSwitchPortOffline,
       "dfmEvtFCSwitchPortOnline": dfmEvtFCSwitchPortOnline,
       "dfmEvtSnapvaultRelationshipCreated": dfmEvtSnapvaultRelationshipCreated,
       "dfmEvtSnapvaultRelationshipDeleted": dfmEvtSnapvaultRelationshipDeleted,
       "dfmEvtSnapvaultRelationshipModified": dfmEvtSnapvaultRelationshipModified,
       "dfmEvtSnapvaultReplicaDateOk": dfmEvtSnapvaultReplicaDateOk,
       "dfmEvtSnapvaultReplicaNearlyOutOfDate": dfmEvtSnapvaultReplicaNearlyOutOfDate,
       "dfmEvtSnapvaultReplicaOutOfDate": dfmEvtSnapvaultReplicaOutOfDate,
       "dfmEvtSnapvaultBackupCompleted": dfmEvtSnapvaultBackupCompleted,
       "dfmEvtSnapvaultBackupAborted": dfmEvtSnapvaultBackupAborted,
       "dfmEvtSnapvaultBackupFailed": dfmEvtSnapvaultBackupFailed,
       "dfmEvtSnapvaultRestoreCompleted": dfmEvtSnapvaultRestoreCompleted,
       "dfmEvtSnapvaultRestoreAborted": dfmEvtSnapvaultRestoreAborted,
       "dfmEvtSnapvaultRestoreFailed": dfmEvtSnapvaultRestoreFailed,
       "dfmEvtSnapvaultRelationshipDiscovered": dfmEvtSnapvaultRelationshipDiscovered,
       "dfmEvtSnapvaultRelationshipCreateFailed": dfmEvtSnapvaultRelationshipCreateFailed,
       "dfmEvtSnapvaultRelationshipCreateAborted": dfmEvtSnapvaultRelationshipCreateAborted,
       "dfmEvtSnapvaultRelationshipDeleteFailed": dfmEvtSnapvaultRelationshipDeleteFailed,
       "dfmEvtSnapvaultRelationshipDeleteAborted": dfmEvtSnapvaultRelationshipDeleteAborted,
       "dfmEvtTestAlarm": dfmEvtTestAlarm,
       "dfmEvtUserDiskSpaceSoftLimitNotExceeded": dfmEvtUserDiskSpaceSoftLimitNotExceeded,
       "dfmEvtUserDiskSpaceSoftLimitExceeded": dfmEvtUserDiskSpaceSoftLimitExceeded,
       "dfmEvtUserFilesSoftLimitNotExceeded": dfmEvtUserFilesSoftLimitNotExceeded,
       "dfmEvtUserFilesSoftLimitExceeded": dfmEvtUserFilesSoftLimitExceeded,
       "dfmEvtHbaPortOnline": dfmEvtHbaPortOnline,
       "dfmEvtHbaPortOffline": dfmEvtHbaPortOffline,
       "dfmEvtHbaPortError": dfmEvtHbaPortError,
       "dfmEvtSanHostLunChanged": dfmEvtSanHostLunChanged,
       "dfmEvtHostAgentUp": dfmEvtHostAgentUp,
       "dfmEvtHostAgentDown": dfmEvtHostAgentDown,
       "dfmEvtHbaPortTrafficHigh": dfmEvtHbaPortTrafficHigh,
       "dfmEvtHbaPortTrafficOk": dfmEvtHbaPortTrafficOk,
       "dfmEvtSnapMirrorInSync": dfmEvtSnapMirrorInSync,
       "dfmEvtSnapMirrorOutOfSync": dfmEvtSnapMirrorOutOfSync,
       "dfmEvtSnapMirrorInitCompleted": dfmEvtSnapMirrorInitCompleted,
       "dfmEvtSnapMirrorInitAborted": dfmEvtSnapMirrorInitAborted,
       "dfmEvtSnapMirrorInitFailed": dfmEvtSnapMirrorInitFailed,
       "dfmEvtSnapMirrorUpdateCompleted": dfmEvtSnapMirrorUpdateCompleted,
       "dfmEvtSnapMirrorUpdateAborted": dfmEvtSnapMirrorUpdateAborted,
       "dfmEvtSnapMirrorUpdateFailed": dfmEvtSnapMirrorUpdateFailed,
       "dfmEvtSnapMirrorBreakCompleted": dfmEvtSnapMirrorBreakCompleted,
       "dfmEvtSnapMirrorBreakFailed": dfmEvtSnapMirrorBreakFailed,
       "dfmEvtSnapMirrorResyncCompleted": dfmEvtSnapMirrorResyncCompleted,
       "dfmEvtSnapMirrorResyncAborted": dfmEvtSnapMirrorResyncAborted,
       "dfmEvtSnapMirrorResyncFailed": dfmEvtSnapMirrorResyncFailed,
       "dfmEvtSnapMirrorQuiesceCompleted": dfmEvtSnapMirrorQuiesceCompleted,
       "dfmEvtSnapMirrorQuiesceAborted": dfmEvtSnapMirrorQuiesceAborted,
       "dfmEvtSnapMirrorQuiesceFailed": dfmEvtSnapMirrorQuiesceFailed,
       "dfmEvtSnapMirrorResumeCompleted": dfmEvtSnapMirrorResumeCompleted,
       "dfmEvtSnapMirrorResumeFailed": dfmEvtSnapMirrorResumeFailed,
       "dfmEvtSnapMirrorAbortCompleted": dfmEvtSnapMirrorAbortCompleted,
       "dfmEvtSnapMirrorAbortFailed": dfmEvtSnapMirrorAbortFailed,
       "dfmEvtSnapMirrorDeleteCompleted": dfmEvtSnapMirrorDeleteCompleted,
       "dfmEvtSnapMirrorDeleteFailed": dfmEvtSnapMirrorDeleteFailed,
       "dfmEvtSnapMirrorDeleteAborted": dfmEvtSnapMirrorDeleteAborted,
       "dfmEvtMgmtStLoadOk": dfmEvtMgmtStLoadOk,
       "dfmEvtMgmtStLoadTooHigh": dfmEvtMgmtStLoadTooHigh,
       "dfmEvtHostSnmpUp": dfmEvtHostSnmpUp,
       "dfmEvtHostSnmpDown": dfmEvtHostSnmpDown,
       "dfmEvtEnvEnclOk": dfmEvtEnvEnclOk,
       "dfmEvtEnvEnclFailed": dfmEvtEnvEnclFailed,
       "dfmEvtEnvEnclFound": dfmEvtEnvEnclFound,
       "dfmEvtEnvEnclDissapeared": dfmEvtEnvEnclDissapeared,
       "dfmEvtEnvEnclInactive": dfmEvtEnvEnclInactive,
       "dfmEvtEnvEnclActive": dfmEvtEnvEnclActive,
       "dfmEvtAggregateSpaceOk": dfmEvtAggregateSpaceOk,
       "dfmEvtAggregateAlmostFull": dfmEvtAggregateAlmostFull,
       "dfmEvtAggregateFull": dfmEvtAggregateFull,
       "dfmEvtAggregateOvercommitOk": dfmEvtAggregateOvercommitOk,
       "dfmEvtAggregateAlmostOvercommitted": dfmEvtAggregateAlmostOvercommitted,
       "dfmEvtAggregateOvercommitted": dfmEvtAggregateOvercommitted,
       "dfmEvtVolumeCloneDiscovered": dfmEvtVolumeCloneDiscovered,
       "dfmEvtVolumeCloneDeleted": dfmEvtVolumeCloneDeleted,
       "dfmEvtAggregateDiscovered": dfmEvtAggregateDiscovered,
       "dfmEvtAggregateDeleted": dfmEvtAggregateDeleted,
       "dfmEvtTrapListenerFailed": dfmEvtTrapListenerFailed,
       "dfmEvtTrapListenerOk": dfmEvtTrapListenerOk,
       "dfmEvtHostColdStart": dfmEvtHostColdStart,
       "dfmEvtEmergencyTrap": dfmEvtEmergencyTrap,
       "dfmEvtAlertTrap": dfmEvtAlertTrap,
       "dfmEvtCriticalTrap": dfmEvtCriticalTrap,
       "dfmEvtErrorTrap": dfmEvtErrorTrap,
       "dfmEvtWarningTrap": dfmEvtWarningTrap,
       "dfmEvtNotificationTrap": dfmEvtNotificationTrap,
       "dfmEvtInformationTrap": dfmEvtInformationTrap,
       "dfmEvtIfAdminStatusUp": dfmEvtIfAdminStatusUp,
       "dfmEvtIfAdminStatusDown": dfmEvtIfAdminStatusDown,
       "dfmEvtIfAdminStatusTesting": dfmEvtIfAdminStatusTesting,
       "dfmEvtIfAdminStatusUnknown": dfmEvtIfAdminStatusUnknown,
       "dfmEvtScriptEmergency": dfmEvtScriptEmergency,
       "dfmEvtScriptCritical": dfmEvtScriptCritical,
       "dfmEvtScriptError": dfmEvtScriptError,
       "dfmEvtScriptWarning": dfmEvtScriptWarning,
       "dfmEvtScriptInformation": dfmEvtScriptInformation,
       "dfmEvtScriptNormal": dfmEvtScriptNormal,
       "dfmEvtScriptScheduleEnabled": dfmEvtScriptScheduleEnabled,
       "dfmEvtScriptScheduleDisabled": dfmEvtScriptScheduleDisabled,
       "dfmEvtAggrSnapReserveOk": dfmEvtAggrSnapReserveOk,
       "dfmEvtAggrSnapReserveNearlyFull": dfmEvtAggrSnapReserveNearlyFull,
       "dfmEvtAggrSnapReserveFull": dfmEvtAggrSnapReserveFull,
       "dfmEvtVolumeSpaceReserveOk": dfmEvtVolumeSpaceReserveOk,
       "dfmEvtVolumeSpaceReserveNearlyFull": dfmEvtVolumeSpaceReserveNearlyFull,
       "dfmEvtVolumeSpaceReserveFull": dfmEvtVolumeSpaceReserveFull,
       "dfmEvtVolumeFirstSnapOk": dfmEvtVolumeFirstSnapOk,
       "dfmEvtVolumeNearlyNoFirstSnap": dfmEvtVolumeNearlyNoFirstSnap,
       "dfmEvtVolumeNoFirstSnap": dfmEvtVolumeNoFirstSnap,
       "dfmEvtVolumeNewSnapshot": dfmEvtVolumeNewSnapshot,
       "dfmEvtVolumeSnapshotDeleted": dfmEvtVolumeSnapshotDeleted,
       "dfmEvtLocalFilerConfigStatusOk": dfmEvtLocalFilerConfigStatusOk,
       "dfmEvtLocalFilerConfigStatusChanged": dfmEvtLocalFilerConfigStatusChanged,
       "dfmEvtFilerLoginOk": dfmEvtFilerLoginOk,
       "dfmEvtFilerLoginFailed": dfmEvtFilerLoginFailed,
       "dfmEvtNdmpStatusUp": dfmEvtNdmpStatusUp,
       "dfmEvtNdmpStatusDown": dfmEvtNdmpStatusDown,
       "dfmEvtFilerConfigPushStatusOk": dfmEvtFilerConfigPushStatusOk,
       "dfmEvtFilerConfigPushStatusError": dfmEvtFilerConfigPushStatusError,
       "dfmEvtVfilerDiscovered": dfmEvtVfilerDiscovered,
       "dfmEvtVfilerDeleted": dfmEvtVfilerDeleted,
       "dfmEvtVfilerRenamed": dfmEvtVfilerRenamed,
       "dfmEvtVfilerStorageUnitAdded": dfmEvtVfilerStorageUnitAdded,
       "dfmEvtVfilerStorageUnitRemoved": dfmEvtVfilerStorageUnitRemoved,
       "dfmEvtVfilerIpAddressAdded": dfmEvtVfilerIpAddressAdded,
       "dfmEvtVfilerIpAddressRemoved": dfmEvtVfilerIpAddressRemoved,
       "dfmEvtVfilerHostingFilerLoginOk": dfmEvtVfilerHostingFilerLoginOk,
       "dfmEvtVfilerHostingFilerLoginFailed": dfmEvtVfilerHostingFilerLoginFailed,
       "dfmEvtVolumeGrowthRateAbnormal": dfmEvtVolumeGrowthRateAbnormal,
       "dfmEvtVolumeGrowthRateOk": dfmEvtVolumeGrowthRateOk,
       "dfmEvtQtreeGrowthRateAbnormal": dfmEvtQtreeGrowthRateAbnormal,
       "dfmEvtQtreeGrowthRateOk": dfmEvtQtreeGrowthRateOk,
       "dfmEvtSnapSchedModified": dfmEvtSnapSchedModified,
       "dfmEvtSnapSchedSmConflict": dfmEvtSnapSchedSmConflict,
       "dfmEvtSnapSchedSmOk": dfmEvtSnapSchedSmOk,
       "dfmEvtSnapSchedSvConflict": dfmEvtSnapSchedSvConflict,
       "dfmEvtSnapSchedSvOk": dfmEvtSnapSchedSvOk,
       "dfmEvtTooManySnapshots": dfmEvtTooManySnapshots,
       "dfmEvtNotTooManySnapshots": dfmEvtNotTooManySnapshots,
       "dfmEvtSnapDisabled": dfmEvtSnapDisabled,
       "dfmEvtSnapEnabled": dfmEvtSnapEnabled,
       "dfmEvtDatabaseBackupSucceeded": dfmEvtDatabaseBackupSucceeded,
       "dfmEvtDatabaseBackupFailed": dfmEvtDatabaseBackupFailed,
       "dfmEvtDatabaseRestoreSucceeded": dfmEvtDatabaseRestoreSucceeded,
       "dfmEvtDatabaseRestoreFailed": dfmEvtDatabaseRestoreFailed,
       "dfmEvtMaxdirsizeReached": dfmEvtMaxdirsizeReached,
       "dfmEvtMaxdirsizeNearlyReached": dfmEvtMaxdirsizeNearlyReached,
       "dfmEvtSnapTooOld": dfmEvtSnapTooOld,
       "dfmEvtSnapNotTooOld": dfmEvtSnapNotTooOld,
       "dfmEvtRpmOnline": dfmEvtRpmOnline,
       "dfmEvtRpmUnavailable": dfmEvtRpmUnavailable,
       "dfmEvtAggregateStateFailed": dfmEvtAggregateStateFailed,
       "dfmEvtAggregateStateOnline": dfmEvtAggregateStateOnline,
       "dfmEvtAggregateStateOffline": dfmEvtAggregateStateOffline,
       "dfmEvtAggregateStateRestricted": dfmEvtAggregateStateRestricted,
       "dfmEvtDatasetCreated": dfmEvtDatasetCreated,
       "dfmEvtDatasetDeleted": dfmEvtDatasetDeleted,
       "dfmEvtDatasetModified": dfmEvtDatasetModified,
       "dfmEvtSnapshotCreated": dfmEvtSnapshotCreated,
       "dfmEvtSnapshotFailed": dfmEvtSnapshotFailed,
       "dfmEvtDatasetProvisioningOk": dfmEvtDatasetProvisioningOk,
       "dfmEvtDatasetProvisioningFailed": dfmEvtDatasetProvisioningFailed,
       "dfmEvtDatasetProtectionProtected": dfmEvtDatasetProtectionProtected,
       "dfmEvtDatasetProtectionFailure": dfmEvtDatasetProtectionFailure,
       "dfmEvtDatasetProtectionSuspended": dfmEvtDatasetProtectionSuspended,
       "dfmEvtDatasetProtectionLagError": dfmEvtDatasetProtectionLagError,
       "dfmEvtDatasetProtectionLagWarning": dfmEvtDatasetProtectionLagWarning,
       "dfmEvtDatasetProtectionUninitialized": dfmEvtDatasetProtectionUninitialized,
       "dfmEvtDatasetConformant": dfmEvtDatasetConformant,
       "dfmEvtDatasetConforming": dfmEvtDatasetConforming,
       "dfmEvtDatasetNonConformant": dfmEvtDatasetNonConformant,
       "dfmEvtDatasetCloneSnapshotFound": dfmEvtDatasetCloneSnapshotFound,
       "dfmEvtDatasetNoCloneSnapshotFound": dfmEvtDatasetNoCloneSnapshotFound,
       "dfmEvtDatasetWriteCheckWarning": dfmEvtDatasetWriteCheckWarning,
       "dfmEvtDatasetWriteCheckOk": dfmEvtDatasetWriteCheckOk,
       "dfmEvtResourcePoolCreated": dfmEvtResourcePoolCreated,
       "dfmEvtResourcePoolDeleted": dfmEvtResourcePoolDeleted,
       "dfmEvtResourcePoolModified": dfmEvtResourcePoolModified,
       "dfmEvtResourcePoolSpaceOk": dfmEvtResourcePoolSpaceOk,
       "dfmEvtResourcePoolSpaceNearlyFull": dfmEvtResourcePoolSpaceNearlyFull,
       "dfmEvtResourcePoolSpaceFull": dfmEvtResourcePoolSpaceFull,
       "dfmEvtDataProtectionPolicyCreated": dfmEvtDataProtectionPolicyCreated,
       "dfmEvtDataProtectionPolicyDeleted": dfmEvtDataProtectionPolicyDeleted,
       "dfmEvtDataProtectionPolicyModified": dfmEvtDataProtectionPolicyModified,
       "dfmEvtDataProtectionScheduleCreated": dfmEvtDataProtectionScheduleCreated,
       "dfmEvtDataProtectionScheduleDeleted": dfmEvtDataProtectionScheduleDeleted,
       "dfmEvtDataProtectionScheduleModified": dfmEvtDataProtectionScheduleModified,
       "dfmEvtNdmpCredentialsGood": dfmEvtNdmpCredentialsGood,
       "dfmEvtNdmpCredentialsBad": dfmEvtNdmpCredentialsBad,
       "dfmEvtDataProtectionJobStarted": dfmEvtDataProtectionJobStarted,
       "dfmEvtHostDeleted": dfmEvtHostDeleted,
       "dfmEvtHostModified": dfmEvtHostModified,
       "dfmEvtResourceGroupCreated": dfmEvtResourceGroupCreated,
       "dfmEvtResourceGroupDeleted": dfmEvtResourceGroupDeleted,
       "dfmEvtResourceGroupModified": dfmEvtResourceGroupModified,
       "dfmEvtAlarmCreated": dfmEvtAlarmCreated,
       "dfmEvtAlarmDeleted": dfmEvtAlarmDeleted,
       "dfmEvtAlarmModified": dfmEvtAlarmModified,
       "dfmEvtNdmpCommunicationUp": dfmEvtNdmpCommunicationUp,
       "dfmEvtNdmpCommunicationDown": dfmEvtNdmpCommunicationDown,
       "dfmEvtDatasetBackupCompleted": dfmEvtDatasetBackupCompleted,
       "dfmEvtDatasetBackupAborted": dfmEvtDatasetBackupAborted,
       "dfmEvtDatasetBackupFailed": dfmEvtDatasetBackupFailed,
       "dfmEvtFilerCommunicationOk": dfmEvtFilerCommunicationOk,
       "dfmEvtFilerCommunicationFailed": dfmEvtFilerCommunicationFailed,
       "dfmEvtLocalVfilerConfigStatusOk": dfmEvtLocalVfilerConfigStatusOk,
       "dfmEvtLocalVfilerConfigStatusChanged": dfmEvtLocalVfilerConfigStatusChanged,
       "dfmEvtVfilerConfigPushStatusOk": dfmEvtVfilerConfigPushStatusOk,
       "dfmEvtVfilerConfigPushStatusError": dfmEvtVfilerConfigPushStatusError,
       "dfmEvtScheduledReportOk": dfmEvtScheduledReportOk,
       "dfmEvtScheduledReportFailed": dfmEvtScheduledReportFailed,
       "dfmEvtReportScheduleEnabled": dfmEvtReportScheduleEnabled,
       "dfmEvtReportScheduleDisabled": dfmEvtReportScheduleDisabled,
       "dfmEvtHostRoleDiscovered": dfmEvtHostRoleDiscovered,
       "dfmEvtHostRoleDeleted": dfmEvtHostRoleDeleted,
       "dfmEvtHostRoleModified": dfmEvtHostRoleModified,
       "dfmEvtHostUsergroupDiscovered": dfmEvtHostUsergroupDiscovered,
       "dfmEvtHostUsergroupDeleted": dfmEvtHostUsergroupDeleted,
       "dfmEvtHostUsergroupModified": dfmEvtHostUsergroupModified,
       "dfmEvtHostUserDiscovered": dfmEvtHostUserDiscovered,
       "dfmEvtHostUserDeleted": dfmEvtHostUserDeleted,
       "dfmEvtHostUserModified": dfmEvtHostUserModified,
       "dfmEvtHostDomainUserModified": dfmEvtHostDomainUserModified,
       "dfmEvtVolumeQuotaOvercommitOk": dfmEvtVolumeQuotaOvercommitOk,
       "dfmEvtVolumeQuotaAlmostOvercommitted": dfmEvtVolumeQuotaAlmostOvercommitted,
       "dfmEvtVolumeQuotaOvercommitted": dfmEvtVolumeQuotaOvercommitted,
       "dfmEvtDataExportOk": dfmEvtDataExportOk,
       "dfmEvtDataExportFailed": dfmEvtDataExportFailed,
       "dfmEvtDatasetMemberResized": dfmEvtDatasetMemberResized,
       "dfmEvtDatasetMemberResizeFailed": dfmEvtDatasetMemberResizeFailed,
       "dfmEvtProvisioningPolicyCreated": dfmEvtProvisioningPolicyCreated,
       "dfmEvtProvisioningPolicyDeleted": dfmEvtProvisioningPolicyDeleted,
       "dfmEvtProvisioningPolicyModified": dfmEvtProvisioningPolicyModified,
       "dfmEvtVFilerTemplateCreated": dfmEvtVFilerTemplateCreated,
       "dfmEvtVFilerTemplateDeleted": dfmEvtVFilerTemplateDeleted,
       "dfmEvtVFilerTemplateModified": dfmEvtVFilerTemplateModified,
       "dfmEvtDatasetSpaceOk": dfmEvtDatasetSpaceOk,
       "dfmEvtDatasetSpaceWarning": dfmEvtDatasetSpaceWarning,
       "dfmEvtDatasetSpaceError": dfmEvtDatasetSpaceError,
       "dfmEvtVolumeAutosized": dfmEvtVolumeAutosized,
       "dfmEvtVolumeSnapshotsAutoDeleted": dfmEvtVolumeSnapshotsAutoDeleted,
       "dfmEvtVolumeNextSnapshotNotPossible": dfmEvtVolumeNextSnapshotNotPossible,
       "dfmEvtVolumeNextSnapshotPossible": dfmEvtVolumeNextSnapshotPossible,
       "dfmEvtDatasetMemberDestroyed": dfmEvtDatasetMemberDestroyed,
       "dfmEvtDatasetMemberDestroyFailed": dfmEvtDatasetMemberDestroyFailed,
       "dfmEvtMgmtStProvMgrNodeLimitOk": dfmEvtMgmtStProvMgrNodeLimitOk,
       "dfmEvtMgmtStProvMgrNodeLimitNearlyReached": dfmEvtMgmtStProvMgrNodeLimitNearlyReached,
       "dfmEvtMgmtStProvMgrNodeLimitReached": dfmEvtMgmtStProvMgrNodeLimitReached,
       "dfmEvtMgmtStProtMgrNodeLimitOk": dfmEvtMgmtStProtMgrNodeLimitOk,
       "dfmEvtMgmtStProtMgrNodeLimitNearlyReached": dfmEvtMgmtStProtMgrNodeLimitNearlyReached,
       "dfmEvtMgmtStProtMgrNodeLimitReached": dfmEvtMgmtStProtMgrNodeLimitReached,
       "dfmEvtDatasetNotMigrating": dfmEvtDatasetNotMigrating,
       "dfmEvtDatasetMigrating": dfmEvtDatasetMigrating,
       "dfmEvtDatasetMigrateFailed": dfmEvtDatasetMigrateFailed,
       "dfmEvtDatasetMigratedWithErrors": dfmEvtDatasetMigratedWithErrors,
       "dfmEvtDatasetMigrated": dfmEvtDatasetMigrated,
       "dfmEvtDatasetRollbackWithErrors": dfmEvtDatasetRollbackWithErrors,
       "dfmEvtDatasetRollback": dfmEvtDatasetRollback,
       "dfmEvtVfilerNotMigrating": dfmEvtVfilerNotMigrating,
       "dfmEvtVfilerMigrating": dfmEvtVfilerMigrating,
       "dfmEvtVfilerMigrateFailed": dfmEvtVfilerMigrateFailed,
       "dfmEvtVfilerMigratedWithErrors": dfmEvtVfilerMigratedWithErrors,
       "dfmEvtVfilerMigrated": dfmEvtVfilerMigrated,
       "dfmEvtVolumeOverDeduplicated": dfmEvtVolumeOverDeduplicated,
       "dfmEvtVfilerRollbackWithErrors": dfmEvtVfilerRollbackWithErrors,
       "dfmEvtVfilerRollback": dfmEvtVfilerRollback,
       "dfmEvtVolumeNearlyOverDeduplicated": dfmEvtVolumeNearlyOverDeduplicated,
       "dfmEvtVolumeNotOverDeduplicated": dfmEvtVolumeNotOverDeduplicated,
       "dfmEvtAggregateOverDeduplicated": dfmEvtAggregateOverDeduplicated,
       "dfmEvtAggregateNearlyOverDeduplicated": dfmEvtAggregateNearlyOverDeduplicated,
       "dfmEvtAggregateNotOverDeduplicated": dfmEvtAggregateNotOverDeduplicated,
       "dfmEvtDatasetMemberDeduplicated": dfmEvtDatasetMemberDeduplicated,
       "dfmEvtDatasetMemberDeduplicationFailed": dfmEvtDatasetMemberDeduplicationFailed,
       "dfmEvtDatasetMemberUndeduplicated": dfmEvtDatasetMemberUndeduplicated,
       "dfmEvtDatasetMemberUndeduplicationFailed": dfmEvtDatasetMemberUndeduplicationFailed,
       "dfmEvtHostNfsServiceStatusUp": dfmEvtHostNfsServiceStatusUp,
       "dfmEvtHostNfsServiceStatusDown": dfmEvtHostNfsServiceStatusDown,
       "dfmEvtHostCifsServiceStatusUp": dfmEvtHostCifsServiceStatusUp,
       "dfmEvtHostCifsServiceStatusDown": dfmEvtHostCifsServiceStatusDown,
       "dfmEvtHostIscsiServiceStatusUp": dfmEvtHostIscsiServiceStatusUp,
       "dfmEvtHostIscsiServiceStatusDown": dfmEvtHostIscsiServiceStatusDown,
       "dfmEvtHostFcpServiceStatusUp": dfmEvtHostFcpServiceStatusUp,
       "dfmEvtHostFcpServiceStatusDown": dfmEvtHostFcpServiceStatusDown,
       "dfmEvtCommentFieldCreated": dfmEvtCommentFieldCreated,
       "dfmEvtCommentFieldModified": dfmEvtCommentFieldModified,
       "dfmEvtCommentFieldDestroyed": dfmEvtCommentFieldDestroyed,
       "dfmEvtNfsPerClientStatsEnabled": dfmEvtNfsPerClientStatsEnabled,
       "dfmEvtNfsPerClientStatsDisabled": dfmEvtNfsPerClientStatsDisabled,
       "dfmEvtCifsPerClientStatsEnabled": dfmEvtCifsPerClientStatsEnabled,
       "dfmEvtCifsPerClientStatsDisabled": dfmEvtCifsPerClientStatsDisabled,
       "dfmEvtDatasetDrStateReady": dfmEvtDatasetDrStateReady,
       "dfmEvtDatasetDrStateFailingOver": dfmEvtDatasetDrStateFailingOver,
       "dfmEvtDatasetDrStateFailedOver": dfmEvtDatasetDrStateFailedOver,
       "dfmEvtDatasetDrStateFailoverError": dfmEvtDatasetDrStateFailoverError,
       "dfmEvtDatasetDrStatusNormal": dfmEvtDatasetDrStatusNormal,
       "dfmEvtDatasetDrStatusWarning": dfmEvtDatasetDrStatusWarning,
       "dfmEvtDatasetDrStatusError": dfmEvtDatasetDrStatusError,
       "dfmEvtVserverDiscovered": dfmEvtVserverDiscovered,
       "dfmEvtVserverDeleted": dfmEvtVserverDeleted,
       "dfmEvtVserverRenamed": dfmEvtVserverRenamed,
       "dfmEvtClusterDiscovered": dfmEvtClusterDiscovered,
       "dfmEvtClusterRenamed": dfmEvtClusterRenamed,
       "dfmEvtClusterNodeAdded": dfmEvtClusterNodeAdded,
       "dfmEvtClusterNodeRemoved": dfmEvtClusterNodeRemoved,
       "dfmEvtPortStatusUndef": dfmEvtPortStatusUndef,
       "dfmEvtPortStatusUp": dfmEvtPortStatusUp,
       "dfmEvtPortStatusDown": dfmEvtPortStatusDown,
       "dfmEvtPortStatusUnknown": dfmEvtPortStatusUnknown,
       "dfmEvtPortRoleChange": dfmEvtPortRoleChange,
       "dfmEvtLifStatusUp": dfmEvtLifStatusUp,
       "dfmEvtLifStatusDown": dfmEvtLifStatusDown,
       "dfmEvtLifStatusUnknown": dfmEvtLifStatusUnknown,
       "dfmEvtLifMigrated": dfmEvtLifMigrated,
       "dfmEvtSpaceManagementJobStarted": dfmEvtSpaceManagementJobStarted,
       "dfmEvtSpaceManagementJobSucceeded": dfmEvtSpaceManagementJobSucceeded,
       "dfmEvtSpaceManagementJobFailed": dfmEvtSpaceManagementJobFailed,
       "dfmEvtStorageServiceCreated": dfmEvtStorageServiceCreated,
       "dfmEvtStorageServiceModified": dfmEvtStorageServiceModified,
       "dfmEvtStorageServiceDeleted": dfmEvtStorageServiceDeleted,
       "dfmEvtStorageServiceDatasetProvisioned": dfmEvtStorageServiceDatasetProvisioned,
       "dfmEvtStorageServiceDatasetDetached": dfmEvtStorageServiceDatasetDetached,
       "dfmEvtStorageServiceDatasetAttached": dfmEvtStorageServiceDatasetAttached,
       "dfmSerialNumber": dfmSerialNumber,
       "dfmEventTable": dfmEventTable,
       "dfmEventEntry": dfmEventEntry,
       "dfmEventId": dfmEventId,
       "dfmEventSourceId": dfmEventSourceId,
       "dfmEventSeverity": dfmEventSeverity,
       "dfmEventTimestamp": dfmEventTimestamp,
       "dfmEventName": dfmEventName,
       "dfmEventMessage": dfmEventMessage,
       "dfmEventMessageDetails": dfmEventMessageDetails,
       "dfmEventSourceTable": dfmEventSourceTable,
       "dfmEventSourceSerialNumber": dfmEventSourceSerialNumber,
       "dfmEventSourceProductId": dfmEventSourceProductId,
       "dfmObjectTable": dfmObjectTable,
       "dfmObjectEntry": dfmObjectEntry,
       "dfmObjectId": dfmObjectId,
       "dfmObjectFullName": dfmObjectFullName,
       "dfmObjectType": dfmObjectType,
       "dfmObjectStatus": dfmObjectStatus,
       "dfmHostFullName": dfmHostFullName,
       "dfmCommentFields": dfmCommentFields,
       "dfmPhysicalHostId": dfmPhysicalHostId,
       "dfmPhysicalHostFullName": dfmPhysicalHostFullName}
)
