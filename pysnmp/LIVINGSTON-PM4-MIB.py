# SNMP MIB module (LIVINGSTON-PM4-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIVINGSTON-PM4-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:27 2024
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

(lucentPM4,) = mibBuilder.importSymbols(
    "LIVINGSTON-ROOT-MIB",
    "lucentPM4")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PMUnitType(Integer32):
    """Custom type PMUnitType based on Integer32"""
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
              10,
              11,
              255)
        )
    )
    namedValues = NamedValues(
        *(("acpwrsup", 9),
          ("allunits", 255),
          ("console", 8),
          ("dcpwrsup", 11),
          ("ether0", 6),
          ("ether1", 7),
          ("fan", 10),
          ("modem", 4),
          ("mrgmodule", 1),
          ("quadt1", 2),
          ("serialport", 5),
          ("trie1", 3))
    )





class PMEquipPRIStatus(Integer32):
    """Custom type PMEquipPRIStatus based on Integer32"""
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
        *(("down", 2),
          ("fault", 4),
          ("loopback", 3),
          ("up", 1))
    )





class PMEquipStatus(Integer32):
    """Custom type PMEquipStatus based on Integer32"""
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
        *(("down", 2),
          ("fault", 4),
          ("maintenance", 3),
          ("other", 5),
          ("up", 1))
    )





class PMDiagCmdStatus(Integer32):
    """Custom type PMDiagCmdStatus based on Integer32"""
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
        *(("aborted", 5),
          ("fail", 2),
          ("inprogress", 3),
          ("notsupported", 4),
          ("other", 6),
          ("success", 1))
    )





class PMDiagTestCntrl(Integer32):
    """Custom type PMDiagTestCntrl based on Integer32"""
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
        *(("abort", 4),
          ("normal", 1),
          ("start", 2),
          ("stop", 3))
    )





class PMAlarmType(Integer32):
    """Custom type PMAlarmType based on Integer32"""
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
        *(("critical", 5),
          ("informational", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LucentPM4Mib_ObjectIdentity = ObjectIdentity
lucentPM4Mib = _LucentPM4Mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1)
)


class _LucentPM4MibRev_Type(DisplayString):
    """Custom type lucentPM4MibRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_LucentPM4MibRev_Type.__name__ = "DisplayString"
_LucentPM4MibRev_Object = MibScalar
lucentPM4MibRev = _LucentPM4MibRev_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 1),
    _LucentPM4MibRev_Type()
)
lucentPM4MibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4MibRev.setStatus("mandatory")


class _LucentPM4SWRev_Type(DisplayString):
    """Custom type lucentPM4SWRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_LucentPM4SWRev_Type.__name__ = "DisplayString"
_LucentPM4SWRev_Object = MibScalar
lucentPM4SWRev = _LucentPM4SWRev_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 2),
    _LucentPM4SWRev_Type()
)
lucentPM4SWRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SWRev.setStatus("mandatory")
_LucentPM4Chassis_ObjectIdentity = ObjectIdentity
lucentPM4Chassis = _LucentPM4Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3)
)


class _LucentPM4ChasSummary_Type(DisplayString):
    """Custom type lucentPM4ChasSummary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(55, 55),
    )


_LucentPM4ChasSummary_Type.__name__ = "DisplayString"
_LucentPM4ChasSummary_Object = MibScalar
lucentPM4ChasSummary = _LucentPM4ChasSummary_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 1),
    _LucentPM4ChasSummary_Type()
)
lucentPM4ChasSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ChasSummary.setStatus("mandatory")
_LucentPM4ChasCmdTable_Object = MibTable
lucentPM4ChasCmdTable = _LucentPM4ChasCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    lucentPM4ChasCmdTable.setStatus("mandatory")
_LucentPM4ChasCmdEntry_Object = MibTableRow
lucentPM4ChasCmdEntry = _LucentPM4ChasCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1)
)
lucentPM4ChasCmdEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4ChasCmdIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4ChasCmdEntry.setStatus("mandatory")


class _LucentPM4ChasCmdIndex_Type(Integer32):
    """Custom type lucentPM4ChasCmdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LucentPM4ChasCmdIndex_Type.__name__ = "Integer32"
_LucentPM4ChasCmdIndex_Object = MibTableColumn
lucentPM4ChasCmdIndex = _LucentPM4ChasCmdIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 1),
    _LucentPM4ChasCmdIndex_Type()
)
lucentPM4ChasCmdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdIndex.setStatus("mandatory")
_LucentPM4ChasCmdBoardId_Type = Integer32
_LucentPM4ChasCmdBoardId_Object = MibTableColumn
lucentPM4ChasCmdBoardId = _LucentPM4ChasCmdBoardId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 2),
    _LucentPM4ChasCmdBoardId_Type()
)
lucentPM4ChasCmdBoardId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdBoardId.setStatus("mandatory")
_LucentPM4ChasCmdUnitType_Type = PMUnitType
_LucentPM4ChasCmdUnitType_Object = MibTableColumn
lucentPM4ChasCmdUnitType = _LucentPM4ChasCmdUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 3),
    _LucentPM4ChasCmdUnitType_Type()
)
lucentPM4ChasCmdUnitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdUnitType.setStatus("mandatory")
_LucentPM4ChasCmdUnitIndex_Type = Integer32
_LucentPM4ChasCmdUnitIndex_Object = MibTableColumn
lucentPM4ChasCmdUnitIndex = _LucentPM4ChasCmdUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 4),
    _LucentPM4ChasCmdUnitIndex_Type()
)
lucentPM4ChasCmdUnitIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdUnitIndex.setStatus("mandatory")


class _LucentPM4ChasCmdDevId_Type(Integer32):
    """Custom type lucentPM4ChasCmdDevId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_LucentPM4ChasCmdDevId_Type.__name__ = "Integer32"
_LucentPM4ChasCmdDevId_Object = MibTableColumn
lucentPM4ChasCmdDevId = _LucentPM4ChasCmdDevId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 5),
    _LucentPM4ChasCmdDevId_Type()
)
lucentPM4ChasCmdDevId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdDevId.setStatus("mandatory")


class _LucentPM4ChasCmdId_Type(Integer32):
    """Custom type lucentPM4ChasCmdId based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("addfilter", 10),
          ("addlocation", 8),
          ("addmodem", 12),
          ("addospfarea", 14),
          ("addprop", 16),
          ("adduser", 6),
          ("deletefilter", 11),
          ("deleteprop", 17),
          ("deleteuser", 7),
          ("diallocation", 9),
          ("eraseallflash", 2),
          ("erasecomos", 28),
          ("eraseconfig", 27),
          ("eraseflashfile", 1),
          ("ifconfig", 26),
          ("ptrace", 25),
          ("reboot", 29),
          ("resetall", 21),
          ("resetconsole", 22),
          ("resetether0", 19),
          ("resetether1", 20),
          ("resetfilter", 5),
          ("resetospf", 15),
          ("resetport", 4),
          ("resetprop", 18),
          ("resetvirtport", 13),
          ("saveall", 3),
          ("traceroutes", 24),
          ("version", 23))
    )


_LucentPM4ChasCmdId_Type.__name__ = "Integer32"
_LucentPM4ChasCmdId_Object = MibTableColumn
lucentPM4ChasCmdId = _LucentPM4ChasCmdId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 6),
    _LucentPM4ChasCmdId_Type()
)
lucentPM4ChasCmdId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdId.setStatus("mandatory")


class _LucentPM4ChasCmdParams_Type(OctetString):
    """Custom type lucentPM4ChasCmdParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LucentPM4ChasCmdParams_Type.__name__ = "OctetString"
_LucentPM4ChasCmdParams_Object = MibTableColumn
lucentPM4ChasCmdParams = _LucentPM4ChasCmdParams_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 7),
    _LucentPM4ChasCmdParams_Type()
)
lucentPM4ChasCmdParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdParams.setStatus("mandatory")
_LucentPM4ChasCmdResult_Type = PMDiagCmdStatus
_LucentPM4ChasCmdResult_Object = MibTableColumn
lucentPM4ChasCmdResult = _LucentPM4ChasCmdResult_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 3, 2, 1, 8),
    _LucentPM4ChasCmdResult_Type()
)
lucentPM4ChasCmdResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ChasCmdResult.setStatus("mandatory")
_LucentPM4ConfigMgmt_ObjectIdentity = ObjectIdentity
lucentPM4ConfigMgmt = _LucentPM4ConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4)
)
_LucentPM4CmInterfaces_ObjectIdentity = ObjectIdentity
lucentPM4CmInterfaces = _LucentPM4CmInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1)
)
_LucentPM4CmSerial_ObjectIdentity = ObjectIdentity
lucentPM4CmSerial = _LucentPM4CmSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1)
)
_LucentPM4SerialTable_Object = MibTable
lucentPM4SerialTable = _LucentPM4SerialTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    lucentPM4SerialTable.setStatus("mandatory")
_LucentPM4SerialEntry_Object = MibTableRow
lucentPM4SerialEntry = _LucentPM4SerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1)
)
lucentPM4SerialEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4SerialBoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4SerialIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4SerialEntry.setStatus("mandatory")
_LucentPM4SerialBoardIndex_Type = Integer32
_LucentPM4SerialBoardIndex_Object = MibTableColumn
lucentPM4SerialBoardIndex = _LucentPM4SerialBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 1),
    _LucentPM4SerialBoardIndex_Type()
)
lucentPM4SerialBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialBoardIndex.setStatus("mandatory")
_LucentPM4SerialUnitType_Type = PMUnitType
_LucentPM4SerialUnitType_Object = MibTableColumn
lucentPM4SerialUnitType = _LucentPM4SerialUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 2),
    _LucentPM4SerialUnitType_Type()
)
lucentPM4SerialUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialUnitType.setStatus("mandatory")
_LucentPM4SerialIndex_Type = Integer32
_LucentPM4SerialIndex_Object = MibTableColumn
lucentPM4SerialIndex = _LucentPM4SerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 3),
    _LucentPM4SerialIndex_Type()
)
lucentPM4SerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialIndex.setStatus("mandatory")
_LucentPM4ModemId_Type = Integer32
_LucentPM4ModemId_Object = MibTableColumn
lucentPM4ModemId = _LucentPM4ModemId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 4),
    _LucentPM4ModemId_Type()
)
lucentPM4ModemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemId.setStatus("mandatory")
_LucentPM4SerialPortNumber_Type = Integer32
_LucentPM4SerialPortNumber_Object = MibTableColumn
lucentPM4SerialPortNumber = _LucentPM4SerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 5),
    _LucentPM4SerialPortNumber_Type()
)
lucentPM4SerialPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialPortNumber.setStatus("mandatory")


class _LucentPM4SerialPhysType_Type(Integer32):
    """Custom type lucentPM4SerialPhysType based on Integer32"""
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
        *(("async", 2),
          ("isdn", 4),
          ("other", 1),
          ("sync", 3))
    )


_LucentPM4SerialPhysType_Type.__name__ = "Integer32"
_LucentPM4SerialPhysType_Object = MibTableColumn
lucentPM4SerialPhysType = _LucentPM4SerialPhysType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 6),
    _LucentPM4SerialPhysType_Type()
)
lucentPM4SerialPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialPhysType.setStatus("mandatory")


class _LucentPM4SerialPortStatus_Type(Integer32):
    """Custom type lucentPM4SerialPortStatus based on Integer32"""
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
        *(("command", 5),
          ("connecting", 2),
          ("disconnecting", 4),
          ("established", 3),
          ("idle", 1),
          ("noservice", 6))
    )


_LucentPM4SerialPortStatus_Type.__name__ = "Integer32"
_LucentPM4SerialPortStatus_Object = MibTableColumn
lucentPM4SerialPortStatus = _LucentPM4SerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 7),
    _LucentPM4SerialPortStatus_Type()
)
lucentPM4SerialPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialPortStatus.setStatus("mandatory")


class _LucentPM4SerialDS0State_Type(Integer32):
    """Custom type lucentPM4SerialDS0State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("busyout", 2),
          ("havecomport", 3),
          ("notavailable", 1))
    )


_LucentPM4SerialDS0State_Type.__name__ = "Integer32"
_LucentPM4SerialDS0State_Object = MibTableColumn
lucentPM4SerialDS0State = _LucentPM4SerialDS0State_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 8),
    _LucentPM4SerialDS0State_Type()
)
lucentPM4SerialDS0State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialDS0State.setStatus("mandatory")


class _LucentPM4SerialUser_Type(DisplayString):
    """Custom type lucentPM4SerialUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LucentPM4SerialUser_Type.__name__ = "DisplayString"
_LucentPM4SerialUser_Object = MibTableColumn
lucentPM4SerialUser = _LucentPM4SerialUser_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 9),
    _LucentPM4SerialUser_Type()
)
lucentPM4SerialUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialUser.setStatus("mandatory")


class _LucentPM4SerialSessionId_Type(DisplayString):
    """Custom type lucentPM4SerialSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LucentPM4SerialSessionId_Type.__name__ = "DisplayString"
_LucentPM4SerialSessionId_Object = MibTableColumn
lucentPM4SerialSessionId = _LucentPM4SerialSessionId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 10),
    _LucentPM4SerialSessionId_Type()
)
lucentPM4SerialSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialSessionId.setStatus("mandatory")


class _LucentPM4SerialTypeHardwired_Type(Integer32):
    """Custom type lucentPM4SerialTypeHardwired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4SerialTypeHardwired_Type.__name__ = "Integer32"
_LucentPM4SerialTypeHardwired_Object = MibTableColumn
lucentPM4SerialTypeHardwired = _LucentPM4SerialTypeHardwired_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 11),
    _LucentPM4SerialTypeHardwired_Type()
)
lucentPM4SerialTypeHardwired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeHardwired.setStatus("mandatory")


class _LucentPM4SerialTypeNwDialIn_Type(Integer32):
    """Custom type lucentPM4SerialTypeNwDialIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4SerialTypeNwDialIn_Type.__name__ = "Integer32"
_LucentPM4SerialTypeNwDialIn_Object = MibTableColumn
lucentPM4SerialTypeNwDialIn = _LucentPM4SerialTypeNwDialIn_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 12),
    _LucentPM4SerialTypeNwDialIn_Type()
)
lucentPM4SerialTypeNwDialIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeNwDialIn.setStatus("mandatory")


class _LucentPM4SerialTypeNwDialout_Type(Integer32):
    """Custom type lucentPM4SerialTypeNwDialout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4SerialTypeNwDialout_Type.__name__ = "Integer32"
_LucentPM4SerialTypeNwDialout_Object = MibTableColumn
lucentPM4SerialTypeNwDialout = _LucentPM4SerialTypeNwDialout_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 13),
    _LucentPM4SerialTypeNwDialout_Type()
)
lucentPM4SerialTypeNwDialout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeNwDialout.setStatus("mandatory")


class _LucentPM4SerialTypeLogin_Type(Integer32):
    """Custom type lucentPM4SerialTypeLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4SerialTypeLogin_Type.__name__ = "Integer32"
_LucentPM4SerialTypeLogin_Object = MibTableColumn
lucentPM4SerialTypeLogin = _LucentPM4SerialTypeLogin_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 14),
    _LucentPM4SerialTypeLogin_Type()
)
lucentPM4SerialTypeLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeLogin.setStatus("mandatory")


class _LucentPM4SerialTypeDevice_Type(Integer32):
    """Custom type lucentPM4SerialTypeDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4SerialTypeDevice_Type.__name__ = "Integer32"
_LucentPM4SerialTypeDevice_Object = MibTableColumn
lucentPM4SerialTypeDevice = _LucentPM4SerialTypeDevice_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 15),
    _LucentPM4SerialTypeDevice_Type()
)
lucentPM4SerialTypeDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeDevice.setStatus("mandatory")
_LucentPM4SerialTypeDeviceName_Type = DisplayString
_LucentPM4SerialTypeDeviceName_Object = MibTableColumn
lucentPM4SerialTypeDeviceName = _LucentPM4SerialTypeDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 16),
    _LucentPM4SerialTypeDeviceName_Type()
)
lucentPM4SerialTypeDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SerialTypeDeviceName.setStatus("mandatory")


class _LucentPM4SerialDirection_Type(Integer32):
    """Custom type lucentPM4SerialDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("inout", 3),
          ("out", 2))
    )


