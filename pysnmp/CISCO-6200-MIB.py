# SNMP MIB module (CISCO-6200-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-6200-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:19 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

cisco6200MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26)
)
cisco6200MIB.setRevisions(
        ("1998-02-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class C6200CardType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
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
        *(("cap16", 4),
          ("cap8", 3),
          ("ctl", 2),
          ("dmt8", 9),
          ("none", -1),
          ("oc3mm", 6),
          ("oc3si", 1),
          ("oc3ss", 5),
          ("stm1mm", 8),
          ("stm1si", 7))
    )



class CommandValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )



class AlarmLevel(Integer32, TextualConvention):
    status = "current"
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
        *(("critical", 4),
          ("major", 3),
          ("minor", 2),
          ("none", 1),
          ("unknown", 5))
    )



class InterfaceStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )



class TestStatus(Integer32, TextualConvention):
    status = "current"
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
          ("active", 2),
          ("fail", 4),
          ("inactive", 1),
          ("pass", 3),
          ("waiting", 6))
    )



class TestType(Integer32, TextualConvention):
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
        *(("capHardware", 2),
          ("dmtLocalTest", 3),
          ("lineQuality", 1),
          ("none", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Cisco6200MibObjects_ObjectIdentity = ObjectIdentity
cisco6200MibObjects = _Cisco6200MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1)
)
_C62System_ObjectIdentity = ObjectIdentity
c62System = _C62System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1)
)


class _SystemType_Type(Integer32):
    """Custom type systemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("c62OC3", 1)
    )


_SystemType_Type.__name__ = "Integer32"
_SystemType_Object = MibScalar
systemType = _SystemType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 1),
    _SystemType_Type()
)
systemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemType.setStatus("current")
_SystemAlarmLevel_Type = AlarmLevel
_SystemAlarmLevel_Object = MibScalar
systemAlarmLevel = _SystemAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 2),
    _SystemAlarmLevel_Type()
)
systemAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmLevel.setStatus("current")
_SystemAlarmLevelChngCounter_Type = Counter32
_SystemAlarmLevelChngCounter_Object = MibScalar
systemAlarmLevelChngCounter = _SystemAlarmLevelChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 3),
    _SystemAlarmLevelChngCounter_Type()
)
systemAlarmLevelChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemAlarmLevelChngCounter.setStatus("current")
_SystemReset_Type = CommandValue
_SystemReset_Object = MibScalar
systemReset = _SystemReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 4),
    _SystemReset_Type()
)
systemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemReset.setStatus("current")
_SystemSaveCnfg_Type = CommandValue
_SystemSaveCnfg_Object = MibScalar
systemSaveCnfg = _SystemSaveCnfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 5),
    _SystemSaveCnfg_Type()
)
systemSaveCnfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSaveCnfg.setStatus("current")
_SystemProvChngCounter_Type = Counter32
_SystemProvChngCounter_Object = MibScalar
systemProvChngCounter = _SystemProvChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 6),
    _SystemProvChngCounter_Type()
)
systemProvChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemProvChngCounter.setStatus("current")
_SystemHClockAlarmLevel_Type = AlarmLevel
_SystemHClockAlarmLevel_Object = MibScalar
systemHClockAlarmLevel = _SystemHClockAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 7),
    _SystemHClockAlarmLevel_Type()
)
systemHClockAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemHClockAlarmLevel.setStatus("current")
_SystemFanAlarmLevel_Type = AlarmLevel
_SystemFanAlarmLevel_Object = MibScalar
systemFanAlarmLevel = _SystemFanAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 8),
    _SystemFanAlarmLevel_Type()
)
systemFanAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemFanAlarmLevel.setStatus("current")
_SystemTemperatureAlarmLevel_Type = AlarmLevel
_SystemTemperatureAlarmLevel_Object = MibScalar
systemTemperatureAlarmLevel = _SystemTemperatureAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 9),
    _SystemTemperatureAlarmLevel_Type()
)
systemTemperatureAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTemperatureAlarmLevel.setStatus("current")
_SystemACO_Type = CommandValue
_SystemACO_Object = MibScalar
systemACO = _SystemACO_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 1, 10),
    _SystemACO_Type()
)
systemACO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemACO.setStatus("current")
_C62Slot_ObjectIdentity = ObjectIdentity
c62Slot = _C62Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2)
)
_SlotTable_Object = MibTable
slotTable = _SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slotTable.setStatus("current")
_SlotEntry_Object = MibTableRow
slotEntry = _SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1)
)
slotEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
)
if mibBuilder.loadTexts:
    slotEntry.setStatus("current")


class _SlotID_Type(Integer32):
    """Custom type slotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_SlotID_Type.__name__ = "Integer32"
_SlotID_Object = MibTableColumn
slotID = _SlotID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 1),
    _SlotID_Type()
)
slotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slotID.setStatus("current")
_SlotType_Type = C6200CardType
_SlotType_Object = MibTableColumn
slotType = _SlotType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 2),
    _SlotType_Type()
)
slotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotType.setStatus("current")


class _SlotStatus_Type(Integer32):
    """Custom type slotStatus based on Integer32"""
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
        *(("empty", 1),
          ("match", 5),
          ("mismatch", 4),
          ("missing", 3),
          ("notProvisioned", 2))
    )


