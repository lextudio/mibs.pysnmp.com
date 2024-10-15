# SNMP MIB module (APAGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APAGENTCAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:10 2024
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

(acmepacketAgentCapability,) = mibBuilder.importSymbols(
    "ACMEPACKET-SMI",
    "acmepacketAgentCapability")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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
 enterprises,
 iso,
 mib_2,
 snmpModules) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "mib-2",
    "snmpModules")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

apAgentCapModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1)
)
apAgentCapModule.setRevisions(
        ("1920-04-11 18:00",
         "1900-06-21 15:00",
         "2006-05-01 00:00",
         "2007-05-07 00:00",
         "1920-12-15 00:00",
         "2012-03-07 00:00",
         "2012-07-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApSnmpMibCapabilities_ObjectIdentity = ObjectIdentity
apSnmpMibCapabilities = _ApSnmpMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 1)
)
_ApIfMibCapabilities_ObjectIdentity = ObjectIdentity
apIfMibCapabilities = _ApIfMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 2)
)
_ApIPMibCapabilities_ObjectIdentity = ObjectIdentity
apIPMibCapabilities = _ApIPMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 3)
)
_ApTCPMibCapabilities_ObjectIdentity = ObjectIdentity
apTCPMibCapabilities = _ApTCPMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 4)
)
_ApUDPMibCapabilities_ObjectIdentity = ObjectIdentity
apUDPMibCapabilities = _ApUDPMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 5)
)
_ApEntityCapabilities_ObjectIdentity = ObjectIdentity
apEntityCapabilities = _ApEntityCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 6)
)
_ApSlogMibCapabilities_ObjectIdentity = ObjectIdentity
apSlogMibCapabilities = _ApSlogMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 7)
)
_ApSmgmtMibCapabilities_ObjectIdentity = ObjectIdentity
apSmgmtMibCapabilities = _ApSmgmtMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8)
)
_ApEnvMonitorMibCapabilities_ObjectIdentity = ObjectIdentity
apEnvMonitorMibCapabilities = _ApEnvMonitorMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 9)
)
_ApSwinventoryMibCapabilities_ObjectIdentity = ObjectIdentity
apSwinventoryMibCapabilities = _ApSwinventoryMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 10)
)
_ApLicenseMibCapabilities_ObjectIdentity = ObjectIdentity
apLicenseMibCapabilities = _ApLicenseMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 11)
)
_ApAmiMibCapabilities_ObjectIdentity = ObjectIdentity
apAmiMibCapabilities = _ApAmiMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 12)
)
_ApCodecMibCapabilities_ObjectIdentity = ObjectIdentity
apCodecMibCapabilities = _ApCodecMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 13)
)
_ApSecurityMibCapabilities_ObjectIdentity = ObjectIdentity
apSecurityMibCapabilities = _ApSecurityMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14)
)
_ApH323MibCapabilites_ObjectIdentity = ObjectIdentity
apH323MibCapabilites = _ApH323MibCapabilites_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 15)
)
_ApSLBMibCapabilities_ObjectIdentity = ObjectIdentity
apSLBMibCapabilities = _ApSLBMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 16)
)
_ApDiamMibCapabilities_ObjectIdentity = ObjectIdentity
apDiamMibCapabilities = _ApDiamMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 17)
)
_ApDDMibCapabilities_ObjectIdentity = ObjectIdentity
apDDMibCapabilities = _ApDDMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 18)
)
_ApDNSALGMibCapabilities_ObjectIdentity = ObjectIdentity
apDNSALGMibCapabilities = _ApDNSALGMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 19)
)
_ApAppsMibCapabilities_ObjectIdentity = ObjectIdentity
apAppsMibCapabilities = _ApAppsMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 20)
)
_ApSipMibCapabilities_ObjectIdentity = ObjectIdentity
apSipMibCapabilities = _ApSipMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 21)
)
_ApUsbcSysMibCapabilities_ObjectIdentity = ObjectIdentity
apUsbcSysMibCapabilities = _ApUsbcSysMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 22)
)
_ApRadiusMibCapabilities_ObjectIdentity = ObjectIdentity
apRadiusMibCapabilities = _ApRadiusMibCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 23)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

apSnmpCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    apSnmpCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSnmpCap.setStatus(
        "current"
    )

apSnmpv3Cap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    apSnmpv3Cap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSnmpv3Cap.setStatus(
        "current"
    )

apInterfacesCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    apInterfacesCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apInterfacesCap.setStatus(
        "current"
    )

apIfMibCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    apIfMibCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apIfMibCap.setStatus(
        "current"
    )

apIfMibHCCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    apIfMibHCCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apIfMibHCCap.setStatus(
        "current"
    )

apIpCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    apIpCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apIpCap.setStatus(
        "current"
    )

apTcpCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    apTcpCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apTcpCap.setStatus(
        "current"
    )

apUdpCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 5, 1)
)
if mibBuilder.loadTexts:
    apUdpCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apUdpCap.setStatus(
        "current"
    )

apEntityCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    apEntityCap.setProductRelease("Acme Packet for Relase 2.0")
if mibBuilder.loadTexts:
    apEntityCap.setStatus(
        "current"
    )

apSyslogCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    apSyslogCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSyslogCap.setStatus(
        "current"
    )

apSmgmtCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 1)
)
if mibBuilder.loadTexts:
    apSmgmtCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap.setStatus(
        "current"
    )

apSmgmtCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 2)
)
if mibBuilder.loadTexts:
    apSmgmtCap2.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap2.setStatus(
        "current"
    )

apSmgmtCap3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 3)
)
if mibBuilder.loadTexts:
    apSmgmtCap3.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap3.setStatus(
        "current"
    )

apSmgmtCap4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 4)
)
if mibBuilder.loadTexts:
    apSmgmtCap4.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap4.setStatus(
        "current"
    )

apSmgmtCap5 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    apSmgmtCap5.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap5.setStatus(
        "current"
    )

apSmgmtCap6 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 6)
)
if mibBuilder.loadTexts:
    apSmgmtCap6.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCap6.setStatus(
        "current"
    )

apSmgmtNSEPCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 7)
)
if mibBuilder.loadTexts:
    apSmgmtNSEPCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtNSEPCap.setStatus(
        "current"
    )

apSmgmtCtrlStatsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 8)
)
if mibBuilder.loadTexts:
    apSmgmtCtrlStatsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCtrlStatsCap.setStatus(
        "current"
    )

apSmgmtLDAPCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 9)
)
if mibBuilder.loadTexts:
    apSmgmtLDAPCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtLDAPCap.setStatus(
        "current"
    )

apSmgmtHDRCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 10)
)
if mibBuilder.loadTexts:
    apSmgmtHDRCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtHDRCap.setStatus(
        "current"
    )

apSmgmtMediaSuperCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 11)
)
if mibBuilder.loadTexts:
    apSmgmtMediaSuperCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtMediaSuperCap.setStatus(
        "current"
    )

apSmgmtH248Cap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 12)
)
if mibBuilder.loadTexts:
    apSmgmtH248Cap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtH248Cap.setStatus(
        "current"
    )

apSmgmtRFactorCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 13)
)
if mibBuilder.loadTexts:
    apSmgmtRFactorCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRFactorCap.setStatus(
        "current"
    )

apSmgmtSipRejectCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 14)
)
if mibBuilder.loadTexts:
    apSmgmtSipRejectCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtSipRejectCap.setStatus(
        "current"
    )

apSmgmtDOSNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 15)
)
if mibBuilder.loadTexts:
    apSmgmtDOSNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtDOSNotifyCap.setStatus(
        "current"
    )

apSmgmtRegNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 16)
)
if mibBuilder.loadTexts:
    apSmgmtRegNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegNotifyCap.setStatus(
        "current"
    )

apSmgmtNTPNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 17)
)
if mibBuilder.loadTexts:
    apSmgmtNTPNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtNTPNotifyCap.setStatus(
        "current"
    )

apSmgmtCollectorPushSuccessNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 18)
)
if mibBuilder.loadTexts:
    apSmgmtCollectorPushSuccessNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCollectorPushSuccessNotifyCap.setStatus(
        "current"
    )

apSmgmtExtSigRealmCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 19)
)
if mibBuilder.loadTexts:
    apSmgmtExtSigRealmCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtExtSigRealmCap.setStatus(
        "current"
    )

apSmgmtClockNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 20)
)
if mibBuilder.loadTexts:
    apSmgmtClockNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtClockNotifyCap.setStatus(
        "current"
    )

apSmgmtRegistrationCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 21)
)
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap.setStatus(
        "current"
    )

apSmgmtRegistrationCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 22)
)
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap2.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap2.setStatus(
        "current"
    )

apSmgmtRegCacheLimCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 23)
)
if mibBuilder.loadTexts:
    apSmgmtRegCacheLimCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegCacheLimCap.setStatus(
        "current"
    )

apSmgmtShortSessionCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 24)
)
if mibBuilder.loadTexts:
    apSmgmtShortSessionCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtShortSessionCap.setStatus(
        "current"
    )

apSystemManagementGatewaySynchronizedMonitorCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 25)
)
if mibBuilder.loadTexts:
    apSystemManagementGatewaySynchronizedMonitorCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSystemManagementGatewaySynchronizedMonitorCap.setStatus(
        "current"
    )

apSmgmtRegistrationCap3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 26)
)
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap3.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegistrationCap3.setStatus(
        "current"
    )

apSmgmtCallRecordingCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 27)
)
if mibBuilder.loadTexts:
    apSmgmtCallRecordingCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCallRecordingCap.setStatus(
        "current"
    )

apSmgmtH323AdditionsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 28)
)
if mibBuilder.loadTexts:
    apSmgmtH323AdditionsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtH323AdditionsCap.setStatus(
        "current"
    )

apSmgmtENUMCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 29)
)
if mibBuilder.loadTexts:
    apSmgmtENUMCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtENUMCap.setStatus(
        "current"
    )

apSmgmtExtSipCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 30)
)
if mibBuilder.loadTexts:
    apSmgmtExtSipCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtExtSipCap.setStatus(
        "current"
    )

apSmgmtRealmIcmpFailureCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 31)
)
if mibBuilder.loadTexts:
    apSmgmtRealmIcmpFailureCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRealmIcmpFailureCap.setStatus(
        "current"
    )

apSmgmtTrapTableObjectCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 32)
)
if mibBuilder.loadTexts:
    apSmgmtTrapTableObjectCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtTrapTableObjectCap.setStatus(
        "current"
    )

apSmgmtCDRPushReceiverFailureCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 33)
)
if mibBuilder.loadTexts:
    apSmgmtCDRPushReceiverFailureCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCDRPushReceiverFailureCap.setStatus(
        "current"
    )

apSmgmtRealmStatsQoSCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 34)
)
if mibBuilder.loadTexts:
    apSmgmtRealmStatsQoSCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRealmStatsQoSCap.setStatus(
        "current"
    )

apSmgmtInetAddrDOSNotifyCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 35)
)
if mibBuilder.loadTexts:
    apSmgmtInetAddrDOSNotifyCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtInetAddrDOSNotifyCap.setStatus(
        "current"
    )

apSmgmtApplicationCPUUsageCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 36)
)
if mibBuilder.loadTexts:
    apSmgmtApplicationCPUUsageCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtApplicationCPUUsageCap.setStatus(
        "current"
    )

apSmgmtRegistrationCapacityCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 37)
)
if mibBuilder.loadTexts:
    apSmgmtRegistrationCapacityCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRegistrationCapacityCap.setStatus(
        "obsolete"
    )

apSmgmtRejectedMessagesCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 38)
)
if mibBuilder.loadTexts:
    apSmgmtRejectedMessagesCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRejectedMessagesCap.setStatus(
        "current"
    )

apSmgmtEndPtDemotionCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 39)
)
if mibBuilder.loadTexts:
    apSmgmtEndPtDemotionCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtEndPtDemotionCap.setStatus(
        "current"
    )

apSmgmtAdminCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 40)
)
if mibBuilder.loadTexts:
    apSmgmtAdminCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtAdminCap.setStatus(
        "current"
    )

apSmgmtLPCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 41)
)
if mibBuilder.loadTexts:
    apSmgmtLPCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtLPCap.setStatus(
        "current"
    )

apSmgmtPhyUtilCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 42)
)
if mibBuilder.loadTexts:
    apSmgmtPhyUtilCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtPhyUtilCap.setStatus(
        "current"
    )

apSmgmtStorageSpaceCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 43)
)
if mibBuilder.loadTexts:
    apSmgmtStorageSpaceCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtStorageSpaceCap.setStatus(
        "current"
    )

apSmgmtCtrlStatsCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 44)
)
if mibBuilder.loadTexts:
    apSmgmtCtrlStatsCap2.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCtrlStatsCap2.setStatus(
        "current"
    )

apSmgmtDatabaseRegCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 45)
)
if mibBuilder.loadTexts:
    apSmgmtDatabaseRegCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtDatabaseRegCap.setStatus(
        "current"
    )

apSmgmtCallsRejectedCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 46)
)
if mibBuilder.loadTexts:
    apSmgmtCallsRejectedCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtCallsRejectedCap.setStatus(
        "current"
    )

apSmgmtSipInterfaceRegCacheLimCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 47)
)
if mibBuilder.loadTexts:
    apSmgmtSipInterfaceRegCacheLimCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtSipInterfaceRegCacheLimCap.setStatus(
        "current"
    )

apSmgmtRealmRegCacheSummaryCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 48)
)
if mibBuilder.loadTexts:
    apSmgmtRealmRegCacheSummaryCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtRealmRegCacheSummaryCap.setStatus(
        "current"
    )

apSmgmtSubscriptionSummaryCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 49)
)
if mibBuilder.loadTexts:
    apSmgmtSubscriptionSummaryCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtSubscriptionSummaryCap.setStatus(
        "current"
    )

apSmgmtH248PortMapUsageCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 50)
)
if mibBuilder.loadTexts:
    apSmgmtH248PortMapUsageCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtH248PortMapUsageCap.setStatus(
        "current"
    )

apSmgmtDOSNotifyTrustedtoUntrustedCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 51)
)
if mibBuilder.loadTexts:
    apSmgmtDOSNotifyTrustedtoUntrustedCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSmgmtDOSNotifyTrustedtoUntrustedCap.setStatus(
        "current"
    )

apSysMgmtETCUtilCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 8, 52)
)
if mibBuilder.loadTexts:
    apSysMgmtETCUtilCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSysMgmtETCUtilCap.setStatus(
        "current"
    )

apEnvMonCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 1)
)
if mibBuilder.loadTexts:
    apEnvMonCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apEnvMonCap.setStatus(
        "current"
    )

apEnvMonCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 2)
)
if mibBuilder.loadTexts:
    apEnvMonCap2.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apEnvMonCap2.setStatus(
        "current"
    )

apEnvMonPortChangeCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 3)
)
if mibBuilder.loadTexts:
    apEnvMonPortChangeCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apEnvMonPortChangeCap.setStatus(
        "current"
    )

apEnvMonCap4 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 9, 4)
)
if mibBuilder.loadTexts:
    apEnvMonCap4.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apEnvMonCap4.setStatus(
        "current"
    )

apSwInventoryCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 10, 1)
)
if mibBuilder.loadTexts:
    apSwInventoryCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSwInventoryCap.setStatus(
        "current"
    )

apLicenseCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    apLicenseCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apLicenseCap.setStatus(
        "current"
    )

apLicenseDatabaseRegCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    apLicenseDatabaseRegCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apLicenseDatabaseRegCap.setStatus(
        "current"
    )

apLicenseExpirationWarnCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 11, 3)
)
if mibBuilder.loadTexts:
    apLicenseExpirationWarnCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apLicenseExpirationWarnCap.setStatus(
        "current"
    )

apAmiCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    apAmiCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apAmiCap.setStatus(
        "current"
    )

apCodecRealmCodecCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 1)
)
if mibBuilder.loadTexts:
    apCodecRealmCodecCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apCodecRealmCodecCap.setStatus(
        "current"
    )

apCodecMediaProcessingCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    apCodecMediaProcessingCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apCodecMediaProcessingCap.setStatus(
        "current"
    )

