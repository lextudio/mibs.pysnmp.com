# SNMP MIB module (RUCKUS-ZD-WLAN-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-ZD-WLAN-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:55 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ruckusZDWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusZDWLANModule")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusZDWLANConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusZDWLANConfigObjects_ObjectIdentity = ObjectIdentity
ruckusZDWLANConfigObjects = _RuckusZDWLANConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1)
)
_RuckusZDWLANConfig_ObjectIdentity = ObjectIdentity
ruckusZDWLANConfig = _RuckusZDWLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1)
)
_RuckusZDWLANConfigTable_Object = MibTable
ruckusZDWLANConfigTable = _RuckusZDWLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusZDWLANConfigTable.setStatus("current")
_RuckusZDWLANConfigEntry_Object = MibTableRow
ruckusZDWLANConfigEntry = _RuckusZDWLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1)
)
ruckusZDWLANConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANConfigEntry.setStatus("current")


class _RuckusZDWLANID_Type(Integer32):
    """Custom type ruckusZDWLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RuckusZDWLANID_Type.__name__ = "Integer32"
_RuckusZDWLANID_Object = MibTableColumn
ruckusZDWLANID = _RuckusZDWLANID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 1),
    _RuckusZDWLANID_Type()
)
ruckusZDWLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDWLANID.setStatus("current")


class _RuckusZDWLANConfigSSID_Type(OctetString):
    """Custom type ruckusZDWLANConfigSSID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusZDWLANConfigSSID_Type.__name__ = "OctetString"
_RuckusZDWLANConfigSSID_Object = MibTableColumn
ruckusZDWLANConfigSSID = _RuckusZDWLANConfigSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 2),
    _RuckusZDWLANConfigSSID_Type()
)
ruckusZDWLANConfigSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigSSID.setStatus("current")


class _RuckusZDWLANConfigDescription_Type(DisplayString):
    """Custom type ruckusZDWLANConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDWLANConfigDescription_Type.__name__ = "DisplayString"
_RuckusZDWLANConfigDescription_Object = MibTableColumn
ruckusZDWLANConfigDescription = _RuckusZDWLANConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 3),
    _RuckusZDWLANConfigDescription_Type()
)
ruckusZDWLANConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDescription.setStatus("current")


class _RuckusZDWLANConfigName_Type(OctetString):
    """Custom type ruckusZDWLANConfigName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RuckusZDWLANConfigName_Type.__name__ = "OctetString"
_RuckusZDWLANConfigName_Object = MibTableColumn
ruckusZDWLANConfigName = _RuckusZDWLANConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 4),
    _RuckusZDWLANConfigName_Type()
)
ruckusZDWLANConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigName.setStatus("current")


class _RuckusZDWLANConfigWLANServiceType_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANServiceType based on Integer32"""
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
        *(("guestAccess", 2),
          ("hotSpotService", 3),
          ("standardUsage", 1))
    )


_RuckusZDWLANConfigWLANServiceType_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANServiceType_Object = MibTableColumn
ruckusZDWLANConfigWLANServiceType = _RuckusZDWLANConfigWLANServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 8),
    _RuckusZDWLANConfigWLANServiceType_Type()
)
ruckusZDWLANConfigWLANServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANServiceType.setStatus("current")


class _RuckusZDWLANConfigAuthentication_Type(Integer32):
    """Custom type ruckusZDWLANConfigAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eap", 3),
          ("eap-mac-mix", 5),
          ("mac-address", 4),
          ("open", 1),
          ("shared", 2))
    )


_RuckusZDWLANConfigAuthentication_Type.__name__ = "Integer32"
_RuckusZDWLANConfigAuthentication_Object = MibTableColumn
ruckusZDWLANConfigAuthentication = _RuckusZDWLANConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 10),
    _RuckusZDWLANConfigAuthentication_Type()
)
ruckusZDWLANConfigAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAuthentication.setStatus("current")