_SlotStatus_Type.__name__ = "Integer32"
_SlotStatus_Object = MibTableColumn
slotStatus = _SlotStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 3),
    _SlotStatus_Type()
)
slotStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotStatus.setStatus("current")
_SlotSwVersion_Type = Integer32
_SlotSwVersion_Object = MibTableColumn
slotSwVersion = _SlotSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 4),
    _SlotSwVersion_Type()
)
slotSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSwVersion.setStatus("current")
_SlotAlarmLevelChngCounter_Type = Counter32
_SlotAlarmLevelChngCounter_Object = MibTableColumn
slotAlarmLevelChngCounter = _SlotAlarmLevelChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 5),
    _SlotAlarmLevelChngCounter_Type()
)
slotAlarmLevelChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAlarmLevelChngCounter.setStatus("current")
_SlotCnfType_Type = C6200CardType
_SlotCnfType_Object = MibTableColumn
slotCnfType = _SlotCnfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 6),
    _SlotCnfType_Type()
)
slotCnfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slotCnfType.setStatus("current")
_SlotSubscriberChngCounter_Type = Counter32
_SlotSubscriberChngCounter_Object = MibTableColumn
slotSubscriberChngCounter = _SlotSubscriberChngCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 7),
    _SlotSubscriberChngCounter_Type()
)
slotSubscriberChngCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotSubscriberChngCounter.setStatus("current")
_SlotAlarmLevel_Type = AlarmLevel
_SlotAlarmLevel_Object = MibTableColumn
slotAlarmLevel = _SlotAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 1, 1, 8),
    _SlotAlarmLevel_Type()
)
slotAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slotAlarmLevel.setStatus("current")


class _PortID_Type(Integer32):
    """Custom type portID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PortID_Type.__name__ = "Integer32"
_PortID_Object = MibScalar
portID = _PortID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 2, 2),
    _PortID_Type()
)
portID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portID.setStatus("current")
_C62OCInterface_ObjectIdentity = ObjectIdentity
c62OCInterface = _C62OCInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3)
)
_OCInterfaceTable_Object = MibTable
oCInterfaceTable = _OCInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1)
)
if mibBuilder.loadTexts:
    oCInterfaceTable.setStatus("current")
_OCInterfaceEntry_Object = MibTableRow
oCInterfaceEntry = _OCInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1)
)
oCInterfaceEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    oCInterfaceEntry.setStatus("current")
_OCIAlarmLevel_Type = AlarmLevel
_OCIAlarmLevel_Object = MibTableColumn
oCIAlarmLevel = _OCIAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 2),
    _OCIAlarmLevel_Type()
)
oCIAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIAlarmLevel.setStatus("current")
_OCIEQF_Type = AlarmLevel
_OCIEQF_Object = MibTableColumn
oCIEQF = _OCIEQF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 3),
    _OCIEQF_Type()
)
oCIEQF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIEQF.setStatus("current")
_OCILOS_Type = AlarmLevel
_OCILOS_Object = MibTableColumn
oCILOS = _OCILOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 4),
    _OCILOS_Type()
)
oCILOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOS.setStatus("current")
_OCILOF_Type = AlarmLevel
_OCILOF_Object = MibTableColumn
oCILOF = _OCILOF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 5),
    _OCILOF_Type()
)
oCILOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOF.setStatus("current")
_OCILAIS_Type = AlarmLevel
_OCILAIS_Object = MibTableColumn
oCILAIS = _OCILAIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 6),
    _OCILAIS_Type()
)
oCILAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILAIS.setStatus("current")
_OCILOP_Type = AlarmLevel
_OCILOP_Object = MibTableColumn
oCILOP = _OCILOP_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 7),
    _OCILOP_Type()
)
oCILOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOP.setStatus("current")
_OCIPAIS_Type = AlarmLevel
_OCIPAIS_Object = MibTableColumn
oCIPAIS = _OCIPAIS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 8),
    _OCIPAIS_Type()
)
oCIPAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIPAIS.setStatus("current")
_OCISLM_Type = AlarmLevel
_OCISLM_Object = MibTableColumn
oCISLM = _OCISLM_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 9),
    _OCISLM_Type()
)
oCISLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCISLM.setStatus("current")
_OCILRFI_Type = AlarmLevel
_OCILRFI_Object = MibTableColumn
oCILRFI = _OCILRFI_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 10),
    _OCILRFI_Type()
)
oCILRFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILRFI.setStatus("current")
_OCIPRFI_Type = AlarmLevel
_OCIPRFI_Object = MibTableColumn
oCIPRFI = _OCIPRFI_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 11),
    _OCIPRFI_Type()
)
oCIPRFI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCIPRFI.setStatus("current")
_OCILOST_Type = AlarmLevel
_OCILOST_Object = MibTableColumn
oCILOST = _OCILOST_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 12),
    _OCILOST_Type()
)
oCILOST.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOST.setStatus("current")
_OCILOCD_Type = AlarmLevel
_OCILOCD_Object = MibTableColumn
oCILOCD = _OCILOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 13),
    _OCILOCD_Type()
)
oCILOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCILOCD.setStatus("current")


class _OCILoopMode_Type(Integer32):
    """Custom type oCILoopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_OCILoopMode_Type.__name__ = "Integer32"
_OCILoopMode_Object = MibTableColumn
oCILoopMode = _OCILoopMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 1, 1, 14),
    _OCILoopMode_Type()
)
oCILoopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oCILoopMode.setStatus("current")
_OCPerfTable_Object = MibTable
oCPerfTable = _OCPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2)
)
if mibBuilder.loadTexts:
    oCPerfTable.setStatus("current")
