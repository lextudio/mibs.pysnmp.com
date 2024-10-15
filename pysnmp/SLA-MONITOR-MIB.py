# SNMP MIB module (SLA-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SLA-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:53:50 2024
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

(Dscp,) = mibBuilder.importSymbols(
    "DIFFSERV-DSCP-TC",
    "Dscp")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")

(policy,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "policy")


# MODULE-IDENTITY

slaMonitorMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8)
)
slaMonitorMib.setRevisions(
        ("2015-05-29 00:00",
         "2013-03-05 00:00",
         "2013-01-31 00:00",
         "2012-12-11 00:00",
         "2012-09-19 00:00",
         "2012-09-04 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlaMonitorMibNotifications_ObjectIdentity = ObjectIdentity
slaMonitorMibNotifications = _SlaMonitorMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 0)
)
_SlaMonitorMibClasses_ObjectIdentity = ObjectIdentity
slaMonitorMibClasses = _SlaMonitorMibClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1)
)
_SlaMonitorAgtClasses_ObjectIdentity = ObjectIdentity
slaMonitorAgtClasses = _SlaMonitorAgtClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1)
)


class _SlaMonitorAgentStatus_Type(Integer32):
    """Custom type slaMonitorAgentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlaMonitorAgentStatus_Type.__name__ = "Integer32"
_SlaMonitorAgentStatus_Object = MibScalar
slaMonitorAgentStatus = _SlaMonitorAgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 1),
    _SlaMonitorAgentStatus_Type()
)
slaMonitorAgentStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentStatus.setStatus("current")
_SlaMonitorAgentAddressType_Type = InetAddressType
_SlaMonitorAgentAddressType_Object = MibScalar
slaMonitorAgentAddressType = _SlaMonitorAgentAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 2),
    _SlaMonitorAgentAddressType_Type()
)
slaMonitorAgentAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentAddressType.setStatus("current")
_SlaMonitorAgentAddress_Type = InetAddress
_SlaMonitorAgentAddress_Object = MibScalar
slaMonitorAgentAddress = _SlaMonitorAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 3),
    _SlaMonitorAgentAddress_Type()
)
slaMonitorAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentAddress.setStatus("current")
_SlaMonitorAgentPort_Type = InetPortNumber
_SlaMonitorAgentPort_Object = MibScalar
slaMonitorAgentPort = _SlaMonitorAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 4),
    _SlaMonitorAgentPort_Type()
)
slaMonitorAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentPort.setStatus("current")


class _SlaMonitorAgentRegisteredWithServer_Type(Integer32):
    """Custom type slaMonitorAgentRegisteredWithServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 2),
          ("registered", 1))
    )


_SlaMonitorAgentRegisteredWithServer_Type.__name__ = "Integer32"
_SlaMonitorAgentRegisteredWithServer_Object = MibScalar
slaMonitorAgentRegisteredWithServer = _SlaMonitorAgentRegisteredWithServer_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 5),
    _SlaMonitorAgentRegisteredWithServer_Type()
)
slaMonitorAgentRegisteredWithServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentRegisteredWithServer.setStatus("current")
_SlaMonitorAgentRegisteredServerAddrType_Type = InetAddressType
_SlaMonitorAgentRegisteredServerAddrType_Object = MibScalar
slaMonitorAgentRegisteredServerAddrType = _SlaMonitorAgentRegisteredServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 6),
    _SlaMonitorAgentRegisteredServerAddrType_Type()
)
slaMonitorAgentRegisteredServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentRegisteredServerAddrType.setStatus("current")
_SlaMonitorAgentRegisteredServerAddr_Type = InetAddress
_SlaMonitorAgentRegisteredServerAddr_Object = MibScalar
slaMonitorAgentRegisteredServerAddr = _SlaMonitorAgentRegisteredServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 7),
    _SlaMonitorAgentRegisteredServerAddr_Type()
)
slaMonitorAgentRegisteredServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentRegisteredServerAddr.setStatus("current")
_SlaMonitorAgentRegisteredServerPort_Type = InetPortNumber
_SlaMonitorAgentRegisteredServerPort_Object = MibScalar
slaMonitorAgentRegisteredServerPort = _SlaMonitorAgentRegisteredServerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 8),
    _SlaMonitorAgentRegisteredServerPort_Type()
)
slaMonitorAgentRegisteredServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentRegisteredServerPort.setStatus("current")
_SlaMonitorAgentRegistrationTime_Type = Unsigned32
_SlaMonitorAgentRegistrationTime_Object = MibScalar
slaMonitorAgentRegistrationTime = _SlaMonitorAgentRegistrationTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 9),
    _SlaMonitorAgentRegistrationTime_Type()
)
slaMonitorAgentRegistrationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentRegistrationTime.setStatus("current")
if mibBuilder.loadTexts:
    slaMonitorAgentRegistrationTime.setUnits("seconds")


class _SlaMonitorAgentCliAvailable_Type(Integer32):
    """Custom type slaMonitorAgentCliAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_SlaMonitorAgentCliAvailable_Type.__name__ = "Integer32"
_SlaMonitorAgentCliAvailable_Object = MibScalar
slaMonitorAgentCliAvailable = _SlaMonitorAgentCliAvailable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 10),
    _SlaMonitorAgentCliAvailable_Type()
)
slaMonitorAgentCliAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentCliAvailable.setStatus("current")
_SlaMonitorAgentCliTimeout_Type = Unsigned32
_SlaMonitorAgentCliTimeout_Object = MibScalar
slaMonitorAgentCliTimeout = _SlaMonitorAgentCliTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 11),
    _SlaMonitorAgentCliTimeout_Type()
)
slaMonitorAgentCliTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentCliTimeout.setStatus("current")
if mibBuilder.loadTexts:
    slaMonitorAgentCliTimeout.setUnits("seconds")


class _SlaMonitorAgentCliTimeoutMode_Type(Integer32):
    """Custom type slaMonitorAgentCliTimeoutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SlaMonitorAgentCliTimeoutMode_Type.__name__ = "Integer32"
_SlaMonitorAgentCliTimeoutMode_Object = MibScalar
slaMonitorAgentCliTimeoutMode = _SlaMonitorAgentCliTimeoutMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 12),
    _SlaMonitorAgentCliTimeoutMode_Type()
)
slaMonitorAgentCliTimeoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentCliTimeoutMode.setStatus("current")


class _SlaMonitorAgentSupportedApps_Type(Bits):
    """Custom type slaMonitorAgentSupportedApps based on Bits"""
    namedValues = NamedValues(
        *(("ntr", 1),
          ("other", 0),
          ("rtp", 2))
    )

