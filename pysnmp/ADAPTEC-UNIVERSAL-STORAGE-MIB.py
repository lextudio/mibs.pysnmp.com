# SNMP MIB module (ADAPTEC-UNIVERSAL-STORAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADAPTEC-UNIVERSAL-STORAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:41 2024
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



class TriState(Integer32):
    """Custom type TriState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 3),
          ("unknown", 1))
    )





class ObjectStatus(Integer32):
    """Custom type ObjectStatus based on Integer32"""
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
        *(("failure", 5),
          ("okay", 3),
          ("other", 2),
          ("unknown", 1),
          ("warning", 4))
    )





class OptionStatus(Integer32):
    """Custom type OptionStatus based on Integer32"""
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
        *(("installedAndActive", 6),
          ("installedAndInactive", 5),
          ("notApplicable", 3),
          ("notInstalled", 4),
          ("other", 2),
          ("unknown", 1))
    )





class BatteryStatus(Integer32):
    """Custom type BatteryStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("charging", 7),
          ("discharging", 8),
          ("failed", 6),
          ("inMaintenanceMode", 9),
          ("notApplicable", 3),
          ("notInstalled", 4),
          ("okay", 5),
          ("other", 2),
          ("unknown", 1))
    )





class IndexList(DisplayString):
    """Custom type IndexList based on DisplayString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adaptec_ObjectIdentity = ObjectIdentity
adaptec = _Adaptec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795)
)
_UniversalStorage_ObjectIdentity = ObjectIdentity
universalStorage = _UniversalStorage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14)
)
_AusMIB_ObjectIdentity = ObjectIdentity
ausMIB = _AusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1)
)
_AusMibStatus_ObjectIdentity = ObjectIdentity
ausMibStatus = _AusMibStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100)
)
_AusMibStatusRevMajor_Type = Integer32
_AusMibStatusRevMajor_Object = MibScalar
ausMibStatusRevMajor = _AusMibStatusRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100, 1),
    _AusMibStatusRevMajor_Type()
)
ausMibStatusRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausMibStatusRevMajor.setStatus("mandatory")
_AusMibStatusRevMinor_Type = Integer32
_AusMibStatusRevMinor_Object = MibScalar
ausMibStatusRevMinor = _AusMibStatusRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100, 2),
    _AusMibStatusRevMinor_Type()
)
ausMibStatusRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausMibStatusRevMinor.setStatus("mandatory")
_AusMibStatusSecondsSinceInitiation_Type = Integer32
_AusMibStatusSecondsSinceInitiation_Object = MibScalar
ausMibStatusSecondsSinceInitiation = _AusMibStatusSecondsSinceInitiation_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100, 3),
    _AusMibStatusSecondsSinceInitiation_Type()
)
ausMibStatusSecondsSinceInitiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausMibStatusSecondsSinceInitiation.setStatus("mandatory")
_AusMibStatusCopyright_Type = DisplayString
_AusMibStatusCopyright_Object = MibScalar
ausMibStatusCopyright = _AusMibStatusCopyright_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100, 4),
    _AusMibStatusCopyright_Type()
)
ausMibStatusCopyright.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausMibStatusCopyright.setStatus("mandatory")
_AusMibStatusOverall_Type = ObjectStatus
_AusMibStatusOverall_Object = MibScalar
ausMibStatusOverall = _AusMibStatusOverall_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 100, 5),
    _AusMibStatusOverall_Type()
)
ausMibStatusOverall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausMibStatusOverall.setStatus("mandatory")
_AusAggregatedController_ObjectIdentity = ObjectIdentity
ausAggregatedController = _AusAggregatedController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 200)
)
_AusAggregatedControllerTable_Object = MibTable
ausAggregatedControllerTable = _AusAggregatedControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 200, 1)
)
if mibBuilder.loadTexts:
    ausAggregatedControllerTable.setStatus("mandatory")
_AusAggregatedControllerEntry_Object = MibTableRow
ausAggregatedControllerEntry = _AusAggregatedControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 200, 1, 1)
)
ausAggregatedControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausAggregatedControllerIndex"),
)
if mibBuilder.loadTexts:
    ausAggregatedControllerEntry.setStatus("mandatory")
_AusAggregatedControllerIndex_Type = Integer32
_AusAggregatedControllerIndex_Object = MibTableColumn
ausAggregatedControllerIndex = _AusAggregatedControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 200, 1, 1, 1),
    _AusAggregatedControllerIndex_Type()
)
ausAggregatedControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausAggregatedControllerIndex.setStatus("mandatory")
_AusAggregatedControllerList_Type = IndexList
_AusAggregatedControllerList_Object = MibTableColumn
ausAggregatedControllerList = _AusAggregatedControllerList_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 200, 1, 1, 2),
    _AusAggregatedControllerList_Type()
)
ausAggregatedControllerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausAggregatedControllerList.setStatus("mandatory")
_AusController_ObjectIdentity = ObjectIdentity
ausController = _AusController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201)
)
_AusControllerTable_Object = MibTable
ausControllerTable = _AusControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1)
)
if mibBuilder.loadTexts:
    ausControllerTable.setStatus("mandatory")
_AusControllerEntry_Object = MibTableRow
ausControllerEntry = _AusControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1)
)
ausControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausControllerIndex"),
)
if mibBuilder.loadTexts:
    ausControllerEntry.setStatus("mandatory")
_AusControllerIndex_Type = Integer32
_AusControllerIndex_Object = MibTableColumn
ausControllerIndex = _AusControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 1),
    _AusControllerIndex_Type()
)
ausControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerIndex.setStatus("mandatory")
_AusControllerUniqueId_Type = DisplayString
_AusControllerUniqueId_Object = MibTableColumn
ausControllerUniqueId = _AusControllerUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 2),
    _AusControllerUniqueId_Type()
)
ausControllerUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerUniqueId.setStatus("mandatory")
_AusControllerVendor_Type = DisplayString
_AusControllerVendor_Object = MibTableColumn
ausControllerVendor = _AusControllerVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 3),
    _AusControllerVendor_Type()
)
ausControllerVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerVendor.setStatus("mandatory")
_AusControllerModel_Type = DisplayString
_AusControllerModel_Object = MibTableColumn
ausControllerModel = _AusControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 4),
    _AusControllerModel_Type()
)
ausControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerModel.setStatus("mandatory")
_AusControllerRevision_Type = DisplayString
_AusControllerRevision_Object = MibTableColumn
ausControllerRevision = _AusControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 5),
    _AusControllerRevision_Type()
)
ausControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerRevision.setStatus("mandatory")
_AusControllerSerialNumber_Type = DisplayString
_AusControllerSerialNumber_Object = MibTableColumn
ausControllerSerialNumber = _AusControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 6),
    _AusControllerSerialNumber_Type()
)
ausControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerSerialNumber.setStatus("mandatory")
_AusControllerDescription_Type = DisplayString
_AusControllerDescription_Object = MibTableColumn
ausControllerDescription = _AusControllerDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 7),
    _AusControllerDescription_Type()
)
ausControllerDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerDescription.setStatus("mandatory")


class _AusControllerHostBusType_Type(Integer32):
    """Custom type ausControllerHostBusType based on Integer32"""
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
        *(("notApplicable", 3),
          ("other", 2),
          ("pci", 4),
          ("pci-32", 5),
          ("pci-64", 6),
          ("picx", 7),
          ("unknown", 1))
    )


_AusControllerHostBusType_Type.__name__ = "Integer32"
_AusControllerHostBusType_Object = MibTableColumn
ausControllerHostBusType = _AusControllerHostBusType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 8),
    _AusControllerHostBusType_Type()
)
ausControllerHostBusType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerHostBusType.setStatus("mandatory")
_AusControllerHostBusMaximumTransferRate_Type = Integer32
_AusControllerHostBusMaximumTransferRate_Object = MibTableColumn
ausControllerHostBusMaximumTransferRate = _AusControllerHostBusMaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 9),
    _AusControllerHostBusMaximumTransferRate_Type()
)
ausControllerHostBusMaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerHostBusMaximumTransferRate.setStatus("mandatory")
_AusControllerNumberOfChannels_Type = Integer32
_AusControllerNumberOfChannels_Object = MibTableColumn
ausControllerNumberOfChannels = _AusControllerNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 10),
    _AusControllerNumberOfChannels_Type()
)
ausControllerNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerNumberOfChannels.setStatus("mandatory")
_AusControllerHighestChannelWithDevices_Type = Integer32
_AusControllerHighestChannelWithDevices_Object = MibTableColumn
ausControllerHighestChannelWithDevices = _AusControllerHighestChannelWithDevices_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 11),
    _AusControllerHighestChannelWithDevices_Type()
)
ausControllerHighestChannelWithDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerHighestChannelWithDevices.setStatus("mandatory")
_AusControllerInstalledMemory_Type = Integer32
_AusControllerInstalledMemory_Object = MibTableColumn
ausControllerInstalledMemory = _AusControllerInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 12),
    _AusControllerInstalledMemory_Type()
)
ausControllerInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerInstalledMemory.setStatus("mandatory")
_AusControllerAudibleAlarmStatus_Type = OptionStatus
_AusControllerAudibleAlarmStatus_Object = MibTableColumn
ausControllerAudibleAlarmStatus = _AusControllerAudibleAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 13),
    _AusControllerAudibleAlarmStatus_Type()
)
ausControllerAudibleAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerAudibleAlarmStatus.setStatus("mandatory")
_AusControllerBatteryStatus_Type = BatteryStatus
_AusControllerBatteryStatus_Object = MibTableColumn
ausControllerBatteryStatus = _AusControllerBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 14),
    _AusControllerBatteryStatus_Type()
)
ausControllerBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerBatteryStatus.setStatus("mandatory")
_AusControllerStatus_Type = ObjectStatus
_AusControllerStatus_Object = MibTableColumn
ausControllerStatus = _AusControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 15),
    _AusControllerStatus_Type()
)
ausControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerStatus.setStatus("mandatory")
_AusControllerOverallStatus_Type = ObjectStatus
_AusControllerOverallStatus_Object = MibTableColumn
ausControllerOverallStatus = _AusControllerOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 201, 1, 1, 16),
    _AusControllerOverallStatus_Type()
)
ausControllerOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerOverallStatus.setStatus("mandatory")
_AusControllerRelationship_ObjectIdentity = ObjectIdentity
ausControllerRelationship = _AusControllerRelationship_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202)
)
_AusControllerRelationshipTable_Object = MibTable
ausControllerRelationshipTable = _AusControllerRelationshipTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1)
)
if mibBuilder.loadTexts:
    ausControllerRelationshipTable.setStatus("mandatory")
_AusControllerRelationshipEntry_Object = MibTableRow
ausControllerRelationshipEntry = _AusControllerRelationshipEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1, 1)
)
ausControllerRelationshipEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausControllerRelationshipIndex"),
)
if mibBuilder.loadTexts:
    ausControllerRelationshipEntry.setStatus("mandatory")
_AusControllerRelationshipIndex_Type = Integer32
_AusControllerRelationshipIndex_Object = MibTableColumn
ausControllerRelationshipIndex = _AusControllerRelationshipIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1, 1, 1),
    _AusControllerRelationshipIndex_Type()
)
ausControllerRelationshipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerRelationshipIndex.setStatus("mandatory")


class _AusControllerRelationshipType_Type(Integer32):
    """Custom type ausControllerRelationshipType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalRaid", 2),
          ("hostAttachedController", 1))
    )


_AusControllerRelationshipType_Type.__name__ = "Integer32"
_AusControllerRelationshipType_Object = MibTableColumn
ausControllerRelationshipType = _AusControllerRelationshipType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1, 1, 2),
    _AusControllerRelationshipType_Type()
)
ausControllerRelationshipType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerRelationshipType.setStatus("mandatory")
_AusControllerRelationshipList_Type = IndexList
_AusControllerRelationshipList_Object = MibTableColumn
ausControllerRelationshipList = _AusControllerRelationshipList_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1, 1, 3),
    _AusControllerRelationshipList_Type()
)
ausControllerRelationshipList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerRelationshipList.setStatus("mandatory")
_AusControllerRelationshipRelation_Type = Integer32
_AusControllerRelationshipRelation_Object = MibTableColumn
ausControllerRelationshipRelation = _AusControllerRelationshipRelation_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 202, 1, 1, 4),
    _AusControllerRelationshipRelation_Type()
)
ausControllerRelationshipRelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausControllerRelationshipRelation.setStatus("mandatory")
_AusI2ORaidController_ObjectIdentity = ObjectIdentity
ausI2ORaidController = _AusI2ORaidController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210)
)
_AusI2ORaidControllerTable_Object = MibTable
ausI2ORaidControllerTable = _AusI2ORaidControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1)
)
if mibBuilder.loadTexts:
    ausI2ORaidControllerTable.setStatus("mandatory")
_AusI2ORaidControllerEntry_Object = MibTableRow
ausI2ORaidControllerEntry = _AusI2ORaidControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1)
)
ausI2ORaidControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausI2ORaidControllerIndex"),
)
if mibBuilder.loadTexts:
    ausI2ORaidControllerEntry.setStatus("mandatory")
_AusI2ORaidControllerIndex_Type = Integer32
_AusI2ORaidControllerIndex_Object = MibTableColumn
ausI2ORaidControllerIndex = _AusI2ORaidControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 1),
    _AusI2ORaidControllerIndex_Type()
)
ausI2ORaidControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerIndex.setStatus("mandatory")


class _AusI2ORaidControllerAddress_Type(Integer32):
    """Custom type ausI2ORaidControllerAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_AusI2ORaidControllerAddress_Type.__name__ = "Integer32"
_AusI2ORaidControllerAddress_Object = MibTableColumn
ausI2ORaidControllerAddress = _AusI2ORaidControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 2),
    _AusI2ORaidControllerAddress_Type()
)
ausI2ORaidControllerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerAddress.setStatus("mandatory")


class _AusI2ORaidControllerBackgroundTaskPriority_Type(Integer32):
    """Custom type ausI2ORaidControllerBackgroundTaskPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AusI2ORaidControllerBackgroundTaskPriority_Type.__name__ = "Integer32"
