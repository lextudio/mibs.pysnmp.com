# SNMP MIB module (H3C-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-WAPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:54 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cwapiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cwapiMIBObjects_ObjectIdentity = ObjectIdentity
h3cwapiMIBObjects = _H3cwapiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1)
)
_H3cwapiModeEnabled_Type = TruthValue
_H3cwapiModeEnabled_Object = MibScalar
h3cwapiModeEnabled = _H3cwapiModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 1),
    _H3cwapiModeEnabled_Type()
)
h3cwapiModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiModeEnabled.setStatus("current")


class _H3cwapiASIPAddressType_Type(InetAddressType):
    """Custom type h3cwapiASIPAddressType based on InetAddressType"""


_H3cwapiASIPAddressType_Object = MibScalar
h3cwapiASIPAddressType = _H3cwapiASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 2),
    _H3cwapiASIPAddressType_Type()
)
h3cwapiASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiASIPAddressType.setStatus("current")
_H3cwapiASIPAddress_Type = InetAddress
_H3cwapiASIPAddress_Object = MibScalar
h3cwapiASIPAddress = _H3cwapiASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 3),
    _H3cwapiASIPAddress_Type()
)
h3cwapiASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiASIPAddress.setStatus("current")
_H3cwapiCertificateInstalled_Type = TruthValue
_H3cwapiCertificateInstalled_Object = MibScalar
h3cwapiCertificateInstalled = _H3cwapiCertificateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 1, 4),
    _H3cwapiCertificateInstalled_Type()
)
h3cwapiCertificateInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiCertificateInstalled.setStatus("current")
_H3cwapiMIBStatsObjects_ObjectIdentity = ObjectIdentity
h3cwapiMIBStatsObjects = _H3cwapiMIBStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2)
)
_H3cwapiStatsWAISignatureErrors_Type = Counter32
_H3cwapiStatsWAISignatureErrors_Object = MibScalar
h3cwapiStatsWAISignatureErrors = _H3cwapiStatsWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 1),
    _H3cwapiStatsWAISignatureErrors_Type()
)
h3cwapiStatsWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAISignatureErrors.setStatus("current")
_H3cwapiStatsWAIHMACErrors_Type = Counter32
_H3cwapiStatsWAIHMACErrors_Object = MibScalar
h3cwapiStatsWAIHMACErrors = _H3cwapiStatsWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 2),
    _H3cwapiStatsWAIHMACErrors_Type()
)
h3cwapiStatsWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIHMACErrors.setStatus("current")
_H3cwapiStatsWAIAuthRsltFailures_Type = Counter32
_H3cwapiStatsWAIAuthRsltFailures_Object = MibScalar
h3cwapiStatsWAIAuthRsltFailures = _H3cwapiStatsWAIAuthRsltFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 3),
    _H3cwapiStatsWAIAuthRsltFailures_Type()
)
h3cwapiStatsWAIAuthRsltFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIAuthRsltFailures.setStatus("current")
_H3cwapiStatsWAIDiscardCounters_Type = Counter32
_H3cwapiStatsWAIDiscardCounters_Object = MibScalar
h3cwapiStatsWAIDiscardCounters = _H3cwapiStatsWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 4),
    _H3cwapiStatsWAIDiscardCounters_Type()
)
h3cwapiStatsWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIDiscardCounters.setStatus("current")
_H3cwapiStatsWAITimeoutCounters_Type = Counter32
_H3cwapiStatsWAITimeoutCounters_Object = MibScalar
h3cwapiStatsWAITimeoutCounters = _H3cwapiStatsWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 5),
    _H3cwapiStatsWAITimeoutCounters_Type()
)
h3cwapiStatsWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAITimeoutCounters.setStatus("current")
_H3cwapiStatsWAIFormatErrors_Type = Counter32
_H3cwapiStatsWAIFormatErrors_Object = MibScalar
h3cwapiStatsWAIFormatErrors = _H3cwapiStatsWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 6),
    _H3cwapiStatsWAIFormatErrors_Type()
)
h3cwapiStatsWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIFormatErrors.setStatus("current")
_H3cwapiStatsWAICtfHskFailures_Type = Counter32
_H3cwapiStatsWAICtfHskFailures_Object = MibScalar
h3cwapiStatsWAICtfHskFailures = _H3cwapiStatsWAICtfHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 7),
    _H3cwapiStatsWAICtfHskFailures_Type()
)
h3cwapiStatsWAICtfHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAICtfHskFailures.setStatus("current")
_H3cwapiStatsWAIUniHskFailures_Type = Counter32
_H3cwapiStatsWAIUniHskFailures_Object = MibScalar
h3cwapiStatsWAIUniHskFailures = _H3cwapiStatsWAIUniHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 8),
    _H3cwapiStatsWAIUniHskFailures_Type()
)
h3cwapiStatsWAIUniHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIUniHskFailures.setStatus("current")
_H3cwapiStatsWAIMulHskFailures_Type = Counter32
_H3cwapiStatsWAIMulHskFailures_Object = MibScalar
h3cwapiStatsWAIMulHskFailures = _H3cwapiStatsWAIMulHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 2, 9),
    _H3cwapiStatsWAIMulHskFailures_Type()
)
h3cwapiStatsWAIMulHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiStatsWAIMulHskFailures.setStatus("current")
_H3cwapiMIBTableObjects_ObjectIdentity = ObjectIdentity
h3cwapiMIBTableObjects = _H3cwapiMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3)
)
_H3cwapiConfigTable_Object = MibTable
h3cwapiConfigTable = _H3cwapiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1)
)
if mibBuilder.loadTexts:
    h3cwapiConfigTable.setStatus("current")
