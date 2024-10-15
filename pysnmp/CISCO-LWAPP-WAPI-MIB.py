# SNMP MIB module (CISCO-LWAPP-WAPI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-WAPI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:06 2024
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

(cLApSysMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApSysMacAddress")

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(CLSecKeyFormat,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLSecKeyFormat")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoLwappWapiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997)
)
ciscoLwappWapiMIB.setRevisions(
        ("2010-12-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappWapiMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWapiMIBObjects = _CiscoLwappWapiMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1)
)
_CLWapiWlanStats_Object = MibTable
cLWapiWlanStats = _CLWapiWlanStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1)
)
if mibBuilder.loadTexts:
    cLWapiWlanStats.setStatus("current")
_CLWapiWlanStatsEntry_Object = MibTableRow
cLWapiWlanStatsEntry = _CLWapiWlanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1)
)
cLWapiWlanStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWapiWlanStatsEntry.setStatus("current")
_CLWWSWAISignatureErrors_Type = Counter32
_CLWWSWAISignatureErrors_Object = MibTableColumn
cLWWSWAISignatureErrors = _CLWWSWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 1),
    _CLWWSWAISignatureErrors_Type()
)
cLWWSWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAISignatureErrors.setStatus("current")
_CLWWSWAIHMACErrors_Type = Counter32
_CLWWSWAIHMACErrors_Object = MibTableColumn
cLWWSWAIHMACErrors = _CLWWSWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 2),
    _CLWWSWAIHMACErrors_Type()
)
cLWWSWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIHMACErrors.setStatus("current")
_CLWWSWAIAuthResultFailures_Type = Counter32
_CLWWSWAIAuthResultFailures_Object = MibTableColumn
cLWWSWAIAuthResultFailures = _CLWWSWAIAuthResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 3),
    _CLWWSWAIAuthResultFailures_Type()
)
cLWWSWAIAuthResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIAuthResultFailures.setStatus("current")
_CLWWSWAIDiscardCounters_Type = Counter32
_CLWWSWAIDiscardCounters_Object = MibTableColumn
cLWWSWAIDiscardCounters = _CLWWSWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 4),
    _CLWWSWAIDiscardCounters_Type()
)
cLWWSWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIDiscardCounters.setStatus("current")
_CLWWSWAITimeoutCounters_Type = Counter32
_CLWWSWAITimeoutCounters_Object = MibTableColumn
cLWWSWAITimeoutCounters = _CLWWSWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 5),
    _CLWWSWAITimeoutCounters_Type()
)
cLWWSWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAITimeoutCounters.setStatus("current")
_CLWWSWAIFormatErrors_Type = Counter32
_CLWWSWAIFormatErrors_Object = MibTableColumn
cLWWSWAIFormatErrors = _CLWWSWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 6),
    _CLWWSWAIFormatErrors_Type()
)
cLWWSWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIFormatErrors.setStatus("current")
_CLWWSWAICertHandshakeFailures_Type = Counter32
_CLWWSWAICertHandshakeFailures_Object = MibTableColumn
cLWWSWAICertHandshakeFailures = _CLWWSWAICertHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 7),
    _CLWWSWAICertHandshakeFailures_Type()
)
cLWWSWAICertHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAICertHandshakeFailures.setStatus("current")
_CLWWSWAIUnicastHandshakeFailures_Type = Counter32
_CLWWSWAIUnicastHandshakeFailures_Object = MibTableColumn
cLWWSWAIUnicastHandshakeFailures = _CLWWSWAIUnicastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 8),
    _CLWWSWAIUnicastHandshakeFailures_Type()
)
cLWWSWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIUnicastHandshakeFailures.setStatus("current")
_CLWWSWAIMulticastHandshakeFailures_Type = Counter32
_CLWWSWAIMulticastHandshakeFailures_Object = MibTableColumn
cLWWSWAIMulticastHandshakeFailures = _CLWWSWAIMulticastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 9),
    _CLWWSWAIMulticastHandshakeFailures_Type()
)
cLWWSWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWAIMulticastHandshakeFailures.setStatus("current")
_CLWWSWPIRXReplayCounters_Type = Counter32
_CLWWSWPIRXReplayCounters_Object = MibTableColumn
cLWWSWPIRXReplayCounters = _CLWWSWPIRXReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 10),
    _CLWWSWPIRXReplayCounters_Type()
)
cLWWSWPIRXReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWPIRXReplayCounters.setStatus("current")
_CLWWSWPIRXMicErrorCounters_Type = Counter64
_CLWWSWPIRXMicErrorCounters_Object = MibTableColumn
cLWWSWPIRXMicErrorCounters = _CLWWSWPIRXMicErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 11),
    _CLWWSWPIRXMicErrorCounters_Type()
)
cLWWSWPIRXMicErrorCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWPIRXMicErrorCounters.setStatus("current")
_CLWWSWPIRXDecryptErrorCounters_Type = Counter64
_CLWWSWPIRXDecryptErrorCounters_Object = MibTableColumn
cLWWSWPIRXDecryptErrorCounters = _CLWWSWPIRXDecryptErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 1, 1, 12),
    _CLWWSWPIRXDecryptErrorCounters_Type()
)
cLWWSWPIRXDecryptErrorCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWWSWPIRXDecryptErrorCounters.setStatus("current")
_CLWapiClientStats_Object = MibTable
cLWapiClientStats = _CLWapiClientStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2)
)
if mibBuilder.loadTexts:
    cLWapiClientStats.setStatus("current")
