# SNMP MIB module (AVICI-BAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVICI-BAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:40 2024
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

(aviciMibs,) = mibBuilder.importSymbols(
    "AVICI-SMI",
    "aviciMibs")

(aviciSysTrapDescr,) = mibBuilder.importSymbols(
    "AVICI-SYSTEM-MIB",
    "aviciSysTrapDescr")

(AviciBayType,
 AviciHighAvailabilityType,
 AviciLedValue,
 AviciPartNumberType,
 AviciProductIdType,
 AviciRevisionType,
 AviciSerialNumberType,
 AviciSlotType,
 AviciUnitType,
 AviciVoltageType) = mibBuilder.importSymbols(
    "AVICI-TC",
    "AviciBayType",
    "AviciHighAvailabilityType",
    "AviciLedValue",
    "AviciPartNumberType",
    "AviciProductIdType",
    "AviciRevisionType",
    "AviciSerialNumberType",
    "AviciSlotType",
    "AviciUnitType",
    "AviciVoltageType")

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

aviciBayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AviciBayObjects_ObjectIdentity = ObjectIdentity
aviciBayObjects = _AviciBayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1)
)
_AviciBayTable_Object = MibTable
aviciBayTable = _AviciBayTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aviciBayTable.setStatus("current")
_AviciBayEntry_Object = MibTableRow
aviciBayEntry = _AviciBayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1)
)
aviciBayEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
)
if mibBuilder.loadTexts:
    aviciBayEntry.setStatus("current")
_AviciBayIndex_Type = AviciBayType
_AviciBayIndex_Object = MibTableColumn
aviciBayIndex = _AviciBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 1),
    _AviciBayIndex_Type()
)
aviciBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayIndex.setStatus("current")
_AviciBayCriticalLed_Type = AviciLedValue
_AviciBayCriticalLed_Object = MibTableColumn
aviciBayCriticalLed = _AviciBayCriticalLed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 2),
    _AviciBayCriticalLed_Type()
)
aviciBayCriticalLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCriticalLed.setStatus("current")
_AviciBayMajorLed_Type = AviciLedValue
_AviciBayMajorLed_Object = MibTableColumn
aviciBayMajorLed = _AviciBayMajorLed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 3),
    _AviciBayMajorLed_Type()
)
aviciBayMajorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayMajorLed.setStatus("current")
_AviciBayMinorLed_Type = AviciLedValue
_AviciBayMinorLed_Object = MibTableColumn
aviciBayMinorLed = _AviciBayMinorLed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 4),
    _AviciBayMinorLed_Type()
)
aviciBayMinorLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayMinorLed.setStatus("current")


class _AviciBayAlarmCutOff_Type(Integer32):
    """Custom type aviciBayAlarmCutOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AviciBayAlarmCutOff_Type.__name__ = "Integer32"
_AviciBayAlarmCutOff_Object = MibTableColumn
aviciBayAlarmCutOff = _AviciBayAlarmCutOff_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 5),
    _AviciBayAlarmCutOff_Type()
)
aviciBayAlarmCutOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayAlarmCutOff.setStatus("current")
_AviciBayModTempCriticalThreshold_Type = Integer32
_AviciBayModTempCriticalThreshold_Object = MibTableColumn
aviciBayModTempCriticalThreshold = _AviciBayModTempCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 6),
    _AviciBayModTempCriticalThreshold_Type()
)
aviciBayModTempCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayModTempCriticalThreshold.setStatus("current")
_AviciBayModTempMajorThreshold_Type = Integer32
_AviciBayModTempMajorThreshold_Object = MibTableColumn
aviciBayModTempMajorThreshold = _AviciBayModTempMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 7),
    _AviciBayModTempMajorThreshold_Type()
)
aviciBayModTempMajorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayModTempMajorThreshold.setStatus("current")
_AviciBayModTempMinorThreshold_Type = Integer32
_AviciBayModTempMinorThreshold_Object = MibTableColumn
aviciBayModTempMinorThreshold = _AviciBayModTempMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 8),
    _AviciBayModTempMinorThreshold_Type()
)
aviciBayModTempMinorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayModTempMinorThreshold.setStatus("current")
_AviciBayTempCriticalThreshold_Type = Integer32
_AviciBayTempCriticalThreshold_Object = MibTableColumn
aviciBayTempCriticalThreshold = _AviciBayTempCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 9),
    _AviciBayTempCriticalThreshold_Type()
)
aviciBayTempCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayTempCriticalThreshold.setStatus("current")
_AviciBayTempMajorThreshold_Type = Integer32
_AviciBayTempMajorThreshold_Object = MibTableColumn
aviciBayTempMajorThreshold = _AviciBayTempMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 10),
    _AviciBayTempMajorThreshold_Type()
)
aviciBayTempMajorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayTempMajorThreshold.setStatus("current")
_AviciBayTempMinorThreshold_Type = Integer32
_AviciBayTempMinorThreshold_Object = MibTableColumn
aviciBayTempMinorThreshold = _AviciBayTempMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 1, 1, 11),
    _AviciBayTempMinorThreshold_Type()
)
aviciBayTempMinorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayTempMinorThreshold.setStatus("current")
_AviciBayControllerTable_Object = MibTable
aviciBayControllerTable = _AviciBayControllerTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    aviciBayControllerTable.setStatus("current")
_AviciBayControllerEntry_Object = MibTableRow
aviciBayControllerEntry = _AviciBayControllerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1)
)
aviciBayControllerEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciBayControllerIndex"),
)
if mibBuilder.loadTexts:
    aviciBayControllerEntry.setStatus("current")


class _AviciBayControllerIndex_Type(Integer32):
    """Custom type aviciBayControllerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AviciBayControllerIndex_Type.__name__ = "Integer32"