_LucentPM4SerialDirection_Type.__name__ = "Integer32"
_LucentPM4SerialDirection_Object = MibTableColumn
lucentPM4SerialDirection = _LucentPM4SerialDirection_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 17),
    _LucentPM4SerialDirection_Type()
)
lucentPM4SerialDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialDirection.setStatus("mandatory")
_LucentPM4SerialStarted_Type = TimeTicks
_LucentPM4SerialStarted_Object = MibScalar
lucentPM4SerialStarted = _LucentPM4SerialStarted_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 18),
    _LucentPM4SerialStarted_Type()
)
lucentPM4SerialStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialStarted.setStatus("mandatory")
_LucentPM4SerialIdle_Type = TimeTicks
_LucentPM4SerialIdle_Object = MibTableColumn
lucentPM4SerialIdle = _LucentPM4SerialIdle_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 19),
    _LucentPM4SerialIdle_Type()
)
lucentPM4SerialIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialIdle.setStatus("mandatory")
_LucentPM4SerialInSpeed_Type = Gauge32
_LucentPM4SerialInSpeed_Object = MibTableColumn
lucentPM4SerialInSpeed = _LucentPM4SerialInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 20),
    _LucentPM4SerialInSpeed_Type()
)
lucentPM4SerialInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialInSpeed.setStatus("mandatory")
_LucentPM4SerialOutSpeed_Type = Gauge32
_LucentPM4SerialOutSpeed_Object = MibTableColumn
lucentPM4SerialOutSpeed = _LucentPM4SerialOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 21),
    _LucentPM4SerialOutSpeed_Type()
)
lucentPM4SerialOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialOutSpeed.setStatus("mandatory")
_LucentPM4SerialIpAddress_Type = IpAddress
_LucentPM4SerialIpAddress_Object = MibTableColumn
lucentPM4SerialIpAddress = _LucentPM4SerialIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 22),
    _LucentPM4SerialIpAddress_Type()
)
lucentPM4SerialIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialIpAddress.setStatus("mandatory")


class _LucentPM4SerialifDescr_Type(DisplayString):
    """Custom type lucentPM4SerialifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LucentPM4SerialifDescr_Type.__name__ = "DisplayString"
_LucentPM4SerialifDescr_Object = MibTableColumn
lucentPM4SerialifDescr = _LucentPM4SerialifDescr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 23),
    _LucentPM4SerialifDescr_Type()
)
lucentPM4SerialifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialifDescr.setStatus("mandatory")
_LucentPM4SerialInOctets_Type = Counter32
_LucentPM4SerialInOctets_Object = MibTableColumn
lucentPM4SerialInOctets = _LucentPM4SerialInOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 24),
    _LucentPM4SerialInOctets_Type()
)
lucentPM4SerialInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialInOctets.setStatus("mandatory")
_LucentPM4SerialOutOctets_Type = Counter32
_LucentPM4SerialOutOctets_Object = MibTableColumn
lucentPM4SerialOutOctets = _LucentPM4SerialOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 25),
    _LucentPM4SerialOutOctets_Type()
)
lucentPM4SerialOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialOutOctets.setStatus("mandatory")
_LucentPM4SerialQOctets_Type = Counter32
_LucentPM4SerialQOctets_Object = MibScalar
lucentPM4SerialQOctets = _LucentPM4SerialQOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 1, 1, 1, 26),
    _LucentPM4SerialQOctets_Type()
)
lucentPM4SerialQOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SerialQOctets.setStatus("mandatory")
_LucentPM4CmT1E1_ObjectIdentity = ObjectIdentity
lucentPM4CmT1E1 = _LucentPM4CmT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2)
)
_LucentPM4T1E1Table_Object = MibTable
lucentPM4T1E1Table = _LucentPM4T1E1Table_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    lucentPM4T1E1Table.setStatus("mandatory")
_LucentPM4T1E1Entry_Object = MibTableRow
lucentPM4T1E1Entry = _LucentPM4T1E1Entry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1)
)
lucentPM4T1E1Entry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1BoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1Index"),
)
if mibBuilder.loadTexts:
    lucentPM4T1E1Entry.setStatus("mandatory")
_LucentPM4T1E1BoardIndex_Type = Integer32
_LucentPM4T1E1BoardIndex_Object = MibTableColumn
lucentPM4T1E1BoardIndex = _LucentPM4T1E1BoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 1),
    _LucentPM4T1E1BoardIndex_Type()
)
lucentPM4T1E1BoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1BoardIndex.setStatus("mandatory")
_LucentPM4T1E1UnitType_Type = PMUnitType
_LucentPM4T1E1UnitType_Object = MibTableColumn
lucentPM4T1E1UnitType = _LucentPM4T1E1UnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 2),
    _LucentPM4T1E1UnitType_Type()
)
lucentPM4T1E1UnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1UnitType.setStatus("mandatory")
_LucentPM4T1E1Index_Type = Integer32
_LucentPM4T1E1Index_Object = MibTableColumn
lucentPM4T1E1Index = _LucentPM4T1E1Index_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 3),
    _LucentPM4T1E1Index_Type()
)
lucentPM4T1E1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1Index.setStatus("mandatory")
_LucentPM4T1E1SerialIndex_Type = Integer32
_LucentPM4T1E1SerialIndex_Object = MibTableColumn
lucentPM4T1E1SerialIndex = _LucentPM4T1E1SerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 4),
    _LucentPM4T1E1SerialIndex_Type()
)
lucentPM4T1E1SerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1SerialIndex.setStatus("mandatory")
_LucentPM4T1E1SerialCount_Type = Integer32
_LucentPM4T1E1SerialCount_Object = MibTableColumn
lucentPM4T1E1SerialCount = _LucentPM4T1E1SerialCount_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 5),
    _LucentPM4T1E1SerialCount_Type()
)
lucentPM4T1E1SerialCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1SerialCount.setStatus("mandatory")


class _LucentPM4T1E1PhysType_Type(Integer32):
    """Custom type lucentPM4T1E1PhysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_LucentPM4T1E1PhysType_Type.__name__ = "Integer32"
_LucentPM4T1E1PhysType_Object = MibTableColumn
lucentPM4T1E1PhysType = _LucentPM4T1E1PhysType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 6),
    _LucentPM4T1E1PhysType_Type()
)
lucentPM4T1E1PhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PhysType.setStatus("mandatory")
_LucentPM4T1E1Status_Type = PMEquipPRIStatus
_LucentPM4T1E1Status_Object = MibTableColumn
lucentPM4T1E1Status = _LucentPM4T1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 7),
    _LucentPM4T1E1Status_Type()
)
lucentPM4T1E1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1Status.setStatus("mandatory")


class _LucentPM4T1E1Function_Type(Integer32):
    """Custom type lucentPM4T1E1Function based on Integer32"""
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
        *(("channelized", 2),
          ("clear", 3),
          ("fractional", 4),
          ("isdn", 1),
          ("isdnfrac", 5))
    )


_LucentPM4T1E1Function_Type.__name__ = "Integer32"
_LucentPM4T1E1Function_Object = MibTableColumn
lucentPM4T1E1Function = _LucentPM4T1E1Function_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 8),
    _LucentPM4T1E1Function_Type()
)
lucentPM4T1E1Function.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1Function.setStatus("mandatory")


class _LucentPM4T1E1Framing_Type(Integer32):
    """Custom type lucentPM4T1E1Framing based on Integer32"""
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
        *(("crc4", 3),
          ("d4", 2),
          ("esf", 1),
          ("fas", 4))
    )


_LucentPM4T1E1Framing_Type.__name__ = "Integer32"
_LucentPM4T1E1Framing_Object = MibTableColumn
lucentPM4T1E1Framing = _LucentPM4T1E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 9),
    _LucentPM4T1E1Framing_Type()
)
lucentPM4T1E1Framing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1Framing.setStatus("mandatory")


class _LucentPM4T1E1Encoding_Type(Integer32):
    """Custom type lucentPM4T1E1Encoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_LucentPM4T1E1Encoding_Type.__name__ = "Integer32"
_LucentPM4T1E1Encoding_Object = MibTableColumn
lucentPM4T1E1Encoding = _LucentPM4T1E1Encoding_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 10),
    _LucentPM4T1E1Encoding_Type()
)
lucentPM4T1E1Encoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1Encoding.setStatus("mandatory")


class _LucentPM4T1E1PCM_Type(Integer32):
    """Custom type lucentPM4T1E1PCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 2),
          ("ulaw", 1))
    )


_LucentPM4T1E1PCM_Type.__name__ = "Integer32"
_LucentPM4T1E1PCM_Object = MibTableColumn
lucentPM4T1E1PCM = _LucentPM4T1E1PCM_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 11),
    _LucentPM4T1E1PCM_Type()
)
lucentPM4T1E1PCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PCM.setStatus("mandatory")


class _LucentPM4T1E1SuperSignal_Type(Integer32):
    """Custom type lucentPM4T1E1SuperSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("em", 1),
          ("groundstart", 2))
    )


_LucentPM4T1E1SuperSignal_Type.__name__ = "Integer32"
_LucentPM4T1E1SuperSignal_Object = MibTableColumn
lucentPM4T1E1SuperSignal = _LucentPM4T1E1SuperSignal_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 12),
    _LucentPM4T1E1SuperSignal_Type()
)
lucentPM4T1E1SuperSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4T1E1SuperSignal.setStatus("mandatory")


class _LucentPM4T1E1StartMode_Type(Integer32):
    """Custom type lucentPM4T1E1StartMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediate", 2),
          ("wink", 1))
    )


_LucentPM4T1E1StartMode_Type.__name__ = "Integer32"
_LucentPM4T1E1StartMode_Object = MibTableColumn
lucentPM4T1E1StartMode = _LucentPM4T1E1StartMode_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 13),
    _LucentPM4T1E1StartMode_Type()
)
lucentPM4T1E1StartMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4T1E1StartMode.setStatus("mandatory")
_LucentPM4T1E1ChangeTime_Type = TimeTicks
_LucentPM4T1E1ChangeTime_Object = MibTableColumn
lucentPM4T1E1ChangeTime = _LucentPM4T1E1ChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 14),
    _LucentPM4T1E1ChangeTime_Type()
)
lucentPM4T1E1ChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1ChangeTime.setStatus("mandatory")
_LucentPM4T1E1RecvLevel_Type = Gauge32
_LucentPM4T1E1RecvLevel_Object = MibTableColumn
lucentPM4T1E1RecvLevel = _LucentPM4T1E1RecvLevel_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 15),
    _LucentPM4T1E1RecvLevel_Type()
)
lucentPM4T1E1RecvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1RecvLevel.setStatus("mandatory")
_LucentPM4T1E1BlueAlarms_Type = Counter32
_LucentPM4T1E1BlueAlarms_Object = MibTableColumn
lucentPM4T1E1BlueAlarms = _LucentPM4T1E1BlueAlarms_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 16),
    _LucentPM4T1E1BlueAlarms_Type()
)
lucentPM4T1E1BlueAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1BlueAlarms.setStatus("mandatory")
_LucentPM4T1E1YellowAlarms_Type = Counter32
_LucentPM4T1E1YellowAlarms_Object = MibTableColumn
lucentPM4T1E1YellowAlarms = _LucentPM4T1E1YellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 17),
    _LucentPM4T1E1YellowAlarms_Type()
)
lucentPM4T1E1YellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1YellowAlarms.setStatus("mandatory")
_LucentPM4T1E1CarrierLoss_Type = Counter32
_LucentPM4T1E1CarrierLoss_Object = MibTableColumn
lucentPM4T1E1CarrierLoss = _LucentPM4T1E1CarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 18),
    _LucentPM4T1E1CarrierLoss_Type()
)
lucentPM4T1E1CarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1CarrierLoss.setStatus("mandatory")
_LucentPM4T1E1SyncLoss_Type = Counter32
_LucentPM4T1E1SyncLoss_Object = MibTableColumn
lucentPM4T1E1SyncLoss = _LucentPM4T1E1SyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 19),
    _LucentPM4T1E1SyncLoss_Type()
)
lucentPM4T1E1SyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1SyncLoss.setStatus("mandatory")
_LucentPM4T1E1BipolarErrors_Type = Counter32
_LucentPM4T1E1BipolarErrors_Object = MibTableColumn
lucentPM4T1E1BipolarErrors = _LucentPM4T1E1BipolarErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 20),
    _LucentPM4T1E1BipolarErrors_Type()
)
lucentPM4T1E1BipolarErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1BipolarErrors.setStatus("mandatory")
_LucentPM4T1E1CRCErrors_Type = Counter32
_LucentPM4T1E1CRCErrors_Object = MibTableColumn
lucentPM4T1E1CRCErrors = _LucentPM4T1E1CRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 21),
    _LucentPM4T1E1CRCErrors_Type()
)
lucentPM4T1E1CRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1CRCErrors.setStatus("mandatory")
_LucentPM4T1E1SyncErrors_Type = Counter32
_LucentPM4T1E1SyncErrors_Object = MibTableColumn
lucentPM4T1E1SyncErrors = _LucentPM4T1E1SyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 2, 1, 1, 22),
    _LucentPM4T1E1SyncErrors_Type()
)
lucentPM4T1E1SyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1SyncErrors.setStatus("mandatory")
_LucentPM4CmModem_ObjectIdentity = ObjectIdentity
lucentPM4CmModem = _LucentPM4CmModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3)
)
_LucentPM4ModemTable_Object = MibTable
lucentPM4ModemTable = _LucentPM4ModemTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lucentPM4ModemTable.setStatus("mandatory")
_LucentPM4ModemEntry_Object = MibTableRow
lucentPM4ModemEntry = _LucentPM4ModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1)
)
lucentPM4ModemEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4ModemBoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4ModemUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4ModemIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4ModemEntry.setStatus("mandatory")
_LucentPM4ModemBoardIndex_Type = Integer32
_LucentPM4ModemBoardIndex_Object = MibTableColumn
lucentPM4ModemBoardIndex = _LucentPM4ModemBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 1),
    _LucentPM4ModemBoardIndex_Type()
)
lucentPM4ModemBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemBoardIndex.setStatus("mandatory")
_LucentPM4ModemUnitType_Type = PMUnitType
_LucentPM4ModemUnitType_Object = MibTableColumn
lucentPM4ModemUnitType = _LucentPM4ModemUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 2),
    _LucentPM4ModemUnitType_Type()
)
lucentPM4ModemUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemUnitType.setStatus("mandatory")
_LucentPM4ModemIndex_Type = Integer32
_LucentPM4ModemIndex_Object = MibTableColumn
lucentPM4ModemIndex = _LucentPM4ModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 3),
    _LucentPM4ModemIndex_Type()
)
lucentPM4ModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemIndex.setStatus("mandatory")


class _LucentPM4ModemPortName_Type(DisplayString):
    """Custom type lucentPM4ModemPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LucentPM4ModemPortName_Type.__name__ = "DisplayString"
_LucentPM4ModemPortName_Object = MibTableColumn
lucentPM4ModemPortName = _LucentPM4ModemPortName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 4),
    _LucentPM4ModemPortName_Type()
)
lucentPM4ModemPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemPortName.setStatus("mandatory")


class _LucentPM4ModemStatus_Type(Integer32):
    """Custom type lucentPM4ModemStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("admin", 9),
          ("bound", 2),
          ("connecting", 3),
          ("down", 6),
          ("halt", 8),
          ("none", 1),
          ("ready", 7),
          ("test", 5))
    )


_LucentPM4ModemStatus_Type.__name__ = "Integer32"
_LucentPM4ModemStatus_Object = MibTableColumn
lucentPM4ModemStatus = _LucentPM4ModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 5),
    _LucentPM4ModemStatus_Type()
)
lucentPM4ModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemStatus.setStatus("mandatory")


class _LucentPM4ModemProtocol_Type(Integer32):
    """Custom type lucentPM4ModemProtocol based on Integer32"""
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
        *(("bufferd", 4),
          ("cellular", 6),
          ("direct", 5),
          ("lapm", 2),
          ("mnp", 3),
          ("none", 1))
    )


_LucentPM4ModemProtocol_Type.__name__ = "Integer32"
_LucentPM4ModemProtocol_Object = MibTableColumn
lucentPM4ModemProtocol = _LucentPM4ModemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 6),
    _LucentPM4ModemProtocol_Type()
)
lucentPM4ModemProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemProtocol.setStatus("mandatory")


class _LucentPM4ModemCompression_Type(Integer32):
    """Custom type lucentPM4ModemCompression based on Integer32"""
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
        *(("mnp5", 3),
          ("none", 1),
          ("stac", 4),
          ("v42bis", 2))
    )