_CLWapiClientStatsEntry_Object = MibTableRow
cLWapiClientStatsEntry = _CLWapiClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1)
)
cLWapiClientStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLWapiClientStatsEntry.setStatus("current")
_CLWCSWapiClientVersion_Type = Integer32
_CLWCSWapiClientVersion_Object = MibTableColumn
cLWCSWapiClientVersion = _CLWCSWapiClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 1),
    _CLWCSWapiClientVersion_Type()
)
cLWCSWapiClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWapiClientVersion.setStatus("current")
_CLWCSWAISignatureErrors_Type = Counter32
_CLWCSWAISignatureErrors_Object = MibTableColumn
cLWCSWAISignatureErrors = _CLWCSWAISignatureErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 2),
    _CLWCSWAISignatureErrors_Type()
)
cLWCSWAISignatureErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAISignatureErrors.setStatus("current")
_CLWCSWAIHMACErrors_Type = Counter32
_CLWCSWAIHMACErrors_Object = MibTableColumn
cLWCSWAIHMACErrors = _CLWCSWAIHMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 3),
    _CLWCSWAIHMACErrors_Type()
)
cLWCSWAIHMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIHMACErrors.setStatus("current")
_CLWCSWAIAuthResultFailures_Type = Counter32
_CLWCSWAIAuthResultFailures_Object = MibTableColumn
cLWCSWAIAuthResultFailures = _CLWCSWAIAuthResultFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 4),
    _CLWCSWAIAuthResultFailures_Type()
)
cLWCSWAIAuthResultFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIAuthResultFailures.setStatus("current")
_CLWCSWAIDiscardCounters_Type = Counter32
_CLWCSWAIDiscardCounters_Object = MibTableColumn
cLWCSWAIDiscardCounters = _CLWCSWAIDiscardCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 5),
    _CLWCSWAIDiscardCounters_Type()
)
cLWCSWAIDiscardCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIDiscardCounters.setStatus("current")
_CLWCSWAITimeoutCounters_Type = Counter32
_CLWCSWAITimeoutCounters_Object = MibTableColumn
cLWCSWAITimeoutCounters = _CLWCSWAITimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 6),
    _CLWCSWAITimeoutCounters_Type()
)
cLWCSWAITimeoutCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAITimeoutCounters.setStatus("current")
_CLWCSWAIFormatErrors_Type = Counter32
_CLWCSWAIFormatErrors_Object = MibTableColumn
cLWCSWAIFormatErrors = _CLWCSWAIFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 7),
    _CLWCSWAIFormatErrors_Type()
)
cLWCSWAIFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIFormatErrors.setStatus("current")
_CLWCSWAICertHandshakeFailures_Type = Counter32
_CLWCSWAICertHandshakeFailures_Object = MibTableColumn
cLWCSWAICertHandshakeFailures = _CLWCSWAICertHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 8),
    _CLWCSWAICertHandshakeFailures_Type()
)
cLWCSWAICertHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAICertHandshakeFailures.setStatus("current")
_CLWCSWAIUnicastHandshakeFailures_Type = Counter32
_CLWCSWAIUnicastHandshakeFailures_Object = MibTableColumn
cLWCSWAIUnicastHandshakeFailures = _CLWCSWAIUnicastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 9),
    _CLWCSWAIUnicastHandshakeFailures_Type()
)
cLWCSWAIUnicastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIUnicastHandshakeFailures.setStatus("current")
_CLWCSWAIMulticastHandshakeFailures_Type = Counter32
_CLWCSWAIMulticastHandshakeFailures_Object = MibTableColumn
cLWCSWAIMulticastHandshakeFailures = _CLWCSWAIMulticastHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 10),
    _CLWCSWAIMulticastHandshakeFailures_Type()
)
cLWCSWAIMulticastHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIMulticastHandshakeFailures.setStatus("current")


class _CLWCSWAIUnicastCipherSuite_Type(OctetString):
    """Custom type cLWCSWAIUnicastCipherSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWAIUnicastCipherSuite_Type.__name__ = "OctetString"
_CLWCSWAIUnicastCipherSuite_Object = MibTableColumn
cLWCSWAIUnicastCipherSuite = _CLWCSWAIUnicastCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 11),
    _CLWCSWAIUnicastCipherSuite_Type()
)
cLWCSWAIUnicastCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIUnicastCipherSuite.setStatus("current")


class _CLWCSWAIMcastCipherSuite_Type(OctetString):
    """Custom type cLWCSWAIMcastCipherSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWAIMcastCipherSuite_Type.__name__ = "OctetString"
_CLWCSWAIMcastCipherSuite_Object = MibTableColumn
cLWCSWAIMcastCipherSuite = _CLWCSWAIMcastCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 12),
    _CLWCSWAIMcastCipherSuite_Type()
)
cLWCSWAIMcastCipherSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIMcastCipherSuite.setStatus("current")


class _CLWCSWAIAuthenticationSuiteRequested_Type(OctetString):
    """Custom type cLWCSWAIAuthenticationSuiteRequested based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWAIAuthenticationSuiteRequested_Type.__name__ = "OctetString"
_CLWCSWAIAuthenticationSuiteRequested_Object = MibTableColumn
cLWCSWAIAuthenticationSuiteRequested = _CLWCSWAIAuthenticationSuiteRequested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 13),
    _CLWCSWAIAuthenticationSuiteRequested_Type()
)
cLWCSWAIAuthenticationSuiteRequested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIAuthenticationSuiteRequested.setStatus("current")


class _CLWCSWAIBKIDUsed_Type(OctetString):
    """Custom type cLWCSWAIBKIDUsed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CLWCSWAIBKIDUsed_Type.__name__ = "OctetString"
