# SNMP MIB module (OPTIX-SONET-ALM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-ALM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:28 2024
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

(optixCommonSonet,) = mibBuilder.importSymbols(
    "OPTIX-OID-MIB",
    "optixCommonSonet")

(AlarmEventType,
 AlmDataNtfcnCdeType,
 AlmDataSrvEffType,
 DirectionType,
 LocationType,
 MOD2Type) = mibBuilder.importSymbols(
    "OPTIX-SONET-TC-MIB",
    "AlarmEventType",
    "AlmDataNtfcnCdeType",
    "AlmDataSrvEffType",
    "DirectionType",
    "LocationType",
    "MOD2Type")

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


# MODULE-IDENTITY

optixSonetAlarm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10)
)
optixSonetAlarm.setRevisions(
        ("2006-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlmData_ObjectIdentity = ObjectIdentity
almData = _AlmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10)
)
_AlmDataTable_Object = MibTable
almDataTable = _AlmDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10)
)
if mibBuilder.loadTexts:
    almDataTable.setStatus("current")
_AlmDataEntry_Object = MibTableRow
almDataEntry = _AlmDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1)
)
almDataEntry.setIndexNames(
    (0, "OPTIX-SONET-ALM-MIB", "almDataMOD2"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataSlot"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataPort"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataPath"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataVT"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataNtfcnCde"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataName"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataSrvEff"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataLocation"),
    (0, "OPTIX-SONET-ALM-MIB", "almDataDirection"),
)
if mibBuilder.loadTexts:
    almDataEntry.setStatus("current")
_AlmDataMOD2_Type = MOD2Type
_AlmDataMOD2_Object = MibTableColumn
almDataMOD2 = _AlmDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 1),
    _AlmDataMOD2_Type()
)
almDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataMOD2.setStatus("current")
_AlmDataSlot_Type = Unsigned32
_AlmDataSlot_Object = MibTableColumn
almDataSlot = _AlmDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 2),
    _AlmDataSlot_Type()
)
almDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataSlot.setStatus("current")
_AlmDataPort_Type = Unsigned32
_AlmDataPort_Object = MibTableColumn
almDataPort = _AlmDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 3),
    _AlmDataPort_Type()
)
almDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataPort.setStatus("current")
_AlmDataPath_Type = Unsigned32
_AlmDataPath_Object = MibTableColumn
almDataPath = _AlmDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 4),
    _AlmDataPath_Type()
)
almDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataPath.setStatus("current")
_AlmDataVT_Type = Unsigned32
_AlmDataVT_Object = MibTableColumn
almDataVT = _AlmDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 5),
    _AlmDataVT_Type()
)
almDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataVT.setStatus("current")
_AlmDataNtfcnCde_Type = AlmDataNtfcnCdeType
_AlmDataNtfcnCde_Object = MibTableColumn
almDataNtfcnCde = _AlmDataNtfcnCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 6),
    _AlmDataNtfcnCde_Type()
)
almDataNtfcnCde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataNtfcnCde.setStatus("current")
_AlmDataName_Type = AlarmEventType
_AlmDataName_Object = MibTableColumn
almDataName = _AlmDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 7),
    _AlmDataName_Type()
)
almDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataName.setStatus("current")
_AlmDataSrvEff_Type = AlmDataSrvEffType
_AlmDataSrvEff_Object = MibTableColumn
almDataSrvEff = _AlmDataSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 8),
    _AlmDataSrvEff_Type()
)
almDataSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataSrvEff.setStatus("current")
_AlmDataLocation_Type = LocationType
_AlmDataLocation_Object = MibTableColumn
almDataLocation = _AlmDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 9),
    _AlmDataLocation_Type()
)
almDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataLocation.setStatus("current")
_AlmDataDirection_Type = DirectionType
_AlmDataDirection_Object = MibTableColumn
almDataDirection = _AlmDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 10),
    _AlmDataDirection_Type()
)
almDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataDirection.setStatus("current")
_AlmDataDateTime_Type = DateAndTime
_AlmDataDateTime_Object = MibTableColumn
almDataDateTime = _AlmDataDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 11),
    _AlmDataDateTime_Type()
)
almDataDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataDateTime.setStatus("current")


