# SNMP MIB module (XYLANTRAP-9-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLANTRAP-9-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:26 2024
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

tempAlarm9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    tempAlarm9.setStatus(
        ""
    )

moduleChange9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 2)
)
moduleChange9.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"))
)
if mibBuilder.loadTexts:
    moduleChange9.setStatus(
        ""
    )

powerEvent9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 3)
)
powerEvent9.setObjects(
      *(("CHASSIS-MIB", "chasPowerSupply1State"),
        ("CHASSIS-MIB", "chasPowerSupply2State"))
)
if mibBuilder.loadTexts:
    powerEvent9.setStatus(
        ""
    )

controllerEvent9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 4)
)
controllerEvent9.setObjects(
      *(("CHASSIS-MIB", "chasControlSlot"),
        ("CHASSIS-MIB", "chasControlState"))
)
if mibBuilder.loadTexts:
    controllerEvent9.setStatus(
        ""
    )

loginViolation9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 5)
)
if mibBuilder.loadTexts:
    loginViolation9.setStatus(
        ""
    )

macVlanViolation9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 6)
)
macVlanViolation9.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macVlanViolation9.setStatus(
        ""
    )

macDuplicatePort9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 7)
)
macDuplicatePort9.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macDuplicatePort9.setStatus(
        ""
    )

portLinkUpEvent9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 8)
)
portLinkUpEvent9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkUpEvent9.setStatus(
        ""
    )

portLinkDownEvent9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 9)
)
portLinkDownEvent9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkDownEvent9.setStatus(
        ""
    )

portPartitioned9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 10)
)
portPartitioned9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portPartitioned9.setStatus(
        ""
    )

portRecordMismatch9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 11)
)
portRecordMismatch9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portRecordMismatch9.setStatus(
        ""
    )

groupChange9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 14)
)
groupChange9.setObjects(
      *(("XYLAN-VLAN-MIB", "vLanNumber"),
        ("XYLAN-VLAN-MIB", "vLanAdmStatus"))
)
if mibBuilder.loadTexts:
    groupChange9.setStatus(
        ""
    )

vlanChange9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 15)
)
vlanChange9.setObjects(
      *(("XYLAN-VLAN-MIB", "atVLANGroupId"),
        ("XYLAN-VLAN-MIB", "atVLANId"),
        ("XYLAN-VLAN-MIB", "atVLANAdminStatus"))
)
if mibBuilder.loadTexts:
    vlanChange9.setStatus(
        ""
    )

portMove9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 16)
)
portMove9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"),
        ("XYLAN-PORT-MIB", "vportAdmStatus"))
)
if mibBuilder.loadTexts:
    portMove9.setStatus(
        ""
    )

moduleResetReload9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 17)
)
moduleResetReload9.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"),
        ("CHASSIS-MIB", "chasModuleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleResetReload9.setStatus(
        ""
    )

systemEvent9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 18)
)
systemEvent9.setObjects(
    ("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber")
)
if mibBuilder.loadTexts:
    systemEvent9.setStatus(
        ""
    )

vlanRouteTableFull9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 19)
)
if mibBuilder.loadTexts:
    vlanRouteTableFull9.setStatus(
        ""
    )

sapTableFull9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 20)
)
if mibBuilder.loadTexts:
    sapTableFull9.setStatus(
        ""
    )

atmSSCOPstate9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 21)
)
atmSSCOPstate9.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"))
)
if mibBuilder.loadTexts:
    atmSSCOPstate9.setStatus(
        ""
    )

ilmiState9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 22)
)
ilmiState9.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"),
        ("XYLAN-ATM-MIB", "atmxPortEnableILMI"))
)
if mibBuilder.loadTexts:
    ilmiState9.setStatus(
        ""
    )

atmConnection9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 23)
)
atmConnection9.setObjects(
      *(("XYLAN-ATM-MIB", "atmxVccSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxVccPortIndex"),
        ("XYLAN-ATM-MIB", "atmxVccVpi"),
        ("XYLAN-ATM-MIB", "atmxVccVci"),
        ("XYLAN-ATM-MIB", "atmxVccAdmStatus"))
)
if mibBuilder.loadTexts:
    atmConnection9.setStatus(
        ""
    )

atmService9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 24)
)
atmService9.setObjects(
      *(("XYLAN-ATM-MIB", "atmxServiceSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxServicePortIndex"),
        ("XYLAN-ATM-MIB", "atmxServiceNumber"),
        ("XYLAN-ATM-MIB", "atmxServiceAdmStatus"))
)
if mibBuilder.loadTexts:
    atmService9.setStatus(
        ""
    )

dlciNew9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 27)
)
dlciNew9.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciNew9.setStatus(
        ""
    )

