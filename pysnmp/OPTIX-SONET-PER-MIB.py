# SNMP MIB module (OPTIX-SONET-PER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPTIX-SONET-PER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:31 2024
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

(DirectionType,
 LocationType,
 MOD2Type,
 PerformanceEventType,
 ValidflagType) = mibBuilder.importSymbols(
    "OPTIX-SONET-TC-MIB",
    "DirectionType",
    "LocationType",
    "MOD2Type",
    "PerformanceEventType",
    "ValidflagType")

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

optixSonetPerformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20)
)
optixSonetPerformance.setRevisions(
        ("2006-02-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PmData_ObjectIdentity = ObjectIdentity
pmData = _PmData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10)
)
_Per15mCurDataTable_Object = MibTable
per15mCurDataTable = _Per15mCurDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10)
)
if mibBuilder.loadTexts:
    per15mCurDataTable.setStatus("current")
_Per15mCurDataEntry_Object = MibTableRow
per15mCurDataEntry = _Per15mCurDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1)
)
per15mCurDataEntry.setIndexNames(
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataMOD2"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataSlot"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataPort"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataPath"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataVT"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataName"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataLocation"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mCurDataDirection"),
)
if mibBuilder.loadTexts:
    per15mCurDataEntry.setStatus("current")
_Pm15mCurDataMOD2_Type = MOD2Type
_Pm15mCurDataMOD2_Object = MibTableColumn
pm15mCurDataMOD2 = _Pm15mCurDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 1),
    _Pm15mCurDataMOD2_Type()
)
pm15mCurDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataMOD2.setStatus("current")
_Pm15mCurDataSlot_Type = Unsigned32
_Pm15mCurDataSlot_Object = MibTableColumn
pm15mCurDataSlot = _Pm15mCurDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 2),
    _Pm15mCurDataSlot_Type()
)
pm15mCurDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataSlot.setStatus("current")
_Pm15mCurDataPort_Type = Unsigned32
_Pm15mCurDataPort_Object = MibTableColumn
pm15mCurDataPort = _Pm15mCurDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 3),
    _Pm15mCurDataPort_Type()
)
pm15mCurDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataPort.setStatus("current")
_Pm15mCurDataPath_Type = Unsigned32
_Pm15mCurDataPath_Object = MibTableColumn
pm15mCurDataPath = _Pm15mCurDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 4),
    _Pm15mCurDataPath_Type()
)
pm15mCurDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataPath.setStatus("current")
_Pm15mCurDataVT_Type = Unsigned32
_Pm15mCurDataVT_Object = MibTableColumn
pm15mCurDataVT = _Pm15mCurDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 5),
    _Pm15mCurDataVT_Type()
)
pm15mCurDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataVT.setStatus("current")
_Pm15mCurDataName_Type = PerformanceEventType
_Pm15mCurDataName_Object = MibTableColumn
pm15mCurDataName = _Pm15mCurDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 6),
    _Pm15mCurDataName_Type()
)
pm15mCurDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataName.setStatus("current")
_Pm15mCurDataLocation_Type = LocationType
_Pm15mCurDataLocation_Object = MibTableColumn
pm15mCurDataLocation = _Pm15mCurDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 7),
    _Pm15mCurDataLocation_Type()
)
pm15mCurDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataLocation.setStatus("current")
_Pm15mCurDataDirection_Type = DirectionType
_Pm15mCurDataDirection_Object = MibTableColumn
pm15mCurDataDirection = _Pm15mCurDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 8),
    _Pm15mCurDataDirection_Type()
)
pm15mCurDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataDirection.setStatus("current")
_Pm15mCurDataMonVal_Type = Integer32
_Pm15mCurDataMonVal_Object = MibTableColumn
pm15mCurDataMonVal = _Pm15mCurDataMonVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 9),
    _Pm15mCurDataMonVal_Type()
)
pm15mCurDataMonVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataMonVal.setStatus("current")
_Pm15mCurDataVldty_Type = ValidflagType
_Pm15mCurDataVldty_Object = MibTableColumn
pm15mCurDataVldty = _Pm15mCurDataVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 10),
    _Pm15mCurDataVldty_Type()
)
pm15mCurDataVldty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataVldty.setStatus("current")
_Pm15mCurDataStartTime_Type = DateAndTime
_Pm15mCurDataStartTime_Object = MibTableColumn
pm15mCurDataStartTime = _Pm15mCurDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 10, 1, 11),
    _Pm15mCurDataStartTime_Type()
)
pm15mCurDataStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mCurDataStartTime.setStatus("current")
_Per15mHisDataTable_Object = MibTable
per15mHisDataTable = _Per15mHisDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20)
)
if mibBuilder.loadTexts:
    per15mHisDataTable.setStatus("current")
