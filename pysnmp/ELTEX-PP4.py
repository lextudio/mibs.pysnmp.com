# SNMP MIB module (ELTEX-PP4) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-PP4
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:14 2024
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

(elHardware,
 eltrapGroup,
 mcTrapDescr,
 mcTrapExState,
 mcTrapID,
 mcTrapLParam1,
 mcTrapLParam2,
 mcTrapLParam3) = mibBuilder.importSymbols(
    "ELTEX-SMI-ACTUAL",
    "elHardware",
    "eltrapGroup",
    "mcTrapDescr",
    "mcTrapExState",
    "mcTrapID",
    "mcTrapLParam1",
    "mcTrapLParam2",
    "mcTrapLParam3")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pp4 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13)
)
pp4.setRevisions(
        ("2009-11-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PP4SysType(Integer32, TextualConvention):
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
        *(("systemPp4g", 1),
          ("systemPp4g2x", 2),
          ("systemPp4x", 3),
          ("systemUnknown", 0))
    )



class Pp4Link(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 0),
          ("linkUp", 1))
    )



class Pp4PortSpeed(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("speed100Mbps", 1),
          ("speed10Gbps", 3),
          ("speed10Mbps", 0),
          ("speed12Gbps", 4),
          ("speed1Gbps", 2),
          ("speed2500Mbps", 5),
          ("speed5Gbps", 6))
    )



class Pp4PortDuplex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 0),
          ("halfDuplex", 1))
    )



class Pp4MacType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("macDynamic", 1),
          ("macStatic", 0))
    )



class Pp4MacPort(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            255
        )
    )
    namedValues = NamedValues(
        ("portCPU", 255)
    )



class Pp4RebootIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101,
              102)
        )
    )
    namedValues = NamedValues(
        *(("master", 100),
          ("slave", 101),
          ("system", 102))
    )



class Pp4SlotBoardType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("elc8", 2),
          ("fxs72megaco", 6),
          ("fxs72sip", 5),
          ("invalid", 255),
          ("none", 0),
          ("plc16", 4),
          ("plc8", 3),
          ("pp4x", 1),
          ("tmg16sip", 7))
    )



class Pp4FanBreakdownState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fanIsBreakDown", 1),
          ("fanIsNormal", 0),
          ("fanIsNotDefine", 2))
    )



class Pp4BoardRole(Integer32, TextualConvention):
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
        *(("backup", 2),
          ("master", 3),
          ("notdefine", 0),
          ("slave", 1))
    )



class Pp4BoardPosition(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("notdefine", 0),
          ("right", 2))
    )



class Pp4SlotFirmwareVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("default", -1),
          ("embedded", -2))
    )



class Pp4FirmwareUnitStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("downloaded", 4),
          ("invalid", 1),
          ("isCurrent", 3),
          ("testing", 5),
          ("timeout", 2),
          ("undefined", 0))
    )



class Pp4FeederStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("error", 1),
          ("highVoltage", 2),
          ("lowVoltage", 3),
          ("notInstalled", 0),
          ("ok", 4))
    )



class Pp4FeederActive(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("backup", 2),
          ("notAvailable", 0))
    )



class Pp4FeederPolarity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mismatch", 2),
          ("notAvailable", 0),
          ("ok", 1))
    )



# MIB Managed Objects in the order of their OIDs



class _Pp4DevName_Type(DisplayString):
    """Custom type pp4DevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4DevName_Type.__name__ = "DisplayString"
_Pp4DevName_Object = MibScalar
pp4DevName = _Pp4DevName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 1),
    _Pp4DevName_Type()
)
pp4DevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4DevName.setStatus("current")
_Pp4DevType_Type = Integer32
_Pp4DevType_Object = MibScalar
pp4DevType = _Pp4DevType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 2),
    _Pp4DevType_Type()
)
pp4DevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4DevType.setStatus("current")


class _Pp4DevCfgBuild_Type(DisplayString):
    """Custom type pp4DevCfgBuild based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4DevCfgBuild_Type.__name__ = "DisplayString"
_Pp4DevCfgBuild_Object = MibScalar
pp4DevCfgBuild = _Pp4DevCfgBuild_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 3),
    _Pp4DevCfgBuild_Type()
)
pp4DevCfgBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4DevCfgBuild.setStatus("current")
_Pp4FreeSpace_Type = Integer32
_Pp4FreeSpace_Object = MibScalar
pp4FreeSpace = _Pp4FreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 4),
    _Pp4FreeSpace_Type()
)
pp4FreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4FreeSpace.setStatus("current")
_Pp4FreeRam_Type = Integer32
_Pp4FreeRam_Object = MibScalar
pp4FreeRam = _Pp4FreeRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 5),
    _Pp4FreeRam_Type()
)
pp4FreeRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4FreeRam.setStatus("current")
_Pp4System_ObjectIdentity = ObjectIdentity
pp4System = _Pp4System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10)
)
_Pp4SystemType_Type = PP4SysType
_Pp4SystemType_Object = MibScalar
pp4SystemType = _Pp4SystemType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 1),
    _Pp4SystemType_Type()
)
pp4SystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemType.setStatus("current")


class _Pp4SystemInfo_Type(DisplayString):
    """Custom type pp4SystemInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4SystemInfo_Type.__name__ = "DisplayString"
_Pp4SystemInfo_Object = MibScalar
pp4SystemInfo = _Pp4SystemInfo_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 2),
    _Pp4SystemInfo_Type()
)
pp4SystemInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemInfo.setStatus("current")
_Pp4SystemUnit1MacAddress_Type = MacAddress
_Pp4SystemUnit1MacAddress_Object = MibScalar
pp4SystemUnit1MacAddress = _Pp4SystemUnit1MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 3),
    _Pp4SystemUnit1MacAddress_Type()
)
pp4SystemUnit1MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1MacAddress.setStatus("current")
_Pp4SystemUnit2MacAddress_Type = MacAddress
_Pp4SystemUnit2MacAddress_Object = MibScalar
pp4SystemUnit2MacAddress = _Pp4SystemUnit2MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 4),
    _Pp4SystemUnit2MacAddress_Type()
)
pp4SystemUnit2MacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2MacAddress.setStatus("current")


class _Pp4SystemUnit1FirmwareVersion_Type(DisplayString):
    """Custom type pp4SystemUnit1FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4SystemUnit1FirmwareVersion_Type.__name__ = "DisplayString"
_Pp4SystemUnit1FirmwareVersion_Object = MibScalar
pp4SystemUnit1FirmwareVersion = _Pp4SystemUnit1FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 5),
    _Pp4SystemUnit1FirmwareVersion_Type()
)
pp4SystemUnit1FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1FirmwareVersion.setStatus("current")


class _Pp4SystemUnit2FirmwareVersion_Type(DisplayString):
    """Custom type pp4SystemUnit2FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4SystemUnit2FirmwareVersion_Type.__name__ = "DisplayString"
_Pp4SystemUnit2FirmwareVersion_Object = MibScalar
pp4SystemUnit2FirmwareVersion = _Pp4SystemUnit2FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 6),
    _Pp4SystemUnit2FirmwareVersion_Type()
)
pp4SystemUnit2FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2FirmwareVersion.setStatus("current")


class _Pp4SystemUnit1LinuxVersion_Type(DisplayString):
    """Custom type pp4SystemUnit1LinuxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4SystemUnit1LinuxVersion_Type.__name__ = "DisplayString"
_Pp4SystemUnit1LinuxVersion_Object = MibScalar
pp4SystemUnit1LinuxVersion = _Pp4SystemUnit1LinuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 7),
    _Pp4SystemUnit1LinuxVersion_Type()
)
pp4SystemUnit1LinuxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1LinuxVersion.setStatus("current")


class _Pp4SystemUnit2LinuxVersion_Type(DisplayString):
    """Custom type pp4SystemUnit2LinuxVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Pp4SystemUnit2LinuxVersion_Type.__name__ = "DisplayString"
_Pp4SystemUnit2LinuxVersion_Object = MibScalar
pp4SystemUnit2LinuxVersion = _Pp4SystemUnit2LinuxVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 8),
    _Pp4SystemUnit2LinuxVersion_Type()
)
pp4SystemUnit2LinuxVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2LinuxVersion.setStatus("current")
_Pp4SystemUnit1UpTime_Type = Integer32
_Pp4SystemUnit1UpTime_Object = MibScalar
pp4SystemUnit1UpTime = _Pp4SystemUnit1UpTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 9),
    _Pp4SystemUnit1UpTime_Type()
)
pp4SystemUnit1UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1UpTime.setStatus("current")
if mibBuilder.loadTexts:
    pp4SystemUnit1UpTime.setUnits("sec")
_Pp4SystemUnit2UpTime_Type = Integer32
_Pp4SystemUnit2UpTime_Object = MibScalar
pp4SystemUnit2UpTime = _Pp4SystemUnit2UpTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 10),
    _Pp4SystemUnit2UpTime_Type()
)
pp4SystemUnit2UpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2UpTime.setStatus("current")
if mibBuilder.loadTexts:
    pp4SystemUnit2UpTime.setUnits("sec")
_Pp4SystemUnit1Role_Type = Pp4BoardRole
_Pp4SystemUnit1Role_Object = MibScalar
pp4SystemUnit1Role = _Pp4SystemUnit1Role_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 11),
    _Pp4SystemUnit1Role_Type()
)
pp4SystemUnit1Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1Role.setStatus("current")
_Pp4SystemUnit2Role_Type = Pp4BoardRole
_Pp4SystemUnit2Role_Object = MibScalar
pp4SystemUnit2Role = _Pp4SystemUnit2Role_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 12),
    _Pp4SystemUnit2Role_Type()
)
pp4SystemUnit2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2Role.setStatus("current")
_Pp4SystemUnit1Position_Type = Pp4BoardPosition
_Pp4SystemUnit1Position_Object = MibScalar
pp4SystemUnit1Position = _Pp4SystemUnit1Position_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 13),
    _Pp4SystemUnit1Position_Type()
)
pp4SystemUnit1Position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1Position.setStatus("current")
_Pp4SystemUnit2Position_Type = Pp4BoardPosition
_Pp4SystemUnit2Position_Object = MibScalar
pp4SystemUnit2Position = _Pp4SystemUnit2Position_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 14),
    _Pp4SystemUnit2Position_Type()
)
pp4SystemUnit2Position.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2Position.setStatus("current")


class _Pp4SystemUnit1SerialNumber_Type(DisplayString):
    """Custom type pp4SystemUnit1SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pp4SystemUnit1SerialNumber_Type.__name__ = "DisplayString"
_Pp4SystemUnit1SerialNumber_Object = MibScalar
pp4SystemUnit1SerialNumber = _Pp4SystemUnit1SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 15),
    _Pp4SystemUnit1SerialNumber_Type()
)
pp4SystemUnit1SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit1SerialNumber.setStatus("current")


class _Pp4SystemUnit2SerialNumber_Type(DisplayString):
    """Custom type pp4SystemUnit2SerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Pp4SystemUnit2SerialNumber_Type.__name__ = "DisplayString"
_Pp4SystemUnit2SerialNumber_Object = MibScalar
pp4SystemUnit2SerialNumber = _Pp4SystemUnit2SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 16),
    _Pp4SystemUnit2SerialNumber_Type()
)
pp4SystemUnit2SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SystemUnit2SerialNumber.setStatus("current")
_Pp4SynchronizationStateInStack_Type = TruthValue
_Pp4SynchronizationStateInStack_Object = MibScalar
pp4SynchronizationStateInStack = _Pp4SynchronizationStateInStack_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 17),
    _Pp4SynchronizationStateInStack_Type()
)
pp4SynchronizationStateInStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4SynchronizationStateInStack.setStatus("current")
_Pp4StackMasterChange_Type = Unsigned32
_Pp4StackMasterChange_Object = MibScalar
pp4StackMasterChange = _Pp4StackMasterChange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 18),
    _Pp4StackMasterChange_Type()
)
pp4StackMasterChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4StackMasterChange.setStatus("current")
_Pp4Services_ObjectIdentity = ObjectIdentity
pp4Services = _Pp4Services_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 30)
)
_Pp4ACSActive_Type = TruthValue
_Pp4ACSActive_Object = MibScalar
pp4ACSActive = _Pp4ACSActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 10, 30, 1),
    _Pp4ACSActive_Type()
)
pp4ACSActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ACSActive.setStatus("current")
_Pp4PortsTable_Object = MibTable
pp4PortsTable = _Pp4PortsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11)
)
if mibBuilder.loadTexts:
    pp4PortsTable.setStatus("current")
_Pp4PortsEntry_Object = MibTableRow
pp4PortsEntry = _Pp4PortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1)
)
pp4PortsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4PortsEntryID"),
)
if mibBuilder.loadTexts:
    pp4PortsEntry.setStatus("current")


class _Pp4PortsEntryID_Type(Integer32):
    """Custom type pp4PortsEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Pp4PortsEntryID_Type.__name__ = "Integer32"
_Pp4PortsEntryID_Object = MibTableColumn
pp4PortsEntryID = _Pp4PortsEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 1),
    _Pp4PortsEntryID_Type()
)
pp4PortsEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsEntryID.setStatus("current")
_Pp4PortsLink_Type = Pp4Link
_Pp4PortsLink_Object = MibTableColumn
pp4PortsLink = _Pp4PortsLink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 2),
    _Pp4PortsLink_Type()
)
pp4PortsLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsLink.setStatus("current")
_Pp4PortsAutoNegotiate_Type = TruthValue
_Pp4PortsAutoNegotiate_Object = MibTableColumn
pp4PortsAutoNegotiate = _Pp4PortsAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 3),
    _Pp4PortsAutoNegotiate_Type()
)
pp4PortsAutoNegotiate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsAutoNegotiate.setStatus("current")
_Pp4PortsAutoNegotiationError_Type = TruthValue
_Pp4PortsAutoNegotiationError_Object = MibTableColumn
pp4PortsAutoNegotiationError = _Pp4PortsAutoNegotiationError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 4),
    _Pp4PortsAutoNegotiationError_Type()
)
pp4PortsAutoNegotiationError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsAutoNegotiationError.setStatus("current")
_Pp4PortsSpeed_Type = Pp4PortSpeed
_Pp4PortsSpeed_Object = MibTableColumn
pp4PortsSpeed = _Pp4PortsSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 5),
    _Pp4PortsSpeed_Type()
)
pp4PortsSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsSpeed.setStatus("current")
_Pp4PortsDuplex_Type = Pp4PortDuplex
_Pp4PortsDuplex_Object = MibTableColumn
pp4PortsDuplex = _Pp4PortsDuplex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 6),
    _Pp4PortsDuplex_Type()
)
pp4PortsDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsDuplex.setStatus("current")
_Pp4PortsFlowControlEnabled_Type = TruthValue
_Pp4PortsFlowControlEnabled_Object = MibTableColumn
pp4PortsFlowControlEnabled = _Pp4PortsFlowControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 7),
    _Pp4PortsFlowControlEnabled_Type()
)
pp4PortsFlowControlEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsFlowControlEnabled.setStatus("current")
_Pp4PortsEnabled_Type = TruthValue
_Pp4PortsEnabled_Object = MibTableColumn
pp4PortsEnabled = _Pp4PortsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 11, 1, 8),
    _Pp4PortsEnabled_Type()
)
pp4PortsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PortsEnabled.setStatus("current")
_Pp4MulticastGroupsTable_Object = MibTable
pp4MulticastGroupsTable = _Pp4MulticastGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12)
)
if mibBuilder.loadTexts:
    pp4MulticastGroupsTable.setStatus("current")
_Pp4MulticastGroupsEntry_Object = MibTableRow
pp4MulticastGroupsEntry = _Pp4MulticastGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1)
)
pp4MulticastGroupsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4MulticastEntryID"),
)
if mibBuilder.loadTexts:
    pp4MulticastGroupsEntry.setStatus("current")


class _Pp4MulticastEntryID_Type(Integer32):
    """Custom type pp4MulticastEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Pp4MulticastEntryID_Type.__name__ = "Integer32"
_Pp4MulticastEntryID_Object = MibTableColumn
pp4MulticastEntryID = _Pp4MulticastEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1, 1),
    _Pp4MulticastEntryID_Type()
)
pp4MulticastEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MulticastEntryID.setStatus("current")
_Pp4MulticastVLAN_Type = Integer32
_Pp4MulticastVLAN_Object = MibTableColumn
pp4MulticastVLAN = _Pp4MulticastVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1, 2),
    _Pp4MulticastVLAN_Type()
)
pp4MulticastVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MulticastVLAN.setStatus("current")
_Pp4MulticastGroupAddress_Type = IpAddress
_Pp4MulticastGroupAddress_Object = MibTableColumn
pp4MulticastGroupAddress = _Pp4MulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1, 3),
    _Pp4MulticastGroupAddress_Type()
)
pp4MulticastGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MulticastGroupAddress.setStatus("current")


class _Pp4MulticastMemberPorts_Type(DisplayString):
    """Custom type pp4MulticastMemberPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pp4MulticastMemberPorts_Type.__name__ = "DisplayString"
_Pp4MulticastMemberPorts_Object = MibTableColumn
pp4MulticastMemberPorts = _Pp4MulticastMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1, 4),
    _Pp4MulticastMemberPorts_Type()
)
pp4MulticastMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MulticastMemberPorts.setStatus("current")
_Pp4MulticastExpires_Type = TimeTicks
_Pp4MulticastExpires_Object = MibTableColumn
pp4MulticastExpires = _Pp4MulticastExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 12, 1, 5),
    _Pp4MulticastExpires_Type()
)
pp4MulticastExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MulticastExpires.setStatus("current")
_Pp4MacAddressTable_Object = MibTable
pp4MacAddressTable = _Pp4MacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13)
)
if mibBuilder.loadTexts:
    pp4MacAddressTable.setStatus("current")
_Pp4MacAddressEntry_Object = MibTableRow
pp4MacAddressEntry = _Pp4MacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1)
)
pp4MacAddressEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4MacAddressEntryID"),
)
if mibBuilder.loadTexts:
    pp4MacAddressEntry.setStatus("current")


