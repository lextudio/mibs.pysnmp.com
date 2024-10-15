# SNMP MIB module (PKTC-IETF-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-IETF-MTA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:56 2024
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

(docsDevSoftwareGroupV2,) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevSoftwareGroupV2")

(DocsX509ASN1DEREncodedCertificate,
 docsBpi2CodeDownloadGroup) = mibBuilder.importSymbols(
    "DOCS-IETF-BPI2-MIB",
    "DocsX509ASN1DEREncodedCertificate",
    "docsBpi2CodeDownloadGroup")

(ifPhysAddress,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifPhysAddress")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(sysDescr,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr")

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
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(LongUtf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "LongUtf8String")


# MODULE-IDENTITY

pktcIetfMtaMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 140)
)
pktcIetfMtaMib.setRevisions(
        ("2006-09-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcMtaDevProvEncryptAlg(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aes128CbcMode", 3),
          ("aes256CbcMode", 4),
          ("des64CbcMode", 1),
          ("none", 0),
          ("t3Des192CbcMode", 2))
    )



# MIB Managed Objects in the order of their OIDs

_PktcMtaNotification_ObjectIdentity = ObjectIdentity
pktcMtaNotification = _PktcMtaNotification_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 0)
)
_PktcMtaMibObjects_ObjectIdentity = ObjectIdentity
pktcMtaMibObjects = _PktcMtaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1)
)
_PktcMtaDevBase_ObjectIdentity = ObjectIdentity
pktcMtaDevBase = _PktcMtaDevBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1, 1)
)
_PktcMtaDevResetNow_Type = TruthValue
_PktcMtaDevResetNow_Object = MibScalar
pktcMtaDevResetNow = _PktcMtaDevResetNow_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 1),
    _PktcMtaDevResetNow_Type()
)
pktcMtaDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevResetNow.setStatus("current")
_PktcMtaDevSerialNumber_Type = SnmpAdminString
_PktcMtaDevSerialNumber_Object = MibScalar
pktcMtaDevSerialNumber = _PktcMtaDevSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 2),
    _PktcMtaDevSerialNumber_Type()
)
pktcMtaDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSerialNumber.setStatus("current")
_PktcMtaDevSwCurrentVers_Type = SnmpAdminString
_PktcMtaDevSwCurrentVers_Object = MibScalar
pktcMtaDevSwCurrentVers = _PktcMtaDevSwCurrentVers_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 3),
    _PktcMtaDevSwCurrentVers_Type()
)
pktcMtaDevSwCurrentVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSwCurrentVers.setStatus("current")
_PktcMtaDevFQDN_Type = SnmpAdminString
_PktcMtaDevFQDN_Object = MibScalar
pktcMtaDevFQDN = _PktcMtaDevFQDN_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 4),
    _PktcMtaDevFQDN_Type()
)
pktcMtaDevFQDN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevFQDN.setStatus("current")


class _PktcMtaDevEndPntCount_Type(Unsigned32):
    """Custom type pktcMtaDevEndPntCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcMtaDevEndPntCount_Type.__name__ = "Unsigned32"
_PktcMtaDevEndPntCount_Object = MibScalar
pktcMtaDevEndPntCount = _PktcMtaDevEndPntCount_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 5),
    _PktcMtaDevEndPntCount_Type()
)
pktcMtaDevEndPntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEndPntCount.setStatus("current")
_PktcMtaDevEnabled_Type = TruthValue
_PktcMtaDevEnabled_Object = MibScalar
pktcMtaDevEnabled = _PktcMtaDevEnabled_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 6),
    _PktcMtaDevEnabled_Type()
)
pktcMtaDevEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEnabled.setStatus("current")
_PktcMtaDevTypeIdentifier_Type = SnmpAdminString
_PktcMtaDevTypeIdentifier_Object = MibScalar
pktcMtaDevTypeIdentifier = _PktcMtaDevTypeIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 7),
    _PktcMtaDevTypeIdentifier_Type()
)
pktcMtaDevTypeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevTypeIdentifier.setStatus("current")


class _PktcMtaDevProvisioningState_Type(Integer32):
    """Custom type pktcMtaDevProvisioningState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("failConfigFileError", 3),
          ("failureInternalError", 6),
          ("failureOtherReason", 7),
          ("inProgress", 2),
          ("pass", 1),
          ("passWithIncompleteParsing", 5),
          ("passWithWarnings", 4))
    )


_PktcMtaDevProvisioningState_Type.__name__ = "Integer32"
_PktcMtaDevProvisioningState_Object = MibScalar
pktcMtaDevProvisioningState = _PktcMtaDevProvisioningState_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 8),
    _PktcMtaDevProvisioningState_Type()
)
pktcMtaDevProvisioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningState.setStatus("current")
_PktcMtaDevHttpAccess_Type = TruthValue
_PktcMtaDevHttpAccess_Object = MibScalar
pktcMtaDevHttpAccess = _PktcMtaDevHttpAccess_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 9),
    _PktcMtaDevHttpAccess_Type()
)
pktcMtaDevHttpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevHttpAccess.setStatus("current")