_AviciBayControllerIndex_Object = MibTableColumn
aviciBayControllerIndex = _AviciBayControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 1),
    _AviciBayControllerIndex_Type()
)
aviciBayControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerIndex.setStatus("current")


class _AviciBayControllerOperStatus_Type(Integer32):
    """Custom type aviciBayControllerOperStatus based on Integer32"""
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
        *(("active", 3),
          ("down", 1),
          ("failed", 4),
          ("passive", 2))
    )


_AviciBayControllerOperStatus_Type.__name__ = "Integer32"
_AviciBayControllerOperStatus_Object = MibTableColumn
aviciBayControllerOperStatus = _AviciBayControllerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 2),
    _AviciBayControllerOperStatus_Type()
)
aviciBayControllerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerOperStatus.setStatus("current")


class _AviciBayControllerAdminStatus_Type(Integer32):
    """Custom type aviciBayControllerAdminStatus based on Integer32"""
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
        *(("active", 3),
          ("diagnostic", 4),
          ("passive", 2),
          ("reboot", 1))
    )


_AviciBayControllerAdminStatus_Type.__name__ = "Integer32"
_AviciBayControllerAdminStatus_Object = MibTableColumn
aviciBayControllerAdminStatus = _AviciBayControllerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 3),
    _AviciBayControllerAdminStatus_Type()
)
aviciBayControllerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aviciBayControllerAdminStatus.setStatus("current")
_AviciBayControllerPartNumber_Type = AviciPartNumberType
_AviciBayControllerPartNumber_Object = MibTableColumn
aviciBayControllerPartNumber = _AviciBayControllerPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 4),
    _AviciBayControllerPartNumber_Type()
)
aviciBayControllerPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerPartNumber.setStatus("current")
_AviciBayControllerSerialNumber_Type = AviciSerialNumberType
_AviciBayControllerSerialNumber_Object = MibTableColumn
aviciBayControllerSerialNumber = _AviciBayControllerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 5),
    _AviciBayControllerSerialNumber_Type()
)
aviciBayControllerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerSerialNumber.setStatus("current")
_AviciBayControllerRevision_Type = AviciRevisionType
_AviciBayControllerRevision_Object = MibTableColumn
aviciBayControllerRevision = _AviciBayControllerRevision_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 6),
    _AviciBayControllerRevision_Type()
)
aviciBayControllerRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerRevision.setStatus("current")


class _AviciBayControllerSoftwareVersion_Type(DisplayString):
    """Custom type aviciBayControllerSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayControllerSoftwareVersion_Type.__name__ = "DisplayString"
_AviciBayControllerSoftwareVersion_Object = MibTableColumn
aviciBayControllerSoftwareVersion = _AviciBayControllerSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 7),
    _AviciBayControllerSoftwareVersion_Type()
)
aviciBayControllerSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerSoftwareVersion.setStatus("current")


class _AviciBayControllerFirmwareVersion_Type(DisplayString):
    """Custom type aviciBayControllerFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayControllerFirmwareVersion_Type.__name__ = "DisplayString"
_AviciBayControllerFirmwareVersion_Object = MibTableColumn
aviciBayControllerFirmwareVersion = _AviciBayControllerFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 8),
    _AviciBayControllerFirmwareVersion_Type()
)
aviciBayControllerFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerFirmwareVersion.setStatus("current")
_AviciBayControllerProductId_Type = AviciProductIdType
_AviciBayControllerProductId_Object = MibTableColumn
aviciBayControllerProductId = _AviciBayControllerProductId_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 9),
    _AviciBayControllerProductId_Type()
)
aviciBayControllerProductId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerProductId.setStatus("current")
_AviciBayControllerProductSerialNumber_Type = AviciSerialNumberType
_AviciBayControllerProductSerialNumber_Object = MibTableColumn
aviciBayControllerProductSerialNumber = _AviciBayControllerProductSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 10),
    _AviciBayControllerProductSerialNumber_Type()
)
aviciBayControllerProductSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerProductSerialNumber.setStatus("current")
_AviciBayControllerProductRevision_Type = AviciRevisionType
_AviciBayControllerProductRevision_Object = MibTableColumn
aviciBayControllerProductRevision = _AviciBayControllerProductRevision_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 11),
    _AviciBayControllerProductRevision_Type()
)
aviciBayControllerProductRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerProductRevision.setStatus("current")


class _AviciBayControllerDescr_Type(DisplayString):
    """Custom type aviciBayControllerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayControllerDescr_Type.__name__ = "DisplayString"
_AviciBayControllerDescr_Object = MibTableColumn
aviciBayControllerDescr = _AviciBayControllerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 2, 1, 12),
    _AviciBayControllerDescr_Type()
)
aviciBayControllerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayControllerDescr.setStatus("current")
_AviciBayVoltageTable_Object = MibTable
aviciBayVoltageTable = _AviciBayVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    aviciBayVoltageTable.setStatus("current")
_AviciBayVoltageEntry_Object = MibTableRow
aviciBayVoltageEntry = _AviciBayVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1)
)
aviciBayVoltageEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciBayVoltageIndex"),
)
if mibBuilder.loadTexts:
    aviciBayVoltageEntry.setStatus("current")


class _AviciBayVoltageIndex_Type(Integer32):
    """Custom type aviciBayVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AviciBayVoltageIndex_Type.__name__ = "Integer32"