class _Pp4MacAddressEntryID_Type(Integer32):
    """Custom type pp4MacAddressEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_Pp4MacAddressEntryID_Type.__name__ = "Integer32"
_Pp4MacAddressEntryID_Object = MibTableColumn
pp4MacAddressEntryID = _Pp4MacAddressEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1, 1),
    _Pp4MacAddressEntryID_Type()
)
pp4MacAddressEntryID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MacAddressEntryID.setStatus("current")
_Pp4MacAddressVLAN_Type = Integer32
_Pp4MacAddressVLAN_Object = MibTableColumn
pp4MacAddressVLAN = _Pp4MacAddressVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1, 2),
    _Pp4MacAddressVLAN_Type()
)
pp4MacAddressVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MacAddressVLAN.setStatus("current")
_Pp4MacAddressAddress_Type = MacAddress
_Pp4MacAddressAddress_Object = MibTableColumn
pp4MacAddressAddress = _Pp4MacAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1, 3),
    _Pp4MacAddressAddress_Type()
)
pp4MacAddressAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MacAddressAddress.setStatus("current")
_Pp4MacAddressPort_Type = Pp4MacPort
_Pp4MacAddressPort_Object = MibTableColumn
pp4MacAddressPort = _Pp4MacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1, 4),
    _Pp4MacAddressPort_Type()
)
pp4MacAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MacAddressPort.setStatus("current")
_Pp4MacAddressType_Type = Pp4MacType
_Pp4MacAddressType_Object = MibTableColumn
pp4MacAddressType = _Pp4MacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 13, 1, 5),
    _Pp4MacAddressType_Type()
)
pp4MacAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MacAddressType.setStatus("current")
_Pp4SlotsTable_Object = MibTable
pp4SlotsTable = _Pp4SlotsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14)
)
if mibBuilder.loadTexts:
    pp4SlotsTable.setStatus("current")
_Pp4SlotsEntry_Object = MibTableRow
pp4SlotsEntry = _Pp4SlotsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1)
)
pp4SlotsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4SlotsSlot"),
)
if mibBuilder.loadTexts:
    pp4SlotsEntry.setStatus("current")


class _Pp4SlotsSlot_Type(Unsigned32):
    """Custom type pp4SlotsSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pp4SlotsSlot_Type.__name__ = "Unsigned32"
_Pp4SlotsSlot_Object = MibTableColumn
pp4SlotsSlot = _Pp4SlotsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 1),
    _Pp4SlotsSlot_Type()
)
pp4SlotsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsSlot.setStatus("current")
_Pp4SlotsBoardType_Type = Pp4SlotBoardType
_Pp4SlotsBoardType_Object = MibTableColumn
pp4SlotsBoardType = _Pp4SlotsBoardType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 2),
    _Pp4SlotsBoardType_Type()
)
pp4SlotsBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsBoardType.setStatus("current")


class _Pp4SlotsLink_Type(Integer32):
    """Custom type pp4SlotsLink based on Integer32"""
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


_Pp4SlotsLink_Type.__name__ = "Integer32"
_Pp4SlotsLink_Object = MibTableColumn
pp4SlotsLink = _Pp4SlotsLink_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 3),
    _Pp4SlotsLink_Type()
)
pp4SlotsLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsLink.setStatus("current")
_Pp4SlotsFirmwareActive_Type = DisplayString
_Pp4SlotsFirmwareActive_Object = MibTableColumn
pp4SlotsFirmwareActive = _Pp4SlotsFirmwareActive_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 4),
    _Pp4SlotsFirmwareActive_Type()
)
pp4SlotsFirmwareActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsFirmwareActive.setStatus("current")
_Pp4SlotsFirmwareRevision_Type = Unsigned32
_Pp4SlotsFirmwareRevision_Object = MibTableColumn
pp4SlotsFirmwareRevision = _Pp4SlotsFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 5),
    _Pp4SlotsFirmwareRevision_Type()
)
pp4SlotsFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsFirmwareRevision.setStatus("current")
_Pp4SlotsSerialNumber_Type = DisplayString
_Pp4SlotsSerialNumber_Object = MibTableColumn
pp4SlotsSerialNumber = _Pp4SlotsSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 6),
    _Pp4SlotsSerialNumber_Type()
)
pp4SlotsSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsSerialNumber.setStatus("current")


class _Pp4SlotsState_Type(Integer32):
    """Custom type pp4SlotsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("absent", 0),
          ("booting", 2),
          ("discovery", 1),
          ("fail", 6),
          ("lost", 4),
          ("notBooting", 7),
          ("operational", 3),
          ("sand", 5))
    )


_Pp4SlotsState_Type.__name__ = "Integer32"
_Pp4SlotsState_Object = MibTableColumn
pp4SlotsState = _Pp4SlotsState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 14, 1, 7),
    _Pp4SlotsState_Type()
)
pp4SlotsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4SlotsState.setStatus("current")
_Pp4ConfigRevisions_ObjectIdentity = ObjectIdentity
pp4ConfigRevisions = _Pp4ConfigRevisions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15)
)
_Pp4ConfigRevisionsPp4x_Type = Unsigned32
_Pp4ConfigRevisionsPp4x_Object = MibScalar
pp4ConfigRevisionsPp4x = _Pp4ConfigRevisionsPp4x_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 1),
    _Pp4ConfigRevisionsPp4x_Type()
)
pp4ConfigRevisionsPp4x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsPp4x.setStatus("current")
_Pp4ConfigRevisionsTable_Object = MibTable
pp4ConfigRevisionsTable = _Pp4ConfigRevisionsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 2)
)
if mibBuilder.loadTexts:
    pp4ConfigRevisionsTable.setStatus("current")
_Pp4ConfigRevisionsEntry_Object = MibTableRow
pp4ConfigRevisionsEntry = _Pp4ConfigRevisionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 2, 1)
)
pp4ConfigRevisionsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4ConfigRevisionsSlot"),
)
if mibBuilder.loadTexts:
    pp4ConfigRevisionsEntry.setStatus("current")
_Pp4ConfigRevisionsSlot_Type = Unsigned32
_Pp4ConfigRevisionsSlot_Object = MibTableColumn
pp4ConfigRevisionsSlot = _Pp4ConfigRevisionsSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 2, 1, 1),
    _Pp4ConfigRevisionsSlot_Type()
)
pp4ConfigRevisionsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsSlot.setStatus("current")
_Pp4ConfigRevisionsRevision_Type = Unsigned32
_Pp4ConfigRevisionsRevision_Object = MibTableColumn
pp4ConfigRevisionsRevision = _Pp4ConfigRevisionsRevision_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 2, 1, 2),
    _Pp4ConfigRevisionsRevision_Type()
)
pp4ConfigRevisionsRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsRevision.setStatus("current")
_Pp4ConfigRevisionsProfilesELC_Type = Unsigned32
_Pp4ConfigRevisionsProfilesELC_Object = MibScalar
pp4ConfigRevisionsProfilesELC = _Pp4ConfigRevisionsProfilesELC_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 3),
    _Pp4ConfigRevisionsProfilesELC_Type()
)
pp4ConfigRevisionsProfilesELC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsProfilesELC.setStatus("current")
_Pp4ConfigRevisionsProfilesPLC_Type = Unsigned32
_Pp4ConfigRevisionsProfilesPLC_Object = MibScalar
pp4ConfigRevisionsProfilesPLC = _Pp4ConfigRevisionsProfilesPLC_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 4),
    _Pp4ConfigRevisionsProfilesPLC_Type()
)
pp4ConfigRevisionsProfilesPLC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsProfilesPLC.setStatus("current")
_Pp4ConfigRevisionsProfilesPLCOLT_Type = Unsigned32
_Pp4ConfigRevisionsProfilesPLCOLT_Object = MibScalar
pp4ConfigRevisionsProfilesPLCOLT = _Pp4ConfigRevisionsProfilesPLCOLT_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 15, 5),
    _Pp4ConfigRevisionsProfilesPLCOLT_Type()
)
pp4ConfigRevisionsProfilesPLCOLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ConfigRevisionsProfilesPLCOLT.setStatus("current")
_Pp4xIfUtilizTable_Object = MibTable
pp4xIfUtilizTable = _Pp4xIfUtilizTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16)
)
if mibBuilder.loadTexts:
    pp4xIfUtilizTable.setStatus("current")
_Pp4xIfUtilizEntry_Object = MibTableRow
pp4xIfUtilizEntry = _Pp4xIfUtilizEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1)
)
pp4xIfUtilizEntry.setIndexNames(
    (0, "ELTEX-PP4", "interfaceIndex"),
)
if mibBuilder.loadTexts:
    pp4xIfUtilizEntry.setStatus("current")
_InterfaceIndex_Type = Unsigned32
_InterfaceIndex_Object = MibTableColumn
interfaceIndex = _InterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 1),
    _InterfaceIndex_Type()
)
interfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    interfaceIndex.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_LastCountersKbitsSent_Type = Unsigned32
_LastCountersKbitsSent_Object = MibTableColumn
lastCountersKbitsSent = _LastCountersKbitsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 3),
    _LastCountersKbitsSent_Type()
)
lastCountersKbitsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCountersKbitsSent.setStatus("current")
_LastCountersKbitsRecv_Type = Unsigned32
_LastCountersKbitsRecv_Object = MibTableColumn
lastCountersKbitsRecv = _LastCountersKbitsRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 4),
    _LastCountersKbitsRecv_Type()
)
lastCountersKbitsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCountersKbitsRecv.setStatus("current")
_LastCountersFramesSent_Type = Unsigned32
_LastCountersFramesSent_Object = MibTableColumn
lastCountersFramesSent = _LastCountersFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 5),
    _LastCountersFramesSent_Type()
)
lastCountersFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCountersFramesSent.setStatus("current")
_LastCountersFramesRecv_Type = Unsigned32
_LastCountersFramesRecv_Object = MibTableColumn
lastCountersFramesRecv = _LastCountersFramesRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 6),
    _LastCountersFramesRecv_Type()
)
lastCountersFramesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastCountersFramesRecv.setStatus("current")
_AverageKbitsSent_Type = Unsigned32
_AverageKbitsSent_Object = MibTableColumn
averageKbitsSent = _AverageKbitsSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 7),
    _AverageKbitsSent_Type()
)
averageKbitsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageKbitsSent.setStatus("current")
_AverageKbitsRecv_Type = Unsigned32
_AverageKbitsRecv_Object = MibTableColumn
averageKbitsRecv = _AverageKbitsRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 8),
    _AverageKbitsRecv_Type()
)
averageKbitsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageKbitsRecv.setStatus("current")
_AverageFramesSent_Type = Unsigned32
_AverageFramesSent_Object = MibTableColumn
averageFramesSent = _AverageFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 9),
    _AverageFramesSent_Type()
)
averageFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageFramesSent.setStatus("current")
_AverageFramesRecv_Type = Unsigned32
_AverageFramesRecv_Object = MibTableColumn
averageFramesRecv = _AverageFramesRecv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 16, 1, 10),
    _AverageFramesRecv_Type()
)
averageFramesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    averageFramesRecv.setStatus("current")
_Pp4xIfUtilizAverageInterval_Type = Integer32
_Pp4xIfUtilizAverageInterval_Object = MibScalar
pp4xIfUtilizAverageInterval = _Pp4xIfUtilizAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 17),
    _Pp4xIfUtilizAverageInterval_Type()
)
pp4xIfUtilizAverageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4xIfUtilizAverageInterval.setStatus("current")
_Pp4xSfpInfoTable_Object = MibTable
pp4xSfpInfoTable = _Pp4xSfpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18)
)
if mibBuilder.loadTexts:
    pp4xSfpInfoTable.setStatus("current")
_Pp4xSfpInfoEntry_Object = MibTableRow
pp4xSfpInfoEntry = _Pp4xSfpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1)
)
pp4xSfpInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pp4xSfpInfoEntry.setStatus("current")


class _SfpInfoStatus_Type(Integer32):
    """Custom type sfpInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ddmNotSupported", 2),
          ("notAvailable", 1),
          ("ok", 0))
    )


_SfpInfoStatus_Type.__name__ = "Integer32"
_SfpInfoStatus_Object = MibTableColumn
sfpInfoStatus = _SfpInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 1),
    _SfpInfoStatus_Type()
)
sfpInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoStatus.setStatus("current")
_SfpInfoTemperature_Type = Unsigned32
_SfpInfoTemperature_Object = MibTableColumn
sfpInfoTemperature = _SfpInfoTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 2),
    _SfpInfoTemperature_Type()
)
sfpInfoTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoTemperature.setStatus("current")
_SfpInfoVoltage_Type = Unsigned32
_SfpInfoVoltage_Object = MibTableColumn
sfpInfoVoltage = _SfpInfoVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 3),
    _SfpInfoVoltage_Type()
)
sfpInfoVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoVoltage.setStatus("current")
_SfpInfoCurrent_Type = Unsigned32
_SfpInfoCurrent_Object = MibTableColumn
sfpInfoCurrent = _SfpInfoCurrent_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 4),
    _SfpInfoCurrent_Type()
)
sfpInfoCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoCurrent.setStatus("current")
_SfpInfoRXPower_Type = Unsigned32
_SfpInfoRXPower_Object = MibTableColumn
sfpInfoRXPower = _SfpInfoRXPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 5),
    _SfpInfoRXPower_Type()
)
sfpInfoRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoRXPower.setStatus("current")
_SfpInfoTXPower_Type = Unsigned32
_SfpInfoTXPower_Object = MibTableColumn
sfpInfoTXPower = _SfpInfoTXPower_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 18, 1, 6),
    _SfpInfoTXPower_Type()
)
sfpInfoTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpInfoTXPower.setStatus("current")
_Pp4PortsConfigTable_Object = MibTable
pp4PortsConfigTable = _Pp4PortsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19)
)
if mibBuilder.loadTexts:
    pp4PortsConfigTable.setStatus("current")
_Pp4PortsConfigEntry_Object = MibTableRow
pp4PortsConfigEntry = _Pp4PortsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1)
)
pp4PortsConfigEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4PortsConfigEntryID"),
)
if mibBuilder.loadTexts:
    pp4PortsConfigEntry.setStatus("current")
_Pp4PortsConfigEntryID_Type = Unsigned32
_Pp4PortsConfigEntryID_Object = MibTableColumn
pp4PortsConfigEntryID = _Pp4PortsConfigEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 1),
    _Pp4PortsConfigEntryID_Type()
)
pp4PortsConfigEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4PortsConfigEntryID.setStatus("current")
_Pp4PortsConfigAutoNegotiate_Type = TruthValue
_Pp4PortsConfigAutoNegotiate_Object = MibTableColumn
pp4PortsConfigAutoNegotiate = _Pp4PortsConfigAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 2),
    _Pp4PortsConfigAutoNegotiate_Type()
)
pp4PortsConfigAutoNegotiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigAutoNegotiate.setStatus("current")
_Pp4PortsConfigSpeed_Type = Pp4PortSpeed
_Pp4PortsConfigSpeed_Object = MibTableColumn
pp4PortsConfigSpeed = _Pp4PortsConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 3),
    _Pp4PortsConfigSpeed_Type()
)
pp4PortsConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigSpeed.setStatus("current")
_Pp4PortsConfigDuplex_Type = Pp4PortDuplex
_Pp4PortsConfigDuplex_Object = MibTableColumn
pp4PortsConfigDuplex = _Pp4PortsConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 4),
    _Pp4PortsConfigDuplex_Type()
)
pp4PortsConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigDuplex.setStatus("current")
_Pp4PortsConfigFlowControlEnabled_Type = TruthValue
_Pp4PortsConfigFlowControlEnabled_Object = MibTableColumn
pp4PortsConfigFlowControlEnabled = _Pp4PortsConfigFlowControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 5),
    _Pp4PortsConfigFlowControlEnabled_Type()
)
pp4PortsConfigFlowControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigFlowControlEnabled.setStatus("current")
_Pp4PortsConfigEnabled_Type = TruthValue
_Pp4PortsConfigEnabled_Object = MibTableColumn
pp4PortsConfigEnabled = _Pp4PortsConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 6),
    _Pp4PortsConfigEnabled_Type()
)
pp4PortsConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigEnabled.setStatus("current")
_Pp4PortsConfigResetCounters_Type = Unsigned32
_Pp4PortsConfigResetCounters_Object = MibTableColumn
pp4PortsConfigResetCounters = _Pp4PortsConfigResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 7),
    _Pp4PortsConfigResetCounters_Type()
)
pp4PortsConfigResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PortsConfigResetCounters.setStatus("current")
_Pp4PortsConfigRowStatus_Type = RowStatus
_Pp4PortsConfigRowStatus_Object = MibTableColumn
pp4PortsConfigRowStatus = _Pp4PortsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 19, 1, 10),
    _Pp4PortsConfigRowStatus_Type()
)
pp4PortsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pp4PortsConfigRowStatus.setStatus("current")
_Pp4RebootTable_Object = MibTable
pp4RebootTable = _Pp4RebootTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 20)
)
if mibBuilder.loadTexts:
    pp4RebootTable.setStatus("current")
_Pp4RebootEntry_Object = MibTableRow
pp4RebootEntry = _Pp4RebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 20, 1)
)
pp4RebootEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4RebootSlot"),
)
if mibBuilder.loadTexts:
    pp4RebootEntry.setStatus("current")


class _Pp4RebootSlot_Type(Integer32):
    """Custom type pp4RebootSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 102),
    )


_Pp4RebootSlot_Type.__name__ = "Integer32"
_Pp4RebootSlot_Object = MibTableColumn
pp4RebootSlot = _Pp4RebootSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 20, 1, 1),
    _Pp4RebootSlot_Type()
)
pp4RebootSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4RebootSlot.setStatus("current")
_Pp4RebootDescription_Type = DisplayString
_Pp4RebootDescription_Object = MibTableColumn
pp4RebootDescription = _Pp4RebootDescription_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 20, 1, 2),
    _Pp4RebootDescription_Type()
)
pp4RebootDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4RebootDescription.setStatus("current")
_Pp4RebootCommand_Type = Unsigned32
_Pp4RebootCommand_Object = MibTableColumn
pp4RebootCommand = _Pp4RebootCommand_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 20, 1, 3),
    _Pp4RebootCommand_Type()
)
pp4RebootCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4RebootCommand.setStatus("current")
_Pp4RebootAfterDelay_Type = Integer32
_Pp4RebootAfterDelay_Object = MibScalar
pp4RebootAfterDelay = _Pp4RebootAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 21),
    _Pp4RebootAfterDelay_Type()
)
pp4RebootAfterDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4RebootAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    pp4RebootAfterDelay.setUnits("sec")
_Pp4ChannelGroupMembershipTable_Object = MibTable
pp4ChannelGroupMembershipTable = _Pp4ChannelGroupMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 22)
)
if mibBuilder.loadTexts:
    pp4ChannelGroupMembershipTable.setStatus("current")
_Pp4ChannelGroupMembershipEntry_Object = MibTableRow
pp4ChannelGroupMembershipEntry = _Pp4ChannelGroupMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 22, 1)
)
pp4ChannelGroupMembershipEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pp4ChannelGroupMembershipEntry.setStatus("current")
_Pp4ChannelGroupMembershipGroupID_Type = Unsigned32
_Pp4ChannelGroupMembershipGroupID_Object = MibTableColumn
pp4ChannelGroupMembershipGroupID = _Pp4ChannelGroupMembershipGroupID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 22, 1, 1),
    _Pp4ChannelGroupMembershipGroupID_Type()
)
pp4ChannelGroupMembershipGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4ChannelGroupMembershipGroupID.setStatus("current")
_Pp4ChannelGroupLACPTable_Object = MibTable
pp4ChannelGroupLACPTable = _Pp4ChannelGroupLACPTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 23)
)
if mibBuilder.loadTexts:
    pp4ChannelGroupLACPTable.setStatus("current")
_Pp4ChannelGroupLACPEntry_Object = MibTableRow
pp4ChannelGroupLACPEntry = _Pp4ChannelGroupLACPEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 23, 1)
)
pp4ChannelGroupLACPEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4ChannelGroupLACPGroupID"),
)
if mibBuilder.loadTexts:
    pp4ChannelGroupLACPEntry.setStatus("current")
_Pp4ChannelGroupLACPGroupID_Type = Unsigned32
_Pp4ChannelGroupLACPGroupID_Object = MibTableColumn
pp4ChannelGroupLACPGroupID = _Pp4ChannelGroupLACPGroupID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 23, 1, 1),
    _Pp4ChannelGroupLACPGroupID_Type()
)
pp4ChannelGroupLACPGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4ChannelGroupLACPGroupID.setStatus("current")
_Pp4ChannelGroupLACPRunning_Type = TruthValue
_Pp4ChannelGroupLACPRunning_Object = MibTableColumn
pp4ChannelGroupLACPRunning = _Pp4ChannelGroupLACPRunning_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 23, 1, 2),
    _Pp4ChannelGroupLACPRunning_Type()
)
pp4ChannelGroupLACPRunning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4ChannelGroupLACPRunning.setStatus("current")
_Pp4ChannelGroupLACPAggregators_Type = OctetString
_Pp4ChannelGroupLACPAggregators_Object = MibTableColumn
pp4ChannelGroupLACPAggregators = _Pp4ChannelGroupLACPAggregators_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 23, 1, 3),
    _Pp4ChannelGroupLACPAggregators_Type()
)
pp4ChannelGroupLACPAggregators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ChannelGroupLACPAggregators.setStatus("current")
_Pp4LACPSystemPriority_Type = Unsigned32
_Pp4LACPSystemPriority_Object = MibScalar
pp4LACPSystemPriority = _Pp4LACPSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 24),
    _Pp4LACPSystemPriority_Type()
)
pp4LACPSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4LACPSystemPriority.setStatus("current")
_Pp4MLDGroupsTable_Object = MibTable
pp4MLDGroupsTable = _Pp4MLDGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25)
)
if mibBuilder.loadTexts:
    pp4MLDGroupsTable.setStatus("current")
_Pp4MLDGroupsEntry_Object = MibTableRow
pp4MLDGroupsEntry = _Pp4MLDGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1)
)
pp4MLDGroupsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4MLDEntryID"),
)
if mibBuilder.loadTexts:
    pp4MLDGroupsEntry.setStatus("current")


class _Pp4MLDEntryID_Type(Integer32):
    """Custom type pp4MLDEntryID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Pp4MLDEntryID_Type.__name__ = "Integer32"
