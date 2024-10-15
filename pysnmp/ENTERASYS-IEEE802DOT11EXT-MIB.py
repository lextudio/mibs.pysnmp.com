# SNMP MIB module (ENTERASYS-IEEE802DOT11EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IEEE802DOT11EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:56 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(dot11WEPDefaultKeyIndex,) = mibBuilder.importSymbols(
    "IEEE802dot11-MIB",
    "dot11WEPDefaultKeyIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(AutonomousType,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysDot11ExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9)
)
etsysDot11ExtMIB.setRevisions(
        ("2002-03-07 19:45",
         "2001-05-08 18:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysDot11ExtObjects_ObjectIdentity = ObjectIdentity
etsysDot11ExtObjects = _EtsysDot11ExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1)
)
_EtsysDot11ExtLinkTest_ObjectIdentity = ObjectIdentity
etsysDot11ExtLinkTest = _EtsysDot11ExtLinkTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1)
)
_EtsysDot11ExtLinkTestTable_Object = MibTable
etsysDot11ExtLinkTestTable = _EtsysDot11ExtLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtLinkTestTable.setStatus("current")
_EtsysDot11ExtLinkTestEntry_Object = MibTableRow
etsysDot11ExtLinkTestEntry = _EtsysDot11ExtLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1, 1)
)
etsysDot11ExtLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtLinkTestEntry.setStatus("current")
_EtsysDot11ExtLTRemoteStationMAC_Type = MacAddress
_EtsysDot11ExtLTRemoteStationMAC_Object = MibTableColumn
etsysDot11ExtLTRemoteStationMAC = _EtsysDot11ExtLTRemoteStationMAC_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1, 1, 1),
    _EtsysDot11ExtLTRemoteStationMAC_Type()
)
etsysDot11ExtLTRemoteStationMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtLTRemoteStationMAC.setStatus("current")


class _EtsysDot11ExtLTRemoteStationName_Type(SnmpAdminString):
    """Custom type etsysDot11ExtLTRemoteStationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EtsysDot11ExtLTRemoteStationName_Type.__name__ = "SnmpAdminString"
_EtsysDot11ExtLTRemoteStationName_Object = MibTableColumn
etsysDot11ExtLTRemoteStationName = _EtsysDot11ExtLTRemoteStationName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1, 1, 2),
    _EtsysDot11ExtLTRemoteStationName_Type()
)
etsysDot11ExtLTRemoteStationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtLTRemoteStationName.setStatus("current")


class _EtsysDot11ExtLTTrigger_Type(Integer32):
    """Custom type etsysDot11ExtLTTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_EtsysDot11ExtLTTrigger_Type.__name__ = "Integer32"
_EtsysDot11ExtLTTrigger_Object = MibTableColumn
etsysDot11ExtLTTrigger = _EtsysDot11ExtLTTrigger_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1, 1, 3),
    _EtsysDot11ExtLTTrigger_Type()
)
etsysDot11ExtLTTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtLTTrigger.setStatus("current")


class _EtsysDot11ExtLTRemoteContents_Type(OctetString):
    """Custom type etsysDot11ExtLTRemoteContents based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(84, 84),
    )


_EtsysDot11ExtLTRemoteContents_Type.__name__ = "OctetString"
_EtsysDot11ExtLTRemoteContents_Object = MibTableColumn
etsysDot11ExtLTRemoteContents = _EtsysDot11ExtLTRemoteContents_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 1, 1, 1, 4),
    _EtsysDot11ExtLTRemoteContents_Type()
)
etsysDot11ExtLTRemoteContents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtLTRemoteContents.setStatus("current")
_EtsysDot11ExtGeneral_ObjectIdentity = ObjectIdentity
etsysDot11ExtGeneral = _EtsysDot11ExtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2)
)
_EtsysDot11ExtGeneralTable_Object = MibTable
etsysDot11ExtGeneralTable = _EtsysDot11ExtGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtGeneralTable.setStatus("current")
_EtsysDot11ExtGeneralEntry_Object = MibTableRow
etsysDot11ExtGeneralEntry = _EtsysDot11ExtGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1)
)
etsysDot11ExtGeneralEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtGeneralEntry.setStatus("current")


class _EtsysDot11ExtPCCardType_Type(Integer32):
    """Custom type etsysDot11ExtPCCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              15)
        )
    )
    namedValues = NamedValues(
        *(("deprecatedValue1", 2),
          ("deprecatedValue2", 3),
          ("deprecatedValue3", 4),
          ("ds80211a", 6),
          ("ds80211b", 5),
          ("none", 1),
          ("unknown", 15))
    )