_LucentPM4ModemCompression_Type.__name__ = "Integer32"
_LucentPM4ModemCompression_Object = MibTableColumn
lucentPM4ModemCompression = _LucentPM4ModemCompression_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 7),
    _LucentPM4ModemCompression_Type()
)
lucentPM4ModemCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemCompression.setStatus("mandatory")
_LucentPM4ModemInSpeed_Type = Gauge32
_LucentPM4ModemInSpeed_Object = MibTableColumn
lucentPM4ModemInSpeed = _LucentPM4ModemInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 8),
    _LucentPM4ModemInSpeed_Type()
)
lucentPM4ModemInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemInSpeed.setStatus("mandatory")
_LucentPM4ModemOutSpeed_Type = Gauge32
_LucentPM4ModemOutSpeed_Object = MibTableColumn
lucentPM4ModemOutSpeed = _LucentPM4ModemOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 9),
    _LucentPM4ModemOutSpeed_Type()
)
lucentPM4ModemOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemOutSpeed.setStatus("mandatory")
_LucentPM4ModemInByteCount_Type = Counter32
_LucentPM4ModemInByteCount_Object = MibTableColumn
lucentPM4ModemInByteCount = _LucentPM4ModemInByteCount_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 10),
    _LucentPM4ModemInByteCount_Type()
)
lucentPM4ModemInByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemInByteCount.setStatus("mandatory")
_LucentPM4ModemOutByteCount_Type = Counter32
_LucentPM4ModemOutByteCount_Object = MibTableColumn
lucentPM4ModemOutByteCount = _LucentPM4ModemOutByteCount_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 11),
    _LucentPM4ModemOutByteCount_Type()
)
lucentPM4ModemOutByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemOutByteCount.setStatus("mandatory")
_LucentPM4ModemRetrains_Type = Counter32
_LucentPM4ModemRetrains_Object = MibTableColumn
lucentPM4ModemRetrains = _LucentPM4ModemRetrains_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 12),
    _LucentPM4ModemRetrains_Type()
)
lucentPM4ModemRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemRetrains.setStatus("mandatory")
_LucentPM4ModemRenegotiates_Type = Counter32
_LucentPM4ModemRenegotiates_Object = MibTableColumn
lucentPM4ModemRenegotiates = _LucentPM4ModemRenegotiates_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 13),
    _LucentPM4ModemRenegotiates_Type()
)
lucentPM4ModemRenegotiates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemRenegotiates.setStatus("mandatory")
_LucentPM4ModemCalls_Type = Counter32
_LucentPM4ModemCalls_Object = MibTableColumn
lucentPM4ModemCalls = _LucentPM4ModemCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 14),
    _LucentPM4ModemCalls_Type()
)
lucentPM4ModemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemCalls.setStatus("mandatory")
_LucentPM4ModemDetects_Type = Counter32
_LucentPM4ModemDetects_Object = MibTableColumn
lucentPM4ModemDetects = _LucentPM4ModemDetects_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 15),
    _LucentPM4ModemDetects_Type()
)
lucentPM4ModemDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemDetects.setStatus("mandatory")
_LucentPM4ModemConnects_Type = Counter32
_LucentPM4ModemConnects_Object = MibTableColumn
lucentPM4ModemConnects = _LucentPM4ModemConnects_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 3, 1, 1, 16),
    _LucentPM4ModemConnects_Type()
)
lucentPM4ModemConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4ModemConnects.setStatus("mandatory")
_LucentPM4CmEther_ObjectIdentity = ObjectIdentity
lucentPM4CmEther = _LucentPM4CmEther_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4)
)
_LucentPM4EtherTable_Object = MibTable
lucentPM4EtherTable = _LucentPM4EtherTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lucentPM4EtherTable.setStatus("mandatory")
_LucentPM4EtherEntry_Object = MibTableRow
lucentPM4EtherEntry = _LucentPM4EtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1)
)
lucentPM4EtherEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4EtherBoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4EtherIfType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4EtherIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4EtherEntry.setStatus("mandatory")
_LucentPM4EtherBoardIndex_Type = Integer32
_LucentPM4EtherBoardIndex_Object = MibTableColumn
lucentPM4EtherBoardIndex = _LucentPM4EtherBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 1),
    _LucentPM4EtherBoardIndex_Type()
)
lucentPM4EtherBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4EtherBoardIndex.setStatus("mandatory")
_LucentPM4EtherIfType_Type = PMUnitType
_LucentPM4EtherIfType_Object = MibTableColumn
lucentPM4EtherIfType = _LucentPM4EtherIfType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 2),
    _LucentPM4EtherIfType_Type()
)
lucentPM4EtherIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4EtherIfType.setStatus("mandatory")


class _LucentPM4EtherIndex_Type(Integer32):
    """Custom type lucentPM4EtherIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ether0", 1),
          ("ether1", 2),
          ("other", 3))
    )


_LucentPM4EtherIndex_Type.__name__ = "Integer32"
_LucentPM4EtherIndex_Object = MibTableColumn
lucentPM4EtherIndex = _LucentPM4EtherIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 3),
    _LucentPM4EtherIndex_Type()
)
lucentPM4EtherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4EtherIndex.setStatus("mandatory")


class _LucentPM4EtherIfIndex_Type(Integer32):
    """Custom type lucentPM4EtherIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(67436545,
              168099841)
        )
    )
    namedValues = NamedValues(
        *(("ether0", 67436545),
          ("ether1", 168099841))
    )


_LucentPM4EtherIfIndex_Type.__name__ = "Integer32"
_LucentPM4EtherIfIndex_Object = MibTableColumn
lucentPM4EtherIfIndex = _LucentPM4EtherIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 4),
    _LucentPM4EtherIfIndex_Type()
)
lucentPM4EtherIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4EtherIfIndex.setStatus("mandatory")


class _LucentPM4EtherPortName_Type(DisplayString):
    """Custom type lucentPM4EtherPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_LucentPM4EtherPortName_Type.__name__ = "DisplayString"
_LucentPM4EtherPortName_Object = MibTableColumn
lucentPM4EtherPortName = _LucentPM4EtherPortName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 5),
    _LucentPM4EtherPortName_Type()
)
lucentPM4EtherPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherPortName.setStatus("mandatory")
_LucentPM4EtherMacAddress_Type = PhysAddress
_LucentPM4EtherMacAddress_Object = MibScalar
lucentPM4EtherMacAddress = _LucentPM4EtherMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 6),
    _LucentPM4EtherMacAddress_Type()
)
lucentPM4EtherMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4EtherMacAddress.setStatus("mandatory")
_LucentPM4EtherIpAddress_Type = IpAddress
_LucentPM4EtherIpAddress_Object = MibScalar
lucentPM4EtherIpAddress = _LucentPM4EtherIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 7),
    _LucentPM4EtherIpAddress_Type()
)
lucentPM4EtherIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherIpAddress.setStatus("mandatory")
_LucentPM4EtherIpGateway_Type = IpAddress
_LucentPM4EtherIpGateway_Object = MibScalar
lucentPM4EtherIpGateway = _LucentPM4EtherIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 8),
    _LucentPM4EtherIpGateway_Type()
)
lucentPM4EtherIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherIpGateway.setStatus("mandatory")
_LucentPM4EtherPriNameServer_Type = IpAddress
_LucentPM4EtherPriNameServer_Object = MibTableColumn
lucentPM4EtherPriNameServer = _LucentPM4EtherPriNameServer_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 9),
    _LucentPM4EtherPriNameServer_Type()
)
lucentPM4EtherPriNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherPriNameServer.setStatus("mandatory")
_LucentPM4EtherAltNameServer_Type = IpAddress
_LucentPM4EtherAltNameServer_Object = MibTableColumn
lucentPM4EtherAltNameServer = _LucentPM4EtherAltNameServer_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 10),
    _LucentPM4EtherAltNameServer_Type()
)
lucentPM4EtherAltNameServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherAltNameServer.setStatus("mandatory")
_LucentPM4EtherSubnetMask_Type = IpAddress
_LucentPM4EtherSubnetMask_Object = MibTableColumn
lucentPM4EtherSubnetMask = _LucentPM4EtherSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 11),
    _LucentPM4EtherSubnetMask_Type()
)
lucentPM4EtherSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherSubnetMask.setStatus("mandatory")


class _LucentPM4EtherInFilter_Type(DisplayString):
    """Custom type lucentPM4EtherInFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LucentPM4EtherInFilter_Type.__name__ = "DisplayString"
_LucentPM4EtherInFilter_Object = MibTableColumn
lucentPM4EtherInFilter = _LucentPM4EtherInFilter_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 12),
    _LucentPM4EtherInFilter_Type()
)
lucentPM4EtherInFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherInFilter.setStatus("mandatory")


class _LucentPM4EtherOutFilter_Type(DisplayString):
    """Custom type lucentPM4EtherOutFilter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LucentPM4EtherOutFilter_Type.__name__ = "DisplayString"
_LucentPM4EtherOutFilter_Object = MibTableColumn
lucentPM4EtherOutFilter = _LucentPM4EtherOutFilter_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 13),
    _LucentPM4EtherOutFilter_Type()
)
lucentPM4EtherOutFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOutFilter.setStatus("mandatory")


class _LucentPM4EtherOptRip_Type(Integer32):
    """Custom type lucentPM4EtherOptRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptRip_Type.__name__ = "Integer32"
_LucentPM4EtherOptRip_Object = MibTableColumn
lucentPM4EtherOptRip = _LucentPM4EtherOptRip_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 14),
    _LucentPM4EtherOptRip_Type()
)
lucentPM4EtherOptRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptRip.setStatus("mandatory")


class _LucentPM4EtherOptSlip_Type(Integer32):
    """Custom type lucentPM4EtherOptSlip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptSlip_Type.__name__ = "Integer32"
_LucentPM4EtherOptSlip_Object = MibTableColumn
lucentPM4EtherOptSlip = _LucentPM4EtherOptSlip_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 15),
    _LucentPM4EtherOptSlip_Type()
)
lucentPM4EtherOptSlip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptSlip.setStatus("mandatory")


class _LucentPM4EtherOptEtherDown_Type(Integer32):
    """Custom type lucentPM4EtherOptEtherDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptEtherDown_Type.__name__ = "Integer32"
_LucentPM4EtherOptEtherDown_Object = MibTableColumn
lucentPM4EtherOptEtherDown = _LucentPM4EtherOptEtherDown_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 16),
    _LucentPM4EtherOptEtherDown_Type()
)
lucentPM4EtherOptEtherDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptEtherDown.setStatus("mandatory")


class _LucentPM4EtherOptBcastHigh_Type(Integer32):
    """Custom type lucentPM4EtherOptBcastHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptBcastHigh_Type.__name__ = "Integer32"
_LucentPM4EtherOptBcastHigh_Object = MibTableColumn
lucentPM4EtherOptBcastHigh = _LucentPM4EtherOptBcastHigh_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 17),
    _LucentPM4EtherOptBcastHigh_Type()
)
lucentPM4EtherOptBcastHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptBcastHigh.setStatus("mandatory")


class _LucentPM4EtherOptSnmp_Type(Integer32):
    """Custom type lucentPM4EtherOptSnmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptSnmp_Type.__name__ = "Integer32"
_LucentPM4EtherOptSnmp_Object = MibTableColumn
lucentPM4EtherOptSnmp = _LucentPM4EtherOptSnmp_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 18),
    _LucentPM4EtherOptSnmp_Type()
)
lucentPM4EtherOptSnmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptSnmp.setStatus("mandatory")


class _LucentPM4EtherOptNoListen_Type(Integer32):
    """Custom type lucentPM4EtherOptNoListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptNoListen_Type.__name__ = "Integer32"
_LucentPM4EtherOptNoListen_Object = MibTableColumn
lucentPM4EtherOptNoListen = _LucentPM4EtherOptNoListen_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 19),
    _LucentPM4EtherOptNoListen_Type()
)
lucentPM4EtherOptNoListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptNoListen.setStatus("mandatory")


class _LucentPM4EtherOptDefaultRip_Type(Integer32):
    """Custom type lucentPM4EtherOptDefaultRip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptDefaultRip_Type.__name__ = "Integer32"
_LucentPM4EtherOptDefaultRip_Object = MibTableColumn
lucentPM4EtherOptDefaultRip = _LucentPM4EtherOptDefaultRip_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 20),
    _LucentPM4EtherOptDefaultRip_Type()
)
lucentPM4EtherOptDefaultRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptDefaultRip.setStatus("mandatory")


class _LucentPM4EtherOptDefaultListen_Type(Integer32):
    """Custom type lucentPM4EtherOptDefaultListen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptDefaultListen_Type.__name__ = "Integer32"
_LucentPM4EtherOptDefaultListen_Object = MibTableColumn
lucentPM4EtherOptDefaultListen = _LucentPM4EtherOptDefaultListen_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 21),
    _LucentPM4EtherOptDefaultListen_Type()
)
lucentPM4EtherOptDefaultListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptDefaultListen.setStatus("mandatory")


class _LucentPM4EtherOptIPFilter_Type(Integer32):
    """Custom type lucentPM4EtherOptIPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptIPFilter_Type.__name__ = "Integer32"
_LucentPM4EtherOptIPFilter_Object = MibTableColumn
lucentPM4EtherOptIPFilter = _LucentPM4EtherOptIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 22),
    _LucentPM4EtherOptIPFilter_Type()
)
lucentPM4EtherOptIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptIPFilter.setStatus("mandatory")


class _LucentPM4EtherOptDns_Type(Integer32):
    """Custom type lucentPM4EtherOptDns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptDns_Type.__name__ = "Integer32"
_LucentPM4EtherOptDns_Object = MibTableColumn
lucentPM4EtherOptDns = _LucentPM4EtherOptDns_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 23),
    _LucentPM4EtherOptDns_Type()
)
lucentPM4EtherOptDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptDns.setStatus("mandatory")


class _LucentPM4EtherOptPmeMsg_Type(Integer32):
    """Custom type lucentPM4EtherOptPmeMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptPmeMsg_Type.__name__ = "Integer32"
_LucentPM4EtherOptPmeMsg_Object = MibTableColumn
lucentPM4EtherOptPmeMsg = _LucentPM4EtherOptPmeMsg_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 24),
    _LucentPM4EtherOptPmeMsg_Type()
)
lucentPM4EtherOptPmeMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptPmeMsg.setStatus("mandatory")


class _LucentPM4EtherOptNoClip_Type(Integer32):
    """Custom type lucentPM4EtherOptNoClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptNoClip_Type.__name__ = "Integer32"
_LucentPM4EtherOptNoClip_Object = MibTableColumn
lucentPM4EtherOptNoClip = _LucentPM4EtherOptNoClip_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 25),
    _LucentPM4EtherOptNoClip_Type()
)
lucentPM4EtherOptNoClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptNoClip.setStatus("mandatory")


class _LucentPM4EtherOptEtherIpx_Type(Integer32):
    """Custom type lucentPM4EtherOptEtherIpx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptEtherIpx_Type.__name__ = "Integer32"
_LucentPM4EtherOptEtherIpx_Object = MibTableColumn
lucentPM4EtherOptEtherIpx = _LucentPM4EtherOptEtherIpx_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 26),
    _LucentPM4EtherOptEtherIpx_Type()
)
lucentPM4EtherOptEtherIpx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptEtherIpx.setStatus("mandatory")


class _LucentPM4EtherOptNetBIOS_Type(Integer32):
    """Custom type lucentPM4EtherOptNetBIOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptNetBIOS_Type.__name__ = "Integer32"
_LucentPM4EtherOptNetBIOS_Object = MibTableColumn
lucentPM4EtherOptNetBIOS = _LucentPM4EtherOptNetBIOS_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 27),
    _LucentPM4EtherOptNetBIOS_Type()
)
lucentPM4EtherOptNetBIOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptNetBIOS.setStatus("mandatory")


class _LucentPM4EtherOptAccounting_Type(Integer32):
    """Custom type lucentPM4EtherOptAccounting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptAccounting_Type.__name__ = "Integer32"
_LucentPM4EtherOptAccounting_Object = MibTableColumn
lucentPM4EtherOptAccounting = _LucentPM4EtherOptAccounting_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 28),
    _LucentPM4EtherOptAccounting_Type()
)
lucentPM4EtherOptAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptAccounting.setStatus("mandatory")


