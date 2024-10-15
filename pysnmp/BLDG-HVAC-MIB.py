# SNMP MIB module (BLDG-HVAC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLDG-HVAC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:12 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

bldgHVACMIB = ModuleIdentity(
    (1, 3, 6, 1, 3, 122)
)
bldgHVACMIB.setRevisions(
        ("2003-03-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BldgHvacOperation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cool", 2),
          ("heat", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BldgHVACObjects_ObjectIdentity = ObjectIdentity
bldgHVACObjects = _BldgHVACObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 122, 1)
)
_BldgHVACTable_Object = MibTable
bldgHVACTable = _BldgHVACTable_Object(
    (1, 3, 6, 1, 3, 122, 1, 1)
)
if mibBuilder.loadTexts:
    bldgHVACTable.setStatus("current")
_BldgHVACEntry_Object = MibTableRow
bldgHVACEntry = _BldgHVACEntry_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1)
)
bldgHVACEntry.setIndexNames(
    (0, "BLDG-HVAC-MIB", "bldgHVACFloor"),
    (0, "BLDG-HVAC-MIB", "bldgHVACOffice"),
)
if mibBuilder.loadTexts:
    bldgHVACEntry.setStatus("current")


class _BldgHVACFloor_Type(Unsigned32):
    """Custom type bldgHVACFloor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_BldgHVACFloor_Type.__name__ = "Unsigned32"
_BldgHVACFloor_Object = MibTableColumn
bldgHVACFloor = _BldgHVACFloor_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 1),
    _BldgHVACFloor_Type()
)
bldgHVACFloor.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bldgHVACFloor.setStatus("current")


class _BldgHVACOffice_Type(Unsigned32):
    """Custom type bldgHVACOffice based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BldgHVACOffice_Type.__name__ = "Unsigned32"
_BldgHVACOffice_Object = MibTableColumn
bldgHVACOffice = _BldgHVACOffice_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 2),
    _BldgHVACOffice_Type()
)
bldgHVACOffice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bldgHVACOffice.setStatus("current")
_BldgHVACCfgTemplate_Type = Unsigned32
_BldgHVACCfgTemplate_Object = MibTableColumn
bldgHVACCfgTemplate = _BldgHVACCfgTemplate_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 3),
    _BldgHVACCfgTemplate_Type()
)
bldgHVACCfgTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplate.setStatus("current")
_BldgHVACFanSpeed_Type = Gauge32
_BldgHVACFanSpeed_Object = MibTableColumn
bldgHVACFanSpeed = _BldgHVACFanSpeed_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 4),
    _BldgHVACFanSpeed_Type()
)
bldgHVACFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bldgHVACFanSpeed.setStatus("current")
if mibBuilder.loadTexts:
    bldgHVACFanSpeed.setUnits("revolutions per minute")
_BldgHVACCurrentTemp_Type = Gauge32
_BldgHVACCurrentTemp_Object = MibTableColumn
bldgHVACCurrentTemp = _BldgHVACCurrentTemp_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 5),
    _BldgHVACCurrentTemp_Type()
)
bldgHVACCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bldgHVACCurrentTemp.setStatus("current")
if mibBuilder.loadTexts:
    bldgHVACCurrentTemp.setUnits("degrees in celsius")
_BldgHVACCoolOrHeatMins_Type = Counter32
_BldgHVACCoolOrHeatMins_Object = MibTableColumn
bldgHVACCoolOrHeatMins = _BldgHVACCoolOrHeatMins_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 6),
    _BldgHVACCoolOrHeatMins_Type()
)
bldgHVACCoolOrHeatMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bldgHVACCoolOrHeatMins.setStatus("current")
if mibBuilder.loadTexts:
    bldgHVACCoolOrHeatMins.setUnits("minutes")
