# SNMP MIB module (DMTF-MOBILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DMTF-MOBILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:31:42 2024
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

(DmiDate,
 DmiString,
 dmiCompId,
 dmiEventAssociatedGroup,
 dmiEventDateTime,
 dmiEventSeverity,
 dmiEventStateKey,
 dmiEventSubSystem,
 dmiEventSystem) = mibBuilder.importSymbols(
    "DMTF-DMI-MIB",
    "DmiDate",
    "DmiString",
    "dmiCompId",
    "dmiEventAssociatedGroup",
    "dmiEventDateTime",
    "dmiEventSeverity",
    "dmiEventStateKey",
    "dmiEventSubSystem",
    "dmiEventSystem")

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

dmtfMobileComputerMIF = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 8)
)


# Types definitions



class DmiCounter(Counter32):
    """Custom type DmiCounter based on Counter32"""




class DmiCounter64(Counter64):
    """Custom type DmiCounter64 based on Counter64"""




class DmiGauge(Gauge32):
    """Custom type DmiGauge based on Gauge32"""




class DmiInteger(Integer32):
    """Custom type DmiInteger based on Integer32"""




class DmiOctetstring(OctetString):
    """Custom type DmiOctetstring based on OctetString"""




class DmiCompId(Integer32):
    """Custom type DmiCompId based on Integer32"""




class DmiGroupId(Integer32):
    """Custom type DmiGroupId based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dmtf_ObjectIdentity = ObjectIdentity
dmtf = _Dmtf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412)
)
_DmtfStdMifs_ObjectIdentity = ObjectIdentity
dmtfStdMifs = _DmtfStdMifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2)
)
_DmtfPortableBatteryTable_Object = MibTable
dmtfPortableBatteryTable = _DmtfPortableBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1)
)
if mibBuilder.loadTexts:
    dmtfPortableBatteryTable.setStatus("current")
_DmtfPortableBatteryTraps_ObjectIdentity = ObjectIdentity
dmtfPortableBatteryTraps = _DmtfPortableBatteryTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 0)
)
_DmtfPortableBatteryEntry_Object = MibTableRow
dmtfPortableBatteryEntry = _DmtfPortableBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1)
)
dmtfPortableBatteryEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "portableBatteryIndex"),
)
if mibBuilder.loadTexts:
    dmtfPortableBatteryEntry.setStatus("current")


class _DmtfPortableBatteryState_Type(Integer32):
    """Custom type dmtfPortableBatteryState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfPortableBatteryState_Type.__name__ = "Integer32"
_DmtfPortableBatteryState_Object = MibTableColumn
dmtfPortableBatteryState = _DmtfPortableBatteryState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 0),
    _DmtfPortableBatteryState_Type()
)
dmtfPortableBatteryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfPortableBatteryState.setStatus("current")
_PortableBatteryIndex_Type = DmiInteger
_PortableBatteryIndex_Object = MibTableColumn
portableBatteryIndex = _PortableBatteryIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 1),
    _PortableBatteryIndex_Type()
)
portableBatteryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryIndex.setStatus("current")
_PortableBatteryLocation_Type = DmiString
_PortableBatteryLocation_Object = MibTableColumn
portableBatteryLocation = _PortableBatteryLocation_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 2),
    _PortableBatteryLocation_Type()
)
portableBatteryLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryLocation.setStatus("current")
_PortableBatteryManufacturer_Type = DmiString
_PortableBatteryManufacturer_Object = MibTableColumn
portableBatteryManufacturer = _PortableBatteryManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 3),
    _PortableBatteryManufacturer_Type()
)
portableBatteryManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryManufacturer.setStatus("current")
_PortableBatteryManufactureDate_Type = DmiDate
_PortableBatteryManufactureDate_Object = MibTableColumn
portableBatteryManufactureDate = _PortableBatteryManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 4),
    _PortableBatteryManufactureDate_Type()
)
portableBatteryManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryManufactureDate.setStatus("current")
_PortableBatterySerialNumber_Type = DmiString
_PortableBatterySerialNumber_Object = MibTableColumn
portableBatterySerialNumber = _PortableBatterySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 5),
    _PortableBatterySerialNumber_Type()
)
portableBatterySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatterySerialNumber.setStatus("current")
_PortableBatteryDeviceName_Type = DmiString
_PortableBatteryDeviceName_Object = MibTableColumn
portableBatteryDeviceName = _PortableBatteryDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 6),
    _PortableBatteryDeviceName_Type()
)
portableBatteryDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryDeviceName.setStatus("current")


class _PortableBatteryDeviceChemistry_Type(Integer32):
    """Custom type portableBatteryDeviceChemistry based on Integer32"""
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
        *(("leadAcid", 3),
          ("lithiumIon", 6),
          ("lithiumPolymer", 8),
          ("nickelCadmium", 4),
          ("nickelMetalHydride", 5),
          ("other", 1),
          ("unknown", 2),
          ("zincAir", 7))
    )