_AusI2ORaidControllerBackgroundTaskPriority_Object = MibTableColumn
ausI2ORaidControllerBackgroundTaskPriority = _AusI2ORaidControllerBackgroundTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 3),
    _AusI2ORaidControllerBackgroundTaskPriority_Type()
)
ausI2ORaidControllerBackgroundTaskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerBackgroundTaskPriority.setStatus("mandatory")
_AusI2ORaidControllerBiosRevision_Type = DisplayString
_AusI2ORaidControllerBiosRevision_Object = MibTableColumn
ausI2ORaidControllerBiosRevision = _AusI2ORaidControllerBiosRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 4),
    _AusI2ORaidControllerBiosRevision_Type()
)
ausI2ORaidControllerBiosRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerBiosRevision.setStatus("mandatory")
_AusI2ORaidControllerSmorRevision_Type = DisplayString
_AusI2ORaidControllerSmorRevision_Object = MibTableColumn
ausI2ORaidControllerSmorRevision = _AusI2ORaidControllerSmorRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 5),
    _AusI2ORaidControllerSmorRevision_Type()
)
ausI2ORaidControllerSmorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerSmorRevision.setStatus("mandatory")
_AusI2ORaidControllerMainIndex_Type = Integer32
_AusI2ORaidControllerMainIndex_Object = MibTableColumn
ausI2ORaidControllerMainIndex = _AusI2ORaidControllerMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 210, 1, 1, 6),
    _AusI2ORaidControllerMainIndex_Type()
)
ausI2ORaidControllerMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausI2ORaidControllerMainIndex.setStatus("mandatory")
_AusCCodeController_ObjectIdentity = ObjectIdentity
ausCCodeController = _AusCCodeController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211)
)
_AusCCodeControllerTable_Object = MibTable
ausCCodeControllerTable = _AusCCodeControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1)
)
if mibBuilder.loadTexts:
    ausCCodeControllerTable.setStatus("mandatory")
_AusCCodeControllerEntry_Object = MibTableRow
ausCCodeControllerEntry = _AusCCodeControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1)
)
ausCCodeControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausCCodeControllerIndex"),
)
if mibBuilder.loadTexts:
    ausCCodeControllerEntry.setStatus("mandatory")
_AusCCodeControllerIndex_Type = Integer32
_AusCCodeControllerIndex_Object = MibTableColumn
ausCCodeControllerIndex = _AusCCodeControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1, 1),
    _AusCCodeControllerIndex_Type()
)
ausCCodeControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausCCodeControllerIndex.setStatus("mandatory")
_AusCCodeControllerPCIBusId_Type = Integer32
_AusCCodeControllerPCIBusId_Object = MibTableColumn
ausCCodeControllerPCIBusId = _AusCCodeControllerPCIBusId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1, 2),
    _AusCCodeControllerPCIBusId_Type()
)
ausCCodeControllerPCIBusId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausCCodeControllerPCIBusId.setStatus("mandatory")
_AusCCodeControllerPCISlotNumber_Type = Integer32
_AusCCodeControllerPCISlotNumber_Object = MibTableColumn
ausCCodeControllerPCISlotNumber = _AusCCodeControllerPCISlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1, 3),
    _AusCCodeControllerPCISlotNumber_Type()
)
ausCCodeControllerPCISlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausCCodeControllerPCISlotNumber.setStatus("mandatory")
_AusCCodeControllerBiosVersion_Type = DisplayString
_AusCCodeControllerBiosVersion_Object = MibTableColumn
ausCCodeControllerBiosVersion = _AusCCodeControllerBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1, 4),
    _AusCCodeControllerBiosVersion_Type()
)
ausCCodeControllerBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausCCodeControllerBiosVersion.setStatus("mandatory")
_AusCCodeControllerMainIndex_Type = Integer32
_AusCCodeControllerMainIndex_Object = MibTableColumn
ausCCodeControllerMainIndex = _AusCCodeControllerMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 211, 1, 1, 5),
    _AusCCodeControllerMainIndex_Type()
)
ausCCodeControllerMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausCCodeControllerMainIndex.setStatus("mandatory")
_AusHostRAIDController_ObjectIdentity = ObjectIdentity
ausHostRAIDController = _AusHostRAIDController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212)
)
_AusHostRAIDControllerTable_Object = MibTable
ausHostRAIDControllerTable = _AusHostRAIDControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1)
)
if mibBuilder.loadTexts:
    ausHostRAIDControllerTable.setStatus("mandatory")
_AusHostRAIDControllerEntry_Object = MibTableRow
ausHostRAIDControllerEntry = _AusHostRAIDControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1)
)
ausHostRAIDControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausHostRAIDControllerIndex"),
)
if mibBuilder.loadTexts:
    ausHostRAIDControllerEntry.setStatus("mandatory")
_AusHostRAIDControllerIndex_Type = Integer32
_AusHostRAIDControllerIndex_Object = MibTableColumn
ausHostRAIDControllerIndex = _AusHostRAIDControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1, 1),
    _AusHostRAIDControllerIndex_Type()
)
ausHostRAIDControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausHostRAIDControllerIndex.setStatus("mandatory")
_AusHostRAIDControllerPCIBus_Type = Integer32
_AusHostRAIDControllerPCIBus_Object = MibTableColumn
ausHostRAIDControllerPCIBus = _AusHostRAIDControllerPCIBus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1, 2),
    _AusHostRAIDControllerPCIBus_Type()
)
ausHostRAIDControllerPCIBus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausHostRAIDControllerPCIBus.setStatus("mandatory")
_AusHostRAIDControllerPCIDevice_Type = Integer32
_AusHostRAIDControllerPCIDevice_Object = MibTableColumn
ausHostRAIDControllerPCIDevice = _AusHostRAIDControllerPCIDevice_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1, 3),
    _AusHostRAIDControllerPCIDevice_Type()
)
ausHostRAIDControllerPCIDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausHostRAIDControllerPCIDevice.setStatus("mandatory")
_AusHostRAIDControllerPCIFunction_Type = Integer32
_AusHostRAIDControllerPCIFunction_Object = MibTableColumn
ausHostRAIDControllerPCIFunction = _AusHostRAIDControllerPCIFunction_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1, 4),
    _AusHostRAIDControllerPCIFunction_Type()
)
ausHostRAIDControllerPCIFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausHostRAIDControllerPCIFunction.setStatus("mandatory")
_AusHostRAIDControllerMainIndex_Type = Integer32
_AusHostRAIDControllerMainIndex_Object = MibTableColumn
ausHostRAIDControllerMainIndex = _AusHostRAIDControllerMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 212, 1, 1, 5),
    _AusHostRAIDControllerMainIndex_Type()
)
ausHostRAIDControllerMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausHostRAIDControllerMainIndex.setStatus("mandatory")
_AusServeRAIDController_ObjectIdentity = ObjectIdentity
ausServeRAIDController = _AusServeRAIDController_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213)
)
_AusServeRAIDControllerTable_Object = MibTable
ausServeRAIDControllerTable = _AusServeRAIDControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1)
)
if mibBuilder.loadTexts:
    ausServeRAIDControllerTable.setStatus("mandatory")
_AusServeRAIDControllerEntry_Object = MibTableRow
ausServeRAIDControllerEntry = _AusServeRAIDControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1)
)
ausServeRAIDControllerEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausServeRAIDControllerIndex"),
)
if mibBuilder.loadTexts:
    ausServeRAIDControllerEntry.setStatus("mandatory")
_AusServeRAIDControllerIndex_Type = Integer32
_AusServeRAIDControllerIndex_Object = MibTableColumn
ausServeRAIDControllerIndex = _AusServeRAIDControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1, 1),
    _AusServeRAIDControllerIndex_Type()
)
ausServeRAIDControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausServeRAIDControllerIndex.setStatus("mandatory")
_AusServeRAIDControllerBIOSRevision_Type = DisplayString
_AusServeRAIDControllerBIOSRevision_Object = MibTableColumn
ausServeRAIDControllerBIOSRevision = _AusServeRAIDControllerBIOSRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1, 2),
    _AusServeRAIDControllerBIOSRevision_Type()
)
ausServeRAIDControllerBIOSRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausServeRAIDControllerBIOSRevision.setStatus("mandatory")


class _AusServeRAIDControllerDefaultRebuildRate_Type(Integer32):
    """Custom type ausServeRAIDControllerDefaultRebuildRate based on Integer32"""
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
        *(("high", 5),
          ("low", 3),
          ("medium", 4),
          ("other", 2),
          ("unknown", 1))
    )


_AusServeRAIDControllerDefaultRebuildRate_Type.__name__ = "Integer32"
_AusServeRAIDControllerDefaultRebuildRate_Object = MibTableColumn
ausServeRAIDControllerDefaultRebuildRate = _AusServeRAIDControllerDefaultRebuildRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1, 3),
    _AusServeRAIDControllerDefaultRebuildRate_Type()
)
ausServeRAIDControllerDefaultRebuildRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausServeRAIDControllerDefaultRebuildRate.setStatus("mandatory")
_AusServeRAIDControllerSlotNumber_Type = Integer32
_AusServeRAIDControllerSlotNumber_Object = MibTableColumn
ausServeRAIDControllerSlotNumber = _AusServeRAIDControllerSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1, 4),
    _AusServeRAIDControllerSlotNumber_Type()
)
ausServeRAIDControllerSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausServeRAIDControllerSlotNumber.setStatus("mandatory")
_AusServeRAIDControllerMainIndex_Type = Integer32
_AusServeRAIDControllerMainIndex_Object = MibTableColumn
ausServeRAIDControllerMainIndex = _AusServeRAIDControllerMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 213, 1, 1, 5),
    _AusServeRAIDControllerMainIndex_Type()
)
ausServeRAIDControllerMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausServeRAIDControllerMainIndex.setStatus("mandatory")
_AusChannel_ObjectIdentity = ObjectIdentity
ausChannel = _AusChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300)
)
_AusChannelTable_Object = MibTable
ausChannelTable = _AusChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1)
)
if mibBuilder.loadTexts:
    ausChannelTable.setStatus("mandatory")
_AusChannelEntry_Object = MibTableRow
ausChannelEntry = _AusChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1)
)
ausChannelEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausChannelIndex"),
)
if mibBuilder.loadTexts:
    ausChannelEntry.setStatus("mandatory")
_AusChannelIndex_Type = Integer32
_AusChannelIndex_Object = MibTableColumn
ausChannelIndex = _AusChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 1),
    _AusChannelIndex_Type()
)
ausChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelIndex.setStatus("mandatory")