_Per15mHisDataEntry_Object = MibTableRow
per15mHisDataEntry = _Per15mHisDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1)
)
per15mHisDataEntry.setIndexNames(
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataMOD2"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataSlot"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataPort"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataPath"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataVT"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataName"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataLocation"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataDirection"),
    (0, "OPTIX-SONET-PER-MIB", "pm15mHisDataInterval"),
)
if mibBuilder.loadTexts:
    per15mHisDataEntry.setStatus("current")
_Pm15mHisDataMOD2_Type = MOD2Type
_Pm15mHisDataMOD2_Object = MibTableColumn
pm15mHisDataMOD2 = _Pm15mHisDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 1),
    _Pm15mHisDataMOD2_Type()
)
pm15mHisDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataMOD2.setStatus("current")
_Pm15mHisDataSlot_Type = Unsigned32
_Pm15mHisDataSlot_Object = MibTableColumn
pm15mHisDataSlot = _Pm15mHisDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 2),
    _Pm15mHisDataSlot_Type()
)
pm15mHisDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataSlot.setStatus("current")
_Pm15mHisDataPort_Type = Unsigned32
_Pm15mHisDataPort_Object = MibTableColumn
pm15mHisDataPort = _Pm15mHisDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 3),
    _Pm15mHisDataPort_Type()
)
pm15mHisDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataPort.setStatus("current")
_Pm15mHisDataPath_Type = Unsigned32
_Pm15mHisDataPath_Object = MibTableColumn
pm15mHisDataPath = _Pm15mHisDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 4),
    _Pm15mHisDataPath_Type()
)
pm15mHisDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataPath.setStatus("current")
_Pm15mHisDataVT_Type = Unsigned32
_Pm15mHisDataVT_Object = MibTableColumn
pm15mHisDataVT = _Pm15mHisDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 5),
    _Pm15mHisDataVT_Type()
)
pm15mHisDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataVT.setStatus("current")
_Pm15mHisDataName_Type = PerformanceEventType
_Pm15mHisDataName_Object = MibTableColumn
pm15mHisDataName = _Pm15mHisDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 6),
    _Pm15mHisDataName_Type()
)
pm15mHisDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataName.setStatus("current")
_Pm15mHisDataLocation_Type = LocationType
_Pm15mHisDataLocation_Object = MibTableColumn
pm15mHisDataLocation = _Pm15mHisDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 7),
    _Pm15mHisDataLocation_Type()
)
pm15mHisDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataLocation.setStatus("current")
_Pm15mHisDataDirection_Type = DirectionType
_Pm15mHisDataDirection_Object = MibTableColumn
pm15mHisDataDirection = _Pm15mHisDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 8),
    _Pm15mHisDataDirection_Type()
)
pm15mHisDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataDirection.setStatus("current")
_Pm15mHisDataInterval_Type = Unsigned32
_Pm15mHisDataInterval_Object = MibTableColumn
pm15mHisDataInterval = _Pm15mHisDataInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 9),
    _Pm15mHisDataInterval_Type()
)
pm15mHisDataInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataInterval.setStatus("current")
_Pm15mHisDataMonVal_Type = Integer32
_Pm15mHisDataMonVal_Object = MibTableColumn
pm15mHisDataMonVal = _Pm15mHisDataMonVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 10),
    _Pm15mHisDataMonVal_Type()
)
pm15mHisDataMonVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataMonVal.setStatus("current")
_Pm15mHisDataVldty_Type = ValidflagType
_Pm15mHisDataVldty_Object = MibTableColumn
pm15mHisDataVldty = _Pm15mHisDataVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 11),
    _Pm15mHisDataVldty_Type()
)
pm15mHisDataVldty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataVldty.setStatus("current")
_Pm15mHisDataStartTime_Type = DateAndTime
_Pm15mHisDataStartTime_Object = MibTableColumn
pm15mHisDataStartTime = _Pm15mHisDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 20, 1, 12),
    _Pm15mHisDataStartTime_Type()
)
pm15mHisDataStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm15mHisDataStartTime.setStatus("current")
_Per1dayCurDataTable_Object = MibTable
per1dayCurDataTable = _Per1dayCurDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30)
)
if mibBuilder.loadTexts:
    per1dayCurDataTable.setStatus("current")