_Pp4MLDEntryID_Object = MibTableColumn
pp4MLDEntryID = _Pp4MLDEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1, 1),
    _Pp4MLDEntryID_Type()
)
pp4MLDEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4MLDEntryID.setStatus("current")
_Pp4MLDVLAN_Type = Integer32
_Pp4MLDVLAN_Object = MibTableColumn
pp4MLDVLAN = _Pp4MLDVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1, 2),
    _Pp4MLDVLAN_Type()
)
pp4MLDVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MLDVLAN.setStatus("current")
_Pp4MLDGroupAddress_Type = Ipv6Address
_Pp4MLDGroupAddress_Object = MibTableColumn
pp4MLDGroupAddress = _Pp4MLDGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1, 3),
    _Pp4MLDGroupAddress_Type()
)
pp4MLDGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MLDGroupAddress.setStatus("current")


class _Pp4MLDMemberPorts_Type(DisplayString):
    """Custom type pp4MLDMemberPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Pp4MLDMemberPorts_Type.__name__ = "DisplayString"
_Pp4MLDMemberPorts_Object = MibTableColumn
pp4MLDMemberPorts = _Pp4MLDMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1, 4),
    _Pp4MLDMemberPorts_Type()
)
pp4MLDMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MLDMemberPorts.setStatus("current")
_Pp4MLDExpires_Type = TimeTicks
_Pp4MLDExpires_Object = MibTableColumn
pp4MLDExpires = _Pp4MLDExpires_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 25, 1, 5),
    _Pp4MLDExpires_Type()
)
pp4MLDExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MLDExpires.setStatus("current")
_Pp4BoardState_ObjectIdentity = ObjectIdentity
pp4BoardState = _Pp4BoardState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30)
)
_Pp4BoardFan1AbsoluteSpeed_Type = Integer32
_Pp4BoardFan1AbsoluteSpeed_Object = MibScalar
pp4BoardFan1AbsoluteSpeed = _Pp4BoardFan1AbsoluteSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 1),
    _Pp4BoardFan1AbsoluteSpeed_Type()
)
pp4BoardFan1AbsoluteSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan1AbsoluteSpeed.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardFan1AbsoluteSpeed.setUnits("rpm")
_Pp4BoardFan2AbsoluteSpeed_Type = Integer32
_Pp4BoardFan2AbsoluteSpeed_Object = MibScalar
pp4BoardFan2AbsoluteSpeed = _Pp4BoardFan2AbsoluteSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 2),
    _Pp4BoardFan2AbsoluteSpeed_Type()
)
pp4BoardFan2AbsoluteSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan2AbsoluteSpeed.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardFan2AbsoluteSpeed.setUnits("rpm")
_Pp4BoardFan3AbsoluteSpeed_Type = Integer32
_Pp4BoardFan3AbsoluteSpeed_Object = MibScalar
pp4BoardFan3AbsoluteSpeed = _Pp4BoardFan3AbsoluteSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 3),
    _Pp4BoardFan3AbsoluteSpeed_Type()
)
pp4BoardFan3AbsoluteSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan3AbsoluteSpeed.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardFan3AbsoluteSpeed.setUnits("rpm")
_Pp4BoardFanRelativeSpeed_Type = Integer32
_Pp4BoardFanRelativeSpeed_Object = MibScalar
pp4BoardFanRelativeSpeed = _Pp4BoardFanRelativeSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 4),
    _Pp4BoardFanRelativeSpeed_Type()
)
pp4BoardFanRelativeSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFanRelativeSpeed.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardFanRelativeSpeed.setUnits("%")
_Pp4BoardFan1Breakdown_Type = Pp4FanBreakdownState
_Pp4BoardFan1Breakdown_Object = MibScalar
pp4BoardFan1Breakdown = _Pp4BoardFan1Breakdown_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 5),
    _Pp4BoardFan1Breakdown_Type()
)
pp4BoardFan1Breakdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan1Breakdown.setStatus("current")
_Pp4BoardFan2Breakdown_Type = Pp4FanBreakdownState
_Pp4BoardFan2Breakdown_Object = MibScalar
pp4BoardFan2Breakdown = _Pp4BoardFan2Breakdown_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 6),
    _Pp4BoardFan2Breakdown_Type()
)
pp4BoardFan2Breakdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan2Breakdown.setStatus("current")
_Pp4BoardFan3Breakdown_Type = Pp4FanBreakdownState
_Pp4BoardFan3Breakdown_Object = MibScalar
pp4BoardFan3Breakdown = _Pp4BoardFan3Breakdown_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 7),
    _Pp4BoardFan3Breakdown_Type()
)
pp4BoardFan3Breakdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardFan3Breakdown.setStatus("current")
_Pp4BoardUnit1TempSfp_Type = Integer32
_Pp4BoardUnit1TempSfp_Object = MibScalar
pp4BoardUnit1TempSfp = _Pp4BoardUnit1TempSfp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 8),
    _Pp4BoardUnit1TempSfp_Type()
)
pp4BoardUnit1TempSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempSfp.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempSfp.setUnits("deg")
_Pp4BoardUnit2TempSfp_Type = Integer32
_Pp4BoardUnit2TempSfp_Object = MibScalar
pp4BoardUnit2TempSfp = _Pp4BoardUnit2TempSfp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 9),
    _Pp4BoardUnit2TempSfp_Type()
)
pp4BoardUnit2TempSfp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempSfp.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempSfp.setUnits("deg")
_Pp4BoardUnit1TempProc_Type = Integer32
_Pp4BoardUnit1TempProc_Object = MibScalar
pp4BoardUnit1TempProc = _Pp4BoardUnit1TempProc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 10),
    _Pp4BoardUnit1TempProc_Type()
)
pp4BoardUnit1TempProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempProc.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempProc.setUnits("deg")
_Pp4BoardUnit2TempProc_Type = Integer32
_Pp4BoardUnit2TempProc_Object = MibScalar
pp4BoardUnit2TempProc = _Pp4BoardUnit2TempProc_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 11),
    _Pp4BoardUnit2TempProc_Type()
)
pp4BoardUnit2TempProc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempProc.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempProc.setUnits("deg")
_Pp4BoardUnit1TempSwitch_Type = Integer32
_Pp4BoardUnit1TempSwitch_Object = MibScalar
pp4BoardUnit1TempSwitch = _Pp4BoardUnit1TempSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 12),
    _Pp4BoardUnit1TempSwitch_Type()
)
pp4BoardUnit1TempSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempSwitch.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TempSwitch.setUnits("deg")
_Pp4BoardUnit2TempSwitch_Type = Integer32
_Pp4BoardUnit2TempSwitch_Object = MibScalar
pp4BoardUnit2TempSwitch = _Pp4BoardUnit2TempSwitch_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 13),
    _Pp4BoardUnit2TempSwitch_Type()
)
pp4BoardUnit2TempSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempSwitch.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TempSwitch.setUnits("deg")
_Pp4BoardUnit1LoadAverage1_Type = Integer32
_Pp4BoardUnit1LoadAverage1_Object = MibScalar
pp4BoardUnit1LoadAverage1 = _Pp4BoardUnit1LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 14),
    _Pp4BoardUnit1LoadAverage1_Type()
)
pp4BoardUnit1LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1LoadAverage1.setStatus("current")
_Pp4BoardUnit2LoadAverage1_Type = Integer32
_Pp4BoardUnit2LoadAverage1_Object = MibScalar
pp4BoardUnit2LoadAverage1 = _Pp4BoardUnit2LoadAverage1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 15),
    _Pp4BoardUnit2LoadAverage1_Type()
)
pp4BoardUnit2LoadAverage1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2LoadAverage1.setStatus("current")
_Pp4BoardUnit1LoadAverage5_Type = Integer32
_Pp4BoardUnit1LoadAverage5_Object = MibScalar
pp4BoardUnit1LoadAverage5 = _Pp4BoardUnit1LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 16),
    _Pp4BoardUnit1LoadAverage5_Type()
)
pp4BoardUnit1LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1LoadAverage5.setStatus("current")
_Pp4BoardUnit2LoadAverage5_Type = Integer32
_Pp4BoardUnit2LoadAverage5_Object = MibScalar
pp4BoardUnit2LoadAverage5 = _Pp4BoardUnit2LoadAverage5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 17),
    _Pp4BoardUnit2LoadAverage5_Type()
)
pp4BoardUnit2LoadAverage5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2LoadAverage5.setStatus("current")
_Pp4BoardUnit1LoadAverage15_Type = Integer32
_Pp4BoardUnit1LoadAverage15_Object = MibScalar
pp4BoardUnit1LoadAverage15 = _Pp4BoardUnit1LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 18),
    _Pp4BoardUnit1LoadAverage15_Type()
)
pp4BoardUnit1LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1LoadAverage15.setStatus("current")
_Pp4BoardUnit2LoadAverage15_Type = Integer32
_Pp4BoardUnit2LoadAverage15_Object = MibScalar
pp4BoardUnit2LoadAverage15 = _Pp4BoardUnit2LoadAverage15_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 19),
    _Pp4BoardUnit2LoadAverage15_Type()
)
pp4BoardUnit2LoadAverage15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2LoadAverage15.setStatus("current")
_Pp4BoardUnit1TotalRam_Type = Integer32
_Pp4BoardUnit1TotalRam_Object = MibScalar
pp4BoardUnit1TotalRam = _Pp4BoardUnit1TotalRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 20),
    _Pp4BoardUnit1TotalRam_Type()
)
pp4BoardUnit1TotalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalRam.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalRam.setUnits("bytes")
_Pp4BoardUnit2TotalRam_Type = Integer32
_Pp4BoardUnit2TotalRam_Object = MibScalar
pp4BoardUnit2TotalRam = _Pp4BoardUnit2TotalRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 21),
    _Pp4BoardUnit2TotalRam_Type()
)
pp4BoardUnit2TotalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalRam.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalRam.setUnits("bytes")
_Pp4BoardUnit1FreeRam_Type = Integer32
_Pp4BoardUnit1FreeRam_Object = MibScalar
pp4BoardUnit1FreeRam = _Pp4BoardUnit1FreeRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 22),
    _Pp4BoardUnit1FreeRam_Type()
)
pp4BoardUnit1FreeRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeRam.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeRam.setUnits("%")
_Pp4BoardUnit2FreeRam_Type = Integer32
_Pp4BoardUnit2FreeRam_Object = MibScalar
pp4BoardUnit2FreeRam = _Pp4BoardUnit2FreeRam_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 23),
    _Pp4BoardUnit2FreeRam_Type()
)
pp4BoardUnit2FreeRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeRam.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeRam.setUnits("%")
_Pp4BoardUnit1TotalFilesystemRoot_Type = Integer32
_Pp4BoardUnit1TotalFilesystemRoot_Object = MibScalar
pp4BoardUnit1TotalFilesystemRoot = _Pp4BoardUnit1TotalFilesystemRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 24),
    _Pp4BoardUnit1TotalFilesystemRoot_Type()
)
pp4BoardUnit1TotalFilesystemRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemRoot.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemRoot.setUnits("bytes")
_Pp4BoardUnit2TotalFilesystemRoot_Type = Integer32
_Pp4BoardUnit2TotalFilesystemRoot_Object = MibScalar
pp4BoardUnit2TotalFilesystemRoot = _Pp4BoardUnit2TotalFilesystemRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 25),
    _Pp4BoardUnit2TotalFilesystemRoot_Type()
)
pp4BoardUnit2TotalFilesystemRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemRoot.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemRoot.setUnits("bytes")
_Pp4BoardUnit1TotalFilesystemTools_Type = Integer32
_Pp4BoardUnit1TotalFilesystemTools_Object = MibScalar
pp4BoardUnit1TotalFilesystemTools = _Pp4BoardUnit1TotalFilesystemTools_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 26),
    _Pp4BoardUnit1TotalFilesystemTools_Type()
)
pp4BoardUnit1TotalFilesystemTools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemTools.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemTools.setUnits("bytes")
_Pp4BoardUnit2TotalFilesystemTools_Type = Integer32
_Pp4BoardUnit2TotalFilesystemTools_Object = MibScalar
pp4BoardUnit2TotalFilesystemTools = _Pp4BoardUnit2TotalFilesystemTools_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 27),
    _Pp4BoardUnit2TotalFilesystemTools_Type()
)
pp4BoardUnit2TotalFilesystemTools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemTools.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemTools.setUnits("bytes")
_Pp4BoardUnit1TotalFilesystemConfig_Type = Integer32
_Pp4BoardUnit1TotalFilesystemConfig_Object = MibScalar
pp4BoardUnit1TotalFilesystemConfig = _Pp4BoardUnit1TotalFilesystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 28),
    _Pp4BoardUnit1TotalFilesystemConfig_Type()
)
pp4BoardUnit1TotalFilesystemConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemConfig.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemConfig.setUnits("bytes")
_Pp4BoardUnit2TotalFilesystemConfig_Type = Integer32
_Pp4BoardUnit2TotalFilesystemConfig_Object = MibScalar
pp4BoardUnit2TotalFilesystemConfig = _Pp4BoardUnit2TotalFilesystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 29),
    _Pp4BoardUnit2TotalFilesystemConfig_Type()
)
pp4BoardUnit2TotalFilesystemConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemConfig.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemConfig.setUnits("bytes")
_Pp4BoardUnit1TotalFilesystemLog_Type = Integer32
_Pp4BoardUnit1TotalFilesystemLog_Object = MibScalar
pp4BoardUnit1TotalFilesystemLog = _Pp4BoardUnit1TotalFilesystemLog_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 30),
    _Pp4BoardUnit1TotalFilesystemLog_Type()
)
pp4BoardUnit1TotalFilesystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemLog.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1TotalFilesystemLog.setUnits("bytes")
_Pp4BoardUnit2TotalFilesystemLog_Type = Integer32
_Pp4BoardUnit2TotalFilesystemLog_Object = MibScalar
pp4BoardUnit2TotalFilesystemLog = _Pp4BoardUnit2TotalFilesystemLog_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 31),
    _Pp4BoardUnit2TotalFilesystemLog_Type()
)
pp4BoardUnit2TotalFilesystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemLog.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2TotalFilesystemLog.setUnits("bytes")
_Pp4BoardUnit1FreeFilesystemRoot_Type = Integer32
_Pp4BoardUnit1FreeFilesystemRoot_Object = MibScalar
pp4BoardUnit1FreeFilesystemRoot = _Pp4BoardUnit1FreeFilesystemRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 32),
    _Pp4BoardUnit1FreeFilesystemRoot_Type()
)
pp4BoardUnit1FreeFilesystemRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemRoot.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemRoot.setUnits("%")
_Pp4BoardUnit2FreeFilesystemRoot_Type = Integer32
_Pp4BoardUnit2FreeFilesystemRoot_Object = MibScalar
pp4BoardUnit2FreeFilesystemRoot = _Pp4BoardUnit2FreeFilesystemRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 33),
    _Pp4BoardUnit2FreeFilesystemRoot_Type()
)
pp4BoardUnit2FreeFilesystemRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemRoot.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemRoot.setUnits("%")
_Pp4BoardUnit1FreeFilesystemTools_Type = Integer32
_Pp4BoardUnit1FreeFilesystemTools_Object = MibScalar
pp4BoardUnit1FreeFilesystemTools = _Pp4BoardUnit1FreeFilesystemTools_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 34),
    _Pp4BoardUnit1FreeFilesystemTools_Type()
)
pp4BoardUnit1FreeFilesystemTools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemTools.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemTools.setUnits("%")
_Pp4BoardUnit2FreeFilesystemTools_Type = Integer32
_Pp4BoardUnit2FreeFilesystemTools_Object = MibScalar
pp4BoardUnit2FreeFilesystemTools = _Pp4BoardUnit2FreeFilesystemTools_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 35),
    _Pp4BoardUnit2FreeFilesystemTools_Type()
)
pp4BoardUnit2FreeFilesystemTools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemTools.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemTools.setUnits("%")
_Pp4BoardUnit1FreeFilesystemConfig_Type = Integer32
_Pp4BoardUnit1FreeFilesystemConfig_Object = MibScalar
pp4BoardUnit1FreeFilesystemConfig = _Pp4BoardUnit1FreeFilesystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 36),
    _Pp4BoardUnit1FreeFilesystemConfig_Type()
)
pp4BoardUnit1FreeFilesystemConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemConfig.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemConfig.setUnits("%")
_Pp4BoardUnit2FreeFilesystemConfig_Type = Integer32
_Pp4BoardUnit2FreeFilesystemConfig_Object = MibScalar
pp4BoardUnit2FreeFilesystemConfig = _Pp4BoardUnit2FreeFilesystemConfig_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 37),
    _Pp4BoardUnit2FreeFilesystemConfig_Type()
)
pp4BoardUnit2FreeFilesystemConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemConfig.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemConfig.setUnits("%")
_Pp4BoardUnit1FreeFilesystemLog_Type = Integer32
_Pp4BoardUnit1FreeFilesystemLog_Object = MibScalar
pp4BoardUnit1FreeFilesystemLog = _Pp4BoardUnit1FreeFilesystemLog_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 38),
    _Pp4BoardUnit1FreeFilesystemLog_Type()
)
pp4BoardUnit1FreeFilesystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemLog.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit1FreeFilesystemLog.setUnits("%")
_Pp4BoardUnit2FreeFilesystemLog_Type = Integer32
_Pp4BoardUnit2FreeFilesystemLog_Object = MibScalar
pp4BoardUnit2FreeFilesystemLog = _Pp4BoardUnit2FreeFilesystemLog_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 30, 39),
    _Pp4BoardUnit2FreeFilesystemLog_Type()
)
pp4BoardUnit2FreeFilesystemLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemLog.setStatus("current")
if mibBuilder.loadTexts:
    pp4BoardUnit2FreeFilesystemLog.setUnits("%")
_Pp4FeederState_ObjectIdentity = ObjectIdentity
pp4FeederState = _Pp4FeederState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31)
)
_Pp4Feeder1Status_Type = Pp4FeederStatus
_Pp4Feeder1Status_Object = MibScalar
pp4Feeder1Status = _Pp4Feeder1Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 1),
    _Pp4Feeder1Status_Type()
)
pp4Feeder1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder1Status.setStatus("current")
_Pp4Feeder1Active_Type = Pp4FeederActive
_Pp4Feeder1Active_Object = MibScalar
pp4Feeder1Active = _Pp4Feeder1Active_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 2),
    _Pp4Feeder1Active_Type()
)
pp4Feeder1Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder1Active.setStatus("current")
_Pp4Feeder1Polarity_Type = Pp4FeederPolarity
_Pp4Feeder1Polarity_Object = MibScalar
pp4Feeder1Polarity = _Pp4Feeder1Polarity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 3),
    _Pp4Feeder1Polarity_Type()
)
pp4Feeder1Polarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder1Polarity.setStatus("current")
_Pp4Feeder1Current_Type = DisplayString
_Pp4Feeder1Current_Object = MibScalar
pp4Feeder1Current = _Pp4Feeder1Current_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 4),
    _Pp4Feeder1Current_Type()
)
pp4Feeder1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder1Current.setStatus("current")
_Pp4Feeder1Voltage_Type = DisplayString
_Pp4Feeder1Voltage_Object = MibScalar
pp4Feeder1Voltage = _Pp4Feeder1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 5),
    _Pp4Feeder1Voltage_Type()
)
pp4Feeder1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder1Voltage.setStatus("current")
_Pp4Feeder2Status_Type = Pp4FeederStatus
_Pp4Feeder2Status_Object = MibScalar
pp4Feeder2Status = _Pp4Feeder2Status_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 6),
    _Pp4Feeder2Status_Type()
)
pp4Feeder2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder2Status.setStatus("current")
_Pp4Feeder2Active_Type = Pp4FeederActive
_Pp4Feeder2Active_Object = MibScalar
pp4Feeder2Active = _Pp4Feeder2Active_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 7),
    _Pp4Feeder2Active_Type()
)
pp4Feeder2Active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder2Active.setStatus("current")
_Pp4Feeder2Polarity_Type = Pp4FeederPolarity
_Pp4Feeder2Polarity_Object = MibScalar
pp4Feeder2Polarity = _Pp4Feeder2Polarity_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 8),
    _Pp4Feeder2Polarity_Type()
)
pp4Feeder2Polarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder2Polarity.setStatus("current")
_Pp4Feeder2Current_Type = DisplayString
_Pp4Feeder2Current_Object = MibScalar
pp4Feeder2Current = _Pp4Feeder2Current_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 9),
    _Pp4Feeder2Current_Type()
)
pp4Feeder2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder2Current.setStatus("current")
_Pp4Feeder2Voltage_Type = DisplayString
_Pp4Feeder2Voltage_Object = MibScalar
pp4Feeder2Voltage = _Pp4Feeder2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 10),
    _Pp4Feeder2Voltage_Type()
)
pp4Feeder2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4Feeder2Voltage.setStatus("current")
_Pp4StationVoltage_Type = DisplayString
_Pp4StationVoltage_Object = MibScalar
pp4StationVoltage = _Pp4StationVoltage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 31, 11),
    _Pp4StationVoltage_Type()
)
pp4StationVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4StationVoltage.setStatus("current")
_Pp4Firmware_ObjectIdentity = ObjectIdentity
pp4Firmware = _Pp4Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35)
)
_Pp4FirmwareTable_Object = MibTable
pp4FirmwareTable = _Pp4FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1)
)
if mibBuilder.loadTexts:
    pp4FirmwareTable.setStatus("current")
_Pp4FirmwareEntry_Object = MibTableRow
pp4FirmwareEntry = _Pp4FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1, 1)
)
pp4FirmwareEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4FirmwareBoardType"),
    (0, "ELTEX-PP4", "pp4FirmwareIndex"),
)
if mibBuilder.loadTexts:
    pp4FirmwareEntry.setStatus("current")
_Pp4FirmwareBoardType_Type = Pp4SlotBoardType
_Pp4FirmwareBoardType_Object = MibTableColumn
pp4FirmwareBoardType = _Pp4FirmwareBoardType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1, 1, 1),
    _Pp4FirmwareBoardType_Type()
)
pp4FirmwareBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4FirmwareBoardType.setStatus("current")
_Pp4FirmwareIndex_Type = Unsigned32
_Pp4FirmwareIndex_Object = MibTableColumn
pp4FirmwareIndex = _Pp4FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1, 1, 2),
    _Pp4FirmwareIndex_Type()
)
pp4FirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4FirmwareIndex.setStatus("current")
_Pp4FirmwareVersion_Type = DisplayString
_Pp4FirmwareVersion_Object = MibTableColumn
pp4FirmwareVersion = _Pp4FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1, 1, 3),
    _Pp4FirmwareVersion_Type()
)
pp4FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4FirmwareVersion.setStatus("current")
_Pp4FirmwareDelete_Type = Unsigned32
_Pp4FirmwareDelete_Object = MibTableColumn
pp4FirmwareDelete = _Pp4FirmwareDelete_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 1, 1, 4),
    _Pp4FirmwareDelete_Type()
)
pp4FirmwareDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareDelete.setStatus("current")
_Pp4DefaultFirmware_ObjectIdentity = ObjectIdentity
pp4DefaultFirmware = _Pp4DefaultFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 2)
)
_Pp4DefaultFirmwareELC_Type = Unsigned32
_Pp4DefaultFirmwareELC_Object = MibScalar
pp4DefaultFirmwareELC = _Pp4DefaultFirmwareELC_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 2, 1),
    _Pp4DefaultFirmwareELC_Type()
)
pp4DefaultFirmwareELC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4DefaultFirmwareELC.setStatus("current")
_Pp4DefaultFirmwarePLC_Type = Unsigned32
_Pp4DefaultFirmwarePLC_Object = MibScalar
pp4DefaultFirmwarePLC = _Pp4DefaultFirmwarePLC_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 2, 2),
    _Pp4DefaultFirmwarePLC_Type()
)
pp4DefaultFirmwarePLC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4DefaultFirmwarePLC.setStatus("current")
_Pp4ShelfConfigTable_Object = MibTable
pp4ShelfConfigTable = _Pp4ShelfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 3)
)
if mibBuilder.loadTexts:
    pp4ShelfConfigTable.setStatus("current")
_Pp4ShelfConfigEntry_Object = MibTableRow
pp4ShelfConfigEntry = _Pp4ShelfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 3, 1)
)
pp4ShelfConfigEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4ShelfConfigSlot"),
)
if mibBuilder.loadTexts:
    pp4ShelfConfigEntry.setStatus("current")


class _Pp4ShelfConfigSlot_Type(Integer32):
    """Custom type pp4ShelfConfigSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Pp4ShelfConfigSlot_Type.__name__ = "Integer32"
