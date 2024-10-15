# SNMP MIB module (SUN-FM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-FM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:32 2024
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

(URLString,) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "URLString")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(products,) = mibBuilder.importSymbols(
    "SUN-MIB",
    "products")


# MODULE-IDENTITY

sunFmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1)
)
sunFmMIB.setRevisions(
        ("2008-08-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SunFmUuidString(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



class SunFmModuleState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("failed", 3),
          ("other", 1))
    )



class SunFmResourceState(Integer32, TextualConvention):
    status = "current"
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
        *(("degraded", 3),
          ("faulted", 5),
          ("ok", 2),
          ("other", 1),
          ("unknown", 4))
    )



class SunFmEventState(Integer32, TextualConvention):
    status = "current"
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
        *(("acquitted", 6),
          ("faulty", 2),
          ("other", 1),
          ("removed", 3),
          ("repaired", 5),
          ("replaced", 4))
    )



# MIB Managed Objects in the order of their OIDs

_Fm_ObjectIdentity = ObjectIdentity
fm = _Fm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 195)
)
_SunFmProblemTable_Object = MibTable
sunFmProblemTable = _SunFmProblemTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1)
)
if mibBuilder.loadTexts:
    sunFmProblemTable.setStatus("current")
_SunFmProblemEntry_Object = MibTableRow
sunFmProblemEntry = _SunFmProblemEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1)
)
sunFmProblemEntry.setIndexNames(
    (0, "SUN-FM-MIB", "sunFmProblemUUIDIndex"),
)
if mibBuilder.loadTexts:
    sunFmProblemEntry.setStatus("current")
_SunFmProblemUUIDIndex_Type = SunFmUuidString
_SunFmProblemUUIDIndex_Object = MibTableColumn
sunFmProblemUUIDIndex = _SunFmProblemUUIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 1),
    _SunFmProblemUUIDIndex_Type()
)
sunFmProblemUUIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunFmProblemUUIDIndex.setStatus("current")
_SunFmProblemUUID_Type = SunFmUuidString
_SunFmProblemUUID_Object = MibTableColumn
sunFmProblemUUID = _SunFmProblemUUID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 2),
    _SunFmProblemUUID_Type()
)
sunFmProblemUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemUUID.setStatus("current")
_SunFmProblemCode_Type = DisplayString
_SunFmProblemCode_Object = MibTableColumn
sunFmProblemCode = _SunFmProblemCode_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 3),
    _SunFmProblemCode_Type()
)
sunFmProblemCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemCode.setStatus("current")
_SunFmProblemURL_Type = URLString
_SunFmProblemURL_Object = MibTableColumn
sunFmProblemURL = _SunFmProblemURL_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 4),
    _SunFmProblemURL_Type()
)
sunFmProblemURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemURL.setStatus("current")
_SunFmProblemDiagEngine_Type = URLString
_SunFmProblemDiagEngine_Object = MibTableColumn
sunFmProblemDiagEngine = _SunFmProblemDiagEngine_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 5),
    _SunFmProblemDiagEngine_Type()
)
sunFmProblemDiagEngine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemDiagEngine.setStatus("current")
_SunFmProblemDiagTime_Type = DateAndTime
_SunFmProblemDiagTime_Object = MibTableColumn
sunFmProblemDiagTime = _SunFmProblemDiagTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 6),
    _SunFmProblemDiagTime_Type()
)
sunFmProblemDiagTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemDiagTime.setStatus("current")
_SunFmProblemSuspectCount_Type = Gauge32
_SunFmProblemSuspectCount_Object = MibTableColumn
sunFmProblemSuspectCount = _SunFmProblemSuspectCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 1, 1, 7),
    _SunFmProblemSuspectCount_Type()
)
sunFmProblemSuspectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmProblemSuspectCount.setStatus("current")
_SunFmFaultEventTable_Object = MibTable
sunFmFaultEventTable = _SunFmFaultEventTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2)
)
if mibBuilder.loadTexts:
    sunFmFaultEventTable.setStatus("current")
_SunFmFaultEventEntry_Object = MibTableRow
sunFmFaultEventEntry = _SunFmFaultEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1)
)
sunFmFaultEventEntry.setIndexNames(
    (0, "SUN-FM-MIB", "sunFmFaultEventUUIDIndex"),
    (0, "SUN-FM-MIB", "sunFmFaultEventIndex"),
)
if mibBuilder.loadTexts:
    sunFmFaultEventEntry.setStatus("current")
