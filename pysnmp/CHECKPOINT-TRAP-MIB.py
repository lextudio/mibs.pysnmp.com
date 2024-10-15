# SNMP MIB module (CHECKPOINT-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CHECKPOINT-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:41 2024
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

(fanSpeedSensorName,
 fanSpeedSensorStatus,
 fanSpeedSensorType,
 fanSpeedSensorUnit,
 fanSpeedSensorValue,
 fwLSConnName,
 fwLSConnOverall,
 fwLSConnOverallDesc,
 fwLSConnState,
 fwLSConnStateDesc,
 fwLocalLoggingDesc,
 fwLocalLoggingStat,
 haBlockState,
 haIP,
 haIdentifier,
 haIfName,
 haProblemDescr,
 haProblemName,
 haProblemPriority,
 haProblemStatus,
 haProblemVerified,
 haShared,
 haStatCode,
 haStatLong,
 haStatShort,
 haState,
 haStatus,
 haTrusted,
 memActiveReal64,
 memActiveVirtual64,
 memTotalReal64,
 memTotalVirtual64,
 multiDiskFreeAvailablePercent,
 multiDiskName,
 multiProcIdleTime,
 multiProcIndex,
 multiProcInterrupts,
 multiProcRunQueue,
 multiProcSystemTime,
 multiProcUsage,
 multiProcUserTime,
 raidDiskFlags,
 raidDiskID,
 raidDiskState,
 raidDiskVolumeID,
 raidVolumeID,
 raidVolumeState,
 svnNetIfAddress,
 svnNetIfName,
 svnNetIfOperState,
 svnNetIfState,
 tempertureSensorName,
 tempertureSensorStatus,
 tempertureSensorType,
 tempertureSensorUnit,
 tempertureSensorValue,
 voltageSensorName,
 voltageSensorStatus,
 voltageSensorType,
 voltageSensorUnit,
 voltageSensorValue) = mibBuilder.importSymbols(
    "CHECKPOINT-MIB",
    "fanSpeedSensorName",
    "fanSpeedSensorStatus",
    "fanSpeedSensorType",
    "fanSpeedSensorUnit",
    "fanSpeedSensorValue",
    "fwLSConnName",
    "fwLSConnOverall",
    "fwLSConnOverallDesc",
    "fwLSConnState",
    "fwLSConnStateDesc",
    "fwLocalLoggingDesc",
    "fwLocalLoggingStat",
    "haBlockState",
    "haIP",
    "haIdentifier",
    "haIfName",
    "haProblemDescr",
    "haProblemName",
    "haProblemPriority",
    "haProblemStatus",
    "haProblemVerified",
    "haShared",
    "haStatCode",
    "haStatLong",
    "haStatShort",
    "haState",
    "haStatus",
    "haTrusted",
    "memActiveReal64",
    "memActiveVirtual64",
    "memTotalReal64",
    "memTotalVirtual64",
    "multiDiskFreeAvailablePercent",
    "multiDiskName",
    "multiProcIdleTime",
    "multiProcIndex",
    "multiProcInterrupts",
    "multiProcRunQueue",
    "multiProcSystemTime",
    "multiProcUsage",
    "multiProcUserTime",
    "raidDiskFlags",
    "raidDiskID",
    "raidDiskState",
    "raidDiskVolumeID",
    "raidVolumeID",
    "raidVolumeState",
    "svnNetIfAddress",
    "svnNetIfName",
    "svnNetIfOperState",
    "svnNetIfState",
    "tempertureSensorName",
    "tempertureSensorStatus",
    "tempertureSensorType",
    "tempertureSensorUnit",
    "tempertureSensorValue",
    "voltageSensorName",
    "voltageSensorStatus",
    "voltageSensorType",
    "voltageSensorUnit",
    "voltageSensorValue")

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

chkpntTrapMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 0)
)
chkpntTrapMibModule.setRevisions(
        ("2013-12-26 13:09",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Checkpoint_ObjectIdentity = ObjectIdentity
checkpoint = _Checkpoint_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1)
)
_ChkpntTrap_ObjectIdentity = ObjectIdentity
chkpntTrap = _ChkpntTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000)
)
_ChkpntTrapInfo_ObjectIdentity = ObjectIdentity
chkpntTrapInfo = _ChkpntTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0)
)
_ChkpntTrapOID_Type = DisplayString
_ChkpntTrapOID_Object = MibScalar
chkpntTrapOID = _ChkpntTrapOID_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 10),
    _ChkpntTrapOID_Type()
)
chkpntTrapOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapOID.setStatus("current")
_ChkpntTrapOIDValue_Type = DisplayString
_ChkpntTrapOIDValue_Object = MibScalar
chkpntTrapOIDValue = _ChkpntTrapOIDValue_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 11),
    _ChkpntTrapOIDValue_Type()
)
chkpntTrapOIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapOIDValue.setStatus("current")
_ChkpntTrapMsgText_Type = DisplayString
_ChkpntTrapMsgText_Object = MibScalar
chkpntTrapMsgText = _ChkpntTrapMsgText_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 12),
    _ChkpntTrapMsgText_Type()
)
chkpntTrapMsgText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapMsgText.setStatus("current")