class _LucentPM4EtherOptNoPAP_Type(Integer32):
    """Custom type lucentPM4EtherOptNoPAP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4EtherOptNoPAP_Type.__name__ = "Integer32"
_LucentPM4EtherOptNoPAP_Object = MibTableColumn
lucentPM4EtherOptNoPAP = _LucentPM4EtherOptNoPAP_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 4, 1, 4, 1, 1, 29),
    _LucentPM4EtherOptNoPAP_Type()
)
lucentPM4EtherOptNoPAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4EtherOptNoPAP.setStatus("mandatory")
_LucentPM4FaultMgmt_ObjectIdentity = ObjectIdentity
lucentPM4FaultMgmt = _LucentPM4FaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5)
)
_LucentPM4FaultMgmtIsolation_ObjectIdentity = ObjectIdentity
lucentPM4FaultMgmtIsolation = _LucentPM4FaultMgmtIsolation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1)
)
_LucentPM4FaultMgmtChasTrap_Object = MibTable
lucentPM4FaultMgmtChasTrap = _LucentPM4FaultMgmtChasTrap_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    lucentPM4FaultMgmtChasTrap.setStatus("mandatory")
_LucentPM4FMChasTrapEntry_Object = MibTableRow
lucentPM4FMChasTrapEntry = _LucentPM4FMChasTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1)
)
lucentPM4FMChasTrapEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMChasTrapIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapEntry.setStatus("mandatory")
_LucentPM4FMChasTrapIndex_Type = Integer32
_LucentPM4FMChasTrapIndex_Object = MibTableColumn
lucentPM4FMChasTrapIndex = _LucentPM4FMChasTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 1),
    _LucentPM4FMChasTrapIndex_Type()
)
lucentPM4FMChasTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapIndex.setStatus("mandatory")
_LucentPM4FMChasTrapBoardID_Type = Integer32
_LucentPM4FMChasTrapBoardID_Object = MibScalar
lucentPM4FMChasTrapBoardID = _LucentPM4FMChasTrapBoardID_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 2),
    _LucentPM4FMChasTrapBoardID_Type()
)
lucentPM4FMChasTrapBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapBoardID.setStatus("mandatory")
_LucentPM4FMChasTrapUnitType_Type = PMUnitType
_LucentPM4FMChasTrapUnitType_Object = MibTableColumn
lucentPM4FMChasTrapUnitType = _LucentPM4FMChasTrapUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 3),
    _LucentPM4FMChasTrapUnitType_Type()
)
lucentPM4FMChasTrapUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapUnitType.setStatus("mandatory")
_LucentPM4FMChasTrapUnitIndex_Type = Integer32
_LucentPM4FMChasTrapUnitIndex_Object = MibTableColumn
lucentPM4FMChasTrapUnitIndex = _LucentPM4FMChasTrapUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 4),
    _LucentPM4FMChasTrapUnitIndex_Type()
)
lucentPM4FMChasTrapUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapUnitIndex.setStatus("mandatory")


class _LucentPM4FMChasTrapStatus_Type(Integer32):
    """Custom type lucentPM4FMChasTrapStatus based on Integer32"""
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
        *(("fault", 5),
          ("maintenance", 4),
          ("notinstalled", 6),
          ("offline", 3),
          ("online", 2),
          ("other", 1))
    )


_LucentPM4FMChasTrapStatus_Type.__name__ = "Integer32"
_LucentPM4FMChasTrapStatus_Object = MibTableColumn
lucentPM4FMChasTrapStatus = _LucentPM4FMChasTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 5),
    _LucentPM4FMChasTrapStatus_Type()
)
lucentPM4FMChasTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapStatus.setStatus("mandatory")
_LucentPM4FMChasTrapSeverity_Type = PMAlarmType
_LucentPM4FMChasTrapSeverity_Object = MibTableColumn
lucentPM4FMChasTrapSeverity = _LucentPM4FMChasTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 6),
    _LucentPM4FMChasTrapSeverity_Type()
)
lucentPM4FMChasTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapSeverity.setStatus("mandatory")
_LucentPM4FMChasTrapTimeStamp_Type = TimeTicks
_LucentPM4FMChasTrapTimeStamp_Object = MibTableColumn
lucentPM4FMChasTrapTimeStamp = _LucentPM4FMChasTrapTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 7),
    _LucentPM4FMChasTrapTimeStamp_Type()
)
lucentPM4FMChasTrapTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapTimeStamp.setStatus("mandatory")


class _LucentPM4FMChasTrapState_Type(Integer32):
    """Custom type lucentPM4FMChasTrapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ackdue", 2),
          ("acked", 3),
          ("trapsent", 1))
    )


_LucentPM4FMChasTrapState_Type.__name__ = "Integer32"
_LucentPM4FMChasTrapState_Object = MibTableColumn
lucentPM4FMChasTrapState = _LucentPM4FMChasTrapState_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 1, 1, 8),
    _LucentPM4FMChasTrapState_Type()
)
lucentPM4FMChasTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMChasTrapState.setStatus("mandatory")
_LucentPM4FMBoardIndex_Type = Integer32
_LucentPM4FMBoardIndex_Object = MibScalar
lucentPM4FMBoardIndex = _LucentPM4FMBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 2),
    _LucentPM4FMBoardIndex_Type()
)
lucentPM4FMBoardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4FMBoardIndex.setStatus("mandatory")
_LucentPM4FMUnitIndex_Type = Integer32
_LucentPM4FMUnitIndex_Object = MibScalar
lucentPM4FMUnitIndex = _LucentPM4FMUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 3),
    _LucentPM4FMUnitIndex_Type()
)
lucentPM4FMUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4FMUnitIndex.setStatus("mandatory")
_LucentPM4FMUnitType_Type = PMUnitType
_LucentPM4FMUnitType_Object = MibScalar
lucentPM4FMUnitType = _LucentPM4FMUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 4),
    _LucentPM4FMUnitType_Type()
)
lucentPM4FMUnitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4FMUnitType.setStatus("mandatory")


class _LucentPM4FMUnitTrapStatus_Type(Integer32):
    """Custom type lucentPM4FMUnitTrapStatus based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ais", 13),
          ("bes", 28),
          ("bpv", 18),
          ("carrierloss", 10),
          ("crc", 17),
          ("css", 27),
          ("cv", 16),
          ("dm", 25),
          ("dtrloss", 9),
          ("es", 21),
          ("failed", 4),
          ("fer", 19),
          ("les", 26),
          ("los", 12),
          ("offline", 2),
          ("online", 3),
          ("other", 1),
          ("pll", 20),
          ("pwrwarn", 6),
          ("redalarm", 14),
          ("renegotiation", 11),
          ("restored", 5),
          ("sefs", 23),
          ("ses", 22),
          ("temphot", 8),
          ("tempwarn", 7),
          ("uas", 24),
          ("yellowalarm", 15))
    )


_LucentPM4FMUnitTrapStatus_Type.__name__ = "Integer32"
_LucentPM4FMUnitTrapStatus_Object = MibScalar
lucentPM4FMUnitTrapStatus = _LucentPM4FMUnitTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 5),
    _LucentPM4FMUnitTrapStatus_Type()
)
lucentPM4FMUnitTrapStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4FMUnitTrapStatus.setStatus("mandatory")
_LucentPM4FMUnitTrapSeverity_Type = PMAlarmType
_LucentPM4FMUnitTrapSeverity_Object = MibScalar
lucentPM4FMUnitTrapSeverity = _LucentPM4FMUnitTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 1, 6),
    _LucentPM4FMUnitTrapSeverity_Type()
)
lucentPM4FMUnitTrapSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4FMUnitTrapSeverity.setStatus("mandatory")
_LucentPM4FMTrapConfig_ObjectIdentity = ObjectIdentity
lucentPM4FMTrapConfig = _LucentPM4FMTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2)
)
_LucentPM4FMEqpTrapCfg_Object = MibTable
lucentPM4FMEqpTrapCfg = _LucentPM4FMEqpTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    lucentPM4FMEqpTrapCfg.setStatus("mandatory")
_LucentPM4FMEqpTrapCfgEntry_Object = MibTableRow
lucentPM4FMEqpTrapCfgEntry = _LucentPM4FMEqpTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1)
)
lucentPM4FMEqpTrapCfgEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEqpBoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEqpUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEqpUnitIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4FMEqpTrapCfgEntry.setStatus("mandatory")
_LucentPM4FMEqpBoardIndex_Type = Integer32
_LucentPM4FMEqpBoardIndex_Object = MibTableColumn
lucentPM4FMEqpBoardIndex = _LucentPM4FMEqpBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 1),
    _LucentPM4FMEqpBoardIndex_Type()
)
lucentPM4FMEqpBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEqpBoardIndex.setStatus("mandatory")
_LucentPM4FMEqpUnitType_Type = PMUnitType
_LucentPM4FMEqpUnitType_Object = MibTableColumn
lucentPM4FMEqpUnitType = _LucentPM4FMEqpUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 2),
    _LucentPM4FMEqpUnitType_Type()
)
lucentPM4FMEqpUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEqpUnitType.setStatus("mandatory")
_LucentPM4FMEqpUnitIndex_Type = Integer32
_LucentPM4FMEqpUnitIndex_Object = MibScalar
lucentPM4FMEqpUnitIndex = _LucentPM4FMEqpUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 3),
    _LucentPM4FMEqpUnitIndex_Type()
)
lucentPM4FMEqpUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEqpUnitIndex.setStatus("mandatory")


class _LucentPM4FMEqpTrapId_Type(Integer32):
    """Custom type lucentPM4FMEqpTrapId based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("boardoffline", 1),
          ("boardonline", 2),
          ("boardpwrshutdown", 14),
          ("boardtempnormal", 8),
          ("boardtempwarn", 7),
          ("boardtoohot", 9),
          ("fanfail", 5),
          ("fanrestored", 6),
          ("linedown", 11),
          ("linethresh", 13),
          ("lineup", 12),
          ("modemfail", 10),
          ("pwrsupfail", 3),
          ("pwrsuprestored", 4),
          ("radiusauthfail", 15))
    )


_LucentPM4FMEqpTrapId_Type.__name__ = "Integer32"
_LucentPM4FMEqpTrapId_Object = MibTableColumn
lucentPM4FMEqpTrapId = _LucentPM4FMEqpTrapId_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 4),
    _LucentPM4FMEqpTrapId_Type()
)
lucentPM4FMEqpTrapId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEqpTrapId.setStatus("mandatory")


class _LucentPM4FMEqpTrapCtl_Type(Integer32):
    """Custom type lucentPM4FMEqpTrapCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4FMEqpTrapCtl_Type.__name__ = "Integer32"
_LucentPM4FMEqpTrapCtl_Object = MibTableColumn
lucentPM4FMEqpTrapCtl = _LucentPM4FMEqpTrapCtl_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 5),
    _LucentPM4FMEqpTrapCtl_Type()
)
lucentPM4FMEqpTrapCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEqpTrapCtl.setStatus("mandatory")
_LucentPM4FMEqpRepTimer_Type = Integer32
_LucentPM4FMEqpRepTimer_Object = MibScalar
lucentPM4FMEqpRepTimer = _LucentPM4FMEqpRepTimer_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 1, 1, 6),
    _LucentPM4FMEqpRepTimer_Type()
)
lucentPM4FMEqpRepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEqpRepTimer.setStatus("mandatory")
_LucentPM4FMT1E1ThreshTrapCfg_Object = MibTable
lucentPM4FMT1E1ThreshTrapCfg = _LucentPM4FMT1E1ThreshTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2)
)
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshTrapCfg.setStatus("mandatory")
_LucentPM4FMT1E1ThreshTrapCfgEntry_Object = MibTableRow
lucentPM4FMT1E1ThreshTrapCfgEntry = _LucentPM4FMT1E1ThreshTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1)
)
lucentPM4FMT1E1ThreshTrapCfgEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMThreshBoardIndex"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMThreshUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMThreshUnitIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshTrapCfgEntry.setStatus("mandatory")
_LucentPM4FMT1E1ThreshBoardIndex_Type = Integer32
_LucentPM4FMT1E1ThreshBoardIndex_Object = MibTableColumn
lucentPM4FMT1E1ThreshBoardIndex = _LucentPM4FMT1E1ThreshBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 1),
    _LucentPM4FMT1E1ThreshBoardIndex_Type()
)
lucentPM4FMT1E1ThreshBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshBoardIndex.setStatus("mandatory")
_LucentPM4FMT1E1ThreshUnitType_Type = PMUnitType
_LucentPM4FMT1E1ThreshUnitType_Object = MibTableColumn
lucentPM4FMT1E1ThreshUnitType = _LucentPM4FMT1E1ThreshUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 2),
    _LucentPM4FMT1E1ThreshUnitType_Type()
)
lucentPM4FMT1E1ThreshUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshUnitType.setStatus("mandatory")
_LucentPM4FMT1E1ThreshESs_Type = Gauge32
_LucentPM4FMT1E1ThreshESs_Object = MibTableColumn
lucentPM4FMT1E1ThreshESs = _LucentPM4FMT1E1ThreshESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 3),
    _LucentPM4FMT1E1ThreshESs_Type()
)
lucentPM4FMT1E1ThreshESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshESs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshSESs_Type = Gauge32
_LucentPM4FMT1E1ThreshSESs_Object = MibTableColumn
lucentPM4FMT1E1ThreshSESs = _LucentPM4FMT1E1ThreshSESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 4),
    _LucentPM4FMT1E1ThreshSESs_Type()
)
lucentPM4FMT1E1ThreshSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshSESs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshSEFSs_Type = Gauge32
_LucentPM4FMT1E1ThreshSEFSs_Object = MibTableColumn
lucentPM4FMT1E1ThreshSEFSs = _LucentPM4FMT1E1ThreshSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 5),
    _LucentPM4FMT1E1ThreshSEFSs_Type()
)
lucentPM4FMT1E1ThreshSEFSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshSEFSs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshUASs_Type = Gauge32
_LucentPM4FMT1E1ThreshUASs_Object = MibTableColumn
lucentPM4FMT1E1ThreshUASs = _LucentPM4FMT1E1ThreshUASs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 6),
    _LucentPM4FMT1E1ThreshUASs_Type()
)
lucentPM4FMT1E1ThreshUASs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshUASs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshCSSs_Type = Gauge32
_LucentPM4FMT1E1ThreshCSSs_Object = MibTableColumn
lucentPM4FMT1E1ThreshCSSs = _LucentPM4FMT1E1ThreshCSSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 7),
    _LucentPM4FMT1E1ThreshCSSs_Type()
)
lucentPM4FMT1E1ThreshCSSs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshCSSs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshPCVs_Type = Gauge32
_LucentPM4FMT1E1ThreshPCVs_Object = MibTableColumn
lucentPM4FMT1E1ThreshPCVs = _LucentPM4FMT1E1ThreshPCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 8),
    _LucentPM4FMT1E1ThreshPCVs_Type()
)
lucentPM4FMT1E1ThreshPCVs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshPCVs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshLESs_Type = Gauge32
_LucentPM4FMT1E1ThreshLESs_Object = MibTableColumn
lucentPM4FMT1E1ThreshLESs = _LucentPM4FMT1E1ThreshLESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 9),
    _LucentPM4FMT1E1ThreshLESs_Type()
)
lucentPM4FMT1E1ThreshLESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshLESs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshBESs_Type = Gauge32
_LucentPM4FMT1E1ThreshBESs_Object = MibTableColumn
lucentPM4FMT1E1ThreshBESs = _LucentPM4FMT1E1ThreshBESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 10),
    _LucentPM4FMT1E1ThreshBESs_Type()
)
lucentPM4FMT1E1ThreshBESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshBESs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshDMs_Type = Gauge32
_LucentPM4FMT1E1ThreshDMs_Object = MibTableColumn
lucentPM4FMT1E1ThreshDMs = _LucentPM4FMT1E1ThreshDMs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 11),
    _LucentPM4FMT1E1ThreshDMs_Type()
)
lucentPM4FMT1E1ThreshDMs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshDMs.setStatus("mandatory")
_LucentPM4FMT1E1ThreshRepTimer_Type = Integer32
_LucentPM4FMT1E1ThreshRepTimer_Object = MibScalar
lucentPM4FMT1E1ThreshRepTimer = _LucentPM4FMT1E1ThreshRepTimer_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 12),
    _LucentPM4FMT1E1ThreshRepTimer_Type()
)
lucentPM4FMT1E1ThreshRepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshRepTimer.setStatus("mandatory")


class _LucentPM4FMT1E1ThreshTrapAck_Type(Integer32):
    """Custom type lucentPM4FMT1E1ThreshTrapAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ack", 3),
          ("noack", 2),
          ("other", 1))
    )