_PortableBatteryDeviceChemistry_Type.__name__ = "Integer32"
_PortableBatteryDeviceChemistry_Object = MibTableColumn
portableBatteryDeviceChemistry = _PortableBatteryDeviceChemistry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 7),
    _PortableBatteryDeviceChemistry_Type()
)
portableBatteryDeviceChemistry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryDeviceChemistry.setStatus("current")
_PortableBatteryDesignCapacity_Type = DmiInteger
_PortableBatteryDesignCapacity_Object = MibTableColumn
portableBatteryDesignCapacity = _PortableBatteryDesignCapacity_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 8),
    _PortableBatteryDesignCapacity_Type()
)
portableBatteryDesignCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryDesignCapacity.setStatus("current")
_PortableBatteryDesignVoltage_Type = DmiInteger
_PortableBatteryDesignVoltage_Object = MibTableColumn
portableBatteryDesignVoltage = _PortableBatteryDesignVoltage_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 9),
    _PortableBatteryDesignVoltage_Type()
)
portableBatteryDesignVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryDesignVoltage.setStatus("current")
_SmartBatteryVersion_Type = DmiString
_SmartBatteryVersion_Object = MibTableColumn
smartBatteryVersion = _SmartBatteryVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 10),
    _SmartBatteryVersion_Type()
)
smartBatteryVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartBatteryVersion.setStatus("current")
_FullChargeCapacity_Type = DmiInteger
_FullChargeCapacity_Object = MibTableColumn
fullChargeCapacity = _FullChargeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 11),
    _FullChargeCapacity_Type()
)
fullChargeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fullChargeCapacity.setStatus("current")
_RemainingCapacity_Type = DmiInteger
_RemainingCapacity_Object = MibTableColumn
remainingCapacity = _RemainingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 12),
    _RemainingCapacity_Type()
)
remainingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remainingCapacity.setStatus("current")
_MaximumError_Type = DmiInteger
_MaximumError_Object = MibTableColumn
maximumError = _MaximumError_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 13),
    _MaximumError_Type()
)
maximumError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumError.setStatus("current")


class _PortableBatteryChargingStatus_Type(Integer32):
    """Custom type portableBatteryChargingStatus based on Integer32"""
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
        *(("charging", 6),
          ("chargingAndCritical", 9),
          ("chargingAndHigh", 7),
          ("chargingAndLow", 8),
          ("critical", 5),
          ("high", 3),
          ("low", 4),
          ("noSystemBattery", 10),
          ("other", 1),
          ("unknown", 2))
    )


_PortableBatteryChargingStatus_Type.__name__ = "Integer32"
_PortableBatteryChargingStatus_Object = MibTableColumn
portableBatteryChargingStatus = _PortableBatteryChargingStatus_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 14),
    _PortableBatteryChargingStatus_Type()
)
portableBatteryChargingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portableBatteryChargingStatus.setStatus("current")
_RemainingBatteryTime_Type = DmiInteger
_RemainingBatteryTime_Object = MibTableColumn
remainingBatteryTime = _RemainingBatteryTime_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 15),
    _RemainingBatteryTime_Type()
)
remainingBatteryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remainingBatteryTime.setStatus("current")
_RemainingTimeToFullBattery_Type = DmiInteger
_RemainingTimeToFullBattery_Object = MibTableColumn
remainingTimeToFullBattery = _RemainingTimeToFullBattery_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 16),
    _RemainingTimeToFullBattery_Type()
)
remainingTimeToFullBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remainingTimeToFullBattery.setStatus("current")
_PowerUnitIndex_Type = DmiInteger
_PowerUnitIndex_Object = MibTableColumn
powerUnitIndex = _PowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 1, 17),
    _PowerUnitIndex_Type()
)
powerUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUnitIndex.setStatus("current")


class _DmtfPortableBatteryEvSys_Type(Integer32):
    """Custom type dmtfPortableBatteryEvSys based on Integer32"""
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
        *(("other", 1),
          ("system1", 3),
          ("system2", 4),
          ("unknown", 2))
    )


_DmtfPortableBatteryEvSys_Type.__name__ = "Integer32"
_DmtfPortableBatteryEvSys_Object = MibScalar
dmtfPortableBatteryEvSys = _DmtfPortableBatteryEvSys_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 6),
    _DmtfPortableBatteryEvSys_Type()
)
dmtfPortableBatteryEvSys.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmtfPortableBatteryEvSys.setStatus("current")


class _DmtfPortableBatteryEvSub_Type(Integer32):
    """Custom type dmtfPortableBatteryEvSub based on Integer32"""
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
        *(("other", 1),
          ("subsystem1", 3),
          ("subsystem2", 4),
          ("unknown", 2))
    )


_DmtfPortableBatteryEvSub_Type.__name__ = "Integer32"
_DmtfPortableBatteryEvSub_Object = MibScalar
dmtfPortableBatteryEvSub = _DmtfPortableBatteryEvSub_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 7),
    _DmtfPortableBatteryEvSub_Type()
)
dmtfPortableBatteryEvSub.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dmtfPortableBatteryEvSub.setStatus("current")
_DmtfDynamicStatesTable_Object = MibTable
dmtfDynamicStatesTable = _DmtfDynamicStatesTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dmtfDynamicStatesTable.setStatus("current")
_DmtfDynamicStatesEntry_Object = MibTableRow
dmtfDynamicStatesEntry = _DmtfDynamicStatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 2, 1)
)
dmtfDynamicStatesEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfDynamicStatesEntry.setStatus("current")