_SlaMonitorAgentSupportedApps_Type.__name__ = "Bits"
_SlaMonitorAgentSupportedApps_Object = MibScalar
slaMonitorAgentSupportedApps = _SlaMonitorAgentSupportedApps_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 13),
    _SlaMonitorAgentSupportedApps_Type()
)
slaMonitorAgentSupportedApps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentSupportedApps.setStatus("current")
_SlaMonitorAgentConfiguredAgentAddrType_Type = InetAddressType
_SlaMonitorAgentConfiguredAgentAddrType_Object = MibScalar
slaMonitorAgentConfiguredAgentAddrType = _SlaMonitorAgentConfiguredAgentAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 14),
    _SlaMonitorAgentConfiguredAgentAddrType_Type()
)
slaMonitorAgentConfiguredAgentAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAgentAddrType.setStatus("current")
_SlaMonitorAgentConfiguredAgentAddr_Type = InetAddress
_SlaMonitorAgentConfiguredAgentAddr_Object = MibScalar
slaMonitorAgentConfiguredAgentAddr = _SlaMonitorAgentConfiguredAgentAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 15),
    _SlaMonitorAgentConfiguredAgentAddr_Type()
)
slaMonitorAgentConfiguredAgentAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAgentAddr.setStatus("current")
_SlaMonitorAgentConfiguredAgentPort_Type = InetPortNumber
_SlaMonitorAgentConfiguredAgentPort_Object = MibScalar
slaMonitorAgentConfiguredAgentPort = _SlaMonitorAgentConfiguredAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 16),
    _SlaMonitorAgentConfiguredAgentPort_Type()
)
slaMonitorAgentConfiguredAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAgentPort.setStatus("current")
_SlaMonitorAgentConfiguredServerAddrType_Type = InetAddressType
_SlaMonitorAgentConfiguredServerAddrType_Object = MibScalar
slaMonitorAgentConfiguredServerAddrType = _SlaMonitorAgentConfiguredServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 17),
    _SlaMonitorAgentConfiguredServerAddrType_Type()
)
slaMonitorAgentConfiguredServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredServerAddrType.setStatus("current")
_SlaMonitorAgentConfiguredServerAddr_Type = InetAddress
_SlaMonitorAgentConfiguredServerAddr_Object = MibScalar
slaMonitorAgentConfiguredServerAddr = _SlaMonitorAgentConfiguredServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 18),
    _SlaMonitorAgentConfiguredServerAddr_Type()
)
slaMonitorAgentConfiguredServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredServerAddr.setStatus("current")
_SlaMonitorAgentConfiguredServerPort_Type = InetPortNumber
_SlaMonitorAgentConfiguredServerPort_Object = MibScalar
slaMonitorAgentConfiguredServerPort = _SlaMonitorAgentConfiguredServerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 19),
    _SlaMonitorAgentConfiguredServerPort_Type()
)
slaMonitorAgentConfiguredServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredServerPort.setStatus("current")
_SlaMonitorAgentConfiguredAltServerAddrType_Type = InetAddressType
_SlaMonitorAgentConfiguredAltServerAddrType_Object = MibScalar
slaMonitorAgentConfiguredAltServerAddrType = _SlaMonitorAgentConfiguredAltServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 20),
    _SlaMonitorAgentConfiguredAltServerAddrType_Type()
)
slaMonitorAgentConfiguredAltServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAltServerAddrType.setStatus("current")
_SlaMonitorAgentConfiguredAltServerAddr_Type = InetAddress
_SlaMonitorAgentConfiguredAltServerAddr_Object = MibScalar
slaMonitorAgentConfiguredAltServerAddr = _SlaMonitorAgentConfiguredAltServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 21),
    _SlaMonitorAgentConfiguredAltServerAddr_Type()
)
slaMonitorAgentConfiguredAltServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAltServerAddr.setStatus("current")
_SlaMonitorAgentConfiguredAltServerPort_Type = InetPortNumber
_SlaMonitorAgentConfiguredAltServerPort_Object = MibScalar
slaMonitorAgentConfiguredAltServerPort = _SlaMonitorAgentConfiguredAltServerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 22),
    _SlaMonitorAgentConfiguredAltServerPort_Type()
)
slaMonitorAgentConfiguredAltServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAltServerPort.setStatus("current")
_SlaMonitorAgentToAgentPort_Type = InetPortNumber
_SlaMonitorAgentToAgentPort_Object = MibScalar
slaMonitorAgentToAgentPort = _SlaMonitorAgentToAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 23),
    _SlaMonitorAgentToAgentPort_Type()
)
slaMonitorAgentToAgentPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentToAgentPort.setStatus("current")
_SlaMonitorAgentConfiguredAgentToAgentPort_Type = InetPortNumber
_SlaMonitorAgentConfiguredAgentToAgentPort_Object = MibScalar
slaMonitorAgentConfiguredAgentToAgentPort = _SlaMonitorAgentConfiguredAgentToAgentPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 24),
    _SlaMonitorAgentConfiguredAgentToAgentPort_Type()
)
slaMonitorAgentConfiguredAgentToAgentPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAgentToAgentPort.setStatus("current")


class _SlaMonitorAgentEncryptionSupport_Type(Integer32):
    """Custom type slaMonitorAgentEncryptionSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_SlaMonitorAgentEncryptionSupport_Type.__name__ = "Integer32"
_SlaMonitorAgentEncryptionSupport_Object = MibScalar
slaMonitorAgentEncryptionSupport = _SlaMonitorAgentEncryptionSupport_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 25),
    _SlaMonitorAgentEncryptionSupport_Type()
)
slaMonitorAgentEncryptionSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorAgentEncryptionSupport.setStatus("current")


class _SlaMonitorAgentConfiguredAgentVrfName_Type(DisplayString):
    """Custom type slaMonitorAgentConfiguredAgentVrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlaMonitorAgentConfiguredAgentVrfName_Type.__name__ = "DisplayString"
_SlaMonitorAgentConfiguredAgentVrfName_Object = MibScalar
slaMonitorAgentConfiguredAgentVrfName = _SlaMonitorAgentConfiguredAgentVrfName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 26),
    _SlaMonitorAgentConfiguredAgentVrfName_Type()
)
slaMonitorAgentConfiguredAgentVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentConfiguredAgentVrfName.setStatus("current")


class _SlaMonitorAgentSlaParameter_Type(DisplayString):
    """Custom type slaMonitorAgentSlaParameter based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SlaMonitorAgentSlaParameter_Type.__name__ = "DisplayString"
_SlaMonitorAgentSlaParameter_Object = MibScalar
slaMonitorAgentSlaParameter = _SlaMonitorAgentSlaParameter_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 27),
    _SlaMonitorAgentSlaParameter_Type()
)
slaMonitorAgentSlaParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentSlaParameter.setStatus("current")


class _SlaMonitorAgentCertFileInstallAction_Type(Integer32):
    """Custom type slaMonitorAgentCertFileInstallAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deinstall", 3),
          ("install", 2),
          ("noAction", 1))
    )


_SlaMonitorAgentCertFileInstallAction_Type.__name__ = "Integer32"
_SlaMonitorAgentCertFileInstallAction_Object = MibScalar
slaMonitorAgentCertFileInstallAction = _SlaMonitorAgentCertFileInstallAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 28),
    _SlaMonitorAgentCertFileInstallAction_Type()
)
slaMonitorAgentCertFileInstallAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentCertFileInstallAction.setStatus("current")


class _SlaMonitorAgentCertFile_Type(DisplayString):
    """Custom type slaMonitorAgentCertFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_SlaMonitorAgentCertFile_Type.__name__ = "DisplayString"
_SlaMonitorAgentCertFile_Object = MibScalar
slaMonitorAgentCertFile = _SlaMonitorAgentCertFile_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 29),
    _SlaMonitorAgentCertFile_Type()
)
slaMonitorAgentCertFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentCertFile.setStatus("current")


class _SlaMonitorAgentServerBypass_Type(Integer32):
    """Custom type slaMonitorAgentServerBypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_SlaMonitorAgentServerBypass_Type.__name__ = "Integer32"
_SlaMonitorAgentServerBypass_Object = MibScalar
slaMonitorAgentServerBypass = _SlaMonitorAgentServerBypass_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 30),
    _SlaMonitorAgentServerBypass_Type()
)
slaMonitorAgentServerBypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentServerBypass.setStatus("current")


