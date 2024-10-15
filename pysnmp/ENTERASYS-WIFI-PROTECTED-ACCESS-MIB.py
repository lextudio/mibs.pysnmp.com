# SNMP MIB module (ENTERASYS-WIFI-PROTECTED-ACCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-WIFI-PROTECTED-ACCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:44 2024
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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysWiFiProtectedAccessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32)
)
etsysWiFiProtectedAccessMIB.setRevisions(
        ("2003-11-06 15:15",
         "2003-08-07 17:08")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysWiFiProtectedAccessObjects_ObjectIdentity = ObjectIdentity
etsysWiFiProtectedAccessObjects = _EtsysWiFiProtectedAccessObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1)
)
_EtsysWPAConfigTable_Object = MibTable
etsysWPAConfigTable = _EtsysWPAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1)
)
if mibBuilder.loadTexts:
    etsysWPAConfigTable.setStatus("current")
_EtsysWPAConfigEntry_Object = MibTableRow
etsysWPAConfigEntry = _EtsysWPAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1)
)
etsysWPAConfigEntry.setIndexNames(
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"),
)
if mibBuilder.loadTexts:
    etsysWPAConfigEntry.setStatus("current")


class _EtsysWPAConfigIndex_Type(Integer32):
    """Custom type etsysWPAConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EtsysWPAConfigIndex_Type.__name__ = "Integer32"
_EtsysWPAConfigIndex_Object = MibTableColumn
etsysWPAConfigIndex = _EtsysWPAConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 1),
    _EtsysWPAConfigIndex_Type()
)
etsysWPAConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysWPAConfigIndex.setStatus("current")
_EtsysWPAConfigOptionImplemented_Type = TruthValue
_EtsysWPAConfigOptionImplemented_Object = MibTableColumn
etsysWPAConfigOptionImplemented = _EtsysWPAConfigOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 2),
    _EtsysWPAConfigOptionImplemented_Type()
)
etsysWPAConfigOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigOptionImplemented.setStatus("current")
_EtsysWPAConfigEnabled_Type = TruthValue
_EtsysWPAConfigEnabled_Object = MibTableColumn
etsysWPAConfigEnabled = _EtsysWPAConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 3),
    _EtsysWPAConfigEnabled_Type()
)
etsysWPAConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigEnabled.setStatus("current")
_EtsysWPAConfigTKIPNumberOfReplayCounters_Type = Integer32
_EtsysWPAConfigTKIPNumberOfReplayCounters_Object = MibTableColumn
etsysWPAConfigTKIPNumberOfReplayCounters = _EtsysWPAConfigTKIPNumberOfReplayCounters_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 4),
    _EtsysWPAConfigTKIPNumberOfReplayCounters_Type()
)
etsysWPAConfigTKIPNumberOfReplayCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigTKIPNumberOfReplayCounters.setStatus("current")
_EtsysWPAConfigVersion_Type = Integer32
_EtsysWPAConfigVersion_Object = MibTableColumn
etsysWPAConfigVersion = _EtsysWPAConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 5),
    _EtsysWPAConfigVersion_Type()
)
etsysWPAConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigVersion.setStatus("current")


class _EtsysWPAConfigPairwiseKeysSupported_Type(Unsigned32):
    """Custom type etsysWPAConfigPairwiseKeysSupported based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EtsysWPAConfigPairwiseKeysSupported_Type.__name__ = "Unsigned32"
_EtsysWPAConfigPairwiseKeysSupported_Object = MibTableColumn
etsysWPAConfigPairwiseKeysSupported = _EtsysWPAConfigPairwiseKeysSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 6),
    _EtsysWPAConfigPairwiseKeysSupported_Type()
)
etsysWPAConfigPairwiseKeysSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigPairwiseKeysSupported.setStatus("current")


class _EtsysWPAConfigMulticastCipher_Type(OctetString):
    """Custom type etsysWPAConfigMulticastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EtsysWPAConfigMulticastCipher_Type.__name__ = "OctetString"
_EtsysWPAConfigMulticastCipher_Object = MibTableColumn
etsysWPAConfigMulticastCipher = _EtsysWPAConfigMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 7),
    _EtsysWPAConfigMulticastCipher_Type()
)
etsysWPAConfigMulticastCipher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigMulticastCipher.setStatus("current")


class _EtsysWPAConfigGroupRekeyMethod_Type(Integer32):
    """Custom type etsysWPAConfigGroupRekeyMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("packetBased", 3),
          ("timeBased", 2))
    )


