# SNMP MIB module (MOXA-IO-E2210-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOXA-IO-E2210-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:41 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

e2210 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210)
)
e2210.setRevisions(
        ("2009-11-04 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_E2000_ObjectIdentity = ObjectIdentity
e2000 = _E2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10)
)


class _TotalChannelNumber_Type(Integer32):
    """Custom type totalChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TotalChannelNumber_Type.__name__ = "Integer32"
_TotalChannelNumber_Object = MibScalar
totalChannelNumber = _TotalChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 1),
    _TotalChannelNumber_Type()
)
totalChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalChannelNumber.setStatus("current")
_ServerModel_Type = OctetString
_ServerModel_Object = MibScalar
serverModel = _ServerModel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 2),
    _ServerModel_Type()
)
serverModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverModel.setStatus("current")
_SystemTime_Type = Integer32
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 3),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_FirmwareVersion_Type = OctetString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_E2210monitor_ObjectIdentity = ObjectIdentity
e2210monitor = _E2210monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10)
)
_DiTable_Object = MibTable
diTable = _DiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1)
)
if mibBuilder.loadTexts:
    diTable.setStatus("current")
_DiEntry_Object = MibTableRow
diEntry = _DiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1)
)
diEntry.setIndexNames(
    (0, "MOXA-IO-E2210-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    diEntry.setStatus("current")


class _DiIndex_Type(Integer32):
    """Custom type diIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_DiIndex_Type.__name__ = "Integer32"
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiType_Type(Integer32):
    """Custom type diType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_DiType_Type.__name__ = "Integer32"
_DiType_Object = MibTableColumn
diType = _DiType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 2),
    _DiType_Type()
)
diType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diType.setStatus("current")


class _DiMode_Type(Integer32):
    """Custom type diMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DiMode_Type.__name__ = "Integer32"
_DiMode_Object = MibTableColumn
diMode = _DiMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 3),
    _DiMode_Type()
)
diMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diMode.setStatus("current")


class _DiStatus_Type(Unsigned32):
    """Custom type diStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DiStatus_Type.__name__ = "Unsigned32"
_DiStatus_Object = MibTableColumn
diStatus = _DiStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 4),
    _DiStatus_Type()
)
diStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diStatus.setStatus("current")


class _DiFilter_Type(Integer32):
    """Custom type diFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_DiFilter_Type.__name__ = "Integer32"
_DiFilter_Object = MibTableColumn
diFilter = _DiFilter_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 5),
    _DiFilter_Type()
)
diFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diFilter.setStatus("current")


class _DiTrigger_Type(Integer32):
    """Custom type diTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DiTrigger_Type.__name__ = "Integer32"
_DiTrigger_Object = MibTableColumn
diTrigger = _DiTrigger_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 6),
    _DiTrigger_Type()
)
diTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diTrigger.setStatus("current")


class _DiCntStart_Type(Integer32):
    """Custom type diCntStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DiCntStart_Type.__name__ = "Integer32"
_DiCntStart_Object = MibTableColumn
diCntStart = _DiCntStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 1, 1, 7),
    _DiCntStart_Type()
)
diCntStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diCntStart.setStatus("current")
_DoTable_Object = MibTable
doTable = _DoTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2)
)
if mibBuilder.loadTexts:
    doTable.setStatus("current")
_DoEntry_Object = MibTableRow
doEntry = _DoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1)
)
doEntry.setIndexNames(
    (0, "MOXA-IO-E2210-MIB", "doIndex"),
)
if mibBuilder.loadTexts:
    doEntry.setStatus("current")


class _DoIndex_Type(Integer32):
    """Custom type doIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DoIndex_Type.__name__ = "Integer32"
_DoIndex_Object = MibTableColumn
doIndex = _DoIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 1),
    _DoIndex_Type()
)
doIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    doIndex.setStatus("current")


class _DoType_Type(Integer32):
    """Custom type doType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_DoType_Type.__name__ = "Integer32"
