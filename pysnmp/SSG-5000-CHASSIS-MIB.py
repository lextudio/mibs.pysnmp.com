# SNMP MIB module (SSG-5000-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SSG-5000-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:42 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(shastaExperiment,) = mibBuilder.importSymbols(
    "SHASTA-MIB",
    "shastaExperiment")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ssg5000ChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PSOperStatus(Integer32, TextualConvention):
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
        *(("diagFault", 6),
          ("empty", 2),
          ("fault", 4),
          ("ok", 3),
          ("partialFault", 5),
          ("unknown", 1))
    )



class AdminStatus(Integer32, TextualConvention):
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
        *(("adminStateAbsent", 2),
          ("adminStateDisabled", 0),
          ("adminStateEnabled", 1),
          ("adminStateStandby", 3))
    )



class OperStatus(Integer32, TextualConvention):
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
        *(("operStateAbsent", 2),
          ("operStateDown", 0),
          ("operStateStandby", 3),
          ("operStateUP", 1))
    )



class PsType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac264", 1),
          ("dc48V", 2),
          ("empty", 3))
    )



class CardType(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("cardAbsent", 0),
          ("cardTypeUnknown", 10),
          ("controlManagementCard", 1),
          ("ds3AtmLineCard", 5),
          ("ds3ChannelizedFrameCard", 11),
          ("e3AtmLineCard", 7),
          ("ethnetLineCard", 12),
          ("hsiLineCard", 6),
          ("oc12DAtmLineCard", 9),
          ("oc12SAtmLineCard", 8),
          ("oc3AtmLineCard", 4),
          ("subscriberServiceCard", 2),
          ("switchFabricCard", 3))
    )



class SystemAlarmType(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("acDcShelfFailure", 7),
          ("acDcShelfOverheat", 8),
          ("batteryFailure", 9),
          ("batteryOverheat", 10),
          ("dcPowerFailure", 6),
          ("fanDead", 3),
          ("fanFailure", 4),
          ("nodeDead", 1),
          ("nodeReboot", 2),
          ("pcmciaCardInserted", 11),
          ("pcmciaCardRemoved", 12),
          ("sysSSMsAreUp", 13),
          ("temperatureOverheat", 5))
    )



class CardAlarmType(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("cardBoot", 5),
          ("cardDead", 11),
          ("cardFailDiag", 10),
          ("cardFailed", 8),
          ("cardInserted", 2),
          ("cardMalfunction", 9),
          ("cardMismatch", 4),
          ("cardMissing", 1),
          ("cardReboot", 6),
          ("cardRemoved", 3),
          ("cardRevMismatch", 7),
          ("cardStandbyNotInRedundant", 13),
          ("cardSwitchToActive", 12))
    )



class ALCPortAlarmType(Integer32, TextualConvention):
    status = "current"
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("portDown", 2),
          ("portLAIS", 6),
          ("portLCD", 11),
          ("portLOF", 5),
          ("portLOP", 8),
          ("portLOS", 4),
          ("portLRDI", 7),
          ("portLoop", 3),
          ("portPAIS", 9),
          ("portPRDI", 10),
          ("portUp", 1))
    )



class SSMAlarmType(Integer32, TextualConvention):
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
        *(("ssmDead", 4),
          ("ssmDown", 5),
          ("ssmFailed", 1),
          ("ssmReset", 2),
          ("ssmUp", 3))
    )



class CT3PortAlarmType(Integer32, TextualConvention):
    status = "current"
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
        *(("ct3DS3AIS", 8),
          ("ct3DS3FERF", 9),
          ("ct3DS3LOS", 6),
          ("ct3DS3OOF", 7),
          ("ct3DS3RED", 10),
          ("ct3Dead", 4),
          ("ct3Down", 5),
          ("ct3Failed", 1),
          ("ct3Reset", 2),
          ("ct3Up", 3))
    )



class CT3DS2AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds2AIS", 2),
          ("ds2OOF", 1),
          ("ds2RAI", 3))
    )



class CT3DS1AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ds1AIS", 2),
          ("ds1OOF", 1),
          ("ds1RAI", 3))
    )



class ServiceAlarmSeverityType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("infomational", 1),
          ("warning", 2))
    )



class ETHPortAlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethLinkDown", 1)
    )



class ALARMStateType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 2),
          ("alarmOccur", 1))
    )



class PVCAlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("connectionDown", 1)
    )



# MIB Managed Objects in the order of their OIDs

_Ssg5000ChassisMIBObjects_ObjectIdentity = ObjectIdentity
ssg5000ChassisMIBObjects = _Ssg5000ChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1)
)
_Ssg5000ChassisGroup_ObjectIdentity = ObjectIdentity
ssg5000ChassisGroup = _Ssg5000ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1)
)
_Ssg5000SysStatus_Type = Integer32
_Ssg5000SysStatus_Object = MibScalar
ssg5000SysStatus = _Ssg5000SysStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 1),
    _Ssg5000SysStatus_Type()
)
ssg5000SysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysStatus.setStatus("current")
_Ssg5000SlotTable_Object = MibTable
ssg5000SlotTable = _Ssg5000SlotTable_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ssg5000SlotTable.setStatus("current")
_Ssg5000SlotEntry_Object = MibTableRow
ssg5000SlotEntry = _Ssg5000SlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1)
)
ssg5000SlotEntry.setIndexNames(
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
)
if mibBuilder.loadTexts:
    ssg5000SlotEntry.setStatus("current")


