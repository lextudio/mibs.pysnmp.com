# SNMP MIB module (KENYA-COMPONENT-TRAPS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KENYA-COMPONENT-TRAPS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:39 2024
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

(nmSoftwares,
 pxSoftwares,
 scSoftwares) = mibBuilder.importSymbols(
    "KENYA-COMPONENT-MIB",
    "nmSoftwares",
    "pxSoftwares",
    "scSoftwares")

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

(vlbComponents,
 volubill) = mibBuilder.importSymbols(
    "VOLUBILL-ROOT-MIB",
    "vlbComponents",
    "volubill")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmDataCollector_ObjectIdentity = ObjectIdentity
nmDataCollector = _NmDataCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1)
)
_DcCheckedOid_Type = OctetString
_DcCheckedOid_Object = MibScalar
dcCheckedOid = _DcCheckedOid_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 1),
    _DcCheckedOid_Type()
)
dcCheckedOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcCheckedOid.setStatus("mandatory")


class _DcErrorString_Type(OctetString):
    """Custom type dcErrorString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_DcErrorString_Type.__name__ = "OctetString"
_DcErrorString_Object = MibScalar
dcErrorString = _DcErrorString_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 2),
    _DcErrorString_Type()
)
dcErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcErrorString.setStatus("mandatory")
_DcTestDescr_Type = OctetString
_DcTestDescr_Object = MibScalar
dcTestDescr = _DcTestDescr_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 3),
    _DcTestDescr_Type()
)
dcTestDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcTestDescr.setStatus("mandatory")
_DcNbRepeat_Type = Integer32
_DcNbRepeat_Object = MibScalar
dcNbRepeat = _DcNbRepeat_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 4),
    _DcNbRepeat_Type()
)
dcNbRepeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcNbRepeat.setStatus("mandatory")
_DcSystemRequirement_Type = OctetString
_DcSystemRequirement_Object = MibScalar
dcSystemRequirement = _DcSystemRequirement_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 5),
    _DcSystemRequirement_Type()
)
dcSystemRequirement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemRequirement.setStatus("mandatory")
_DcSystemErrorDate_Type = OctetString
_DcSystemErrorDate_Object = MibScalar
dcSystemErrorDate = _DcSystemErrorDate_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 1, 6),
    _DcSystemErrorDate_Type()
)
dcSystemErrorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcSystemErrorDate.setStatus("mandatory")
_ProcRespawner_ObjectIdentity = ObjectIdentity
procRespawner = _ProcRespawner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 2)
)


class _PrMissingProcName_Type(OctetString):
    """Custom type prMissingProcName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_PrMissingProcName_Type.__name__ = "OctetString"
