# SNMP MIB module (XYLANTRAP-M-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLANTRAP-M-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:27 2024
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

(chasControlSlot,
 chasControlState,
 chasModuleOperStatus,
 chasModuleSlot,
 chasModuleSubUnit,
 chasModuleType,
 chasPowerSupply1State,
 chasPowerSupply2State) = mibBuilder.importSymbols(
    "CHASSIS-MIB",
    "chasControlSlot",
    "chasControlState",
    "chasModuleOperStatus",
    "chasModuleSlot",
    "chasModuleSubUnit",
    "chasModuleType",
    "chasPowerSupply1State",
    "chasPowerSupply2State")

(fddimibSMTCFState,
 fddimibSMTIndex) = mibBuilder.importSymbols(
    "FDDI-SMT73-MIB",
    "fddimibSMTCFState",
    "fddimibSMTIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(atmxPortEnableILMI,
 atmxPortPortIndex,
 atmxPortSlotIndex,
 atmxServiceAdmStatus,
 atmxServiceNumber,
 atmxServicePortIndex,
 atmxServiceSlotIndex,
 atmxVccAdmStatus,
 atmxVccPortIndex,
 atmxVccSlotIndex,
 atmxVccVci,
 atmxVccVpi) = mibBuilder.importSymbols(
    "XYLAN-ATM-MIB",
    "atmxPortEnableILMI",
    "atmxPortPortIndex",
    "atmxPortSlotIndex",
    "atmxServiceAdmStatus",
    "atmxServiceNumber",
    "atmxServicePortIndex",
    "atmxServiceSlotIndex",
    "atmxVccAdmStatus",
    "atmxVccPortIndex",
    "atmxVccSlotIndex",
    "atmxVccVci",
    "atmxVccVpi")

(microSwitch,
 omniswitch5,
 omniswitch9,
 pizzaSwitch,
 xylan,
 xylanSwitchDevice) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "microSwitch",
    "omniswitch5",
    "omniswitch9",
    "pizzaSwitch",
    "xylan",
    "xylanSwitchDevice")

(frxVcControlDlci,
 frxVcControlPortIndex,
 frxVcControlSlotIndex) = mibBuilder.importSymbols(
    "XYLAN-FRAME-RELAY-MIB",
    "frxVcControlDlci",
    "frxVcControlPortIndex",
    "frxVcControlSlotIndex")

(healthThreshDevTrapData,
 healthThreshModTrapCount,
 healthThreshModTrapData) = mibBuilder.importSymbols(
    "XYLAN-HEALTH-MIB",
    "healthThreshDevTrapData",
    "healthThreshModTrapCount",
    "healthThreshModTrapData")

(xylanIpAssocAddr,
 xylanIpAssocDupIntf,
 xylanIpAssocDupMac,
 xylanIpAssocDupSlot,
 xylanIpAssocIntf,
 xylanIpAssocMac,
 xylanIpAssocSlot) = mibBuilder.importSymbols(
    "XYLAN-IP-MIB",
    "xylanIpAssocAddr",
    "xylanIpAssocDupIntf",
    "xylanIpAssocDupMac",
    "xylanIpAssocDupSlot",
    "xylanIpAssocIntf",
    "xylanIpAssocMac",
    "xylanIpAssocSlot")

(systemEventTrapNumber,) = mibBuilder.importSymbols(
    "XYLAN-MGMTSTN-MIB",
    "systemEventTrapNumber")

(vportAdmStatus,
 vportFuncType,
 vportFuncTypeInstance,
 vportIF,
 vportSlot) = mibBuilder.importSymbols(
    "XYLAN-PORT-MIB",
    "vportAdmStatus",
    "vportFuncType",
    "vportFuncTypeInstance",
    "vportIF",
    "vportSlot")

(atVLANAdminStatus,
 atVLANGroupId,
 atVLANId,
 vBrdgTpFdbAddress,
 vDupMacIntf,
 vDupMacMac,
 vDupMacSlot,
 vDupMacTime,
 vLanAdmStatus,
 vLanNumber) = mibBuilder.importSymbols(
    "XYLAN-VLAN-MIB",
    "atVLANAdminStatus",
    "atVLANGroupId",
    "atVLANId",
    "vBrdgTpFdbAddress",
    "vDupMacIntf",
    "vDupMacMac",
    "vDupMacSlot",
    "vDupMacTime",
    "vLanAdmStatus",
    "vLanNumber")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

tempAlarmM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 1)
)
if mibBuilder.loadTexts:
    tempAlarmM.setStatus(
        ""
    )

