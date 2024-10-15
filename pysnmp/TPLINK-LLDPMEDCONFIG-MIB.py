# SNMP MIB module (TPLINK-LLDPMEDCONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-LLDPMEDCONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:20 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkLldpMIBObjects,) = mibBuilder.importSymbols(
    "TPLINK-LLDP-MIB",
    "tplinkLldpMIBObjects")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

lldpMedNeighborInfo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5)
)
lldpMedNeighborInfo.setRevisions(
        ("2011-09-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpMed_ObjectIdentity = ObjectIdentity
lldpMed = _LldpMed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4)
)
_LldpMedGlobalConfig_ObjectIdentity = ObjectIdentity
lldpMedGlobalConfig = _LldpMedGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 1)
)


class _LldpMedGlobalConfigFastStartRepeatCount_Type(Integer32):
    """Custom type lldpMedGlobalConfigFastStartRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_LldpMedGlobalConfigFastStartRepeatCount_Type.__name__ = "Integer32"
_LldpMedGlobalConfigFastStartRepeatCount_Object = MibScalar
lldpMedGlobalConfigFastStartRepeatCount = _LldpMedGlobalConfigFastStartRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 1, 1),
    _LldpMedGlobalConfigFastStartRepeatCount_Type()
)
lldpMedGlobalConfigFastStartRepeatCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedGlobalConfigFastStartRepeatCount.setStatus("current")
_LldpMedPortConfigTable_Object = MibTable
lldpMedPortConfigTable = _LldpMedPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lldpMedPortConfigTable.setStatus("current")
_LldpMedPortConfigEntry_Object = MibTableRow
lldpMedPortConfigEntry = _LldpMedPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1)
)
lldpMedPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpMedPortConfigEntry.setStatus("current")


class _LldpMedConfigPortId_Type(OctetString):
    """Custom type lldpMedConfigPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpMedConfigPortId_Type.__name__ = "OctetString"
_LldpMedConfigPortId_Object = MibTableColumn
lldpMedConfigPortId = _LldpMedConfigPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 1),
    _LldpMedConfigPortId_Type()
)
lldpMedConfigPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedConfigPortId.setStatus("current")


class _LldpMedConfigPortStatus_Type(Integer32):
    """Custom type lldpMedConfigPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpMedConfigPortStatus_Type.__name__ = "Integer32"
_LldpMedConfigPortStatus_Object = MibTableColumn
lldpMedConfigPortStatus = _LldpMedConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 2),
    _LldpMedConfigPortStatus_Type()
)
lldpMedConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortStatus.setStatus("current")


class _LldpMedConfigPortTlvNetworkPolicy_Type(Integer32):
    """Custom type lldpMedConfigPortTlvNetworkPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpMedConfigPortTlvNetworkPolicy_Type.__name__ = "Integer32"
_LldpMedConfigPortTlvNetworkPolicy_Object = MibTableColumn
lldpMedConfigPortTlvNetworkPolicy = _LldpMedConfigPortTlvNetworkPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 3),
    _LldpMedConfigPortTlvNetworkPolicy_Type()
)
lldpMedConfigPortTlvNetworkPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortTlvNetworkPolicy.setStatus("current")


class _LldpMedConfigPortTlvLocationId_Type(Integer32):
    """Custom type lldpMedConfigPortTlvLocationId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpMedConfigPortTlvLocationId_Type.__name__ = "Integer32"
_LldpMedConfigPortTlvLocationId_Object = MibTableColumn
lldpMedConfigPortTlvLocationId = _LldpMedConfigPortTlvLocationId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 4),
    _LldpMedConfigPortTlvLocationId_Type()
)
lldpMedConfigPortTlvLocationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortTlvLocationId.setStatus("current")


class _LldpMedConfigPortTlvExtendedPower_Type(Integer32):
    """Custom type lldpMedConfigPortTlvExtendedPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpMedConfigPortTlvExtendedPower_Type.__name__ = "Integer32"
_LldpMedConfigPortTlvExtendedPower_Object = MibTableColumn
lldpMedConfigPortTlvExtendedPower = _LldpMedConfigPortTlvExtendedPower_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 5),
    _LldpMedConfigPortTlvExtendedPower_Type()
)
lldpMedConfigPortTlvExtendedPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortTlvExtendedPower.setStatus("current")


class _LldpMedConfigPortTlvInventory_Type(Integer32):
    """Custom type lldpMedConfigPortTlvInventory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LldpMedConfigPortTlvInventory_Type.__name__ = "Integer32"
_LldpMedConfigPortTlvInventory_Object = MibTableColumn
lldpMedConfigPortTlvInventory = _LldpMedConfigPortTlvInventory_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 2, 1, 6),
    _LldpMedConfigPortTlvInventory_Type()
)
lldpMedConfigPortTlvInventory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortTlvInventory.setStatus("current")
_LldpMedPortConfigTlvLocationTable_Object = MibTable
lldpMedPortConfigTlvLocationTable = _LldpMedPortConfigTlvLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lldpMedPortConfigTlvLocationTable.setStatus("current")
_LldpMedPortConfigTlvLocationEntry_Object = MibTableRow
lldpMedPortConfigTlvLocationEntry = _LldpMedPortConfigTlvLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1)
)
lldpMedPortConfigTlvLocationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpMedPortConfigTlvLocationEntry.setStatus("current")


class _LldpMedConfigLocationPortId_Type(OctetString):
    """Custom type lldpMedConfigLocationPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpMedConfigLocationPortId_Type.__name__ = "OctetString"