class _PktcMtaDevProvisioningTimer_Type(Unsigned32):
    """Custom type pktcMtaDevProvisioningTimer based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_PktcMtaDevProvisioningTimer_Type.__name__ = "Unsigned32"
_PktcMtaDevProvisioningTimer_Object = MibScalar
pktcMtaDevProvisioningTimer = _PktcMtaDevProvisioningTimer_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 10),
    _PktcMtaDevProvisioningTimer_Type()
)
pktcMtaDevProvisioningTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningTimer.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningTimer.setUnits("minutes")
_PktcMtaDevProvisioningCounter_Type = Counter32
_PktcMtaDevProvisioningCounter_Object = MibScalar
pktcMtaDevProvisioningCounter = _PktcMtaDevProvisioningCounter_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 11),
    _PktcMtaDevProvisioningCounter_Type()
)
pktcMtaDevProvisioningCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningCounter.setStatus("current")
_PktcMtaDevErrorOidsTable_Object = MibTable
pktcMtaDevErrorOidsTable = _PktcMtaDevErrorOidsTable_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12)
)
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidsTable.setStatus("current")
_PktcMtaDevErrorOidsEntry_Object = MibTableRow
pktcMtaDevErrorOidsEntry = _PktcMtaDevErrorOidsEntry_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12, 1)
)
pktcMtaDevErrorOidsEntry.setIndexNames(
    (0, "PKTC-IETF-MTA-MIB", "pktcMtaDevErrorOidIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidsEntry.setStatus("current")


class _PktcMtaDevErrorOidIndex_Type(Unsigned32):
    """Custom type pktcMtaDevErrorOidIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PktcMtaDevErrorOidIndex_Type.__name__ = "Unsigned32"
_PktcMtaDevErrorOidIndex_Object = MibTableColumn
pktcMtaDevErrorOidIndex = _PktcMtaDevErrorOidIndex_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12, 1, 1),
    _PktcMtaDevErrorOidIndex_Type()
)
pktcMtaDevErrorOidIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevErrorOidIndex.setStatus("current")
_PktcMtaDevErrorOid_Type = SnmpAdminString
_PktcMtaDevErrorOid_Object = MibTableColumn
pktcMtaDevErrorOid = _PktcMtaDevErrorOid_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12, 1, 2),
    _PktcMtaDevErrorOid_Type()
)
pktcMtaDevErrorOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorOid.setStatus("current")
_PktcMtaDevErrorValue_Type = SnmpAdminString
_PktcMtaDevErrorValue_Object = MibTableColumn
pktcMtaDevErrorValue = _PktcMtaDevErrorValue_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12, 1, 3),
    _PktcMtaDevErrorValue_Type()
)
pktcMtaDevErrorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorValue.setStatus("current")
_PktcMtaDevErrorReason_Type = SnmpAdminString
_PktcMtaDevErrorReason_Object = MibTableColumn
pktcMtaDevErrorReason = _PktcMtaDevErrorReason_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 1, 12, 1, 4),
    _PktcMtaDevErrorReason_Type()
)
pktcMtaDevErrorReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevErrorReason.setStatus("current")
_PktcMtaDevServer_ObjectIdentity = ObjectIdentity
pktcMtaDevServer = _PktcMtaDevServer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1, 2)
)


class _PktcMtaDevDhcpServerAddressType_Type(InetAddressType):
    """Custom type pktcMtaDevDhcpServerAddressType based on InetAddressType"""


_PktcMtaDevDhcpServerAddressType_Object = MibScalar
pktcMtaDevDhcpServerAddressType = _PktcMtaDevDhcpServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 1),
    _PktcMtaDevDhcpServerAddressType_Type()
)
pktcMtaDevDhcpServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevDhcpServerAddressType.setStatus("current")
_PktcMtaDevServerDhcp1_Type = InetAddress
_PktcMtaDevServerDhcp1_Object = MibScalar
pktcMtaDevServerDhcp1 = _PktcMtaDevServerDhcp1_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 2),
    _PktcMtaDevServerDhcp1_Type()
)
pktcMtaDevServerDhcp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp1.setStatus("current")
_PktcMtaDevServerDhcp2_Type = InetAddress
_PktcMtaDevServerDhcp2_Object = MibScalar
pktcMtaDevServerDhcp2 = _PktcMtaDevServerDhcp2_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 3),
    _PktcMtaDevServerDhcp2_Type()
)
pktcMtaDevServerDhcp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp2.setStatus("current")


class _PktcMtaDevDnsServerAddressType_Type(InetAddressType):
    """Custom type pktcMtaDevDnsServerAddressType based on InetAddressType"""