class _RuckusZDWLANConfigEncryption_Type(Integer32):
    """Custom type ruckusZDWLANConfigEncryption based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none-enc", 6),
          ("wep-128", 5),
          ("wep-64", 4),
          ("wpa", 1),
          ("wpa-Mixed", 3),
          ("wpa2", 2))
    )


_RuckusZDWLANConfigEncryption_Type.__name__ = "Integer32"
_RuckusZDWLANConfigEncryption_Object = MibTableColumn
ruckusZDWLANConfigEncryption = _RuckusZDWLANConfigEncryption_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 12),
    _RuckusZDWLANConfigEncryption_Type()
)
ruckusZDWLANConfigEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigEncryption.setStatus("current")


class _RuckusZDWLANConfigWEPKeyIndex_Type(Integer32):
    """Custom type ruckusZDWLANConfigWEPKeyIndex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusZDWLANConfigWEPKeyIndex_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWEPKeyIndex_Object = MibTableColumn
ruckusZDWLANConfigWEPKeyIndex = _RuckusZDWLANConfigWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 15),
    _RuckusZDWLANConfigWEPKeyIndex_Type()
)
ruckusZDWLANConfigWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWEPKeyIndex.setStatus("current")


class _RuckusZDWLANConfigWEPKey_Type(OctetString):
    """Custom type ruckusZDWLANConfigWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
        ValueSizeConstraint(26, 26),
    )


_RuckusZDWLANConfigWEPKey_Type.__name__ = "OctetString"
_RuckusZDWLANConfigWEPKey_Object = MibTableColumn
ruckusZDWLANConfigWEPKey = _RuckusZDWLANConfigWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 16),
    _RuckusZDWLANConfigWEPKey_Type()
)
ruckusZDWLANConfigWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWEPKey.setStatus("current")


class _RuckusZDWLANConfigWPACipherType_Type(Integer32):
    """Custom type ruckusZDWLANConfigWPACipherType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 2),
          ("auto", 3),
          ("none", 0),
          ("tkip", 1))
    )


_RuckusZDWLANConfigWPACipherType_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWPACipherType_Object = MibTableColumn
ruckusZDWLANConfigWPACipherType = _RuckusZDWLANConfigWPACipherType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 20),
    _RuckusZDWLANConfigWPACipherType_Type()
)
ruckusZDWLANConfigWPACipherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWPACipherType.setStatus("current")


class _RuckusZDWLANConfigWPAKey_Type(OctetString):
    """Custom type ruckusZDWLANConfigWPAKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
        ValueSizeConstraint(64, 64),
    )


_RuckusZDWLANConfigWPAKey_Type.__name__ = "OctetString"
_RuckusZDWLANConfigWPAKey_Object = MibTableColumn
ruckusZDWLANConfigWPAKey = _RuckusZDWLANConfigWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 21),
    _RuckusZDWLANConfigWPAKey_Type()
)
ruckusZDWLANConfigWPAKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWPAKey.setStatus("current")
_RuckusZDWLANConfigAuthenticationServerID_Type = Integer32
_RuckusZDWLANConfigAuthenticationServerID_Object = MibTableColumn
ruckusZDWLANConfigAuthenticationServerID = _RuckusZDWLANConfigAuthenticationServerID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 25),
    _RuckusZDWLANConfigAuthenticationServerID_Type()
)
ruckusZDWLANConfigAuthenticationServerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAuthenticationServerID.setStatus("current")


class _RuckusZDWLANConfigWirelessClientIsolation_Type(Integer32):
    """Custom type ruckusZDWLANConfigWirelessClientIsolation based on Integer32"""
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
        *(("full", 3),
          ("local", 2),
          ("none", 1))
    )


_RuckusZDWLANConfigWirelessClientIsolation_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWirelessClientIsolation_Object = MibTableColumn
ruckusZDWLANConfigWirelessClientIsolation = _RuckusZDWLANConfigWirelessClientIsolation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 28),
    _RuckusZDWLANConfigWirelessClientIsolation_Type()
)
ruckusZDWLANConfigWirelessClientIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWirelessClientIsolation.setStatus("current")


class _RuckusZDWLANConfigZeroITActivation_Type(Integer32):
    """Custom type ruckusZDWLANConfigZeroITActivation based on Integer32"""
    defaultValue = 2

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


_RuckusZDWLANConfigZeroITActivation_Type.__name__ = "Integer32"
_RuckusZDWLANConfigZeroITActivation_Object = MibTableColumn
ruckusZDWLANConfigZeroITActivation = _RuckusZDWLANConfigZeroITActivation_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 30),
    _RuckusZDWLANConfigZeroITActivation_Type()
)
ruckusZDWLANConfigZeroITActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigZeroITActivation.setStatus("current")


class _RuckusZDWLANConfigWLANHotspotID_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANHotspotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_RuckusZDWLANConfigWLANHotspotID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANHotspotID_Object = MibTableColumn
ruckusZDWLANConfigWLANHotspotID = _RuckusZDWLANConfigWLANHotspotID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 31),
    _RuckusZDWLANConfigWLANHotspotID_Type()
)
ruckusZDWLANConfigWLANHotspotID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANHotspotID.setStatus("current")


class _RuckusZDWLANConfigWLANServicePriority_Type(Integer32):
    """Custom type ruckusZDWLANConfigWLANServicePriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 2))
    )


