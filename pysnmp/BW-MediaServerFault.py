# SNMP MIB module (BW-MediaServerFault) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BW-MediaServerFault
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:07 2024
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

bwPMMediaServerLaunched = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1501)
)
bwPMMediaServerLaunched.setObjects(
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
    bwPMMediaServerLaunched.setStatus(
        "current"
    )

bwPMMediaServerShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1502)
)
bwPMMediaServerShutDown.setObjects(
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
    bwPMMediaServerShutDown.setStatus(
        "current"
    )

bwPMMediaServerRestarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1503)
)
bwPMMediaServerRestarted.setObjects(
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
    bwPMMediaServerRestarted.setStatus(
        "current"
    )

bwPMMediaServerDeath = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1504)
)
bwPMMediaServerDeath.setObjects(
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
    bwPMMediaServerDeath.setStatus(
        "current"
    )

msSoftwareError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1505)
)
msSoftwareError.setObjects(
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
    msSoftwareError.setStatus(
        "current"
    )

msMemAllocFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1506)
)
msMemAllocFailure.setObjects(
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
    msMemAllocFailure.setStatus(
        "current"
    )

msStaleSession = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1507)
)
msStaleSession.setObjects(
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
    msStaleSession.setStatus(
        "current"
    )

msInvalidAudioFile = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1509)
)
msInvalidAudioFile.setObjects(
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
    msInvalidAudioFile.setStatus(
        "current"
    )

msShutDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1510)
)
msShutDown.setObjects(
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
    msShutDown.setStatus(
        "current"
    )

msSmtpFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1511)
)
msSmtpFailure.setObjects(
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
    msSmtpFailure.setStatus(
        "current"
    )

msLicenseHWViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1512)
)
msLicenseHWViolation.setObjects(
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
    msLicenseHWViolation.setStatus(
        "current"
    )

msHTTPConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1513)
)
msHTTPConnectionFailure.setObjects(
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
    msHTTPConnectionFailure.setStatus(
        "current"
    )

msHTTPFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1515)
)
msHTTPFileNotFound.setObjects(
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
    msHTTPFileNotFound.setStatus(
        "current"
    )

msHTTPReceiveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1516)
)
msHTTPReceiveFailure.setObjects(
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
    msHTTPReceiveFailure.setStatus(
        "current"
    )

msRTPInterfaceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1517)
)
msRTPInterfaceFailure.setObjects(
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
    msRTPInterfaceFailure.setStatus(
        "current"
    )

msRTPInterfaceNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1518)
)
msRTPInterfaceNotFound.setObjects(
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
    msRTPInterfaceNotFound.setStatus(
        "current"
    )

msnddExecutionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1519)
)
msnddExecutionFailure.setObjects(
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
    msnddExecutionFailure.setStatus(
        "current"
    )

msLiveAudioHWFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1520)
)
msLiveAudioHWFailure.setObjects(
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
    msLiveAudioHWFailure.setStatus(
        "current"
    )

msLiveAudioLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1521)
)
msLiveAudioLicenseViolation.setObjects(
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
    msLiveAudioLicenseViolation.setStatus(
        "current"
    )

msNoPortsAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1522)
)
msNoPortsAvailable.setObjects(
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
    msNoPortsAvailable.setStatus(
        "current"
    )

msVXMLAppServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1523)
)
msVXMLAppServerUnreachable.setObjects(
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
    msVXMLAppServerUnreachable.setStatus(
        "current"
    )

msVxmlScriptError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1524)
)
msVxmlScriptError.setObjects(
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
    msVxmlScriptError.setStatus(
        "current"
    )

msVXMLSecurityThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1525)
)
msVXMLSecurityThresholdExceeded.setObjects(
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
    msVXMLSecurityThresholdExceeded.setStatus(
        "current"
    )

msMrcpConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1526)
)
msMrcpConnectionFailure.setObjects(
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
    msMrcpConnectionFailure.setStatus(
        "current"
    )

msMrcpKeepAliveFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1527)
)
msMrcpKeepAliveFailure.setObjects(
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
    msMrcpKeepAliveFailure.setStatus(
        "current"
    )

msRouteAdvance = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1528)
)
msRouteAdvance.setObjects(
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
    msRouteAdvance.setStatus(
        "current"
    )

msMrcpError = NotificationType(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 1, 1529)
)
msMrcpError.setObjects(
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
    msMrcpError.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BW-MediaServerFault",
    **{"systemFaults": systemFaults,
       "bwPMMediaServerLaunched": bwPMMediaServerLaunched,
       "bwPMMediaServerShutDown": bwPMMediaServerShutDown,
       "bwPMMediaServerRestarted": bwPMMediaServerRestarted,
       "bwPMMediaServerDeath": bwPMMediaServerDeath,
       "msSoftwareError": msSoftwareError,
       "msMemAllocFailure": msMemAllocFailure,
       "msStaleSession": msStaleSession,
       "msInvalidAudioFile": msInvalidAudioFile,
       "msShutDown": msShutDown,
       "msSmtpFailure": msSmtpFailure,
       "msLicenseHWViolation": msLicenseHWViolation,
       "msHTTPConnectionFailure": msHTTPConnectionFailure,
       "msHTTPFileNotFound": msHTTPFileNotFound,
       "msHTTPReceiveFailure": msHTTPReceiveFailure,
       "msRTPInterfaceFailure": msRTPInterfaceFailure,
       "msRTPInterfaceNotFound": msRTPInterfaceNotFound,
       "msnddExecutionFailure": msnddExecutionFailure,
       "msLiveAudioHWFailure": msLiveAudioHWFailure,
       "msLiveAudioLicenseViolation": msLiveAudioLicenseViolation,
       "msNoPortsAvailable": msNoPortsAvailable,
       "msVXMLAppServerUnreachable": msVXMLAppServerUnreachable,
       "msVxmlScriptError": msVxmlScriptError,
       "msVXMLSecurityThresholdExceeded": msVXMLSecurityThresholdExceeded,
       "msMrcpConnectionFailure": msMrcpConnectionFailure,
       "msMrcpKeepAliveFailure": msMrcpKeepAliveFailure,
       "msRouteAdvance": msRouteAdvance,
       "msMrcpError": msMrcpError}
)