_PktcMtaDevDnsServerAddressType_Object = MibScalar
pktcMtaDevDnsServerAddressType = _PktcMtaDevDnsServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 4),
    _PktcMtaDevDnsServerAddressType_Type()
)
pktcMtaDevDnsServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevDnsServerAddressType.setStatus("current")
_PktcMtaDevServerDns1_Type = InetAddress
_PktcMtaDevServerDns1_Object = MibScalar
pktcMtaDevServerDns1 = _PktcMtaDevServerDns1_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 5),
    _PktcMtaDevServerDns1_Type()
)
pktcMtaDevServerDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns1.setStatus("current")
_PktcMtaDevServerDns2_Type = InetAddress
_PktcMtaDevServerDns2_Object = MibScalar
pktcMtaDevServerDns2 = _PktcMtaDevServerDns2_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 6),
    _PktcMtaDevServerDns2_Type()
)
pktcMtaDevServerDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns2.setStatus("current")


class _PktcMtaDevTimeServerAddressType_Type(InetAddressType):
    """Custom type pktcMtaDevTimeServerAddressType based on InetAddressType"""


_PktcMtaDevTimeServerAddressType_Object = MibScalar
pktcMtaDevTimeServerAddressType = _PktcMtaDevTimeServerAddressType_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 7),
    _PktcMtaDevTimeServerAddressType_Type()
)
pktcMtaDevTimeServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevTimeServerAddressType.setStatus("current")
_PktcMtaDevTimeServer_Type = InetAddress
_PktcMtaDevTimeServer_Object = MibScalar
pktcMtaDevTimeServer = _PktcMtaDevTimeServer_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 8),
    _PktcMtaDevTimeServer_Type()
)
pktcMtaDevTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevTimeServer.setStatus("current")
_PktcMtaDevConfigFile_Type = SnmpAdminString
_PktcMtaDevConfigFile_Object = MibScalar
pktcMtaDevConfigFile = _PktcMtaDevConfigFile_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 9),
    _PktcMtaDevConfigFile_Type()
)
pktcMtaDevConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevConfigFile.setStatus("current")
_PktcMtaDevSnmpEntity_Type = SnmpAdminString
_PktcMtaDevSnmpEntity_Object = MibScalar
pktcMtaDevSnmpEntity = _PktcMtaDevSnmpEntity_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 10),
    _PktcMtaDevSnmpEntity_Type()
)
pktcMtaDevSnmpEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSnmpEntity.setStatus("current")


class _PktcMtaDevProvConfigHash_Type(OctetString):
    """Custom type pktcMtaDevProvConfigHash based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_PktcMtaDevProvConfigHash_Type.__name__ = "OctetString"
_PktcMtaDevProvConfigHash_Object = MibScalar
pktcMtaDevProvConfigHash = _PktcMtaDevProvConfigHash_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 11),
    _PktcMtaDevProvConfigHash_Type()
)
pktcMtaDevProvConfigHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvConfigHash.setStatus("current")


class _PktcMtaDevProvConfigKey_Type(OctetString):
    """Custom type pktcMtaDevProvConfigKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_PktcMtaDevProvConfigKey_Type.__name__ = "OctetString"
_PktcMtaDevProvConfigKey_Object = MibScalar
pktcMtaDevProvConfigKey = _PktcMtaDevProvConfigKey_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 12),
    _PktcMtaDevProvConfigKey_Type()
)
pktcMtaDevProvConfigKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvConfigKey.setStatus("current")


class _PktcMtaDevProvConfigEncryptAlg_Type(PktcMtaDevProvEncryptAlg):
    """Custom type pktcMtaDevProvConfigEncryptAlg based on PktcMtaDevProvEncryptAlg"""


_PktcMtaDevProvConfigEncryptAlg_Object = MibScalar
pktcMtaDevProvConfigEncryptAlg = _PktcMtaDevProvConfigEncryptAlg_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 13),
    _PktcMtaDevProvConfigEncryptAlg_Type()
)
pktcMtaDevProvConfigEncryptAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvConfigEncryptAlg.setStatus("current")


class _PktcMtaDevProvSolicitedKeyTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevProvSolicitedKeyTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_PktcMtaDevProvSolicitedKeyTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevProvSolicitedKeyTimeout_Object = MibScalar
pktcMtaDevProvSolicitedKeyTimeout = _PktcMtaDevProvSolicitedKeyTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 14),
    _PktcMtaDevProvSolicitedKeyTimeout_Type()
)
pktcMtaDevProvSolicitedKeyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevProvSolicitedKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvSolicitedKeyTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevProvUnsolicitedKeyMaxTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyMaxTimeout = _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 15),
    _PktcMtaDevProvUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevProvUnsolicitedKeyMaxTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyNomTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevProvUnsolicitedKeyNomTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PktcMtaDevProvUnsolicitedKeyNomTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevProvUnsolicitedKeyNomTimeout_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyNomTimeout = _PktcMtaDevProvUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 16),
    _PktcMtaDevProvUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevProvUnsolicitedKeyNomTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyNomTimeout.setUnits("seconds")