_H3cwapiConfigEntry_Object = MibTableRow
h3cwapiConfigEntry = _H3cwapiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1)
)
h3cwapiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cwapiConfigEntry.setStatus("current")
_H3cwapiConfigASIPAddressType_Type = InetAddressType
_H3cwapiConfigASIPAddressType_Object = MibTableColumn
h3cwapiConfigASIPAddressType = _H3cwapiConfigASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 1),
    _H3cwapiConfigASIPAddressType_Type()
)
h3cwapiConfigASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigASIPAddressType.setStatus("current")
_H3cwapiConfigASIPAddress_Type = InetAddress
_H3cwapiConfigASIPAddress_Object = MibTableColumn
h3cwapiConfigASIPAddress = _H3cwapiConfigASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 2),
    _H3cwapiConfigASIPAddress_Type()
)
h3cwapiConfigASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigASIPAddress.setStatus("current")


class _H3cwapiConfigAuthMethod_Type(Integer32):
    """Custom type h3cwapiConfigAuthMethod based on Integer32"""
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
        *(("certificate", 1),
          ("certificatePsk", 3),
          ("psk", 2))
    )


_H3cwapiConfigAuthMethod_Type.__name__ = "Integer32"
_H3cwapiConfigAuthMethod_Object = MibTableColumn
h3cwapiConfigAuthMethod = _H3cwapiConfigAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 3),
    _H3cwapiConfigAuthMethod_Type()
)
h3cwapiConfigAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigAuthMethod.setStatus("current")


class _H3cwapiConfigAuthMode_Type(Integer32):
    """Custom type h3cwapiConfigAuthMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radiusExtension", 2),
          ("standard", 1))
    )


_H3cwapiConfigAuthMode_Type.__name__ = "Integer32"
_H3cwapiConfigAuthMode_Object = MibTableColumn
h3cwapiConfigAuthMode = _H3cwapiConfigAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 4),
    _H3cwapiConfigAuthMode_Type()
)
h3cwapiConfigAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigAuthMode.setStatus("current")


class _H3cwapiConfigISPDomain_Type(OctetString):
    """Custom type h3cwapiConfigISPDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_H3cwapiConfigISPDomain_Type.__name__ = "OctetString"
_H3cwapiConfigISPDomain_Object = MibTableColumn
h3cwapiConfigISPDomain = _H3cwapiConfigISPDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 5),
    _H3cwapiConfigISPDomain_Type()
)
h3cwapiConfigISPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigISPDomain.setStatus("current")


class _H3cwapiConfigCertificateDomain_Type(OctetString):
    """Custom type h3cwapiConfigCertificateDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cwapiConfigCertificateDomain_Type.__name__ = "OctetString"
_H3cwapiConfigCertificateDomain_Object = MibTableColumn
h3cwapiConfigCertificateDomain = _H3cwapiConfigCertificateDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 6),
    _H3cwapiConfigCertificateDomain_Type()
)
h3cwapiConfigCertificateDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigCertificateDomain.setStatus("current")


class _H3cwapiConfigASName_Type(OctetString):
    """Custom type h3cwapiConfigASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cwapiConfigASName_Type.__name__ = "OctetString"
