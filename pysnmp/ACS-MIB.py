# SNMP MIB module (ACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:38 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

acs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16)
)
acs.setRevisions(
        ("2010-10-10 00:00",
         "2009-12-11 00:00",
         "2007-09-17 00:00")
)


# Types definitions



class PowerSupplyState(Integer32):
    """Custom type PowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("powerNotInstaled", 9999),
          ("statePowerOff", 2),
          ("statePowerOn", 1))
    )





class SerialPortSpeed(Integer32):
    """Custom type SerialPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200,
              230400,
              460800)
        )
    )
    namedValues = NamedValues(
        *(("speed115200bps", 115200),
          ("speed1200bps", 1200),
          ("speed19200bps", 19200),
          ("speed230400bps", 230400),
          ("speed2400bps", 2400),
          ("speed300bps", 300),
          ("speed38400bps", 38400),
          ("speed460800bps", 460800),
          ("speed4800bps", 4800),
          ("speed57600bps", 57600),
          ("speed600bps", 600),
          ("speed9600bps", 9600))
    )





class SerialPortSignalState(Integer32):
    """Custom type SerialPortSignalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )





class SerialPortPinOut(Integer32):
    """Custom type SerialPortPinOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 2),
          ("cyclades", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcsProducts_ObjectIdentity = ObjectIdentity
acsProducts = _AcsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1)
)
_Acs6016_ObjectIdentity = ObjectIdentity
acs6016 = _Acs6016_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1, 1)
)
_Acs6032_ObjectIdentity = ObjectIdentity
acs6032 = _Acs6032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1, 2)
)
_Acs6048_ObjectIdentity = ObjectIdentity
acs6048 = _Acs6048_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1, 3)
)
_Acs6004_ObjectIdentity = ObjectIdentity
acs6004 = _Acs6004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1, 4)
)
_Acs6008_ObjectIdentity = ObjectIdentity
acs6008 = _Acs6008_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 1, 5)
)
_AcsManagement_ObjectIdentity = ObjectIdentity
acsManagement = _AcsManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2)
)
_AcsAppliance_ObjectIdentity = ObjectIdentity
acsAppliance = _AcsAppliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1)
)


class _AcsHostName_Type(DisplayString):
    """Custom type acsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsHostName_Type.__name__ = "DisplayString"
_AcsHostName_Object = MibScalar
acsHostName = _AcsHostName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 1),
    _AcsHostName_Type()
)
acsHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsHostName.setStatus("current")


class _AcsProductModel_Type(DisplayString):
    """Custom type acsProductModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcsProductModel_Type.__name__ = "DisplayString"
_AcsProductModel_Object = MibScalar
acsProductModel = _AcsProductModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 2),
    _AcsProductModel_Type()
)
acsProductModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsProductModel.setStatus("current")


class _AcsPartNumber_Type(DisplayString):
    """Custom type acsPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsPartNumber_Type.__name__ = "DisplayString"
_AcsPartNumber_Object = MibScalar
acsPartNumber = _AcsPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 3),
    _AcsPartNumber_Type()
)
acsPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPartNumber.setStatus("current")


class _AcsSerialNumber_Type(DisplayString):
    """Custom type acsSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsSerialNumber_Type.__name__ = "DisplayString"
_AcsSerialNumber_Object = MibScalar
acsSerialNumber = _AcsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 4),
    _AcsSerialNumber_Type()
)
acsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialNumber.setStatus("current")


class _AcsEIDNumber_Type(DisplayString):
    """Custom type acsEIDNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsEIDNumber_Type.__name__ = "DisplayString"
_AcsEIDNumber_Object = MibScalar
acsEIDNumber = _AcsEIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 5),
    _AcsEIDNumber_Type()
)
acsEIDNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsEIDNumber.setStatus("current")


class _AcsBootcodeVersion_Type(DisplayString):
    """Custom type acsBootcodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsBootcodeVersion_Type.__name__ = "DisplayString"
_AcsBootcodeVersion_Object = MibScalar
acsBootcodeVersion = _AcsBootcodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 6),
    _AcsBootcodeVersion_Type()
)
acsBootcodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsBootcodeVersion.setStatus("current")


class _AcsFirmwareVersion_Type(DisplayString):
    """Custom type acsFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsFirmwareVersion_Type.__name__ = "DisplayString"
_AcsFirmwareVersion_Object = MibScalar
acsFirmwareVersion = _AcsFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 7),
    _AcsFirmwareVersion_Type()
)
acsFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsFirmwareVersion.setStatus("current")
_AcsPowerSupply_ObjectIdentity = ObjectIdentity
acsPowerSupply = _AcsPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 8)
)
if mibBuilder.loadTexts:
    acsPowerSupply.setStatus("current")
_AcsPowerSupplyNumber_Type = Integer32
_AcsPowerSupplyNumber_Object = MibScalar
acsPowerSupplyNumber = _AcsPowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 8, 1),
    _AcsPowerSupplyNumber_Type()
)
acsPowerSupplyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyNumber.setStatus("current")
_AcsPowerSupplyStatePw1_Type = PowerSupplyState
_AcsPowerSupplyStatePw1_Object = MibScalar
acsPowerSupplyStatePw1 = _AcsPowerSupplyStatePw1_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 8, 2),
    _AcsPowerSupplyStatePw1_Type()
)
acsPowerSupplyStatePw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyStatePw1.setStatus("current")
_AcsPowerSupplyStatePw2_Type = PowerSupplyState
_AcsPowerSupplyStatePw2_Object = MibScalar
acsPowerSupplyStatePw2 = _AcsPowerSupplyStatePw2_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 8, 3),
    _AcsPowerSupplyStatePw2_Type()
)
acsPowerSupplyStatePw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerSupplyStatePw2.setStatus("current")


class _AcsReboot_Type(Integer32):
    """Custom type acsReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reboot", 2))
    )


_AcsReboot_Type.__name__ = "Integer32"
_AcsReboot_Object = MibScalar
acsReboot = _AcsReboot_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 1, 9),
    _AcsReboot_Type()
)
acsReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsReboot.setStatus("current")
_AcsSessions_ObjectIdentity = ObjectIdentity
acsSessions = _AcsSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2)
)
_AcsActiveSessionsNumberOfSession_Type = Integer32
_AcsActiveSessionsNumberOfSession_Object = MibScalar
acsActiveSessionsNumberOfSession = _AcsActiveSessionsNumberOfSession_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 1),
    _AcsActiveSessionsNumberOfSession_Type()
)
acsActiveSessionsNumberOfSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsNumberOfSession.setStatus("current")
_AcsActiveSessionsTable_Object = MibTable
acsActiveSessionsTable = _AcsActiveSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2)
)
if mibBuilder.loadTexts:
    acsActiveSessionsTable.setStatus("current")
_AcsActiveSessionsTableEntry_Object = MibTableRow
acsActiveSessionsTableEntry = _AcsActiveSessionsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1)
)
acsActiveSessionsTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsActiveSessionsTableIndex"),
)
if mibBuilder.loadTexts:
    acsActiveSessionsTableEntry.setStatus("current")
_AcsActiveSessionsTableIndex_Type = InterfaceIndexOrZero
_AcsActiveSessionsTableIndex_Object = MibTableColumn
acsActiveSessionsTableIndex = _AcsActiveSessionsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 1),
    _AcsActiveSessionsTableIndex_Type()
)
acsActiveSessionsTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableIndex.setStatus("current")


class _AcsActiveSessionsTableUser_Type(DisplayString):
    """Custom type acsActiveSessionsTableUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableUser_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableUser_Object = MibTableColumn
acsActiveSessionsTableUser = _AcsActiveSessionsTableUser_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 2),
    _AcsActiveSessionsTableUser_Type()
)
acsActiveSessionsTableUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableUser.setStatus("current")


class _AcsActiveSessionsTableGroup_Type(DisplayString):
    """Custom type acsActiveSessionsTableGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableGroup_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableGroup_Object = MibTableColumn
acsActiveSessionsTableGroup = _AcsActiveSessionsTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 3),
    _AcsActiveSessionsTableGroup_Type()
)
acsActiveSessionsTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableGroup.setStatus("current")


class _AcsActiveSessionsTableType_Type(DisplayString):
    """Custom type acsActiveSessionsTableType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableType_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableType_Object = MibTableColumn
acsActiveSessionsTableType = _AcsActiveSessionsTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 4),
    _AcsActiveSessionsTableType_Type()
)
acsActiveSessionsTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableType.setStatus("current")


class _AcsActiveSessionsTableConnection_Type(DisplayString):
    """Custom type acsActiveSessionsTableConnection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableConnection_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableConnection_Object = MibTableColumn
acsActiveSessionsTableConnection = _AcsActiveSessionsTableConnection_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 5),
    _AcsActiveSessionsTableConnection_Type()
)
acsActiveSessionsTableConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableConnection.setStatus("current")


class _AcsActiveSessionsTableSessionTime_Type(DisplayString):
    """Custom type acsActiveSessionsTableSessionTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableSessionTime_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableSessionTime_Object = MibTableColumn
acsActiveSessionsTableSessionTime = _AcsActiveSessionsTableSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 6),
    _AcsActiveSessionsTableSessionTime_Type()
)
acsActiveSessionsTableSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableSessionTime.setStatus("current")


class _AcsActiveSessionsTableFrom_Type(DisplayString):
    """Custom type acsActiveSessionsTableFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcsActiveSessionsTableFrom_Type.__name__ = "DisplayString"
_AcsActiveSessionsTableFrom_Object = MibTableColumn
acsActiveSessionsTableFrom = _AcsActiveSessionsTableFrom_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 7),
    _AcsActiveSessionsTableFrom_Type()
)
acsActiveSessionsTableFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsActiveSessionsTableFrom.setStatus("current")


class _AcsActiveSessionsTableKill_Type(Integer32):
    """Custom type acsActiveSessionsTableKill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("killSession", 2),
          ("noAction", 1))
    )


_AcsActiveSessionsTableKill_Type.__name__ = "Integer32"
_AcsActiveSessionsTableKill_Object = MibTableColumn
acsActiveSessionsTableKill = _AcsActiveSessionsTableKill_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 2, 2, 1, 8),
    _AcsActiveSessionsTableKill_Type()
)
acsActiveSessionsTableKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsActiveSessionsTableKill.setStatus("current")
_AcsSerialPort_ObjectIdentity = ObjectIdentity
acsSerialPort = _AcsSerialPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3)
)
_AcsSerialPortNumberOfPorts_Type = Integer32
_AcsSerialPortNumberOfPorts_Object = MibScalar
acsSerialPortNumberOfPorts = _AcsSerialPortNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 1),
    _AcsSerialPortNumberOfPorts_Type()
)
acsSerialPortNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortNumberOfPorts.setStatus("current")
_AcsSerialPortTable_Object = MibTable
acsSerialPortTable = _AcsSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2)
)
if mibBuilder.loadTexts:
    acsSerialPortTable.setStatus("current")
_AcsSerialPortTableEntry_Object = MibTableRow
acsSerialPortTableEntry = _AcsSerialPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1)
)
acsSerialPortTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsSerialPortTableNumber"),
)
if mibBuilder.loadTexts:
    acsSerialPortTableEntry.setStatus("current")


class _AcsSerialPortTableNumber_Type(Integer32):
    """Custom type acsSerialPortTableNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 49),
    )


_AcsSerialPortTableNumber_Type.__name__ = "Integer32"
_AcsSerialPortTableNumber_Object = MibTableColumn
acsSerialPortTableNumber = _AcsSerialPortTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 1),
    _AcsSerialPortTableNumber_Type()
)
acsSerialPortTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableNumber.setStatus("current")


class _AcsSerialPortTableDeviceName_Type(DisplayString):
    """Custom type acsSerialPortTableDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsSerialPortTableDeviceName_Type.__name__ = "DisplayString"
_AcsSerialPortTableDeviceName_Object = MibTableColumn
acsSerialPortTableDeviceName = _AcsSerialPortTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 2),
    _AcsSerialPortTableDeviceName_Type()
)
acsSerialPortTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableDeviceName.setStatus("current")


class _AcsSerialPortTableStatus_Type(Integer32):
    """Custom type acsSerialPortTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("idle", 2),
          ("inUse", 3))
    )


_AcsSerialPortTableStatus_Type.__name__ = "Integer32"
_AcsSerialPortTableStatus_Object = MibTableColumn
acsSerialPortTableStatus = _AcsSerialPortTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 3),
    _AcsSerialPortTableStatus_Type()
)
acsSerialPortTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableStatus.setStatus("current")


class _AcsSerialPortTableName_Type(DisplayString):
    """Custom type acsSerialPortTableName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_AcsSerialPortTableName_Type.__name__ = "DisplayString"
_AcsSerialPortTableName_Object = MibTableColumn
acsSerialPortTableName = _AcsSerialPortTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 4),
    _AcsSerialPortTableName_Type()
)
acsSerialPortTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableName.setStatus("current")


class _AcsSerialPortTableProfile_Type(Integer32):
    """Custom type acsSerialPortTableProfile based on Integer32"""
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
        *(("casProfile", 1),
          ("dialInProfile", 3),
          ("powerProfile", 4),
          ("tsProfile", 2))
    )


_AcsSerialPortTableProfile_Type.__name__ = "Integer32"
_AcsSerialPortTableProfile_Object = MibTableColumn
acsSerialPortTableProfile = _AcsSerialPortTableProfile_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 5),
    _AcsSerialPortTableProfile_Type()
)
acsSerialPortTableProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableProfile.setStatus("current")
_AcsSerialPortTablePinOut_Type = SerialPortPinOut
_AcsSerialPortTablePinOut_Object = MibTableColumn
acsSerialPortTablePinOut = _AcsSerialPortTablePinOut_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 6),
    _AcsSerialPortTablePinOut_Type()
)
acsSerialPortTablePinOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTablePinOut.setStatus("current")
_AcsSerialPortTableComSpeed_Type = SerialPortSpeed
_AcsSerialPortTableComSpeed_Object = MibTableColumn
acsSerialPortTableComSpeed = _AcsSerialPortTableComSpeed_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 7),
    _AcsSerialPortTableComSpeed_Type()
)
acsSerialPortTableComSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComSpeed.setStatus("current")


class _AcsSerialPortTableComParity_Type(Integer32):
    """Custom type acsSerialPortTableComParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_AcsSerialPortTableComParity_Type.__name__ = "Integer32"
