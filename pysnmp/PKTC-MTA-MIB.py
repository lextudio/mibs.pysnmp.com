# SNMP MIB module (PKTC-MTA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-MTA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:58 2024
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

(clabProjPacketCable,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjPacketCable")

(docsDevSwCurrentVers,) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevSwCurrentVers")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcMtaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class X509Certificate(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4096),
    )



# MIB Managed Objects in the order of their OIDs

_PktcMtaMibObjects_ObjectIdentity = ObjectIdentity
pktcMtaMibObjects = _PktcMtaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1)
)
_PktcMtaDevBase_ObjectIdentity = ObjectIdentity
pktcMtaDevBase = _PktcMtaDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1)
)
_PktcMtaDevResetNow_Type = TruthValue
_PktcMtaDevResetNow_Object = MibScalar
pktcMtaDevResetNow = _PktcMtaDevResetNow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 1),
    _PktcMtaDevResetNow_Type()
)
pktcMtaDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevResetNow.setStatus("current")


class _PktcMtaDevSerialNumber_Type(DisplayString):
    """Custom type pktcMtaDevSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PktcMtaDevSerialNumber_Type.__name__ = "DisplayString"
_PktcMtaDevSerialNumber_Object = MibScalar
pktcMtaDevSerialNumber = _PktcMtaDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 2),
    _PktcMtaDevSerialNumber_Type()
)
pktcMtaDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSerialNumber.setStatus("current")


class _PktcMtaDevHardwareVersion_Type(DisplayString):
    """Custom type pktcMtaDevHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_PktcMtaDevHardwareVersion_Type.__name__ = "DisplayString"
_PktcMtaDevHardwareVersion_Object = MibScalar
pktcMtaDevHardwareVersion = _PktcMtaDevHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 3),
    _PktcMtaDevHardwareVersion_Type()
)
pktcMtaDevHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevHardwareVersion.setStatus("current")
_PktcMtaDevMacAddress_Type = OctetString
_PktcMtaDevMacAddress_Object = MibScalar
pktcMtaDevMacAddress = _PktcMtaDevMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 4),
    _PktcMtaDevMacAddress_Type()
)
pktcMtaDevMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevMacAddress.setStatus("current")
_PktcMtaDevFQDN_Type = DisplayString
_PktcMtaDevFQDN_Object = MibScalar
pktcMtaDevFQDN = _PktcMtaDevFQDN_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 5),
    _PktcMtaDevFQDN_Type()
)
pktcMtaDevFQDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevFQDN.setStatus("current")


class _PktcMtaDevEndPntCount_Type(Integer32):
    """Custom type pktcMtaDevEndPntCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PktcMtaDevEndPntCount_Type.__name__ = "Integer32"
_PktcMtaDevEndPntCount_Object = MibScalar
pktcMtaDevEndPntCount = _PktcMtaDevEndPntCount_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 6),
    _PktcMtaDevEndPntCount_Type()
)
pktcMtaDevEndPntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEndPntCount.setStatus("current")
_PktcMtaDevEnabled_Type = TruthValue
_PktcMtaDevEnabled_Object = MibScalar
pktcMtaDevEnabled = _PktcMtaDevEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 7),
    _PktcMtaDevEnabled_Type()
)
pktcMtaDevEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEnabled.setStatus("current")
_PktcMtaDevTypeIdentifier_Type = DisplayString
_PktcMtaDevTypeIdentifier_Object = MibScalar
pktcMtaDevTypeIdentifier = _PktcMtaDevTypeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 8),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("inProgress", 2),
          ("pass", 1))
    )


_PktcMtaDevProvisioningState_Type.__name__ = "Integer32"
_PktcMtaDevProvisioningState_Object = MibScalar
pktcMtaDevProvisioningState = _PktcMtaDevProvisioningState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 9),
    _PktcMtaDevProvisioningState_Type()
)
pktcMtaDevProvisioningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevProvisioningState.setStatus("current")
_PktcMtaDevHttpAccess_Type = TruthValue
_PktcMtaDevHttpAccess_Object = MibScalar
pktcMtaDevHttpAccess = _PktcMtaDevHttpAccess_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 1, 10),
    _PktcMtaDevHttpAccess_Type()
)
pktcMtaDevHttpAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevHttpAccess.setStatus("current")
_PktcMtaDevServer_ObjectIdentity = ObjectIdentity
pktcMtaDevServer = _PktcMtaDevServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2)
)


class _PktcMtaDevServerBootState_Type(Integer32):
    """Custom type pktcMtaDevServerBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("operational", 1),
          ("other", 7),
          ("refusedByCmts", 6),
          ("unknown", 8),
          ("waitingForConfig", 5),
          ("waitingForDhcpOffer", 3),
          ("waitingForDhcpResponse", 4))
    )


