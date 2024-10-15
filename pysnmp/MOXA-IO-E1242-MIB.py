# SNMP MIB module (MOXA-IO-E1242-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOXA-IO-E1242-MIB
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

e1242 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242)
)
e1242.setRevisions(
        ("2013-02-21 14:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_IoLogik_ObjectIdentity = ObjectIdentity
ioLogik = _IoLogik_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10)
)


class _TotalChannelNumber_Type(Integer32):
    """Custom type totalChannelNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TotalChannelNumber_Type.__name__ = "Integer32"
_TotalChannelNumber_Object = MibScalar
totalChannelNumber = _TotalChannelNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 1),
    _TotalChannelNumber_Type()
)
totalChannelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalChannelNumber.setStatus("current")
_ServerModel_Type = OctetString
_ServerModel_Object = MibScalar
serverModel = _ServerModel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 2),
    _ServerModel_Type()
)
serverModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverModel.setStatus("current")
_SystemTime_Type = Integer32
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 3),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("current")
_FirmwareVersion_Type = OctetString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")
_E1242monitor_ObjectIdentity = ObjectIdentity
e1242monitor = _E1242monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10)
)
_DiTable_Object = MibTable
diTable = _DiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1)
)
if mibBuilder.loadTexts:
    diTable.setStatus("current")
_DiEntry_Object = MibTableRow
diEntry = _DiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1)
)
diEntry.setIndexNames(
    (0, "MOXA-IO-E1242-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    diEntry.setStatus("current")


class _DiIndex_Type(Integer32):
    """Custom type diIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiIndex_Type.__name__ = "Integer32"
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiType_Type(Integer32):
    """Custom type diType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DiType_Type.__name__ = "Integer32"
_DiType_Object = MibTableColumn
diType = _DiType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 3),
    _DiMode_Type()
)
diMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diMode.setStatus("current")


class _DiStatus_Type(Integer32):
    """Custom type diStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DiStatus_Type.__name__ = "Integer32"
_DiStatus_Object = MibTableColumn
diStatus = _DiStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 4),
    _DiStatus_Type()
)
diStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diStatus.setStatus("current")


class _DiFilter_Type(Integer32):
    """Custom type diFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiFilter_Type.__name__ = "Integer32"
_DiFilter_Object = MibTableColumn
diFilter = _DiFilter_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 5),
    _DiFilter_Type()
)
diFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diFilter.setStatus("current")


class _DiTrigger_Type(Integer32):
    """Custom type diTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DiTrigger_Type.__name__ = "Integer32"
_DiTrigger_Object = MibTableColumn
diTrigger = _DiTrigger_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 1, 1, 7),
    _DiCntStart_Type()
)
diCntStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diCntStart.setStatus("current")
_DioTable_Object = MibTable
dioTable = _DioTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3)
)
if mibBuilder.loadTexts:
    dioTable.setStatus("current")
_DioEntry_Object = MibTableRow
dioEntry = _DioEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1)
)
dioEntry.setIndexNames(
    (0, "MOXA-IO-E1242-MIB", "dioIndex"),
)
if mibBuilder.loadTexts:
    dioEntry.setStatus("current")


class _DioIndex_Type(Integer32):
    """Custom type dioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DioIndex_Type.__name__ = "Integer32"
_DioIndex_Object = MibTableColumn
dioIndex = _DioIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 1),
    _DioIndex_Type()
)
dioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dioIndex.setStatus("current")


class _DioType_Type(Integer32):
    """Custom type dioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DioType_Type.__name__ = "Integer32"
_DioType_Object = MibTableColumn
dioType = _DioType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 2),
    _DioType_Type()
)
dioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dioType.setStatus("current")


class _DioMode_Type(Integer32):
    """Custom type dioMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DioMode_Type.__name__ = "Integer32"
_DioMode_Object = MibTableColumn
dioMode = _DioMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 3),
    _DioMode_Type()
)
dioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioMode.setStatus("current")


class _DioStatus_Type(Integer32):
    """Custom type dioStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_DioStatus_Type.__name__ = "Integer32"