class _AusChannelLocation_Type(Integer32):
    """Custom type ausChannelLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalRaid", 2),
          ("hostAttached", 1))
    )


_AusChannelLocation_Type.__name__ = "Integer32"
_AusChannelLocation_Object = MibTableColumn
ausChannelLocation = _AusChannelLocation_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 2),
    _AusChannelLocation_Type()
)
ausChannelLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelLocation.setStatus("mandatory")
_AusChannelAusControllerIndex_Type = Integer32
_AusChannelAusControllerIndex_Object = MibTableColumn
ausChannelAusControllerIndex = _AusChannelAusControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 3),
    _AusChannelAusControllerIndex_Type()
)
ausChannelAusControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelAusControllerIndex.setStatus("mandatory")
_AusChannelAusControllerChannelNumber_Type = Integer32
_AusChannelAusControllerChannelNumber_Object = MibTableColumn
ausChannelAusControllerChannelNumber = _AusChannelAusControllerChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 4),
    _AusChannelAusControllerChannelNumber_Type()
)
ausChannelAusControllerChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelAusControllerChannelNumber.setStatus("mandatory")


class _AusChannelType_Type(Integer32):
    """Custom type ausChannelType based on Integer32"""
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
        *(("fibreChannel", 5),
          ("ide", 4),
          ("other", 2),
          ("sas", 7),
          ("sata", 6),
          ("scsi", 3),
          ("unknown", 1))
    )


_AusChannelType_Type.__name__ = "Integer32"
_AusChannelType_Object = MibTableColumn
ausChannelType = _AusChannelType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 5),
    _AusChannelType_Type()
)
ausChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelType.setStatus("mandatory")
_AusChannelTypeDescription_Type = DisplayString
_AusChannelTypeDescription_Object = MibTableColumn
ausChannelTypeDescription = _AusChannelTypeDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 6),
    _AusChannelTypeDescription_Type()
)
ausChannelTypeDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelTypeDescription.setStatus("mandatory")
_AusChannelControllerId_Type = DisplayString
_AusChannelControllerId_Object = MibTableColumn
ausChannelControllerId = _AusChannelControllerId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 7),
    _AusChannelControllerId_Type()
)
ausChannelControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelControllerId.setStatus("mandatory")
_AusChannelControllerSubId_Type = DisplayString
_AusChannelControllerSubId_Object = MibTableColumn
ausChannelControllerSubId = _AusChannelControllerSubId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 8),
    _AusChannelControllerSubId_Type()
)
ausChannelControllerSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelControllerSubId.setStatus("mandatory")
_AusChannelWidth_Type = Integer32
_AusChannelWidth_Object = MibTableColumn
ausChannelWidth = _AusChannelWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 9),
    _AusChannelWidth_Type()
)
ausChannelWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelWidth.setStatus("mandatory")
_AusChannelMaximumTransferRate_Type = Integer32
_AusChannelMaximumTransferRate_Object = MibTableColumn
ausChannelMaximumTransferRate = _AusChannelMaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 10),
    _AusChannelMaximumTransferRate_Type()
)
ausChannelMaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelMaximumTransferRate.setStatus("mandatory")
_AusChannelMaximumAttachments_Type = Integer32
_AusChannelMaximumAttachments_Object = MibTableColumn
ausChannelMaximumAttachments = _AusChannelMaximumAttachments_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 11),
    _AusChannelMaximumAttachments_Type()
)
ausChannelMaximumAttachments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelMaximumAttachments.setStatus("mandatory")
_AusChannelOverallStatus_Type = ObjectStatus
_AusChannelOverallStatus_Object = MibTableColumn
ausChannelOverallStatus = _AusChannelOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 300, 1, 1, 12),
    _AusChannelOverallStatus_Type()
)
ausChannelOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelOverallStatus.setStatus("mandatory")
_AusChannelRelationship_ObjectIdentity = ObjectIdentity
ausChannelRelationship = _AusChannelRelationship_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301)
)
_AusChannelRelationshipTable_Object = MibTable
ausChannelRelationshipTable = _AusChannelRelationshipTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301, 1)
)
if mibBuilder.loadTexts:
    ausChannelRelationshipTable.setStatus("mandatory")
_AusChannelRelationshipEntry_Object = MibTableRow
ausChannelRelationshipEntry = _AusChannelRelationshipEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301, 1, 1)
)
ausChannelRelationshipEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausChannelRelationshipIndex"),
)
if mibBuilder.loadTexts:
    ausChannelRelationshipEntry.setStatus("mandatory")
_AusChannelRelationshipIndex_Type = Integer32
_AusChannelRelationshipIndex_Object = MibTableColumn
ausChannelRelationshipIndex = _AusChannelRelationshipIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301, 1, 1, 1),
    _AusChannelRelationshipIndex_Type()
)
ausChannelRelationshipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelRelationshipIndex.setStatus("mandatory")
_AusChannelRelationshipList_Type = IndexList
_AusChannelRelationshipList_Object = MibTableColumn
ausChannelRelationshipList = _AusChannelRelationshipList_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301, 1, 1, 2),
    _AusChannelRelationshipList_Type()
)
ausChannelRelationshipList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelRelationshipList.setStatus("mandatory")
_AusChannelRelationshipRelation_Type = Integer32
_AusChannelRelationshipRelation_Object = MibTableColumn
ausChannelRelationshipRelation = _AusChannelRelationshipRelation_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 301, 1, 1, 3),
    _AusChannelRelationshipRelation_Type()
)
ausChannelRelationshipRelation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausChannelRelationshipRelation.setStatus("mandatory")
_AusDevice_ObjectIdentity = ObjectIdentity
ausDevice = _AusDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400)
)
_AusDeviceTable_Object = MibTable
ausDeviceTable = _AusDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1)
)
if mibBuilder.loadTexts:
    ausDeviceTable.setStatus("mandatory")
_AusDeviceEntry_Object = MibTableRow
ausDeviceEntry = _AusDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1)
)
ausDeviceEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausDeviceIndex"),
)
if mibBuilder.loadTexts:
    ausDeviceEntry.setStatus("mandatory")
_AusDeviceIndex_Type = Integer32
_AusDeviceIndex_Object = MibTableColumn
ausDeviceIndex = _AusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 1),
    _AusDeviceIndex_Type()
)
ausDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceIndex.setStatus("mandatory")
_AusDeviceUniqueId_Type = DisplayString
_AusDeviceUniqueId_Object = MibTableColumn
ausDeviceUniqueId = _AusDeviceUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 2),
    _AusDeviceUniqueId_Type()
)
ausDeviceUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceUniqueId.setStatus("mandatory")
_AusDeviceAusChannelIndices_Type = IndexList
_AusDeviceAusChannelIndices_Object = MibTableColumn
ausDeviceAusChannelIndices = _AusDeviceAusChannelIndices_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 3),
    _AusDeviceAusChannelIndices_Type()
)
ausDeviceAusChannelIndices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceAusChannelIndices.setStatus("mandatory")


class _AusDeviceType_Type(Integer32):
    """Custom type ausDeviceType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("cdRom", 8),
          ("communications", 12),
          ("directAccess", 3),
          ("mediumChanger", 11),
          ("opticalMemory", 10),
          ("other", 2),
          ("printer", 5),
          ("processor", 6),
          ("scanner", 9),
          ("sequentialAccess", 4),
          ("unknown", 1),
          ("writeOnce", 7))
    )


_AusDeviceType_Type.__name__ = "Integer32"
_AusDeviceType_Object = MibTableColumn
ausDeviceType = _AusDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 4),
    _AusDeviceType_Type()
)
ausDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceType.setStatus("mandatory")


class _AusDeviceTypeGroup_Type(Integer32):
    """Custom type ausDeviceTypeGroup based on Integer32"""
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
        *(("enclosureDevice", 3),
          ("externalRaidDevice", 4),
          ("noSubordinateTable", 1),
          ("otherDevice", 5),
          ("storageDevice", 2))
    )


_AusDeviceTypeGroup_Type.__name__ = "Integer32"
_AusDeviceTypeGroup_Object = MibTableColumn
ausDeviceTypeGroup = _AusDeviceTypeGroup_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 5),
    _AusDeviceTypeGroup_Type()
)
ausDeviceTypeGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceTypeGroup.setStatus("mandatory")
_AusDeviceVendor_Type = DisplayString
_AusDeviceVendor_Object = MibTableColumn
ausDeviceVendor = _AusDeviceVendor_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 6),
    _AusDeviceVendor_Type()
)
ausDeviceVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceVendor.setStatus("mandatory")
_AusDeviceModel_Type = DisplayString
_AusDeviceModel_Object = MibTableColumn
ausDeviceModel = _AusDeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 7),
    _AusDeviceModel_Type()
)
ausDeviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceModel.setStatus("mandatory")
_AusDeviceRevision_Type = DisplayString
_AusDeviceRevision_Object = MibTableColumn
ausDeviceRevision = _AusDeviceRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 8),
    _AusDeviceRevision_Type()
)
ausDeviceRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceRevision.setStatus("mandatory")
_AusDeviceSerialNumber_Type = DisplayString
_AusDeviceSerialNumber_Object = MibTableColumn
ausDeviceSerialNumber = _AusDeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 9),
    _AusDeviceSerialNumber_Type()
)
ausDeviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceSerialNumber.setStatus("mandatory")
_AusDeviceNumberOfPorts_Type = Integer32
_AusDeviceNumberOfPorts_Object = MibTableColumn
ausDeviceNumberOfPorts = _AusDeviceNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 10),
    _AusDeviceNumberOfPorts_Type()
)
ausDeviceNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceNumberOfPorts.setStatus("mandatory")
_AusDeviceStatus_Type = ObjectStatus
_AusDeviceStatus_Object = MibTableColumn
ausDeviceStatus = _AusDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 400, 1, 1, 11),
    _AusDeviceStatus_Type()
)
ausDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDeviceStatus.setStatus("mandatory")
_AusDevicePort_ObjectIdentity = ObjectIdentity
ausDevicePort = _AusDevicePort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401)
)
_AusDevicePortTable_Object = MibTable
ausDevicePortTable = _AusDevicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1)
)
if mibBuilder.loadTexts:
    ausDevicePortTable.setStatus("mandatory")
_AusDevicePortEntry_Object = MibTableRow
ausDevicePortEntry = _AusDevicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1)
)
ausDevicePortEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausDevicePortIndex"),
)
if mibBuilder.loadTexts:
    ausDevicePortEntry.setStatus("mandatory")
_AusDevicePortIndex_Type = Integer32
_AusDevicePortIndex_Object = MibTableColumn
ausDevicePortIndex = _AusDevicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 1),
    _AusDevicePortIndex_Type()
)
ausDevicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortIndex.setStatus("mandatory")
_AusDevicePortUniqueId_Type = DisplayString
_AusDevicePortUniqueId_Object = MibTableColumn
ausDevicePortUniqueId = _AusDevicePortUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 2),
    _AusDevicePortUniqueId_Type()
)
ausDevicePortUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortUniqueId.setStatus("mandatory")
_AusDevicePortAusDeviceIndex_Type = Integer32
_AusDevicePortAusDeviceIndex_Object = MibTableColumn
ausDevicePortAusDeviceIndex = _AusDevicePortAusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 3),
    _AusDevicePortAusDeviceIndex_Type()
)
ausDevicePortAusDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortAusDeviceIndex.setStatus("mandatory")
_AusDevicePortAusDevicePortNumber_Type = Integer32
_AusDevicePortAusDevicePortNumber_Object = MibTableColumn
ausDevicePortAusDevicePortNumber = _AusDevicePortAusDevicePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 4),
    _AusDevicePortAusDevicePortNumber_Type()
)
ausDevicePortAusDevicePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortAusDevicePortNumber.setStatus("mandatory")
_AusDevicePortAusChannelIndex_Type = Integer32
_AusDevicePortAusChannelIndex_Object = MibTableColumn
ausDevicePortAusChannelIndex = _AusDevicePortAusChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 5),
    _AusDevicePortAusChannelIndex_Type()
)
ausDevicePortAusChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortAusChannelIndex.setStatus("mandatory")
_AusDevicePortId_Type = DisplayString
_AusDevicePortId_Object = MibTableColumn
ausDevicePortId = _AusDevicePortId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 6),
    _AusDevicePortId_Type()
)
ausDevicePortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortId.setStatus("mandatory")
_AusDevicePortSubId_Type = DisplayString
_AusDevicePortSubId_Object = MibTableColumn
ausDevicePortSubId = _AusDevicePortSubId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 7),
    _AusDevicePortSubId_Type()
)
ausDevicePortSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortSubId.setStatus("mandatory")
_AusDevicePortWidth_Type = Integer32
_AusDevicePortWidth_Object = MibTableColumn
ausDevicePortWidth = _AusDevicePortWidth_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 8),
    _AusDevicePortWidth_Type()
)
ausDevicePortWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortWidth.setStatus("mandatory")
_AusDevicePortMaximumTransferRate_Type = Integer32
_AusDevicePortMaximumTransferRate_Object = MibTableColumn
ausDevicePortMaximumTransferRate = _AusDevicePortMaximumTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 9),
    _AusDevicePortMaximumTransferRate_Type()
)
ausDevicePortMaximumTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortMaximumTransferRate.setStatus("mandatory")
_AusDevicePortNegotiatedTransferRate_Type = Integer32
_AusDevicePortNegotiatedTransferRate_Object = MibTableColumn
ausDevicePortNegotiatedTransferRate = _AusDevicePortNegotiatedTransferRate_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 10),
    _AusDevicePortNegotiatedTransferRate_Type()
)
ausDevicePortNegotiatedTransferRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortNegotiatedTransferRate.setStatus("mandatory")
_AusDevicePortStatus_Type = ObjectStatus
_AusDevicePortStatus_Object = MibTableColumn
ausDevicePortStatus = _AusDevicePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 401, 1, 1, 11),
    _AusDevicePortStatus_Type()
)
ausDevicePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausDevicePortStatus.setStatus("mandatory")
_AusStorageDevice_ObjectIdentity = ObjectIdentity
ausStorageDevice = _AusStorageDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410)
)
_AusStorageDeviceTable_Object = MibTable
ausStorageDeviceTable = _AusStorageDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1)
)
if mibBuilder.loadTexts:
    ausStorageDeviceTable.setStatus("mandatory")
_AusStorageDeviceEntry_Object = MibTableRow
ausStorageDeviceEntry = _AusStorageDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1)
)
ausStorageDeviceEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausStorageDeviceIndex"),
)
if mibBuilder.loadTexts:
    ausStorageDeviceEntry.setStatus("mandatory")
_AusStorageDeviceIndex_Type = Integer32
_AusStorageDeviceIndex_Object = MibTableColumn
ausStorageDeviceIndex = _AusStorageDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 1),
    _AusStorageDeviceIndex_Type()
)
ausStorageDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceIndex.setStatus("mandatory")
_AusStorageDeviceDescription_Type = DisplayString
_AusStorageDeviceDescription_Object = MibTableColumn
ausStorageDeviceDescription = _AusStorageDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 2),
    _AusStorageDeviceDescription_Type()
)
ausStorageDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceDescription.setStatus("mandatory")
_AusStorageDeviceFormattedCapacity_Type = Integer32
_AusStorageDeviceFormattedCapacity_Object = MibTableColumn
ausStorageDeviceFormattedCapacity = _AusStorageDeviceFormattedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 3),
    _AusStorageDeviceFormattedCapacity_Type()
)
ausStorageDeviceFormattedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceFormattedCapacity.setStatus("mandatory")
_AusStorageDeviceBlockSize_Type = Integer32
_AusStorageDeviceBlockSize_Object = MibTableColumn
ausStorageDeviceBlockSize = _AusStorageDeviceBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 4),
    _AusStorageDeviceBlockSize_Type()
)
ausStorageDeviceBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceBlockSize.setStatus("mandatory")
_AusStorageDeviceNumberOfBlocksLow_Type = Integer32
_AusStorageDeviceNumberOfBlocksLow_Object = MibTableColumn
ausStorageDeviceNumberOfBlocksLow = _AusStorageDeviceNumberOfBlocksLow_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 5),
    _AusStorageDeviceNumberOfBlocksLow_Type()
)
ausStorageDeviceNumberOfBlocksLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceNumberOfBlocksLow.setStatus("mandatory")
_AusStorageDeviceNumberOfBlocksHigh_Type = Integer32
_AusStorageDeviceNumberOfBlocksHigh_Object = MibTableColumn
ausStorageDeviceNumberOfBlocksHigh = _AusStorageDeviceNumberOfBlocksHigh_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 6),
    _AusStorageDeviceNumberOfBlocksHigh_Type()
)
ausStorageDeviceNumberOfBlocksHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceNumberOfBlocksHigh.setStatus("mandatory")