_PktcMtaDevServerBootState_Type.__name__ = "Integer32"
_PktcMtaDevServerBootState_Object = MibScalar
pktcMtaDevServerBootState = _PktcMtaDevServerBootState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 1),
    _PktcMtaDevServerBootState_Type()
)
pktcMtaDevServerBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevServerBootState.setStatus("current")
_PktcMtaDevServerDhcp_Type = DisplayString
_PktcMtaDevServerDhcp_Object = MibScalar
pktcMtaDevServerDhcp = _PktcMtaDevServerDhcp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 2),
    _PktcMtaDevServerDhcp_Type()
)
pktcMtaDevServerDhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDhcp.setStatus("current")
_PktcMtaDevServerDns1_Type = DisplayString
_PktcMtaDevServerDns1_Object = MibScalar
pktcMtaDevServerDns1 = _PktcMtaDevServerDns1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 3),
    _PktcMtaDevServerDns1_Type()
)
pktcMtaDevServerDns1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns1.setStatus("current")
_PktcMtaDevServerDns2_Type = DisplayString
_PktcMtaDevServerDns2_Object = MibScalar
pktcMtaDevServerDns2 = _PktcMtaDevServerDns2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 4),
    _PktcMtaDevServerDns2_Type()
)
pktcMtaDevServerDns2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServerDns2.setStatus("current")
_PktcMtaDevConfigFile_Type = DisplayString
_PktcMtaDevConfigFile_Object = MibScalar
pktcMtaDevConfigFile = _PktcMtaDevConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 5),
    _PktcMtaDevConfigFile_Type()
)
pktcMtaDevConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevConfigFile.setStatus("current")
_PktcMtaDevSnmpEntity_Type = DisplayString
_PktcMtaDevSnmpEntity_Object = MibScalar
pktcMtaDevSnmpEntity = _PktcMtaDevSnmpEntity_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 2, 6),
    _PktcMtaDevSnmpEntity_Type()
)
pktcMtaDevSnmpEntity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevSnmpEntity.setStatus("current")
_PktcMtaDevSecurity_ObjectIdentity = ObjectIdentity
pktcMtaDevSecurity = _PktcMtaDevSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3)
)
_PktcMtaDevManufacturerCertificate_Type = X509Certificate
_PktcMtaDevManufacturerCertificate_Object = MibScalar
pktcMtaDevManufacturerCertificate = _PktcMtaDevManufacturerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 1),
    _PktcMtaDevManufacturerCertificate_Type()
)
pktcMtaDevManufacturerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevManufacturerCertificate.setStatus("current")
_PktcMtaDevCertificate_Type = X509Certificate
_PktcMtaDevCertificate_Object = MibScalar
pktcMtaDevCertificate = _PktcMtaDevCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 2),
    _PktcMtaDevCertificate_Type()
)
pktcMtaDevCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCertificate.setStatus("current")


