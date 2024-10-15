# SNMP MIB module (MY-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MY-ENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:19 2024
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

myEntityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21)
)
myEntityMIB.setRevisions(
        ("2002-03-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyDeviceMIBObjects_ObjectIdentity = ObjectIdentity
myDeviceMIBObjects = _MyDeviceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1)
)
_MyDeviceMaxNumber_Type = Integer32
_MyDeviceMaxNumber_Object = MibScalar
myDeviceMaxNumber = _MyDeviceMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 1),
    _MyDeviceMaxNumber_Type()
)
myDeviceMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceMaxNumber.setStatus("current")
_MyDeviceInfoTable_Object = MibTable
myDeviceInfoTable = _MyDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2)
)
if mibBuilder.loadTexts:
    myDeviceInfoTable.setStatus("current")
_MyDeviceInfoEntry_Object = MibTableRow
myDeviceInfoEntry = _MyDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1)
)
myDeviceInfoEntry.setIndexNames(
    (0, "MY-ENTITY-MIB", "myDeviceInfoIndex"),
)
if mibBuilder.loadTexts:
    myDeviceInfoEntry.setStatus("current")
_MyDeviceInfoIndex_Type = Integer32
_MyDeviceInfoIndex_Object = MibTableColumn
myDeviceInfoIndex = _MyDeviceInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 1),
    _MyDeviceInfoIndex_Type()
)
myDeviceInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceInfoIndex.setStatus("current")


class _MyDeviceInfoDescr_Type(DisplayString):
    """Custom type myDeviceInfoDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDeviceInfoDescr_Type.__name__ = "DisplayString"
_MyDeviceInfoDescr_Object = MibTableColumn
myDeviceInfoDescr = _MyDeviceInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 2),
    _MyDeviceInfoDescr_Type()
)
myDeviceInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceInfoDescr.setStatus("current")
_MyDeviceInfoSlotNumber_Type = Integer32
_MyDeviceInfoSlotNumber_Object = MibTableColumn
myDeviceInfoSlotNumber = _MyDeviceInfoSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 3),
    _MyDeviceInfoSlotNumber_Type()
)
myDeviceInfoSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceInfoSlotNumber.setStatus("current")


class _MyDevicePowerStatus_Type(Integer32):
    """Custom type myDevicePowerStatus based on Integer32"""
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
        *(("rpsLinkAndNoPower", 2),
          ("rpsLinkAndPower", 4),
          ("rpsLinkAndReadyForPower", 3),
          ("rpsNoLink", 1))
    )


_MyDevicePowerStatus_Type.__name__ = "Integer32"
_MyDevicePowerStatus_Object = MibTableColumn
myDevicePowerStatus = _MyDevicePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 4),
    _MyDevicePowerStatus_Type()
)
myDevicePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDevicePowerStatus.setStatus("current")
_MyDeviceMacAddress_Type = MacAddress
_MyDeviceMacAddress_Object = MibTableColumn
myDeviceMacAddress = _MyDeviceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 5),
    _MyDeviceMacAddress_Type()
)
myDeviceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceMacAddress.setStatus("current")


class _MyDevicePriority_Type(Integer32):
    """Custom type myDevicePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MyDevicePriority_Type.__name__ = "Integer32"
_MyDevicePriority_Object = MibTableColumn
myDevicePriority = _MyDevicePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 6),
    _MyDevicePriority_Type()
)
myDevicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDevicePriority.setStatus("current")


class _MyDeviceAlias_Type(DisplayString):
    """Custom type myDeviceAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyDeviceAlias_Type.__name__ = "DisplayString"
_MyDeviceAlias_Object = MibTableColumn
myDeviceAlias = _MyDeviceAlias_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 7),
    _MyDeviceAlias_Type()
)
myDeviceAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDeviceAlias.setStatus("current")


class _MyDeviceSWVersion_Type(DisplayString):
    """Custom type myDeviceSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyDeviceSWVersion_Type.__name__ = "DisplayString"
_MyDeviceSWVersion_Object = MibTableColumn
myDeviceSWVersion = _MyDeviceSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 8),
    _MyDeviceSWVersion_Type()
)
myDeviceSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceSWVersion.setStatus("current")