_RuckusZDWLANConfigWLANServicePriority_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWLANServicePriority_Object = MibTableColumn
ruckusZDWLANConfigWLANServicePriority = _RuckusZDWLANConfigWLANServicePriority_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 32),
    _RuckusZDWLANConfigWLANServicePriority_Type()
)
ruckusZDWLANConfigWLANServicePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWLANServicePriority.setStatus("current")


class _RuckusZDWLANConfigAccountingServerID_Type(Integer32):
    """Custom type ruckusZDWLANConfigAccountingServerID based on Integer32"""
    defaultValue = 0


_RuckusZDWLANConfigAccountingServerID_Object = MibTableColumn
ruckusZDWLANConfigAccountingServerID = _RuckusZDWLANConfigAccountingServerID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 35),
    _RuckusZDWLANConfigAccountingServerID_Type()
)
ruckusZDWLANConfigAccountingServerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAccountingServerID.setStatus("current")


class _RuckusZDWLANConfigAccountingUpdateInterval_Type(Integer32):
    """Custom type ruckusZDWLANConfigAccountingUpdateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_RuckusZDWLANConfigAccountingUpdateInterval_Type.__name__ = "Integer32"
_RuckusZDWLANConfigAccountingUpdateInterval_Object = MibTableColumn
ruckusZDWLANConfigAccountingUpdateInterval = _RuckusZDWLANConfigAccountingUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 36),
    _RuckusZDWLANConfigAccountingUpdateInterval_Type()
)
ruckusZDWLANConfigAccountingUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigAccountingUpdateInterval.setStatus("current")


class _RuckusZDWLANConfigUplinkRate_Type(OctetString):
    """Custom type ruckusZDWLANConfigUplinkRate based on OctetString"""
    defaultValue = OctetString("disable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANConfigUplinkRate_Type.__name__ = "OctetString"
_RuckusZDWLANConfigUplinkRate_Object = MibTableColumn
ruckusZDWLANConfigUplinkRate = _RuckusZDWLANConfigUplinkRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 40),
    _RuckusZDWLANConfigUplinkRate_Type()
)
ruckusZDWLANConfigUplinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigUplinkRate.setStatus("current")


class _RuckusZDWLANConfigDownlinkRate_Type(OctetString):
    """Custom type ruckusZDWLANConfigDownlinkRate based on OctetString"""
    defaultValue = OctetString("disable")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_RuckusZDWLANConfigDownlinkRate_Type.__name__ = "OctetString"
_RuckusZDWLANConfigDownlinkRate_Object = MibTableColumn
ruckusZDWLANConfigDownlinkRate = _RuckusZDWLANConfigDownlinkRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 41),
    _RuckusZDWLANConfigDownlinkRate_Type()
)
ruckusZDWLANConfigDownlinkRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDownlinkRate.setStatus("current")


class _RuckusZDWLANConfigIGMPSnooping_Type(Integer32):
    """Custom type ruckusZDWLANConfigIGMPSnooping based on Integer32"""
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


_RuckusZDWLANConfigIGMPSnooping_Type.__name__ = "Integer32"
_RuckusZDWLANConfigIGMPSnooping_Object = MibTableColumn
ruckusZDWLANConfigIGMPSnooping = _RuckusZDWLANConfigIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 42),
    _RuckusZDWLANConfigIGMPSnooping_Type()
)
ruckusZDWLANConfigIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigIGMPSnooping.setStatus("current")


class _RuckusZDWLANConfigVlanID_Type(Integer32):
    """Custom type ruckusZDWLANConfigVlanID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANConfigVlanID_Type.__name__ = "Integer32"