class _PktcMtaDevSignature_Type(OctetString):
    """Custom type pktcMtaDevSignature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_PktcMtaDevSignature_Type.__name__ = "OctetString"
_PktcMtaDevSignature_Object = MibScalar
pktcMtaDevSignature = _PktcMtaDevSignature_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 3),
    _PktcMtaDevSignature_Type()
)
pktcMtaDevSignature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevSignature.setStatus("current")
_PktcMtaDevCorrelationId_Type = Integer32
_PktcMtaDevCorrelationId_Object = MibScalar
pktcMtaDevCorrelationId = _PktcMtaDevCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 4),
    _PktcMtaDevCorrelationId_Type()
)
pktcMtaDevCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevCorrelationId.setStatus("current")
_PktcMtaDevSecurityTable_Object = MibTable
pktcMtaDevSecurityTable = _PktcMtaDevSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5)
)
if mibBuilder.loadTexts:
    pktcMtaDevSecurityTable.setStatus("current")
_PktcMtaDevSecurityEntry_Object = MibTableRow
pktcMtaDevSecurityEntry = _PktcMtaDevSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1)
)
pktcMtaDevSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevSecurityEntry.setStatus("current")
_PktcMtaDevServProviderCertificate_Type = X509Certificate
_PktcMtaDevServProviderCertificate_Object = MibTableColumn
pktcMtaDevServProviderCertificate = _PktcMtaDevServProviderCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 1),
    _PktcMtaDevServProviderCertificate_Type()
)
pktcMtaDevServProviderCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServProviderCertificate.setStatus("current")
_PktcMtaDevTelephonyCertificate_Type = X509Certificate
_PktcMtaDevTelephonyCertificate_Object = MibTableColumn
pktcMtaDevTelephonyCertificate = _PktcMtaDevTelephonyCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 2),
    _PktcMtaDevTelephonyCertificate_Type()
)
pktcMtaDevTelephonyCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevTelephonyCertificate.setStatus("current")


class _PktcMtaDevKerberosRealm_Type(OctetString):
    """Custom type pktcMtaDevKerberosRealm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_PktcMtaDevKerberosRealm_Type.__name__ = "OctetString"
_PktcMtaDevKerberosRealm_Object = MibTableColumn
pktcMtaDevKerberosRealm = _PktcMtaDevKerberosRealm_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 3),
    _PktcMtaDevKerberosRealm_Type()
)
pktcMtaDevKerberosRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKerberosRealm.setStatus("current")


class _PktcMtaDevKerbPrincipalName_Type(DisplayString):
    """Custom type pktcMtaDevKerbPrincipalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_PktcMtaDevKerbPrincipalName_Type.__name__ = "DisplayString"
_PktcMtaDevKerbPrincipalName_Object = MibTableColumn
pktcMtaDevKerbPrincipalName = _PktcMtaDevKerbPrincipalName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 4),
    _PktcMtaDevKerbPrincipalName_Type()
)
pktcMtaDevKerbPrincipalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKerbPrincipalName.setStatus("current")


class _PktcMtaDevServGracePeriod_Type(Integer32):
    """Custom type pktcMtaDevServGracePeriod based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevServGracePeriod_Type.__name__ = "Integer32"
_PktcMtaDevServGracePeriod_Object = MibTableColumn
pktcMtaDevServGracePeriod = _PktcMtaDevServGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 5),
    _PktcMtaDevServGracePeriod_Type()
)
pktcMtaDevServGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevServGracePeriod.setStatus("current")
_PktcMtaDevLocalSystemCertificate_Type = X509Certificate
_PktcMtaDevLocalSystemCertificate_Object = MibTableColumn
pktcMtaDevLocalSystemCertificate = _PktcMtaDevLocalSystemCertificate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 6),
    _PktcMtaDevLocalSystemCertificate_Type()
)
pktcMtaDevLocalSystemCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevLocalSystemCertificate.setStatus("current")


class _PktcMtaDevKeyMgmtTimeout1_Type(Integer32):
    """Custom type pktcMtaDevKeyMgmtTimeout1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevKeyMgmtTimeout1_Type.__name__ = "Integer32"
_PktcMtaDevKeyMgmtTimeout1_Object = MibTableColumn
pktcMtaDevKeyMgmtTimeout1 = _PktcMtaDevKeyMgmtTimeout1_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 7),
    _PktcMtaDevKeyMgmtTimeout1_Type()
)
pktcMtaDevKeyMgmtTimeout1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout1.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout1.setUnits("seconds")


class _PktcMtaDevKeyMgmtTimeout2_Type(Integer32):
    """Custom type pktcMtaDevKeyMgmtTimeout2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_PktcMtaDevKeyMgmtTimeout2_Type.__name__ = "Integer32"
