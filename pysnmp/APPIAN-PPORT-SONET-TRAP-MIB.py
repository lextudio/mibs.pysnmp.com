# SNMP MIB module (APPIAN-PPORT-SONET-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APPIAN-PPORT-SONET-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:43 2024
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

(acChassisCurrentTime,
 acChassisRingId) = mibBuilder.importSymbols(
    "APPIAN-CHASSIS-MIB",
    "acChassisCurrentTime",
    "acChassisRingId")

(acSonet,
 acSonetFarEndLine,
 acSonetFarEndLine15MinuteIntervalNodeId,
 acSonetFarEndLine15MinuteIntervalNumber,
 acSonetFarEndLine15MinuteIntervalPort,
 acSonetFarEndLine15MinuteIntervalSlot,
 acSonetFarEndLineDayIntervalNodeId,
 acSonetFarEndLineDayIntervalNumber,
 acSonetFarEndLineDayIntervalPort,
 acSonetFarEndLineDayIntervalSlot,
 acSonetFarEndPath,
 acSonetFarEndPath15MinuteIntervalNodeId,
 acSonetFarEndPath15MinuteIntervalNumber,
 acSonetFarEndPath15MinuteIntervalPath,
 acSonetFarEndPath15MinuteIntervalPort,
 acSonetFarEndPath15MinuteIntervalSlot,
 acSonetFarEndPathDayIntervalNodeId,
 acSonetFarEndPathDayIntervalNumber,
 acSonetFarEndPathDayIntervalPath,
 acSonetFarEndPathDayIntervalPort,
 acSonetFarEndPathDayIntervalSlot,
 acSonetFarEndVT,
 acSonetFarEndVT15MinuteIntervalNodeId,
 acSonetFarEndVT15MinuteIntervalNumber,
 acSonetFarEndVT15MinuteIntervalPort,
 acSonetFarEndVT15MinuteIntervalSlot,
 acSonetFarEndVT15MinuteIntervalVT,
 acSonetFarEndVTDayIntervalNodeId,
 acSonetFarEndVTDayIntervalNumber,
 acSonetFarEndVTDayIntervalPort,
 acSonetFarEndVTDayIntervalSlot,
 acSonetFarEndVTDayIntervalVT,
 acSonetLine,
 acSonetLine15MinuteIntervalNodeId,
 acSonetLine15MinuteIntervalNumber,
 acSonetLine15MinuteIntervalPort,
 acSonetLine15MinuteIntervalSlot,
 acSonetLineDayIntervalNodeId,
 acSonetLineDayIntervalNumber,
 acSonetLineDayIntervalPort,
 acSonetLineDayIntervalSlot,
 acSonetLineProtectionNodeId,
 acSonetLineProtectionPort,
 acSonetLineProtectionSlot,
 acSonetPath,
 acSonetPath15MinuteIntervalNodeId,
 acSonetPath15MinuteIntervalNumber,
 acSonetPath15MinuteIntervalPath,
 acSonetPath15MinuteIntervalPort,
 acSonetPath15MinuteIntervalSlot,
 acSonetPathDayIntervalNodeId,
 acSonetPathDayIntervalNumber,
 acSonetPathDayIntervalPath,
 acSonetPathDayIntervalPort,
 acSonetPathDayIntervalSlot,
 acSonetPathPLMNodeId,
 acSonetPathPLMPath,
 acSonetPathPLMPort,
 acSonetPathPLMSlot,
 acSonetPathProtectionNodeId,
 acSonetPathProtectionPath,
 acSonetPathProtectionPort,
 acSonetPathProtectionSlot,
 acSonetPathTIMNodeId,
 acSonetPathTIMPath,
 acSonetPathTIMPort,
 acSonetPathTIMSlot,
 acSonetPort,
 acSonetPortNodeId,
 acSonetPortPort,
 acSonetPortSlot,
 acSonetSection,
 acSonetSection15MinuteIntervalNodeId,
 acSonetSection15MinuteIntervalNumber,
 acSonetSection15MinuteIntervalPort,
 acSonetSection15MinuteIntervalSlot,
 acSonetSectionDayIntervalNodeId,
 acSonetSectionDayIntervalNumber,
 acSonetSectionDayIntervalPort,
 acSonetSectionDayIntervalSlot,
 acSonetSectionTIMNodeId,
 acSonetSectionTIMPort,
 acSonetSectionTIMSlot,
 acSonetVT,
 acSonetVT15MinuteIntervalNodeId,
 acSonetVT15MinuteIntervalNumber,
 acSonetVT15MinuteIntervalPort,
 acSonetVT15MinuteIntervalSlot,
 acSonetVT15MinuteIntervalVT,
 acSonetVTDayIntervalNodeId,
 acSonetVTDayIntervalNumber,
 acSonetVTDayIntervalPort,
 acSonetVTDayIntervalSlot,
 acSonetVTDayIntervalVT,
 acSonetVTProtectionNodeId,
 acSonetVTProtectionPort,
 acSonetVTProtectionSlot,
 acSonetVTProtectionVT) = mibBuilder.importSymbols(
    "APPIAN-PPORT-SONET-MIB",
    "acSonet",
    "acSonetFarEndLine",
    "acSonetFarEndLine15MinuteIntervalNodeId",
    "acSonetFarEndLine15MinuteIntervalNumber",
    "acSonetFarEndLine15MinuteIntervalPort",
    "acSonetFarEndLine15MinuteIntervalSlot",
    "acSonetFarEndLineDayIntervalNodeId",
    "acSonetFarEndLineDayIntervalNumber",
    "acSonetFarEndLineDayIntervalPort",
    "acSonetFarEndLineDayIntervalSlot",
    "acSonetFarEndPath",
    "acSonetFarEndPath15MinuteIntervalNodeId",
    "acSonetFarEndPath15MinuteIntervalNumber",
    "acSonetFarEndPath15MinuteIntervalPath",
    "acSonetFarEndPath15MinuteIntervalPort",
    "acSonetFarEndPath15MinuteIntervalSlot",
    "acSonetFarEndPathDayIntervalNodeId",
    "acSonetFarEndPathDayIntervalNumber",
    "acSonetFarEndPathDayIntervalPath",
    "acSonetFarEndPathDayIntervalPort",
    "acSonetFarEndPathDayIntervalSlot",
    "acSonetFarEndVT",
    "acSonetFarEndVT15MinuteIntervalNodeId",
    "acSonetFarEndVT15MinuteIntervalNumber",
    "acSonetFarEndVT15MinuteIntervalPort",
    "acSonetFarEndVT15MinuteIntervalSlot",
    "acSonetFarEndVT15MinuteIntervalVT",
    "acSonetFarEndVTDayIntervalNodeId",
    "acSonetFarEndVTDayIntervalNumber",
    "acSonetFarEndVTDayIntervalPort",
    "acSonetFarEndVTDayIntervalSlot",
    "acSonetFarEndVTDayIntervalVT",
    "acSonetLine",
    "acSonetLine15MinuteIntervalNodeId",
    "acSonetLine15MinuteIntervalNumber",
    "acSonetLine15MinuteIntervalPort",
    "acSonetLine15MinuteIntervalSlot",
    "acSonetLineDayIntervalNodeId",
    "acSonetLineDayIntervalNumber",
    "acSonetLineDayIntervalPort",
    "acSonetLineDayIntervalSlot",
    "acSonetLineProtectionNodeId",
    "acSonetLineProtectionPort",
    "acSonetLineProtectionSlot",
    "acSonetPath",
    "acSonetPath15MinuteIntervalNodeId",
    "acSonetPath15MinuteIntervalNumber",
    "acSonetPath15MinuteIntervalPath",
    "acSonetPath15MinuteIntervalPort",
    "acSonetPath15MinuteIntervalSlot",
    "acSonetPathDayIntervalNodeId",
    "acSonetPathDayIntervalNumber",
    "acSonetPathDayIntervalPath",
    "acSonetPathDayIntervalPort",
    "acSonetPathDayIntervalSlot",
    "acSonetPathPLMNodeId",
    "acSonetPathPLMPath",
    "acSonetPathPLMPort",
    "acSonetPathPLMSlot",
    "acSonetPathProtectionNodeId",
    "acSonetPathProtectionPath",
    "acSonetPathProtectionPort",
    "acSonetPathProtectionSlot",
    "acSonetPathTIMNodeId",
    "acSonetPathTIMPath",
    "acSonetPathTIMPort",
    "acSonetPathTIMSlot",
    "acSonetPort",
    "acSonetPortNodeId",
    "acSonetPortPort",
    "acSonetPortSlot",
    "acSonetSection",
    "acSonetSection15MinuteIntervalNodeId",
    "acSonetSection15MinuteIntervalNumber",
    "acSonetSection15MinuteIntervalPort",
    "acSonetSection15MinuteIntervalSlot",
    "acSonetSectionDayIntervalNodeId",
    "acSonetSectionDayIntervalNumber",
    "acSonetSectionDayIntervalPort",
    "acSonetSectionDayIntervalSlot",
    "acSonetSectionTIMNodeId",
    "acSonetSectionTIMPort",
    "acSonetSectionTIMSlot",
    "acSonetVT",
    "acSonetVT15MinuteIntervalNodeId",
    "acSonetVT15MinuteIntervalNumber",
    "acSonetVT15MinuteIntervalPort",
    "acSonetVT15MinuteIntervalSlot",
    "acSonetVT15MinuteIntervalVT",
    "acSonetVTDayIntervalNodeId",
    "acSonetVTDayIntervalNumber",
    "acSonetVTDayIntervalPort",
    "acSonetVTDayIntervalSlot",
    "acSonetVTDayIntervalVT",
    "acSonetVTProtectionNodeId",
    "acSonetVTProtectionPort",
    "acSonetVTProtectionSlot",
    "acSonetVTProtectionVT")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

