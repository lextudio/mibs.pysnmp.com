# SNMP MIB module (CISCO-WAN-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-MODULE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:09 2024
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

ciscoWanModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145)
)
ciscoWanModuleMIB.setRevisions(
        ("2002-09-11 00:00",
         "2001-07-20 00:00",
         "1999-10-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class StatisticsLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("levelOne", 1),
          ("levelThree", 3),
          ("levelTwo", 2),
          ("notApplicable", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CwmMIBObjects_ObjectIdentity = ObjectIdentity
cwmMIBObjects = _CwmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1)
)
_CwmConfig_ObjectIdentity = ObjectIdentity
cwmConfig = _CwmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1)
)
_CwmConfigTable_Object = MibTable
cwmConfigTable = _CwmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwmConfigTable.setStatus("current")
_CwmConfigEntry_Object = MibTableRow
cwmConfigEntry = _CwmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1)
)
cwmConfigEntry.setIndexNames(
    (0, "CISCO-WAN-MODULE-MIB", "cwmIndex"),
)
if mibBuilder.loadTexts:
    cwmConfigEntry.setStatus("current")


class _CwmIndex_Type(Unsigned32):
    """Custom type cwmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CwmIndex_Type.__name__ = "Unsigned32"
_CwmIndex_Object = MibTableColumn
cwmIndex = _CwmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 1),
    _CwmIndex_Type()
)
cwmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwmIndex.setStatus("current")


class _CwmIngressSCTFileId_Type(Unsigned32):
    """Custom type cwmIngressSCTFileId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CwmIngressSCTFileId_Type.__name__ = "Unsigned32"
_CwmIngressSCTFileId_Object = MibTableColumn
cwmIngressSCTFileId = _CwmIngressSCTFileId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 2),
    _CwmIngressSCTFileId_Type()
)
cwmIngressSCTFileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmIngressSCTFileId.setStatus("current")
_CwmIngressSCTFileName_Type = DisplayString
_CwmIngressSCTFileName_Object = MibTableColumn
cwmIngressSCTFileName = _CwmIngressSCTFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 3),
    _CwmIngressSCTFileName_Type()
)
cwmIngressSCTFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmIngressSCTFileName.setStatus("current")


class _CwmAutoLineDiagEnable_Type(Integer32):
    """Custom type cwmAutoLineDiagEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CwmAutoLineDiagEnable_Type.__name__ = "Integer32"
_CwmAutoLineDiagEnable_Object = MibTableColumn
cwmAutoLineDiagEnable = _CwmAutoLineDiagEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 4),
    _CwmAutoLineDiagEnable_Type()
)
cwmAutoLineDiagEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmAutoLineDiagEnable.setStatus("current")


class _CwmSCTFileVerCfg_Type(Unsigned32):
    """Custom type cwmSCTFileVerCfg based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwmSCTFileVerCfg_Type.__name__ = "Unsigned32"
_CwmSCTFileVerCfg_Object = MibTableColumn
cwmSCTFileVerCfg = _CwmSCTFileVerCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 5),
    _CwmSCTFileVerCfg_Type()
)
cwmSCTFileVerCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmSCTFileVerCfg.setStatus("current")


class _CwmSCTFileVerOpr_Type(Unsigned32):
    """Custom type cwmSCTFileVerOpr based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwmSCTFileVerOpr_Type.__name__ = "Unsigned32"
_CwmSCTFileVerOpr_Object = MibTableColumn
cwmSCTFileVerOpr = _CwmSCTFileVerOpr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 6),
    _CwmSCTFileVerOpr_Type()
)
cwmSCTFileVerOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwmSCTFileVerOpr.setStatus("current")


class _CwmUploadCounter_Type(Unsigned32):
    """Custom type cwmUploadCounter based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwmUploadCounter_Type.__name__ = "Unsigned32"