_LucentPM4FMT1E1ThreshTrapAck_Type.__name__ = "Integer32"
_LucentPM4FMT1E1ThreshTrapAck_Object = MibTableColumn
lucentPM4FMT1E1ThreshTrapAck = _LucentPM4FMT1E1ThreshTrapAck_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 2, 1, 13),
    _LucentPM4FMT1E1ThreshTrapAck_Type()
)
lucentPM4FMT1E1ThreshTrapAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMT1E1ThreshTrapAck.setStatus("mandatory")
_LucentPM4FMEnvTrapCfg_Object = MibTable
lucentPM4FMEnvTrapCfg = _LucentPM4FMEnvTrapCfg_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3)
)
if mibBuilder.loadTexts:
    lucentPM4FMEnvTrapCfg.setStatus("mandatory")
_LucentPM4FMEnvTrapCfgEntry_Object = MibTableRow
lucentPM4FMEnvTrapCfgEntry = _LucentPM4FMEnvTrapCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1)
)
lucentPM4FMEnvTrapCfgEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEnvBoardID"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEnvUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4FMEnvUnitIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4FMEnvTrapCfgEntry.setStatus("mandatory")
_LucentPM4FMEnvBoardID_Type = Integer32
_LucentPM4FMEnvBoardID_Object = MibTableColumn
lucentPM4FMEnvBoardID = _LucentPM4FMEnvBoardID_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 1),
    _LucentPM4FMEnvBoardID_Type()
)
lucentPM4FMEnvBoardID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEnvBoardID.setStatus("mandatory")
_LucentPM4FMEnvUnitType_Type = PMUnitType
_LucentPM4FMEnvUnitType_Object = MibTableColumn
lucentPM4FMEnvUnitType = _LucentPM4FMEnvUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 2),
    _LucentPM4FMEnvUnitType_Type()
)
lucentPM4FMEnvUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEnvUnitType.setStatus("mandatory")
_LucentPM4FMEnvUnitIndex_Type = Integer32
_LucentPM4FMEnvUnitIndex_Object = MibTableColumn
lucentPM4FMEnvUnitIndex = _LucentPM4FMEnvUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 3),
    _LucentPM4FMEnvUnitIndex_Type()
)
lucentPM4FMEnvUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4FMEnvUnitIndex.setStatus("mandatory")
_LucentPM4FMEnvOptUnitTemp_Type = Integer32
_LucentPM4FMEnvOptUnitTemp_Object = MibTableColumn
lucentPM4FMEnvOptUnitTemp = _LucentPM4FMEnvOptUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 4),
    _LucentPM4FMEnvOptUnitTemp_Type()
)
lucentPM4FMEnvOptUnitTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEnvOptUnitTemp.setStatus("mandatory")
_LucentPM4FMEnvUnitTempRange_Type = Integer32
_LucentPM4FMEnvUnitTempRange_Object = MibTableColumn
lucentPM4FMEnvUnitTempRange = _LucentPM4FMEnvUnitTempRange_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 5),
    _LucentPM4FMEnvUnitTempRange_Type()
)
lucentPM4FMEnvUnitTempRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEnvUnitTempRange.setStatus("mandatory")
_LucentPM4FMEnvOptUnitPwrLvl_Type = Integer32
_LucentPM4FMEnvOptUnitPwrLvl_Object = MibTableColumn
lucentPM4FMEnvOptUnitPwrLvl = _LucentPM4FMEnvOptUnitPwrLvl_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 6),
    _LucentPM4FMEnvOptUnitPwrLvl_Type()
)
lucentPM4FMEnvOptUnitPwrLvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEnvOptUnitPwrLvl.setStatus("mandatory")
_LucentPM4FMEnvUnitPwrRange_Type = Integer32
_LucentPM4FMEnvUnitPwrRange_Object = MibTableColumn
lucentPM4FMEnvUnitPwrRange = _LucentPM4FMEnvUnitPwrRange_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 7),
    _LucentPM4FMEnvUnitPwrRange_Type()
)
lucentPM4FMEnvUnitPwrRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEnvUnitPwrRange.setStatus("mandatory")


class _LucentPM4FMEnvTrapCtl_Type(Integer32):
    """Custom type lucentPM4FMEnvTrapCtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_LucentPM4FMEnvTrapCtl_Type.__name__ = "Integer32"
_LucentPM4FMEnvTrapCtl_Object = MibTableColumn
lucentPM4FMEnvTrapCtl = _LucentPM4FMEnvTrapCtl_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 5, 2, 3, 1, 8),
    _LucentPM4FMEnvTrapCtl_Type()
)
lucentPM4FMEnvTrapCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4FMEnvTrapCtl.setStatus("mandatory")
_LucentPM4PerfMgmt_ObjectIdentity = ObjectIdentity
lucentPM4PerfMgmt = _LucentPM4PerfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6)
)
_LucentPM4T1E1PerfMgmt_ObjectIdentity = ObjectIdentity
lucentPM4T1E1PerfMgmt = _LucentPM4T1E1PerfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1)
)
_LucentPM4T1E1PMCur_Object = MibTable
lucentPM4T1E1PMCur = _LucentPM4T1E1PMCur_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCur.setStatus("mandatory")
_LucentPM4T1E1PMCurEntry_Object = MibTableRow
lucentPM4T1E1PMCurEntry = _LucentPM4T1E1PMCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1)
)
lucentPM4T1E1PMCurEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMBoardID"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMLineNum"),
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurEntry.setStatus("mandatory")
_LucentPM4T1E1PMCurBoard_Type = Integer32
_LucentPM4T1E1PMCurBoard_Object = MibScalar
lucentPM4T1E1PMCurBoard = _LucentPM4T1E1PMCurBoard_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 1),
    _LucentPM4T1E1PMCurBoard_Type()
)
lucentPM4T1E1PMCurBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurBoard.setStatus("mandatory")
_LucentPM4T1E1PMCurUnitType_Type = PMUnitType
_LucentPM4T1E1PMCurUnitType_Object = MibTableColumn
lucentPM4T1E1PMCurUnitType = _LucentPM4T1E1PMCurUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 2),
    _LucentPM4T1E1PMCurUnitType_Type()
)
lucentPM4T1E1PMCurUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurUnitType.setStatus("mandatory")
_LucentPM4T1E1PMCurLineNum_Type = Integer32
_LucentPM4T1E1PMCurLineNum_Object = MibTableColumn
lucentPM4T1E1PMCurLineNum = _LucentPM4T1E1PMCurLineNum_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 3),
    _LucentPM4T1E1PMCurLineNum_Type()
)
lucentPM4T1E1PMCurLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurLineNum.setStatus("mandatory")
_LucentPM4T1E1PMCurIfIndex_Type = Integer32
_LucentPM4T1E1PMCurIfIndex_Object = MibTableColumn
lucentPM4T1E1PMCurIfIndex = _LucentPM4T1E1PMCurIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 4),
    _LucentPM4T1E1PMCurIfIndex_Type()
)
lucentPM4T1E1PMCurIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurIfIndex.setStatus("mandatory")
_LucentPM4T1E1PMCurESs_Type = Gauge32
_LucentPM4T1E1PMCurESs_Object = MibTableColumn
lucentPM4T1E1PMCurESs = _LucentPM4T1E1PMCurESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 5),
    _LucentPM4T1E1PMCurESs_Type()
)
lucentPM4T1E1PMCurESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurESs.setStatus("mandatory")
_LucentPM4T1E1PMCurSESs_Type = Gauge32
_LucentPM4T1E1PMCurSESs_Object = MibTableColumn
lucentPM4T1E1PMCurSESs = _LucentPM4T1E1PMCurSESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 6),
    _LucentPM4T1E1PMCurSESs_Type()
)
lucentPM4T1E1PMCurSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurSESs.setStatus("mandatory")
_LucentPM4T1E1PMCurSEFSs_Type = Gauge32
_LucentPM4T1E1PMCurSEFSs_Object = MibScalar
lucentPM4T1E1PMCurSEFSs = _LucentPM4T1E1PMCurSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 7),
    _LucentPM4T1E1PMCurSEFSs_Type()
)
lucentPM4T1E1PMCurSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurSEFSs.setStatus("mandatory")
_LucentPM4T1E1PMCurUASs_Type = Gauge32
_LucentPM4T1E1PMCurUASs_Object = MibTableColumn
lucentPM4T1E1PMCurUASs = _LucentPM4T1E1PMCurUASs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 8),
    _LucentPM4T1E1PMCurUASs_Type()
)
lucentPM4T1E1PMCurUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurUASs.setStatus("mandatory")
_LucentPM4T1E1PMCurCSSs_Type = Gauge32
_LucentPM4T1E1PMCurCSSs_Object = MibTableColumn
lucentPM4T1E1PMCurCSSs = _LucentPM4T1E1PMCurCSSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 9),
    _LucentPM4T1E1PMCurCSSs_Type()
)
lucentPM4T1E1PMCurCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurCSSs.setStatus("mandatory")
_LucentPM4T1E1PMCurPCVs_Type = Gauge32
_LucentPM4T1E1PMCurPCVs_Object = MibTableColumn
lucentPM4T1E1PMCurPCVs = _LucentPM4T1E1PMCurPCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 10),
    _LucentPM4T1E1PMCurPCVs_Type()
)
lucentPM4T1E1PMCurPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurPCVs.setStatus("mandatory")
_LucentPM4T1E1PMCurLESs_Type = Gauge32
_LucentPM4T1E1PMCurLESs_Object = MibTableColumn
lucentPM4T1E1PMCurLESs = _LucentPM4T1E1PMCurLESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 11),
    _LucentPM4T1E1PMCurLESs_Type()
)
lucentPM4T1E1PMCurLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurLESs.setStatus("mandatory")
_LucentPM4T1E1PMCurBESs_Type = Gauge32
_LucentPM4T1E1PMCurBESs_Object = MibTableColumn
lucentPM4T1E1PMCurBESs = _LucentPM4T1E1PMCurBESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 12),
    _LucentPM4T1E1PMCurBESs_Type()
)
lucentPM4T1E1PMCurBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurBESs.setStatus("mandatory")
_LucentPM4T1E1PMCurDMs_Type = Gauge32
_LucentPM4T1E1PMCurDMs_Object = MibTableColumn
lucentPM4T1E1PMCurDMs = _LucentPM4T1E1PMCurDMs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 13),
    _LucentPM4T1E1PMCurDMs_Type()
)
lucentPM4T1E1PMCurDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurDMs.setStatus("mandatory")
_LucentPM4T1E1PMCurLCVs_Type = Gauge32
_LucentPM4T1E1PMCurLCVs_Object = MibTableColumn
lucentPM4T1E1PMCurLCVs = _LucentPM4T1E1PMCurLCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 1, 1, 1, 14),
    _LucentPM4T1E1PMCurLCVs_Type()
)
lucentPM4T1E1PMCurLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMCurLCVs.setStatus("mandatory")
_LucentPM4T1E1PMInt_Object = MibTable
lucentPM4T1E1PMInt = _LucentPM4T1E1PMInt_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMInt.setStatus("mandatory")
_LucentPM4T1E1PMIntEntry_Object = MibTableRow
lucentPM4T1E1PMIntEntry = _LucentPM4T1E1PMIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1)
)
lucentPM4T1E1PMIntEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMIntBoard"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMIntUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMIntLineNum"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMIntInterval"),
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntEntry.setStatus("mandatory")
_LucentPM4T1E1PMIntBoard_Type = Integer32
_LucentPM4T1E1PMIntBoard_Object = MibTableColumn
lucentPM4T1E1PMIntBoard = _LucentPM4T1E1PMIntBoard_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 1),
    _LucentPM4T1E1PMIntBoard_Type()
)
lucentPM4T1E1PMIntBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntBoard.setStatus("mandatory")
_LucentPM4T1E1PMIntUnitType_Type = PMUnitType
_LucentPM4T1E1PMIntUnitType_Object = MibTableColumn
lucentPM4T1E1PMIntUnitType = _LucentPM4T1E1PMIntUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 2),
    _LucentPM4T1E1PMIntUnitType_Type()
)
lucentPM4T1E1PMIntUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntUnitType.setStatus("mandatory")
_LucentPM4T1E1PMIntLineNum_Type = Integer32
_LucentPM4T1E1PMIntLineNum_Object = MibTableColumn
lucentPM4T1E1PMIntLineNum = _LucentPM4T1E1PMIntLineNum_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 3),
    _LucentPM4T1E1PMIntLineNum_Type()
)
lucentPM4T1E1PMIntLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntLineNum.setStatus("mandatory")


class _LucentPM4T1E1PMIntInterval_Type(Integer32):
    """Custom type lucentPM4T1E1PMIntInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_LucentPM4T1E1PMIntInterval_Type.__name__ = "Integer32"