class _AlmDataDesc_Type(OctetString):
    """Custom type almDataDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlmDataDesc_Type.__name__ = "OctetString"
_AlmDataDesc_Object = MibTableColumn
almDataDesc = _AlmDataDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 12),
    _AlmDataDesc_Type()
)
almDataDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataDesc.setStatus("current")
_AlmDataAiddet_Type = Unsigned32
_AlmDataAiddet_Object = MibTableColumn
almDataAiddet = _AlmDataAiddet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 10, 1, 13),
    _AlmDataAiddet_Type()
)
almDataAiddet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almDataAiddet.setStatus("current")
_CondDataTable_Object = MibTable
condDataTable = _CondDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20)
)
if mibBuilder.loadTexts:
    condDataTable.setStatus("current")
_CondDataEntry_Object = MibTableRow
condDataEntry = _CondDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1)
)
condDataEntry.setIndexNames(
    (0, "OPTIX-SONET-ALM-MIB", "condDataMOD2"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataSlot"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataPort"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataPath"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataVT"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataName"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataLocation"),
    (0, "OPTIX-SONET-ALM-MIB", "condDataDirection"),
)
if mibBuilder.loadTexts:
    condDataEntry.setStatus("current")
_CondDataMOD2_Type = MOD2Type
_CondDataMOD2_Object = MibTableColumn
condDataMOD2 = _CondDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 1),
    _CondDataMOD2_Type()
)
condDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataMOD2.setStatus("current")
_CondDataSlot_Type = Unsigned32
_CondDataSlot_Object = MibTableColumn
condDataSlot = _CondDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 2),
    _CondDataSlot_Type()
)
condDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataSlot.setStatus("current")
_CondDataPort_Type = Unsigned32
_CondDataPort_Object = MibTableColumn
condDataPort = _CondDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 3),
    _CondDataPort_Type()
)
condDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataPort.setStatus("current")
_CondDataPath_Type = Unsigned32
_CondDataPath_Object = MibTableColumn
condDataPath = _CondDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 4),
    _CondDataPath_Type()
)
condDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataPath.setStatus("current")
_CondDataVT_Type = Unsigned32
_CondDataVT_Object = MibTableColumn
condDataVT = _CondDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 5),
    _CondDataVT_Type()
)
condDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataVT.setStatus("current")
_CondDataName_Type = AlarmEventType
_CondDataName_Object = MibTableColumn
condDataName = _CondDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 6),
    _CondDataName_Type()
)
condDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataName.setStatus("current")
_CondDataLocation_Type = LocationType
_CondDataLocation_Object = MibTableColumn
condDataLocation = _CondDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 7),
    _CondDataLocation_Type()
)
condDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataLocation.setStatus("current")
_CondDataDirection_Type = DirectionType
_CondDataDirection_Object = MibTableColumn
condDataDirection = _CondDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 8),
    _CondDataDirection_Type()
)
condDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataDirection.setStatus("current")
_CondDataNtfcnCde_Type = AlmDataNtfcnCdeType
_CondDataNtfcnCde_Object = MibTableColumn
condDataNtfcnCde = _CondDataNtfcnCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 9),
    _CondDataNtfcnCde_Type()
)
condDataNtfcnCde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataNtfcnCde.setStatus("current")
_CondDataSrvEff_Type = AlmDataSrvEffType
_CondDataSrvEff_Object = MibTableColumn
condDataSrvEff = _CondDataSrvEff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 10),
    _CondDataSrvEff_Type()
)
condDataSrvEff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataSrvEff.setStatus("current")
_CondDataDateTime_Type = DateAndTime
_CondDataDateTime_Object = MibTableColumn
condDataDateTime = _CondDataDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 11),
    _CondDataDateTime_Type()
)
condDataDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataDateTime.setStatus("current")


class _CondDataDesc_Type(OctetString):
    """Custom type condDataDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CondDataDesc_Type.__name__ = "OctetString"
_CondDataDesc_Object = MibTableColumn
condDataDesc = _CondDataDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 20, 1, 12),
    _CondDataDesc_Type()
)
condDataDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    condDataDesc.setStatus("current")
_AlmEnvDataTable_Object = MibTable
almEnvDataTable = _AlmEnvDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30)
)
if mibBuilder.loadTexts:
    almEnvDataTable.setStatus("current")