_PrMissingProcName_Object = MibScalar
prMissingProcName = _PrMissingProcName_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 2, 1),
    _PrMissingProcName_Type()
)
prMissingProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prMissingProcName.setStatus("mandatory")
_PrRespawnCommand_Type = OctetString
_PrRespawnCommand_Object = MibScalar
prRespawnCommand = _PrRespawnCommand_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 2, 2),
    _PrRespawnCommand_Type()
)
prRespawnCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prRespawnCommand.setStatus("mandatory")
_NmsGolbalStatusProcessor_ObjectIdentity = ObjectIdentity
nmsGolbalStatusProcessor = _NmsGolbalStatusProcessor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 3)
)
_SnmpFailedComponent_Type = OctetString
_SnmpFailedComponent_Object = MibScalar
snmpFailedComponent = _SnmpFailedComponent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 3, 1),
    _SnmpFailedComponent_Type()
)
snmpFailedComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpFailedComponent.setStatus("mandatory")
_SnmpRequestedOid_Type = OctetString
_SnmpRequestedOid_Object = MibScalar
snmpRequestedOid = _SnmpRequestedOid_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 3, 2),
    _SnmpRequestedOid_Type()
)
snmpRequestedOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRequestedOid.setStatus("mandatory")
_ComponentTrapSender_ObjectIdentity = ObjectIdentity
componentTrapSender = _ComponentTrapSender_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 4)
)
_SourceComponent_Type = OctetString
_SourceComponent_Object = MibScalar
sourceComponent = _SourceComponent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 4, 1),
    _SourceComponent_Type()
)
sourceComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sourceComponent.setStatus("mandatory")
_ComponentInfo_Type = OctetString
_ComponentInfo_Object = MibScalar
componentInfo = _ComponentInfo_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 4, 2),
    _ComponentInfo_Type()
)
componentInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    componentInfo.setStatus("mandatory")
_AlarmDescription_Type = OctetString
_AlarmDescription_Object = MibScalar
alarmDescription = _AlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 4, 3),
    _AlarmDescription_Type()
)
alarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmDescription.setStatus("mandatory")
_ProcessName_Type = OctetString
_ProcessName_Object = MibScalar
processName = _ProcessName_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 2, 4, 4),
    _ProcessName_Type()
)
processName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processName.setStatus("mandatory")
_ScAgentApplication_ObjectIdentity = ObjectIdentity
scAgentApplication = _ScAgentApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 1)
)
_ScaSourceComponent_Type = OctetString
_ScaSourceComponent_Object = MibScalar
scaSourceComponent = _ScaSourceComponent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 1, 1),
    _ScaSourceComponent_Type()
)
scaSourceComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scaSourceComponent.setStatus("mandatory")
_ScaErrorMessage_Type = OctetString
_ScaErrorMessage_Object = MibScalar
scaErrorMessage = _ScaErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 1, 2),
    _ScaErrorMessage_Type()
)
scaErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scaErrorMessage.setStatus("mandatory")
_UdrWriterApplication_ObjectIdentity = ObjectIdentity
udrWriterApplication = _UdrWriterApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 2)
)
_UwSourceComponent_Type = OctetString
_UwSourceComponent_Object = MibScalar
uwSourceComponent = _UwSourceComponent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 2, 1),
    _UwSourceComponent_Type()
)
uwSourceComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uwSourceComponent.setStatus("mandatory")
_UwInfoMessage_Type = OctetString
_UwInfoMessage_Object = MibScalar
uwInfoMessage = _UwInfoMessage_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 3, 2, 2),
    _UwInfoMessage_Type()
)
uwInfoMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uwInfoMessage.setStatus("mandatory")
_ProxyApplication_ObjectIdentity = ObjectIdentity
proxyApplication = _ProxyApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9905, 2, 4, 1)
)
_PxSourceComponent_Type = OctetString
_PxSourceComponent_Object = MibScalar
pxSourceComponent = _PxSourceComponent_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 4, 1, 1),
    _PxSourceComponent_Type()
)
pxSourceComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxSourceComponent.setStatus("mandatory")
_PxErrorMessage_Type = OctetString
_PxErrorMessage_Object = MibScalar
pxErrorMessage = _PxErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 4, 1, 2),
    _PxErrorMessage_Type()
)
pxErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pxErrorMessage.setStatus("mandatory")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("informative", 1),
          ("serious", 3),
          ("warning", 2))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9905, 2, 5),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects

procMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 1)
)
procMissing.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "prMissingProcName"),
        ("KENYA-COMPONENT-TRAPS", "prRespawnCommand"))
)
if mibBuilder.loadTexts:
    procMissing.setStatus(
        ""
    )

procMissingAfterRespawn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 2)
)
procMissingAfterRespawn.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "prMissingProcName"),
        ("KENYA-COMPONENT-TRAPS", "prRespawnCommand"))
)
if mibBuilder.loadTexts:
    procMissingAfterRespawn.setStatus(
        ""
    )

snmpUnreachableHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 3)
)
snmpUnreachableHost.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "snmpFailedComponent"),
        ("KENYA-COMPONENT-TRAPS", "snmpRequestedOid"))
)
if mibBuilder.loadTexts:
    snmpUnreachableHost.setStatus(
        ""
    )

dataCollectorThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 4)
)
dataCollectorThresholdExceeded.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "dcCheckedOid"),
        ("KENYA-COMPONENT-TRAPS", "dcErrorString"),
        ("KENYA-COMPONENT-TRAPS", "dcTestDescr"),
        ("KENYA-COMPONENT-TRAPS", "dcNbRepeat"))
)
if mibBuilder.loadTexts:
    dataCollectorThresholdExceeded.setStatus(
        ""
    )

dataCollectorSystemRequirement = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 5)
)
dataCollectorSystemRequirement.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "dcSystemRequirement"),
        ("KENYA-COMPONENT-TRAPS", "dcSystemErrorDate"))
)
if mibBuilder.loadTexts:
    dataCollectorSystemRequirement.setStatus(
        ""
    )

dataCollectorSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 6)
)
dataCollectorSystemError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "dcSystemRequirement"))
)
if mibBuilder.loadTexts:
    dataCollectorSystemError.setStatus(
        ""
    )