_OCPerfEntry_Object = MibTableRow
oCPerfEntry = _OCPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1)
)
oCPerfEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    oCPerfEntry.setStatus("current")
_OCPTxCellCount_Type = Counter32
_OCPTxCellCount_Object = MibTableColumn
oCPTxCellCount = _OCPTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 1),
    _OCPTxCellCount_Type()
)
oCPTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPTxCellCount.setStatus("current")
_OCPRxCellCount_Type = Counter32
_OCPRxCellCount_Object = MibTableColumn
oCPRxCellCount = _OCPRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 2),
    _OCPRxCellCount_Type()
)
oCPRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPRxCellCount.setStatus("current")
_OCPHecErrCount_Type = Counter32
_OCPHecErrCount_Object = MibTableColumn
oCPHecErrCount = _OCPHecErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 3, 2, 1, 3),
    _OCPHecErrCount_Type()
)
oCPHecErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oCPHecErrCount.setStatus("current")
_C62LineInterface_ObjectIdentity = ObjectIdentity
c62LineInterface = _C62LineInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4)
)
_LineInterfaceTable_Object = MibTable
lineInterfaceTable = _LineInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lineInterfaceTable.setStatus("current")
_LineInterfaceEntry_Object = MibTableRow
lineInterfaceEntry = _LineInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1)
)
lineInterfaceEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    lineInterfaceEntry.setStatus("current")
_LineAlarmLevel_Type = AlarmLevel
_LineAlarmLevel_Object = MibTableColumn
lineAlarmLevel = _LineAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 1),
    _LineAlarmLevel_Type()
)
lineAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineAlarmLevel.setStatus("current")
_LineDwnSNRMargin_Type = Integer32
_LineDwnSNRMargin_Object = MibTableColumn
lineDwnSNRMargin = _LineDwnSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 2),
    _LineDwnSNRMargin_Type()
)
lineDwnSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnSNRMargin.setStatus("current")
if mibBuilder.loadTexts:
    lineDwnSNRMargin.setUnits("dB")
_LineDwnLOCD_Type = AlarmLevel
_LineDwnLOCD_Object = MibTableColumn
lineDwnLOCD = _LineDwnLOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 3),
    _LineDwnLOCD_Type()
)
lineDwnLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnLOCD.setStatus("deprecated")
_LineDwnErrSecs_Type = Counter32
_LineDwnErrSecs_Object = MibTableColumn
lineDwnErrSecs = _LineDwnErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 4),
    _LineDwnErrSecs_Type()
)
lineDwnErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnErrSecs.setStatus("current")
_LineDwnLineRate_Type = Gauge32
_LineDwnLineRate_Object = MibTableColumn
lineDwnLineRate = _LineDwnLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 5),
    _LineDwnLineRate_Type()
)
lineDwnLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDwnLineRate.setStatus("current")
if mibBuilder.loadTexts:
    lineDwnLineRate.setUnits("kbps")
_LineUpSNRMargin_Type = Integer32
_LineUpSNRMargin_Object = MibTableColumn
lineUpSNRMargin = _LineUpSNRMargin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 6),
    _LineUpSNRMargin_Type()
)
lineUpSNRMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpSNRMargin.setStatus("current")
if mibBuilder.loadTexts:
    lineUpSNRMargin.setUnits("dB")
_LineUpLOCD_Type = AlarmLevel
_LineUpLOCD_Object = MibTableColumn
lineUpLOCD = _LineUpLOCD_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 7),
    _LineUpLOCD_Type()
)
lineUpLOCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpLOCD.setStatus("current")
_LineUpErrSecs_Type = Counter32
_LineUpErrSecs_Object = MibTableColumn
lineUpErrSecs = _LineUpErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 8),
    _LineUpErrSecs_Type()
)
lineUpErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpErrSecs.setStatus("current")
_LineUpLineRate_Type = Gauge32
_LineUpLineRate_Object = MibTableColumn
lineUpLineRate = _LineUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 9),
    _LineUpLineRate_Type()
)
lineUpLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineUpLineRate.setStatus("current")
if mibBuilder.loadTexts:
    lineUpLineRate.setUnits("kbps")


class _LineRateAlarm_Type(Integer32):
    """Custom type lineRateAlarm based on Integer32"""
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
          ("downAndUp", 4),
          ("ok", 1),
          ("up", 3))
    )


_LineRateAlarm_Type.__name__ = "Integer32"
_LineRateAlarm_Object = MibTableColumn
lineRateAlarm = _LineRateAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 10),
    _LineRateAlarm_Type()
)
lineRateAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineRateAlarm.setStatus("current")


class _LineMode_Type(Integer32):
    """Custom type lineMode based on Integer32"""
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
          ("down", 4),
          ("testing", 1),
          ("training", 2))
    )


_LineMode_Type.__name__ = "Integer32"
_LineMode_Object = MibTableColumn
lineMode = _LineMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 11),
    _LineMode_Type()
)
lineMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineMode.setStatus("current")
_LineDMTDwnAttenuation_Type = Gauge32
_LineDMTDwnAttenuation_Object = MibTableColumn
lineDMTDwnAttenuation = _LineDMTDwnAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 12),
    _LineDMTDwnAttenuation_Type()
)
lineDMTDwnAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    lineDMTDwnAttenuation.setUnits("dB")
_LineDMTUpAttenuation_Type = Gauge32
_LineDMTUpAttenuation_Object = MibTableColumn
lineDMTUpAttenuation = _LineDMTUpAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 13),
    _LineDMTUpAttenuation_Type()
)
lineDMTUpAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    lineDMTUpAttenuation.setUnits("dB")
_LineDMTDwnLPR_Type = AlarmLevel
_LineDMTDwnLPR_Object = MibTableColumn
lineDMTDwnLPR = _LineDMTDwnLPR_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 14),
    _LineDMTDwnLPR_Type()
)
lineDMTDwnLPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnLPR.setStatus("current")
_LineDMTUpLOS_Type = AlarmLevel
_LineDMTUpLOS_Object = MibTableColumn
lineDMTUpLOS = _LineDMTUpLOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 15),
    _LineDMTUpLOS_Type()
)
lineDMTUpLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOS.setStatus("current")
_LineDMTUpLOF_Type = AlarmLevel
_LineDMTUpLOF_Object = MibTableColumn
lineDMTUpLOF = _LineDMTUpLOF_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 16),
    _LineDMTUpLOF_Type()
)
lineDMTUpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOF.setStatus("current")