class _Ssg5000SlotIndex_Type(Integer32):
    """Custom type ssg5000SlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_Ssg5000SlotIndex_Type.__name__ = "Integer32"
_Ssg5000SlotIndex_Object = MibTableColumn
ssg5000SlotIndex = _Ssg5000SlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 1),
    _Ssg5000SlotIndex_Type()
)
ssg5000SlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotIndex.setStatus("current")
_Ssg5000SlotCardType_Type = CardType
_Ssg5000SlotCardType_Object = MibTableColumn
ssg5000SlotCardType = _Ssg5000SlotCardType_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 2),
    _Ssg5000SlotCardType_Type()
)
ssg5000SlotCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotCardType.setStatus("current")
_Ssg5000SlotCardDescr_Type = DisplayString
_Ssg5000SlotCardDescr_Object = MibTableColumn
ssg5000SlotCardDescr = _Ssg5000SlotCardDescr_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 3),
    _Ssg5000SlotCardDescr_Type()
)
ssg5000SlotCardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotCardDescr.setStatus("current")
_Ssg5000SlotAdminStatus_Type = AdminStatus
_Ssg5000SlotAdminStatus_Object = MibTableColumn
ssg5000SlotAdminStatus = _Ssg5000SlotAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 4),
    _Ssg5000SlotAdminStatus_Type()
)
ssg5000SlotAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotAdminStatus.setStatus("current")
_Ssg5000SlotOperStatus_Type = OperStatus
_Ssg5000SlotOperStatus_Object = MibTableColumn
ssg5000SlotOperStatus = _Ssg5000SlotOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 5),
    _Ssg5000SlotOperStatus_Type()
)
ssg5000SlotOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotOperStatus.setStatus("current")
_Ssg5000SlotCardNumPorts_Type = Integer32
_Ssg5000SlotCardNumPorts_Object = MibTableColumn
ssg5000SlotCardNumPorts = _Ssg5000SlotCardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 6),
    _Ssg5000SlotCardNumPorts_Type()
)
ssg5000SlotCardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotCardNumPorts.setStatus("current")
_Ssg5000SlotCardHwVersion_Type = DisplayString
_Ssg5000SlotCardHwVersion_Object = MibTableColumn
ssg5000SlotCardHwVersion = _Ssg5000SlotCardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 7),
    _Ssg5000SlotCardHwVersion_Type()
)
ssg5000SlotCardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotCardHwVersion.setStatus("current")
_Ssg5000SlotCardSerialNumber_Type = DisplayString
_Ssg5000SlotCardSerialNumber_Object = MibTableColumn
ssg5000SlotCardSerialNumber = _Ssg5000SlotCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 8),
    _Ssg5000SlotCardSerialNumber_Type()
)
ssg5000SlotCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotCardSerialNumber.setStatus("current")
_Ssg5000SlotAlarms_Type = Integer32
_Ssg5000SlotAlarms_Object = MibTableColumn
ssg5000SlotAlarms = _Ssg5000SlotAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 2, 1, 9),
    _Ssg5000SlotAlarms_Type()
)
ssg5000SlotAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SlotAlarms.setStatus("current")
_Ssg5000SSMStatTable_Object = MibTable
ssg5000SSMStatTable = _Ssg5000SSMStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ssg5000SSMStatTable.setStatus("current")
_Ssg5000SSMStatEntry_Object = MibTableRow
ssg5000SSMStatEntry = _Ssg5000SSMStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1)
)
ssg5000SSMStatEntry.setIndexNames(
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SSMIndex"),
)
if mibBuilder.loadTexts:
    ssg5000SSMStatEntry.setStatus("current")
_Ssg5000SSMIndex_Type = Integer32
_Ssg5000SSMIndex_Object = MibTableColumn
ssg5000SSMIndex = _Ssg5000SSMIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 1),
    _Ssg5000SSMIndex_Type()
)
ssg5000SSMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMIndex.setStatus("current")
_Ssg5000SSMAdminStatus_Type = AdminStatus
_Ssg5000SSMAdminStatus_Object = MibTableColumn
ssg5000SSMAdminStatus = _Ssg5000SSMAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 2),
    _Ssg5000SSMAdminStatus_Type()
)
ssg5000SSMAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMAdminStatus.setStatus("current")
_Ssg5000SSMOperStatus_Type = OperStatus
_Ssg5000SSMOperStatus_Object = MibTableColumn
ssg5000SSMOperStatus = _Ssg5000SSMOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 3),
    _Ssg5000SSMOperStatus_Type()
)
ssg5000SSMOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMOperStatus.setStatus("current")
_Ssg5000SSMCPUIdleTics5Sec_Type = Integer32
_Ssg5000SSMCPUIdleTics5Sec_Object = MibTableColumn
ssg5000SSMCPUIdleTics5Sec = _Ssg5000SSMCPUIdleTics5Sec_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 4),
    _Ssg5000SSMCPUIdleTics5Sec_Type()
)
ssg5000SSMCPUIdleTics5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUIdleTics5Sec.setStatus("current")
_Ssg5000SSMCPUTics5Sec_Type = Integer32
_Ssg5000SSMCPUTics5Sec_Object = MibTableColumn
ssg5000SSMCPUTics5Sec = _Ssg5000SSMCPUTics5Sec_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 5),
    _Ssg5000SSMCPUTics5Sec_Type()
)
ssg5000SSMCPUTics5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUTics5Sec.setStatus("current")
_Ssg5000SSMCPUIdleTicsReboot_Type = Integer32
_Ssg5000SSMCPUIdleTicsReboot_Object = MibTableColumn
ssg5000SSMCPUIdleTicsReboot = _Ssg5000SSMCPUIdleTicsReboot_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 6),
    _Ssg5000SSMCPUIdleTicsReboot_Type()
)
ssg5000SSMCPUIdleTicsReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUIdleTicsReboot.setStatus("current")
_Ssg5000SSMCPUTicsReboot_Type = Integer32
_Ssg5000SSMCPUTicsReboot_Object = MibTableColumn
ssg5000SSMCPUTicsReboot = _Ssg5000SSMCPUTicsReboot_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 7),
    _Ssg5000SSMCPUTicsReboot_Type()
)
ssg5000SSMCPUTicsReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUTicsReboot.setStatus("current")
_Ssg5000SSMCPUMemHeapFree_Type = Integer32
_Ssg5000SSMCPUMemHeapFree_Object = MibTableColumn
ssg5000SSMCPUMemHeapFree = _Ssg5000SSMCPUMemHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 8),
    _Ssg5000SSMCPUMemHeapFree_Type()
)
ssg5000SSMCPUMemHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUMemHeapFree.setStatus("current")
_Ssg5000SSMCPUMemHeapTotal_Type = Integer32
_Ssg5000SSMCPUMemHeapTotal_Object = MibTableColumn
ssg5000SSMCPUMemHeapTotal = _Ssg5000SSMCPUMemHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 9),
    _Ssg5000SSMCPUMemHeapTotal_Type()
)
ssg5000SSMCPUMemHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUMemHeapTotal.setStatus("current")
_Ssg5000SSMCPUMBufClusterFree_Type = Integer32
_Ssg5000SSMCPUMBufClusterFree_Object = MibTableColumn
ssg5000SSMCPUMBufClusterFree = _Ssg5000SSMCPUMBufClusterFree_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 10),
    _Ssg5000SSMCPUMBufClusterFree_Type()
)
ssg5000SSMCPUMBufClusterFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUMBufClusterFree.setStatus("current")
_Ssg5000SSMCPUMBufClusterTotal_Type = Integer32
_Ssg5000SSMCPUMBufClusterTotal_Object = MibTableColumn
ssg5000SSMCPUMBufClusterTotal = _Ssg5000SSMCPUMBufClusterTotal_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 11),
    _Ssg5000SSMCPUMBufClusterTotal_Type()
)
ssg5000SSMCPUMBufClusterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMCPUMBufClusterTotal.setStatus("current")
_Ssg5000SSMActiveAccessConn_Type = Integer32
_Ssg5000SSMActiveAccessConn_Object = MibTableColumn
ssg5000SSMActiveAccessConn = _Ssg5000SSMActiveAccessConn_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 12),
    _Ssg5000SSMActiveAccessConn_Type()
)
ssg5000SSMActiveAccessConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMActiveAccessConn.setStatus("current")
_Ssg5000SSMActiveSubscribers_Type = Integer32
_Ssg5000SSMActiveSubscribers_Object = MibTableColumn
ssg5000SSMActiveSubscribers = _Ssg5000SSMActiveSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 13),
    _Ssg5000SSMActiveSubscribers_Type()
)
ssg5000SSMActiveSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMActiveSubscribers.setStatus("current")
_Ssg5000SSMPacketsDropped_Type = Integer32
_Ssg5000SSMPacketsDropped_Object = MibTableColumn
ssg5000SSMPacketsDropped = _Ssg5000SSMPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 14),
    _Ssg5000SSMPacketsDropped_Type()
)
ssg5000SSMPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMPacketsDropped.setStatus("current")
_Ssg5000SSMPacketsForwarded_Type = Integer32
_Ssg5000SSMPacketsForwarded_Object = MibTableColumn
ssg5000SSMPacketsForwarded = _Ssg5000SSMPacketsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 15),
    _Ssg5000SSMPacketsForwarded_Type()
)
ssg5000SSMPacketsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMPacketsForwarded.setStatus("current")
_Ssg5000SSMAlarms_Type = Integer32
_Ssg5000SSMAlarms_Object = MibTableColumn
ssg5000SSMAlarms = _Ssg5000SSMAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 3, 1, 16),
    _Ssg5000SSMAlarms_Type()
)
ssg5000SSMAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SSMAlarms.setStatus("current")
_Ssg5000ALCPortStatTable_Object = MibTable
ssg5000ALCPortStatTable = _Ssg5000ALCPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ssg5000ALCPortStatTable.setStatus("current")
_Ssg5000ALCPortStatEntry_Object = MibTableRow
ssg5000ALCPortStatEntry = _Ssg5000ALCPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1)
)
ssg5000ALCPortStatEntry.setIndexNames(
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000ALCPortIndex"),
)
if mibBuilder.loadTexts:
    ssg5000ALCPortStatEntry.setStatus("current")
_Ssg5000ALCPortIndex_Type = Integer32
_Ssg5000ALCPortIndex_Object = MibTableColumn
ssg5000ALCPortIndex = _Ssg5000ALCPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 1),
    _Ssg5000ALCPortIndex_Type()
)
ssg5000ALCPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortIndex.setStatus("current")
_Ssg5000ALCPortIfIndex_Type = Integer32
_Ssg5000ALCPortIfIndex_Object = MibTableColumn
ssg5000ALCPortIfIndex = _Ssg5000ALCPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 2),
    _Ssg5000ALCPortIfIndex_Type()
)
ssg5000ALCPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortIfIndex.setStatus("current")
_Ssg5000ALCPortAdminStatus_Type = AdminStatus
_Ssg5000ALCPortAdminStatus_Object = MibTableColumn
ssg5000ALCPortAdminStatus = _Ssg5000ALCPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 3),
    _Ssg5000ALCPortAdminStatus_Type()
)
ssg5000ALCPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortAdminStatus.setStatus("current")
_Ssg5000ALCPortOperStatus_Type = OperStatus
_Ssg5000ALCPortOperStatus_Object = MibTableColumn
ssg5000ALCPortOperStatus = _Ssg5000ALCPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 4),
    _Ssg5000ALCPortOperStatus_Type()
)
ssg5000ALCPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortOperStatus.setStatus("current")
_Ssg5000ALCPortActiveAccessConn_Type = Integer32
_Ssg5000ALCPortActiveAccessConn_Object = MibTableColumn
ssg5000ALCPortActiveAccessConn = _Ssg5000ALCPortActiveAccessConn_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 5),
    _Ssg5000ALCPortActiveAccessConn_Type()
)
ssg5000ALCPortActiveAccessConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortActiveAccessConn.setStatus("current")
_Ssg5000ALCPortActiveTrunkConn_Type = Integer32
_Ssg5000ALCPortActiveTrunkConn_Object = MibTableColumn
ssg5000ALCPortActiveTrunkConn = _Ssg5000ALCPortActiveTrunkConn_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 6),
    _Ssg5000ALCPortActiveTrunkConn_Type()
)
ssg5000ALCPortActiveTrunkConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortActiveTrunkConn.setStatus("current")
_Ssg5000ALCPortCellsReceived_Type = Counter64
_Ssg5000ALCPortCellsReceived_Object = MibTableColumn
ssg5000ALCPortCellsReceived = _Ssg5000ALCPortCellsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 7),
    _Ssg5000ALCPortCellsReceived_Type()
)
ssg5000ALCPortCellsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortCellsReceived.setStatus("current")
_Ssg5000ALCPortCellsTransmitted_Type = Counter64
_Ssg5000ALCPortCellsTransmitted_Object = MibTableColumn
ssg5000ALCPortCellsTransmitted = _Ssg5000ALCPortCellsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 8),
    _Ssg5000ALCPortCellsTransmitted_Type()
)
ssg5000ALCPortCellsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortCellsTransmitted.setStatus("current")
_Ssg5000ALCPortCellsDropped_Type = Counter64
_Ssg5000ALCPortCellsDropped_Object = MibTableColumn
ssg5000ALCPortCellsDropped = _Ssg5000ALCPortCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 9),
    _Ssg5000ALCPortCellsDropped_Type()
)
ssg5000ALCPortCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortCellsDropped.setStatus("current")
_Ssg5000ALCPortAlarms_Type = Integer32
_Ssg5000ALCPortAlarms_Object = MibTableColumn
ssg5000ALCPortAlarms = _Ssg5000ALCPortAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 4, 1, 10),
    _Ssg5000ALCPortAlarms_Type()
)
ssg5000ALCPortAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ALCPortAlarms.setStatus("current")
_Ssg5000ETHPortStatTable_Object = MibTable
ssg5000ETHPortStatTable = _Ssg5000ETHPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ssg5000ETHPortStatTable.setStatus("current")
_Ssg5000ETHPortStatEntry_Object = MibTableRow
ssg5000ETHPortStatEntry = _Ssg5000ETHPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5, 1)
)
ssg5000ETHPortStatEntry.setIndexNames(
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000ETHPortIndex"),
)
if mibBuilder.loadTexts:
    ssg5000ETHPortStatEntry.setStatus("current")
_Ssg5000ETHPortIndex_Type = Integer32
_Ssg5000ETHPortIndex_Object = MibTableColumn
ssg5000ETHPortIndex = _Ssg5000ETHPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5, 1, 1),
    _Ssg5000ETHPortIndex_Type()
)
ssg5000ETHPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ETHPortIndex.setStatus("current")
_Ssg5000ETHPortAdminStatus_Type = AdminStatus
_Ssg5000ETHPortAdminStatus_Object = MibTableColumn
ssg5000ETHPortAdminStatus = _Ssg5000ETHPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5, 1, 2),
    _Ssg5000ETHPortAdminStatus_Type()
)
ssg5000ETHPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ETHPortAdminStatus.setStatus("current")
_Ssg5000ETHPortOperStatus_Type = OperStatus
_Ssg5000ETHPortOperStatus_Object = MibTableColumn
ssg5000ETHPortOperStatus = _Ssg5000ETHPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5, 1, 3),
    _Ssg5000ETHPortOperStatus_Type()
)
ssg5000ETHPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ETHPortOperStatus.setStatus("current")
_Ssg5000ETHPortAlarms_Type = Integer32
_Ssg5000ETHPortAlarms_Object = MibTableColumn
ssg5000ETHPortAlarms = _Ssg5000ETHPortAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 5, 1, 4),
    _Ssg5000ETHPortAlarms_Type()
)
ssg5000ETHPortAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000ETHPortAlarms.setStatus("current")
_Ssg5000CT3PortStatTable_Object = MibTable
ssg5000CT3PortStatTable = _Ssg5000CT3PortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ssg5000CT3PortStatTable.setStatus("current")
_Ssg5000CT3PortStatEntry_Object = MibTableRow
ssg5000CT3PortStatEntry = _Ssg5000CT3PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6, 1)
)
ssg5000CT3PortStatEntry.setIndexNames(
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
    (0, "SSG-5000-CHASSIS-MIB", "ssg5000CT3PortIndex"),
)
if mibBuilder.loadTexts:
    ssg5000CT3PortStatEntry.setStatus("current")
_Ssg5000CT3PortIndex_Type = Integer32
_Ssg5000CT3PortIndex_Object = MibTableColumn
ssg5000CT3PortIndex = _Ssg5000CT3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6, 1, 1),
    _Ssg5000CT3PortIndex_Type()
)
ssg5000CT3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CT3PortIndex.setStatus("current")
_Ssg5000CT3PortAdminStatus_Type = AdminStatus
_Ssg5000CT3PortAdminStatus_Object = MibTableColumn
ssg5000CT3PortAdminStatus = _Ssg5000CT3PortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6, 1, 2),
    _Ssg5000CT3PortAdminStatus_Type()
)
ssg5000CT3PortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CT3PortAdminStatus.setStatus("current")
_Ssg5000CT3PortOperStatus_Type = OperStatus
_Ssg5000CT3PortOperStatus_Object = MibTableColumn
ssg5000CT3PortOperStatus = _Ssg5000CT3PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6, 1, 3),
    _Ssg5000CT3PortOperStatus_Type()
)
ssg5000CT3PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CT3PortOperStatus.setStatus("current")
_Ssg5000CT3PortAlarms_Type = Integer32
_Ssg5000CT3PortAlarms_Object = MibTableColumn
ssg5000CT3PortAlarms = _Ssg5000CT3PortAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 1, 6, 1, 4),
    _Ssg5000CT3PortAlarms_Type()
)
ssg5000CT3PortAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CT3PortAlarms.setStatus("current")
_Ssg5000SysHealthGroup_ObjectIdentity = ObjectIdentity
ssg5000SysHealthGroup = _Ssg5000SysHealthGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2)
)
_Ssg5000SysFanStatus_Type = PSOperStatus
_Ssg5000SysFanStatus_Object = MibScalar
ssg5000SysFanStatus = _Ssg5000SysFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 1),
    _Ssg5000SysFanStatus_Type()
)
ssg5000SysFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysFanStatus.setStatus("current")


class _Ssg5000SysTempStatus_Type(Integer32):
    """Custom type ssg5000SysTempStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("overTemperature", 2),
          ("underTemperature", 3))
    )