class _ChkpntTrapSeverity_Type(Integer32):
    """Custom type chkpntTrapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChkpntTrapSeverity_Type.__name__ = "Integer32"
_ChkpntTrapSeverity_Object = MibScalar
chkpntTrapSeverity = _ChkpntTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 13),
    _ChkpntTrapSeverity_Type()
)
chkpntTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapSeverity.setStatus("current")
_ChkpntTrapCategory_Type = DisplayString
_ChkpntTrapCategory_Object = MibScalar
chkpntTrapCategory = _ChkpntTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 0, 14),
    _ChkpntTrapCategory_Type()
)
chkpntTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chkpntTrapCategory.setStatus("current")
_ChkpntTrapNet_ObjectIdentity = ObjectIdentity
chkpntTrapNet = _ChkpntTrapNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1)
)
_ChkpntTrapDisk_ObjectIdentity = ObjectIdentity
chkpntTrapDisk = _ChkpntTrapDisk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2)
)
_ChkpntTrapCPU_ObjectIdentity = ObjectIdentity
chkpntTrapCPU = _ChkpntTrapCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3)
)
_ChkpntTrapMemory_ObjectIdentity = ObjectIdentity
chkpntTrapMemory = _ChkpntTrapMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4)
)
_ChkpntTrapHWSensor_ObjectIdentity = ObjectIdentity
chkpntTrapHWSensor = _ChkpntTrapHWSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5)
)
_ChkpntTrapTempertureSensor_ObjectIdentity = ObjectIdentity
chkpntTrapTempertureSensor = _ChkpntTrapTempertureSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1)
)
_ChkpntTrapFanSpeedSensor_ObjectIdentity = ObjectIdentity
chkpntTrapFanSpeedSensor = _ChkpntTrapFanSpeedSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2)
)
_ChkpntTrapVoltageSensor_ObjectIdentity = ObjectIdentity
chkpntTrapVoltageSensor = _ChkpntTrapVoltageSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3)
)
_ChkpntTrapHA_ObjectIdentity = ObjectIdentity
chkpntTrapHA = _ChkpntTrapHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6)
)
_ChkpntTrapLSConn_ObjectIdentity = ObjectIdentity
chkpntTrapLSConn = _ChkpntTrapLSConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7)
)

# Managed Objects groups


# Notification objects

chkpntTrapNetIfState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 1)
)
chkpntTrapNetIfState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"),
        ("CHECKPOINT-MIB", "svnNetIfState"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfState.setStatus(
        "current"
    )

chkpntTrapNetIfUnplugged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 2)
)
chkpntTrapNetIfUnplugged.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfUnplugged.setStatus(
        "current"
    )

chkpntTrapNewConnRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 3)
)
chkpntTrapNewConnRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapNewConnRate.setStatus(
        "current"
    )

chkpntTrapConcurrentConnRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 4)
)
chkpntTrapConcurrentConnRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapConcurrentConnRate.setStatus(
        "current"
    )

chkpntTrapBytesThroughput = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 5)
)
chkpntTrapBytesThroughput.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapBytesThroughput.setStatus(
        "current"
    )

chkpntTrapAcceptedPacketRate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 6)
)
chkpntTrapAcceptedPacketRate.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"))
)
if mibBuilder.loadTexts:
    chkpntTrapAcceptedPacketRate.setStatus(
        "current"
    )

chkpntTrapNetIfOperState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 1, 7)
)
chkpntTrapNetIfOperState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "svnNetIfName"),
        ("CHECKPOINT-MIB", "svnNetIfAddress"),
        ("CHECKPOINT-MIB", "svnNetIfOperState"))
)
if mibBuilder.loadTexts:
    chkpntTrapNetIfOperState.setStatus(
        "current"
    )

chkpntDiskSpaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 1)
)
chkpntDiskSpaceTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiDiskName"),
        ("CHECKPOINT-MIB", "multiDiskFreeAvailablePercent"))
)
if mibBuilder.loadTexts:
    chkpntDiskSpaceTrap.setStatus(
        "current"
    )

chkpntRAIDVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 2)
)
chkpntRAIDVolumeTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidVolumeID"),
        ("CHECKPOINT-MIB", "raidVolumeState"))
)
if mibBuilder.loadTexts:
    chkpntRAIDVolumeTrap.setStatus(
        "current"
    )

chkpntRAIDDiskTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 3)
)
chkpntRAIDDiskTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"))
)
if mibBuilder.loadTexts:
    chkpntRAIDDiskTrap.setStatus(
        "current"
    )

chkpntRAIDDiskFlagsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 2, 4)
)
chkpntRAIDDiskFlagsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "raidDiskVolumeID"),
        ("CHECKPOINT-MIB", "raidDiskID"),
        ("CHECKPOINT-MIB", "raidDiskState"),
        ("CHECKPOINT-MIB", "raidDiskFlags"))
)
if mibBuilder.loadTexts:
    chkpntRAIDDiskFlagsTrap.setStatus(
        "current"
    )

chkpntCPUCoreUtilTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 1)
)
chkpntCPUCoreUtilTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"))
)
if mibBuilder.loadTexts:
    chkpntCPUCoreUtilTrap.setStatus(
        "current"
    )

chkpntCPUCoreInterruptsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 3, 2)
)
chkpntCPUCoreInterruptsTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "multiProcIndex"),
        ("CHECKPOINT-MIB", "multiProcUserTime"),
        ("CHECKPOINT-MIB", "multiProcSystemTime"),
        ("CHECKPOINT-MIB", "multiProcIdleTime"),
        ("CHECKPOINT-MIB", "multiProcUsage"),
        ("CHECKPOINT-MIB", "multiProcRunQueue"),
        ("CHECKPOINT-MIB", "multiProcInterrupts"))
)
if mibBuilder.loadTexts:
    chkpntCPUCoreInterruptsTrap.setStatus(
        "current"
    )

chkpntSwapMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 1)
)
chkpntSwapMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "memTotalVirtual64"),
        ("CHECKPOINT-MIB", "memActiveVirtual64"))
)
if mibBuilder.loadTexts:
    chkpntSwapMemoryTrap.setStatus(
        "current"
    )

chkpntRealMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 4, 2)
)
chkpntRealMemoryTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "memTotalReal64"),
        ("CHECKPOINT-MIB", "memActiveReal64"))
)
if mibBuilder.loadTexts:
    chkpntRealMemoryTrap.setStatus(
        "current"
    )

chkpntTempertureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 1, 1)
)
chkpntTempertureTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "tempertureSensorName"),
        ("CHECKPOINT-MIB", "tempertureSensorValue"),
        ("CHECKPOINT-MIB", "tempertureSensorUnit"),
        ("CHECKPOINT-MIB", "tempertureSensorType"),
        ("CHECKPOINT-MIB", "tempertureSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntTempertureTrap.setStatus(
        "current"
    )

chkpntFanSpeedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 2, 1)
)
chkpntFanSpeedTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fanSpeedSensorName"),
        ("CHECKPOINT-MIB", "fanSpeedSensorValue"),
        ("CHECKPOINT-MIB", "fanSpeedSensorUnit"),
        ("CHECKPOINT-MIB", "fanSpeedSensorType"),
        ("CHECKPOINT-MIB", "fanSpeedSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntFanSpeedTrap.setStatus(
        "current"
    )

chkpntVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 5, 3, 1)
)
chkpntVoltageTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "voltageSensorName"),
        ("CHECKPOINT-MIB", "voltageSensorValue"),
        ("CHECKPOINT-MIB", "voltageSensorUnit"),
        ("CHECKPOINT-MIB", "voltageSensorType"),
        ("CHECKPOINT-MIB", "voltageSensorStatus"))
)
if mibBuilder.loadTexts:
    chkpntVoltageTrap.setStatus(
        "current"
    )

chkpntClusterMemberStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 1)
)
chkpntClusterMemberStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haState"))
)
if mibBuilder.loadTexts:
    chkpntClusterMemberStateTrap.setStatus(
        "current"
    )

chkpntClusterBlockStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 2)
)
chkpntClusterBlockStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haBlockState"),
        ("CHECKPOINT-MIB", "haState"))
)
if mibBuilder.loadTexts:
    chkpntClusterBlockStateTrap.setStatus(
        "current"
    )

chkpntClusterStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 3)
)
chkpntClusterStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIdentifier"),
        ("CHECKPOINT-MIB", "haBlockState"),
        ("CHECKPOINT-MIB", "haState"),
        ("CHECKPOINT-MIB", "haStatCode"),
        ("CHECKPOINT-MIB", "haStatShort"),
        ("CHECKPOINT-MIB", "haStatLong"))
)
if mibBuilder.loadTexts:
    chkpntClusterStateTrap.setStatus(
        "current"
    )

chkpntClusterProblemStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 4)
)
chkpntClusterProblemStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haProblemName"),
        ("CHECKPOINT-MIB", "haProblemStatus"),
        ("CHECKPOINT-MIB", "haProblemPriority"),
        ("CHECKPOINT-MIB", "haProblemVerified"),
        ("CHECKPOINT-MIB", "haProblemDescr"))
)
if mibBuilder.loadTexts:
    chkpntClusterProblemStateTrap.setStatus(
        "current"
    )

chkpntClusterInterfaceStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 6, 5)
)
chkpntClusterInterfaceStateTrap.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "haIfName"),
        ("CHECKPOINT-MIB", "haIP"),
        ("CHECKPOINT-MIB", "haStatus"),
        ("CHECKPOINT-MIB", "haTrusted"),
        ("CHECKPOINT-MIB", "haShared"))
)
if mibBuilder.loadTexts:
    chkpntClusterInterfaceStateTrap.setStatus(
        "current"
    )

chkpntTrapLSConnState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 1)
)
chkpntTrapLSConnState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnName"),
        ("CHECKPOINT-MIB", "fwLSConnState"),
        ("CHECKPOINT-MIB", "fwLSConnStateDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapLSConnState.setStatus(
        "current"
    )

chkpntTrapOverallLSConnState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 2)
)
chkpntTrapOverallLSConnState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnOverall"),
        ("CHECKPOINT-MIB", "fwLSConnOverallDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapOverallLSConnState.setStatus(
        "current"
    )

chkpntTrapLocalLoggingState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2620, 1, 2000, 7, 3)
)
chkpntTrapLocalLoggingState.setObjects(
      *(("CHECKPOINT-TRAP-MIB", "chkpntTrapOID"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapOIDValue"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapMsgText"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapSeverity"),
        ("CHECKPOINT-TRAP-MIB", "chkpntTrapCategory"),
        ("CHECKPOINT-MIB", "fwLSConnOverall"),
        ("CHECKPOINT-MIB", "fwLSConnOverallDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingDesc"),
        ("CHECKPOINT-MIB", "fwLocalLoggingStat"))
)
if mibBuilder.loadTexts:
    chkpntTrapLocalLoggingState.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CHECKPOINT-TRAP-MIB",
    **{"checkpoint": checkpoint,
       "products": products,
       "chkpntTrap": chkpntTrap,
       "chkpntTrapInfo": chkpntTrapInfo,
       "chkpntTrapMibModule": chkpntTrapMibModule,
       "chkpntTrapOID": chkpntTrapOID,
       "chkpntTrapOIDValue": chkpntTrapOIDValue,
       "chkpntTrapMsgText": chkpntTrapMsgText,
       "chkpntTrapSeverity": chkpntTrapSeverity,
       "chkpntTrapCategory": chkpntTrapCategory,
       "chkpntTrapNet": chkpntTrapNet,
       "chkpntTrapNetIfState": chkpntTrapNetIfState,
       "chkpntTrapNetIfUnplugged": chkpntTrapNetIfUnplugged,
       "chkpntTrapNewConnRate": chkpntTrapNewConnRate,
       "chkpntTrapConcurrentConnRate": chkpntTrapConcurrentConnRate,
       "chkpntTrapBytesThroughput": chkpntTrapBytesThroughput,
       "chkpntTrapAcceptedPacketRate": chkpntTrapAcceptedPacketRate,
       "chkpntTrapNetIfOperState": chkpntTrapNetIfOperState,
       "chkpntTrapDisk": chkpntTrapDisk,
       "chkpntDiskSpaceTrap": chkpntDiskSpaceTrap,
       "chkpntRAIDVolumeTrap": chkpntRAIDVolumeTrap,
       "chkpntRAIDDiskTrap": chkpntRAIDDiskTrap,
       "chkpntRAIDDiskFlagsTrap": chkpntRAIDDiskFlagsTrap,
       "chkpntTrapCPU": chkpntTrapCPU,
       "chkpntCPUCoreUtilTrap": chkpntCPUCoreUtilTrap,
       "chkpntCPUCoreInterruptsTrap": chkpntCPUCoreInterruptsTrap,
       "chkpntTrapMemory": chkpntTrapMemory,
       "chkpntSwapMemoryTrap": chkpntSwapMemoryTrap,
       "chkpntRealMemoryTrap": chkpntRealMemoryTrap,
       "chkpntTrapHWSensor": chkpntTrapHWSensor,
       "chkpntTrapTempertureSensor": chkpntTrapTempertureSensor,
       "chkpntTempertureTrap": chkpntTempertureTrap,
       "chkpntTrapFanSpeedSensor": chkpntTrapFanSpeedSensor,
       "chkpntFanSpeedTrap": chkpntFanSpeedTrap,
       "chkpntTrapVoltageSensor": chkpntTrapVoltageSensor,
       "chkpntVoltageTrap": chkpntVoltageTrap,
       "chkpntTrapHA": chkpntTrapHA,
       "chkpntClusterMemberStateTrap": chkpntClusterMemberStateTrap,
       "chkpntClusterBlockStateTrap": chkpntClusterBlockStateTrap,
       "chkpntClusterStateTrap": chkpntClusterStateTrap,
       "chkpntClusterProblemStateTrap": chkpntClusterProblemStateTrap,
       "chkpntClusterInterfaceStateTrap": chkpntClusterInterfaceStateTrap,
       "chkpntTrapLSConn": chkpntTrapLSConn,
       "chkpntTrapLSConnState": chkpntTrapLSConnState,
       "chkpntTrapOverallLSConnState": chkpntTrapOverallLSConnState,
       "chkpntTrapLocalLoggingState": chkpntTrapLocalLoggingState}
)
