# SNMP MIB module (RADLAN-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:43:45 2024
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

(rldot1dStpTrapVrblVID,
 rldot1dStpTrapVrblifIndex) = mibBuilder.importSymbols(
    "RADLAN-BRIDGEMIBOBJECTS-MIB",
    "rldot1dStpTrapVrblVID",
    "rldot1dStpTrapVrblifIndex")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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

rndNotifications = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 0)
)
rndNotifications.setRevisions(
        ("2010-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

rxOverflowHWFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 3)
)
rxOverflowHWFault.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rxOverflowHWFault.setStatus(
        "current"
    )

txOverflowHWFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 4)
)
txOverflowHWFault.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    txOverflowHWFault.setStatus(
        "current"
    )

routeTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 5)
)
routeTableOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    routeTableOverflow.setStatus(
        "current"
    )

resetRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 10)
)
resetRequired.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    resetRequired.setStatus(
        "current"
    )

endTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 12)
)
endTftp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    endTftp.setStatus(
        "current"
    )

abortTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 13)
)
abortTftp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    abortTftp.setStatus(
        "current"
    )

startTftp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 14)
)
startTftp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    startTftp.setStatus(
        "current"
    )

faultBackUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 23)
)
faultBackUp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    faultBackUp.setStatus(
        "current"
    )

mainLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 24)
)
mainLinkUp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    mainLinkUp.setStatus(
        "current"
    )

ipxRipTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 36)
)
ipxRipTblOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxRipTblOverflow.setStatus(
        "current"
    )

ipxSapTblOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 37)
)
ipxSapTblOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    ipxSapTblOverflow.setStatus(
        "current"
    )

facsAccessVoilation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 49)
)
facsAccessVoilation.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    facsAccessVoilation.setStatus(
        "current"
    )

autoConfigurationCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 50)
)
autoConfigurationCompleted.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    autoConfigurationCompleted.setStatus(
        "current"
    )

forwardingTabOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 51)
)
forwardingTabOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    forwardingTabOverflow.setStatus(
        "current"
    )

framRelaySwitchConnectionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 53)
)
framRelaySwitchConnectionUp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    framRelaySwitchConnectionUp.setStatus(
        "current"
    )

framRelaySwitchConnectionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 54)
)
framRelaySwitchConnectionDown.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    framRelaySwitchConnectionDown.setStatus(
        "current"
    )

errorsDuringInit = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 61)
)
errorsDuringInit.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    errorsDuringInit.setStatus(
        "current"
    )

vlanDynPortAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 66)
)
vlanDynPortAdded.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortAdded.setStatus(
        "current"
    )

vlanDynPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 67)
)
vlanDynPortRemoved.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynPortRemoved.setStatus(
        "current"
    )

rsSDclientsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 68)
)
rsSDclientsTableOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDclientsTableOverflow.setStatus(
        "current"
    )

rsSDinactiveServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 69)
)
rsSDinactiveServer.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSDinactiveServer.setStatus(
        "current"
    )

rsIpZhrConnectionsTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 70)
)
rsIpZhrConnectionsTableOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrConnectionsTableOverflow.setStatus(
        "current"
    )

rsIpZhrReqStaticConnNotAccepted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 71)
)
rsIpZhrReqStaticConnNotAccepted.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrReqStaticConnNotAccepted.setStatus(
        "current"
    )

rsIpZhrVirtualIpAsSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 72)
)
rsIpZhrVirtualIpAsSource.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrVirtualIpAsSource.setStatus(
        "current"
    )

rsIpZhrNotAllocVirtualIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 73)
)
rsIpZhrNotAllocVirtualIp.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsIpZhrNotAllocVirtualIp.setStatus(
        "current"
    )

rsSnmpSetRequestInSpecialCfgState = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 74)
)
rsSnmpSetRequestInSpecialCfgState.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsSnmpSetRequestInSpecialCfgState.setStatus(
        "current"
    )

rsPingCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 136)
)
rsPingCompletion.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsPingCompletion.setStatus(
        "current"
    )

pppSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 137)
)
pppSecurityViolation.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    pppSecurityViolation.setStatus(
        "current"
    )

frDLCIStatudChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 138)
)
frDLCIStatudChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    frDLCIStatudChange.setStatus(
        "current"
    )

papFailedCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 139)
)
papFailedCommunication.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    papFailedCommunication.setStatus(
        "current"
    )

chapFailedCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 140)
)
chapFailedCommunication.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    chapFailedCommunication.setStatus(
        "current"
    )

rsWSDRedundancySwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 141)
)
rsWSDRedundancySwitch.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsWSDRedundancySwitch.setStatus(
        "current"
    )

rsDhcpAllocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 142)
)
rsDhcpAllocationFailure.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rsDhcpAllocationFailure.setStatus(
        "current"
    )

rlIpFftStnOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 145)
)
rlIpFftStnOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpFftStnOverflow.setStatus(
        "current"
    )

rlIpFftSubOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 146)
)
rlIpFftSubOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpFftSubOverflow.setStatus(
        "current"
    )

rlIpxFftStnOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 147)
)
rlIpxFftStnOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpxFftStnOverflow.setStatus(
        "current"
    )

rlIpxFftSubOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 148)
)
rlIpxFftSubOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpxFftSubOverflow.setStatus(
        "current"
    )

rlIpmFftOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 149)
)
rlIpmFftOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIpmFftOverflow.setStatus(
        "current"
    )

rlPhysicalDescriptionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 150)
)
rlPhysicalDescriptionChanged.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPhysicalDescriptionChanged.setStatus(
        "current"
    )

rldot1dStpPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 151)
)
rldot1dStpPortStateForwarding.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    rldot1dStpPortStateForwarding.setStatus(
        "current"
    )

rldot1dStpPortStateNotForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 152)
)
rldot1dStpPortStateNotForwarding.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblifIndex"),
        ("RADLAN-BRIDGEMIBOBJECTS-MIB", "rldot1dStpTrapVrblVID"))
)
if mibBuilder.loadTexts:
    rldot1dStpPortStateNotForwarding.setStatus(
        "current"
    )

rlPolicyDropPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 153)
)
rlPolicyDropPacketTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPolicyDropPacketTrap.setStatus(
        "current"
    )

rlPolicyForwardPacketTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 154)
)
rlPolicyForwardPacketTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPolicyForwardPacketTrap.setStatus(
        "current"
    )

rlIgmpProxyTableOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 156)
)
rlIgmpProxyTableOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpProxyTableOverflow.setStatus(
        "current"
    )

rlIgmpV1MsgReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 157)
)
rlIgmpV1MsgReceived.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpV1MsgReceived.setStatus(
        "current"
    )

rlVrrpEntriesDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 158)
)
rlVrrpEntriesDeleted.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlVrrpEntriesDeleted.setStatus(
        "current"
    )

rlHotSwapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 159)
)
rlHotSwapTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlHotSwapTrap.setStatus(
        "current"
    )

rlTrunkPortAddedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 160)
)
rlTrunkPortAddedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortAddedTrap.setStatus(
        "current"
    )

rlTrunkPortRemovedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 161)
)
rlTrunkPortRemovedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortRemovedTrap.setStatus(
        "current"
    )

rlTrunkPortNotCapableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 162)
)
rlTrunkPortNotCapableTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlTrunkPortNotCapableTrap.setStatus(
        "current"
    )

rlLockPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 170)
)
rlLockPortTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlLockPortTrap.setStatus(
        "current"
    )

vlanDynVlanAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 171)
)
vlanDynVlanAdded.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynVlanAdded.setStatus(
        "current"
    )

vlanDynVlanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 172)
)
vlanDynVlanRemoved.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynVlanRemoved.setStatus(
        "current"
    )

vlanDynamicToStatic = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 173)
)
vlanDynamicToStatic.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanDynamicToStatic.setStatus(
        "current"
    )

vlanStaticToDynamic = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 174)
)
vlanStaticToDynamic.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    vlanStaticToDynamic.setStatus(
        "current"
    )

dstrSysLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 175)
)
dstrSysLog.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    dstrSysLog.setStatus(
        "current"
    )

rlEnvMonFanStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 176)
)
rlEnvMonFanStateChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonFanStateChange.setStatus(
        "current"
    )

rlEnvMonPowerSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 177)
)
rlEnvMonPowerSupplyStateChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonPowerSupplyStateChange.setStatus(
        "current"
    )

rlStackStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 178)
)
rlStackStateChange.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackStateChange.setStatus(
        "current"
    )

rlEnvMonTemperatureRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 179)
)
rlEnvMonTemperatureRisingAlarm.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEnvMonTemperatureRisingAlarm.setStatus(
        "current"
    )

rlBrgMacAddFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 183)
)
rlBrgMacAddFailedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlBrgMacAddFailedTrap.setStatus(
        "current"
    )

rldot1xPortStatusAuthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 184)
)
rldot1xPortStatusAuthorizedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xPortStatusAuthorizedTrap.setStatus(
        "current"
    )

rldot1xPortStatusUnauthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 185)
)
rldot1xPortStatusUnauthorizedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xPortStatusUnauthorizedTrap.setStatus(
        "current"
    )

swIfTablePortLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 192)
)
swIfTablePortLock.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    swIfTablePortLock.setStatus(
        "current"
    )

swIfTablePortUnLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 193)
)
swIfTablePortUnLock.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    swIfTablePortUnLock.setStatus(
        "current"
    )

rlAAAUserLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 194)
)
rlAAAUserLocked.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlAAAUserLocked.setStatus(
        "current"
    )

bpduGuardPortSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 202)
)
bpduGuardPortSuspended.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    bpduGuardPortSuspended.setStatus(
        "current"
    )

rldot1xSupplicantMacAuthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 203)
)
rldot1xSupplicantMacAuthorizedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantMacAuthorizedTrap.setStatus(
        "current"
    )

rldot1xSupplicantMacUnauthorizedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 204)
)
rldot1xSupplicantMacUnauthorizedTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantMacUnauthorizedTrap.setStatus(
        "current"
    )

stpLoopbackDetection = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 205)
)
stpLoopbackDetection.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    stpLoopbackDetection.setStatus(
        "current"
    )

stpLoopbackDetectionResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 206)
)
stpLoopbackDetectionResolved.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    stpLoopbackDetectionResolved.setStatus(
        "current"
    )

loopbackDetectionPortSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 207)
)
loopbackDetectionPortSuspended.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    loopbackDetectionPortSuspended.setStatus(
        "current"
    )

rlPortSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 213)
)
rlPortSuspended.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlPortSuspended.setStatus(
        "current"
    )

rlSpecialBpduDbOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 214)
)
rlSpecialBpduDbOverflow.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlSpecialBpduDbOverflow.setStatus(
        "current"
    )

rldot1xSupplicantLoggedOutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 215)
)
rldot1xSupplicantLoggedOutTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantLoggedOutTrap.setStatus(
        "current"
    )

rldot1xPortControlModeNotAutoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 216)
)
rldot1xPortControlModeNotAutoTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xPortControlModeNotAutoTrap.setStatus(
        "current"
    )

rlEeeLldpMultipleNeighbours = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 217)
)
rlEeeLldpMultipleNeighbours.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEeeLldpMultipleNeighbours.setStatus(
        "current"
    )

rlEeeLldpSingleNeighbour = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 218)
)
rlEeeLldpSingleNeighbour.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlEeeLldpSingleNeighbour.setStatus(
        "current"
    )

rldot1xSupplicantQuietPeriodTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 219)
)
rldot1xSupplicantQuietPeriodTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rldot1xSupplicantQuietPeriodTrap.setStatus(
        "current"
    )

rlStackVersionUpgradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 222)
)
rlStackVersionUpgradeTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackVersionUpgradeTrap.setStatus(
        "current"
    )

rlStackVersionDowngradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 223)
)
rlStackVersionDowngradeTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStackVersionDowngradeTrap.setStatus(
        "current"
    )

pseInrushPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 240)
)
pseInrushPort.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    pseInrushPort.setStatus(
        "current"
    )

pseOverloadPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 241)
)
pseOverloadPort.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    pseOverloadPort.setStatus(
        "current"
    )

poePowerNegotiationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 242)
)
poePowerNegotiationInfo.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    poePowerNegotiationInfo.setStatus(
        "current"
    )

poePowerNegotiation4Wire = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 243)
)
poePowerNegotiation4Wire.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    poePowerNegotiation4Wire.setStatus(
        "current"
    )

poePowerHWFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 244)
)
poePowerHWFail.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    poePowerHWFail.setStatus(
        "current"
    )

rlStormControlMinRateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 246)
)
rlStormControlMinRateTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStormControlMinRateTrap.setStatus(
        "current"
    )

rlApBackplanePortResolutionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 247)
)
rlApBackplanePortResolutionTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlApBackplanePortResolutionTrap.setStatus(
        "current"
    )

sfpPortPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 248)
)
sfpPortPresent.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    sfpPortPresent.setStatus(
        "current"
    )

sfpPortNotPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 249)
)
sfpPortNotPresent.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    sfpPortNotPresent.setStatus(
        "current"
    )

sfpPortLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 250)
)
sfpPortLoss.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    sfpPortLoss.setStatus(
        "current"
    )

sfpPortNotLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 251)
)
sfpPortNotLoss.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    sfpPortNotLoss.setStatus(
        "current"
    )

rlStormControlOccursTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 252)
)
rlStormControlOccursTrap.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlStormControlOccursTrap.setStatus(
        "current"
    )

rlRadiusServTrapAcct = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 255)
)
rlRadiusServTrapAcct.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlRadiusServTrapAcct.setStatus(
        "current"
    )

rlRadiusServTrapAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 256)
)
rlRadiusServTrapAuthFailure.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlRadiusServTrapAuthFailure.setStatus(
        "current"
    )

rlRadiusServTrapAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 257)
)
rlRadiusServTrapAuthSuccess.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlRadiusServTrapAuthSuccess.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-TRAPS-MIB",
    **{"rndNotifications": rndNotifications,
       "rxOverflowHWFault": rxOverflowHWFault,
       "txOverflowHWFault": txOverflowHWFault,
       "routeTableOverflow": routeTableOverflow,
       "resetRequired": resetRequired,
       "endTftp": endTftp,
       "abortTftp": abortTftp,
       "startTftp": startTftp,
       "faultBackUp": faultBackUp,
       "mainLinkUp": mainLinkUp,
       "ipxRipTblOverflow": ipxRipTblOverflow,
       "ipxSapTblOverflow": ipxSapTblOverflow,
       "facsAccessVoilation": facsAccessVoilation,
       "autoConfigurationCompleted": autoConfigurationCompleted,
       "forwardingTabOverflow": forwardingTabOverflow,
       "framRelaySwitchConnectionUp": framRelaySwitchConnectionUp,
       "framRelaySwitchConnectionDown": framRelaySwitchConnectionDown,
       "errorsDuringInit": errorsDuringInit,
       "vlanDynPortAdded": vlanDynPortAdded,
       "vlanDynPortRemoved": vlanDynPortRemoved,
       "rsSDclientsTableOverflow": rsSDclientsTableOverflow,
       "rsSDinactiveServer": rsSDinactiveServer,
       "rsIpZhrConnectionsTableOverflow": rsIpZhrConnectionsTableOverflow,
       "rsIpZhrReqStaticConnNotAccepted": rsIpZhrReqStaticConnNotAccepted,
       "rsIpZhrVirtualIpAsSource": rsIpZhrVirtualIpAsSource,
       "rsIpZhrNotAllocVirtualIp": rsIpZhrNotAllocVirtualIp,
       "rsSnmpSetRequestInSpecialCfgState": rsSnmpSetRequestInSpecialCfgState,
       "rsPingCompletion": rsPingCompletion,
       "pppSecurityViolation": pppSecurityViolation,
       "frDLCIStatudChange": frDLCIStatudChange,
       "papFailedCommunication": papFailedCommunication,
       "chapFailedCommunication": chapFailedCommunication,
       "rsWSDRedundancySwitch": rsWSDRedundancySwitch,
       "rsDhcpAllocationFailure": rsDhcpAllocationFailure,
       "rlIpFftStnOverflow": rlIpFftStnOverflow,
       "rlIpFftSubOverflow": rlIpFftSubOverflow,
       "rlIpxFftStnOverflow": rlIpxFftStnOverflow,
       "rlIpxFftSubOverflow": rlIpxFftSubOverflow,
       "rlIpmFftOverflow": rlIpmFftOverflow,
       "rlPhysicalDescriptionChanged": rlPhysicalDescriptionChanged,
       "rldot1dStpPortStateForwarding": rldot1dStpPortStateForwarding,
       "rldot1dStpPortStateNotForwarding": rldot1dStpPortStateNotForwarding,
       "rlPolicyDropPacketTrap": rlPolicyDropPacketTrap,
       "rlPolicyForwardPacketTrap": rlPolicyForwardPacketTrap,
       "rlIgmpProxyTableOverflow": rlIgmpProxyTableOverflow,
       "rlIgmpV1MsgReceived": rlIgmpV1MsgReceived,
       "rlVrrpEntriesDeleted": rlVrrpEntriesDeleted,
       "rlHotSwapTrap": rlHotSwapTrap,
       "rlTrunkPortAddedTrap": rlTrunkPortAddedTrap,
       "rlTrunkPortRemovedTrap": rlTrunkPortRemovedTrap,
       "rlTrunkPortNotCapableTrap": rlTrunkPortNotCapableTrap,
       "rlLockPortTrap": rlLockPortTrap,
       "vlanDynVlanAdded": vlanDynVlanAdded,
       "vlanDynVlanRemoved": vlanDynVlanRemoved,
       "vlanDynamicToStatic": vlanDynamicToStatic,
       "vlanStaticToDynamic": vlanStaticToDynamic,
       "dstrSysLog": dstrSysLog,
       "rlEnvMonFanStateChange": rlEnvMonFanStateChange,
       "rlEnvMonPowerSupplyStateChange": rlEnvMonPowerSupplyStateChange,
       "rlStackStateChange": rlStackStateChange,
       "rlEnvMonTemperatureRisingAlarm": rlEnvMonTemperatureRisingAlarm,
       "rlBrgMacAddFailedTrap": rlBrgMacAddFailedTrap,
       "rldot1xPortStatusAuthorizedTrap": rldot1xPortStatusAuthorizedTrap,
       "rldot1xPortStatusUnauthorizedTrap": rldot1xPortStatusUnauthorizedTrap,
       "swIfTablePortLock": swIfTablePortLock,
       "swIfTablePortUnLock": swIfTablePortUnLock,
       "rlAAAUserLocked": rlAAAUserLocked,
       "bpduGuardPortSuspended": bpduGuardPortSuspended,
       "rldot1xSupplicantMacAuthorizedTrap": rldot1xSupplicantMacAuthorizedTrap,
       "rldot1xSupplicantMacUnauthorizedTrap": rldot1xSupplicantMacUnauthorizedTrap,
       "stpLoopbackDetection": stpLoopbackDetection,
       "stpLoopbackDetectionResolved": stpLoopbackDetectionResolved,
       "loopbackDetectionPortSuspended": loopbackDetectionPortSuspended,
       "rlPortSuspended": rlPortSuspended,
       "rlSpecialBpduDbOverflow": rlSpecialBpduDbOverflow,
       "rldot1xSupplicantLoggedOutTrap": rldot1xSupplicantLoggedOutTrap,
       "rldot1xPortControlModeNotAutoTrap": rldot1xPortControlModeNotAutoTrap,
       "rlEeeLldpMultipleNeighbours": rlEeeLldpMultipleNeighbours,
       "rlEeeLldpSingleNeighbour": rlEeeLldpSingleNeighbour,
       "rldot1xSupplicantQuietPeriodTrap": rldot1xSupplicantQuietPeriodTrap,
       "rlStackVersionUpgradeTrap": rlStackVersionUpgradeTrap,
       "rlStackVersionDowngradeTrap": rlStackVersionDowngradeTrap,
       "pseInrushPort": pseInrushPort,
       "pseOverloadPort": pseOverloadPort,
       "poePowerNegotiationInfo": poePowerNegotiationInfo,
       "poePowerNegotiation4Wire": poePowerNegotiation4Wire,
       "poePowerHWFail": poePowerHWFail,
       "rlStormControlMinRateTrap": rlStormControlMinRateTrap,
       "rlApBackplanePortResolutionTrap": rlApBackplanePortResolutionTrap,
       "sfpPortPresent": sfpPortPresent,
       "sfpPortNotPresent": sfpPortNotPresent,
       "sfpPortLoss": sfpPortLoss,
       "sfpPortNotLoss": sfpPortNotLoss,
       "rlStormControlOccursTrap": rlStormControlOccursTrap,
       "rlRadiusServTrapAcct": rlRadiusServTrapAcct,
       "rlRadiusServTrapAuthFailure": rlRadiusServTrapAuthFailure,
       "rlRadiusServTrapAuthSuccess": rlRadiusServTrapAuthSuccess}
)