moduleChangeM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 2)
)
moduleChangeM.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"))
)
if mibBuilder.loadTexts:
    moduleChangeM.setStatus(
        ""
    )

powerEventM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 3)
)
powerEventM.setObjects(
      *(("CHASSIS-MIB", "chasPowerSupply1State"),
        ("CHASSIS-MIB", "chasPowerSupply2State"))
)
if mibBuilder.loadTexts:
    powerEventM.setStatus(
        ""
    )

controllerEventM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 4)
)
controllerEventM.setObjects(
      *(("CHASSIS-MIB", "chasControlSlot"),
        ("CHASSIS-MIB", "chasControlState"))
)
if mibBuilder.loadTexts:
    controllerEventM.setStatus(
        ""
    )

loginViolationM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 5)
)
if mibBuilder.loadTexts:
    loginViolationM.setStatus(
        ""
    )

macVlanViolationM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 6)
)
macVlanViolationM.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macVlanViolationM.setStatus(
        ""
    )

macDuplicatePortM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 7)
)
macDuplicatePortM.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macDuplicatePortM.setStatus(
        ""
    )

portLinkUpEventM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 8)
)
portLinkUpEventM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkUpEventM.setStatus(
        ""
    )

portLinkDownEventM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 9)
)
portLinkDownEventM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkDownEventM.setStatus(
        ""
    )

portPartitionedM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 10)
)
portPartitionedM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portPartitionedM.setStatus(
        ""
    )

portRecordMismatchM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 11)
)
portRecordMismatchM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portRecordMismatchM.setStatus(
        ""
    )

groupChangeM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 14)
)
groupChangeM.setObjects(
      *(("XYLAN-VLAN-MIB", "vLanNumber"),
        ("XYLAN-VLAN-MIB", "vLanAdmStatus"))
)
if mibBuilder.loadTexts:
    groupChangeM.setStatus(
        ""
    )

vlanChangeM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 15)
)
vlanChangeM.setObjects(
      *(("XYLAN-VLAN-MIB", "atVLANGroupId"),
        ("XYLAN-VLAN-MIB", "atVLANId"),
        ("XYLAN-VLAN-MIB", "atVLANAdminStatus"))
)
if mibBuilder.loadTexts:
    vlanChangeM.setStatus(
        ""
    )

portMoveM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 16)
)
portMoveM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"),
        ("XYLAN-PORT-MIB", "vportAdmStatus"))
)
if mibBuilder.loadTexts:
    portMoveM.setStatus(
        ""
    )

moduleResetReloadM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 17)
)
moduleResetReloadM.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"),
        ("CHASSIS-MIB", "chasModuleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleResetReloadM.setStatus(
        ""
    )

systemEventM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 18)
)
systemEventM.setObjects(
    ("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber")
)
if mibBuilder.loadTexts:
    systemEventM.setStatus(
        ""
    )

vlanRouteTableFullM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 19)
)
if mibBuilder.loadTexts:
    vlanRouteTableFullM.setStatus(
        ""
    )

sapTableFullM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 20)
)
if mibBuilder.loadTexts:
    sapTableFullM.setStatus(
        ""
    )

atmSSCOPstateM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 21)
)
atmSSCOPstateM.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"))
)
if mibBuilder.loadTexts:
    atmSSCOPstateM.setStatus(
        ""
    )

ilmiStateM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 22)
)
ilmiStateM.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"),
        ("XYLAN-ATM-MIB", "atmxPortEnableILMI"))
)
if mibBuilder.loadTexts:
    ilmiStateM.setStatus(
        ""
    )

atmConnectionM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 23)
)
atmConnectionM.setObjects(
      *(("XYLAN-ATM-MIB", "atmxVccSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxVccPortIndex"),
        ("XYLAN-ATM-MIB", "atmxVccVpi"),
        ("XYLAN-ATM-MIB", "atmxVccVci"),
        ("XYLAN-ATM-MIB", "atmxVccAdmStatus"))
)
if mibBuilder.loadTexts:
    atmConnectionM.setStatus(
        ""
    )

atmServiceM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 24)
)
atmServiceM.setObjects(
      *(("XYLAN-ATM-MIB", "atmxServiceSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxServicePortIndex"),
        ("XYLAN-ATM-MIB", "atmxServiceNumber"),
        ("XYLAN-ATM-MIB", "atmxServiceAdmStatus"))
)
if mibBuilder.loadTexts:
    atmServiceM.setStatus(
        ""
    )

dlciNewM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 27)
)
dlciNewM.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciNewM.setStatus(
        ""
    )

dlciDelM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 28)
)
dlciDelM.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDelM.setStatus(
        ""
    )