class _MyDeviceHWVersion_Type(DisplayString):
    """Custom type myDeviceHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyDeviceHWVersion_Type.__name__ = "DisplayString"
_MyDeviceHWVersion_Object = MibTableColumn
myDeviceHWVersion = _MyDeviceHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 2, 1, 9),
    _MyDeviceHWVersion_Type()
)
myDeviceHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDeviceHWVersion.setStatus("current")
_MySlotInfoTable_Object = MibTable
mySlotInfoTable = _MySlotInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3)
)
if mibBuilder.loadTexts:
    mySlotInfoTable.setStatus("current")
_MySlotInfoEntry_Object = MibTableRow
mySlotInfoEntry = _MySlotInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1)
)
mySlotInfoEntry.setIndexNames(
    (0, "MY-ENTITY-MIB", "mySlotInfoDeviceIndex"),
    (0, "MY-ENTITY-MIB", "mySlotInfoIndex"),
)
if mibBuilder.loadTexts:
    mySlotInfoEntry.setStatus("current")
_MySlotInfoDeviceIndex_Type = Integer32
_MySlotInfoDeviceIndex_Object = MibTableColumn
mySlotInfoDeviceIndex = _MySlotInfoDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 1),
    _MySlotInfoDeviceIndex_Type()
)
mySlotInfoDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotInfoDeviceIndex.setStatus("current")
_MySlotInfoIndex_Type = Integer32
_MySlotInfoIndex_Object = MibTableColumn
mySlotInfoIndex = _MySlotInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 2),
    _MySlotInfoIndex_Type()
)
mySlotInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotInfoIndex.setStatus("current")
_MySlotModuleInfoDescr_Type = DisplayString
_MySlotModuleInfoDescr_Object = MibTableColumn
mySlotModuleInfoDescr = _MySlotModuleInfoDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 3),
    _MySlotModuleInfoDescr_Type()
)
mySlotModuleInfoDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotModuleInfoDescr.setStatus("current")
_MySlotInfoPortNumber_Type = Integer32
_MySlotInfoPortNumber_Object = MibTableColumn
mySlotInfoPortNumber = _MySlotInfoPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 4),
    _MySlotInfoPortNumber_Type()
)
mySlotInfoPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotInfoPortNumber.setStatus("current")
_MySlotInfoPortMaxNumber_Type = Integer32
_MySlotInfoPortMaxNumber_Object = MibTableColumn
mySlotInfoPortMaxNumber = _MySlotInfoPortMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 5),
    _MySlotInfoPortMaxNumber_Type()
)
mySlotInfoPortMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotInfoPortMaxNumber.setStatus("current")


class _MySlotInfoDesc_Type(DisplayString):
    """Custom type mySlotInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MySlotInfoDesc_Type.__name__ = "DisplayString"
_MySlotInfoDesc_Object = MibTableColumn
mySlotInfoDesc = _MySlotInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 3, 1, 6),
    _MySlotInfoDesc_Type()
)
mySlotInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySlotInfoDesc.setStatus("current")
_MyModuleTempStateTable_Object = MibTable
myModuleTempStateTable = _MyModuleTempStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 4)
)
if mibBuilder.loadTexts:
    myModuleTempStateTable.setStatus("current")
_MyModuleTempStateEntry_Object = MibTableRow
myModuleTempStateEntry = _MyModuleTempStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 4, 1)
)
myModuleTempStateEntry.setIndexNames(
    (0, "MY-ENTITY-MIB", "myModuleTempStateDeviceIndex"),
    (0, "MY-ENTITY-MIB", "myModuleTempStateIndex"),
)
if mibBuilder.loadTexts:
    myModuleTempStateEntry.setStatus("current")
_MyModuleTempStateDeviceIndex_Type = Integer32
_MyModuleTempStateDeviceIndex_Object = MibTableColumn
myModuleTempStateDeviceIndex = _MyModuleTempStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 4, 1, 1),
    _MyModuleTempStateDeviceIndex_Type()
)
myModuleTempStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myModuleTempStateDeviceIndex.setStatus("current")
_MyModuleTempStateIndex_Type = Integer32
_MyModuleTempStateIndex_Object = MibTableColumn
myModuleTempStateIndex = _MyModuleTempStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 4, 1, 2),
    _MyModuleTempStateIndex_Type()
)
myModuleTempStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myModuleTempStateIndex.setStatus("current")