_EtsysWPAConfigGroupRekeyMethod_Type.__name__ = "Integer32"
_EtsysWPAConfigGroupRekeyMethod_Object = MibTableColumn
etsysWPAConfigGroupRekeyMethod = _EtsysWPAConfigGroupRekeyMethod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 8),
    _EtsysWPAConfigGroupRekeyMethod_Type()
)
etsysWPAConfigGroupRekeyMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyMethod.setStatus("current")


class _EtsysWPAConfigGroupRekeyTime_Type(Unsigned32):
    """Custom type etsysWPAConfigGroupRekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigGroupRekeyTime_Type.__name__ = "Unsigned32"
_EtsysWPAConfigGroupRekeyTime_Object = MibTableColumn
etsysWPAConfigGroupRekeyTime = _EtsysWPAConfigGroupRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 9),
    _EtsysWPAConfigGroupRekeyTime_Type()
)
etsysWPAConfigGroupRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyTime.setUnits("seconds")


class _EtsysWPAConfigGroupRekeyPackets_Type(Unsigned32):
    """Custom type etsysWPAConfigGroupRekeyPackets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigGroupRekeyPackets_Type.__name__ = "Unsigned32"
_EtsysWPAConfigGroupRekeyPackets_Object = MibTableColumn
etsysWPAConfigGroupRekeyPackets = _EtsysWPAConfigGroupRekeyPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 10),
    _EtsysWPAConfigGroupRekeyPackets_Type()
)
etsysWPAConfigGroupRekeyPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyPackets.setStatus("current")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyPackets.setUnits("1000 packets")
_EtsysWPAConfigGroupRekeyStrict_Type = TruthValue
_EtsysWPAConfigGroupRekeyStrict_Object = MibTableColumn
etsysWPAConfigGroupRekeyStrict = _EtsysWPAConfigGroupRekeyStrict_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 11),
    _EtsysWPAConfigGroupRekeyStrict_Type()
)
etsysWPAConfigGroupRekeyStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupRekeyStrict.setStatus("current")


class _EtsysWPAConfigPSKValue_Type(OctetString):
    """Custom type etsysWPAConfigPSKValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_EtsysWPAConfigPSKValue_Type.__name__ = "OctetString"
_EtsysWPAConfigPSKValue_Object = MibTableColumn
etsysWPAConfigPSKValue = _EtsysWPAConfigPSKValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 12),
    _EtsysWPAConfigPSKValue_Type()
)
etsysWPAConfigPSKValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigPSKValue.setStatus("current")
_EtsysWPAConfigPSKPassPhrase_Type = DisplayString
_EtsysWPAConfigPSKPassPhrase_Object = MibTableColumn
etsysWPAConfigPSKPassPhrase = _EtsysWPAConfigPSKPassPhrase_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 13),
    _EtsysWPAConfigPSKPassPhrase_Type()
)
etsysWPAConfigPSKPassPhrase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigPSKPassPhrase.setStatus("current")
_EtsysWPAConfigPSKValueEntered_Type = TruthValue
_EtsysWPAConfigPSKValueEntered_Object = MibTableColumn
etsysWPAConfigPSKValueEntered = _EtsysWPAConfigPSKValueEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 14),
    _EtsysWPAConfigPSKValueEntered_Type()
)
etsysWPAConfigPSKValueEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigPSKValueEntered.setStatus("current")
_EtsysWPAConfigMultipleAuthSuitesSupported_Type = TruthValue
_EtsysWPAConfigMultipleAuthSuitesSupported_Object = MibTableColumn
etsysWPAConfigMultipleAuthSuitesSupported = _EtsysWPAConfigMultipleAuthSuitesSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 15),
    _EtsysWPAConfigMultipleAuthSuitesSupported_Type()
)
etsysWPAConfigMultipleAuthSuitesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigMultipleAuthSuitesSupported.setStatus("current")


class _EtsysWPAConfigGroupMasterRekeyTime_Type(Unsigned32):
    """Custom type etsysWPAConfigGroupMasterRekeyTime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigGroupMasterRekeyTime_Type.__name__ = "Unsigned32"