_BldgHVACDiscontinuityTime_Type = TimeStamp
_BldgHVACDiscontinuityTime_Object = MibTableColumn
bldgHVACDiscontinuityTime = _BldgHVACDiscontinuityTime_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 7),
    _BldgHVACDiscontinuityTime_Type()
)
bldgHVACDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bldgHVACDiscontinuityTime.setStatus("current")
_BldgHVACOwner_Type = SnmpAdminString
_BldgHVACOwner_Object = MibTableColumn
bldgHVACOwner = _BldgHVACOwner_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 8),
    _BldgHVACOwner_Type()
)
bldgHVACOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACOwner.setStatus("current")
_BldgHVACStorageType_Type = StorageType
_BldgHVACStorageType_Object = MibTableColumn
bldgHVACStorageType = _BldgHVACStorageType_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 9),
    _BldgHVACStorageType_Type()
)
bldgHVACStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACStorageType.setStatus("current")
_BldgHVACStatus_Type = RowStatus
_BldgHVACStatus_Object = MibTableColumn
bldgHVACStatus = _BldgHVACStatus_Object(
    (1, 3, 6, 1, 3, 122, 1, 1, 1, 10),
    _BldgHVACStatus_Type()
)
bldgHVACStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACStatus.setStatus("current")
_BldgHVACCfgTemplateInfoTable_Object = MibTable
bldgHVACCfgTemplateInfoTable = _BldgHVACCfgTemplateInfoTable_Object(
    (1, 3, 6, 1, 3, 122, 1, 2)
)
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoTable.setStatus("current")
_BldgHVACCfgTemplateInfoEntry_Object = MibTableRow
bldgHVACCfgTemplateInfoEntry = _BldgHVACCfgTemplateInfoEntry_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1)
)
bldgHVACCfgTemplateInfoEntry.setIndexNames(
    (0, "BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoIndex"),
)
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoEntry.setStatus("current")


class _BldgHVACCfgTemplateInfoIndex_Type(Unsigned32):
    """Custom type bldgHVACCfgTemplateInfoIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BldgHVACCfgTemplateInfoIndex_Type.__name__ = "Unsigned32"
_BldgHVACCfgTemplateInfoIndex_Object = MibTableColumn
bldgHVACCfgTemplateInfoIndex = _BldgHVACCfgTemplateInfoIndex_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 1),
    _BldgHVACCfgTemplateInfoIndex_Type()
)
bldgHVACCfgTemplateInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoIndex.setStatus("current")
_BldgHVACCfgTemplateInfoID_Type = SnmpAdminString
_BldgHVACCfgTemplateInfoID_Object = MibTableColumn
bldgHVACCfgTemplateInfoID = _BldgHVACCfgTemplateInfoID_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 2),
    _BldgHVACCfgTemplateInfoID_Type()
)
bldgHVACCfgTemplateInfoID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoID.setStatus("current")
_BldgHVACCfgTemplateInfoDescr_Type = SnmpAdminString
_BldgHVACCfgTemplateInfoDescr_Object = MibTableColumn
bldgHVACCfgTemplateInfoDescr = _BldgHVACCfgTemplateInfoDescr_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 3),
    _BldgHVACCfgTemplateInfoDescr_Type()
)
bldgHVACCfgTemplateInfoDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoDescr.setStatus("current")
_BldgHVACCfgTemplateInfoOwner_Type = SnmpAdminString
_BldgHVACCfgTemplateInfoOwner_Object = MibTableColumn
bldgHVACCfgTemplateInfoOwner = _BldgHVACCfgTemplateInfoOwner_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 4),
    _BldgHVACCfgTemplateInfoOwner_Type()
)
bldgHVACCfgTemplateInfoOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoOwner.setStatus("current")
_BldgHVACCfgTemplateInfoStatus_Type = RowStatus
_BldgHVACCfgTemplateInfoStatus_Object = MibTableColumn
bldgHVACCfgTemplateInfoStatus = _BldgHVACCfgTemplateInfoStatus_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 5),
    _BldgHVACCfgTemplateInfoStatus_Type()
)
bldgHVACCfgTemplateInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoStatus.setStatus("current")
_BldgHVACCfgTemplateInfoStorType_Type = StorageType
_BldgHVACCfgTemplateInfoStorType_Object = MibTableColumn
bldgHVACCfgTemplateInfoStorType = _BldgHVACCfgTemplateInfoStorType_Object(
    (1, 3, 6, 1, 3, 122, 1, 2, 1, 6),
    _BldgHVACCfgTemplateInfoStorType_Type()
)
bldgHVACCfgTemplateInfoStorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfoStorType.setStatus("current")
_BldgHVACCfgTemplateTable_Object = MibTable
bldgHVACCfgTemplateTable = _BldgHVACCfgTemplateTable_Object(
    (1, 3, 6, 1, 3, 122, 1, 3)
)
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateTable.setStatus("current")
_BldgHVACCfgTemplateEntry_Object = MibTableRow
bldgHVACCfgTemplateEntry = _BldgHVACCfgTemplateEntry_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1)
)
bldgHVACCfgTemplateEntry.setIndexNames(
    (0, "BLDG-HVAC-MIB", "bldgHVACCfgTemplateIndex"),
)
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateEntry.setStatus("current")


class _BldgHVACCfgTemplateIndex_Type(Unsigned32):
    """Custom type bldgHVACCfgTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_BldgHVACCfgTemplateIndex_Type.__name__ = "Unsigned32"