_AlmEnvDataEntry_Object = MibTableRow
almEnvDataEntry = _AlmEnvDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1)
)
almEnvDataEntry.setIndexNames(
    (0, "OPTIX-SONET-ALM-MIB", "almEnvDataAid"),
    (0, "OPTIX-SONET-ALM-MIB", "almEnvDataNtfcnCde"),
    (0, "OPTIX-SONET-ALM-MIB", "almEnvDataName"),
)
if mibBuilder.loadTexts:
    almEnvDataEntry.setStatus("current")
_AlmEnvDataAid_Type = Unsigned32
_AlmEnvDataAid_Object = MibTableColumn
almEnvDataAid = _AlmEnvDataAid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1, 1),
    _AlmEnvDataAid_Type()
)
almEnvDataAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almEnvDataAid.setStatus("current")
_AlmEnvDataNtfcnCde_Type = AlmDataNtfcnCdeType
_AlmEnvDataNtfcnCde_Object = MibTableColumn
almEnvDataNtfcnCde = _AlmEnvDataNtfcnCde_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1, 2),
    _AlmEnvDataNtfcnCde_Type()
)
almEnvDataNtfcnCde.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almEnvDataNtfcnCde.setStatus("current")
_AlmEnvDataName_Type = AlarmEventType
_AlmEnvDataName_Object = MibTableColumn
almEnvDataName = _AlmEnvDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1, 3),
    _AlmEnvDataName_Type()
)
almEnvDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almEnvDataName.setStatus("current")
_AlmEnvDataDateTime_Type = DateAndTime
_AlmEnvDataDateTime_Object = MibTableColumn
almEnvDataDateTime = _AlmEnvDataDateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1, 4),
    _AlmEnvDataDateTime_Type()
)
almEnvDataDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almEnvDataDateTime.setStatus("current")