_PktcMtaDevKeyMgmtTimeout2_Object = MibTableColumn
pktcMtaDevKeyMgmtTimeout2 = _PktcMtaDevKeyMgmtTimeout2_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 5, 1, 8),
    _PktcMtaDevKeyMgmtTimeout2_Type()
)
pktcMtaDevKeyMgmtTimeout2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout2.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevKeyMgmtTimeout2.setUnits("seconds")
_PktcMtaDevTgsTable_Object = MibTable
pktcMtaDevTgsTable = _PktcMtaDevTgsTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8)
)
if mibBuilder.loadTexts:
    pktcMtaDevTgsTable.setStatus("current")
_PktcMtaDevTgsEntry_Object = MibTableRow
pktcMtaDevTgsEntry = _PktcMtaDevTgsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1)
)
pktcMtaDevTgsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PKTC-MTA-MIB", "pktcMtaDevTgsIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevTgsEntry.setStatus("current")
_PktcMtaDevTgsIndex_Type = Integer32
_PktcMtaDevTgsIndex_Object = MibTableColumn
pktcMtaDevTgsIndex = _PktcMtaDevTgsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 1),
    _PktcMtaDevTgsIndex_Type()
)
pktcMtaDevTgsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevTgsIndex.setStatus("current")


class _PktcMtaDevTgsLocation_Type(DisplayString):
    """Custom type pktcMtaDevTgsLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PktcMtaDevTgsLocation_Type.__name__ = "DisplayString"
_PktcMtaDevTgsLocation_Object = MibTableColumn
pktcMtaDevTgsLocation = _PktcMtaDevTgsLocation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 2),
    _PktcMtaDevTgsLocation_Type()
)
pktcMtaDevTgsLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevTgsLocation.setStatus("current")
_PktcMtaDevTgsStatus_Type = RowStatus
_PktcMtaDevTgsStatus_Object = MibTableColumn
pktcMtaDevTgsStatus = _PktcMtaDevTgsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 3, 8, 1, 3),
    _PktcMtaDevTgsStatus_Type()
)
pktcMtaDevTgsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcMtaDevTgsStatus.setStatus("current")
_PktcMtaDevEvent_ObjectIdentity = ObjectIdentity
pktcMtaDevEvent = _PktcMtaDevEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4)
)


class _PktcMtaDevEvControl_Type(Integer32):
    """Custom type pktcMtaDevEvControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetLog", 1),
          ("useDefaultReporting", 2))
    )


_PktcMtaDevEvControl_Type.__name__ = "Integer32"
_PktcMtaDevEvControl_Object = MibScalar
pktcMtaDevEvControl = _PktcMtaDevEvControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 1),
    _PktcMtaDevEvControl_Type()
)
pktcMtaDevEvControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvControl.setStatus("current")
_PktcMtaDevEvSyslog_Type = DisplayString
_PktcMtaDevEvSyslog_Object = MibScalar
pktcMtaDevEvSyslog = _PktcMtaDevEvSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 2),
    _PktcMtaDevEvSyslog_Type()
)
pktcMtaDevEvSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvSyslog.setStatus("current")


class _PktcMtaDevEvThrottleAdminStatus_Type(Integer32):
    """Custom type pktcMtaDevEvThrottleAdminStatus based on Integer32"""
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
        *(("inhibited", 4),
          ("maintainBelowThreshold", 2),
          ("stopAtThreshold", 3),
          ("unconstrained", 1))
    )