class _ACLineStatus_Type(Integer32):
    """Custom type aCLineStatus based on Integer32"""
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
        *(("offLine", 3),
          ("onBackupPower", 5),
          ("onLine", 4),
          ("other", 1),
          ("unknown", 2))
    )


_ACLineStatus_Type.__name__ = "Integer32"
_ACLineStatus_Object = MibTableColumn
aCLineStatus = _ACLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 2, 1, 1),
    _ACLineStatus_Type()
)
aCLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aCLineStatus.setStatus("current")


class _DockingStatus_Type(Integer32):
    """Custom type dockingStatus based on Integer32"""
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
        *(("docked", 3),
          ("notDocked", 4),
          ("other", 1),
          ("unknown", 2))
    )


_DockingStatus_Type.__name__ = "Integer32"
_DockingStatus_Object = MibTableColumn
dockingStatus = _DockingStatus_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 2, 1, 2),
    _DockingStatus_Type()
)
dockingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dockingStatus.setStatus("current")
_DmtfVideoOutputDeviceTable_Object = MibTable
dmtfVideoOutputDeviceTable = _DmtfVideoOutputDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3)
)
if mibBuilder.loadTexts:
    dmtfVideoOutputDeviceTable.setStatus("current")
_DmtfVideoOutputDeviceEntry_Object = MibTableRow
dmtfVideoOutputDeviceEntry = _DmtfVideoOutputDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1)
)
dmtfVideoOutputDeviceEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "index"),
)
if mibBuilder.loadTexts:
    dmtfVideoOutputDeviceEntry.setStatus("current")


class _DmtfVideoOutputDeviceState_Type(Integer32):
    """Custom type dmtfVideoOutputDeviceState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfVideoOutputDeviceState_Type.__name__ = "Integer32"
_DmtfVideoOutputDeviceState_Object = MibTableColumn
dmtfVideoOutputDeviceState = _DmtfVideoOutputDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 0),
    _DmtfVideoOutputDeviceState_Type()
)
dmtfVideoOutputDeviceState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfVideoOutputDeviceState.setStatus("current")
_Index2_Type = DmiInteger
_Index2_Object = MibScalar
index2 = _Index2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 1),
    _Index2_Type()
)
index2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index2.setStatus("current")


class _BuiltIn_Type(Integer32):
    """Custom type builtIn based on Integer32"""
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
        *(("no", 4),
          ("other", 1),
          ("unknown", 2),
          ("yes", 3))
    )


_BuiltIn_Type.__name__ = "Integer32"
_BuiltIn_Object = MibTableColumn
builtIn = _BuiltIn_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 2),
    _BuiltIn_Type()
)
builtIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    builtIn.setStatus("current")


class _Type2_Type(Integer32):
    """Custom type type2 based on Integer32"""
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
        *(("cRT", 3),
          ("dSTN", 6),
          ("other", 1),
          ("sTN", 5),
          ("tFT", 4),
          ("unknown", 2))
    )


_Type2_Type.__name__ = "Integer32"
_Type2_Object = MibScalar
type2 = _Type2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 3),
    _Type2_Type()
)
type2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type2.setStatus("current")


class _ColorSupport_Type(Integer32):
    """Custom type colorSupport based on Integer32"""
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
        *(("no", 4),
          ("other", 1),
          ("unknown", 2),
          ("yes", 3))
    )


_ColorSupport_Type.__name__ = "Integer32"
_ColorSupport_Object = MibTableColumn
colorSupport = _ColorSupport_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 4),
    _ColorSupport_Type()
)
colorSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    colorSupport.setStatus("current")
_Brightness_Type = DmiInteger
_Brightness_Object = MibTableColumn
brightness = _Brightness_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 5),
    _Brightness_Type()
)
brightness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brightness.setStatus("current")
_Contrast_Type = DmiInteger
_Contrast_Object = MibTableColumn
contrast = _Contrast_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 6),
    _Contrast_Type()
)
contrast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contrast.setStatus("current")
_VideoGroupReference_Type = DmiString
_VideoGroupReference_Object = MibTableColumn
videoGroupReference = _VideoGroupReference_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 3, 1, 7),
    _VideoGroupReference_Type()
)
videoGroupReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoGroupReference.setStatus("current")
_DmtfInfraredPortTable_Object = MibTable
dmtfInfraredPortTable = _DmtfInfraredPortTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4)
)
if mibBuilder.loadTexts:
    dmtfInfraredPortTable.setStatus("current")
_DmtfInfraredPortEntry_Object = MibTableRow
dmtfInfraredPortEntry = _DmtfInfraredPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1)
)
dmtfInfraredPortEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "iRIndex"),
)
if mibBuilder.loadTexts:
    dmtfInfraredPortEntry.setStatus("current")


class _DmtfInfraredPortState_Type(Integer32):
    """Custom type dmtfInfraredPortState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfInfraredPortState_Type.__name__ = "Integer32"