class _AlmEnvDataCondDesc_Type(OctetString):
    """Custom type almEnvDataCondDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AlmEnvDataCondDesc_Type.__name__ = "OctetString"
_AlmEnvDataCondDesc_Object = MibTableColumn
almEnvDataCondDesc = _AlmEnvDataCondDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 10, 30, 1, 5),
    _AlmEnvDataCondDesc_Type()
)
almEnvDataCondDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almEnvDataCondDesc.setStatus("current")
_AlmSummary_ObjectIdentity = ObjectIdentity
almSummary = _AlmSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 11)
)
_AlmSummaryCritical_Type = Integer32
_AlmSummaryCritical_Object = MibScalar
almSummaryCritical = _AlmSummaryCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 11, 10),
    _AlmSummaryCritical_Type()
)
almSummaryCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almSummaryCritical.setStatus("current")
_AlmSummaryMajor_Type = Integer32
_AlmSummaryMajor_Object = MibScalar
almSummaryMajor = _AlmSummaryMajor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 11, 20),
    _AlmSummaryMajor_Type()
)
almSummaryMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almSummaryMajor.setStatus("current")
_AlmSummaryMinor_Type = Integer32
_AlmSummaryMinor_Object = MibScalar
almSummaryMinor = _AlmSummaryMinor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 11, 30),
    _AlmSummaryMinor_Type()
)
almSummaryMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almSummaryMinor.setStatus("current")
_OptixSonetAlarmConformance_ObjectIdentity = ObjectIdentity
optixSonetAlarmConformance = _OptixSonetAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 20)
)
_OptixSonetAlarmGroups_ObjectIdentity = ObjectIdentity
optixSonetAlarmGroups = _OptixSonetAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 20, 1)
)
_OptixSonetAlarmCompliances_ObjectIdentity = ObjectIdentity
optixSonetAlarmCompliances = _OptixSonetAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 20, 2)
)

# Managed Objects groups

optixSonetAlarmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 20, 1, 1)
)
optixSonetAlarmObjectGroup.setObjects(
      *(("OPTIX-SONET-ALM-MIB", "almDataMOD2"),
        ("OPTIX-SONET-ALM-MIB", "almDataSlot"),
        ("OPTIX-SONET-ALM-MIB", "almDataPort"),
        ("OPTIX-SONET-ALM-MIB", "almDataPath"),
        ("OPTIX-SONET-ALM-MIB", "almDataVT"),
        ("OPTIX-SONET-ALM-MIB", "almDataNtfcnCde"),
        ("OPTIX-SONET-ALM-MIB", "almDataName"),
        ("OPTIX-SONET-ALM-MIB", "almDataSrvEff"),
        ("OPTIX-SONET-ALM-MIB", "almDataLocation"),
        ("OPTIX-SONET-ALM-MIB", "almDataDirection"),
        ("OPTIX-SONET-ALM-MIB", "almDataDateTime"),
        ("OPTIX-SONET-ALM-MIB", "almDataDesc"),
        ("OPTIX-SONET-ALM-MIB", "almDataAiddet"),
        ("OPTIX-SONET-ALM-MIB", "condDataMOD2"),
        ("OPTIX-SONET-ALM-MIB", "condDataSlot"),
        ("OPTIX-SONET-ALM-MIB", "condDataPort"),
        ("OPTIX-SONET-ALM-MIB", "condDataPath"),
        ("OPTIX-SONET-ALM-MIB", "condDataVT"),
        ("OPTIX-SONET-ALM-MIB", "condDataName"),
        ("OPTIX-SONET-ALM-MIB", "condDataLocation"),
        ("OPTIX-SONET-ALM-MIB", "condDataDirection"),
        ("OPTIX-SONET-ALM-MIB", "condDataNtfcnCde"),
        ("OPTIX-SONET-ALM-MIB", "condDataSrvEff"),
        ("OPTIX-SONET-ALM-MIB", "condDataDateTime"),
        ("OPTIX-SONET-ALM-MIB", "condDataDesc"),
        ("OPTIX-SONET-ALM-MIB", "almEnvDataAid"),
        ("OPTIX-SONET-ALM-MIB", "almEnvDataNtfcnCde"),
        ("OPTIX-SONET-ALM-MIB", "almEnvDataName"),
        ("OPTIX-SONET-ALM-MIB", "almEnvDataDateTime"),
        ("OPTIX-SONET-ALM-MIB", "almEnvDataCondDesc"))
)
if mibBuilder.loadTexts:
    optixSonetAlarmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

optixSonetAlarmBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 10, 20, 2, 1)
)
if mibBuilder.loadTexts:
    optixSonetAlarmBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-ALM-MIB",
    **{"optixSonetAlarm": optixSonetAlarm,
       "almData": almData,
       "almDataTable": almDataTable,
       "almDataEntry": almDataEntry,
       "almDataMOD2": almDataMOD2,
       "almDataSlot": almDataSlot,
       "almDataPort": almDataPort,
       "almDataPath": almDataPath,
       "almDataVT": almDataVT,
       "almDataNtfcnCde": almDataNtfcnCde,
       "almDataName": almDataName,
       "almDataSrvEff": almDataSrvEff,
       "almDataLocation": almDataLocation,
       "almDataDirection": almDataDirection,
       "almDataDateTime": almDataDateTime,
       "almDataDesc": almDataDesc,
       "almDataAiddet": almDataAiddet,
       "condDataTable": condDataTable,
       "condDataEntry": condDataEntry,
       "condDataMOD2": condDataMOD2,
       "condDataSlot": condDataSlot,
       "condDataPort": condDataPort,
       "condDataPath": condDataPath,
       "condDataVT": condDataVT,
       "condDataName": condDataName,
       "condDataLocation": condDataLocation,
       "condDataDirection": condDataDirection,
       "condDataNtfcnCde": condDataNtfcnCde,
       "condDataSrvEff": condDataSrvEff,
       "condDataDateTime": condDataDateTime,
       "condDataDesc": condDataDesc,
       "almEnvDataTable": almEnvDataTable,
       "almEnvDataEntry": almEnvDataEntry,
       "almEnvDataAid": almEnvDataAid,
       "almEnvDataNtfcnCde": almEnvDataNtfcnCde,
       "almEnvDataName": almEnvDataName,
       "almEnvDataDateTime": almEnvDataDateTime,
       "almEnvDataCondDesc": almEnvDataCondDesc,
       "almSummary": almSummary,
       "almSummaryCritical": almSummaryCritical,
       "almSummaryMajor": almSummaryMajor,
       "almSummaryMinor": almSummaryMinor,
       "optixSonetAlarmConformance": optixSonetAlarmConformance,
       "optixSonetAlarmGroups": optixSonetAlarmGroups,
       "optixSonetAlarmObjectGroup": optixSonetAlarmObjectGroup,
       "optixSonetAlarmCompliances": optixSonetAlarmCompliances,
       "optixSonetAlarmBasicCompliance": optixSonetAlarmBasicCompliance}
)