_H3cwapiConfigASName_Object = MibTableColumn
h3cwapiConfigASName = _H3cwapiConfigASName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 7),
    _H3cwapiConfigASName_Type()
)
h3cwapiConfigASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigASName.setStatus("current")
_H3cwapiConfigBKRekeyEnabled_Type = TruthValue
_H3cwapiConfigBKRekeyEnabled_Object = MibTableColumn
h3cwapiConfigBKRekeyEnabled = _H3cwapiConfigBKRekeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 1, 1, 8),
    _H3cwapiConfigBKRekeyEnabled_Type()
)
h3cwapiConfigBKRekeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigBKRekeyEnabled.setStatus("current")
_H3cwapiConfigExtTable_Object = MibTable
h3cwapiConfigExtTable = _H3cwapiConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2)
)
if mibBuilder.loadTexts:
    h3cwapiConfigExtTable.setStatus("current")
_H3cwapiConfigExtEntry_Object = MibTableRow
h3cwapiConfigExtEntry = _H3cwapiConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1)
)
h3cwapiConfigExtEntry.setIndexNames(
    (0, "H3C-WAPI-MIB", "h3cwapiConfigServicePolicyID"),
)
if mibBuilder.loadTexts:
    h3cwapiConfigExtEntry.setStatus("current")
_H3cwapiConfigServicePolicyID_Type = Integer32
_H3cwapiConfigServicePolicyID_Object = MibTableColumn
h3cwapiConfigServicePolicyID = _H3cwapiConfigServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 1),
    _H3cwapiConfigServicePolicyID_Type()
)
h3cwapiConfigServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cwapiConfigServicePolicyID.setStatus("current")
_H3cwapiConfigUnicastCipherEnabled_Type = TruthValue
_H3cwapiConfigUnicastCipherEnabled_Object = MibTableColumn
h3cwapiConfigUnicastCipherEnabled = _H3cwapiConfigUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 2),
    _H3cwapiConfigUnicastCipherEnabled_Type()
)
h3cwapiConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigUnicastCipherEnabled.setStatus("current")


class _H3cwapiConfigUnicastCipherSize_Type(Unsigned32):
    """Custom type h3cwapiConfigUnicastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cwapiConfigUnicastCipherSize_Type.__name__ = "Unsigned32"
_H3cwapiConfigUnicastCipherSize_Object = MibTableColumn
h3cwapiConfigUnicastCipherSize = _H3cwapiConfigUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 3),
    _H3cwapiConfigUnicastCipherSize_Type()
)
h3cwapiConfigUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiConfigUnicastCipherSize.setStatus("current")
_H3cwapiConfigAuthenticationSuiteEnabled_Type = TruthValue
_H3cwapiConfigAuthenticationSuiteEnabled_Object = MibTableColumn
h3cwapiConfigAuthenticationSuiteEnabled = _H3cwapiConfigAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 4),
    _H3cwapiConfigAuthenticationSuiteEnabled_Type()
)
h3cwapiConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiConfigAuthenticationSuiteEnabled.setStatus("current")


class _H3cwapiConfigAuthenticationSuite_Type(OctetString):
    """Custom type h3cwapiConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_H3cwapiConfigAuthenticationSuite_Type.__name__ = "OctetString"
_H3cwapiConfigAuthenticationSuite_Object = MibTableColumn
h3cwapiConfigAuthenticationSuite = _H3cwapiConfigAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 5),
    _H3cwapiConfigAuthenticationSuite_Type()
)
h3cwapiConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiConfigAuthenticationSuite.setStatus("current")
_H3cwapiCfgExtASIPAddressType_Type = InetAddressType
_H3cwapiCfgExtASIPAddressType_Object = MibTableColumn
h3cwapiCfgExtASIPAddressType = _H3cwapiCfgExtASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 6),
    _H3cwapiCfgExtASIPAddressType_Type()
)
h3cwapiCfgExtASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiCfgExtASIPAddressType.setStatus("current")
_H3cwapiCfgExtASIPAddress_Type = InetAddress
_H3cwapiCfgExtASIPAddress_Object = MibTableColumn
h3cwapiCfgExtASIPAddress = _H3cwapiCfgExtASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 7),
    _H3cwapiCfgExtASIPAddress_Type()
)
h3cwapiCfgExtASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiCfgExtASIPAddress.setStatus("current")


