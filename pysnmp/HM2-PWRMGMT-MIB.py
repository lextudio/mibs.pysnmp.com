# SNMP MIB module (HM2-PWRMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PWRMGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:53 2024
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

(hm2ConfigurationMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2ConfigurationMibs")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

hm2PowerMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 11)
)
hm2PowerMgmtMib.setRevisions(
        ("2011-03-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2PowerMgmtMibNotifications_ObjectIdentity = ObjectIdentity
hm2PowerMgmtMibNotifications = _Hm2PowerMgmtMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 0)
)
_Hm2PowerMgmtMibObjects_ObjectIdentity = ObjectIdentity
hm2PowerMgmtMibObjects = _Hm2PowerMgmtMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1)
)
_Hm2PowerSupplyGroup_ObjectIdentity = ObjectIdentity
hm2PowerSupplyGroup = _Hm2PowerSupplyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1)
)
_Hm2PSTable_Object = MibTable
hm2PSTable = _Hm2PSTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2PSTable.setStatus("current")
_Hm2PSEntry_Object = MibTableRow
hm2PSEntry = _Hm2PSEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1)
)
hm2PSEntry.setIndexNames(
    (0, "HM2-PWRMGMT-MIB", "hm2PSID"),
)
if mibBuilder.loadTexts:
    hm2PSEntry.setStatus("current")


class _Hm2PSID_Type(Integer32):
    """Custom type hm2PSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Hm2PSID_Type.__name__ = "Integer32"
_Hm2PSID_Object = MibTableColumn
hm2PSID = _Hm2PSID_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 1),
    _Hm2PSID_Type()
)
hm2PSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSID.setStatus("current")


class _Hm2PSState_Type(Integer32):
    """Custom type hm2PSState based on Integer32"""
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
        *(("defective", 2),
          ("notInstalled", 3),
          ("present", 1),
          ("unknown", 4))
    )


_Hm2PSState_Type.__name__ = "Integer32"
_Hm2PSState_Object = MibTableColumn
hm2PSState = _Hm2PSState_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 1, 1, 2),
    _Hm2PSState_Type()
)
hm2PSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSState.setStatus("current")
_Hm2PSUSlotInfoTable_Object = MibTable
hm2PSUSlotInfoTable = _Hm2PSUSlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hm2PSUSlotInfoTable.setStatus("current")
_Hm2PSUSlotInfoEntry_Object = MibTableRow
hm2PSUSlotInfoEntry = _Hm2PSUSlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1)
)
hm2PSUSlotInfoEntry.setIndexNames(
    (0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"),
)
if mibBuilder.loadTexts:
    hm2PSUSlotInfoEntry.setStatus("current")


class _Hm2PSUSlotIndex_Type(Integer32):
    """Custom type hm2PSUSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_Hm2PSUSlotIndex_Type.__name__ = "Integer32"
_Hm2PSUSlotIndex_Object = MibTableColumn
hm2PSUSlotIndex = _Hm2PSUSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 1),
    _Hm2PSUSlotIndex_Type()
)
hm2PSUSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PSUSlotIndex.setStatus("current")


class _Hm2PSUSlotChassisTypeId_Type(Integer32):
    """Custom type hm2PSUSlotChassisTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("grs", 4),
          ("mach1020", 1),
          ("mach4000", 2),
          ("other", 0),
          ("railswitch", 3))
    )


_Hm2PSUSlotChassisTypeId_Type.__name__ = "Integer32"
_Hm2PSUSlotChassisTypeId_Object = MibTableColumn
hm2PSUSlotChassisTypeId = _Hm2PSUSlotChassisTypeId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 2),
    _Hm2PSUSlotChassisTypeId_Type()
)
hm2PSUSlotChassisTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotChassisTypeId.setStatus("current")


class _Hm2PSUSlotManufacturerId_Type(Integer32):
    """Custom type hm2PSUSlotManufacturerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hirschmann", 1),
          ("other", 0))
    )