class _LineDMTLoopback_Type(Integer32):
    """Custom type lineDMTLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dslline", 2),
          ("local", 3),
          ("none", 1))
    )


_LineDMTLoopback_Type.__name__ = "Integer32"
_LineDMTLoopback_Object = MibTableColumn
lineDMTLoopback = _LineDMTLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 1, 1, 17),
    _LineDMTLoopback_Type()
)
lineDMTLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineDMTLoopback.setStatus("current")
_LinePerfTable_Object = MibTable
linePerfTable = _LinePerfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    linePerfTable.setStatus("current")
_LinePerfEntry_Object = MibTableRow
linePerfEntry = _LinePerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1)
)
linePerfEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    linePerfEntry.setStatus("current")
_LineTxCellCount_Type = Counter32
_LineTxCellCount_Object = MibTableColumn
lineTxCellCount = _LineTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 1),
    _LineTxCellCount_Type()
)
lineTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTxCellCount.setStatus("current")
_LineRxCellCount_Type = Counter32
_LineRxCellCount_Object = MibTableColumn
lineRxCellCount = _LineRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 2),
    _LineRxCellCount_Type()
)
lineRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineRxCellCount.setStatus("current")
_LineHecErrCount_Type = Counter32
_LineHecErrCount_Object = MibTableColumn
lineHecErrCount = _LineHecErrCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 3),
    _LineHecErrCount_Type()
)
lineHecErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineHecErrCount.setStatus("current")
_LineDMTDwnFECCount_Type = Counter32
_LineDMTDwnFECCount_Object = MibTableColumn
lineDMTDwnFECCount = _LineDMTDwnFECCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 4),
    _LineDMTDwnFECCount_Type()
)
lineDMTDwnFECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnFECCount.setStatus("current")
_LineDMTUpFECCount_Type = Counter32
_LineDMTUpFECCount_Object = MibTableColumn
lineDMTUpFECCount = _LineDMTUpFECCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 5),
    _LineDMTUpFECCount_Type()
)
lineDMTUpFECCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpFECCount.setStatus("current")
_LineDMTDwnCRCCount_Type = Counter32
_LineDMTDwnCRCCount_Object = MibTableColumn
lineDMTDwnCRCCount = _LineDMTDwnCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 6),
    _LineDMTDwnCRCCount_Type()
)
lineDMTDwnCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnCRCCount.setStatus("current")
_LineDMTUpCRCCount_Type = Counter32
_LineDMTUpCRCCount_Object = MibTableColumn
lineDMTUpCRCCount = _LineDMTUpCRCCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 7),
    _LineDMTUpCRCCount_Type()
)
lineDMTUpCRCCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpCRCCount.setStatus("current")
_LineDMTDwnLOSCount_Type = Counter32
_LineDMTDwnLOSCount_Object = MibTableColumn
lineDMTDwnLOSCount = _LineDMTDwnLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 8),
    _LineDMTDwnLOSCount_Type()
)
lineDMTDwnLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnLOSCount.setStatus("current")
_LineDMTUpLOSCount_Type = Counter32
_LineDMTUpLOSCount_Object = MibTableColumn
lineDMTUpLOSCount = _LineDMTUpLOSCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 9),
    _LineDMTUpLOSCount_Type()
)
lineDMTUpLOSCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpLOSCount.setStatus("current")
_LineDMTDwnSEFCount_Type = Counter32
_LineDMTDwnSEFCount_Object = MibTableColumn
lineDMTDwnSEFCount = _LineDMTDwnSEFCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 10),
    _LineDMTDwnSEFCount_Type()
)
lineDMTDwnSEFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTDwnSEFCount.setStatus("current")
_LineDMTUpRDICount_Type = Counter32
_LineDMTUpRDICount_Object = MibTableColumn
lineDMTUpRDICount = _LineDMTUpRDICount_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 2, 1, 11),
    _LineDMTUpRDICount_Type()
)
lineDMTUpRDICount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineDMTUpRDICount.setStatus("current")
_LineTestTable_Object = MibTable
lineTestTable = _LineTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lineTestTable.setStatus("current")
_LineTestEntry_Object = MibTableRow
lineTestEntry = _LineTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1)
)
lineTestEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    lineTestEntry.setStatus("current")


class _LineTestTrigger_Type(Integer32):
    """Custom type lineTestTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 3),
          ("start", 2),
          ("stop", 1))
    )


_LineTestTrigger_Type.__name__ = "Integer32"
_LineTestTrigger_Object = MibTableColumn
lineTestTrigger = _LineTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 1),
    _LineTestTrigger_Type()
)
lineTestTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestTrigger.setStatus("current")
_LineTestType_Type = TestType
_LineTestType_Object = MibTableColumn
lineTestType = _LineTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 2),
    _LineTestType_Type()
)
lineTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestType.setStatus("current")


class _LineTestTimeIntvl_Type(Integer32):
    """Custom type lineTestTimeIntvl based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_LineTestTimeIntvl_Type.__name__ = "Integer32"
_LineTestTimeIntvl_Object = MibTableColumn
lineTestTimeIntvl = _LineTestTimeIntvl_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 3),
    _LineTestTimeIntvl_Type()
)
lineTestTimeIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestTimeIntvl.setStatus("current")
if mibBuilder.loadTexts:
    lineTestTimeIntvl.setUnits("minutes")
_LineTestStatus_Type = TestStatus
_LineTestStatus_Object = MibTableColumn
lineTestStatus = _LineTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 4),
    _LineTestStatus_Type()
)
lineTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestStatus.setStatus("current")
_LineTestDwnBitErrRate_Type = Integer32
_LineTestDwnBitErrRate_Object = MibTableColumn
lineTestDwnBitErrRate = _LineTestDwnBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 5),
    _LineTestDwnBitErrRate_Type()
)
lineTestDwnBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestDwnBitErrRate.setStatus("current")
_LineTestUpBitErrRate_Type = Integer32
_LineTestUpBitErrRate_Object = MibTableColumn
lineTestUpBitErrRate = _LineTestUpBitErrRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 6),
    _LineTestUpBitErrRate_Type()
)
lineTestUpBitErrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestUpBitErrRate.setStatus("current")
_LineTestStartTime_Type = DateAndTime
_LineTestStartTime_Object = MibTableColumn
lineTestStartTime = _LineTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 7),
    _LineTestStartTime_Type()
)
lineTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestStartTime.setStatus("current")
_LineTestCmplTime_Type = DateAndTime
_LineTestCmplTime_Object = MibTableColumn
lineTestCmplTime = _LineTestCmplTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 8),
    _LineTestCmplTime_Type()
)
lineTestCmplTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineTestCmplTime.setStatus("current")


class _LineTestBitErrRateLimit_Type(Integer32):
    """Custom type lineTestBitErrRateLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 10),
    )