_AviciBayVoltageIndex_Object = MibTableColumn
aviciBayVoltageIndex = _AviciBayVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1, 1),
    _AviciBayVoltageIndex_Type()
)
aviciBayVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayVoltageIndex.setStatus("current")
_AviciBayVoltageType_Type = AviciVoltageType
_AviciBayVoltageType_Object = MibTableColumn
aviciBayVoltageType = _AviciBayVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1, 2),
    _AviciBayVoltageType_Type()
)
aviciBayVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayVoltageType.setStatus("current")
_AviciBayVoltage_Type = Integer32
_AviciBayVoltage_Object = MibTableColumn
aviciBayVoltage = _AviciBayVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1, 3),
    _AviciBayVoltage_Type()
)
aviciBayVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayVoltage.setStatus("current")


class _AviciBayVoltageStatus_Type(Integer32):
    """Custom type aviciBayVoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inSpec", 1),
          ("outSpec", 2))
    )


_AviciBayVoltageStatus_Type.__name__ = "Integer32"
_AviciBayVoltageStatus_Object = MibTableColumn
aviciBayVoltageStatus = _AviciBayVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1, 4),
    _AviciBayVoltageStatus_Type()
)
aviciBayVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayVoltageStatus.setStatus("current")


class _AviciBayVoltageDescr_Type(DisplayString):
    """Custom type aviciBayVoltageDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayVoltageDescr_Type.__name__ = "DisplayString"
_AviciBayVoltageDescr_Object = MibTableColumn
aviciBayVoltageDescr = _AviciBayVoltageDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 3, 1, 5),
    _AviciBayVoltageDescr_Type()
)
aviciBayVoltageDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayVoltageDescr.setStatus("current")
_AviciBayFanTable_Object = MibTable
aviciBayFanTable = _AviciBayFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    aviciBayFanTable.setStatus("current")
_AviciBayFanEntry_Object = MibTableRow
aviciBayFanEntry = _AviciBayFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1)
)
aviciBayFanEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciBayFanIndex"),
)
if mibBuilder.loadTexts:
    aviciBayFanEntry.setStatus("current")


class _AviciBayFanIndex_Type(Integer32):
    """Custom type aviciBayFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AviciBayFanIndex_Type.__name__ = "Integer32"
_AviciBayFanIndex_Object = MibTableColumn
aviciBayFanIndex = _AviciBayFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 1),
    _AviciBayFanIndex_Type()
)
aviciBayFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanIndex.setStatus("current")


class _AviciBayFanAdminStatus_Type(Integer32):
    """Custom type aviciBayFanAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autonomous", 2),
          ("controlled", 3),
          ("offline", 1))
    )


_AviciBayFanAdminStatus_Type.__name__ = "Integer32"
_AviciBayFanAdminStatus_Object = MibTableColumn
aviciBayFanAdminStatus = _AviciBayFanAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 2),
    _AviciBayFanAdminStatus_Type()
)
aviciBayFanAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanAdminStatus.setStatus("current")


class _AviciBayFanOperStatus_Type(Integer32):
    """Custom type aviciBayFanOperStatus based on Integer32"""
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
        *(("autonomous", 2),
          ("controlled", 3),
          ("failed", 4),
          ("offline", 1))
    )


_AviciBayFanOperStatus_Type.__name__ = "Integer32"
_AviciBayFanOperStatus_Object = MibTableColumn
aviciBayFanOperStatus = _AviciBayFanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 3),
    _AviciBayFanOperStatus_Type()
)
aviciBayFanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanOperStatus.setStatus("current")


class _AviciBayFanSpeed_Type(Integer32):
    """Custom type aviciBayFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2700),
    )


_AviciBayFanSpeed_Type.__name__ = "Integer32"
_AviciBayFanSpeed_Object = MibTableColumn
aviciBayFanSpeed = _AviciBayFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 4),
    _AviciBayFanSpeed_Type()
)
aviciBayFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanSpeed.setStatus("current")
_AviciBayFanCurrTemp_Type = Integer32
_AviciBayFanCurrTemp_Object = MibTableColumn
aviciBayFanCurrTemp = _AviciBayFanCurrTemp_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 5),
    _AviciBayFanCurrTemp_Type()
)
aviciBayFanCurrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanCurrTemp.setStatus("current")
_AviciBayFanMaxTemp_Type = Gauge32
_AviciBayFanMaxTemp_Object = MibTableColumn
aviciBayFanMaxTemp = _AviciBayFanMaxTemp_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 6),
    _AviciBayFanMaxTemp_Type()
)
aviciBayFanMaxTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanMaxTemp.setStatus("current")
_AviciBayFanLedStatus_Type = AviciLedValue
_AviciBayFanLedStatus_Object = MibTableColumn
aviciBayFanLedStatus = _AviciBayFanLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 7),
    _AviciBayFanLedStatus_Type()
)
aviciBayFanLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanLedStatus.setStatus("current")


class _AviciBayFanCurrFailures_Type(Integer32):
    """Custom type aviciBayFanCurrFailures based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_AviciBayFanCurrFailures_Type.__name__ = "Integer32"
_AviciBayFanCurrFailures_Object = MibTableColumn
aviciBayFanCurrFailures = _AviciBayFanCurrFailures_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 8),
    _AviciBayFanCurrFailures_Type()
)
aviciBayFanCurrFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanCurrFailures.setStatus("current")