_AcsSerialPortTableComParity_Object = MibTableColumn
acsSerialPortTableComParity = _AcsSerialPortTableComParity_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 8),
    _AcsSerialPortTableComParity_Type()
)
acsSerialPortTableComParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComParity.setStatus("current")
_AcsSerialPortTableComDataSize_Type = Integer32
_AcsSerialPortTableComDataSize_Object = MibTableColumn
acsSerialPortTableComDataSize = _AcsSerialPortTableComDataSize_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 9),
    _AcsSerialPortTableComDataSize_Type()
)
acsSerialPortTableComDataSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComDataSize.setStatus("current")
_AcsSerialPortTableComStopBits_Type = Integer32
_AcsSerialPortTableComStopBits_Object = MibTableColumn
acsSerialPortTableComStopBits = _AcsSerialPortTableComStopBits_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 10),
    _AcsSerialPortTableComStopBits_Type()
)
acsSerialPortTableComStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComStopBits.setStatus("current")


class _AcsSerialPortTableComFlowControl_Type(Integer32):
    """Custom type acsSerialPortTableComFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 2),
          ("none", 1),
          ("software", 3))
    )


_AcsSerialPortTableComFlowControl_Type.__name__ = "Integer32"
_AcsSerialPortTableComFlowControl_Object = MibTableColumn
acsSerialPortTableComFlowControl = _AcsSerialPortTableComFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 11),
    _AcsSerialPortTableComFlowControl_Type()
)
acsSerialPortTableComFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableComFlowControl.setStatus("current")
_AcsSerialPortTableSignalStateDTR_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateDTR_Object = MibTableColumn
acsSerialPortTableSignalStateDTR = _AcsSerialPortTableSignalStateDTR_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 12),
    _AcsSerialPortTableSignalStateDTR_Type()
)
acsSerialPortTableSignalStateDTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateDTR.setStatus("current")
_AcsSerialPortTableSignalStateDCD_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateDCD_Object = MibTableColumn
acsSerialPortTableSignalStateDCD = _AcsSerialPortTableSignalStateDCD_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 13),
    _AcsSerialPortTableSignalStateDCD_Type()
)
acsSerialPortTableSignalStateDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateDCD.setStatus("current")
_AcsSerialPortTableSignalStateRTS_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateRTS_Object = MibTableColumn
acsSerialPortTableSignalStateRTS = _AcsSerialPortTableSignalStateRTS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 14),
    _AcsSerialPortTableSignalStateRTS_Type()
)
acsSerialPortTableSignalStateRTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateRTS.setStatus("current")
_AcsSerialPortTableSignalStateCTS_Type = SerialPortSignalState
_AcsSerialPortTableSignalStateCTS_Object = MibTableColumn
acsSerialPortTableSignalStateCTS = _AcsSerialPortTableSignalStateCTS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 15),
    _AcsSerialPortTableSignalStateCTS_Type()
)
acsSerialPortTableSignalStateCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableSignalStateCTS.setStatus("current")
_AcsSerialPortTableTxBytes_Type = Integer32
_AcsSerialPortTableTxBytes_Object = MibTableColumn
acsSerialPortTableTxBytes = _AcsSerialPortTableTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 16),
    _AcsSerialPortTableTxBytes_Type()
)
acsSerialPortTableTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableTxBytes.setStatus("current")
_AcsSerialPortTableRxBytes_Type = Integer32
_AcsSerialPortTableRxBytes_Object = MibTableColumn
acsSerialPortTableRxBytes = _AcsSerialPortTableRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 17),
    _AcsSerialPortTableRxBytes_Type()
)
acsSerialPortTableRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableRxBytes.setStatus("current")
_AcsSerialPortTableFrameError_Type = Integer32
_AcsSerialPortTableFrameError_Object = MibTableColumn
acsSerialPortTableFrameError = _AcsSerialPortTableFrameError_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 18),
    _AcsSerialPortTableFrameError_Type()
)
acsSerialPortTableFrameError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableFrameError.setStatus("current")
_AcsSerialPortTableParityError_Type = Integer32
_AcsSerialPortTableParityError_Object = MibTableColumn
acsSerialPortTableParityError = _AcsSerialPortTableParityError_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 19),
    _AcsSerialPortTableParityError_Type()
)
acsSerialPortTableParityError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableParityError.setStatus("current")
_AcsSerialPortTableBreak_Type = Integer32
_AcsSerialPortTableBreak_Object = MibTableColumn
acsSerialPortTableBreak = _AcsSerialPortTableBreak_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 20),
    _AcsSerialPortTableBreak_Type()
)
acsSerialPortTableBreak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableBreak.setStatus("current")
_AcsSerialPortTableOverrun_Type = Integer32
_AcsSerialPortTableOverrun_Object = MibTableColumn
acsSerialPortTableOverrun = _AcsSerialPortTableOverrun_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 3, 2, 1, 21),
    _AcsSerialPortTableOverrun_Type()
)
acsSerialPortTableOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsSerialPortTableOverrun.setStatus("current")
_AcsPowerMgmt_ObjectIdentity = ObjectIdentity
acsPowerMgmt = _AcsPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5)
)
_AcsPowerMgmtNumSerialPorts_Type = Integer32
_AcsPowerMgmtNumSerialPorts_Object = MibScalar
acsPowerMgmtNumSerialPorts = _AcsPowerMgmtNumSerialPorts_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 1),
    _AcsPowerMgmtNumSerialPorts_Type()
)
acsPowerMgmtNumSerialPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtNumSerialPorts.setStatus("current")
_AcsPowerMgmtSerialTable_Object = MibTable
acsPowerMgmtSerialTable = _AcsPowerMgmtSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2)
)
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTable.setStatus("current")
_AcsPowerMgmtSerialTableEntry_Object = MibTableRow
acsPowerMgmtSerialTableEntry = _AcsPowerMgmtSerialTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2, 1)
)
acsPowerMgmtSerialTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtSerialTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableEntry.setStatus("current")
_AcsPowerMgmtSerialTableIndex_Type = InterfaceIndex
_AcsPowerMgmtSerialTableIndex_Object = MibTableColumn
acsPowerMgmtSerialTableIndex = _AcsPowerMgmtSerialTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2, 1, 1),
    _AcsPowerMgmtSerialTableIndex_Type()
)
acsPowerMgmtSerialTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableIndex.setStatus("current")
_AcsPowerMgmtSerialTablePortNumber_Type = Integer32
_AcsPowerMgmtSerialTablePortNumber_Object = MibTableColumn
acsPowerMgmtSerialTablePortNumber = _AcsPowerMgmtSerialTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2, 1, 2),
    _AcsPowerMgmtSerialTablePortNumber_Type()
)
acsPowerMgmtSerialTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTablePortNumber.setStatus("current")
_AcsPowerMgmtSerialTableDeviceName_Type = DisplayString
_AcsPowerMgmtSerialTableDeviceName_Object = MibTableColumn
acsPowerMgmtSerialTableDeviceName = _AcsPowerMgmtSerialTableDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2, 1, 3),
    _AcsPowerMgmtSerialTableDeviceName_Type()
)
acsPowerMgmtSerialTableDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableDeviceName.setStatus("current")
_AcsPowerMgmtSerialTableNumberPDUs_Type = Integer32
_AcsPowerMgmtSerialTableNumberPDUs_Object = MibTableColumn
acsPowerMgmtSerialTableNumberPDUs = _AcsPowerMgmtSerialTableNumberPDUs_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 2, 1, 4),
    _AcsPowerMgmtSerialTableNumberPDUs_Type()
)
acsPowerMgmtSerialTableNumberPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtSerialTableNumberPDUs.setStatus("current")
_AcsPowerMgmtPDUTable_Object = MibTable
acsPowerMgmtPDUTable = _AcsPowerMgmtPDUTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3)
)
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTable.setStatus("current")
_AcsPowerMgmtPDUTableEntry_Object = MibTableRow
acsPowerMgmtPDUTableEntry = _AcsPowerMgmtPDUTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1)
)
acsPowerMgmtPDUTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtPDUTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtPDUTablePduIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableEntry.setStatus("current")
_AcsPowerMgmtPDUTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtPDUTablePortNumber_Object = MibTableColumn
acsPowerMgmtPDUTablePortNumber = _AcsPowerMgmtPDUTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 1),
    _AcsPowerMgmtPDUTablePortNumber_Type()
)
acsPowerMgmtPDUTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePortNumber.setStatus("current")
_AcsPowerMgmtPDUTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPDUTablePduIndex_Object = MibTableColumn
acsPowerMgmtPDUTablePduIndex = _AcsPowerMgmtPDUTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 2),
    _AcsPowerMgmtPDUTablePduIndex_Type()
)
acsPowerMgmtPDUTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduIndex.setStatus("current")
_AcsPowerMgmtPDUTablePduId_Type = DisplayString
_AcsPowerMgmtPDUTablePduId_Object = MibTableColumn
acsPowerMgmtPDUTablePduId = _AcsPowerMgmtPDUTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 3),
    _AcsPowerMgmtPDUTablePduId_Type()
)
acsPowerMgmtPDUTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePduId.setStatus("current")
_AcsPowerMgmtPDUTablePortName_Type = DisplayString
_AcsPowerMgmtPDUTablePortName_Object = MibTableColumn
acsPowerMgmtPDUTablePortName = _AcsPowerMgmtPDUTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 4),
    _AcsPowerMgmtPDUTablePortName_Type()
)
acsPowerMgmtPDUTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePortName.setStatus("current")
_AcsPowerMgmtPDUTableModel_Type = DisplayString
_AcsPowerMgmtPDUTableModel_Object = MibTableColumn
acsPowerMgmtPDUTableModel = _AcsPowerMgmtPDUTableModel_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 5),
    _AcsPowerMgmtPDUTableModel_Type()
)
acsPowerMgmtPDUTableModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableModel.setStatus("current")
_AcsPowerMgmtPDUTableVendor_Type = DisplayString
_AcsPowerMgmtPDUTableVendor_Object = MibTableColumn
acsPowerMgmtPDUTableVendor = _AcsPowerMgmtPDUTableVendor_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 6),
    _AcsPowerMgmtPDUTableVendor_Type()
)
acsPowerMgmtPDUTableVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVendor.setStatus("current")
_AcsPowerMgmtPDUTableFirmwareVersion_Type = DisplayString
_AcsPowerMgmtPDUTableFirmwareVersion_Object = MibTableColumn
acsPowerMgmtPDUTableFirmwareVersion = _AcsPowerMgmtPDUTableFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 7),
    _AcsPowerMgmtPDUTableFirmwareVersion_Type()
)
acsPowerMgmtPDUTableFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableFirmwareVersion.setStatus("current")
_AcsPowerMgmtPDUTableNumberOfOutlets_Type = Integer32
_AcsPowerMgmtPDUTableNumberOfOutlets_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfOutlets = _AcsPowerMgmtPDUTableNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 8),
    _AcsPowerMgmtPDUTableNumberOfOutlets_Type()
)
acsPowerMgmtPDUTableNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfOutlets.setStatus("current")
_AcsPowerMgmtPDUTableCurrentNOS_Type = Integer32
_AcsPowerMgmtPDUTableCurrentNOS_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentNOS = _AcsPowerMgmtPDUTableCurrentNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 9),
    _AcsPowerMgmtPDUTableCurrentNOS_Type()
)
acsPowerMgmtPDUTableCurrentNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent1Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent1Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent1Value = _AcsPowerMgmtPDUTableCurrent1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 10),
    _AcsPowerMgmtPDUTableCurrent1Value_Type()
)
acsPowerMgmtPDUTableCurrent1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent1Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent1Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent1Max = _AcsPowerMgmtPDUTableCurrent1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 11),
    _AcsPowerMgmtPDUTableCurrent1Max_Type()
)
acsPowerMgmtPDUTableCurrent1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent2Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent2Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent2Value = _AcsPowerMgmtPDUTableCurrent2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 12),
    _AcsPowerMgmtPDUTableCurrent2Value_Type()
)
acsPowerMgmtPDUTableCurrent2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent2Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent2Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent2Max = _AcsPowerMgmtPDUTableCurrent2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 13),
    _AcsPowerMgmtPDUTableCurrent2Max_Type()
)
acsPowerMgmtPDUTableCurrent2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent3Value_Type = Integer32
_AcsPowerMgmtPDUTableCurrent3Value_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent3Value = _AcsPowerMgmtPDUTableCurrent3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 14),
    _AcsPowerMgmtPDUTableCurrent3Value_Type()
)
acsPowerMgmtPDUTableCurrent3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableCurrent3Max_Type = Integer32
_AcsPowerMgmtPDUTableCurrent3Max_Object = MibTableColumn
acsPowerMgmtPDUTableCurrent3Max = _AcsPowerMgmtPDUTableCurrent3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 15),
    _AcsPowerMgmtPDUTableCurrent3Max_Type()
)
acsPowerMgmtPDUTableCurrent3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrent3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperatureNOS_Type = Integer32
_AcsPowerMgmtPDUTableTemperatureNOS_Object = MibTableColumn
acsPowerMgmtPDUTableTemperatureNOS = _AcsPowerMgmtPDUTableTemperatureNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 16),
    _AcsPowerMgmtPDUTableTemperatureNOS_Type()
)
acsPowerMgmtPDUTableTemperatureNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperatureNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature1Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature1Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature1Value = _AcsPowerMgmtPDUTableTemperature1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 17),
    _AcsPowerMgmtPDUTableTemperature1Value_Type()
)
acsPowerMgmtPDUTableTemperature1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature1Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature1Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature1Max = _AcsPowerMgmtPDUTableTemperature1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 18),
    _AcsPowerMgmtPDUTableTemperature1Max_Type()
)
acsPowerMgmtPDUTableTemperature1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature2Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature2Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature2Value = _AcsPowerMgmtPDUTableTemperature2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 19),
    _AcsPowerMgmtPDUTableTemperature2Value_Type()
)
acsPowerMgmtPDUTableTemperature2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature2Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature2Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature2Max = _AcsPowerMgmtPDUTableTemperature2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 20),
    _AcsPowerMgmtPDUTableTemperature2Max_Type()
)
acsPowerMgmtPDUTableTemperature2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature3Value_Type = Integer32
_AcsPowerMgmtPDUTableTemperature3Value_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature3Value = _AcsPowerMgmtPDUTableTemperature3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 21),
    _AcsPowerMgmtPDUTableTemperature3Value_Type()
)
acsPowerMgmtPDUTableTemperature3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableTemperature3Max_Type = Integer32
_AcsPowerMgmtPDUTableTemperature3Max_Object = MibTableColumn
acsPowerMgmtPDUTableTemperature3Max = _AcsPowerMgmtPDUTableTemperature3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 22),
    _AcsPowerMgmtPDUTableTemperature3Max_Type()
)
acsPowerMgmtPDUTableTemperature3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableTemperature3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidityNOS_Type = Integer32
_AcsPowerMgmtPDUTableHumidityNOS_Object = MibTableColumn
acsPowerMgmtPDUTableHumidityNOS = _AcsPowerMgmtPDUTableHumidityNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 23),
    _AcsPowerMgmtPDUTableHumidityNOS_Type()
)
acsPowerMgmtPDUTableHumidityNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidityNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity1Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity1Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity1Value = _AcsPowerMgmtPDUTableHumidity1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 24),
    _AcsPowerMgmtPDUTableHumidity1Value_Type()
)
acsPowerMgmtPDUTableHumidity1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity1Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity1Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity1Max = _AcsPowerMgmtPDUTableHumidity1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 25),
    _AcsPowerMgmtPDUTableHumidity1Max_Type()
)
acsPowerMgmtPDUTableHumidity1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity2Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity2Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity2Value = _AcsPowerMgmtPDUTableHumidity2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 26),
    _AcsPowerMgmtPDUTableHumidity2Value_Type()
)
acsPowerMgmtPDUTableHumidity2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity2Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity2Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity2Max = _AcsPowerMgmtPDUTableHumidity2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 27),
    _AcsPowerMgmtPDUTableHumidity2Max_Type()
)
acsPowerMgmtPDUTableHumidity2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity3Value_Type = Integer32
_AcsPowerMgmtPDUTableHumidity3Value_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity3Value = _AcsPowerMgmtPDUTableHumidity3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 28),
    _AcsPowerMgmtPDUTableHumidity3Value_Type()
)
acsPowerMgmtPDUTableHumidity3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableHumidity3Max_Type = Integer32
_AcsPowerMgmtPDUTableHumidity3Max_Object = MibTableColumn
acsPowerMgmtPDUTableHumidity3Max = _AcsPowerMgmtPDUTableHumidity3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 29),
    _AcsPowerMgmtPDUTableHumidity3Max_Type()
)
acsPowerMgmtPDUTableHumidity3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableHumidity3Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltageNOS_Type = Integer32
_AcsPowerMgmtPDUTableVoltageNOS_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageNOS = _AcsPowerMgmtPDUTableVoltageNOS_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 30),
    _AcsPowerMgmtPDUTableVoltageNOS_Type()
)
acsPowerMgmtPDUTableVoltageNOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageNOS.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage1Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage1Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage1Value = _AcsPowerMgmtPDUTableVoltage1Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 31),
    _AcsPowerMgmtPDUTableVoltage1Value_Type()
)
acsPowerMgmtPDUTableVoltage1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage1Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage1Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage1Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage1Max = _AcsPowerMgmtPDUTableVoltage1Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 32),
    _AcsPowerMgmtPDUTableVoltage1Max_Type()
)
acsPowerMgmtPDUTableVoltage1Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage1Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage2Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage2Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage2Value = _AcsPowerMgmtPDUTableVoltage2Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 33),
    _AcsPowerMgmtPDUTableVoltage2Value_Type()
)
acsPowerMgmtPDUTableVoltage2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage2Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage2Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage2Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage2Max = _AcsPowerMgmtPDUTableVoltage2Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 34),
    _AcsPowerMgmtPDUTableVoltage2Max_Type()
)
acsPowerMgmtPDUTableVoltage2Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage2Max.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage3Value_Type = Integer32
_AcsPowerMgmtPDUTableVoltage3Value_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage3Value = _AcsPowerMgmtPDUTableVoltage3Value_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 35),
    _AcsPowerMgmtPDUTableVoltage3Value_Type()
)
acsPowerMgmtPDUTableVoltage3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage3Value.setStatus("obsolete")
_AcsPowerMgmtPDUTableVoltage3Max_Type = Integer32
_AcsPowerMgmtPDUTableVoltage3Max_Object = MibTableColumn
acsPowerMgmtPDUTableVoltage3Max = _AcsPowerMgmtPDUTableVoltage3Max_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 36),
    _AcsPowerMgmtPDUTableVoltage3Max_Type()
)
acsPowerMgmtPDUTableVoltage3Max.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltage3Max.setStatus("obsolete")


class _AcsPowerMgmtPDUTableNumberOfPhases_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableNumberOfPhases based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("single-phase", 0),
          ("three-phase", 3))
    )


_AcsPowerMgmtPDUTableNumberOfPhases_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableNumberOfPhases_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfPhases = _AcsPowerMgmtPDUTableNumberOfPhases_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 37),
    _AcsPowerMgmtPDUTableNumberOfPhases_Type()
)
acsPowerMgmtPDUTableNumberOfPhases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfPhases.setStatus("current")
_AcsPowerMgmtPDUTableNumberOfBanks_Type = Integer32
_AcsPowerMgmtPDUTableNumberOfBanks_Object = MibTableColumn
acsPowerMgmtPDUTableNumberOfBanks = _AcsPowerMgmtPDUTableNumberOfBanks_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 38),
    _AcsPowerMgmtPDUTableNumberOfBanks_Type()
)
acsPowerMgmtPDUTableNumberOfBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableNumberOfBanks.setStatus("current")
_AcsPowerMgmtPDUTableCurrentValue_Type = Integer32
_AcsPowerMgmtPDUTableCurrentValue_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentValue = _AcsPowerMgmtPDUTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 39),
    _AcsPowerMgmtPDUTableCurrentValue_Type()
)
acsPowerMgmtPDUTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentValue.setStatus("current")
_AcsPowerMgmtPDUTableCurrentMax_Type = Integer32
_AcsPowerMgmtPDUTableCurrentMax_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentMax = _AcsPowerMgmtPDUTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 40),
    _AcsPowerMgmtPDUTableCurrentMax_Type()
)
acsPowerMgmtPDUTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentMax.setStatus("current")
_AcsPowerMgmtPDUTableCurrentMin_Type = Integer32
_AcsPowerMgmtPDUTableCurrentMin_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentMin = _AcsPowerMgmtPDUTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 41),
    _AcsPowerMgmtPDUTableCurrentMin_Type()
)
acsPowerMgmtPDUTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentMin.setStatus("current")
_AcsPowerMgmtPDUTableCurrentAvg_Type = Integer32
_AcsPowerMgmtPDUTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentAvg = _AcsPowerMgmtPDUTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 42),
    _AcsPowerMgmtPDUTableCurrentAvg_Type()
)
acsPowerMgmtPDUTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtPDUTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableCurrentReset_Object = MibTableColumn
acsPowerMgmtPDUTableCurrentReset = _AcsPowerMgmtPDUTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 43),
    _AcsPowerMgmtPDUTableCurrentReset_Type()
)
acsPowerMgmtPDUTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableCurrentReset.setStatus("current")


class _AcsPowerMgmtPDUTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPDUTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableVoltageType_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageType = _AcsPowerMgmtPDUTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 44),
    _AcsPowerMgmtPDUTableVoltageType_Type()
)
acsPowerMgmtPDUTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageType.setStatus("current")
_AcsPowerMgmtPDUTableVoltageValue_Type = Integer32
_AcsPowerMgmtPDUTableVoltageValue_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageValue = _AcsPowerMgmtPDUTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 45),
    _AcsPowerMgmtPDUTableVoltageValue_Type()
)
acsPowerMgmtPDUTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageValue.setStatus("current")
_AcsPowerMgmtPDUTableVoltageMax_Type = Integer32
_AcsPowerMgmtPDUTableVoltageMax_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageMax = _AcsPowerMgmtPDUTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 46),
    _AcsPowerMgmtPDUTableVoltageMax_Type()
)
acsPowerMgmtPDUTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageMax.setStatus("current")
_AcsPowerMgmtPDUTableVoltageMin_Type = Integer32
_AcsPowerMgmtPDUTableVoltageMin_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageMin = _AcsPowerMgmtPDUTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 47),
    _AcsPowerMgmtPDUTableVoltageMin_Type()
)
acsPowerMgmtPDUTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageMin.setStatus("current")
_AcsPowerMgmtPDUTableVoltageAvg_Type = Integer32
_AcsPowerMgmtPDUTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageAvg = _AcsPowerMgmtPDUTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 48),
    _AcsPowerMgmtPDUTableVoltageAvg_Type()
)
acsPowerMgmtPDUTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtPDUTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableVoltageReset_Object = MibTableColumn
acsPowerMgmtPDUTableVoltageReset = _AcsPowerMgmtPDUTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 49),
    _AcsPowerMgmtPDUTableVoltageReset_Type()
)
acsPowerMgmtPDUTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableVoltageReset.setStatus("current")


class _AcsPowerMgmtPDUTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPDUTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerType_Object = MibTableColumn
acsPowerMgmtPDUTablePowerType = _AcsPowerMgmtPDUTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 50),
    _AcsPowerMgmtPDUTablePowerType_Type()
)
acsPowerMgmtPDUTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerType.setStatus("current")
_AcsPowerMgmtPDUTablePowerValue_Type = Integer32
_AcsPowerMgmtPDUTablePowerValue_Object = MibTableColumn
acsPowerMgmtPDUTablePowerValue = _AcsPowerMgmtPDUTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 51),
    _AcsPowerMgmtPDUTablePowerValue_Type()
)
acsPowerMgmtPDUTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerValue.setStatus("current")
_AcsPowerMgmtPDUTablePowerMax_Type = Integer32
_AcsPowerMgmtPDUTablePowerMax_Object = MibTableColumn
acsPowerMgmtPDUTablePowerMax = _AcsPowerMgmtPDUTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 52),
    _AcsPowerMgmtPDUTablePowerMax_Type()
)
acsPowerMgmtPDUTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerMax.setStatus("current")
_AcsPowerMgmtPDUTablePowerMin_Type = Integer32
_AcsPowerMgmtPDUTablePowerMin_Object = MibTableColumn
acsPowerMgmtPDUTablePowerMin = _AcsPowerMgmtPDUTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 53),
    _AcsPowerMgmtPDUTablePowerMin_Type()
)
acsPowerMgmtPDUTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerMin.setStatus("current")
_AcsPowerMgmtPDUTablePowerAvg_Type = Integer32
_AcsPowerMgmtPDUTablePowerAvg_Object = MibTableColumn
acsPowerMgmtPDUTablePowerAvg = _AcsPowerMgmtPDUTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 54),
    _AcsPowerMgmtPDUTablePowerAvg_Type()
)
acsPowerMgmtPDUTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerAvg.setStatus("current")


class _AcsPowerMgmtPDUTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerReset_Object = MibTableColumn
acsPowerMgmtPDUTablePowerReset = _AcsPowerMgmtPDUTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 55),
    _AcsPowerMgmtPDUTablePowerReset_Type()
)
acsPowerMgmtPDUTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerReset.setStatus("current")


class _AcsPowerMgmtPDUTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPDUTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorType = _AcsPowerMgmtPDUTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 56),
    _AcsPowerMgmtPDUTablePowerFactorType_Type()
)
acsPowerMgmtPDUTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorType.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorValue = _AcsPowerMgmtPDUTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 57),
    _AcsPowerMgmtPDUTablePowerFactorValue_Type()
)
acsPowerMgmtPDUTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorMax = _AcsPowerMgmtPDUTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 58),
    _AcsPowerMgmtPDUTablePowerFactorMax_Type()
)
acsPowerMgmtPDUTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorMin = _AcsPowerMgmtPDUTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 59),
    _AcsPowerMgmtPDUTablePowerFactorMin_Type()
)
acsPowerMgmtPDUTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtPDUTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtPDUTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorAvg = _AcsPowerMgmtPDUTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 60),
    _AcsPowerMgmtPDUTablePowerFactorAvg_Type()
)
acsPowerMgmtPDUTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtPDUTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtPDUTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPDUTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtPDUTablePowerFactorReset = _AcsPowerMgmtPDUTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 61),
    _AcsPowerMgmtPDUTablePowerFactorReset_Type()
)
acsPowerMgmtPDUTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtPDUTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtPDUTableAlarm based on Integer32"""
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
        *(("blow-fuse", 2),
          ("high-critical", 4),
          ("high-warning", 5),
          ("hw-ocp", 3),
          ("low-critical", 7),
          ("low-warning", 6),
          ("normal", 1))
    )


_AcsPowerMgmtPDUTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtPDUTableAlarm_Object = MibTableColumn
acsPowerMgmtPDUTableAlarm = _AcsPowerMgmtPDUTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 62),
    _AcsPowerMgmtPDUTableAlarm_Type()
)
acsPowerMgmtPDUTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableAlarm.setStatus("current")
_AcsPowerMgmtPDUTableEnvSensors_Type = Integer32
_AcsPowerMgmtPDUTableEnvSensors_Object = MibTableColumn
acsPowerMgmtPDUTableEnvSensors = _AcsPowerMgmtPDUTableEnvSensors_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 3, 1, 63),
    _AcsPowerMgmtPDUTableEnvSensors_Type()
)
acsPowerMgmtPDUTableEnvSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPDUTableEnvSensors.setStatus("current")
_AcsPowerMgmtTotalNumberOfOutlets_Type = Integer32
_AcsPowerMgmtTotalNumberOfOutlets_Object = MibScalar
acsPowerMgmtTotalNumberOfOutlets = _AcsPowerMgmtTotalNumberOfOutlets_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 4),
    _AcsPowerMgmtTotalNumberOfOutlets_Type()
)
acsPowerMgmtTotalNumberOfOutlets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtTotalNumberOfOutlets.setStatus("current")
_AcsPowerMgmtOutletsTable_Object = MibTable
acsPowerMgmtOutletsTable = _AcsPowerMgmtOutletsTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5)
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTable.setStatus("current")
_AcsPowerMgmtOutletsTableEntry_Object = MibTableRow
acsPowerMgmtOutletsTableEntry = _AcsPowerMgmtOutletsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1)
)
acsPowerMgmtOutletsTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtOutletsTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtOutletsTablePduNumber"),
    (0, "ACS-MIB", "acsPowerMgmtOutletsTableNumber"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableEntry.setStatus("current")
_AcsPowerMgmtOutletsTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTablePortNumber_Object = MibTableColumn
acsPowerMgmtOutletsTablePortNumber = _AcsPowerMgmtOutletsTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 1),
    _AcsPowerMgmtOutletsTablePortNumber_Type()
)
acsPowerMgmtOutletsTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePortNumber.setStatus("current")
_AcsPowerMgmtOutletsTablePduNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTablePduNumber_Object = MibTableColumn
acsPowerMgmtOutletsTablePduNumber = _AcsPowerMgmtOutletsTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 2),
    _AcsPowerMgmtOutletsTablePduNumber_Type()
)
acsPowerMgmtOutletsTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePduNumber.setStatus("current")
_AcsPowerMgmtOutletsTableNumber_Type = InterfaceIndex
_AcsPowerMgmtOutletsTableNumber_Object = MibTableColumn
acsPowerMgmtOutletsTableNumber = _AcsPowerMgmtOutletsTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 3),
    _AcsPowerMgmtOutletsTableNumber_Type()
)
acsPowerMgmtOutletsTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableNumber.setStatus("current")
_AcsPowerMgmtOutletsTableName_Type = DisplayString
_AcsPowerMgmtOutletsTableName_Object = MibTableColumn
acsPowerMgmtOutletsTableName = _AcsPowerMgmtOutletsTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 4),
    _AcsPowerMgmtOutletsTableName_Type()
)
acsPowerMgmtOutletsTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableName.setStatus("current")


class _AcsPowerMgmtOutletsTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtOutletsTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AcsPowerMgmtOutletsTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtOutletsTableStatus_Object = MibTableColumn
acsPowerMgmtOutletsTableStatus = _AcsPowerMgmtOutletsTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 5),
    _AcsPowerMgmtOutletsTableStatus_Type()
)
acsPowerMgmtOutletsTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTableStatus.setStatus("current")


class _AcsPowerMgmtOutletsTablePowerControl_Type(Integer32):
    """Custom type acsPowerMgmtOutletsTablePowerControl based on Integer32"""
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
        *(("noAction", 1),
          ("powerCycle", 4),
          ("powerLock", 5),
          ("powerOff", 3),
          ("powerOn", 2),
          ("powerUnlock", 6))
    )


_AcsPowerMgmtOutletsTablePowerControl_Type.__name__ = "Integer32"
_AcsPowerMgmtOutletsTablePowerControl_Object = MibTableColumn
acsPowerMgmtOutletsTablePowerControl = _AcsPowerMgmtOutletsTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 6),
    _AcsPowerMgmtOutletsTablePowerControl_Type()
)
acsPowerMgmtOutletsTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePowerControl.setStatus("current")
_AcsPowerMgmtOutletsTablePortName_Type = DisplayString
_AcsPowerMgmtOutletsTablePortName_Object = MibTableColumn
acsPowerMgmtOutletsTablePortName = _AcsPowerMgmtOutletsTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 7),
    _AcsPowerMgmtOutletsTablePortName_Type()
)
acsPowerMgmtOutletsTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePortName.setStatus("current")
_AcsPowerMgmtOutletsTablePduId_Type = DisplayString
_AcsPowerMgmtOutletsTablePduId_Object = MibTableColumn
acsPowerMgmtOutletsTablePduId = _AcsPowerMgmtOutletsTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 5, 1, 8),
    _AcsPowerMgmtOutletsTablePduId_Type()
)
acsPowerMgmtOutletsTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutletsTablePduId.setStatus("current")
_AcsPowerMgmtNumberOfOutletGroup_Type = Integer32
_AcsPowerMgmtNumberOfOutletGroup_Object = MibScalar
acsPowerMgmtNumberOfOutletGroup = _AcsPowerMgmtNumberOfOutletGroup_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 6),
    _AcsPowerMgmtNumberOfOutletGroup_Type()
)
acsPowerMgmtNumberOfOutletGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtNumberOfOutletGroup.setStatus("current")
_AcsPowerMgmtGroupTable_Object = MibTable
acsPowerMgmtGroupTable = _AcsPowerMgmtGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7)
)
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTable.setStatus("current")
_AcsPowerMgmtGroupTableEntry_Object = MibTableRow
acsPowerMgmtGroupTableEntry = _AcsPowerMgmtGroupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7, 1)
)
acsPowerMgmtGroupTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtGroupTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableEntry.setStatus("current")
_AcsPowerMgmtGroupTableIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtGroupTableIndex_Object = MibTableColumn
acsPowerMgmtGroupTableIndex = _AcsPowerMgmtGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7, 1, 1),
    _AcsPowerMgmtGroupTableIndex_Type()
)
acsPowerMgmtGroupTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableIndex.setStatus("current")
_AcsPowerMgmtGroupTableName_Type = DisplayString
_AcsPowerMgmtGroupTableName_Object = MibTableColumn
acsPowerMgmtGroupTableName = _AcsPowerMgmtGroupTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7, 1, 2),
    _AcsPowerMgmtGroupTableName_Type()
)
acsPowerMgmtGroupTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableName.setStatus("current")


class _AcsPowerMgmtGroupTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtGroupTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AcsPowerMgmtGroupTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtGroupTableStatus_Object = MibTableColumn
acsPowerMgmtGroupTableStatus = _AcsPowerMgmtGroupTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7, 1, 3),
    _AcsPowerMgmtGroupTableStatus_Type()
)
acsPowerMgmtGroupTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTableStatus.setStatus("current")


class _AcsPowerMgmtGroupTablePowerControl_Type(Integer32):
    """Custom type acsPowerMgmtGroupTablePowerControl based on Integer32"""
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
        *(("noAction", 1),
          ("powerCycle", 4),
          ("powerOff", 3),
          ("powerOn", 2))
    )


_AcsPowerMgmtGroupTablePowerControl_Type.__name__ = "Integer32"
_AcsPowerMgmtGroupTablePowerControl_Object = MibTableColumn
acsPowerMgmtGroupTablePowerControl = _AcsPowerMgmtGroupTablePowerControl_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 7, 1, 4),
    _AcsPowerMgmtGroupTablePowerControl_Type()
)
acsPowerMgmtGroupTablePowerControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtGroupTablePowerControl.setStatus("current")
_AcsPowerMgmtPhasesTable_Object = MibTable
acsPowerMgmtPhasesTable = _AcsPowerMgmtPhasesTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8)
)
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTable.setStatus("current")
_AcsPowerMgmtPhasesTableEntry_Object = MibTableRow
acsPowerMgmtPhasesTableEntry = _AcsPowerMgmtPhasesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1)
)
acsPowerMgmtPhasesTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtPhasesTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtPhasesTablePduIndex"),
    (0, "ACS-MIB", "acsPowerMgmtPhasesTablePhaseIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableEntry.setStatus("current")
_AcsPowerMgmtPhasesTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtPhasesTablePortNumber_Object = MibTableColumn
acsPowerMgmtPhasesTablePortNumber = _AcsPowerMgmtPhasesTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 1),
    _AcsPowerMgmtPhasesTablePortNumber_Type()
)
acsPowerMgmtPhasesTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePortNumber.setStatus("current")
_AcsPowerMgmtPhasesTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPhasesTablePduIndex_Object = MibTableColumn
acsPowerMgmtPhasesTablePduIndex = _AcsPowerMgmtPhasesTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 2),
    _AcsPowerMgmtPhasesTablePduIndex_Type()
)
acsPowerMgmtPhasesTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePduIndex.setStatus("current")
_AcsPowerMgmtPhasesTablePhaseIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtPhasesTablePhaseIndex_Object = MibTableColumn
acsPowerMgmtPhasesTablePhaseIndex = _AcsPowerMgmtPhasesTablePhaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 3),
    _AcsPowerMgmtPhasesTablePhaseIndex_Type()
)
acsPowerMgmtPhasesTablePhaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePhaseIndex.setStatus("current")
_AcsPowerMgmtPhasesTablePhaseName_Type = DisplayString
_AcsPowerMgmtPhasesTablePhaseName_Object = MibTableColumn
acsPowerMgmtPhasesTablePhaseName = _AcsPowerMgmtPhasesTablePhaseName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 4),
    _AcsPowerMgmtPhasesTablePhaseName_Type()
)
acsPowerMgmtPhasesTablePhaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePhaseName.setStatus("current")
_AcsPowerMgmtPhasesTablePduId_Type = DisplayString
_AcsPowerMgmtPhasesTablePduId_Object = MibTableColumn
acsPowerMgmtPhasesTablePduId = _AcsPowerMgmtPhasesTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 5),
    _AcsPowerMgmtPhasesTablePduId_Type()
)
acsPowerMgmtPhasesTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePduId.setStatus("current")
_AcsPowerMgmtPhasesTablePortName_Type = DisplayString
_AcsPowerMgmtPhasesTablePortName_Object = MibTableColumn
acsPowerMgmtPhasesTablePortName = _AcsPowerMgmtPhasesTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 6),
    _AcsPowerMgmtPhasesTablePortName_Type()
)
acsPowerMgmtPhasesTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePortName.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentValue_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentValue_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentValue = _AcsPowerMgmtPhasesTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 7),
    _AcsPowerMgmtPhasesTableCurrentValue_Type()
)
acsPowerMgmtPhasesTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentValue.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentMax_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentMax_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentMax = _AcsPowerMgmtPhasesTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 8),
    _AcsPowerMgmtPhasesTableCurrentMax_Type()
)
acsPowerMgmtPhasesTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentMax.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentMin_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentMin_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentMin = _AcsPowerMgmtPhasesTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 9),
    _AcsPowerMgmtPhasesTableCurrentMin_Type()
)
acsPowerMgmtPhasesTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentMin.setStatus("current")
_AcsPowerMgmtPhasesTableCurrentAvg_Type = Integer32
_AcsPowerMgmtPhasesTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentAvg = _AcsPowerMgmtPhasesTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 10),
    _AcsPowerMgmtPhasesTableCurrentAvg_Type()
)
acsPowerMgmtPhasesTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtPhasesTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableCurrentReset_Object = MibTableColumn
acsPowerMgmtPhasesTableCurrentReset = _AcsPowerMgmtPhasesTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 11),
    _AcsPowerMgmtPhasesTableCurrentReset_Type()
)
acsPowerMgmtPhasesTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableCurrentReset.setStatus("current")


class _AcsPowerMgmtPhasesTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableVoltageType_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageType = _AcsPowerMgmtPhasesTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 12),
    _AcsPowerMgmtPhasesTableVoltageType_Type()
)
acsPowerMgmtPhasesTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageType.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageValue_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageValue_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageValue = _AcsPowerMgmtPhasesTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 13),
    _AcsPowerMgmtPhasesTableVoltageValue_Type()
)
acsPowerMgmtPhasesTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageValue.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageMax_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageMax_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageMax = _AcsPowerMgmtPhasesTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 14),
    _AcsPowerMgmtPhasesTableVoltageMax_Type()
)
acsPowerMgmtPhasesTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageMax.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageMin_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageMin_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageMin = _AcsPowerMgmtPhasesTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 15),
    _AcsPowerMgmtPhasesTableVoltageMin_Type()
)
acsPowerMgmtPhasesTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageMin.setStatus("current")
_AcsPowerMgmtPhasesTableVoltageAvg_Type = Integer32
_AcsPowerMgmtPhasesTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageAvg = _AcsPowerMgmtPhasesTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 16),
    _AcsPowerMgmtPhasesTableVoltageAvg_Type()
)
acsPowerMgmtPhasesTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtPhasesTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableVoltageReset_Object = MibTableColumn
acsPowerMgmtPhasesTableVoltageReset = _AcsPowerMgmtPhasesTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 17),
    _AcsPowerMgmtPhasesTableVoltageReset_Type()
)
acsPowerMgmtPhasesTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableVoltageReset.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerType_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerType = _AcsPowerMgmtPhasesTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 18),
    _AcsPowerMgmtPhasesTablePowerType_Type()
)
acsPowerMgmtPhasesTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerType.setStatus("current")
_AcsPowerMgmtPhasesTablePowerValue_Type = Integer32
_AcsPowerMgmtPhasesTablePowerValue_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerValue = _AcsPowerMgmtPhasesTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 19),
    _AcsPowerMgmtPhasesTablePowerValue_Type()
)
acsPowerMgmtPhasesTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerValue.setStatus("current")
_AcsPowerMgmtPhasesTablePowerMax_Type = Integer32
_AcsPowerMgmtPhasesTablePowerMax_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerMax = _AcsPowerMgmtPhasesTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 20),
    _AcsPowerMgmtPhasesTablePowerMax_Type()
)
acsPowerMgmtPhasesTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerMax.setStatus("current")
_AcsPowerMgmtPhasesTablePowerMin_Type = Integer32
_AcsPowerMgmtPhasesTablePowerMin_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerMin = _AcsPowerMgmtPhasesTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 21),
    _AcsPowerMgmtPhasesTablePowerMin_Type()
)
acsPowerMgmtPhasesTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerMin.setStatus("current")
_AcsPowerMgmtPhasesTablePowerAvg_Type = Integer32
_AcsPowerMgmtPhasesTablePowerAvg_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerAvg = _AcsPowerMgmtPhasesTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 22),
    _AcsPowerMgmtPhasesTablePowerAvg_Type()
)
acsPowerMgmtPhasesTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerAvg.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerReset_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerReset = _AcsPowerMgmtPhasesTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 23),
    _AcsPowerMgmtPhasesTablePowerReset_Type()
)
acsPowerMgmtPhasesTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerReset.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtPhasesTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorType = _AcsPowerMgmtPhasesTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 24),
    _AcsPowerMgmtPhasesTablePowerFactorType_Type()
)
acsPowerMgmtPhasesTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorType.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorValue = _AcsPowerMgmtPhasesTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 25),
    _AcsPowerMgmtPhasesTablePowerFactorValue_Type()
)
acsPowerMgmtPhasesTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorMax = _AcsPowerMgmtPhasesTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 26),
    _AcsPowerMgmtPhasesTablePowerFactorMax_Type()
)
acsPowerMgmtPhasesTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorMin = _AcsPowerMgmtPhasesTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 27),
    _AcsPowerMgmtPhasesTablePowerFactorMin_Type()
)
acsPowerMgmtPhasesTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtPhasesTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtPhasesTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorAvg = _AcsPowerMgmtPhasesTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 28),
    _AcsPowerMgmtPhasesTablePowerFactorAvg_Type()
)
acsPowerMgmtPhasesTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtPhasesTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtPhasesTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtPhasesTablePowerFactorReset = _AcsPowerMgmtPhasesTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 29),
    _AcsPowerMgmtPhasesTablePowerFactorReset_Type()
)
acsPowerMgmtPhasesTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtPhasesTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtPhasesTableAlarm based on Integer32"""
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
        *(("blow-fuse", 2),
          ("high-critical", 4),
          ("high-warning", 5),
          ("hw-ocp", 3),
          ("low-critical", 7),
          ("low-warning", 6),
          ("normal", 1))
    )


_AcsPowerMgmtPhasesTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtPhasesTableAlarm_Object = MibTableColumn
acsPowerMgmtPhasesTableAlarm = _AcsPowerMgmtPhasesTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 8, 1, 30),
    _AcsPowerMgmtPhasesTableAlarm_Type()
)
acsPowerMgmtPhasesTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtPhasesTableAlarm.setStatus("current")
_AcsPowerMgmtBanksTable_Object = MibTable
acsPowerMgmtBanksTable = _AcsPowerMgmtBanksTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9)
)
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTable.setStatus("current")
_AcsPowerMgmtBanksTableEntry_Object = MibTableRow
acsPowerMgmtBanksTableEntry = _AcsPowerMgmtBanksTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1)
)
acsPowerMgmtBanksTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtBanksTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtBanksTablePduIndex"),
    (0, "ACS-MIB", "acsPowerMgmtBanksTableBankIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableEntry.setStatus("current")
_AcsPowerMgmtBanksTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtBanksTablePortNumber_Object = MibTableColumn
acsPowerMgmtBanksTablePortNumber = _AcsPowerMgmtBanksTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 1),
    _AcsPowerMgmtBanksTablePortNumber_Type()
)
acsPowerMgmtBanksTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePortNumber.setStatus("current")
_AcsPowerMgmtBanksTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtBanksTablePduIndex_Object = MibTableColumn
acsPowerMgmtBanksTablePduIndex = _AcsPowerMgmtBanksTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 2),
    _AcsPowerMgmtBanksTablePduIndex_Type()
)
acsPowerMgmtBanksTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePduIndex.setStatus("current")
_AcsPowerMgmtBanksTableBankIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtBanksTableBankIndex_Object = MibTableColumn
acsPowerMgmtBanksTableBankIndex = _AcsPowerMgmtBanksTableBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 3),
    _AcsPowerMgmtBanksTableBankIndex_Type()
)
acsPowerMgmtBanksTableBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableBankIndex.setStatus("current")
_AcsPowerMgmtBanksTableBankName_Type = DisplayString
_AcsPowerMgmtBanksTableBankName_Object = MibTableColumn
acsPowerMgmtBanksTableBankName = _AcsPowerMgmtBanksTableBankName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 4),
    _AcsPowerMgmtBanksTableBankName_Type()
)
acsPowerMgmtBanksTableBankName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableBankName.setStatus("current")
_AcsPowerMgmtBanksTablePduId_Type = DisplayString
_AcsPowerMgmtBanksTablePduId_Object = MibTableColumn
acsPowerMgmtBanksTablePduId = _AcsPowerMgmtBanksTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 5),
    _AcsPowerMgmtBanksTablePduId_Type()
)
acsPowerMgmtBanksTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePduId.setStatus("current")
_AcsPowerMgmtBanksTablePortName_Type = DisplayString
_AcsPowerMgmtBanksTablePortName_Object = MibTableColumn
acsPowerMgmtBanksTablePortName = _AcsPowerMgmtBanksTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 6),
    _AcsPowerMgmtBanksTablePortName_Type()
)
acsPowerMgmtBanksTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePortName.setStatus("current")
_AcsPowerMgmtBanksTableCurrentValue_Type = Integer32
_AcsPowerMgmtBanksTableCurrentValue_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentValue = _AcsPowerMgmtBanksTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 7),
    _AcsPowerMgmtBanksTableCurrentValue_Type()
)
acsPowerMgmtBanksTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentValue.setStatus("current")
_AcsPowerMgmtBanksTableCurrentMax_Type = Integer32
_AcsPowerMgmtBanksTableCurrentMax_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentMax = _AcsPowerMgmtBanksTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 8),
    _AcsPowerMgmtBanksTableCurrentMax_Type()
)
acsPowerMgmtBanksTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentMax.setStatus("current")
_AcsPowerMgmtBanksTableCurrentMin_Type = Integer32
_AcsPowerMgmtBanksTableCurrentMin_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentMin = _AcsPowerMgmtBanksTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 9),
    _AcsPowerMgmtBanksTableCurrentMin_Type()
)
acsPowerMgmtBanksTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentMin.setStatus("current")
_AcsPowerMgmtBanksTableCurrentAvg_Type = Integer32
_AcsPowerMgmtBanksTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentAvg = _AcsPowerMgmtBanksTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 10),
    _AcsPowerMgmtBanksTableCurrentAvg_Type()
)
acsPowerMgmtBanksTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtBanksTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableCurrentReset_Object = MibTableColumn
acsPowerMgmtBanksTableCurrentReset = _AcsPowerMgmtBanksTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 11),
    _AcsPowerMgmtBanksTableCurrentReset_Type()
)
acsPowerMgmtBanksTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableCurrentReset.setStatus("current")


class _AcsPowerMgmtBanksTableVoltageType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableVoltageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtBanksTableVoltageType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableVoltageType_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageType = _AcsPowerMgmtBanksTableVoltageType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 12),
    _AcsPowerMgmtBanksTableVoltageType_Type()
)
acsPowerMgmtBanksTableVoltageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageType.setStatus("current")
_AcsPowerMgmtBanksTableVoltageValue_Type = Integer32
_AcsPowerMgmtBanksTableVoltageValue_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageValue = _AcsPowerMgmtBanksTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 13),
    _AcsPowerMgmtBanksTableVoltageValue_Type()
)
acsPowerMgmtBanksTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageValue.setStatus("current")
_AcsPowerMgmtBanksTableVoltageMax_Type = Integer32
_AcsPowerMgmtBanksTableVoltageMax_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageMax = _AcsPowerMgmtBanksTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 14),
    _AcsPowerMgmtBanksTableVoltageMax_Type()
)
acsPowerMgmtBanksTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageMax.setStatus("current")
_AcsPowerMgmtBanksTableVoltageMin_Type = Integer32
_AcsPowerMgmtBanksTableVoltageMin_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageMin = _AcsPowerMgmtBanksTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 15),
    _AcsPowerMgmtBanksTableVoltageMin_Type()
)
acsPowerMgmtBanksTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageMin.setStatus("current")
_AcsPowerMgmtBanksTableVoltageAvg_Type = Integer32
_AcsPowerMgmtBanksTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageAvg = _AcsPowerMgmtBanksTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 16),
    _AcsPowerMgmtBanksTableVoltageAvg_Type()
)
acsPowerMgmtBanksTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtBanksTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableVoltageReset_Object = MibTableColumn
acsPowerMgmtBanksTableVoltageReset = _AcsPowerMgmtBanksTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 17),
    _AcsPowerMgmtBanksTableVoltageReset_Type()
)
acsPowerMgmtBanksTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableVoltageReset.setStatus("current")


class _AcsPowerMgmtBanksTablePowerType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtBanksTablePowerType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerType_Object = MibTableColumn
acsPowerMgmtBanksTablePowerType = _AcsPowerMgmtBanksTablePowerType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 18),
    _AcsPowerMgmtBanksTablePowerType_Type()
)
acsPowerMgmtBanksTablePowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerType.setStatus("current")
_AcsPowerMgmtBanksTablePowerValue_Type = Integer32
_AcsPowerMgmtBanksTablePowerValue_Object = MibTableColumn
acsPowerMgmtBanksTablePowerValue = _AcsPowerMgmtBanksTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 19),
    _AcsPowerMgmtBanksTablePowerValue_Type()
)
acsPowerMgmtBanksTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerValue.setStatus("current")
_AcsPowerMgmtBanksTablePowerMax_Type = Integer32
_AcsPowerMgmtBanksTablePowerMax_Object = MibTableColumn
acsPowerMgmtBanksTablePowerMax = _AcsPowerMgmtBanksTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 20),
    _AcsPowerMgmtBanksTablePowerMax_Type()
)
acsPowerMgmtBanksTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerMax.setStatus("current")
_AcsPowerMgmtBanksTablePowerMin_Type = Integer32
_AcsPowerMgmtBanksTablePowerMin_Object = MibTableColumn
acsPowerMgmtBanksTablePowerMin = _AcsPowerMgmtBanksTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 21),
    _AcsPowerMgmtBanksTablePowerMin_Type()
)
acsPowerMgmtBanksTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerMin.setStatus("current")
_AcsPowerMgmtBanksTablePowerAvg_Type = Integer32
_AcsPowerMgmtBanksTablePowerAvg_Object = MibTableColumn
acsPowerMgmtBanksTablePowerAvg = _AcsPowerMgmtBanksTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 22),
    _AcsPowerMgmtBanksTablePowerAvg_Type()
)
acsPowerMgmtBanksTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerAvg.setStatus("current")


class _AcsPowerMgmtBanksTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerReset_Object = MibTableColumn
acsPowerMgmtBanksTablePowerReset = _AcsPowerMgmtBanksTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 23),
    _AcsPowerMgmtBanksTablePowerReset_Type()
)
acsPowerMgmtBanksTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerReset.setStatus("current")


class _AcsPowerMgmtBanksTablePowerFactorType_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerFactorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("estimated", 1),
          ("none-sensor", 0),
          ("read", 2))
    )


_AcsPowerMgmtBanksTablePowerFactorType_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerFactorType_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorType = _AcsPowerMgmtBanksTablePowerFactorType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 24),
    _AcsPowerMgmtBanksTablePowerFactorType_Type()
)
acsPowerMgmtBanksTablePowerFactorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorType.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorValue = _AcsPowerMgmtBanksTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 25),
    _AcsPowerMgmtBanksTablePowerFactorValue_Type()
)
acsPowerMgmtBanksTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorMax = _AcsPowerMgmtBanksTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 26),
    _AcsPowerMgmtBanksTablePowerFactorMax_Type()
)
acsPowerMgmtBanksTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorMin = _AcsPowerMgmtBanksTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 27),
    _AcsPowerMgmtBanksTablePowerFactorMin_Type()
)
acsPowerMgmtBanksTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtBanksTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtBanksTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorAvg = _AcsPowerMgmtBanksTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 28),
    _AcsPowerMgmtBanksTablePowerFactorAvg_Type()
)
acsPowerMgmtBanksTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtBanksTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtBanksTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("reset", 2))
    )


_AcsPowerMgmtBanksTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtBanksTablePowerFactorReset = _AcsPowerMgmtBanksTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 29),
    _AcsPowerMgmtBanksTablePowerFactorReset_Type()
)
acsPowerMgmtBanksTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtBanksTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtBanksTableAlarm based on Integer32"""
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
        *(("blow-fuse", 2),
          ("high-critical", 4),
          ("high-warning", 5),
          ("hw-ocp", 3),
          ("low-critical", 7),
          ("low-warning", 6),
          ("normal", 1))
    )


_AcsPowerMgmtBanksTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtBanksTableAlarm_Object = MibTableColumn
acsPowerMgmtBanksTableAlarm = _AcsPowerMgmtBanksTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 9, 1, 30),
    _AcsPowerMgmtBanksTableAlarm_Type()
)
acsPowerMgmtBanksTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtBanksTableAlarm.setStatus("current")
_AcsPowerMgmtEnvMonTable_Object = MibTable
acsPowerMgmtEnvMonTable = _AcsPowerMgmtEnvMonTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10)
)
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTable.setStatus("current")
_AcsPowerMgmtEnvMonTableEntry_Object = MibTableRow
acsPowerMgmtEnvMonTableEntry = _AcsPowerMgmtEnvMonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1)
)
acsPowerMgmtEnvMonTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtEnvMonTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtEnvMonTablePduIndex"),
    (0, "ACS-MIB", "acsPowerMgmtEnvMonTableIndex"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableEntry.setStatus("current")
_AcsPowerMgmtEnvMonTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtEnvMonTablePortNumber_Object = MibTableColumn
acsPowerMgmtEnvMonTablePortNumber = _AcsPowerMgmtEnvMonTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 1),
    _AcsPowerMgmtEnvMonTablePortNumber_Type()
)
acsPowerMgmtEnvMonTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePortNumber.setStatus("current")
_AcsPowerMgmtEnvMonTablePduIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtEnvMonTablePduIndex_Object = MibTableColumn
acsPowerMgmtEnvMonTablePduIndex = _AcsPowerMgmtEnvMonTablePduIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 2),
    _AcsPowerMgmtEnvMonTablePduIndex_Type()
)
acsPowerMgmtEnvMonTablePduIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePduIndex.setStatus("current")
_AcsPowerMgmtEnvMonTableIndex_Type = InterfaceIndexOrZero
_AcsPowerMgmtEnvMonTableIndex_Object = MibTableColumn
acsPowerMgmtEnvMonTableIndex = _AcsPowerMgmtEnvMonTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 3),
    _AcsPowerMgmtEnvMonTableIndex_Type()
)
acsPowerMgmtEnvMonTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableIndex.setStatus("current")
_AcsPowerMgmtEnvMonTableName_Type = DisplayString
_AcsPowerMgmtEnvMonTableName_Object = MibTableColumn
acsPowerMgmtEnvMonTableName = _AcsPowerMgmtEnvMonTableName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 4),
    _AcsPowerMgmtEnvMonTableName_Type()
)
acsPowerMgmtEnvMonTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableName.setStatus("current")
_AcsPowerMgmtEnvMonTablePduId_Type = DisplayString
_AcsPowerMgmtEnvMonTablePduId_Object = MibTableColumn
acsPowerMgmtEnvMonTablePduId = _AcsPowerMgmtEnvMonTablePduId_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 5),
    _AcsPowerMgmtEnvMonTablePduId_Type()
)
acsPowerMgmtEnvMonTablePduId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePduId.setStatus("current")
_AcsPowerMgmtEnvMonTablePortName_Type = DisplayString
_AcsPowerMgmtEnvMonTablePortName_Object = MibTableColumn
acsPowerMgmtEnvMonTablePortName = _AcsPowerMgmtEnvMonTablePortName_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 6),
    _AcsPowerMgmtEnvMonTablePortName_Type()
)
acsPowerMgmtEnvMonTablePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTablePortName.setStatus("current")


class _AcsPowerMgmtEnvMonTableType_Type(Integer32):
    """Custom type acsPowerMgmtEnvMonTableType based on Integer32"""
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
        *(("air-flow", 4),
          ("dry-concact", 6),
          ("humidity", 3),
          ("motion", 8),
          ("smoke", 5),
          ("temp-internal", 1),
          ("temperature", 2),
          ("unknown", 10),
          ("unplugged", 9),
          ("water-level", 7))
    )


_AcsPowerMgmtEnvMonTableType_Type.__name__ = "Integer32"
_AcsPowerMgmtEnvMonTableType_Object = MibTableColumn
acsPowerMgmtEnvMonTableType = _AcsPowerMgmtEnvMonTableType_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 7),
    _AcsPowerMgmtEnvMonTableType_Type()
)
acsPowerMgmtEnvMonTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableType.setStatus("current")