_SunFmFaultEventUUIDIndex_Type = SunFmUuidString
_SunFmFaultEventUUIDIndex_Object = MibTableColumn
sunFmFaultEventUUIDIndex = _SunFmFaultEventUUIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 1),
    _SunFmFaultEventUUIDIndex_Type()
)
sunFmFaultEventUUIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunFmFaultEventUUIDIndex.setStatus("current")
_SunFmFaultEventIndex_Type = Unsigned32
_SunFmFaultEventIndex_Object = MibTableColumn
sunFmFaultEventIndex = _SunFmFaultEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 2),
    _SunFmFaultEventIndex_Type()
)
sunFmFaultEventIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunFmFaultEventIndex.setStatus("current")
_SunFmFaultEventProblemUUID_Type = SunFmUuidString
_SunFmFaultEventProblemUUID_Object = MibTableColumn
sunFmFaultEventProblemUUID = _SunFmFaultEventProblemUUID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 3),
    _SunFmFaultEventProblemUUID_Type()
)
sunFmFaultEventProblemUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventProblemUUID.setStatus("current")
_SunFmFaultEventClass_Type = DisplayString
_SunFmFaultEventClass_Object = MibTableColumn
sunFmFaultEventClass = _SunFmFaultEventClass_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 4),
    _SunFmFaultEventClass_Type()
)
sunFmFaultEventClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventClass.setStatus("current")


class _SunFmFaultEventCertainty_Type(Gauge32):
    """Custom type sunFmFaultEventCertainty based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SunFmFaultEventCertainty_Type.__name__ = "Gauge32"
_SunFmFaultEventCertainty_Object = MibTableColumn
sunFmFaultEventCertainty = _SunFmFaultEventCertainty_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 5),
    _SunFmFaultEventCertainty_Type()
)
sunFmFaultEventCertainty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventCertainty.setStatus("current")
_SunFmFaultEventASRU_Type = URLString
_SunFmFaultEventASRU_Object = MibTableColumn
sunFmFaultEventASRU = _SunFmFaultEventASRU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 6),
    _SunFmFaultEventASRU_Type()
)
sunFmFaultEventASRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventASRU.setStatus("current")
_SunFmFaultEventFRU_Type = URLString
_SunFmFaultEventFRU_Object = MibTableColumn
sunFmFaultEventFRU = _SunFmFaultEventFRU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 7),
    _SunFmFaultEventFRU_Type()
)
sunFmFaultEventFRU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventFRU.setStatus("current")
_SunFmFaultEventResource_Type = URLString
_SunFmFaultEventResource_Object = MibTableColumn
sunFmFaultEventResource = _SunFmFaultEventResource_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 8),
    _SunFmFaultEventResource_Type()
)
sunFmFaultEventResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventResource.setStatus("current")
_SunFmFaultEventStatus_Type = SunFmEventState
_SunFmFaultEventStatus_Object = MibTableColumn
sunFmFaultEventStatus = _SunFmFaultEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 9),
    _SunFmFaultEventStatus_Type()
)
sunFmFaultEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventStatus.setStatus("current")
_SunFmFaultEventLocation_Type = URLString
_SunFmFaultEventLocation_Object = MibTableColumn
sunFmFaultEventLocation = _SunFmFaultEventLocation_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 2, 1, 10),
    _SunFmFaultEventLocation_Type()
)
sunFmFaultEventLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmFaultEventLocation.setStatus("current")
_SunFmModuleTable_Object = MibTable
sunFmModuleTable = _SunFmModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3)
)
if mibBuilder.loadTexts:
    sunFmModuleTable.setStatus("current")
_SunFmModuleEntry_Object = MibTableRow
sunFmModuleEntry = _SunFmModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1)
)
sunFmModuleEntry.setIndexNames(
    (0, "SUN-FM-MIB", "sunFmModuleIndex"),
)
if mibBuilder.loadTexts:
    sunFmModuleEntry.setStatus("current")
_SunFmModuleIndex_Type = Unsigned32
_SunFmModuleIndex_Object = MibTableColumn
sunFmModuleIndex = _SunFmModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1, 1),
    _SunFmModuleIndex_Type()
)
sunFmModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunFmModuleIndex.setStatus("current")


class _SunFmModuleName_Type(DisplayString):
    """Custom type sunFmModuleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SunFmModuleName_Type.__name__ = "DisplayString"