_Hm2PSUSlotManufacturerId_Type.__name__ = "Integer32"
_Hm2PSUSlotManufacturerId_Object = MibTableColumn
hm2PSUSlotManufacturerId = _Hm2PSUSlotManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 3),
    _Hm2PSUSlotManufacturerId_Type()
)
hm2PSUSlotManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotManufacturerId.setStatus("current")
_Hm2PSUSlotManufacturerDate_Type = SnmpAdminString
_Hm2PSUSlotManufacturerDate_Object = MibTableColumn
hm2PSUSlotManufacturerDate = _Hm2PSUSlotManufacturerDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 4),
    _Hm2PSUSlotManufacturerDate_Type()
)
hm2PSUSlotManufacturerDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotManufacturerDate.setStatus("obsolete")
_Hm2PSUSlotSerialNumber_Type = SnmpAdminString
_Hm2PSUSlotSerialNumber_Object = MibTableColumn
hm2PSUSlotSerialNumber = _Hm2PSUSlotSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 5),
    _Hm2PSUSlotSerialNumber_Type()
)
hm2PSUSlotSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotSerialNumber.setStatus("current")
_Hm2PSUSlotProductCode_Type = SnmpAdminString
_Hm2PSUSlotProductCode_Object = MibTableColumn
hm2PSUSlotProductCode = _Hm2PSUSlotProductCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 6),
    _Hm2PSUSlotProductCode_Type()
)
hm2PSUSlotProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotProductCode.setStatus("current")
_Hm2PSUSlotDescription_Type = SnmpAdminString
_Hm2PSUSlotDescription_Object = MibTableColumn
hm2PSUSlotDescription = _Hm2PSUSlotDescription_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 7),
    _Hm2PSUSlotDescription_Type()
)
hm2PSUSlotDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotDescription.setStatus("current")


class _Hm2PSUSlotCombinationType_Type(Integer32):
    """Custom type hm2PSUSlotCombinationType based on Integer32"""
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
        *(("only-on-psu1", 0),
          ("psu1-poe-psu2-sys", 2),
          ("psu1-sys-psu2-poe", 1),
          ("two-separate-psus", 3))
    )


_Hm2PSUSlotCombinationType_Type.__name__ = "Integer32"
_Hm2PSUSlotCombinationType_Object = MibTableColumn
hm2PSUSlotCombinationType = _Hm2PSUSlotCombinationType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 8),
    _Hm2PSUSlotCombinationType_Type()
)
hm2PSUSlotCombinationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotCombinationType.setStatus("current")


class _Hm2PSUSlotTemperatureRange_Type(Integer32):
    """Custom type hm2PSUSlotTemperatureRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("tr-0-60", 0),
          ("tr-minus40-60", 1),
          ("tr-minus40-70", 2),
          ("tr-minus40-70cc", 3),
          ("tr-minus40-85", 4),
          ("tr-minus40-85cc", 5))
    )


_Hm2PSUSlotTemperatureRange_Type.__name__ = "Integer32"
_Hm2PSUSlotTemperatureRange_Object = MibTableColumn
hm2PSUSlotTemperatureRange = _Hm2PSUSlotTemperatureRange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 9),
    _Hm2PSUSlotTemperatureRange_Type()
)
hm2PSUSlotTemperatureRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotTemperatureRange.setStatus("current")


class _Hm2PSUSlotRevisionId_Type(Integer32):
    """Custom type hm2PSUSlotRevisionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hm2PSUSlotRevisionId_Type.__name__ = "Integer32"
_Hm2PSUSlotRevisionId_Object = MibTableColumn
hm2PSUSlotRevisionId = _Hm2PSUSlotRevisionId_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 10, 1, 10),
    _Hm2PSUSlotRevisionId_Type()
)
hm2PSUSlotRevisionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUSlotRevisionId.setStatus("current")
_Hm2PSUUnitInfoTable_Object = MibTable
hm2PSUUnitInfoTable = _Hm2PSUUnitInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hm2PSUUnitInfoTable.setStatus("current")
_Hm2PSUUnitInfoEntry_Object = MibTableRow
hm2PSUUnitInfoEntry = _Hm2PSUUnitInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1)
)
hm2PSUUnitInfoEntry.setIndexNames(
    (0, "HM2-PWRMGMT-MIB", "hm2PSUSlotIndex"),
    (0, "HM2-PWRMGMT-MIB", "hm2PSUUnitIndex"),
)
if mibBuilder.loadTexts:
    hm2PSUUnitInfoEntry.setStatus("current")