class _AusStorageDeviceRemovableMedia_Type(Integer32):
    """Custom type ausStorageDeviceRemovableMedia based on Integer32"""
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
        *(("notSupported", 2),
          ("supportedAndLoaded", 4),
          ("supportedAndNotLoaded", 3),
          ("unknown", 1))
    )


_AusStorageDeviceRemovableMedia_Type.__name__ = "Integer32"
_AusStorageDeviceRemovableMedia_Object = MibTableColumn
ausStorageDeviceRemovableMedia = _AusStorageDeviceRemovableMedia_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 7),
    _AusStorageDeviceRemovableMedia_Type()
)
ausStorageDeviceRemovableMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceRemovableMedia.setStatus("mandatory")


class _AusStorageDeviceSmartStatus_Type(Integer32):
    """Custom type ausStorageDeviceSmartStatus based on Integer32"""
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
        *(("errorPredicted", 5),
          ("notEnabled", 3),
          ("notSupported", 2),
          ("okay", 4),
          ("unknown", 1))
    )


_AusStorageDeviceSmartStatus_Type.__name__ = "Integer32"
_AusStorageDeviceSmartStatus_Object = MibTableColumn
ausStorageDeviceSmartStatus = _AusStorageDeviceSmartStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 8),
    _AusStorageDeviceSmartStatus_Type()
)
ausStorageDeviceSmartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceSmartStatus.setStatus("mandatory")
_AusStorageDeviceMainIndex_Type = Integer32
_AusStorageDeviceMainIndex_Object = MibTableColumn
ausStorageDeviceMainIndex = _AusStorageDeviceMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 410, 1, 1, 9),
    _AusStorageDeviceMainIndex_Type()
)
ausStorageDeviceMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausStorageDeviceMainIndex.setStatus("mandatory")
_AusEnclosureDevice_ObjectIdentity = ObjectIdentity
ausEnclosureDevice = _AusEnclosureDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411)
)
_AusEnclosureDeviceTable_Object = MibTable
ausEnclosureDeviceTable = _AusEnclosureDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1)
)
if mibBuilder.loadTexts:
    ausEnclosureDeviceTable.setStatus("mandatory")
_AusEnclosureDeviceEntry_Object = MibTableRow
ausEnclosureDeviceEntry = _AusEnclosureDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1)
)
ausEnclosureDeviceEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEnclosureDeviceIndex"),
)
if mibBuilder.loadTexts:
    ausEnclosureDeviceEntry.setStatus("mandatory")
_AusEnclosureDeviceIndex_Type = Integer32
_AusEnclosureDeviceIndex_Object = MibTableColumn
ausEnclosureDeviceIndex = _AusEnclosureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 1),
    _AusEnclosureDeviceIndex_Type()
)
ausEnclosureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceIndex.setStatus("mandatory")
_AusEnclosureDeviceDescription_Type = DisplayString
_AusEnclosureDeviceDescription_Object = MibTableColumn
ausEnclosureDeviceDescription = _AusEnclosureDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 2),
    _AusEnclosureDeviceDescription_Type()
)
ausEnclosureDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceDescription.setStatus("mandatory")


class _AusEnclosureDeviceProcessorType_Type(Integer32):
    """Custom type ausEnclosureDeviceProcessorType based on Integer32"""
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
        *(("aemi", 6),
          ("decFault", 3),
          ("other", 2),
          ("saf-te", 4),
          ("ses", 5),
          ("unknown", 1))
    )


_AusEnclosureDeviceProcessorType_Type.__name__ = "Integer32"
_AusEnclosureDeviceProcessorType_Object = MibTableColumn
ausEnclosureDeviceProcessorType = _AusEnclosureDeviceProcessorType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 3),
    _AusEnclosureDeviceProcessorType_Type()
)
ausEnclosureDeviceProcessorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceProcessorType.setStatus("mandatory")
_AusEnclosureDeviceNumberOfFans_Type = Integer32
_AusEnclosureDeviceNumberOfFans_Object = MibTableColumn
ausEnclosureDeviceNumberOfFans = _AusEnclosureDeviceNumberOfFans_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 4),
    _AusEnclosureDeviceNumberOfFans_Type()
)
ausEnclosureDeviceNumberOfFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceNumberOfFans.setStatus("mandatory")
_AusEnclosureDeviceNumberOfPowerSupplies_Type = Integer32
_AusEnclosureDeviceNumberOfPowerSupplies_Object = MibTableColumn
ausEnclosureDeviceNumberOfPowerSupplies = _AusEnclosureDeviceNumberOfPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 5),
    _AusEnclosureDeviceNumberOfPowerSupplies_Type()
)
ausEnclosureDeviceNumberOfPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceNumberOfPowerSupplies.setStatus("mandatory")
_AusEnclosureDeviceNumberOfSlots_Type = Integer32
_AusEnclosureDeviceNumberOfSlots_Object = MibTableColumn
ausEnclosureDeviceNumberOfSlots = _AusEnclosureDeviceNumberOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 6),
    _AusEnclosureDeviceNumberOfSlots_Type()
)
ausEnclosureDeviceNumberOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceNumberOfSlots.setStatus("mandatory")
_AusEnclosureDeviceNumberOfTemperatureSensors_Type = Integer32
_AusEnclosureDeviceNumberOfTemperatureSensors_Object = MibTableColumn
ausEnclosureDeviceNumberOfTemperatureSensors = _AusEnclosureDeviceNumberOfTemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 7),
    _AusEnclosureDeviceNumberOfTemperatureSensors_Type()
)
ausEnclosureDeviceNumberOfTemperatureSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceNumberOfTemperatureSensors.setStatus("mandatory")
_AusEnclosureDeviceIdLow_Type = Integer32
_AusEnclosureDeviceIdLow_Object = MibTableColumn
ausEnclosureDeviceIdLow = _AusEnclosureDeviceIdLow_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 8),
    _AusEnclosureDeviceIdLow_Type()
)
ausEnclosureDeviceIdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceIdLow.setStatus("mandatory")
_AusEnclosureDeviceIdHigh_Type = Integer32
_AusEnclosureDeviceIdHigh_Object = MibTableColumn
ausEnclosureDeviceIdHigh = _AusEnclosureDeviceIdHigh_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 9),
    _AusEnclosureDeviceIdHigh_Type()
)
ausEnclosureDeviceIdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceIdHigh.setStatus("mandatory")
_AusEnclosureDeviceStandardRevision_Type = DisplayString
_AusEnclosureDeviceStandardRevision_Object = MibTableColumn
ausEnclosureDeviceStandardRevision = _AusEnclosureDeviceStandardRevision_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 10),
    _AusEnclosureDeviceStandardRevision_Type()
)
ausEnclosureDeviceStandardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceStandardRevision.setStatus("mandatory")
_AusEnclosureDevicePowerOnTime_Type = Integer32
_AusEnclosureDevicePowerOnTime_Object = MibTableColumn
ausEnclosureDevicePowerOnTime = _AusEnclosureDevicePowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 11),
    _AusEnclosureDevicePowerOnTime_Type()
)
ausEnclosureDevicePowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDevicePowerOnTime.setStatus("mandatory")
_AusEnclosureDevicePowerCycles_Type = Integer32
_AusEnclosureDevicePowerCycles_Object = MibTableColumn
ausEnclosureDevicePowerCycles = _AusEnclosureDevicePowerCycles_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 12),
    _AusEnclosureDevicePowerCycles_Type()
)
ausEnclosureDevicePowerCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDevicePowerCycles.setStatus("mandatory")
_AusEnclosureDeviceDoorLock_Type = OptionStatus
_AusEnclosureDeviceDoorLock_Object = MibTableColumn
ausEnclosureDeviceDoorLock = _AusEnclosureDeviceDoorLock_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 13),
    _AusEnclosureDeviceDoorLock_Type()
)
ausEnclosureDeviceDoorLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceDoorLock.setStatus("mandatory")
_AusEnclosureDeviceSpeaker_Type = OptionStatus
_AusEnclosureDeviceSpeaker_Object = MibTableColumn
ausEnclosureDeviceSpeaker = _AusEnclosureDeviceSpeaker_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 14),
    _AusEnclosureDeviceSpeaker_Type()
)
ausEnclosureDeviceSpeaker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceSpeaker.setStatus("mandatory")


class _AusEnclosureDeviceTemperatureState_Type(Integer32):
    """Custom type ausEnclosureDeviceTemperatureState based on Integer32"""
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
        *(("okay", 3),
          ("other", 2),
          ("tooHot", 4),
          ("unknown", 1))
    )


_AusEnclosureDeviceTemperatureState_Type.__name__ = "Integer32"
_AusEnclosureDeviceTemperatureState_Object = MibTableColumn
ausEnclosureDeviceTemperatureState = _AusEnclosureDeviceTemperatureState_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 15),
    _AusEnclosureDeviceTemperatureState_Type()
)
ausEnclosureDeviceTemperatureState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceTemperatureState.setStatus("mandatory")
_AusEnclosureDeviceMainIndex_Type = Integer32
_AusEnclosureDeviceMainIndex_Object = MibTableColumn
ausEnclosureDeviceMainIndex = _AusEnclosureDeviceMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 411, 1, 1, 16),
    _AusEnclosureDeviceMainIndex_Type()
)
ausEnclosureDeviceMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureDeviceMainIndex.setStatus("mandatory")
_AusExternalRaidDevice_ObjectIdentity = ObjectIdentity
ausExternalRaidDevice = _AusExternalRaidDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412)
)
_AusExternalRaidDeviceTable_Object = MibTable
ausExternalRaidDeviceTable = _AusExternalRaidDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1)
)
if mibBuilder.loadTexts:
    ausExternalRaidDeviceTable.setStatus("mandatory")
_AusExternalRaidDeviceEntry_Object = MibTableRow
ausExternalRaidDeviceEntry = _AusExternalRaidDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1)
)
ausExternalRaidDeviceEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausExternalRaidDeviceIndex"),
)
if mibBuilder.loadTexts:
    ausExternalRaidDeviceEntry.setStatus("mandatory")
_AusExternalRaidDeviceIndex_Type = Integer32
_AusExternalRaidDeviceIndex_Object = MibTableColumn
ausExternalRaidDeviceIndex = _AusExternalRaidDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 1),
    _AusExternalRaidDeviceIndex_Type()
)
ausExternalRaidDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceIndex.setStatus("mandatory")
_AusExternalRaidDeviceDescription_Type = DisplayString
_AusExternalRaidDeviceDescription_Object = MibTableColumn
ausExternalRaidDeviceDescription = _AusExternalRaidDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 2),
    _AusExternalRaidDeviceDescription_Type()
)
ausExternalRaidDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceDescription.setStatus("mandatory")
_AusExternalRaidDeviceNumberOfChannels_Type = Integer32
_AusExternalRaidDeviceNumberOfChannels_Object = MibTableColumn
ausExternalRaidDeviceNumberOfChannels = _AusExternalRaidDeviceNumberOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 3),
    _AusExternalRaidDeviceNumberOfChannels_Type()
)
ausExternalRaidDeviceNumberOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceNumberOfChannels.setStatus("mandatory")
_AusExternalRaidDeviceInstalledMemory_Type = Integer32
_AusExternalRaidDeviceInstalledMemory_Object = MibTableColumn
ausExternalRaidDeviceInstalledMemory = _AusExternalRaidDeviceInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 4),
    _AusExternalRaidDeviceInstalledMemory_Type()
)
ausExternalRaidDeviceInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceInstalledMemory.setStatus("mandatory")
_AusExternalRaidDeviceAudibleAlarmStatus_Type = OptionStatus
_AusExternalRaidDeviceAudibleAlarmStatus_Object = MibTableColumn
ausExternalRaidDeviceAudibleAlarmStatus = _AusExternalRaidDeviceAudibleAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 5),
    _AusExternalRaidDeviceAudibleAlarmStatus_Type()
)
ausExternalRaidDeviceAudibleAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceAudibleAlarmStatus.setStatus("mandatory")
_AusExternalRaidDeviceBatteryStatus_Type = BatteryStatus
_AusExternalRaidDeviceBatteryStatus_Object = MibTableColumn
ausExternalRaidDeviceBatteryStatus = _AusExternalRaidDeviceBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 6),
    _AusExternalRaidDeviceBatteryStatus_Type()
)
ausExternalRaidDeviceBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceBatteryStatus.setStatus("mandatory")
_AusExternalRaidDeviceMainIndex_Type = Integer32
_AusExternalRaidDeviceMainIndex_Object = MibTableColumn
ausExternalRaidDeviceMainIndex = _AusExternalRaidDeviceMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 412, 1, 1, 7),
    _AusExternalRaidDeviceMainIndex_Type()
)
ausExternalRaidDeviceMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExternalRaidDeviceMainIndex.setStatus("mandatory")
_AusOtherDevice_ObjectIdentity = ObjectIdentity
ausOtherDevice = _AusOtherDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499)
)
_AusOtherDeviceTable_Object = MibTable
ausOtherDeviceTable = _AusOtherDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499, 1)
)
if mibBuilder.loadTexts:
    ausOtherDeviceTable.setStatus("mandatory")
_AusOtherDeviceEntry_Object = MibTableRow
ausOtherDeviceEntry = _AusOtherDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499, 1, 1)
)
ausOtherDeviceEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausOtherDeviceIndex"),
)
if mibBuilder.loadTexts:
    ausOtherDeviceEntry.setStatus("mandatory")