_RuckusZDWLANConfigVlanID_Object = MibTableColumn
ruckusZDWLANConfigVlanID = _RuckusZDWLANConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 45),
    _RuckusZDWLANConfigVlanID_Type()
)
ruckusZDWLANConfigVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigVlanID.setStatus("current")


class _RuckusZDWLANConfigDynamicVLAN_Type(Integer32):
    """Custom type ruckusZDWLANConfigDynamicVLAN based on Integer32"""
    defaultValue = 2

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


_RuckusZDWLANConfigDynamicVLAN_Type.__name__ = "Integer32"
_RuckusZDWLANConfigDynamicVLAN_Object = MibTableColumn
ruckusZDWLANConfigDynamicVLAN = _RuckusZDWLANConfigDynamicVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 46),
    _RuckusZDWLANConfigDynamicVLAN_Type()
)
ruckusZDWLANConfigDynamicVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigDynamicVLAN.setStatus("current")


class _RuckusZDWLANConfigHideSSID_Type(TruthValue):
    """Custom type ruckusZDWLANConfigHideSSID based on TruthValue"""


_RuckusZDWLANConfigHideSSID_Object = MibTableColumn
ruckusZDWLANConfigHideSSID = _RuckusZDWLANConfigHideSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 50),
    _RuckusZDWLANConfigHideSSID_Type()
)
ruckusZDWLANConfigHideSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigHideSSID.setStatus("current")


class _RuckusZDWLANConfigTunnelMode_Type(TruthValue):
    """Custom type ruckusZDWLANConfigTunnelMode based on TruthValue"""


_RuckusZDWLANConfigTunnelMode_Object = MibTableColumn
ruckusZDWLANConfigTunnelMode = _RuckusZDWLANConfigTunnelMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 52),
    _RuckusZDWLANConfigTunnelMode_Type()
)
ruckusZDWLANConfigTunnelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigTunnelMode.setStatus("current")


class _RuckusZDWLANConfigBackgroundScanning_Type(TruthValue):
    """Custom type ruckusZDWLANConfigBackgroundScanning based on TruthValue"""


_RuckusZDWLANConfigBackgroundScanning_Object = MibTableColumn
ruckusZDWLANConfigBackgroundScanning = _RuckusZDWLANConfigBackgroundScanning_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 53),
    _RuckusZDWLANConfigBackgroundScanning_Type()
)
ruckusZDWLANConfigBackgroundScanning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigBackgroundScanning.setStatus("current")