_LucentPM4T1E1PMIntInterval_Object = MibTableColumn
lucentPM4T1E1PMIntInterval = _LucentPM4T1E1PMIntInterval_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 4),
    _LucentPM4T1E1PMIntInterval_Type()
)
lucentPM4T1E1PMIntInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntInterval.setStatus("mandatory")
_LucentPM4T1E1PMIntIfIndex_Type = Integer32
_LucentPM4T1E1PMIntIfIndex_Object = MibTableColumn
lucentPM4T1E1PMIntIfIndex = _LucentPM4T1E1PMIntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 5),
    _LucentPM4T1E1PMIntIfIndex_Type()
)
lucentPM4T1E1PMIntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntIfIndex.setStatus("mandatory")
_LucentPM4T1E1PMIntESs_Type = Gauge32
_LucentPM4T1E1PMIntESs_Object = MibTableColumn
lucentPM4T1E1PMIntESs = _LucentPM4T1E1PMIntESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 6),
    _LucentPM4T1E1PMIntESs_Type()
)
lucentPM4T1E1PMIntESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntESs.setStatus("mandatory")
_LucentPM4T1E1PMIntSESs_Type = Gauge32
_LucentPM4T1E1PMIntSESs_Object = MibTableColumn
lucentPM4T1E1PMIntSESs = _LucentPM4T1E1PMIntSESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 7),
    _LucentPM4T1E1PMIntSESs_Type()
)
lucentPM4T1E1PMIntSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntSESs.setStatus("mandatory")
_LucentPM4T1E1PMIntSEFSs_Type = Gauge32
_LucentPM4T1E1PMIntSEFSs_Object = MibScalar
lucentPM4T1E1PMIntSEFSs = _LucentPM4T1E1PMIntSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 8),
    _LucentPM4T1E1PMIntSEFSs_Type()
)
lucentPM4T1E1PMIntSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntSEFSs.setStatus("mandatory")
_LucentPM4T1E1PMIntUASs_Type = Gauge32
_LucentPM4T1E1PMIntUASs_Object = MibTableColumn
lucentPM4T1E1PMIntUASs = _LucentPM4T1E1PMIntUASs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 9),
    _LucentPM4T1E1PMIntUASs_Type()
)
lucentPM4T1E1PMIntUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntUASs.setStatus("mandatory")
_LucentPM4T1E1PMIntCSSs_Type = Gauge32
_LucentPM4T1E1PMIntCSSs_Object = MibTableColumn
lucentPM4T1E1PMIntCSSs = _LucentPM4T1E1PMIntCSSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 10),
    _LucentPM4T1E1PMIntCSSs_Type()
)
lucentPM4T1E1PMIntCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntCSSs.setStatus("mandatory")
_LucentPM4T1E1PMIntPCVs_Type = Gauge32
_LucentPM4T1E1PMIntPCVs_Object = MibTableColumn
lucentPM4T1E1PMIntPCVs = _LucentPM4T1E1PMIntPCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 11),
    _LucentPM4T1E1PMIntPCVs_Type()
)
lucentPM4T1E1PMIntPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntPCVs.setStatus("mandatory")
_LucentPM4T1E1PMIntLESs_Type = Gauge32
_LucentPM4T1E1PMIntLESs_Object = MibTableColumn
lucentPM4T1E1PMIntLESs = _LucentPM4T1E1PMIntLESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 12),
    _LucentPM4T1E1PMIntLESs_Type()
)
lucentPM4T1E1PMIntLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntLESs.setStatus("mandatory")
_LucentPM4T1E1PMIntBESs_Type = Gauge32
_LucentPM4T1E1PMIntBESs_Object = MibTableColumn
lucentPM4T1E1PMIntBESs = _LucentPM4T1E1PMIntBESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 13),
    _LucentPM4T1E1PMIntBESs_Type()
)
lucentPM4T1E1PMIntBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntBESs.setStatus("mandatory")
_LucentPM4T1E1PMIntDMs_Type = Gauge32
_LucentPM4T1E1PMIntDMs_Object = MibTableColumn
lucentPM4T1E1PMIntDMs = _LucentPM4T1E1PMIntDMs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 14),
    _LucentPM4T1E1PMIntDMs_Type()
)
lucentPM4T1E1PMIntDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntDMs.setStatus("mandatory")
_LucentPM4T1E1PMIntLCVs_Type = Gauge32
_LucentPM4T1E1PMIntLCVs_Object = MibTableColumn
lucentPM4T1E1PMIntLCVs = _LucentPM4T1E1PMIntLCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 2, 1, 15),
    _LucentPM4T1E1PMIntLCVs_Type()
)
lucentPM4T1E1PMIntLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMIntLCVs.setStatus("mandatory")
_LucentPM4T1E1PMTotal_Object = MibTable
lucentPM4T1E1PMTotal = _LucentPM4T1E1PMTotal_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotal.setStatus("mandatory")
_LucentPM4T1E1PMTotalEntry_Object = MibTableRow
lucentPM4T1E1PMTotalEntry = _LucentPM4T1E1PMTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1)
)
lucentPM4T1E1PMTotalEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMTotalBoard"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMTotalUnitType"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMTotalLineNum"),
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4T1E1PMTotalInterval"),
)
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalEntry.setStatus("mandatory")
_LucentPM4T1E1PMTotalBoard_Type = Integer32
_LucentPM4T1E1PMTotalBoard_Object = MibTableColumn
lucentPM4T1E1PMTotalBoard = _LucentPM4T1E1PMTotalBoard_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 1),
    _LucentPM4T1E1PMTotalBoard_Type()
)
lucentPM4T1E1PMTotalBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalBoard.setStatus("mandatory")
_LucentPM4T1E1PMTotalUnitType_Type = PMUnitType
_LucentPM4T1E1PMTotalUnitType_Object = MibTableColumn
lucentPM4T1E1PMTotalUnitType = _LucentPM4T1E1PMTotalUnitType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 2),
    _LucentPM4T1E1PMTotalUnitType_Type()
)
lucentPM4T1E1PMTotalUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalUnitType.setStatus("mandatory")
_LucentPM4T1E1PMTotalLineNum_Type = Integer32
_LucentPM4T1E1PMTotalLineNum_Object = MibTableColumn
lucentPM4T1E1PMTotalLineNum = _LucentPM4T1E1PMTotalLineNum_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 3),
    _LucentPM4T1E1PMTotalLineNum_Type()
)
lucentPM4T1E1PMTotalLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalLineNum.setStatus("mandatory")
_LucentPM4T1E1PMTotalIfIndex_Type = Integer32
_LucentPM4T1E1PMTotalIfIndex_Object = MibTableColumn
lucentPM4T1E1PMTotalIfIndex = _LucentPM4T1E1PMTotalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 4),
    _LucentPM4T1E1PMTotalIfIndex_Type()
)
lucentPM4T1E1PMTotalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalIfIndex.setStatus("mandatory")
_LucentPM4T1E1PMTotalESs_Type = Gauge32
_LucentPM4T1E1PMTotalESs_Object = MibTableColumn
lucentPM4T1E1PMTotalESs = _LucentPM4T1E1PMTotalESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 5),
    _LucentPM4T1E1PMTotalESs_Type()
)
lucentPM4T1E1PMTotalESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalESs.setStatus("mandatory")
_LucentPM4T1E1PMTotalSESs_Type = Gauge32
_LucentPM4T1E1PMTotalSESs_Object = MibTableColumn
lucentPM4T1E1PMTotalSESs = _LucentPM4T1E1PMTotalSESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 6),
    _LucentPM4T1E1PMTotalSESs_Type()
)
lucentPM4T1E1PMTotalSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalSESs.setStatus("mandatory")
_LucentPM4T1E1PMTotalSEFSs_Type = Gauge32
_LucentPM4T1E1PMTotalSEFSs_Object = MibScalar
lucentPM4T1E1PMTotalSEFSs = _LucentPM4T1E1PMTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 7),
    _LucentPM4T1E1PMTotalSEFSs_Type()
)
lucentPM4T1E1PMTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalSEFSs.setStatus("mandatory")
_LucentPM4T1E1PMTotalUASs_Type = Gauge32
_LucentPM4T1E1PMTotalUASs_Object = MibTableColumn
lucentPM4T1E1PMTotalUASs = _LucentPM4T1E1PMTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 8),
    _LucentPM4T1E1PMTotalUASs_Type()
)
lucentPM4T1E1PMTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalUASs.setStatus("mandatory")
_LucentPM4T1E1PMTotalCSSs_Type = Gauge32
_LucentPM4T1E1PMTotalCSSs_Object = MibTableColumn
lucentPM4T1E1PMTotalCSSs = _LucentPM4T1E1PMTotalCSSs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 9),
    _LucentPM4T1E1PMTotalCSSs_Type()
)
lucentPM4T1E1PMTotalCSSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalCSSs.setStatus("mandatory")
_LucentPM4T1E1PMTotalPCVs_Type = Gauge32
_LucentPM4T1E1PMTotalPCVs_Object = MibTableColumn
lucentPM4T1E1PMTotalPCVs = _LucentPM4T1E1PMTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 10),
    _LucentPM4T1E1PMTotalPCVs_Type()
)
lucentPM4T1E1PMTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalPCVs.setStatus("mandatory")
_LucentPM4T1E1PMTotalLESs_Type = Gauge32
_LucentPM4T1E1PMTotalLESs_Object = MibTableColumn
lucentPM4T1E1PMTotalLESs = _LucentPM4T1E1PMTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 11),
    _LucentPM4T1E1PMTotalLESs_Type()
)
lucentPM4T1E1PMTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalLESs.setStatus("mandatory")
_LucentPM4T1E1PMTotalBESs_Type = Gauge32
_LucentPM4T1E1PMTotalBESs_Object = MibTableColumn
lucentPM4T1E1PMTotalBESs = _LucentPM4T1E1PMTotalBESs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 12),
    _LucentPM4T1E1PMTotalBESs_Type()
)
lucentPM4T1E1PMTotalBESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalBESs.setStatus("mandatory")
_LucentPM4T1E1PMTotalDMs_Type = Gauge32
_LucentPM4T1E1PMTotalDMs_Object = MibTableColumn
lucentPM4T1E1PMTotalDMs = _LucentPM4T1E1PMTotalDMs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 13),
    _LucentPM4T1E1PMTotalDMs_Type()
)
lucentPM4T1E1PMTotalDMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalDMs.setStatus("mandatory")
_LucentPM4T1E1PMTotalLCVs_Type = Gauge32
_LucentPM4T1E1PMTotalLCVs_Object = MibTableColumn
lucentPM4T1E1PMTotalLCVs = _LucentPM4T1E1PMTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 6, 3, 1, 14),
    _LucentPM4T1E1PMTotalLCVs_Type()
)
lucentPM4T1E1PMTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4T1E1PMTotalLCVs.setStatus("mandatory")
_LucentPM4SecurityMgmt_ObjectIdentity = ObjectIdentity
lucentPM4SecurityMgmt = _LucentPM4SecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 7)
)
_LucentPM4AcctMgmt_ObjectIdentity = ObjectIdentity
lucentPM4AcctMgmt = _LucentPM4AcctMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8)
)
_LucentPM4AcctMgmtComm_ObjectIdentity = ObjectIdentity
lucentPM4AcctMgmtComm = _LucentPM4AcctMgmtComm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1)
)
_LucentPM4SnmpCommTable_Object = MibTable
lucentPM4SnmpCommTable = _LucentPM4SnmpCommTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    lucentPM4SnmpCommTable.setStatus("mandatory")
_LucentPM4SnmpCommEntry_Object = MibTableRow
lucentPM4SnmpCommEntry = _LucentPM4SnmpCommEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1)
)
lucentPM4SnmpCommEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4SnmpCommName"),
)
if mibBuilder.loadTexts:
    lucentPM4SnmpCommEntry.setStatus("mandatory")


class _LucentPM4SnmpCommIndex_Type(Integer32):
    """Custom type lucentPM4SnmpCommIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LucentPM4SnmpCommIndex_Type.__name__ = "Integer32"
_LucentPM4SnmpCommIndex_Object = MibTableColumn
lucentPM4SnmpCommIndex = _LucentPM4SnmpCommIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 1),
    _LucentPM4SnmpCommIndex_Type()
)
lucentPM4SnmpCommIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommIndex.setStatus("mandatory")


class _LucentPM4SnmpCommName_Type(DisplayString):
    """Custom type lucentPM4SnmpCommName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_LucentPM4SnmpCommName_Type.__name__ = "DisplayString"
_LucentPM4SnmpCommName_Object = MibTableColumn
lucentPM4SnmpCommName = _LucentPM4SnmpCommName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 2),
    _LucentPM4SnmpCommName_Type()
)
lucentPM4SnmpCommName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommName.setStatus("mandatory")
_LucentPM4SnmpCommIpAddr_Type = IpAddress
_LucentPM4SnmpCommIpAddr_Object = MibTableColumn
lucentPM4SnmpCommIpAddr = _LucentPM4SnmpCommIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 3),
    _LucentPM4SnmpCommIpAddr_Type()
)
lucentPM4SnmpCommIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommIpAddr.setStatus("mandatory")


class _LucentPM4SnmpCommReadAccess_Type(Integer32):
    """Custom type lucentPM4SnmpCommReadAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ensable", 2))
    )


_LucentPM4SnmpCommReadAccess_Type.__name__ = "Integer32"
_LucentPM4SnmpCommReadAccess_Object = MibTableColumn
lucentPM4SnmpCommReadAccess = _LucentPM4SnmpCommReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 4),
    _LucentPM4SnmpCommReadAccess_Type()
)
lucentPM4SnmpCommReadAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommReadAccess.setStatus("mandatory")


class _LucentPM4SnmpCommWriteAccess_Type(Integer32):
    """Custom type lucentPM4SnmpCommWriteAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ensable", 2))
    )


_LucentPM4SnmpCommWriteAccess_Type.__name__ = "Integer32"
_LucentPM4SnmpCommWriteAccess_Object = MibTableColumn
lucentPM4SnmpCommWriteAccess = _LucentPM4SnmpCommWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 5),
    _LucentPM4SnmpCommWriteAccess_Type()
)
lucentPM4SnmpCommWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommWriteAccess.setStatus("mandatory")


class _LucentPM4SnmpCommTraps_Type(Integer32):
    """Custom type lucentPM4SnmpCommTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ensable", 2))
    )


_LucentPM4SnmpCommTraps_Type.__name__ = "Integer32"
_LucentPM4SnmpCommTraps_Object = MibTableColumn
lucentPM4SnmpCommTraps = _LucentPM4SnmpCommTraps_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 6),
    _LucentPM4SnmpCommTraps_Type()
)
lucentPM4SnmpCommTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommTraps.setStatus("mandatory")


class _LucentPM4SnmpCommStatus_Type(Integer32):
    """Custom type lucentPM4SnmpCommStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("normal", 1))
    )


_LucentPM4SnmpCommStatus_Type.__name__ = "Integer32"
_LucentPM4SnmpCommStatus_Object = MibTableColumn
lucentPM4SnmpCommStatus = _LucentPM4SnmpCommStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 7),
    _LucentPM4SnmpCommStatus_Type()
)
lucentPM4SnmpCommStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommStatus.setStatus("mandatory")


class _LucentPM4SnmpCommLastError_Type(DisplayString):
    """Custom type lucentPM4SnmpCommLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 511),
    )


_LucentPM4SnmpCommLastError_Type.__name__ = "DisplayString"
_LucentPM4SnmpCommLastError_Object = MibTableColumn
lucentPM4SnmpCommLastError = _LucentPM4SnmpCommLastError_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 1, 1, 1, 8),
    _LucentPM4SnmpCommLastError_Type()
)
lucentPM4SnmpCommLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4SnmpCommLastError.setStatus("mandatory")
_LucentPM4AcctMgmtCallEvent_ObjectIdentity = ObjectIdentity
lucentPM4AcctMgmtCallEvent = _LucentPM4AcctMgmtCallEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2)
)
_LucentPM4AMCallEventTable_Object = MibTable
lucentPM4AMCallEventTable = _LucentPM4AMCallEventTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    lucentPM4AMCallEventTable.setStatus("mandatory")
_LucentPM4AMCallEventEntry_Object = MibTableRow
lucentPM4AMCallEventEntry = _LucentPM4AMCallEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1)
)
lucentPM4AMCallEventEntry.setIndexNames(
    (0, "LIVINGSTON-PM4-MIB", "lucentPM4AMCEIndex"),
)
if mibBuilder.loadTexts:
    lucentPM4AMCallEventEntry.setStatus("mandatory")
_LucentPM4AMCEIndex_Type = Integer32
_LucentPM4AMCEIndex_Object = MibTableColumn
lucentPM4AMCEIndex = _LucentPM4AMCEIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 1),
    _LucentPM4AMCEIndex_Type()
)
lucentPM4AMCEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEIndex.setStatus("mandatory")
_LucentPM4AMCETimeStamp_Type = Integer32
_LucentPM4AMCETimeStamp_Object = MibTableColumn
lucentPM4AMCETimeStamp = _LucentPM4AMCETimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 2),
    _LucentPM4AMCETimeStamp_Type()
)
lucentPM4AMCETimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCETimeStamp.setStatus("mandatory")


class _LucentPM4AMCEType_Type(Integer32):
    """Custom type lucentPM4AMCEType based on Integer32"""
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
        *(("baudratechanged", 6),
          ("callanswered", 2),
          ("callcleared", 3),
          ("calloriginated", 1),
          ("namechanged", 5),
          ("servicechanged", 4))
    )


_LucentPM4AMCEType_Type.__name__ = "Integer32"
_LucentPM4AMCEType_Object = MibTableColumn
lucentPM4AMCEType = _LucentPM4AMCEType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 3),
    _LucentPM4AMCEType_Type()
)
lucentPM4AMCEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEType.setStatus("mandatory")


class _LucentPM4AMCESvcType_Type(Integer32):
    """Custom type lucentPM4AMCESvcType based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("combinet", 6),
          ("euraw", 8),
          ("euui", 9),
          ("frameRelay", 7),
          ("mp", 14),
          ("mpp", 4),
          ("none", 1),
          ("ppp", 2),
          ("rawTcp", 12),
          ("slip", 3),
          ("telnet", 10),
          ("telnetBinary", 11),
          ("terminalServer", 13),
          ("virtualConnect", 15),
          ("x25", 5),
          ("x25DChannel", 16))
    )