_DioStatus_Object = MibTableColumn
dioStatus = _DioStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 4),
    _DioStatus_Type()
)
dioStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioStatus.setStatus("current")


class _DioDIFilter_Type(Integer32):
    """Custom type dioDIFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DioDIFilter_Type.__name__ = "Integer32"
_DioDIFilter_Object = MibTableColumn
dioDIFilter = _DioDIFilter_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 5),
    _DioDIFilter_Type()
)
dioDIFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDIFilter.setStatus("current")


class _DioDITrigger_Type(Integer32):
    """Custom type dioDITrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_DioDITrigger_Type.__name__ = "Integer32"
_DioDITrigger_Object = MibTableColumn
dioDITrigger = _DioDITrigger_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 6),
    _DioDITrigger_Type()
)
dioDITrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDITrigger.setStatus("current")


class _DioDICntStart_Type(Integer32):
    """Custom type dioDICntStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DioDICntStart_Type.__name__ = "Integer32"
_DioDICntStart_Object = MibTableColumn
dioDICntStart = _DioDICntStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 7),
    _DioDICntStart_Type()
)
dioDICntStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDICntStart.setStatus("current")


class _DioDOPulsONWidth_Type(Integer32):
    """Custom type dioDOPulsONWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DioDOPulsONWidth_Type.__name__ = "Integer32"
_DioDOPulsONWidth_Object = MibTableColumn
dioDOPulsONWidth = _DioDOPulsONWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 8),
    _DioDOPulsONWidth_Type()
)
dioDOPulsONWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDOPulsONWidth.setStatus("current")


class _DioDOPulsOFFWidth_Type(Integer32):
    """Custom type dioDOPulsOFFWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DioDOPulsOFFWidth_Type.__name__ = "Integer32"
_DioDOPulsOFFWidth_Object = MibTableColumn
dioDOPulsOFFWidth = _DioDOPulsOFFWidth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 9),
    _DioDOPulsOFFWidth_Type()
)
dioDOPulsOFFWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDOPulsOFFWidth.setStatus("current")


class _DioDOPulseStart_Type(Integer32):
    """Custom type dioDOPulseStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DioDOPulseStart_Type.__name__ = "Integer32"
_DioDOPulseStart_Object = MibTableColumn
dioDOPulseStart = _DioDOPulseStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 3, 1, 10),
    _DioDOPulseStart_Type()
)
dioDOPulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dioDOPulseStart.setStatus("current")
_AiTable_Object = MibTable
aiTable = _AiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4)
)
if mibBuilder.loadTexts:
    aiTable.setStatus("current")
_AiEntry_Object = MibTableRow
aiEntry = _AiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1)
)
aiEntry.setIndexNames(
    (0, "MOXA-IO-E1242-MIB", "aiIndex"),
)
if mibBuilder.loadTexts:
    aiEntry.setStatus("current")


class _AiIndex_Type(Integer32):
    """Custom type aiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AiIndex_Type.__name__ = "Integer32"
_AiIndex_Object = MibTableColumn
aiIndex = _AiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 1),
    _AiIndex_Type()
)
aiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiIndex.setStatus("current")


class _AiEnable_Type(Integer32):
    """Custom type aiEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AiEnable_Type.__name__ = "Integer32"
_AiEnable_Object = MibTableColumn
aiEnable = _AiEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 2),
    _AiEnable_Type()
)
aiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiEnable.setStatus("current")


class _AiMode_Type(Integer32):
    """Custom type aiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AiMode_Type.__name__ = "Integer32"
_AiMode_Object = MibTableColumn
aiMode = _AiMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 3),
    _AiMode_Type()
)
aiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aiMode.setStatus("current")


class _AiValue_Type(Integer32):
    """Custom type aiValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiValue_Type.__name__ = "Integer32"
_AiValue_Object = MibTableColumn
aiValue = _AiValue_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 4),
    _AiValue_Type()
)
aiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiValue.setStatus("current")


class _AiMin_Type(Integer32):
    """Custom type aiMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiMin_Type.__name__ = "Integer32"
_AiMin_Object = MibTableColumn
aiMin = _AiMin_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 5),
    _AiMin_Type()
)
aiMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMin.setStatus("current")


class _AiMax_Type(Integer32):
    """Custom type aiMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AiMax_Type.__name__ = "Integer32"