class _RuckusZDWLANConfigMaxClientsPerAP_Type(Integer32):
    """Custom type ruckusZDWLANConfigMaxClientsPerAP based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RuckusZDWLANConfigMaxClientsPerAP_Type.__name__ = "Integer32"
_RuckusZDWLANConfigMaxClientsPerAP_Object = MibTableColumn
ruckusZDWLANConfigMaxClientsPerAP = _RuckusZDWLANConfigMaxClientsPerAP_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 55),
    _RuckusZDWLANConfigMaxClientsPerAP_Type()
)
ruckusZDWLANConfigMaxClientsPerAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigMaxClientsPerAP.setStatus("current")


class _RuckusZDWLANConfigWebAuthentication_Type(Integer32):
    """Custom type ruckusZDWLANConfigWebAuthentication based on Integer32"""
    defaultValue = 2

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


_RuckusZDWLANConfigWebAuthentication_Type.__name__ = "Integer32"
_RuckusZDWLANConfigWebAuthentication_Object = MibTableColumn
ruckusZDWLANConfigWebAuthentication = _RuckusZDWLANConfigWebAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 60),
    _RuckusZDWLANConfigWebAuthentication_Type()
)
ruckusZDWLANConfigWebAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigWebAuthentication.setStatus("current")
_RuckusZDWLANConfigRowStatus_Type = RowStatus
_RuckusZDWLANConfigRowStatus_Object = MibTableColumn
ruckusZDWLANConfigRowStatus = _RuckusZDWLANConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 1, 1, 63),
    _RuckusZDWLANConfigRowStatus_Type()
)
ruckusZDWLANConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANConfigRowStatus.setStatus("current")
_RuckusZDWLANGroupConfigTable_Object = MibTable
ruckusZDWLANGroupConfigTable = _RuckusZDWLANGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigTable.setStatus("current")
_RuckusZDWLANGroupConfigEntry_Object = MibTableRow
ruckusZDWLANGroupConfigEntry = _RuckusZDWLANGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1)
)
ruckusZDWLANGroupConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigEntry.setStatus("current")


class _RuckusZDWLANGroupID_Type(Integer32):
    """Custom type ruckusZDWLANGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_RuckusZDWLANGroupID_Type.__name__ = "Integer32"
_RuckusZDWLANGroupID_Object = MibTableColumn
ruckusZDWLANGroupID = _RuckusZDWLANGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 1),
    _RuckusZDWLANGroupID_Type()
)
ruckusZDWLANGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupID.setStatus("current")


class _RuckusZDWLANGroupConfigName_Type(DisplayString):
    """Custom type ruckusZDWLANGroupConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDWLANGroupConfigName_Type.__name__ = "DisplayString"
_RuckusZDWLANGroupConfigName_Object = MibTableColumn
ruckusZDWLANGroupConfigName = _RuckusZDWLANGroupConfigName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 5),
    _RuckusZDWLANGroupConfigName_Type()
)
ruckusZDWLANGroupConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigName.setStatus("current")


class _RuckusZDWLANGroupConfigDescription_Type(DisplayString):
    """Custom type ruckusZDWLANGroupConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusZDWLANGroupConfigDescription_Type.__name__ = "DisplayString"
_RuckusZDWLANGroupConfigDescription_Object = MibTableColumn
ruckusZDWLANGroupConfigDescription = _RuckusZDWLANGroupConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 6),
    _RuckusZDWLANGroupConfigDescription_Type()
)
ruckusZDWLANGroupConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigDescription.setStatus("current")
_RuckusZDWLANGroupVlanOverrideStatus_Type = TruthValue
_RuckusZDWLANGroupVlanOverrideStatus_Object = MibTableColumn
ruckusZDWLANGroupVlanOverrideStatus = _RuckusZDWLANGroupVlanOverrideStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 8),
    _RuckusZDWLANGroupVlanOverrideStatus_Type()
)
ruckusZDWLANGroupVlanOverrideStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupVlanOverrideStatus.setStatus("current")
_RuckusZDWLANGroupConfigRowStatus_Type = RowStatus
_RuckusZDWLANGroupConfigRowStatus_Object = MibTableColumn
ruckusZDWLANGroupConfigRowStatus = _RuckusZDWLANGroupConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 2, 1, 15),
    _RuckusZDWLANGroupConfigRowStatus_Type()
)
ruckusZDWLANGroupConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupConfigRowStatus.setStatus("current")
_RuckusZDWLANGroupCfgAttrTable_Object = MibTable
ruckusZDWLANGroupCfgAttrTable = _RuckusZDWLANGroupCfgAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrTable.setStatus("current")
_RuckusZDWLANGroupCfgAttrEntry_Object = MibTableRow
ruckusZDWLANGroupCfgAttrEntry = _RuckusZDWLANGroupCfgAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1)
)
ruckusZDWLANGroupCfgAttrEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANGroupID"),
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDWLANID"),
)
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrEntry.setStatus("current")