_CLWCSWAIBKIDUsed_Object = MibTableColumn
cLWCSWAIBKIDUsed = _CLWCSWAIBKIDUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 14),
    _CLWCSWAIBKIDUsed_Type()
)
cLWCSWAIBKIDUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAIBKIDUsed.setStatus("current")
_CLWCSWAICtrPortState_Type = TruthValue
_CLWCSWAICtrPortState_Object = MibTableColumn
cLWCSWAICtrPortState = _CLWCSWAICtrPortState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 2, 1, 15),
    _CLWCSWAICtrPortState_Type()
)
cLWCSWAICtrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWAICtrPortState.setStatus("current")
_CLWapiWlanConfig_Object = MibTable
cLWapiWlanConfig = _CLWapiWlanConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3)
)
if mibBuilder.loadTexts:
    cLWapiWlanConfig.setStatus("current")
_CLWapiWlanConfigEntrty_Object = MibTableRow
cLWapiWlanConfigEntrty = _CLWapiWlanConfigEntrty_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1)
)
cLWapiWlanConfigEntrty.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLWapiWlanConfigEntrty.setStatus("current")
_CLWCSWlanWapiEnable_Type = TruthValue
_CLWCSWlanWapiEnable_Object = MibTableColumn
cLWCSWlanWapiEnable = _CLWCSWlanWapiEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 1),
    _CLWCSWlanWapiEnable_Type()
)
cLWCSWlanWapiEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiEnable.setStatus("current")


class _CLWCSWlanWapiAkmKeyMgmtMode_Type(Integer32):
    """Custom type cLWCSWlanWapiAkmKeyMgmtMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cert", 1),
          ("invalid", 0),
          ("psk", 2))
    )


_CLWCSWlanWapiAkmKeyMgmtMode_Type.__name__ = "Integer32"
_CLWCSWlanWapiAkmKeyMgmtMode_Object = MibTableColumn
cLWCSWlanWapiAkmKeyMgmtMode = _CLWCSWlanWapiAkmKeyMgmtMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 2),
    _CLWCSWlanWapiAkmKeyMgmtMode_Type()
)
cLWCSWlanWapiAkmKeyMgmtMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiAkmKeyMgmtMode.setStatus("current")


class _CLWCSWlanWapiEncryptType_Type(Bits):
    """Custom type cLWCSWlanWapiEncryptType based on Bits"""
    namedValues = NamedValues(
        ("sms4", 0)
    )

_CLWCSWlanWapiEncryptType_Type.__name__ = "Bits"
_CLWCSWlanWapiEncryptType_Object = MibTableColumn
cLWCSWlanWapiEncryptType = _CLWCSWlanWapiEncryptType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 3),
    _CLWCSWlanWapiEncryptType_Type()
)
cLWCSWlanWapiEncryptType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiEncryptType.setStatus("current")


class _CLWCSWlanWapiPskFmt_Type(CLSecKeyFormat):
    """Custom type cLWCSWlanWapiPskFmt based on CLSecKeyFormat"""


_CLWCSWlanWapiPskFmt_Object = MibTableColumn
cLWCSWlanWapiPskFmt = _CLWCSWlanWapiPskFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 4),
    _CLWCSWlanWapiPskFmt_Type()
)
cLWCSWlanWapiPskFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiPskFmt.setStatus("current")


class _CLWCSWlanWapiPsk_Type(OctetString):
    """Custom type cLWCSWlanWapiPsk based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 80),
    )


_CLWCSWlanWapiPsk_Type.__name__ = "OctetString"
_CLWCSWlanWapiPsk_Object = MibTableColumn
cLWCSWlanWapiPsk = _CLWCSWlanWapiPsk_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 5),
    _CLWCSWlanWapiPsk_Type()
)
cLWCSWlanWapiPsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiPsk.setStatus("current")


class _CLWCSWlanWapiConfigUnicasCiphersEntry_Type(OctetString):
    """Custom type cLWCSWlanWapiConfigUnicasCiphersEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiConfigUnicasCiphersEntry_Type.__name__ = "OctetString"
_CLWCSWlanWapiConfigUnicasCiphersEntry_Object = MibTableColumn
cLWCSWlanWapiConfigUnicasCiphersEntry = _CLWCSWlanWapiConfigUnicasCiphersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 6),
    _CLWCSWlanWapiConfigUnicasCiphersEntry_Type()
)
cLWCSWlanWapiConfigUnicasCiphersEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiConfigUnicasCiphersEntry.setStatus("current")
_CLWCSWlanWapiConfigUnicastCipherSize_Type = Unsigned32
_CLWCSWlanWapiConfigUnicastCipherSize_Object = MibTableColumn
cLWCSWlanWapiConfigUnicastCipherSize = _CLWCSWlanWapiConfigUnicastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 7),
    _CLWCSWlanWapiConfigUnicastCipherSize_Type()
)
cLWCSWlanWapiConfigUnicastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiConfigUnicastCipherSize.setStatus("current")
_CLWCSWlanWapiMcastCipherSize_Type = Unsigned32
_CLWCSWlanWapiMcastCipherSize_Object = MibTableColumn
cLWCSWlanWapiMcastCipherSize = _CLWCSWlanWapiMcastCipherSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 8),
    _CLWCSWlanWapiMcastCipherSize_Type()
)
cLWCSWlanWapiMcastCipherSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiMcastCipherSize.setStatus("current")


class _CLWCSWlanBKLifeTime_Type(Unsigned32):
    """Custom type cLWCSWlanBKLifeTime based on Unsigned32"""
    defaultValue = 43200


_CLWCSWlanBKLifeTime_Object = MibTableColumn
cLWCSWlanBKLifeTime = _CLWCSWlanBKLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 9),
    _CLWCSWlanBKLifeTime_Type()
)
cLWCSWlanBKLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanBKLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    cLWCSWlanBKLifeTime.setUnits("seconds")


class _CLWCSWlanBKReauthThreshold_Type(Unsigned32):
    """Custom type cLWCSWlanBKReauthThreshold based on Unsigned32"""
    defaultValue = 70


_CLWCSWlanBKReauthThreshold_Object = MibTableColumn
cLWCSWlanBKReauthThreshold = _CLWCSWlanBKReauthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 10),
    _CLWCSWlanBKReauthThreshold_Type()
)
cLWCSWlanBKReauthThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanBKReauthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cLWCSWlanBKReauthThreshold.setUnits("percentage")


class _CLWCSWlanWapiConfigMulticastCipher_Type(OctetString):
    """Custom type cLWCSWlanWapiConfigMulticastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiConfigMulticastCipher_Type.__name__ = "OctetString"