_PktcMtaDevEvThrottleAdminStatus_Type.__name__ = "Integer32"
_PktcMtaDevEvThrottleAdminStatus_Object = MibScalar
pktcMtaDevEvThrottleAdminStatus = _PktcMtaDevEvThrottleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 3),
    _PktcMtaDevEvThrottleAdminStatus_Type()
)
pktcMtaDevEvThrottleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvThrottleAdminStatus.setStatus("current")
_PktcMtaDevEvThrottleInhibited_Type = TruthValue
_PktcMtaDevEvThrottleInhibited_Object = MibScalar
pktcMtaDevEvThrottleInhibited = _PktcMtaDevEvThrottleInhibited_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 4),
    _PktcMtaDevEvThrottleInhibited_Type()
)
pktcMtaDevEvThrottleInhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvThrottleInhibited.setStatus("current")
_PktcMtaDevEvThrottleThreshold_Type = Unsigned32
_PktcMtaDevEvThrottleThreshold_Object = MibScalar
pktcMtaDevEvThrottleThreshold = _PktcMtaDevEvThrottleThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 5),
    _PktcMtaDevEvThrottleThreshold_Type()
)
pktcMtaDevEvThrottleThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvThrottleThreshold.setStatus("current")


class _PktcMtaDevEvThrottleInterval_Type(Integer32):
    """Custom type pktcMtaDevEvThrottleInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcMtaDevEvThrottleInterval_Type.__name__ = "Integer32"
_PktcMtaDevEvThrottleInterval_Object = MibScalar
pktcMtaDevEvThrottleInterval = _PktcMtaDevEvThrottleInterval_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 6),
    _PktcMtaDevEvThrottleInterval_Type()
)
pktcMtaDevEvThrottleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvThrottleInterval.setStatus("current")
if mibBuilder.loadTexts:
    pktcMtaDevEvThrottleInterval.setUnits("seconds")
_PktcMtaDevEvControlTable_Object = MibTable
pktcMtaDevEvControlTable = _PktcMtaDevEvControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 7)
)
if mibBuilder.loadTexts:
    pktcMtaDevEvControlTable.setStatus("current")
_PktcMtaDevEvControlEntry_Object = MibTableRow
pktcMtaDevEvControlEntry = _PktcMtaDevEvControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 7, 1)
)
pktcMtaDevEvControlEntry.setIndexNames(
    (0, "PKTC-MTA-MIB", "pktcMtaDevEvPriority"),
)
if mibBuilder.loadTexts:
    pktcMtaDevEvControlEntry.setStatus("current")


class _PktcMtaDevEvPriority_Type(Integer32):
    """Custom type pktcMtaDevEvPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("critical", 3),
          ("debug", 8),
          ("emergency", 1),
          ("error", 4),
          ("information", 7),
          ("notice", 6),
          ("warning", 5))
    )


_PktcMtaDevEvPriority_Type.__name__ = "Integer32"
_PktcMtaDevEvPriority_Object = MibTableColumn
pktcMtaDevEvPriority = _PktcMtaDevEvPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 7, 1, 1),
    _PktcMtaDevEvPriority_Type()
)
pktcMtaDevEvPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevEvPriority.setStatus("current")


class _PktcMtaDevEvReporting_Type(Bits):
    """Custom type pktcMtaDevEvReporting based on Bits"""
    namedValues = NamedValues(
        *(("local", 0),
          ("syslog", 2),
          ("traps", 1))
    )

_PktcMtaDevEvReporting_Type.__name__ = "Bits"
_PktcMtaDevEvReporting_Object = MibTableColumn
pktcMtaDevEvReporting = _PktcMtaDevEvReporting_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 7, 1, 2),
    _PktcMtaDevEvReporting_Type()
)
pktcMtaDevEvReporting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcMtaDevEvReporting.setStatus("current")
_PktcMtaDevEventTable_Object = MibTable
pktcMtaDevEventTable = _PktcMtaDevEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8)
)
if mibBuilder.loadTexts:
    pktcMtaDevEventTable.setStatus("current")
