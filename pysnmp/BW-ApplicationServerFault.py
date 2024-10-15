# SNMP MIB module (BW-ApplicationServerFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-ApplicationServerFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:59 2024
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

bwApplicationServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2501)
)
bwApplicationServerUnreachable.setObjects(
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
    bwApplicationServerUnreachable.setStatus(
        "current"
    )

bwNetworkServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2502)
)
bwNetworkServerUnreachable.setObjects(
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
    bwNetworkServerUnreachable.setStatus(
        "current"
    )

bwNetworkServerRequestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2503)
)
bwNetworkServerRequestError.setObjects(
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
    bwNetworkServerRequestError.setStatus(
        "current"
    )

bwCMSConnectivityDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2504)
)
bwCMSConnectivityDown.setObjects(
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
    bwCMSConnectivityDown.setStatus(
        "current"
    )

bwCMSConnectivityUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2505)
)
bwCMSConnectivityUp.setObjects(
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
    bwCMSConnectivityUp.setStatus(
        "current"
    )

bwCMSDatabaseMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 2506)
)
bwCMSDatabaseMismatch.setObjects(
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
    bwCMSDatabaseMismatch.setStatus(
        "current"
    )

bwPMExecutionServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3501)
)
bwPMExecutionServerLaunched.setObjects(
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
    bwPMExecutionServerLaunched.setStatus(
        "current"
    )

bwPMExecutionServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3502)
)
bwPMExecutionServerShutDown.setObjects(
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
    bwPMExecutionServerShutDown.setStatus(
        "current"
    )

bwPMExecutionServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3503)
)
bwPMExecutionServerRestarted.setObjects(
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
    bwPMExecutionServerRestarted.setStatus(
        "current"
    )

bwPMExecutionServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3504)
)
bwPMExecutionServerDeath.setObjects(
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
    bwPMExecutionServerDeath.setStatus(
        "current"
    )

bwPMProvisioningServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3505)
)
bwPMProvisioningServerLaunched.setObjects(
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
    bwPMProvisioningServerLaunched.setStatus(
        "current"
    )

bwPMProvisioningServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3506)
)
bwPMProvisioningServerShutDown.setObjects(
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
    bwPMProvisioningServerShutDown.setStatus(
        "current"
    )

bwPMProvisioningServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3507)
)
bwPMProvisioningServerRestarted.setObjects(
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
    bwPMProvisioningServerRestarted.setStatus(
        "current"
    )

bwPMProvisioningServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3508)
)
bwPMProvisioningServerDeath.setObjects(
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
    bwPMProvisioningServerDeath.setStatus(
        "current"
    )

bwSipMessageParsingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3509)
)
bwSipMessageParsingError.setObjects(
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
    bwSipMessageParsingError.setStatus(
        "current"
    )

bwSipRegistrationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3510)
)
bwSipRegistrationFailure.setObjects(
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
    bwSipRegistrationFailure.setStatus(
        "current"
    )

bwSipUnexpectedMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3511)
)
bwSipUnexpectedMessage.setObjects(
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
    bwSipUnexpectedMessage.setStatus(
        "current"
    )

bwSipMaxRetriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3512)
)
bwSipMaxRetriesExceeded.setObjects(
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
    bwSipMaxRetriesExceeded.setStatus(
        "current"
    )

bwSipRequestTimeOutReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3513)
)
bwSipRequestTimeOutReceived.setObjects(
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
    bwSipRequestTimeOutReceived.setStatus(
        "current"
    )

bwSipServiceUnavailableReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3514)
)
bwSipServiceUnavailableReceived.setObjects(
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
    bwSipServiceUnavailableReceived.setStatus(
        "current"
    )

bwSipServerTimeOutReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3515)
)
bwSipServerTimeOutReceived.setObjects(
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
    bwSipServerTimeOutReceived.setStatus(
        "current"
    )

bwSipAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3516)
)
bwSipAuthenticationFailure.setObjects(
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
    bwSipAuthenticationFailure.setStatus(
        "current"
    )

bwAclViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3517)
)
bwAclViolation.setObjects(
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
    bwAclViolation.setStatus(
        "current"
    )

bwSipUnrecognisedDomainName = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3518)
)
bwSipUnrecognisedDomainName.setObjects(
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
    bwSipUnrecognisedDomainName.setStatus(
        "current"
    )

bwSMTPPrimaryServerEmailMessageDeliveryError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3519)
)
bwSMTPPrimaryServerEmailMessageDeliveryError.setObjects(
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
    bwSMTPPrimaryServerEmailMessageDeliveryError.setStatus(
        "current"
    )

bwSMTPConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3520)
)
bwSMTPConnectivityFailure.setObjects(
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
    bwSMTPConnectivityFailure.setStatus(
        "current"
    )

bwIMSRetrieveMessageError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3521)
)
bwIMSRetrieveMessageError.setObjects(
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
    bwIMSRetrieveMessageError.setStatus(
        "current"
    )

bwIMSRetrieveMailBoxInfoError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3522)
)
bwIMSRetrieveMailBoxInfoError.setObjects(
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
    bwIMSRetrieveMailBoxInfoError.setStatus(
        "current"
    )

bwIMSConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3523)
)
bwIMSConnectionFailure.setObjects(
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
    bwIMSConnectionFailure.setStatus(
        "current"
    )

bwIMSCloseConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3524)
)
bwIMSCloseConnectionError.setObjects(
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
    bwIMSCloseConnectionError.setStatus(
        "current"
    )

bwIMSUpdateMailBoxError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3525)
)
bwIMSUpdateMailBoxError.setObjects(
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
    bwIMSUpdateMailBoxError.setStatus(
        "current"
    )

bwMediaServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3526)
)
bwMediaServerNotResponding.setObjects(
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
    bwMediaServerNotResponding.setStatus(
        "current"
    )

bwMssNetworkServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3527)
)
bwMssNetworkServerNotResponding.setObjects(
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
    bwMssNetworkServerNotResponding.setStatus(
        "current"
    )

bwMssNoResponse = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3528)
)
bwMssNoResponse.setObjects(
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
    bwMssNoResponse.setStatus(
        "current"
    )

bwMGCPIOControllerUnknownReqIDInNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3529)
)
bwMGCPIOControllerUnknownReqIDInNotification.setObjects(
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
    bwMGCPIOControllerUnknownReqIDInNotification.setStatus(
        "current"
    )

bwMGCPMessageParsingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3530)
)
bwMGCPMessageParsingError.setObjects(
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
    bwMGCPMessageParsingError.setStatus(
        "current"
    )

bwMGCPCallAgentFailedMessageProcessing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3531)
)
bwMGCPCallAgentFailedMessageProcessing.setObjects(
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
    bwMGCPCallAgentFailedMessageProcessing.setStatus(
        "current"
    )

bwMGCPCallAgentMessageProcessing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3532)
)
bwMGCPCallAgentMessageProcessing.setObjects(
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
    bwMGCPCallAgentMessageProcessing.setStatus(
        "current"
    )

bwMGCPReTransmissionTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3533)
)
bwMGCPReTransmissionTimeout.setObjects(
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
    bwMGCPReTransmissionTimeout.setStatus(
        "current"
    )

bwMGCPUnrecognisedDomainName = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3534)
)
bwMGCPUnrecognisedDomainName.setObjects(
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
    bwMGCPUnrecognisedDomainName.setStatus(
        "current"
    )

bwMGCPUDPTransmitter = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3535)
)
bwMGCPUDPTransmitter.setObjects(
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
    bwMGCPUDPTransmitter.setStatus(
        "current"
    )

bwAuditAbnormalCallTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3536)
)
bwAuditAbnormalCallTermination.setObjects(
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
    bwAuditAbnormalCallTermination.setStatus(
        "current"
    )

bwNSSynchronizationConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3537)
)
bwNSSynchronizationConnectivityFailure.setObjects(
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
    bwNSSynchronizationConnectivityFailure.setStatus(
        "current"
    )

bwNSSynchronizationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3538)
)
bwNSSynchronizationFailure.setObjects(
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
    bwNSSynchronizationFailure.setStatus(
        "current"
    )

bwNSLocationConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3539)
)
bwNSLocationConnectivityFailure.setObjects(
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
    bwNSLocationConnectivityFailure.setStatus(
        "current"
    )

bwNSLocationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3540)
)
bwNSLocationFailure.setObjects(
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
    bwNSLocationFailure.setStatus(
        "current"
    )

bwLicenseAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3541)
)
bwLicenseAuthenticationFailure.setObjects(
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
    bwLicenseAuthenticationFailure.setStatus(
        "current"
    )

bwLicenseAccntViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3544)
)
bwLicenseAccntViolation.setObjects(
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
    bwLicenseAccntViolation.setStatus(
        "current"
    )

bwLicenseUserServiceAccntViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3545)
)
bwLicenseUserServiceAccntViolation.setObjects(
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
    bwLicenseUserServiceAccntViolation.setStatus(
        "current"
    )

bwAddUserEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3546)
)
bwAddUserEvent.setObjects(
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
    bwAddUserEvent.setStatus(
        "current"
    )

bwDeleteUserEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3547)
)
bwDeleteUserEvent.setObjects(
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
    bwDeleteUserEvent.setStatus(
        "current"
    )

bwAddGroupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3548)
)
bwAddGroupEvent.setObjects(
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
    bwAddGroupEvent.setStatus(
        "current"
    )

bwDeleteGroupEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3549)
)
bwDeleteGroupEvent.setObjects(
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
    bwDeleteGroupEvent.setStatus(
        "current"
    )

bwUserAddressChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3550)
)
bwUserAddressChangeEvent.setObjects(
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
    bwUserAddressChangeEvent.setStatus(
        "current"
    )

bwGroupAddressChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3551)
)
bwGroupAddressChangeEvent.setObjects(
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
    bwGroupAddressChangeEvent.setStatus(
        "current"
    )

bwEmergencyCallRoutingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3552)
)
bwEmergencyCallRoutingFailure.setObjects(
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
    bwEmergencyCallRoutingFailure.setStatus(
        "current"
    )

bwNetworkRoutingServiceRouteExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3553)
)
bwNetworkRoutingServiceRouteExhaustion.setObjects(
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
    bwNetworkRoutingServiceRouteExhaustion.setStatus(
        "current"
    )

bwCallPThreadAutoRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3555)
)
bwCallPThreadAutoRestart.setObjects(
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
    bwCallPThreadAutoRestart.setStatus(
        "current"
    )

bwForcedExitDueToHungThread = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3556)
)
bwForcedExitDueToHungThread.setObjects(
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
    bwForcedExitDueToHungThread.setStatus(
        "current"
    )

bwOCPMissingCountryCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3557)
)
bwOCPMissingCountryCode.setObjects(
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
    bwOCPMissingCountryCode.setStatus(
        "current"
    )

bwSystemDomainNameReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3558)
)
bwSystemDomainNameReset.setObjects(
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
    bwSystemDomainNameReset.setStatus(
        "current"
    )

bwAccountingFTPConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3560)
)
bwAccountingFTPConnectionError.setObjects(
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
    bwAccountingFTPConnectionError.setStatus(
        "current"
    )

bwCustomerOriginatedTrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3561)
)
bwCustomerOriginatedTrace.setObjects(
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
    bwCustomerOriginatedTrace.setStatus(
        "current"
    )

bwMaliciousCallTrace = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3562)
)
bwMaliciousCallTrace.setObjects(
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
    bwMaliciousCallTrace.setStatus(
        "current"
    )

bwLDAPConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3563)
)
bwLDAPConnectionError.setObjects(
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
    bwLDAPConnectionError.setStatus(
        "current"
    )

bwLDAPConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3564)
)
bwLDAPConfigurationError.setObjects(
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
    bwLDAPConfigurationError.setStatus(
        "current"
    )

bwCallCapacityManagementaddCallID = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3565)
)
bwCallCapacityManagementaddCallID.setObjects(
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
    bwCallCapacityManagementaddCallID.setStatus(
        "current"
    )

bwSMDIsessionRejected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3566)
)
bwSMDIsessionRejected.setObjects(
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
    bwSMDIsessionRejected.setStatus(
        "current"
    )

bwOCPMissingTransferNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3567)
)
bwOCPMissingTransferNumber.setObjects(
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
    bwOCPMissingTransferNumber.setStatus(
        "current"
    )

bwOCPMissingAuthorizationCode = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3568)
)
bwOCPMissingAuthorizationCode.setObjects(
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
    bwOCPMissingAuthorizationCode.setStatus(
        "current"
    )

bwDeviceStatusIsOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3569)
)
bwDeviceStatusIsOnline.setObjects(
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
    bwDeviceStatusIsOnline.setStatus(
        "current"
    )

bwDeviceStatusIsUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3570)
)
bwDeviceStatusIsUnavailable.setObjects(
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
    bwDeviceStatusIsUnavailable.setStatus(
        "current"
    )

bwCPEDeviceConfigurationFileNotTransmitted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3571)
)
bwCPEDeviceConfigurationFileNotTransmitted.setObjects(
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
    bwCPEDeviceConfigurationFileNotTransmitted.setStatus(
        "current"
    )

bwCPEDeviceConfigurationDeviceReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3572)
)
bwCPEDeviceConfigurationDeviceReset.setObjects(
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
    bwCPEDeviceConfigurationDeviceReset.setStatus(
        "current"
    )

bwCPEDeviceConfigurationFTPLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3573)
)
bwCPEDeviceConfigurationFTPLogin.setObjects(
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
    bwCPEDeviceConfigurationFTPLogin.setStatus(
        "current"
    )

bwSMDIInterfaceError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3574)
)
bwSMDIInterfaceError.setObjects(
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
    bwSMDIInterfaceError.setStatus(
        "current"
    )

bwSMDIConfigurationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3575)
)
bwSMDIConfigurationError.setObjects(
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
    bwSMDIConfigurationError.setStatus(
        "current"
    )

bwSMDIOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3576)
)
bwSMDIOperationFailure.setObjects(
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
    bwSMDIOperationFailure.setStatus(
        "current"
    )

bwSMDIRouteExhaustion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3577)
)
bwSMDIRouteExhaustion.setObjects(
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
    bwSMDIRouteExhaustion.setStatus(
        "current"
    )

bwICBridgeCommunicationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3578)
)
bwICBridgeCommunicationError.setObjects(
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
    bwICBridgeCommunicationError.setStatus(
        "current"
    )

bwICBridgeResetError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3579)
)
bwICBridgeResetError.setObjects(
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
    bwICBridgeResetError.setStatus(
        "current"
    )

bwIcPublicClusterFqdnNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3580)
)
bwIcPublicClusterFqdnNotConfigured.setObjects(
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
    bwIcPublicClusterFqdnNotConfigured.setStatus(
        "obsolete"
    )

bwLicenseFileExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3581)
)
bwLicenseFileExpiring.setObjects(
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
    bwLicenseFileExpiring.setStatus(
        "current"
    )

bwLicenseFileExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3582)
)
bwLicenseFileExpired.setObjects(
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
    bwLicenseFileExpired.setStatus(
        "current"
    )

bwExternalAuthenticationUnknownUser = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3583)
)
bwExternalAuthenticationUnknownUser.setObjects(
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
    bwExternalAuthenticationUnknownUser.setStatus(
        "current"
    )

bwSrvcPackMigrationTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3584)
)
bwSrvcPackMigrationTerminated.setObjects(
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
    bwSrvcPackMigrationTerminated.setStatus(
        "current"
    )

bwSrvcPackMigrationCompletedWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3585)
)
bwSrvcPackMigrationCompletedWithErrors.setObjects(
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
    bwSrvcPackMigrationCompletedWithErrors.setStatus(
        "current"
    )

bwSrvcPackMigrationStoppedDueToErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3586)
)
bwSrvcPackMigrationStoppedDueToErrors.setObjects(
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
    bwSrvcPackMigrationStoppedDueToErrors.setStatus(
        "current"
    )

bwSrvcPackMigrationStoppedDueToTimeLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3587)
)
bwSrvcPackMigrationStoppedDueToTimeLimit.setObjects(
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
    bwSrvcPackMigrationStoppedDueToTimeLimit.setStatus(
        "current"
    )

bwSrvcPackMigrationStoppedBySysShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3588)
)
bwSrvcPackMigrationStoppedBySysShutdown.setObjects(
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
    bwSrvcPackMigrationStoppedBySysShutdown.setStatus(
        "current"
    )

bwSrvcPackMigrationFoundUnfinishedTask = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3589)
)
bwSrvcPackMigrationFoundUnfinishedTask.setObjects(
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
    bwSrvcPackMigrationFoundUnfinishedTask.setStatus(
        "current"
    )

bwSrvcPackMigrationLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3590)
)
bwSrvcPackMigrationLicenseViolation.setObjects(
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
    bwSrvcPackMigrationLicenseViolation.setStatus(
        "current"
    )

bwSrvcPackMigrationSpSrvcQuantityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3591)
)
bwSrvcPackMigrationSpSrvcQuantityViolation.setObjects(
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
    bwSrvcPackMigrationSpSrvcQuantityViolation.setStatus(
        "current"
    )

bwSrvcPackMigrationSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3592)
)
bwSrvcPackMigrationSystemError.setObjects(
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
    bwSrvcPackMigrationSystemError.setStatus(
        "current"
    )

bwOverloadZoneTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3593)
)
bwOverloadZoneTransition.setObjects(
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
    bwOverloadZoneTransition.setStatus(
        "current"
    )

bwThreadDelayDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3594)
)
bwThreadDelayDetected.setObjects(
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
    bwThreadDelayDetected.setStatus(
        "current"
    )

bwSipTcpConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3595)
)
bwSipTcpConnectionFailure.setObjects(
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
    bwSipTcpConnectionFailure.setStatus(
        "current"
    )

bwAccountingRadiusServerNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3596)
)
bwAccountingRadiusServerNotResponding.setObjects(
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
    bwAccountingRadiusServerNotResponding.setStatus(
        "current"
    )

bwAccountingRadiusServersNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3597)
)
bwAccountingRadiusServersNotConfigured.setObjects(
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
    bwAccountingRadiusServersNotConfigured.setStatus(
        "current"
    )

bwMaximumFailedVoicePortalLoginAttempts = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3598)
)
bwMaximumFailedVoicePortalLoginAttempts.setObjects(
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
    bwMaximumFailedVoicePortalLoginAttempts.setStatus(
        "current"
    )

bwASRDatabaseOutOfSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3599)
)
bwASRDatabaseOutOfSync.setObjects(
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
    bwASRDatabaseOutOfSync.setStatus(
        "current"
    )

bwCallLogSOAPServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3600)
)
bwCallLogSOAPServerUnreachable.setObjects(
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
    bwCallLogSOAPServerUnreachable.setStatus(
        "current"
    )

bwCallLogRadiusServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3601)
)
bwCallLogRadiusServerUnreachable.setObjects(
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
    bwCallLogRadiusServerUnreachable.setStatus(
        "current"
    )

bwCallLogRadiusServersNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3602)
)
bwCallLogRadiusServersNotConfigured.setObjects(
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
    bwCallLogRadiusServersNotConfigured.setStatus(
        "current"
    )

bwCPEDeviceConfigurationInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3603)
)
bwCPEDeviceConfigurationInfo.setObjects(
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
    bwCPEDeviceConfigurationInfo.setStatus(
        "current"
    )

bwUserExceededMaxSimultaneousCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3604)
)
bwUserExceededMaxSimultaneousCalls.setObjects(
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
    bwUserExceededMaxSimultaneousCalls.setStatus(
        "current"
    )

bwUserExceededMaxCallTime = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3605)
)
bwUserExceededMaxCallTime.setObjects(
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
    bwUserExceededMaxCallTime.setStatus(
        "current"
    )

bwInvalidRingbackMediaFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3606)
)
bwInvalidRingbackMediaFile.setObjects(
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
    bwInvalidRingbackMediaFile.setStatus(
        "current"
    )

bwOciReportingAclViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3607)
)
bwOciReportingAclViolation.setObjects(
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
    bwOciReportingAclViolation.setStatus(
        "current"
    )

bwOciReportingConnectionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3608)
)
bwOciReportingConnectionError.setObjects(
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
    bwOciReportingConnectionError.setStatus(
        "current"
    )

bwPhysicalLocationOriginationBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3609)
)
bwPhysicalLocationOriginationBlocked.setObjects(
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
    bwPhysicalLocationOriginationBlocked.setStatus(
        "current"
    )

bwCallLogRadiusQueueNotProgressing = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3610)
)
bwCallLogRadiusQueueNotProgressing.setObjects(
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
    bwCallLogRadiusQueueNotProgressing.setStatus(
        "current"
    )

bwCallLogRadiusQueueFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3611)
)
bwCallLogRadiusQueueFileDeleted.setObjects(
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
    bwCallLogRadiusQueueFileDeleted.setStatus(
        "current"
    )

bwConcurrentCallsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3612)
)
bwConcurrentCallsExceeded.setObjects(
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
    bwConcurrentCallsExceeded.setStatus(
        "current"
    )

bwENServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3613)
)
bwENServerUnreachable.setObjects(
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
    bwENServerUnreachable.setStatus(
        "current"
    )

bwENServerNumberInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3614)
)
bwENServerNumberInvalid.setObjects(
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
    bwENServerNumberInvalid.setStatus(
        "current"
    )

bwOciReportingBackLogFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3615)
)
bwOciReportingBackLogFileDeleted.setObjects(
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
    bwOciReportingBackLogFileDeleted.setStatus(
        "current"
    )

bwProvisioningValidationConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3616)
)
bwProvisioningValidationConnectionFailure.setObjects(
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
    bwProvisioningValidationConnectionFailure.setStatus(
        "current"
    )

bwXSOCICommunicationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3617)
)
bwXSOCICommunicationError.setObjects(
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
    bwXSOCICommunicationError.setStatus(
        "current"
    )

bwCallOverloadZoneTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3618)
)
bwCallOverloadZoneTransition.setObjects(
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
    bwCallOverloadZoneTransition.setStatus(
        "current"
    )

bwNonCallOverloadZoneTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3619)
)
bwNonCallOverloadZoneTransition.setObjects(
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
    bwNonCallOverloadZoneTransition.setStatus(
        "current"
    )

bwUserExceededMaxSimultaneousVideoCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3620)
)
bwUserExceededMaxSimultaneousVideoCalls.setObjects(
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
    bwUserExceededMaxSimultaneousVideoCalls.setStatus(
        "current"
    )

bwMediaTypeNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3621)
)
bwMediaTypeNotSupported.setObjects(
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
    bwMediaTypeNotSupported.setStatus(
        "current"
    )

bwENTranslationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3622)
)
bwENTranslationFailed.setObjects(
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
    bwENTranslationFailed.setStatus(
        "current"
    )

bwSOAPThreadNumberTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3623)
)
bwSOAPThreadNumberTooLow.setObjects(
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
    bwSOAPThreadNumberTooLow.setStatus(
        "current"
    )

bwUserExceededMaxConcurrentRedirectedCalls = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3624)
)
bwUserExceededMaxConcurrentRedirectedCalls.setObjects(
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
    bwUserExceededMaxConcurrentRedirectedCalls.setStatus(
        "current"
    )

bwUserExceededMaxFindMeFollowMeDepth = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3625)
)
bwUserExceededMaxFindMeFollowMeDepth.setObjects(
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
    bwUserExceededMaxFindMeFollowMeDepth.setStatus(
        "current"
    )

bwUserExceededMaxRedirectionDepth = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3626)
)
bwUserExceededMaxRedirectionDepth.setObjects(
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
    bwUserExceededMaxRedirectionDepth.setStatus(
        "current"
    )

bwUserExceededMaxFindMeFollowMeInvocations = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3627)
)
bwUserExceededMaxFindMeFollowMeInvocations.setObjects(
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
    bwUserExceededMaxFindMeFollowMeInvocations.setStatus(
        "current"
    )

bwTrunkGroupCapacityExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3628)
)
bwTrunkGroupCapacityExceeded.setObjects(
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
    bwTrunkGroupCapacityExceeded.setStatus(
        "current"
    )

bwTrunkGroupUnreachableDestination = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3629)
)
bwTrunkGroupUnreachableDestination.setObjects(
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
    bwTrunkGroupUnreachableDestination.setStatus(
        "current"
    )

bwForwardDestinationLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3630)
)
bwForwardDestinationLoop.setObjects(
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
    bwForwardDestinationLoop.setStatus(
        "current"
    )

bwSmppConnectionLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3631)
)
bwSmppConnectionLost.setObjects(
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
    bwSmppConnectionLost.setStatus(
        "current"
    )

bwSmppConnectionAttemptFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3632)
)
bwSmppConnectionAttemptFailure.setObjects(
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
    bwSmppConnectionAttemptFailure.setStatus(
        "current"
    )

bwSmppRoutesExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3633)
)
bwSmppRoutesExhausted.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "alarmState"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwSmppRoutesExhausted.setStatus(
        "current"
    )

bwExternalCustomRingbackServerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3634)
)
bwExternalCustomRingbackServerFailure.setObjects(
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
    bwExternalCustomRingbackServerFailure.setStatus(
        "current"
    )

bwCongestionManagementNeighborOverloaded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3635)
)
bwCongestionManagementNeighborOverloaded.setObjects(
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
    bwCongestionManagementNeighborOverloaded.setStatus(
        "current"
    )

bwCongestionManagementNeighborsInhibited = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3636)
)
bwCongestionManagementNeighborsInhibited.setObjects(
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
    bwCongestionManagementNeighborsInhibited.setStatus(
        "current"
    )

bwMobilityManagerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3637)
)
bwMobilityManagerUnreachable.setObjects(
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
    bwMobilityManagerUnreachable.setStatus(
        "current"
    )

bwMobilityManagerError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3638)
)
bwMobilityManagerError.setObjects(
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
    bwMobilityManagerError.setStatus(
        "current"
    )

bwShNoAvailableHosts = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3639)
)
bwShNoAvailableHosts.setObjects(
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
    bwShNoAvailableHosts.setStatus(
        "current"
    )

bwShUserUnknownInHSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3640)
)
bwShUserUnknownInHSS.setObjects(
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
    bwShUserUnknownInHSS.setStatus(
        "current"
    )

bwShUserUnknownInAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3641)
)
bwShUserUnknownInAS.setObjects(
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
    bwShUserUnknownInAS.setStatus(
        "current"
    )

bwShGeneralErrorReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3642)
)
bwShGeneralErrorReceived.setObjects(
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
    bwShGeneralErrorReceived.setStatus(
        "current"
    )

bwShSystemRefreshInitiated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3643)
)
bwShSystemRefreshInitiated.setObjects(
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
    bwShSystemRefreshInitiated.setStatus(
        "current"
    )

bwShSystemRefreshTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3644)
)
bwShSystemRefreshTerminated.setObjects(
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
    bwShSystemRefreshTerminated.setStatus(
        "current"
    )

bwDnsServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3645)
)
bwDnsServerUnreachable.setObjects(
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
    bwDnsServerUnreachable.setStatus(
        "current"
    )

bwDnsAllServersUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3646)
)
bwDnsAllServersUnreachable.setObjects(
      *(("BroadworksFault", "identifier"),
        ("BroadworksFault", "timeStamp"),
        ("BroadworksFault", "alarmName"),
        ("BroadworksFault", "systemName"),
        ("BroadworksFault", "alarmState"),
        ("BroadworksFault", "severity"),
        ("BroadworksFault", "component"),
        ("BroadworksFault", "subcomponent"),
        ("BroadworksFault", "problemText"),
        ("BroadworksFault", "recommendedActionsText"))
)
if mibBuilder.loadTexts:
    bwDnsAllServersUnreachable.setStatus(
        "current"
    )

bwRemoteOfficeEmergencyCallBlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3647)
)
bwRemoteOfficeEmergencyCallBlocked.setObjects(
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
    bwRemoteOfficeEmergencyCallBlocked.setStatus(
        "current"
    )

bwEmergencyCallOriginated = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3648)
)
bwEmergencyCallOriginated.setObjects(
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
    bwEmergencyCallOriginated.setStatus(
        "current"
    )

bwShInterfaceInitializationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3649)
)
bwShInterfaceInitializationError.setObjects(
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
    bwShInterfaceInitializationError.setStatus(
        "current"
    )

bwCPEDeviceConfigurationNumFilesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3654)
)
bwCPEDeviceConfigurationNumFilesExceeded.setObjects(
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
    bwCPEDeviceConfigurationNumFilesExceeded.setStatus(
        "current"
    )

bwCallCenterConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3661)
)
bwCallCenterConnectionFailure.setObjects(
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
    bwCallCenterConnectionFailure.setStatus(
        "current"
    )

bwTrunkingLicensedCapacityExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 3662)
)
bwTrunkingLicensedCapacityExceeded.setObjects(
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
    bwTrunkingLicensedCapacityExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-ApplicationServerFault",
    **{"systemFaults": systemFaults,
       "bwApplicationServerUnreachable": bwApplicationServerUnreachable,
       "bwNetworkServerUnreachable": bwNetworkServerUnreachable,
       "bwNetworkServerRequestError": bwNetworkServerRequestError,
       "bwCMSConnectivityDown": bwCMSConnectivityDown,
       "bwCMSConnectivityUp": bwCMSConnectivityUp,
       "bwCMSDatabaseMismatch": bwCMSDatabaseMismatch,
       "bwPMExecutionServerLaunched": bwPMExecutionServerLaunched,
       "bwPMExecutionServerShutDown": bwPMExecutionServerShutDown,
       "bwPMExecutionServerRestarted": bwPMExecutionServerRestarted,
       "bwPMExecutionServerDeath": bwPMExecutionServerDeath,
       "bwPMProvisioningServerLaunched": bwPMProvisioningServerLaunched,
       "bwPMProvisioningServerShutDown": bwPMProvisioningServerShutDown,
       "bwPMProvisioningServerRestarted": bwPMProvisioningServerRestarted,
       "bwPMProvisioningServerDeath": bwPMProvisioningServerDeath,
       "bwSipMessageParsingError": bwSipMessageParsingError,
       "bwSipRegistrationFailure": bwSipRegistrationFailure,
       "bwSipUnexpectedMessage": bwSipUnexpectedMessage,
       "bwSipMaxRetriesExceeded": bwSipMaxRetriesExceeded,
       "bwSipRequestTimeOutReceived": bwSipRequestTimeOutReceived,
       "bwSipServiceUnavailableReceived": bwSipServiceUnavailableReceived,
       "bwSipServerTimeOutReceived": bwSipServerTimeOutReceived,
       "bwSipAuthenticationFailure": bwSipAuthenticationFailure,
       "bwAclViolation": bwAclViolation,
       "bwSipUnrecognisedDomainName": bwSipUnrecognisedDomainName,
       "bwSMTPPrimaryServerEmailMessageDeliveryError": bwSMTPPrimaryServerEmailMessageDeliveryError,
       "bwSMTPConnectivityFailure": bwSMTPConnectivityFailure,
       "bwIMSRetrieveMessageError": bwIMSRetrieveMessageError,
       "bwIMSRetrieveMailBoxInfoError": bwIMSRetrieveMailBoxInfoError,
       "bwIMSConnectionFailure": bwIMSConnectionFailure,
       "bwIMSCloseConnectionError": bwIMSCloseConnectionError,
       "bwIMSUpdateMailBoxError": bwIMSUpdateMailBoxError,
       "bwMediaServerNotResponding": bwMediaServerNotResponding,
       "bwMssNetworkServerNotResponding": bwMssNetworkServerNotResponding,
       "bwMssNoResponse": bwMssNoResponse,
       "bwMGCPIOControllerUnknownReqIDInNotification": bwMGCPIOControllerUnknownReqIDInNotification,
       "bwMGCPMessageParsingError": bwMGCPMessageParsingError,
       "bwMGCPCallAgentFailedMessageProcessing": bwMGCPCallAgentFailedMessageProcessing,
       "bwMGCPCallAgentMessageProcessing": bwMGCPCallAgentMessageProcessing,
       "bwMGCPReTransmissionTimeout": bwMGCPReTransmissionTimeout,
       "bwMGCPUnrecognisedDomainName": bwMGCPUnrecognisedDomainName,
       "bwMGCPUDPTransmitter": bwMGCPUDPTransmitter,
       "bwAuditAbnormalCallTermination": bwAuditAbnormalCallTermination,
       "bwNSSynchronizationConnectivityFailure": bwNSSynchronizationConnectivityFailure,
       "bwNSSynchronizationFailure": bwNSSynchronizationFailure,
       "bwNSLocationConnectivityFailure": bwNSLocationConnectivityFailure,
       "bwNSLocationFailure": bwNSLocationFailure,
       "bwLicenseAuthenticationFailure": bwLicenseAuthenticationFailure,
       "bwLicenseAccntViolation": bwLicenseAccntViolation,
       "bwLicenseUserServiceAccntViolation": bwLicenseUserServiceAccntViolation,
       "bwAddUserEvent": bwAddUserEvent,
       "bwDeleteUserEvent": bwDeleteUserEvent,
       "bwAddGroupEvent": bwAddGroupEvent,
       "bwDeleteGroupEvent": bwDeleteGroupEvent,
       "bwUserAddressChangeEvent": bwUserAddressChangeEvent,
       "bwGroupAddressChangeEvent": bwGroupAddressChangeEvent,
       "bwEmergencyCallRoutingFailure": bwEmergencyCallRoutingFailure,
       "bwNetworkRoutingServiceRouteExhaustion": bwNetworkRoutingServiceRouteExhaustion,
       "bwCallPThreadAutoRestart": bwCallPThreadAutoRestart,
       "bwForcedExitDueToHungThread": bwForcedExitDueToHungThread,
       "bwOCPMissingCountryCode": bwOCPMissingCountryCode,
       "bwSystemDomainNameReset": bwSystemDomainNameReset,
       "bwAccountingFTPConnectionError": bwAccountingFTPConnectionError,
       "bwCustomerOriginatedTrace": bwCustomerOriginatedTrace,
       "bwMaliciousCallTrace": bwMaliciousCallTrace,
       "bwLDAPConnectionError": bwLDAPConnectionError,
       "bwLDAPConfigurationError": bwLDAPConfigurationError,
       "bwCallCapacityManagementaddCallID": bwCallCapacityManagementaddCallID,
       "bwSMDIsessionRejected": bwSMDIsessionRejected,
       "bwOCPMissingTransferNumber": bwOCPMissingTransferNumber,
       "bwOCPMissingAuthorizationCode": bwOCPMissingAuthorizationCode,
       "bwDeviceStatusIsOnline": bwDeviceStatusIsOnline,
       "bwDeviceStatusIsUnavailable": bwDeviceStatusIsUnavailable,
       "bwCPEDeviceConfigurationFileNotTransmitted": bwCPEDeviceConfigurationFileNotTransmitted,
       "bwCPEDeviceConfigurationDeviceReset": bwCPEDeviceConfigurationDeviceReset,
       "bwCPEDeviceConfigurationFTPLogin": bwCPEDeviceConfigurationFTPLogin,
       "bwSMDIInterfaceError": bwSMDIInterfaceError,
       "bwSMDIConfigurationError": bwSMDIConfigurationError,
       "bwSMDIOperationFailure": bwSMDIOperationFailure,
       "bwSMDIRouteExhaustion": bwSMDIRouteExhaustion,
       "bwICBridgeCommunicationError": bwICBridgeCommunicationError,
       "bwICBridgeResetError": bwICBridgeResetError,
       "bwIcPublicClusterFqdnNotConfigured": bwIcPublicClusterFqdnNotConfigured,
       "bwLicenseFileExpiring": bwLicenseFileExpiring,
       "bwLicenseFileExpired": bwLicenseFileExpired,
       "bwExternalAuthenticationUnknownUser": bwExternalAuthenticationUnknownUser,
       "bwSrvcPackMigrationTerminated": bwSrvcPackMigrationTerminated,
       "bwSrvcPackMigrationCompletedWithErrors": bwSrvcPackMigrationCompletedWithErrors,
       "bwSrvcPackMigrationStoppedDueToErrors": bwSrvcPackMigrationStoppedDueToErrors,
       "bwSrvcPackMigrationStoppedDueToTimeLimit": bwSrvcPackMigrationStoppedDueToTimeLimit,
       "bwSrvcPackMigrationStoppedBySysShutdown": bwSrvcPackMigrationStoppedBySysShutdown,
       "bwSrvcPackMigrationFoundUnfinishedTask": bwSrvcPackMigrationFoundUnfinishedTask,
       "bwSrvcPackMigrationLicenseViolation": bwSrvcPackMigrationLicenseViolation,
       "bwSrvcPackMigrationSpSrvcQuantityViolation": bwSrvcPackMigrationSpSrvcQuantityViolation,
       "bwSrvcPackMigrationSystemError": bwSrvcPackMigrationSystemError,
       "bwOverloadZoneTransition": bwOverloadZoneTransition,
       "bwThreadDelayDetected": bwThreadDelayDetected,
       "bwSipTcpConnectionFailure": bwSipTcpConnectionFailure,
       "bwAccountingRadiusServerNotResponding": bwAccountingRadiusServerNotResponding,
       "bwAccountingRadiusServersNotConfigured": bwAccountingRadiusServersNotConfigured,
       "bwMaximumFailedVoicePortalLoginAttempts": bwMaximumFailedVoicePortalLoginAttempts,
       "bwASRDatabaseOutOfSync": bwASRDatabaseOutOfSync,
       "bwCallLogSOAPServerUnreachable": bwCallLogSOAPServerUnreachable,
       "bwCallLogRadiusServerUnreachable": bwCallLogRadiusServerUnreachable,
       "bwCallLogRadiusServersNotConfigured": bwCallLogRadiusServersNotConfigured,
       "bwCPEDeviceConfigurationInfo": bwCPEDeviceConfigurationInfo,
       "bwUserExceededMaxSimultaneousCalls": bwUserExceededMaxSimultaneousCalls,
       "bwUserExceededMaxCallTime": bwUserExceededMaxCallTime,
       "bwInvalidRingbackMediaFile": bwInvalidRingbackMediaFile,
       "bwOciReportingAclViolation": bwOciReportingAclViolation,
       "bwOciReportingConnectionError": bwOciReportingConnectionError,
       "bwPhysicalLocationOriginationBlocked": bwPhysicalLocationOriginationBlocked,
       "bwCallLogRadiusQueueNotProgressing": bwCallLogRadiusQueueNotProgressing,
       "bwCallLogRadiusQueueFileDeleted": bwCallLogRadiusQueueFileDeleted,
       "bwConcurrentCallsExceeded": bwConcurrentCallsExceeded,
       "bwENServerUnreachable": bwENServerUnreachable,
       "bwENServerNumberInvalid": bwENServerNumberInvalid,
       "bwOciReportingBackLogFileDeleted": bwOciReportingBackLogFileDeleted,
       "bwProvisioningValidationConnectionFailure": bwProvisioningValidationConnectionFailure,
       "bwXSOCICommunicationError": bwXSOCICommunicationError,
       "bwCallOverloadZoneTransition": bwCallOverloadZoneTransition,
       "bwNonCallOverloadZoneTransition": bwNonCallOverloadZoneTransition,
       "bwUserExceededMaxSimultaneousVideoCalls": bwUserExceededMaxSimultaneousVideoCalls,
       "bwMediaTypeNotSupported": bwMediaTypeNotSupported,
       "bwENTranslationFailed": bwENTranslationFailed,
       "bwSOAPThreadNumberTooLow": bwSOAPThreadNumberTooLow,
       "bwUserExceededMaxConcurrentRedirectedCalls": bwUserExceededMaxConcurrentRedirectedCalls,
       "bwUserExceededMaxFindMeFollowMeDepth": bwUserExceededMaxFindMeFollowMeDepth,
       "bwUserExceededMaxRedirectionDepth": bwUserExceededMaxRedirectionDepth,
       "bwUserExceededMaxFindMeFollowMeInvocations": bwUserExceededMaxFindMeFollowMeInvocations,
       "bwTrunkGroupCapacityExceeded": bwTrunkGroupCapacityExceeded,
       "bwTrunkGroupUnreachableDestination": bwTrunkGroupUnreachableDestination,
       "bwForwardDestinationLoop": bwForwardDestinationLoop,
       "bwSmppConnectionLost": bwSmppConnectionLost,
       "bwSmppConnectionAttemptFailure": bwSmppConnectionAttemptFailure,
       "bwSmppRoutesExhausted": bwSmppRoutesExhausted,
       "bwExternalCustomRingbackServerFailure": bwExternalCustomRingbackServerFailure,
       "bwCongestionManagementNeighborOverloaded": bwCongestionManagementNeighborOverloaded,
       "bwCongestionManagementNeighborsInhibited": bwCongestionManagementNeighborsInhibited,
       "bwMobilityManagerUnreachable": bwMobilityManagerUnreachable,
       "bwMobilityManagerError": bwMobilityManagerError,
       "bwShNoAvailableHosts": bwShNoAvailableHosts,
       "bwShUserUnknownInHSS": bwShUserUnknownInHSS,
       "bwShUserUnknownInAS": bwShUserUnknownInAS,
       "bwShGeneralErrorReceived": bwShGeneralErrorReceived,
       "bwShSystemRefreshInitiated": bwShSystemRefreshInitiated,
       "bwShSystemRefreshTerminated": bwShSystemRefreshTerminated,
       "bwDnsServerUnreachable": bwDnsServerUnreachable,
       "bwDnsAllServersUnreachable": bwDnsAllServersUnreachable,
       "bwRemoteOfficeEmergencyCallBlocked": bwRemoteOfficeEmergencyCallBlocked,
       "bwEmergencyCallOriginated": bwEmergencyCallOriginated,
       "bwShInterfaceInitializationError": bwShInterfaceInitializationError,
       "bwCPEDeviceConfigurationNumFilesExceeded": bwCPEDeviceConfigurationNumFilesExceeded,
       "bwCallCenterConnectionFailure": bwCallCenterConnectionFailure,
       "bwTrunkingLicensedCapacityExceeded": bwTrunkingLicensedCapacityExceeded}
)