dlciDel9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 28)
)
dlciDel9.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDel9.setStatus(
        ""
    )

dlciUp9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 29)
)
dlciUp9.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciUp9.setStatus(
        ""
    )

dlciDn9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 30)
)
dlciDn9.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDn9.setStatus(
        ""
    )

portManualForwardingMode9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 31)
)
portManualForwardingMode9.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portManualForwardingMode9.setStatus(
        ""
    )

fddiCFStateChange9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 32)
)
fddiCFStateChange9.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibSMTCFState"))
)
if mibBuilder.loadTexts:
    fddiCFStateChange9.setStatus(
        ""
    )

duplicateIPaddress9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 35)
)
duplicateIPaddress9.setObjects(
      *(("XYLAN-IP-MIB", "xylanIpAssocAddr"),
        ("XYLAN-IP-MIB", "xylanIpAssocMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocIntf"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupIntf"))
)
if mibBuilder.loadTexts:
    duplicateIPaddress9.setStatus(
        ""
    )

duplicateMACaddress9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 36)
)
duplicateMACaddress9.setObjects(
      *(("XYLAN-VLAN-MIB", "vDupMacMac"),
        ("XYLAN-VLAN-MIB", "vDupMacSlot"),
        ("XYLAN-VLAN-MIB", "vDupMacIntf"),
        ("XYLAN-VLAN-MIB", "vDupMacTime"))
)
if mibBuilder.loadTexts:
    duplicateMACaddress9.setStatus(
        ""
    )

healthThresholdRising9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 37)
)
if mibBuilder.loadTexts:
    healthThresholdRising9.setStatus(
        ""
    )

healthThresholdFalling9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 38)
)
if mibBuilder.loadTexts:
    healthThresholdFalling9.setStatus(
        ""
    )

healthThresholdDevice9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 39)
)
healthThresholdDevice9.setObjects(
    ("XYLAN-HEALTH-MIB", "healthThreshDevTrapData")
)
if mibBuilder.loadTexts:
    healthThresholdDevice9.setStatus(
        ""
    )

healthThresholdModule9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 40)
)
healthThresholdModule9.setObjects(
      *(("XYLAN-HEALTH-MIB", "healthThreshModTrapCount"),
        ("XYLAN-HEALTH-MIB", "healthThreshModTrapData"))
)
if mibBuilder.loadTexts:
    healthThresholdModule9.setStatus(
        ""
    )

pnniRouteConflictPort9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 50)
)
if mibBuilder.loadTexts:
    pnniRouteConflictPort9.setStatus(
        ""
    )

pnniRouteConflictSamePG9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 2, 0, 51)
)
if mibBuilder.loadTexts:
    pnniRouteConflictSamePG9.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLANTRAP-9-MIB",
    **{"tempAlarm9": tempAlarm9,
       "moduleChange9": moduleChange9,
       "powerEvent9": powerEvent9,
       "controllerEvent9": controllerEvent9,
       "loginViolation9": loginViolation9,
       "macVlanViolation9": macVlanViolation9,
       "macDuplicatePort9": macDuplicatePort9,
       "portLinkUpEvent9": portLinkUpEvent9,
       "portLinkDownEvent9": portLinkDownEvent9,
       "portPartitioned9": portPartitioned9,
       "portRecordMismatch9": portRecordMismatch9,
       "groupChange9": groupChange9,
       "vlanChange9": vlanChange9,
       "portMove9": portMove9,
       "moduleResetReload9": moduleResetReload9,
       "systemEvent9": systemEvent9,
       "vlanRouteTableFull9": vlanRouteTableFull9,
       "sapTableFull9": sapTableFull9,
       "atmSSCOPstate9": atmSSCOPstate9,
       "ilmiState9": ilmiState9,
       "atmConnection9": atmConnection9,
       "atmService9": atmService9,
       "dlciNew9": dlciNew9,
       "dlciDel9": dlciDel9,
       "dlciUp9": dlciUp9,
       "dlciDn9": dlciDn9,
       "portManualForwardingMode9": portManualForwardingMode9,
       "fddiCFStateChange9": fddiCFStateChange9,
       "duplicateIPaddress9": duplicateIPaddress9,
       "duplicateMACaddress9": duplicateMACaddress9,
       "healthThresholdRising9": healthThresholdRising9,
       "healthThresholdFalling9": healthThresholdFalling9,
       "healthThresholdDevice9": healthThresholdDevice9,
       "healthThresholdModule9": healthThresholdModule9,
       "pnniRouteConflictPort9": pnniRouteConflictPort9,
       "pnniRouteConflictSamePG9": pnniRouteConflictSamePG9}
)