_AusOtherDeviceIndex_Type = Integer32
_AusOtherDeviceIndex_Object = MibTableColumn
ausOtherDeviceIndex = _AusOtherDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499, 1, 1, 1),
    _AusOtherDeviceIndex_Type()
)
ausOtherDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausOtherDeviceIndex.setStatus("mandatory")
_AusOtherDeviceDescription_Type = DisplayString
_AusOtherDeviceDescription_Object = MibTableColumn
ausOtherDeviceDescription = _AusOtherDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499, 1, 1, 2),
    _AusOtherDeviceDescription_Type()
)
ausOtherDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausOtherDeviceDescription.setStatus("mandatory")
_AusOtherDeviceMainIndex_Type = Integer32
_AusOtherDeviceMainIndex_Object = MibTableColumn
ausOtherDeviceMainIndex = _AusOtherDeviceMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 499, 1, 1, 3),
    _AusOtherDeviceMainIndex_Type()
)
ausOtherDeviceMainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausOtherDeviceMainIndex.setStatus("mandatory")
_AusEnclosureFan_ObjectIdentity = ObjectIdentity
ausEnclosureFan = _AusEnclosureFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500)
)
_AusEnclosureFanTable_Object = MibTable
ausEnclosureFanTable = _AusEnclosureFanTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1)
)
if mibBuilder.loadTexts:
    ausEnclosureFanTable.setStatus("mandatory")
_AusEnclosureFanEntry_Object = MibTableRow
ausEnclosureFanEntry = _AusEnclosureFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1)
)
ausEnclosureFanEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEnclosureFanIndex"),
)
if mibBuilder.loadTexts:
    ausEnclosureFanEntry.setStatus("mandatory")
_AusEnclosureFanIndex_Type = Integer32
_AusEnclosureFanIndex_Object = MibTableColumn
ausEnclosureFanIndex = _AusEnclosureFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1, 1),
    _AusEnclosureFanIndex_Type()
)
ausEnclosureFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureFanIndex.setStatus("mandatory")
_AusEnclosureFanAusEnclosureDeviceIndex_Type = Integer32
_AusEnclosureFanAusEnclosureDeviceIndex_Object = MibTableColumn
ausEnclosureFanAusEnclosureDeviceIndex = _AusEnclosureFanAusEnclosureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1, 2),
    _AusEnclosureFanAusEnclosureDeviceIndex_Type()
)
ausEnclosureFanAusEnclosureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureFanAusEnclosureDeviceIndex.setStatus("mandatory")
_AusEnclosureFanOrdinal_Type = Integer32
_AusEnclosureFanOrdinal_Object = MibTableColumn
ausEnclosureFanOrdinal = _AusEnclosureFanOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1, 3),
    _AusEnclosureFanOrdinal_Type()
)
ausEnclosureFanOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureFanOrdinal.setStatus("mandatory")


class _AusEnclosureFanSpeed_Type(Integer32):
    """Custom type ausEnclosureFanSpeed based on Integer32"""
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
        *(("fullSpeed", 7),
          ("halfSpeed", 5),
          ("off", 3),
          ("other", 2),
          ("quarterSpeed", 4),
          ("threeQuartersSpeed", 6),
          ("unknown", 1))
    )


_AusEnclosureFanSpeed_Type.__name__ = "Integer32"
_AusEnclosureFanSpeed_Object = MibTableColumn
ausEnclosureFanSpeed = _AusEnclosureFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1, 4),
    _AusEnclosureFanSpeed_Type()
)
ausEnclosureFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureFanSpeed.setStatus("mandatory")
_AusEnclosureFanStatus_Type = ObjectStatus
_AusEnclosureFanStatus_Object = MibTableColumn
ausEnclosureFanStatus = _AusEnclosureFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 500, 1, 1, 5),
    _AusEnclosureFanStatus_Type()
)
ausEnclosureFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureFanStatus.setStatus("mandatory")
_AusEnclosurePowerSupply_ObjectIdentity = ObjectIdentity
ausEnclosurePowerSupply = _AusEnclosurePowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501)
)
_AusEnclosurePowerSupplyTable_Object = MibTable
ausEnclosurePowerSupplyTable = _AusEnclosurePowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1)
)
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyTable.setStatus("mandatory")
_AusEnclosurePowerSupplyEntry_Object = MibTableRow
ausEnclosurePowerSupplyEntry = _AusEnclosurePowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1, 1)
)
ausEnclosurePowerSupplyEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEnclosurePowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyEntry.setStatus("mandatory")
_AusEnclosurePowerSupplyIndex_Type = Integer32
_AusEnclosurePowerSupplyIndex_Object = MibTableColumn
ausEnclosurePowerSupplyIndex = _AusEnclosurePowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1, 1, 1),
    _AusEnclosurePowerSupplyIndex_Type()
)
ausEnclosurePowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyIndex.setStatus("mandatory")
_AusEnclosurePowerSupplyAusEnclosureDeviceIndex_Type = Integer32
_AusEnclosurePowerSupplyAusEnclosureDeviceIndex_Object = MibTableColumn
ausEnclosurePowerSupplyAusEnclosureDeviceIndex = _AusEnclosurePowerSupplyAusEnclosureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1, 1, 2),
    _AusEnclosurePowerSupplyAusEnclosureDeviceIndex_Type()
)
ausEnclosurePowerSupplyAusEnclosureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyAusEnclosureDeviceIndex.setStatus("mandatory")
_AusEnclosurePowerSupplyOrdinal_Type = Integer32
_AusEnclosurePowerSupplyOrdinal_Object = MibTableColumn
ausEnclosurePowerSupplyOrdinal = _AusEnclosurePowerSupplyOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1, 1, 3),
    _AusEnclosurePowerSupplyOrdinal_Type()
)
ausEnclosurePowerSupplyOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyOrdinal.setStatus("mandatory")


class _AusEnclosurePowerSupplyStatus_Type(Integer32):
    """Custom type ausEnclosurePowerSupplyStatus based on Integer32"""
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
        *(("installed", 7),
          ("notInstalled", 8),
          ("offAndMalfunctioning", 6),
          ("onAndMalfunctioning", 5),
          ("operationalAndOff", 4),
          ("operationalAndOn", 3),
          ("other", 2),
          ("unknown", 1))
    )


_AusEnclosurePowerSupplyStatus_Type.__name__ = "Integer32"
_AusEnclosurePowerSupplyStatus_Object = MibTableColumn
ausEnclosurePowerSupplyStatus = _AusEnclosurePowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 501, 1, 1, 4),
    _AusEnclosurePowerSupplyStatus_Type()
)
ausEnclosurePowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosurePowerSupplyStatus.setStatus("mandatory")
_AusEnclosureTemperatureSensor_ObjectIdentity = ObjectIdentity
ausEnclosureTemperatureSensor = _AusEnclosureTemperatureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502)
)
_AusEnclosureTemperatureSensorTable_Object = MibTable
ausEnclosureTemperatureSensorTable = _AusEnclosureTemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1)
)
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorTable.setStatus("mandatory")
_AusEnclosureTemperatureSensorEntry_Object = MibTableRow
ausEnclosureTemperatureSensorEntry = _AusEnclosureTemperatureSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1)
)
ausEnclosureTemperatureSensorEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEnclosureTemperatureSensorIndex"),
)
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorEntry.setStatus("mandatory")
_AusEnclosureTemperatureSensorIndex_Type = Integer32
_AusEnclosureTemperatureSensorIndex_Object = MibTableColumn
ausEnclosureTemperatureSensorIndex = _AusEnclosureTemperatureSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1, 1),
    _AusEnclosureTemperatureSensorIndex_Type()
)
ausEnclosureTemperatureSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorIndex.setStatus("mandatory")
_AusEnclosureTemperatureSensorAusEnclosureDeviceIndex_Type = Integer32
_AusEnclosureTemperatureSensorAusEnclosureDeviceIndex_Object = MibTableColumn
ausEnclosureTemperatureSensorAusEnclosureDeviceIndex = _AusEnclosureTemperatureSensorAusEnclosureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1, 2),
    _AusEnclosureTemperatureSensorAusEnclosureDeviceIndex_Type()
)
ausEnclosureTemperatureSensorAusEnclosureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorAusEnclosureDeviceIndex.setStatus("mandatory")
_AusEnclosureTemperatureSensorOrdinal_Type = Integer32
_AusEnclosureTemperatureSensorOrdinal_Object = MibTableColumn
ausEnclosureTemperatureSensorOrdinal = _AusEnclosureTemperatureSensorOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1, 3),
    _AusEnclosureTemperatureSensorOrdinal_Type()
)
ausEnclosureTemperatureSensorOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorOrdinal.setStatus("mandatory")
_AusEnclosureTemperatureSensorOverTemperature_Type = ObjectStatus
_AusEnclosureTemperatureSensorOverTemperature_Object = MibTableColumn
ausEnclosureTemperatureSensorOverTemperature = _AusEnclosureTemperatureSensorOverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1, 4),
    _AusEnclosureTemperatureSensorOverTemperature_Type()
)
ausEnclosureTemperatureSensorOverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorOverTemperature.setStatus("mandatory")
_AusEnclosureTemperatureSensorDegrees_Type = Integer32
_AusEnclosureTemperatureSensorDegrees_Object = MibTableColumn
ausEnclosureTemperatureSensorDegrees = _AusEnclosureTemperatureSensorDegrees_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 502, 1, 1, 5),
    _AusEnclosureTemperatureSensorDegrees_Type()
)
ausEnclosureTemperatureSensorDegrees.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureTemperatureSensorDegrees.setStatus("mandatory")
_AusEnclosureSlot_ObjectIdentity = ObjectIdentity
ausEnclosureSlot = _AusEnclosureSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503)
)
_AusEnclosureSlotTable_Object = MibTable
ausEnclosureSlotTable = _AusEnclosureSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1)
)
if mibBuilder.loadTexts:
    ausEnclosureSlotTable.setStatus("mandatory")
_AusEnclosureSlotEntry_Object = MibTableRow
ausEnclosureSlotEntry = _AusEnclosureSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1)
)
ausEnclosureSlotEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEnclosureSlotIndex"),
)
if mibBuilder.loadTexts:
    ausEnclosureSlotEntry.setStatus("mandatory")
_AusEnclosureSlotIndex_Type = Integer32
_AusEnclosureSlotIndex_Object = MibTableColumn
ausEnclosureSlotIndex = _AusEnclosureSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1, 1),
    _AusEnclosureSlotIndex_Type()
)
ausEnclosureSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureSlotIndex.setStatus("mandatory")
_AusEnclosureSlotAusEnclosureDeviceIndex_Type = Integer32
_AusEnclosureSlotAusEnclosureDeviceIndex_Object = MibTableColumn
ausEnclosureSlotAusEnclosureDeviceIndex = _AusEnclosureSlotAusEnclosureDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1, 2),
    _AusEnclosureSlotAusEnclosureDeviceIndex_Type()
)
ausEnclosureSlotAusEnclosureDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureSlotAusEnclosureDeviceIndex.setStatus("mandatory")
_AusEnclosureSlotOrdinal_Type = Integer32
_AusEnclosureSlotOrdinal_Object = MibTableColumn
ausEnclosureSlotOrdinal = _AusEnclosureSlotOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1, 3),
    _AusEnclosureSlotOrdinal_Type()
)
ausEnclosureSlotOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureSlotOrdinal.setStatus("mandatory")
_AusEnclosureSlotPortId_Type = DisplayString
_AusEnclosureSlotPortId_Object = MibTableColumn
ausEnclosureSlotPortId = _AusEnclosureSlotPortId_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1, 4),
    _AusEnclosureSlotPortId_Type()
)
ausEnclosureSlotPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureSlotPortId.setStatus("mandatory")
_AusEnclosureSlotInsertions_Type = Integer32
_AusEnclosureSlotInsertions_Object = MibTableColumn
ausEnclosureSlotInsertions = _AusEnclosureSlotInsertions_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 503, 1, 1, 5),
    _AusEnclosureSlotInsertions_Type()
)
ausEnclosureSlotInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEnclosureSlotInsertions.setStatus("mandatory")
_AusArray_ObjectIdentity = ObjectIdentity
ausArray = _AusArray_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000)
)
_AusArrayTable_Object = MibTable
ausArrayTable = _AusArrayTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1)
)
if mibBuilder.loadTexts:
    ausArrayTable.setStatus("mandatory")
_AusArrayEntry_Object = MibTableRow
ausArrayEntry = _AusArrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1)
)
ausArrayEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausArrayIndex"),
)
if mibBuilder.loadTexts:
    ausArrayEntry.setStatus("mandatory")
_AusArrayIndex_Type = Integer32
_AusArrayIndex_Object = MibTableColumn
ausArrayIndex = _AusArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 1),
    _AusArrayIndex_Type()
)
ausArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayIndex.setStatus("mandatory")
_AusArrayName_Type = DisplayString
_AusArrayName_Object = MibTableColumn
ausArrayName = _AusArrayName_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 2),
    _AusArrayName_Type()
)
ausArrayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayName.setStatus("mandatory")
_AusArrayCapacity_Type = Integer32
_AusArrayCapacity_Object = MibTableColumn
ausArrayCapacity = _AusArrayCapacity_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 3),
    _AusArrayCapacity_Type()
)
ausArrayCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayCapacity.setStatus("mandatory")


class _AusArrayType_Type(Integer32):
    """Custom type ausArrayType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("other", 2),
          ("raid-volume", 18),
          ("raid0", 3),
          ("raid1", 4),
          ("raid10", 10),
          ("raid1e", 16),
          ("raid2", 5),
          ("raid3", 6),
          ("raid4", 7),
          ("raid5", 8),
          ("raid50", 11),
          ("raid5ee", 17),
          ("raid6", 9),
          ("raid60", 19),
          ("unknown", 1),
          ("volume", 12),
          ("volume-of-raid0", 13),
          ("volume-of-raid1", 14),
          ("volume-of-raid5", 15))
    )


_AusArrayType_Type.__name__ = "Integer32"
_AusArrayType_Object = MibTableColumn
ausArrayType = _AusArrayType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 4),
    _AusArrayType_Type()
)
ausArrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayType.setStatus("mandatory")
_AusArrayStripeSize_Type = Integer32
_AusArrayStripeSize_Object = MibTableColumn
ausArrayStripeSize = _AusArrayStripeSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 5),
    _AusArrayStripeSize_Type()
)
ausArrayStripeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayStripeSize.setStatus("mandatory")


class _AusArrayTaskStatus_Type(Integer32):
    """Custom type ausArrayTaskStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("compaction", 10),
          ("copyback", 9),
          ("expansion", 11),
          ("modification", 8),
          ("noTaskActive", 3),
          ("other", 2),
          ("reconstruct", 4),
          ("snapshotBackup", 12),
          ("unknown", 1),
          ("verify", 6),
          ("verifyWithFix", 7),
          ("zeroInitialize", 5))
    )


