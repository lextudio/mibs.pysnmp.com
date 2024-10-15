# SNMP MIB module (BW-NetworkServerFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-NetworkServerFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:08 2024
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

(alarmName,
 alarmState,
 common,
 component,
 faultFields,
 identifier,
 problemText,
 recommendedActionsText,
 severity,
 subcomponent,
 systemName,
 timeStamp) = mibBuilder.importSymbols(
    "BroadworksFault",
    "alarmName",
    "alarmState",
    "common",
    "component",
    "faultFields",
    "identifier",
    "problemText",
    "recommendedActionsText",
    "severity",
    "subcomponent",
    "systemName",
    "timeStamp")

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

systemFaults = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1)
)
systemFaults.setRevisions(
        ("2000-09-19 14:31",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects

bwPMNSExecutionServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1001)
)
bwPMNSExecutionServerLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSExecutionServerLaunched.setStatus(
        "current"
    )

bwPMNSExecutionServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1002)
)
bwPMNSExecutionServerShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSExecutionServerShutDown.setStatus(
        "current"
    )

bwPMNSExecutionServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1003)
)
bwPMNSExecutionServerRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSExecutionServerRestarted.setStatus(
        "current"
    )

bwPMNSExecutionServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1004)
)
bwPMNSExecutionServerDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSExecutionServerDeath.setStatus(
        "current"
    )

bwPMNSProvisioningServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1005)
)
bwPMNSProvisioningServerLaunched.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSProvisioningServerLaunched.setStatus(
        "current"
    )

bwPMNSProvisioningServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1006)
)
bwPMNSProvisioningServerShutDown.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSProvisioningServerShutDown.setStatus(
        "current"
    )

bwPMNSProvisioningServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1007)
)
bwPMNSProvisioningServerRestarted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSProvisioningServerRestarted.setStatus(
        "current"
    )

bwPMNSProvisioningServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1008)
)
bwPMNSProvisioningServerDeath.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwPMNSProvisioningServerDeath.setStatus(
        "current"
    )

bwNoRowInNNACLFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1009)
)
bwNoRowInNNACLFailure.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNoRowInNNACLFailure.setStatus(
        "current"
    )

bwNSMemLeakInSessionFactory = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1010)
)
bwNSMemLeakInSessionFactory.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSMemLeakInSessionFactory.setStatus(
        "current"
    )

bwNSPolicyDeploymentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1011)
)
bwNSPolicyDeploymentError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSPolicyDeploymentError.setStatus(
        "current"
    )

bwNSDatabaseDataInconsistencyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1012)
)
bwNSDatabaseDataInconsistencyError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSDatabaseDataInconsistencyError.setStatus(
        "current"
    )

bwNSCallGotTreatment = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1013)
)
bwNSCallGotTreatment.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSCallGotTreatment.setStatus(
        "current"
    )

bwNSInvalidDialPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1014)
)
bwNSInvalidDialPlan.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSInvalidDialPlan.setStatus(
        "current"
    )

bwNSSCRPInconsistentList = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1015)
)
bwNSSCRPInconsistentList.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSCRPInconsistentList.setStatus(
        "current"
    )

bwNSUnlicensedFeature = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1016)
)
bwNSUnlicensedFeature.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSUnlicensedFeature.setStatus(
        "current"
    )

bwCallLogRegister = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1019)
)
bwCallLogRegister.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCallLogRegister.setStatus(
        "current"
    )

bwCallLogUnregister = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1020)
)
bwCallLogUnregister.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCallLogUnregister.setStatus(
        "current"
    )

bwCallLogFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1021)
)
bwCallLogFailure.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCallLogFailure.setStatus(
        "current"
    )

bwCallLogUnregisterFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1022)
)
bwCallLogUnregisterFailure.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwCallLogUnregisterFailure.setStatus(
        "current"
    )

bwNSASRUnknowHostError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1023)
)
bwNSASRUnknowHostError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSASRUnknowHostError.setStatus(
        "current"
    )

bwNSSynchUnknownHostnameError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1024)
)
bwNSSynchUnknownHostnameError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUnknownHostnameError.setStatus(
        "current"
    )

bwNSSynchTrustedKeyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1025)
)
bwNSSynchTrustedKeyError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchTrustedKeyError.setStatus(
        "current"
    )

bwNSSynchExceptionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1026)
)
bwNSSynchExceptionError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchExceptionError.setStatus(
        "current"
    )

bwNSSynchUpdateXMLError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1027)
)
bwNSSynchUpdateXMLError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUpdateXMLError.setStatus(
        "current"
    )

bwNSSynchUpdateFailureError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1028)
)
bwNSSynchUpdateFailureError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUpdateFailureError.setStatus(
        "current"
    )

bwNSSynchUpdateExceptionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1029)
)
bwNSSynchUpdateExceptionError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUpdateExceptionError.setStatus(
        "current"
    )

bwNSSynchUpdateIncorrectVersionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1030)
)
bwNSSynchUpdateIncorrectVersionError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUpdateIncorrectVersionError.setStatus(
        "current"
    )