_CwmUploadCounter_Object = MibTableColumn
cwmUploadCounter = _CwmUploadCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 1, 1, 1, 7),
    _CwmUploadCounter_Type()
)
cwmUploadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwmUploadCounter.setStatus("current")
_CwmStatsConfig_ObjectIdentity = ObjectIdentity
cwmStatsConfig = _CwmStatsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2)
)
_CwmStatConfigTable_Object = MibTable
cwmStatConfigTable = _CwmStatConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwmStatConfigTable.setStatus("current")
_CwmStatConfigEntry_Object = MibTableRow
cwmStatConfigEntry = _CwmStatConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1)
)
cwmStatConfigEntry.setIndexNames(
    (0, "CISCO-WAN-MODULE-MIB", "cwmIndex"),
)
if mibBuilder.loadTexts:
    cwmStatConfigEntry.setStatus("current")


class _CwmStatBucketInterval_Type(Integer32):
    """Custom type cwmStatBucketInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              10,
              15,
              20,
              30,
              60)
        )
    )
    namedValues = NamedValues(
        *(("fifteen", 15),
          ("five", 5),
          ("sixty", 60),
          ("ten", 10),
          ("thirty", 30),
          ("twenty", 20))
    )


_CwmStatBucketInterval_Type.__name__ = "Integer32"
_CwmStatBucketInterval_Object = MibTableColumn
cwmStatBucketInterval = _CwmStatBucketInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 1),
    _CwmStatBucketInterval_Type()
)
cwmStatBucketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmStatBucketInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwmStatBucketInterval.setUnits("minutes")


class _CwmStatCollectionInterval_Type(Integer32):
    """Custom type cwmStatCollectionInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              5)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("five", 5),
          ("one", 1))
    )


_CwmStatCollectionInterval_Type.__name__ = "Integer32"
_CwmStatCollectionInterval_Object = MibTableColumn
cwmStatCollectionInterval = _CwmStatCollectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 2),
    _CwmStatCollectionInterval_Type()
)
cwmStatCollectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmStatCollectionInterval.setStatus("current")
if mibBuilder.loadTexts:
    cwmStatCollectionInterval.setUnits("minutes")


