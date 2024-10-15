# SNMP MIB module (XYLANTRAP-3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLANTRAP-3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:22 2024
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

tempAlarm3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 1)
)
if mibBuilder.loadTexts:
    tempAlarm3.setStatus(
        ""
    )

moduleChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 2)
)
moduleChange3.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"))
)
if mibBuilder.loadTexts:
    moduleChange3.setStatus(
        ""
    )

powerEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 3)
)
powerEvent3.setObjects(
      *(("CHASSIS-MIB", "chasPowerSupply1State"),
        ("CHASSIS-MIB", "chasPowerSupply2State"))
)
if mibBuilder.loadTexts:
    powerEvent3.setStatus(
        ""
    )

controllerEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 4)
)
controllerEvent3.setObjects(
      *(("CHASSIS-MIB", "chasControlSlot"),
        ("CHASSIS-MIB", "chasControlState"))
)
if mibBuilder.loadTexts:
    controllerEvent3.setStatus(
        ""
    )

loginViolation3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 5)
)
if mibBuilder.loadTexts:
    loginViolation3.setStatus(
        ""
    )

macVlanViolation3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 6)
)
macVlanViolation3.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macVlanViolation3.setStatus(
        ""
    )

macDuplicatePort3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 7)
)
macDuplicatePort3.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macDuplicatePort3.setStatus(
        ""
    )

portLinkUpEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 8)
)
portLinkUpEvent3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkUpEvent3.setStatus(
        ""
    )

portLinkDownEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 9)
)
portLinkDownEvent3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkDownEvent3.setStatus(
        ""
    )

portPartitioned3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 10)
)
portPartitioned3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portPartitioned3.setStatus(
        ""
    )

portRecordMismatch3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 11)
)
portRecordMismatch3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portRecordMismatch3.setStatus(
        ""
    )

groupChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 14)
)
groupChange3.setObjects(
      *(("XYLAN-VLAN-MIB", "vLanNumber"),
        ("XYLAN-VLAN-MIB", "vLanAdmStatus"))
)
if mibBuilder.loadTexts:
    groupChange3.setStatus(
        ""
    )

vlanChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 15)
)
vlanChange3.setObjects(
      *(("XYLAN-VLAN-MIB", "atVLANGroupId"),
        ("XYLAN-VLAN-MIB", "atVLANId"),
        ("XYLAN-VLAN-MIB", "atVLANAdminStatus"))
)
if mibBuilder.loadTexts:
    vlanChange3.setStatus(
        ""
    )

portMove3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 16)
)
portMove3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"),
        ("XYLAN-PORT-MIB", "vportAdmStatus"))
)
if mibBuilder.loadTexts:
    portMove3.setStatus(
        ""
    )

moduleResetReload3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 17)
)
moduleResetReload3.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"),
        ("CHASSIS-MIB", "chasModuleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleResetReload3.setStatus(
        ""
    )

systemEvent3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 18)
)
systemEvent3.setObjects(
    ("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber")
)
if mibBuilder.loadTexts:
    systemEvent3.setStatus(
        ""
    )

vlanRouteTableFull3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 19)
)
if mibBuilder.loadTexts:
    vlanRouteTableFull3.setStatus(
        ""
    )

sapTableFull3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 20)
)
if mibBuilder.loadTexts:
    sapTableFull3.setStatus(
        ""
    )

atmSSCOPstate3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 21)
)
atmSSCOPstate3.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"))
)
if mibBuilder.loadTexts:
    atmSSCOPstate3.setStatus(
        ""
    )

ilmiState3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 22)
)
ilmiState3.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"),
        ("XYLAN-ATM-MIB", "atmxPortEnableILMI"))
)
if mibBuilder.loadTexts:
    ilmiState3.setStatus(
        ""
    )

atmConnection3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 23)
)
atmConnection3.setObjects(
      *(("XYLAN-ATM-MIB", "atmxVccSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxVccPortIndex"),
        ("XYLAN-ATM-MIB", "atmxVccVpi"),
        ("XYLAN-ATM-MIB", "atmxVccVci"),
        ("XYLAN-ATM-MIB", "atmxVccAdmStatus"))
)
if mibBuilder.loadTexts:
    atmConnection3.setStatus(
        ""
    )

atmService3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 24)
)
atmService3.setObjects(
      *(("XYLAN-ATM-MIB", "atmxServiceSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxServicePortIndex"),
        ("XYLAN-ATM-MIB", "atmxServiceNumber"),
        ("XYLAN-ATM-MIB", "atmxServiceAdmStatus"))
)
if mibBuilder.loadTexts:
    atmService3.setStatus(
        ""
    )

dlciNew3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 27)
)
dlciNew3.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciNew3.setStatus(
        ""
    )