_LineTestBitErrRateLimit_Type.__name__ = "Integer32"
_LineTestBitErrRateLimit_Object = MibTableColumn
lineTestBitErrRateLimit = _LineTestBitErrRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 4, 3, 1, 9),
    _LineTestBitErrRateLimit_Type()
)
lineTestBitErrRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineTestBitErrRateLimit.setStatus("current")
_C62Subscriber_ObjectIdentity = ObjectIdentity
c62Subscriber = _C62Subscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5)
)
_SubscriberTable_Object = MibTable
subscriberTable = _SubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1)
)
if mibBuilder.loadTexts:
    subscriberTable.setStatus("current")
_SubscriberEntry_Object = MibTableRow
subscriberEntry = _SubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1)
)
subscriberEntry.setIndexNames(
    (0, "CISCO-6200-MIB", "slotID"),
    (0, "CISCO-6200-MIB", "portID"),
)
if mibBuilder.loadTexts:
    subscriberEntry.setStatus("current")


class _SubscriberName_Type(DisplayString):
    """Custom type subscriberName based on DisplayString"""
    defaultValue = OctetString("DSL<slotID>/<portID>")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SubscriberName_Type.__name__ = "DisplayString"
_SubscriberName_Object = MibTableColumn
subscriberName = _SubscriberName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 1),
    _SubscriberName_Type()
)
subscriberName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberName.setStatus("current")
_SubscriberUpLineRate_Type = Integer32
_SubscriberUpLineRate_Object = MibTableColumn
subscriberUpLineRate = _SubscriberUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 2),
    _SubscriberUpLineRate_Type()
)
subscriberUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberUpLineRate.setStatus("current")
if mibBuilder.loadTexts:
    subscriberUpLineRate.setUnits("kbps")
_SubscriberDwnLineRate_Type = Integer32
_SubscriberDwnLineRate_Object = MibTableColumn
subscriberDwnLineRate = _SubscriberDwnLineRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 3),
    _SubscriberDwnLineRate_Type()
)
subscriberDwnLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberDwnLineRate.setStatus("current")
if mibBuilder.loadTexts:
    subscriberDwnLineRate.setUnits("kbps")


class _SubscriberLineState_Type(InterfaceStatus):
    """Custom type subscriberLineState based on InterfaceStatus"""


_SubscriberLineState_Object = MibTableColumn
subscriberLineState = _SubscriberLineState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 4),
    _SubscriberLineState_Type()
)
subscriberLineState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberLineState.setStatus("current")


class _SubscriberDMTLOSConfig_Type(InterfaceStatus):
    """Custom type subscriberDMTLOSConfig based on InterfaceStatus"""


_SubscriberDMTLOSConfig_Object = MibTableColumn
subscriberDMTLOSConfig = _SubscriberDMTLOSConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 1, 5, 1, 1, 5),
    _SubscriberDMTLOSConfig_Type()
)
subscriberDMTLOSConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberDMTLOSConfig.setStatus("current")
_CiscoC6200MIBConformance_ObjectIdentity = ObjectIdentity
ciscoC6200MIBConformance = _CiscoC6200MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2)
)
_CiscoC6200MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoC6200MIBCompliances = _CiscoC6200MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1)
)
_CiscoC6200MIBGroups_ObjectIdentity = ObjectIdentity
ciscoC6200MIBGroups = _CiscoC6200MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2)
)

# Managed Objects groups

ciscoC6200SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 1)
)
ciscoC6200SystemGroup.setObjects(
      *(("CISCO-6200-MIB", "systemType"),
        ("CISCO-6200-MIB", "systemAlarmLevel"),
        ("CISCO-6200-MIB", "systemAlarmLevelChngCounter"),
        ("CISCO-6200-MIB", "systemReset"),
        ("CISCO-6200-MIB", "systemSaveCnfg"),
        ("CISCO-6200-MIB", "systemProvChngCounter"),
        ("CISCO-6200-MIB", "systemHClockAlarmLevel"),
        ("CISCO-6200-MIB", "systemFanAlarmLevel"),
        ("CISCO-6200-MIB", "systemTemperatureAlarmLevel"),
        ("CISCO-6200-MIB", "systemACO"))
)
if mibBuilder.loadTexts:
    ciscoC6200SystemGroup.setStatus("obsolete")

ciscoC6200SlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 2)
)
ciscoC6200SlotGroup.setObjects(
      *(("CISCO-6200-MIB", "slotType"),
        ("CISCO-6200-MIB", "slotStatus"),
        ("CISCO-6200-MIB", "slotSwVersion"),
        ("CISCO-6200-MIB", "slotAlarmLevelChngCounter"),
        ("CISCO-6200-MIB", "slotCnfType"),
        ("CISCO-6200-MIB", "slotSubscriberChngCounter"),
        ("CISCO-6200-MIB", "slotAlarmLevel"))
)
if mibBuilder.loadTexts:
    ciscoC6200SlotGroup.setStatus("obsolete")

ciscoC6200oCIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 3)
)
ciscoC6200oCIGroup.setObjects(
      *(("CISCO-6200-MIB", "oCIAlarmLevel"),
        ("CISCO-6200-MIB", "oCIEQF"),
        ("CISCO-6200-MIB", "oCILOS"),
        ("CISCO-6200-MIB", "oCILOF"),
        ("CISCO-6200-MIB", "oCILAIS"),
        ("CISCO-6200-MIB", "oCILOP"),
        ("CISCO-6200-MIB", "oCIPAIS"),
        ("CISCO-6200-MIB", "oCISLM"),
        ("CISCO-6200-MIB", "oCILRFI"),
        ("CISCO-6200-MIB", "oCIPRFI"),
        ("CISCO-6200-MIB", "oCILOST"),
        ("CISCO-6200-MIB", "oCILOCD"),
        ("CISCO-6200-MIB", "oCILoopMode"))
)
if mibBuilder.loadTexts:
    ciscoC6200oCIGroup.setStatus("obsolete")

