# SNMP MIB module (HH3C-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-WAPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:23 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cwapiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cwapiMIBObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBObjects = _Hh3cwapiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1)
)
_Hh3cwapiModeEnabled_Type = TruthValue
_Hh3cwapiModeEnabled_Object = MibScalar
hh3cwapiModeEnabled = _Hh3cwapiModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 1),
    _Hh3cwapiModeEnabled_Type()
)
hh3cwapiModeEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiModeEnabled.setStatus("current")


class _Hh3cwapiASIPAddressType_Type(InetAddressType):
    """Custom type hh3cwapiASIPAddressType based on InetAddressType"""


_Hh3cwapiASIPAddressType_Object = MibScalar
hh3cwapiASIPAddressType = _Hh3cwapiASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 2),
    _Hh3cwapiASIPAddressType_Type()
)
hh3cwapiASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddressType.setStatus("current")
_Hh3cwapiASIPAddress_Type = InetAddress
_Hh3cwapiASIPAddress_Object = MibScalar
hh3cwapiASIPAddress = _Hh3cwapiASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 3),
    _Hh3cwapiASIPAddress_Type()
)
hh3cwapiASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiASIPAddress.setStatus("current")
_Hh3cwapiCertificateInstalled_Type = TruthValue
_Hh3cwapiCertificateInstalled_Object = MibScalar
hh3cwapiCertificateInstalled = _Hh3cwapiCertificateInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 1, 4),
    _Hh3cwapiCertificateInstalled_Type()
)
hh3cwapiCertificateInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCertificateInstalled.setStatus("current")
_Hh3cwapiMIBStatsObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBStatsObjects = _Hh3cwapiMIBStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2)
)
_Hh3cwapiStatsWAISignatureErrors_Type = Counter32
_Hh3cwapiStatsWAISignatureErrors_Object = MibScalar
hh3cwapiStatsWAISignatureErrors = _Hh3cwapiStatsWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 1),
    _Hh3cwapiStatsWAISignatureErrors_Type()
)
hh3cwapiStatsWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAISignatureErrors.setStatus("current")
_Hh3cwapiStatsWAIHMACErrors_Type = Counter32
_Hh3cwapiStatsWAIHMACErrors_Object = MibScalar
hh3cwapiStatsWAIHMACErrors = _Hh3cwapiStatsWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 2),
    _Hh3cwapiStatsWAIHMACErrors_Type()
)
hh3cwapiStatsWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIHMACErrors.setStatus("current")
_Hh3cwapiStatsWAIAuthRsltFailures_Type = Counter32
_Hh3cwapiStatsWAIAuthRsltFailures_Object = MibScalar
hh3cwapiStatsWAIAuthRsltFailures = _Hh3cwapiStatsWAIAuthRsltFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 3),
    _Hh3cwapiStatsWAIAuthRsltFailures_Type()
)
hh3cwapiStatsWAIAuthRsltFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIAuthRsltFailures.setStatus("current")
_Hh3cwapiStatsWAIDiscardCounters_Type = Counter32
_Hh3cwapiStatsWAIDiscardCounters_Object = MibScalar
hh3cwapiStatsWAIDiscardCounters = _Hh3cwapiStatsWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 4),
    _Hh3cwapiStatsWAIDiscardCounters_Type()
)
hh3cwapiStatsWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIDiscardCounters.setStatus("current")
_Hh3cwapiStatsWAITimeoutCounters_Type = Counter32
_Hh3cwapiStatsWAITimeoutCounters_Object = MibScalar
hh3cwapiStatsWAITimeoutCounters = _Hh3cwapiStatsWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 5),
    _Hh3cwapiStatsWAITimeoutCounters_Type()
)
hh3cwapiStatsWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAITimeoutCounters.setStatus("current")
_Hh3cwapiStatsWAIFormatErrors_Type = Counter32
_Hh3cwapiStatsWAIFormatErrors_Object = MibScalar
hh3cwapiStatsWAIFormatErrors = _Hh3cwapiStatsWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 6),
    _Hh3cwapiStatsWAIFormatErrors_Type()
)
hh3cwapiStatsWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIFormatErrors.setStatus("current")
_Hh3cwapiStatsWAICtfHskFailures_Type = Counter32
_Hh3cwapiStatsWAICtfHskFailures_Object = MibScalar
hh3cwapiStatsWAICtfHskFailures = _Hh3cwapiStatsWAICtfHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 7),
    _Hh3cwapiStatsWAICtfHskFailures_Type()
)
hh3cwapiStatsWAICtfHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAICtfHskFailures.setStatus("current")
_Hh3cwapiStatsWAIUniHskFailures_Type = Counter32
_Hh3cwapiStatsWAIUniHskFailures_Object = MibScalar
hh3cwapiStatsWAIUniHskFailures = _Hh3cwapiStatsWAIUniHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 8),
    _Hh3cwapiStatsWAIUniHskFailures_Type()
)
hh3cwapiStatsWAIUniHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIUniHskFailures.setStatus("current")
_Hh3cwapiStatsWAIMulHskFailures_Type = Counter32
_Hh3cwapiStatsWAIMulHskFailures_Object = MibScalar
hh3cwapiStatsWAIMulHskFailures = _Hh3cwapiStatsWAIMulHskFailures_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 2, 9),
    _Hh3cwapiStatsWAIMulHskFailures_Type()
)
hh3cwapiStatsWAIMulHskFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiStatsWAIMulHskFailures.setStatus("current")
_Hh3cwapiMIBTableObjects_ObjectIdentity = ObjectIdentity
hh3cwapiMIBTableObjects = _Hh3cwapiMIBTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3)
)
_Hh3cwapiConfigTable_Object = MibTable
hh3cwapiConfigTable = _Hh3cwapiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cwapiConfigTable.setStatus("current")
_Hh3cwapiConfigEntry_Object = MibTableRow
hh3cwapiConfigEntry = _Hh3cwapiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1)
)
hh3cwapiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cwapiConfigEntry.setStatus("current")
_Hh3cwapiConfigASIPAddressType_Type = InetAddressType
_Hh3cwapiConfigASIPAddressType_Object = MibTableColumn
hh3cwapiConfigASIPAddressType = _Hh3cwapiConfigASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 1),
    _Hh3cwapiConfigASIPAddressType_Type()
)
hh3cwapiConfigASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASIPAddressType.setStatus("current")
_Hh3cwapiConfigASIPAddress_Type = InetAddress
_Hh3cwapiConfigASIPAddress_Object = MibTableColumn
hh3cwapiConfigASIPAddress = _Hh3cwapiConfigASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 2),
    _Hh3cwapiConfigASIPAddress_Type()
)
hh3cwapiConfigASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASIPAddress.setStatus("current")