_Per1dayCurDataEntry_Object = MibTableRow
per1dayCurDataEntry = _Per1dayCurDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1)
)
per1dayCurDataEntry.setIndexNames(
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataMOD2"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataSlot"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataPort"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataPath"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataVT"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataName"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataLocation"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayCurDataDirection"),
)
if mibBuilder.loadTexts:
    per1dayCurDataEntry.setStatus("current")
_Pm1dayCurDataMOD2_Type = MOD2Type
_Pm1dayCurDataMOD2_Object = MibTableColumn
pm1dayCurDataMOD2 = _Pm1dayCurDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 1),
    _Pm1dayCurDataMOD2_Type()
)
pm1dayCurDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataMOD2.setStatus("current")
_Pm1dayCurDataSlot_Type = Unsigned32
_Pm1dayCurDataSlot_Object = MibTableColumn
pm1dayCurDataSlot = _Pm1dayCurDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 2),
    _Pm1dayCurDataSlot_Type()
)
pm1dayCurDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataSlot.setStatus("current")
_Pm1dayCurDataPort_Type = Unsigned32
_Pm1dayCurDataPort_Object = MibTableColumn
pm1dayCurDataPort = _Pm1dayCurDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 3),
    _Pm1dayCurDataPort_Type()
)
pm1dayCurDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataPort.setStatus("current")
_Pm1dayCurDataPath_Type = Unsigned32
_Pm1dayCurDataPath_Object = MibTableColumn
pm1dayCurDataPath = _Pm1dayCurDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 4),
    _Pm1dayCurDataPath_Type()
)
pm1dayCurDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataPath.setStatus("current")
_Pm1dayCurDataVT_Type = Unsigned32
_Pm1dayCurDataVT_Object = MibTableColumn
pm1dayCurDataVT = _Pm1dayCurDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 5),
    _Pm1dayCurDataVT_Type()
)
pm1dayCurDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataVT.setStatus("current")
_Pm1dayCurDataName_Type = PerformanceEventType
_Pm1dayCurDataName_Object = MibTableColumn
pm1dayCurDataName = _Pm1dayCurDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 6),
    _Pm1dayCurDataName_Type()
)
pm1dayCurDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataName.setStatus("current")
_Pm1dayCurDataLocation_Type = LocationType
_Pm1dayCurDataLocation_Object = MibTableColumn
pm1dayCurDataLocation = _Pm1dayCurDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 7),
    _Pm1dayCurDataLocation_Type()
)
pm1dayCurDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataLocation.setStatus("current")
_Pm1dayCurDataDirection_Type = DirectionType
_Pm1dayCurDataDirection_Object = MibTableColumn
pm1dayCurDataDirection = _Pm1dayCurDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 8),
    _Pm1dayCurDataDirection_Type()
)
pm1dayCurDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataDirection.setStatus("current")
_Pm1dayCurDataMonVal_Type = Integer32
_Pm1dayCurDataMonVal_Object = MibTableColumn
pm1dayCurDataMonVal = _Pm1dayCurDataMonVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 9),
    _Pm1dayCurDataMonVal_Type()
)
pm1dayCurDataMonVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataMonVal.setStatus("current")
_Pm1dayCurDataVldty_Type = ValidflagType
_Pm1dayCurDataVldty_Object = MibTableColumn
pm1dayCurDataVldty = _Pm1dayCurDataVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 10),
    _Pm1dayCurDataVldty_Type()
)
pm1dayCurDataVldty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataVldty.setStatus("current")
_Pm1dayCurDataStartTime_Type = DateAndTime
_Pm1dayCurDataStartTime_Object = MibTableColumn
pm1dayCurDataStartTime = _Pm1dayCurDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 30, 1, 11),
    _Pm1dayCurDataStartTime_Type()
)
pm1dayCurDataStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayCurDataStartTime.setStatus("current")
_Per1dayHisDataTable_Object = MibTable
per1dayHisDataTable = _Per1dayHisDataTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40)
)
if mibBuilder.loadTexts:
    per1dayHisDataTable.setStatus("current")