_EtsysDot11ExtPCCardType_Type.__name__ = "Integer32"
_EtsysDot11ExtPCCardType_Object = MibTableColumn
etsysDot11ExtPCCardType = _EtsysDot11ExtPCCardType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 1),
    _EtsysDot11ExtPCCardType_Type()
)
etsysDot11ExtPCCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtPCCardType.setStatus("current")


class _EtsysDot11ExtPCCardVersions_Type(SnmpAdminString):
    """Custom type etsysDot11ExtPCCardVersions based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_EtsysDot11ExtPCCardVersions_Type.__name__ = "SnmpAdminString"
_EtsysDot11ExtPCCardVersions_Object = MibTableColumn
etsysDot11ExtPCCardVersions = _EtsysDot11ExtPCCardVersions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 2),
    _EtsysDot11ExtPCCardVersions_Type()
)
etsysDot11ExtPCCardVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtPCCardVersions.setStatus("current")


class _EtsysDot11ExtBridgeMode_Type(Integer32):
    """Custom type etsysDot11ExtBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lanToLanEndpoint", 2),
          ("lanToLanMultipoint", 3),
          ("workgroup", 1))
    )


_EtsysDot11ExtBridgeMode_Type.__name__ = "Integer32"
_EtsysDot11ExtBridgeMode_Object = MibTableColumn
etsysDot11ExtBridgeMode = _EtsysDot11ExtBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 3),
    _EtsysDot11ExtBridgeMode_Type()
)
etsysDot11ExtBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBridgeMode.setStatus("current")


class _EtsysDot11ExtResetOptions_Type(Integer32):
    """Custom type etsysDot11ExtResetOptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 0),
          ("resetRadioCardIfNecessary", 1),
          ("resetRadioCardRegardless", 2))
    )


_EtsysDot11ExtResetOptions_Type.__name__ = "Integer32"
_EtsysDot11ExtResetOptions_Object = MibTableColumn
etsysDot11ExtResetOptions = _EtsysDot11ExtResetOptions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 4),
    _EtsysDot11ExtResetOptions_Type()
)
etsysDot11ExtResetOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtResetOptions.setStatus("current")


class _EtsysDot11ExtSystemScale_Type(Integer32):
    """Custom type etsysDot11ExtSystemScale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_EtsysDot11ExtSystemScale_Type.__name__ = "Integer32"
_EtsysDot11ExtSystemScale_Object = MibTableColumn
etsysDot11ExtSystemScale = _EtsysDot11ExtSystemScale_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 5),
    _EtsysDot11ExtSystemScale_Type()
)
etsysDot11ExtSystemScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtSystemScale.setStatus("current")
_EtsysDot11ExtSecureAccess_Type = EnabledStatus
_EtsysDot11ExtSecureAccess_Object = MibTableColumn
etsysDot11ExtSecureAccess = _EtsysDot11ExtSecureAccess_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 6),
    _EtsysDot11ExtSecureAccess_Type()
)
etsysDot11ExtSecureAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtSecureAccess.setStatus("current")


class _EtsysDot11ExtMulticastTxRate_Type(Integer32):
    """Custom type etsysDot11ExtMulticastTxRate based on Integer32"""
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
        *(("fixed1Mbit", 1),
          ("fixed2Mbit", 2),
          ("fixedHighRate", 4),
          ("fixedMediumRate", 3))
    )


_EtsysDot11ExtMulticastTxRate_Type.__name__ = "Integer32"
_EtsysDot11ExtMulticastTxRate_Object = MibTableColumn
etsysDot11ExtMulticastTxRate = _EtsysDot11ExtMulticastTxRate_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 7),
    _EtsysDot11ExtMulticastTxRate_Type()
)
etsysDot11ExtMulticastTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtMulticastTxRate.setStatus("current")
_EtsysDot11ExtIntraBSSRelay_Type = EnabledStatus
_EtsysDot11ExtIntraBSSRelay_Object = MibTableColumn
etsysDot11ExtIntraBSSRelay = _EtsysDot11ExtIntraBSSRelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 8),
    _EtsysDot11ExtIntraBSSRelay_Type()
)
etsysDot11ExtIntraBSSRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtIntraBSSRelay.setStatus("current")