class _AviciBayFanDescr_Type(DisplayString):
    """Custom type aviciBayFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayFanDescr_Type.__name__ = "DisplayString"
_AviciBayFanDescr_Object = MibTableColumn
aviciBayFanDescr = _AviciBayFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 4, 1, 9),
    _AviciBayFanDescr_Type()
)
aviciBayFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayFanDescr.setStatus("current")
_AviciBaySlotTable_Object = MibTable
aviciBaySlotTable = _AviciBaySlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    aviciBaySlotTable.setStatus("current")
_AviciBaySlotEntry_Object = MibTableRow
aviciBaySlotEntry = _AviciBaySlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1)
)
aviciBaySlotEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciSlotIndex"),
)
if mibBuilder.loadTexts:
    aviciBaySlotEntry.setStatus("current")
_AviciSlotIndex_Type = AviciSlotType
_AviciSlotIndex_Object = MibTableColumn
aviciSlotIndex = _AviciSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 1),
    _AviciSlotIndex_Type()
)
aviciSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciSlotIndex.setStatus("current")


class _AviciBaySlotStatus_Type(Integer32):
    """Custom type aviciBaySlotStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("identified", 3),
          ("occupied", 2))
    )


_AviciBaySlotStatus_Type.__name__ = "Integer32"
_AviciBaySlotStatus_Object = MibTableColumn
aviciBaySlotStatus = _AviciBaySlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 2),
    _AviciBaySlotStatus_Type()
)
aviciBaySlotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotStatus.setStatus("current")
_AviciBaySlotRxOctets_Type = Counter32
_AviciBaySlotRxOctets_Object = MibTableColumn
aviciBaySlotRxOctets = _AviciBaySlotRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 3),
    _AviciBaySlotRxOctets_Type()
)
aviciBaySlotRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxOctets.setStatus("current")
_AviciBaySlotRxMessages_Type = Counter32
_AviciBaySlotRxMessages_Object = MibTableColumn
aviciBaySlotRxMessages = _AviciBaySlotRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 4),
    _AviciBaySlotRxMessages_Type()
)
aviciBaySlotRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxMessages.setStatus("current")
_AviciBaySlotRxDiscards_Type = Counter32
_AviciBaySlotRxDiscards_Object = MibTableColumn
aviciBaySlotRxDiscards = _AviciBaySlotRxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 5),
    _AviciBaySlotRxDiscards_Type()
)
aviciBaySlotRxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxDiscards.setStatus("current")
_AviciBaySlotRxProtoErrs_Type = Counter32
_AviciBaySlotRxProtoErrs_Object = MibTableColumn
aviciBaySlotRxProtoErrs = _AviciBaySlotRxProtoErrs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 6),
    _AviciBaySlotRxProtoErrs_Type()
)
aviciBaySlotRxProtoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxProtoErrs.setStatus("current")
_AviciBaySlotRxIOErrs_Type = Counter32
_AviciBaySlotRxIOErrs_Object = MibTableColumn
aviciBaySlotRxIOErrs = _AviciBaySlotRxIOErrs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 7),
    _AviciBaySlotRxIOErrs_Type()
)
aviciBaySlotRxIOErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxIOErrs.setStatus("current")
_AviciBaySlotRxTimeouts_Type = Counter32
_AviciBaySlotRxTimeouts_Object = MibTableColumn
aviciBaySlotRxTimeouts = _AviciBaySlotRxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 8),
    _AviciBaySlotRxTimeouts_Type()
)
aviciBaySlotRxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotRxTimeouts.setStatus("current")
_AviciBaySlotTxOctets_Type = Counter32
_AviciBaySlotTxOctets_Object = MibTableColumn
aviciBaySlotTxOctets = _AviciBaySlotTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 9),
    _AviciBaySlotTxOctets_Type()
)
aviciBaySlotTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxOctets.setStatus("current")
_AviciBaySlotTxMessages_Type = Counter32
_AviciBaySlotTxMessages_Object = MibTableColumn
aviciBaySlotTxMessages = _AviciBaySlotTxMessages_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 10),
    _AviciBaySlotTxMessages_Type()
)
aviciBaySlotTxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxMessages.setStatus("current")
_AviciBaySlotTxDiscards_Type = Counter32
_AviciBaySlotTxDiscards_Object = MibTableColumn
aviciBaySlotTxDiscards = _AviciBaySlotTxDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 11),
    _AviciBaySlotTxDiscards_Type()
)
aviciBaySlotTxDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxDiscards.setStatus("current")
_AviciBaySlotTxProtoErrs_Type = Counter32
_AviciBaySlotTxProtoErrs_Object = MibTableColumn
aviciBaySlotTxProtoErrs = _AviciBaySlotTxProtoErrs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 12),
    _AviciBaySlotTxProtoErrs_Type()
)
aviciBaySlotTxProtoErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxProtoErrs.setStatus("current")
_AviciBaySlotTxIOErrs_Type = Counter32
_AviciBaySlotTxIOErrs_Object = MibTableColumn
aviciBaySlotTxIOErrs = _AviciBaySlotTxIOErrs_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 13),
    _AviciBaySlotTxIOErrs_Type()
)
aviciBaySlotTxIOErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxIOErrs.setStatus("current")
_AviciBaySlotTxTimeouts_Type = Counter32
_AviciBaySlotTxTimeouts_Object = MibTableColumn
aviciBaySlotTxTimeouts = _AviciBaySlotTxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 5, 1, 14),
    _AviciBaySlotTxTimeouts_Type()
)
aviciBaySlotTxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBaySlotTxTimeouts.setStatus("current")
_AviciBayBreakerTable_Object = MibTable
aviciBayBreakerTable = _AviciBayBreakerTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    aviciBayBreakerTable.setStatus("current")
_AviciBayBreakerEntry_Object = MibTableRow
aviciBayBreakerEntry = _AviciBayBreakerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6, 1)
)
aviciBayBreakerEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciBayBreakerIndex"),
)
if mibBuilder.loadTexts:
    aviciBayBreakerEntry.setStatus("current")