class _CwmStatCollectionStatus_Type(Integer32):
    """Custom type cwmStatCollectionStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CwmStatCollectionStatus_Type.__name__ = "Integer32"
_CwmStatCollectionStatus_Object = MibTableColumn
cwmStatCollectionStatus = _CwmStatCollectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 3),
    _CwmStatCollectionStatus_Type()
)
cwmStatCollectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmStatCollectionStatus.setStatus("current")
_CwmStatCurrentLevel_Type = StatisticsLevel
_CwmStatCurrentLevel_Object = MibTableColumn
cwmStatCurrentLevel = _CwmStatCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 4),
    _CwmStatCurrentLevel_Type()
)
cwmStatCurrentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwmStatCurrentLevel.setStatus("current")


class _CwmStatLevelConfigured_Type(StatisticsLevel):
    """Custom type cwmStatLevelConfigured based on StatisticsLevel"""


_CwmStatLevelConfigured_Object = MibTableColumn
cwmStatLevelConfigured = _CwmStatLevelConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 5),
    _CwmStatLevelConfigured_Type()
)
cwmStatLevelConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwmStatLevelConfigured.setStatus("current")
_CwmStatMaximumConnections_Type = Unsigned32
_CwmStatMaximumConnections_Object = MibTableColumn
cwmStatMaximumConnections = _CwmStatMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 1, 2, 1, 1, 6),
    _CwmStatMaximumConnections_Type()
)
cwmStatMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwmStatMaximumConnections.setStatus("current")
_CiscoWanModuleMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoWanModuleMIBNotificationPrefix = _CiscoWanModuleMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 2)
)
_CiscoWanModuleMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoWanModuleMIBNotifications = _CiscoWanModuleMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 2, 0)
)
_CiscoWanModuleMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanModuleMIBConformance = _CiscoWanModuleMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3)
)
_CiscoWanModuleMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanModuleMIBCompliances = _CiscoWanModuleMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1)
)
_CiscoWanModuleMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanModuleMIBGroups = _CiscoWanModuleMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2)
)

# Managed Objects groups

cwmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 1)
)
cwmConfigGroup.setObjects(
      *(("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileId"),
        ("CISCO-WAN-MODULE-MIB", "cwmIngressSCTFileName"),
        ("CISCO-WAN-MODULE-MIB", "cwmAutoLineDiagEnable"))
)
if mibBuilder.loadTexts:
    cwmConfigGroup.setStatus("current")

cwmStatConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 2)
)
cwmStatConfigGroup.setObjects(
      *(("CISCO-WAN-MODULE-MIB", "cwmStatBucketInterval"),
        ("CISCO-WAN-MODULE-MIB", "cwmStatCurrentLevel"),
        ("CISCO-WAN-MODULE-MIB", "cwmStatLevelConfigured"),
        ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionStatus"),
        ("CISCO-WAN-MODULE-MIB", "cwmStatCollectionInterval"),
        ("CISCO-WAN-MODULE-MIB", "cwmStatMaximumConnections"))
)
if mibBuilder.loadTexts:
    cwmStatConfigGroup.setStatus("current")

cwmConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 3)
)
cwmConfigGroup2.setObjects(
      *(("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerCfg"),
        ("CISCO-WAN-MODULE-MIB", "cwmSCTFileVerOpr"))
)
if mibBuilder.loadTexts:
    cwmConfigGroup2.setStatus("current")

cwmUploadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 2, 4)
)
cwmUploadGroup.setObjects(
    ("CISCO-WAN-MODULE-MIB", "cwmUploadCounter")
)
if mibBuilder.loadTexts:
    cwmUploadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanModuleMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWanModuleMIBCompliance.setStatus(
        "deprecated"
    )

ciscoWanModuleMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoWanModuleMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoWanModuleMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 145, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoWanModuleMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-MODULE-MIB",
    **{"StatisticsLevel": StatisticsLevel,
       "ciscoWanModuleMIB": ciscoWanModuleMIB,
       "cwmMIBObjects": cwmMIBObjects,
       "cwmConfig": cwmConfig,
       "cwmConfigTable": cwmConfigTable,
       "cwmConfigEntry": cwmConfigEntry,
       "cwmIndex": cwmIndex,
       "cwmIngressSCTFileId": cwmIngressSCTFileId,
       "cwmIngressSCTFileName": cwmIngressSCTFileName,
       "cwmAutoLineDiagEnable": cwmAutoLineDiagEnable,
       "cwmSCTFileVerCfg": cwmSCTFileVerCfg,
       "cwmSCTFileVerOpr": cwmSCTFileVerOpr,
       "cwmUploadCounter": cwmUploadCounter,
       "cwmStatsConfig": cwmStatsConfig,
       "cwmStatConfigTable": cwmStatConfigTable,
       "cwmStatConfigEntry": cwmStatConfigEntry,
       "cwmStatBucketInterval": cwmStatBucketInterval,
       "cwmStatCollectionInterval": cwmStatCollectionInterval,
       "cwmStatCollectionStatus": cwmStatCollectionStatus,
       "cwmStatCurrentLevel": cwmStatCurrentLevel,
       "cwmStatLevelConfigured": cwmStatLevelConfigured,
       "cwmStatMaximumConnections": cwmStatMaximumConnections,
       "ciscoWanModuleMIBNotificationPrefix": ciscoWanModuleMIBNotificationPrefix,
       "ciscoWanModuleMIBNotifications": ciscoWanModuleMIBNotifications,
       "ciscoWanModuleMIBConformance": ciscoWanModuleMIBConformance,
       "ciscoWanModuleMIBCompliances": ciscoWanModuleMIBCompliances,
       "ciscoWanModuleMIBCompliance": ciscoWanModuleMIBCompliance,
       "ciscoWanModuleMIBComplianceRev1": ciscoWanModuleMIBComplianceRev1,
       "ciscoWanModuleMIBComplianceRev2": ciscoWanModuleMIBComplianceRev2,
       "ciscoWanModuleMIBGroups": ciscoWanModuleMIBGroups,
       "cwmConfigGroup": cwmConfigGroup,
       "cwmStatConfigGroup": cwmStatConfigGroup,
       "cwmConfigGroup2": cwmConfigGroup2,
       "cwmUploadGroup": cwmUploadGroup}
)