apCodecRealmCodecCap2 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 3)
)
if mibBuilder.loadTexts:
    apCodecRealmCodecCap2.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apCodecRealmCodecCap2.setStatus(
        "current"
    )

apCodecTranscodingStatsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 13, 4)
)
if mibBuilder.loadTexts:
    apCodecTranscodingStatsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apCodecTranscodingStatsCap.setStatus(
        "current"
    )

apSecurityCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 1)
)
if mibBuilder.loadTexts:
    apSecurityCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityCap.setStatus(
        "current"
    )

apSecurityIPsecTunnelsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 2)
)
if mibBuilder.loadTexts:
    apSecurityIPsecTunnelsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityIPsecTunnelsCap.setStatus(
        "current"
    )

apSecurityIkeInterfaceCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 3)
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceCap.setStatus(
        "current"
    )

apSecurityTacacsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 4)
)
if mibBuilder.loadTexts:
    apSecurityTacacsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityTacacsCap.setStatus(
        "current"
    )

apSecurityCertStatusCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 5)
)
if mibBuilder.loadTexts:
    apSecurityCertStatusCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityCertStatusCap.setStatus(
        "current"
    )

apSecurityIkeDDoSCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 6)
)
if mibBuilder.loadTexts:
    apSecurityIkeDDoSCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityIkeDDoSCap.setStatus(
        "current"
    )

apSecurityCertificateCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 7)
)
if mibBuilder.loadTexts:
    apSecurityCertificateCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityCertificateCap.setStatus(
        "current"
    )

apSecurityGtpStatusCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 8)
)
if mibBuilder.loadTexts:
    apSecurityGtpStatusCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityGtpStatusCap.setStatus(
        "current"
    )

apSecurityIkeInterfaceInfoCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 9)
)
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInfoCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityIkeInterfaceInfoCap.setStatus(
        "current"
    )

apSecurityTacacsNotifCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 10)
)
if mibBuilder.loadTexts:
    apSecurityTacacsNotifCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityTacacsNotifCap.setStatus(
        "current"
    )

apSecurityInetCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 11)
)
if mibBuilder.loadTexts:
    apSecurityInetCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityInetCap.setStatus(
        "current"
    )

apSecurityIkeDDoSInetCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 14, 12)
)
if mibBuilder.loadTexts:
    apSecurityIkeDDoSInetCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSecurityIkeDDoSInetCap.setStatus(
        "current"
    )

apH323StackCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 15, 1)
)
if mibBuilder.loadTexts:
    apH323StackCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apH323StackCap.setStatus(
        "current"
    )

apSLBEndpointCapacityCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 1)
)
if mibBuilder.loadTexts:
    apSLBEndpointCapacityCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSLBEndpointCapacityCap.setStatus(
        "current"
    )

apSLBUntrustedEndpointCapacityCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 16, 2)
)
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSLBUntrustedEndpointCapacityCap.setStatus(
        "current"
    )

apDiamMibCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 17, 1)
)
if mibBuilder.loadTexts:
    apDiamMibCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apDiamMibCap.setStatus(
        "current"
    )

apDDStatsGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    apDDStatsGroupCap.setProductRelease("Acme Packet Diameter Signaling Controller")
if mibBuilder.loadTexts:
    apDDStatsGroupCap.setStatus(
        "current"
    )

apDDNotifGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 2)
)
if mibBuilder.loadTexts:
    apDDNotifGroupCap.setProductRelease("Acme Packet Diameter Signaling Controller")
if mibBuilder.loadTexts:
    apDDNotifGroupCap.setStatus(
        "current"
    )

apDDStatsGroup2Cap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 3)
)
if mibBuilder.loadTexts:
    apDDStatsGroup2Cap.setProductRelease("Acme Packet Diameter Signaling Controller")
if mibBuilder.loadTexts:
    apDDStatsGroup2Cap.setStatus(
        "current"
    )

apDDStatsGroup3Cap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 18, 4)
)
if mibBuilder.loadTexts:
    apDDStatsGroup3Cap.setProductRelease("Acme Packet Diameter Signaling Controller")