class _PktcMtaDevProvUnsolicitedKeyMaxRetries_Type(Unsigned32):
    """Custom type pktcMtaDevProvUnsolicitedKeyMaxRetries based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PktcMtaDevProvUnsolicitedKeyMaxRetries_Type.__name__ = "Unsigned32"
_PktcMtaDevProvUnsolicitedKeyMaxRetries_Object = MibScalar
pktcMtaDevProvUnsolicitedKeyMaxRetries = _PktcMtaDevProvUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 17),
    _PktcMtaDevProvUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevProvUnsolicitedKeyMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvUnsolicitedKeyMaxRetries.setStatus("current")


class _PktcMtaDevProvKerbRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevProvKerbRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevProvKerbRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevProvKerbRealmName_Object = MibScalar
pktcMtaDevProvKerbRealmName = _PktcMtaDevProvKerbRealmName_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 18),
    _PktcMtaDevProvKerbRealmName_Type()
)
pktcMtaDevProvKerbRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvKerbRealmName.setStatus("current")


class _PktcMtaDevProvState_Type(Integer32):
    """Custom type pktcMtaDevProvState based on Integer32"""
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
        *(("operational", 1),
          ("waitingForConfigFile", 4),
          ("waitingForSnmpSetInfo", 2),
          ("waitingForTftpAddrResponse", 3))
    )


_PktcMtaDevProvState_Type.__name__ = "Integer32"
_PktcMtaDevProvState_Object = MibScalar
pktcMtaDevProvState = _PktcMtaDevProvState_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 2, 19),
    _PktcMtaDevProvState_Type()
)
pktcMtaDevProvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvState.setStatus("current")
_PktcMtaDevSecurity_ObjectIdentity = ObjectIdentity
pktcMtaDevSecurity = _PktcMtaDevSecurity_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1, 3)
)
_PktcMtaDevManufacturerCertificate_Type = DocsX509ASN1DEREncodedCertificate
_PktcMtaDevManufacturerCertificate_Object = MibScalar
pktcMtaDevManufacturerCertificate = _PktcMtaDevManufacturerCertificate_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 1),
    _PktcMtaDevManufacturerCertificate_Type()
)
pktcMtaDevManufacturerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevManufacturerCertificate.setStatus("current")
_PktcMtaDevCertificate_Type = DocsX509ASN1DEREncodedCertificate
_PktcMtaDevCertificate_Object = MibScalar
pktcMtaDevCertificate = _PktcMtaDevCertificate_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 2),
    _PktcMtaDevCertificate_Type()
)
pktcMtaDevCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCertificate.setStatus("current")
_PktcMtaDevCorrelationId_Type = Unsigned32
_PktcMtaDevCorrelationId_Object = MibScalar
pktcMtaDevCorrelationId = _PktcMtaDevCorrelationId_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 3),
    _PktcMtaDevCorrelationId_Type()
)
pktcMtaDevCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCorrelationId.setStatus("current")
_PktcMtaDevTelephonyRootCertificate_Type = DocsX509ASN1DEREncodedCertificate
_PktcMtaDevTelephonyRootCertificate_Object = MibScalar
pktcMtaDevTelephonyRootCertificate = _PktcMtaDevTelephonyRootCertificate_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 4),
    _PktcMtaDevTelephonyRootCertificate_Type()
)
pktcMtaDevTelephonyRootCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevTelephonyRootCertificate.setStatus("current")


class _PktcMtaDevRealmAvailSlot_Type(Unsigned32):
    """Custom type pktcMtaDevRealmAvailSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_PktcMtaDevRealmAvailSlot_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmAvailSlot_Object = MibScalar
pktcMtaDevRealmAvailSlot = _PktcMtaDevRealmAvailSlot_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 5),
    _PktcMtaDevRealmAvailSlot_Type()
)
pktcMtaDevRealmAvailSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevRealmAvailSlot.setStatus("current")
_PktcMtaDevRealmTable_Object = MibTable
pktcMtaDevRealmTable = _PktcMtaDevRealmTable_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6)
)
if mibBuilder.loadTexts:
    pktcMtaDevRealmTable.setStatus("current")
_PktcMtaDevRealmEntry_Object = MibTableRow
pktcMtaDevRealmEntry = _PktcMtaDevRealmEntry_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1)
)
pktcMtaDevRealmEntry.setIndexNames(
    (0, "PKTC-IETF-MTA-MIB", "pktcMtaDevRealmIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevRealmEntry.setStatus("current")


class _PktcMtaDevRealmIndex_Type(Unsigned32):
    """Custom type pktcMtaDevRealmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_PktcMtaDevRealmIndex_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmIndex_Object = MibTableColumn
pktcMtaDevRealmIndex = _PktcMtaDevRealmIndex_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 1),
    _PktcMtaDevRealmIndex_Type()
)
pktcMtaDevRealmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevRealmIndex.setStatus("current")


class _PktcMtaDevRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevRealmName_Object = MibTableColumn
pktcMtaDevRealmName = _PktcMtaDevRealmName_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 2),
    _PktcMtaDevRealmName_Type()
)
pktcMtaDevRealmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmName.setStatus("current")


class _PktcMtaDevRealmPkinitGracePeriod_Type(Unsigned32):
    """Custom type pktcMtaDevRealmPkinitGracePeriod based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevRealmPkinitGracePeriod_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmPkinitGracePeriod_Object = MibTableColumn
pktcMtaDevRealmPkinitGracePeriod = _PktcMtaDevRealmPkinitGracePeriod_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 3),
    _PktcMtaDevRealmPkinitGracePeriod_Type()
)
pktcMtaDevRealmPkinitGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmPkinitGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmPkinitGracePeriod.setUnits("minutes")