_SunFmModuleName_Object = MibTableColumn
sunFmModuleName = _SunFmModuleName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1, 2),
    _SunFmModuleName_Type()
)
sunFmModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmModuleName.setStatus("current")
_SunFmModuleVersion_Type = DisplayString
_SunFmModuleVersion_Object = MibTableColumn
sunFmModuleVersion = _SunFmModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1, 3),
    _SunFmModuleVersion_Type()
)
sunFmModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmModuleVersion.setStatus("current")
_SunFmModuleStatus_Type = SunFmModuleState
_SunFmModuleStatus_Object = MibTableColumn
sunFmModuleStatus = _SunFmModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1, 4),
    _SunFmModuleStatus_Type()
)
sunFmModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmModuleStatus.setStatus("current")
_SunFmModuleDescription_Type = DisplayString
_SunFmModuleDescription_Object = MibTableColumn
sunFmModuleDescription = _SunFmModuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 3, 1, 5),
    _SunFmModuleDescription_Type()
)
sunFmModuleDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmModuleDescription.setStatus("current")
_SunFmResourceCount_Type = Gauge32
_SunFmResourceCount_Object = MibScalar
sunFmResourceCount = _SunFmResourceCount_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 4),
    _SunFmResourceCount_Type()
)
sunFmResourceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmResourceCount.setStatus("current")
_SunFmResourceTable_Object = MibTable
sunFmResourceTable = _SunFmResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5)
)
if mibBuilder.loadTexts:
    sunFmResourceTable.setStatus("current")
_SunFmResourceEntry_Object = MibTableRow
sunFmResourceEntry = _SunFmResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5, 1)
)
sunFmResourceEntry.setIndexNames(
    (0, "SUN-FM-MIB", "sunFmResourceIndex"),
)
if mibBuilder.loadTexts:
    sunFmResourceEntry.setStatus("current")
_SunFmResourceIndex_Type = Unsigned32
_SunFmResourceIndex_Object = MibTableColumn
sunFmResourceIndex = _SunFmResourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5, 1, 1),
    _SunFmResourceIndex_Type()
)
sunFmResourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunFmResourceIndex.setStatus("current")