ciscoC6200oCIPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 4)
)
ciscoC6200oCIPerfGroup.setObjects(
      *(("CISCO-6200-MIB", "oCPTxCellCount"),
        ("CISCO-6200-MIB", "oCPRxCellCount"),
        ("CISCO-6200-MIB", "oCPHecErrCount"))
)
if mibBuilder.loadTexts:
    ciscoC6200oCIPerfGroup.setStatus("obsolete")

ciscoC6200lineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 5)
)
ciscoC6200lineGroup.setObjects(
      *(("CISCO-6200-MIB", "lineAlarmLevel"),
        ("CISCO-6200-MIB", "lineDwnSNRMargin"),
        ("CISCO-6200-MIB", "lineDwnLOCD"),
        ("CISCO-6200-MIB", "lineDwnErrSecs"),
        ("CISCO-6200-MIB", "lineDwnLineRate"),
        ("CISCO-6200-MIB", "lineUpSNRMargin"),
        ("CISCO-6200-MIB", "lineUpLOCD"),
        ("CISCO-6200-MIB", "lineUpErrSecs"),
        ("CISCO-6200-MIB", "lineUpLineRate"),
        ("CISCO-6200-MIB", "lineRateAlarm"),
        ("CISCO-6200-MIB", "lineMode"))
)
if mibBuilder.loadTexts:
    ciscoC6200lineGroup.setStatus("obsolete")

ciscoC6200linePerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 6)
)
ciscoC6200linePerfGroup.setObjects(
      *(("CISCO-6200-MIB", "lineTxCellCount"),
        ("CISCO-6200-MIB", "lineRxCellCount"),
        ("CISCO-6200-MIB", "lineHecErrCount"))
)
if mibBuilder.loadTexts:
    ciscoC6200linePerfGroup.setStatus("obsolete")

ciscoC6200lineTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 7)
)
ciscoC6200lineTestGroup.setObjects(
      *(("CISCO-6200-MIB", "lineTestTrigger"),
        ("CISCO-6200-MIB", "lineTestType"),
        ("CISCO-6200-MIB", "lineTestTimeIntvl"),
        ("CISCO-6200-MIB", "lineTestStatus"),
        ("CISCO-6200-MIB", "lineTestDwnBitErrRate"),
        ("CISCO-6200-MIB", "lineTestUpBitErrRate"),
        ("CISCO-6200-MIB", "lineTestStartTime"),
        ("CISCO-6200-MIB", "lineTestCmplTime"),
        ("CISCO-6200-MIB", "lineTestBitErrRateLimit"))
)
if mibBuilder.loadTexts:
    ciscoC6200lineTestGroup.setStatus("obsolete")

ciscoC6200subscriberGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 8)
)
ciscoC6200subscriberGroup.setObjects(
      *(("CISCO-6200-MIB", "subscriberName"),
        ("CISCO-6200-MIB", "subscriberUpLineRate"),
        ("CISCO-6200-MIB", "subscriberDwnLineRate"),
        ("CISCO-6200-MIB", "subscriberLineState"))
)
if mibBuilder.loadTexts:
    ciscoC6200subscriberGroup.setStatus("obsolete")

ciscoC6200SystemGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 9)
)
ciscoC6200SystemGroup2.setObjects(
      *(("CISCO-6200-MIB", "systemType"),
        ("CISCO-6200-MIB", "systemAlarmLevel"),
        ("CISCO-6200-MIB", "systemAlarmLevelChngCounter"),
        ("CISCO-6200-MIB", "systemReset"),
        ("CISCO-6200-MIB", "systemSaveCnfg"),
        ("CISCO-6200-MIB", "systemProvChngCounter"),
        ("CISCO-6200-MIB", "systemHClockAlarmLevel"),
        ("CISCO-6200-MIB", "systemFanAlarmLevel"),
        ("CISCO-6200-MIB", "systemTemperatureAlarmLevel"),
        ("CISCO-6200-MIB", "systemACO"))
)
if mibBuilder.loadTexts:
    ciscoC6200SystemGroup2.setStatus("current")

ciscoC6200SlotGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 10)
)
ciscoC6200SlotGroup2.setObjects(
      *(("CISCO-6200-MIB", "slotType"),
        ("CISCO-6200-MIB", "slotStatus"),
        ("CISCO-6200-MIB", "slotSwVersion"),
        ("CISCO-6200-MIB", "slotAlarmLevelChngCounter"),
        ("CISCO-6200-MIB", "slotCnfType"),
        ("CISCO-6200-MIB", "slotSubscriberChngCounter"),
        ("CISCO-6200-MIB", "slotAlarmLevel"))
)
if mibBuilder.loadTexts:
    ciscoC6200SlotGroup2.setStatus("current")

ciscoC6200oCIGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 11)
)
ciscoC6200oCIGroup2.setObjects(
      *(("CISCO-6200-MIB", "oCIAlarmLevel"),
        ("CISCO-6200-MIB", "oCIEQF"),
        ("CISCO-6200-MIB", "oCILOS"),
        ("CISCO-6200-MIB", "oCILOF"),
        ("CISCO-6200-MIB", "oCILAIS"),
        ("CISCO-6200-MIB", "oCILOP"),
        ("CISCO-6200-MIB", "oCIPAIS"),
        ("CISCO-6200-MIB", "oCISLM"),
        ("CISCO-6200-MIB", "oCILRFI"),
        ("CISCO-6200-MIB", "oCIPRFI"),
        ("CISCO-6200-MIB", "oCILOST"),
        ("CISCO-6200-MIB", "oCILOCD"),
        ("CISCO-6200-MIB", "oCILoopMode"))
)
if mibBuilder.loadTexts:
    ciscoC6200oCIGroup2.setStatus("current")