bwNSSynchUpdateIncorrectProtocolError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1031)
)
bwNSSynchUpdateIncorrectProtocolError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNSSynchUpdateIncorrectProtocolError.setStatus(
        "current"
    )

bwNetworkDeviceNodeIsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1032)
)
bwNetworkDeviceNodeIsFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNetworkDeviceNodeIsFailed.setStatus(
        "current"
    )

bwNetworkDeviceNodeIsOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1033)
)
bwNetworkDeviceNodeIsOnline.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNetworkDeviceNodeIsOnline.setStatus(
        "current"
    )

bwLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1034)
)
bwLicenseViolation.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseViolation.setStatus(
        "current"
    )

bwLicenseThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1035)
)
bwLicenseThreshold.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLicenseThreshold.setStatus(
        "current"
    )

bwServiceControlProxyConnFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1036)
)
bwServiceControlProxyConnFailed.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwServiceControlProxyConnFailed.setStatus(
        "current"
    )

bwServiceControlProxyConnTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1037)
)
bwServiceControlProxyConnTerminated.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwServiceControlProxyConnTerminated.setStatus(
        "current"
    )

bwNonInviteLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1038)
)
bwNonInviteLicenseViolation.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNonInviteLicenseViolation.setStatus(
        "current"
    )

bwNonInviteLicenseThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1039)
)
bwNonInviteLicenseThreshold.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwNonInviteLicenseThreshold.setStatus(
        "current"
    )

bwLocationAPIRequestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1040)
)
bwLocationAPIRequestError.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwLocationAPIRequestError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-NetworkServerFault",
    **{"systemFaults": systemFaults,
       "bwPMNSExecutionServerLaunched": bwPMNSExecutionServerLaunched,
       "bwPMNSExecutionServerShutDown": bwPMNSExecutionServerShutDown,
       "bwPMNSExecutionServerRestarted": bwPMNSExecutionServerRestarted,
       "bwPMNSExecutionServerDeath": bwPMNSExecutionServerDeath,
       "bwPMNSProvisioningServerLaunched": bwPMNSProvisioningServerLaunched,
       "bwPMNSProvisioningServerShutDown": bwPMNSProvisioningServerShutDown,
       "bwPMNSProvisioningServerRestarted": bwPMNSProvisioningServerRestarted,
       "bwPMNSProvisioningServerDeath": bwPMNSProvisioningServerDeath,
       "bwNoRowInNNACLFailure": bwNoRowInNNACLFailure,
       "bwNSMemLeakInSessionFactory": bwNSMemLeakInSessionFactory,
       "bwNSPolicyDeploymentError": bwNSPolicyDeploymentError,
       "bwNSDatabaseDataInconsistencyError": bwNSDatabaseDataInconsistencyError,
       "bwNSCallGotTreatment": bwNSCallGotTreatment,
       "bwNSInvalidDialPlan": bwNSInvalidDialPlan,
       "bwNSSCRPInconsistentList": bwNSSCRPInconsistentList,
       "bwNSUnlicensedFeature": bwNSUnlicensedFeature,
       "bwCallLogRegister": bwCallLogRegister,
       "bwCallLogUnregister": bwCallLogUnregister,
       "bwCallLogFailure": bwCallLogFailure,
       "bwCallLogUnregisterFailure": bwCallLogUnregisterFailure,
       "bwNSASRUnknowHostError": bwNSASRUnknowHostError,
       "bwNSSynchUnknownHostnameError": bwNSSynchUnknownHostnameError,
       "bwNSSynchTrustedKeyError": bwNSSynchTrustedKeyError,
       "bwNSSynchExceptionError": bwNSSynchExceptionError,
       "bwNSSynchUpdateXMLError": bwNSSynchUpdateXMLError,
       "bwNSSynchUpdateFailureError": bwNSSynchUpdateFailureError,
       "bwNSSynchUpdateExceptionError": bwNSSynchUpdateExceptionError,
       "bwNSSynchUpdateIncorrectVersionError": bwNSSynchUpdateIncorrectVersionError,
       "bwNSSynchUpdateIncorrectProtocolError": bwNSSynchUpdateIncorrectProtocolError,
       "bwNetworkDeviceNodeIsFailed": bwNetworkDeviceNodeIsFailed,
       "bwNetworkDeviceNodeIsOnline": bwNetworkDeviceNodeIsOnline,
       "bwLicenseViolation": bwLicenseViolation,
       "bwLicenseThreshold": bwLicenseThreshold,
       "bwServiceControlProxyConnFailed": bwServiceControlProxyConnFailed,
       "bwServiceControlProxyConnTerminated": bwServiceControlProxyConnTerminated,
       "bwNonInviteLicenseViolation": bwNonInviteLicenseViolation,
       "bwNonInviteLicenseThreshold": bwNonInviteLicenseThreshold,
       "bwLocationAPIRequestError": bwLocationAPIRequestError}
)