class _Hh3cwapiConfigAuthMethod_Type(Integer32):
    """Custom type hh3cwapiConfigAuthMethod based on Integer32"""
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


_Hh3cwapiConfigAuthMethod_Type.__name__ = "Integer32"
_Hh3cwapiConfigAuthMethod_Object = MibTableColumn
hh3cwapiConfigAuthMethod = _Hh3cwapiConfigAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 3),
    _Hh3cwapiConfigAuthMethod_Type()
)
hh3cwapiConfigAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthMethod.setStatus("current")


class _Hh3cwapiConfigAuthMode_Type(Integer32):
    """Custom type hh3cwapiConfigAuthMode based on Integer32"""
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


_Hh3cwapiConfigAuthMode_Type.__name__ = "Integer32"
_Hh3cwapiConfigAuthMode_Object = MibTableColumn
hh3cwapiConfigAuthMode = _Hh3cwapiConfigAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 4),
    _Hh3cwapiConfigAuthMode_Type()
)
hh3cwapiConfigAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthMode.setStatus("current")


class _Hh3cwapiConfigISPDomain_Type(OctetString):
    """Custom type hh3cwapiConfigISPDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Hh3cwapiConfigISPDomain_Type.__name__ = "OctetString"
_Hh3cwapiConfigISPDomain_Object = MibTableColumn
hh3cwapiConfigISPDomain = _Hh3cwapiConfigISPDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 5),
    _Hh3cwapiConfigISPDomain_Type()
)
hh3cwapiConfigISPDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigISPDomain.setStatus("current")


class _Hh3cwapiConfigCertificateDomain_Type(OctetString):
    """Custom type hh3cwapiConfigCertificateDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiConfigCertificateDomain_Type.__name__ = "OctetString"
_Hh3cwapiConfigCertificateDomain_Object = MibTableColumn
hh3cwapiConfigCertificateDomain = _Hh3cwapiConfigCertificateDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 6),
    _Hh3cwapiConfigCertificateDomain_Type()
)
hh3cwapiConfigCertificateDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigCertificateDomain.setStatus("current")