_LldpMedConfigLocationPortId_Object = MibTableColumn
lldpMedConfigLocationPortId = _LldpMedConfigLocationPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 1),
    _LldpMedConfigLocationPortId_Type()
)
lldpMedConfigLocationPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedConfigLocationPortId.setStatus("current")


class _LldpMedConfigPortLocationEmergencyNumber_Type(OctetString):
    """Custom type lldpMedConfigPortLocationEmergencyNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 25),
    )


_LldpMedConfigPortLocationEmergencyNumber_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationEmergencyNumber_Object = MibTableColumn
lldpMedConfigPortLocationEmergencyNumber = _LldpMedConfigPortLocationEmergencyNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 2),
    _LldpMedConfigPortLocationEmergencyNumber_Type()
)
lldpMedConfigPortLocationEmergencyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationEmergencyNumber.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressWhat_Type(Integer32):
    """Custom type lldpMedConfigPortLocationCivicAddressWhat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-server", 0),
          ("lldp-med-endpoint", 2),
          ("switch", 1))
    )


_LldpMedConfigPortLocationCivicAddressWhat_Type.__name__ = "Integer32"
_LldpMedConfigPortLocationCivicAddressWhat_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressWhat = _LldpMedConfigPortLocationCivicAddressWhat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 3),
    _LldpMedConfigPortLocationCivicAddressWhat_Type()
)
lldpMedConfigPortLocationCivicAddressWhat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressWhat.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressCountryCode_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_LldpMedConfigPortLocationCivicAddressCountryCode_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressCountryCode_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressCountryCode = _LldpMedConfigPortLocationCivicAddressCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 4),
    _LldpMedConfigPortLocationCivicAddressCountryCode_Type()
)
lldpMedConfigPortLocationCivicAddressCountryCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressCountryCode.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressLanguage_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressLanguage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressLanguage_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressLanguage_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressLanguage = _LldpMedConfigPortLocationCivicAddressLanguage_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 5),
    _LldpMedConfigPortLocationCivicAddressLanguage_Type()
)
lldpMedConfigPortLocationCivicAddressLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressLanguage.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressProvince_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressProvince based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressProvince_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressProvince_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressProvince = _LldpMedConfigPortLocationCivicAddressProvince_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 6),
    _LldpMedConfigPortLocationCivicAddressProvince_Type()
)
lldpMedConfigPortLocationCivicAddressProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressProvince.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressCounty_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressCounty based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressCounty_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressCounty_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressCounty = _LldpMedConfigPortLocationCivicAddressCounty_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 7),
    _LldpMedConfigPortLocationCivicAddressCounty_Type()
)
lldpMedConfigPortLocationCivicAddressCounty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressCounty.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressCity_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressCity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressCity_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressCity_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressCity = _LldpMedConfigPortLocationCivicAddressCity_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 8),
    _LldpMedConfigPortLocationCivicAddressCity_Type()
)
lldpMedConfigPortLocationCivicAddressCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressCity.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressStreet_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressStreet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressStreet_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressStreet_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressStreet = _LldpMedConfigPortLocationCivicAddressStreet_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 9),
    _LldpMedConfigPortLocationCivicAddressStreet_Type()
)
lldpMedConfigPortLocationCivicAddressStreet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressStreet.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressHouseNumber_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressHouseNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressHouseNumber_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressHouseNumber_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressHouseNumber = _LldpMedConfigPortLocationCivicAddressHouseNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 10),
    _LldpMedConfigPortLocationCivicAddressHouseNumber_Type()
)
lldpMedConfigPortLocationCivicAddressHouseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressHouseNumber.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressName_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressName_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressName_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressName = _LldpMedConfigPortLocationCivicAddressName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 11),
    _LldpMedConfigPortLocationCivicAddressName_Type()
)
lldpMedConfigPortLocationCivicAddressName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressName.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressPostalZipCode_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressPostalZipCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressPostalZipCode_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressPostalZipCode_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressPostalZipCode = _LldpMedConfigPortLocationCivicAddressPostalZipCode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 12),
    _LldpMedConfigPortLocationCivicAddressPostalZipCode_Type()
)
lldpMedConfigPortLocationCivicAddressPostalZipCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressPostalZipCode.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressRoomNumber_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressRoomNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressRoomNumber_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressRoomNumber_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressRoomNumber = _LldpMedConfigPortLocationCivicAddressRoomNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 13),
    _LldpMedConfigPortLocationCivicAddressRoomNumber_Type()
)
lldpMedConfigPortLocationCivicAddressRoomNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressRoomNumber.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressPostOfficeBox based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressPostOfficeBox_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressPostOfficeBox = _LldpMedConfigPortLocationCivicAddressPostOfficeBox_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 14),
    _LldpMedConfigPortLocationCivicAddressPostOfficeBox_Type()
)
lldpMedConfigPortLocationCivicAddressPostOfficeBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressPostOfficeBox.setStatus("current")