scAgentError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 7)
)
scAgentError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "scaSourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "scaErrorMessage"))
)
if mibBuilder.loadTexts:
    scAgentError.setStatus(
        ""
    )

healthCheckError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 8)
)
healthCheckError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"))
)
if mibBuilder.loadTexts:
    healthCheckError.setStatus(
        ""
    )

proxyError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 9)
)
proxyError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "pxSourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "pxErrorMessage"))
)
if mibBuilder.loadTexts:
    proxyError.setStatus(
        ""
    )

switchProvisioningError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 10)
)
switchProvisioningError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"))
)
if mibBuilder.loadTexts:
    switchProvisioningError.setStatus(
        ""
    )

powerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 11)
)
powerFailure.setObjects(
    ("KENYA-COMPONENT-TRAPS", "trapSeverity")
)
if mibBuilder.loadTexts:
    powerFailure.setStatus(
        ""
    )

linkFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 12)
)
linkFailure.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    linkFailure.setStatus(
        ""
    )

caInvalidVIPStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 13)
)
caInvalidVIPStatus.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    caInvalidVIPStatus.setStatus(
        ""
    )

caValidVIPStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 14)
)
caValidVIPStatus.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    caValidVIPStatus.setStatus(
        ""
    )

successfulProvisioning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 15)
)
successfulProvisioning.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    successfulProvisioning.setStatus(
        ""
    )

sSNModuleNotHA = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 16)
)
sSNModuleNotHA.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    sSNModuleNotHA.setStatus(
        ""
    )

successfulRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 17)
)
successfulRollback.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    successfulRollback.setStatus(
        ""
    )

procStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 18)
)
procStarted.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "processName"))
)
if mibBuilder.loadTexts:
    procStarted.setStatus(
        ""
    )

rectifierAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 19)
)
rectifierAlarm.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "alarmDescription"))
)
if mibBuilder.loadTexts:
    rectifierAlarm.setStatus(
        ""
    )

powerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 20)
)
powerOn.setObjects(
    ("KENYA-COMPONENT-TRAPS", "trapSeverity")
)
if mibBuilder.loadTexts:
    powerOn.setStatus(
        ""
    )

uwMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 21)
)
uwMessage.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "uwSourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "uwInfoMessage"))
)
if mibBuilder.loadTexts:
    uwMessage.setStatus(
        ""
    )

vlbProcStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 22)
)
vlbProcStarted.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "processName"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    vlbProcStarted.setStatus(
        ""
    )

vlbProcNotStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 23)
)
vlbProcNotStarted.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "processName"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    vlbProcNotStarted.setStatus(
        ""
    )

vlbProcStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 24)
)
vlbProcStopped.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "processName"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    vlbProcStopped.setStatus(
        ""
    )

vlbLogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 25)
)
vlbLogTrap.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "processName"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    vlbLogTrap.setStatus(
        ""
    )

bssgStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 30)
)
bssgStart.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgStart.setStatus(
        ""
    )

bssgStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 31)
)
bssgStop.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgStop.setStatus(
        ""
    )

bssgSmiConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 32)
)
bssgSmiConnectFailure.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgSmiConnectFailure.setStatus(
        ""
    )

bssgQuickRulesConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 33)
)
bssgQuickRulesConnectFailure.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgQuickRulesConnectFailure.setStatus(
        ""
    )

bssgSCDKDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 34)
)
bssgSCDKDisconnect.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgSCDKDisconnect.setStatus(
        ""
    )

bssgDatabaseConnectFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 35)
)
bssgDatabaseConnectFailure.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgDatabaseConnectFailure.setStatus(
        ""
    )

bssgReloadConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 36)
)
bssgReloadConfig.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    bssgReloadConfig.setStatus(
        ""
    )

start = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 70)
)
start.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    start.setStatus(
        ""
    )

stop = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 71)
)
stop.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    stop.setStatus(
        ""
    )

overloadActivatedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 72)
)
overloadActivatedTrap.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    overloadActivatedTrap.setStatus(
        ""
    )

overloadDesactivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 73)
)
overloadDesactivated.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    overloadDesactivated.setStatus(
        ""
    )

sCDKConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 74)
)
sCDKConnection.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    sCDKConnection.setStatus(
        ""
    )

sCDKDisconnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 75)
)
sCDKDisconnection.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    sCDKDisconnection.setStatus(
        ""
    )

uDRWritingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 76)
)
uDRWritingError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    uDRWritingError.setStatus(
        ""
    )

provisioningError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 77)
)
provisioningError.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    provisioningError.setStatus(
        ""
    )

activatedUDRZipper = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 78)
)
activatedUDRZipper.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    activatedUDRZipper.setStatus(
        ""
    )

desactivatedUDRZipper = NotificationType(
    (1, 3, 6, 1, 4, 1, 9905, 0, 79)
)
desactivatedUDRZipper.setObjects(
      *(("KENYA-COMPONENT-TRAPS", "trapSeverity"),
        ("KENYA-COMPONENT-TRAPS", "sourceComponent"),
        ("KENYA-COMPONENT-TRAPS", "componentInfo"))
)
if mibBuilder.loadTexts:
    desactivatedUDRZipper.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KENYA-COMPONENT-TRAPS",
    **{"procMissing": procMissing,
       "procMissingAfterRespawn": procMissingAfterRespawn,
       "snmpUnreachableHost": snmpUnreachableHost,
       "dataCollectorThresholdExceeded": dataCollectorThresholdExceeded,
       "dataCollectorSystemRequirement": dataCollectorSystemRequirement,
       "dataCollectorSystemError": dataCollectorSystemError,
       "scAgentError": scAgentError,
       "healthCheckError": healthCheckError,
       "proxyError": proxyError,
       "switchProvisioningError": switchProvisioningError,
       "powerFailure": powerFailure,
       "linkFailure": linkFailure,
       "caInvalidVIPStatus": caInvalidVIPStatus,
       "caValidVIPStatus": caValidVIPStatus,
       "successfulProvisioning": successfulProvisioning,
       "sSNModuleNotHA": sSNModuleNotHA,
       "successfulRollback": successfulRollback,
       "procStarted": procStarted,
       "rectifierAlarm": rectifierAlarm,
       "powerOn": powerOn,
       "uwMessage": uwMessage,
       "vlbProcStarted": vlbProcStarted,
       "vlbProcNotStarted": vlbProcNotStarted,
       "vlbProcStopped": vlbProcStopped,
       "vlbLogTrap": vlbLogTrap,
       "bssgStart": bssgStart,
       "bssgStop": bssgStop,
       "bssgSmiConnectFailure": bssgSmiConnectFailure,
       "bssgQuickRulesConnectFailure": bssgQuickRulesConnectFailure,
       "bssgSCDKDisconnect": bssgSCDKDisconnect,
       "bssgDatabaseConnectFailure": bssgDatabaseConnectFailure,
       "bssgReloadConfig": bssgReloadConfig,
       "start": start,
       "stop": stop,
       "overloadActivatedTrap": overloadActivatedTrap,
       "overloadDesactivated": overloadDesactivated,
       "sCDKConnection": sCDKConnection,
       "sCDKDisconnection": sCDKDisconnection,
       "uDRWritingError": uDRWritingError,
       "provisioningError": provisioningError,
       "activatedUDRZipper": activatedUDRZipper,
       "desactivatedUDRZipper": desactivatedUDRZipper,
       "nmDataCollector": nmDataCollector,
       "dcCheckedOid": dcCheckedOid,
       "dcErrorString": dcErrorString,
       "dcTestDescr": dcTestDescr,
       "dcNbRepeat": dcNbRepeat,
       "dcSystemRequirement": dcSystemRequirement,
       "dcSystemErrorDate": dcSystemErrorDate,
       "procRespawner": procRespawner,
       "prMissingProcName": prMissingProcName,
       "prRespawnCommand": prRespawnCommand,
       "nmsGolbalStatusProcessor": nmsGolbalStatusProcessor,
       "snmpFailedComponent": snmpFailedComponent,
       "snmpRequestedOid": snmpRequestedOid,
       "componentTrapSender": componentTrapSender,
       "sourceComponent": sourceComponent,
       "componentInfo": componentInfo,
       "alarmDescription": alarmDescription,
       "processName": processName,
       "scAgentApplication": scAgentApplication,
       "scaSourceComponent": scaSourceComponent,
       "scaErrorMessage": scaErrorMessage,
       "udrWriterApplication": udrWriterApplication,
       "uwSourceComponent": uwSourceComponent,
       "uwInfoMessage": uwInfoMessage,
       "proxyApplication": proxyApplication,
       "pxSourceComponent": pxSourceComponent,
       "pxErrorMessage": pxErrorMessage,
       "trapSeverity": trapSeverity}
)