_AusArrayTaskStatus_Type.__name__ = "Integer32"
_AusArrayTaskStatus_Object = MibTableColumn
ausArrayTaskStatus = _AusArrayTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 6),
    _AusArrayTaskStatus_Type()
)
ausArrayTaskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayTaskStatus.setStatus("mandatory")


class _AusArrayTaskCompletion_Type(Integer32):
    """Custom type ausArrayTaskCompletion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AusArrayTaskCompletion_Type.__name__ = "Integer32"
_AusArrayTaskCompletion_Object = MibTableColumn
ausArrayTaskCompletion = _AusArrayTaskCompletion_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 7),
    _AusArrayTaskCompletion_Type()
)
ausArrayTaskCompletion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayTaskCompletion.setStatus("mandatory")


class _AusArrayTaskPriority_Type(Integer32):
    """Custom type ausArrayTaskPriority based on Integer32"""
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
        *(("high", 8),
          ("low", 6),
          ("medium", 7),
          ("none", 5),
          ("notApplicable", 4),
          ("notSupported", 3),
          ("other", 2),
          ("unknown", 1))
    )


_AusArrayTaskPriority_Type.__name__ = "Integer32"
_AusArrayTaskPriority_Object = MibTableColumn
ausArrayTaskPriority = _AusArrayTaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 8),
    _AusArrayTaskPriority_Type()
)
ausArrayTaskPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayTaskPriority.setStatus("mandatory")


class _AusArrayHostingControllerType_Type(Integer32):
    """Custom type ausArrayHostingControllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregateController", 2),
          ("externalRaidController", 3),
          ("physicalController", 1))
    )


_AusArrayHostingControllerType_Type.__name__ = "Integer32"
_AusArrayHostingControllerType_Object = MibTableColumn
ausArrayHostingControllerType = _AusArrayHostingControllerType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 9),
    _AusArrayHostingControllerType_Type()
)
ausArrayHostingControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayHostingControllerType.setStatus("mandatory")
_AusArrayHostingControllerIndex_Type = Integer32
_AusArrayHostingControllerIndex_Object = MibTableColumn
ausArrayHostingControllerIndex = _AusArrayHostingControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 10),
    _AusArrayHostingControllerIndex_Type()
)
ausArrayHostingControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayHostingControllerIndex.setStatus("mandatory")
_AusArrayStatus_Type = ObjectStatus
_AusArrayStatus_Object = MibTableColumn
ausArrayStatus = _AusArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 11),
    _AusArrayStatus_Type()
)
ausArrayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayStatus.setStatus("mandatory")


class _AusArrayState_Type(Integer32):
    """Custom type ausArrayState based on Integer32"""
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
        *(("compacted", 8),
          ("degraded", 6),
          ("failed", 7),
          ("impacted", 5),
          ("optimal", 3),
          ("other", 2),
          ("quickInited", 4),
          ("unknown", 1))
    )


_AusArrayState_Type.__name__ = "Integer32"
_AusArrayState_Object = MibTableColumn
ausArrayState = _AusArrayState_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 12),
    _AusArrayState_Type()
)
ausArrayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayState.setStatus("mandatory")


class _AusArrayCacheStatus_Type(Integer32):
    """Custom type ausArrayCacheStatus based on Integer32"""
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
        *(("disabled", 3),
          ("other", 2),
          ("unknown", 1),
          ("writeBack", 4),
          ("writeThru", 5))
    )


_AusArrayCacheStatus_Type.__name__ = "Integer32"
_AusArrayCacheStatus_Object = MibTableColumn
ausArrayCacheStatus = _AusArrayCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 13),
    _AusArrayCacheStatus_Type()
)
ausArrayCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayCacheStatus.setStatus("mandatory")
_AusArrayMembership_Type = Integer32
_AusArrayMembership_Object = MibTableColumn
ausArrayMembership = _AusArrayMembership_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1000, 1, 1, 14),
    _AusArrayMembership_Type()
)
ausArrayMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausArrayMembership.setStatus("mandatory")
_AusExtent_ObjectIdentity = ObjectIdentity
ausExtent = _AusExtent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001)
)
_AusExtentTable_Object = MibTable
ausExtentTable = _AusExtentTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1)
)
if mibBuilder.loadTexts:
    ausExtentTable.setStatus("mandatory")
_AusExtentEntry_Object = MibTableRow
ausExtentEntry = _AusExtentEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1)
)
ausExtentEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausExtentIndex"),
)
if mibBuilder.loadTexts:
    ausExtentEntry.setStatus("mandatory")
_AusExtentIndex_Type = Integer32
_AusExtentIndex_Object = MibTableColumn
ausExtentIndex = _AusExtentIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 1),
    _AusExtentIndex_Type()
)
ausExtentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentIndex.setStatus("mandatory")
_AusExtentAusDeviceIndex_Type = Integer32
_AusExtentAusDeviceIndex_Object = MibTableColumn
ausExtentAusDeviceIndex = _AusExtentAusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 2),
    _AusExtentAusDeviceIndex_Type()
)
ausExtentAusDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentAusDeviceIndex.setStatus("mandatory")
_AusExtentSize_Type = Integer32
_AusExtentSize_Object = MibTableColumn
ausExtentSize = _AusExtentSize_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 3),
    _AusExtentSize_Type()
)
ausExtentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentSize.setStatus("mandatory")
_AusExtentStartingLBALow_Type = Integer32
_AusExtentStartingLBALow_Object = MibTableColumn
ausExtentStartingLBALow = _AusExtentStartingLBALow_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 4),
    _AusExtentStartingLBALow_Type()
)
ausExtentStartingLBALow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentStartingLBALow.setStatus("mandatory")
_AusExtentStartingLBAHigh_Type = Integer32
_AusExtentStartingLBAHigh_Object = MibTableColumn
ausExtentStartingLBAHigh = _AusExtentStartingLBAHigh_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 5),
    _AusExtentStartingLBAHigh_Type()
)
ausExtentStartingLBAHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentStartingLBAHigh.setStatus("mandatory")
_AusExtentNumberOfBlocksLow_Type = Integer32
_AusExtentNumberOfBlocksLow_Object = MibTableColumn
ausExtentNumberOfBlocksLow = _AusExtentNumberOfBlocksLow_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 6),
    _AusExtentNumberOfBlocksLow_Type()
)
ausExtentNumberOfBlocksLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentNumberOfBlocksLow.setStatus("mandatory")
_AusExtentNumberOfBlocksHigh_Type = Integer32
_AusExtentNumberOfBlocksHigh_Object = MibTableColumn
ausExtentNumberOfBlocksHigh = _AusExtentNumberOfBlocksHigh_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 7),
    _AusExtentNumberOfBlocksHigh_Type()
)
ausExtentNumberOfBlocksHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentNumberOfBlocksHigh.setStatus("mandatory")
_AusExtentArrayMembership_Type = Integer32
_AusExtentArrayMembership_Object = MibTableColumn
ausExtentArrayMembership = _AusExtentArrayMembership_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1001, 1, 1, 8),
    _AusExtentArrayMembership_Type()
)
ausExtentArrayMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausExtentArrayMembership.setStatus("mandatory")
_AusSpare_ObjectIdentity = ObjectIdentity
ausSpare = _AusSpare_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002)
)
_AusSpareTable_Object = MibTable
ausSpareTable = _AusSpareTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1)
)
if mibBuilder.loadTexts:
    ausSpareTable.setStatus("mandatory")
_AusSpareEntry_Object = MibTableRow
ausSpareEntry = _AusSpareEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1, 1)
)
ausSpareEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausSpareIndex"),
)
if mibBuilder.loadTexts:
    ausSpareEntry.setStatus("mandatory")
_AusSpareIndex_Type = Integer32
_AusSpareIndex_Object = MibTableColumn
ausSpareIndex = _AusSpareIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1, 1, 1),
    _AusSpareIndex_Type()
)
ausSpareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausSpareIndex.setStatus("mandatory")
_AusSpareAusDeviceIndex_Type = Integer32
_AusSpareAusDeviceIndex_Object = MibTableColumn
ausSpareAusDeviceIndex = _AusSpareAusDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1, 1, 2),
    _AusSpareAusDeviceIndex_Type()
)
ausSpareAusDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausSpareAusDeviceIndex.setStatus("mandatory")


class _AusSpareType_Type(Integer32):
    """Custom type ausSpareType based on Integer32"""
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
        *(("dedicated", 2),
          ("externalRaidGlobal", 3),
          ("global", 1),
          ("other", 5),
          ("standby", 6),
          ("unknown", 4))
    )


_AusSpareType_Type.__name__ = "Integer32"
_AusSpareType_Object = MibTableColumn
ausSpareType = _AusSpareType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1, 1, 3),
    _AusSpareType_Type()
)
ausSpareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausSpareType.setStatus("mandatory")
_AusSpareAusControllerOrArrayIndex_Type = Integer32
_AusSpareAusControllerOrArrayIndex_Object = MibTableColumn
ausSpareAusControllerOrArrayIndex = _AusSpareAusControllerOrArrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 1002, 1, 1, 4),
    _AusSpareAusControllerOrArrayIndex_Type()
)
ausSpareAusControllerOrArrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausSpareAusControllerOrArrayIndex.setStatus("mandatory")
_AusEventLogCount_ObjectIdentity = ObjectIdentity
ausEventLogCount = _AusEventLogCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2000)
)
_AusEventLogNumEntries_Type = Integer32
_AusEventLogNumEntries_Object = MibScalar
ausEventLogNumEntries = _AusEventLogNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2000, 1),
    _AusEventLogNumEntries_Type()
)
ausEventLogNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEventLogNumEntries.setStatus("mandatory")
_AusEventLog_ObjectIdentity = ObjectIdentity
ausEventLog = _AusEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001)
)
_AusEventLogTable_Object = MibTable
ausEventLogTable = _AusEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001, 1)
)
if mibBuilder.loadTexts:
    ausEventLogTable.setStatus("mandatory")
_AusEventLogEntry_Object = MibTableRow
ausEventLogEntry = _AusEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001, 1, 1)
)
ausEventLogEntry.setIndexNames(
    (0, "ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausEventLogIndex"),
)
if mibBuilder.loadTexts:
    ausEventLogEntry.setStatus("mandatory")
_AusEventLogIndex_Type = Integer32
_AusEventLogIndex_Object = MibTableColumn
ausEventLogIndex = _AusEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001, 1, 1, 1),
    _AusEventLogIndex_Type()
)
ausEventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEventLogIndex.setStatus("mandatory")
_AusEventLogString_Type = DisplayString
_AusEventLogString_Object = MibTableColumn
ausEventLogString = _AusEventLogString_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001, 1, 1, 2),
    _AusEventLogString_Type()
)
ausEventLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEventLogString.setStatus("mandatory")
_AusEventLogTimeStamp_Type = Integer32
_AusEventLogTimeStamp_Object = MibTableColumn
ausEventLogTimeStamp = _AusEventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 2001, 1, 1, 3),
    _AusEventLogTimeStamp_Type()
)
ausEventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ausEventLogTimeStamp.setStatus("mandatory")
_AusTrapObjects_ObjectIdentity = ObjectIdentity
ausTrapObjects = _AusTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000)
)
_AusTrapMessage_Type = DisplayString
_AusTrapMessage_Object = MibScalar
ausTrapMessage = _AusTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 1),
    _AusTrapMessage_Type()
)
ausTrapMessage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapMessage.setStatus("mandatory")
_AusTrapObjectIndex_Type = Integer32
_AusTrapObjectIndex_Object = MibScalar
ausTrapObjectIndex = _AusTrapObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 2),
    _AusTrapObjectIndex_Type()
)
ausTrapObjectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapObjectIndex.setStatus("mandatory")


class _AusTrapControllerType_Type(Integer32):
    """Custom type ausTrapControllerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aggregateController", 1),
          ("externalController", 3),
          ("internalController", 2))
    )


_AusTrapControllerType_Type.__name__ = "Integer32"
_AusTrapControllerType_Object = MibScalar
ausTrapControllerType = _AusTrapControllerType_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 3),
    _AusTrapControllerType_Type()
)
ausTrapControllerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapControllerType.setStatus("mandatory")


class _AusTrapControllerStatus_Type(Integer32):
    """Custom type ausTrapControllerStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("cannotReadControllerInformation", 7),
          ("commandsNotResponding", 6),
          ("controllerAdded", 3),
          ("controllerDeleted", 4),
          ("controllerFailover", 5),
          ("defectiveCache", 9),
          ("firmwareVersionMismatch", 10),
          ("noControllersFound", 2),
          ("okay", 1),
          ("replaceBattery", 8))
    )


_AusTrapControllerStatus_Type.__name__ = "Integer32"
_AusTrapControllerStatus_Object = MibScalar
ausTrapControllerStatus = _AusTrapControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 4),
    _AusTrapControllerStatus_Type()
)
ausTrapControllerStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapControllerStatus.setStatus("mandatory")


class _AusTrapDeviceStatus_Type(Integer32):
    """Custom type ausTrapDeviceStatus based on Integer32"""
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
        *(("deviceAdded", 2),
          ("deviceFailed", 4),
          ("deviceRemoved", 3),
          ("okay", 1),
          ("smartEvent", 5),
          ("unsupportedDeviceType", 6))
    )