_Pp4ShelfConfigSlot_Object = MibTableColumn
pp4ShelfConfigSlot = _Pp4ShelfConfigSlot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 3, 1, 1),
    _Pp4ShelfConfigSlot_Type()
)
pp4ShelfConfigSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ShelfConfigSlot.setStatus("current")
_Pp4ShelfConfigBoardType_Type = Pp4SlotBoardType
_Pp4ShelfConfigBoardType_Object = MibTableColumn
pp4ShelfConfigBoardType = _Pp4ShelfConfigBoardType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 3, 1, 2),
    _Pp4ShelfConfigBoardType_Type()
)
pp4ShelfConfigBoardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4ShelfConfigBoardType.setStatus("current")
_Pp4ShelfConfigFirmwareVersion_Type = Pp4SlotFirmwareVersion
_Pp4ShelfConfigFirmwareVersion_Object = MibTableColumn
pp4ShelfConfigFirmwareVersion = _Pp4ShelfConfigFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 3, 1, 3),
    _Pp4ShelfConfigFirmwareVersion_Type()
)
pp4ShelfConfigFirmwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4ShelfConfigFirmwareVersion.setStatus("current")
_Pp4BootVarTable_Object = MibTable
pp4BootVarTable = _Pp4BootVarTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4)
)
if mibBuilder.loadTexts:
    pp4BootVarTable.setStatus("current")
_Pp4BootVarEntry_Object = MibTableRow
pp4BootVarEntry = _Pp4BootVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1)
)
pp4BootVarEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4BootVarUnit"),
    (0, "ELTEX-PP4", "pp4BootVarIndex"),
)
if mibBuilder.loadTexts:
    pp4BootVarEntry.setStatus("current")


class _Pp4BootVarUnit_Type(Integer32):
    """Custom type pp4BootVarUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pp4BootVarUnit_Type.__name__ = "Integer32"
_Pp4BootVarUnit_Object = MibTableColumn
pp4BootVarUnit = _Pp4BootVarUnit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1, 1),
    _Pp4BootVarUnit_Type()
)
pp4BootVarUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4BootVarUnit.setStatus("current")


class _Pp4BootVarIndex_Type(Integer32):
    """Custom type pp4BootVarIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Pp4BootVarIndex_Type.__name__ = "Integer32"
_Pp4BootVarIndex_Object = MibTableColumn
pp4BootVarIndex = _Pp4BootVarIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1, 2),
    _Pp4BootVarIndex_Type()
)
pp4BootVarIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4BootVarIndex.setStatus("current")
_Pp4BootVarValid_Type = TruthValue
_Pp4BootVarValid_Object = MibTableColumn
pp4BootVarValid = _Pp4BootVarValid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1, 3),
    _Pp4BootVarValid_Type()
)
pp4BootVarValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BootVarValid.setStatus("current")
_Pp4BootVarTimestamp_Type = DisplayString
_Pp4BootVarTimestamp_Object = MibTableColumn
pp4BootVarTimestamp = _Pp4BootVarTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1, 4),
    _Pp4BootVarTimestamp_Type()
)
pp4BootVarTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BootVarTimestamp.setStatus("current")
_Pp4BootVarVersionString_Type = DisplayString
_Pp4BootVarVersionString_Object = MibTableColumn
pp4BootVarVersionString = _Pp4BootVarVersionString_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 4, 1, 5),
    _Pp4BootVarVersionString_Type()
)
pp4BootVarVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4BootVarVersionString.setStatus("current")
_Pp4UnitsFirmwareTable_Object = MibTable
pp4UnitsFirmwareTable = _Pp4UnitsFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5)
)
if mibBuilder.loadTexts:
    pp4UnitsFirmwareTable.setStatus("current")
_Pp4UnitsFirmwareEntry_Object = MibTableRow
pp4UnitsFirmwareEntry = _Pp4UnitsFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1)
)
pp4UnitsFirmwareEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4BootVarUnit"),
)
if mibBuilder.loadTexts:
    pp4UnitsFirmwareEntry.setStatus("current")
_Pp4UnitsStatus_Type = Pp4FirmwareUnitStatus
_Pp4UnitsStatus_Object = MibTableColumn
pp4UnitsStatus = _Pp4UnitsStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1, 1),
    _Pp4UnitsStatus_Type()
)
pp4UnitsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4UnitsStatus.setStatus("current")
_Pp4UnitsActivePartition_Type = Integer32
_Pp4UnitsActivePartition_Object = MibTableColumn
pp4UnitsActivePartition = _Pp4UnitsActivePartition_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1, 2),
    _Pp4UnitsActivePartition_Type()
)
pp4UnitsActivePartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UnitsActivePartition.setStatus("current")
_Pp4UnitsFallbackPartition_Type = Integer32
_Pp4UnitsFallbackPartition_Object = MibTableColumn
pp4UnitsFallbackPartition = _Pp4UnitsFallbackPartition_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1, 3),
    _Pp4UnitsFallbackPartition_Type()
)
pp4UnitsFallbackPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UnitsFallbackPartition.setStatus("current")
_Pp4UnitsRunningPartition_Type = Integer32
_Pp4UnitsRunningPartition_Object = MibTableColumn
pp4UnitsRunningPartition = _Pp4UnitsRunningPartition_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1, 4),
    _Pp4UnitsRunningPartition_Type()
)
pp4UnitsRunningPartition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4UnitsRunningPartition.setStatus("current")
_Pp4UnitsConfirm_Type = TruthValue
_Pp4UnitsConfirm_Object = MibTableColumn
pp4UnitsConfirm = _Pp4UnitsConfirm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 5, 1, 5),
    _Pp4UnitsConfirm_Type()
)
pp4UnitsConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UnitsConfirm.setStatus("current")
_Pp4FirmwareDeleteUnused_Type = Unsigned32
_Pp4FirmwareDeleteUnused_Object = MibScalar
pp4FirmwareDeleteUnused = _Pp4FirmwareDeleteUnused_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 6),
    _Pp4FirmwareDeleteUnused_Type()
)
pp4FirmwareDeleteUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareDeleteUnused.setStatus("current")
_Pp4FirmwareUpdate_ObjectIdentity = ObjectIdentity
pp4FirmwareUpdate = _Pp4FirmwareUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10)
)
_Pp4FirmwareUpdateFileName_Type = DisplayString
_Pp4FirmwareUpdateFileName_Object = MibScalar
pp4FirmwareUpdateFileName = _Pp4FirmwareUpdateFileName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 1),
    _Pp4FirmwareUpdateFileName_Type()
)
pp4FirmwareUpdateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateFileName.setStatus("current")
_Pp4FirmwareUpdateIpAddress_Type = IpAddress
_Pp4FirmwareUpdateIpAddress_Object = MibScalar
pp4FirmwareUpdateIpAddress = _Pp4FirmwareUpdateIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 2),
    _Pp4FirmwareUpdateIpAddress_Type()
)
pp4FirmwareUpdateIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateIpAddress.setStatus("current")
_Pp4FirmwareUpdateConfigName_Type = DisplayString
_Pp4FirmwareUpdateConfigName_Object = MibScalar
pp4FirmwareUpdateConfigName = _Pp4FirmwareUpdateConfigName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 3),
    _Pp4FirmwareUpdateConfigName_Type()
)
pp4FirmwareUpdateConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateConfigName.setStatus("current")
_Pp4FirmwareUpdateSwitchVersion_Type = TruthValue
_Pp4FirmwareUpdateSwitchVersion_Object = MibScalar
pp4FirmwareUpdateSwitchVersion = _Pp4FirmwareUpdateSwitchVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 4),
    _Pp4FirmwareUpdateSwitchVersion_Type()
)
pp4FirmwareUpdateSwitchVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateSwitchVersion.setStatus("current")
_Pp4FirmwareUpdateNeedRestart_Type = TruthValue
_Pp4FirmwareUpdateNeedRestart_Object = MibScalar
pp4FirmwareUpdateNeedRestart = _Pp4FirmwareUpdateNeedRestart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 5),
    _Pp4FirmwareUpdateNeedRestart_Type()
)
pp4FirmwareUpdateNeedRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateNeedRestart.setStatus("current")
_Pp4FirmwareUpdateNSSU_Type = TruthValue
_Pp4FirmwareUpdateNSSU_Object = MibScalar
pp4FirmwareUpdateNSSU = _Pp4FirmwareUpdateNSSU_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 6),
    _Pp4FirmwareUpdateNSSU_Type()
)
pp4FirmwareUpdateNSSU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateNSSU.setStatus("current")
_Pp4FirmwareUpdateConfigIpAddress_Type = IpAddress
_Pp4FirmwareUpdateConfigIpAddress_Object = MibScalar
pp4FirmwareUpdateConfigIpAddress = _Pp4FirmwareUpdateConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 7),
    _Pp4FirmwareUpdateConfigIpAddress_Type()
)
pp4FirmwareUpdateConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateConfigIpAddress.setStatus("current")


class _Pp4FirmwareUpdateProtocol_Type(Integer32):
    """Custom type pp4FirmwareUpdateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 2),
          ("tftp", 1))
    )


_Pp4FirmwareUpdateProtocol_Type.__name__ = "Integer32"
_Pp4FirmwareUpdateProtocol_Object = MibScalar
pp4FirmwareUpdateProtocol = _Pp4FirmwareUpdateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 8),
    _Pp4FirmwareUpdateProtocol_Type()
)
pp4FirmwareUpdateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateProtocol.setStatus("current")
_Pp4FirmwareUpdatePort_Type = Unsigned32
_Pp4FirmwareUpdatePort_Object = MibScalar
pp4FirmwareUpdatePort = _Pp4FirmwareUpdatePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 9),
    _Pp4FirmwareUpdatePort_Type()
)
pp4FirmwareUpdatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdatePort.setStatus("current")
_Pp4FirmwareUpdateAction_Type = Unsigned32
_Pp4FirmwareUpdateAction_Object = MibScalar
pp4FirmwareUpdateAction = _Pp4FirmwareUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 10),
    _Pp4FirmwareUpdateAction_Type()
)
pp4FirmwareUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateAction.setStatus("current")


class _Pp4FirmwareUpdateConfigProtocol_Type(Integer32):
    """Custom type pp4FirmwareUpdateConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("http", 2),
          ("tftp", 1))
    )