_CLWCSWlanWapiConfigMulticastCipher_Object = MibTableColumn
cLWCSWlanWapiConfigMulticastCipher = _CLWCSWlanWapiConfigMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 11),
    _CLWCSWlanWapiConfigMulticastCipher_Type()
)
cLWCSWlanWapiConfigMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiConfigMulticastCipher.setStatus("current")


class _CLWCSWlanWapiAuthenticationSuiteSelected_Type(OctetString):
    """Custom type cLWCSWlanWapiAuthenticationSuiteSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiAuthenticationSuiteSelected_Type.__name__ = "OctetString"
_CLWCSWlanWapiAuthenticationSuiteSelected_Object = MibTableColumn
cLWCSWlanWapiAuthenticationSuiteSelected = _CLWCSWlanWapiAuthenticationSuiteSelected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 12),
    _CLWCSWlanWapiAuthenticationSuiteSelected_Type()
)
cLWCSWlanWapiAuthenticationSuiteSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiAuthenticationSuiteSelected.setStatus("current")


class _CLWCSWlanWapiUnicastCipherSelected_Type(OctetString):
    """Custom type cLWCSWlanWapiUnicastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiUnicastCipherSelected_Type.__name__ = "OctetString"
_CLWCSWlanWapiUnicastCipherSelected_Object = MibTableColumn
cLWCSWlanWapiUnicastCipherSelected = _CLWCSWlanWapiUnicastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 13),
    _CLWCSWlanWapiUnicastCipherSelected_Type()
)
cLWCSWlanWapiUnicastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiUnicastCipherSelected.setStatus("current")


class _CLWCSWlanWapiMulticastCipherSelected_Type(OctetString):
    """Custom type cLWCSWlanWapiMulticastCipherSelected based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiMulticastCipherSelected_Type.__name__ = "OctetString"
_CLWCSWlanWapiMulticastCipherSelected_Object = MibTableColumn
cLWCSWlanWapiMulticastCipherSelected = _CLWCSWlanWapiMulticastCipherSelected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 14),
    _CLWCSWlanWapiMulticastCipherSelected_Type()
)
cLWCSWlanWapiMulticastCipherSelected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiMulticastCipherSelected.setStatus("current")
_CLWCSWlanWapiPreauthenticationState_Type = TruthValue
_CLWCSWlanWapiPreauthenticationState_Object = MibTableColumn
cLWCSWlanWapiPreauthenticationState = _CLWCSWlanWapiPreauthenticationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 3, 1, 15),
    _CLWCSWlanWapiPreauthenticationState_Type()
)
cLWCSWlanWapiPreauthenticationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiPreauthenticationState.setStatus("current")
_CLWapiAPTable_Object = MibTable
cLWapiAPTable = _CLWapiAPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4)
)
if mibBuilder.loadTexts:
    cLWapiAPTable.setStatus("current")
_CLWapiAPEntry_Object = MibTableRow
cLWapiAPEntry = _CLWapiAPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4, 1)
)
cLWapiAPEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    cLWapiAPEntry.setStatus("current")
_CLWCSWapiAPMaxUnicastKeysSupport_Type = Integer32
_CLWCSWapiAPMaxUnicastKeysSupport_Object = MibTableColumn
cLWCSWapiAPMaxUnicastKeysSupport = _CLWCSWapiAPMaxUnicastKeysSupport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 4, 1, 1),
    _CLWCSWapiAPMaxUnicastKeysSupport_Type()
)
cLWCSWapiAPMaxUnicastKeysSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWapiAPMaxUnicastKeysSupport.setStatus("current")
_CLWapiWlanAKMSuitesConfigTable_Object = MibTable
cLWapiWlanAKMSuitesConfigTable = _CLWapiWlanAKMSuitesConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5)
)
if mibBuilder.loadTexts:
    cLWapiWlanAKMSuitesConfigTable.setStatus("current")
_CLWapiWlanAKMSuitesConfigEntry_Object = MibTableRow
cLWapiWlanAKMSuitesConfigEntry = _CLWapiWlanAKMSuitesConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1)
)
cLWapiWlanAKMSuitesConfigEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WAPI-MIB", "cLWCSWlanWapiAuthenticationSuiteIndex"),
)
if mibBuilder.loadTexts:
    cLWapiWlanAKMSuitesConfigEntry.setStatus("current")


class _CLWCSWlanWapiAuthenticationSuiteIndex_Type(Integer32):
    """Custom type cLWCSWlanWapiAuthenticationSuiteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cert", 1),
          ("psk", 2))
    )


_CLWCSWlanWapiAuthenticationSuiteIndex_Type.__name__ = "Integer32"
_CLWCSWlanWapiAuthenticationSuiteIndex_Object = MibTableColumn
cLWCSWlanWapiAuthenticationSuiteIndex = _CLWCSWlanWapiAuthenticationSuiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 1),
    _CLWCSWlanWapiAuthenticationSuiteIndex_Type()
)
cLWCSWlanWapiAuthenticationSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWCSWlanWapiAuthenticationSuiteIndex.setStatus("current")