class _Hh3cwapiConfigASName_Type(OctetString):
    """Custom type hh3cwapiConfigASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiConfigASName_Type.__name__ = "OctetString"
_Hh3cwapiConfigASName_Object = MibTableColumn
hh3cwapiConfigASName = _Hh3cwapiConfigASName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 7),
    _Hh3cwapiConfigASName_Type()
)
hh3cwapiConfigASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigASName.setStatus("current")
_Hh3cwapiConfigBKRekeyEnabled_Type = TruthValue
_Hh3cwapiConfigBKRekeyEnabled_Object = MibTableColumn
hh3cwapiConfigBKRekeyEnabled = _Hh3cwapiConfigBKRekeyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 1, 1, 8),
    _Hh3cwapiConfigBKRekeyEnabled_Type()
)
hh3cwapiConfigBKRekeyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigBKRekeyEnabled.setStatus("current")
_Hh3cwapiConfigExtTable_Object = MibTable
hh3cwapiConfigExtTable = _Hh3cwapiConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cwapiConfigExtTable.setStatus("current")
_Hh3cwapiConfigExtEntry_Object = MibTableRow
hh3cwapiConfigExtEntry = _Hh3cwapiConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1)
)
hh3cwapiConfigExtEntry.setIndexNames(
    (0, "HH3C-WAPI-MIB", "hh3cwapiConfigServicePolicyID"),
)
if mibBuilder.loadTexts:
    hh3cwapiConfigExtEntry.setStatus("current")
_Hh3cwapiConfigServicePolicyID_Type = Integer32
_Hh3cwapiConfigServicePolicyID_Object = MibTableColumn
hh3cwapiConfigServicePolicyID = _Hh3cwapiConfigServicePolicyID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 1),
    _Hh3cwapiConfigServicePolicyID_Type()
)
hh3cwapiConfigServicePolicyID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cwapiConfigServicePolicyID.setStatus("current")
_Hh3cwapiConfigUnicastCipherEnabled_Type = TruthValue
_Hh3cwapiConfigUnicastCipherEnabled_Object = MibTableColumn
hh3cwapiConfigUnicastCipherEnabled = _Hh3cwapiConfigUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 2),
    _Hh3cwapiConfigUnicastCipherEnabled_Type()
)
hh3cwapiConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigUnicastCipherEnabled.setStatus("current")


class _Hh3cwapiConfigUnicastCipherSize_Type(Unsigned32):
    """Custom type hh3cwapiConfigUnicastCipherSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cwapiConfigUnicastCipherSize_Type.__name__ = "Unsigned32"
_Hh3cwapiConfigUnicastCipherSize_Object = MibTableColumn
hh3cwapiConfigUnicastCipherSize = _Hh3cwapiConfigUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 3),
    _Hh3cwapiConfigUnicastCipherSize_Type()
)
hh3cwapiConfigUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiConfigUnicastCipherSize.setStatus("current")
_Hh3cwapiConfigAuthenticationSuiteEnabled_Type = TruthValue
_Hh3cwapiConfigAuthenticationSuiteEnabled_Object = MibTableColumn
hh3cwapiConfigAuthenticationSuiteEnabled = _Hh3cwapiConfigAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 4),
    _Hh3cwapiConfigAuthenticationSuiteEnabled_Type()
)
hh3cwapiConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthenticationSuiteEnabled.setStatus("current")


class _Hh3cwapiConfigAuthenticationSuite_Type(OctetString):
    """Custom type hh3cwapiConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cwapiConfigAuthenticationSuite_Type.__name__ = "OctetString"
_Hh3cwapiConfigAuthenticationSuite_Object = MibTableColumn
hh3cwapiConfigAuthenticationSuite = _Hh3cwapiConfigAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 5),
    _Hh3cwapiConfigAuthenticationSuite_Type()
)
hh3cwapiConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiConfigAuthenticationSuite.setStatus("current")
_Hh3cwapiCfgExtASIPAddressType_Type = InetAddressType
_Hh3cwapiCfgExtASIPAddressType_Object = MibTableColumn
hh3cwapiCfgExtASIPAddressType = _Hh3cwapiCfgExtASIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 6),
    _Hh3cwapiCfgExtASIPAddressType_Type()
)
hh3cwapiCfgExtASIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASIPAddressType.setStatus("current")
_Hh3cwapiCfgExtASIPAddress_Type = InetAddress
_Hh3cwapiCfgExtASIPAddress_Object = MibTableColumn
hh3cwapiCfgExtASIPAddress = _Hh3cwapiCfgExtASIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 7),
    _Hh3cwapiCfgExtASIPAddress_Type()
)
hh3cwapiCfgExtASIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASIPAddress.setStatus("current")


class _Hh3cwapiCfgExtASName_Type(OctetString):
    """Custom type hh3cwapiCfgExtASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiCfgExtASName_Type.__name__ = "OctetString"
