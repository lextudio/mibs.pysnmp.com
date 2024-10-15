# SNMP MIB module (XYLANTRAP-5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLANTRAP-5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:24 2024
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

tempAlarm5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 1)
)
if mibBuilder.loadTexts:
    tempAlarm5.setStatus(
        ""
    )

moduleChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 2)
)
moduleChange5.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"))
)
if mibBuilder.loadTexts:
    moduleChange5.setStatus(
        ""
    )

powerEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 3)
)
powerEvent5.setObjects(
      *(("CHASSIS-MIB", "chasPowerSupply1State"),
        ("CHASSIS-MIB", "chasPowerSupply2State"))
)
if mibBuilder.loadTexts:
    powerEvent5.setStatus(
        ""
    )

controllerEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 4)
)
controllerEvent5.setObjects(
      *(("CHASSIS-MIB", "chasControlSlot"),
        ("CHASSIS-MIB", "chasControlState"))
)
if mibBuilder.loadTexts:
    controllerEvent5.setStatus(
        ""
    )

loginViolation5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    loginViolation5.setStatus(
        ""
    )

macVlanViolation5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 6)
)
macVlanViolation5.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macVlanViolation5.setStatus(
        ""
    )

macDuplicatePort5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 7)
)
macDuplicatePort5.setObjects(
    ("XYLAN-VLAN-MIB", "vBrdgTpFdbAddress")
)
if mibBuilder.loadTexts:
    macDuplicatePort5.setStatus(
        ""
    )

portLinkUpEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 8)
)
portLinkUpEvent5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkUpEvent5.setStatus(
        ""
    )

portLinkDownEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 9)
)
portLinkDownEvent5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portLinkDownEvent5.setStatus(
        ""
    )

portPartitioned5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 10)
)
portPartitioned5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portPartitioned5.setStatus(
        ""
    )

portRecordMismatch5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 11)
)
portRecordMismatch5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portRecordMismatch5.setStatus(
        ""
    )

groupChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 14)
)
groupChange5.setObjects(
      *(("XYLAN-VLAN-MIB", "vLanNumber"),
        ("XYLAN-VLAN-MIB", "vLanAdmStatus"))
)
if mibBuilder.loadTexts:
    groupChange5.setStatus(
        ""
    )

vlanChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 15)
)
vlanChange5.setObjects(
      *(("XYLAN-VLAN-MIB", "atVLANGroupId"),
        ("XYLAN-VLAN-MIB", "atVLANId"),
        ("XYLAN-VLAN-MIB", "atVLANAdminStatus"))
)
if mibBuilder.loadTexts:
    vlanChange5.setStatus(
        ""
    )

portMove5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 16)
)
portMove5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"),
        ("XYLAN-PORT-MIB", "vportAdmStatus"))
)
if mibBuilder.loadTexts:
    portMove5.setStatus(
        ""
    )

moduleResetReload5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 17)
)
moduleResetReload5.setObjects(
      *(("CHASSIS-MIB", "chasModuleSlot"),
        ("CHASSIS-MIB", "chasModuleSubUnit"),
        ("CHASSIS-MIB", "chasModuleType"),
        ("CHASSIS-MIB", "chasModuleOperStatus"))
)
if mibBuilder.loadTexts:
    moduleResetReload5.setStatus(
        ""
    )

systemEvent5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 18)
)
systemEvent5.setObjects(
    ("XYLAN-MGMTSTN-MIB", "systemEventTrapNumber")
)
if mibBuilder.loadTexts:
    systemEvent5.setStatus(
        ""
    )

vlanRouteTableFull5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 19)
)
if mibBuilder.loadTexts:
    vlanRouteTableFull5.setStatus(
        ""
    )

sapTableFull5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 20)
)
if mibBuilder.loadTexts:
    sapTableFull5.setStatus(
        ""
    )

atmSSCOPstate5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 21)
)
atmSSCOPstate5.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"))
)
if mibBuilder.loadTexts:
    atmSSCOPstate5.setStatus(
        ""
    )

ilmiState5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 22)
)
ilmiState5.setObjects(
      *(("XYLAN-ATM-MIB", "atmxPortSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxPortPortIndex"),
        ("XYLAN-ATM-MIB", "atmxPortEnableILMI"))
)
if mibBuilder.loadTexts:
    ilmiState5.setStatus(
        ""
    )

atmConnection5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 23)
)
atmConnection5.setObjects(
      *(("XYLAN-ATM-MIB", "atmxVccSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxVccPortIndex"),
        ("XYLAN-ATM-MIB", "atmxVccVpi"),
        ("XYLAN-ATM-MIB", "atmxVccVci"),
        ("XYLAN-ATM-MIB", "atmxVccAdmStatus"))
)
if mibBuilder.loadTexts:
    atmConnection5.setStatus(
        ""
    )

atmService5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 24)
)
atmService5.setObjects(
      *(("XYLAN-ATM-MIB", "atmxServiceSlotIndex"),
        ("XYLAN-ATM-MIB", "atmxServicePortIndex"),
        ("XYLAN-ATM-MIB", "atmxServiceNumber"),
        ("XYLAN-ATM-MIB", "atmxServiceAdmStatus"))
)
if mibBuilder.loadTexts:
    atmService5.setStatus(
        ""
    )

dlciNew5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 27)
)
dlciNew5.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciNew5.setStatus(
        ""
    )