class _CLWCSWlanWapiAuthenticationSuite_Type(OctetString):
    """Custom type cLWCSWlanWapiAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CLWCSWlanWapiAuthenticationSuite_Type.__name__ = "OctetString"
_CLWCSWlanWapiAuthenticationSuite_Object = MibTableColumn
cLWCSWlanWapiAuthenticationSuite = _CLWCSWlanWapiAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 2),
    _CLWCSWlanWapiAuthenticationSuite_Type()
)
cLWCSWlanWapiAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWlanWapiAuthenticationSuite.setStatus("current")
_CLWCSWlanWapiAuthenticationSuiteEnable_Type = TruthValue
_CLWCSWlanWapiAuthenticationSuiteEnable_Object = MibTableColumn
cLWCSWlanWapiAuthenticationSuiteEnable = _CLWCSWlanWapiAuthenticationSuiteEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 5, 1, 3),
    _CLWCSWlanWapiAuthenticationSuiteEnable_Type()
)
cLWCSWlanWapiAuthenticationSuiteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanWapiAuthenticationSuiteEnable.setStatus("current")
_CLWapiCiphers_Object = MibTable
cLWapiCiphers = _CLWapiCiphers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6)
)
if mibBuilder.loadTexts:
    cLWapiCiphers.setStatus("current")
_CLWapiCiphersEntry_Object = MibTableRow
cLWapiCiphersEntry = _CLWapiCiphersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1)
)
cLWapiCiphersEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
    (0, "CISCO-LWAPP-WAPI-MIB", "cLWCSWlanCipherIndex"),
)
if mibBuilder.loadTexts:
    cLWapiCiphersEntry.setStatus("current")
_CLWCSWlanCipherIndex_Type = Unsigned32
_CLWCSWlanCipherIndex_Object = MibTableColumn
cLWCSWlanCipherIndex = _CLWCSWlanCipherIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1, 1),
    _CLWCSWlanCipherIndex_Type()
)
cLWCSWlanCipherIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cLWCSWlanCipherIndex.setStatus("current")
_CLWCSWlanCipherEnabled_Type = TruthValue
_CLWCSWlanCipherEnabled_Object = MibTableColumn
cLWCSWlanCipherEnabled = _CLWCSWlanCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 1, 6, 1, 2),
    _CLWCSWlanCipherEnabled_Type()
)
cLWCSWlanCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLWCSWlanCipherEnabled.setStatus("current")
_CiscoLwappWapiConfig_ObjectIdentity = ObjectIdentity
ciscoLwappWapiConfig = _CiscoLwappWapiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2)
)
_ClWapiASIpAddress_Type = IpAddress
_ClWapiASIpAddress_Object = MibScalar
clWapiASIpAddress = _ClWapiASIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 1),
    _ClWapiASIpAddress_Type()
)
clWapiASIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiASIpAddress.setStatus("current")
_ClWapiASPortNumber_Type = Integer32
_ClWapiASPortNumber_Object = MibScalar
clWapiASPortNumber = _ClWapiASPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 2),
    _ClWapiASPortNumber_Type()
)
clWapiASPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiASPortNumber.setStatus("current")
_ClWapiASRequestTimeout_Type = Integer32
_ClWapiASRequestTimeout_Object = MibScalar
clWapiASRequestTimeout = _ClWapiASRequestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 3),
    _ClWapiASRequestTimeout_Type()
)
clWapiASRequestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiASRequestTimeout.setStatus("current")


class _ClWapiMulticastRekeyMethod_Type(Integer32):
    """Custom type clWapiMulticastRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("messageBased", 3),
          ("timeBased", 2),
          ("timemessageBased", 4))
    )


_ClWapiMulticastRekeyMethod_Type.__name__ = "Integer32"
_ClWapiMulticastRekeyMethod_Object = MibScalar
clWapiMulticastRekeyMethod = _ClWapiMulticastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 4),
    _ClWapiMulticastRekeyMethod_Type()
)
clWapiMulticastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiMulticastRekeyMethod.setStatus("current")


class _ClWapiMulticastRekeyTime_Type(Unsigned32):
    """Custom type clWapiMulticastRekeyTime based on Unsigned32"""
    defaultValue = 86400


_ClWapiMulticastRekeyTime_Object = MibScalar
clWapiMulticastRekeyTime = _ClWapiMulticastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 5),
    _ClWapiMulticastRekeyTime_Type()
)
clWapiMulticastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiMulticastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    clWapiMulticastRekeyTime.setUnits("seconds")
_ClWapiMulticastRekeyMessages_Type = Unsigned32
_ClWapiMulticastRekeyMessages_Object = MibScalar
clWapiMulticastRekeyMessages = _ClWapiMulticastRekeyMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 6),
    _ClWapiMulticastRekeyMessages_Type()
)
clWapiMulticastRekeyMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiMulticastRekeyMessages.setStatus("current")
_ClWapiMulticastRekeyStrict_Type = TruthValue
_ClWapiMulticastRekeyStrict_Object = MibScalar
clWapiMulticastRekeyStrict = _ClWapiMulticastRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 7),
    _ClWapiMulticastRekeyStrict_Type()
)
clWapiMulticastRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiMulticastRekeyStrict.setStatus("current")


class _ClWapiConfigCertificateUpdateCount_Type(Unsigned32):
    """Custom type clWapiConfigCertificateUpdateCount based on Unsigned32"""
    defaultValue = 3


_ClWapiConfigCertificateUpdateCount_Object = MibScalar
clWapiConfigCertificateUpdateCount = _ClWapiConfigCertificateUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 8),
    _ClWapiConfigCertificateUpdateCount_Type()
)
clWapiConfigCertificateUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiConfigCertificateUpdateCount.setStatus("current")


class _ClWapiConfigMulticastUpdateCount_Type(Unsigned32):
    """Custom type clWapiConfigMulticastUpdateCount based on Unsigned32"""
    defaultValue = 3


_ClWapiConfigMulticastUpdateCount_Object = MibScalar
clWapiConfigMulticastUpdateCount = _ClWapiConfigMulticastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 9),
    _ClWapiConfigMulticastUpdateCount_Type()
)
clWapiConfigMulticastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiConfigMulticastUpdateCount.setStatus("current")