_Pp4FirmwareUpdateConfigProtocol_Type.__name__ = "Integer32"
_Pp4FirmwareUpdateConfigProtocol_Object = MibScalar
pp4FirmwareUpdateConfigProtocol = _Pp4FirmwareUpdateConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 11),
    _Pp4FirmwareUpdateConfigProtocol_Type()
)
pp4FirmwareUpdateConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateConfigProtocol.setStatus("current")
_Pp4FirmwareUpdateConfigPort_Type = Unsigned32
_Pp4FirmwareUpdateConfigPort_Object = MibScalar
pp4FirmwareUpdateConfigPort = _Pp4FirmwareUpdateConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 12),
    _Pp4FirmwareUpdateConfigPort_Type()
)
pp4FirmwareUpdateConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateConfigPort.setStatus("current")
_Pp4FirmwareUpdateConfirm_Type = Unsigned32
_Pp4FirmwareUpdateConfirm_Object = MibScalar
pp4FirmwareUpdateConfirm = _Pp4FirmwareUpdateConfirm_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 35, 10, 20),
    _Pp4FirmwareUpdateConfirm_Type()
)
pp4FirmwareUpdateConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4FirmwareUpdateConfirm.setStatus("current")
_Pp4AlarmsJournal_ObjectIdentity = ObjectIdentity
pp4AlarmsJournal = _Pp4AlarmsJournal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 40)
)
_Pp4AlarmsJournalCleanJournal_Type = Unsigned32
_Pp4AlarmsJournalCleanJournal_Object = MibScalar
pp4AlarmsJournalCleanJournal = _Pp4AlarmsJournalCleanJournal_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 40, 1),
    _Pp4AlarmsJournalCleanJournal_Type()
)
pp4AlarmsJournalCleanJournal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AlarmsJournalCleanJournal.setStatus("current")
_Pp4UserTable_Object = MibTable
pp4UserTable = _Pp4UserTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50)
)
if mibBuilder.loadTexts:
    pp4UserTable.setStatus("current")
_Pp4UserEntry_Object = MibTableRow
pp4UserEntry = _Pp4UserEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1)
)
pp4UserEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4UserName"),
)
if mibBuilder.loadTexts:
    pp4UserEntry.setStatus("current")
_Pp4UserName_Type = DisplayString
_Pp4UserName_Object = MibTableColumn
pp4UserName = _Pp4UserName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1, 1),
    _Pp4UserName_Type()
)
pp4UserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4UserName.setStatus("current")


class _Pp4UserPermissions_Type(OctetString):
    """Custom type pp4UserPermissions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Pp4UserPermissions_Type.__name__ = "OctetString"
_Pp4UserPermissions_Object = MibTableColumn
pp4UserPermissions = _Pp4UserPermissions_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1, 2),
    _Pp4UserPermissions_Type()
)
pp4UserPermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UserPermissions.setStatus("current")
_Pp4UserOldPassword_Type = DisplayString
_Pp4UserOldPassword_Object = MibTableColumn
pp4UserOldPassword = _Pp4UserOldPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1, 3),
    _Pp4UserOldPassword_Type()
)
pp4UserOldPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UserOldPassword.setStatus("current")
_Pp4UserNewPassword_Type = DisplayString
_Pp4UserNewPassword_Object = MibTableColumn
pp4UserNewPassword = _Pp4UserNewPassword_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1, 4),
    _Pp4UserNewPassword_Type()
)
pp4UserNewPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UserNewPassword.setStatus("current")
_Pp4UserRowStatus_Type = RowStatus
_Pp4UserRowStatus_Object = MibTableColumn
pp4UserRowStatus = _Pp4UserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 50, 1, 5),
    _Pp4UserRowStatus_Type()
)
pp4UserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4UserRowStatus.setStatus("current")
_Pp4Privileges_ObjectIdentity = ObjectIdentity
pp4Privileges = _Pp4Privileges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51)
)
_Pp4PrivilegesNamesTable_Object = MibTable
pp4PrivilegesNamesTable = _Pp4PrivilegesNamesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 1)
)
if mibBuilder.loadTexts:
    pp4PrivilegesNamesTable.setStatus("current")
_Pp4PrivilegesNamesEntry_Object = MibTableRow
pp4PrivilegesNamesEntry = _Pp4PrivilegesNamesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 1, 1)
)
pp4PrivilegesNamesEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4PrivilegesNamesIndex"),
)
if mibBuilder.loadTexts:
    pp4PrivilegesNamesEntry.setStatus("current")
_Pp4PrivilegesNamesIndex_Type = Unsigned32
_Pp4PrivilegesNamesIndex_Object = MibTableColumn
pp4PrivilegesNamesIndex = _Pp4PrivilegesNamesIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 1, 1, 1),
    _Pp4PrivilegesNamesIndex_Type()
)
pp4PrivilegesNamesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4PrivilegesNamesIndex.setStatus("current")
_Pp4PrivilegesNamesName_Type = DisplayString
_Pp4PrivilegesNamesName_Object = MibTableColumn
pp4PrivilegesNamesName = _Pp4PrivilegesNamesName_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 1, 1, 2),
    _Pp4PrivilegesNamesName_Type()
)
pp4PrivilegesNamesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4PrivilegesNamesName.setStatus("current")
_Pp4PrivilegesLevelsTable_Object = MibTable
pp4PrivilegesLevelsTable = _Pp4PrivilegesLevelsTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 2)
)
if mibBuilder.loadTexts:
    pp4PrivilegesLevelsTable.setStatus("current")
_Pp4PrivilegesLevelsEntry_Object = MibTableRow
pp4PrivilegesLevelsEntry = _Pp4PrivilegesLevelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 2, 1)
)
pp4PrivilegesLevelsEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4PrivilegesLevelsLevel"),
)
if mibBuilder.loadTexts:
    pp4PrivilegesLevelsEntry.setStatus("current")
_Pp4PrivilegesLevelsLevel_Type = Unsigned32
_Pp4PrivilegesLevelsLevel_Object = MibTableColumn
pp4PrivilegesLevelsLevel = _Pp4PrivilegesLevelsLevel_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 2, 1, 1),
    _Pp4PrivilegesLevelsLevel_Type()
)
pp4PrivilegesLevelsLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4PrivilegesLevelsLevel.setStatus("current")


class _Pp4PrivilegesLevelsAllowed_Type(OctetString):
    """Custom type pp4PrivilegesLevelsAllowed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Pp4PrivilegesLevelsAllowed_Type.__name__ = "OctetString"
_Pp4PrivilegesLevelsAllowed_Object = MibTableColumn
pp4PrivilegesLevelsAllowed = _Pp4PrivilegesLevelsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 51, 2, 1, 2),
    _Pp4PrivilegesLevelsAllowed_Type()
)
pp4PrivilegesLevelsAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4PrivilegesLevelsAllowed.setStatus("current")
_Pp4IGMPConfig_ObjectIdentity = ObjectIdentity
pp4IGMPConfig = _Pp4IGMPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55)
)
_Pp4IGMPSnoopingEnable_Type = TruthValue
_Pp4IGMPSnoopingEnable_Object = MibScalar
pp4IGMPSnoopingEnable = _Pp4IGMPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 1),
    _Pp4IGMPSnoopingEnable_Type()
)
pp4IGMPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPSnoopingEnable.setStatus("current")
_Pp4IGMPProxyReportEnable_Type = TruthValue
_Pp4IGMPProxyReportEnable_Object = MibScalar
pp4IGMPProxyReportEnable = _Pp4IGMPProxyReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 2),
    _Pp4IGMPProxyReportEnable_Type()
)
pp4IGMPProxyReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportEnable.setStatus("current")
_Pp4MLDSnoopingEnable_Type = TruthValue
_Pp4MLDSnoopingEnable_Object = MibScalar
pp4MLDSnoopingEnable = _Pp4MLDSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 5),
    _Pp4MLDSnoopingEnable_Type()
)
pp4MLDSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDSnoopingEnable.setStatus("current")
_Pp4MLDProxyReportEnable_Type = TruthValue
_Pp4MLDProxyReportEnable_Object = MibScalar
pp4MLDProxyReportEnable = _Pp4MLDProxyReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 6),
    _Pp4MLDProxyReportEnable_Type()
)
pp4MLDProxyReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyReportEnable.setStatus("current")
_Pp4IGMPSnoopingVLANTable_Object = MibTable
pp4IGMPSnoopingVLANTable = _Pp4IGMPSnoopingVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10)
)
if mibBuilder.loadTexts:
    pp4IGMPSnoopingVLANTable.setStatus("current")
_Pp4IGMPSnoopingVLANEntry_Object = MibTableRow
pp4IGMPSnoopingVLANEntry = _Pp4IGMPSnoopingVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1)
)
pp4IGMPSnoopingVLANEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4IGMPSnoopingVLANVID"),
)
if mibBuilder.loadTexts:
    pp4IGMPSnoopingVLANEntry.setStatus("current")
_Pp4IGMPSnoopingVLANVID_Type = Unsigned32
_Pp4IGMPSnoopingVLANVID_Object = MibTableColumn
pp4IGMPSnoopingVLANVID = _Pp4IGMPSnoopingVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1, 1),
    _Pp4IGMPSnoopingVLANVID_Type()
)
pp4IGMPSnoopingVLANVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4IGMPSnoopingVLANVID.setStatus("current")
_Pp4IGMPSnoopingVLANEnabled_Type = TruthValue
_Pp4IGMPSnoopingVLANEnabled_Object = MibTableColumn
pp4IGMPSnoopingVLANEnabled = _Pp4IGMPSnoopingVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1, 2),
    _Pp4IGMPSnoopingVLANEnabled_Type()
)
pp4IGMPSnoopingVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPSnoopingVLANEnabled.setStatus("current")
_Pp4IGMPSnoopingVLANQuerierEnabled_Type = TruthValue
_Pp4IGMPSnoopingVLANQuerierEnabled_Object = MibTableColumn
pp4IGMPSnoopingVLANQuerierEnabled = _Pp4IGMPSnoopingVLANQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1, 3),
    _Pp4IGMPSnoopingVLANQuerierEnabled_Type()
)
pp4IGMPSnoopingVLANQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPSnoopingVLANQuerierEnabled.setStatus("current")
_Pp4MLDSnoopingVLANEnabled_Type = TruthValue
_Pp4MLDSnoopingVLANEnabled_Object = MibTableColumn
pp4MLDSnoopingVLANEnabled = _Pp4MLDSnoopingVLANEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1, 4),
    _Pp4MLDSnoopingVLANEnabled_Type()
)
pp4MLDSnoopingVLANEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDSnoopingVLANEnabled.setStatus("current")
_Pp4MLDSnoopingVLANQuerierEnabled_Type = TruthValue
_Pp4MLDSnoopingVLANQuerierEnabled_Object = MibTableColumn
pp4MLDSnoopingVLANQuerierEnabled = _Pp4MLDSnoopingVLANQuerierEnabled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 10, 1, 5),
    _Pp4MLDSnoopingVLANQuerierEnabled_Type()
)
pp4MLDSnoopingVLANQuerierEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDSnoopingVLANQuerierEnabled.setStatus("current")
_Pp4IGMPProxyReportRangesTable_Object = MibTable
pp4IGMPProxyReportRangesTable = _Pp4IGMPProxyReportRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20)
)
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesTable.setStatus("current")
_Pp4IGMPProxyReportRangesEntry_Object = MibTableRow
pp4IGMPProxyReportRangesEntry = _Pp4IGMPProxyReportRangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1)
)
pp4IGMPProxyReportRangesEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4IGMPProxyReportRangesID"),
)
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesEntry.setStatus("current")
_Pp4IGMPProxyReportRangesID_Type = Unsigned32
_Pp4IGMPProxyReportRangesID_Object = MibTableColumn
pp4IGMPProxyReportRangesID = _Pp4IGMPProxyReportRangesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 1),
    _Pp4IGMPProxyReportRangesID_Type()
)
pp4IGMPProxyReportRangesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesID.setStatus("current")
_Pp4IGMPProxyReportRangesStart_Type = IpAddress
_Pp4IGMPProxyReportRangesStart_Object = MibTableColumn
pp4IGMPProxyReportRangesStart = _Pp4IGMPProxyReportRangesStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 2),
    _Pp4IGMPProxyReportRangesStart_Type()
)
pp4IGMPProxyReportRangesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesStart.setStatus("current")
_Pp4IGMPProxyReportRangesEnd_Type = IpAddress
_Pp4IGMPProxyReportRangesEnd_Object = MibTableColumn
pp4IGMPProxyReportRangesEnd = _Pp4IGMPProxyReportRangesEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 3),
    _Pp4IGMPProxyReportRangesEnd_Type()
)
pp4IGMPProxyReportRangesEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesEnd.setStatus("current")
_Pp4IGMPProxyReportRangesFromVLAN_Type = Unsigned32
_Pp4IGMPProxyReportRangesFromVLAN_Object = MibTableColumn
pp4IGMPProxyReportRangesFromVLAN = _Pp4IGMPProxyReportRangesFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 4),
    _Pp4IGMPProxyReportRangesFromVLAN_Type()
)
pp4IGMPProxyReportRangesFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesFromVLAN.setStatus("current")
_Pp4IGMPProxyReportRangesToVLAN_Type = Unsigned32
_Pp4IGMPProxyReportRangesToVLAN_Object = MibTableColumn
pp4IGMPProxyReportRangesToVLAN = _Pp4IGMPProxyReportRangesToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 5),
    _Pp4IGMPProxyReportRangesToVLAN_Type()
)
pp4IGMPProxyReportRangesToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyReportRangesToVLAN.setStatus("current")
_Pp4IGMPProxyRowStatus_Type = RowStatus
_Pp4IGMPProxyRowStatus_Object = MibTableColumn
pp4IGMPProxyRowStatus = _Pp4IGMPProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 20, 1, 10),
    _Pp4IGMPProxyRowStatus_Type()
)
pp4IGMPProxyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4IGMPProxyRowStatus.setStatus("current")
_Pp4MLDProxyReportRangesTable_Object = MibTable
pp4MLDProxyReportRangesTable = _Pp4MLDProxyReportRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25)
)
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesTable.setStatus("current")
_Pp4MLDProxyReportRangesEntry_Object = MibTableRow
pp4MLDProxyReportRangesEntry = _Pp4MLDProxyReportRangesEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1)
)
pp4MLDProxyReportRangesEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4MLDProxyReportRangesID"),
)
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesEntry.setStatus("current")
_Pp4MLDProxyReportRangesID_Type = Unsigned32
_Pp4MLDProxyReportRangesID_Object = MibTableColumn
pp4MLDProxyReportRangesID = _Pp4MLDProxyReportRangesID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 1),
    _Pp4MLDProxyReportRangesID_Type()
)
pp4MLDProxyReportRangesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesID.setStatus("current")
_Pp4MLDProxyReportRangesStart_Type = Ipv6Address
_Pp4MLDProxyReportRangesStart_Object = MibTableColumn
pp4MLDProxyReportRangesStart = _Pp4MLDProxyReportRangesStart_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 2),
    _Pp4MLDProxyReportRangesStart_Type()
)
pp4MLDProxyReportRangesStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesStart.setStatus("current")
_Pp4MLDProxyReportRangesEnd_Type = Ipv6Address
_Pp4MLDProxyReportRangesEnd_Object = MibTableColumn
pp4MLDProxyReportRangesEnd = _Pp4MLDProxyReportRangesEnd_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 3),
    _Pp4MLDProxyReportRangesEnd_Type()
)
pp4MLDProxyReportRangesEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesEnd.setStatus("current")
_Pp4MLDProxyReportRangesFromVLAN_Type = Unsigned32
_Pp4MLDProxyReportRangesFromVLAN_Object = MibTableColumn
pp4MLDProxyReportRangesFromVLAN = _Pp4MLDProxyReportRangesFromVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 4),
    _Pp4MLDProxyReportRangesFromVLAN_Type()
)
pp4MLDProxyReportRangesFromVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesFromVLAN.setStatus("current")
_Pp4MLDProxyReportRangesToVLAN_Type = Unsigned32
_Pp4MLDProxyReportRangesToVLAN_Object = MibTableColumn
pp4MLDProxyReportRangesToVLAN = _Pp4MLDProxyReportRangesToVLAN_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 5),
    _Pp4MLDProxyReportRangesToVLAN_Type()
)
pp4MLDProxyReportRangesToVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyReportRangesToVLAN.setStatus("current")
_Pp4MLDProxyRowStatus_Type = RowStatus
_Pp4MLDProxyRowStatus_Object = MibTableColumn
pp4MLDProxyRowStatus = _Pp4MLDProxyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 55, 25, 1, 10),
    _Pp4MLDProxyRowStatus_Type()
)
pp4MLDProxyRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4MLDProxyRowStatus.setStatus("current")
_Pp4QOSConfig_ObjectIdentity = ObjectIdentity
pp4QOSConfig = _Pp4QOSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60)
)


class _Pp4QOSDefaultQueue_Type(Unsigned32):
    """Custom type pp4QOSDefaultQueue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_Pp4QOSDefaultQueue_Type.__name__ = "Unsigned32"
_Pp4QOSDefaultQueue_Object = MibScalar
pp4QOSDefaultQueue = _Pp4QOSDefaultQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 1),
    _Pp4QOSDefaultQueue_Type()
)
pp4QOSDefaultQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4QOSDefaultQueue.setStatus("current")


class _Pp4QOSType_Type(Integer32):
    """Custom type pp4QOSType based on Integer32"""
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
        *(("type8021p", 1),
          ("typeAllEqual", 0),
          ("typeDscpTos", 2),
          ("typeDscpTos8021p", 3))
    )


_Pp4QOSType_Type.__name__ = "Integer32"
_Pp4QOSType_Object = MibScalar
pp4QOSType = _Pp4QOSType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 2),
    _Pp4QOSType_Type()
)
pp4QOSType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4QOSType.setStatus("current")
_Pp4QOS8021pMappingTable_Object = MibTable
pp4QOS8021pMappingTable = _Pp4QOS8021pMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 3)
)
if mibBuilder.loadTexts:
    pp4QOS8021pMappingTable.setStatus("current")
_Pp4QOS8021pMappingEntry_Object = MibTableRow
pp4QOS8021pMappingEntry = _Pp4QOS8021pMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 3, 1)
)
pp4QOS8021pMappingEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4QOS8021pMappingQueue"),
)
if mibBuilder.loadTexts:
    pp4QOS8021pMappingEntry.setStatus("current")
_Pp4QOS8021pMappingQueue_Type = Unsigned32
_Pp4QOS8021pMappingQueue_Object = MibTableColumn
pp4QOS8021pMappingQueue = _Pp4QOS8021pMappingQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 3, 1, 1),
    _Pp4QOS8021pMappingQueue_Type()
)
pp4QOS8021pMappingQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4QOS8021pMappingQueue.setStatus("current")


class _Pp4QOS8021pMappingFields_Type(OctetString):
    """Custom type pp4QOS8021pMappingFields based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Pp4QOS8021pMappingFields_Type.__name__ = "OctetString"
_Pp4QOS8021pMappingFields_Object = MibTableColumn
pp4QOS8021pMappingFields = _Pp4QOS8021pMappingFields_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 3, 1, 2),
    _Pp4QOS8021pMappingFields_Type()
)
pp4QOS8021pMappingFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4QOS8021pMappingFields.setStatus("current")
_Pp4QOSDSCPMappingTable_Object = MibTable
pp4QOSDSCPMappingTable = _Pp4QOSDSCPMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 4)
)
if mibBuilder.loadTexts:
    pp4QOSDSCPMappingTable.setStatus("current")
_Pp4QOSDSCPMappingEntry_Object = MibTableRow
pp4QOSDSCPMappingEntry = _Pp4QOSDSCPMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 4, 1)
)
pp4QOSDSCPMappingEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4QOSDSCPMappingQueue"),
)
if mibBuilder.loadTexts:
    pp4QOSDSCPMappingEntry.setStatus("current")