_Ssg5000SysTempStatus_Type.__name__ = "Integer32"
_Ssg5000SysTempStatus_Object = MibScalar
ssg5000SysTempStatus = _Ssg5000SysTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 2),
    _Ssg5000SysTempStatus_Type()
)
ssg5000SysTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysTempStatus.setStatus("current")
_Ssg5000SysFabricCellsDropped_Type = Counter64
_Ssg5000SysFabricCellsDropped_Object = MibScalar
ssg5000SysFabricCellsDropped = _Ssg5000SysFabricCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 3),
    _Ssg5000SysFabricCellsDropped_Type()
)
ssg5000SysFabricCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysFabricCellsDropped.setStatus("current")
_Ssg5000SysFabricMemUtilization_Type = Integer32
_Ssg5000SysFabricMemUtilization_Object = MibScalar
ssg5000SysFabricMemUtilization = _Ssg5000SysFabricMemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 4),
    _Ssg5000SysFabricMemUtilization_Type()
)
ssg5000SysFabricMemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysFabricMemUtilization.setStatus("current")
_Ssg5000SysActiveAccessConn_Type = Integer32
_Ssg5000SysActiveAccessConn_Object = MibScalar
ssg5000SysActiveAccessConn = _Ssg5000SysActiveAccessConn_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 5),
    _Ssg5000SysActiveAccessConn_Type()
)
ssg5000SysActiveAccessConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysActiveAccessConn.setStatus("current")
_Ssg5000SysActiveTrunkConn_Type = Integer32
_Ssg5000SysActiveTrunkConn_Object = MibScalar
ssg5000SysActiveTrunkConn = _Ssg5000SysActiveTrunkConn_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 6),
    _Ssg5000SysActiveTrunkConn_Type()
)
ssg5000SysActiveTrunkConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysActiveTrunkConn.setStatus("current")
_Ssg5000SysPacketsDropped_Type = Integer32
_Ssg5000SysPacketsDropped_Object = MibScalar
ssg5000SysPacketsDropped = _Ssg5000SysPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 7),
    _Ssg5000SysPacketsDropped_Type()
)
ssg5000SysPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysPacketsDropped.setStatus("current")
_Ssg5000SysCellsDropped_Type = Counter64
_Ssg5000SysCellsDropped_Object = MibScalar
ssg5000SysCellsDropped = _Ssg5000SysCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 8),
    _Ssg5000SysCellsDropped_Type()
)
ssg5000SysCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SysCellsDropped.setStatus("current")
_Ssg5000CmcCPUIdleTics5Sec_Type = Integer32
_Ssg5000CmcCPUIdleTics5Sec_Object = MibScalar
ssg5000CmcCPUIdleTics5Sec = _Ssg5000CmcCPUIdleTics5Sec_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 9),
    _Ssg5000CmcCPUIdleTics5Sec_Type()
)
ssg5000CmcCPUIdleTics5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUIdleTics5Sec.setStatus("current")
_Ssg5000CmcCPUTotalTics5Sec_Type = Integer32
_Ssg5000CmcCPUTotalTics5Sec_Object = MibScalar
ssg5000CmcCPUTotalTics5Sec = _Ssg5000CmcCPUTotalTics5Sec_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 10),
    _Ssg5000CmcCPUTotalTics5Sec_Type()
)
ssg5000CmcCPUTotalTics5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUTotalTics5Sec.setStatus("current")
_Ssg5000CmcCPUIdleTicsReboot_Type = Integer32
_Ssg5000CmcCPUIdleTicsReboot_Object = MibScalar
ssg5000CmcCPUIdleTicsReboot = _Ssg5000CmcCPUIdleTicsReboot_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 11),
    _Ssg5000CmcCPUIdleTicsReboot_Type()
)
ssg5000CmcCPUIdleTicsReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUIdleTicsReboot.setStatus("current")
_Ssg5000CmcCPUTotalTicsReboot_Type = Integer32
_Ssg5000CmcCPUTotalTicsReboot_Object = MibScalar
ssg5000CmcCPUTotalTicsReboot = _Ssg5000CmcCPUTotalTicsReboot_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 12),
    _Ssg5000CmcCPUTotalTicsReboot_Type()
)
ssg5000CmcCPUTotalTicsReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUTotalTicsReboot.setStatus("current")
_Ssg5000CmcCPUMemHeapFree_Type = Integer32
_Ssg5000CmcCPUMemHeapFree_Object = MibScalar
ssg5000CmcCPUMemHeapFree = _Ssg5000CmcCPUMemHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 13),
    _Ssg5000CmcCPUMemHeapFree_Type()
)
ssg5000CmcCPUMemHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUMemHeapFree.setStatus("current")
_Ssg5000CmcCPUMemHeapTotal_Type = Integer32
_Ssg5000CmcCPUMemHeapTotal_Object = MibScalar
ssg5000CmcCPUMemHeapTotal = _Ssg5000CmcCPUMemHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 14),
    _Ssg5000CmcCPUMemHeapTotal_Type()
)
ssg5000CmcCPUMemHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUMemHeapTotal.setStatus("current")
_Ssg5000CmcCPUMBufClusterFree_Type = Integer32
_Ssg5000CmcCPUMBufClusterFree_Object = MibScalar
ssg5000CmcCPUMBufClusterFree = _Ssg5000CmcCPUMBufClusterFree_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 15),
    _Ssg5000CmcCPUMBufClusterFree_Type()
)
ssg5000CmcCPUMBufClusterFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUMBufClusterFree.setStatus("current")
_Ssg5000CmcCPUMBufClusterTotal_Type = Integer32
_Ssg5000CmcCPUMBufClusterTotal_Object = MibScalar
ssg5000CmcCPUMBufClusterTotal = _Ssg5000CmcCPUMBufClusterTotal_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 16),
    _Ssg5000CmcCPUMBufClusterTotal_Type()
)
ssg5000CmcCPUMBufClusterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUMBufClusterTotal.setStatus("current")
_Ssg5000CmcCPUAverageLoad_Type = Integer32
_Ssg5000CmcCPUAverageLoad_Object = MibScalar
ssg5000CmcCPUAverageLoad = _Ssg5000CmcCPUAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 17),
    _Ssg5000CmcCPUAverageLoad_Type()
)
ssg5000CmcCPUAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000CmcCPUAverageLoad.setStatus("current")
_Ssg5000SspCPUnoEncryptionAverageLoad_Type = Integer32
_Ssg5000SspCPUnoEncryptionAverageLoad_Object = MibScalar
ssg5000SspCPUnoEncryptionAverageLoad = _Ssg5000SspCPUnoEncryptionAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 18),
    _Ssg5000SspCPUnoEncryptionAverageLoad_Type()
)
ssg5000SspCPUnoEncryptionAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SspCPUnoEncryptionAverageLoad.setStatus("current")
_Ssg5000SspCPUwEncryptionAverageLoad_Type = Integer32
_Ssg5000SspCPUwEncryptionAverageLoad_Object = MibScalar
ssg5000SspCPUwEncryptionAverageLoad = _Ssg5000SspCPUwEncryptionAverageLoad_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 2, 19),
    _Ssg5000SspCPUwEncryptionAverageLoad_Type()
)
ssg5000SspCPUwEncryptionAverageLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ssg5000SspCPUwEncryptionAverageLoad.setStatus("current")
_Ssg5000TrapIndexGroup_ObjectIdentity = ObjectIdentity
ssg5000TrapIndexGroup = _Ssg5000TrapIndexGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3)
)
_Ssg5000TrapSystemAlarmId_Type = SystemAlarmType
_Ssg5000TrapSystemAlarmId_Object = MibScalar
ssg5000TrapSystemAlarmId = _Ssg5000TrapSystemAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 1),
    _Ssg5000TrapSystemAlarmId_Type()
)
ssg5000TrapSystemAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapSystemAlarmId.setStatus("current")
_Ssg5000TrapCardAlarmId_Type = CardAlarmType
_Ssg5000TrapCardAlarmId_Object = MibScalar
ssg5000TrapCardAlarmId = _Ssg5000TrapCardAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 2),
    _Ssg5000TrapCardAlarmId_Type()
)
ssg5000TrapCardAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapCardAlarmId.setStatus("current")
_Ssg5000TrapALCPortAlarmId_Type = ALCPortAlarmType
_Ssg5000TrapALCPortAlarmId_Object = MibScalar
ssg5000TrapALCPortAlarmId = _Ssg5000TrapALCPortAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 3),
    _Ssg5000TrapALCPortAlarmId_Type()
)
ssg5000TrapALCPortAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapALCPortAlarmId.setStatus("current")
_Ssg5000TrapSSMAlarmId_Type = SSMAlarmType
_Ssg5000TrapSSMAlarmId_Object = MibScalar
ssg5000TrapSSMAlarmId = _Ssg5000TrapSSMAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 4),
    _Ssg5000TrapSSMAlarmId_Type()
)
ssg5000TrapSSMAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapSSMAlarmId.setStatus("current")
_Ssg5000TrapSlotId_Type = Integer32
_Ssg5000TrapSlotId_Object = MibScalar
ssg5000TrapSlotId = _Ssg5000TrapSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 5),
    _Ssg5000TrapSlotId_Type()
)
ssg5000TrapSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapSlotId.setStatus("current")
_Ssg5000TrapCardType_Type = CardType
_Ssg5000TrapCardType_Object = MibScalar
ssg5000TrapCardType = _Ssg5000TrapCardType_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 6),
    _Ssg5000TrapCardType_Type()
)
ssg5000TrapCardType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapCardType.setStatus("current")
_Ssg5000TrapPortId_Type = Integer32
_Ssg5000TrapPortId_Object = MibScalar
ssg5000TrapPortId = _Ssg5000TrapPortId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 7),
    _Ssg5000TrapPortId_Type()
)
ssg5000TrapPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapPortId.setStatus("current")
_Ssg5000TrapOccurClearTag_Type = ALARMStateType
_Ssg5000TrapOccurClearTag_Object = MibScalar
ssg5000TrapOccurClearTag = _Ssg5000TrapOccurClearTag_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 8),
    _Ssg5000TrapOccurClearTag_Type()
)
ssg5000TrapOccurClearTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapOccurClearTag.setStatus("current")
_Ssg5000TrapPVCAlarmId_Type = PVCAlarmType
_Ssg5000TrapPVCAlarmId_Object = MibScalar
ssg5000TrapPVCAlarmId = _Ssg5000TrapPVCAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 9),
    _Ssg5000TrapPVCAlarmId_Type()
)
ssg5000TrapPVCAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapPVCAlarmId.setStatus("current")
_Ssg5000TrapInterfaceNumber_Type = Integer32
_Ssg5000TrapInterfaceNumber_Object = MibScalar
ssg5000TrapInterfaceNumber = _Ssg5000TrapInterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 10),
    _Ssg5000TrapInterfaceNumber_Type()
)
ssg5000TrapInterfaceNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapInterfaceNumber.setStatus("current")
_Ssg5000TrapVPINumber_Type = Integer32
_Ssg5000TrapVPINumber_Object = MibScalar
ssg5000TrapVPINumber = _Ssg5000TrapVPINumber_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 11),
    _Ssg5000TrapVPINumber_Type()
)
ssg5000TrapVPINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapVPINumber.setStatus("current")
_Ssg5000TrapVCINumber_Type = Integer32
_Ssg5000TrapVCINumber_Object = MibScalar
ssg5000TrapVCINumber = _Ssg5000TrapVCINumber_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 12),
    _Ssg5000TrapVCINumber_Type()
)
ssg5000TrapVCINumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapVCINumber.setStatus("current")
_Ssg5000TrapCT3PortAlarmId_Type = CT3PortAlarmType
_Ssg5000TrapCT3PortAlarmId_Object = MibScalar
ssg5000TrapCT3PortAlarmId = _Ssg5000TrapCT3PortAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 13),
    _Ssg5000TrapCT3PortAlarmId_Type()
)
ssg5000TrapCT3PortAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapCT3PortAlarmId.setStatus("current")
_Ssg5000TrapETHPortAlarmId_Type = ETHPortAlarmType
_Ssg5000TrapETHPortAlarmId_Object = MibScalar
ssg5000TrapETHPortAlarmId = _Ssg5000TrapETHPortAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 14),
    _Ssg5000TrapETHPortAlarmId_Type()
)
ssg5000TrapETHPortAlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapETHPortAlarmId.setStatus("current")
_Ssg5000TrapSSGHostAddress_Type = IpAddress
_Ssg5000TrapSSGHostAddress_Object = MibScalar
ssg5000TrapSSGHostAddress = _Ssg5000TrapSSGHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 15),
    _Ssg5000TrapSSGHostAddress_Type()
)
ssg5000TrapSSGHostAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapSSGHostAddress.setStatus("current")
_Ssg5000TrapCT3DS2AlarmId_Type = CT3DS2AlarmType
_Ssg5000TrapCT3DS2AlarmId_Object = MibScalar
ssg5000TrapCT3DS2AlarmId = _Ssg5000TrapCT3DS2AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 16),
    _Ssg5000TrapCT3DS2AlarmId_Type()
)
ssg5000TrapCT3DS2AlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapCT3DS2AlarmId.setStatus("current")
_Ssg5000TrapCT3DS1AlarmId_Type = CT3DS1AlarmType
_Ssg5000TrapCT3DS1AlarmId_Object = MibScalar
ssg5000TrapCT3DS1AlarmId = _Ssg5000TrapCT3DS1AlarmId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 17),
    _Ssg5000TrapCT3DS1AlarmId_Type()
)
ssg5000TrapCT3DS1AlarmId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapCT3DS1AlarmId.setStatus("current")
_Ssg5000TrapDS2ChannelId_Type = Integer32
_Ssg5000TrapDS2ChannelId_Object = MibScalar
ssg5000TrapDS2ChannelId = _Ssg5000TrapDS2ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 18),
    _Ssg5000TrapDS2ChannelId_Type()
)
ssg5000TrapDS2ChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapDS2ChannelId.setStatus("current")
_Ssg5000TrapDS1ChannelId_Type = Integer32
_Ssg5000TrapDS1ChannelId_Object = MibScalar
ssg5000TrapDS1ChannelId = _Ssg5000TrapDS1ChannelId_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 19),
    _Ssg5000TrapDS1ChannelId_Type()
)
ssg5000TrapDS1ChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapDS1ChannelId.setStatus("current")
_Ssg5000TrapServiceModuleAlarm_Type = DisplayString
_Ssg5000TrapServiceModuleAlarm_Object = MibScalar
ssg5000TrapServiceModuleAlarm = _Ssg5000TrapServiceModuleAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 20),
    _Ssg5000TrapServiceModuleAlarm_Type()
)
ssg5000TrapServiceModuleAlarm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapServiceModuleAlarm.setStatus("current")
_Ssg5000TrapServiceAlarmSeverity_Type = ServiceAlarmSeverityType
_Ssg5000TrapServiceAlarmSeverity_Object = MibScalar
ssg5000TrapServiceAlarmSeverity = _Ssg5000TrapServiceAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 21),
    _Ssg5000TrapServiceAlarmSeverity_Type()
)
ssg5000TrapServiceAlarmSeverity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapServiceAlarmSeverity.setStatus("current")
_Ssg5000TrapServiceAlarmDescription_Type = DisplayString
_Ssg5000TrapServiceAlarmDescription_Object = MibScalar
ssg5000TrapServiceAlarmDescription = _Ssg5000TrapServiceAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 1, 3, 22),
    _Ssg5000TrapServiceAlarmDescription_Type()
)
ssg5000TrapServiceAlarmDescription.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ssg5000TrapServiceAlarmDescription.setStatus("current")
_Ssg5000MIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ssg5000MIBNotificationPrefix = _Ssg5000MIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2)
)
_Ssg5000MIBNotification_ObjectIdentity = ObjectIdentity
ssg5000MIBNotification = _Ssg5000MIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0)
)
_Ssg5000ChassisMIBConformance_ObjectIdentity = ObjectIdentity
ssg5000ChassisMIBConformance = _Ssg5000ChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3)
)
_Ssg5000ChassisMIBCompliances_ObjectIdentity = ObjectIdentity
ssg5000ChassisMIBCompliances = _Ssg5000ChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3, 1)
)
_Ssg5000ChassisMIBGroups_ObjectIdentity = ObjectIdentity
ssg5000ChassisMIBGroups = _Ssg5000ChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3, 2)
)