class _ClWapiConfigUnicastUpdateCount_Type(Unsigned32):
    """Custom type clWapiConfigUnicastUpdateCount based on Unsigned32"""
    defaultValue = 3


_ClWapiConfigUnicastUpdateCount_Object = MibScalar
clWapiConfigUnicastUpdateCount = _ClWapiConfigUnicastUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 10),
    _ClWapiConfigUnicastUpdateCount_Type()
)
clWapiConfigUnicastUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiConfigUnicastUpdateCount.setStatus("current")
_CLWCSWapiConfigureVersion_Type = Integer32
_CLWCSWapiConfigureVersion_Object = MibScalar
cLWCSWapiConfigureVersion = _CLWCSWapiConfigureVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 11),
    _CLWCSWapiConfigureVersion_Type()
)
cLWCSWapiConfigureVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLWCSWapiConfigureVersion.setStatus("current")


class _ClWapiConfigControlledPortControl_Type(Integer32):
    """Custom type clWapiConfigControlledPortControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("auto", 0)
    )


_ClWapiConfigControlledPortControl_Type.__name__ = "Integer32"
_ClWapiConfigControlledPortControl_Object = MibScalar
clWapiConfigControlledPortControl = _ClWapiConfigControlledPortControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 12),
    _ClWapiConfigControlledPortControl_Type()
)
clWapiConfigControlledPortControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiConfigControlledPortControl.setStatus("current")
_ClWapiUserInvalidCertificationInbreakNetwork_Type = DisplayString
_ClWapiUserInvalidCertificationInbreakNetwork_Object = MibScalar
clWapiUserInvalidCertificationInbreakNetwork = _ClWapiUserInvalidCertificationInbreakNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 13),
    _ClWapiUserInvalidCertificationInbreakNetwork_Type()
)
clWapiUserInvalidCertificationInbreakNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiUserInvalidCertificationInbreakNetwork.setStatus("current")
_CLApWAPISecurityLowAttack_Type = DisplayString
_CLApWAPISecurityLowAttack_Object = MibScalar
cLApWAPISecurityLowAttack = _CLApWAPISecurityLowAttack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 14),
    _CLApWAPISecurityLowAttack_Type()
)
cLApWAPISecurityLowAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWAPISecurityLowAttack.setStatus("current")


class _ClWapiUnicastRekeyMethod_Type(Integer32):
    """Custom type clWapiUnicastRekeyMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("messageBased", 3),
          ("timeBased", 2),
          ("timeMessageBased", 4))
    )


_ClWapiUnicastRekeyMethod_Type.__name__ = "Integer32"
_ClWapiUnicastRekeyMethod_Object = MibScalar
clWapiUnicastRekeyMethod = _ClWapiUnicastRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 15),
    _ClWapiUnicastRekeyMethod_Type()
)
clWapiUnicastRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiUnicastRekeyMethod.setStatus("current")


class _ClWapiUnicastRekeyTime_Type(Unsigned32):
    """Custom type clWapiUnicastRekeyTime based on Unsigned32"""
    defaultValue = 86400


_ClWapiUnicastRekeyTime_Object = MibScalar
clWapiUnicastRekeyTime = _ClWapiUnicastRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 16),
    _ClWapiUnicastRekeyTime_Type()
)
clWapiUnicastRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiUnicastRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    clWapiUnicastRekeyTime.setUnits("seconds")
_ClWapiUnicastRekeyMessage_Type = Unsigned32
_ClWapiUnicastRekeyMessage_Object = MibScalar
clWapiUnicastRekeyMessage = _ClWapiUnicastRekeyMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 17),
    _ClWapiUnicastRekeyMessage_Type()
)
clWapiUnicastRekeyMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiUnicastRekeyMessage.setStatus("current")
if mibBuilder.loadTexts:
    clWapiUnicastRekeyMessage.setUnits("1000 messages")


class _ClWapiConfigSATimeout_Type(Unsigned32):
    """Custom type clWapiConfigSATimeout based on Unsigned32"""
    defaultValue = 60


_ClWapiConfigSATimeout_Object = MibScalar
clWapiConfigSATimeout = _ClWapiConfigSATimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 18),
    _ClWapiConfigSATimeout_Type()
)
clWapiConfigSATimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clWapiConfigSATimeout.setStatus("current")
if mibBuilder.loadTexts:
    clWapiConfigSATimeout.setUnits("seconds")
_CLApWAPIReplayAttack_Type = DisplayString
_CLApWAPIReplayAttack_Object = MibScalar
cLApWAPIReplayAttack = _CLApWAPIReplayAttack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 19),
    _CLApWAPIReplayAttack_Type()
)
cLApWAPIReplayAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWAPIReplayAttack.setStatus("current")
_CLApWAPITamperAttack_Type = DisplayString
_CLApWAPITamperAttack_Object = MibScalar
cLApWAPITamperAttack = _CLApWAPITamperAttack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 20),
    _CLApWAPITamperAttack_Type()
)
cLApWAPITamperAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLApWAPITamperAttack.setStatus("current")
_ClWapiAddressRedirectAttack_Type = DisplayString
_ClWapiAddressRedirectAttack_Object = MibScalar
clWapiAddressRedirectAttack = _ClWapiAddressRedirectAttack_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 2, 21),
    _ClWapiAddressRedirectAttack_Type()
)
clWapiAddressRedirectAttack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiAddressRedirectAttack.setStatus("current")
_CiscoLwappWapiCertificateObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWapiCertificateObjects = _CiscoLwappWapiCertificateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 3)
)
_ClWapiWLCCertificateStatus_Type = TruthValue
_ClWapiWLCCertificateStatus_Object = MibScalar
clWapiWLCCertificateStatus = _ClWapiWLCCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 1),
    _ClWapiWLCCertificateStatus_Type()
)
clWapiWLCCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiWLCCertificateStatus.setStatus("current")
_ClWapiCACertificateStatus_Type = TruthValue
_ClWapiCACertificateStatus_Object = MibScalar
clWapiCACertificateStatus = _ClWapiCACertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 2),
    _ClWapiCACertificateStatus_Type()
)
clWapiCACertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiCACertificateStatus.setStatus("current")
_ClWapiASCertificateStatus_Type = TruthValue
_ClWapiASCertificateStatus_Object = MibScalar
clWapiASCertificateStatus = _ClWapiASCertificateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 3, 3),
    _ClWapiASCertificateStatus_Type()
)
clWapiASCertificateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clWapiASCertificateStatus.setStatus("current")
_CiscoLwappWapiMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappWapiMIBNotifObjects = _CiscoLwappWapiMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4)
)