_DmtfInfraredPortState_Object = MibTableColumn
dmtfInfraredPortState = _DmtfInfraredPortState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 0),
    _DmtfInfraredPortState_Type()
)
dmtfInfraredPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfInfraredPortState.setStatus("current")
_IRIndex_Type = DmiInteger
_IRIndex_Object = MibTableColumn
iRIndex = _IRIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 1),
    _IRIndex_Type()
)
iRIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRIndex.setStatus("current")
_IRLocation_Type = DmiString
_IRLocation_Object = MibTableColumn
iRLocation = _IRLocation_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 2),
    _IRLocation_Type()
)
iRLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRLocation.setStatus("current")


class _IREnableState_Type(Integer32):
    """Custom type iREnableState based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_IREnableState_Type.__name__ = "Integer32"
_IREnableState_Object = MibTableColumn
iREnableState = _IREnableState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 3),
    _IREnableState_Type()
)
iREnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iREnableState.setStatus("current")


class _IRLimitSpeedEnable_Type(Integer32):
    """Custom type iRLimitSpeedEnable based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_IRLimitSpeedEnable_Type.__name__ = "Integer32"
_IRLimitSpeedEnable_Object = MibTableColumn
iRLimitSpeedEnable = _IRLimitSpeedEnable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 4),
    _IRLimitSpeedEnable_Type()
)
iRLimitSpeedEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRLimitSpeedEnable.setStatus("current")
_IRSpeedLimit_Type = DmiInteger
_IRSpeedLimit_Object = MibTableColumn
iRSpeedLimit = _IRSpeedLimit_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 5),
    _IRSpeedLimit_Type()
)
iRSpeedLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRSpeedLimit.setStatus("current")
_IRPhysicalPortName_Type = DmiString
_IRPhysicalPortName_Object = MibTableColumn
iRPhysicalPortName = _IRPhysicalPortName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 6),
    _IRPhysicalPortName_Type()
)
iRPhysicalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRPhysicalPortName.setStatus("current")
_IRVirtualCOMPortName_Type = DmiString
_IRVirtualCOMPortName_Object = MibTableColumn
iRVirtualCOMPortName = _IRVirtualCOMPortName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 7),
    _IRVirtualCOMPortName_Type()
)
iRVirtualCOMPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRVirtualCOMPortName.setStatus("current")
_IRVirtualLPTPortName_Type = DmiString
_IRVirtualLPTPortName_Object = MibTableColumn
iRVirtualLPTPortName = _IRVirtualLPTPortName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 8),
    _IRVirtualLPTPortName_Type()
)
iRVirtualLPTPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRVirtualLPTPortName.setStatus("current")


class _IRProtocol_Type(Integer32):
    """Custom type iRProtocol based on Integer32"""
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
        *(("fIR", 4),
          ("mIR", 5),
          ("other", 1),
          ("sIR", 3),
          ("unknown", 2))
    )


_IRProtocol_Type.__name__ = "Integer32"
_IRProtocol_Object = MibTableColumn
iRProtocol = _IRProtocol_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 4, 1, 9),
    _IRProtocol_Type()
)
iRProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iRProtocol.setStatus("current")
_DmtfPointingDeviceTable_Object = MibTable
dmtfPointingDeviceTable = _DmtfPointingDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5)
)
if mibBuilder.loadTexts:
    dmtfPointingDeviceTable.setStatus("current")
_DmtfPointingDeviceEntry_Object = MibTableRow
dmtfPointingDeviceEntry = _DmtfPointingDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1)
)
dmtfPointingDeviceEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfPointingDeviceEntry.setStatus("current")


class _PointingDeviceType_Type(Integer32):
    """Custom type pointingDeviceType based on Integer32"""
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
        *(("glidePoint", 6),
          ("mouse", 3),
          ("other", 1),
          ("touchPad", 7),
          ("trackBall", 4),
          ("trackPoint", 5),
          ("unknown", 2))
    )


_PointingDeviceType_Type.__name__ = "Integer32"
_PointingDeviceType_Object = MibTableColumn
pointingDeviceType = _PointingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 1),
    _PointingDeviceType_Type()
)
pointingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceType.setStatus("current")


class _PointingDeviceInterface_Type(Integer32):
    """Custom type pointingDeviceInterface based on Integer32"""
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
              160,
              161,
              162)
        )
    )
    namedValues = NamedValues(
        *(("aDB", 8),
          ("busMouse", 7),
          ("busMouseDB9", 160),
          ("busMouseMicroDIN", 161),
          ("hPHIL", 6),
          ("infrared", 5),
          ("other", 1),
          ("pS2", 4),
          ("serial", 3),
          ("uSB", 162),
          ("unknown", 2))
    )