ciscoC6200oCIPerfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 12)
)
ciscoC6200oCIPerfGroup2.setObjects(
      *(("CISCO-6200-MIB", "oCPTxCellCount"),
        ("CISCO-6200-MIB", "oCPRxCellCount"),
        ("CISCO-6200-MIB", "oCPHecErrCount"))
)
if mibBuilder.loadTexts:
    ciscoC6200oCIPerfGroup2.setStatus("current")

ciscoC6200lineGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 13)
)
ciscoC6200lineGroup2.setObjects(
      *(("CISCO-6200-MIB", "lineAlarmLevel"),
        ("CISCO-6200-MIB", "lineDwnSNRMargin"),
        ("CISCO-6200-MIB", "lineDwnErrSecs"),
        ("CISCO-6200-MIB", "lineDwnLineRate"),
        ("CISCO-6200-MIB", "lineUpSNRMargin"),
        ("CISCO-6200-MIB", "lineUpLOCD"),
        ("CISCO-6200-MIB", "lineUpErrSecs"),
        ("CISCO-6200-MIB", "lineUpLineRate"),
        ("CISCO-6200-MIB", "lineRateAlarm"),
        ("CISCO-6200-MIB", "lineMode"),
        ("CISCO-6200-MIB", "lineDMTDwnAttenuation"),
        ("CISCO-6200-MIB", "lineDMTUpAttenuation"),
        ("CISCO-6200-MIB", "lineDMTDwnLPR"),
        ("CISCO-6200-MIB", "lineDMTUpLOS"),
        ("CISCO-6200-MIB", "lineDMTUpLOF"),
        ("CISCO-6200-MIB", "lineDMTLoopback"))
)
if mibBuilder.loadTexts:
    ciscoC6200lineGroup2.setStatus("current")

ciscoC6200linePerfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 14)
)
ciscoC6200linePerfGroup2.setObjects(
      *(("CISCO-6200-MIB", "lineTxCellCount"),
        ("CISCO-6200-MIB", "lineRxCellCount"),
        ("CISCO-6200-MIB", "lineHecErrCount"),
        ("CISCO-6200-MIB", "lineDMTDwnFECCount"),
        ("CISCO-6200-MIB", "lineDMTUpFECCount"),
        ("CISCO-6200-MIB", "lineDMTDwnCRCCount"),
        ("CISCO-6200-MIB", "lineDMTUpCRCCount"),
        ("CISCO-6200-MIB", "lineDMTDwnLOSCount"),
        ("CISCO-6200-MIB", "lineDMTUpLOSCount"),
        ("CISCO-6200-MIB", "lineDMTDwnSEFCount"),
        ("CISCO-6200-MIB", "lineDMTUpRDICount"))
)
if mibBuilder.loadTexts:
    ciscoC6200linePerfGroup2.setStatus("current")

ciscoC6200lineTestGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 15)
)
ciscoC6200lineTestGroup2.setObjects(
      *(("CISCO-6200-MIB", "lineTestTrigger"),
        ("CISCO-6200-MIB", "lineTestType"),
        ("CISCO-6200-MIB", "lineTestTimeIntvl"),
        ("CISCO-6200-MIB", "lineTestStatus"),
        ("CISCO-6200-MIB", "lineTestDwnBitErrRate"),
        ("CISCO-6200-MIB", "lineTestUpBitErrRate"),
        ("CISCO-6200-MIB", "lineTestStartTime"),
        ("CISCO-6200-MIB", "lineTestCmplTime"),
        ("CISCO-6200-MIB", "lineTestBitErrRateLimit"))
)
if mibBuilder.loadTexts:
    ciscoC6200lineTestGroup2.setStatus("current")

ciscoC6200subscriberGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 2, 16)
)
ciscoC6200subscriberGroup2.setObjects(
      *(("CISCO-6200-MIB", "subscriberName"),
        ("CISCO-6200-MIB", "subscriberUpLineRate"),
        ("CISCO-6200-MIB", "subscriberDwnLineRate"),
        ("CISCO-6200-MIB", "subscriberLineState"),
        ("CISCO-6200-MIB", "subscriberDMTLOSConfig"))
)
if mibBuilder.loadTexts:
    ciscoC6200subscriberGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoC6200MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoC6200MIBCompliance.setStatus(
        "obsolete"
    )