# Managed Objects groups


# Notification objects

ciscoLwappWapiUserInvalidCertificateNetworkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 1)
)
ciscoLwappWapiUserInvalidCertificateNetworkTrap.setObjects(
    ("CISCO-LWAPP-WAPI-MIB", "clWapiUserInvalidCertificationInbreakNetwork")
)
if mibBuilder.loadTexts:
    ciscoLwappWapiUserInvalidCertificateNetworkTrap.setStatus(
        "current"
    )

ciscoLwappWapiSecurityLowAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 2)
)
ciscoLwappWapiSecurityLowAttackTrap.setObjects(
    ("CISCO-LWAPP-WAPI-MIB", "cLApWAPISecurityLowAttack")
)
if mibBuilder.loadTexts:
    ciscoLwappWapiSecurityLowAttackTrap.setStatus(
        "current"
    )

ciscoLwappWapiReplayAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 3)
)
ciscoLwappWapiReplayAttackTrap.setObjects(
    ("CISCO-LWAPP-WAPI-MIB", "cLApWAPIReplayAttack")
)
if mibBuilder.loadTexts:
    ciscoLwappWapiReplayAttackTrap.setStatus(
        "current"
    )

ciscoLwappWapiTamperAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 4)
)
ciscoLwappWapiTamperAttackTrap.setObjects(
    ("CISCO-LWAPP-WAPI-MIB", "cLApWAPITamperAttack")
)
if mibBuilder.loadTexts:
    ciscoLwappWapiTamperAttackTrap.setStatus(
        "current"
    )

ciscoLwappWapiAddressRedirectAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 9997, 4, 5)
)
ciscoLwappWapiAddressRedirectAttackTrap.setObjects(
    ("CISCO-LWAPP-WAPI-MIB", "clWapiAddressRedirectAttack")
)
if mibBuilder.loadTexts:
    ciscoLwappWapiAddressRedirectAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-WAPI-MIB",
    **{"ciscoLwappWapiMIB": ciscoLwappWapiMIB,
       "ciscoLwappWapiMIBObjects": ciscoLwappWapiMIBObjects,
       "cLWapiWlanStats": cLWapiWlanStats,
       "cLWapiWlanStatsEntry": cLWapiWlanStatsEntry,
       "cLWWSWAISignatureErrors": cLWWSWAISignatureErrors,
       "cLWWSWAIHMACErrors": cLWWSWAIHMACErrors,
       "cLWWSWAIAuthResultFailures": cLWWSWAIAuthResultFailures,
       "cLWWSWAIDiscardCounters": cLWWSWAIDiscardCounters,
       "cLWWSWAITimeoutCounters": cLWWSWAITimeoutCounters,
       "cLWWSWAIFormatErrors": cLWWSWAIFormatErrors,
       "cLWWSWAICertHandshakeFailures": cLWWSWAICertHandshakeFailures,
       "cLWWSWAIUnicastHandshakeFailures": cLWWSWAIUnicastHandshakeFailures,
       "cLWWSWAIMulticastHandshakeFailures": cLWWSWAIMulticastHandshakeFailures,
       "cLWWSWPIRXReplayCounters": cLWWSWPIRXReplayCounters,
       "cLWWSWPIRXMicErrorCounters": cLWWSWPIRXMicErrorCounters,
       "cLWWSWPIRXDecryptErrorCounters": cLWWSWPIRXDecryptErrorCounters,
       "cLWapiClientStats": cLWapiClientStats,
       "cLWapiClientStatsEntry": cLWapiClientStatsEntry,
       "cLWCSWapiClientVersion": cLWCSWapiClientVersion,
       "cLWCSWAISignatureErrors": cLWCSWAISignatureErrors,
       "cLWCSWAIHMACErrors": cLWCSWAIHMACErrors,
       "cLWCSWAIAuthResultFailures": cLWCSWAIAuthResultFailures,
       "cLWCSWAIDiscardCounters": cLWCSWAIDiscardCounters,
       "cLWCSWAITimeoutCounters": cLWCSWAITimeoutCounters,
       "cLWCSWAIFormatErrors": cLWCSWAIFormatErrors,
       "cLWCSWAICertHandshakeFailures": cLWCSWAICertHandshakeFailures,
       "cLWCSWAIUnicastHandshakeFailures": cLWCSWAIUnicastHandshakeFailures,
       "cLWCSWAIMulticastHandshakeFailures": cLWCSWAIMulticastHandshakeFailures,
       "cLWCSWAIUnicastCipherSuite": cLWCSWAIUnicastCipherSuite,
       "cLWCSWAIMcastCipherSuite": cLWCSWAIMcastCipherSuite,
       "cLWCSWAIAuthenticationSuiteRequested": cLWCSWAIAuthenticationSuiteRequested,
       "cLWCSWAIBKIDUsed": cLWCSWAIBKIDUsed,
       "cLWCSWAICtrPortState": cLWCSWAICtrPortState,
       "cLWapiWlanConfig": cLWapiWlanConfig,
       "cLWapiWlanConfigEntrty": cLWapiWlanConfigEntrty,
       "cLWCSWlanWapiEnable": cLWCSWlanWapiEnable,
       "cLWCSWlanWapiAkmKeyMgmtMode": cLWCSWlanWapiAkmKeyMgmtMode,
       "cLWCSWlanWapiEncryptType": cLWCSWlanWapiEncryptType,
       "cLWCSWlanWapiPskFmt": cLWCSWlanWapiPskFmt,
       "cLWCSWlanWapiPsk": cLWCSWlanWapiPsk,
       "cLWCSWlanWapiConfigUnicasCiphersEntry": cLWCSWlanWapiConfigUnicasCiphersEntry,
       "cLWCSWlanWapiConfigUnicastCipherSize": cLWCSWlanWapiConfigUnicastCipherSize,
       "cLWCSWlanWapiMcastCipherSize": cLWCSWlanWapiMcastCipherSize,
       "cLWCSWlanBKLifeTime": cLWCSWlanBKLifeTime,
       "cLWCSWlanBKReauthThreshold": cLWCSWlanBKReauthThreshold,
       "cLWCSWlanWapiConfigMulticastCipher": cLWCSWlanWapiConfigMulticastCipher,
       "cLWCSWlanWapiAuthenticationSuiteSelected": cLWCSWlanWapiAuthenticationSuiteSelected,
       "cLWCSWlanWapiUnicastCipherSelected": cLWCSWlanWapiUnicastCipherSelected,
       "cLWCSWlanWapiMulticastCipherSelected": cLWCSWlanWapiMulticastCipherSelected,
       "cLWCSWlanWapiPreauthenticationState": cLWCSWlanWapiPreauthenticationState,
       "cLWapiAPTable": cLWapiAPTable,
       "cLWapiAPEntry": cLWapiAPEntry,
       "cLWCSWapiAPMaxUnicastKeysSupport": cLWCSWapiAPMaxUnicastKeysSupport,
       "cLWapiWlanAKMSuitesConfigTable": cLWapiWlanAKMSuitesConfigTable,
       "cLWapiWlanAKMSuitesConfigEntry": cLWapiWlanAKMSuitesConfigEntry,
       "cLWCSWlanWapiAuthenticationSuiteIndex": cLWCSWlanWapiAuthenticationSuiteIndex,
       "cLWCSWlanWapiAuthenticationSuite": cLWCSWlanWapiAuthenticationSuite,
       "cLWCSWlanWapiAuthenticationSuiteEnable": cLWCSWlanWapiAuthenticationSuiteEnable,
       "cLWapiCiphers": cLWapiCiphers,
       "cLWapiCiphersEntry": cLWapiCiphersEntry,
       "cLWCSWlanCipherIndex": cLWCSWlanCipherIndex,
       "cLWCSWlanCipherEnabled": cLWCSWlanCipherEnabled,
       "ciscoLwappWapiConfig": ciscoLwappWapiConfig,
       "clWapiASIpAddress": clWapiASIpAddress,
       "clWapiASPortNumber": clWapiASPortNumber,
       "clWapiASRequestTimeout": clWapiASRequestTimeout,
       "clWapiMulticastRekeyMethod": clWapiMulticastRekeyMethod,
       "clWapiMulticastRekeyTime": clWapiMulticastRekeyTime,
       "clWapiMulticastRekeyMessages": clWapiMulticastRekeyMessages,
       "clWapiMulticastRekeyStrict": clWapiMulticastRekeyStrict,
       "clWapiConfigCertificateUpdateCount": clWapiConfigCertificateUpdateCount,
       "clWapiConfigMulticastUpdateCount": clWapiConfigMulticastUpdateCount,
       "clWapiConfigUnicastUpdateCount": clWapiConfigUnicastUpdateCount,
       "cLWCSWapiConfigureVersion": cLWCSWapiConfigureVersion,
       "clWapiConfigControlledPortControl": clWapiConfigControlledPortControl,
       "clWapiUserInvalidCertificationInbreakNetwork": clWapiUserInvalidCertificationInbreakNetwork,
       "cLApWAPISecurityLowAttack": cLApWAPISecurityLowAttack,
       "clWapiUnicastRekeyMethod": clWapiUnicastRekeyMethod,
       "clWapiUnicastRekeyTime": clWapiUnicastRekeyTime,
       "clWapiUnicastRekeyMessage": clWapiUnicastRekeyMessage,
       "clWapiConfigSATimeout": clWapiConfigSATimeout,
       "cLApWAPIReplayAttack": cLApWAPIReplayAttack,
       "cLApWAPITamperAttack": cLApWAPITamperAttack,
       "clWapiAddressRedirectAttack": clWapiAddressRedirectAttack,
       "ciscoLwappWapiCertificateObjects": ciscoLwappWapiCertificateObjects,
       "clWapiWLCCertificateStatus": clWapiWLCCertificateStatus,
       "clWapiCACertificateStatus": clWapiCACertificateStatus,
       "clWapiASCertificateStatus": clWapiASCertificateStatus,
       "ciscoLwappWapiMIBNotifObjects": ciscoLwappWapiMIBNotifObjects,
       "ciscoLwappWapiUserInvalidCertificateNetworkTrap": ciscoLwappWapiUserInvalidCertificateNetworkTrap,
       "ciscoLwappWapiSecurityLowAttackTrap": ciscoLwappWapiSecurityLowAttackTrap,
       "ciscoLwappWapiReplayAttackTrap": ciscoLwappWapiReplayAttackTrap,
       "ciscoLwappWapiTamperAttackTrap": ciscoLwappWapiTamperAttackTrap,
       "ciscoLwappWapiAddressRedirectAttackTrap": ciscoLwappWapiAddressRedirectAttackTrap}
)
