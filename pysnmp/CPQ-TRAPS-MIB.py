# SNMP MIB module (CPQ-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQ-TRAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:13 2024
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

(agentBscSwFile,
 agentBscSwFileAddr,
 agentBscSwFileLoadType,
 agentBscSwFileStatus,
 agentSNTPServer1IPAddr,
 agentSNTPServer2IPAddr,
 agentSwitchCubeSpareName,
 agentSwitchCubeSparePartNumber,
 agentSwitchCubeType,
 agentSwitchFanCondition,
 agentSwitchFanIndex,
 agentSwitchPowerSupplyCondition,
 agentSwitchPowerSupplyCurPwrOutput,
 agentSwitchPowerSupplyExhaustTemp,
 agentSwitchPowerSupplyInputLineStatus,
 agentSwitchPowerSupplyIntakeTemp,
 agentSwitchPowerSupplyMaxPwrOutput,
 agentSwitchPowerSupplyStatus,
 agentSwitchTempSensorCondition,
 agentSwitchTempSensorCurrent,
 agentSwitchTempSensorIndex,
 agentSwitchTempSensorTempType,
 agentSwitchTempSensorThreshold) = mibBuilder.importSymbols(
    "COMPAQ-AGENT-MIB",
    "agentBscSwFile",
    "agentBscSwFileAddr",
    "agentBscSwFileLoadType",
    "agentBscSwFileStatus",
    "agentSNTPServer1IPAddr",
    "agentSNTPServer2IPAddr",
    "agentSwitchCubeSpareName",
    "agentSwitchCubeSparePartNumber",
    "agentSwitchCubeType",
    "agentSwitchFanCondition",
    "agentSwitchFanIndex",
    "agentSwitchPowerSupplyCondition",
    "agentSwitchPowerSupplyCurPwrOutput",
    "agentSwitchPowerSupplyExhaustTemp",
    "agentSwitchPowerSupplyInputLineStatus",
    "agentSwitchPowerSupplyIntakeTemp",
    "agentSwitchPowerSupplyMaxPwrOutput",
    "agentSwitchPowerSupplyStatus",
    "agentSwitchTempSensorCondition",
    "agentSwitchTempSensorCurrent",
    "agentSwitchTempSensorIndex",
    "agentSwitchTempSensorTempType",
    "agentSwitchTempSensorThreshold")

(compaq_common_mgmt,) = mibBuilder.importSymbols(
    "COMPAQ-ID-REC-MIB",
    "compaq-common-mgmt")

(compaq,) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq")

(cpqRackCommonEnclosureName,
 cpqRackCommonEnclosureSerialNum,
 cpqRackName,
 cpqRackNetConnectorFWRev,
 cpqRackNetConnectorLocation,
 cpqRackNetConnectorName,
 cpqRackNetConnectorSerialNum,
 cpqRackNetConnectorSparePartNumber,
 cpqRackUid) = mibBuilder.importSymbols(
    "CPQRACK-MIB",
    "cpqRackCommonEnclosureName",
    "cpqRackCommonEnclosureSerialNum",
    "cpqRackName",
    "cpqRackNetConnectorFWRev",
    "cpqRackNetConnectorLocation",
    "cpqRackNetConnectorName",
    "cpqRackNetConnectorSerialNum",
    "cpqRackNetConnectorSparePartNumber",
    "cpqRackUid")

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
 enterprises,
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EntityMIB_ObjectIdentity = ObjectIdentity
entityMIB = _EntityMIB_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 47)
)
_EntityMIBTraps_ObjectIdentity = ObjectIdentity
entityMIBTraps = _EntityMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 47, 2)
)
_EntityMIBTrapPrefix_ObjectIdentity = ObjectIdentity
entityMIBTrapPrefix = _EntityMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 47, 2, 0)
)

# Managed Objects groups


# Notification objects

entConfigChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 47, 2, 0, 0, 1)
)
if mibBuilder.loadTexts:
    entConfigChange.setStatus(
        ""
    )

switchFirmwareTransferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161001)
)
switchFirmwareTransferred.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileAddr"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFile"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileLoadType"),
        ("CPQRACK-MIB", "cpqRackNetConnectorFWRev"))
)
if mibBuilder.loadTexts:
    switchFirmwareTransferred.setStatus(
        ""
    )

switchConfigFileTransferred = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161002)
)
switchConfigFileTransferred.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileAddr"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFile"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileLoadType"))
)
if mibBuilder.loadTexts:
    switchConfigFileTransferred.setStatus(
        ""
    )

switchTFTPTransferSucceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161003)
)
switchTFTPTransferSucceeded.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileAddr"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFile"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileLoadType"))
)
if mibBuilder.loadTexts:
    switchTFTPTransferSucceeded.setStatus(
        ""
    )

switchTFTPTransferFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161004)
)
switchTFTPTransferFailed.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileAddr"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFile"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileLoadType"))
)
if mibBuilder.loadTexts:
    switchTFTPTransferFailed.setStatus(
        ""
    )

switchFileInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161005)
)
switchFileInvalid.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileAddr"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFile"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileLoadType"),
        ("COMPAQ-AGENT-MIB", "agentBscSwFileStatus"))
)
if mibBuilder.loadTexts:
    switchFileInvalid.setStatus(
        ""
    )

switchFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161006)
)
switchFanFailed.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchFanIndex"),
        ("COMPAQ-AGENT-MIB", "agentSwitchFanCondition"))
)
if mibBuilder.loadTexts:
    switchFanFailed.setStatus(
        ""
    )

switchFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161007)
)
switchFanOk.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchFanIndex"),
        ("COMPAQ-AGENT-MIB", "agentSwitchFanCondition"))
)
if mibBuilder.loadTexts:
    switchFanOk.setStatus(
        ""
    )

switchTempSensorDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161008)
)
switchTempSensorDegraded.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorIndex"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCurrent"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorThreshold"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCondition"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorTempType"))
)
if mibBuilder.loadTexts:
    switchTempSensorDegraded.setStatus(
        ""
    )

switchTempSensorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161009)
)
switchTempSensorFailed.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorIndex"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCurrent"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorThreshold"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCondition"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorTempType"))
)
if mibBuilder.loadTexts:
    switchTempSensorFailed.setStatus(
        ""
    )

switchTempSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161010)
)
switchTempSensorOk.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorIndex"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCurrent"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorThreshold"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorCondition"),
        ("COMPAQ-AGENT-MIB", "agentSwitchTempSensorTempType"))
)
if mibBuilder.loadTexts:
    switchTempSensorOk.setStatus(
        ""
    )

switchPostSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161011)
)
switchPostSuccess.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"))
)
if mibBuilder.loadTexts:
    switchPostSuccess.setStatus(
        ""
    )

switchLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161012)
)
switchLoginFailure.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"))
)
if mibBuilder.loadTexts:
    switchLoginFailure.setStatus(
        ""
    )

switchLocationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161013)
)
switchLocationChange.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"))
)
if mibBuilder.loadTexts:
    switchLocationChange.setStatus(
        ""
    )

switchCubeTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161014)
)
switchCubeTypeChange.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSparePartNumber"),
        ("COMPAQ-AGENT-MIB", "agentSwitchCubeType"),
        ("COMPAQ-AGENT-MIB", "agentSwitchCubeSpareName"),
        ("COMPAQ-AGENT-MIB", "agentSwitchCubeSparePartNumber"))
)
if mibBuilder.loadTexts:
    switchCubeTypeChange.setStatus(
        ""
    )

switchSNTPServiceUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 161015)
)
switchSNTPServiceUnavailable.setObjects(
      *(("CPQRACK-MIB", "cpqRackUid"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureSerialNum"),
        ("CPQRACK-MIB", "cpqRackNetConnectorSerialNum"),
        ("CPQRACK-MIB", "cpqRackName"),
        ("CPQRACK-MIB", "cpqRackCommonEnclosureName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorName"),
        ("CPQRACK-MIB", "cpqRackNetConnectorLocation"),
        ("COMPAQ-AGENT-MIB", "agentSNTPServer1IPAddr"),
        ("COMPAQ-AGENT-MIB", "agentSNTPServer2IPAddr"))
)
if mibBuilder.loadTexts:
    switchSNTPServiceUnavailable.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQ-TRAPS-MIB",
    **{"entityMIB": entityMIB,
       "entityMIBTraps": entityMIBTraps,
       "entityMIBTrapPrefix": entityMIBTrapPrefix,
       "entConfigChange": entConfigChange,
       "switchFirmwareTransferred": switchFirmwareTransferred,
       "switchConfigFileTransferred": switchConfigFileTransferred,
       "switchTFTPTransferSucceeded": switchTFTPTransferSucceeded,
       "switchTFTPTransferFailed": switchTFTPTransferFailed,
       "switchFileInvalid": switchFileInvalid,
       "switchFanFailed": switchFanFailed,
       "switchFanOk": switchFanOk,
       "switchTempSensorDegraded": switchTempSensorDegraded,
       "switchTempSensorFailed": switchTempSensorFailed,
       "switchTempSensorOk": switchTempSensorOk,
       "switchPostSuccess": switchPostSuccess,
       "switchLoginFailure": switchLoginFailure,
       "switchLocationChange": switchLocationChange,
       "switchCubeTypeChange": switchCubeTypeChange,
       "switchSNTPServiceUnavailable": switchSNTPServiceUnavailable}
)