_PointingDeviceInterface_Type.__name__ = "Integer32"
_PointingDeviceInterface_Object = MibTableColumn
pointingDeviceInterface = _PointingDeviceInterface_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 2),
    _PointingDeviceInterface_Type()
)
pointingDeviceInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceInterface.setStatus("current")
_PointingDeviceIRQ_Type = DmiInteger
_PointingDeviceIRQ_Object = MibTableColumn
pointingDeviceIRQ = _PointingDeviceIRQ_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 3),
    _PointingDeviceIRQ_Type()
)
pointingDeviceIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceIRQ.setStatus("current")
_PointingDeviceButtons_Type = DmiInteger
_PointingDeviceButtons_Object = MibTableColumn
pointingDeviceButtons = _PointingDeviceButtons_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 4),
    _PointingDeviceButtons_Type()
)
pointingDeviceButtons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceButtons.setStatus("current")
_PointingDevicePortName_Type = DmiString
_PointingDevicePortName_Object = MibTableColumn
pointingDevicePortName = _PointingDevicePortName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 5),
    _PointingDevicePortName_Type()
)
pointingDevicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDevicePortName.setStatus("current")
_PointingDeviceDriverName_Type = DmiString
_PointingDeviceDriverName_Object = MibTableColumn
pointingDeviceDriverName = _PointingDeviceDriverName_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 6),
    _PointingDeviceDriverName_Type()
)
pointingDeviceDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceDriverName.setStatus("current")
_PointingDeviceDriverVersion_Type = DmiString
_PointingDeviceDriverVersion_Object = MibTableColumn
pointingDeviceDriverVersion = _PointingDeviceDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 7),
    _PointingDeviceDriverVersion_Type()
)
pointingDeviceDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pointingDeviceDriverVersion.setStatus("current")
_FRUGroupIndex_Type = DmiInteger
_FRUGroupIndex_Object = MibTableColumn
fRUGroupIndex = _FRUGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 8),
    _FRUGroupIndex_Type()
)
fRUGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fRUGroupIndex.setStatus("current")
_OperationalGroupIndex_Type = DmiInteger
_OperationalGroupIndex_Object = MibTableColumn
operationalGroupIndex = _OperationalGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 9),
    _OperationalGroupIndex_Type()
)
operationalGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    operationalGroupIndex.setStatus("current")


class _SecuritySettings_Type(Integer32):
    """Custom type securitySettings based on Integer32"""
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
        *(("externalInterfaceEnabled", 5),
          ("externalInterfaceLockedOut", 4),
          ("none", 3),
          ("other", 1),
          ("unknown", 2))
    )


_SecuritySettings_Type.__name__ = "Integer32"
_SecuritySettings_Object = MibTableColumn
securitySettings = _SecuritySettings_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 5, 1, 10),
    _SecuritySettings_Type()
)
securitySettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securitySettings.setStatus("current")
_DmtfSystemPowerManagementTable_Object = MibTable
dmtfSystemPowerManagementTable = _DmtfSystemPowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6)
)
if mibBuilder.loadTexts:
    dmtfSystemPowerManagementTable.setStatus("current")
_DmtfSystemPowerManagementEntry_Object = MibTableRow
dmtfSystemPowerManagementEntry = _DmtfSystemPowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1)
)
dmtfSystemPowerManagementEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
)
if mibBuilder.loadTexts:
    dmtfSystemPowerManagementEntry.setStatus("current")


class _PowerManagementCapabilities_Type(Integer32):
    """Custom type powerManagementCapabilities based on Integer32"""
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
        *(("aCPI10", 5),
          ("aPM11", 3),
          ("aPM12", 4),
          ("other", 1),
          ("unknown", 2))
    )


_PowerManagementCapabilities_Type.__name__ = "Integer32"
_PowerManagementCapabilities_Object = MibTableColumn
powerManagementCapabilities = _PowerManagementCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1, 1),
    _PowerManagementCapabilities_Type()
)
powerManagementCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerManagementCapabilities.setStatus("current")


class _ReducedCPUClockSpeed_Type(Integer32):
    """Custom type reducedCPUClockSpeed based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ReducedCPUClockSpeed_Type.__name__ = "Integer32"
_ReducedCPUClockSpeed_Object = MibTableColumn
reducedCPUClockSpeed = _ReducedCPUClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1, 2),
    _ReducedCPUClockSpeed_Type()
)
reducedCPUClockSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reducedCPUClockSpeed.setStatus("current")


class _OverrideAC_Type(Integer32):
    """Custom type overrideAC based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_OverrideAC_Type.__name__ = "Integer32"
_OverrideAC_Object = MibTableColumn
overrideAC = _OverrideAC_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1, 3),
    _OverrideAC_Type()
)
overrideAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    overrideAC.setStatus("current")


class _RingEventResume_Type(Integer32):
    """Custom type ringEventResume based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_RingEventResume_Type.__name__ = "Integer32"
_RingEventResume_Object = MibTableColumn
ringEventResume = _RingEventResume_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1, 4),
    _RingEventResume_Type()
)
ringEventResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringEventResume.setStatus("current")


class _AlarmResume_Type(Integer32):
    """Custom type alarmResume based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_AlarmResume_Type.__name__ = "Integer32"
_AlarmResume_Object = MibTableColumn
alarmResume = _AlarmResume_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 6, 1, 5),
    _AlarmResume_Type()
)
alarmResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmResume.setStatus("current")
_DmtfPowerManagementTable_Object = MibTable
dmtfPowerManagementTable = _DmtfPowerManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7)
)
if mibBuilder.loadTexts:
    dmtfPowerManagementTable.setStatus("current")
_DmtfPowerManagementEntry_Object = MibTableRow
dmtfPowerManagementEntry = _DmtfPowerManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1)
)
dmtfPowerManagementEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "PowerManagementEnabledDisabled"),
)
if mibBuilder.loadTexts:
    dmtfPowerManagementEntry.setStatus("current")