class _SunFmResourceFMRI_Type(DisplayString):
    """Custom type sunFmResourceFMRI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SunFmResourceFMRI_Type.__name__ = "DisplayString"
_SunFmResourceFMRI_Object = MibTableColumn
sunFmResourceFMRI = _SunFmResourceFMRI_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5, 1, 2),
    _SunFmResourceFMRI_Type()
)
sunFmResourceFMRI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmResourceFMRI.setStatus("current")
_SunFmResourceStatus_Type = SunFmResourceState
_SunFmResourceStatus_Object = MibTableColumn
sunFmResourceStatus = _SunFmResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5, 1, 3),
    _SunFmResourceStatus_Type()
)
sunFmResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmResourceStatus.setStatus("current")
_SunFmResourceDiagnosisUUID_Type = SunFmUuidString
_SunFmResourceDiagnosisUUID_Object = MibTableColumn
sunFmResourceDiagnosisUUID = _SunFmResourceDiagnosisUUID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 5, 1, 4),
    _SunFmResourceDiagnosisUUID_Type()
)
sunFmResourceDiagnosisUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunFmResourceDiagnosisUUID.setStatus("current")
_SunFmObjectGroups_ObjectIdentity = ObjectIdentity
sunFmObjectGroups = _SunFmObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 6)
)
_SunFmTraps_ObjectIdentity = ObjectIdentity
sunFmTraps = _SunFmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 7, 0)
)

# Managed Objects groups

sunFmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 6, 1)
)
sunFmObjectGroup.setObjects(
      *(("SUN-FM-MIB", "sunFmProblemUUID"),
        ("SUN-FM-MIB", "sunFmProblemCode"),
        ("SUN-FM-MIB", "sunFmProblemURL"),
        ("SUN-FM-MIB", "sunFmProblemDiagEngine"),
        ("SUN-FM-MIB", "sunFmProblemDiagTime"),
        ("SUN-FM-MIB", "sunFmProblemSuspectCount"),
        ("SUN-FM-MIB", "sunFmFaultEventProblemUUID"),
        ("SUN-FM-MIB", "sunFmFaultEventClass"),
        ("SUN-FM-MIB", "sunFmFaultEventCertainty"),
        ("SUN-FM-MIB", "sunFmFaultEventASRU"),
        ("SUN-FM-MIB", "sunFmFaultEventFRU"),
        ("SUN-FM-MIB", "sunFmFaultEventResource"),
        ("SUN-FM-MIB", "sunFmFaultEventStatus"),
        ("SUN-FM-MIB", "sunFmFaultEventLocation"),
        ("SUN-FM-MIB", "sunFmModuleName"),
        ("SUN-FM-MIB", "sunFmModuleVersion"),
        ("SUN-FM-MIB", "sunFmModuleStatus"),
        ("SUN-FM-MIB", "sunFmModuleDescription"),
        ("SUN-FM-MIB", "sunFmResourceCount"),
        ("SUN-FM-MIB", "sunFmResourceFMRI"),
        ("SUN-FM-MIB", "sunFmResourceStatus"),
        ("SUN-FM-MIB", "sunFmResourceDiagnosisUUID"))
)
if mibBuilder.loadTexts:
    sunFmObjectGroup.setStatus("current")


# Notification objects

sunFmProblemTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 7, 0, 1)
)
sunFmProblemTrap.setObjects(
      *(("SUN-FM-MIB", "sunFmProblemUUID"),
        ("SUN-FM-MIB", "sunFmProblemCode"),
        ("SUN-FM-MIB", "sunFmProblemURL"))
)
if mibBuilder.loadTexts:
    sunFmProblemTrap.setStatus(
        "current"
    )


# Notifications groups

sunFmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 195, 1, 6, 2)
)
sunFmNotificationGroup.setObjects(
    ("SUN-FM-MIB", "sunFmProblemTrap")
)
if mibBuilder.loadTexts:
    sunFmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-FM-MIB",
    **{"SunFmUuidString": SunFmUuidString,
       "SunFmModuleState": SunFmModuleState,
       "SunFmResourceState": SunFmResourceState,
       "SunFmEventState": SunFmEventState,
       "fm": fm,
       "sunFmMIB": sunFmMIB,
       "sunFmProblemTable": sunFmProblemTable,
       "sunFmProblemEntry": sunFmProblemEntry,
       "sunFmProblemUUIDIndex": sunFmProblemUUIDIndex,
       "sunFmProblemUUID": sunFmProblemUUID,
       "sunFmProblemCode": sunFmProblemCode,
       "sunFmProblemURL": sunFmProblemURL,
       "sunFmProblemDiagEngine": sunFmProblemDiagEngine,
       "sunFmProblemDiagTime": sunFmProblemDiagTime,
       "sunFmProblemSuspectCount": sunFmProblemSuspectCount,
       "sunFmFaultEventTable": sunFmFaultEventTable,
       "sunFmFaultEventEntry": sunFmFaultEventEntry,
       "sunFmFaultEventUUIDIndex": sunFmFaultEventUUIDIndex,
       "sunFmFaultEventIndex": sunFmFaultEventIndex,
       "sunFmFaultEventProblemUUID": sunFmFaultEventProblemUUID,
       "sunFmFaultEventClass": sunFmFaultEventClass,
       "sunFmFaultEventCertainty": sunFmFaultEventCertainty,
       "sunFmFaultEventASRU": sunFmFaultEventASRU,
       "sunFmFaultEventFRU": sunFmFaultEventFRU,
       "sunFmFaultEventResource": sunFmFaultEventResource,
       "sunFmFaultEventStatus": sunFmFaultEventStatus,
       "sunFmFaultEventLocation": sunFmFaultEventLocation,
       "sunFmModuleTable": sunFmModuleTable,
       "sunFmModuleEntry": sunFmModuleEntry,
       "sunFmModuleIndex": sunFmModuleIndex,
       "sunFmModuleName": sunFmModuleName,
       "sunFmModuleVersion": sunFmModuleVersion,
       "sunFmModuleStatus": sunFmModuleStatus,
       "sunFmModuleDescription": sunFmModuleDescription,
       "sunFmResourceCount": sunFmResourceCount,
       "sunFmResourceTable": sunFmResourceTable,
       "sunFmResourceEntry": sunFmResourceEntry,
       "sunFmResourceIndex": sunFmResourceIndex,
       "sunFmResourceFMRI": sunFmResourceFMRI,
       "sunFmResourceStatus": sunFmResourceStatus,
       "sunFmResourceDiagnosisUUID": sunFmResourceDiagnosisUUID,
       "sunFmObjectGroups": sunFmObjectGroups,
       "sunFmObjectGroup": sunFmObjectGroup,
       "sunFmNotificationGroup": sunFmNotificationGroup,
       "sunFmTraps": sunFmTraps,
       "sunFmProblemTrap": sunFmProblemTrap}
)