class _EtsysDot11ExtStationName_Type(SnmpAdminString):
    """Custom type etsysDot11ExtStationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_EtsysDot11ExtStationName_Type.__name__ = "SnmpAdminString"
_EtsysDot11ExtStationName_Object = MibTableColumn
etsysDot11ExtStationName = _EtsysDot11ExtStationName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 2, 1, 1, 9),
    _EtsysDot11ExtStationName_Type()
)
etsysDot11ExtStationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtStationName.setStatus("current")
_EtsysDot11ExtBldg_ObjectIdentity = ObjectIdentity
etsysDot11ExtBldg = _EtsysDot11ExtBldg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3)
)
_EtsysDot11ExtBldgTable_Object = MibTable
etsysDot11ExtBldgTable = _EtsysDot11ExtBldgTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtBldgTable.setStatus("current")
_EtsysDot11ExtBldgEntry_Object = MibTableRow
etsysDot11ExtBldgEntry = _EtsysDot11ExtBldgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1)
)
etsysDot11ExtBldgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtBldgEntry.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC1_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC1_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC1 = _EtsysDot11ExtBldgRemoteMAC1_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 1),
    _EtsysDot11ExtBldgRemoteMAC1_Type()
)
etsysDot11ExtBldgRemoteMAC1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC1.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC2_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC2_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC2 = _EtsysDot11ExtBldgRemoteMAC2_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 2),
    _EtsysDot11ExtBldgRemoteMAC2_Type()
)
etsysDot11ExtBldgRemoteMAC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC2.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC3_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC3_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC3 = _EtsysDot11ExtBldgRemoteMAC3_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 3),
    _EtsysDot11ExtBldgRemoteMAC3_Type()
)
etsysDot11ExtBldgRemoteMAC3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC3.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC4_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC4_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC4 = _EtsysDot11ExtBldgRemoteMAC4_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 4),
    _EtsysDot11ExtBldgRemoteMAC4_Type()
)
etsysDot11ExtBldgRemoteMAC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC4.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC5_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC5_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC5 = _EtsysDot11ExtBldgRemoteMAC5_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 5),
    _EtsysDot11ExtBldgRemoteMAC5_Type()
)
etsysDot11ExtBldgRemoteMAC5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC5.setStatus("current")
_EtsysDot11ExtBldgRemoteMAC6_Type = MacAddress
_EtsysDot11ExtBldgRemoteMAC6_Object = MibTableColumn
etsysDot11ExtBldgRemoteMAC6 = _EtsysDot11ExtBldgRemoteMAC6_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 6),
    _EtsysDot11ExtBldgRemoteMAC6_Type()
)
etsysDot11ExtBldgRemoteMAC6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgRemoteMAC6.setStatus("current")


class _EtsysDot11ExtBldgMPActivationKey_Type(OctetString):
    """Custom type etsysDot11ExtBldgMPActivationKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtsysDot11ExtBldgMPActivationKey_Type.__name__ = "OctetString"
_EtsysDot11ExtBldgMPActivationKey_Object = MibTableColumn
etsysDot11ExtBldgMPActivationKey = _EtsysDot11ExtBldgMPActivationKey_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 3, 1, 1, 7),
    _EtsysDot11ExtBldgMPActivationKey_Type()
)
etsysDot11ExtBldgMPActivationKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtBldgMPActivationKey.setStatus("current")
_EtsysDot11ExtWEP_ObjectIdentity = ObjectIdentity
etsysDot11ExtWEP = _EtsysDot11ExtWEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4)
)
_EtsysDot11ExtWEPDefaultKeysTable_Object = MibTable
etsysDot11ExtWEPDefaultKeysTable = _EtsysDot11ExtWEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtWEPDefaultKeysTable.setStatus("current")
_EtsysDot11ExtWEPDefaultKeysEntry_Object = MibTableRow
etsysDot11ExtWEPDefaultKeysEntry = _EtsysDot11ExtWEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 1, 1)
)
etsysDot11ExtWEPDefaultKeysEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IEEE802dot11-MIB", "dot11WEPDefaultKeyIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtWEPDefaultKeysEntry.setStatus("current")
_EtsysDot11ExtWEPKeyDefined_Type = TruthValue
_EtsysDot11ExtWEPKeyDefined_Object = MibTableColumn
etsysDot11ExtWEPKeyDefined = _EtsysDot11ExtWEPKeyDefined_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 1, 1, 1),
    _EtsysDot11ExtWEPKeyDefined_Type()
)
etsysDot11ExtWEPKeyDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtWEPKeyDefined.setStatus("current")