class _SlaMonitorAgentRefuseServerTests_Type(Integer32):
    """Custom type slaMonitorAgentRefuseServerTests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("refuse", 2))
    )


_SlaMonitorAgentRefuseServerTests_Type.__name__ = "Integer32"
_SlaMonitorAgentRefuseServerTests_Object = MibScalar
slaMonitorAgentRefuseServerTests = _SlaMonitorAgentRefuseServerTests_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 1, 31),
    _SlaMonitorAgentRefuseServerTests_Type()
)
slaMonitorAgentRefuseServerTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slaMonitorAgentRefuseServerTests.setStatus("current")
_SlaMonitorAgtTestClasses_ObjectIdentity = ObjectIdentity
slaMonitorAgtTestClasses = _SlaMonitorAgtTestClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2)
)
_SlaMonitorNtrCtrlTable_Object = MibTable
slaMonitorNtrCtrlTable = _SlaMonitorNtrCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlTable.setStatus("current")
_SlaMonitorNtrCtrlEntry_Object = MibTableRow
slaMonitorNtrCtrlEntry = _SlaMonitorNtrCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1)
)
slaMonitorNtrCtrlEntry.setIndexNames(
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlOwnerId"),
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlTestName"),
)
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlEntry.setStatus("current")


class _SlaMonitorNtrCtrlOwnerId_Type(SnmpAdminString):
    """Custom type slaMonitorNtrCtrlOwnerId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlaMonitorNtrCtrlOwnerId_Type.__name__ = "SnmpAdminString"
_SlaMonitorNtrCtrlOwnerId_Object = MibTableColumn
slaMonitorNtrCtrlOwnerId = _SlaMonitorNtrCtrlOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 1),
    _SlaMonitorNtrCtrlOwnerId_Type()
)
slaMonitorNtrCtrlOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlOwnerId.setStatus("current")


class _SlaMonitorNtrCtrlTestName_Type(SnmpAdminString):
    """Custom type slaMonitorNtrCtrlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlaMonitorNtrCtrlTestName_Type.__name__ = "SnmpAdminString"
_SlaMonitorNtrCtrlTestName_Object = MibTableColumn
slaMonitorNtrCtrlTestName = _SlaMonitorNtrCtrlTestName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 2),
    _SlaMonitorNtrCtrlTestName_Type()
)
slaMonitorNtrCtrlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlTestName.setStatus("current")


class _SlaMonitorNtrCtrlTargetAddressType_Type(InetAddressType):
    """Custom type slaMonitorNtrCtrlTargetAddressType based on InetAddressType"""


_SlaMonitorNtrCtrlTargetAddressType_Object = MibTableColumn
slaMonitorNtrCtrlTargetAddressType = _SlaMonitorNtrCtrlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 3),
    _SlaMonitorNtrCtrlTargetAddressType_Type()
)
slaMonitorNtrCtrlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlTargetAddressType.setStatus("current")
_SlaMonitorNtrCtrlTargetAddress_Type = InetAddress
_SlaMonitorNtrCtrlTargetAddress_Object = MibTableColumn
slaMonitorNtrCtrlTargetAddress = _SlaMonitorNtrCtrlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 4),
    _SlaMonitorNtrCtrlTargetAddress_Type()
)
slaMonitorNtrCtrlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlTargetAddress.setStatus("current")


class _SlaMonitorNtrCtrlDscp_Type(Dscp):
    """Custom type slaMonitorNtrCtrlDscp based on Dscp"""
    defaultValue = 0


_SlaMonitorNtrCtrlDscp_Object = MibTableColumn
slaMonitorNtrCtrlDscp = _SlaMonitorNtrCtrlDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 5),
    _SlaMonitorNtrCtrlDscp_Type()
)
slaMonitorNtrCtrlDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlDscp.setStatus("current")


class _SlaMonitorNtrCtrlAttempts_Type(Integer32):
    """Custom type slaMonitorNtrCtrlAttempts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SlaMonitorNtrCtrlAttempts_Type.__name__ = "Integer32"
_SlaMonitorNtrCtrlAttempts_Object = MibTableColumn
slaMonitorNtrCtrlAttempts = _SlaMonitorNtrCtrlAttempts_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 6),
    _SlaMonitorNtrCtrlAttempts_Type()
)
slaMonitorNtrCtrlAttempts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlAttempts.setStatus("current")


class _SlaMonitorNtrCtrlPeriod_Type(Integer32):
    """Custom type slaMonitorNtrCtrlPeriod based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 200000),
    )


_SlaMonitorNtrCtrlPeriod_Type.__name__ = "Integer32"
_SlaMonitorNtrCtrlPeriod_Object = MibTableColumn
slaMonitorNtrCtrlPeriod = _SlaMonitorNtrCtrlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 7),
    _SlaMonitorNtrCtrlPeriod_Type()
)
slaMonitorNtrCtrlPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlPeriod.setStatus("current")


class _SlaMonitorNtrCtrlAdminStatus_Type(Integer32):
    """Custom type slaMonitorNtrCtrlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlaMonitorNtrCtrlAdminStatus_Type.__name__ = "Integer32"
_SlaMonitorNtrCtrlAdminStatus_Object = MibTableColumn
slaMonitorNtrCtrlAdminStatus = _SlaMonitorNtrCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 8),
    _SlaMonitorNtrCtrlAdminStatus_Type()
)
slaMonitorNtrCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlAdminStatus.setStatus("current")


class _SlaMonitorNtrCtrlLabel_Type(SnmpAdminString):
    """Custom type slaMonitorNtrCtrlLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlaMonitorNtrCtrlLabel_Type.__name__ = "SnmpAdminString"
_SlaMonitorNtrCtrlLabel_Object = MibTableColumn
slaMonitorNtrCtrlLabel = _SlaMonitorNtrCtrlLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 9),
    _SlaMonitorNtrCtrlLabel_Type()
)
slaMonitorNtrCtrlLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlLabel.setStatus("current")


class _SlaMonitorNtrCtrlStorageType_Type(StorageType):
    """Custom type slaMonitorNtrCtrlStorageType based on StorageType"""


_SlaMonitorNtrCtrlStorageType_Object = MibTableColumn
slaMonitorNtrCtrlStorageType = _SlaMonitorNtrCtrlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 10),
    _SlaMonitorNtrCtrlStorageType_Type()
)
slaMonitorNtrCtrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlStorageType.setStatus("current")
_SlaMonitorNtrCtrlRowStatus_Type = RowStatus
_SlaMonitorNtrCtrlRowStatus_Object = MibTableColumn
slaMonitorNtrCtrlRowStatus = _SlaMonitorNtrCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 1, 1, 11),
    _SlaMonitorNtrCtrlRowStatus_Type()
)
slaMonitorNtrCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorNtrCtrlRowStatus.setStatus("current")
_SlaMonitorNtrResultsTable_Object = MibTable
slaMonitorNtrResultsTable = _SlaMonitorNtrResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    slaMonitorNtrResultsTable.setStatus("current")
_SlaMonitorNtrResultsEntry_Object = MibTableRow
slaMonitorNtrResultsEntry = _SlaMonitorNtrResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1)
)
slaMonitorNtrResultsEntry.setIndexNames(
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlOwnerId"),
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlTestName"),
)
if mibBuilder.loadTexts:
    slaMonitorNtrResultsEntry.setStatus("current")


class _SlaMonitorNtrResultsOperStatus_Type(Integer32):
    """Custom type slaMonitorNtrResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 2),
          ("completed", 3),
          ("inProgress", 1))
    )