class _RuckusZDWLANGroupCfgAttrOverrideType_Type(Integer32):
    """Custom type ruckusZDWLANGroupCfgAttrOverrideType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("tag", 2))
    )


_RuckusZDWLANGroupCfgAttrOverrideType_Type.__name__ = "Integer32"
_RuckusZDWLANGroupCfgAttrOverrideType_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrOverrideType = _RuckusZDWLANGroupCfgAttrOverrideType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 3),
    _RuckusZDWLANGroupCfgAttrOverrideType_Type()
)
ruckusZDWLANGroupCfgAttrOverrideType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrOverrideType.setStatus("current")


class _RuckusZDWLANGroupCfgAttrWGVlanTag_Type(Integer32):
    """Custom type ruckusZDWLANGroupCfgAttrWGVlanTag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusZDWLANGroupCfgAttrWGVlanTag_Type.__name__ = "Integer32"
_RuckusZDWLANGroupCfgAttrWGVlanTag_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrWGVlanTag = _RuckusZDWLANGroupCfgAttrWGVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 4),
    _RuckusZDWLANGroupCfgAttrWGVlanTag_Type()
)
ruckusZDWLANGroupCfgAttrWGVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrWGVlanTag.setStatus("current")
_RuckusZDWLANGroupCfgAttrRowStatus_Type = RowStatus
_RuckusZDWLANGroupCfgAttrRowStatus_Object = MibTableColumn
ruckusZDWLANGroupCfgAttrRowStatus = _RuckusZDWLANGroupCfgAttrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 3, 1, 10),
    _RuckusZDWLANGroupCfgAttrRowStatus_Type()
)
ruckusZDWLANGroupCfgAttrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDWLANGroupCfgAttrRowStatus.setStatus("current")
_RuckusZDHotspotConfigTable_Object = MibTable
ruckusZDHotspotConfigTable = _RuckusZDHotspotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ruckusZDHotspotConfigTable.setStatus("current")
_RuckusZDHotspotConfigEntry_Object = MibTableRow
ruckusZDHotspotConfigEntry = _RuckusZDHotspotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1)
)
ruckusZDHotspotConfigEntry.setIndexNames(
    (0, "RUCKUS-ZD-WLAN-CONFIG-MIB", "ruckusZDHotspotID"),
)
if mibBuilder.loadTexts:
    ruckusZDHotspotConfigEntry.setStatus("current")


class _RuckusZDHotspotID_Type(Integer32):
    """Custom type ruckusZDHotspotID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_RuckusZDHotspotID_Type.__name__ = "Integer32"
_RuckusZDHotspotID_Object = MibTableColumn
ruckusZDHotspotID = _RuckusZDHotspotID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 1),
    _RuckusZDHotspotID_Type()
)
ruckusZDHotspotID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusZDHotspotID.setStatus("current")


class _RuckusZDHotspotName_Type(DisplayString):
    """Custom type ruckusZDHotspotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RuckusZDHotspotName_Type.__name__ = "DisplayString"