_AviciBayBreakerIndex_Type = Integer32
_AviciBayBreakerIndex_Object = MibTableColumn
aviciBayBreakerIndex = _AviciBayBreakerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6, 1, 1),
    _AviciBayBreakerIndex_Type()
)
aviciBayBreakerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayBreakerIndex.setStatus("current")
_AviciBayBreakerType_Type = AviciHighAvailabilityType
_AviciBayBreakerType_Object = MibTableColumn
aviciBayBreakerType = _AviciBayBreakerType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6, 1, 2),
    _AviciBayBreakerType_Type()
)
aviciBayBreakerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayBreakerType.setStatus("current")


class _AviciBayBreakerStatus_Type(Integer32):
    """Custom type aviciBayBreakerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 3),
          ("open", 2),
          ("unknown", 1))
    )


_AviciBayBreakerStatus_Type.__name__ = "Integer32"
_AviciBayBreakerStatus_Object = MibTableColumn
aviciBayBreakerStatus = _AviciBayBreakerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6, 1, 3),
    _AviciBayBreakerStatus_Type()
)
aviciBayBreakerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayBreakerStatus.setStatus("current")


class _AviciBayBreakerDescr_Type(DisplayString):
    """Custom type aviciBayBreakerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayBreakerDescr_Type.__name__ = "DisplayString"
_AviciBayBreakerDescr_Object = MibTableColumn
aviciBayBreakerDescr = _AviciBayBreakerDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 6, 1, 4),
    _AviciBayBreakerDescr_Type()
)
aviciBayBreakerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayBreakerDescr.setStatus("current")
_AviciBayCoAlarmSystem_ObjectIdentity = ObjectIdentity
aviciBayCoAlarmSystem = _AviciBayCoAlarmSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 7)
)
_AviciBayCoActiveAlarmCount_Type = Integer32
_AviciBayCoActiveAlarmCount_Object = MibScalar
aviciBayCoActiveAlarmCount = _AviciBayCoActiveAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 7, 1),
    _AviciBayCoActiveAlarmCount_Type()
)
aviciBayCoActiveAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoActiveAlarmCount.setStatus("current")
_AviciBayCoAlarmLastChange_Type = TimeTicks
_AviciBayCoAlarmLastChange_Object = MibScalar
aviciBayCoAlarmLastChange = _AviciBayCoAlarmLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 7, 2),
    _AviciBayCoAlarmLastChange_Type()
)
aviciBayCoAlarmLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmLastChange.setStatus("current")
_AviciBayCoAlarmTable_Object = MibTable
aviciBayCoAlarmTable = _AviciBayCoAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8)
)
if mibBuilder.loadTexts:
    aviciBayCoAlarmTable.setStatus("current")
_AviciBayCoAlarmEntry_Object = MibTableRow
aviciBayCoAlarmEntry = _AviciBayCoAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1)
)
aviciBayCoAlarmEntry.setIndexNames(
    (0, "AVICI-BAY-MIB", "aviciBayIndex"),
    (0, "AVICI-BAY-MIB", "aviciBayCoAlarmIndex"),
)
if mibBuilder.loadTexts:
    aviciBayCoAlarmEntry.setStatus("current")


class _AviciBayCoAlarmIndex_Type(Integer32):
    """Custom type aviciBayCoAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AviciBayCoAlarmIndex_Type.__name__ = "Integer32"
_AviciBayCoAlarmIndex_Object = MibTableColumn
aviciBayCoAlarmIndex = _AviciBayCoAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 1),
    _AviciBayCoAlarmIndex_Type()
)
aviciBayCoAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmIndex.setStatus("current")


class _AviciBayCoAlarmType_Type(Integer32):
    """Custom type aviciBayCoAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("major", 2),
          ("minor", 3))
    )


_AviciBayCoAlarmType_Type.__name__ = "Integer32"
_AviciBayCoAlarmType_Object = MibTableColumn
aviciBayCoAlarmType = _AviciBayCoAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 2),
    _AviciBayCoAlarmType_Type()
)
aviciBayCoAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmType.setStatus("current")