_Pp4QOSDSCPMappingQueue_Type = Unsigned32
_Pp4QOSDSCPMappingQueue_Object = MibTableColumn
pp4QOSDSCPMappingQueue = _Pp4QOSDSCPMappingQueue_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 4, 1, 1),
    _Pp4QOSDSCPMappingQueue_Type()
)
pp4QOSDSCPMappingQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4QOSDSCPMappingQueue.setStatus("current")


class _Pp4QOSDSCPMappingFields_Type(OctetString):
    """Custom type pp4QOSDSCPMappingFields based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Pp4QOSDSCPMappingFields_Type.__name__ = "OctetString"
_Pp4QOSDSCPMappingFields_Object = MibTableColumn
pp4QOSDSCPMappingFields = _Pp4QOSDSCPMappingFields_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 60, 4, 1, 2),
    _Pp4QOSDSCPMappingFields_Type()
)
pp4QOSDSCPMappingFields.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4QOSDSCPMappingFields.setStatus("current")
_Pp4AccessList_ObjectIdentity = ObjectIdentity
pp4AccessList = _Pp4AccessList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65)
)


class _Pp4AccessListDefaultPolicyType_Type(Integer32):
    """Custom type pp4AccessListDefaultPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("deny", 1))
    )


_Pp4AccessListDefaultPolicyType_Type.__name__ = "Integer32"
_Pp4AccessListDefaultPolicyType_Object = MibScalar
pp4AccessListDefaultPolicyType = _Pp4AccessListDefaultPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 1),
    _Pp4AccessListDefaultPolicyType_Type()
)
pp4AccessListDefaultPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListDefaultPolicyType.setStatus("current")
_Pp4AccessListTable_Object = MibTable
pp4AccessListTable = _Pp4AccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2)
)
if mibBuilder.loadTexts:
    pp4AccessListTable.setStatus("current")
_Pp4AccessListEntry_Object = MibTableRow
pp4AccessListEntry = _Pp4AccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1)
)
pp4AccessListEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4AccessListEntryID"),
)
if mibBuilder.loadTexts:
    pp4AccessListEntry.setStatus("current")
_Pp4AccessListEntryID_Type = Unsigned32
_Pp4AccessListEntryID_Object = MibTableColumn
pp4AccessListEntryID = _Pp4AccessListEntryID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 1),
    _Pp4AccessListEntryID_Type()
)
pp4AccessListEntryID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4AccessListEntryID.setStatus("current")


class _Pp4AccessListPolicyType_Type(Integer32):
    """Custom type pp4AccessListPolicyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 0),
          ("deny", 1))
    )


_Pp4AccessListPolicyType_Type.__name__ = "Integer32"
_Pp4AccessListPolicyType_Object = MibTableColumn
pp4AccessListPolicyType = _Pp4AccessListPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 2),
    _Pp4AccessListPolicyType_Type()
)
pp4AccessListPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListPolicyType.setStatus("current")


class _Pp4AccessListService_Type(Integer32):
    """Custom type pp4AccessListService based on Integer32"""
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
        *(("serviceAny", 4),
          ("serviceHttp", 0),
          ("serviceSnmp", 1),
          ("serviceSsh", 2),
          ("serviceTelnet", 3))
    )


_Pp4AccessListService_Type.__name__ = "Integer32"
_Pp4AccessListService_Object = MibTableColumn
pp4AccessListService = _Pp4AccessListService_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 3),
    _Pp4AccessListService_Type()
)
pp4AccessListService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListService.setStatus("current")


class _Pp4AccessListIfIndex_Type(Integer32):
    """Custom type pp4AccessListIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("any", -1)
    )


_Pp4AccessListIfIndex_Type.__name__ = "Integer32"
_Pp4AccessListIfIndex_Object = MibTableColumn
pp4AccessListIfIndex = _Pp4AccessListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 4),
    _Pp4AccessListIfIndex_Type()
)
pp4AccessListIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListIfIndex.setStatus("current")


class _Pp4AccessListSourceAddressType_Type(Integer32):
    """Custom type pp4AccessListSourceAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sourceAny", 2),
          ("sourceIpAddress", 1),
          ("sourceMacAddress", 0))
    )


_Pp4AccessListSourceAddressType_Type.__name__ = "Integer32"
_Pp4AccessListSourceAddressType_Object = MibTableColumn
pp4AccessListSourceAddressType = _Pp4AccessListSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 5),
    _Pp4AccessListSourceAddressType_Type()
)
pp4AccessListSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListSourceAddressType.setStatus("current")
_Pp4AccessListSourceMacAddress_Type = MacAddress
_Pp4AccessListSourceMacAddress_Object = MibTableColumn
pp4AccessListSourceMacAddress = _Pp4AccessListSourceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 6),
    _Pp4AccessListSourceMacAddress_Type()
)
pp4AccessListSourceMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListSourceMacAddress.setStatus("current")
_Pp4AccessListSourceIpAddress_Type = IpAddress
_Pp4AccessListSourceIpAddress_Object = MibTableColumn
pp4AccessListSourceIpAddress = _Pp4AccessListSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 7),
    _Pp4AccessListSourceIpAddress_Type()
)
pp4AccessListSourceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListSourceIpAddress.setStatus("current")
_Pp4AccessListSourceMask_Type = IpAddress
_Pp4AccessListSourceMask_Object = MibTableColumn
pp4AccessListSourceMask = _Pp4AccessListSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 8),
    _Pp4AccessListSourceMask_Type()
)
pp4AccessListSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListSourceMask.setStatus("current")
_Pp4AccessListChangeIndex_Type = Unsigned32
_Pp4AccessListChangeIndex_Object = MibTableColumn
pp4AccessListChangeIndex = _Pp4AccessListChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 9),
    _Pp4AccessListChangeIndex_Type()
)
pp4AccessListChangeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListChangeIndex.setStatus("current")
_Pp4AccessListRowStatus_Type = RowStatus
_Pp4AccessListRowStatus_Object = MibTableColumn
pp4AccessListRowStatus = _Pp4AccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 65, 2, 1, 10),
    _Pp4AccessListRowStatus_Type()
)
pp4AccessListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4AccessListRowStatus.setStatus("current")
_Pp4ONTLicense_ObjectIdentity = ObjectIdentity
pp4ONTLicense = _Pp4ONTLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70)
)
_Pp4ONTLicenseInstalled_Type = TruthValue
_Pp4ONTLicenseInstalled_Object = MibScalar
pp4ONTLicenseInstalled = _Pp4ONTLicenseInstalled_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 1),
    _Pp4ONTLicenseInstalled_Type()
)
pp4ONTLicenseInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseInstalled.setStatus("current")
_Pp4ONTLicenseValid_Type = TruthValue
_Pp4ONTLicenseValid_Object = MibScalar
pp4ONTLicenseValid = _Pp4ONTLicenseValid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 2),
    _Pp4ONTLicenseValid_Type()
)
pp4ONTLicenseValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseValid.setStatus("current")
_Pp4ONTLicenseVersion_Type = DisplayString
_Pp4ONTLicenseVersion_Object = MibScalar
pp4ONTLicenseVersion = _Pp4ONTLicenseVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 3),
    _Pp4ONTLicenseVersion_Type()
)
pp4ONTLicenseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseVersion.setStatus("current")
_Pp4ONTLicenseCarrier_Type = DisplayString
_Pp4ONTLicenseCarrier_Object = MibScalar
pp4ONTLicenseCarrier = _Pp4ONTLicenseCarrier_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 4),
    _Pp4ONTLicenseCarrier_Type()
)
pp4ONTLicenseCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseCarrier.setStatus("current")
_Pp4ONTLicenseVendor_Type = DisplayString
_Pp4ONTLicenseVendor_Object = MibScalar
pp4ONTLicenseVendor = _Pp4ONTLicenseVendor_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 5),
    _Pp4ONTLicenseVendor_Type()
)
pp4ONTLicenseVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseVendor.setStatus("current")


class _Pp4ONTLicenseONTCountLicensed_Type(Integer32):
    """Custom type pp4ONTLicenseONTCountLicensed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2147483647
        )
    )
    namedValues = NamedValues(
        ("unlimited", 2147483647)
    )


_Pp4ONTLicenseONTCountLicensed_Type.__name__ = "Integer32"
_Pp4ONTLicenseONTCountLicensed_Object = MibScalar
pp4ONTLicenseONTCountLicensed = _Pp4ONTLicenseONTCountLicensed_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 6),
    _Pp4ONTLicenseONTCountLicensed_Type()
)
pp4ONTLicenseONTCountLicensed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseONTCountLicensed.setStatus("current")
_Pp4ONTLicenseONTCountOnline_Type = Unsigned32
_Pp4ONTLicenseONTCountOnline_Object = MibScalar
pp4ONTLicenseONTCountOnline = _Pp4ONTLicenseONTCountOnline_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 7),
    _Pp4ONTLicenseONTCountOnline_Type()
)
pp4ONTLicenseONTCountOnline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseONTCountOnline.setStatus("current")
_Pp4ONTLicenseSerialNumbers_Type = DisplayString
_Pp4ONTLicenseSerialNumbers_Object = MibScalar
pp4ONTLicenseSerialNumbers = _Pp4ONTLicenseSerialNumbers_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 8),
    _Pp4ONTLicenseSerialNumbers_Type()
)
pp4ONTLicenseSerialNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseSerialNumbers.setStatus("current")
_Pp4ONTLicenseMacAddresses_Type = DisplayString
_Pp4ONTLicenseMacAddresses_Object = MibScalar
pp4ONTLicenseMacAddresses = _Pp4ONTLicenseMacAddresses_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 70, 9),
    _Pp4ONTLicenseMacAddresses_Type()
)
pp4ONTLicenseMacAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pp4ONTLicenseMacAddresses.setStatus("current")
_Pp4RawData_ObjectIdentity = ObjectIdentity
pp4RawData = _Pp4RawData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 300)
)
_Pp4RawMacTable_Object = MibTable
pp4RawMacTable = _Pp4RawMacTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 300, 1)
)
if mibBuilder.loadTexts:
    pp4RawMacTable.setStatus("current")
_Pp4RawMacEntry_Object = MibTableRow
pp4RawMacEntry = _Pp4RawMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 300, 1, 1)
)
pp4RawMacEntry.setIndexNames(
    (0, "ELTEX-PP4", "pp4RawMacChunkID"),
)
if mibBuilder.loadTexts:
    pp4RawMacEntry.setStatus("current")
_Pp4RawMacChunkID_Type = Unsigned32
_Pp4RawMacChunkID_Object = MibTableColumn
pp4RawMacChunkID = _Pp4RawMacChunkID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 300, 1, 1, 1),
    _Pp4RawMacChunkID_Type()
)
pp4RawMacChunkID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pp4RawMacChunkID.setStatus("current")