class _LldpMedConfigPortLocationCivicAddressAdditional_Type(OctetString):
    """Custom type lldpMedConfigPortLocationCivicAddressAdditional based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_LldpMedConfigPortLocationCivicAddressAdditional_Type.__name__ = "OctetString"
_LldpMedConfigPortLocationCivicAddressAdditional_Object = MibTableColumn
lldpMedConfigPortLocationCivicAddressAdditional = _LldpMedConfigPortLocationCivicAddressAdditional_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 3, 1, 15),
    _LldpMedConfigPortLocationCivicAddressAdditional_Type()
)
lldpMedConfigPortLocationCivicAddressAdditional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMedConfigPortLocationCivicAddressAdditional.setStatus("current")
_LldpMedLocalInfoTable_Object = MibTable
lldpMedLocalInfoTable = _LldpMedLocalInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lldpMedLocalInfoTable.setStatus("current")
_LldpMedLocalInfoEntry_Object = MibTableRow
lldpMedLocalInfoEntry = _LldpMedLocalInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1)
)
lldpMedLocalInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpMedLocalInfoEntry.setStatus("current")


class _LldpMedLocalPortId_Type(OctetString):
    """Custom type lldpMedLocalPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpMedLocalPortId_Type.__name__ = "OctetString"
_LldpMedLocalPortId_Object = MibTableColumn
lldpMedLocalPortId = _LldpMedLocalPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 1),
    _LldpMedLocalPortId_Type()
)
lldpMedLocalPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalPortId.setStatus("current")


class _LldpMEDLocalCapabilities_Type(OctetString):
    """Custom type lldpMEDLocalCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_LldpMEDLocalCapabilities_Type.__name__ = "OctetString"
_LldpMEDLocalCapabilities_Object = MibTableColumn
lldpMEDLocalCapabilities = _LldpMEDLocalCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 2),
    _LldpMEDLocalCapabilities_Type()
)
lldpMEDLocalCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMEDLocalCapabilities.setStatus("current")


class _LldpMedLocalDeviceType_Type(OctetString):
    """Custom type lldpMedLocalDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalDeviceType_Type.__name__ = "OctetString"
_LldpMedLocalDeviceType_Object = MibTableColumn
lldpMedLocalDeviceType = _LldpMedLocalDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 3),
    _LldpMedLocalDeviceType_Type()
)
lldpMedLocalDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalDeviceType.setStatus("current")


class _LldpMedLocalApplicationType_Type(OctetString):
    """Custom type lldpMedLocalApplicationType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalApplicationType_Type.__name__ = "OctetString"
_LldpMedLocalApplicationType_Object = MibTableColumn
lldpMedLocalApplicationType = _LldpMedLocalApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 4),
    _LldpMedLocalApplicationType_Type()
)
lldpMedLocalApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalApplicationType.setStatus("current")


class _LldpMedLocalUnknownPolicy_Type(OctetString):
    """Custom type lldpMedLocalUnknownPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LldpMedLocalUnknownPolicy_Type.__name__ = "OctetString"
_LldpMedLocalUnknownPolicy_Object = MibTableColumn
lldpMedLocalUnknownPolicy = _LldpMedLocalUnknownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 5),
    _LldpMedLocalUnknownPolicy_Type()
)
lldpMedLocalUnknownPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalUnknownPolicy.setStatus("current")


class _LldpMedLocalAppTagged_Type(OctetString):
    """Custom type lldpMedLocalAppTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LldpMedLocalAppTagged_Type.__name__ = "OctetString"
_LldpMedLocalAppTagged_Object = MibTableColumn
lldpMedLocalAppTagged = _LldpMedLocalAppTagged_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 6),
    _LldpMedLocalAppTagged_Type()
)
lldpMedLocalAppTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalAppTagged.setStatus("current")
_LldpMedLocalAppVLANID_Type = Integer32
_LldpMedLocalAppVLANID_Object = MibTableColumn
lldpMedLocalAppVLANID = _LldpMedLocalAppVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 7),
    _LldpMedLocalAppVLANID_Type()
)
lldpMedLocalAppVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalAppVLANID.setStatus("current")
_LldpMedLocalAppLayer2Priority_Type = Integer32
_LldpMedLocalAppLayer2Priority_Object = MibTableColumn
lldpMedLocalAppLayer2Priority = _LldpMedLocalAppLayer2Priority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 8),
    _LldpMedLocalAppLayer2Priority_Type()
)
lldpMedLocalAppLayer2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalAppLayer2Priority.setStatus("current")
_LldpMedLocalAppDSCP_Type = Integer32
_LldpMedLocalAppDSCP_Object = MibTableColumn
lldpMedLocalAppDSCP = _LldpMedLocalAppDSCP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 9),
    _LldpMedLocalAppDSCP_Type()
)
lldpMedLocalAppDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalAppDSCP.setStatus("current")


class _LldpMedLocalLocationDataFormat_Type(OctetString):
    """Custom type lldpMedLocalLocationDataFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalLocationDataFormat_Type.__name__ = "OctetString"
_LldpMedLocalLocationDataFormat_Object = MibTableColumn
lldpMedLocalLocationDataFormat = _LldpMedLocalLocationDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 10),
    _LldpMedLocalLocationDataFormat_Type()
)
lldpMedLocalLocationDataFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalLocationDataFormat.setStatus("current")