_Per1dayHisDataEntry_Object = MibTableRow
per1dayHisDataEntry = _Per1dayHisDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1)
)
per1dayHisDataEntry.setIndexNames(
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataMOD2"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataSlot"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataPort"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataPath"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataVT"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataName"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataLocation"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataDirection"),
    (0, "OPTIX-SONET-PER-MIB", "pm1dayHisDataInterval"),
)
if mibBuilder.loadTexts:
    per1dayHisDataEntry.setStatus("current")
_Pm1dayHisDataMOD2_Type = MOD2Type
_Pm1dayHisDataMOD2_Object = MibTableColumn
pm1dayHisDataMOD2 = _Pm1dayHisDataMOD2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 1),
    _Pm1dayHisDataMOD2_Type()
)
pm1dayHisDataMOD2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataMOD2.setStatus("current")
_Pm1dayHisDataSlot_Type = Unsigned32
_Pm1dayHisDataSlot_Object = MibTableColumn
pm1dayHisDataSlot = _Pm1dayHisDataSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 2),
    _Pm1dayHisDataSlot_Type()
)
pm1dayHisDataSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataSlot.setStatus("current")
_Pm1dayHisDataPort_Type = Unsigned32
_Pm1dayHisDataPort_Object = MibTableColumn
pm1dayHisDataPort = _Pm1dayHisDataPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 3),
    _Pm1dayHisDataPort_Type()
)
pm1dayHisDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataPort.setStatus("current")
_Pm1dayHisDataPath_Type = Unsigned32
_Pm1dayHisDataPath_Object = MibTableColumn
pm1dayHisDataPath = _Pm1dayHisDataPath_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 4),
    _Pm1dayHisDataPath_Type()
)
pm1dayHisDataPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataPath.setStatus("current")
_Pm1dayHisDataVT_Type = Unsigned32
_Pm1dayHisDataVT_Object = MibTableColumn
pm1dayHisDataVT = _Pm1dayHisDataVT_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 5),
    _Pm1dayHisDataVT_Type()
)
pm1dayHisDataVT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataVT.setStatus("current")
_Pm1dayHisDataName_Type = PerformanceEventType
_Pm1dayHisDataName_Object = MibTableColumn
pm1dayHisDataName = _Pm1dayHisDataName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 6),
    _Pm1dayHisDataName_Type()
)
pm1dayHisDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataName.setStatus("current")
_Pm1dayHisDataLocation_Type = LocationType
_Pm1dayHisDataLocation_Object = MibTableColumn
pm1dayHisDataLocation = _Pm1dayHisDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 7),
    _Pm1dayHisDataLocation_Type()
)
pm1dayHisDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataLocation.setStatus("current")
_Pm1dayHisDataDirection_Type = DirectionType
_Pm1dayHisDataDirection_Object = MibTableColumn
pm1dayHisDataDirection = _Pm1dayHisDataDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 8),
    _Pm1dayHisDataDirection_Type()
)
pm1dayHisDataDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataDirection.setStatus("current")
_Pm1dayHisDataInterval_Type = Unsigned32
_Pm1dayHisDataInterval_Object = MibTableColumn
pm1dayHisDataInterval = _Pm1dayHisDataInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 9),
    _Pm1dayHisDataInterval_Type()
)
pm1dayHisDataInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataInterval.setStatus("current")
_Pm1dayHisDataMonVal_Type = Integer32
_Pm1dayHisDataMonVal_Object = MibTableColumn
pm1dayHisDataMonVal = _Pm1dayHisDataMonVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 10),
    _Pm1dayHisDataMonVal_Type()
)
pm1dayHisDataMonVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataMonVal.setStatus("current")
_Pm1dayHisDataVldty_Type = ValidflagType
_Pm1dayHisDataVldty_Object = MibTableColumn
pm1dayHisDataVldty = _Pm1dayHisDataVldty_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 11),
    _Pm1dayHisDataVldty_Type()
)
pm1dayHisDataVldty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataVldty.setStatus("current")
_Pm1dayHisDataStartTime_Type = DateAndTime
_Pm1dayHisDataStartTime_Object = MibTableColumn
pm1dayHisDataStartTime = _Pm1dayHisDataStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 10, 40, 1, 12),
    _Pm1dayHisDataStartTime_Type()
)
pm1dayHisDataStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pm1dayHisDataStartTime.setStatus("current")
_OptixSonetPmConformance_ObjectIdentity = ObjectIdentity
optixSonetPmConformance = _OptixSonetPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 20)
)
_OptixSonetPmGroups_ObjectIdentity = ObjectIdentity
optixSonetPmGroups = _OptixSonetPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 20, 1)
)
_OptixSonetPmCompliances_ObjectIdentity = ObjectIdentity
optixSonetPmCompliances = _OptixSonetPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 20, 2)
)