_SlaMonitorNtrResultsOperStatus_Type.__name__ = "Integer32"
_SlaMonitorNtrResultsOperStatus_Object = MibTableColumn
slaMonitorNtrResultsOperStatus = _SlaMonitorNtrResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 1),
    _SlaMonitorNtrResultsOperStatus_Type()
)
slaMonitorNtrResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsOperStatus.setStatus("current")
_SlaMonitorNtrResultsSrcAddressType_Type = InetAddressType
_SlaMonitorNtrResultsSrcAddressType_Object = MibTableColumn
slaMonitorNtrResultsSrcAddressType = _SlaMonitorNtrResultsSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 2),
    _SlaMonitorNtrResultsSrcAddressType_Type()
)
slaMonitorNtrResultsSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsSrcAddressType.setStatus("current")
_SlaMonitorNtrResultsSrcAddress_Type = InetAddress
_SlaMonitorNtrResultsSrcAddress_Object = MibTableColumn
slaMonitorNtrResultsSrcAddress = _SlaMonitorNtrResultsSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 3),
    _SlaMonitorNtrResultsSrcAddress_Type()
)
slaMonitorNtrResultsSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsSrcAddress.setStatus("current")
_SlaMonitorNtrResultsDstAddressType_Type = InetAddressType
_SlaMonitorNtrResultsDstAddressType_Object = MibTableColumn
slaMonitorNtrResultsDstAddressType = _SlaMonitorNtrResultsDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 4),
    _SlaMonitorNtrResultsDstAddressType_Type()
)
slaMonitorNtrResultsDstAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsDstAddressType.setStatus("current")
_SlaMonitorNtrResultsDstAddress_Type = InetAddress
_SlaMonitorNtrResultsDstAddress_Object = MibTableColumn
slaMonitorNtrResultsDstAddress = _SlaMonitorNtrResultsDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 5),
    _SlaMonitorNtrResultsDstAddress_Type()
)
slaMonitorNtrResultsDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsDstAddress.setStatus("current")
_SlaMonitorNtrResultsSrcPort_Type = InetPortNumber
_SlaMonitorNtrResultsSrcPort_Object = MibTableColumn
slaMonitorNtrResultsSrcPort = _SlaMonitorNtrResultsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 6),
    _SlaMonitorNtrResultsSrcPort_Type()
)
slaMonitorNtrResultsSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsSrcPort.setStatus("current")
_SlaMonitorNtrResultsDstPort_Type = InetPortNumber
_SlaMonitorNtrResultsDstPort_Object = MibTableColumn
slaMonitorNtrResultsDstPort = _SlaMonitorNtrResultsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 7),
    _SlaMonitorNtrResultsDstPort_Type()
)
slaMonitorNtrResultsDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsDstPort.setStatus("current")
_SlaMonitorNtrResultsDscp_Type = Dscp
_SlaMonitorNtrResultsDscp_Object = MibTableColumn
slaMonitorNtrResultsDscp = _SlaMonitorNtrResultsDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 8),
    _SlaMonitorNtrResultsDscp_Type()
)
slaMonitorNtrResultsDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsDscp.setStatus("current")
_SlaMonitorNtrResultsTTL_Type = Unsigned32
_SlaMonitorNtrResultsTTL_Object = MibTableColumn
slaMonitorNtrResultsTTL = _SlaMonitorNtrResultsTTL_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 9),
    _SlaMonitorNtrResultsTTL_Type()
)
slaMonitorNtrResultsTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsTTL.setStatus("current")


class _SlaMonitorNtrResultsCompletionData_Type(Bits):
    """Custom type slaMonitorNtrResultsCompletionData based on Bits"""
    namedValues = NamedValues(
        *(("other", 0),
          ("remoteFirewalledUnreachable", 6),
          ("remoteHostUnreachable", 4),
          ("remoteNetUnreachable", 3),
          ("remoteNoResponse", 9),
          ("remotePortUnreachable", 2),
          ("remoteProtocolUnreachable", 5),
          ("remoteResponded", 7),
          ("remoteResponseLikely", 8),
          ("remoteUnreachable", 1))
    )

_SlaMonitorNtrResultsCompletionData_Type.__name__ = "Bits"
_SlaMonitorNtrResultsCompletionData_Object = MibTableColumn
slaMonitorNtrResultsCompletionData = _SlaMonitorNtrResultsCompletionData_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 10),
    _SlaMonitorNtrResultsCompletionData_Type()
)
slaMonitorNtrResultsCompletionData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsCompletionData.setStatus("current")


class _SlaMonitorNtrResultsCompletionSummary_Type(SnmpAdminString):
    """Custom type slaMonitorNtrResultsCompletionSummary based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlaMonitorNtrResultsCompletionSummary_Type.__name__ = "SnmpAdminString"
_SlaMonitorNtrResultsCompletionSummary_Object = MibTableColumn
slaMonitorNtrResultsCompletionSummary = _SlaMonitorNtrResultsCompletionSummary_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 11),
    _SlaMonitorNtrResultsCompletionSummary_Type()
)
slaMonitorNtrResultsCompletionSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsCompletionSummary.setStatus("current")


class _SlaMonitorNtrResultsAbortData_Type(Bits):
    """Custom type slaMonitorNtrResultsAbortData based on Bits"""
    namedValues = NamedValues(
        *(("agentBusy", 2),
          ("agentDisabled", 1),
          ("cancelled", 4),
          ("other", 0),
          ("timeout", 3))
    )

_SlaMonitorNtrResultsAbortData_Type.__name__ = "Bits"
_SlaMonitorNtrResultsAbortData_Object = MibTableColumn
slaMonitorNtrResultsAbortData = _SlaMonitorNtrResultsAbortData_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 12),
    _SlaMonitorNtrResultsAbortData_Type()
)
slaMonitorNtrResultsAbortData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsAbortData.setStatus("current")
_SlaMonitorNtrResultsHopCount_Type = Unsigned32
_SlaMonitorNtrResultsHopCount_Object = MibTableColumn
slaMonitorNtrResultsHopCount = _SlaMonitorNtrResultsHopCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 2, 1, 13),
    _SlaMonitorNtrResultsHopCount_Type()
)
slaMonitorNtrResultsHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrResultsHopCount.setStatus("current")
_SlaMonitorNtrHopsTable_Object = MibTable
slaMonitorNtrHopsTable = _SlaMonitorNtrHopsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    slaMonitorNtrHopsTable.setStatus("current")
_SlaMonitorNtrHopsEntry_Object = MibTableRow
slaMonitorNtrHopsEntry = _SlaMonitorNtrHopsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1)
)
slaMonitorNtrHopsEntry.setIndexNames(
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlOwnerId"),
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrCtrlTestName"),
    (0, "SLA-MONITOR-MIB", "slaMonitorNtrHopsHopIndex"),
)
if mibBuilder.loadTexts:
    slaMonitorNtrHopsEntry.setStatus("current")


class _SlaMonitorNtrHopsHopIndex_Type(Unsigned32):
    """Custom type slaMonitorNtrHopsHopIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SlaMonitorNtrHopsHopIndex_Type.__name__ = "Unsigned32"
_SlaMonitorNtrHopsHopIndex_Object = MibTableColumn
slaMonitorNtrHopsHopIndex = _SlaMonitorNtrHopsHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 1),
    _SlaMonitorNtrHopsHopIndex_Type()
)
slaMonitorNtrHopsHopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsHopIndex.setStatus("current")
_SlaMonitorNtrHopsTgtAddressType_Type = InetAddressType
_SlaMonitorNtrHopsTgtAddressType_Object = MibTableColumn
slaMonitorNtrHopsTgtAddressType = _SlaMonitorNtrHopsTgtAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 2),
    _SlaMonitorNtrHopsTgtAddressType_Type()
)
slaMonitorNtrHopsTgtAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsTgtAddressType.setStatus("current")
_SlaMonitorNtrHopsTgtAddress_Type = InetAddress
_SlaMonitorNtrHopsTgtAddress_Object = MibTableColumn
slaMonitorNtrHopsTgtAddress = _SlaMonitorNtrHopsTgtAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 3),
    _SlaMonitorNtrHopsTgtAddress_Type()
)
slaMonitorNtrHopsTgtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsTgtAddress.setStatus("current")
_SlaMonitorNtrHopsRtt_Type = Unsigned32
_SlaMonitorNtrHopsRtt_Object = MibTableColumn
slaMonitorNtrHopsRtt = _SlaMonitorNtrHopsRtt_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 4),
    _SlaMonitorNtrHopsRtt_Type()
)
slaMonitorNtrHopsRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsRtt.setStatus("current")
_SlaMonitorNtrHopsIngressDscp_Type = Dscp
_SlaMonitorNtrHopsIngressDscp_Object = MibTableColumn
slaMonitorNtrHopsIngressDscp = _SlaMonitorNtrHopsIngressDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 5),
    _SlaMonitorNtrHopsIngressDscp_Type()
)
slaMonitorNtrHopsIngressDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsIngressDscp.setStatus("current")
_SlaMonitorNtrHopsEgressDscp_Type = Dscp
_SlaMonitorNtrHopsEgressDscp_Object = MibTableColumn
slaMonitorNtrHopsEgressDscp = _SlaMonitorNtrHopsEgressDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 3, 1, 6),
    _SlaMonitorNtrHopsEgressDscp_Type()
)
slaMonitorNtrHopsEgressDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorNtrHopsEgressDscp.setStatus("current")
_SlaMonitorRtpCtrlTable_Object = MibTable
slaMonitorRtpCtrlTable = _SlaMonitorRtpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlTable.setStatus("current")
_SlaMonitorRtpCtrlEntry_Object = MibTableRow
slaMonitorRtpCtrlEntry = _SlaMonitorRtpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1)
)
slaMonitorRtpCtrlEntry.setIndexNames(
    (0, "SLA-MONITOR-MIB", "slaMonitorRtpCtrlOwnerId"),
    (0, "SLA-MONITOR-MIB", "slaMonitorRtpCtrlTestName"),
)
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlEntry.setStatus("current")