dlciDel5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 28)
)
dlciDel5.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDel5.setStatus(
        ""
    )

dlciUp5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 29)
)
dlciUp5.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciUp5.setStatus(
        ""
    )

dlciDn5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 30)
)
dlciDn5.setObjects(
      *(("XYLAN-FRAME-RELAY-MIB", "frxVcControlSlotIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlPortIndex"),
        ("XYLAN-FRAME-RELAY-MIB", "frxVcControlDlci"))
)
if mibBuilder.loadTexts:
    dlciDn5.setStatus(
        ""
    )

portManualForwardingMode5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 31)
)
portManualForwardingMode5.setObjects(
      *(("XYLAN-PORT-MIB", "vportSlot"),
        ("XYLAN-PORT-MIB", "vportIF"),
        ("XYLAN-PORT-MIB", "vportFuncType"),
        ("XYLAN-PORT-MIB", "vportFuncTypeInstance"))
)
if mibBuilder.loadTexts:
    portManualForwardingMode5.setStatus(
        ""
    )

fddiCFStateChange5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 32)
)
fddiCFStateChange5.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibSMTCFState"))
)
if mibBuilder.loadTexts:
    fddiCFStateChange5.setStatus(
        ""
    )

duplicateIPaddress5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 35)
)
duplicateIPaddress5.setObjects(
      *(("XYLAN-IP-MIB", "xylanIpAssocAddr"),
        ("XYLAN-IP-MIB", "xylanIpAssocMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocIntf"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupMac"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupSlot"),
        ("XYLAN-IP-MIB", "xylanIpAssocDupIntf"))
)
if mibBuilder.loadTexts:
    duplicateIPaddress5.setStatus(
        ""
    )

duplicateMACaddress5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 36)
)
duplicateMACaddress5.setObjects(
      *(("XYLAN-VLAN-MIB", "vDupMacMac"),
        ("XYLAN-VLAN-MIB", "vDupMacSlot"),
        ("XYLAN-VLAN-MIB", "vDupMacIntf"),
        ("XYLAN-VLAN-MIB", "vDupMacTime"))
)
if mibBuilder.loadTexts:
    duplicateMACaddress5.setStatus(
        ""
    )

healthThresholdRising5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 37)
)
if mibBuilder.loadTexts:
    healthThresholdRising5.setStatus(
        ""
    )

healthThresholdFalling5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 38)
)
if mibBuilder.loadTexts:
    healthThresholdFalling5.setStatus(
        ""
    )

healthThresholdDevice5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 39)
)
healthThresholdDevice5.setObjects(
    ("XYLAN-HEALTH-MIB", "healthThreshDevTrapData")
)
if mibBuilder.loadTexts:
    healthThresholdDevice5.setStatus(
        ""
    )

healthThresholdModule5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 40)
)
healthThresholdModule5.setObjects(
      *(("XYLAN-HEALTH-MIB", "healthThreshModTrapCount"),
        ("XYLAN-HEALTH-MIB", "healthThreshModTrapData"))
)
if mibBuilder.loadTexts:
    healthThresholdModule5.setStatus(
        ""
    )

pnniRouteConflictPort5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 50)
)
if mibBuilder.loadTexts:
    pnniRouteConflictPort5.setStatus(
        ""
    )

pnniRouteConflictSamePG5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 800, 3, 1, 1, 1, 0, 51)
)
if mibBuilder.loadTexts:
    pnniRouteConflictSamePG5.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLANTRAP-5-MIB",
    **{"tempAlarm5": tempAlarm5,
       "moduleChange5": moduleChange5,
       "powerEvent5": powerEvent5,
       "controllerEvent5": controllerEvent5,
       "loginViolation5": loginViolation5,
       "macVlanViolation5": macVlanViolation5,
       "macDuplicatePort5": macDuplicatePort5,
       "portLinkUpEvent5": portLinkUpEvent5,
       "portLinkDownEvent5": portLinkDownEvent5,
       "portPartitioned5": portPartitioned5,
       "portRecordMismatch5": portRecordMismatch5,
       "groupChange5": groupChange5,
       "vlanChange5": vlanChange5,
       "portMove5": portMove5,
       "moduleResetReload5": moduleResetReload5,
       "systemEvent5": systemEvent5,
       "vlanRouteTableFull5": vlanRouteTableFull5,
       "sapTableFull5": sapTableFull5,
       "atmSSCOPstate5": atmSSCOPstate5,
       "ilmiState5": ilmiState5,
       "atmConnection5": atmConnection5,
       "atmService5": atmService5,
       "dlciNew5": dlciNew5,
       "dlciDel5": dlciDel5,
       "dlciUp5": dlciUp5,
       "dlciDn5": dlciDn5,
       "portManualForwardingMode5": portManualForwardingMode5,
       "fddiCFStateChange5": fddiCFStateChange5,
       "duplicateIPaddress5": duplicateIPaddress5,
       "duplicateMACaddress5": duplicateMACaddress5,
       "healthThresholdRising5": healthThresholdRising5,
       "healthThresholdFalling5": healthThresholdFalling5,
       "healthThresholdDevice5": healthThresholdDevice5,
       "healthThresholdModule5": healthThresholdModule5,
       "pnniRouteConflictPort5": pnniRouteConflictPort5,
       "pnniRouteConflictSamePG5": pnniRouteConflictSamePG5}
)