_BldgHVACCfgTemplateIndex_Object = MibTableColumn
bldgHVACCfgTemplateIndex = _BldgHVACCfgTemplateIndex_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 1),
    _BldgHVACCfgTemplateIndex_Type()
)
bldgHVACCfgTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateIndex.setStatus("current")
_BldgHVACCfgTemplateDesiredTemp_Type = Gauge32
_BldgHVACCfgTemplateDesiredTemp_Object = MibTableColumn
bldgHVACCfgTemplateDesiredTemp = _BldgHVACCfgTemplateDesiredTemp_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 2),
    _BldgHVACCfgTemplateDesiredTemp_Type()
)
bldgHVACCfgTemplateDesiredTemp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateDesiredTemp.setStatus("current")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateDesiredTemp.setUnits("degrees in celsius")
_BldgHVACCfgTemplateCoolOrHeat_Type = BldgHvacOperation
_BldgHVACCfgTemplateCoolOrHeat_Object = MibTableColumn
bldgHVACCfgTemplateCoolOrHeat = _BldgHVACCfgTemplateCoolOrHeat_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 3),
    _BldgHVACCfgTemplateCoolOrHeat_Type()
)
bldgHVACCfgTemplateCoolOrHeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateCoolOrHeat.setStatus("current")
_BldgHVACCfgTemplateInfo_Type = Unsigned32
_BldgHVACCfgTemplateInfo_Object = MibTableColumn
bldgHVACCfgTemplateInfo = _BldgHVACCfgTemplateInfo_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 4),
    _BldgHVACCfgTemplateInfo_Type()
)
bldgHVACCfgTemplateInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateInfo.setStatus("current")
_BldgHVACCfgTemplateOwner_Type = SnmpAdminString
_BldgHVACCfgTemplateOwner_Object = MibTableColumn
bldgHVACCfgTemplateOwner = _BldgHVACCfgTemplateOwner_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 5),
    _BldgHVACCfgTemplateOwner_Type()
)
bldgHVACCfgTemplateOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateOwner.setStatus("current")
_BldgHVACCfgTemplateStorage_Type = StorageType
_BldgHVACCfgTemplateStorage_Object = MibTableColumn
bldgHVACCfgTemplateStorage = _BldgHVACCfgTemplateStorage_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 6),
    _BldgHVACCfgTemplateStorage_Type()
)
bldgHVACCfgTemplateStorage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateStorage.setStatus("current")
_BldgHVACCfgTemplateStatus_Type = RowStatus
_BldgHVACCfgTemplateStatus_Object = MibTableColumn
bldgHVACCfgTemplateStatus = _BldgHVACCfgTemplateStatus_Object(
    (1, 3, 6, 1, 3, 122, 1, 3, 1, 7),
    _BldgHVACCfgTemplateStatus_Type()
)
bldgHVACCfgTemplateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bldgHVACCfgTemplateStatus.setStatus("current")
_BldgConformance_ObjectIdentity = ObjectIdentity
bldgConformance = _BldgConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 122, 2)
)
_BldgCompliances_ObjectIdentity = ObjectIdentity
bldgCompliances = _BldgCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 122, 2, 1)
)
_BldgGroups_ObjectIdentity = ObjectIdentity
bldgGroups = _BldgGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 122, 2, 2)
)

# Managed Objects groups

bldgHVACObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 122, 2, 2, 1)
)
bldgHVACObjectsGroup.setObjects(
      *(("BLDG-HVAC-MIB", "bldgHVACCfgTemplate"),
        ("BLDG-HVAC-MIB", "bldgHVACFanSpeed"),
        ("BLDG-HVAC-MIB", "bldgHVACCurrentTemp"),
        ("BLDG-HVAC-MIB", "bldgHVACCoolOrHeatMins"),
        ("BLDG-HVAC-MIB", "bldgHVACDiscontinuityTime"),
        ("BLDG-HVAC-MIB", "bldgHVACOwner"),
        ("BLDG-HVAC-MIB", "bldgHVACStatus"),
        ("BLDG-HVAC-MIB", "bldgHVACStorageType"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoID"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoDescr"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoOwner"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoStatus"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfoStorType"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateDesiredTemp"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateCoolOrHeat"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateInfo"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateOwner"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateStorage"),
        ("BLDG-HVAC-MIB", "bldgHVACCfgTemplateStatus"))
)
if mibBuilder.loadTexts:
    bldgHVACObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bldgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 122, 2, 1, 1)
)
if mibBuilder.loadTexts:
    bldgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLDG-HVAC-MIB",
    **{"BldgHvacOperation": BldgHvacOperation,
       "bldgHVACMIB": bldgHVACMIB,
       "bldgHVACObjects": bldgHVACObjects,
       "bldgHVACTable": bldgHVACTable,
       "bldgHVACEntry": bldgHVACEntry,
       "bldgHVACFloor": bldgHVACFloor,
       "bldgHVACOffice": bldgHVACOffice,
       "bldgHVACCfgTemplate": bldgHVACCfgTemplate,
       "bldgHVACFanSpeed": bldgHVACFanSpeed,
       "bldgHVACCurrentTemp": bldgHVACCurrentTemp,
       "bldgHVACCoolOrHeatMins": bldgHVACCoolOrHeatMins,
       "bldgHVACDiscontinuityTime": bldgHVACDiscontinuityTime,
       "bldgHVACOwner": bldgHVACOwner,
       "bldgHVACStorageType": bldgHVACStorageType,
       "bldgHVACStatus": bldgHVACStatus,
       "bldgHVACCfgTemplateInfoTable": bldgHVACCfgTemplateInfoTable,
       "bldgHVACCfgTemplateInfoEntry": bldgHVACCfgTemplateInfoEntry,
       "bldgHVACCfgTemplateInfoIndex": bldgHVACCfgTemplateInfoIndex,
       "bldgHVACCfgTemplateInfoID": bldgHVACCfgTemplateInfoID,
       "bldgHVACCfgTemplateInfoDescr": bldgHVACCfgTemplateInfoDescr,
       "bldgHVACCfgTemplateInfoOwner": bldgHVACCfgTemplateInfoOwner,
       "bldgHVACCfgTemplateInfoStatus": bldgHVACCfgTemplateInfoStatus,
       "bldgHVACCfgTemplateInfoStorType": bldgHVACCfgTemplateInfoStorType,
       "bldgHVACCfgTemplateTable": bldgHVACCfgTemplateTable,
       "bldgHVACCfgTemplateEntry": bldgHVACCfgTemplateEntry,
       "bldgHVACCfgTemplateIndex": bldgHVACCfgTemplateIndex,
       "bldgHVACCfgTemplateDesiredTemp": bldgHVACCfgTemplateDesiredTemp,
       "bldgHVACCfgTemplateCoolOrHeat": bldgHVACCfgTemplateCoolOrHeat,
       "bldgHVACCfgTemplateInfo": bldgHVACCfgTemplateInfo,
       "bldgHVACCfgTemplateOwner": bldgHVACCfgTemplateOwner,
       "bldgHVACCfgTemplateStorage": bldgHVACCfgTemplateStorage,
       "bldgHVACCfgTemplateStatus": bldgHVACCfgTemplateStatus,
       "bldgConformance": bldgConformance,
       "bldgCompliances": bldgCompliances,
       "bldgCompliance": bldgCompliance,
       "bldgGroups": bldgGroups,
       "bldgHVACObjectsGroup": bldgHVACObjectsGroup}
)