# Managed Objects groups

ssg5000ChassisMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3, 2, 1)
)
ssg5000ChassisMIBGroup.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000SysStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotIndex"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotCardDescr"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotAdminStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotOperStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotCardNumPorts"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotCardHwVersion"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotCardSerialNumber"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SlotAlarms"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMIndex"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMAdminStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMOperStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUIdleTics5Sec"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUTics5Sec"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUIdleTicsReboot"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUTicsReboot"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUMemHeapFree"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUMemHeapTotal"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUMBufClusterFree"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMCPUMBufClusterTotal"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMActiveAccessConn"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMActiveSubscribers"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMPacketsDropped"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMPacketsForwarded"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SSMAlarms"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortIndex"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortIfIndex"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortAdminStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortOperStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortActiveAccessConn"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortActiveTrunkConn"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortCellsReceived"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortCellsTransmitted"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortCellsDropped"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000ALCPortAlarms"))
)
if mibBuilder.loadTexts:
    ssg5000ChassisMIBGroup.setStatus("current")

ssg5000SysHealthMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3, 2, 2)
)
ssg5000SysHealthMIBGroup.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000SysFanStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysTempStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysFabricCellsDropped"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysFabricMemUtilization"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysActiveAccessConn"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysActiveTrunkConn"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysPacketsDropped"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysCellsDropped"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUIdleTics5Sec"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUTotalTics5Sec"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUIdleTicsReboot"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUTotalTicsReboot"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUMemHeapFree"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUMemHeapTotal"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUMBufClusterFree"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUMBufClusterTotal"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000CmcCPUAverageLoad"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SspCPUnoEncryptionAverageLoad"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SspCPUwEncryptionAverageLoad"))
)
if mibBuilder.loadTexts:
    ssg5000SysHealthMIBGroup.setStatus("current")