_EtsysWPAConfigGroupMasterRekeyTime_Object = MibTableColumn
etsysWPAConfigGroupMasterRekeyTime = _EtsysWPAConfigGroupMasterRekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 16),
    _EtsysWPAConfigGroupMasterRekeyTime_Type()
)
etsysWPAConfigGroupMasterRekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupMasterRekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupMasterRekeyTime.setUnits("seconds")


class _EtsysWPAConfigGroupUpdateTimeOut_Type(Unsigned32):
    """Custom type etsysWPAConfigGroupUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigGroupUpdateTimeOut_Type.__name__ = "Unsigned32"
_EtsysWPAConfigGroupUpdateTimeOut_Object = MibTableColumn
etsysWPAConfigGroupUpdateTimeOut = _EtsysWPAConfigGroupUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 17),
    _EtsysWPAConfigGroupUpdateTimeOut_Type()
)
etsysWPAConfigGroupUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupUpdateTimeOut.setUnits("seconds")


class _EtsysWPAConfigGroupUpdateCount_Type(Unsigned32):
    """Custom type etsysWPAConfigGroupUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigGroupUpdateCount_Type.__name__ = "Unsigned32"
_EtsysWPAConfigGroupUpdateCount_Object = MibTableColumn
etsysWPAConfigGroupUpdateCount = _EtsysWPAConfigGroupUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 18),
    _EtsysWPAConfigGroupUpdateCount_Type()
)
etsysWPAConfigGroupUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigGroupUpdateCount.setStatus("current")


class _EtsysWPAConfigPairwiseUpdateTimeOut_Type(Unsigned32):
    """Custom type etsysWPAConfigPairwiseUpdateTimeOut based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigPairwiseUpdateTimeOut_Type.__name__ = "Unsigned32"
_EtsysWPAConfigPairwiseUpdateTimeOut_Object = MibTableColumn
etsysWPAConfigPairwiseUpdateTimeOut = _EtsysWPAConfigPairwiseUpdateTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 19),
    _EtsysWPAConfigPairwiseUpdateTimeOut_Type()
)
etsysWPAConfigPairwiseUpdateTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigPairwiseUpdateTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    etsysWPAConfigPairwiseUpdateTimeOut.setUnits("seconds")


class _EtsysWPAConfigPairwiseUpdateCount_Type(Unsigned32):
    """Custom type etsysWPAConfigPairwiseUpdateCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigPairwiseUpdateCount_Type.__name__ = "Unsigned32"
_EtsysWPAConfigPairwiseUpdateCount_Object = MibTableColumn
etsysWPAConfigPairwiseUpdateCount = _EtsysWPAConfigPairwiseUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 20),
    _EtsysWPAConfigPairwiseUpdateCount_Type()
)
etsysWPAConfigPairwiseUpdateCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigPairwiseUpdateCount.setStatus("current")
_EtsysWPAConfigLegacyOptionSupported_Type = TruthValue
_EtsysWPAConfigLegacyOptionSupported_Object = MibTableColumn
etsysWPAConfigLegacyOptionSupported = _EtsysWPAConfigLegacyOptionSupported_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 21),
    _EtsysWPAConfigLegacyOptionSupported_Type()
)
etsysWPAConfigLegacyOptionSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigLegacyOptionSupported.setStatus("current")
_EtsysWPAConfigAllowLegacyClients_Type = TruthValue
_EtsysWPAConfigAllowLegacyClients_Object = MibTableColumn
etsysWPAConfigAllowLegacyClients = _EtsysWPAConfigAllowLegacyClients_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 22),
    _EtsysWPAConfigAllowLegacyClients_Type()
)
etsysWPAConfigAllowLegacyClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigAllowLegacyClients.setStatus("current")
_EtsysWPAConfigRekeyPairwiseWEP_Type = TruthValue
_EtsysWPAConfigRekeyPairwiseWEP_Object = MibTableColumn
etsysWPAConfigRekeyPairwiseWEP = _EtsysWPAConfigRekeyPairwiseWEP_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 1, 1, 23),
    _EtsysWPAConfigRekeyPairwiseWEP_Type()
)
etsysWPAConfigRekeyPairwiseWEP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigRekeyPairwiseWEP.setStatus("current")
_EtsysWPAConfigUnicastCiphersTable_Object = MibTable
etsysWPAConfigUnicastCiphersTable = _EtsysWPAConfigUnicastCiphersTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2)
)
if mibBuilder.loadTexts:
    etsysWPAConfigUnicastCiphersTable.setStatus("current")