class _MyModuleTempState_Type(Integer32):
    """Custom type myModuleTempState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempNormal", 1),
          ("tempWarning", 2))
    )


_MyModuleTempState_Type.__name__ = "Integer32"
_MyModuleTempState_Object = MibTableColumn
myModuleTempState = _MyModuleTempState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 4, 1, 3),
    _MyModuleTempState_Type()
)
myModuleTempState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myModuleTempState.setStatus("current")
_MyPowerStateTable_Object = MibTable
myPowerStateTable = _MyPowerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5)
)
if mibBuilder.loadTexts:
    myPowerStateTable.setStatus("current")
_MyPowerStateEntry_Object = MibTableRow
myPowerStateEntry = _MyPowerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5, 1)
)
myPowerStateEntry.setIndexNames(
    (0, "MY-ENTITY-MIB", "myPowerStateDeviceIndex"),
    (0, "MY-ENTITY-MIB", "myPowerStateIndex"),
)
if mibBuilder.loadTexts:
    myPowerStateEntry.setStatus("current")
_MyPowerStateDeviceIndex_Type = Integer32
_MyPowerStateDeviceIndex_Object = MibTableColumn
myPowerStateDeviceIndex = _MyPowerStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5, 1, 1),
    _MyPowerStateDeviceIndex_Type()
)
myPowerStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPowerStateDeviceIndex.setStatus("current")
_MyPowerStateIndex_Type = Integer32
_MyPowerStateIndex_Object = MibTableColumn
myPowerStateIndex = _MyPowerStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5, 1, 2),
    _MyPowerStateIndex_Type()
)
myPowerStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPowerStateIndex.setStatus("current")


class _MyPowerState_Type(Integer32):
    """Custom type myPowerState based on Integer32"""
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
        *(("linkAndNoPower", 2),
          ("linkAndPower", 4),
          ("linkAndPowerAbnormal", 5),
          ("linkAndReadyForPower", 3),
          ("noLink", 1))
    )


_MyPowerState_Type.__name__ = "Integer32"
_MyPowerState_Object = MibTableColumn
myPowerState = _MyPowerState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5, 1, 3),
    _MyPowerState_Type()
)
myPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPowerState.setStatus("current")


class _MyPowerStatePowerDescr_Type(DisplayString):
    """Custom type myPowerStatePowerDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyPowerStatePowerDescr_Type.__name__ = "DisplayString"
_MyPowerStatePowerDescr_Object = MibTableColumn
myPowerStatePowerDescr = _MyPowerStatePowerDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 5, 1, 4),
    _MyPowerStatePowerDescr_Type()
)
myPowerStatePowerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPowerStatePowerDescr.setStatus("current")
_MyFanStateTable_Object = MibTable
myFanStateTable = _MyFanStateTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6)
)
if mibBuilder.loadTexts:
    myFanStateTable.setStatus("current")
_MyFanStateEntry_Object = MibTableRow
myFanStateEntry = _MyFanStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6, 1)
)
myFanStateEntry.setIndexNames(
    (0, "MY-ENTITY-MIB", "myFanStateDeviceIndex"),
    (0, "MY-ENTITY-MIB", "myFanStateIndex"),
)
if mibBuilder.loadTexts:
    myFanStateEntry.setStatus("current")
_MyFanStateDeviceIndex_Type = Integer32
_MyFanStateDeviceIndex_Object = MibTableColumn
myFanStateDeviceIndex = _MyFanStateDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6, 1, 1),
    _MyFanStateDeviceIndex_Type()
)
myFanStateDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFanStateDeviceIndex.setStatus("current")
_MyFanStateIndex_Type = Integer32
_MyFanStateIndex_Object = MibTableColumn
myFanStateIndex = _MyFanStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6, 1, 2),
    _MyFanStateIndex_Type()
)
myFanStateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFanStateIndex.setStatus("current")


class _MyFanState_Type(Integer32):
    """Custom type myFanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 2),
          ("work", 1))
    )


_MyFanState_Type.__name__ = "Integer32"
_MyFanState_Object = MibTableColumn
myFanState = _MyFanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6, 1, 3),
    _MyFanState_Type()
)
myFanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFanState.setStatus("current")


class _MyFanStateFanDescr_Type(DisplayString):
    """Custom type myFanStateFanDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyFanStateFanDescr_Type.__name__ = "DisplayString"
_MyFanStateFanDescr_Object = MibTableColumn
myFanStateFanDescr = _MyFanStateFanDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 1, 6, 1, 4),
    _MyFanStateFanDescr_Type()
)
myFanStateFanDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myFanStateFanDescr.setStatus("current")
_MyEntityMIBTraps_ObjectIdentity = ObjectIdentity
myEntityMIBTraps = _MyEntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 2)
)
_MyEntityStateChgDesc_Type = DisplayString
_MyEntityStateChgDesc_Object = MibScalar
myEntityStateChgDesc = _MyEntityStateChgDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 2, 1),
    _MyEntityStateChgDesc_Type()
)
myEntityStateChgDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    myEntityStateChgDesc.setStatus("current")