class _LldpMedLocalLocationID_Type(OctetString):
    """Custom type lldpMedLocalLocationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpMedLocalLocationID_Type.__name__ = "OctetString"
_LldpMedLocalLocationID_Object = MibTableColumn
lldpMedLocalLocationID = _LldpMedLocalLocationID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 11),
    _LldpMedLocalLocationID_Type()
)
lldpMedLocalLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalLocationID.setStatus("current")


class _LldpMedLocalPowerType_Type(OctetString):
    """Custom type lldpMedLocalPowerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalPowerType_Type.__name__ = "OctetString"
_LldpMedLocalPowerType_Object = MibTableColumn
lldpMedLocalPowerType = _LldpMedLocalPowerType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 12),
    _LldpMedLocalPowerType_Type()
)
lldpMedLocalPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalPowerType.setStatus("current")


class _LldpMedLocalPowerSource_Type(OctetString):
    """Custom type lldpMedLocalPowerSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalPowerSource_Type.__name__ = "OctetString"
_LldpMedLocalPowerSource_Object = MibTableColumn
lldpMedLocalPowerSource = _LldpMedLocalPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 13),
    _LldpMedLocalPowerSource_Type()
)
lldpMedLocalPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalPowerSource.setStatus("current")


class _LldpMedLocalPowerPriority_Type(OctetString):
    """Custom type lldpMedLocalPowerPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalPowerPriority_Type.__name__ = "OctetString"
_LldpMedLocalPowerPriority_Object = MibTableColumn
lldpMedLocalPowerPriority = _LldpMedLocalPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 14),
    _LldpMedLocalPowerPriority_Type()
)
lldpMedLocalPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalPowerPriority.setStatus("current")


class _LldpMedLocalPowerValue_Type(OctetString):
    """Custom type lldpMedLocalPowerValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedLocalPowerValue_Type.__name__ = "OctetString"
_LldpMedLocalPowerValue_Object = MibTableColumn
lldpMedLocalPowerValue = _LldpMedLocalPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 15),
    _LldpMedLocalPowerValue_Type()
)
lldpMedLocalPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalPowerValue.setStatus("current")


class _LldpMedLocalInventoryHardwareRevision_Type(OctetString):
    """Custom type lldpMedLocalInventoryHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventoryHardwareRevision_Type.__name__ = "OctetString"
_LldpMedLocalInventoryHardwareRevision_Object = MibTableColumn
lldpMedLocalInventoryHardwareRevision = _LldpMedLocalInventoryHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 16),
    _LldpMedLocalInventoryHardwareRevision_Type()
)
lldpMedLocalInventoryHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventoryHardwareRevision.setStatus("current")


class _LldpMedLocalInventoryFirmwareRevision_Type(OctetString):
    """Custom type lldpMedLocalInventoryFirmwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventoryFirmwareRevision_Type.__name__ = "OctetString"
_LldpMedLocalInventoryFirmwareRevision_Object = MibTableColumn
lldpMedLocalInventoryFirmwareRevision = _LldpMedLocalInventoryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 17),
    _LldpMedLocalInventoryFirmwareRevision_Type()
)
lldpMedLocalInventoryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventoryFirmwareRevision.setStatus("current")


class _LldpMedLocalInventorySoftwareRevision_Type(OctetString):
    """Custom type lldpMedLocalInventorySoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventorySoftwareRevision_Type.__name__ = "OctetString"
_LldpMedLocalInventorySoftwareRevision_Object = MibTableColumn
lldpMedLocalInventorySoftwareRevision = _LldpMedLocalInventorySoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 18),
    _LldpMedLocalInventorySoftwareRevision_Type()
)
lldpMedLocalInventorySoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventorySoftwareRevision.setStatus("current")


class _LldpMedLocalInventorySerialNumber_Type(OctetString):
    """Custom type lldpMedLocalInventorySerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventorySerialNumber_Type.__name__ = "OctetString"
_LldpMedLocalInventorySerialNumber_Object = MibTableColumn
lldpMedLocalInventorySerialNumber = _LldpMedLocalInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 19),
    _LldpMedLocalInventorySerialNumber_Type()
)
lldpMedLocalInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventorySerialNumber.setStatus("current")


class _LldpMedLocalInventoryManufacturerName_Type(OctetString):
    """Custom type lldpMedLocalInventoryManufacturerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventoryManufacturerName_Type.__name__ = "OctetString"
_LldpMedLocalInventoryManufacturerName_Object = MibTableColumn
lldpMedLocalInventoryManufacturerName = _LldpMedLocalInventoryManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 20),
    _LldpMedLocalInventoryManufacturerName_Type()
)
lldpMedLocalInventoryManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventoryManufacturerName.setStatus("current")


class _LldpMedLocalInventoryModelName_Type(OctetString):
    """Custom type lldpMedLocalInventoryModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventoryModelName_Type.__name__ = "OctetString"
_LldpMedLocalInventoryModelName_Object = MibTableColumn
lldpMedLocalInventoryModelName = _LldpMedLocalInventoryModelName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 21),
    _LldpMedLocalInventoryModelName_Type()
)
lldpMedLocalInventoryModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventoryModelName.setStatus("current")


class _LldpMedLocalInventoryAssetID_Type(OctetString):
    """Custom type lldpMedLocalInventoryAssetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedLocalInventoryAssetID_Type.__name__ = "OctetString"