# Notification objects

ssg5000ChassisFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 1)
)
ssg5000ChassisFailureNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000SysFanStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000SysTempStatus"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000ChassisFailureNotification.setStatus(
        "current"
    )

ssg5000SysAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 2)
)
ssg5000SysAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapSystemAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000SysAlarmNotification.setStatus(
        "current"
    )

ssg5000CardAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 3)
)
ssg5000CardAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000CardAlarmNotification.setStatus(
        "current"
    )

ssg5000PortAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 4)
)
ssg5000PortAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapALCPortAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000PortAlarmNotification.setStatus(
        "current"
    )

ssg5000SSMAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 5)
)
ssg5000SSMAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSMAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000SSMAlarmNotification.setStatus(
        "current"
    )

ssg5000PVCAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 6)
)
ssg5000PVCAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapPVCAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapInterfaceNumber"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapVPINumber"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapVCINumber"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000PVCAlarmNotification.setStatus(
        "current"
    )

ssg5000CT3PortAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 7)
)
ssg5000CT3PortAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapCT3PortAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000CT3PortAlarmNotification.setStatus(
        "current"
    )

ssg5000ETHPortAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 8)
)
ssg5000ETHPortAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapETHPortAlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000ETHPortAlarmNotification.setStatus(
        "current"
    )