class _PktcMtaDevRealmTgsGracePeriod_Type(Unsigned32):
    """Custom type pktcMtaDevRealmTgsGracePeriod based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevRealmTgsGracePeriod_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmTgsGracePeriod_Object = MibTableColumn
pktcMtaDevRealmTgsGracePeriod = _PktcMtaDevRealmTgsGracePeriod_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 4),
    _PktcMtaDevRealmTgsGracePeriod_Type()
)
pktcMtaDevRealmTgsGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmTgsGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmTgsGracePeriod.setUnits("minutes")
_PktcMtaDevRealmOrgName_Type = LongUtf8String
_PktcMtaDevRealmOrgName_Object = MibTableColumn
pktcMtaDevRealmOrgName = _PktcMtaDevRealmOrgName_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 5),
    _PktcMtaDevRealmOrgName_Type()
)
pktcMtaDevRealmOrgName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmOrgName.setStatus("current")


class _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyMaxTimeout based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxTimeout = _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 6),
    _PktcMtaDevRealmUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyNomTimeout based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 600000),
    )


_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyNomTimeout = _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 7),
    _PktcMtaDevRealmUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevRealmUnsolicitedKeyNomTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyNomTimeout.setUnits("milliseconds")


class _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type(Unsigned32):
    """Custom type pktcMtaDevRealmUnsolicitedKeyMaxRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type.__name__ = "Unsigned32"
_PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object = MibTableColumn
pktcMtaDevRealmUnsolicitedKeyMaxRetries = _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 8),
    _PktcMtaDevRealmUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevRealmUnsolicitedKeyMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmUnsolicitedKeyMaxRetries.setStatus("current")
_PktcMtaDevRealmStatus_Type = RowStatus
_PktcMtaDevRealmStatus_Object = MibTableColumn
pktcMtaDevRealmStatus = _PktcMtaDevRealmStatus_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 6, 1, 9),
    _PktcMtaDevRealmStatus_Type()
)
pktcMtaDevRealmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevRealmStatus.setStatus("current")


class _PktcMtaDevCmsAvailSlot_Type(Unsigned32):
    """Custom type pktcMtaDevCmsAvailSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_PktcMtaDevCmsAvailSlot_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsAvailSlot_Object = MibScalar
pktcMtaDevCmsAvailSlot = _PktcMtaDevCmsAvailSlot_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 7),
    _PktcMtaDevCmsAvailSlot_Type()
)
pktcMtaDevCmsAvailSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCmsAvailSlot.setStatus("current")
_PktcMtaDevCmsTable_Object = MibTable
pktcMtaDevCmsTable = _PktcMtaDevCmsTable_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8)
)
if mibBuilder.loadTexts:
    pktcMtaDevCmsTable.setStatus("current")
_PktcMtaDevCmsEntry_Object = MibTableRow
pktcMtaDevCmsEntry = _PktcMtaDevCmsEntry_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1)
)
pktcMtaDevCmsEntry.setIndexNames(
    (0, "PKTC-IETF-MTA-MIB", "pktcMtaDevCmsIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevCmsEntry.setStatus("current")


class _PktcMtaDevCmsIndex_Type(Unsigned32):
    """Custom type pktcMtaDevCmsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PktcMtaDevCmsIndex_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsIndex_Object = MibTableColumn
pktcMtaDevCmsIndex = _PktcMtaDevCmsIndex_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 1),
    _PktcMtaDevCmsIndex_Type()
)
pktcMtaDevCmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevCmsIndex.setStatus("current")


class _PktcMtaDevCmsFqdn_Type(SnmpAdminString):
    """Custom type pktcMtaDevCmsFqdn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevCmsFqdn_Type.__name__ = "SnmpAdminString"
_PktcMtaDevCmsFqdn_Object = MibTableColumn
pktcMtaDevCmsFqdn = _PktcMtaDevCmsFqdn_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 2),
    _PktcMtaDevCmsFqdn_Type()
)
pktcMtaDevCmsFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsFqdn.setStatus("current")


class _PktcMtaDevCmsKerbRealmName_Type(SnmpAdminString):
    """Custom type pktcMtaDevCmsKerbRealmName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_PktcMtaDevCmsKerbRealmName_Type.__name__ = "SnmpAdminString"
_PktcMtaDevCmsKerbRealmName_Object = MibTableColumn
pktcMtaDevCmsKerbRealmName = _PktcMtaDevCmsKerbRealmName_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 3),
    _PktcMtaDevCmsKerbRealmName_Type()
)
pktcMtaDevCmsKerbRealmName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsKerbRealmName.setStatus("current")