_EtsysWPAConfigUnicastCiphersEntry_Object = MibTableRow
etsysWPAConfigUnicastCiphersEntry = _EtsysWPAConfigUnicastCiphersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1)
)
etsysWPAConfigUnicastCiphersEntry.setIndexNames(
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"),
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipherIndex"),
)
if mibBuilder.loadTexts:
    etsysWPAConfigUnicastCiphersEntry.setStatus("current")


class _EtsysWPAConfigUnicastCipherIndex_Type(Unsigned32):
    """Custom type etsysWPAConfigUnicastCipherIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigUnicastCipherIndex_Type.__name__ = "Unsigned32"
_EtsysWPAConfigUnicastCipherIndex_Object = MibTableColumn
etsysWPAConfigUnicastCipherIndex = _EtsysWPAConfigUnicastCipherIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 1),
    _EtsysWPAConfigUnicastCipherIndex_Type()
)
etsysWPAConfigUnicastCipherIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysWPAConfigUnicastCipherIndex.setStatus("current")


class _EtsysWPAConfigUnicastCipher_Type(OctetString):
    """Custom type etsysWPAConfigUnicastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EtsysWPAConfigUnicastCipher_Type.__name__ = "OctetString"
_EtsysWPAConfigUnicastCipher_Object = MibTableColumn
etsysWPAConfigUnicastCipher = _EtsysWPAConfigUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 2),
    _EtsysWPAConfigUnicastCipher_Type()
)
etsysWPAConfigUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigUnicastCipher.setStatus("current")
_EtsysWPAConfigUnicastCipherEnabled_Type = TruthValue
_EtsysWPAConfigUnicastCipherEnabled_Object = MibTableColumn
etsysWPAConfigUnicastCipherEnabled = _EtsysWPAConfigUnicastCipherEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 2, 1, 3),
    _EtsysWPAConfigUnicastCipherEnabled_Type()
)
etsysWPAConfigUnicastCipherEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigUnicastCipherEnabled.setStatus("current")
_EtsysWPAConfigAuthenticationSuitesTable_Object = MibTable
etsysWPAConfigAuthenticationSuitesTable = _EtsysWPAConfigAuthenticationSuitesTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3)
)
if mibBuilder.loadTexts:
    etsysWPAConfigAuthenticationSuitesTable.setStatus("current")
_EtsysWPAConfigAuthenticationSuitesEntry_Object = MibTableRow
etsysWPAConfigAuthenticationSuitesEntry = _EtsysWPAConfigAuthenticationSuitesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1)
)
etsysWPAConfigAuthenticationSuitesEntry.setIndexNames(
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"),
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuiteIndex"),
)
if mibBuilder.loadTexts:
    etsysWPAConfigAuthenticationSuitesEntry.setStatus("current")


class _EtsysWPAConfigAuthenticationSuiteIndex_Type(Unsigned32):
    """Custom type etsysWPAConfigAuthenticationSuiteIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAConfigAuthenticationSuiteIndex_Type.__name__ = "Unsigned32"
_EtsysWPAConfigAuthenticationSuiteIndex_Object = MibTableColumn
etsysWPAConfigAuthenticationSuiteIndex = _EtsysWPAConfigAuthenticationSuiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 1),
    _EtsysWPAConfigAuthenticationSuiteIndex_Type()
)
etsysWPAConfigAuthenticationSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysWPAConfigAuthenticationSuiteIndex.setStatus("current")


class _EtsysWPAConfigAuthenticationSuite_Type(OctetString):
    """Custom type etsysWPAConfigAuthenticationSuite based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EtsysWPAConfigAuthenticationSuite_Type.__name__ = "OctetString"