_LldpMedLocalInventoryAssetID_Object = MibTableColumn
lldpMedLocalInventoryAssetID = _LldpMedLocalInventoryAssetID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 4, 1, 22),
    _LldpMedLocalInventoryAssetID_Type()
)
lldpMedLocalInventoryAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedLocalInventoryAssetID.setStatus("current")
_LldpMedNeighborInfoTable_Object = MibTable
lldpMedNeighborInfoTable = _LldpMedNeighborInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    lldpMedNeighborInfoTable.setStatus("current")
_LldpMedNeighborInfoEntry_Object = MibTableRow
lldpMedNeighborInfoEntry = _LldpMedNeighborInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1)
)
lldpMedNeighborInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-LLDPMEDCONFIG-MIB", "lldpMedNeighborPortIndexId"),
)
if mibBuilder.loadTexts:
    lldpMedNeighborInfoEntry.setStatus("current")


class _LldpMedNeighborPortId_Type(OctetString):
    """Custom type lldpMedNeighborPortId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpMedNeighborPortId_Type.__name__ = "OctetString"
_LldpMedNeighborPortId_Object = MibTableColumn
lldpMedNeighborPortId = _LldpMedNeighborPortId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 1),
    _LldpMedNeighborPortId_Type()
)
lldpMedNeighborPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPortId.setStatus("current")
_LldpMedNeighborPortIndexId_Type = Integer32
_LldpMedNeighborPortIndexId_Object = MibTableColumn
lldpMedNeighborPortIndexId = _LldpMedNeighborPortIndexId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 2),
    _LldpMedNeighborPortIndexId_Type()
)
lldpMedNeighborPortIndexId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPortIndexId.setStatus("current")


class _LldpMEDNeighborCapabilities_Type(OctetString):
    """Custom type lldpMEDNeighborCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_LldpMEDNeighborCapabilities_Type.__name__ = "OctetString"
_LldpMEDNeighborCapabilities_Object = MibTableColumn
lldpMEDNeighborCapabilities = _LldpMEDNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 3),
    _LldpMEDNeighborCapabilities_Type()
)
lldpMEDNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMEDNeighborCapabilities.setStatus("current")


class _LldpMedNeighborDeviceType_Type(OctetString):
    """Custom type lldpMedNeighborDeviceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborDeviceType_Type.__name__ = "OctetString"
_LldpMedNeighborDeviceType_Object = MibTableColumn
lldpMedNeighborDeviceType = _LldpMedNeighborDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 4),
    _LldpMedNeighborDeviceType_Type()
)
lldpMedNeighborDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborDeviceType.setStatus("current")


class _LldpMedNeighborLocationDataFormat_Type(OctetString):
    """Custom type lldpMedNeighborLocationDataFormat based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborLocationDataFormat_Type.__name__ = "OctetString"
_LldpMedNeighborLocationDataFormat_Object = MibTableColumn
lldpMedNeighborLocationDataFormat = _LldpMedNeighborLocationDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 5),
    _LldpMedNeighborLocationDataFormat_Type()
)
lldpMedNeighborLocationDataFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborLocationDataFormat.setStatus("current")


class _LldpMedNeighborLocationID_Type(OctetString):
    """Custom type lldpMedNeighborLocationID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LldpMedNeighborLocationID_Type.__name__ = "OctetString"
_LldpMedNeighborLocationID_Object = MibTableColumn
lldpMedNeighborLocationID = _LldpMedNeighborLocationID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 6),
    _LldpMedNeighborLocationID_Type()
)
lldpMedNeighborLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborLocationID.setStatus("current")


class _LldpMedNeighborPowerType_Type(OctetString):
    """Custom type lldpMedNeighborPowerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborPowerType_Type.__name__ = "OctetString"
_LldpMedNeighborPowerType_Object = MibTableColumn
lldpMedNeighborPowerType = _LldpMedNeighborPowerType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 7),
    _LldpMedNeighborPowerType_Type()
)
lldpMedNeighborPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPowerType.setStatus("current")


class _LldpMedNeighborPowerSource_Type(OctetString):
    """Custom type lldpMedNeighborPowerSource based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborPowerSource_Type.__name__ = "OctetString"
_LldpMedNeighborPowerSource_Object = MibTableColumn
lldpMedNeighborPowerSource = _LldpMedNeighborPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 8),
    _LldpMedNeighborPowerSource_Type()
)
lldpMedNeighborPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPowerSource.setStatus("current")


class _LldpMedNeighborPowerPriority_Type(OctetString):
    """Custom type lldpMedNeighborPowerPriority based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborPowerPriority_Type.__name__ = "OctetString"
_LldpMedNeighborPowerPriority_Object = MibTableColumn
lldpMedNeighborPowerPriority = _LldpMedNeighborPowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 9),
    _LldpMedNeighborPowerPriority_Type()
)
lldpMedNeighborPowerPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPowerPriority.setStatus("current")


class _LldpMedNeighborPowerValue_Type(OctetString):
    """Custom type lldpMedNeighborPowerValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborPowerValue_Type.__name__ = "OctetString"
_LldpMedNeighborPowerValue_Object = MibTableColumn
lldpMedNeighborPowerValue = _LldpMedNeighborPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 10),
    _LldpMedNeighborPowerValue_Type()
)
lldpMedNeighborPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPowerValue.setStatus("current")


class _LldpMedNeighborInventoryHardwareRevision_Type(OctetString):
    """Custom type lldpMedNeighborInventoryHardwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventoryHardwareRevision_Type.__name__ = "OctetString"