class _H3cwapiCfgExtASName_Type(OctetString):
    """Custom type h3cwapiCfgExtASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cwapiCfgExtASName_Type.__name__ = "OctetString"
_H3cwapiCfgExtASName_Object = MibTableColumn
h3cwapiCfgExtASName = _H3cwapiCfgExtASName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 8),
    _H3cwapiCfgExtASName_Type()
)
h3cwapiCfgExtASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiCfgExtASName.setStatus("current")


class _H3cwapiCfgExtCertDomain_Type(OctetString):
    """Custom type h3cwapiCfgExtCertDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cwapiCfgExtCertDomain_Type.__name__ = "OctetString"
_H3cwapiCfgExtCertDomain_Object = MibTableColumn
h3cwapiCfgExtCertDomain = _H3cwapiCfgExtCertDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 9),
    _H3cwapiCfgExtCertDomain_Type()
)
h3cwapiCfgExtCertDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cwapiCfgExtCertDomain.setStatus("current")
_H3cwapiCfgExtCertInstalled_Type = TruthValue
_H3cwapiCfgExtCertInstalled_Object = MibTableColumn
h3cwapiCfgExtCertInstalled = _H3cwapiCfgExtCertInstalled_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 3, 2, 1, 10),
    _H3cwapiCfgExtCertInstalled_Type()
)
h3cwapiCfgExtCertInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cwapiCfgExtCertInstalled.setStatus("current")
_H3cwapiTrap_ObjectIdentity = ObjectIdentity
h3cwapiTrap = _H3cwapiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4)
)
_H3cwapiTrapPrefix_ObjectIdentity = ObjectIdentity
h3cwapiTrapPrefix = _H3cwapiTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0)
)
_H3cwapiTrapInfo_ObjectIdentity = ObjectIdentity
h3cwapiTrapInfo = _H3cwapiTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1)
)
_H3cwapiTrapInfoMacAddr_Type = MacAddress
_H3cwapiTrapInfoMacAddr_Object = MibScalar
h3cwapiTrapInfoMacAddr = _H3cwapiTrapInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 1),
    _H3cwapiTrapInfoMacAddr_Type()
)
h3cwapiTrapInfoMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cwapiTrapInfoMacAddr.setStatus("current")
_H3cwapiTrapInfoAPId_Type = Integer32
_H3cwapiTrapInfoAPId_Object = MibScalar
h3cwapiTrapInfoAPId = _H3cwapiTrapInfoAPId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 2),
    _H3cwapiTrapInfoAPId_Type()
)
h3cwapiTrapInfoAPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cwapiTrapInfoAPId.setStatus("current")
_H3cwapiTrapInfoRadioId_Type = Integer32
_H3cwapiTrapInfoRadioId_Object = MibScalar
h3cwapiTrapInfoRadioId = _H3cwapiTrapInfoRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 3),
    _H3cwapiTrapInfoRadioId_Type()
)
h3cwapiTrapInfoRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cwapiTrapInfoRadioId.setStatus("current")
_H3cwapiTrapInfoBSSId_Type = MacAddress
_H3cwapiTrapInfoBSSId_Object = MibScalar
h3cwapiTrapInfoBSSId = _H3cwapiTrapInfoBSSId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 1, 4),
    _H3cwapiTrapInfoBSSId_Type()
)
h3cwapiTrapInfoBSSId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cwapiTrapInfoBSSId.setStatus("current")

# Managed Objects groups


# Notification objects

h3cwapiUserwithInvalidCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 1)
)
h3cwapiUserwithInvalidCertificate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    h3cwapiUserwithInvalidCertificate.setStatus(
        "current"
    )

h3cwapiStationReplayAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 2)
)
h3cwapiStationReplayAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    h3cwapiStationReplayAttack.setStatus(
        "current"
    )

h3cwapiTamperAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 3)
)
h3cwapiTamperAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    h3cwapiTamperAttack.setStatus(
        "current"
    )

h3cwapiLowSafeLevelAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 4)
)
h3cwapiLowSafeLevelAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    h3cwapiLowSafeLevelAttack.setStatus(
        "current"
    )

