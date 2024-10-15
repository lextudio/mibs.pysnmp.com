# SNMP MIB module (HUAWEI-DC-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-DC-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:27 2024
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

(entPhysicalName,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalName")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwDCTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwDCTrapControl_ObjectIdentity = ObjectIdentity
hwDCTrapControl = _HwDCTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 1)
)


class _HwDCCtrlTrap_Type(OctetString):
    """Custom type hwDCCtrlTrap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HwDCCtrlTrap_Type.__name__ = "OctetString"
_HwDCCtrlTrap_Object = MibScalar
hwDCCtrlTrap = _HwDCCtrlTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 1, 1),
    _HwDCCtrlTrap_Type()
)
hwDCCtrlTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDCCtrlTrap.setStatus("current")


class _HwTunnelGroupID_Type(Integer32):
    """Custom type hwTunnelGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_HwTunnelGroupID_Type.__name__ = "Integer32"
_HwTunnelGroupID_Object = MibScalar
hwTunnelGroupID = _HwTunnelGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 1, 2),
    _HwTunnelGroupID_Type()
)
hwTunnelGroupID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTunnelGroupID.setStatus("current")
_HwDCTrapReason_Type = DisplayString
_HwDCTrapReason_Object = MibScalar
hwDCTrapReason = _HwDCTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 1, 3),
    _HwDCTrapReason_Type()
)
hwDCTrapReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDCTrapReason.setStatus("current")
_HwDCTraps_ObjectIdentity = ObjectIdentity
hwDCTraps = _HwDCTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2)
)
_HwDCTrapConformance_ObjectIdentity = ObjectIdentity
hwDCTrapConformance = _HwDCTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3)
)
_HwDCTrapGroups_ObjectIdentity = ObjectIdentity
hwDCTrapGroups = _HwDCTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3, 1)
)
_HwDCTrapCompliances_ObjectIdentity = ObjectIdentity
hwDCTrapCompliances = _HwDCTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3, 2)
)

# Managed Objects groups

hwDCTrapControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3, 1, 1)
)
hwDCTrapControlGroup.setObjects(
      *(("HUAWEI-DC-TRAP-MIB", "hwDCCtrlTrap"),
        ("HUAWEI-DC-TRAP-MIB", "hwTunnelGroupID"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwDCTrapControlGroup.setStatus("current")


# Notification objects

hwMPUSynClkFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 1)
)
hwMPUSynClkFaulty.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMPUSynClkFaulty.setStatus(
        "current"
    )

hwMPUSynClkFaultyResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 2)
)
hwMPUSynClkFaultyResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMPUSynClkFaultyResume.setStatus(
        "current"
    )

hwSlaveMPUNoResp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 3)
)
hwSlaveMPUNoResp.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSlaveMPUNoResp.setStatus(
        "current"
    )

hwSlaveMPUNoRespResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 4)
)
hwSlaveMPUNoRespResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSlaveMPUNoRespResume.setStatus(
        "current"
    )

hwBrdChannelFaulty = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 5)
)
hwBrdChannelFaulty.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdChannelFaulty.setStatus(
        "current"
    )

hwBrdChannelFaultyResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 6)
)
hwBrdChannelFaultyResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdChannelFaultyResume.setStatus(
        "current"
    )

hwBrdNofullin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 7)
)
hwBrdNofullin.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdNofullin.setStatus(
        "current"
    )

hwBrdNofullinResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 8)
)
hwBrdNofullinResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdNofullinResume.setStatus(
        "current"
    )

hwBrdTypeNoMatchReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 9)
)
hwBrdTypeNoMatchReset.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdTypeNoMatchReset.setStatus(
        "current"
    )

hwBrdAutoSwtFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 10)
)
hwBrdAutoSwtFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdAutoSwtFail.setStatus(
        "current"
    )

hwBrdAutoSwt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 11)
)
hwBrdAutoSwt.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdAutoSwt.setStatus(
        "current"
    )

hwBrdClkLockERR = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 12)
)
hwBrdClkLockERR.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdClkLockERR.setStatus(
        "current"
    )

hwBrdClkLockERRResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 13)
)
hwBrdClkLockERRResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdClkLockERRResume.setStatus(
        "current"
    )

hwBrdRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 14)
)
hwBrdRemoved.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdRemoved.setStatus(
        "current"
    )

hwBrdInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 15)
)
hwBrdInserted.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdInserted.setStatus(
        "current"
    )

hwBrdUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 16)
)
hwBrdUp.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBrdUp.setStatus(
        "current"
    )

hwClkSrcMiss = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 17)
)
hwClkSrcMiss.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkSrcMiss.setStatus(
        "current"
    )

hwClkAllSrcLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 18)
)
hwClkAllSrcLost.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkAllSrcLost.setStatus(
        "current"
    )

hwClkAllSrcLostResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 19)
)
hwClkAllSrcLostResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkAllSrcLostResume.setStatus(
        "current"
    )

hwClkFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 20)
)
hwClkFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkFail.setStatus(
        "current"
    )

hwClkFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 21)
)
hwClkFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkFailResume.setStatus(
        "current"
    )

hwClkNoHeartbeat = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 22)
)
hwClkNoHeartbeat.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkNoHeartbeat.setStatus(
        "current"
    )

hwClkNoHeartbeatResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 23)
)
hwClkNoHeartbeatResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwClkNoHeartbeatResume.setStatus(
        "current"
    )

hwLPULostSynAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 24)
)
hwLPULostSynAlarm.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLPULostSynAlarm.setStatus(
        "current"
    )

hwLPUOpenChannelError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 25)
)
hwLPUOpenChannelError.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLPUOpenChannelError.setStatus(
        "current"
    )

hwLPUSlfTstErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 26)
)
hwLPUSlfTstErr.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLPUSlfTstErr.setStatus(
        "current"
    )

hwLPU3ClkSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 27)
)
hwLPU3ClkSwitch.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLPU3ClkSwitch.setStatus(
        "current"
    )

hwSFULostHrtReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 28)
)
hwSFULostHrtReset.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSFULostHrtReset.setStatus(
        "current"
    )

hwSFULinkLostReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 29)
)
hwSFULinkLostReset.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSFULinkLostReset.setStatus(
        "current"
    )

hwSFUChannelLinkLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 30)
)
hwSFUChannelLinkLost.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSFUChannelLinkLost.setStatus(
        "current"
    )

hwSFUInChannelOpenFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 31)
)
hwSFUInChannelOpenFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSFUInChannelOpenFail.setStatus(
        "current"
    )

hwVoltSensorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 32)
)
hwVoltSensorFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSensorFail.setStatus(
        "current"
    )

hwVoltSensorFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 33)
)
hwVoltSensorFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSensorFailResume.setStatus(
        "current"
    )

hwVoltBtmC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 34)
)
hwVoltBtmC.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltBtmC.setStatus(
        "current"
    )

hwVoltBtmCResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 35)
)
hwVoltBtmCResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltBtmCResume.setStatus(
        "current"
    )

hwVoltSprC = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 36)
)
hwVoltSprC.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSprC.setStatus(
        "current"
    )

hwVoltSprCResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 37)
)
hwVoltSprCResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSprCResume.setStatus(
        "current"
    )

hwVoltBtmM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 38)
)
hwVoltBtmM.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltBtmM.setStatus(
        "current"
    )

hwVoltBtmMResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 39)
)
hwVoltBtmMResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltBtmMResume.setStatus(
        "current"
    )

hwVoltSprM = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 40)
)
hwVoltSprM.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSprM.setStatus(
        "current"
    )

hwVoltSprMResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 41)
)
hwVoltSprMResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwVoltSprMResume.setStatus(
        "current"
    )

hwTempSensorFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 42)
)
hwTempSensorFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempSensorFail.setStatus(
        "current"
    )

hwTempSensorFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 43)
)
hwTempSensorFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempSensorFailResume.setStatus(
        "current"
    )

hwTempMnr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 44)
)
hwTempMnr.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempMnr.setStatus(
        "current"
    )

hwTempMnrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 45)
)
hwTempMnrResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempMnrResume.setStatus(
        "current"
    )

hwTempMjr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 46)
)
hwTempMjr.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempMjr.setStatus(
        "current"
    )

hwTempMjrResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 47)
)
hwTempMjrResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempMjrResume.setStatus(
        "current"
    )

hwTempCtl = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 48)
)
hwTempCtl.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempCtl.setStatus(
        "current"
    )

hwTempCtlResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 49)
)
hwTempCtlResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempCtlResume.setStatus(
        "current"
    )

hwFanHFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 50)
)
hwFanHFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanHFail.setStatus(
        "current"
    )

hwFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 51)
)
hwFanFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanFail.setStatus(
        "current"
    )

hwFanFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 52)
)
hwFanFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanFailResume.setStatus(
        "current"
    )

hwFanAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 53)
)
hwFanAbsent.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanAbsent.setStatus(
        "current"
    )

hwFanAbsentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 54)
)
hwFanAbsentResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanAbsentResume.setStatus(
        "current"
    )

hwFanCabUN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 55)
)
hwFanCabUN.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanCabUN.setStatus(
        "current"
    )

hwFanCabUNResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 56)
)
hwFanCabUNResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanCabUNResume.setStatus(
        "current"
    )

hwPwrFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 57)
)
hwPwrFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrFail.setStatus(
        "current"
    )

hwPwrFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 58)
)
hwPwrFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrFailResume.setStatus(
        "current"
    )

hwPwrAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 59)
)
hwPwrAbsent.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrAbsent.setStatus(
        "current"
    )

hwPwrAbsentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 60)
)
hwPwrAbsentResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrAbsentResume.setStatus(
        "current"
    )

hwPwrCabUN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 61)
)
hwPwrCabUN.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrCabUN.setStatus(
        "current"
    )

hwPwrCabUNResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 62)
)
hwPwrCabUNResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPwrCabUNResume.setStatus(
        "current"
    )

hwLCDHFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 63)
)
hwLCDHFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDHFail.setStatus(
        "current"
    )

hwLCDFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 64)
)
hwLCDFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDFail.setStatus(
        "current"
    )

hwLCDAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 65)
)
hwLCDAbsent.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDAbsent.setStatus(
        "current"
    )

hwLCDAbsentResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 66)
)
hwLCDAbsentResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDAbsentResume.setStatus(
        "current"
    )

hwLCDCabUN = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 67)
)
hwLCDCabUN.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDCabUN.setStatus(
        "current"
    )

hwLCDCabUNResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 68)
)
hwLCDCabUNResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLCDCabUNResume.setStatus(
        "current"
    )

hwROMFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 69)
)
hwROMFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwROMFail.setStatus(
        "current"
    )

hwMonitorBUSFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 70)
)
hwMonitorBUSFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMonitorBUSFail.setStatus(
        "current"
    )

hwMonitorBUSFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 71)
)
hwMonitorBUSFailResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMonitorBUSFailResume.setStatus(
        "current"
    )

hwBoardOfflineChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 72)
)
hwBoardOfflineChange.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBoardOfflineChange.setStatus(
        "current"
    )

hwWriteFlashError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 100)
)
hwWriteFlashError.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwWriteFlashError.setStatus(
        "current"
    )

hwBoardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 101)
)
hwBoardReset.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBoardReset.setStatus(
        "current"
    )

hwBoardResetSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 102)
)
hwBoardResetSuccess.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBoardResetSuccess.setStatus(
        "current"
    )

hwSlaveMPUReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 103)
)
hwSlaveMPUReset.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSlaveMPUReset.setStatus(
        "current"
    )

hwMasterSlaveSwap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 104)
)
hwMasterSlaveSwap.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMasterSlaveSwap.setStatus(
        "current"
    )

hwRTCFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 105)
)
hwRTCFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwRTCFail.setStatus(
        "current"
    )

hwExchangeChipFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 106)
)
hwExchangeChipFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwExchangeChipFail.setStatus(
        "current"
    )

hwTempResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 107)
)
hwTempResume.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwTempResume.setStatus(
        "current"
    )

hwOpticalModuleInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 108)
)
hwOpticalModuleInsert.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwOpticalModuleInsert.setStatus(
        "current"
    )

hwOpticalModuleRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 109)
)
hwOpticalModuleRemove.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwOpticalModuleRemove.setStatus(
        "current"
    )

hwFPGAAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 110)
)
hwFPGAAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFPGAAbnormal.setStatus(
        "current"
    )

hwMinMTunnelDownAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 111)
)
hwMinMTunnelDownAlarm.setObjects(
    ("HUAWEI-DC-TRAP-MIB", "hwTunnelGroupID")
)
if mibBuilder.loadTexts:
    hwMinMTunnelDownAlarm.setStatus(
        "current"
    )

hwMinMTunnelUpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 112)
)
hwMinMTunnelUpAlarm.setObjects(
    ("HUAWEI-DC-TRAP-MIB", "hwTunnelGroupID")
)
if mibBuilder.loadTexts:
    hwMinMTunnelUpAlarm.setStatus(
        "current"
    )

hwInterfacePhysicalDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 113)
)
hwInterfacePhysicalDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hwInterfacePhysicalDown.setStatus(
        "current"
    )

hwInterfacePhysicalUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 114)
)
hwInterfacePhysicalUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hwInterfacePhysicalUp.setStatus(
        "current"
    )

hwBTBStartupFileNameDifferent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 119)
)
hwBTBStartupFileNameDifferent.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBStartupFileNameDifferent.setStatus(
        "current"
    )

hwBTBChassisRunningModeConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 120)
)
hwBTBChassisRunningModeConflict.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBChassisRunningModeConflict.setStatus(
        "current"
    )

hwBTBCtrlChannelFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 121)
)
hwBTBCtrlChannelFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBCtrlChannelFail.setStatus(
        "current"
    )

hwBTBCtrlChannelFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 122)
)
hwBTBCtrlChannelFailResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBCtrlChannelFailResume.setStatus(
        "current"
    )

hwBTBDataChannelFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 123)
)
hwBTBDataChannelFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBDataChannelFail.setStatus(
        "current"
    )

hwBTBDataChannelFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 124)
)
hwBTBDataChannelFailResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBDataChannelFailResume.setStatus(
        "current"
    )

hwBTBClkChannelFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 125)
)
hwBTBClkChannelFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBClkChannelFail.setStatus(
        "current"
    )

hwBTBClkChannelFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 126)
)
hwBTBClkChannelFailResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBClkChannelFailResume.setStatus(
        "current"
    )

hwBTBSFUOpticInterfaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 127)
)
hwBTBSFUOpticInterfaceError.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBSFUOpticInterfaceError.setStatus(
        "current"
    )

hwBTBSFUOpticInterfaceErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 128)
)
hwBTBSFUOpticInterfaceErrorResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBSFUOpticInterfaceErrorResume.setStatus(
        "current"
    )

hwBTBVSRInterfaceInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 129)
)
hwBTBVSRInterfaceInvalid.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBVSRInterfaceInvalid.setStatus(
        "current"
    )

hwBTBVSRInterfaceInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 130)
)
hwBTBVSRInterfaceInvalidResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBVSRInterfaceInvalidResume.setStatus(
        "current"
    )

hwBTBSlaveChassisNoHeart = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 131)
)
hwBTBSlaveChassisNoHeart.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBSlaveChassisNoHeart.setStatus(
        "current"
    )

hwBTBNoSlaveChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 132)
)
hwBTBNoSlaveChassis.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBNoSlaveChassis.setStatus(
        "current"
    )

hwBTBSlaveChassisRegisted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 133)
)
hwBTBSlaveChassisRegisted.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBSlaveChassisRegisted.setStatus(
        "current"
    )

hwBTBSlaveChassisRegisteFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 134)
)
hwBTBSlaveChassisRegisteFail.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBSlaveChassisRegisteFail.setStatus(
        "current"
    )

hwBTBChassisTypeConflict = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 135)
)
hwBTBChassisTypeConflict.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-DC-TRAP-MIB", "hwDCTrapReason"))
)
if mibBuilder.loadTexts:
    hwBTBChassisTypeConflict.setStatus(
        "current"
    )

hwSuperChangeSuccesful = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 136)
)
if mibBuilder.loadTexts:
    hwSuperChangeSuccesful.setStatus(
        "current"
    )

hwSuperChangeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 137)
)
if mibBuilder.loadTexts:
    hwSuperChangeFailure.setStatus(
        "current"
    )

hwOpticaPowerAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 138)
)
hwOpticaPowerAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwOpticaPowerAbnormal.setStatus(
        "current"
    )

hwEpldAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 139)
)
hwEpldAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwEpldAbnormal.setStatus(
        "current"
    )

hwPhyChipAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 140)
)
hwPhyChipAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPhyChipAbnormal.setStatus(
        "current"
    )

hwSerdesAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 141)
)
hwSerdesAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwSerdesAbnormal.setStatus(
        "current"
    )

hwBoardAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 142)
)
hwBoardAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwBoardAbnormal.setStatus(
        "current"
    )

hwFeChannelAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 143)
)
hwFeChannelAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFeChannelAbnormal.setStatus(
        "current"
    )

hwParityCheckAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 144)
)
hwParityCheckAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwParityCheckAbnormal.setStatus(
        "current"
    )

hwPhyClockAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 145)
)
hwPhyClockAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPhyClockAbnormal.setStatus(
        "current"
    )

hwPortAutoNegotiateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 146)
)
hwPortAutoNegotiateFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPortAutoNegotiateFail.setStatus(
        "current"
    )

hwPortSemiduplex = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 147)
)
hwPortSemiduplex.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwPortSemiduplex.setStatus(
        "current"
    )

hwScuStartModeSetFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 148)
)
hwScuStartModeSetFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwScuStartModeSetFail.setStatus(
        "current"
    )

hwMemoryExhaust = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 149)
)
if mibBuilder.loadTexts:
    hwMemoryExhaust.setStatus(
        "current"
    )

hwMemoryExhaustClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 150)
)
if mibBuilder.loadTexts:
    hwMemoryExhaustClear.setStatus(
        "current"
    )

hwMethAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 151)
)
hwMethAbnormal.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwMethAbnormal.setStatus(
        "current"
    )

hwLpuNotTight = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 152)
)
hwLpuNotTight.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLpuNotTight.setStatus(
        "current"
    )

hwLicenseFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 153)
)
hwLicenseFail.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwLicenseFail.setStatus(
        "current"
    )

hwHaBatchBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 154)
)
hwHaBatchBegin.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwHaBatchBegin.setStatus(
        "current"
    )

hwHaBatchEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 155)
)
hwHaBatchEnd.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwHaBatchEnd.setStatus(
        "current"
    )

hwHaSmoothBegin = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 156)
)
hwHaSmoothBegin.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwHaSmoothBegin.setStatus(
        "current"
    )

hwHaSmoothEnd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 157)
)
hwHaSmoothEnd.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwHaSmoothEnd.setStatus(
        "current"
    )

hwFanUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 2, 158)
)
hwFanUp.setObjects(
    ("ENTITY-MIB", "entPhysicalName")
)
if mibBuilder.loadTexts:
    hwFanUp.setStatus(
        "current"
    )


# Notifications groups

hwDCNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3, 1, 2)
)
hwDCNotificationGroup.setObjects(
      *(("HUAWEI-DC-TRAP-MIB", "hwMPUSynClkFaulty"),
        ("HUAWEI-DC-TRAP-MIB", "hwMPUSynClkFaultyResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwSlaveMPUNoResp"),
        ("HUAWEI-DC-TRAP-MIB", "hwSlaveMPUNoRespResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdChannelFaulty"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdChannelFaultyResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdNofullin"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdNofullinResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdTypeNoMatchReset"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdAutoSwtFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdAutoSwt"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdClkLockERR"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdClkLockERRResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdRemoved"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdUp"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkSrcMiss"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkAllSrcLost"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkAllSrcLostResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkNoHeartbeat"),
        ("HUAWEI-DC-TRAP-MIB", "hwClkNoHeartbeatResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwLPULostSynAlarm"),
        ("HUAWEI-DC-TRAP-MIB", "hwLPUOpenChannelError"),
        ("HUAWEI-DC-TRAP-MIB", "hwLPUSlfTstErr"),
        ("HUAWEI-DC-TRAP-MIB", "hwLPU3ClkSwitch"),
        ("HUAWEI-DC-TRAP-MIB", "hwSFULostHrtReset"),
        ("HUAWEI-DC-TRAP-MIB", "hwSFULinkLostReset"),
        ("HUAWEI-DC-TRAP-MIB", "hwSFUChannelLinkLost"),
        ("HUAWEI-DC-TRAP-MIB", "hwSFUInChannelOpenFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSensorFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSensorFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltBtmC"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltBtmCResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSprC"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSprCResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltBtmM"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltBtmMResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSprM"),
        ("HUAWEI-DC-TRAP-MIB", "hwVoltSprMResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempSensorFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempSensorFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempMnr"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempMnrResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempMjr"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempMjrResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempCtl"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempCtlResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanHFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanAbsent"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanAbsentResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanCabUN"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanCabUNResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrAbsent"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrAbsentResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrCabUN"),
        ("HUAWEI-DC-TRAP-MIB", "hwPwrCabUNResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDHFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDAbsent"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDAbsentResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDCabUN"),
        ("HUAWEI-DC-TRAP-MIB", "hwLCDCabUNResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwROMFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwMonitorBUSFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwMonitorBUSFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwWriteFlashError"),
        ("HUAWEI-DC-TRAP-MIB", "hwBoardReset"),
        ("HUAWEI-DC-TRAP-MIB", "hwBoardResetSuccess"),
        ("HUAWEI-DC-TRAP-MIB", "hwSlaveMPUReset"),
        ("HUAWEI-DC-TRAP-MIB", "hwMasterSlaveSwap"),
        ("HUAWEI-DC-TRAP-MIB", "hwRTCFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwExchangeChipFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwTempResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwOpticalModuleInsert"),
        ("HUAWEI-DC-TRAP-MIB", "hwOpticalModuleRemove"),
        ("HUAWEI-DC-TRAP-MIB", "hwBoardOfflineChange"),
        ("HUAWEI-DC-TRAP-MIB", "hwInterfacePhysicalDown"),
        ("HUAWEI-DC-TRAP-MIB", "hwInterfacePhysicalUp"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBStartupFileNameDifferent"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBChassisRunningModeConflict"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBCtrlChannelFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBCtrlChannelFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBDataChannelFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBDataChannelFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBClkChannelFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBClkChannelFailResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBSFUOpticInterfaceError"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBSFUOpticInterfaceErrorResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBVSRInterfaceInvalid"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBVSRInterfaceInvalidResume"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBSlaveChassisNoHeart"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBNoSlaveChassis"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBSlaveChassisRegisted"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBSlaveChassisRegisteFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwBTBChassisTypeConflict"),
        ("HUAWEI-DC-TRAP-MIB", "hwOpticaPowerAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwFPGAAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwBrdInserted"),
        ("HUAWEI-DC-TRAP-MIB", "hwMinMTunnelDownAlarm"),
        ("HUAWEI-DC-TRAP-MIB", "hwMinMTunnelUpAlarm"),
        ("HUAWEI-DC-TRAP-MIB", "hwSuperChangeSuccesful"),
        ("HUAWEI-DC-TRAP-MIB", "hwSuperChangeFailure"),
        ("HUAWEI-DC-TRAP-MIB", "hwEpldAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwPhyChipAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwSerdesAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwBoardAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwFeChannelAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwParityCheckAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwPhyClockAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwPortAutoNegotiateFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwPortSemiduplex"),
        ("HUAWEI-DC-TRAP-MIB", "hwScuStartModeSetFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwMemoryExhaust"),
        ("HUAWEI-DC-TRAP-MIB", "hwMemoryExhaustClear"),
        ("HUAWEI-DC-TRAP-MIB", "hwMethAbnormal"),
        ("HUAWEI-DC-TRAP-MIB", "hwLpuNotTight"),
        ("HUAWEI-DC-TRAP-MIB", "hwLicenseFail"),
        ("HUAWEI-DC-TRAP-MIB", "hwHaBatchBegin"),
        ("HUAWEI-DC-TRAP-MIB", "hwHaBatchEnd"),
        ("HUAWEI-DC-TRAP-MIB", "hwHaSmoothBegin"),
        ("HUAWEI-DC-TRAP-MIB", "hwHaSmoothEnd"),
        ("HUAWEI-DC-TRAP-MIB", "hwFanUp"))
)
if mibBuilder.loadTexts:
    hwDCNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwDCTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 37, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwDCTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-DC-TRAP-MIB",
    **{"hwDCTrapMIB": hwDCTrapMIB,
       "hwDCTrapControl": hwDCTrapControl,
       "hwDCCtrlTrap": hwDCCtrlTrap,
       "hwTunnelGroupID": hwTunnelGroupID,
       "hwDCTrapReason": hwDCTrapReason,
       "hwDCTraps": hwDCTraps,
       "hwMPUSynClkFaulty": hwMPUSynClkFaulty,
       "hwMPUSynClkFaultyResume": hwMPUSynClkFaultyResume,
       "hwSlaveMPUNoResp": hwSlaveMPUNoResp,
       "hwSlaveMPUNoRespResume": hwSlaveMPUNoRespResume,
       "hwBrdChannelFaulty": hwBrdChannelFaulty,
       "hwBrdChannelFaultyResume": hwBrdChannelFaultyResume,
       "hwBrdNofullin": hwBrdNofullin,
       "hwBrdNofullinResume": hwBrdNofullinResume,
       "hwBrdTypeNoMatchReset": hwBrdTypeNoMatchReset,
       "hwBrdAutoSwtFail": hwBrdAutoSwtFail,
       "hwBrdAutoSwt": hwBrdAutoSwt,
       "hwBrdClkLockERR": hwBrdClkLockERR,
       "hwBrdClkLockERRResume": hwBrdClkLockERRResume,
       "hwBrdRemoved": hwBrdRemoved,
       "hwBrdInserted": hwBrdInserted,
       "hwBrdUp": hwBrdUp,
       "hwClkSrcMiss": hwClkSrcMiss,
       "hwClkAllSrcLost": hwClkAllSrcLost,
       "hwClkAllSrcLostResume": hwClkAllSrcLostResume,
       "hwClkFail": hwClkFail,
       "hwClkFailResume": hwClkFailResume,
       "hwClkNoHeartbeat": hwClkNoHeartbeat,
       "hwClkNoHeartbeatResume": hwClkNoHeartbeatResume,
       "hwLPULostSynAlarm": hwLPULostSynAlarm,
       "hwLPUOpenChannelError": hwLPUOpenChannelError,
       "hwLPUSlfTstErr": hwLPUSlfTstErr,
       "hwLPU3ClkSwitch": hwLPU3ClkSwitch,
       "hwSFULostHrtReset": hwSFULostHrtReset,
       "hwSFULinkLostReset": hwSFULinkLostReset,
       "hwSFUChannelLinkLost": hwSFUChannelLinkLost,
       "hwSFUInChannelOpenFail": hwSFUInChannelOpenFail,
       "hwVoltSensorFail": hwVoltSensorFail,
       "hwVoltSensorFailResume": hwVoltSensorFailResume,
       "hwVoltBtmC": hwVoltBtmC,
       "hwVoltBtmCResume": hwVoltBtmCResume,
       "hwVoltSprC": hwVoltSprC,
       "hwVoltSprCResume": hwVoltSprCResume,
       "hwVoltBtmM": hwVoltBtmM,
       "hwVoltBtmMResume": hwVoltBtmMResume,
       "hwVoltSprM": hwVoltSprM,
       "hwVoltSprMResume": hwVoltSprMResume,
       "hwTempSensorFail": hwTempSensorFail,
       "hwTempSensorFailResume": hwTempSensorFailResume,
       "hwTempMnr": hwTempMnr,
       "hwTempMnrResume": hwTempMnrResume,
       "hwTempMjr": hwTempMjr,
       "hwTempMjrResume": hwTempMjrResume,
       "hwTempCtl": hwTempCtl,
       "hwTempCtlResume": hwTempCtlResume,
       "hwFanHFail": hwFanHFail,
       "hwFanFail": hwFanFail,
       "hwFanFailResume": hwFanFailResume,
       "hwFanAbsent": hwFanAbsent,
       "hwFanAbsentResume": hwFanAbsentResume,
       "hwFanCabUN": hwFanCabUN,
       "hwFanCabUNResume": hwFanCabUNResume,
       "hwPwrFail": hwPwrFail,
       "hwPwrFailResume": hwPwrFailResume,
       "hwPwrAbsent": hwPwrAbsent,
       "hwPwrAbsentResume": hwPwrAbsentResume,
       "hwPwrCabUN": hwPwrCabUN,
       "hwPwrCabUNResume": hwPwrCabUNResume,
       "hwLCDHFail": hwLCDHFail,
       "hwLCDFail": hwLCDFail,
       "hwLCDAbsent": hwLCDAbsent,
       "hwLCDAbsentResume": hwLCDAbsentResume,
       "hwLCDCabUN": hwLCDCabUN,
       "hwLCDCabUNResume": hwLCDCabUNResume,
       "hwROMFail": hwROMFail,
       "hwMonitorBUSFail": hwMonitorBUSFail,
       "hwMonitorBUSFailResume": hwMonitorBUSFailResume,
       "hwBoardOfflineChange": hwBoardOfflineChange,
       "hwWriteFlashError": hwWriteFlashError,
       "hwBoardReset": hwBoardReset,
       "hwBoardResetSuccess": hwBoardResetSuccess,
       "hwSlaveMPUReset": hwSlaveMPUReset,
       "hwMasterSlaveSwap": hwMasterSlaveSwap,
       "hwRTCFail": hwRTCFail,
       "hwExchangeChipFail": hwExchangeChipFail,
       "hwTempResume": hwTempResume,
       "hwOpticalModuleInsert": hwOpticalModuleInsert,
       "hwOpticalModuleRemove": hwOpticalModuleRemove,
       "hwFPGAAbnormal": hwFPGAAbnormal,
       "hwMinMTunnelDownAlarm": hwMinMTunnelDownAlarm,
       "hwMinMTunnelUpAlarm": hwMinMTunnelUpAlarm,
       "hwInterfacePhysicalDown": hwInterfacePhysicalDown,
       "hwInterfacePhysicalUp": hwInterfacePhysicalUp,
       "hwBTBStartupFileNameDifferent": hwBTBStartupFileNameDifferent,
       "hwBTBChassisRunningModeConflict": hwBTBChassisRunningModeConflict,
       "hwBTBCtrlChannelFail": hwBTBCtrlChannelFail,
       "hwBTBCtrlChannelFailResume": hwBTBCtrlChannelFailResume,
       "hwBTBDataChannelFail": hwBTBDataChannelFail,
       "hwBTBDataChannelFailResume": hwBTBDataChannelFailResume,
       "hwBTBClkChannelFail": hwBTBClkChannelFail,
       "hwBTBClkChannelFailResume": hwBTBClkChannelFailResume,
       "hwBTBSFUOpticInterfaceError": hwBTBSFUOpticInterfaceError,
       "hwBTBSFUOpticInterfaceErrorResume": hwBTBSFUOpticInterfaceErrorResume,
       "hwBTBVSRInterfaceInvalid": hwBTBVSRInterfaceInvalid,
       "hwBTBVSRInterfaceInvalidResume": hwBTBVSRInterfaceInvalidResume,
       "hwBTBSlaveChassisNoHeart": hwBTBSlaveChassisNoHeart,
       "hwBTBNoSlaveChassis": hwBTBNoSlaveChassis,
       "hwBTBSlaveChassisRegisted": hwBTBSlaveChassisRegisted,
       "hwBTBSlaveChassisRegisteFail": hwBTBSlaveChassisRegisteFail,
       "hwBTBChassisTypeConflict": hwBTBChassisTypeConflict,
       "hwSuperChangeSuccesful": hwSuperChangeSuccesful,
       "hwSuperChangeFailure": hwSuperChangeFailure,
       "hwOpticaPowerAbnormal": hwOpticaPowerAbnormal,
       "hwEpldAbnormal": hwEpldAbnormal,
       "hwPhyChipAbnormal": hwPhyChipAbnormal,
       "hwSerdesAbnormal": hwSerdesAbnormal,
       "hwBoardAbnormal": hwBoardAbnormal,
       "hwFeChannelAbnormal": hwFeChannelAbnormal,
       "hwParityCheckAbnormal": hwParityCheckAbnormal,
       "hwPhyClockAbnormal": hwPhyClockAbnormal,
       "hwPortAutoNegotiateFail": hwPortAutoNegotiateFail,
       "hwPortSemiduplex": hwPortSemiduplex,
       "hwScuStartModeSetFail": hwScuStartModeSetFail,
       "hwMemoryExhaust": hwMemoryExhaust,
       "hwMemoryExhaustClear": hwMemoryExhaustClear,
       "hwMethAbnormal": hwMethAbnormal,
       "hwLpuNotTight": hwLpuNotTight,
       "hwLicenseFail": hwLicenseFail,
       "hwHaBatchBegin": hwHaBatchBegin,
       "hwHaBatchEnd": hwHaBatchEnd,
       "hwHaSmoothBegin": hwHaSmoothBegin,
       "hwHaSmoothEnd": hwHaSmoothEnd,
       "hwFanUp": hwFanUp,
       "hwDCTrapConformance": hwDCTrapConformance,
       "hwDCTrapGroups": hwDCTrapGroups,
       "hwDCTrapControlGroup": hwDCTrapControlGroup,
       "hwDCNotificationGroup": hwDCNotificationGroup,
       "hwDCTrapCompliances": hwDCTrapCompliances,
       "hwDCTrapCompliance": hwDCTrapCompliance}
)