class _PktcMtaDevCmsMaxClockSkew_Type(Unsigned32):
    """Custom type pktcMtaDevCmsMaxClockSkew based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_PktcMtaDevCmsMaxClockSkew_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsMaxClockSkew_Object = MibTableColumn
pktcMtaDevCmsMaxClockSkew = _PktcMtaDevCmsMaxClockSkew_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 4),
    _PktcMtaDevCmsMaxClockSkew_Type()
)
pktcMtaDevCmsMaxClockSkew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsMaxClockSkew.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsMaxClockSkew.setUnits("seconds")


class _PktcMtaDevCmsSolicitedKeyTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevCmsSolicitedKeyTimeout based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PktcMtaDevCmsSolicitedKeyTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsSolicitedKeyTimeout_Object = MibTableColumn
pktcMtaDevCmsSolicitedKeyTimeout = _PktcMtaDevCmsSolicitedKeyTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 5),
    _PktcMtaDevCmsSolicitedKeyTimeout_Type()
)
pktcMtaDevCmsSolicitedKeyTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsSolicitedKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsSolicitedKeyTimeout.setUnits("milliseconds")


class _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyMaxTimeout based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxTimeout = _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 6),
    _PktcMtaDevCmsUnsolicitedKeyMaxTimeout_Type()
)
pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxTimeout.setUnits("seconds")


class _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type(Unsigned32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyNomTimeout based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 30000),
    )


_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyNomTimeout = _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 7),
    _PktcMtaDevCmsUnsolicitedKeyNomTimeout_Type()
)
pktcMtaDevCmsUnsolicitedKeyNomTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyNomTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyNomTimeout.setUnits("milliseconds")


class _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type(Unsigned32):
    """Custom type pktcMtaDevCmsUnsolicitedKeyMaxRetries based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type.__name__ = "Unsigned32"
_PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object = MibTableColumn
pktcMtaDevCmsUnsolicitedKeyMaxRetries = _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 8),
    _PktcMtaDevCmsUnsolicitedKeyMaxRetries_Type()
)
pktcMtaDevCmsUnsolicitedKeyMaxRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsUnsolicitedKeyMaxRetries.setStatus("current")


class _PktcMtaDevCmsIpsecCtrl_Type(TruthValue):
    """Custom type pktcMtaDevCmsIpsecCtrl based on TruthValue"""


_PktcMtaDevCmsIpsecCtrl_Object = MibTableColumn
pktcMtaDevCmsIpsecCtrl = _PktcMtaDevCmsIpsecCtrl_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 9),
    _PktcMtaDevCmsIpsecCtrl_Type()
)
pktcMtaDevCmsIpsecCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCmsIpsecCtrl.setStatus("current")
_PktcMtaDevCmsStatus_Type = RowStatus
_PktcMtaDevCmsStatus_Object = MibTableColumn
pktcMtaDevCmsStatus = _PktcMtaDevCmsStatus_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 8, 1, 10),
    _PktcMtaDevCmsStatus_Type()
)
pktcMtaDevCmsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevCmsStatus.setStatus("current")