class _AviciBayCoAlarmDescr_Type(DisplayString):
    """Custom type aviciBayCoAlarmDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AviciBayCoAlarmDescr_Type.__name__ = "DisplayString"
_AviciBayCoAlarmDescr_Object = MibTableColumn
aviciBayCoAlarmDescr = _AviciBayCoAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 3),
    _AviciBayCoAlarmDescr_Type()
)
aviciBayCoAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmDescr.setStatus("current")
_AviciBayCoAlarmTime_Type = TimeTicks
_AviciBayCoAlarmTime_Object = MibTableColumn
aviciBayCoAlarmTime = _AviciBayCoAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 4),
    _AviciBayCoAlarmTime_Type()
)
aviciBayCoAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmTime.setStatus("current")
_AviciBayCoAlarmUnitNum_Type = Integer32
_AviciBayCoAlarmUnitNum_Object = MibTableColumn
aviciBayCoAlarmUnitNum = _AviciBayCoAlarmUnitNum_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 5),
    _AviciBayCoAlarmUnitNum_Type()
)
aviciBayCoAlarmUnitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmUnitNum.setStatus("current")
_AviciBayCoAlarmUnitType_Type = AviciUnitType
_AviciBayCoAlarmUnitType_Object = MibTableColumn
aviciBayCoAlarmUnitType = _AviciBayCoAlarmUnitType_Object(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 1, 8, 1, 6),
    _AviciBayCoAlarmUnitType_Type()
)
aviciBayCoAlarmUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aviciBayCoAlarmUnitType.setStatus("current")
_AviciBayNotifications_ObjectIdentity = ObjectIdentity
aviciBayNotifications = _AviciBayNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2)
)
_AviciBayNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciBayNotificationPrefix = _AviciBayNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0)
)
_AviciBayControllerNotifications_ObjectIdentity = ObjectIdentity
aviciBayControllerNotifications = _AviciBayControllerNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 3)
)
_AviciBayControllerNotificationPrefix_ObjectIdentity = ObjectIdentity
aviciBayControllerNotificationPrefix = _AviciBayControllerNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 3, 0)
)
_AviciBayMIBConformance_ObjectIdentity = ObjectIdentity
aviciBayMIBConformance = _AviciBayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4)
)
_AviciBayMIBCompliances_ObjectIdentity = ObjectIdentity
aviciBayMIBCompliances = _AviciBayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 1)
)
_AviciBayMIBGroups_ObjectIdentity = ObjectIdentity
aviciBayMIBGroups = _AviciBayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 2)
)

# Managed Objects groups

aviciBayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 2, 1)
)
aviciBayGroup.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayCriticalLed"),
        ("AVICI-BAY-MIB", "aviciBayMajorLed"),
        ("AVICI-BAY-MIB", "aviciBayMinorLed"),
        ("AVICI-BAY-MIB", "aviciBayAlarmCutOff"),
        ("AVICI-BAY-MIB", "aviciBayModTempCriticalThreshold"),
        ("AVICI-BAY-MIB", "aviciBayModTempMajorThreshold"),
        ("AVICI-BAY-MIB", "aviciBayModTempMinorThreshold"),
        ("AVICI-BAY-MIB", "aviciBayTempCriticalThreshold"),
        ("AVICI-BAY-MIB", "aviciBayTempMajorThreshold"),
        ("AVICI-BAY-MIB", "aviciBayTempMinorThreshold"),
        ("AVICI-BAY-MIB", "aviciBayVoltageIndex"),
        ("AVICI-BAY-MIB", "aviciBayVoltageType"),
        ("AVICI-BAY-MIB", "aviciBayVoltage"),
        ("AVICI-BAY-MIB", "aviciBayVoltageStatus"),
        ("AVICI-BAY-MIB", "aviciBayVoltageDescr"),
        ("AVICI-BAY-MIB", "aviciBayFanIndex"),
        ("AVICI-BAY-MIB", "aviciBayFanAdminStatus"),
        ("AVICI-BAY-MIB", "aviciBayFanOperStatus"),
        ("AVICI-BAY-MIB", "aviciBayFanSpeed"),
        ("AVICI-BAY-MIB", "aviciBayFanCurrTemp"),
        ("AVICI-BAY-MIB", "aviciBayFanMaxTemp"),
        ("AVICI-BAY-MIB", "aviciBayFanLedStatus"),
        ("AVICI-BAY-MIB", "aviciBayFanCurrFailures"),
        ("AVICI-BAY-MIB", "aviciBayFanDescr"),
        ("AVICI-BAY-MIB", "aviciSlotIndex"),
        ("AVICI-BAY-MIB", "aviciBaySlotStatus"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxOctets"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxMessages"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxDiscards"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxProtoErrs"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxIOErrs"),
        ("AVICI-BAY-MIB", "aviciBaySlotRxTimeouts"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxOctets"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxMessages"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxDiscards"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxProtoErrs"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxIOErrs"),
        ("AVICI-BAY-MIB", "aviciBaySlotTxTimeouts"),
        ("AVICI-BAY-MIB", "aviciBayBreakerIndex"),
        ("AVICI-BAY-MIB", "aviciBayBreakerType"),
        ("AVICI-BAY-MIB", "aviciBayBreakerStatus"),
        ("AVICI-BAY-MIB", "aviciBayBreakerDescr"))
)
if mibBuilder.loadTexts:
    aviciBayGroup.setStatus("current")

aviciBayControllerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 2, 2)
)
aviciBayControllerGroup.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayControllerIndex"),
        ("AVICI-BAY-MIB", "aviciBayControllerOperStatus"),
        ("AVICI-BAY-MIB", "aviciBayControllerAdminStatus"),
        ("AVICI-BAY-MIB", "aviciBayControllerPartNumber"),
        ("AVICI-BAY-MIB", "aviciBayControllerSerialNumber"),
        ("AVICI-BAY-MIB", "aviciBayControllerRevision"),
        ("AVICI-BAY-MIB", "aviciBayControllerSoftwareVersion"),
        ("AVICI-BAY-MIB", "aviciBayControllerFirmwareVersion"),
        ("AVICI-BAY-MIB", "aviciBayControllerProductId"),
        ("AVICI-BAY-MIB", "aviciBayControllerProductSerialNumber"),
        ("AVICI-BAY-MIB", "aviciBayControllerProductRevision"),
        ("AVICI-BAY-MIB", "aviciBayControllerDescr"))
)
if mibBuilder.loadTexts:
    aviciBayControllerGroup.setStatus("current")

aviciBayCentralOfficeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 2, 3)
)
aviciBayCentralOfficeGroup.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayCoActiveAlarmCount"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmLastChange"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmIndex"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmType"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmDescr"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmTime"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmUnitNum"),
        ("AVICI-BAY-MIB", "aviciBayCoAlarmUnitType"))
)
if mibBuilder.loadTexts:
    aviciBayCentralOfficeGroup.setStatus("current")


# Notification objects

aviciBayVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0, 1)
)
aviciBayVoltageNotification.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayVoltageIndex"),
        ("AVICI-BAY-MIB", "aviciBayVoltage"),
        ("AVICI-BAY-MIB", "aviciBayVoltageStatus"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayVoltageNotification.setStatus(
        "current"
    )

aviciBayFanNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0, 2)
)
aviciBayFanNotification.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayFanIndex"),
        ("AVICI-BAY-MIB", "aviciBayFanCurrFailures"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayFanNotification.setStatus(
        "current"
    )

aviciBayBreakerNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0, 3)
)
aviciBayBreakerNotification.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayBreakerIndex"),
        ("AVICI-BAY-MIB", "aviciBayBreakerType"),
        ("AVICI-BAY-MIB", "aviciBayBreakerStatus"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayBreakerNotification.setStatus(
        "current"
    )

aviciBayMultiFanFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0, 4)
)
aviciBayMultiFanFailures.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayMultiFanFailures.setStatus(
        "current"
    )

aviciBayMultiBayControllerFailures = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 2, 0, 5)
)
aviciBayMultiBayControllerFailures.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayMultiBayControllerFailures.setStatus(
        "current"
    )

aviciBayControllerColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 3, 0, 1)
)
aviciBayControllerColdStart.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayControllerIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayControllerColdStart.setStatus(
        "current"
    )

aviciBayControllerWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 3, 0, 2)
)
aviciBayControllerWarmStart.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayControllerIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayControllerWarmStart.setStatus(
        "current"
    )

aviciBayControllerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 3, 0, 3)
)
aviciBayControllerDown.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayIndex"),
        ("AVICI-BAY-MIB", "aviciBayControllerIndex"),
        ("AVICI-SYSTEM-MIB", "aviciSysTrapDescr"))
)
if mibBuilder.loadTexts:
    aviciBayControllerDown.setStatus(
        "current"
    )


# Notifications groups

aviciBayNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 2, 4)
)
aviciBayNotificationGroup.setObjects(
      *(("AVICI-BAY-MIB", "aviciBayControllerColdStart"),
        ("AVICI-BAY-MIB", "aviciBayControllerWarmStart"),
        ("AVICI-BAY-MIB", "aviciBayControllerDown"),
        ("AVICI-BAY-MIB", "aviciBayVoltageNotification"),
        ("AVICI-BAY-MIB", "aviciBayFanNotification"),
        ("AVICI-BAY-MIB", "aviciBayBreakerNotification"),
        ("AVICI-BAY-MIB", "aviciBayMultiFanFailures"),
        ("AVICI-BAY-MIB", "aviciBayMultiBayControllerFailures"))
)
if mibBuilder.loadTexts:
    aviciBayNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

aviciBayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2474, 1, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    aviciBayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVICI-BAY-MIB",
    **{"aviciBayMIB": aviciBayMIB,
       "aviciBayObjects": aviciBayObjects,
       "aviciBayTable": aviciBayTable,
       "aviciBayEntry": aviciBayEntry,
       "aviciBayIndex": aviciBayIndex,
       "aviciBayCriticalLed": aviciBayCriticalLed,
       "aviciBayMajorLed": aviciBayMajorLed,
       "aviciBayMinorLed": aviciBayMinorLed,
       "aviciBayAlarmCutOff": aviciBayAlarmCutOff,
       "aviciBayModTempCriticalThreshold": aviciBayModTempCriticalThreshold,
       "aviciBayModTempMajorThreshold": aviciBayModTempMajorThreshold,
       "aviciBayModTempMinorThreshold": aviciBayModTempMinorThreshold,
       "aviciBayTempCriticalThreshold": aviciBayTempCriticalThreshold,
       "aviciBayTempMajorThreshold": aviciBayTempMajorThreshold,
       "aviciBayTempMinorThreshold": aviciBayTempMinorThreshold,
       "aviciBayControllerTable": aviciBayControllerTable,
       "aviciBayControllerEntry": aviciBayControllerEntry,
       "aviciBayControllerIndex": aviciBayControllerIndex,
       "aviciBayControllerOperStatus": aviciBayControllerOperStatus,
       "aviciBayControllerAdminStatus": aviciBayControllerAdminStatus,
       "aviciBayControllerPartNumber": aviciBayControllerPartNumber,
       "aviciBayControllerSerialNumber": aviciBayControllerSerialNumber,
       "aviciBayControllerRevision": aviciBayControllerRevision,
       "aviciBayControllerSoftwareVersion": aviciBayControllerSoftwareVersion,
       "aviciBayControllerFirmwareVersion": aviciBayControllerFirmwareVersion,
       "aviciBayControllerProductId": aviciBayControllerProductId,
       "aviciBayControllerProductSerialNumber": aviciBayControllerProductSerialNumber,
       "aviciBayControllerProductRevision": aviciBayControllerProductRevision,
       "aviciBayControllerDescr": aviciBayControllerDescr,
       "aviciBayVoltageTable": aviciBayVoltageTable,
       "aviciBayVoltageEntry": aviciBayVoltageEntry,
       "aviciBayVoltageIndex": aviciBayVoltageIndex,
       "aviciBayVoltageType": aviciBayVoltageType,
       "aviciBayVoltage": aviciBayVoltage,
       "aviciBayVoltageStatus": aviciBayVoltageStatus,
       "aviciBayVoltageDescr": aviciBayVoltageDescr,
       "aviciBayFanTable": aviciBayFanTable,
       "aviciBayFanEntry": aviciBayFanEntry,
       "aviciBayFanIndex": aviciBayFanIndex,
       "aviciBayFanAdminStatus": aviciBayFanAdminStatus,
       "aviciBayFanOperStatus": aviciBayFanOperStatus,
       "aviciBayFanSpeed": aviciBayFanSpeed,
       "aviciBayFanCurrTemp": aviciBayFanCurrTemp,
       "aviciBayFanMaxTemp": aviciBayFanMaxTemp,
       "aviciBayFanLedStatus": aviciBayFanLedStatus,
       "aviciBayFanCurrFailures": aviciBayFanCurrFailures,
       "aviciBayFanDescr": aviciBayFanDescr,
       "aviciBaySlotTable": aviciBaySlotTable,
       "aviciBaySlotEntry": aviciBaySlotEntry,
       "aviciSlotIndex": aviciSlotIndex,
       "aviciBaySlotStatus": aviciBaySlotStatus,
       "aviciBaySlotRxOctets": aviciBaySlotRxOctets,
       "aviciBaySlotRxMessages": aviciBaySlotRxMessages,
       "aviciBaySlotRxDiscards": aviciBaySlotRxDiscards,
       "aviciBaySlotRxProtoErrs": aviciBaySlotRxProtoErrs,
       "aviciBaySlotRxIOErrs": aviciBaySlotRxIOErrs,
       "aviciBaySlotRxTimeouts": aviciBaySlotRxTimeouts,
       "aviciBaySlotTxOctets": aviciBaySlotTxOctets,
       "aviciBaySlotTxMessages": aviciBaySlotTxMessages,
       "aviciBaySlotTxDiscards": aviciBaySlotTxDiscards,
       "aviciBaySlotTxProtoErrs": aviciBaySlotTxProtoErrs,
       "aviciBaySlotTxIOErrs": aviciBaySlotTxIOErrs,
       "aviciBaySlotTxTimeouts": aviciBaySlotTxTimeouts,
       "aviciBayBreakerTable": aviciBayBreakerTable,
       "aviciBayBreakerEntry": aviciBayBreakerEntry,
       "aviciBayBreakerIndex": aviciBayBreakerIndex,
       "aviciBayBreakerType": aviciBayBreakerType,
       "aviciBayBreakerStatus": aviciBayBreakerStatus,
       "aviciBayBreakerDescr": aviciBayBreakerDescr,
       "aviciBayCoAlarmSystem": aviciBayCoAlarmSystem,
       "aviciBayCoActiveAlarmCount": aviciBayCoActiveAlarmCount,
       "aviciBayCoAlarmLastChange": aviciBayCoAlarmLastChange,
       "aviciBayCoAlarmTable": aviciBayCoAlarmTable,
       "aviciBayCoAlarmEntry": aviciBayCoAlarmEntry,
       "aviciBayCoAlarmIndex": aviciBayCoAlarmIndex,
       "aviciBayCoAlarmType": aviciBayCoAlarmType,
       "aviciBayCoAlarmDescr": aviciBayCoAlarmDescr,
       "aviciBayCoAlarmTime": aviciBayCoAlarmTime,
       "aviciBayCoAlarmUnitNum": aviciBayCoAlarmUnitNum,
       "aviciBayCoAlarmUnitType": aviciBayCoAlarmUnitType,
       "aviciBayNotifications": aviciBayNotifications,
       "aviciBayNotificationPrefix": aviciBayNotificationPrefix,
       "aviciBayVoltageNotification": aviciBayVoltageNotification,
       "aviciBayFanNotification": aviciBayFanNotification,
       "aviciBayBreakerNotification": aviciBayBreakerNotification,
       "aviciBayMultiFanFailures": aviciBayMultiFanFailures,
       "aviciBayMultiBayControllerFailures": aviciBayMultiBayControllerFailures,
       "aviciBayControllerNotifications": aviciBayControllerNotifications,
       "aviciBayControllerNotificationPrefix": aviciBayControllerNotificationPrefix,
       "aviciBayControllerColdStart": aviciBayControllerColdStart,
       "aviciBayControllerWarmStart": aviciBayControllerWarmStart,
       "aviciBayControllerDown": aviciBayControllerDown,
       "aviciBayMIBConformance": aviciBayMIBConformance,
       "aviciBayMIBCompliances": aviciBayMIBCompliances,
       "aviciBayMIBCompliance": aviciBayMIBCompliance,
       "aviciBayMIBGroups": aviciBayMIBGroups,
       "aviciBayGroup": aviciBayGroup,
       "aviciBayControllerGroup": aviciBayControllerGroup,
       "aviciBayCentralOfficeGroup": aviciBayCentralOfficeGroup,
       "aviciBayNotificationGroup": aviciBayNotificationGroup}
)