_AusTrapDeviceStatus_Type.__name__ = "Integer32"
_AusTrapDeviceStatus_Object = MibScalar
ausTrapDeviceStatus = _AusTrapDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 5),
    _AusTrapDeviceStatus_Type()
)
ausTrapDeviceStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapDeviceStatus.setStatus("mandatory")


class _AusTrapEnclosureStatus_Type(Integer32):
    """Custom type ausTrapEnclosureStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("enclosureNotResponding", 2),
          ("enclosureResponding", 1),
          ("fanInstalled", 6),
          ("fanMalfunction", 3),
          ("fanOperational", 4),
          ("fanRemoved", 5),
          ("powerSupplyInstalled", 12),
          ("powerSupplyMalfunction", 9),
          ("powerSupplyOperational", 10),
          ("powerSupplyRemoved", 11),
          ("temperatureInRange", 7),
          ("temperatureOutOfRange", 8))
    )


_AusTrapEnclosureStatus_Type.__name__ = "Integer32"
_AusTrapEnclosureStatus_Object = MibScalar
ausTrapEnclosureStatus = _AusTrapEnclosureStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 6),
    _AusTrapEnclosureStatus_Type()
)
ausTrapEnclosureStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapEnclosureStatus.setStatus("mandatory")
_AusTrapEnclosureObjectOrdinal_Type = Integer32
_AusTrapEnclosureObjectOrdinal_Object = MibScalar
ausTrapEnclosureObjectOrdinal = _AusTrapEnclosureObjectOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 7),
    _AusTrapEnclosureObjectOrdinal_Type()
)
ausTrapEnclosureObjectOrdinal.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapEnclosureObjectOrdinal.setStatus("mandatory")


class _AusTrapArrayStatus_Type(Integer32):
    """Custom type ausTrapArrayStatus based on Integer32"""
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
        *(("blocked", 4),
          ("critical", 2),
          ("offline", 3),
          ("okay", 1),
          ("unblocked", 5))
    )


_AusTrapArrayStatus_Type.__name__ = "Integer32"
_AusTrapArrayStatus_Object = MibScalar
ausTrapArrayStatus = _AusTrapArrayStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 8),
    _AusTrapArrayStatus_Type()
)
ausTrapArrayStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapArrayStatus.setStatus("mandatory")


class _AusTrapArrayTaskStatus_Type(Integer32):
    """Custom type ausTrapArrayTaskStatus based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("compacting", 16),
          ("compactionComplete", 17),
          ("compactionFailed", 18),
          ("compressing", 10),
          ("compressionComplete", 11),
          ("compressionFailed", 12),
          ("decompressing", 13),
          ("decompressionComplete", 14),
          ("decompressionFailed", 15),
          ("expanding", 19),
          ("expansionComplete", 20),
          ("expansionFailed", 21),
          ("flashCopyComplete", 23),
          ("flashCopyFailed", 24),
          ("flashCopying", 22),
          ("migrating", 7),
          ("migrationComplete", 8),
          ("migrationFailed", 9),
          ("rebuildComplete", 2),
          ("rebuildFailed", 3),
          ("rebuilding", 1),
          ("synchronizationComplete", 5),
          ("synchronizationFailed", 6),
          ("synchronizing", 4))
    )


_AusTrapArrayTaskStatus_Type.__name__ = "Integer32"
_AusTrapArrayTaskStatus_Object = MibScalar
ausTrapArrayTaskStatus = _AusTrapArrayTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 9),
    _AusTrapArrayTaskStatus_Type()
)
ausTrapArrayTaskStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapArrayTaskStatus.setStatus("mandatory")


class _AusTrapSpareStatus_Type(Integer32):
    """Custom type ausTrapSpareStatus based on Integer32"""
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
        *(("added", 2),
          ("deleted", 3),
          ("failed", 4),
          ("okay", 1))
    )


_AusTrapSpareStatus_Type.__name__ = "Integer32"
_AusTrapSpareStatus_Object = MibScalar
ausTrapSpareStatus = _AusTrapSpareStatus_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 10),
    _AusTrapSpareStatus_Type()
)
ausTrapSpareStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapSpareStatus.setStatus("mandatory")
_AusTrapEnumAsText_Type = DisplayString
_AusTrapEnumAsText_Object = MibScalar
ausTrapEnumAsText = _AusTrapEnumAsText_Object(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 9000, 11),
    _AusTrapEnumAsText_Type()
)
ausTrapEnumAsText.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ausTrapEnumAsText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

ausTrapOtherInformational = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1001)
)
ausTrapOtherInformational.setObjects(
    ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapMessage")
)
if mibBuilder.loadTexts:
    ausTrapOtherInformational.setStatus(
        ""
    )

ausTrapOtherWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1002)
)
ausTrapOtherWarning.setObjects(
    ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapMessage")
)
if mibBuilder.loadTexts:
    ausTrapOtherWarning.setStatus(
        ""
    )

ausTrapOtherFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1003)
)
ausTrapOtherFatal.setObjects(
    ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapMessage")
)
if mibBuilder.loadTexts:
    ausTrapOtherFatal.setStatus(
        ""
    )

ausTrapDeviceInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1010)
)
ausTrapDeviceInformation.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapDeviceStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapDeviceInformation.setStatus(
        ""
    )

ausTrapDeviceWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1011)
)
ausTrapDeviceWarning.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapDeviceStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapDeviceWarning.setStatus(
        ""
    )

ausTrapDeviceFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1012)
)
ausTrapDeviceFatal.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapDeviceStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapDeviceFatal.setStatus(
        ""
    )

ausTrapEnclosureInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1020)
)
ausTrapEnclosureInformation.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureObjectOrdinal"))
)
if mibBuilder.loadTexts:
    ausTrapEnclosureInformation.setStatus(
        ""
    )

ausTrapEnclosureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1021)
)
ausTrapEnclosureWarning.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureObjectOrdinal"))
)
if mibBuilder.loadTexts:
    ausTrapEnclosureWarning.setStatus(
        ""
    )

ausTrapEnclosureFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1022)
)
ausTrapEnclosureFatal.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnclosureObjectOrdinal"))
)
if mibBuilder.loadTexts:
    ausTrapEnclosureFatal.setStatus(
        ""
    )

ausTrapArrayInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1030)
)
ausTrapArrayInformation.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayInformation.setStatus(
        ""
    )

ausTrapArrayWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1031)
)
ausTrapArrayWarning.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayWarning.setStatus(
        ""
    )

ausTrapArrayFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1032)
)
ausTrapArrayFatal.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayFatal.setStatus(
        ""
    )

ausTrapArrayTaskInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1040)
)
ausTrapArrayTaskInformation.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayTaskStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayTaskInformation.setStatus(
        ""
    )

ausTrapArrayTaskWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1041)
)
ausTrapArrayTaskWarning.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayTaskStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayTaskWarning.setStatus(
        ""
    )

ausTrapArrayTaskFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1042)
)
ausTrapArrayTaskFatal.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapArrayTaskStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapArrayTaskFatal.setStatus(
        ""
    )

ausTrapSpareInformation = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1050)
)
ausTrapSpareInformation.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapSpareStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapSpareInformation.setStatus(
        ""
    )

ausTrapSpareWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1051)
)
ausTrapSpareWarning.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapSpareStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapSpareWarning.setStatus(
        ""
    )

ausTrapSpareFatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 795, 14, 1, 0, 1052)
)
ausTrapSpareFatal.setObjects(
      *(("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapObjectIndex"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapSpareStatus"),
        ("ADAPTEC-UNIVERSAL-STORAGE-MIB", "ausTrapEnumAsText"))
)
if mibBuilder.loadTexts:
    ausTrapSpareFatal.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADAPTEC-UNIVERSAL-STORAGE-MIB",
    **{"TriState": TriState,
       "ObjectStatus": ObjectStatus,
       "OptionStatus": OptionStatus,
       "BatteryStatus": BatteryStatus,
       "IndexList": IndexList,
       "adaptec": adaptec,
       "universalStorage": universalStorage,
       "ausMIB": ausMIB,
       "ausTrapOtherInformational": ausTrapOtherInformational,
       "ausTrapOtherWarning": ausTrapOtherWarning,
       "ausTrapOtherFatal": ausTrapOtherFatal,
       "ausTrapDeviceInformation": ausTrapDeviceInformation,
       "ausTrapDeviceWarning": ausTrapDeviceWarning,
       "ausTrapDeviceFatal": ausTrapDeviceFatal,
       "ausTrapEnclosureInformation": ausTrapEnclosureInformation,
       "ausTrapEnclosureWarning": ausTrapEnclosureWarning,
       "ausTrapEnclosureFatal": ausTrapEnclosureFatal,
       "ausTrapArrayInformation": ausTrapArrayInformation,
       "ausTrapArrayWarning": ausTrapArrayWarning,
       "ausTrapArrayFatal": ausTrapArrayFatal,
       "ausTrapArrayTaskInformation": ausTrapArrayTaskInformation,
       "ausTrapArrayTaskWarning": ausTrapArrayTaskWarning,
       "ausTrapArrayTaskFatal": ausTrapArrayTaskFatal,
       "ausTrapSpareInformation": ausTrapSpareInformation,
       "ausTrapSpareWarning": ausTrapSpareWarning,
       "ausTrapSpareFatal": ausTrapSpareFatal,
       "ausMibStatus": ausMibStatus,
       "ausMibStatusRevMajor": ausMibStatusRevMajor,
       "ausMibStatusRevMinor": ausMibStatusRevMinor,
       "ausMibStatusSecondsSinceInitiation": ausMibStatusSecondsSinceInitiation,
       "ausMibStatusCopyright": ausMibStatusCopyright,
       "ausMibStatusOverall": ausMibStatusOverall,
       "ausAggregatedController": ausAggregatedController,
       "ausAggregatedControllerTable": ausAggregatedControllerTable,
       "ausAggregatedControllerEntry": ausAggregatedControllerEntry,
       "ausAggregatedControllerIndex": ausAggregatedControllerIndex,
       "ausAggregatedControllerList": ausAggregatedControllerList,
       "ausController": ausController,
       "ausControllerTable": ausControllerTable,
       "ausControllerEntry": ausControllerEntry,
       "ausControllerIndex": ausControllerIndex,
       "ausControllerUniqueId": ausControllerUniqueId,
       "ausControllerVendor": ausControllerVendor,
       "ausControllerModel": ausControllerModel,
       "ausControllerRevision": ausControllerRevision,
       "ausControllerSerialNumber": ausControllerSerialNumber,
       "ausControllerDescription": ausControllerDescription,
       "ausControllerHostBusType": ausControllerHostBusType,
       "ausControllerHostBusMaximumTransferRate": ausControllerHostBusMaximumTransferRate,
       "ausControllerNumberOfChannels": ausControllerNumberOfChannels,
       "ausControllerHighestChannelWithDevices": ausControllerHighestChannelWithDevices,
       "ausControllerInstalledMemory": ausControllerInstalledMemory,
       "ausControllerAudibleAlarmStatus": ausControllerAudibleAlarmStatus,
       "ausControllerBatteryStatus": ausControllerBatteryStatus,
       "ausControllerStatus": ausControllerStatus,
       "ausControllerOverallStatus": ausControllerOverallStatus,
       "ausControllerRelationship": ausControllerRelationship,
       "ausControllerRelationshipTable": ausControllerRelationshipTable,
       "ausControllerRelationshipEntry": ausControllerRelationshipEntry,
       "ausControllerRelationshipIndex": ausControllerRelationshipIndex,
       "ausControllerRelationshipType": ausControllerRelationshipType,
       "ausControllerRelationshipList": ausControllerRelationshipList,
       "ausControllerRelationshipRelation": ausControllerRelationshipRelation,
       "ausI2ORaidController": ausI2ORaidController,
       "ausI2ORaidControllerTable": ausI2ORaidControllerTable,
       "ausI2ORaidControllerEntry": ausI2ORaidControllerEntry,
       "ausI2ORaidControllerIndex": ausI2ORaidControllerIndex,
       "ausI2ORaidControllerAddress": ausI2ORaidControllerAddress,
       "ausI2ORaidControllerBackgroundTaskPriority": ausI2ORaidControllerBackgroundTaskPriority,
       "ausI2ORaidControllerBiosRevision": ausI2ORaidControllerBiosRevision,
       "ausI2ORaidControllerSmorRevision": ausI2ORaidControllerSmorRevision,
       "ausI2ORaidControllerMainIndex": ausI2ORaidControllerMainIndex,
       "ausCCodeController": ausCCodeController,
       "ausCCodeControllerTable": ausCCodeControllerTable,
       "ausCCodeControllerEntry": ausCCodeControllerEntry,
       "ausCCodeControllerIndex": ausCCodeControllerIndex,
       "ausCCodeControllerPCIBusId": ausCCodeControllerPCIBusId,
       "ausCCodeControllerPCISlotNumber": ausCCodeControllerPCISlotNumber,
       "ausCCodeControllerBiosVersion": ausCCodeControllerBiosVersion,
       "ausCCodeControllerMainIndex": ausCCodeControllerMainIndex,
       "ausHostRAIDController": ausHostRAIDController,
       "ausHostRAIDControllerTable": ausHostRAIDControllerTable,
       "ausHostRAIDControllerEntry": ausHostRAIDControllerEntry,
       "ausHostRAIDControllerIndex": ausHostRAIDControllerIndex,
       "ausHostRAIDControllerPCIBus": ausHostRAIDControllerPCIBus,
       "ausHostRAIDControllerPCIDevice": ausHostRAIDControllerPCIDevice,
       "ausHostRAIDControllerPCIFunction": ausHostRAIDControllerPCIFunction,
       "ausHostRAIDControllerMainIndex": ausHostRAIDControllerMainIndex,
       "ausServeRAIDController": ausServeRAIDController,
       "ausServeRAIDControllerTable": ausServeRAIDControllerTable,
       "ausServeRAIDControllerEntry": ausServeRAIDControllerEntry,
       "ausServeRAIDControllerIndex": ausServeRAIDControllerIndex,
       "ausServeRAIDControllerBIOSRevision": ausServeRAIDControllerBIOSRevision,
       "ausServeRAIDControllerDefaultRebuildRate": ausServeRAIDControllerDefaultRebuildRate,
       "ausServeRAIDControllerSlotNumber": ausServeRAIDControllerSlotNumber,
       "ausServeRAIDControllerMainIndex": ausServeRAIDControllerMainIndex,
       "ausChannel": ausChannel,
       "ausChannelTable": ausChannelTable,
       "ausChannelEntry": ausChannelEntry,
       "ausChannelIndex": ausChannelIndex,
       "ausChannelLocation": ausChannelLocation,
       "ausChannelAusControllerIndex": ausChannelAusControllerIndex,
       "ausChannelAusControllerChannelNumber": ausChannelAusControllerChannelNumber,
       "ausChannelType": ausChannelType,
       "ausChannelTypeDescription": ausChannelTypeDescription,
       "ausChannelControllerId": ausChannelControllerId,
       "ausChannelControllerSubId": ausChannelControllerSubId,
       "ausChannelWidth": ausChannelWidth,
       "ausChannelMaximumTransferRate": ausChannelMaximumTransferRate,
       "ausChannelMaximumAttachments": ausChannelMaximumAttachments,
       "ausChannelOverallStatus": ausChannelOverallStatus,
       "ausChannelRelationship": ausChannelRelationship,
       "ausChannelRelationshipTable": ausChannelRelationshipTable,
       "ausChannelRelationshipEntry": ausChannelRelationshipEntry,
       "ausChannelRelationshipIndex": ausChannelRelationshipIndex,
       "ausChannelRelationshipList": ausChannelRelationshipList,
       "ausChannelRelationshipRelation": ausChannelRelationshipRelation,
       "ausDevice": ausDevice,
       "ausDeviceTable": ausDeviceTable,
       "ausDeviceEntry": ausDeviceEntry,
       "ausDeviceIndex": ausDeviceIndex,
       "ausDeviceUniqueId": ausDeviceUniqueId,
       "ausDeviceAusChannelIndices": ausDeviceAusChannelIndices,
       "ausDeviceType": ausDeviceType,
       "ausDeviceTypeGroup": ausDeviceTypeGroup,
       "ausDeviceVendor": ausDeviceVendor,
       "ausDeviceModel": ausDeviceModel,
       "ausDeviceRevision": ausDeviceRevision,
       "ausDeviceSerialNumber": ausDeviceSerialNumber,
       "ausDeviceNumberOfPorts": ausDeviceNumberOfPorts,
       "ausDeviceStatus": ausDeviceStatus,
       "ausDevicePort": ausDevicePort,
       "ausDevicePortTable": ausDevicePortTable,
       "ausDevicePortEntry": ausDevicePortEntry,
       "ausDevicePortIndex": ausDevicePortIndex,
       "ausDevicePortUniqueId": ausDevicePortUniqueId,
       "ausDevicePortAusDeviceIndex": ausDevicePortAusDeviceIndex,
       "ausDevicePortAusDevicePortNumber": ausDevicePortAusDevicePortNumber,
       "ausDevicePortAusChannelIndex": ausDevicePortAusChannelIndex,
       "ausDevicePortId": ausDevicePortId,
       "ausDevicePortSubId": ausDevicePortSubId,
       "ausDevicePortWidth": ausDevicePortWidth,
       "ausDevicePortMaximumTransferRate": ausDevicePortMaximumTransferRate,
       "ausDevicePortNegotiatedTransferRate": ausDevicePortNegotiatedTransferRate,
       "ausDevicePortStatus": ausDevicePortStatus,
       "ausStorageDevice": ausStorageDevice,
       "ausStorageDeviceTable": ausStorageDeviceTable,
       "ausStorageDeviceEntry": ausStorageDeviceEntry,
       "ausStorageDeviceIndex": ausStorageDeviceIndex,
       "ausStorageDeviceDescription": ausStorageDeviceDescription,
       "ausStorageDeviceFormattedCapacity": ausStorageDeviceFormattedCapacity,
       "ausStorageDeviceBlockSize": ausStorageDeviceBlockSize,
       "ausStorageDeviceNumberOfBlocksLow": ausStorageDeviceNumberOfBlocksLow,
       "ausStorageDeviceNumberOfBlocksHigh": ausStorageDeviceNumberOfBlocksHigh,
       "ausStorageDeviceRemovableMedia": ausStorageDeviceRemovableMedia,
       "ausStorageDeviceSmartStatus": ausStorageDeviceSmartStatus,
       "ausStorageDeviceMainIndex": ausStorageDeviceMainIndex,
       "ausEnclosureDevice": ausEnclosureDevice,
       "ausEnclosureDeviceTable": ausEnclosureDeviceTable,
       "ausEnclosureDeviceEntry": ausEnclosureDeviceEntry,
       "ausEnclosureDeviceIndex": ausEnclosureDeviceIndex,
       "ausEnclosureDeviceDescription": ausEnclosureDeviceDescription,
       "ausEnclosureDeviceProcessorType": ausEnclosureDeviceProcessorType,
       "ausEnclosureDeviceNumberOfFans": ausEnclosureDeviceNumberOfFans,
       "ausEnclosureDeviceNumberOfPowerSupplies": ausEnclosureDeviceNumberOfPowerSupplies,
       "ausEnclosureDeviceNumberOfSlots": ausEnclosureDeviceNumberOfSlots,
       "ausEnclosureDeviceNumberOfTemperatureSensors": ausEnclosureDeviceNumberOfTemperatureSensors,
       "ausEnclosureDeviceIdLow": ausEnclosureDeviceIdLow,
       "ausEnclosureDeviceIdHigh": ausEnclosureDeviceIdHigh,
       "ausEnclosureDeviceStandardRevision": ausEnclosureDeviceStandardRevision,
       "ausEnclosureDevicePowerOnTime": ausEnclosureDevicePowerOnTime,
       "ausEnclosureDevicePowerCycles": ausEnclosureDevicePowerCycles,
       "ausEnclosureDeviceDoorLock": ausEnclosureDeviceDoorLock,
       "ausEnclosureDeviceSpeaker": ausEnclosureDeviceSpeaker,
       "ausEnclosureDeviceTemperatureState": ausEnclosureDeviceTemperatureState,
       "ausEnclosureDeviceMainIndex": ausEnclosureDeviceMainIndex,
       "ausExternalRaidDevice": ausExternalRaidDevice,
       "ausExternalRaidDeviceTable": ausExternalRaidDeviceTable,
       "ausExternalRaidDeviceEntry": ausExternalRaidDeviceEntry,
       "ausExternalRaidDeviceIndex": ausExternalRaidDeviceIndex,
       "ausExternalRaidDeviceDescription": ausExternalRaidDeviceDescription,
       "ausExternalRaidDeviceNumberOfChannels": ausExternalRaidDeviceNumberOfChannels,
       "ausExternalRaidDeviceInstalledMemory": ausExternalRaidDeviceInstalledMemory,
       "ausExternalRaidDeviceAudibleAlarmStatus": ausExternalRaidDeviceAudibleAlarmStatus,
       "ausExternalRaidDeviceBatteryStatus": ausExternalRaidDeviceBatteryStatus,
       "ausExternalRaidDeviceMainIndex": ausExternalRaidDeviceMainIndex,
       "ausOtherDevice": ausOtherDevice,
       "ausOtherDeviceTable": ausOtherDeviceTable,
       "ausOtherDeviceEntry": ausOtherDeviceEntry,
       "ausOtherDeviceIndex": ausOtherDeviceIndex,
       "ausOtherDeviceDescription": ausOtherDeviceDescription,
       "ausOtherDeviceMainIndex": ausOtherDeviceMainIndex,
       "ausEnclosureFan": ausEnclosureFan,
       "ausEnclosureFanTable": ausEnclosureFanTable,
       "ausEnclosureFanEntry": ausEnclosureFanEntry,
       "ausEnclosureFanIndex": ausEnclosureFanIndex,
       "ausEnclosureFanAusEnclosureDeviceIndex": ausEnclosureFanAusEnclosureDeviceIndex,
       "ausEnclosureFanOrdinal": ausEnclosureFanOrdinal,
       "ausEnclosureFanSpeed": ausEnclosureFanSpeed,
       "ausEnclosureFanStatus": ausEnclosureFanStatus,
       "ausEnclosurePowerSupply": ausEnclosurePowerSupply,
       "ausEnclosurePowerSupplyTable": ausEnclosurePowerSupplyTable,
       "ausEnclosurePowerSupplyEntry": ausEnclosurePowerSupplyEntry,
       "ausEnclosurePowerSupplyIndex": ausEnclosurePowerSupplyIndex,
       "ausEnclosurePowerSupplyAusEnclosureDeviceIndex": ausEnclosurePowerSupplyAusEnclosureDeviceIndex,
       "ausEnclosurePowerSupplyOrdinal": ausEnclosurePowerSupplyOrdinal,
       "ausEnclosurePowerSupplyStatus": ausEnclosurePowerSupplyStatus,
       "ausEnclosureTemperatureSensor": ausEnclosureTemperatureSensor,
       "ausEnclosureTemperatureSensorTable": ausEnclosureTemperatureSensorTable,
       "ausEnclosureTemperatureSensorEntry": ausEnclosureTemperatureSensorEntry,
       "ausEnclosureTemperatureSensorIndex": ausEnclosureTemperatureSensorIndex,
       "ausEnclosureTemperatureSensorAusEnclosureDeviceIndex": ausEnclosureTemperatureSensorAusEnclosureDeviceIndex,
       "ausEnclosureTemperatureSensorOrdinal": ausEnclosureTemperatureSensorOrdinal,
       "ausEnclosureTemperatureSensorOverTemperature": ausEnclosureTemperatureSensorOverTemperature,
       "ausEnclosureTemperatureSensorDegrees": ausEnclosureTemperatureSensorDegrees,
       "ausEnclosureSlot": ausEnclosureSlot,
       "ausEnclosureSlotTable": ausEnclosureSlotTable,
       "ausEnclosureSlotEntry": ausEnclosureSlotEntry,
       "ausEnclosureSlotIndex": ausEnclosureSlotIndex,
       "ausEnclosureSlotAusEnclosureDeviceIndex": ausEnclosureSlotAusEnclosureDeviceIndex,
       "ausEnclosureSlotOrdinal": ausEnclosureSlotOrdinal,
       "ausEnclosureSlotPortId": ausEnclosureSlotPortId,
       "ausEnclosureSlotInsertions": ausEnclosureSlotInsertions,
       "ausArray": ausArray,
       "ausArrayTable": ausArrayTable,
       "ausArrayEntry": ausArrayEntry,
       "ausArrayIndex": ausArrayIndex,
       "ausArrayName": ausArrayName,
       "ausArrayCapacity": ausArrayCapacity,
       "ausArrayType": ausArrayType,
       "ausArrayStripeSize": ausArrayStripeSize,
       "ausArrayTaskStatus": ausArrayTaskStatus,
       "ausArrayTaskCompletion": ausArrayTaskCompletion,
       "ausArrayTaskPriority": ausArrayTaskPriority,
       "ausArrayHostingControllerType": ausArrayHostingControllerType,
       "ausArrayHostingControllerIndex": ausArrayHostingControllerIndex,
       "ausArrayStatus": ausArrayStatus,
       "ausArrayState": ausArrayState,
       "ausArrayCacheStatus": ausArrayCacheStatus,
       "ausArrayMembership": ausArrayMembership,
       "ausExtent": ausExtent,
       "ausExtentTable": ausExtentTable,
       "ausExtentEntry": ausExtentEntry,
       "ausExtentIndex": ausExtentIndex,
       "ausExtentAusDeviceIndex": ausExtentAusDeviceIndex,
       "ausExtentSize": ausExtentSize,
       "ausExtentStartingLBALow": ausExtentStartingLBALow,
       "ausExtentStartingLBAHigh": ausExtentStartingLBAHigh,
       "ausExtentNumberOfBlocksLow": ausExtentNumberOfBlocksLow,
       "ausExtentNumberOfBlocksHigh": ausExtentNumberOfBlocksHigh,
       "ausExtentArrayMembership": ausExtentArrayMembership,
       "ausSpare": ausSpare,
       "ausSpareTable": ausSpareTable,
       "ausSpareEntry": ausSpareEntry,
       "ausSpareIndex": ausSpareIndex,
       "ausSpareAusDeviceIndex": ausSpareAusDeviceIndex,
       "ausSpareType": ausSpareType,
       "ausSpareAusControllerOrArrayIndex": ausSpareAusControllerOrArrayIndex,
       "ausEventLogCount": ausEventLogCount,
       "ausEventLogNumEntries": ausEventLogNumEntries,
       "ausEventLog": ausEventLog,
       "ausEventLogTable": ausEventLogTable,
       "ausEventLogEntry": ausEventLogEntry,
       "ausEventLogIndex": ausEventLogIndex,
       "ausEventLogString": ausEventLogString,
       "ausEventLogTimeStamp": ausEventLogTimeStamp,
       "ausTrapObjects": ausTrapObjects,
       "ausTrapMessage": ausTrapMessage,
       "ausTrapObjectIndex": ausTrapObjectIndex,
       "ausTrapControllerType": ausTrapControllerType,
       "ausTrapControllerStatus": ausTrapControllerStatus,
       "ausTrapDeviceStatus": ausTrapDeviceStatus,
       "ausTrapEnclosureStatus": ausTrapEnclosureStatus,
       "ausTrapEnclosureObjectOrdinal": ausTrapEnclosureObjectOrdinal,
       "ausTrapArrayStatus": ausTrapArrayStatus,
       "ausTrapArrayTaskStatus": ausTrapArrayTaskStatus,
       "ausTrapSpareStatus": ausTrapSpareStatus,
       "ausTrapEnumAsText": ausTrapEnumAsText}
)