ssg5000CT3DS2AlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 9)
)
ssg5000CT3DS2AlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapCT3DS2AlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapDS2ChannelId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000CT3DS2AlarmNotification.setStatus(
        "current"
    )

ssg5000CT3DS1AlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 10)
)
ssg5000CT3DS1AlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapCT3DS1AlarmId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSlotId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapCardType"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapPortId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapDS1ChannelId"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapOccurClearTag"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000CT3DS1AlarmNotification.setStatus(
        "current"
    )

ssg5000ServiceAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 2, 0, 11)
)
ssg5000ServiceAlarmNotification.setObjects(
      *(("SSG-5000-CHASSIS-MIB", "ssg5000TrapServiceModuleAlarm"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapServiceAlarmSeverity"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapServiceAlarmDescription"),
        ("SSG-5000-CHASSIS-MIB", "ssg5000TrapSSGHostAddress"))
)
if mibBuilder.loadTexts:
    ssg5000ServiceAlarmNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ssg5000ChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3199, 10, 28, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ssg5000ChassisMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SSG-5000-CHASSIS-MIB",
    **{"PSOperStatus": PSOperStatus,
       "AdminStatus": AdminStatus,
       "OperStatus": OperStatus,
       "PsType": PsType,
       "CardType": CardType,
       "SystemAlarmType": SystemAlarmType,
       "CardAlarmType": CardAlarmType,
       "ALCPortAlarmType": ALCPortAlarmType,
       "SSMAlarmType": SSMAlarmType,
       "CT3PortAlarmType": CT3PortAlarmType,
       "CT3DS2AlarmType": CT3DS2AlarmType,
       "CT3DS1AlarmType": CT3DS1AlarmType,
       "ServiceAlarmSeverityType": ServiceAlarmSeverityType,
       "ETHPortAlarmType": ETHPortAlarmType,
       "ALARMStateType": ALARMStateType,
       "PVCAlarmType": PVCAlarmType,
       "ssg5000ChassisMIB": ssg5000ChassisMIB,
       "ssg5000ChassisMIBObjects": ssg5000ChassisMIBObjects,
       "ssg5000ChassisGroup": ssg5000ChassisGroup,
       "ssg5000SysStatus": ssg5000SysStatus,
       "ssg5000SlotTable": ssg5000SlotTable,
       "ssg5000SlotEntry": ssg5000SlotEntry,
       "ssg5000SlotIndex": ssg5000SlotIndex,
       "ssg5000SlotCardType": ssg5000SlotCardType,
       "ssg5000SlotCardDescr": ssg5000SlotCardDescr,
       "ssg5000SlotAdminStatus": ssg5000SlotAdminStatus,
       "ssg5000SlotOperStatus": ssg5000SlotOperStatus,
       "ssg5000SlotCardNumPorts": ssg5000SlotCardNumPorts,
       "ssg5000SlotCardHwVersion": ssg5000SlotCardHwVersion,
       "ssg5000SlotCardSerialNumber": ssg5000SlotCardSerialNumber,
       "ssg5000SlotAlarms": ssg5000SlotAlarms,
       "ssg5000SSMStatTable": ssg5000SSMStatTable,
       "ssg5000SSMStatEntry": ssg5000SSMStatEntry,
       "ssg5000SSMIndex": ssg5000SSMIndex,
       "ssg5000SSMAdminStatus": ssg5000SSMAdminStatus,
       "ssg5000SSMOperStatus": ssg5000SSMOperStatus,
       "ssg5000SSMCPUIdleTics5Sec": ssg5000SSMCPUIdleTics5Sec,
       "ssg5000SSMCPUTics5Sec": ssg5000SSMCPUTics5Sec,
       "ssg5000SSMCPUIdleTicsReboot": ssg5000SSMCPUIdleTicsReboot,
       "ssg5000SSMCPUTicsReboot": ssg5000SSMCPUTicsReboot,
       "ssg5000SSMCPUMemHeapFree": ssg5000SSMCPUMemHeapFree,
       "ssg5000SSMCPUMemHeapTotal": ssg5000SSMCPUMemHeapTotal,
       "ssg5000SSMCPUMBufClusterFree": ssg5000SSMCPUMBufClusterFree,
       "ssg5000SSMCPUMBufClusterTotal": ssg5000SSMCPUMBufClusterTotal,
       "ssg5000SSMActiveAccessConn": ssg5000SSMActiveAccessConn,
       "ssg5000SSMActiveSubscribers": ssg5000SSMActiveSubscribers,
       "ssg5000SSMPacketsDropped": ssg5000SSMPacketsDropped,
       "ssg5000SSMPacketsForwarded": ssg5000SSMPacketsForwarded,
       "ssg5000SSMAlarms": ssg5000SSMAlarms,
       "ssg5000ALCPortStatTable": ssg5000ALCPortStatTable,
       "ssg5000ALCPortStatEntry": ssg5000ALCPortStatEntry,
       "ssg5000ALCPortIndex": ssg5000ALCPortIndex,
       "ssg5000ALCPortIfIndex": ssg5000ALCPortIfIndex,
       "ssg5000ALCPortAdminStatus": ssg5000ALCPortAdminStatus,
       "ssg5000ALCPortOperStatus": ssg5000ALCPortOperStatus,
       "ssg5000ALCPortActiveAccessConn": ssg5000ALCPortActiveAccessConn,
       "ssg5000ALCPortActiveTrunkConn": ssg5000ALCPortActiveTrunkConn,
       "ssg5000ALCPortCellsReceived": ssg5000ALCPortCellsReceived,
       "ssg5000ALCPortCellsTransmitted": ssg5000ALCPortCellsTransmitted,
       "ssg5000ALCPortCellsDropped": ssg5000ALCPortCellsDropped,
       "ssg5000ALCPortAlarms": ssg5000ALCPortAlarms,
       "ssg5000ETHPortStatTable": ssg5000ETHPortStatTable,
       "ssg5000ETHPortStatEntry": ssg5000ETHPortStatEntry,
       "ssg5000ETHPortIndex": ssg5000ETHPortIndex,
       "ssg5000ETHPortAdminStatus": ssg5000ETHPortAdminStatus,
       "ssg5000ETHPortOperStatus": ssg5000ETHPortOperStatus,
       "ssg5000ETHPortAlarms": ssg5000ETHPortAlarms,
       "ssg5000CT3PortStatTable": ssg5000CT3PortStatTable,
       "ssg5000CT3PortStatEntry": ssg5000CT3PortStatEntry,
       "ssg5000CT3PortIndex": ssg5000CT3PortIndex,
       "ssg5000CT3PortAdminStatus": ssg5000CT3PortAdminStatus,
       "ssg5000CT3PortOperStatus": ssg5000CT3PortOperStatus,
       "ssg5000CT3PortAlarms": ssg5000CT3PortAlarms,
       "ssg5000SysHealthGroup": ssg5000SysHealthGroup,
       "ssg5000SysFanStatus": ssg5000SysFanStatus,
       "ssg5000SysTempStatus": ssg5000SysTempStatus,
       "ssg5000SysFabricCellsDropped": ssg5000SysFabricCellsDropped,
       "ssg5000SysFabricMemUtilization": ssg5000SysFabricMemUtilization,
       "ssg5000SysActiveAccessConn": ssg5000SysActiveAccessConn,
       "ssg5000SysActiveTrunkConn": ssg5000SysActiveTrunkConn,
       "ssg5000SysPacketsDropped": ssg5000SysPacketsDropped,
       "ssg5000SysCellsDropped": ssg5000SysCellsDropped,
       "ssg5000CmcCPUIdleTics5Sec": ssg5000CmcCPUIdleTics5Sec,
       "ssg5000CmcCPUTotalTics5Sec": ssg5000CmcCPUTotalTics5Sec,
       "ssg5000CmcCPUIdleTicsReboot": ssg5000CmcCPUIdleTicsReboot,
       "ssg5000CmcCPUTotalTicsReboot": ssg5000CmcCPUTotalTicsReboot,
       "ssg5000CmcCPUMemHeapFree": ssg5000CmcCPUMemHeapFree,
       "ssg5000CmcCPUMemHeapTotal": ssg5000CmcCPUMemHeapTotal,
       "ssg5000CmcCPUMBufClusterFree": ssg5000CmcCPUMBufClusterFree,
       "ssg5000CmcCPUMBufClusterTotal": ssg5000CmcCPUMBufClusterTotal,
       "ssg5000CmcCPUAverageLoad": ssg5000CmcCPUAverageLoad,
       "ssg5000SspCPUnoEncryptionAverageLoad": ssg5000SspCPUnoEncryptionAverageLoad,
       "ssg5000SspCPUwEncryptionAverageLoad": ssg5000SspCPUwEncryptionAverageLoad,
       "ssg5000TrapIndexGroup": ssg5000TrapIndexGroup,
       "ssg5000TrapSystemAlarmId": ssg5000TrapSystemAlarmId,
       "ssg5000TrapCardAlarmId": ssg5000TrapCardAlarmId,
       "ssg5000TrapALCPortAlarmId": ssg5000TrapALCPortAlarmId,
       "ssg5000TrapSSMAlarmId": ssg5000TrapSSMAlarmId,
       "ssg5000TrapSlotId": ssg5000TrapSlotId,
       "ssg5000TrapCardType": ssg5000TrapCardType,
       "ssg5000TrapPortId": ssg5000TrapPortId,
       "ssg5000TrapOccurClearTag": ssg5000TrapOccurClearTag,
       "ssg5000TrapPVCAlarmId": ssg5000TrapPVCAlarmId,
       "ssg5000TrapInterfaceNumber": ssg5000TrapInterfaceNumber,
       "ssg5000TrapVPINumber": ssg5000TrapVPINumber,
       "ssg5000TrapVCINumber": ssg5000TrapVCINumber,
       "ssg5000TrapCT3PortAlarmId": ssg5000TrapCT3PortAlarmId,
       "ssg5000TrapETHPortAlarmId": ssg5000TrapETHPortAlarmId,
       "ssg5000TrapSSGHostAddress": ssg5000TrapSSGHostAddress,
       "ssg5000TrapCT3DS2AlarmId": ssg5000TrapCT3DS2AlarmId,
       "ssg5000TrapCT3DS1AlarmId": ssg5000TrapCT3DS1AlarmId,
       "ssg5000TrapDS2ChannelId": ssg5000TrapDS2ChannelId,
       "ssg5000TrapDS1ChannelId": ssg5000TrapDS1ChannelId,
       "ssg5000TrapServiceModuleAlarm": ssg5000TrapServiceModuleAlarm,
       "ssg5000TrapServiceAlarmSeverity": ssg5000TrapServiceAlarmSeverity,
       "ssg5000TrapServiceAlarmDescription": ssg5000TrapServiceAlarmDescription,
       "ssg5000MIBNotificationPrefix": ssg5000MIBNotificationPrefix,
       "ssg5000MIBNotification": ssg5000MIBNotification,
       "ssg5000ChassisFailureNotification": ssg5000ChassisFailureNotification,
       "ssg5000SysAlarmNotification": ssg5000SysAlarmNotification,
       "ssg5000CardAlarmNotification": ssg5000CardAlarmNotification,
       "ssg5000PortAlarmNotification": ssg5000PortAlarmNotification,
       "ssg5000SSMAlarmNotification": ssg5000SSMAlarmNotification,
       "ssg5000PVCAlarmNotification": ssg5000PVCAlarmNotification,
       "ssg5000CT3PortAlarmNotification": ssg5000CT3PortAlarmNotification,
       "ssg5000ETHPortAlarmNotification": ssg5000ETHPortAlarmNotification,
       "ssg5000CT3DS2AlarmNotification": ssg5000CT3DS2AlarmNotification,
       "ssg5000CT3DS1AlarmNotification": ssg5000CT3DS1AlarmNotification,
       "ssg5000ServiceAlarmNotification": ssg5000ServiceAlarmNotification,
       "ssg5000ChassisMIBConformance": ssg5000ChassisMIBConformance,
       "ssg5000ChassisMIBCompliances": ssg5000ChassisMIBCompliances,
       "ssg5000ChassisMIBCompliance": ssg5000ChassisMIBCompliance,
       "ssg5000ChassisMIBGroups": ssg5000ChassisMIBGroups,
       "ssg5000ChassisMIBGroup": ssg5000ChassisMIBGroup,
       "ssg5000SysHealthMIBGroup": ssg5000SysHealthMIBGroup}
)