_LucentPM4AMCESvcType_Type.__name__ = "Integer32"
_LucentPM4AMCESvcType_Object = MibTableColumn
lucentPM4AMCESvcType = _LucentPM4AMCESvcType_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 4),
    _LucentPM4AMCESvcType_Type()
)
lucentPM4AMCESvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCESvcType.setStatus("mandatory")
_LucentPM4AMCEUName_Type = DisplayString
_LucentPM4AMCEUName_Object = MibTableColumn
lucentPM4AMCEUName = _LucentPM4AMCEUName_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 5),
    _LucentPM4AMCEUName_Type()
)
lucentPM4AMCEUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEUName.setStatus("mandatory")
_LucentPM4AMCEModemBoard_Type = Integer32
_LucentPM4AMCEModemBoard_Object = MibTableColumn
lucentPM4AMCEModemBoard = _LucentPM4AMCEModemBoard_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 6),
    _LucentPM4AMCEModemBoard_Type()
)
lucentPM4AMCEModemBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEModemBoard.setStatus("mandatory")
_LucentPM4AMCEModemID_Type = Integer32
_LucentPM4AMCEModemID_Object = MibTableColumn
lucentPM4AMCEModemID = _LucentPM4AMCEModemID_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 7),
    _LucentPM4AMCEModemID_Type()
)
lucentPM4AMCEModemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEModemID.setStatus("mandatory")
_LucentPM4AMCEModemPort_Type = DisplayString
_LucentPM4AMCEModemPort_Object = MibTableColumn
lucentPM4AMCEModemPort = _LucentPM4AMCEModemPort_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 8),
    _LucentPM4AMCEModemPort_Type()
)
lucentPM4AMCEModemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEModemPort.setStatus("mandatory")
_LucentPM4AMCEDataRate_Type = Integer32
_LucentPM4AMCEDataRate_Object = MibTableColumn
lucentPM4AMCEDataRate = _LucentPM4AMCEDataRate_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 9),
    _LucentPM4AMCEDataRate_Type()
)
lucentPM4AMCEDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEDataRate.setStatus("mandatory")
_LucentPM4AMCECallingPartyID_Type = DisplayString
_LucentPM4AMCECallingPartyID_Object = MibTableColumn
lucentPM4AMCECallingPartyID = _LucentPM4AMCECallingPartyID_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 10),
    _LucentPM4AMCECallingPartyID_Type()
)
lucentPM4AMCECallingPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCECallingPartyID.setStatus("mandatory")
_LucentPM4AMCECalledPartyID_Type = DisplayString
_LucentPM4AMCECalledPartyID_Object = MibTableColumn
lucentPM4AMCECalledPartyID = _LucentPM4AMCECalledPartyID_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 11),
    _LucentPM4AMCECalledPartyID_Type()
)
lucentPM4AMCECalledPartyID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCECalledPartyID.setStatus("mandatory")
_LucentPM4AMCEInOctets_Type = Integer32
_LucentPM4AMCEInOctets_Object = MibTableColumn
lucentPM4AMCEInOctets = _LucentPM4AMCEInOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 12),
    _LucentPM4AMCEInOctets_Type()
)
lucentPM4AMCEInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEInOctets.setStatus("mandatory")
_LucentPM4AMCEOutOctets_Type = Integer32
_LucentPM4AMCEOutOctets_Object = MibTableColumn
lucentPM4AMCEOutOctets = _LucentPM4AMCEOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 13),
    _LucentPM4AMCEOutOctets_Type()
)
lucentPM4AMCEOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEOutOctets.setStatus("mandatory")
_LucentPM4AMCECallCharge_Type = Integer32
_LucentPM4AMCECallCharge_Object = MibTableColumn
lucentPM4AMCECallCharge = _LucentPM4AMCECallCharge_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 14),
    _LucentPM4AMCECallCharge_Type()
)
lucentPM4AMCECallCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCECallCharge.setStatus("mandatory")