class _EtsysDot11ExtWEPKeyValue_Type(OctetString):
    """Custom type etsysDot11ExtWEPKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )


_EtsysDot11ExtWEPKeyValue_Type.__name__ = "OctetString"
_EtsysDot11ExtWEPKeyValue_Object = MibTableColumn
etsysDot11ExtWEPKeyValue = _EtsysDot11ExtWEPKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 1, 1, 2),
    _EtsysDot11ExtWEPKeyValue_Type()
)
etsysDot11ExtWEPKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot11ExtWEPKeyValue.setStatus("current")
_EtsysDot11ExtWEPEnhancedTable_Object = MibTable
etsysDot11ExtWEPEnhancedTable = _EtsysDot11ExtWEPEnhancedTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 2)
)
if mibBuilder.loadTexts:
    etsysDot11ExtWEPEnhancedTable.setStatus("current")
_EtsysDot11ExtWEPEnhancedEntry_Object = MibTableRow
etsysDot11ExtWEPEnhancedEntry = _EtsysDot11ExtWEPEnhancedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 2, 1)
)
etsysDot11ExtWEPEnhancedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtWEPEnhancedEntry.setStatus("current")
_EtsysDot11ExtWEPEnhancedImplemented_Type = TruthValue
_EtsysDot11ExtWEPEnhancedImplemented_Object = MibTableColumn
etsysDot11ExtWEPEnhancedImplemented = _EtsysDot11ExtWEPEnhancedImplemented_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 4, 2, 1, 1),
    _EtsysDot11ExtWEPEnhancedImplemented_Type()
)
etsysDot11ExtWEPEnhancedImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtWEPEnhancedImplemented.setStatus("current")
_EtsysDot11ExtEffect_ObjectIdentity = ObjectIdentity
etsysDot11ExtEffect = _EtsysDot11ExtEffect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 5)
)
_EtsysDot11ExtOIDNotInEffectTable_Object = MibTable
etsysDot11ExtOIDNotInEffectTable = _EtsysDot11ExtOIDNotInEffectTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 5, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtOIDNotInEffectTable.setStatus("current")
_EtsysDot11ExtOIDNotInEffectEntry_Object = MibTableRow
etsysDot11ExtOIDNotInEffectEntry = _EtsysDot11ExtOIDNotInEffectEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 5, 1, 1)
)
etsysDot11ExtOIDNotInEffectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtOIDIndex"),
)
if mibBuilder.loadTexts:
    etsysDot11ExtOIDNotInEffectEntry.setStatus("current")
_EtsysDot11ExtOIDIndex_Type = AutonomousType
_EtsysDot11ExtOIDIndex_Object = MibTableColumn
etsysDot11ExtOIDIndex = _EtsysDot11ExtOIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 5, 1, 1, 1),
    _EtsysDot11ExtOIDIndex_Type()
)
etsysDot11ExtOIDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysDot11ExtOIDIndex.setStatus("current")
_EtsysDot11ExtOIDNotInEffect_Type = TruthValue
_EtsysDot11ExtOIDNotInEffect_Object = MibTableColumn
etsysDot11ExtOIDNotInEffect = _EtsysDot11ExtOIDNotInEffect_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 1, 5, 1, 1, 2),
    _EtsysDot11ExtOIDNotInEffect_Type()
)
etsysDot11ExtOIDNotInEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysDot11ExtOIDNotInEffect.setStatus("current")
_EtsysDot11ExtConformance_ObjectIdentity = ObjectIdentity
etsysDot11ExtConformance = _EtsysDot11ExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 2)
)
_EtsysDot11ExtGroups_ObjectIdentity = ObjectIdentity
etsysDot11ExtGroups = _EtsysDot11ExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 2, 1)
)
_EtsysDot11ExtCompliances_ObjectIdentity = ObjectIdentity
etsysDot11ExtCompliances = _EtsysDot11ExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 2, 2)
)

# Managed Objects groups

etsysDot11ExtBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 2, 1, 1)
)
etsysDot11ExtBaseGroup.setObjects(
      *(("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtLTRemoteStationMAC"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtLTRemoteStationName"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtLTTrigger"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtLTRemoteContents"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtSystemScale"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtSecureAccess"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtMulticastTxRate"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtIntraBSSRelay"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtPCCardType"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtPCCardVersions"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBridgeMode"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtResetOptions"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtStationName"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC1"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC2"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC3"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC4"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC5"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgRemoteMAC6"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtBldgMPActivationKey"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtWEPKeyDefined"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtWEPKeyValue"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtWEPEnhancedImplemented"),
        ("ENTERASYS-IEEE802DOT11EXT-MIB", "etsysDot11ExtOIDNotInEffect"))
)
if mibBuilder.loadTexts:
    etsysDot11ExtBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysDot11ExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot11ExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IEEE802DOT11EXT-MIB",
    **{"etsysDot11ExtMIB": etsysDot11ExtMIB,
       "etsysDot11ExtObjects": etsysDot11ExtObjects,
       "etsysDot11ExtLinkTest": etsysDot11ExtLinkTest,
       "etsysDot11ExtLinkTestTable": etsysDot11ExtLinkTestTable,
       "etsysDot11ExtLinkTestEntry": etsysDot11ExtLinkTestEntry,
       "etsysDot11ExtLTRemoteStationMAC": etsysDot11ExtLTRemoteStationMAC,
       "etsysDot11ExtLTRemoteStationName": etsysDot11ExtLTRemoteStationName,
       "etsysDot11ExtLTTrigger": etsysDot11ExtLTTrigger,
       "etsysDot11ExtLTRemoteContents": etsysDot11ExtLTRemoteContents,
       "etsysDot11ExtGeneral": etsysDot11ExtGeneral,
       "etsysDot11ExtGeneralTable": etsysDot11ExtGeneralTable,
       "etsysDot11ExtGeneralEntry": etsysDot11ExtGeneralEntry,
       "etsysDot11ExtPCCardType": etsysDot11ExtPCCardType,
       "etsysDot11ExtPCCardVersions": etsysDot11ExtPCCardVersions,
       "etsysDot11ExtBridgeMode": etsysDot11ExtBridgeMode,
       "etsysDot11ExtResetOptions": etsysDot11ExtResetOptions,
       "etsysDot11ExtSystemScale": etsysDot11ExtSystemScale,
       "etsysDot11ExtSecureAccess": etsysDot11ExtSecureAccess,
       "etsysDot11ExtMulticastTxRate": etsysDot11ExtMulticastTxRate,
       "etsysDot11ExtIntraBSSRelay": etsysDot11ExtIntraBSSRelay,
       "etsysDot11ExtStationName": etsysDot11ExtStationName,
       "etsysDot11ExtBldg": etsysDot11ExtBldg,
       "etsysDot11ExtBldgTable": etsysDot11ExtBldgTable,
       "etsysDot11ExtBldgEntry": etsysDot11ExtBldgEntry,
       "etsysDot11ExtBldgRemoteMAC1": etsysDot11ExtBldgRemoteMAC1,
       "etsysDot11ExtBldgRemoteMAC2": etsysDot11ExtBldgRemoteMAC2,
       "etsysDot11ExtBldgRemoteMAC3": etsysDot11ExtBldgRemoteMAC3,
       "etsysDot11ExtBldgRemoteMAC4": etsysDot11ExtBldgRemoteMAC4,
       "etsysDot11ExtBldgRemoteMAC5": etsysDot11ExtBldgRemoteMAC5,
       "etsysDot11ExtBldgRemoteMAC6": etsysDot11ExtBldgRemoteMAC6,
       "etsysDot11ExtBldgMPActivationKey": etsysDot11ExtBldgMPActivationKey,
       "etsysDot11ExtWEP": etsysDot11ExtWEP,
       "etsysDot11ExtWEPDefaultKeysTable": etsysDot11ExtWEPDefaultKeysTable,
       "etsysDot11ExtWEPDefaultKeysEntry": etsysDot11ExtWEPDefaultKeysEntry,
       "etsysDot11ExtWEPKeyDefined": etsysDot11ExtWEPKeyDefined,
       "etsysDot11ExtWEPKeyValue": etsysDot11ExtWEPKeyValue,
       "etsysDot11ExtWEPEnhancedTable": etsysDot11ExtWEPEnhancedTable,
       "etsysDot11ExtWEPEnhancedEntry": etsysDot11ExtWEPEnhancedEntry,
       "etsysDot11ExtWEPEnhancedImplemented": etsysDot11ExtWEPEnhancedImplemented,
       "etsysDot11ExtEffect": etsysDot11ExtEffect,
       "etsysDot11ExtOIDNotInEffectTable": etsysDot11ExtOIDNotInEffectTable,
       "etsysDot11ExtOIDNotInEffectEntry": etsysDot11ExtOIDNotInEffectEntry,
       "etsysDot11ExtOIDIndex": etsysDot11ExtOIDIndex,
       "etsysDot11ExtOIDNotInEffect": etsysDot11ExtOIDNotInEffect,
       "etsysDot11ExtConformance": etsysDot11ExtConformance,
       "etsysDot11ExtGroups": etsysDot11ExtGroups,
       "etsysDot11ExtBaseGroup": etsysDot11ExtBaseGroup,
       "etsysDot11ExtCompliances": etsysDot11ExtCompliances,
       "etsysDot11ExtCompliance": etsysDot11ExtCompliance}
)