dlciUpM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 29)
)
dlciUpM.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciUpM.setStatus(
        ""
    )

dlciDnM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 30)
)
dlciDnM.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDnM.setStatus(
        ""
    )

portManualForwardingModeM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 31)
)
portManualForwardingModeM.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portManualForwardingModeM.setStatus(
        ""
    )

fddiCFStateChangeM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 32)
)
fddiCFStateChangeM.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibSMTCFState"))
)
if mibBuilder.loadTexts:
    fddiCFStateChangeM.setStatus(
        ""
    )

duplicateIPaddressM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 35)
)
duplicateIPaddressM.setObjects(
      *(("XYLAN-IP-MIB", "xylanIpAssocAddr"),
        ("XYLAN-IP-MIB", "xylanIpAssocMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocIntf"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupIntf"))
)
if mibBuilder.loadTexts:
    duplicateIPaddressM.setStatus(
        ""
    )

duplicateMACaddressM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 36)
)
duplicateMACaddressM.setObjects(
      *(("XYLAN-VLAN-MIB", "vDupMacMac"),
        ("XYLAN-VLAN-MIB", "vDupMacSlot"),
        ("XYLAN-VLAN-MIB", "vDupMacIntf"),
        ("XYLAN-VLAN-MIB", "vDupMacTime"))
)
if mibBuilder.loadTexts:
    duplicateMACaddressM.setStatus(
        ""
    )

healthThresholdRisingM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 37)
)
if mibBuilder.loadTexts:
    healthThresholdRisingM.setStatus(
        ""
    )

healthThresholdFallingM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 38)
)
if mibBuilder.loadTexts:
    healthThresholdFallingM.setStatus(
        ""
    )

healthThresholdDeviceM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 39)
)
healthThresholdDeviceM.setObjects(
    ("XYLAN-HEALTH-MIB", "healthThreshDevTrapData")
)
if mibBuilder.loadTexts:
    healthThresholdDeviceM.setStatus(
        ""
    )

healthThresholdModuleM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 40)
)
healthThresholdModuleM.setObjects(
      *(("XYLAN-HEALTH-MIB", "healthThreshModTrapCount"),
        ("XYLAN-HEALTH-MIB", "healthThreshModTrapData"))
)
if mibBuilder.loadTexts:
    healthThresholdModuleM.setStatus(
        ""
    )

pnniRouteConflictPortM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 50)
)
if mibBuilder.loadTexts:
    pnniRouteConflictPortM.setStatus(
        ""
    )

pnniRouteConflictSamePGM = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 4, 0, 51)
)
if mibBuilder.loadTexts:
    pnniRouteConflictSamePGM.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLANTRAP-M-MIB",
    **{"tempAlarmM": tempAlarmM,
       "moduleChangeM": moduleChangeM,
       "powerEventM": powerEventM,
       "controllerEventM": controllerEventM,
       "loginViolationM": loginViolationM,
       "macVlanViolationM": macVlanViolationM,
       "macDuplicatePortM": macDuplicatePortM,
       "portLinkUpEventM": portLinkUpEventM,
       "portLinkDownEventM": portLinkDownEventM,
       "portPartitionedM": portPartitionedM,
       "portRecordMismatchM": portRecordMismatchM,
       "groupChangeM": groupChangeM,
       "vlanChangeM": vlanChangeM,
       "portMoveM": portMoveM,
       "moduleResetReloadM": moduleResetReloadM,
       "systemEventM": systemEventM,
       "vlanRouteTableFullM": vlanRouteTableFullM,
       "sapTableFullM": sapTableFullM,
       "atmSSCOPstateM": atmSSCOPstateM,
       "ilmiStateM": ilmiStateM,
       "atmConnectionM": atmConnectionM,
       "atmServiceM": atmServiceM,
       "dlciNewM": dlciNewM,
       "dlciDelM": dlciDelM,
       "dlciUpM": dlciUpM,
       "dlciDnM": dlciDnM,
       "portManualForwardingModeM": portManualForwardingModeM,
       "fddiCFStateChangeM": fddiCFStateChangeM,
       "duplicateIPaddressM": duplicateIPaddressM,
       "duplicateMACaddressM": duplicateMACaddressM,
       "healthThresholdRisingM": healthThresholdRisingM,
       "healthThresholdFallingM": healthThresholdFallingM,
       "healthThresholdDeviceM": healthThresholdDeviceM,
       "healthThresholdModuleM": healthThresholdModuleM,
       "pnniRouteConflictPortM": pnniRouteConflictPortM,
       "pnniRouteConflictSamePGM": pnniRouteConflictSamePGM}
)