_Hh3cwapiCfgExtASName_Object = MibTableColumn
hh3cwapiCfgExtASName = _Hh3cwapiCfgExtASName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 8),
    _Hh3cwapiCfgExtASName_Type()
)
hh3cwapiCfgExtASName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtASName.setStatus("current")


class _Hh3cwapiCfgExtCertDomain_Type(OctetString):
    """Custom type hh3cwapiCfgExtCertDomain based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cwapiCfgExtCertDomain_Type.__name__ = "OctetString"
_Hh3cwapiCfgExtCertDomain_Object = MibTableColumn
hh3cwapiCfgExtCertDomain = _Hh3cwapiCfgExtCertDomain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 9),
    _Hh3cwapiCfgExtCertDomain_Type()
)
hh3cwapiCfgExtCertDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtCertDomain.setStatus("current")
_Hh3cwapiCfgExtCertInstalled_Type = TruthValue
_Hh3cwapiCfgExtCertInstalled_Object = MibTableColumn
hh3cwapiCfgExtCertInstalled = _Hh3cwapiCfgExtCertInstalled_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 3, 2, 1, 10),
    _Hh3cwapiCfgExtCertInstalled_Type()
)
hh3cwapiCfgExtCertInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cwapiCfgExtCertInstalled.setStatus("current")
_Hh3cwapiTrap_ObjectIdentity = ObjectIdentity
hh3cwapiTrap = _Hh3cwapiTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4)
)
_Hh3cwapiTrapPrefix_ObjectIdentity = ObjectIdentity
hh3cwapiTrapPrefix = _Hh3cwapiTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0)
)
_Hh3cwapiTrapInfo_ObjectIdentity = ObjectIdentity
hh3cwapiTrapInfo = _Hh3cwapiTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1)
)
_Hh3cwapiTrapInfoMacAddr_Type = MacAddress
_Hh3cwapiTrapInfoMacAddr_Object = MibScalar
hh3cwapiTrapInfoMacAddr = _Hh3cwapiTrapInfoMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 1),
    _Hh3cwapiTrapInfoMacAddr_Type()
)
hh3cwapiTrapInfoMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoMacAddr.setStatus("current")
_Hh3cwapiTrapInfoAPId_Type = Integer32
_Hh3cwapiTrapInfoAPId_Object = MibScalar
hh3cwapiTrapInfoAPId = _Hh3cwapiTrapInfoAPId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 2),
    _Hh3cwapiTrapInfoAPId_Type()
)
hh3cwapiTrapInfoAPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoAPId.setStatus("current")
_Hh3cwapiTrapInfoRadioId_Type = Integer32
_Hh3cwapiTrapInfoRadioId_Object = MibScalar
hh3cwapiTrapInfoRadioId = _Hh3cwapiTrapInfoRadioId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 3),
    _Hh3cwapiTrapInfoRadioId_Type()
)
hh3cwapiTrapInfoRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoRadioId.setStatus("current")
_Hh3cwapiTrapInfoBSSId_Type = MacAddress
_Hh3cwapiTrapInfoBSSId_Object = MibScalar
hh3cwapiTrapInfoBSSId = _Hh3cwapiTrapInfoBSSId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 1, 4),
    _Hh3cwapiTrapInfoBSSId_Type()
)
hh3cwapiTrapInfoBSSId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cwapiTrapInfoBSSId.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cwapiUserwithInvalidCertificate = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 1)
)
hh3cwapiUserwithInvalidCertificate.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    hh3cwapiUserwithInvalidCertificate.setStatus(
        "current"
    )

hh3cwapiStationReplayAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 2)
)
hh3cwapiStationReplayAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    hh3cwapiStationReplayAttack.setStatus(
        "current"
    )

hh3cwapiTamperAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 3)
)
hh3cwapiTamperAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    hh3cwapiTamperAttack.setStatus(
        "current"
    )

hh3cwapiLowSafeLevelAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 4)
)
hh3cwapiLowSafeLevelAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    hh3cwapiLowSafeLevelAttack.setStatus(
        "current"
    )

hh3cwapiAddressRedirectionAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 77, 4, 0, 5)
)
hh3cwapiAddressRedirectionAttack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoMacAddr"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoAPId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoRadioId"),
        ("HH3C-WAPI-MIB", "hh3cwapiTrapInfoBSSId"))
)
if mibBuilder.loadTexts:
    hh3cwapiAddressRedirectionAttack.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-WAPI-MIB",
    **{"hh3cwapiMIB": hh3cwapiMIB,
       "hh3cwapiMIBObjects": hh3cwapiMIBObjects,
       "hh3cwapiModeEnabled": hh3cwapiModeEnabled,
       "hh3cwapiASIPAddressType": hh3cwapiASIPAddressType,
       "hh3cwapiASIPAddress": hh3cwapiASIPAddress,
       "hh3cwapiCertificateInstalled": hh3cwapiCertificateInstalled,
       "hh3cwapiMIBStatsObjects": hh3cwapiMIBStatsObjects,
       "hh3cwapiStatsWAISignatureErrors": hh3cwapiStatsWAISignatureErrors,
       "hh3cwapiStatsWAIHMACErrors": hh3cwapiStatsWAIHMACErrors,
       "hh3cwapiStatsWAIAuthRsltFailures": hh3cwapiStatsWAIAuthRsltFailures,
       "hh3cwapiStatsWAIDiscardCounters": hh3cwapiStatsWAIDiscardCounters,
       "hh3cwapiStatsWAITimeoutCounters": hh3cwapiStatsWAITimeoutCounters,
       "hh3cwapiStatsWAIFormatErrors": hh3cwapiStatsWAIFormatErrors,
       "hh3cwapiStatsWAICtfHskFailures": hh3cwapiStatsWAICtfHskFailures,
       "hh3cwapiStatsWAIUniHskFailures": hh3cwapiStatsWAIUniHskFailures,
       "hh3cwapiStatsWAIMulHskFailures": hh3cwapiStatsWAIMulHskFailures,
       "hh3cwapiMIBTableObjects": hh3cwapiMIBTableObjects,
       "hh3cwapiConfigTable": hh3cwapiConfigTable,
       "hh3cwapiConfigEntry": hh3cwapiConfigEntry,
       "hh3cwapiConfigASIPAddressType": hh3cwapiConfigASIPAddressType,
       "hh3cwapiConfigASIPAddress": hh3cwapiConfigASIPAddress,
       "hh3cwapiConfigAuthMethod": hh3cwapiConfigAuthMethod,
       "hh3cwapiConfigAuthMode": hh3cwapiConfigAuthMode,
       "hh3cwapiConfigISPDomain": hh3cwapiConfigISPDomain,
       "hh3cwapiConfigCertificateDomain": hh3cwapiConfigCertificateDomain,
       "hh3cwapiConfigASName": hh3cwapiConfigASName,
       "hh3cwapiConfigBKRekeyEnabled": hh3cwapiConfigBKRekeyEnabled,
       "hh3cwapiConfigExtTable": hh3cwapiConfigExtTable,
       "hh3cwapiConfigExtEntry": hh3cwapiConfigExtEntry,
       "hh3cwapiConfigServicePolicyID": hh3cwapiConfigServicePolicyID,
       "hh3cwapiConfigUnicastCipherEnabled": hh3cwapiConfigUnicastCipherEnabled,
       "hh3cwapiConfigUnicastCipherSize": hh3cwapiConfigUnicastCipherSize,
       "hh3cwapiConfigAuthenticationSuiteEnabled": hh3cwapiConfigAuthenticationSuiteEnabled,
       "hh3cwapiConfigAuthenticationSuite": hh3cwapiConfigAuthenticationSuite,
       "hh3cwapiCfgExtASIPAddressType": hh3cwapiCfgExtASIPAddressType,
       "hh3cwapiCfgExtASIPAddress": hh3cwapiCfgExtASIPAddress,
       "hh3cwapiCfgExtASName": hh3cwapiCfgExtASName,
       "hh3cwapiCfgExtCertDomain": hh3cwapiCfgExtCertDomain,
       "hh3cwapiCfgExtCertInstalled": hh3cwapiCfgExtCertInstalled,
       "hh3cwapiTrap": hh3cwapiTrap,
       "hh3cwapiTrapPrefix": hh3cwapiTrapPrefix,
       "hh3cwapiUserwithInvalidCertificate": hh3cwapiUserwithInvalidCertificate,
       "hh3cwapiStationReplayAttack": hh3cwapiStationReplayAttack,
       "hh3cwapiTamperAttack": hh3cwapiTamperAttack,
       "hh3cwapiLowSafeLevelAttack": hh3cwapiLowSafeLevelAttack,
       "hh3cwapiAddressRedirectionAttack": hh3cwapiAddressRedirectionAttack,
       "hh3cwapiTrapInfo": hh3cwapiTrapInfo,
       "hh3cwapiTrapInfoMacAddr": hh3cwapiTrapInfoMacAddr,
       "hh3cwapiTrapInfoAPId": hh3cwapiTrapInfoAPId,
       "hh3cwapiTrapInfoRadioId": hh3cwapiTrapInfoRadioId,
       "hh3cwapiTrapInfoBSSId": hh3cwapiTrapInfoBSSId}
)