class _AcsPowerMgmtEnvMonTableStatus_Type(Integer32):
    """Custom type acsPowerMgmtEnvMonTableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("not-applicable", 3),
          ("triggered", 2))
    )


_AcsPowerMgmtEnvMonTableStatus_Type.__name__ = "Integer32"
_AcsPowerMgmtEnvMonTableStatus_Object = MibTableColumn
acsPowerMgmtEnvMonTableStatus = _AcsPowerMgmtEnvMonTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 8),
    _AcsPowerMgmtEnvMonTableStatus_Type()
)
acsPowerMgmtEnvMonTableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableStatus.setStatus("current")
_AcsPowerMgmtEnvMonTableValue_Type = Integer32
_AcsPowerMgmtEnvMonTableValue_Object = MibTableColumn
acsPowerMgmtEnvMonTableValue = _AcsPowerMgmtEnvMonTableValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 9),
    _AcsPowerMgmtEnvMonTableValue_Type()
)
acsPowerMgmtEnvMonTableValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableValue.setStatus("current")
_AcsPowerMgmtEnvMonTableMaxValue_Type = Integer32
_AcsPowerMgmtEnvMonTableMaxValue_Object = MibTableColumn
acsPowerMgmtEnvMonTableMaxValue = _AcsPowerMgmtEnvMonTableMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 10, 1, 10),
    _AcsPowerMgmtEnvMonTableMaxValue_Type()
)
acsPowerMgmtEnvMonTableMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtEnvMonTableMaxValue.setStatus("current")
_AcsPowerMgmtOutElecMonTable_Object = MibTable
acsPowerMgmtOutElecMonTable = _AcsPowerMgmtOutElecMonTable_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11)
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTable.setStatus("current")
_AcsPowerMgmtOutElecMonTableEntry_Object = MibTableRow
acsPowerMgmtOutElecMonTableEntry = _AcsPowerMgmtOutElecMonTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1)
)
acsPowerMgmtOutElecMonTableEntry.setIndexNames(
    (0, "ACS-MIB", "acsPowerMgmtOutElecMonTablePortNumber"),
    (0, "ACS-MIB", "acsPowerMgmtOutElecMonTablePduNumber"),
    (0, "ACS-MIB", "acsPowerMgmtOutElecMonTableNumber"),
)
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableEntry.setStatus("current")
_AcsPowerMgmtOutElecMonTablePortNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTablePortNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePortNumber = _AcsPowerMgmtOutElecMonTablePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 1),
    _AcsPowerMgmtOutElecMonTablePortNumber_Type()
)
acsPowerMgmtOutElecMonTablePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePortNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTablePduNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTablePduNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePduNumber = _AcsPowerMgmtOutElecMonTablePduNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 2),
    _AcsPowerMgmtOutElecMonTablePduNumber_Type()
)
acsPowerMgmtOutElecMonTablePduNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePduNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTableNumber_Type = InterfaceIndex
_AcsPowerMgmtOutElecMonTableNumber_Object = MibTableColumn
acsPowerMgmtOutElecMonTableNumber = _AcsPowerMgmtOutElecMonTableNumber_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 3),
    _AcsPowerMgmtOutElecMonTableNumber_Type()
)
acsPowerMgmtOutElecMonTableNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableNumber.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentValue_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentValue = _AcsPowerMgmtOutElecMonTableCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 4),
    _AcsPowerMgmtOutElecMonTableCurrentValue_Type()
)
acsPowerMgmtOutElecMonTableCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentValue.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentMax_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentMax = _AcsPowerMgmtOutElecMonTableCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 5),
    _AcsPowerMgmtOutElecMonTableCurrentMax_Type()
)
acsPowerMgmtOutElecMonTableCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentMax.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentMin_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentMin = _AcsPowerMgmtOutElecMonTableCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 6),
    _AcsPowerMgmtOutElecMonTableCurrentMin_Type()
)
acsPowerMgmtOutElecMonTableCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentMin.setStatus("current")
_AcsPowerMgmtOutElecMonTableCurrentAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTableCurrentAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentAvg = _AcsPowerMgmtOutElecMonTableCurrentAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 7),
    _AcsPowerMgmtOutElecMonTableCurrentAvg_Type()
)
acsPowerMgmtOutElecMonTableCurrentAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTableCurrentReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableCurrentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTableCurrentReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableCurrentReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTableCurrentReset = _AcsPowerMgmtOutElecMonTableCurrentReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 8),
    _AcsPowerMgmtOutElecMonTableCurrentReset_Type()
)
acsPowerMgmtOutElecMonTableCurrentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableCurrentReset.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerValue_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerValue = _AcsPowerMgmtOutElecMonTablePowerValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 9),
    _AcsPowerMgmtOutElecMonTablePowerValue_Type()
)
acsPowerMgmtOutElecMonTablePowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerValue.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerMax_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerMax = _AcsPowerMgmtOutElecMonTablePowerMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 10),
    _AcsPowerMgmtOutElecMonTablePowerMax_Type()
)
acsPowerMgmtOutElecMonTablePowerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerMax.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerMin_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerMin = _AcsPowerMgmtOutElecMonTablePowerMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 11),
    _AcsPowerMgmtOutElecMonTablePowerMin_Type()
)
acsPowerMgmtOutElecMonTablePowerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerMin.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerAvg = _AcsPowerMgmtOutElecMonTablePowerAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 12),
    _AcsPowerMgmtOutElecMonTablePowerAvg_Type()
)
acsPowerMgmtOutElecMonTablePowerAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTablePowerReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTablePowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTablePowerReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTablePowerReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerReset = _AcsPowerMgmtOutElecMonTablePowerReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 13),
    _AcsPowerMgmtOutElecMonTablePowerReset_Type()
)
acsPowerMgmtOutElecMonTablePowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerReset.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageValue_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageValue = _AcsPowerMgmtOutElecMonTableVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 14),
    _AcsPowerMgmtOutElecMonTableVoltageValue_Type()
)
acsPowerMgmtOutElecMonTableVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageValue.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageMax_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageMax = _AcsPowerMgmtOutElecMonTableVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 15),
    _AcsPowerMgmtOutElecMonTableVoltageMax_Type()
)
acsPowerMgmtOutElecMonTableVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageMax.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageMin_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageMin = _AcsPowerMgmtOutElecMonTableVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 16),
    _AcsPowerMgmtOutElecMonTableVoltageMin_Type()
)
acsPowerMgmtOutElecMonTableVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageMin.setStatus("current")
_AcsPowerMgmtOutElecMonTableVoltageAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTableVoltageAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageAvg = _AcsPowerMgmtOutElecMonTableVoltageAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 17),
    _AcsPowerMgmtOutElecMonTableVoltageAvg_Type()
)
acsPowerMgmtOutElecMonTableVoltageAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTableVoltageReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableVoltageReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTableVoltageReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableVoltageReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTableVoltageReset = _AcsPowerMgmtOutElecMonTableVoltageReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 18),
    _AcsPowerMgmtOutElecMonTableVoltageReset_Type()
)
acsPowerMgmtOutElecMonTableVoltageReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableVoltageReset.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorValue_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorValue_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorValue = _AcsPowerMgmtOutElecMonTablePowerFactorValue_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 19),
    _AcsPowerMgmtOutElecMonTablePowerFactorValue_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorValue.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorMax_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorMax_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorMax = _AcsPowerMgmtOutElecMonTablePowerFactorMax_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 20),
    _AcsPowerMgmtOutElecMonTablePowerFactorMax_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorMax.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorMin_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorMin_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorMin = _AcsPowerMgmtOutElecMonTablePowerFactorMin_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 21),
    _AcsPowerMgmtOutElecMonTablePowerFactorMin_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorMin.setStatus("current")
_AcsPowerMgmtOutElecMonTablePowerFactorAvg_Type = Integer32
_AcsPowerMgmtOutElecMonTablePowerFactorAvg_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorAvg = _AcsPowerMgmtOutElecMonTablePowerFactorAvg_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 22),
    _AcsPowerMgmtOutElecMonTablePowerFactorAvg_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorAvg.setStatus("current")


class _AcsPowerMgmtOutElecMonTablePowerFactorReset_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTablePowerFactorReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("reset", 2))
    )


_AcsPowerMgmtOutElecMonTablePowerFactorReset_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTablePowerFactorReset_Object = MibTableColumn
acsPowerMgmtOutElecMonTablePowerFactorReset = _AcsPowerMgmtOutElecMonTablePowerFactorReset_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 23),
    _AcsPowerMgmtOutElecMonTablePowerFactorReset_Type()
)
acsPowerMgmtOutElecMonTablePowerFactorReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTablePowerFactorReset.setStatus("current")


class _AcsPowerMgmtOutElecMonTableAlarm_Type(Integer32):
    """Custom type acsPowerMgmtOutElecMonTableAlarm based on Integer32"""
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
        *(("blow-fuse", 2),
          ("high-critical", 4),
          ("high-warning", 5),
          ("hw-ocp", 3),
          ("low-critical", 7),
          ("low-warning", 6),
          ("normal", 1))
    )


_AcsPowerMgmtOutElecMonTableAlarm_Type.__name__ = "Integer32"
_AcsPowerMgmtOutElecMonTableAlarm_Object = MibTableColumn
acsPowerMgmtOutElecMonTableAlarm = _AcsPowerMgmtOutElecMonTableAlarm_Object(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 5, 11, 1, 24),
    _AcsPowerMgmtOutElecMonTableAlarm_Type()
)
acsPowerMgmtOutElecMonTableAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acsPowerMgmtOutElecMonTableAlarm.setStatus("current")
_AcsTrapObject_ObjectIdentity = ObjectIdentity
acsTrapObject = _AcsTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10418, 16, 2, 6)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACS-MIB",
    **{"PowerSupplyState": PowerSupplyState,
       "SerialPortSpeed": SerialPortSpeed,
       "SerialPortSignalState": SerialPortSignalState,
       "SerialPortPinOut": SerialPortPinOut,
       "acs": acs,
       "acsProducts": acsProducts,
       "acs6016": acs6016,
       "acs6032": acs6032,
       "acs6048": acs6048,
       "acs6004": acs6004,
       "acs6008": acs6008,
       "acsManagement": acsManagement,
       "acsAppliance": acsAppliance,
       "acsHostName": acsHostName,
       "acsProductModel": acsProductModel,
       "acsPartNumber": acsPartNumber,
       "acsSerialNumber": acsSerialNumber,
       "acsEIDNumber": acsEIDNumber,
       "acsBootcodeVersion": acsBootcodeVersion,
       "acsFirmwareVersion": acsFirmwareVersion,
       "acsPowerSupply": acsPowerSupply,
       "acsPowerSupplyNumber": acsPowerSupplyNumber,
       "acsPowerSupplyStatePw1": acsPowerSupplyStatePw1,
       "acsPowerSupplyStatePw2": acsPowerSupplyStatePw2,
       "acsReboot": acsReboot,
       "acsSessions": acsSessions,
       "acsActiveSessionsNumberOfSession": acsActiveSessionsNumberOfSession,
       "acsActiveSessionsTable": acsActiveSessionsTable,
       "acsActiveSessionsTableEntry": acsActiveSessionsTableEntry,
       "acsActiveSessionsTableIndex": acsActiveSessionsTableIndex,
       "acsActiveSessionsTableUser": acsActiveSessionsTableUser,
       "acsActiveSessionsTableGroup": acsActiveSessionsTableGroup,
       "acsActiveSessionsTableType": acsActiveSessionsTableType,
       "acsActiveSessionsTableConnection": acsActiveSessionsTableConnection,
       "acsActiveSessionsTableSessionTime": acsActiveSessionsTableSessionTime,
       "acsActiveSessionsTableFrom": acsActiveSessionsTableFrom,
       "acsActiveSessionsTableKill": acsActiveSessionsTableKill,
       "acsSerialPort": acsSerialPort,
       "acsSerialPortNumberOfPorts": acsSerialPortNumberOfPorts,
       "acsSerialPortTable": acsSerialPortTable,
       "acsSerialPortTableEntry": acsSerialPortTableEntry,
       "acsSerialPortTableNumber": acsSerialPortTableNumber,
       "acsSerialPortTableDeviceName": acsSerialPortTableDeviceName,
       "acsSerialPortTableStatus": acsSerialPortTableStatus,
       "acsSerialPortTableName": acsSerialPortTableName,
       "acsSerialPortTableProfile": acsSerialPortTableProfile,
       "acsSerialPortTablePinOut": acsSerialPortTablePinOut,
       "acsSerialPortTableComSpeed": acsSerialPortTableComSpeed,
       "acsSerialPortTableComParity": acsSerialPortTableComParity,
       "acsSerialPortTableComDataSize": acsSerialPortTableComDataSize,
       "acsSerialPortTableComStopBits": acsSerialPortTableComStopBits,
       "acsSerialPortTableComFlowControl": acsSerialPortTableComFlowControl,
       "acsSerialPortTableSignalStateDTR": acsSerialPortTableSignalStateDTR,
       "acsSerialPortTableSignalStateDCD": acsSerialPortTableSignalStateDCD,
       "acsSerialPortTableSignalStateRTS": acsSerialPortTableSignalStateRTS,
       "acsSerialPortTableSignalStateCTS": acsSerialPortTableSignalStateCTS,
       "acsSerialPortTableTxBytes": acsSerialPortTableTxBytes,
       "acsSerialPortTableRxBytes": acsSerialPortTableRxBytes,
       "acsSerialPortTableFrameError": acsSerialPortTableFrameError,
       "acsSerialPortTableParityError": acsSerialPortTableParityError,
       "acsSerialPortTableBreak": acsSerialPortTableBreak,
       "acsSerialPortTableOverrun": acsSerialPortTableOverrun,
       "acsPowerMgmt": acsPowerMgmt,
       "acsPowerMgmtNumSerialPorts": acsPowerMgmtNumSerialPorts,
       "acsPowerMgmtSerialTable": acsPowerMgmtSerialTable,
       "acsPowerMgmtSerialTableEntry": acsPowerMgmtSerialTableEntry,
       "acsPowerMgmtSerialTableIndex": acsPowerMgmtSerialTableIndex,
       "acsPowerMgmtSerialTablePortNumber": acsPowerMgmtSerialTablePortNumber,
       "acsPowerMgmtSerialTableDeviceName": acsPowerMgmtSerialTableDeviceName,
       "acsPowerMgmtSerialTableNumberPDUs": acsPowerMgmtSerialTableNumberPDUs,
       "acsPowerMgmtPDUTable": acsPowerMgmtPDUTable,
       "acsPowerMgmtPDUTableEntry": acsPowerMgmtPDUTableEntry,
       "acsPowerMgmtPDUTablePortNumber": acsPowerMgmtPDUTablePortNumber,
       "acsPowerMgmtPDUTablePduIndex": acsPowerMgmtPDUTablePduIndex,
       "acsPowerMgmtPDUTablePduId": acsPowerMgmtPDUTablePduId,
       "acsPowerMgmtPDUTablePortName": acsPowerMgmtPDUTablePortName,
       "acsPowerMgmtPDUTableModel": acsPowerMgmtPDUTableModel,
       "acsPowerMgmtPDUTableVendor": acsPowerMgmtPDUTableVendor,
       "acsPowerMgmtPDUTableFirmwareVersion": acsPowerMgmtPDUTableFirmwareVersion,
       "acsPowerMgmtPDUTableNumberOfOutlets": acsPowerMgmtPDUTableNumberOfOutlets,
       "acsPowerMgmtPDUTableCurrentNOS": acsPowerMgmtPDUTableCurrentNOS,
       "acsPowerMgmtPDUTableCurrent1Value": acsPowerMgmtPDUTableCurrent1Value,
       "acsPowerMgmtPDUTableCurrent1Max": acsPowerMgmtPDUTableCurrent1Max,
       "acsPowerMgmtPDUTableCurrent2Value": acsPowerMgmtPDUTableCurrent2Value,
       "acsPowerMgmtPDUTableCurrent2Max": acsPowerMgmtPDUTableCurrent2Max,
       "acsPowerMgmtPDUTableCurrent3Value": acsPowerMgmtPDUTableCurrent3Value,
       "acsPowerMgmtPDUTableCurrent3Max": acsPowerMgmtPDUTableCurrent3Max,
       "acsPowerMgmtPDUTableTemperatureNOS": acsPowerMgmtPDUTableTemperatureNOS,
       "acsPowerMgmtPDUTableTemperature1Value": acsPowerMgmtPDUTableTemperature1Value,
       "acsPowerMgmtPDUTableTemperature1Max": acsPowerMgmtPDUTableTemperature1Max,
       "acsPowerMgmtPDUTableTemperature2Value": acsPowerMgmtPDUTableTemperature2Value,
       "acsPowerMgmtPDUTableTemperature2Max": acsPowerMgmtPDUTableTemperature2Max,
       "acsPowerMgmtPDUTableTemperature3Value": acsPowerMgmtPDUTableTemperature3Value,
       "acsPowerMgmtPDUTableTemperature3Max": acsPowerMgmtPDUTableTemperature3Max,
       "acsPowerMgmtPDUTableHumidityNOS": acsPowerMgmtPDUTableHumidityNOS,
       "acsPowerMgmtPDUTableHumidity1Value": acsPowerMgmtPDUTableHumidity1Value,
       "acsPowerMgmtPDUTableHumidity1Max": acsPowerMgmtPDUTableHumidity1Max,
       "acsPowerMgmtPDUTableHumidity2Value": acsPowerMgmtPDUTableHumidity2Value,
       "acsPowerMgmtPDUTableHumidity2Max": acsPowerMgmtPDUTableHumidity2Max,
       "acsPowerMgmtPDUTableHumidity3Value": acsPowerMgmtPDUTableHumidity3Value,
       "acsPowerMgmtPDUTableHumidity3Max": acsPowerMgmtPDUTableHumidity3Max,
       "acsPowerMgmtPDUTableVoltageNOS": acsPowerMgmtPDUTableVoltageNOS,
       "acsPowerMgmtPDUTableVoltage1Value": acsPowerMgmtPDUTableVoltage1Value,
       "acsPowerMgmtPDUTableVoltage1Max": acsPowerMgmtPDUTableVoltage1Max,
       "acsPowerMgmtPDUTableVoltage2Value": acsPowerMgmtPDUTableVoltage2Value,
       "acsPowerMgmtPDUTableVoltage2Max": acsPowerMgmtPDUTableVoltage2Max,
       "acsPowerMgmtPDUTableVoltage3Value": acsPowerMgmtPDUTableVoltage3Value,
       "acsPowerMgmtPDUTableVoltage3Max": acsPowerMgmtPDUTableVoltage3Max,
       "acsPowerMgmtPDUTableNumberOfPhases": acsPowerMgmtPDUTableNumberOfPhases,
       "acsPowerMgmtPDUTableNumberOfBanks": acsPowerMgmtPDUTableNumberOfBanks,
       "acsPowerMgmtPDUTableCurrentValue": acsPowerMgmtPDUTableCurrentValue,
       "acsPowerMgmtPDUTableCurrentMax": acsPowerMgmtPDUTableCurrentMax,
       "acsPowerMgmtPDUTableCurrentMin": acsPowerMgmtPDUTableCurrentMin,
       "acsPowerMgmtPDUTableCurrentAvg": acsPowerMgmtPDUTableCurrentAvg,
       "acsPowerMgmtPDUTableCurrentReset": acsPowerMgmtPDUTableCurrentReset,
       "acsPowerMgmtPDUTableVoltageType": acsPowerMgmtPDUTableVoltageType,
       "acsPowerMgmtPDUTableVoltageValue": acsPowerMgmtPDUTableVoltageValue,
       "acsPowerMgmtPDUTableVoltageMax": acsPowerMgmtPDUTableVoltageMax,
       "acsPowerMgmtPDUTableVoltageMin": acsPowerMgmtPDUTableVoltageMin,
       "acsPowerMgmtPDUTableVoltageAvg": acsPowerMgmtPDUTableVoltageAvg,
       "acsPowerMgmtPDUTableVoltageReset": acsPowerMgmtPDUTableVoltageReset,
       "acsPowerMgmtPDUTablePowerType": acsPowerMgmtPDUTablePowerType,
       "acsPowerMgmtPDUTablePowerValue": acsPowerMgmtPDUTablePowerValue,
       "acsPowerMgmtPDUTablePowerMax": acsPowerMgmtPDUTablePowerMax,
       "acsPowerMgmtPDUTablePowerMin": acsPowerMgmtPDUTablePowerMin,
       "acsPowerMgmtPDUTablePowerAvg": acsPowerMgmtPDUTablePowerAvg,
       "acsPowerMgmtPDUTablePowerReset": acsPowerMgmtPDUTablePowerReset,
       "acsPowerMgmtPDUTablePowerFactorType": acsPowerMgmtPDUTablePowerFactorType,
       "acsPowerMgmtPDUTablePowerFactorValue": acsPowerMgmtPDUTablePowerFactorValue,
       "acsPowerMgmtPDUTablePowerFactorMax": acsPowerMgmtPDUTablePowerFactorMax,
       "acsPowerMgmtPDUTablePowerFactorMin": acsPowerMgmtPDUTablePowerFactorMin,
       "acsPowerMgmtPDUTablePowerFactorAvg": acsPowerMgmtPDUTablePowerFactorAvg,
       "acsPowerMgmtPDUTablePowerFactorReset": acsPowerMgmtPDUTablePowerFactorReset,
       "acsPowerMgmtPDUTableAlarm": acsPowerMgmtPDUTableAlarm,
       "acsPowerMgmtPDUTableEnvSensors": acsPowerMgmtPDUTableEnvSensors,
       "acsPowerMgmtTotalNumberOfOutlets": acsPowerMgmtTotalNumberOfOutlets,
       "acsPowerMgmtOutletsTable": acsPowerMgmtOutletsTable,
       "acsPowerMgmtOutletsTableEntry": acsPowerMgmtOutletsTableEntry,
       "acsPowerMgmtOutletsTablePortNumber": acsPowerMgmtOutletsTablePortNumber,
       "acsPowerMgmtOutletsTablePduNumber": acsPowerMgmtOutletsTablePduNumber,
       "acsPowerMgmtOutletsTableNumber": acsPowerMgmtOutletsTableNumber,
       "acsPowerMgmtOutletsTableName": acsPowerMgmtOutletsTableName,
       "acsPowerMgmtOutletsTableStatus": acsPowerMgmtOutletsTableStatus,
       "acsPowerMgmtOutletsTablePowerControl": acsPowerMgmtOutletsTablePowerControl,
       "acsPowerMgmtOutletsTablePortName": acsPowerMgmtOutletsTablePortName,
       "acsPowerMgmtOutletsTablePduId": acsPowerMgmtOutletsTablePduId,
       "acsPowerMgmtNumberOfOutletGroup": acsPowerMgmtNumberOfOutletGroup,
       "acsPowerMgmtGroupTable": acsPowerMgmtGroupTable,
       "acsPowerMgmtGroupTableEntry": acsPowerMgmtGroupTableEntry,
       "acsPowerMgmtGroupTableIndex": acsPowerMgmtGroupTableIndex,
       "acsPowerMgmtGroupTableName": acsPowerMgmtGroupTableName,
       "acsPowerMgmtGroupTableStatus": acsPowerMgmtGroupTableStatus,
       "acsPowerMgmtGroupTablePowerControl": acsPowerMgmtGroupTablePowerControl,
       "acsPowerMgmtPhasesTable": acsPowerMgmtPhasesTable,
       "acsPowerMgmtPhasesTableEntry": acsPowerMgmtPhasesTableEntry,
       "acsPowerMgmtPhasesTablePortNumber": acsPowerMgmtPhasesTablePortNumber,
       "acsPowerMgmtPhasesTablePduIndex": acsPowerMgmtPhasesTablePduIndex,
       "acsPowerMgmtPhasesTablePhaseIndex": acsPowerMgmtPhasesTablePhaseIndex,
       "acsPowerMgmtPhasesTablePhaseName": acsPowerMgmtPhasesTablePhaseName,
       "acsPowerMgmtPhasesTablePduId": acsPowerMgmtPhasesTablePduId,
       "acsPowerMgmtPhasesTablePortName": acsPowerMgmtPhasesTablePortName,
       "acsPowerMgmtPhasesTableCurrentValue": acsPowerMgmtPhasesTableCurrentValue,
       "acsPowerMgmtPhasesTableCurrentMax": acsPowerMgmtPhasesTableCurrentMax,
       "acsPowerMgmtPhasesTableCurrentMin": acsPowerMgmtPhasesTableCurrentMin,
       "acsPowerMgmtPhasesTableCurrentAvg": acsPowerMgmtPhasesTableCurrentAvg,
       "acsPowerMgmtPhasesTableCurrentReset": acsPowerMgmtPhasesTableCurrentReset,
       "acsPowerMgmtPhasesTableVoltageType": acsPowerMgmtPhasesTableVoltageType,
       "acsPowerMgmtPhasesTableVoltageValue": acsPowerMgmtPhasesTableVoltageValue,
       "acsPowerMgmtPhasesTableVoltageMax": acsPowerMgmtPhasesTableVoltageMax,
       "acsPowerMgmtPhasesTableVoltageMin": acsPowerMgmtPhasesTableVoltageMin,
       "acsPowerMgmtPhasesTableVoltageAvg": acsPowerMgmtPhasesTableVoltageAvg,
       "acsPowerMgmtPhasesTableVoltageReset": acsPowerMgmtPhasesTableVoltageReset,
       "acsPowerMgmtPhasesTablePowerType": acsPowerMgmtPhasesTablePowerType,
       "acsPowerMgmtPhasesTablePowerValue": acsPowerMgmtPhasesTablePowerValue,
       "acsPowerMgmtPhasesTablePowerMax": acsPowerMgmtPhasesTablePowerMax,
       "acsPowerMgmtPhasesTablePowerMin": acsPowerMgmtPhasesTablePowerMin,
       "acsPowerMgmtPhasesTablePowerAvg": acsPowerMgmtPhasesTablePowerAvg,
       "acsPowerMgmtPhasesTablePowerReset": acsPowerMgmtPhasesTablePowerReset,
       "acsPowerMgmtPhasesTablePowerFactorType": acsPowerMgmtPhasesTablePowerFactorType,
       "acsPowerMgmtPhasesTablePowerFactorValue": acsPowerMgmtPhasesTablePowerFactorValue,
       "acsPowerMgmtPhasesTablePowerFactorMax": acsPowerMgmtPhasesTablePowerFactorMax,
       "acsPowerMgmtPhasesTablePowerFactorMin": acsPowerMgmtPhasesTablePowerFactorMin,
       "acsPowerMgmtPhasesTablePowerFactorAvg": acsPowerMgmtPhasesTablePowerFactorAvg,
       "acsPowerMgmtPhasesTablePowerFactorReset": acsPowerMgmtPhasesTablePowerFactorReset,
       "acsPowerMgmtPhasesTableAlarm": acsPowerMgmtPhasesTableAlarm,
       "acsPowerMgmtBanksTable": acsPowerMgmtBanksTable,
       "acsPowerMgmtBanksTableEntry": acsPowerMgmtBanksTableEntry,
       "acsPowerMgmtBanksTablePortNumber": acsPowerMgmtBanksTablePortNumber,
       "acsPowerMgmtBanksTablePduIndex": acsPowerMgmtBanksTablePduIndex,
       "acsPowerMgmtBanksTableBankIndex": acsPowerMgmtBanksTableBankIndex,
       "acsPowerMgmtBanksTableBankName": acsPowerMgmtBanksTableBankName,
       "acsPowerMgmtBanksTablePduId": acsPowerMgmtBanksTablePduId,
       "acsPowerMgmtBanksTablePortName": acsPowerMgmtBanksTablePortName,
       "acsPowerMgmtBanksTableCurrentValue": acsPowerMgmtBanksTableCurrentValue,
       "acsPowerMgmtBanksTableCurrentMax": acsPowerMgmtBanksTableCurrentMax,
       "acsPowerMgmtBanksTableCurrentMin": acsPowerMgmtBanksTableCurrentMin,
       "acsPowerMgmtBanksTableCurrentAvg": acsPowerMgmtBanksTableCurrentAvg,
       "acsPowerMgmtBanksTableCurrentReset": acsPowerMgmtBanksTableCurrentReset,
       "acsPowerMgmtBanksTableVoltageType": acsPowerMgmtBanksTableVoltageType,
       "acsPowerMgmtBanksTableVoltageValue": acsPowerMgmtBanksTableVoltageValue,
       "acsPowerMgmtBanksTableVoltageMax": acsPowerMgmtBanksTableVoltageMax,
       "acsPowerMgmtBanksTableVoltageMin": acsPowerMgmtBanksTableVoltageMin,
       "acsPowerMgmtBanksTableVoltageAvg": acsPowerMgmtBanksTableVoltageAvg,
       "acsPowerMgmtBanksTableVoltageReset": acsPowerMgmtBanksTableVoltageReset,
       "acsPowerMgmtBanksTablePowerType": acsPowerMgmtBanksTablePowerType,
       "acsPowerMgmtBanksTablePowerValue": acsPowerMgmtBanksTablePowerValue,
       "acsPowerMgmtBanksTablePowerMax": acsPowerMgmtBanksTablePowerMax,
       "acsPowerMgmtBanksTablePowerMin": acsPowerMgmtBanksTablePowerMin,
       "acsPowerMgmtBanksTablePowerAvg": acsPowerMgmtBanksTablePowerAvg,
       "acsPowerMgmtBanksTablePowerReset": acsPowerMgmtBanksTablePowerReset,
       "acsPowerMgmtBanksTablePowerFactorType": acsPowerMgmtBanksTablePowerFactorType,
       "acsPowerMgmtBanksTablePowerFactorValue": acsPowerMgmtBanksTablePowerFactorValue,
       "acsPowerMgmtBanksTablePowerFactorMax": acsPowerMgmtBanksTablePowerFactorMax,
       "acsPowerMgmtBanksTablePowerFactorMin": acsPowerMgmtBanksTablePowerFactorMin,
       "acsPowerMgmtBanksTablePowerFactorAvg": acsPowerMgmtBanksTablePowerFactorAvg,
       "acsPowerMgmtBanksTablePowerFactorReset": acsPowerMgmtBanksTablePowerFactorReset,
       "acsPowerMgmtBanksTableAlarm": acsPowerMgmtBanksTableAlarm,
       "acsPowerMgmtEnvMonTable": acsPowerMgmtEnvMonTable,
       "acsPowerMgmtEnvMonTableEntry": acsPowerMgmtEnvMonTableEntry,
       "acsPowerMgmtEnvMonTablePortNumber": acsPowerMgmtEnvMonTablePortNumber,
       "acsPowerMgmtEnvMonTablePduIndex": acsPowerMgmtEnvMonTablePduIndex,
       "acsPowerMgmtEnvMonTableIndex": acsPowerMgmtEnvMonTableIndex,
       "acsPowerMgmtEnvMonTableName": acsPowerMgmtEnvMonTableName,
       "acsPowerMgmtEnvMonTablePduId": acsPowerMgmtEnvMonTablePduId,
       "acsPowerMgmtEnvMonTablePortName": acsPowerMgmtEnvMonTablePortName,
       "acsPowerMgmtEnvMonTableType": acsPowerMgmtEnvMonTableType,
       "acsPowerMgmtEnvMonTableStatus": acsPowerMgmtEnvMonTableStatus,
       "acsPowerMgmtEnvMonTableValue": acsPowerMgmtEnvMonTableValue,
       "acsPowerMgmtEnvMonTableMaxValue": acsPowerMgmtEnvMonTableMaxValue,
       "acsPowerMgmtOutElecMonTable": acsPowerMgmtOutElecMonTable,
       "acsPowerMgmtOutElecMonTableEntry": acsPowerMgmtOutElecMonTableEntry,
       "acsPowerMgmtOutElecMonTablePortNumber": acsPowerMgmtOutElecMonTablePortNumber,
       "acsPowerMgmtOutElecMonTablePduNumber": acsPowerMgmtOutElecMonTablePduNumber,
       "acsPowerMgmtOutElecMonTableNumber": acsPowerMgmtOutElecMonTableNumber,
       "acsPowerMgmtOutElecMonTableCurrentValue": acsPowerMgmtOutElecMonTableCurrentValue,
       "acsPowerMgmtOutElecMonTableCurrentMax": acsPowerMgmtOutElecMonTableCurrentMax,
       "acsPowerMgmtOutElecMonTableCurrentMin": acsPowerMgmtOutElecMonTableCurrentMin,
       "acsPowerMgmtOutElecMonTableCurrentAvg": acsPowerMgmtOutElecMonTableCurrentAvg,
       "acsPowerMgmtOutElecMonTableCurrentReset": acsPowerMgmtOutElecMonTableCurrentReset,
       "acsPowerMgmtOutElecMonTablePowerValue": acsPowerMgmtOutElecMonTablePowerValue,
       "acsPowerMgmtOutElecMonTablePowerMax": acsPowerMgmtOutElecMonTablePowerMax,
       "acsPowerMgmtOutElecMonTablePowerMin": acsPowerMgmtOutElecMonTablePowerMin,
       "acsPowerMgmtOutElecMonTablePowerAvg": acsPowerMgmtOutElecMonTablePowerAvg,
       "acsPowerMgmtOutElecMonTablePowerReset": acsPowerMgmtOutElecMonTablePowerReset,
       "acsPowerMgmtOutElecMonTableVoltageValue": acsPowerMgmtOutElecMonTableVoltageValue,
       "acsPowerMgmtOutElecMonTableVoltageMax": acsPowerMgmtOutElecMonTableVoltageMax,
       "acsPowerMgmtOutElecMonTableVoltageMin": acsPowerMgmtOutElecMonTableVoltageMin,
       "acsPowerMgmtOutElecMonTableVoltageAvg": acsPowerMgmtOutElecMonTableVoltageAvg,
       "acsPowerMgmtOutElecMonTableVoltageReset": acsPowerMgmtOutElecMonTableVoltageReset,
       "acsPowerMgmtOutElecMonTablePowerFactorValue": acsPowerMgmtOutElecMonTablePowerFactorValue,
       "acsPowerMgmtOutElecMonTablePowerFactorMax": acsPowerMgmtOutElecMonTablePowerFactorMax,
       "acsPowerMgmtOutElecMonTablePowerFactorMin": acsPowerMgmtOutElecMonTablePowerFactorMin,
       "acsPowerMgmtOutElecMonTablePowerFactorAvg": acsPowerMgmtOutElecMonTablePowerFactorAvg,
       "acsPowerMgmtOutElecMonTablePowerFactorReset": acsPowerMgmtOutElecMonTablePowerFactorReset,
       "acsPowerMgmtOutElecMonTableAlarm": acsPowerMgmtOutElecMonTableAlarm,
       "acsTrapObject": acsTrapObject}
)