class _Pp4RawMacText_Type(OctetString):
    """Custom type pp4RawMacText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_Pp4RawMacText_Type.__name__ = "OctetString"
_Pp4RawMacText_Object = MibTableColumn
pp4RawMacText = _Pp4RawMacText_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 300, 1, 1, 2),
    _Pp4RawMacText_Type()
)
pp4RawMacText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pp4RawMacText.setStatus("current")
_Ma4000AlarmTraps_ObjectIdentity = ObjectIdentity
ma4000AlarmTraps = _Ma4000AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35)
)
_Ma4000OkTraps_ObjectIdentity = ObjectIdentity
ma4000OkTraps = _Ma4000OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36)
)

# Managed Objects groups

pp4Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 13, 200)
)
pp4Group.setObjects(
      *(("ELTEX-PP4", "pp4DevName"),
        ("ELTEX-PP4", "pp4DevType"),
        ("ELTEX-PP4", "pp4DevCfgBuild"),
        ("ELTEX-PP4", "pp4FreeSpace"),
        ("ELTEX-PP4", "pp4FreeRam"),
        ("ELTEX-PP4", "pp4SystemType"),
        ("ELTEX-PP4", "pp4SystemInfo"),
        ("ELTEX-PP4", "pp4SystemUnit1MacAddress"),
        ("ELTEX-PP4", "pp4SystemUnit2MacAddress"),
        ("ELTEX-PP4", "pp4SystemUnit1FirmwareVersion"),
        ("ELTEX-PP4", "pp4SystemUnit2FirmwareVersion"),
        ("ELTEX-PP4", "pp4SystemUnit1LinuxVersion"),
        ("ELTEX-PP4", "pp4SystemUnit2LinuxVersion"),
        ("ELTEX-PP4", "pp4SystemUnit1UpTime"),
        ("ELTEX-PP4", "pp4SystemUnit2UpTime"),
        ("ELTEX-PP4", "pp4PortsEntryID"),
        ("ELTEX-PP4", "pp4PortsLink"),
        ("ELTEX-PP4", "pp4PortsAutoNegotiate"),
        ("ELTEX-PP4", "pp4PortsAutoNegotiationError"),
        ("ELTEX-PP4", "pp4PortsSpeed"),
        ("ELTEX-PP4", "pp4PortsDuplex"),
        ("ELTEX-PP4", "pp4PortsFlowControlEnabled"),
        ("ELTEX-PP4", "pp4PortsEnabled"),
        ("ELTEX-PP4", "pp4MulticastEntryID"),
        ("ELTEX-PP4", "pp4MulticastVLAN"),
        ("ELTEX-PP4", "pp4MulticastGroupAddress"),
        ("ELTEX-PP4", "pp4MulticastMemberPorts"),
        ("ELTEX-PP4", "pp4MulticastExpires"),
        ("ELTEX-PP4", "pp4MacAddressEntryID"),
        ("ELTEX-PP4", "pp4MacAddressVLAN"),
        ("ELTEX-PP4", "pp4MacAddressAddress"),
        ("ELTEX-PP4", "pp4MacAddressPort"),
        ("ELTEX-PP4", "pp4MacAddressType"),
        ("ELTEX-PP4", "pp4RebootSlot"),
        ("ELTEX-PP4", "pp4RebootDescription"),
        ("ELTEX-PP4", "pp4RebootCommand"),
        ("ELTEX-PP4", "pp4RebootAfterDelay"),
        ("ELTEX-PP4", "pp4BoardFan1AbsoluteSpeed"),
        ("ELTEX-PP4", "pp4BoardFan2AbsoluteSpeed"),
        ("ELTEX-PP4", "pp4BoardFan3AbsoluteSpeed"),
        ("ELTEX-PP4", "pp4BoardFanRelativeSpeed"),
        ("ELTEX-PP4", "pp4BoardFan1Breakdown"),
        ("ELTEX-PP4", "pp4BoardFan2Breakdown"),
        ("ELTEX-PP4", "pp4BoardFan3Breakdown"),
        ("ELTEX-PP4", "pp4BoardUnit1TempSfp"),
        ("ELTEX-PP4", "pp4BoardUnit2TempSfp"),
        ("ELTEX-PP4", "pp4BoardUnit1TempProc"),
        ("ELTEX-PP4", "pp4BoardUnit2TempProc"),
        ("ELTEX-PP4", "pp4BoardUnit1TempSwitch"),
        ("ELTEX-PP4", "pp4BoardUnit2TempSwitch"),
        ("ELTEX-PP4", "pp4BoardUnit1LoadAverage1"),
        ("ELTEX-PP4", "pp4BoardUnit2LoadAverage1"),
        ("ELTEX-PP4", "pp4BoardUnit1LoadAverage5"),
        ("ELTEX-PP4", "pp4BoardUnit2LoadAverage5"),
        ("ELTEX-PP4", "pp4BoardUnit1LoadAverage15"),
        ("ELTEX-PP4", "pp4BoardUnit2LoadAverage15"),
        ("ELTEX-PP4", "pp4BoardUnit1TotalRam"),
        ("ELTEX-PP4", "pp4BoardUnit2TotalRam"),
        ("ELTEX-PP4", "pp4BoardUnit1FreeRam"),
        ("ELTEX-PP4", "pp4BoardUnit2FreeRam"),
        ("ELTEX-PP4", "pp4BoardUnit1TotalFilesystemRoot"),
        ("ELTEX-PP4", "pp4BoardUnit2TotalFilesystemRoot"),
        ("ELTEX-PP4", "pp4BoardUnit1TotalFilesystemTools"),
        ("ELTEX-PP4", "pp4BoardUnit2TotalFilesystemTools"),
        ("ELTEX-PP4", "pp4BoardUnit1TotalFilesystemConfig"),
        ("ELTEX-PP4", "pp4BoardUnit2TotalFilesystemConfig"),
        ("ELTEX-PP4", "pp4BoardUnit1TotalFilesystemLog"),
        ("ELTEX-PP4", "pp4BoardUnit2TotalFilesystemLog"),
        ("ELTEX-PP4", "pp4BoardUnit1FreeFilesystemRoot"),
        ("ELTEX-PP4", "pp4BoardUnit2FreeFilesystemRoot"),
        ("ELTEX-PP4", "pp4BoardUnit1FreeFilesystemTools"),
        ("ELTEX-PP4", "pp4BoardUnit2FreeFilesystemTools"),
        ("ELTEX-PP4", "pp4BoardUnit1FreeFilesystemConfig"),
        ("ELTEX-PP4", "pp4BoardUnit2FreeFilesystemConfig"),
        ("ELTEX-PP4", "pp4BoardUnit1FreeFilesystemLog"),
        ("ELTEX-PP4", "pp4BoardUnit2FreeFilesystemLog"),
        ("ELTEX-PP4", "pp4AlarmsJournalCleanJournal"))
)
if mibBuilder.loadTexts:
    pp4Group.setStatus("current")


# Notification objects

ma4000ConfigSaveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 1)
)
ma4000ConfigSaveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ConfigSaveAlarmTrap.setStatus(
        "current"
    )

ma4000ConfigApplyAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 2)
)
ma4000ConfigApplyAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ConfigApplyAlarmTrap.setStatus(
        "current"
    )

ma4000LoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 3)
)
ma4000LoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000LoginAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpAckAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 5)
)
ma4000DhcpAckAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpAckAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpAgentUpAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 6)
)
ma4000DhcpAgentUpAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpAgentUpAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpServerUpAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 7)
)
ma4000DhcpServerUpAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpServerUpAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpIpGotAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 8)
)
ma4000DhcpIpGotAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpIpGotAlarmTrap.setStatus(
        "current"
    )

ma4000Pp4CpuLoadCriticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 9)
)
ma4000Pp4CpuLoadCriticalAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000Pp4CpuLoadCriticalAlarmTrap.setStatus(
        "current"
    )

ma4000OutOfRamAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 10)
)
ma4000OutOfRamAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000OutOfRamAlarmTrap.setStatus(
        "current"
    )

ma4000MacSyncVlanDuplicateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 11)
)
ma4000MacSyncVlanDuplicateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000MacSyncVlanDuplicateAlarmTrap.setStatus(
        "current"
    )

ma4000LinksPortFlappingPhyAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 12)
)
ma4000LinksPortFlappingPhyAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000LinksPortFlappingPhyAlarmTrap.setStatus(
        "current"
    )

ma4000LinkDownAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 13)
)
ma4000LinkDownAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000LinkDownAlarmTrap.setStatus(
        "current"
    )

ma4000UnitLostAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 14)
)
ma4000UnitLostAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000UnitLostAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpOfferAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 15)
)
ma4000DhcpOfferAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpOfferAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpAgentDownAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 16)
)
ma4000DhcpAgentDownAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpAgentDownAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpServerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 17)
)
ma4000DhcpServerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpServerAlarmTrap.setStatus(
        "current"
    )

ma4000DhcpIpFailedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 18)
)
ma4000DhcpIpFailedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000DhcpIpFailedAlarmTrap.setStatus(
        "current"
    )

ma4000IgmpSyncFailedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 20)
)
ma4000IgmpSyncFailedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000IgmpSyncFailedAlarmTrap.setStatus(
        "current"
    )

ma4000StpSyncFailedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 21)
)
ma4000StpSyncFailedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000StpSyncFailedAlarmTrap.setStatus(
        "current"
    )

ma4000StpLinkChangedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 22)
)
ma4000StpLinkChangedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000StpLinkChangedAlarmTrap.setStatus(
        "current"
    )

ma4000PortCntrErrorsFoundAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 23)
)
ma4000PortCntrErrorsFoundAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000PortCntrErrorsFoundAlarmTrap.setStatus(
        "current"
    )

ma4000SyncDisallowedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 25)
)
ma4000SyncDisallowedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SyncDisallowedAlarmTrap.setStatus(
        "current"
    )

ma4000SlotInvalidAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 26)
)
ma4000SlotInvalidAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SlotInvalidAlarmTrap.setStatus(
        "current"
    )

ma4000SlotErrorAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 27)
)
ma4000SlotErrorAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SlotErrorAlarmTrap.setStatus(
        "current"
    )

ma4000SlotDownAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 28)
)
ma4000SlotDownAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SlotDownAlarmTrap.setStatus(
        "current"
    )

ma4000OmsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 31)
)
ma4000OmsAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000OmsAlarmTrap.setStatus(
        "current"
    )

ma4000FanSpeedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 32)
)
ma4000FanSpeedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanSpeedAlarmTrap.setStatus(
        "current"
    )

ma4000FanFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 33)
)
ma4000FanFailAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanFailAlarmTrap.setStatus(
        "current"
    )

ma4000FanControllerFailAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 34)
)
ma4000FanControllerFailAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanControllerFailAlarmTrap.setStatus(
        "current"
    )

ma4000RebootStackAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 35)
)
ma4000RebootStackAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000RebootStackAlarmTrap.setStatus(
        "current"
    )

ma4000RebootUnitAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 36)
)
ma4000RebootUnitAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000RebootUnitAlarmTrap.setStatus(
        "current"
    )

ma4000RebootFwTimerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 37)
)
ma4000RebootFwTimerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000RebootFwTimerAlarmTrap.setStatus(
        "current"
    )

ma4000FwUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 38)
)
ma4000FwUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FwUpdateAlarmTrap.setStatus(
        "current"
    )

ma4000FwConfirmNeededAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 39)
)
ma4000FwConfirmNeededAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FwConfirmNeededAlarmTrap.setStatus(
        "current"
    )

ma4000CpuLoadHighAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 48)
)
ma4000CpuLoadHighAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000CpuLoadHighAlarmTrap.setStatus(
        "current"
    )

ma4000ComCopyAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 54)
)
ma4000ComCopyAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ComCopyAlarmTrap.setStatus(
        "current"
    )

ma4000CscdDuplicateUnitIdAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 35, 64)
)
ma4000CscdDuplicateUnitIdAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000CscdDuplicateUnitIdAlarmTrap.setStatus(
        "current"
    )

ma4000ConfigSavedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 1)
)
ma4000ConfigSavedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ConfigSavedOkTrap.setStatus(
        "current"
    )

ma4000ConfigAppliedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 2)
)
ma4000ConfigAppliedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ConfigAppliedOkTrap.setStatus(
        "current"
    )

ma4000Pp4CpuLoadCriticalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 9)
)
ma4000Pp4CpuLoadCriticalOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000Pp4CpuLoadCriticalOkTrap.setStatus(
        "current"
    )

ma4000LinksPortFlappingPhyOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 12)
)
ma4000LinksPortFlappingPhyOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000LinksPortFlappingPhyOkTrap.setStatus(
        "current"
    )

ma4000LinkUpOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 13)
)
ma4000LinkUpOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000LinkUpOkTrap.setStatus(
        "current"
    )

ma4000UnitLostOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 14)
)
ma4000UnitLostOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000UnitLostOkTrap.setStatus(
        "current"
    )

ma4000SlotOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 19)
)
ma4000SlotOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SlotOkTrap.setStatus(
        "current"
    )

ma4000PortCntrErrorsFreeOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 23)
)
ma4000PortCntrErrorsFreeOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000PortCntrErrorsFreeOkTrap.setStatus(
        "current"
    )

ma4000CscdMasterChandedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 24)
)
ma4000CscdMasterChandedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000CscdMasterChandedOkTrap.setStatus(
        "current"
    )

ma4000SyncDisallowedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 25)
)
ma4000SyncDisallowedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SyncDisallowedOkTrap.setStatus(
        "current"
    )

ma4000BufferIverflowOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 29)
)
ma4000BufferIverflowOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000BufferIverflowOkTrap.setStatus(
        "current"
    )

ma4000ConfigRestoreOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 30)
)
ma4000ConfigRestoreOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ConfigRestoreOkTrap.setStatus(
        "current"
    )

ma4000OmsOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 31)
)
ma4000OmsOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000OmsOkTrap.setStatus(
        "current"
    )

ma4000FanSpeedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 32)
)
ma4000FanSpeedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanSpeedOkTrap.setStatus(
        "current"
    )

ma4000FanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 33)
)
ma4000FanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanOkTrap.setStatus(
        "current"
    )

ma4000FanControllerOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 34)
)
ma4000FanControllerOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FanControllerOkTrap.setStatus(
        "current"
    )

ma4000RebootUnitOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 36)
)
ma4000RebootUnitOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000RebootUnitOkTrap.setStatus(
        "current"
    )

ma4000FwUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 38)
)
ma4000FwUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FwUpdateOkTrap.setStatus(
        "current"
    )

ma4000CpuLoadHighOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 48)
)
ma4000CpuLoadHighOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000CpuLoadHighOkTrap.setStatus(
        "current"
    )

ma4000ComCopyOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 54)
)
ma4000ComCopyOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000ComCopyOkTrap.setStatus(
        "current"
    )

ma4000FirmwareUpdateStateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 63)
)
ma4000FirmwareUpdateStateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FirmwareUpdateStateOkTrap.setStatus(
        "current"
    )

ma4000SystemColdstartOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 65)
)
ma4000SystemColdstartOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000SystemColdstartOkTrap.setStatus(
        "current"
    )

ma4000FallbackWasInvokedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 516)
)
ma4000FallbackWasInvokedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FallbackWasInvokedOkTrap.setStatus(
        "current"
    )

ma4000NSSRStatusOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 517)
)
ma4000NSSRStatusOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000NSSRStatusOkTrap.setStatus(
        "current"
    )

ma4000FirmwareUpdateStateV2OkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 36, 518)
)
ma4000FirmwareUpdateStateV2OkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ma4000FirmwareUpdateStateV2OkTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-PP4",
    **{"PP4SysType": PP4SysType,
       "Pp4Link": Pp4Link,
       "Pp4PortSpeed": Pp4PortSpeed,
       "Pp4PortDuplex": Pp4PortDuplex,
       "Pp4MacType": Pp4MacType,
       "Pp4MacPort": Pp4MacPort,
       "Pp4RebootIndex": Pp4RebootIndex,
       "Pp4SlotBoardType": Pp4SlotBoardType,
       "Pp4FanBreakdownState": Pp4FanBreakdownState,
       "Pp4BoardRole": Pp4BoardRole,
       "Pp4BoardPosition": Pp4BoardPosition,
       "Pp4SlotFirmwareVersion": Pp4SlotFirmwareVersion,
       "Pp4FirmwareUnitStatus": Pp4FirmwareUnitStatus,
       "Pp4FeederStatus": Pp4FeederStatus,
       "Pp4FeederActive": Pp4FeederActive,
       "Pp4FeederPolarity": Pp4FeederPolarity,
       "pp4": pp4,
       "pp4DevName": pp4DevName,
       "pp4DevType": pp4DevType,
       "pp4DevCfgBuild": pp4DevCfgBuild,
       "pp4FreeSpace": pp4FreeSpace,
       "pp4FreeRam": pp4FreeRam,
       "pp4System": pp4System,
       "pp4SystemType": pp4SystemType,
       "pp4SystemInfo": pp4SystemInfo,
       "pp4SystemUnit1MacAddress": pp4SystemUnit1MacAddress,
       "pp4SystemUnit2MacAddress": pp4SystemUnit2MacAddress,
       "pp4SystemUnit1FirmwareVersion": pp4SystemUnit1FirmwareVersion,
       "pp4SystemUnit2FirmwareVersion": pp4SystemUnit2FirmwareVersion,
       "pp4SystemUnit1LinuxVersion": pp4SystemUnit1LinuxVersion,
       "pp4SystemUnit2LinuxVersion": pp4SystemUnit2LinuxVersion,
       "pp4SystemUnit1UpTime": pp4SystemUnit1UpTime,
       "pp4SystemUnit2UpTime": pp4SystemUnit2UpTime,
       "pp4SystemUnit1Role": pp4SystemUnit1Role,
       "pp4SystemUnit2Role": pp4SystemUnit2Role,
       "pp4SystemUnit1Position": pp4SystemUnit1Position,
       "pp4SystemUnit2Position": pp4SystemUnit2Position,
       "pp4SystemUnit1SerialNumber": pp4SystemUnit1SerialNumber,
       "pp4SystemUnit2SerialNumber": pp4SystemUnit2SerialNumber,
       "pp4SynchronizationStateInStack": pp4SynchronizationStateInStack,
       "pp4StackMasterChange": pp4StackMasterChange,
       "pp4Services": pp4Services,
       "pp4ACSActive": pp4ACSActive,
       "pp4PortsTable": pp4PortsTable,
       "pp4PortsEntry": pp4PortsEntry,
       "pp4PortsEntryID": pp4PortsEntryID,
       "pp4PortsLink": pp4PortsLink,
       "pp4PortsAutoNegotiate": pp4PortsAutoNegotiate,
       "pp4PortsAutoNegotiationError": pp4PortsAutoNegotiationError,
       "pp4PortsSpeed": pp4PortsSpeed,
       "pp4PortsDuplex": pp4PortsDuplex,
       "pp4PortsFlowControlEnabled": pp4PortsFlowControlEnabled,
       "pp4PortsEnabled": pp4PortsEnabled,
       "pp4MulticastGroupsTable": pp4MulticastGroupsTable,
       "pp4MulticastGroupsEntry": pp4MulticastGroupsEntry,
       "pp4MulticastEntryID": pp4MulticastEntryID,
       "pp4MulticastVLAN": pp4MulticastVLAN,
       "pp4MulticastGroupAddress": pp4MulticastGroupAddress,
       "pp4MulticastMemberPorts": pp4MulticastMemberPorts,
       "pp4MulticastExpires": pp4MulticastExpires,
       "pp4MacAddressTable": pp4MacAddressTable,
       "pp4MacAddressEntry": pp4MacAddressEntry,
       "pp4MacAddressEntryID": pp4MacAddressEntryID,
       "pp4MacAddressVLAN": pp4MacAddressVLAN,
       "pp4MacAddressAddress": pp4MacAddressAddress,
       "pp4MacAddressPort": pp4MacAddressPort,
       "pp4MacAddressType": pp4MacAddressType,
       "pp4SlotsTable": pp4SlotsTable,
       "pp4SlotsEntry": pp4SlotsEntry,
       "pp4SlotsSlot": pp4SlotsSlot,
       "pp4SlotsBoardType": pp4SlotsBoardType,
       "pp4SlotsLink": pp4SlotsLink,
       "pp4SlotsFirmwareActive": pp4SlotsFirmwareActive,
       "pp4SlotsFirmwareRevision": pp4SlotsFirmwareRevision,
       "pp4SlotsSerialNumber": pp4SlotsSerialNumber,
       "pp4SlotsState": pp4SlotsState,
       "pp4ConfigRevisions": pp4ConfigRevisions,
       "pp4ConfigRevisionsPp4x": pp4ConfigRevisionsPp4x,
       "pp4ConfigRevisionsTable": pp4ConfigRevisionsTable,
       "pp4ConfigRevisionsEntry": pp4ConfigRevisionsEntry,
       "pp4ConfigRevisionsSlot": pp4ConfigRevisionsSlot,
       "pp4ConfigRevisionsRevision": pp4ConfigRevisionsRevision,
       "pp4ConfigRevisionsProfilesELC": pp4ConfigRevisionsProfilesELC,
       "pp4ConfigRevisionsProfilesPLC": pp4ConfigRevisionsProfilesPLC,
       "pp4ConfigRevisionsProfilesPLCOLT": pp4ConfigRevisionsProfilesPLCOLT,
       "pp4xIfUtilizTable": pp4xIfUtilizTable,
       "pp4xIfUtilizEntry": pp4xIfUtilizEntry,
       "interfaceIndex": interfaceIndex,
       "portName": portName,
       "lastCountersKbitsSent": lastCountersKbitsSent,
       "lastCountersKbitsRecv": lastCountersKbitsRecv,
       "lastCountersFramesSent": lastCountersFramesSent,
       "lastCountersFramesRecv": lastCountersFramesRecv,
       "averageKbitsSent": averageKbitsSent,
       "averageKbitsRecv": averageKbitsRecv,
       "averageFramesSent": averageFramesSent,
       "averageFramesRecv": averageFramesRecv,
       "pp4xIfUtilizAverageInterval": pp4xIfUtilizAverageInterval,
       "pp4xSfpInfoTable": pp4xSfpInfoTable,
       "pp4xSfpInfoEntry": pp4xSfpInfoEntry,
       "sfpInfoStatus": sfpInfoStatus,
       "sfpInfoTemperature": sfpInfoTemperature,
       "sfpInfoVoltage": sfpInfoVoltage,
       "sfpInfoCurrent": sfpInfoCurrent,
       "sfpInfoRXPower": sfpInfoRXPower,
       "sfpInfoTXPower": sfpInfoTXPower,
       "pp4PortsConfigTable": pp4PortsConfigTable,
       "pp4PortsConfigEntry": pp4PortsConfigEntry,
       "pp4PortsConfigEntryID": pp4PortsConfigEntryID,
       "pp4PortsConfigAutoNegotiate": pp4PortsConfigAutoNegotiate,
       "pp4PortsConfigSpeed": pp4PortsConfigSpeed,
       "pp4PortsConfigDuplex": pp4PortsConfigDuplex,
       "pp4PortsConfigFlowControlEnabled": pp4PortsConfigFlowControlEnabled,
       "pp4PortsConfigEnabled": pp4PortsConfigEnabled,
       "pp4PortsConfigResetCounters": pp4PortsConfigResetCounters,
       "pp4PortsConfigRowStatus": pp4PortsConfigRowStatus,
       "pp4RebootTable": pp4RebootTable,
       "pp4RebootEntry": pp4RebootEntry,
       "pp4RebootSlot": pp4RebootSlot,
       "pp4RebootDescription": pp4RebootDescription,
       "pp4RebootCommand": pp4RebootCommand,
       "pp4RebootAfterDelay": pp4RebootAfterDelay,
       "pp4ChannelGroupMembershipTable": pp4ChannelGroupMembershipTable,
       "pp4ChannelGroupMembershipEntry": pp4ChannelGroupMembershipEntry,
       "pp4ChannelGroupMembershipGroupID": pp4ChannelGroupMembershipGroupID,
       "pp4ChannelGroupLACPTable": pp4ChannelGroupLACPTable,
       "pp4ChannelGroupLACPEntry": pp4ChannelGroupLACPEntry,
       "pp4ChannelGroupLACPGroupID": pp4ChannelGroupLACPGroupID,
       "pp4ChannelGroupLACPRunning": pp4ChannelGroupLACPRunning,
       "pp4ChannelGroupLACPAggregators": pp4ChannelGroupLACPAggregators,
       "pp4LACPSystemPriority": pp4LACPSystemPriority,
       "pp4MLDGroupsTable": pp4MLDGroupsTable,
       "pp4MLDGroupsEntry": pp4MLDGroupsEntry,
       "pp4MLDEntryID": pp4MLDEntryID,
       "pp4MLDVLAN": pp4MLDVLAN,
       "pp4MLDGroupAddress": pp4MLDGroupAddress,
       "pp4MLDMemberPorts": pp4MLDMemberPorts,
       "pp4MLDExpires": pp4MLDExpires,
       "pp4BoardState": pp4BoardState,
       "pp4BoardFan1AbsoluteSpeed": pp4BoardFan1AbsoluteSpeed,
       "pp4BoardFan2AbsoluteSpeed": pp4BoardFan2AbsoluteSpeed,
       "pp4BoardFan3AbsoluteSpeed": pp4BoardFan3AbsoluteSpeed,
       "pp4BoardFanRelativeSpeed": pp4BoardFanRelativeSpeed,
       "pp4BoardFan1Breakdown": pp4BoardFan1Breakdown,
       "pp4BoardFan2Breakdown": pp4BoardFan2Breakdown,
       "pp4BoardFan3Breakdown": pp4BoardFan3Breakdown,
       "pp4BoardUnit1TempSfp": pp4BoardUnit1TempSfp,
       "pp4BoardUnit2TempSfp": pp4BoardUnit2TempSfp,
       "pp4BoardUnit1TempProc": pp4BoardUnit1TempProc,
       "pp4BoardUnit2TempProc": pp4BoardUnit2TempProc,
       "pp4BoardUnit1TempSwitch": pp4BoardUnit1TempSwitch,
       "pp4BoardUnit2TempSwitch": pp4BoardUnit2TempSwitch,
       "pp4BoardUnit1LoadAverage1": pp4BoardUnit1LoadAverage1,
       "pp4BoardUnit2LoadAverage1": pp4BoardUnit2LoadAverage1,
       "pp4BoardUnit1LoadAverage5": pp4BoardUnit1LoadAverage5,
       "pp4BoardUnit2LoadAverage5": pp4BoardUnit2LoadAverage5,
       "pp4BoardUnit1LoadAverage15": pp4BoardUnit1LoadAverage15,
       "pp4BoardUnit2LoadAverage15": pp4BoardUnit2LoadAverage15,
       "pp4BoardUnit1TotalRam": pp4BoardUnit1TotalRam,
       "pp4BoardUnit2TotalRam": pp4BoardUnit2TotalRam,
       "pp4BoardUnit1FreeRam": pp4BoardUnit1FreeRam,
       "pp4BoardUnit2FreeRam": pp4BoardUnit2FreeRam,
       "pp4BoardUnit1TotalFilesystemRoot": pp4BoardUnit1TotalFilesystemRoot,
       "pp4BoardUnit2TotalFilesystemRoot": pp4BoardUnit2TotalFilesystemRoot,
       "pp4BoardUnit1TotalFilesystemTools": pp4BoardUnit1TotalFilesystemTools,
       "pp4BoardUnit2TotalFilesystemTools": pp4BoardUnit2TotalFilesystemTools,
       "pp4BoardUnit1TotalFilesystemConfig": pp4BoardUnit1TotalFilesystemConfig,
       "pp4BoardUnit2TotalFilesystemConfig": pp4BoardUnit2TotalFilesystemConfig,
       "pp4BoardUnit1TotalFilesystemLog": pp4BoardUnit1TotalFilesystemLog,
       "pp4BoardUnit2TotalFilesystemLog": pp4BoardUnit2TotalFilesystemLog,
       "pp4BoardUnit1FreeFilesystemRoot": pp4BoardUnit1FreeFilesystemRoot,
       "pp4BoardUnit2FreeFilesystemRoot": pp4BoardUnit2FreeFilesystemRoot,
       "pp4BoardUnit1FreeFilesystemTools": pp4BoardUnit1FreeFilesystemTools,
       "pp4BoardUnit2FreeFilesystemTools": pp4BoardUnit2FreeFilesystemTools,
       "pp4BoardUnit1FreeFilesystemConfig": pp4BoardUnit1FreeFilesystemConfig,
       "pp4BoardUnit2FreeFilesystemConfig": pp4BoardUnit2FreeFilesystemConfig,
       "pp4BoardUnit1FreeFilesystemLog": pp4BoardUnit1FreeFilesystemLog,
       "pp4BoardUnit2FreeFilesystemLog": pp4BoardUnit2FreeFilesystemLog,
       "pp4FeederState": pp4FeederState,
       "pp4Feeder1Status": pp4Feeder1Status,
       "pp4Feeder1Active": pp4Feeder1Active,
       "pp4Feeder1Polarity": pp4Feeder1Polarity,
       "pp4Feeder1Current": pp4Feeder1Current,
       "pp4Feeder1Voltage": pp4Feeder1Voltage,
       "pp4Feeder2Status": pp4Feeder2Status,
       "pp4Feeder2Active": pp4Feeder2Active,
       "pp4Feeder2Polarity": pp4Feeder2Polarity,
       "pp4Feeder2Current": pp4Feeder2Current,
       "pp4Feeder2Voltage": pp4Feeder2Voltage,
       "pp4StationVoltage": pp4StationVoltage,
       "pp4Firmware": pp4Firmware,
       "pp4FirmwareTable": pp4FirmwareTable,
       "pp4FirmwareEntry": pp4FirmwareEntry,
       "pp4FirmwareBoardType": pp4FirmwareBoardType,
       "pp4FirmwareIndex": pp4FirmwareIndex,
       "pp4FirmwareVersion": pp4FirmwareVersion,
       "pp4FirmwareDelete": pp4FirmwareDelete,
       "pp4DefaultFirmware": pp4DefaultFirmware,
       "pp4DefaultFirmwareELC": pp4DefaultFirmwareELC,
       "pp4DefaultFirmwarePLC": pp4DefaultFirmwarePLC,
       "pp4ShelfConfigTable": pp4ShelfConfigTable,
       "pp4ShelfConfigEntry": pp4ShelfConfigEntry,
       "pp4ShelfConfigSlot": pp4ShelfConfigSlot,
       "pp4ShelfConfigBoardType": pp4ShelfConfigBoardType,
       "pp4ShelfConfigFirmwareVersion": pp4ShelfConfigFirmwareVersion,
       "pp4BootVarTable": pp4BootVarTable,
       "pp4BootVarEntry": pp4BootVarEntry,
       "pp4BootVarUnit": pp4BootVarUnit,
       "pp4BootVarIndex": pp4BootVarIndex,
       "pp4BootVarValid": pp4BootVarValid,
       "pp4BootVarTimestamp": pp4BootVarTimestamp,
       "pp4BootVarVersionString": pp4BootVarVersionString,
       "pp4UnitsFirmwareTable": pp4UnitsFirmwareTable,
       "pp4UnitsFirmwareEntry": pp4UnitsFirmwareEntry,
       "pp4UnitsStatus": pp4UnitsStatus,
       "pp4UnitsActivePartition": pp4UnitsActivePartition,
       "pp4UnitsFallbackPartition": pp4UnitsFallbackPartition,
       "pp4UnitsRunningPartition": pp4UnitsRunningPartition,
       "pp4UnitsConfirm": pp4UnitsConfirm,
       "pp4FirmwareDeleteUnused": pp4FirmwareDeleteUnused,
       "pp4FirmwareUpdate": pp4FirmwareUpdate,
       "pp4FirmwareUpdateFileName": pp4FirmwareUpdateFileName,
       "pp4FirmwareUpdateIpAddress": pp4FirmwareUpdateIpAddress,
       "pp4FirmwareUpdateConfigName": pp4FirmwareUpdateConfigName,
       "pp4FirmwareUpdateSwitchVersion": pp4FirmwareUpdateSwitchVersion,
       "pp4FirmwareUpdateNeedRestart": pp4FirmwareUpdateNeedRestart,
       "pp4FirmwareUpdateNSSU": pp4FirmwareUpdateNSSU,
       "pp4FirmwareUpdateConfigIpAddress": pp4FirmwareUpdateConfigIpAddress,
       "pp4FirmwareUpdateProtocol": pp4FirmwareUpdateProtocol,
       "pp4FirmwareUpdatePort": pp4FirmwareUpdatePort,
       "pp4FirmwareUpdateAction": pp4FirmwareUpdateAction,
       "pp4FirmwareUpdateConfigProtocol": pp4FirmwareUpdateConfigProtocol,
       "pp4FirmwareUpdateConfigPort": pp4FirmwareUpdateConfigPort,
       "pp4FirmwareUpdateConfirm": pp4FirmwareUpdateConfirm,
       "pp4AlarmsJournal": pp4AlarmsJournal,
       "pp4AlarmsJournalCleanJournal": pp4AlarmsJournalCleanJournal,
       "pp4UserTable": pp4UserTable,
       "pp4UserEntry": pp4UserEntry,
       "pp4UserName": pp4UserName,
       "pp4UserPermissions": pp4UserPermissions,
       "pp4UserOldPassword": pp4UserOldPassword,
       "pp4UserNewPassword": pp4UserNewPassword,
       "pp4UserRowStatus": pp4UserRowStatus,
       "pp4Privileges": pp4Privileges,
       "pp4PrivilegesNamesTable": pp4PrivilegesNamesTable,
       "pp4PrivilegesNamesEntry": pp4PrivilegesNamesEntry,
       "pp4PrivilegesNamesIndex": pp4PrivilegesNamesIndex,
       "pp4PrivilegesNamesName": pp4PrivilegesNamesName,
       "pp4PrivilegesLevelsTable": pp4PrivilegesLevelsTable,
       "pp4PrivilegesLevelsEntry": pp4PrivilegesLevelsEntry,
       "pp4PrivilegesLevelsLevel": pp4PrivilegesLevelsLevel,
       "pp4PrivilegesLevelsAllowed": pp4PrivilegesLevelsAllowed,
       "pp4IGMPConfig": pp4IGMPConfig,
       "pp4IGMPSnoopingEnable": pp4IGMPSnoopingEnable,
       "pp4IGMPProxyReportEnable": pp4IGMPProxyReportEnable,
       "pp4MLDSnoopingEnable": pp4MLDSnoopingEnable,
       "pp4MLDProxyReportEnable": pp4MLDProxyReportEnable,
       "pp4IGMPSnoopingVLANTable": pp4IGMPSnoopingVLANTable,
       "pp4IGMPSnoopingVLANEntry": pp4IGMPSnoopingVLANEntry,
       "pp4IGMPSnoopingVLANVID": pp4IGMPSnoopingVLANVID,
       "pp4IGMPSnoopingVLANEnabled": pp4IGMPSnoopingVLANEnabled,
       "pp4IGMPSnoopingVLANQuerierEnabled": pp4IGMPSnoopingVLANQuerierEnabled,
       "pp4MLDSnoopingVLANEnabled": pp4MLDSnoopingVLANEnabled,
       "pp4MLDSnoopingVLANQuerierEnabled": pp4MLDSnoopingVLANQuerierEnabled,
       "pp4IGMPProxyReportRangesTable": pp4IGMPProxyReportRangesTable,
       "pp4IGMPProxyReportRangesEntry": pp4IGMPProxyReportRangesEntry,
       "pp4IGMPProxyReportRangesID": pp4IGMPProxyReportRangesID,
       "pp4IGMPProxyReportRangesStart": pp4IGMPProxyReportRangesStart,
       "pp4IGMPProxyReportRangesEnd": pp4IGMPProxyReportRangesEnd,
       "pp4IGMPProxyReportRangesFromVLAN": pp4IGMPProxyReportRangesFromVLAN,
       "pp4IGMPProxyReportRangesToVLAN": pp4IGMPProxyReportRangesToVLAN,
       "pp4IGMPProxyRowStatus": pp4IGMPProxyRowStatus,
       "pp4MLDProxyReportRangesTable": pp4MLDProxyReportRangesTable,
       "pp4MLDProxyReportRangesEntry": pp4MLDProxyReportRangesEntry,
       "pp4MLDProxyReportRangesID": pp4MLDProxyReportRangesID,
       "pp4MLDProxyReportRangesStart": pp4MLDProxyReportRangesStart,
       "pp4MLDProxyReportRangesEnd": pp4MLDProxyReportRangesEnd,
       "pp4MLDProxyReportRangesFromVLAN": pp4MLDProxyReportRangesFromVLAN,
       "pp4MLDProxyReportRangesToVLAN": pp4MLDProxyReportRangesToVLAN,
       "pp4MLDProxyRowStatus": pp4MLDProxyRowStatus,
       "pp4QOSConfig": pp4QOSConfig,
       "pp4QOSDefaultQueue": pp4QOSDefaultQueue,
       "pp4QOSType": pp4QOSType,
       "pp4QOS8021pMappingTable": pp4QOS8021pMappingTable,
       "pp4QOS8021pMappingEntry": pp4QOS8021pMappingEntry,
       "pp4QOS8021pMappingQueue": pp4QOS8021pMappingQueue,
       "pp4QOS8021pMappingFields": pp4QOS8021pMappingFields,
       "pp4QOSDSCPMappingTable": pp4QOSDSCPMappingTable,
       "pp4QOSDSCPMappingEntry": pp4QOSDSCPMappingEntry,
       "pp4QOSDSCPMappingQueue": pp4QOSDSCPMappingQueue,
       "pp4QOSDSCPMappingFields": pp4QOSDSCPMappingFields,
       "pp4AccessList": pp4AccessList,
       "pp4AccessListDefaultPolicyType": pp4AccessListDefaultPolicyType,
       "pp4AccessListTable": pp4AccessListTable,
       "pp4AccessListEntry": pp4AccessListEntry,
       "pp4AccessListEntryID": pp4AccessListEntryID,
       "pp4AccessListPolicyType": pp4AccessListPolicyType,
       "pp4AccessListService": pp4AccessListService,
       "pp4AccessListIfIndex": pp4AccessListIfIndex,
       "pp4AccessListSourceAddressType": pp4AccessListSourceAddressType,
       "pp4AccessListSourceMacAddress": pp4AccessListSourceMacAddress,
       "pp4AccessListSourceIpAddress": pp4AccessListSourceIpAddress,
       "pp4AccessListSourceMask": pp4AccessListSourceMask,
       "pp4AccessListChangeIndex": pp4AccessListChangeIndex,
       "pp4AccessListRowStatus": pp4AccessListRowStatus,
       "pp4ONTLicense": pp4ONTLicense,
       "pp4ONTLicenseInstalled": pp4ONTLicenseInstalled,
       "pp4ONTLicenseValid": pp4ONTLicenseValid,
       "pp4ONTLicenseVersion": pp4ONTLicenseVersion,
       "pp4ONTLicenseCarrier": pp4ONTLicenseCarrier,
       "pp4ONTLicenseVendor": pp4ONTLicenseVendor,
       "pp4ONTLicenseONTCountLicensed": pp4ONTLicenseONTCountLicensed,
       "pp4ONTLicenseONTCountOnline": pp4ONTLicenseONTCountOnline,
       "pp4ONTLicenseSerialNumbers": pp4ONTLicenseSerialNumbers,
       "pp4ONTLicenseMacAddresses": pp4ONTLicenseMacAddresses,
       "pp4Group": pp4Group,
       "pp4RawData": pp4RawData,
       "pp4RawMacTable": pp4RawMacTable,
       "pp4RawMacEntry": pp4RawMacEntry,
       "pp4RawMacChunkID": pp4RawMacChunkID,
       "pp4RawMacText": pp4RawMacText,
       "ma4000AlarmTraps": ma4000AlarmTraps,
       "ma4000ConfigSaveAlarmTrap": ma4000ConfigSaveAlarmTrap,
       "ma4000ConfigApplyAlarmTrap": ma4000ConfigApplyAlarmTrap,
       "ma4000LoginAlarmTrap": ma4000LoginAlarmTrap,
       "ma4000DhcpAckAlarmTrap": ma4000DhcpAckAlarmTrap,
       "ma4000DhcpAgentUpAlarmTrap": ma4000DhcpAgentUpAlarmTrap,
       "ma4000DhcpServerUpAlarmTrap": ma4000DhcpServerUpAlarmTrap,
       "ma4000DhcpIpGotAlarmTrap": ma4000DhcpIpGotAlarmTrap,
       "ma4000Pp4CpuLoadCriticalAlarmTrap": ma4000Pp4CpuLoadCriticalAlarmTrap,
       "ma4000OutOfRamAlarmTrap": ma4000OutOfRamAlarmTrap,
       "ma4000MacSyncVlanDuplicateAlarmTrap": ma4000MacSyncVlanDuplicateAlarmTrap,
       "ma4000LinksPortFlappingPhyAlarmTrap": ma4000LinksPortFlappingPhyAlarmTrap,
       "ma4000LinkDownAlarmTrap": ma4000LinkDownAlarmTrap,
       "ma4000UnitLostAlarmTrap": ma4000UnitLostAlarmTrap,
       "ma4000DhcpOfferAlarmTrap": ma4000DhcpOfferAlarmTrap,
       "ma4000DhcpAgentDownAlarmTrap": ma4000DhcpAgentDownAlarmTrap,
       "ma4000DhcpServerAlarmTrap": ma4000DhcpServerAlarmTrap,
       "ma4000DhcpIpFailedAlarmTrap": ma4000DhcpIpFailedAlarmTrap,
       "ma4000IgmpSyncFailedAlarmTrap": ma4000IgmpSyncFailedAlarmTrap,
       "ma4000StpSyncFailedAlarmTrap": ma4000StpSyncFailedAlarmTrap,
       "ma4000StpLinkChangedAlarmTrap": ma4000StpLinkChangedAlarmTrap,
       "ma4000PortCntrErrorsFoundAlarmTrap": ma4000PortCntrErrorsFoundAlarmTrap,
       "ma4000SyncDisallowedAlarmTrap": ma4000SyncDisallowedAlarmTrap,
       "ma4000SlotInvalidAlarmTrap": ma4000SlotInvalidAlarmTrap,
       "ma4000SlotErrorAlarmTrap": ma4000SlotErrorAlarmTrap,
       "ma4000SlotDownAlarmTrap": ma4000SlotDownAlarmTrap,
       "ma4000OmsAlarmTrap": ma4000OmsAlarmTrap,
       "ma4000FanSpeedAlarmTrap": ma4000FanSpeedAlarmTrap,
       "ma4000FanFailAlarmTrap": ma4000FanFailAlarmTrap,
       "ma4000FanControllerFailAlarmTrap": ma4000FanControllerFailAlarmTrap,
       "ma4000RebootStackAlarmTrap": ma4000RebootStackAlarmTrap,
       "ma4000RebootUnitAlarmTrap": ma4000RebootUnitAlarmTrap,
       "ma4000RebootFwTimerAlarmTrap": ma4000RebootFwTimerAlarmTrap,
       "ma4000FwUpdateAlarmTrap": ma4000FwUpdateAlarmTrap,
       "ma4000FwConfirmNeededAlarmTrap": ma4000FwConfirmNeededAlarmTrap,
       "ma4000CpuLoadHighAlarmTrap": ma4000CpuLoadHighAlarmTrap,
       "ma4000ComCopyAlarmTrap": ma4000ComCopyAlarmTrap,
       "ma4000CscdDuplicateUnitIdAlarmTrap": ma4000CscdDuplicateUnitIdAlarmTrap,
       "ma4000OkTraps": ma4000OkTraps,
       "ma4000ConfigSavedOkTrap": ma4000ConfigSavedOkTrap,
       "ma4000ConfigAppliedOkTrap": ma4000ConfigAppliedOkTrap,
       "ma4000Pp4CpuLoadCriticalOkTrap": ma4000Pp4CpuLoadCriticalOkTrap,
       "ma4000LinksPortFlappingPhyOkTrap": ma4000LinksPortFlappingPhyOkTrap,
       "ma4000LinkUpOkTrap": ma4000LinkUpOkTrap,
       "ma4000UnitLostOkTrap": ma4000UnitLostOkTrap,
       "ma4000SlotOkTrap": ma4000SlotOkTrap,
       "ma4000PortCntrErrorsFreeOkTrap": ma4000PortCntrErrorsFreeOkTrap,
       "ma4000CscdMasterChandedOkTrap": ma4000CscdMasterChandedOkTrap,
       "ma4000SyncDisallowedOkTrap": ma4000SyncDisallowedOkTrap,
       "ma4000BufferIverflowOkTrap": ma4000BufferIverflowOkTrap,
       "ma4000ConfigRestoreOkTrap": ma4000ConfigRestoreOkTrap,
       "ma4000OmsOkTrap": ma4000OmsOkTrap,
       "ma4000FanSpeedOkTrap": ma4000FanSpeedOkTrap,
       "ma4000FanOkTrap": ma4000FanOkTrap,
       "ma4000FanControllerOkTrap": ma4000FanControllerOkTrap,
       "ma4000RebootUnitOkTrap": ma4000RebootUnitOkTrap,
       "ma4000FwUpdateOkTrap": ma4000FwUpdateOkTrap,
       "ma4000CpuLoadHighOkTrap": ma4000CpuLoadHighOkTrap,
       "ma4000ComCopyOkTrap": ma4000ComCopyOkTrap,
       "ma4000FirmwareUpdateStateOkTrap": ma4000FirmwareUpdateStateOkTrap,
       "ma4000SystemColdstartOkTrap": ma4000SystemColdstartOkTrap,
       "ma4000FallbackWasInvokedOkTrap": ma4000FallbackWasInvokedOkTrap,
       "ma4000NSSRStatusOkTrap": ma4000NSSRStatusOkTrap,
       "ma4000FirmwareUpdateStateV2OkTrap": ma4000FirmwareUpdateStateV2OkTrap}
)