_RuckusZDHotspotName_Object = MibTableColumn
ruckusZDHotspotName = _RuckusZDHotspotName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 2),
    _RuckusZDHotspotName_Type()
)
ruckusZDHotspotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotName.setStatus("current")


class _RuckusZDHotspotRedirectLoginPage_Type(DisplayString):
    """Custom type ruckusZDHotspotRedirectLoginPage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDHotspotRedirectLoginPage_Type.__name__ = "DisplayString"
_RuckusZDHotspotRedirectLoginPage_Object = MibTableColumn
ruckusZDHotspotRedirectLoginPage = _RuckusZDHotspotRedirectLoginPage_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 3),
    _RuckusZDHotspotRedirectLoginPage_Type()
)
ruckusZDHotspotRedirectLoginPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectLoginPage.setStatus("current")


class _RuckusZDHotspotRedirectStartURL_Type(DisplayString):
    """Custom type ruckusZDHotspotRedirectStartURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_RuckusZDHotspotRedirectStartURL_Type.__name__ = "DisplayString"
_RuckusZDHotspotRedirectStartURL_Object = MibTableColumn
ruckusZDHotspotRedirectStartURL = _RuckusZDHotspotRedirectStartURL_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 4),
    _RuckusZDHotspotRedirectStartURL_Type()
)
ruckusZDHotspotRedirectStartURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectStartURL.setStatus("current")