acSonetTraps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 4)
)
acSonetTraps.setRevisions(
        ("1900-03-04 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcSonetPortTraps_ObjectIdentity = ObjectIdentity
acSonetPortTraps = _AcSonetPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0)
)
_AcSonetSectionTraps_ObjectIdentity = ObjectIdentity
acSonetSectionTraps = _AcSonetSectionTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0)
)
_AcSonetLineTraps_ObjectIdentity = ObjectIdentity
acSonetLineTraps = _AcSonetLineTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0)
)
_AcSonetFarEndLineTraps_ObjectIdentity = ObjectIdentity
acSonetFarEndLineTraps = _AcSonetFarEndLineTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0)
)
_AcSonetPathTraps_ObjectIdentity = ObjectIdentity
acSonetPathTraps = _AcSonetPathTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0)
)
_AcSonetFarEndPathTraps_ObjectIdentity = ObjectIdentity
acSonetFarEndPathTraps = _AcSonetFarEndPathTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0)
)
_AcSonetVTTrap_ObjectIdentity = ObjectIdentity
acSonetVTTrap = _AcSonetVTTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0)
)
_AcSonetFarEndVTTraps_ObjectIdentity = ObjectIdentity
acSonetFarEndVTTraps = _AcSonetFarEndVTTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0)
)

# Managed Objects groups


# Notification objects

acSonetPortFacilityLoopbackActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 1)
)
acSonetPortFacilityLoopbackActiveTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortFacilityLoopbackActiveTrap.setStatus(
        "current"
    )

acSonetPortFacilityLoopbackClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 2)
)
acSonetPortFacilityLoopbackClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortFacilityLoopbackClearTrap.setStatus(
        "current"
    )

acSonetPortSectionDCCFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 3)
)
acSonetPortSectionDCCFailureAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortSectionDCCFailureAlarmTrap.setStatus(
        "current"
    )

acSonetPortSectionDCCFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 4)
)
acSonetPortSectionDCCFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortSectionDCCFailureClearTrap.setStatus(
        "current"
    )

acSonetPortLineDCCFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 5)
)
acSonetPortLineDCCFailureAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortLineDCCFailureAlarmTrap.setStatus(
        "current"
    )

acSonetPortLineDCCFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 6)
)
acSonetPortLineDCCFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortLineDCCFailureClearTrap.setStatus(
        "current"
    )

acSonetPortAppianDCCFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 7)
)
acSonetPortAppianDCCFailureAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortAppianDCCFailureAlarmTrap.setStatus(
        "current"
    )

acSonetPortAppianDCCFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 1, 0, 8)
)
acSonetPortAppianDCCFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPortPort"))
)
if mibBuilder.loadTexts:
    acSonetPortAppianDCCFailureClearTrap.setStatus(
        "current"
    )

acSonetSectionLOSAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 1)
)
acSonetSectionLOSAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOSAlarmTrap.setStatus(
        "current"
    )

acSonetSectionLOSClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 2)
)
acSonetSectionLOSClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOSClearTrap.setStatus(
        "current"
    )

acSonetSectionLOFAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 3)
)
acSonetSectionLOFAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOFAlarmTrap.setStatus(
        "current"
    )

acSonetSectionLOFClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 4)
)
acSonetSectionLOFClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionLOFClearTrap.setStatus(
        "current"
    )

acSonetSectionTraceAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 5)
)
acSonetSectionTraceAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMPort"))
)
if mibBuilder.loadTexts:
    acSonetSectionTraceAlarmTrap.setStatus(
        "current"
    )

acSonetSectionTraceClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 6)
)
acSonetSectionTraceClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionTIMPort"))
)
if mibBuilder.loadTexts:
    acSonetSectionTraceClearTrap.setStatus(
        "current"
    )

acSonetSection15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 7)
)
acSonetSection15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetSection15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 8)
)
acSonetSection15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetSection15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 9)
)
acSonetSection15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetSection15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 10)
)
acSonetSection15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetSection15MinuteSEFAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 11)
)
acSonetSection15MinuteSEFAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteSEFAlarmTrap.setStatus(
        "current"
    )

acSonetSection15MinuteSEFClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 12)
)
acSonetSection15MinuteSEFClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteSEFClearTrap.setStatus(
        "current"
    )

acSonetSection15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 13)
)
acSonetSection15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetSection15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 14)
)
acSonetSection15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSection15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSection15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetSectionDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 15)
)
acSonetSectionDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDayESAlarmTrap.setStatus(
        "current"
    )

acSonetSectionDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 16)
)
acSonetSectionDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDayESClearTrap.setStatus(
        "current"
    )

acSonetSectionDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 17)
)
acSonetSectionDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetSectionDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 18)
)
acSonetSectionDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDaySESClearTrap.setStatus(
        "current"
    )

acSonetSectionDaySEFAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 19)
)
acSonetSectionDaySEFAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDaySEFAlarmTrap.setStatus(
        "current"
    )

acSonetSectionDaySEFClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 20)
)
acSonetSectionDaySEFClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDaySEFClearTrap.setStatus(
        "current"
    )

acSonetSectionDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 21)
)
acSonetSectionDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetSectionDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 2, 0, 22)
)
acSonetSectionDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetSectionDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetSectionDayCVClearTrap.setStatus(
        "current"
    )

acSonetLineAISAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 1)
)
acSonetLineAISAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineAISAlarmTrap.setStatus(
        "current"
    )

acSonetLineAISClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 2)
)
acSonetLineAISClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineAISClearTrap.setStatus(
        "current"
    )

acSonetLineRDIAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 3)
)
acSonetLineRDIAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineRDIAlarmTrap.setStatus(
        "current"
    )

acSonetLineRDIClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 4)
)
acSonetLineRDIClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineRDIClearTrap.setStatus(
        "current"
    )

acSonetLine15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 5)
)
acSonetLine15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetLine15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 6)
)
acSonetLine15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetLine15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 7)
)
acSonetLine15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetLine15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 8)
)
acSonetLine15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetLine15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 9)
)
acSonetLine15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetLine15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 10)
)
acSonetLine15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetLine15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 11)
)
acSonetLine15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetLine15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 12)
)
acSonetLine15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLine15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetLineDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 13)
)
acSonetLineDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayESAlarmTrap.setStatus(
        "current"
    )

acSonetLineDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 14)
)
acSonetLineDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayESClearTrap.setStatus(
        "current"
    )

acSonetLineDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 15)
)
acSonetLineDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetLineDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 16)
)
acSonetLineDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDaySESClearTrap.setStatus(
        "current"
    )

acSonetLineDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 17)
)
acSonetLineDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetLineDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 18)
)
acSonetLineDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayCVClearTrap.setStatus(
        "current"
    )

acSonetLineDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 19)
)
acSonetLineDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetLineDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 20)
)
acSonetLineDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetLineDayUASClearTrap.setStatus(
        "current"
    )

acSonetLineProtectionSwitchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 21)
)
acSonetLineProtectionSwitchAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionSwitchAlarmTrap.setStatus(
        "current"
    )

acSonetLineProtectionSwitchClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 22)
)
acSonetLineProtectionSwitchClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionSwitchClearTrap.setStatus(
        "current"
    )

acSonetLineProtectionFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 23)
)
acSonetLineProtectionFailureAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionFailureAlarmTrap.setStatus(
        "current"
    )

acSonetLineProtectionFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 24)
)
acSonetLineProtectionFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionFailureClearTrap.setStatus(
        "current"
    )

acSonetLineProtectionChannelMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 25)
)
acSonetLineProtectionChannelMismatchAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionChannelMismatchAlarmTrap.setStatus(
        "current"
    )

acSonetLineProtectionChannelMismatchClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 26)
)
acSonetLineProtectionChannelMismatchClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionChannelMismatchClearTrap.setStatus(
        "current"
    )

acSonetLineProtectionModeMismatchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 27)
)
acSonetLineProtectionModeMismatchAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionModeMismatchAlarmTrap.setStatus(
        "current"
    )

acSonetLineProtectionModeMismatchClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 28)
)
acSonetLineProtectionModeMismatchClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionModeMismatchClearTrap.setStatus(
        "current"
    )

acSonetLineProtectionSwitchingByteFailureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 29)
)
acSonetLineProtectionSwitchingByteFailureAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionSwitchingByteFailureAlarmTrap.setStatus(
        "current"
    )

acSonetLineProtectionSwitchingByteFailureClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 3, 0, 30)
)
acSonetLineProtectionSwitchingByteFailureClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetLineProtectionPort"))
)
if mibBuilder.loadTexts:
    acSonetLineProtectionSwitchingByteFailureClearTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 1)
)
acSonetFarEndLine15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 2)
)
acSonetFarEndLine15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 3)
)
acSonetFarEndLine15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 4)
)
acSonetFarEndLine15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 5)
)
acSonetFarEndLine15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 6)
)
acSonetFarEndLine15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 7)
)
acSonetFarEndLine15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLine15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 8)
)
acSonetFarEndLine15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLine15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 9)
)
acSonetFarEndLineDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLine15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 10)
)
acSonetFarEndLineDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayESClearTrap.setStatus(
        "current"
    )

acSonetFarEndLineDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 11)
)
acSonetFarEndLineDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLineDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 12)
)
acSonetFarEndLineDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDaySESClearTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 13)
)
acSonetFarEndLineDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 14)
)
acSonetFarEndLineDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 15)
)
acSonetFarEndLineDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndLineDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 1, 4, 0, 16)
)
acSonetFarEndLineDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndLineDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndLineDayUASClearTrap.setStatus(
        "current"
    )

acSonetPathLOPAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 1)
)
acSonetPathLOPAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathLOPAlarmTrap.setStatus(
        "current"
    )

acSonetPathLOPClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 2)
)
acSonetPathLOPClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathLOPClearTrap.setStatus(
        "current"
    )

acSonetPathAISAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 3)
)
acSonetPathAISAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathAISAlarmTrap.setStatus(
        "current"
    )

acSonetPathAISClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 4)
)
acSonetPathAISClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathAISClearTrap.setStatus(
        "current"
    )

acSonetPathRDIAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 5)
)
acSonetPathRDIAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathRDIAlarmTrap.setStatus(
        "current"
    )

acSonetPathRDIClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 6)
)
acSonetPathRDIClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathRDIClearTrap.setStatus(
        "current"
    )

acSonetPathUnequipedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 7)
)
acSonetPathUnequipedAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathUnequipedAlarmTrap.setStatus(
        "current"
    )

acSonetPathUnequipedClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 8)
)
acSonetPathUnequipedClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathUnequipedClearTrap.setStatus(
        "current"
    )

acSonetPathTraceAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 9)
)
acSonetPathTraceAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPath"))
)
if mibBuilder.loadTexts:
    acSonetPathTraceAlarmTrap.setStatus(
        "current"
    )

acSonetPathTraceClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 10)
)
acSonetPathTraceClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathTIMPath"))
)
if mibBuilder.loadTexts:
    acSonetPathTraceClearTrap.setStatus(
        "current"
    )

acSonetPathPLMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 11)
)
acSonetPathPLMAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPath"))
)
if mibBuilder.loadTexts:
    acSonetPathPLMAlarmTrap.setStatus(
        "current"
    )

acSonetPathPLMClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 12)
)
acSonetPathPLMClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathPLMPath"))
)
if mibBuilder.loadTexts:
    acSonetPathPLMClearTrap.setStatus(
        "current"
    )

acSonetPathSDAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 13)
)
acSonetPathSDAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathSDAlarmTrap.setStatus(
        "current"
    )

acSonetPathSDClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 14)
)
acSonetPathSDClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathSDClearTrap.setStatus(
        "current"
    )

acSonetPathSFAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 15)
)
acSonetPathSFAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathSFAlarmTrap.setStatus(
        "current"
    )

acSonetPathSFClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 16)
)
acSonetPathSFClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathSFClearTrap.setStatus(
        "current"
    )

acSonetPath15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 17)
)
acSonetPath15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetPath15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 18)
)
acSonetPath15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetPath15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 19)
)
acSonetPath15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetPath15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 20)
)
acSonetPath15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetPath15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 21)
)
acSonetPath15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetPath15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 22)
)
acSonetPath15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetPath15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 23)
)
acSonetPath15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetPath15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 24)
)
acSonetPath15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPath15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetPathDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 25)
)
acSonetPathDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayESAlarmTrap.setStatus(
        "current"
    )

acSonetPathDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 26)
)
acSonetPathDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayESClearTrap.setStatus(
        "current"
    )

acSonetPathDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 27)
)
acSonetPathDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetPathDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 28)
)
acSonetPathDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDaySESClearTrap.setStatus(
        "current"
    )

acSonetPathDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 29)
)
acSonetPathDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetPathDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 30)
)
acSonetPathDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayCVClearTrap.setStatus(
        "current"
    )

acSonetPathDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 31)
)
acSonetPathDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetPathDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 32)
)
acSonetPathDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetPathDayUASClearTrap.setStatus(
        "current"
    )

acSonetPathRingProtAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 33)
)
acSonetPathRingProtAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPath"))
)
if mibBuilder.loadTexts:
    acSonetPathRingProtAlarmTrap.setStatus(
        "current"
    )

acSonetPathRingProtClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 1, 0, 34)
)
acSonetPathRingProtClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetPathProtectionPath"))
)
if mibBuilder.loadTexts:
    acSonetPathRingProtClearTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 1)
)
acSonetFarEndPath15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 2)
)
acSonetFarEndPath15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 3)
)
acSonetFarEndPath15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 4)
)
acSonetFarEndPath15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 5)
)
acSonetFarEndPath15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 6)
)
acSonetFarEndPath15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 7)
)
acSonetFarEndPath15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPath15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 8)
)
acSonetFarEndPath15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPath15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPath15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 9)
)
acSonetFarEndPathDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 10)
)
acSonetFarEndPathDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayESClearTrap.setStatus(
        "current"
    )

acSonetFarEndPathDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 11)
)
acSonetFarEndPathDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPathDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 12)
)
acSonetFarEndPathDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDaySESClearTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 13)
)
acSonetFarEndPathDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 14)
)
acSonetFarEndPathDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 15)
)
acSonetFarEndPathDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndPathDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 2, 2, 0, 16)
)
acSonetFarEndPathDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalPath"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndPathDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndPathDayUASClearTrap.setStatus(
        "current"
    )

acSonetVTLOPAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 1)
)
acSonetVTLOPAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTLOPAlarmTrap.setStatus(
        "current"
    )

acSonetVTLOPClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 2)
)
acSonetVTLOPClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTLOPClearTrap.setStatus(
        "current"
    )

acSonetVTPathAISAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 3)
)
acSonetVTPathAISAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPathAISAlarmTrap.setStatus(
        "current"
    )

acSonetVTPathAISClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 4)
)
acSonetVTPathAISClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPathAISClearTrap.setStatus(
        "current"
    )

acSonetVTPathRFIAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 5)
)
acSonetVTPathRFIAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPathRFIAlarmTrap.setStatus(
        "current"
    )

acSonetVTPathRFIClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 6)
)
acSonetVTPathRFIClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPathRFIClearTrap.setStatus(
        "current"
    )

acSonetVTUnequippedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 7)
)
acSonetVTUnequippedAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTUnequippedAlarmTrap.setStatus(
        "current"
    )

acSonetVTUnequippedClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 8)
)
acSonetVTUnequippedClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTUnequippedClearTrap.setStatus(
        "current"
    )

acSonetVTPLMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 9)
)
acSonetVTPLMAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPLMAlarmTrap.setStatus(
        "current"
    )

acSonetVTPLMClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 10)
)
acSonetVTPLMClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTPLMClearTrap.setStatus(
        "current"
    )

acSonetVTSDAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 11)
)
acSonetVTSDAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTSDAlarmTrap.setStatus(
        "current"
    )

acSonetVTSDClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 12)
)
acSonetVTSDClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTSDClearTrap.setStatus(
        "current"
    )

acSonetVTSFAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 13)
)
acSonetVTSFAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTSFAlarmTrap.setStatus(
        "current"
    )

acSonetVTSFClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 14)
)
acSonetVTSFClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTSFClearTrap.setStatus(
        "current"
    )

acSonetVT15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 15)
)
acSonetVT15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetVT15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 16)
)
acSonetVT15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetVT15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 17)
)
acSonetVT15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetVT15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 18)
)
acSonetVT15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetVT15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 19)
)
acSonetVT15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetVT15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 20)
)
acSonetVT15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetVT15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 21)
)
acSonetVT15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetVT15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 22)
)
acSonetVT15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVT15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetVTDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 23)
)
acSonetVTDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayESAlarmTrap.setStatus(
        "current"
    )

acSonetVTDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 24)
)
acSonetVTDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayESClearTrap.setStatus(
        "current"
    )

acSonetVTDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 25)
)
acSonetVTDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetVTDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 26)
)
acSonetVTDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDaySESClearTrap.setStatus(
        "current"
    )

acSonetVTDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 27)
)
acSonetVTDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetVTDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 28)
)
acSonetVTDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayCVClearTrap.setStatus(
        "current"
    )

acSonetVTDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 29)
)
acSonetVTDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetVTDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 30)
)
acSonetVTDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetVTDayUASClearTrap.setStatus(
        "current"
    )

acSonetVTRingProtSwitchAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 31)
)
acSonetVTRingProtSwitchAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionVT"))
)
if mibBuilder.loadTexts:
    acSonetVTRingProtSwitchAlarmTrap.setStatus(
        "current"
    )

acSonetVTRingProtSwitchClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 1, 0, 32)
)
acSonetVTRingProtSwitchClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetVTProtectionVT"))
)
if mibBuilder.loadTexts:
    acSonetVTRingProtSwitchClearTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 1)
)
acSonetFarEndVT15MinuteESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 2)
)
acSonetFarEndVT15MinuteESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteESClearTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteSESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 3)
)
acSonetFarEndVT15MinuteSESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteSESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteSESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 4)
)
acSonetFarEndVT15MinuteSESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteSESClearTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 5)
)
acSonetFarEndVT15MinuteCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 6)
)
acSonetFarEndVT15MinuteCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 7)
)
acSonetFarEndVT15MinuteUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVT15MinuteUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 8)
)
acSonetFarEndVT15MinuteUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVT15MinuteIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVT15MinuteUASClearTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 9)
)
acSonetFarEndVTDayESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 10)
)
acSonetFarEndVTDayESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayESClearTrap.setStatus(
        "current"
    )

acSonetFarEndVTDaySESAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 11)
)
acSonetFarEndVTDaySESAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDaySESAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVTDaySESClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 12)
)
acSonetFarEndVTDaySESClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDaySESClearTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayCVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 13)
)
acSonetFarEndVTDayCVAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayCVAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayCVClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 14)
)
acSonetFarEndVTDayCVClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayCVClearTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayUASAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 15)
)
acSonetFarEndVTDayUASAlarmTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayUASAlarmTrap.setStatus(
        "current"
    )

acSonetFarEndVTDayUASClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 6, 3, 2, 0, 16)
)
acSonetFarEndVTDayUASClearTrap.setObjects(
      *(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"),
        ("APPIAN-CHASSIS-MIB", "acChassisRingId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNodeId"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalSlot"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalPort"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalVT"),
        ("APPIAN-PPORT-SONET-MIB", "acSonetFarEndVTDayIntervalNumber"))
)
if mibBuilder.loadTexts:
    acSonetFarEndVTDayUASClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APPIAN-PPORT-SONET-TRAP-MIB",
    **{"acSonetPortTraps": acSonetPortTraps,
       "acSonetPortFacilityLoopbackActiveTrap": acSonetPortFacilityLoopbackActiveTrap,
       "acSonetPortFacilityLoopbackClearTrap": acSonetPortFacilityLoopbackClearTrap,
       "acSonetPortSectionDCCFailureAlarmTrap": acSonetPortSectionDCCFailureAlarmTrap,
       "acSonetPortSectionDCCFailureClearTrap": acSonetPortSectionDCCFailureClearTrap,
       "acSonetPortLineDCCFailureAlarmTrap": acSonetPortLineDCCFailureAlarmTrap,
       "acSonetPortLineDCCFailureClearTrap": acSonetPortLineDCCFailureClearTrap,
       "acSonetPortAppianDCCFailureAlarmTrap": acSonetPortAppianDCCFailureAlarmTrap,
       "acSonetPortAppianDCCFailureClearTrap": acSonetPortAppianDCCFailureClearTrap,
       "acSonetSectionTraps": acSonetSectionTraps,
       "acSonetSectionLOSAlarmTrap": acSonetSectionLOSAlarmTrap,
       "acSonetSectionLOSClearTrap": acSonetSectionLOSClearTrap,
       "acSonetSectionLOFAlarmTrap": acSonetSectionLOFAlarmTrap,
       "acSonetSectionLOFClearTrap": acSonetSectionLOFClearTrap,
       "acSonetSectionTraceAlarmTrap": acSonetSectionTraceAlarmTrap,
       "acSonetSectionTraceClearTrap": acSonetSectionTraceClearTrap,
       "acSonetSection15MinuteESAlarmTrap": acSonetSection15MinuteESAlarmTrap,
       "acSonetSection15MinuteESClearTrap": acSonetSection15MinuteESClearTrap,
       "acSonetSection15MinuteSESAlarmTrap": acSonetSection15MinuteSESAlarmTrap,
       "acSonetSection15MinuteSESClearTrap": acSonetSection15MinuteSESClearTrap,
       "acSonetSection15MinuteSEFAlarmTrap": acSonetSection15MinuteSEFAlarmTrap,
       "acSonetSection15MinuteSEFClearTrap": acSonetSection15MinuteSEFClearTrap,
       "acSonetSection15MinuteCVAlarmTrap": acSonetSection15MinuteCVAlarmTrap,
       "acSonetSection15MinuteCVClearTrap": acSonetSection15MinuteCVClearTrap,
       "acSonetSectionDayESAlarmTrap": acSonetSectionDayESAlarmTrap,
       "acSonetSectionDayESClearTrap": acSonetSectionDayESClearTrap,
       "acSonetSectionDaySESAlarmTrap": acSonetSectionDaySESAlarmTrap,
       "acSonetSectionDaySESClearTrap": acSonetSectionDaySESClearTrap,
       "acSonetSectionDaySEFAlarmTrap": acSonetSectionDaySEFAlarmTrap,
       "acSonetSectionDaySEFClearTrap": acSonetSectionDaySEFClearTrap,
       "acSonetSectionDayCVAlarmTrap": acSonetSectionDayCVAlarmTrap,
       "acSonetSectionDayCVClearTrap": acSonetSectionDayCVClearTrap,
       "acSonetLineTraps": acSonetLineTraps,
       "acSonetLineAISAlarmTrap": acSonetLineAISAlarmTrap,
       "acSonetLineAISClearTrap": acSonetLineAISClearTrap,
       "acSonetLineRDIAlarmTrap": acSonetLineRDIAlarmTrap,
       "acSonetLineRDIClearTrap": acSonetLineRDIClearTrap,
       "acSonetLine15MinuteESAlarmTrap": acSonetLine15MinuteESAlarmTrap,
       "acSonetLine15MinuteESClearTrap": acSonetLine15MinuteESClearTrap,
       "acSonetLine15MinuteSESAlarmTrap": acSonetLine15MinuteSESAlarmTrap,
       "acSonetLine15MinuteSESClearTrap": acSonetLine15MinuteSESClearTrap,
       "acSonetLine15MinuteCVAlarmTrap": acSonetLine15MinuteCVAlarmTrap,
       "acSonetLine15MinuteCVClearTrap": acSonetLine15MinuteCVClearTrap,
       "acSonetLine15MinuteUASAlarmTrap": acSonetLine15MinuteUASAlarmTrap,
       "acSonetLine15MinuteUASClearTrap": acSonetLine15MinuteUASClearTrap,
       "acSonetLineDayESAlarmTrap": acSonetLineDayESAlarmTrap,
       "acSonetLineDayESClearTrap": acSonetLineDayESClearTrap,
       "acSonetLineDaySESAlarmTrap": acSonetLineDaySESAlarmTrap,
       "acSonetLineDaySESClearTrap": acSonetLineDaySESClearTrap,
       "acSonetLineDayCVAlarmTrap": acSonetLineDayCVAlarmTrap,
       "acSonetLineDayCVClearTrap": acSonetLineDayCVClearTrap,
       "acSonetLineDayUASAlarmTrap": acSonetLineDayUASAlarmTrap,
       "acSonetLineDayUASClearTrap": acSonetLineDayUASClearTrap,
       "acSonetLineProtectionSwitchAlarmTrap": acSonetLineProtectionSwitchAlarmTrap,
       "acSonetLineProtectionSwitchClearTrap": acSonetLineProtectionSwitchClearTrap,
       "acSonetLineProtectionFailureAlarmTrap": acSonetLineProtectionFailureAlarmTrap,
       "acSonetLineProtectionFailureClearTrap": acSonetLineProtectionFailureClearTrap,
       "acSonetLineProtectionChannelMismatchAlarmTrap": acSonetLineProtectionChannelMismatchAlarmTrap,
       "acSonetLineProtectionChannelMismatchClearTrap": acSonetLineProtectionChannelMismatchClearTrap,
       "acSonetLineProtectionModeMismatchAlarmTrap": acSonetLineProtectionModeMismatchAlarmTrap,
       "acSonetLineProtectionModeMismatchClearTrap": acSonetLineProtectionModeMismatchClearTrap,
       "acSonetLineProtectionSwitchingByteFailureAlarmTrap": acSonetLineProtectionSwitchingByteFailureAlarmTrap,
       "acSonetLineProtectionSwitchingByteFailureClearTrap": acSonetLineProtectionSwitchingByteFailureClearTrap,
       "acSonetFarEndLineTraps": acSonetFarEndLineTraps,
       "acSonetFarEndLine15MinuteESAlarmTrap": acSonetFarEndLine15MinuteESAlarmTrap,
       "acSonetFarEndLine15MinuteESClearTrap": acSonetFarEndLine15MinuteESClearTrap,
       "acSonetFarEndLine15MinuteSESAlarmTrap": acSonetFarEndLine15MinuteSESAlarmTrap,
       "acSonetFarEndLine15MinuteSESClearTrap": acSonetFarEndLine15MinuteSESClearTrap,
       "acSonetFarEndLine15MinuteCVAlarmTrap": acSonetFarEndLine15MinuteCVAlarmTrap,
       "acSonetFarEndLine15MinuteCVClearTrap": acSonetFarEndLine15MinuteCVClearTrap,
       "acSonetFarEndLine15MinuteUASAlarmTrap": acSonetFarEndLine15MinuteUASAlarmTrap,
       "acSonetFarEndLine15MinuteUASClearTrap": acSonetFarEndLine15MinuteUASClearTrap,
       "acSonetFarEndLineDayESAlarmTrap": acSonetFarEndLineDayESAlarmTrap,
       "acSonetFarEndLineDayESClearTrap": acSonetFarEndLineDayESClearTrap,
       "acSonetFarEndLineDaySESAlarmTrap": acSonetFarEndLineDaySESAlarmTrap,
       "acSonetFarEndLineDaySESClearTrap": acSonetFarEndLineDaySESClearTrap,
       "acSonetFarEndLineDayCVAlarmTrap": acSonetFarEndLineDayCVAlarmTrap,
       "acSonetFarEndLineDayCVClearTrap": acSonetFarEndLineDayCVClearTrap,
       "acSonetFarEndLineDayUASAlarmTrap": acSonetFarEndLineDayUASAlarmTrap,
       "acSonetFarEndLineDayUASClearTrap": acSonetFarEndLineDayUASClearTrap,
       "acSonetPathTraps": acSonetPathTraps,
       "acSonetPathLOPAlarmTrap": acSonetPathLOPAlarmTrap,
       "acSonetPathLOPClearTrap": acSonetPathLOPClearTrap,
       "acSonetPathAISAlarmTrap": acSonetPathAISAlarmTrap,
       "acSonetPathAISClearTrap": acSonetPathAISClearTrap,
       "acSonetPathRDIAlarmTrap": acSonetPathRDIAlarmTrap,
       "acSonetPathRDIClearTrap": acSonetPathRDIClearTrap,
       "acSonetPathUnequipedAlarmTrap": acSonetPathUnequipedAlarmTrap,
       "acSonetPathUnequipedClearTrap": acSonetPathUnequipedClearTrap,
       "acSonetPathTraceAlarmTrap": acSonetPathTraceAlarmTrap,
       "acSonetPathTraceClearTrap": acSonetPathTraceClearTrap,
       "acSonetPathPLMAlarmTrap": acSonetPathPLMAlarmTrap,
       "acSonetPathPLMClearTrap": acSonetPathPLMClearTrap,
       "acSonetPathSDAlarmTrap": acSonetPathSDAlarmTrap,
       "acSonetPathSDClearTrap": acSonetPathSDClearTrap,
       "acSonetPathSFAlarmTrap": acSonetPathSFAlarmTrap,
       "acSonetPathSFClearTrap": acSonetPathSFClearTrap,
       "acSonetPath15MinuteESAlarmTrap": acSonetPath15MinuteESAlarmTrap,
       "acSonetPath15MinuteESClearTrap": acSonetPath15MinuteESClearTrap,
       "acSonetPath15MinuteSESAlarmTrap": acSonetPath15MinuteSESAlarmTrap,
       "acSonetPath15MinuteSESClearTrap": acSonetPath15MinuteSESClearTrap,
       "acSonetPath15MinuteCVAlarmTrap": acSonetPath15MinuteCVAlarmTrap,
       "acSonetPath15MinuteCVClearTrap": acSonetPath15MinuteCVClearTrap,
       "acSonetPath15MinuteUASAlarmTrap": acSonetPath15MinuteUASAlarmTrap,
       "acSonetPath15MinuteUASClearTrap": acSonetPath15MinuteUASClearTrap,
       "acSonetPathDayESAlarmTrap": acSonetPathDayESAlarmTrap,
       "acSonetPathDayESClearTrap": acSonetPathDayESClearTrap,
       "acSonetPathDaySESAlarmTrap": acSonetPathDaySESAlarmTrap,
       "acSonetPathDaySESClearTrap": acSonetPathDaySESClearTrap,
       "acSonetPathDayCVAlarmTrap": acSonetPathDayCVAlarmTrap,
       "acSonetPathDayCVClearTrap": acSonetPathDayCVClearTrap,
       "acSonetPathDayUASAlarmTrap": acSonetPathDayUASAlarmTrap,
       "acSonetPathDayUASClearTrap": acSonetPathDayUASClearTrap,
       "acSonetPathRingProtAlarmTrap": acSonetPathRingProtAlarmTrap,
       "acSonetPathRingProtClearTrap": acSonetPathRingProtClearTrap,
       "acSonetFarEndPathTraps": acSonetFarEndPathTraps,
       "acSonetFarEndPath15MinuteESAlarmTrap": acSonetFarEndPath15MinuteESAlarmTrap,
       "acSonetFarEndPath15MinuteESClearTrap": acSonetFarEndPath15MinuteESClearTrap,
       "acSonetFarEndPath15MinuteSESAlarmTrap": acSonetFarEndPath15MinuteSESAlarmTrap,
       "acSonetFarEndPath15MinuteSESClearTrap": acSonetFarEndPath15MinuteSESClearTrap,
       "acSonetFarEndPath15MinuteCVAlarmTrap": acSonetFarEndPath15MinuteCVAlarmTrap,
       "acSonetFarEndPath15MinuteCVClearTrap": acSonetFarEndPath15MinuteCVClearTrap,
       "acSonetFarEndPath15MinuteUASAlarmTrap": acSonetFarEndPath15MinuteUASAlarmTrap,
       "acSonetFarEndPath15MinuteUASClearTrap": acSonetFarEndPath15MinuteUASClearTrap,
       "acSonetFarEndPathDayESAlarmTrap": acSonetFarEndPathDayESAlarmTrap,
       "acSonetFarEndPathDayESClearTrap": acSonetFarEndPathDayESClearTrap,
       "acSonetFarEndPathDaySESAlarmTrap": acSonetFarEndPathDaySESAlarmTrap,
       "acSonetFarEndPathDaySESClearTrap": acSonetFarEndPathDaySESClearTrap,
       "acSonetFarEndPathDayCVAlarmTrap": acSonetFarEndPathDayCVAlarmTrap,
       "acSonetFarEndPathDayCVClearTrap": acSonetFarEndPathDayCVClearTrap,
       "acSonetFarEndPathDayUASAlarmTrap": acSonetFarEndPathDayUASAlarmTrap,
       "acSonetFarEndPathDayUASClearTrap": acSonetFarEndPathDayUASClearTrap,
       "acSonetVTTrap": acSonetVTTrap,
       "acSonetVTLOPAlarmTrap": acSonetVTLOPAlarmTrap,
       "acSonetVTLOPClearTrap": acSonetVTLOPClearTrap,
       "acSonetVTPathAISAlarmTrap": acSonetVTPathAISAlarmTrap,
       "acSonetVTPathAISClearTrap": acSonetVTPathAISClearTrap,
       "acSonetVTPathRFIAlarmTrap": acSonetVTPathRFIAlarmTrap,
       "acSonetVTPathRFIClearTrap": acSonetVTPathRFIClearTrap,
       "acSonetVTUnequippedAlarmTrap": acSonetVTUnequippedAlarmTrap,
       "acSonetVTUnequippedClearTrap": acSonetVTUnequippedClearTrap,
       "acSonetVTPLMAlarmTrap": acSonetVTPLMAlarmTrap,
       "acSonetVTPLMClearTrap": acSonetVTPLMClearTrap,
       "acSonetVTSDAlarmTrap": acSonetVTSDAlarmTrap,
       "acSonetVTSDClearTrap": acSonetVTSDClearTrap,
       "acSonetVTSFAlarmTrap": acSonetVTSFAlarmTrap,
       "acSonetVTSFClearTrap": acSonetVTSFClearTrap,
       "acSonetVT15MinuteESAlarmTrap": acSonetVT15MinuteESAlarmTrap,
       "acSonetVT15MinuteESClearTrap": acSonetVT15MinuteESClearTrap,
       "acSonetVT15MinuteSESAlarmTrap": acSonetVT15MinuteSESAlarmTrap,
       "acSonetVT15MinuteSESClearTrap": acSonetVT15MinuteSESClearTrap,
       "acSonetVT15MinuteCVAlarmTrap": acSonetVT15MinuteCVAlarmTrap,
       "acSonetVT15MinuteCVClearTrap": acSonetVT15MinuteCVClearTrap,
       "acSonetVT15MinuteUASAlarmTrap": acSonetVT15MinuteUASAlarmTrap,
       "acSonetVT15MinuteUASClearTrap": acSonetVT15MinuteUASClearTrap,
       "acSonetVTDayESAlarmTrap": acSonetVTDayESAlarmTrap,
       "acSonetVTDayESClearTrap": acSonetVTDayESClearTrap,
       "acSonetVTDaySESAlarmTrap": acSonetVTDaySESAlarmTrap,
       "acSonetVTDaySESClearTrap": acSonetVTDaySESClearTrap,
       "acSonetVTDayCVAlarmTrap": acSonetVTDayCVAlarmTrap,
       "acSonetVTDayCVClearTrap": acSonetVTDayCVClearTrap,
       "acSonetVTDayUASAlarmTrap": acSonetVTDayUASAlarmTrap,
       "acSonetVTDayUASClearTrap": acSonetVTDayUASClearTrap,
       "acSonetVTRingProtSwitchAlarmTrap": acSonetVTRingProtSwitchAlarmTrap,
       "acSonetVTRingProtSwitchClearTrap": acSonetVTRingProtSwitchClearTrap,
       "acSonetFarEndVTTraps": acSonetFarEndVTTraps,
       "acSonetFarEndVT15MinuteESAlarmTrap": acSonetFarEndVT15MinuteESAlarmTrap,
       "acSonetFarEndVT15MinuteESClearTrap": acSonetFarEndVT15MinuteESClearTrap,
       "acSonetFarEndVT15MinuteSESAlarmTrap": acSonetFarEndVT15MinuteSESAlarmTrap,
       "acSonetFarEndVT15MinuteSESClearTrap": acSonetFarEndVT15MinuteSESClearTrap,
       "acSonetFarEndVT15MinuteCVAlarmTrap": acSonetFarEndVT15MinuteCVAlarmTrap,
       "acSonetFarEndVT15MinuteCVClearTrap": acSonetFarEndVT15MinuteCVClearTrap,
       "acSonetFarEndVT15MinuteUASAlarmTrap": acSonetFarEndVT15MinuteUASAlarmTrap,
       "acSonetFarEndVT15MinuteUASClearTrap": acSonetFarEndVT15MinuteUASClearTrap,
       "acSonetFarEndVTDayESAlarmTrap": acSonetFarEndVTDayESAlarmTrap,
       "acSonetFarEndVTDayESClearTrap": acSonetFarEndVTDayESClearTrap,
       "acSonetFarEndVTDaySESAlarmTrap": acSonetFarEndVTDaySESAlarmTrap,
       "acSonetFarEndVTDaySESClearTrap": acSonetFarEndVTDaySESClearTrap,
       "acSonetFarEndVTDayCVAlarmTrap": acSonetFarEndVTDayCVAlarmTrap,
       "acSonetFarEndVTDayCVClearTrap": acSonetFarEndVTDayCVClearTrap,
       "acSonetFarEndVTDayUASAlarmTrap": acSonetFarEndVTDayUASAlarmTrap,
       "acSonetFarEndVTDayUASClearTrap": acSonetFarEndVTDayUASClearTrap,
       "acSonetTraps": acSonetTraps}
)