if mibBuilder.loadTexts:
    apDDStatsGroup3Cap.setStatus(
        "current"
    )

apDNSALGStatsGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 1)
)
if mibBuilder.loadTexts:
    apDNSALGStatsGroupCap.setProductRelease("Acme Packet DNS ALG")
if mibBuilder.loadTexts:
    apDNSALGStatsGroupCap.setStatus(
        "current"
    )

apDNSALGNotifGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 19, 2)
)
if mibBuilder.loadTexts:
    apDNSALGNotifGroupCap.setProductRelease("Acme Packet PEC")
if mibBuilder.loadTexts:
    apDNSALGNotifGroupCap.setStatus(
        "current"
    )

apAppsENUMStatusGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 1)
)
if mibBuilder.loadTexts:
    apAppsENUMStatusGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apAppsENUMStatusGroupCap.setStatus(
        "current"
    )

apAppsDNSStatusGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 2)
)
if mibBuilder.loadTexts:
    apAppsDNSStatusGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apAppsDNSStatusGroupCap.setStatus(
        "current"
    )

apAppsENUMSvrNotifGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 3)
)
if mibBuilder.loadTexts:
    apAppsENUMSvrNotifGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apAppsENUMSvrNotifGroupCap.setStatus(
        "current"
    )

apAppsDNSSvrNotifGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 20, 4)
)
if mibBuilder.loadTexts:
    apAppsDNSSvrNotifGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apAppsDNSSvrNotifGroupCap.setStatus(
        "current"
    )

apSipSecInterfaceRegNotifGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 1)
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegNotifGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSipSecInterfaceRegNotifGroupCap.setStatus(
        "current"
    )

apSipSecInterfaceRegObjectsGroupCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 21, 2)
)
if mibBuilder.loadTexts:
    apSipSecInterfaceRegObjectsGroupCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apSipSecInterfaceRegObjectsGroupCap.setStatus(
        "current"
    )

apUsbcSysCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 22, 1)
)
if mibBuilder.loadTexts:
    apUsbcSysCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apUsbcSysCap.setStatus(
        "current"
    )

apRadiusMibCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    apRadiusMibCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apRadiusMibCap.setStatus(
        "current"
    )