_PktcMtaDevEventEntry_Object = MibTableRow
pktcMtaDevEventEntry = _PktcMtaDevEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1)
)
pktcMtaDevEventEntry.setIndexNames(
    (0, "PKTC-MTA-MIB", "pktcMtaDevEvIndex"),
)
if mibBuilder.loadTexts:
    pktcMtaDevEventEntry.setStatus("current")


class _PktcMtaDevEvIndex_Type(Integer32):
    """Custom type pktcMtaDevEvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcMtaDevEvIndex_Type.__name__ = "Integer32"
_PktcMtaDevEvIndex_Object = MibTableColumn
pktcMtaDevEvIndex = _PktcMtaDevEvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 1),
    _PktcMtaDevEvIndex_Type()
)
pktcMtaDevEvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcMtaDevEvIndex.setStatus("current")
_PktcMtaDevEvFirstTime_Type = DateAndTime
_PktcMtaDevEvFirstTime_Object = MibTableColumn
pktcMtaDevEvFirstTime = _PktcMtaDevEvFirstTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 2),
    _PktcMtaDevEvFirstTime_Type()
)
pktcMtaDevEvFirstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvFirstTime.setStatus("current")
_PktcMtaDevEvLastTime_Type = DateAndTime
_PktcMtaDevEvLastTime_Object = MibTableColumn
pktcMtaDevEvLastTime = _PktcMtaDevEvLastTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 3),
    _PktcMtaDevEvLastTime_Type()
)
pktcMtaDevEvLastTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvLastTime.setStatus("current")
_PktcMtaDevEvCounts_Type = Counter32
_PktcMtaDevEvCounts_Object = MibTableColumn
pktcMtaDevEvCounts = _PktcMtaDevEvCounts_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 4),
    _PktcMtaDevEvCounts_Type()
)
pktcMtaDevEvCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvCounts.setStatus("current")


class _PktcMtaDevEvLevel_Type(Integer32):
    """Custom type pktcMtaDevEvLevel based on Integer32"""
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
        *(("critical", 1),
          ("debug", 7),
          ("information", 5),
          ("major", 2),
          ("minor", 3),
          ("notice", 6),
          ("warning", 4))
    )


_PktcMtaDevEvLevel_Type.__name__ = "Integer32"
_PktcMtaDevEvLevel_Object = MibTableColumn
pktcMtaDevEvLevel = _PktcMtaDevEvLevel_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 5),
    _PktcMtaDevEvLevel_Type()
)
pktcMtaDevEvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvLevel.setStatus("current")
_PktcMtaDevEvId_Type = Unsigned32
_PktcMtaDevEvId_Object = MibTableColumn
pktcMtaDevEvId = _PktcMtaDevEvId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 6),
    _PktcMtaDevEvId_Type()
)
pktcMtaDevEvId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvId.setStatus("current")
_PktcMtaDevEvText_Type = DisplayString
_PktcMtaDevEvText_Object = MibTableColumn
pktcMtaDevEvText = _PktcMtaDevEvText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 1, 4, 8, 1, 7),
    _PktcMtaDevEvText_Type()
)
pktcMtaDevEvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcMtaDevEvText.setStatus("current")
_PktcMtaNotification_ObjectIdentity = ObjectIdentity
pktcMtaNotification = _PktcMtaNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2)
)
_PktcMtaConformance_ObjectIdentity = ObjectIdentity
pktcMtaConformance = _PktcMtaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3)
)
_PktcMtaCompliances_ObjectIdentity = ObjectIdentity
pktcMtaCompliances = _PktcMtaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 1)
)
_PktcMtaGroups_ObjectIdentity = ObjectIdentity
pktcMtaGroups = _PktcMtaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2)
)

# Managed Objects groups

pktcMtaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 2, 1)
)
pktcMtaGroup.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevResetNow"),
        ("PKTC-MTA-MIB", "pktcMtaDevSerialNumber"),
        ("PKTC-MTA-MIB", "pktcMtaDevHardwareVersion"),
        ("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevFQDN"),
        ("PKTC-MTA-MIB", "pktcMtaDevEndPntCount"),
        ("PKTC-MTA-MIB", "pktcMtaDevEnabled"),
        ("PKTC-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningState"),
        ("PKTC-MTA-MIB", "pktcMtaDevCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevSignature"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-MTA-MIB", "pktcMtaDevManufacturerCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevTelephonyCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevServProviderCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevLocalSystemCertificate"),
        ("PKTC-MTA-MIB", "pktcMtaDevKerberosRealm"),
        ("PKTC-MTA-MIB", "pktcMtaDevTgsLocation"),
        ("PKTC-MTA-MIB", "pktcMtaDevKerbPrincipalName"),
        ("PKTC-MTA-MIB", "pktcMtaDevServGracePeriod"),
        ("PKTC-MTA-MIB", "pktcMtaDevKeyMgmtTimeout1"),
        ("PKTC-MTA-MIB", "pktcMtaDevKeyMgmtTimeout2"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerBootState"),
        ("PKTC-MTA-MIB", "pktcMtaDevServerDhcp"),
        ("PKTC-MTA-MIB", "pktcMtaDevSnmpEntity"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvControl"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvSyslog"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvThrottleAdminStatus"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvThrottleInhibited"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvThrottleThreshold"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvThrottleInterval"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvReporting"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvFirstTime"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvLastTime"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvCounts"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvLevel"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvId"),
        ("PKTC-MTA-MIB", "pktcMtaDevEvText"))
)
if mibBuilder.loadTexts:
    pktcMtaGroup.setStatus("current")


# Notification objects

pktcMtaProvisioningEnrollment = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2, 1)
)
pktcMtaProvisioningEnrollment.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevHardwareVersion"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwCurrentVers"),
        ("PKTC-MTA-MIB", "pktcMtaDevTypeIdentifier"),
        ("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-MTA-MIB", "pktcMtaDevSignature"))
)
if mibBuilder.loadTexts:
    pktcMtaProvisioningEnrollment.setStatus(
        "current"
    )

pktcMtaProvisioningStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 2, 2)
)
pktcMtaProvisioningStatus.setObjects(
      *(("PKTC-MTA-MIB", "pktcMtaDevMacAddress"),
        ("PKTC-MTA-MIB", "pktcMtaDevCorrelationId"),
        ("PKTC-MTA-MIB", "pktcMtaDevSignature"),
        ("PKTC-MTA-MIB", "pktcMtaDevProvisioningState"))
)
if mibBuilder.loadTexts:
    pktcMtaProvisioningStatus.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

pktcMtaBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    pktcMtaBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-MTA-MIB",
    **{"X509Certificate": X509Certificate,
       "pktcMtaMib": pktcMtaMib,
       "pktcMtaMibObjects": pktcMtaMibObjects,
       "pktcMtaDevBase": pktcMtaDevBase,
       "pktcMtaDevResetNow": pktcMtaDevResetNow,
       "pktcMtaDevSerialNumber": pktcMtaDevSerialNumber,
       "pktcMtaDevHardwareVersion": pktcMtaDevHardwareVersion,
       "pktcMtaDevMacAddress": pktcMtaDevMacAddress,
       "pktcMtaDevFQDN": pktcMtaDevFQDN,
       "pktcMtaDevEndPntCount": pktcMtaDevEndPntCount,
       "pktcMtaDevEnabled": pktcMtaDevEnabled,
       "pktcMtaDevTypeIdentifier": pktcMtaDevTypeIdentifier,
       "pktcMtaDevProvisioningState": pktcMtaDevProvisioningState,
       "pktcMtaDevHttpAccess": pktcMtaDevHttpAccess,
       "pktcMtaDevServer": pktcMtaDevServer,
       "pktcMtaDevServerBootState": pktcMtaDevServerBootState,
       "pktcMtaDevServerDhcp": pktcMtaDevServerDhcp,
       "pktcMtaDevServerDns1": pktcMtaDevServerDns1,
       "pktcMtaDevServerDns2": pktcMtaDevServerDns2,
       "pktcMtaDevConfigFile": pktcMtaDevConfigFile,
       "pktcMtaDevSnmpEntity": pktcMtaDevSnmpEntity,
       "pktcMtaDevSecurity": pktcMtaDevSecurity,
       "pktcMtaDevManufacturerCertificate": pktcMtaDevManufacturerCertificate,
       "pktcMtaDevCertificate": pktcMtaDevCertificate,
       "pktcMtaDevSignature": pktcMtaDevSignature,
       "pktcMtaDevCorrelationId": pktcMtaDevCorrelationId,
       "pktcMtaDevSecurityTable": pktcMtaDevSecurityTable,
       "pktcMtaDevSecurityEntry": pktcMtaDevSecurityEntry,
       "pktcMtaDevServProviderCertificate": pktcMtaDevServProviderCertificate,
       "pktcMtaDevTelephonyCertificate": pktcMtaDevTelephonyCertificate,
       "pktcMtaDevKerberosRealm": pktcMtaDevKerberosRealm,
       "pktcMtaDevKerbPrincipalName": pktcMtaDevKerbPrincipalName,
       "pktcMtaDevServGracePeriod": pktcMtaDevServGracePeriod,
       "pktcMtaDevLocalSystemCertificate": pktcMtaDevLocalSystemCertificate,
       "pktcMtaDevKeyMgmtTimeout1": pktcMtaDevKeyMgmtTimeout1,
       "pktcMtaDevKeyMgmtTimeout2": pktcMtaDevKeyMgmtTimeout2,
       "pktcMtaDevTgsTable": pktcMtaDevTgsTable,
       "pktcMtaDevTgsEntry": pktcMtaDevTgsEntry,
       "pktcMtaDevTgsIndex": pktcMtaDevTgsIndex,
       "pktcMtaDevTgsLocation": pktcMtaDevTgsLocation,
       "pktcMtaDevTgsStatus": pktcMtaDevTgsStatus,
       "pktcMtaDevEvent": pktcMtaDevEvent,
       "pktcMtaDevEvControl": pktcMtaDevEvControl,
       "pktcMtaDevEvSyslog": pktcMtaDevEvSyslog,
       "pktcMtaDevEvThrottleAdminStatus": pktcMtaDevEvThrottleAdminStatus,
       "pktcMtaDevEvThrottleInhibited": pktcMtaDevEvThrottleInhibited,
       "pktcMtaDevEvThrottleThreshold": pktcMtaDevEvThrottleThreshold,
       "pktcMtaDevEvThrottleInterval": pktcMtaDevEvThrottleInterval,
       "pktcMtaDevEvControlTable": pktcMtaDevEvControlTable,
       "pktcMtaDevEvControlEntry": pktcMtaDevEvControlEntry,
       "pktcMtaDevEvPriority": pktcMtaDevEvPriority,
       "pktcMtaDevEvReporting": pktcMtaDevEvReporting,
       "pktcMtaDevEventTable": pktcMtaDevEventTable,
       "pktcMtaDevEventEntry": pktcMtaDevEventEntry,
       "pktcMtaDevEvIndex": pktcMtaDevEvIndex,
       "pktcMtaDevEvFirstTime": pktcMtaDevEvFirstTime,
       "pktcMtaDevEvLastTime": pktcMtaDevEvLastTime,
       "pktcMtaDevEvCounts": pktcMtaDevEvCounts,
       "pktcMtaDevEvLevel": pktcMtaDevEvLevel,
       "pktcMtaDevEvId": pktcMtaDevEvId,
       "pktcMtaDevEvText": pktcMtaDevEvText,
       "pktcMtaNotification": pktcMtaNotification,
       "pktcMtaProvisioningEnrollment": pktcMtaProvisioningEnrollment,
       "pktcMtaProvisioningStatus": pktcMtaProvisioningStatus,
       "pktcMtaConformance": pktcMtaConformance,
       "pktcMtaCompliances": pktcMtaCompliances,
       "pktcMtaBasicCompliance": pktcMtaBasicCompliance,
       "pktcMtaGroups": pktcMtaGroups,
       "pktcMtaGroup": pktcMtaGroup}
)