class _RuckusZDHotspotRedirectType_Type(Integer32):
    """Custom type ruckusZDHotspotRedirectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("url", 2),
          ("user", 1))
    )


_RuckusZDHotspotRedirectType_Type.__name__ = "Integer32"
_RuckusZDHotspotRedirectType_Object = MibTableColumn
ruckusZDHotspotRedirectType = _RuckusZDHotspotRedirectType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 6),
    _RuckusZDHotspotRedirectType_Type()
)
ruckusZDHotspotRedirectType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusZDHotspotRedirectType.setStatus("current")
_RuckusZDHotspotRowStatus_Type = RowStatus
_RuckusZDHotspotRowStatus_Object = MibTableColumn
ruckusZDHotspotRowStatus = _RuckusZDHotspotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 2, 2, 2, 1, 1, 8, 1, 15),
    _RuckusZDHotspotRowStatus_Type()
)
ruckusZDHotspotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ruckusZDHotspotRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-ZD-WLAN-CONFIG-MIB",
    **{"ruckusZDWLANConfigMIB": ruckusZDWLANConfigMIB,
       "ruckusZDWLANConfigObjects": ruckusZDWLANConfigObjects,
       "ruckusZDWLANConfig": ruckusZDWLANConfig,
       "ruckusZDWLANConfigTable": ruckusZDWLANConfigTable,
       "ruckusZDWLANConfigEntry": ruckusZDWLANConfigEntry,
       "ruckusZDWLANID": ruckusZDWLANID,
       "ruckusZDWLANConfigSSID": ruckusZDWLANConfigSSID,
       "ruckusZDWLANConfigDescription": ruckusZDWLANConfigDescription,
       "ruckusZDWLANConfigName": ruckusZDWLANConfigName,
       "ruckusZDWLANConfigWLANServiceType": ruckusZDWLANConfigWLANServiceType,
       "ruckusZDWLANConfigAuthentication": ruckusZDWLANConfigAuthentication,
       "ruckusZDWLANConfigEncryption": ruckusZDWLANConfigEncryption,
       "ruckusZDWLANConfigWEPKeyIndex": ruckusZDWLANConfigWEPKeyIndex,
       "ruckusZDWLANConfigWEPKey": ruckusZDWLANConfigWEPKey,
       "ruckusZDWLANConfigWPACipherType": ruckusZDWLANConfigWPACipherType,
       "ruckusZDWLANConfigWPAKey": ruckusZDWLANConfigWPAKey,
       "ruckusZDWLANConfigAuthenticationServerID": ruckusZDWLANConfigAuthenticationServerID,
       "ruckusZDWLANConfigWirelessClientIsolation": ruckusZDWLANConfigWirelessClientIsolation,
       "ruckusZDWLANConfigZeroITActivation": ruckusZDWLANConfigZeroITActivation,
       "ruckusZDWLANConfigWLANHotspotID": ruckusZDWLANConfigWLANHotspotID,
       "ruckusZDWLANConfigWLANServicePriority": ruckusZDWLANConfigWLANServicePriority,
       "ruckusZDWLANConfigAccountingServerID": ruckusZDWLANConfigAccountingServerID,
       "ruckusZDWLANConfigAccountingUpdateInterval": ruckusZDWLANConfigAccountingUpdateInterval,
       "ruckusZDWLANConfigUplinkRate": ruckusZDWLANConfigUplinkRate,
       "ruckusZDWLANConfigDownlinkRate": ruckusZDWLANConfigDownlinkRate,
       "ruckusZDWLANConfigIGMPSnooping": ruckusZDWLANConfigIGMPSnooping,
       "ruckusZDWLANConfigVlanID": ruckusZDWLANConfigVlanID,
       "ruckusZDWLANConfigDynamicVLAN": ruckusZDWLANConfigDynamicVLAN,
       "ruckusZDWLANConfigHideSSID": ruckusZDWLANConfigHideSSID,
       "ruckusZDWLANConfigTunnelMode": ruckusZDWLANConfigTunnelMode,
       "ruckusZDWLANConfigBackgroundScanning": ruckusZDWLANConfigBackgroundScanning,
       "ruckusZDWLANConfigMaxClientsPerAP": ruckusZDWLANConfigMaxClientsPerAP,
       "ruckusZDWLANConfigWebAuthentication": ruckusZDWLANConfigWebAuthentication,
       "ruckusZDWLANConfigRowStatus": ruckusZDWLANConfigRowStatus,
       "ruckusZDWLANGroupConfigTable": ruckusZDWLANGroupConfigTable,
       "ruckusZDWLANGroupConfigEntry": ruckusZDWLANGroupConfigEntry,
       "ruckusZDWLANGroupID": ruckusZDWLANGroupID,
       "ruckusZDWLANGroupConfigName": ruckusZDWLANGroupConfigName,
       "ruckusZDWLANGroupConfigDescription": ruckusZDWLANGroupConfigDescription,
       "ruckusZDWLANGroupVlanOverrideStatus": ruckusZDWLANGroupVlanOverrideStatus,
       "ruckusZDWLANGroupConfigRowStatus": ruckusZDWLANGroupConfigRowStatus,
       "ruckusZDWLANGroupCfgAttrTable": ruckusZDWLANGroupCfgAttrTable,
       "ruckusZDWLANGroupCfgAttrEntry": ruckusZDWLANGroupCfgAttrEntry,
       "ruckusZDWLANGroupCfgAttrOverrideType": ruckusZDWLANGroupCfgAttrOverrideType,
       "ruckusZDWLANGroupCfgAttrWGVlanTag": ruckusZDWLANGroupCfgAttrWGVlanTag,
       "ruckusZDWLANGroupCfgAttrRowStatus": ruckusZDWLANGroupCfgAttrRowStatus,
       "ruckusZDHotspotConfigTable": ruckusZDHotspotConfigTable,
       "ruckusZDHotspotConfigEntry": ruckusZDHotspotConfigEntry,
       "ruckusZDHotspotID": ruckusZDHotspotID,
       "ruckusZDHotspotName": ruckusZDHotspotName,
       "ruckusZDHotspotRedirectLoginPage": ruckusZDHotspotRedirectLoginPage,
       "ruckusZDHotspotRedirectStartURL": ruckusZDHotspotRedirectStartURL,
       "ruckusZDHotspotRedirectType": ruckusZDHotspotRedirectType,
       "ruckusZDHotspotRowStatus": ruckusZDHotspotRowStatus}
)