class _DmtfPowerManagementTableState_Type(Integer32):
    """Custom type dmtfPowerManagementTableState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfPowerManagementTableState_Type.__name__ = "Integer32"
_DmtfPowerManagementTableState_Object = MibTableColumn
dmtfPowerManagementTableState = _DmtfPowerManagementTableState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 0),
    _DmtfPowerManagementTableState_Type()
)
dmtfPowerManagementTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfPowerManagementTableState.setStatus("current")


class _PowerManagementEnabledDisabled_Type(Integer32):
    """Custom type powerManagementEnabledDisabled based on Integer32"""
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
        *(("disabled", 4),
          ("enabled", 3),
          ("other", 1),
          ("unknown", 2))
    )


_PowerManagementEnabledDisabled_Type.__name__ = "Integer32"
_PowerManagementEnabledDisabled_Object = MibTableColumn
powerManagementEnabledDisabled = _PowerManagementEnabledDisabled_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 1),
    _PowerManagementEnabledDisabled_Type()
)
powerManagementEnabledDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerManagementEnabledDisabled.setStatus("current")


class _CurrentPowerManagementState_Type(Integer32):
    """Custom type currentPowerManagementState based on Integer32"""
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
        *(("d0WorkingFullyON", 3),
          ("d1Sleeping", 4),
          ("d2NonVolatileSleepSoftOff", 5),
          ("d3OFF", 6),
          ("other", 1),
          ("unknown", 2))
    )


_CurrentPowerManagementState_Type.__name__ = "Integer32"
_CurrentPowerManagementState_Object = MibTableColumn
currentPowerManagementState = _CurrentPowerManagementState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 2),
    _CurrentPowerManagementState_Type()
)
currentPowerManagementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentPowerManagementState.setStatus("current")
_D1TimerValue_Type = DmiInteger
_D1TimerValue_Object = MibTableColumn
d1TimerValue = _D1TimerValue_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 3),
    _D1TimerValue_Type()
)
d1TimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d1TimerValue.setStatus("current")
_D2TimerValue_Type = DmiInteger
_D2TimerValue_Object = MibTableColumn
d2TimerValue = _D2TimerValue_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 4),
    _D2TimerValue_Type()
)
d2TimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d2TimerValue.setStatus("current")
_D3TimerValue_Type = DmiInteger
_D3TimerValue_Object = MibTableColumn
d3TimerValue = _D3TimerValue_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 7, 1, 5),
    _D3TimerValue_Type()
)
d3TimerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d3TimerValue.setStatus("current")
_DmtfPowerManagementBinaryAssociationTable_Object = MibTable
dmtfPowerManagementBinaryAssociationTable = _DmtfPowerManagementBinaryAssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8)
)
if mibBuilder.loadTexts:
    dmtfPowerManagementBinaryAssociationTable.setStatus("current")
_DmtfPowerManagementBinaryAssociationEntry_Object = MibTableRow
dmtfPowerManagementBinaryAssociationEntry = _DmtfPowerManagementBinaryAssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1)
)
dmtfPowerManagementBinaryAssociationEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "index"),
)
if mibBuilder.loadTexts:
    dmtfPowerManagementBinaryAssociationEntry.setStatus("current")


class _DmtfPowerManagementBinaryAssociationTableState_Type(Integer32):
    """Custom type dmtfPowerManagementBinaryAssociationTableState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfPowerManagementBinaryAssociationTableState_Type.__name__ = "Integer32"
_DmtfPowerManagementBinaryAssociationTableState_Object = MibTableColumn
dmtfPowerManagementBinaryAssociationTableState = _DmtfPowerManagementBinaryAssociationTableState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1, 0),
    _DmtfPowerManagementBinaryAssociationTableState_Type()
)
dmtfPowerManagementBinaryAssociationTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfPowerManagementBinaryAssociationTableState.setStatus("current")
_Index_Type = DmiInteger
_Index_Object = MibTableColumn
index = _Index_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1, 1),
    _Index_Type()
)
index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    index.setStatus("current")
_Type_Type = DmiString
_Type_Object = MibTableColumn
type = _Type_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1, 2),
    _Type_Type()
)
type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    type.setStatus("current")
_Ref1_Type = DmiString
_Ref1_Object = MibTableColumn
ref1 = _Ref1_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1, 3),
    _Ref1_Type()
)
ref1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ref1.setStatus("current")
_Ref2_Type = DmiString
_Ref2_Object = MibTableColumn
ref2 = _Ref2_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 8, 1, 4),
    _Ref2_Type()
)
ref2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ref2.setStatus("current")
_DmtfDeviceBayTable_Object = MibTable
dmtfDeviceBayTable = _DmtfDeviceBayTable_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9)
)
if mibBuilder.loadTexts:
    dmtfDeviceBayTable.setStatus("current")
_DmtfDeviceBayEntry_Object = MibTableRow
dmtfDeviceBayEntry = _DmtfDeviceBayEntry_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1)
)
dmtfDeviceBayEntry.setIndexNames(
    (0, "DMTF-MOBILE-MIB", "DmiCompId"),
    (0, "DMTF-MOBILE-MIB", "DmiGroupId"),
    (0, "DMTF-MOBILE-MIB", "deviceBayIndex"),
)
if mibBuilder.loadTexts:
    dmtfDeviceBayEntry.setStatus("current")