class _LucentPM4AMCEDisconnReason_Type(Integer32):
    """Custom type lucentPM4AMCEDisconnReason based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              35,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              100,
              101,
              102,
              120,
              150,
              151,
              152,
              160,
              170,
              180,
              185,
              190,
              195,
              201,
              210)
        )
    )
    namedValues = NamedValues(
        *(("boardDied", 210),
          ("clidAuthFailed", 4),
          ("clidAuthRequestCallback", 6),
          ("clidAuthServTimeout", 5),
          ("disconnected", 3),
          ("invalidProtocol", 120),
          ("localAdmin", 151),
          ("localSnmp", 152),
          ("lowMemory", 201),
          ("maxCallDurationReached", 195),
          ("mpNullMessageTimeout", 35),
          ("noModemAvailable", 9),
          ("noModemLossCarrier", 11),
          ("noModemNoCarrier", 10),
          ("noModemOpenFailed", 13),
          ("noModemOpenFailedDiag", 14),
          ("noModemResultCodes", 12),
          ("notApplicable", 1),
          ("pppAuthTimeout", 170),
          ("pppCHAPAuthFail", 43),
          ("pppCloseEvent", 46),
          ("pppCloseMpAddChanFail", 49),
          ("pppCloseNoNcpsOpened", 47),
          ("pppCloseUnknownMpBundle", 48),
          ("pppLcpNegotiateFail", 41),
          ("pppLcpTimeout", 40),
          ("pppPAPAuthFail", 42),
          ("pppRcvTerminate", 45),
          ("pppRemoteAuthFail", 44),
          ("preT310Timeout", 7),
          ("remoteEndHungUp", 185),
          ("requestByRadiusClient", 150),
          ("resourceQuiesced", 190),
          ("sessCallback", 102),
          ("sessFailSecurity", 101),
          ("sessTimeOut", 100),
          ("tsClosedVirtualConnect", 29),
          ("tsControlC", 27),
          ("tsDestroyed", 28),
          ("tsErrorResource", 33),
          ("tsExitErrBadPort", 54),
          ("tsExitErrClosed", 63),
          ("tsExitErrConnRefused", 61),
          ("tsExitErrHostAdminUnreach", 67),
          ("tsExitErrHostName", 53),
          ("tsExitErrHostReset", 60),
          ("tsExitErrHostUnreach", 65),
          ("tsExitErrInvalidIP", 52),
          ("tsExitErrNetAdminUnreach", 66),
          ("tsExitErrNetUnreach", 64),
          ("tsExitErrPortUnreach", 68),
          ("tsExitErrResource", 51),
          ("tsExitErrTimedOut", 62),
          ("tsExitErrTooMany", 50),
          ("tsExitRlogin", 31),
          ("tsExitTcp", 24),
          ("tsExitTelnet", 22),
          ("tsIdleTimeout", 21),
          ("tsNoIPAddr", 23),
          ("tsPassWordFail", 25),
          ("tsRawTCPDisable", 26),
          ("tsRloginBadOption", 32),
          ("tsUserExit", 20),
          ("tsVirtualConnectDestroyed", 30),
          ("unknown", 2),
          ("userCallClearRequest", 180),
          ("v110Timeout", 160))
    )


_LucentPM4AMCEDisconnReason_Type.__name__ = "Integer32"
_LucentPM4AMCEDisconnReason_Object = MibTableColumn
lucentPM4AMCEDisconnReason = _LucentPM4AMCEDisconnReason_Object(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 1, 8, 2, 1, 1, 15),
    _LucentPM4AMCEDisconnReason_Type()
)
lucentPM4AMCEDisconnReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lucentPM4AMCEDisconnReason.setStatus("mandatory")
_LucentPM4Traps_ObjectIdentity = ObjectIdentity
lucentPM4Traps = _LucentPM4Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2)
)

# Managed Objects groups


# Notification objects

lucentPM4BoardOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 1)
)
lucentPM4BoardOfflineTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardOfflineTrap.setStatus(
        ""
    )

lucentPM4BoardOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 2)
)
lucentPM4BoardOnlineTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardOnlineTrap.setStatus(
        ""
    )

lucentPM4PwrSupFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 3)
)
lucentPM4PwrSupFailTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4PwrSupFailTrap.setStatus(
        ""
    )

lucentPM4PwrSupWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 4)
)
lucentPM4PwrSupWarnTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4PwrSupWarnTrap.setStatus(
        ""
    )

lucentPM4PwrSupRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 5)
)
lucentPM4PwrSupRestoredTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4PwrSupRestoredTrap.setStatus(
        ""
    )

lucentPM4FanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 6)
)
lucentPM4FanFailTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4FanFailTrap.setStatus(
        ""
    )

lucentPM4FanRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 7)
)
lucentPM4FanRestoredTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4FanRestoredTrap.setStatus(
        ""
    )

lucentPM4BoardTempWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 8)
)
lucentPM4BoardTempWarnTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardTempWarnTrap.setStatus(
        ""
    )

lucentPM4BoardTempNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 9)
)
lucentPM4BoardTempNormalTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardTempNormalTrap.setStatus(
        ""
    )

lucentPM4BoardTooHotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 10)
)
lucentPM4BoardTooHotTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardTooHotTrap.setStatus(
        ""
    )

lucentPM4ModemFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 11)
)
lucentPM4ModemFailTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4ModemFailTrap.setStatus(
        ""
    )

lucentPM4T1E1LineDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 12)
)
lucentPM4T1E1LineDownTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4T1E1LineDownTrap.setStatus(
        ""
    )

lucentPM4T1E1LineUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 13)
)
lucentPM4T1E1LineUpTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4T1E1LineUpTrap.setStatus(
        ""
    )

lucentPM4T1E1LineThreshTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 14)
)
lucentPM4T1E1LineThreshTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4T1E1LineThreshTrap.setStatus(
        ""
    )

lucentPM4BoardPwrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 15)
)
lucentPM4BoardPwrOffTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitType"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitTrapStatus"))
)
if mibBuilder.loadTexts:
    lucentPM4BoardPwrOffTrap.setStatus(
        ""
    )

lucentPM4RadiusAuthFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 1, 1, 2, 2, 0, 16)
)
lucentPM4RadiusAuthFailTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMBoardIndex"),
        ("LIVINGSTON-PM4-MIB", "lucentPM4FMUnitIndex"))
)
if mibBuilder.loadTexts:
    lucentPM4RadiusAuthFailTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIVINGSTON-PM4-MIB",
    **{"PMUnitType": PMUnitType,
       "PMEquipPRIStatus": PMEquipPRIStatus,
       "PMEquipStatus": PMEquipStatus,
       "PMDiagCmdStatus": PMDiagCmdStatus,
       "PMDiagTestCntrl": PMDiagTestCntrl,
       "PMAlarmType": PMAlarmType,
       "lucentPM4Mib": lucentPM4Mib,
       "lucentPM4MibRev": lucentPM4MibRev,
       "lucentPM4SWRev": lucentPM4SWRev,
       "lucentPM4Chassis": lucentPM4Chassis,
       "lucentPM4ChasSummary": lucentPM4ChasSummary,
       "lucentPM4ChasCmdTable": lucentPM4ChasCmdTable,
       "lucentPM4ChasCmdEntry": lucentPM4ChasCmdEntry,
       "lucentPM4ChasCmdIndex": lucentPM4ChasCmdIndex,
       "lucentPM4ChasCmdBoardId": lucentPM4ChasCmdBoardId,
       "lucentPM4ChasCmdUnitType": lucentPM4ChasCmdUnitType,
       "lucentPM4ChasCmdUnitIndex": lucentPM4ChasCmdUnitIndex,
       "lucentPM4ChasCmdDevId": lucentPM4ChasCmdDevId,
       "lucentPM4ChasCmdId": lucentPM4ChasCmdId,
       "lucentPM4ChasCmdParams": lucentPM4ChasCmdParams,
       "lucentPM4ChasCmdResult": lucentPM4ChasCmdResult,
       "lucentPM4ConfigMgmt": lucentPM4ConfigMgmt,
       "lucentPM4CmInterfaces": lucentPM4CmInterfaces,
       "lucentPM4CmSerial": lucentPM4CmSerial,
       "lucentPM4SerialTable": lucentPM4SerialTable,
       "lucentPM4SerialEntry": lucentPM4SerialEntry,
       "lucentPM4SerialBoardIndex": lucentPM4SerialBoardIndex,
       "lucentPM4SerialUnitType": lucentPM4SerialUnitType,
       "lucentPM4SerialIndex": lucentPM4SerialIndex,
       "lucentPM4ModemId": lucentPM4ModemId,
       "lucentPM4SerialPortNumber": lucentPM4SerialPortNumber,
       "lucentPM4SerialPhysType": lucentPM4SerialPhysType,
       "lucentPM4SerialPortStatus": lucentPM4SerialPortStatus,
       "lucentPM4SerialDS0State": lucentPM4SerialDS0State,
       "lucentPM4SerialUser": lucentPM4SerialUser,
       "lucentPM4SerialSessionId": lucentPM4SerialSessionId,
       "lucentPM4SerialTypeHardwired": lucentPM4SerialTypeHardwired,
       "lucentPM4SerialTypeNwDialIn": lucentPM4SerialTypeNwDialIn,
       "lucentPM4SerialTypeNwDialout": lucentPM4SerialTypeNwDialout,
       "lucentPM4SerialTypeLogin": lucentPM4SerialTypeLogin,
       "lucentPM4SerialTypeDevice": lucentPM4SerialTypeDevice,
       "lucentPM4SerialTypeDeviceName": lucentPM4SerialTypeDeviceName,
       "lucentPM4SerialDirection": lucentPM4SerialDirection,
       "lucentPM4SerialStarted": lucentPM4SerialStarted,
       "lucentPM4SerialIdle": lucentPM4SerialIdle,
       "lucentPM4SerialInSpeed": lucentPM4SerialInSpeed,
       "lucentPM4SerialOutSpeed": lucentPM4SerialOutSpeed,
       "lucentPM4SerialIpAddress": lucentPM4SerialIpAddress,
       "lucentPM4SerialifDescr": lucentPM4SerialifDescr,
       "lucentPM4SerialInOctets": lucentPM4SerialInOctets,
       "lucentPM4SerialOutOctets": lucentPM4SerialOutOctets,
       "lucentPM4SerialQOctets": lucentPM4SerialQOctets,
       "lucentPM4CmT1E1": lucentPM4CmT1E1,
       "lucentPM4T1E1Table": lucentPM4T1E1Table,
       "lucentPM4T1E1Entry": lucentPM4T1E1Entry,
       "lucentPM4T1E1BoardIndex": lucentPM4T1E1BoardIndex,
       "lucentPM4T1E1UnitType": lucentPM4T1E1UnitType,
       "lucentPM4T1E1Index": lucentPM4T1E1Index,
       "lucentPM4T1E1SerialIndex": lucentPM4T1E1SerialIndex,
       "lucentPM4T1E1SerialCount": lucentPM4T1E1SerialCount,
       "lucentPM4T1E1PhysType": lucentPM4T1E1PhysType,
       "lucentPM4T1E1Status": lucentPM4T1E1Status,
       "lucentPM4T1E1Function": lucentPM4T1E1Function,
       "lucentPM4T1E1Framing": lucentPM4T1E1Framing,
       "lucentPM4T1E1Encoding": lucentPM4T1E1Encoding,
       "lucentPM4T1E1PCM": lucentPM4T1E1PCM,
       "lucentPM4T1E1SuperSignal": lucentPM4T1E1SuperSignal,
       "lucentPM4T1E1StartMode": lucentPM4T1E1StartMode,
       "lucentPM4T1E1ChangeTime": lucentPM4T1E1ChangeTime,
       "lucentPM4T1E1RecvLevel": lucentPM4T1E1RecvLevel,
       "lucentPM4T1E1BlueAlarms": lucentPM4T1E1BlueAlarms,
       "lucentPM4T1E1YellowAlarms": lucentPM4T1E1YellowAlarms,
       "lucentPM4T1E1CarrierLoss": lucentPM4T1E1CarrierLoss,
       "lucentPM4T1E1SyncLoss": lucentPM4T1E1SyncLoss,
       "lucentPM4T1E1BipolarErrors": lucentPM4T1E1BipolarErrors,
       "lucentPM4T1E1CRCErrors": lucentPM4T1E1CRCErrors,
       "lucentPM4T1E1SyncErrors": lucentPM4T1E1SyncErrors,
       "lucentPM4CmModem": lucentPM4CmModem,
       "lucentPM4ModemTable": lucentPM4ModemTable,
       "lucentPM4ModemEntry": lucentPM4ModemEntry,
       "lucentPM4ModemBoardIndex": lucentPM4ModemBoardIndex,
       "lucentPM4ModemUnitType": lucentPM4ModemUnitType,
       "lucentPM4ModemIndex": lucentPM4ModemIndex,
       "lucentPM4ModemPortName": lucentPM4ModemPortName,
       "lucentPM4ModemStatus": lucentPM4ModemStatus,
       "lucentPM4ModemProtocol": lucentPM4ModemProtocol,
       "lucentPM4ModemCompression": lucentPM4ModemCompression,
       "lucentPM4ModemInSpeed": lucentPM4ModemInSpeed,
       "lucentPM4ModemOutSpeed": lucentPM4ModemOutSpeed,
       "lucentPM4ModemInByteCount": lucentPM4ModemInByteCount,
       "lucentPM4ModemOutByteCount": lucentPM4ModemOutByteCount,
       "lucentPM4ModemRetrains": lucentPM4ModemRetrains,
       "lucentPM4ModemRenegotiates": lucentPM4ModemRenegotiates,
       "lucentPM4ModemCalls": lucentPM4ModemCalls,
       "lucentPM4ModemDetects": lucentPM4ModemDetects,
       "lucentPM4ModemConnects": lucentPM4ModemConnects,
       "lucentPM4CmEther": lucentPM4CmEther,
       "lucentPM4EtherTable": lucentPM4EtherTable,
       "lucentPM4EtherEntry": lucentPM4EtherEntry,
       "lucentPM4EtherBoardIndex": lucentPM4EtherBoardIndex,
       "lucentPM4EtherIfType": lucentPM4EtherIfType,
       "lucentPM4EtherIndex": lucentPM4EtherIndex,
       "lucentPM4EtherIfIndex": lucentPM4EtherIfIndex,
       "lucentPM4EtherPortName": lucentPM4EtherPortName,
       "lucentPM4EtherMacAddress": lucentPM4EtherMacAddress,
       "lucentPM4EtherIpAddress": lucentPM4EtherIpAddress,
       "lucentPM4EtherIpGateway": lucentPM4EtherIpGateway,
       "lucentPM4EtherPriNameServer": lucentPM4EtherPriNameServer,
       "lucentPM4EtherAltNameServer": lucentPM4EtherAltNameServer,
       "lucentPM4EtherSubnetMask": lucentPM4EtherSubnetMask,
       "lucentPM4EtherInFilter": lucentPM4EtherInFilter,
       "lucentPM4EtherOutFilter": lucentPM4EtherOutFilter,
       "lucentPM4EtherOptRip": lucentPM4EtherOptRip,
       "lucentPM4EtherOptSlip": lucentPM4EtherOptSlip,
       "lucentPM4EtherOptEtherDown": lucentPM4EtherOptEtherDown,
       "lucentPM4EtherOptBcastHigh": lucentPM4EtherOptBcastHigh,
       "lucentPM4EtherOptSnmp": lucentPM4EtherOptSnmp,
       "lucentPM4EtherOptNoListen": lucentPM4EtherOptNoListen,
       "lucentPM4EtherOptDefaultRip": lucentPM4EtherOptDefaultRip,
       "lucentPM4EtherOptDefaultListen": lucentPM4EtherOptDefaultListen,
       "lucentPM4EtherOptIPFilter": lucentPM4EtherOptIPFilter,
       "lucentPM4EtherOptDns": lucentPM4EtherOptDns,
       "lucentPM4EtherOptPmeMsg": lucentPM4EtherOptPmeMsg,
       "lucentPM4EtherOptNoClip": lucentPM4EtherOptNoClip,
       "lucentPM4EtherOptEtherIpx": lucentPM4EtherOptEtherIpx,
       "lucentPM4EtherOptNetBIOS": lucentPM4EtherOptNetBIOS,
       "lucentPM4EtherOptAccounting": lucentPM4EtherOptAccounting,
       "lucentPM4EtherOptNoPAP": lucentPM4EtherOptNoPAP,
       "lucentPM4FaultMgmt": lucentPM4FaultMgmt,
       "lucentPM4FaultMgmtIsolation": lucentPM4FaultMgmtIsolation,
       "lucentPM4FaultMgmtChasTrap": lucentPM4FaultMgmtChasTrap,
       "lucentPM4FMChasTrapEntry": lucentPM4FMChasTrapEntry,
       "lucentPM4FMChasTrapIndex": lucentPM4FMChasTrapIndex,
       "lucentPM4FMChasTrapBoardID": lucentPM4FMChasTrapBoardID,
       "lucentPM4FMChasTrapUnitType": lucentPM4FMChasTrapUnitType,
       "lucentPM4FMChasTrapUnitIndex": lucentPM4FMChasTrapUnitIndex,
       "lucentPM4FMChasTrapStatus": lucentPM4FMChasTrapStatus,
       "lucentPM4FMChasTrapSeverity": lucentPM4FMChasTrapSeverity,
       "lucentPM4FMChasTrapTimeStamp": lucentPM4FMChasTrapTimeStamp,
       "lucentPM4FMChasTrapState": lucentPM4FMChasTrapState,
       "lucentPM4FMBoardIndex": lucentPM4FMBoardIndex,
       "lucentPM4FMUnitIndex": lucentPM4FMUnitIndex,
       "lucentPM4FMUnitType": lucentPM4FMUnitType,
       "lucentPM4FMUnitTrapStatus": lucentPM4FMUnitTrapStatus,
       "lucentPM4FMUnitTrapSeverity": lucentPM4FMUnitTrapSeverity,
       "lucentPM4FMTrapConfig": lucentPM4FMTrapConfig,
       "lucentPM4FMEqpTrapCfg": lucentPM4FMEqpTrapCfg,
       "lucentPM4FMEqpTrapCfgEntry": lucentPM4FMEqpTrapCfgEntry,
       "lucentPM4FMEqpBoardIndex": lucentPM4FMEqpBoardIndex,
       "lucentPM4FMEqpUnitType": lucentPM4FMEqpUnitType,
       "lucentPM4FMEqpUnitIndex": lucentPM4FMEqpUnitIndex,
       "lucentPM4FMEqpTrapId": lucentPM4FMEqpTrapId,
       "lucentPM4FMEqpTrapCtl": lucentPM4FMEqpTrapCtl,
       "lucentPM4FMEqpRepTimer": lucentPM4FMEqpRepTimer,
       "lucentPM4FMT1E1ThreshTrapCfg": lucentPM4FMT1E1ThreshTrapCfg,
       "lucentPM4FMT1E1ThreshTrapCfgEntry": lucentPM4FMT1E1ThreshTrapCfgEntry,
       "lucentPM4FMT1E1ThreshBoardIndex": lucentPM4FMT1E1ThreshBoardIndex,
       "lucentPM4FMT1E1ThreshUnitType": lucentPM4FMT1E1ThreshUnitType,
       "lucentPM4FMT1E1ThreshESs": lucentPM4FMT1E1ThreshESs,
       "lucentPM4FMT1E1ThreshSESs": lucentPM4FMT1E1ThreshSESs,
       "lucentPM4FMT1E1ThreshSEFSs": lucentPM4FMT1E1ThreshSEFSs,
       "lucentPM4FMT1E1ThreshUASs": lucentPM4FMT1E1ThreshUASs,
       "lucentPM4FMT1E1ThreshCSSs": lucentPM4FMT1E1ThreshCSSs,
       "lucentPM4FMT1E1ThreshPCVs": lucentPM4FMT1E1ThreshPCVs,
       "lucentPM4FMT1E1ThreshLESs": lucentPM4FMT1E1ThreshLESs,
       "lucentPM4FMT1E1ThreshBESs": lucentPM4FMT1E1ThreshBESs,
       "lucentPM4FMT1E1ThreshDMs": lucentPM4FMT1E1ThreshDMs,
       "lucentPM4FMT1E1ThreshRepTimer": lucentPM4FMT1E1ThreshRepTimer,
       "lucentPM4FMT1E1ThreshTrapAck": lucentPM4FMT1E1ThreshTrapAck,
       "lucentPM4FMEnvTrapCfg": lucentPM4FMEnvTrapCfg,
       "lucentPM4FMEnvTrapCfgEntry": lucentPM4FMEnvTrapCfgEntry,
       "lucentPM4FMEnvBoardID": lucentPM4FMEnvBoardID,
       "lucentPM4FMEnvUnitType": lucentPM4FMEnvUnitType,
       "lucentPM4FMEnvUnitIndex": lucentPM4FMEnvUnitIndex,
       "lucentPM4FMEnvOptUnitTemp": lucentPM4FMEnvOptUnitTemp,
       "lucentPM4FMEnvUnitTempRange": lucentPM4FMEnvUnitTempRange,
       "lucentPM4FMEnvOptUnitPwrLvl": lucentPM4FMEnvOptUnitPwrLvl,
       "lucentPM4FMEnvUnitPwrRange": lucentPM4FMEnvUnitPwrRange,
       "lucentPM4FMEnvTrapCtl": lucentPM4FMEnvTrapCtl,
       "lucentPM4PerfMgmt": lucentPM4PerfMgmt,
       "lucentPM4T1E1PerfMgmt": lucentPM4T1E1PerfMgmt,
       "lucentPM4T1E1PMCur": lucentPM4T1E1PMCur,
       "lucentPM4T1E1PMCurEntry": lucentPM4T1E1PMCurEntry,
       "lucentPM4T1E1PMCurBoard": lucentPM4T1E1PMCurBoard,
       "lucentPM4T1E1PMCurUnitType": lucentPM4T1E1PMCurUnitType,
       "lucentPM4T1E1PMCurLineNum": lucentPM4T1E1PMCurLineNum,
       "lucentPM4T1E1PMCurIfIndex": lucentPM4T1E1PMCurIfIndex,
       "lucentPM4T1E1PMCurESs": lucentPM4T1E1PMCurESs,
       "lucentPM4T1E1PMCurSESs": lucentPM4T1E1PMCurSESs,
       "lucentPM4T1E1PMCurSEFSs": lucentPM4T1E1PMCurSEFSs,
       "lucentPM4T1E1PMCurUASs": lucentPM4T1E1PMCurUASs,
       "lucentPM4T1E1PMCurCSSs": lucentPM4T1E1PMCurCSSs,
       "lucentPM4T1E1PMCurPCVs": lucentPM4T1E1PMCurPCVs,
       "lucentPM4T1E1PMCurLESs": lucentPM4T1E1PMCurLESs,
       "lucentPM4T1E1PMCurBESs": lucentPM4T1E1PMCurBESs,
       "lucentPM4T1E1PMCurDMs": lucentPM4T1E1PMCurDMs,
       "lucentPM4T1E1PMCurLCVs": lucentPM4T1E1PMCurLCVs,
       "lucentPM4T1E1PMInt": lucentPM4T1E1PMInt,
       "lucentPM4T1E1PMIntEntry": lucentPM4T1E1PMIntEntry,
       "lucentPM4T1E1PMIntBoard": lucentPM4T1E1PMIntBoard,
       "lucentPM4T1E1PMIntUnitType": lucentPM4T1E1PMIntUnitType,
       "lucentPM4T1E1PMIntLineNum": lucentPM4T1E1PMIntLineNum,
       "lucentPM4T1E1PMIntInterval": lucentPM4T1E1PMIntInterval,
       "lucentPM4T1E1PMIntIfIndex": lucentPM4T1E1PMIntIfIndex,
       "lucentPM4T1E1PMIntESs": lucentPM4T1E1PMIntESs,
       "lucentPM4T1E1PMIntSESs": lucentPM4T1E1PMIntSESs,
       "lucentPM4T1E1PMIntSEFSs": lucentPM4T1E1PMIntSEFSs,
       "lucentPM4T1E1PMIntUASs": lucentPM4T1E1PMIntUASs,
       "lucentPM4T1E1PMIntCSSs": lucentPM4T1E1PMIntCSSs,
       "lucentPM4T1E1PMIntPCVs": lucentPM4T1E1PMIntPCVs,
       "lucentPM4T1E1PMIntLESs": lucentPM4T1E1PMIntLESs,
       "lucentPM4T1E1PMIntBESs": lucentPM4T1E1PMIntBESs,
       "lucentPM4T1E1PMIntDMs": lucentPM4T1E1PMIntDMs,
       "lucentPM4T1E1PMIntLCVs": lucentPM4T1E1PMIntLCVs,
       "lucentPM4T1E1PMTotal": lucentPM4T1E1PMTotal,
       "lucentPM4T1E1PMTotalEntry": lucentPM4T1E1PMTotalEntry,
       "lucentPM4T1E1PMTotalBoard": lucentPM4T1E1PMTotalBoard,
       "lucentPM4T1E1PMTotalUnitType": lucentPM4T1E1PMTotalUnitType,
       "lucentPM4T1E1PMTotalLineNum": lucentPM4T1E1PMTotalLineNum,
       "lucentPM4T1E1PMTotalIfIndex": lucentPM4T1E1PMTotalIfIndex,
       "lucentPM4T1E1PMTotalESs": lucentPM4T1E1PMTotalESs,
       "lucentPM4T1E1PMTotalSESs": lucentPM4T1E1PMTotalSESs,
       "lucentPM4T1E1PMTotalSEFSs": lucentPM4T1E1PMTotalSEFSs,
       "lucentPM4T1E1PMTotalUASs": lucentPM4T1E1PMTotalUASs,
       "lucentPM4T1E1PMTotalCSSs": lucentPM4T1E1PMTotalCSSs,
       "lucentPM4T1E1PMTotalPCVs": lucentPM4T1E1PMTotalPCVs,
       "lucentPM4T1E1PMTotalLESs": lucentPM4T1E1PMTotalLESs,
       "lucentPM4T1E1PMTotalBESs": lucentPM4T1E1PMTotalBESs,
       "lucentPM4T1E1PMTotalDMs": lucentPM4T1E1PMTotalDMs,
       "lucentPM4T1E1PMTotalLCVs": lucentPM4T1E1PMTotalLCVs,
       "lucentPM4SecurityMgmt": lucentPM4SecurityMgmt,
       "lucentPM4AcctMgmt": lucentPM4AcctMgmt,
       "lucentPM4AcctMgmtComm": lucentPM4AcctMgmtComm,
       "lucentPM4SnmpCommTable": lucentPM4SnmpCommTable,
       "lucentPM4SnmpCommEntry": lucentPM4SnmpCommEntry,
       "lucentPM4SnmpCommIndex": lucentPM4SnmpCommIndex,
       "lucentPM4SnmpCommName": lucentPM4SnmpCommName,
       "lucentPM4SnmpCommIpAddr": lucentPM4SnmpCommIpAddr,
       "lucentPM4SnmpCommReadAccess": lucentPM4SnmpCommReadAccess,
       "lucentPM4SnmpCommWriteAccess": lucentPM4SnmpCommWriteAccess,
       "lucentPM4SnmpCommTraps": lucentPM4SnmpCommTraps,
       "lucentPM4SnmpCommStatus": lucentPM4SnmpCommStatus,
       "lucentPM4SnmpCommLastError": lucentPM4SnmpCommLastError,
       "lucentPM4AcctMgmtCallEvent": lucentPM4AcctMgmtCallEvent,
       "lucentPM4AMCallEventTable": lucentPM4AMCallEventTable,
       "lucentPM4AMCallEventEntry": lucentPM4AMCallEventEntry,
       "lucentPM4AMCEIndex": lucentPM4AMCEIndex,
       "lucentPM4AMCETimeStamp": lucentPM4AMCETimeStamp,
       "lucentPM4AMCEType": lucentPM4AMCEType,
       "lucentPM4AMCESvcType": lucentPM4AMCESvcType,
       "lucentPM4AMCEUName": lucentPM4AMCEUName,
       "lucentPM4AMCEModemBoard": lucentPM4AMCEModemBoard,
       "lucentPM4AMCEModemID": lucentPM4AMCEModemID,
       "lucentPM4AMCEModemPort": lucentPM4AMCEModemPort,
       "lucentPM4AMCEDataRate": lucentPM4AMCEDataRate,
       "lucentPM4AMCECallingPartyID": lucentPM4AMCECallingPartyID,
       "lucentPM4AMCECalledPartyID": lucentPM4AMCECalledPartyID,
       "lucentPM4AMCEInOctets": lucentPM4AMCEInOctets,
       "lucentPM4AMCEOutOctets": lucentPM4AMCEOutOctets,
       "lucentPM4AMCECallCharge": lucentPM4AMCECallCharge,
       "lucentPM4AMCEDisconnReason": lucentPM4AMCEDisconnReason,
       "lucentPM4Traps": lucentPM4Traps,
       "lucentPM4BoardOfflineTrap": lucentPM4BoardOfflineTrap,
       "lucentPM4BoardOnlineTrap": lucentPM4BoardOnlineTrap,
       "lucentPM4PwrSupFailTrap": lucentPM4PwrSupFailTrap,
       "lucentPM4PwrSupWarnTrap": lucentPM4PwrSupWarnTrap,
       "lucentPM4PwrSupRestoredTrap": lucentPM4PwrSupRestoredTrap,
       "lucentPM4FanFailTrap": lucentPM4FanFailTrap,
       "lucentPM4FanRestoredTrap": lucentPM4FanRestoredTrap,
       "lucentPM4BoardTempWarnTrap": lucentPM4BoardTempWarnTrap,
       "lucentPM4BoardTempNormalTrap": lucentPM4BoardTempNormalTrap,
       "lucentPM4BoardTooHotTrap": lucentPM4BoardTooHotTrap,
       "lucentPM4ModemFailTrap": lucentPM4ModemFailTrap,
       "lucentPM4T1E1LineDownTrap": lucentPM4T1E1LineDownTrap,
       "lucentPM4T1E1LineUpTrap": lucentPM4T1E1LineUpTrap,
       "lucentPM4T1E1LineThreshTrap": lucentPM4T1E1LineThreshTrap,
       "lucentPM4BoardPwrOffTrap": lucentPM4BoardPwrOffTrap,
       "lucentPM4RadiusAuthFailTrap": lucentPM4RadiusAuthFailTrap}
)