dlciDel3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 28)
)
dlciDel3.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDel3.setStatus(
        ""
    )

dlciUp3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 29)
)
dlciUp3.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciUp3.setStatus(
        ""
    )

dlciDn3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 30)
)
dlciDn3.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDn3.setStatus(
        ""
    )

portManualForwardingMode3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 31)
)
portManualForwardingMode3.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portManualForwardingMode3.setStatus(
        ""
    )

fddiCFStateChange3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 32)
)
fddiCFStateChange3.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibSMTCFState"))
)
if mibBuilder.loadTexts:
    fddiCFStateChange3.setStatus(
        ""
    )

duplicateIPaddress3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 35)
)
duplicateIPaddress3.setObjects(
      *(("XYLAN-IP-MIB", "xylanIpAssocAddr"),
        ("XYLAN-IP-MIB", "xylanIpAssocMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocIntf"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupIntf"))
)
if mibBuilder.loadTexts:
    duplicateIPaddress3.setStatus(
        ""
    )

duplicateMACaddress3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 36)
)
duplicateMACaddress3.setObjects(
      *(("XYLAN-VLAN-MIB", "vDupMacMac"),
        ("XYLAN-VLAN-MIB", "vDupMacSlot"),
        ("XYLAN-VLAN-MIB", "vDupMacIntf"),
        ("XYLAN-VLAN-MIB", "vDupMacTime"))
)
if mibBuilder.loadTexts:
    duplicateMACaddress3.setStatus(
        ""
    )

healthThresholdRising3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 37)
)
if mibBuilder.loadTexts:
    healthThresholdRising3.setStatus(
        ""
    )

healthThresholdFalling3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 38)
)
if mibBuilder.loadTexts:
    healthThresholdFalling3.setStatus(
        ""
    )

healthThresholdDevice3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 39)
)
healthThresholdDevice3.setObjects(
    ("XYLAN-HEALTH-MIB", "healthThreshDevTrapData")
)
if mibBuilder.loadTexts:
    healthThresholdDevice3.setStatus(
        ""
    )

healthThresholdModule3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 40)
)
healthThresholdModule3.setObjects(
      *(("XYLAN-HEALTH-MIB", "healthThreshModTrapCount"),
        ("XYLAN-HEALTH-MIB", "healthThreshModTrapData"))
)
if mibBuilder.loadTexts:
    healthThresholdModule3.setStatus(
        ""
    )

pnniRouteConflictPort3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 50)
)
if mibBuilder.loadTexts:
    pnniRouteConflictPort3.setStatus(
        ""
    )

pnniRouteConflictSamePG3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 3, 0, 51)
)
if mibBuilder.loadTexts:
    pnniRouteConflictSamePG3.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLANTRAP-3-MIB",
    **{"tempAlarm3": tempAlarm3,
       "moduleChange3": moduleChange3,
       "powerEvent3": powerEvent3,
       "controllerEvent3": controllerEvent3,
       "loginViolation3": loginViolation3,
       "macVlanViolation3": macVlanViolation3,
       "macDuplicatePort3": macDuplicatePort3,
       "portLinkUpEvent3": portLinkUpEvent3,
       "portLinkDownEvent3": portLinkDownEvent3,
       "portPartitioned3": portPartitioned3,
       "portRecordMismatch3": portRecordMismatch3,
       "groupChange3": groupChange3,
       "vlanChange3": vlanChange3,
       "portMove3": portMove3,
       "moduleResetReload3": moduleResetReload3,
       "systemEvent3": systemEvent3,
       "vlanRouteTableFull3": vlanRouteTableFull3,
       "sapTableFull3": sapTableFull3,
       "atmSSCOPstate3": atmSSCOPstate3,
       "ilmiState3": ilmiState3,
       "atmConnection3": atmConnection3,
       "atmService3": atmService3,
       "dlciNew3": dlciNew3,
       "dlciDel3": dlciDel3,
       "dlciUp3": dlciUp3,
       "dlciDn3": dlciDn3,
       "portManualForwardingMode3": portManualForwardingMode3,
       "fddiCFStateChange3": fddiCFStateChange3,
       "duplicateIPaddress3": duplicateIPaddress3,
       "duplicateMACaddress3": duplicateMACaddress3,
       "healthThresholdRising3": healthThresholdRising3,
       "healthThresholdFalling3": healthThresholdFalling3,
       "healthThresholdDevice3": healthThresholdDevice3,
       "healthThresholdModule3": healthThresholdModule3,
       "pnniRouteConflictPort3": pnniRouteConflictPort3,
       "pnniRouteConflictSamePG3": pnniRouteConflictSamePG3}
)