class _Hm2PSUUnitIndex_Type(Integer32):
    """Custom type hm2PSUUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Hm2PSUUnitIndex_Type.__name__ = "Integer32"
_Hm2PSUUnitIndex_Object = MibTableColumn
hm2PSUUnitIndex = _Hm2PSUUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 1),
    _Hm2PSUUnitIndex_Type()
)
hm2PSUUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2PSUUnitIndex.setStatus("current")


class _Hm2PSUUnitConverterType_Type(Integer32):
    """Custom type hm2PSUUnitConverterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_Hm2PSUUnitConverterType_Type.__name__ = "Integer32"
_Hm2PSUUnitConverterType_Object = MibTableColumn
hm2PSUUnitConverterType = _Hm2PSUUnitConverterType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 2),
    _Hm2PSUUnitConverterType_Type()
)
hm2PSUUnitConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitConverterType.setStatus("current")


class _Hm2PSUUnitNumberOfInputs_Type(Integer32):
    """Custom type hm2PSUUnitNumberOfInputs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hm2PSUUnitNumberOfInputs_Type.__name__ = "Integer32"
_Hm2PSUUnitNumberOfInputs_Object = MibTableColumn
hm2PSUUnitNumberOfInputs = _Hm2PSUUnitNumberOfInputs_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 3),
    _Hm2PSUUnitNumberOfInputs_Type()
)
hm2PSUUnitNumberOfInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitNumberOfInputs.setStatus("current")


class _Hm2PSUUnitOutputType_Type(Integer32):
    """Custom type hm2PSUUnitOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("poe", 3),
          ("system", 1))
    )


_Hm2PSUUnitOutputType_Type.__name__ = "Integer32"
_Hm2PSUUnitOutputType_Object = MibTableColumn
hm2PSUUnitOutputType = _Hm2PSUUnitOutputType_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 4),
    _Hm2PSUUnitOutputType_Type()
)
hm2PSUUnitOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitOutputType.setStatus("current")


class _Hm2PSUUnitSystemBudget_Type(Integer32):
    """Custom type hm2PSUUnitSystemBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Hm2PSUUnitSystemBudget_Type.__name__ = "Integer32"
_Hm2PSUUnitSystemBudget_Object = MibTableColumn
hm2PSUUnitSystemBudget = _Hm2PSUUnitSystemBudget_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 5),
    _Hm2PSUUnitSystemBudget_Type()
)
hm2PSUUnitSystemBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitSystemBudget.setStatus("current")


class _Hm2PSUUnitPoeBudget_Type(Integer32):
    """Custom type hm2PSUUnitPoeBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Hm2PSUUnitPoeBudget_Type.__name__ = "Integer32"
_Hm2PSUUnitPoeBudget_Object = MibTableColumn
hm2PSUUnitPoeBudget = _Hm2PSUUnitPoeBudget_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 6),
    _Hm2PSUUnitPoeBudget_Type()
)
hm2PSUUnitPoeBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitPoeBudget.setStatus("current")


class _Hm2PSUUnitFanCount_Type(Integer32):
    """Custom type hm2PSUUnitFanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_Hm2PSUUnitFanCount_Type.__name__ = "Integer32"
_Hm2PSUUnitFanCount_Object = MibTableColumn
hm2PSUUnitFanCount = _Hm2PSUUnitFanCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 7),
    _Hm2PSUUnitFanCount_Type()
)
hm2PSUUnitFanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitFanCount.setStatus("current")


class _Hm2PSUUnitVoltageRange_Type(Integer32):
    """Custom type hm2PSUUnitVoltageRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vr-18-60vdc", 0),
          ("vr-24-48vdc", 2),
          ("vr-24-60vdc", 1),
          ("vr-48-54vdc-poe", 4),
          ("vr-60-250vdc-110-240vac", 3))
    )