ciscoC6200MIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 26, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoC6200MIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-6200-MIB",
    **{"C6200CardType": C6200CardType,
       "CommandValue": CommandValue,
       "AlarmLevel": AlarmLevel,
       "InterfaceStatus": InterfaceStatus,
       "TestStatus": TestStatus,
       "TestType": TestType,
       "cisco6200MIB": cisco6200MIB,
       "cisco6200MibObjects": cisco6200MibObjects,
       "c62System": c62System,
       "systemType": systemType,
       "systemAlarmLevel": systemAlarmLevel,
       "systemAlarmLevelChngCounter": systemAlarmLevelChngCounter,
       "systemReset": systemReset,
       "systemSaveCnfg": systemSaveCnfg,
       "systemProvChngCounter": systemProvChngCounter,
       "systemHClockAlarmLevel": systemHClockAlarmLevel,
       "systemFanAlarmLevel": systemFanAlarmLevel,
       "systemTemperatureAlarmLevel": systemTemperatureAlarmLevel,
       "systemACO": systemACO,
       "c62Slot": c62Slot,
       "slotTable": slotTable,
       "slotEntry": slotEntry,
       "slotID": slotID,
       "slotType": slotType,
       "slotStatus": slotStatus,
       "slotSwVersion": slotSwVersion,
       "slotAlarmLevelChngCounter": slotAlarmLevelChngCounter,
       "slotCnfType": slotCnfType,
       "slotSubscriberChngCounter": slotSubscriberChngCounter,
       "slotAlarmLevel": slotAlarmLevel,
       "portID": portID,
       "c62OCInterface": c62OCInterface,
       "oCInterfaceTable": oCInterfaceTable,
       "oCInterfaceEntry": oCInterfaceEntry,
       "oCIAlarmLevel": oCIAlarmLevel,
       "oCIEQF": oCIEQF,
       "oCILOS": oCILOS,
       "oCILOF": oCILOF,
       "oCILAIS": oCILAIS,
       "oCILOP": oCILOP,
       "oCIPAIS": oCIPAIS,
       "oCISLM": oCISLM,
       "oCILRFI": oCILRFI,
       "oCIPRFI": oCIPRFI,
       "oCILOST": oCILOST,
       "oCILOCD": oCILOCD,
       "oCILoopMode": oCILoopMode,
       "oCPerfTable": oCPerfTable,
       "oCPerfEntry": oCPerfEntry,
       "oCPTxCellCount": oCPTxCellCount,
       "oCPRxCellCount": oCPRxCellCount,
       "oCPHecErrCount": oCPHecErrCount,
       "c62LineInterface": c62LineInterface,
       "lineInterfaceTable": lineInterfaceTable,
       "lineInterfaceEntry": lineInterfaceEntry,
       "lineAlarmLevel": lineAlarmLevel,
       "lineDwnSNRMargin": lineDwnSNRMargin,
       "lineDwnLOCD": lineDwnLOCD,
       "lineDwnErrSecs": lineDwnErrSecs,
       "lineDwnLineRate": lineDwnLineRate,
       "lineUpSNRMargin": lineUpSNRMargin,
       "lineUpLOCD": lineUpLOCD,
       "lineUpErrSecs": lineUpErrSecs,
       "lineUpLineRate": lineUpLineRate,
       "lineRateAlarm": lineRateAlarm,
       "lineMode": lineMode,
       "lineDMTDwnAttenuation": lineDMTDwnAttenuation,
       "lineDMTUpAttenuation": lineDMTUpAttenuation,
       "lineDMTDwnLPR": lineDMTDwnLPR,
       "lineDMTUpLOS": lineDMTUpLOS,
       "lineDMTUpLOF": lineDMTUpLOF,
       "lineDMTLoopback": lineDMTLoopback,
       "linePerfTable": linePerfTable,
       "linePerfEntry": linePerfEntry,
       "lineTxCellCount": lineTxCellCount,
       "lineRxCellCount": lineRxCellCount,
       "lineHecErrCount": lineHecErrCount,
       "lineDMTDwnFECCount": lineDMTDwnFECCount,
       "lineDMTUpFECCount": lineDMTUpFECCount,
       "lineDMTDwnCRCCount": lineDMTDwnCRCCount,
       "lineDMTUpCRCCount": lineDMTUpCRCCount,
       "lineDMTDwnLOSCount": lineDMTDwnLOSCount,
       "lineDMTUpLOSCount": lineDMTUpLOSCount,
       "lineDMTDwnSEFCount": lineDMTDwnSEFCount,
       "lineDMTUpRDICount": lineDMTUpRDICount,
       "lineTestTable": lineTestTable,
       "lineTestEntry": lineTestEntry,
       "lineTestTrigger": lineTestTrigger,
       "lineTestType": lineTestType,
       "lineTestTimeIntvl": lineTestTimeIntvl,
       "lineTestStatus": lineTestStatus,
       "lineTestDwnBitErrRate": lineTestDwnBitErrRate,
       "lineTestUpBitErrRate": lineTestUpBitErrRate,
       "lineTestStartTime": lineTestStartTime,
       "lineTestCmplTime": lineTestCmplTime,
       "lineTestBitErrRateLimit": lineTestBitErrRateLimit,
       "c62Subscriber": c62Subscriber,
       "subscriberTable": subscriberTable,
       "subscriberEntry": subscriberEntry,
       "subscriberName": subscriberName,
       "subscriberUpLineRate": subscriberUpLineRate,
       "subscriberDwnLineRate": subscriberDwnLineRate,
       "subscriberLineState": subscriberLineState,
       "subscriberDMTLOSConfig": subscriberDMTLOSConfig,
       "ciscoC6200MIBConformance": ciscoC6200MIBConformance,
       "ciscoC6200MIBCompliances": ciscoC6200MIBCompliances,
       "ciscoC6200MIBCompliance": ciscoC6200MIBCompliance,
       "ciscoC6200MIBCompliance2": ciscoC6200MIBCompliance2,
       "ciscoC6200MIBGroups": ciscoC6200MIBGroups,
       "ciscoC6200SystemGroup": ciscoC6200SystemGroup,
       "ciscoC6200SlotGroup": ciscoC6200SlotGroup,
       "ciscoC6200oCIGroup": ciscoC6200oCIGroup,
       "ciscoC6200oCIPerfGroup": ciscoC6200oCIPerfGroup,
       "ciscoC6200lineGroup": ciscoC6200lineGroup,
       "ciscoC6200linePerfGroup": ciscoC6200linePerfGroup,
       "ciscoC6200lineTestGroup": ciscoC6200lineTestGroup,
       "ciscoC6200subscriberGroup": ciscoC6200subscriberGroup,
       "ciscoC6200SystemGroup2": ciscoC6200SystemGroup2,
       "ciscoC6200SlotGroup2": ciscoC6200SlotGroup2,
       "ciscoC6200oCIGroup2": ciscoC6200oCIGroup2,
       "ciscoC6200oCIPerfGroup2": ciscoC6200oCIPerfGroup2,
       "ciscoC6200lineGroup2": ciscoC6200lineGroup2,
       "ciscoC6200linePerfGroup2": ciscoC6200linePerfGroup2,
       "ciscoC6200lineTestGroup2": ciscoC6200lineTestGroup2,
       "ciscoC6200subscriberGroup2": ciscoC6200subscriberGroup2}
)