_EtsysWPAConfigAuthenticationSuite_Object = MibTableColumn
etsysWPAConfigAuthenticationSuite = _EtsysWPAConfigAuthenticationSuite_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 2),
    _EtsysWPAConfigAuthenticationSuite_Type()
)
etsysWPAConfigAuthenticationSuite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAConfigAuthenticationSuite.setStatus("current")
_EtsysWPAConfigAuthenticationSuiteEnabled_Type = TruthValue
_EtsysWPAConfigAuthenticationSuiteEnabled_Object = MibTableColumn
etsysWPAConfigAuthenticationSuiteEnabled = _EtsysWPAConfigAuthenticationSuiteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 3, 1, 3),
    _EtsysWPAConfigAuthenticationSuiteEnabled_Type()
)
etsysWPAConfigAuthenticationSuiteEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysWPAConfigAuthenticationSuiteEnabled.setStatus("current")
_EtsysWPAStatsTable_Object = MibTable
etsysWPAStatsTable = _EtsysWPAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4)
)
if mibBuilder.loadTexts:
    etsysWPAStatsTable.setStatus("current")
_EtsysWPAStatsEntry_Object = MibTableRow
etsysWPAStatsEntry = _EtsysWPAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1)
)
etsysWPAStatsEntry.setIndexNames(
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigIndex"),
    (0, "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsIndex"),
)
if mibBuilder.loadTexts:
    etsysWPAStatsEntry.setStatus("current")


class _EtsysWPAStatsIndex_Type(Unsigned32):
    """Custom type etsysWPAStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAStatsIndex_Type.__name__ = "Unsigned32"
_EtsysWPAStatsIndex_Object = MibTableColumn
etsysWPAStatsIndex = _EtsysWPAStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 1),
    _EtsysWPAStatsIndex_Type()
)
etsysWPAStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysWPAStatsIndex.setStatus("current")
_EtsysWPAStatsSTAAddress_Type = MacAddress
_EtsysWPAStatsSTAAddress_Object = MibTableColumn
etsysWPAStatsSTAAddress = _EtsysWPAStatsSTAAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 2),
    _EtsysWPAStatsSTAAddress_Type()
)
etsysWPAStatsSTAAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsSTAAddress.setStatus("current")


class _EtsysWPAStatsVersion_Type(Unsigned32):
    """Custom type etsysWPAStatsVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EtsysWPAStatsVersion_Type.__name__ = "Unsigned32"
_EtsysWPAStatsVersion_Object = MibTableColumn
etsysWPAStatsVersion = _EtsysWPAStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 3),
    _EtsysWPAStatsVersion_Type()
)
etsysWPAStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsVersion.setStatus("current")