class _PktcMtaDevResetKrbTickets_Type(Bits):
    """Custom type pktcMtaDevResetKrbTickets based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("invalidateAllCmsOnReboot", 1),
          ("invalidateProvOnReboot", 0))
    )

_PktcMtaDevResetKrbTickets_Type.__name__ = "Bits"
_PktcMtaDevResetKrbTickets_Object = MibScalar
pktcMtaDevResetKrbTickets = _PktcMtaDevResetKrbTickets_Object(
    (1, 3, 6, 1, 2, 1, 140, 1, 3, 9),
    _PktcMtaDevResetKrbTickets_Type()
)
pktcMtaDevResetKrbTickets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevResetKrbTickets.setStatus("current")
_PktcMtaDevErrors_ObjectIdentity = ObjectIdentity
pktcMtaDevErrors = _PktcMtaDevErrors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1, 4)
)
_PktcMtaDevErrorsTooManyErrors_ObjectIdentity = ObjectIdentity
pktcMtaDevErrorsTooManyErrors = _PktcMtaDevErrorsTooManyErrors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pktcMtaDevErrorsTooManyErrors.setStatus("current")
_PktcMtaConformance_ObjectIdentity = ObjectIdentity
pktcMtaConformance = _PktcMtaConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 2)
)
_PktcMtaCompliances_ObjectIdentity = ObjectIdentity
pktcMtaCompliances = _PktcMtaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 2, 1)
)
_PktcMtaGroups_ObjectIdentity = ObjectIdentity
pktcMtaGroups = _PktcMtaGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 140, 2, 2)
)

# Managed Objects groups

pktcMtaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 140, 2, 2, 1)
)
pktcMtaGroup.setObjects(
      *(("PKTC-IETF-MTA-MIB", "pktcMtaDevResetNow"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevSerialNumber"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevSwCurrentVers"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevFQDN"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevEndPntCount"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevEnabled"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningCounter"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevErrorOid"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevErrorValue"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevErrorReason"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningState"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevHttpAccess"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCertificate"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevManufacturerCertificate"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevDhcpServerAddressType"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevDnsServerAddressType"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevTimeServerAddressType"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvConfigEncryptAlg"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevServerDhcp1"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevServerDhcp2"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevServerDns1"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevServerDns2"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevTimeServer"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevConfigFile"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevSnmpEntity"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmPkinitGracePeriod"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmTgsGracePeriod"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmAvailSlot"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmName"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmOrgName"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyMaxTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyNomTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmUnsolicitedKeyMaxRetries"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevRealmStatus"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsAvailSlot"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsFqdn"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsKerbRealmName"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyMaxTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyNomTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsUnsolicitedKeyMaxRetries"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsSolicitedKeyTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsMaxClockSkew"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsIpsecCtrl"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCmsStatus"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevResetKrbTickets"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyMaxTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyNomTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvUnsolicitedKeyMaxRetries"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvKerbRealmName"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvSolicitedKeyTimeout"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvConfigHash"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvConfigKey"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvState"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningTimer"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevTelephonyRootCertificate"))
)
if mibBuilder.loadTexts:
    pktcMtaGroup.setStatus("current")


# Notification objects

pktcMtaDevProvisioningEnrollment = NotificationType(
    (1, 3, 6, 1, 2, 1, 140, 0, 1)
)
pktcMtaDevProvisioningEnrollment.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevSwCurrentVers"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("IF-MIB", "ifPhysAddress"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCorrelationId"))
)
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningEnrollment.setStatus(
        "current"
    )

pktcMtaDevProvisioningStatus = NotificationType(
    (1, 3, 6, 1, 2, 1, 140, 0, 2)
)
pktcMtaDevProvisioningStatus.setObjects(
      *(("IF-MIB", "ifPhysAddress"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningState"))
)
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningStatus.setStatus(
        "current"
    )


# Notifications groups

pktcMtaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 140, 2, 2, 2)
)
pktcMtaNotificationGroup.setObjects(
      *(("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningStatus"),
        ("PKTC-IETF-MTA-MIB", "pktcMtaDevProvisioningEnrollment"))
)
if mibBuilder.loadTexts:
    pktcMtaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pktcMtaBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 140, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcMtaBasicCompliance.setStatus(
        "current"
    )

pktcMtaBasicSmtaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 140, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pktcMtaBasicSmtaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-IETF-MTA-MIB",
    **{"PktcMtaDevProvEncryptAlg": PktcMtaDevProvEncryptAlg,
       "pktcIetfMtaMib": pktcIetfMtaMib,
       "pktcMtaNotification": pktcMtaNotification,
       "pktcMtaDevProvisioningEnrollment": pktcMtaDevProvisioningEnrollment,
       "pktcMtaDevProvisioningStatus": pktcMtaDevProvisioningStatus,
       "pktcMtaMibObjects": pktcMtaMibObjects,
       "pktcMtaDevBase": pktcMtaDevBase,
       "pktcMtaDevResetNow": pktcMtaDevResetNow,
       "pktcMtaDevSerialNumber": pktcMtaDevSerialNumber,
       "pktcMtaDevSwCurrentVers": pktcMtaDevSwCurrentVers,
       "pktcMtaDevFQDN": pktcMtaDevFQDN,
       "pktcMtaDevEndPntCount": pktcMtaDevEndPntCount,
       "pktcMtaDevEnabled": pktcMtaDevEnabled,
       "pktcMtaDevTypeIdentifier": pktcMtaDevTypeIdentifier,
       "pktcMtaDevProvisioningState": pktcMtaDevProvisioningState,
       "pktcMtaDevHttpAccess": pktcMtaDevHttpAccess,
       "pktcMtaDevProvisioningTimer": pktcMtaDevProvisioningTimer,
       "pktcMtaDevProvisioningCounter": pktcMtaDevProvisioningCounter,
       "pktcMtaDevErrorOidsTable": pktcMtaDevErrorOidsTable,
       "pktcMtaDevErrorOidsEntry": pktcMtaDevErrorOidsEntry,
       "pktcMtaDevErrorOidIndex": pktcMtaDevErrorOidIndex,
       "pktcMtaDevErrorOid": pktcMtaDevErrorOid,
       "pktcMtaDevErrorValue": pktcMtaDevErrorValue,
       "pktcMtaDevErrorReason": pktcMtaDevErrorReason,
       "pktcMtaDevServer": pktcMtaDevServer,
       "pktcMtaDevDhcpServerAddressType": pktcMtaDevDhcpServerAddressType,
       "pktcMtaDevServerDhcp1": pktcMtaDevServerDhcp1,
       "pktcMtaDevServerDhcp2": pktcMtaDevServerDhcp2,
       "pktcMtaDevDnsServerAddressType": pktcMtaDevDnsServerAddressType,
       "pktcMtaDevServerDns1": pktcMtaDevServerDns1,
       "pktcMtaDevServerDns2": pktcMtaDevServerDns2,
       "pktcMtaDevTimeServerAddressType": pktcMtaDevTimeServerAddressType,
       "pktcMtaDevTimeServer": pktcMtaDevTimeServer,
       "pktcMtaDevConfigFile": pktcMtaDevConfigFile,
       "pktcMtaDevSnmpEntity": pktcMtaDevSnmpEntity,
       "pktcMtaDevProvConfigHash": pktcMtaDevProvConfigHash,
       "pktcMtaDevProvConfigKey": pktcMtaDevProvConfigKey,
       "pktcMtaDevProvConfigEncryptAlg": pktcMtaDevProvConfigEncryptAlg,
       "pktcMtaDevProvSolicitedKeyTimeout": pktcMtaDevProvSolicitedKeyTimeout,
       "pktcMtaDevProvUnsolicitedKeyMaxTimeout": pktcMtaDevProvUnsolicitedKeyMaxTimeout,
       "pktcMtaDevProvUnsolicitedKeyNomTimeout": pktcMtaDevProvUnsolicitedKeyNomTimeout,
       "pktcMtaDevProvUnsolicitedKeyMaxRetries": pktcMtaDevProvUnsolicitedKeyMaxRetries,
       "pktcMtaDevProvKerbRealmName": pktcMtaDevProvKerbRealmName,
       "pktcMtaDevProvState": pktcMtaDevProvState,
       "pktcMtaDevSecurity": pktcMtaDevSecurity,
       "pktcMtaDevManufacturerCertificate": pktcMtaDevManufacturerCertificate,
       "pktcMtaDevCertificate": pktcMtaDevCertificate,
       "pktcMtaDevCorrelationId": pktcMtaDevCorrelationId,
       "pktcMtaDevTelephonyRootCertificate": pktcMtaDevTelephonyRootCertificate,
       "pktcMtaDevRealmAvailSlot": pktcMtaDevRealmAvailSlot,
       "pktcMtaDevRealmTable": pktcMtaDevRealmTable,
       "pktcMtaDevRealmEntry": pktcMtaDevRealmEntry,
       "pktcMtaDevRealmIndex": pktcMtaDevRealmIndex,
       "pktcMtaDevRealmName": pktcMtaDevRealmName,
       "pktcMtaDevRealmPkinitGracePeriod": pktcMtaDevRealmPkinitGracePeriod,
       "pktcMtaDevRealmTgsGracePeriod": pktcMtaDevRealmTgsGracePeriod,
       "pktcMtaDevRealmOrgName": pktcMtaDevRealmOrgName,
       "pktcMtaDevRealmUnsolicitedKeyMaxTimeout": pktcMtaDevRealmUnsolicitedKeyMaxTimeout,
       "pktcMtaDevRealmUnsolicitedKeyNomTimeout": pktcMtaDevRealmUnsolicitedKeyNomTimeout,
       "pktcMtaDevRealmUnsolicitedKeyMaxRetries": pktcMtaDevRealmUnsolicitedKeyMaxRetries,
       "pktcMtaDevRealmStatus": pktcMtaDevRealmStatus,
       "pktcMtaDevCmsAvailSlot": pktcMtaDevCmsAvailSlot,
       "pktcMtaDevCmsTable": pktcMtaDevCmsTable,
       "pktcMtaDevCmsEntry": pktcMtaDevCmsEntry,
       "pktcMtaDevCmsIndex": pktcMtaDevCmsIndex,
       "pktcMtaDevCmsFqdn": pktcMtaDevCmsFqdn,
       "pktcMtaDevCmsKerbRealmName": pktcMtaDevCmsKerbRealmName,
       "pktcMtaDevCmsMaxClockSkew": pktcMtaDevCmsMaxClockSkew,
       "pktcMtaDevCmsSolicitedKeyTimeout": pktcMtaDevCmsSolicitedKeyTimeout,
       "pktcMtaDevCmsUnsolicitedKeyMaxTimeout": pktcMtaDevCmsUnsolicitedKeyMaxTimeout,
       "pktcMtaDevCmsUnsolicitedKeyNomTimeout": pktcMtaDevCmsUnsolicitedKeyNomTimeout,
       "pktcMtaDevCmsUnsolicitedKeyMaxRetries": pktcMtaDevCmsUnsolicitedKeyMaxRetries,
       "pktcMtaDevCmsIpsecCtrl": pktcMtaDevCmsIpsecCtrl,
       "pktcMtaDevCmsStatus": pktcMtaDevCmsStatus,
       "pktcMtaDevResetKrbTickets": pktcMtaDevResetKrbTickets,
       "pktcMtaDevErrors": pktcMtaDevErrors,
       "pktcMtaDevErrorsTooManyErrors": pktcMtaDevErrorsTooManyErrors,
       "pktcMtaConformance": pktcMtaConformance,
       "pktcMtaCompliances": pktcMtaCompliances,
       "pktcMtaBasicCompliance": pktcMtaBasicCompliance,
       "pktcMtaBasicSmtaCompliance": pktcMtaBasicSmtaCompliance,
       "pktcMtaGroups": pktcMtaGroups,
       "pktcMtaGroup": pktcMtaGroup,
       "pktcMtaNotificationGroup": pktcMtaNotificationGroup}
)