class _SlaMonitorRtpCtrlOwnerId_Type(SnmpAdminString):
    """Custom type slaMonitorRtpCtrlOwnerId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlaMonitorRtpCtrlOwnerId_Type.__name__ = "SnmpAdminString"
_SlaMonitorRtpCtrlOwnerId_Object = MibTableColumn
slaMonitorRtpCtrlOwnerId = _SlaMonitorRtpCtrlOwnerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 1),
    _SlaMonitorRtpCtrlOwnerId_Type()
)
slaMonitorRtpCtrlOwnerId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlOwnerId.setStatus("current")


class _SlaMonitorRtpCtrlTestName_Type(SnmpAdminString):
    """Custom type slaMonitorRtpCtrlTestName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SlaMonitorRtpCtrlTestName_Type.__name__ = "SnmpAdminString"
_SlaMonitorRtpCtrlTestName_Object = MibTableColumn
slaMonitorRtpCtrlTestName = _SlaMonitorRtpCtrlTestName_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 2),
    _SlaMonitorRtpCtrlTestName_Type()
)
slaMonitorRtpCtrlTestName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlTestName.setStatus("current")


class _SlaMonitorRtpCtrlTargetAddressType_Type(InetAddressType):
    """Custom type slaMonitorRtpCtrlTargetAddressType based on InetAddressType"""


_SlaMonitorRtpCtrlTargetAddressType_Object = MibTableColumn
slaMonitorRtpCtrlTargetAddressType = _SlaMonitorRtpCtrlTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 3),
    _SlaMonitorRtpCtrlTargetAddressType_Type()
)
slaMonitorRtpCtrlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlTargetAddressType.setStatus("current")
_SlaMonitorRtpCtrlTargetAddress_Type = InetAddress
_SlaMonitorRtpCtrlTargetAddress_Object = MibTableColumn
slaMonitorRtpCtrlTargetAddress = _SlaMonitorRtpCtrlTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 4),
    _SlaMonitorRtpCtrlTargetAddress_Type()
)
slaMonitorRtpCtrlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlTargetAddress.setStatus("current")


class _SlaMonitorRtpCtrlDscp_Type(Dscp):
    """Custom type slaMonitorRtpCtrlDscp based on Dscp"""
    defaultValue = 0


_SlaMonitorRtpCtrlDscp_Object = MibTableColumn
slaMonitorRtpCtrlDscp = _SlaMonitorRtpCtrlDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 5),
    _SlaMonitorRtpCtrlDscp_Type()
)
slaMonitorRtpCtrlDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlDscp.setStatus("current")


class _SlaMonitorRtpCtrlTestPackets_Type(Integer32):
    """Custom type slaMonitorRtpCtrlTestPackets based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SlaMonitorRtpCtrlTestPackets_Type.__name__ = "Integer32"
_SlaMonitorRtpCtrlTestPackets_Object = MibTableColumn
slaMonitorRtpCtrlTestPackets = _SlaMonitorRtpCtrlTestPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 6),
    _SlaMonitorRtpCtrlTestPackets_Type()
)
slaMonitorRtpCtrlTestPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlTestPackets.setStatus("current")


class _SlaMonitorRtpCtrlSyncPackets_Type(Integer32):
    """Custom type slaMonitorRtpCtrlSyncPackets based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100),
    )


_SlaMonitorRtpCtrlSyncPackets_Type.__name__ = "Integer32"
_SlaMonitorRtpCtrlSyncPackets_Object = MibTableColumn
slaMonitorRtpCtrlSyncPackets = _SlaMonitorRtpCtrlSyncPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 7),
    _SlaMonitorRtpCtrlSyncPackets_Type()
)
slaMonitorRtpCtrlSyncPackets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlSyncPackets.setStatus("current")


class _SlaMonitorRtpCtrlPeriod_Type(Integer32):
    """Custom type slaMonitorRtpCtrlPeriod based on Integer32"""
    defaultValue = 20000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 200000),
    )


_SlaMonitorRtpCtrlPeriod_Type.__name__ = "Integer32"
_SlaMonitorRtpCtrlPeriod_Object = MibTableColumn
slaMonitorRtpCtrlPeriod = _SlaMonitorRtpCtrlPeriod_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 8),
    _SlaMonitorRtpCtrlPeriod_Type()
)
slaMonitorRtpCtrlPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlPeriod.setStatus("current")


class _SlaMonitorRtpCtrlAdminStatus_Type(Integer32):
    """Custom type slaMonitorRtpCtrlAdminStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SlaMonitorRtpCtrlAdminStatus_Type.__name__ = "Integer32"
_SlaMonitorRtpCtrlAdminStatus_Object = MibTableColumn
slaMonitorRtpCtrlAdminStatus = _SlaMonitorRtpCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 9),
    _SlaMonitorRtpCtrlAdminStatus_Type()
)
slaMonitorRtpCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlAdminStatus.setStatus("current")


class _SlaMonitorRtpCtrlLabel_Type(SnmpAdminString):
    """Custom type slaMonitorRtpCtrlLabel based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlaMonitorRtpCtrlLabel_Type.__name__ = "SnmpAdminString"
_SlaMonitorRtpCtrlLabel_Object = MibTableColumn
slaMonitorRtpCtrlLabel = _SlaMonitorRtpCtrlLabel_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 10),
    _SlaMonitorRtpCtrlLabel_Type()
)
slaMonitorRtpCtrlLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlLabel.setStatus("current")


class _SlaMonitorRtpCtrlStorageType_Type(StorageType):
    """Custom type slaMonitorRtpCtrlStorageType based on StorageType"""


_SlaMonitorRtpCtrlStorageType_Object = MibTableColumn
slaMonitorRtpCtrlStorageType = _SlaMonitorRtpCtrlStorageType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 11),
    _SlaMonitorRtpCtrlStorageType_Type()
)
slaMonitorRtpCtrlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlStorageType.setStatus("current")
_SlaMonitorRtpCtrlRowStatus_Type = RowStatus
_SlaMonitorRtpCtrlRowStatus_Object = MibTableColumn
slaMonitorRtpCtrlRowStatus = _SlaMonitorRtpCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 4, 1, 12),
    _SlaMonitorRtpCtrlRowStatus_Type()
)
slaMonitorRtpCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    slaMonitorRtpCtrlRowStatus.setStatus("current")
_SlaMonitorRtpResultsTable_Object = MibTable
slaMonitorRtpResultsTable = _SlaMonitorRtpResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    slaMonitorRtpResultsTable.setStatus("current")
_SlaMonitorRtpResultsEntry_Object = MibTableRow
slaMonitorRtpResultsEntry = _SlaMonitorRtpResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1)
)
slaMonitorRtpResultsEntry.setIndexNames(
    (0, "SLA-MONITOR-MIB", "slaMonitorRtpCtrlOwnerId"),
    (0, "SLA-MONITOR-MIB", "slaMonitorRtpCtrlTestName"),
)
if mibBuilder.loadTexts:
    slaMonitorRtpResultsEntry.setStatus("current")