_AiMax_Object = MibTableColumn
aiMax = _AiMax_Object(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 10, 4, 1, 6),
    _AiMax_Type()
)
aiMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aiMax.setStatus("current")
_AiTrap_Greater_ObjectIdentity = ObjectIdentity
aiTrap_Greater = _AiTrap_Greater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22)
)
_AiTrap_Smaller_ObjectIdentity = ObjectIdentity
aiTrap_Smaller = _AiTrap_Smaller_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23)
)
_MessageTrap_ObjectIdentity = ObjectIdentity
messageTrap = _MessageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 30)
)

# Managed Objects groups


# Notification objects

aiTrapG0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22, 0, 1)
)
if mibBuilder.loadTexts:
    aiTrapG0.setStatus(
        ""
    )

aiTrapG1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22, 0, 2)
)
if mibBuilder.loadTexts:
    aiTrapG1.setStatus(
        ""
    )

aiTrapG2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22, 0, 3)
)
if mibBuilder.loadTexts:
    aiTrapG2.setStatus(
        ""
    )

aiTrapG3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 22, 0, 4)
)
if mibBuilder.loadTexts:
    aiTrapG3.setStatus(
        ""
    )

aiTrapS0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23, 0, 1)
)
if mibBuilder.loadTexts:
    aiTrapS0.setStatus(
        ""
    )

aiTrapS1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23, 0, 2)
)
if mibBuilder.loadTexts:
    aiTrapS1.setStatus(
        ""
    )

aiTrapS2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23, 0, 3)
)
if mibBuilder.loadTexts:
    aiTrapS2.setStatus(
        ""
    )

aiTrapS3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 23, 0, 4)
)
if mibBuilder.loadTexts:
    aiTrapS3.setStatus(
        ""
    )

activeMessageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 10, 1242, 30, 0, 1)
)
if mibBuilder.loadTexts:
    activeMessageTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-IO-E1242-MIB",
    **{"moxa": moxa,
       "ioLogik": ioLogik,
       "e1242": e1242,
       "totalChannelNumber": totalChannelNumber,
       "serverModel": serverModel,
       "systemTime": systemTime,
       "firmwareVersion": firmwareVersion,
       "e1242monitor": e1242monitor,
       "diTable": diTable,
       "diEntry": diEntry,
       "diIndex": diIndex,
       "diType": diType,
       "diMode": diMode,
       "diStatus": diStatus,
       "diFilter": diFilter,
       "diTrigger": diTrigger,
       "diCntStart": diCntStart,
       "dioTable": dioTable,
       "dioEntry": dioEntry,
       "dioIndex": dioIndex,
       "dioType": dioType,
       "dioMode": dioMode,
       "dioStatus": dioStatus,
       "dioDIFilter": dioDIFilter,
       "dioDITrigger": dioDITrigger,
       "dioDICntStart": dioDICntStart,
       "dioDOPulsONWidth": dioDOPulsONWidth,
       "dioDOPulsOFFWidth": dioDOPulsOFFWidth,
       "dioDOPulseStart": dioDOPulseStart,
       "aiTable": aiTable,
       "aiEntry": aiEntry,
       "aiIndex": aiIndex,
       "aiEnable": aiEnable,
       "aiMode": aiMode,
       "aiValue": aiValue,
       "aiMin": aiMin,
       "aiMax": aiMax,
       "aiTrap_Greater": aiTrap_Greater,
       "aiTrapG0": aiTrapG0,
       "aiTrapG1": aiTrapG1,
       "aiTrapG2": aiTrapG2,
       "aiTrapG3": aiTrapG3,
       "aiTrap_Smaller": aiTrap_Smaller,
       "aiTrapS0": aiTrapS0,
       "aiTrapS1": aiTrapS1,
       "aiTrapS2": aiTrapS2,
       "aiTrapS3": aiTrapS3,
       "messageTrap": messageTrap,
       "activeMessageTrap": activeMessageTrap}
)