class _DmtfDeviceBayState_Type(Integer32):
    """Custom type dmtfDeviceBayState based on Integer32"""
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_DmtfDeviceBayState_Type.__name__ = "Integer32"
_DmtfDeviceBayState_Object = MibTableColumn
dmtfDeviceBayState = _DmtfDeviceBayState_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 0),
    _DmtfDeviceBayState_Type()
)
dmtfDeviceBayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dmtfDeviceBayState.setStatus("current")
_DeviceBayIndex_Type = DmiInteger
_DeviceBayIndex_Object = MibTableColumn
deviceBayIndex = _DeviceBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 1),
    _DeviceBayIndex_Type()
)
deviceBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBayIndex.setStatus("current")


class _DeviceBayType_Type(Integer32):
    """Custom type deviceBayType based on Integer32"""
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
        *(("other", 1),
          ("proprietaryBay", 3),
          ("standardDesktopDeviceBay", 4),
          ("standardMobileDeviceBay", 5),
          ("standardUltraMobileDeviceBay", 6),
          ("unknown", 2))
    )


_DeviceBayType_Type.__name__ = "Integer32"
_DeviceBayType_Object = MibTableColumn
deviceBayType = _DeviceBayType_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 2),
    _DeviceBayType_Type()
)
deviceBayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBayType.setStatus("current")
_DeviceBayLocation_Type = DmiString
_DeviceBayLocation_Object = MibTableColumn
deviceBayLocation = _DeviceBayLocation_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 3),
    _DeviceBayLocation_Type()
)
deviceBayLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceBayLocation.setStatus("current")
_DevicesSupported_Type = DmiString
_DevicesSupported_Object = MibTableColumn
devicesSupported = _DevicesSupported_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 4),
    _DevicesSupported_Type()
)
devicesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicesSupported.setStatus("current")
_DeviceCurrentlyAttached_Type = DmiString
_DeviceCurrentlyAttached_Object = MibTableColumn
deviceCurrentlyAttached = _DeviceCurrentlyAttached_Object(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 9, 1, 5),
    _DeviceCurrentlyAttached_Type()
)
deviceCurrentlyAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCurrentlyAttached.setStatus("current")
_DmtfDynOids_ObjectIdentity = ObjectIdentity
dmtfDynOids = _DmtfDynOids_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 412, 3)
)

# Managed Objects groups


# Notification objects

dmtfPortableBatteryLowCombinedBatterysCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 0, 1)
)
dmtfPortableBatteryLowCombinedBatterysCharge.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSys"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSub"))
)
if mibBuilder.loadTexts:
    dmtfPortableBatteryLowCombinedBatterysCharge.setStatus(
        "current"
    )

dmtfPortableBatteryCriticalCombinedBatterysCharge = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 0, 2)
)
dmtfPortableBatteryCriticalCombinedBatterysCharge.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSys"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSub"))
)
if mibBuilder.loadTexts:
    dmtfPortableBatteryCriticalCombinedBatterysCharge.setStatus(
        "current"
    )

dmtfPortableBatteryMaintenanceRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 412, 2, 8, 1, 0, 3)
)
dmtfPortableBatteryMaintenanceRequired.setObjects(
      *(("DMTF-DMI-MIB", "dmiEventDateTime"),
        ("DMTF-DMI-MIB", "dmiCompId"),
        ("DMTF-DMI-MIB", "dmiEventSeverity"),
        ("DMTF-DMI-MIB", "dmiEventStateKey"),
        ("DMTF-DMI-MIB", "dmiEventAssociatedGroup"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSys"),
        ("DMTF-MOBILE-MIB", "dmtfPortableBatteryEvSub"))
)
if mibBuilder.loadTexts:
    dmtfPortableBatteryMaintenanceRequired.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DMTF-MOBILE-MIB",
    **{"DmiCounter": DmiCounter,
       "DmiCounter64": DmiCounter64,
       "DmiGauge": DmiGauge,
       "DmiInteger": DmiInteger,
       "DmiOctetstring": DmiOctetstring,
       "DmiCompId": DmiCompId,
       "DmiGroupId": DmiGroupId,
       "dmtf": dmtf,
       "dmtfStdMifs": dmtfStdMifs,
       "dmtfMobileComputerMIF": dmtfMobileComputerMIF,
       "dmtfPortableBatteryTable": dmtfPortableBatteryTable,
       "dmtfPortableBatteryTraps": dmtfPortableBatteryTraps,
       "dmtfPortableBatteryLowCombinedBatterysCharge": dmtfPortableBatteryLowCombinedBatterysCharge,
       "dmtfPortableBatteryCriticalCombinedBatterysCharge": dmtfPortableBatteryCriticalCombinedBatterysCharge,
       "dmtfPortableBatteryMaintenanceRequired": dmtfPortableBatteryMaintenanceRequired,
       "dmtfPortableBatteryEntry": dmtfPortableBatteryEntry,
       "dmtfPortableBatteryState": dmtfPortableBatteryState,
       "portableBatteryIndex": portableBatteryIndex,
       "portableBatteryLocation": portableBatteryLocation,
       "portableBatteryManufacturer": portableBatteryManufacturer,
       "portableBatteryManufactureDate": portableBatteryManufactureDate,
       "portableBatterySerialNumber": portableBatterySerialNumber,
       "portableBatteryDeviceName": portableBatteryDeviceName,
       "portableBatteryDeviceChemistry": portableBatteryDeviceChemistry,
       "portableBatteryDesignCapacity": portableBatteryDesignCapacity,
       "portableBatteryDesignVoltage": portableBatteryDesignVoltage,
       "smartBatteryVersion": smartBatteryVersion,
       "fullChargeCapacity": fullChargeCapacity,
       "remainingCapacity": remainingCapacity,
       "maximumError": maximumError,
       "portableBatteryChargingStatus": portableBatteryChargingStatus,
       "remainingBatteryTime": remainingBatteryTime,
       "remainingTimeToFullBattery": remainingTimeToFullBattery,
       "powerUnitIndex": powerUnitIndex,
       "dmtfPortableBatteryEvSys": dmtfPortableBatteryEvSys,
       "dmtfPortableBatteryEvSub": dmtfPortableBatteryEvSub,
       "dmtfDynamicStatesTable": dmtfDynamicStatesTable,
       "dmtfDynamicStatesEntry": dmtfDynamicStatesEntry,
       "aCLineStatus": aCLineStatus,
       "dockingStatus": dockingStatus,
       "dmtfVideoOutputDeviceTable": dmtfVideoOutputDeviceTable,
       "dmtfVideoOutputDeviceEntry": dmtfVideoOutputDeviceEntry,
       "dmtfVideoOutputDeviceState": dmtfVideoOutputDeviceState,
       "index2": index2,
       "builtIn": builtIn,
       "type2": type2,
       "colorSupport": colorSupport,
       "brightness": brightness,
       "contrast": contrast,
       "videoGroupReference": videoGroupReference,
       "dmtfInfraredPortTable": dmtfInfraredPortTable,
       "dmtfInfraredPortEntry": dmtfInfraredPortEntry,
       "dmtfInfraredPortState": dmtfInfraredPortState,
       "iRIndex": iRIndex,
       "iRLocation": iRLocation,
       "iREnableState": iREnableState,
       "iRLimitSpeedEnable": iRLimitSpeedEnable,
       "iRSpeedLimit": iRSpeedLimit,
       "iRPhysicalPortName": iRPhysicalPortName,
       "iRVirtualCOMPortName": iRVirtualCOMPortName,
       "iRVirtualLPTPortName": iRVirtualLPTPortName,
       "iRProtocol": iRProtocol,
       "dmtfPointingDeviceTable": dmtfPointingDeviceTable,
       "dmtfPointingDeviceEntry": dmtfPointingDeviceEntry,
       "pointingDeviceType": pointingDeviceType,
       "pointingDeviceInterface": pointingDeviceInterface,
       "pointingDeviceIRQ": pointingDeviceIRQ,
       "pointingDeviceButtons": pointingDeviceButtons,
       "pointingDevicePortName": pointingDevicePortName,
       "pointingDeviceDriverName": pointingDeviceDriverName,
       "pointingDeviceDriverVersion": pointingDeviceDriverVersion,
       "fRUGroupIndex": fRUGroupIndex,
       "operationalGroupIndex": operationalGroupIndex,
       "securitySettings": securitySettings,
       "dmtfSystemPowerManagementTable": dmtfSystemPowerManagementTable,
       "dmtfSystemPowerManagementEntry": dmtfSystemPowerManagementEntry,
       "powerManagementCapabilities": powerManagementCapabilities,
       "reducedCPUClockSpeed": reducedCPUClockSpeed,
       "overrideAC": overrideAC,
       "ringEventResume": ringEventResume,
       "alarmResume": alarmResume,
       "dmtfPowerManagementTable": dmtfPowerManagementTable,
       "dmtfPowerManagementEntry": dmtfPowerManagementEntry,
       "dmtfPowerManagementTableState": dmtfPowerManagementTableState,
       "powerManagementEnabledDisabled": powerManagementEnabledDisabled,
       "currentPowerManagementState": currentPowerManagementState,
       "d1TimerValue": d1TimerValue,
       "d2TimerValue": d2TimerValue,
       "d3TimerValue": d3TimerValue,
       "dmtfPowerManagementBinaryAssociationTable": dmtfPowerManagementBinaryAssociationTable,
       "dmtfPowerManagementBinaryAssociationEntry": dmtfPowerManagementBinaryAssociationEntry,
       "dmtfPowerManagementBinaryAssociationTableState": dmtfPowerManagementBinaryAssociationTableState,
       "index": index,
       "type": type,
       "ref1": ref1,
       "ref2": ref2,
       "dmtfDeviceBayTable": dmtfDeviceBayTable,
       "dmtfDeviceBayEntry": dmtfDeviceBayEntry,
       "dmtfDeviceBayState": dmtfDeviceBayState,
       "deviceBayIndex": deviceBayIndex,
       "deviceBayType": deviceBayType,
       "deviceBayLocation": deviceBayLocation,
       "devicesSupported": devicesSupported,
       "deviceCurrentlyAttached": deviceCurrentlyAttached,
       "dmtfDynOids": dmtfDynOids}
)