apRadiusServerStatsCap = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 9148, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    apRadiusServerStatsCap.setProductRelease("Acme Packet SD")
if mibBuilder.loadTexts:
    apRadiusServerStatsCap.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APAGENTCAP-MIB",
    **{"apAgentCapModule": apAgentCapModule,
       "apSnmpMibCapabilities": apSnmpMibCapabilities,
       "apSnmpCap": apSnmpCap,
       "apSnmpv3Cap": apSnmpv3Cap,
       "apIfMibCapabilities": apIfMibCapabilities,
       "apInterfacesCap": apInterfacesCap,
       "apIfMibCap": apIfMibCap,
       "apIfMibHCCap": apIfMibHCCap,
       "apIPMibCapabilities": apIPMibCapabilities,
       "apIpCap": apIpCap,
       "apTCPMibCapabilities": apTCPMibCapabilities,
       "apTcpCap": apTcpCap,
       "apUDPMibCapabilities": apUDPMibCapabilities,
       "apUdpCap": apUdpCap,
       "apEntityCapabilities": apEntityCapabilities,
       "apEntityCap": apEntityCap,
       "apSlogMibCapabilities": apSlogMibCapabilities,
       "apSyslogCap": apSyslogCap,
       "apSmgmtMibCapabilities": apSmgmtMibCapabilities,
       "apSmgmtCap": apSmgmtCap,
       "apSmgmtCap2": apSmgmtCap2,
       "apSmgmtCap3": apSmgmtCap3,
       "apSmgmtCap4": apSmgmtCap4,
       "apSmgmtCap5": apSmgmtCap5,
       "apSmgmtCap6": apSmgmtCap6,
       "apSmgmtNSEPCap": apSmgmtNSEPCap,
       "apSmgmtCtrlStatsCap": apSmgmtCtrlStatsCap,
       "apSmgmtLDAPCap": apSmgmtLDAPCap,
       "apSmgmtHDRCap": apSmgmtHDRCap,
       "apSmgmtMediaSuperCap": apSmgmtMediaSuperCap,
       "apSmgmtH248Cap": apSmgmtH248Cap,
       "apSmgmtRFactorCap": apSmgmtRFactorCap,
       "apSmgmtSipRejectCap": apSmgmtSipRejectCap,
       "apSmgmtDOSNotifyCap": apSmgmtDOSNotifyCap,
       "apSmgmtRegNotifyCap": apSmgmtRegNotifyCap,
       "apSmgmtNTPNotifyCap": apSmgmtNTPNotifyCap,
       "apSmgmtCollectorPushSuccessNotifyCap": apSmgmtCollectorPushSuccessNotifyCap,
       "apSmgmtExtSigRealmCap": apSmgmtExtSigRealmCap,
       "apSmgmtClockNotifyCap": apSmgmtClockNotifyCap,
       "apSmgmtRegistrationCap": apSmgmtRegistrationCap,
       "apSmgmtRegistrationCap2": apSmgmtRegistrationCap2,
       "apSmgmtRegCacheLimCap": apSmgmtRegCacheLimCap,
       "apSmgmtShortSessionCap": apSmgmtShortSessionCap,
       "apSystemManagementGatewaySynchronizedMonitorCap": apSystemManagementGatewaySynchronizedMonitorCap,
       "apSmgmtRegistrationCap3": apSmgmtRegistrationCap3,
       "apSmgmtCallRecordingCap": apSmgmtCallRecordingCap,
       "apSmgmtH323AdditionsCap": apSmgmtH323AdditionsCap,
       "apSmgmtENUMCap": apSmgmtENUMCap,
       "apSmgmtExtSipCap": apSmgmtExtSipCap,
       "apSmgmtRealmIcmpFailureCap": apSmgmtRealmIcmpFailureCap,
       "apSmgmtTrapTableObjectCap": apSmgmtTrapTableObjectCap,
       "apSmgmtCDRPushReceiverFailureCap": apSmgmtCDRPushReceiverFailureCap,
       "apSmgmtRealmStatsQoSCap": apSmgmtRealmStatsQoSCap,
       "apSmgmtInetAddrDOSNotifyCap": apSmgmtInetAddrDOSNotifyCap,
       "apSmgmtApplicationCPUUsageCap": apSmgmtApplicationCPUUsageCap,
       "apSmgmtRegistrationCapacityCap": apSmgmtRegistrationCapacityCap,
       "apSmgmtRejectedMessagesCap": apSmgmtRejectedMessagesCap,
       "apSmgmtEndPtDemotionCap": apSmgmtEndPtDemotionCap,
       "apSmgmtAdminCap": apSmgmtAdminCap,
       "apSmgmtLPCap": apSmgmtLPCap,
       "apSmgmtPhyUtilCap": apSmgmtPhyUtilCap,
       "apSmgmtStorageSpaceCap": apSmgmtStorageSpaceCap,
       "apSmgmtCtrlStatsCap2": apSmgmtCtrlStatsCap2,
       "apSmgmtDatabaseRegCap": apSmgmtDatabaseRegCap,
       "apSmgmtCallsRejectedCap": apSmgmtCallsRejectedCap,
       "apSmgmtSipInterfaceRegCacheLimCap": apSmgmtSipInterfaceRegCacheLimCap,
       "apSmgmtRealmRegCacheSummaryCap": apSmgmtRealmRegCacheSummaryCap,
       "apSmgmtSubscriptionSummaryCap": apSmgmtSubscriptionSummaryCap,
       "apSmgmtH248PortMapUsageCap": apSmgmtH248PortMapUsageCap,
       "apSmgmtDOSNotifyTrustedtoUntrustedCap": apSmgmtDOSNotifyTrustedtoUntrustedCap,
       "apSysMgmtETCUtilCap": apSysMgmtETCUtilCap,
       "apEnvMonitorMibCapabilities": apEnvMonitorMibCapabilities,
       "apEnvMonCap": apEnvMonCap,
       "apEnvMonCap2": apEnvMonCap2,
       "apEnvMonPortChangeCap": apEnvMonPortChangeCap,
       "apEnvMonCap4": apEnvMonCap4,
       "apSwinventoryMibCapabilities": apSwinventoryMibCapabilities,
       "apSwInventoryCap": apSwInventoryCap,
       "apLicenseMibCapabilities": apLicenseMibCapabilities,
       "apLicenseCap": apLicenseCap,
       "apLicenseDatabaseRegCap": apLicenseDatabaseRegCap,
       "apLicenseExpirationWarnCap": apLicenseExpirationWarnCap,
       "apAmiMibCapabilities": apAmiMibCapabilities,
       "apAmiCap": apAmiCap,
       "apCodecMibCapabilities": apCodecMibCapabilities,
       "apCodecRealmCodecCap": apCodecRealmCodecCap,
       "apCodecMediaProcessingCap": apCodecMediaProcessingCap,
       "apCodecRealmCodecCap2": apCodecRealmCodecCap2,
       "apCodecTranscodingStatsCap": apCodecTranscodingStatsCap,
       "apSecurityMibCapabilities": apSecurityMibCapabilities,
       "apSecurityCap": apSecurityCap,
       "apSecurityIPsecTunnelsCap": apSecurityIPsecTunnelsCap,
       "apSecurityIkeInterfaceCap": apSecurityIkeInterfaceCap,
       "apSecurityTacacsCap": apSecurityTacacsCap,
       "apSecurityCertStatusCap": apSecurityCertStatusCap,
       "apSecurityIkeDDoSCap": apSecurityIkeDDoSCap,
       "apSecurityCertificateCap": apSecurityCertificateCap,
       "apSecurityGtpStatusCap": apSecurityGtpStatusCap,
       "apSecurityIkeInterfaceInfoCap": apSecurityIkeInterfaceInfoCap,
       "apSecurityTacacsNotifCap": apSecurityTacacsNotifCap,
       "apSecurityInetCap": apSecurityInetCap,
       "apSecurityIkeDDoSInetCap": apSecurityIkeDDoSInetCap,
       "apH323MibCapabilites": apH323MibCapabilites,
       "apH323StackCap": apH323StackCap,
       "apSLBMibCapabilities": apSLBMibCapabilities,
       "apSLBEndpointCapacityCap": apSLBEndpointCapacityCap,
       "apSLBUntrustedEndpointCapacityCap": apSLBUntrustedEndpointCapacityCap,
       "apDiamMibCapabilities": apDiamMibCapabilities,
       "apDiamMibCap": apDiamMibCap,
       "apDDMibCapabilities": apDDMibCapabilities,
       "apDDStatsGroupCap": apDDStatsGroupCap,
       "apDDNotifGroupCap": apDDNotifGroupCap,
       "apDDStatsGroup2Cap": apDDStatsGroup2Cap,
       "apDDStatsGroup3Cap": apDDStatsGroup3Cap,
       "apDNSALGMibCapabilities": apDNSALGMibCapabilities,
       "apDNSALGStatsGroupCap": apDNSALGStatsGroupCap,
       "apDNSALGNotifGroupCap": apDNSALGNotifGroupCap,
       "apAppsMibCapabilities": apAppsMibCapabilities,
       "apAppsENUMStatusGroupCap": apAppsENUMStatusGroupCap,
       "apAppsDNSStatusGroupCap": apAppsDNSStatusGroupCap,
       "apAppsENUMSvrNotifGroupCap": apAppsENUMSvrNotifGroupCap,
       "apAppsDNSSvrNotifGroupCap": apAppsDNSSvrNotifGroupCap,
       "apSipMibCapabilities": apSipMibCapabilities,
       "apSipSecInterfaceRegNotifGroupCap": apSipSecInterfaceRegNotifGroupCap,
       "apSipSecInterfaceRegObjectsGroupCap": apSipSecInterfaceRegObjectsGroupCap,
       "apUsbcSysMibCapabilities": apUsbcSysMibCapabilities,
       "apUsbcSysCap": apUsbcSysCap,
       "apRadiusMibCapabilities": apRadiusMibCapabilities,
       "apRadiusMibCap": apRadiusMibCap,
       "apRadiusServerStatsCap": apRadiusServerStatsCap}
)