_LldpMedNeighborInventoryHardwareRevision_Object = MibTableColumn
lldpMedNeighborInventoryHardwareRevision = _LldpMedNeighborInventoryHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 11),
    _LldpMedNeighborInventoryHardwareRevision_Type()
)
lldpMedNeighborInventoryHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventoryHardwareRevision.setStatus("current")


class _LldpMedNeighborInventoryFirmwareRevision_Type(OctetString):
    """Custom type lldpMedNeighborInventoryFirmwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventoryFirmwareRevision_Type.__name__ = "OctetString"
_LldpMedNeighborInventoryFirmwareRevision_Object = MibTableColumn
lldpMedNeighborInventoryFirmwareRevision = _LldpMedNeighborInventoryFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 12),
    _LldpMedNeighborInventoryFirmwareRevision_Type()
)
lldpMedNeighborInventoryFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventoryFirmwareRevision.setStatus("current")


class _LldpMedNeighborInventorySoftwareRevision_Type(OctetString):
    """Custom type lldpMedNeighborInventorySoftwareRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventorySoftwareRevision_Type.__name__ = "OctetString"
_LldpMedNeighborInventorySoftwareRevision_Object = MibTableColumn
lldpMedNeighborInventorySoftwareRevision = _LldpMedNeighborInventorySoftwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 13),
    _LldpMedNeighborInventorySoftwareRevision_Type()
)
lldpMedNeighborInventorySoftwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventorySoftwareRevision.setStatus("current")


class _LldpMedNeighborInventorySerialNumber_Type(OctetString):
    """Custom type lldpMedNeighborInventorySerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventorySerialNumber_Type.__name__ = "OctetString"
_LldpMedNeighborInventorySerialNumber_Object = MibTableColumn
lldpMedNeighborInventorySerialNumber = _LldpMedNeighborInventorySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 14),
    _LldpMedNeighborInventorySerialNumber_Type()
)
lldpMedNeighborInventorySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventorySerialNumber.setStatus("current")


class _LldpMedNeighborInventoryManufacturerName_Type(OctetString):
    """Custom type lldpMedNeighborInventoryManufacturerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventoryManufacturerName_Type.__name__ = "OctetString"
_LldpMedNeighborInventoryManufacturerName_Object = MibTableColumn
lldpMedNeighborInventoryManufacturerName = _LldpMedNeighborInventoryManufacturerName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 15),
    _LldpMedNeighborInventoryManufacturerName_Type()
)
lldpMedNeighborInventoryManufacturerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventoryManufacturerName.setStatus("current")


class _LldpMedNeighborInventoryModelName_Type(OctetString):
    """Custom type lldpMedNeighborInventoryModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventoryModelName_Type.__name__ = "OctetString"
_LldpMedNeighborInventoryModelName_Object = MibTableColumn
lldpMedNeighborInventoryModelName = _LldpMedNeighborInventoryModelName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 16),
    _LldpMedNeighborInventoryModelName_Type()
)
lldpMedNeighborInventoryModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventoryModelName.setStatus("current")


class _LldpMedNeighborInventoryAssetID_Type(OctetString):
    """Custom type lldpMedNeighborInventoryAssetID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LldpMedNeighborInventoryAssetID_Type.__name__ = "OctetString"
_LldpMedNeighborInventoryAssetID_Object = MibTableColumn
lldpMedNeighborInventoryAssetID = _LldpMedNeighborInventoryAssetID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 1, 1, 17),
    _LldpMedNeighborInventoryAssetID_Type()
)
lldpMedNeighborInventoryAssetID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborInventoryAssetID.setStatus("current")
_LldpMedNeighborMediaPolicyInfoTable_Object = MibTable
lldpMedNeighborMediaPolicyInfoTable = _LldpMedNeighborMediaPolicyInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2)
)
if mibBuilder.loadTexts:
    lldpMedNeighborMediaPolicyInfoTable.setStatus("current")
_LldpMedNeighborMediaPolicyInfoEntry_Object = MibTableRow
lldpMedNeighborMediaPolicyInfoEntry = _LldpMedNeighborMediaPolicyInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1)
)
lldpMedNeighborMediaPolicyInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TPLINK-LLDPMEDCONFIG-MIB", "lldpMedNeighborPortIndex"),
    (0, "TPLINK-LLDPMEDCONFIG-MIB", "lldpMedNeighborMediaPolicyIndex"),
)
if mibBuilder.loadTexts:
    lldpMedNeighborMediaPolicyInfoEntry.setStatus("current")


class _LldpMedNeighborPort_Type(OctetString):
    """Custom type lldpMedNeighborPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LldpMedNeighborPort_Type.__name__ = "OctetString"
_LldpMedNeighborPort_Object = MibTableColumn
lldpMedNeighborPort = _LldpMedNeighborPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 1),
    _LldpMedNeighborPort_Type()
)
lldpMedNeighborPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPort.setStatus("current")
_LldpMedNeighborPortIndex_Type = Integer32
_LldpMedNeighborPortIndex_Object = MibTableColumn
lldpMedNeighborPortIndex = _LldpMedNeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 2),
    _LldpMedNeighborPortIndex_Type()
)
lldpMedNeighborPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborPortIndex.setStatus("current")
_LldpMedNeighborMediaPolicyIndex_Type = Integer32
_LldpMedNeighborMediaPolicyIndex_Object = MibTableColumn
lldpMedNeighborMediaPolicyIndex = _LldpMedNeighborMediaPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 3),
    _LldpMedNeighborMediaPolicyIndex_Type()
)
lldpMedNeighborMediaPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborMediaPolicyIndex.setStatus("current")


class _LldpMedNeighborApplicationType_Type(OctetString):
    """Custom type lldpMedNeighborApplicationType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_LldpMedNeighborApplicationType_Type.__name__ = "OctetString"