_DoType_Object = MibTableColumn
doType = _DoType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 2),
    _DoType_Type()
)
doType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    doType.setStatus("current")


class _DoMode_Type(Integer32):
    """Custom type doMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DoMode_Type.__name__ = "Integer32"
_DoMode_Object = MibTableColumn
doMode = _DoMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 3),
    _DoMode_Type()
)
doMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doMode.setStatus("current")


class _DoStatus_Type(Unsigned32):
    """Custom type doStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DoStatus_Type.__name__ = "Unsigned32"
_DoStatus_Object = MibTableColumn
doStatus = _DoStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 4),
    _DoStatus_Type()
)
doStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doStatus.setStatus("current")


class _DoLowWidth_Type(Integer32):
    """Custom type doLowWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_DoLowWidth_Type.__name__ = "Integer32"
_DoLowWidth_Object = MibTableColumn
doLowWidth = _DoLowWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 5),
    _DoLowWidth_Type()
)
doLowWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doLowWidth.setStatus("current")


class _DoHighWidth_Type(Integer32):
    """Custom type doHighWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_DoHighWidth_Type.__name__ = "Integer32"
_DoHighWidth_Object = MibTableColumn
doHighWidth = _DoHighWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 6),
    _DoHighWidth_Type()
)
doHighWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doHighWidth.setStatus("current")


class _DoPulseStart_Type(Integer32):
    """Custom type doPulseStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DoPulseStart_Type.__name__ = "Integer32"
_DoPulseStart_Object = MibTableColumn
doPulseStart = _DoPulseStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 2, 1, 7),
    _DoPulseStart_Type()
)
doPulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    doPulseStart.setStatus("current")
_LogicSettings_ObjectIdentity = ObjectIdentity
logicSettings = _LogicSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4)
)
_IrTable_Object = MibTable
irTable = _IrTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1)
)
if mibBuilder.loadTexts:
    irTable.setStatus("current")
_IrEntry_Object = MibTableRow
irEntry = _IrEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1)
)
irEntry.setIndexNames(
    (0, "MOXA-IO-E2210-MIB", "irIndex"),
)
if mibBuilder.loadTexts:
    irEntry.setStatus("current")


class _IrIndex_Type(Integer32):
    """Custom type irIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_IrIndex_Type.__name__ = "Integer32"
_IrIndex_Object = MibTableColumn
irIndex = _IrIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 1),
    _IrIndex_Type()
)
irIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irIndex.setStatus("current")


class _IrName_Type(OctetString):
    """Custom type irName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_IrName_Type.__name__ = "OctetString"
_IrName_Object = MibTableColumn
irName = _IrName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 2),
    _IrName_Type()
)
irName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irName.setStatus("current")


class _IrValue_Type(Integer32):
    """Custom type irValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IrValue_Type.__name__ = "Integer32"
_IrValue_Object = MibTableColumn
irValue = _IrValue_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 10, 4, 1, 1, 3),
    _IrValue_Type()
)
irValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irValue.setStatus("current")
_DiChannelTrap_ObjectIdentity = ObjectIdentity
diChannelTrap = _DiChannelTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 11)
)
_DoChannelTrap_ObjectIdentity = ObjectIdentity
doChannelTrap = _DoChannelTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 12)
)
_MessageTrap_ObjectIdentity = ObjectIdentity
messageTrap = _MessageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 13)
)

# Managed Objects groups


# Notification objects

diChannel0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 1)
)
if mibBuilder.loadTexts:
    diChannel0.setStatus(
        ""
    )

doChannel0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 1)
)
if mibBuilder.loadTexts:
    doChannel0.setStatus(
        ""
    )

activeMessageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 1)
)
if mibBuilder.loadTexts:
    activeMessageTrap.setStatus(
        ""
    )

diChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 2)
)
if mibBuilder.loadTexts:
    diChannel1.setStatus(
        ""
    )

doChannel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 2)
)
if mibBuilder.loadTexts:
    doChannel1.setStatus(
        ""
    )

diChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 3)
)
if mibBuilder.loadTexts:
    diChannel2.setStatus(
        ""
    )

doChannel2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 3)
)
if mibBuilder.loadTexts:
    doChannel2.setStatus(
        ""
    )

diChannel3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 4)
)
if mibBuilder.loadTexts:
    diChannel3.setStatus(
        ""
    )

doChannel3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 4)
)
if mibBuilder.loadTexts:
    doChannel3.setStatus(
        ""
    )

diChannel4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 5)
)
if mibBuilder.loadTexts:
    diChannel4.setStatus(
        ""
    )

doChannel4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 5)
)
if mibBuilder.loadTexts:
    doChannel4.setStatus(
        ""
    )

diChannel5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 6)
)
if mibBuilder.loadTexts:
    diChannel5.setStatus(
        ""
    )

doChannel5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 6)
)
if mibBuilder.loadTexts:
    doChannel5.setStatus(
        ""
    )

diChannel6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 7)
)
if mibBuilder.loadTexts:
    diChannel6.setStatus(
        ""
    )

doChannel6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 7)
)
if mibBuilder.loadTexts:
    doChannel6.setStatus(
        ""
    )

diChannel7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 8)
)
if mibBuilder.loadTexts:
    diChannel7.setStatus(
        ""
    )

doChannel7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 8)
)
if mibBuilder.loadTexts:
    doChannel7.setStatus(
        ""
    )

diChannel8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 9)
)
if mibBuilder.loadTexts:
    diChannel8.setStatus(
        ""
    )

diChannel9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 10)
)
if mibBuilder.loadTexts:
    diChannel9.setStatus(
        ""
    )

diChannel10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 11)
)
if mibBuilder.loadTexts:
    diChannel10.setStatus(
        ""
    )

diChannel11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 2210, 0, 12)
)
if mibBuilder.loadTexts:
    diChannel11.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-IO-E2210-MIB",
    **{"moxa": moxa,
       "e2000": e2000,
       "e2210": e2210,
       "diChannel0": diChannel0,
       "doChannel0": doChannel0,
       "activeMessageTrap": activeMessageTrap,
       "diChannel1": diChannel1,
       "doChannel1": doChannel1,
       "diChannel2": diChannel2,
       "doChannel2": doChannel2,
       "diChannel3": diChannel3,
       "doChannel3": doChannel3,
       "diChannel4": diChannel4,
       "doChannel4": doChannel4,
       "diChannel5": diChannel5,
       "doChannel5": doChannel5,
       "diChannel6": diChannel6,
       "doChannel6": doChannel6,
       "diChannel7": diChannel7,
       "doChannel7": doChannel7,
       "diChannel8": diChannel8,
       "diChannel9": diChannel9,
       "diChannel10": diChannel10,
       "diChannel11": diChannel11,
       "totalChannelNumber": totalChannelNumber,
       "serverModel": serverModel,
       "systemTime": systemTime,
       "firmwareVersion": firmwareVersion,
       "e2210monitor": e2210monitor,
       "diTable": diTable,
       "diEntry": diEntry,
       "diIndex": diIndex,
       "diType": diType,
       "diMode": diMode,
       "diStatus": diStatus,
       "diFilter": diFilter,
       "diTrigger": diTrigger,
       "diCntStart": diCntStart,
       "doTable": doTable,
       "doEntry": doEntry,
       "doIndex": doIndex,
       "doType": doType,
       "doMode": doMode,
       "doStatus": doStatus,
       "doLowWidth": doLowWidth,
       "doHighWidth": doHighWidth,
       "doPulseStart": doPulseStart,
       "logicSettings": logicSettings,
       "irTable": irTable,
       "irEntry": irEntry,
       "irIndex": irIndex,
       "irName": irName,
       "irValue": irValue,
       "diChannelTrap": diChannelTrap,
       "doChannelTrap": doChannelTrap,
       "messageTrap": messageTrap}
)