class _MyTemperatureWarningDesc_Type(DisplayString):
    """Custom type myTemperatureWarningDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MyTemperatureWarningDesc_Type.__name__ = "DisplayString"
_MyTemperatureWarningDesc_Object = MibScalar
myTemperatureWarningDesc = _MyTemperatureWarningDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 2, 3),
    _MyTemperatureWarningDesc_Type()
)
myTemperatureWarningDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    myTemperatureWarningDesc.setStatus("current")
_MyDeviceMIBConformance_ObjectIdentity = ObjectIdentity
myDeviceMIBConformance = _MyDeviceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3)
)
_MyDeviceMIBCompliances_ObjectIdentity = ObjectIdentity
myDeviceMIBCompliances = _MyDeviceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 1)
)
_MyDeviceMIBGroups_ObjectIdentity = ObjectIdentity
myDeviceMIBGroups = _MyDeviceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2)
)

# Managed Objects groups

myDeviceInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 1)
)
myDeviceInfoMIBGroup.setObjects(
      *(("MY-ENTITY-MIB", "myDeviceMaxNumber"),
        ("MY-ENTITY-MIB", "myDeviceInfoIndex"),
        ("MY-ENTITY-MIB", "myDeviceInfoDescr"),
        ("MY-ENTITY-MIB", "myDeviceInfoSlotNumber"),
        ("MY-ENTITY-MIB", "myDevicePowerStatus"))
)
if mibBuilder.loadTexts:
    myDeviceInfoMIBGroup.setStatus("current")

myOptionalDevInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 2)
)
myOptionalDevInfoMIBGroup.setObjects(
      *(("MY-ENTITY-MIB", "myDeviceMacAddress"),
        ("MY-ENTITY-MIB", "myDevicePriority"),
        ("MY-ENTITY-MIB", "myDeviceAlias"),
        ("MY-ENTITY-MIB", "myDeviceSWVersion"),
        ("MY-ENTITY-MIB", "myDeviceHWVersion"))
)
if mibBuilder.loadTexts:
    myOptionalDevInfoMIBGroup.setStatus("current")

myModuleInfoMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 3)
)
myModuleInfoMIBGroup.setObjects(
      *(("MY-ENTITY-MIB", "mySlotInfoDeviceIndex"),
        ("MY-ENTITY-MIB", "mySlotInfoIndex"),
        ("MY-ENTITY-MIB", "mySlotModuleInfoDescr"),
        ("MY-ENTITY-MIB", "mySlotInfoPortNumber"),
        ("MY-ENTITY-MIB", "mySlotInfoPortMaxNumber"),
        ("MY-ENTITY-MIB", "mySlotInfoDesc"))
)
if mibBuilder.loadTexts:
    myModuleInfoMIBGroup.setStatus("current")

myEntityChgDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 4)
)
myEntityChgDescGroup.setObjects(
    ("MY-ENTITY-MIB", "myEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    myEntityChgDescGroup.setStatus("current")

myModuleTempStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 6)
)
myModuleTempStateGroup.setObjects(
      *(("MY-ENTITY-MIB", "myModuleTempStateDeviceIndex"),
        ("MY-ENTITY-MIB", "myModuleTempStateIndex"),
        ("MY-ENTITY-MIB", "myModuleTempState"))
)
if mibBuilder.loadTexts:
    myModuleTempStateGroup.setStatus("current")

myPowerStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 7)
)
myPowerStateGroup.setObjects(
      *(("MY-ENTITY-MIB", "myPowerStateDeviceIndex"),
        ("MY-ENTITY-MIB", "myPowerStateIndex"),
        ("MY-ENTITY-MIB", "myPowerState"),
        ("MY-ENTITY-MIB", "myPowerStatePowerDescr"))
)
if mibBuilder.loadTexts:
    myPowerStateGroup.setStatus("current")

myFanStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 8)
)
myFanStateGroup.setObjects(
      *(("MY-ENTITY-MIB", "myFanStateDeviceIndex"),
        ("MY-ENTITY-MIB", "myFanStateIndex"),
        ("MY-ENTITY-MIB", "myFanState"),
        ("MY-ENTITY-MIB", "myFanStateFanDescr"))
)
if mibBuilder.loadTexts:
    myFanStateGroup.setStatus("current")

myTemperatureWarningDescGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 9)
)
myTemperatureWarningDescGroup.setObjects(
    ("MY-ENTITY-MIB", "myTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    myTemperatureWarningDescGroup.setStatus("current")


# Notification objects

myEntityStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 2, 2)
)
myEntityStatusChange.setObjects(
    ("MY-ENTITY-MIB", "myEntityStateChgDesc")
)
if mibBuilder.loadTexts:
    myEntityStatusChange.setStatus(
        "current"
    )

myTemperatureWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 2, 4)
)
myTemperatureWarning.setObjects(
    ("MY-ENTITY-MIB", "myTemperatureWarningDesc")
)
if mibBuilder.loadTexts:
    myTemperatureWarning.setStatus(
        "current"
    )


# Notifications groups

myDeviceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 5)
)
myDeviceMIBNotificationGroup.setObjects(
    ("MY-ENTITY-MIB", "myEntityStatusChange")
)
if mibBuilder.loadTexts:
    myDeviceMIBNotificationGroup.setStatus(
        "current"
    )

myTemperatureWarningGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 2, 10)
)
myTemperatureWarningGroup.setObjects(
    ("MY-ENTITY-MIB", "myTemperatureWarning")
)
if mibBuilder.loadTexts:
    myTemperatureWarningGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

myDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    myDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-ENTITY-MIB",
    **{"myEntityMIB": myEntityMIB,
       "myDeviceMIBObjects": myDeviceMIBObjects,
       "myDeviceMaxNumber": myDeviceMaxNumber,
       "myDeviceInfoTable": myDeviceInfoTable,
       "myDeviceInfoEntry": myDeviceInfoEntry,
       "myDeviceInfoIndex": myDeviceInfoIndex,
       "myDeviceInfoDescr": myDeviceInfoDescr,
       "myDeviceInfoSlotNumber": myDeviceInfoSlotNumber,
       "myDevicePowerStatus": myDevicePowerStatus,
       "myDeviceMacAddress": myDeviceMacAddress,
       "myDevicePriority": myDevicePriority,
       "myDeviceAlias": myDeviceAlias,
       "myDeviceSWVersion": myDeviceSWVersion,
       "myDeviceHWVersion": myDeviceHWVersion,
       "mySlotInfoTable": mySlotInfoTable,
       "mySlotInfoEntry": mySlotInfoEntry,
       "mySlotInfoDeviceIndex": mySlotInfoDeviceIndex,
       "mySlotInfoIndex": mySlotInfoIndex,
       "mySlotModuleInfoDescr": mySlotModuleInfoDescr,
       "mySlotInfoPortNumber": mySlotInfoPortNumber,
       "mySlotInfoPortMaxNumber": mySlotInfoPortMaxNumber,
       "mySlotInfoDesc": mySlotInfoDesc,
       "myModuleTempStateTable": myModuleTempStateTable,
       "myModuleTempStateEntry": myModuleTempStateEntry,
       "myModuleTempStateDeviceIndex": myModuleTempStateDeviceIndex,
       "myModuleTempStateIndex": myModuleTempStateIndex,
       "myModuleTempState": myModuleTempState,
       "myPowerStateTable": myPowerStateTable,
       "myPowerStateEntry": myPowerStateEntry,
       "myPowerStateDeviceIndex": myPowerStateDeviceIndex,
       "myPowerStateIndex": myPowerStateIndex,
       "myPowerState": myPowerState,
       "myPowerStatePowerDescr": myPowerStatePowerDescr,
       "myFanStateTable": myFanStateTable,
       "myFanStateEntry": myFanStateEntry,
       "myFanStateDeviceIndex": myFanStateDeviceIndex,
       "myFanStateIndex": myFanStateIndex,
       "myFanState": myFanState,
       "myFanStateFanDescr": myFanStateFanDescr,
       "myEntityMIBTraps": myEntityMIBTraps,
       "myEntityStateChgDesc": myEntityStateChgDesc,
       "myEntityStatusChange": myEntityStatusChange,
       "myTemperatureWarningDesc": myTemperatureWarningDesc,
       "myTemperatureWarning": myTemperatureWarning,
       "myDeviceMIBConformance": myDeviceMIBConformance,
       "myDeviceMIBCompliances": myDeviceMIBCompliances,
       "myDeviceMIBCompliance": myDeviceMIBCompliance,
       "myDeviceMIBGroups": myDeviceMIBGroups,
       "myDeviceInfoMIBGroup": myDeviceInfoMIBGroup,
       "myOptionalDevInfoMIBGroup": myOptionalDevInfoMIBGroup,
       "myModuleInfoMIBGroup": myModuleInfoMIBGroup,
       "myEntityChgDescGroup": myEntityChgDescGroup,
       "myDeviceMIBNotificationGroup": myDeviceMIBNotificationGroup,
       "myModuleTempStateGroup": myModuleTempStateGroup,
       "myPowerStateGroup": myPowerStateGroup,
       "myFanStateGroup": myFanStateGroup,
       "myTemperatureWarningDescGroup": myTemperatureWarningDescGroup,
       "myTemperatureWarningGroup": myTemperatureWarningGroup}
)