_LldpMedNeighborApplicationType_Object = MibTableColumn
lldpMedNeighborApplicationType = _LldpMedNeighborApplicationType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 4),
    _LldpMedNeighborApplicationType_Type()
)
lldpMedNeighborApplicationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborApplicationType.setStatus("current")


class _LldpMedNeighborUnknownPolicy_Type(OctetString):
    """Custom type lldpMedNeighborUnknownPolicy based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LldpMedNeighborUnknownPolicy_Type.__name__ = "OctetString"
_LldpMedNeighborUnknownPolicy_Object = MibTableColumn
lldpMedNeighborUnknownPolicy = _LldpMedNeighborUnknownPolicy_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 5),
    _LldpMedNeighborUnknownPolicy_Type()
)
lldpMedNeighborUnknownPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborUnknownPolicy.setStatus("current")


class _LldpMedNeighborAppTagged_Type(OctetString):
    """Custom type lldpMedNeighborAppTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_LldpMedNeighborAppTagged_Type.__name__ = "OctetString"
_LldpMedNeighborAppTagged_Object = MibTableColumn
lldpMedNeighborAppTagged = _LldpMedNeighborAppTagged_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 6),
    _LldpMedNeighborAppTagged_Type()
)
lldpMedNeighborAppTagged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborAppTagged.setStatus("current")
_LldpMedNeighborAppVLANID_Type = Integer32
_LldpMedNeighborAppVLANID_Object = MibTableColumn
lldpMedNeighborAppVLANID = _LldpMedNeighborAppVLANID_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 7),
    _LldpMedNeighborAppVLANID_Type()
)
lldpMedNeighborAppVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborAppVLANID.setStatus("current")
_LldpMedNeighborAppLayer2Priority_Type = Integer32
_LldpMedNeighborAppLayer2Priority_Object = MibTableColumn
lldpMedNeighborAppLayer2Priority = _LldpMedNeighborAppLayer2Priority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 8),
    _LldpMedNeighborAppLayer2Priority_Type()
)
lldpMedNeighborAppLayer2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborAppLayer2Priority.setStatus("current")
_LldpMedNeighborAppDSCP_Type = Integer32
_LldpMedNeighborAppDSCP_Object = MibTableColumn
lldpMedNeighborAppDSCP = _LldpMedNeighborAppDSCP_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 35, 1, 4, 5, 2, 1, 9),
    _LldpMedNeighborAppDSCP_Type()
)
lldpMedNeighborAppDSCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpMedNeighborAppDSCP.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-LLDPMEDCONFIG-MIB",
    **{"lldpMed": lldpMed,
       "lldpMedGlobalConfig": lldpMedGlobalConfig,
       "lldpMedGlobalConfigFastStartRepeatCount": lldpMedGlobalConfigFastStartRepeatCount,
       "lldpMedPortConfigTable": lldpMedPortConfigTable,
       "lldpMedPortConfigEntry": lldpMedPortConfigEntry,
       "lldpMedConfigPortId": lldpMedConfigPortId,
       "lldpMedConfigPortStatus": lldpMedConfigPortStatus,
       "lldpMedConfigPortTlvNetworkPolicy": lldpMedConfigPortTlvNetworkPolicy,
       "lldpMedConfigPortTlvLocationId": lldpMedConfigPortTlvLocationId,
       "lldpMedConfigPortTlvExtendedPower": lldpMedConfigPortTlvExtendedPower,
       "lldpMedConfigPortTlvInventory": lldpMedConfigPortTlvInventory,
       "lldpMedPortConfigTlvLocationTable": lldpMedPortConfigTlvLocationTable,
       "lldpMedPortConfigTlvLocationEntry": lldpMedPortConfigTlvLocationEntry,
       "lldpMedConfigLocationPortId": lldpMedConfigLocationPortId,
       "lldpMedConfigPortLocationEmergencyNumber": lldpMedConfigPortLocationEmergencyNumber,
       "lldpMedConfigPortLocationCivicAddressWhat": lldpMedConfigPortLocationCivicAddressWhat,
       "lldpMedConfigPortLocationCivicAddressCountryCode": lldpMedConfigPortLocationCivicAddressCountryCode,
       "lldpMedConfigPortLocationCivicAddressLanguage": lldpMedConfigPortLocationCivicAddressLanguage,
       "lldpMedConfigPortLocationCivicAddressProvince": lldpMedConfigPortLocationCivicAddressProvince,
       "lldpMedConfigPortLocationCivicAddressCounty": lldpMedConfigPortLocationCivicAddressCounty,
       "lldpMedConfigPortLocationCivicAddressCity": lldpMedConfigPortLocationCivicAddressCity,
       "lldpMedConfigPortLocationCivicAddressStreet": lldpMedConfigPortLocationCivicAddressStreet,
       "lldpMedConfigPortLocationCivicAddressHouseNumber": lldpMedConfigPortLocationCivicAddressHouseNumber,
       "lldpMedConfigPortLocationCivicAddressName": lldpMedConfigPortLocationCivicAddressName,
       "lldpMedConfigPortLocationCivicAddressPostalZipCode": lldpMedConfigPortLocationCivicAddressPostalZipCode,
       "lldpMedConfigPortLocationCivicAddressRoomNumber": lldpMedConfigPortLocationCivicAddressRoomNumber,
       "lldpMedConfigPortLocationCivicAddressPostOfficeBox": lldpMedConfigPortLocationCivicAddressPostOfficeBox,
       "lldpMedConfigPortLocationCivicAddressAdditional": lldpMedConfigPortLocationCivicAddressAdditional,
       "lldpMedLocalInfoTable": lldpMedLocalInfoTable,
       "lldpMedLocalInfoEntry": lldpMedLocalInfoEntry,
       "lldpMedLocalPortId": lldpMedLocalPortId,
       "lldpMEDLocalCapabilities": lldpMEDLocalCapabilities,
       "lldpMedLocalDeviceType": lldpMedLocalDeviceType,
       "lldpMedLocalApplicationType": lldpMedLocalApplicationType,
       "lldpMedLocalUnknownPolicy": lldpMedLocalUnknownPolicy,
       "lldpMedLocalAppTagged": lldpMedLocalAppTagged,
       "lldpMedLocalAppVLANID": lldpMedLocalAppVLANID,
       "lldpMedLocalAppLayer2Priority": lldpMedLocalAppLayer2Priority,
       "lldpMedLocalAppDSCP": lldpMedLocalAppDSCP,
       "lldpMedLocalLocationDataFormat": lldpMedLocalLocationDataFormat,
       "lldpMedLocalLocationID": lldpMedLocalLocationID,
       "lldpMedLocalPowerType": lldpMedLocalPowerType,
       "lldpMedLocalPowerSource": lldpMedLocalPowerSource,
       "lldpMedLocalPowerPriority": lldpMedLocalPowerPriority,
       "lldpMedLocalPowerValue": lldpMedLocalPowerValue,
       "lldpMedLocalInventoryHardwareRevision": lldpMedLocalInventoryHardwareRevision,
       "lldpMedLocalInventoryFirmwareRevision": lldpMedLocalInventoryFirmwareRevision,
       "lldpMedLocalInventorySoftwareRevision": lldpMedLocalInventorySoftwareRevision,
       "lldpMedLocalInventorySerialNumber": lldpMedLocalInventorySerialNumber,
       "lldpMedLocalInventoryManufacturerName": lldpMedLocalInventoryManufacturerName,
       "lldpMedLocalInventoryModelName": lldpMedLocalInventoryModelName,
       "lldpMedLocalInventoryAssetID": lldpMedLocalInventoryAssetID,
       "lldpMedNeighborInfo": lldpMedNeighborInfo,
       "lldpMedNeighborInfoTable": lldpMedNeighborInfoTable,
       "lldpMedNeighborInfoEntry": lldpMedNeighborInfoEntry,
       "lldpMedNeighborPortId": lldpMedNeighborPortId,
       "lldpMedNeighborPortIndexId": lldpMedNeighborPortIndexId,
       "lldpMEDNeighborCapabilities": lldpMEDNeighborCapabilities,
       "lldpMedNeighborDeviceType": lldpMedNeighborDeviceType,
       "lldpMedNeighborLocationDataFormat": lldpMedNeighborLocationDataFormat,
       "lldpMedNeighborLocationID": lldpMedNeighborLocationID,
       "lldpMedNeighborPowerType": lldpMedNeighborPowerType,
       "lldpMedNeighborPowerSource": lldpMedNeighborPowerSource,
       "lldpMedNeighborPowerPriority": lldpMedNeighborPowerPriority,
       "lldpMedNeighborPowerValue": lldpMedNeighborPowerValue,
       "lldpMedNeighborInventoryHardwareRevision": lldpMedNeighborInventoryHardwareRevision,
       "lldpMedNeighborInventoryFirmwareRevision": lldpMedNeighborInventoryFirmwareRevision,
       "lldpMedNeighborInventorySoftwareRevision": lldpMedNeighborInventorySoftwareRevision,
       "lldpMedNeighborInventorySerialNumber": lldpMedNeighborInventorySerialNumber,
       "lldpMedNeighborInventoryManufacturerName": lldpMedNeighborInventoryManufacturerName,
       "lldpMedNeighborInventoryModelName": lldpMedNeighborInventoryModelName,
       "lldpMedNeighborInventoryAssetID": lldpMedNeighborInventoryAssetID,
       "lldpMedNeighborMediaPolicyInfoTable": lldpMedNeighborMediaPolicyInfoTable,
       "lldpMedNeighborMediaPolicyInfoEntry": lldpMedNeighborMediaPolicyInfoEntry,
       "lldpMedNeighborPort": lldpMedNeighborPort,
       "lldpMedNeighborPortIndex": lldpMedNeighborPortIndex,
       "lldpMedNeighborMediaPolicyIndex": lldpMedNeighborMediaPolicyIndex,
       "lldpMedNeighborApplicationType": lldpMedNeighborApplicationType,
       "lldpMedNeighborUnknownPolicy": lldpMedNeighborUnknownPolicy,
       "lldpMedNeighborAppTagged": lldpMedNeighborAppTagged,
       "lldpMedNeighborAppVLANID": lldpMedNeighborAppVLANID,
       "lldpMedNeighborAppLayer2Priority": lldpMedNeighborAppLayer2Priority,
       "lldpMedNeighborAppDSCP": lldpMedNeighborAppDSCP}
)