# Managed Objects groups

optixSonetPmObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 20, 1, 1)
)
optixSonetPmObjectGroup.setObjects(
      *(("OPTIX-SONET-PER-MIB", "pm15mCurDataMOD2"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataSlot"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataPort"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataPath"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataVT"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataName"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataLocation"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataDirection"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataMonVal"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataVldty"),
        ("OPTIX-SONET-PER-MIB", "pm15mCurDataStartTime"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataMOD2"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataSlot"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataPort"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataPath"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataVT"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataName"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataLocation"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataDirection"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataInterval"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataMonVal"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataVldty"),
        ("OPTIX-SONET-PER-MIB", "pm15mHisDataStartTime"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataMOD2"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataSlot"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataPort"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataPath"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataVT"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataName"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataLocation"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataDirection"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataMonVal"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataVldty"),
        ("OPTIX-SONET-PER-MIB", "pm1dayCurDataStartTime"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataMOD2"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataSlot"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataPort"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataPath"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataVT"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataName"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataLocation"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataDirection"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataInterval"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataMonVal"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataVldty"),
        ("OPTIX-SONET-PER-MIB", "pm1dayHisDataStartTime"))
)
if mibBuilder.loadTexts:
    optixSonetPmObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

optixSonetPmBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 2, 25, 3, 20, 20, 20, 2, 1)
)
if mibBuilder.loadTexts:
    optixSonetPmBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPTIX-SONET-PER-MIB",
    **{"optixSonetPerformance": optixSonetPerformance,
       "pmData": pmData,
       "per15mCurDataTable": per15mCurDataTable,
       "per15mCurDataEntry": per15mCurDataEntry,
       "pm15mCurDataMOD2": pm15mCurDataMOD2,
       "pm15mCurDataSlot": pm15mCurDataSlot,
       "pm15mCurDataPort": pm15mCurDataPort,
       "pm15mCurDataPath": pm15mCurDataPath,
       "pm15mCurDataVT": pm15mCurDataVT,
       "pm15mCurDataName": pm15mCurDataName,
       "pm15mCurDataLocation": pm15mCurDataLocation,
       "pm15mCurDataDirection": pm15mCurDataDirection,
       "pm15mCurDataMonVal": pm15mCurDataMonVal,
       "pm15mCurDataVldty": pm15mCurDataVldty,
       "pm15mCurDataStartTime": pm15mCurDataStartTime,
       "per15mHisDataTable": per15mHisDataTable,
       "per15mHisDataEntry": per15mHisDataEntry,
       "pm15mHisDataMOD2": pm15mHisDataMOD2,
       "pm15mHisDataSlot": pm15mHisDataSlot,
       "pm15mHisDataPort": pm15mHisDataPort,
       "pm15mHisDataPath": pm15mHisDataPath,
       "pm15mHisDataVT": pm15mHisDataVT,
       "pm15mHisDataName": pm15mHisDataName,
       "pm15mHisDataLocation": pm15mHisDataLocation,
       "pm15mHisDataDirection": pm15mHisDataDirection,
       "pm15mHisDataInterval": pm15mHisDataInterval,
       "pm15mHisDataMonVal": pm15mHisDataMonVal,
       "pm15mHisDataVldty": pm15mHisDataVldty,
       "pm15mHisDataStartTime": pm15mHisDataStartTime,
       "per1dayCurDataTable": per1dayCurDataTable,
       "per1dayCurDataEntry": per1dayCurDataEntry,
       "pm1dayCurDataMOD2": pm1dayCurDataMOD2,
       "pm1dayCurDataSlot": pm1dayCurDataSlot,
       "pm1dayCurDataPort": pm1dayCurDataPort,
       "pm1dayCurDataPath": pm1dayCurDataPath,
       "pm1dayCurDataVT": pm1dayCurDataVT,
       "pm1dayCurDataName": pm1dayCurDataName,
       "pm1dayCurDataLocation": pm1dayCurDataLocation,
       "pm1dayCurDataDirection": pm1dayCurDataDirection,
       "pm1dayCurDataMonVal": pm1dayCurDataMonVal,
       "pm1dayCurDataVldty": pm1dayCurDataVldty,
       "pm1dayCurDataStartTime": pm1dayCurDataStartTime,
       "per1dayHisDataTable": per1dayHisDataTable,
       "per1dayHisDataEntry": per1dayHisDataEntry,
       "pm1dayHisDataMOD2": pm1dayHisDataMOD2,
       "pm1dayHisDataSlot": pm1dayHisDataSlot,
       "pm1dayHisDataPort": pm1dayHisDataPort,
       "pm1dayHisDataPath": pm1dayHisDataPath,
       "pm1dayHisDataVT": pm1dayHisDataVT,
       "pm1dayHisDataName": pm1dayHisDataName,
       "pm1dayHisDataLocation": pm1dayHisDataLocation,
       "pm1dayHisDataDirection": pm1dayHisDataDirection,
       "pm1dayHisDataInterval": pm1dayHisDataInterval,
       "pm1dayHisDataMonVal": pm1dayHisDataMonVal,
       "pm1dayHisDataVldty": pm1dayHisDataVldty,
       "pm1dayHisDataStartTime": pm1dayHisDataStartTime,
       "optixSonetPmConformance": optixSonetPmConformance,
       "optixSonetPmGroups": optixSonetPmGroups,
       "optixSonetPmObjectGroup": optixSonetPmObjectGroup,
       "optixSonetPmCompliances": optixSonetPmCompliances,
       "optixSonetPmBasicCompliance": optixSonetPmBasicCompliance}
)