_Hm2PSUUnitVoltageRange_Type.__name__ = "Integer32"
_Hm2PSUUnitVoltageRange_Object = MibTableColumn
hm2PSUUnitVoltageRange = _Hm2PSUUnitVoltageRange_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 8),
    _Hm2PSUUnitVoltageRange_Type()
)
hm2PSUUnitVoltageRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitVoltageRange.setStatus("current")


class _Hm2PSUUnitPowerInterruption_Type(Integer32):
    """Custom type hm2PSUUnitPowerInterruption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_Hm2PSUUnitPowerInterruption_Type.__name__ = "Integer32"
_Hm2PSUUnitPowerInterruption_Object = MibTableColumn
hm2PSUUnitPowerInterruption = _Hm2PSUUnitPowerInterruption_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 1, 1, 20, 1, 9),
    _Hm2PSUUnitPowerInterruption_Type()
)
hm2PSUUnitPowerInterruption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2PSUUnitPowerInterruption.setStatus("current")

# Managed Objects groups


# Notification objects

hm2PowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 11, 11, 0, 1)
)
hm2PowerSupplyTrap.setObjects(
      *(("HM2-PWRMGMT-MIB", "hm2PSID"),
        ("HM2-PWRMGMT-MIB", "hm2PSState"))
)
if mibBuilder.loadTexts:
    hm2PowerSupplyTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PWRMGMT-MIB",
    **{"hm2PowerMgmtMib": hm2PowerMgmtMib,
       "hm2PowerMgmtMibNotifications": hm2PowerMgmtMibNotifications,
       "hm2PowerSupplyTrap": hm2PowerSupplyTrap,
       "hm2PowerMgmtMibObjects": hm2PowerMgmtMibObjects,
       "hm2PowerSupplyGroup": hm2PowerSupplyGroup,
       "hm2PSTable": hm2PSTable,
       "hm2PSEntry": hm2PSEntry,
       "hm2PSID": hm2PSID,
       "hm2PSState": hm2PSState,
       "hm2PSUSlotInfoTable": hm2PSUSlotInfoTable,
       "hm2PSUSlotInfoEntry": hm2PSUSlotInfoEntry,
       "hm2PSUSlotIndex": hm2PSUSlotIndex,
       "hm2PSUSlotChassisTypeId": hm2PSUSlotChassisTypeId,
       "hm2PSUSlotManufacturerId": hm2PSUSlotManufacturerId,
       "hm2PSUSlotManufacturerDate": hm2PSUSlotManufacturerDate,
       "hm2PSUSlotSerialNumber": hm2PSUSlotSerialNumber,
       "hm2PSUSlotProductCode": hm2PSUSlotProductCode,
       "hm2PSUSlotDescription": hm2PSUSlotDescription,
       "hm2PSUSlotCombinationType": hm2PSUSlotCombinationType,
       "hm2PSUSlotTemperatureRange": hm2PSUSlotTemperatureRange,
       "hm2PSUSlotRevisionId": hm2PSUSlotRevisionId,
       "hm2PSUUnitInfoTable": hm2PSUUnitInfoTable,
       "hm2PSUUnitInfoEntry": hm2PSUUnitInfoEntry,
       "hm2PSUUnitIndex": hm2PSUUnitIndex,
       "hm2PSUUnitConverterType": hm2PSUUnitConverterType,
       "hm2PSUUnitNumberOfInputs": hm2PSUUnitNumberOfInputs,
       "hm2PSUUnitOutputType": hm2PSUUnitOutputType,
       "hm2PSUUnitSystemBudget": hm2PSUUnitSystemBudget,
       "hm2PSUUnitPoeBudget": hm2PSUUnitPoeBudget,
       "hm2PSUUnitFanCount": hm2PSUUnitFanCount,
       "hm2PSUUnitVoltageRange": hm2PSUUnitVoltageRange,
       "hm2PSUUnitPowerInterruption": hm2PSUUnitPowerInterruption}
)