h3cwapiAddressRedirectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 77, 4, 0, 5)
)
h3cwapiAddressRedirectionAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoMacAddr"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoAPId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoRadioId"),
        ("H3C-WAPI-MIB", "h3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    h3cwapiAddressRedirectionAttack.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-WAPI-MIB",
    **{"h3cwapiMIB": h3cwapiMIB,
       "h3cwapiMIBObjects": h3cwapiMIBObjects,
       "h3cwapiModeEnabled": h3cwapiModeEnabled,
       "h3cwapiASIPAddressType": h3cwapiASIPAddressType,
       "h3cwapiASIPAddress": h3cwapiASIPAddress,
       "h3cwapiCertificateInstalled": h3cwapiCertificateInstalled,
       "h3cwapiMIBStatsObjects": h3cwapiMIBStatsObjects,
       "h3cwapiStatsWAISignatureErrors": h3cwapiStatsWAISignatureErrors,
       "h3cwapiStatsWAIHMACErrors": h3cwapiStatsWAIHMACErrors,
       "h3cwapiStatsWAIAuthRsltFailures": h3cwapiStatsWAIAuthRsltFailures,
       "h3cwapiStatsWAIDiscardCounters": h3cwapiStatsWAIDiscardCounters,
       "h3cwapiStatsWAITimeoutCounters": h3cwapiStatsWAITimeoutCounters,
       "h3cwapiStatsWAIFormatErrors": h3cwapiStatsWAIFormatErrors,
       "h3cwapiStatsWAICtfHskFailures": h3cwapiStatsWAICtfHskFailures,
       "h3cwapiStatsWAIUniHskFailures": h3cwapiStatsWAIUniHskFailures,
       "h3cwapiStatsWAIMulHskFailures": h3cwapiStatsWAIMulHskFailures,
       "h3cwapiMIBTableObjects": h3cwapiMIBTableObjects,
       "h3cwapiConfigTable": h3cwapiConfigTable,
       "h3cwapiConfigEntry": h3cwapiConfigEntry,
       "h3cwapiConfigASIPAddressType": h3cwapiConfigASIPAddressType,
       "h3cwapiConfigASIPAddress": h3cwapiConfigASIPAddress,
       "h3cwapiConfigAuthMethod": h3cwapiConfigAuthMethod,
       "h3cwapiConfigAuthMode": h3cwapiConfigAuthMode,
       "h3cwapiConfigISPDomain": h3cwapiConfigISPDomain,
       "h3cwapiConfigCertificateDomain": h3cwapiConfigCertificateDomain,
       "h3cwapiConfigASName": h3cwapiConfigASName,
       "h3cwapiConfigBKRekeyEnabled": h3cwapiConfigBKRekeyEnabled,
       "h3cwapiConfigExtTable": h3cwapiConfigExtTable,
       "h3cwapiConfigExtEntry": h3cwapiConfigExtEntry,
       "h3cwapiConfigServicePolicyID": h3cwapiConfigServicePolicyID,
       "h3cwapiConfigUnicastCipherEnabled": h3cwapiConfigUnicastCipherEnabled,
       "h3cwapiConfigUnicastCipherSize": h3cwapiConfigUnicastCipherSize,
       "h3cwapiConfigAuthenticationSuiteEnabled": h3cwapiConfigAuthenticationSuiteEnabled,
       "h3cwapiConfigAuthenticationSuite": h3cwapiConfigAuthenticationSuite,
       "h3cwapiCfgExtASIPAddressType": h3cwapiCfgExtASIPAddressType,
       "h3cwapiCfgExtASIPAddress": h3cwapiCfgExtASIPAddress,
       "h3cwapiCfgExtASName": h3cwapiCfgExtASName,
       "h3cwapiCfgExtCertDomain": h3cwapiCfgExtCertDomain,
       "h3cwapiCfgExtCertInstalled": h3cwapiCfgExtCertInstalled,
       "h3cwapiTrap": h3cwapiTrap,
       "h3cwapiTrapPrefix": h3cwapiTrapPrefix,
       "h3cwapiUserwithInvalidCertificate": h3cwapiUserwithInvalidCertificate,
       "h3cwapiStationReplayAttack": h3cwapiStationReplayAttack,
       "h3cwapiTamperAttack": h3cwapiTamperAttack,
       "h3cwapiLowSafeLevelAttack": h3cwapiLowSafeLevelAttack,
       "h3cwapiAddressRedirectionAttack": h3cwapiAddressRedirectionAttack,
       "h3cwapiTrapInfo": h3cwapiTrapInfo,
       "h3cwapiTrapInfoMacAddr": h3cwapiTrapInfoMacAddr,
       "h3cwapiTrapInfoAPId": h3cwapiTrapInfoAPId,
       "h3cwapiTrapInfoRadioId": h3cwapiTrapInfoRadioId,
       "h3cwapiTrapInfoBSSId": h3cwapiTrapInfoBSSId}
)