class _SlaMonitorRtpResultsOperStatus_Type(Integer32):
    """Custom type slaMonitorRtpResultsOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 2),
          ("completed", 3),
          ("inProgress", 1))
    )


_SlaMonitorRtpResultsOperStatus_Type.__name__ = "Integer32"
_SlaMonitorRtpResultsOperStatus_Object = MibTableColumn
slaMonitorRtpResultsOperStatus = _SlaMonitorRtpResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 1),
    _SlaMonitorRtpResultsOperStatus_Type()
)
slaMonitorRtpResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsOperStatus.setStatus("current")
_SlaMonitorRtpResultsSrcAddressType_Type = InetAddressType
_SlaMonitorRtpResultsSrcAddressType_Object = MibTableColumn
slaMonitorRtpResultsSrcAddressType = _SlaMonitorRtpResultsSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 2),
    _SlaMonitorRtpResultsSrcAddressType_Type()
)
slaMonitorRtpResultsSrcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsSrcAddressType.setStatus("current")
_SlaMonitorRtpResultsSrcAddress_Type = InetAddress
_SlaMonitorRtpResultsSrcAddress_Object = MibTableColumn
slaMonitorRtpResultsSrcAddress = _SlaMonitorRtpResultsSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 3),
    _SlaMonitorRtpResultsSrcAddress_Type()
)
slaMonitorRtpResultsSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsSrcAddress.setStatus("current")
_SlaMonitorRtpResultsDstAddressType_Type = InetAddressType
_SlaMonitorRtpResultsDstAddressType_Object = MibTableColumn
slaMonitorRtpResultsDstAddressType = _SlaMonitorRtpResultsDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 4),
    _SlaMonitorRtpResultsDstAddressType_Type()
)
slaMonitorRtpResultsDstAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsDstAddressType.setStatus("current")
_SlaMonitorRtpResultsDstAddress_Type = InetAddress
_SlaMonitorRtpResultsDstAddress_Object = MibTableColumn
slaMonitorRtpResultsDstAddress = _SlaMonitorRtpResultsDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 5),
    _SlaMonitorRtpResultsDstAddress_Type()
)
slaMonitorRtpResultsDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsDstAddress.setStatus("current")
_SlaMonitorRtpResultsSrcPort_Type = InetPortNumber
_SlaMonitorRtpResultsSrcPort_Object = MibTableColumn
slaMonitorRtpResultsSrcPort = _SlaMonitorRtpResultsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 6),
    _SlaMonitorRtpResultsSrcPort_Type()
)
slaMonitorRtpResultsSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsSrcPort.setStatus("current")
_SlaMonitorRtpResultsDstPort_Type = InetPortNumber
_SlaMonitorRtpResultsDstPort_Object = MibTableColumn
slaMonitorRtpResultsDstPort = _SlaMonitorRtpResultsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 7),
    _SlaMonitorRtpResultsDstPort_Type()
)
slaMonitorRtpResultsDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsDstPort.setStatus("current")
_SlaMonitorRtpResultsDscp_Type = Dscp
_SlaMonitorRtpResultsDscp_Object = MibTableColumn
slaMonitorRtpResultsDscp = _SlaMonitorRtpResultsDscp_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 8),
    _SlaMonitorRtpResultsDscp_Type()
)
slaMonitorRtpResultsDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsDscp.setStatus("current")
_SlaMonitorRtpResultsAverageDelay_Type = Unsigned32
_SlaMonitorRtpResultsAverageDelay_Object = MibTableColumn
slaMonitorRtpResultsAverageDelay = _SlaMonitorRtpResultsAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 9),
    _SlaMonitorRtpResultsAverageDelay_Type()
)
slaMonitorRtpResultsAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsAverageDelay.setStatus("current")
_SlaMonitorRtpResultsMedianDelay_Type = Unsigned32
_SlaMonitorRtpResultsMedianDelay_Object = MibTableColumn
slaMonitorRtpResultsMedianDelay = _SlaMonitorRtpResultsMedianDelay_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 10),
    _SlaMonitorRtpResultsMedianDelay_Type()
)
slaMonitorRtpResultsMedianDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsMedianDelay.setStatus("current")
_SlaMonitorRtpResultsPacketLoss_Type = Unsigned32
_SlaMonitorRtpResultsPacketLoss_Object = MibTableColumn
slaMonitorRtpResultsPacketLoss = _SlaMonitorRtpResultsPacketLoss_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 11),
    _SlaMonitorRtpResultsPacketLoss_Type()
)
slaMonitorRtpResultsPacketLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsPacketLoss.setStatus("current")
_SlaMonitorRtpResultsOutOfOrderArrivals_Type = Unsigned32
_SlaMonitorRtpResultsOutOfOrderArrivals_Object = MibTableColumn
slaMonitorRtpResultsOutOfOrderArrivals = _SlaMonitorRtpResultsOutOfOrderArrivals_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 12),
    _SlaMonitorRtpResultsOutOfOrderArrivals_Type()
)
slaMonitorRtpResultsOutOfOrderArrivals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsOutOfOrderArrivals.setStatus("current")
_SlaMonitorRtpResultsJitterQuartile0_Type = Unsigned32
_SlaMonitorRtpResultsJitterQuartile0_Object = MibTableColumn
slaMonitorRtpResultsJitterQuartile0 = _SlaMonitorRtpResultsJitterQuartile0_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 13),
    _SlaMonitorRtpResultsJitterQuartile0_Type()
)
slaMonitorRtpResultsJitterQuartile0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsJitterQuartile0.setStatus("current")
_SlaMonitorRtpResultsJitterQuartile1_Type = Unsigned32
_SlaMonitorRtpResultsJitterQuartile1_Object = MibTableColumn
slaMonitorRtpResultsJitterQuartile1 = _SlaMonitorRtpResultsJitterQuartile1_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 14),
    _SlaMonitorRtpResultsJitterQuartile1_Type()
)
slaMonitorRtpResultsJitterQuartile1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsJitterQuartile1.setStatus("current")
_SlaMonitorRtpResultsJitterQuartile2_Type = Unsigned32
_SlaMonitorRtpResultsJitterQuartile2_Object = MibTableColumn
slaMonitorRtpResultsJitterQuartile2 = _SlaMonitorRtpResultsJitterQuartile2_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 15),
    _SlaMonitorRtpResultsJitterQuartile2_Type()
)
slaMonitorRtpResultsJitterQuartile2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsJitterQuartile2.setStatus("current")
_SlaMonitorRtpResultsJitterQuartile3_Type = Unsigned32
_SlaMonitorRtpResultsJitterQuartile3_Object = MibTableColumn
slaMonitorRtpResultsJitterQuartile3 = _SlaMonitorRtpResultsJitterQuartile3_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 16),
    _SlaMonitorRtpResultsJitterQuartile3_Type()
)
slaMonitorRtpResultsJitterQuartile3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsJitterQuartile3.setStatus("current")
_SlaMonitorRtpResultsJitterQuartile4_Type = Unsigned32
_SlaMonitorRtpResultsJitterQuartile4_Object = MibTableColumn
slaMonitorRtpResultsJitterQuartile4 = _SlaMonitorRtpResultsJitterQuartile4_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 17),
    _SlaMonitorRtpResultsJitterQuartile4_Type()
)
slaMonitorRtpResultsJitterQuartile4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsJitterQuartile4.setStatus("current")


class _SlaMonitorRtpResultsAbortData_Type(Bits):
    """Custom type slaMonitorRtpResultsAbortData based on Bits"""
    namedValues = NamedValues(
        *(("agentBusy", 2),
          ("agentDisabled", 1),
          ("cancelled", 4),
          ("deniedByTarget", 5),
          ("networkIssue", 6),
          ("other", 0),
          ("timeSync", 7),
          ("timeout", 3))
    )

_SlaMonitorRtpResultsAbortData_Type.__name__ = "Bits"
_SlaMonitorRtpResultsAbortData_Object = MibTableColumn
slaMonitorRtpResultsAbortData = _SlaMonitorRtpResultsAbortData_Object(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 1, 2, 5, 1, 18),
    _SlaMonitorRtpResultsAbortData_Type()
)
slaMonitorRtpResultsAbortData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaMonitorRtpResultsAbortData.setStatus("current")
_SlaMonitorMibConformance_ObjectIdentity = ObjectIdentity
slaMonitorMibConformance = _SlaMonitorMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2)
)
_SlaMonitorMibCompliances_ObjectIdentity = ObjectIdentity
slaMonitorMibCompliances = _SlaMonitorMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 1)
)
_SlaMonitorMibGroups_ObjectIdentity = ObjectIdentity
slaMonitorMibGroups = _SlaMonitorMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 2)
)

# Managed Objects groups

slaMonitorAgentConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 2, 1)
)
slaMonitorAgentConfigGroup.setObjects(
      *(("SLA-MONITOR-MIB", "slaMonitorAgentStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRegisteredWithServer"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRegisteredServerAddrType"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRegisteredServerAddr"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRegisteredServerPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRegistrationTime"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentCliAvailable"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentCliTimeout"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentCliTimeoutMode"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentSupportedApps"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAgentAddrType"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAgentAddr"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAgentPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredServerAddrType"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredServerAddr"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredServerPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAltServerAddrType"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAltServerAddr"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAltServerPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentToAgentPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAgentToAgentPort"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentEncryptionSupport"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentConfiguredAgentVrfName"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentSlaParameter"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentCertFileInstallAction"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentCertFile"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentServerBypass"),
        ("SLA-MONITOR-MIB", "slaMonitorAgentRefuseServerTests"))
)
if mibBuilder.loadTexts:
    slaMonitorAgentConfigGroup.setStatus("current")

slaMonitorAgentNtrTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 2, 2)
)
slaMonitorAgentNtrTestGroup.setObjects(
      *(("SLA-MONITOR-MIB", "slaMonitorNtrCtrlTargetAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlTargetAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlDscp"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlAttempts"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlPeriod"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlAdminStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlLabel"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlStorageType"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrCtrlRowStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsOperStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsSrcAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsSrcAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsDstAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsDstAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsSrcPort"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsDstPort"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsDscp"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsTTL"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsCompletionData"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsCompletionSummary"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsAbortData"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrResultsHopCount"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrHopsTgtAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrHopsTgtAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrHopsRtt"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrHopsIngressDscp"),
        ("SLA-MONITOR-MIB", "slaMonitorNtrHopsEgressDscp"))
)
if mibBuilder.loadTexts:
    slaMonitorAgentNtrTestGroup.setStatus("current")

slaMonitorAgentRtpTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 2, 3)
)
slaMonitorAgentRtpTestGroup.setObjects(
      *(("SLA-MONITOR-MIB", "slaMonitorRtpCtrlTargetAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlTargetAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlDscp"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlTestPackets"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlSyncPackets"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlPeriod"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlAdminStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlLabel"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlStorageType"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpCtrlRowStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsOperStatus"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsSrcAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsSrcAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsDstAddressType"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsDstAddress"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsSrcPort"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsDstPort"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsDscp"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsAverageDelay"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsMedianDelay"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsPacketLoss"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsOutOfOrderArrivals"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsJitterQuartile0"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsJitterQuartile1"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsJitterQuartile2"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsJitterQuartile3"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsJitterQuartile4"),
        ("SLA-MONITOR-MIB", "slaMonitorRtpResultsAbortData"))
)
if mibBuilder.loadTexts:
    slaMonitorAgentRtpTestGroup.setStatus("current")


# Notification objects

slaMonitorAgentExceptionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 0, 1)
)
if mibBuilder.loadTexts:
    slaMonitorAgentExceptionDetected.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

slaMonitorMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 45, 4, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    slaMonitorMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLA-MONITOR-MIB",
    **{"slaMonitorMib": slaMonitorMib,
       "slaMonitorMibNotifications": slaMonitorMibNotifications,
       "slaMonitorAgentExceptionDetected": slaMonitorAgentExceptionDetected,
       "slaMonitorMibClasses": slaMonitorMibClasses,
       "slaMonitorAgtClasses": slaMonitorAgtClasses,
       "slaMonitorAgentStatus": slaMonitorAgentStatus,
       "slaMonitorAgentAddressType": slaMonitorAgentAddressType,
       "slaMonitorAgentAddress": slaMonitorAgentAddress,
       "slaMonitorAgentPort": slaMonitorAgentPort,
       "slaMonitorAgentRegisteredWithServer": slaMonitorAgentRegisteredWithServer,
       "slaMonitorAgentRegisteredServerAddrType": slaMonitorAgentRegisteredServerAddrType,
       "slaMonitorAgentRegisteredServerAddr": slaMonitorAgentRegisteredServerAddr,
       "slaMonitorAgentRegisteredServerPort": slaMonitorAgentRegisteredServerPort,
       "slaMonitorAgentRegistrationTime": slaMonitorAgentRegistrationTime,
       "slaMonitorAgentCliAvailable": slaMonitorAgentCliAvailable,
       "slaMonitorAgentCliTimeout": slaMonitorAgentCliTimeout,
       "slaMonitorAgentCliTimeoutMode": slaMonitorAgentCliTimeoutMode,
       "slaMonitorAgentSupportedApps": slaMonitorAgentSupportedApps,
       "slaMonitorAgentConfiguredAgentAddrType": slaMonitorAgentConfiguredAgentAddrType,
       "slaMonitorAgentConfiguredAgentAddr": slaMonitorAgentConfiguredAgentAddr,
       "slaMonitorAgentConfiguredAgentPort": slaMonitorAgentConfiguredAgentPort,
       "slaMonitorAgentConfiguredServerAddrType": slaMonitorAgentConfiguredServerAddrType,
       "slaMonitorAgentConfiguredServerAddr": slaMonitorAgentConfiguredServerAddr,
       "slaMonitorAgentConfiguredServerPort": slaMonitorAgentConfiguredServerPort,
       "slaMonitorAgentConfiguredAltServerAddrType": slaMonitorAgentConfiguredAltServerAddrType,
       "slaMonitorAgentConfiguredAltServerAddr": slaMonitorAgentConfiguredAltServerAddr,
       "slaMonitorAgentConfiguredAltServerPort": slaMonitorAgentConfiguredAltServerPort,
       "slaMonitorAgentToAgentPort": slaMonitorAgentToAgentPort,
       "slaMonitorAgentConfiguredAgentToAgentPort": slaMonitorAgentConfiguredAgentToAgentPort,
       "slaMonitorAgentEncryptionSupport": slaMonitorAgentEncryptionSupport,
       "slaMonitorAgentConfiguredAgentVrfName": slaMonitorAgentConfiguredAgentVrfName,
       "slaMonitorAgentSlaParameter": slaMonitorAgentSlaParameter,
       "slaMonitorAgentCertFileInstallAction": slaMonitorAgentCertFileInstallAction,
       "slaMonitorAgentCertFile": slaMonitorAgentCertFile,
       "slaMonitorAgentServerBypass": slaMonitorAgentServerBypass,
       "slaMonitorAgentRefuseServerTests": slaMonitorAgentRefuseServerTests,
       "slaMonitorAgtTestClasses": slaMonitorAgtTestClasses,
       "slaMonitorNtrCtrlTable": slaMonitorNtrCtrlTable,
       "slaMonitorNtrCtrlEntry": slaMonitorNtrCtrlEntry,
       "slaMonitorNtrCtrlOwnerId": slaMonitorNtrCtrlOwnerId,
       "slaMonitorNtrCtrlTestName": slaMonitorNtrCtrlTestName,
       "slaMonitorNtrCtrlTargetAddressType": slaMonitorNtrCtrlTargetAddressType,
       "slaMonitorNtrCtrlTargetAddress": slaMonitorNtrCtrlTargetAddress,
       "slaMonitorNtrCtrlDscp": slaMonitorNtrCtrlDscp,
       "slaMonitorNtrCtrlAttempts": slaMonitorNtrCtrlAttempts,
       "slaMonitorNtrCtrlPeriod": slaMonitorNtrCtrlPeriod,
       "slaMonitorNtrCtrlAdminStatus": slaMonitorNtrCtrlAdminStatus,
       "slaMonitorNtrCtrlLabel": slaMonitorNtrCtrlLabel,
       "slaMonitorNtrCtrlStorageType": slaMonitorNtrCtrlStorageType,
       "slaMonitorNtrCtrlRowStatus": slaMonitorNtrCtrlRowStatus,
       "slaMonitorNtrResultsTable": slaMonitorNtrResultsTable,
       "slaMonitorNtrResultsEntry": slaMonitorNtrResultsEntry,
       "slaMonitorNtrResultsOperStatus": slaMonitorNtrResultsOperStatus,
       "slaMonitorNtrResultsSrcAddressType": slaMonitorNtrResultsSrcAddressType,
       "slaMonitorNtrResultsSrcAddress": slaMonitorNtrResultsSrcAddress,
       "slaMonitorNtrResultsDstAddressType": slaMonitorNtrResultsDstAddressType,
       "slaMonitorNtrResultsDstAddress": slaMonitorNtrResultsDstAddress,
       "slaMonitorNtrResultsSrcPort": slaMonitorNtrResultsSrcPort,
       "slaMonitorNtrResultsDstPort": slaMonitorNtrResultsDstPort,
       "slaMonitorNtrResultsDscp": slaMonitorNtrResultsDscp,
       "slaMonitorNtrResultsTTL": slaMonitorNtrResultsTTL,
       "slaMonitorNtrResultsCompletionData": slaMonitorNtrResultsCompletionData,
       "slaMonitorNtrResultsCompletionSummary": slaMonitorNtrResultsCompletionSummary,
       "slaMonitorNtrResultsAbortData": slaMonitorNtrResultsAbortData,
       "slaMonitorNtrResultsHopCount": slaMonitorNtrResultsHopCount,
       "slaMonitorNtrHopsTable": slaMonitorNtrHopsTable,
       "slaMonitorNtrHopsEntry": slaMonitorNtrHopsEntry,
       "slaMonitorNtrHopsHopIndex": slaMonitorNtrHopsHopIndex,
       "slaMonitorNtrHopsTgtAddressType": slaMonitorNtrHopsTgtAddressType,
       "slaMonitorNtrHopsTgtAddress": slaMonitorNtrHopsTgtAddress,
       "slaMonitorNtrHopsRtt": slaMonitorNtrHopsRtt,
       "slaMonitorNtrHopsIngressDscp": slaMonitorNtrHopsIngressDscp,
       "slaMonitorNtrHopsEgressDscp": slaMonitorNtrHopsEgressDscp,
       "slaMonitorRtpCtrlTable": slaMonitorRtpCtrlTable,
       "slaMonitorRtpCtrlEntry": slaMonitorRtpCtrlEntry,
       "slaMonitorRtpCtrlOwnerId": slaMonitorRtpCtrlOwnerId,
       "slaMonitorRtpCtrlTestName": slaMonitorRtpCtrlTestName,
       "slaMonitorRtpCtrlTargetAddressType": slaMonitorRtpCtrlTargetAddressType,
       "slaMonitorRtpCtrlTargetAddress": slaMonitorRtpCtrlTargetAddress,
       "slaMonitorRtpCtrlDscp": slaMonitorRtpCtrlDscp,
       "slaMonitorRtpCtrlTestPackets": slaMonitorRtpCtrlTestPackets,
       "slaMonitorRtpCtrlSyncPackets": slaMonitorRtpCtrlSyncPackets,
       "slaMonitorRtpCtrlPeriod": slaMonitorRtpCtrlPeriod,
       "slaMonitorRtpCtrlAdminStatus": slaMonitorRtpCtrlAdminStatus,
       "slaMonitorRtpCtrlLabel": slaMonitorRtpCtrlLabel,
       "slaMonitorRtpCtrlStorageType": slaMonitorRtpCtrlStorageType,
       "slaMonitorRtpCtrlRowStatus": slaMonitorRtpCtrlRowStatus,
       "slaMonitorRtpResultsTable": slaMonitorRtpResultsTable,
       "slaMonitorRtpResultsEntry": slaMonitorRtpResultsEntry,
       "slaMonitorRtpResultsOperStatus": slaMonitorRtpResultsOperStatus,
       "slaMonitorRtpResultsSrcAddressType": slaMonitorRtpResultsSrcAddressType,
       "slaMonitorRtpResultsSrcAddress": slaMonitorRtpResultsSrcAddress,
       "slaMonitorRtpResultsDstAddressType": slaMonitorRtpResultsDstAddressType,
       "slaMonitorRtpResultsDstAddress": slaMonitorRtpResultsDstAddress,
       "slaMonitorRtpResultsSrcPort": slaMonitorRtpResultsSrcPort,
       "slaMonitorRtpResultsDstPort": slaMonitorRtpResultsDstPort,
       "slaMonitorRtpResultsDscp": slaMonitorRtpResultsDscp,
       "slaMonitorRtpResultsAverageDelay": slaMonitorRtpResultsAverageDelay,
       "slaMonitorRtpResultsMedianDelay": slaMonitorRtpResultsMedianDelay,
       "slaMonitorRtpResultsPacketLoss": slaMonitorRtpResultsPacketLoss,
       "slaMonitorRtpResultsOutOfOrderArrivals": slaMonitorRtpResultsOutOfOrderArrivals,
       "slaMonitorRtpResultsJitterQuartile0": slaMonitorRtpResultsJitterQuartile0,
       "slaMonitorRtpResultsJitterQuartile1": slaMonitorRtpResultsJitterQuartile1,
       "slaMonitorRtpResultsJitterQuartile2": slaMonitorRtpResultsJitterQuartile2,
       "slaMonitorRtpResultsJitterQuartile3": slaMonitorRtpResultsJitterQuartile3,
       "slaMonitorRtpResultsJitterQuartile4": slaMonitorRtpResultsJitterQuartile4,
       "slaMonitorRtpResultsAbortData": slaMonitorRtpResultsAbortData,
       "slaMonitorMibConformance": slaMonitorMibConformance,
       "slaMonitorMibCompliances": slaMonitorMibCompliances,
       "slaMonitorMibCompliance": slaMonitorMibCompliance,
       "slaMonitorMibGroups": slaMonitorMibGroups,
       "slaMonitorAgentConfigGroup": slaMonitorAgentConfigGroup,
       "slaMonitorAgentNtrTestGroup": slaMonitorAgentNtrTestGroup,
       "slaMonitorAgentRtpTestGroup": slaMonitorAgentRtpTestGroup}
)