class _EtsysWPAStatsSelectedUnicastCipher_Type(OctetString):
    """Custom type etsysWPAStatsSelectedUnicastCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_EtsysWPAStatsSelectedUnicastCipher_Type.__name__ = "OctetString"
_EtsysWPAStatsSelectedUnicastCipher_Object = MibTableColumn
etsysWPAStatsSelectedUnicastCipher = _EtsysWPAStatsSelectedUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 4),
    _EtsysWPAStatsSelectedUnicastCipher_Type()
)
etsysWPAStatsSelectedUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsSelectedUnicastCipher.setStatus("current")
_EtsysWPAStatsTKIPICVErrors_Type = Counter32
_EtsysWPAStatsTKIPICVErrors_Object = MibTableColumn
etsysWPAStatsTKIPICVErrors = _EtsysWPAStatsTKIPICVErrors_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 5),
    _EtsysWPAStatsTKIPICVErrors_Type()
)
etsysWPAStatsTKIPICVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsTKIPICVErrors.setStatus("current")
_EtsysWPAStatsTKIPLocalMICFailures_Type = Counter32
_EtsysWPAStatsTKIPLocalMICFailures_Object = MibTableColumn
etsysWPAStatsTKIPLocalMICFailures = _EtsysWPAStatsTKIPLocalMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 6),
    _EtsysWPAStatsTKIPLocalMICFailures_Type()
)
etsysWPAStatsTKIPLocalMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsTKIPLocalMICFailures.setStatus("current")
_EtsysWPAStatsTKIPRemoteMICFailures_Type = Counter32
_EtsysWPAStatsTKIPRemoteMICFailures_Object = MibTableColumn
etsysWPAStatsTKIPRemoteMICFailures = _EtsysWPAStatsTKIPRemoteMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 7),
    _EtsysWPAStatsTKIPRemoteMICFailures_Type()
)
etsysWPAStatsTKIPRemoteMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsTKIPRemoteMICFailures.setStatus("current")
_EtsysWPAStatsTKIPCounterMeasuresInvoked_Type = Counter32
_EtsysWPAStatsTKIPCounterMeasuresInvoked_Object = MibTableColumn
etsysWPAStatsTKIPCounterMeasuresInvoked = _EtsysWPAStatsTKIPCounterMeasuresInvoked_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 1, 4, 1, 8),
    _EtsysWPAStatsTKIPCounterMeasuresInvoked_Type()
)
etsysWPAStatsTKIPCounterMeasuresInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysWPAStatsTKIPCounterMeasuresInvoked.setStatus("current")
_EtsysWpaConformance_ObjectIdentity = ObjectIdentity
etsysWpaConformance = _EtsysWpaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2)
)
_EtsysWpaGroups_ObjectIdentity = ObjectIdentity
etsysWpaGroups = _EtsysWpaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1)
)
_EtsysWpaCompliances_ObjectIdentity = ObjectIdentity
etsysWpaCompliances = _EtsysWpaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 2)
)

# Managed Objects groups

etsysWpaBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 1)
)
etsysWpaBaseGroup.setObjects(
      *(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigOptionImplemented"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigEnabled"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigTKIPNumberOfReplayCounters"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigVersion"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseKeysSupported"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigMulticastCipher"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyMethod"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyTime"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyPackets"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupRekeyStrict"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKValue"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKValueEntered"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigMultipleAuthSuitesSupported"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPSKPassPhrase"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupMasterRekeyTime"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupUpdateTimeOut"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigGroupUpdateCount"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseUpdateTimeOut"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigPairwiseUpdateCount"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigLegacyOptionSupported"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAllowLegacyClients"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigRekeyPairwiseWEP"))
)
if mibBuilder.loadTexts:
    etsysWpaBaseGroup.setStatus("current")

etsysWpaUnicastCipherGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 2)
)
etsysWpaUnicastCipherGroup.setObjects(
      *(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipher"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigUnicastCipherEnabled"))
)
if mibBuilder.loadTexts:
    etsysWpaUnicastCipherGroup.setStatus("current")

etsysWpaAuthSuiteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 3)
)
etsysWpaAuthSuiteGroup.setObjects(
      *(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuite"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAConfigAuthenticationSuiteEnabled"))
)
if mibBuilder.loadTexts:
    etsysWpaAuthSuiteGroup.setStatus("current")

etsysWpaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 1, 4)
)
etsysWpaStatsGroup.setObjects(
      *(("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsSTAAddress"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsVersion"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsSelectedUnicastCipher"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPICVErrors"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPLocalMICFailures"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPRemoteMICFailures"),
        ("ENTERASYS-WIFI-PROTECTED-ACCESS-MIB", "etsysWPAStatsTKIPCounterMeasuresInvoked"))
)
if mibBuilder.loadTexts:
    etsysWpaStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysWpaCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 32, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysWpaCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-WIFI-PROTECTED-ACCESS-MIB",
    **{"etsysWiFiProtectedAccessMIB": etsysWiFiProtectedAccessMIB,
       "etsysWiFiProtectedAccessObjects": etsysWiFiProtectedAccessObjects,
       "etsysWPAConfigTable": etsysWPAConfigTable,
       "etsysWPAConfigEntry": etsysWPAConfigEntry,
       "etsysWPAConfigIndex": etsysWPAConfigIndex,
       "etsysWPAConfigOptionImplemented": etsysWPAConfigOptionImplemented,
       "etsysWPAConfigEnabled": etsysWPAConfigEnabled,
       "etsysWPAConfigTKIPNumberOfReplayCounters": etsysWPAConfigTKIPNumberOfReplayCounters,
       "etsysWPAConfigVersion": etsysWPAConfigVersion,
       "etsysWPAConfigPairwiseKeysSupported": etsysWPAConfigPairwiseKeysSupported,
       "etsysWPAConfigMulticastCipher": etsysWPAConfigMulticastCipher,
       "etsysWPAConfigGroupRekeyMethod": etsysWPAConfigGroupRekeyMethod,
       "etsysWPAConfigGroupRekeyTime": etsysWPAConfigGroupRekeyTime,
       "etsysWPAConfigGroupRekeyPackets": etsysWPAConfigGroupRekeyPackets,
       "etsysWPAConfigGroupRekeyStrict": etsysWPAConfigGroupRekeyStrict,
       "etsysWPAConfigPSKValue": etsysWPAConfigPSKValue,
       "etsysWPAConfigPSKPassPhrase": etsysWPAConfigPSKPassPhrase,
       "etsysWPAConfigPSKValueEntered": etsysWPAConfigPSKValueEntered,
       "etsysWPAConfigMultipleAuthSuitesSupported": etsysWPAConfigMultipleAuthSuitesSupported,
       "etsysWPAConfigGroupMasterRekeyTime": etsysWPAConfigGroupMasterRekeyTime,
       "etsysWPAConfigGroupUpdateTimeOut": etsysWPAConfigGroupUpdateTimeOut,
       "etsysWPAConfigGroupUpdateCount": etsysWPAConfigGroupUpdateCount,
       "etsysWPAConfigPairwiseUpdateTimeOut": etsysWPAConfigPairwiseUpdateTimeOut,
       "etsysWPAConfigPairwiseUpdateCount": etsysWPAConfigPairwiseUpdateCount,
       "etsysWPAConfigLegacyOptionSupported": etsysWPAConfigLegacyOptionSupported,
       "etsysWPAConfigAllowLegacyClients": etsysWPAConfigAllowLegacyClients,
       "etsysWPAConfigRekeyPairwiseWEP": etsysWPAConfigRekeyPairwiseWEP,
       "etsysWPAConfigUnicastCiphersTable": etsysWPAConfigUnicastCiphersTable,
       "etsysWPAConfigUnicastCiphersEntry": etsysWPAConfigUnicastCiphersEntry,
       "etsysWPAConfigUnicastCipherIndex": etsysWPAConfigUnicastCipherIndex,
       "etsysWPAConfigUnicastCipher": etsysWPAConfigUnicastCipher,
       "etsysWPAConfigUnicastCipherEnabled": etsysWPAConfigUnicastCipherEnabled,
       "etsysWPAConfigAuthenticationSuitesTable": etsysWPAConfigAuthenticationSuitesTable,
       "etsysWPAConfigAuthenticationSuitesEntry": etsysWPAConfigAuthenticationSuitesEntry,
       "etsysWPAConfigAuthenticationSuiteIndex": etsysWPAConfigAuthenticationSuiteIndex,
       "etsysWPAConfigAuthenticationSuite": etsysWPAConfigAuthenticationSuite,
       "etsysWPAConfigAuthenticationSuiteEnabled": etsysWPAConfigAuthenticationSuiteEnabled,
       "etsysWPAStatsTable": etsysWPAStatsTable,
       "etsysWPAStatsEntry": etsysWPAStatsEntry,
       "etsysWPAStatsIndex": etsysWPAStatsIndex,
       "etsysWPAStatsSTAAddress": etsysWPAStatsSTAAddress,
       "etsysWPAStatsVersion": etsysWPAStatsVersion,
       "etsysWPAStatsSelectedUnicastCipher": etsysWPAStatsSelectedUnicastCipher,
       "etsysWPAStatsTKIPICVErrors": etsysWPAStatsTKIPICVErrors,
       "etsysWPAStatsTKIPLocalMICFailures": etsysWPAStatsTKIPLocalMICFailures,
       "etsysWPAStatsTKIPRemoteMICFailures": etsysWPAStatsTKIPRemoteMICFailures,
       "etsysWPAStatsTKIPCounterMeasuresInvoked": etsysWPAStatsTKIPCounterMeasuresInvoked,
       "etsysWpaConformance": etsysWpaConformance,
       "etsysWpaGroups": etsysWpaGroups,
       "etsysWpaBaseGroup": etsysWpaBaseGroup,
       "etsysWpaUnicastCipherGroup": etsysWpaUnicastCipherGroup,
       "etsysWpaAuthSuiteGroup": etsysWpaAuthSuiteGroup,
       "etsysWpaStatsGroup": etsysWpaStatsGroup,
       "etsysWpaCompliances": etsysWpaCompliances,
       "etsysWpaCompliance": etsysWpaCompliance}
)
