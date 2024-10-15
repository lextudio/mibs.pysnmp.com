# SNMP MIB module (ARTEM-COMPOINT-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARTEM-COMPOINT-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:44 2024
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
 enterprises,
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
    "enterprises",
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

artem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4280)
)
artem.setRevisions(
        ("2005-05-12 10:05",
         "2005-04-21 14:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ArtemRSSI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-110, 0),
    )



# MIB Managed Objects in the order of their OIDs

_ArtemWLAN_ObjectIdentity = ObjectIdentity
artemWLAN = _ArtemWLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5)
)
if mibBuilder.loadTexts:
    artemWLAN.setStatus("current")
_ArtemBridge_ObjectIdentity = ObjectIdentity
artemBridge = _ArtemBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1)
)


class _ArtemBridgeConfigScanTimeout_Type(Integer32):
    """Custom type artemBridgeConfigScanTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ArtemBridgeConfigScanTimeout_Type.__name__ = "Integer32"
_ArtemBridgeConfigScanTimeout_Object = MibScalar
artemBridgeConfigScanTimeout = _ArtemBridgeConfigScanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 1),
    _ArtemBridgeConfigScanTimeout_Type()
)
artemBridgeConfigScanTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgeConfigScanTimeout.setStatus("current")
if mibBuilder.loadTexts:
    artemBridgeConfigScanTimeout.setUnits("seconds")


class _ArtemBridgeConfigSetupTimeout_Type(Integer32):
    """Custom type artemBridgeConfigSetupTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ArtemBridgeConfigSetupTimeout_Type.__name__ = "Integer32"
_ArtemBridgeConfigSetupTimeout_Object = MibScalar
artemBridgeConfigSetupTimeout = _ArtemBridgeConfigSetupTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 2),
    _ArtemBridgeConfigSetupTimeout_Type()
)
artemBridgeConfigSetupTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgeConfigSetupTimeout.setStatus("current")
if mibBuilder.loadTexts:
    artemBridgeConfigSetupTimeout.setUnits("seconds")
_ArtemBridgeLinksTable_Object = MibTable
artemBridgeLinksTable = _ArtemBridgeLinksTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3)
)
if mibBuilder.loadTexts:
    artemBridgeLinksTable.setStatus("current")
_ArtemBridgeLinksEntry_Object = MibTableRow
artemBridgeLinksEntry = _ArtemBridgeLinksEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1)
)
artemBridgeLinksEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemRadioIndex"),
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkIndex"),
)
if mibBuilder.loadTexts:
    artemBridgeLinksEntry.setStatus("current")


class _ArtemBridgeLinkIndex_Type(Integer32):
    """Custom type artemBridgeLinkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemBridgeLinkIndex_Type.__name__ = "Integer32"
_ArtemBridgeLinkIndex_Object = MibTableColumn
artemBridgeLinkIndex = _ArtemBridgeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 1),
    _ArtemBridgeLinkIndex_Type()
)
artemBridgeLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemBridgeLinkIndex.setStatus("current")
_ArtemBridgeLinkRowStatus_Type = RowStatus
_ArtemBridgeLinkRowStatus_Object = MibTableColumn
artemBridgeLinkRowStatus = _ArtemBridgeLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 2),
    _ArtemBridgeLinkRowStatus_Type()
)
artemBridgeLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemBridgeLinkRowStatus.setStatus("current")


class _ArtemBridgeLinkIfIndex_Type(Integer32):
    """Custom type artemBridgeLinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemBridgeLinkIfIndex_Type.__name__ = "Integer32"
_ArtemBridgeLinkIfIndex_Object = MibTableColumn
artemBridgeLinkIfIndex = _ArtemBridgeLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 3),
    _ArtemBridgeLinkIfIndex_Type()
)
artemBridgeLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgeLinkIfIndex.setStatus("current")


class _ArtemBridgeLinkAdminStatus_Type(TruthValue):
    """Custom type artemBridgeLinkAdminStatus based on TruthValue"""


_ArtemBridgeLinkAdminStatus_Object = MibTableColumn
artemBridgeLinkAdminStatus = _ArtemBridgeLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 4),
    _ArtemBridgeLinkAdminStatus_Type()
)
artemBridgeLinkAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemBridgeLinkAdminStatus.setStatus("current")


class _ArtemBridgeLinkAliasName_Type(OctetString):
    """Custom type artemBridgeLinkAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ArtemBridgeLinkAliasName_Type.__name__ = "OctetString"
_ArtemBridgeLinkAliasName_Object = MibTableColumn
artemBridgeLinkAliasName = _ArtemBridgeLinkAliasName_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 5),
    _ArtemBridgeLinkAliasName_Type()
)
artemBridgeLinkAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemBridgeLinkAliasName.setStatus("current")


class _ArtemBridgeLinkCurrentSpeed_Type(Integer32):
    """Custom type artemBridgeLinkCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 54),
    )


_ArtemBridgeLinkCurrentSpeed_Type.__name__ = "Integer32"
_ArtemBridgeLinkCurrentSpeed_Object = MibTableColumn
artemBridgeLinkCurrentSpeed = _ArtemBridgeLinkCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 6),
    _ArtemBridgeLinkCurrentSpeed_Type()
)
artemBridgeLinkCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgeLinkCurrentSpeed.setStatus("current")
_ArtemBridgeLinkPartnerRadioMacAddress_Type = MacAddress
_ArtemBridgeLinkPartnerRadioMacAddress_Object = MibTableColumn
artemBridgeLinkPartnerRadioMacAddress = _ArtemBridgeLinkPartnerRadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 7),
    _ArtemBridgeLinkPartnerRadioMacAddress_Type()
)
artemBridgeLinkPartnerRadioMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemBridgeLinkPartnerRadioMacAddress.setStatus("current")
_ArtemBridgeLinkOperStatus_Type = TruthValue
_ArtemBridgeLinkOperStatus_Object = MibTableColumn
artemBridgeLinkOperStatus = _ArtemBridgeLinkOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 3, 1, 8),
    _ArtemBridgeLinkOperStatus_Type()
)
artemBridgeLinkOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgeLinkOperStatus.setStatus("current")
_ArtemBridgePrivacyTable_Object = MibTable
artemBridgePrivacyTable = _ArtemBridgePrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 4)
)
if mibBuilder.loadTexts:
    artemBridgePrivacyTable.setStatus("current")
_ArtemBridgePrivacyEntry_Object = MibTableRow
artemBridgePrivacyEntry = _ArtemBridgePrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 4, 1)
)
artemBridgePrivacyEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemRadioIndex"),
)
if mibBuilder.loadTexts:
    artemBridgePrivacyEntry.setStatus("current")


class _ArtemBridgePrivacyMode_Type(Integer32):
    """Custom type artemBridgePrivacyMode based on Integer32"""
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
        *(("aes", 3),
          ("none", 0),
          ("tkip", 2),
          ("wep", 1))
    )


_ArtemBridgePrivacyMode_Type.__name__ = "Integer32"
_ArtemBridgePrivacyMode_Object = MibTableColumn
artemBridgePrivacyMode = _ArtemBridgePrivacyMode_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 4, 1, 1),
    _ArtemBridgePrivacyMode_Type()
)
artemBridgePrivacyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgePrivacyMode.setStatus("current")


class _ArtemBridgePrivacyAutoKey_Type(Integer32):
    """Custom type artemBridgePrivacyAutoKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ArtemBridgePrivacyAutoKey_Type.__name__ = "Integer32"
_ArtemBridgePrivacyAutoKey_Object = MibTableColumn
artemBridgePrivacyAutoKey = _ArtemBridgePrivacyAutoKey_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 4, 1, 2),
    _ArtemBridgePrivacyAutoKey_Type()
)
artemBridgePrivacyAutoKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgePrivacyAutoKey.setStatus("current")
_ArtemBridgeAutoConfigTable_Object = MibTable
artemBridgeAutoConfigTable = _ArtemBridgeAutoConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 5)
)
if mibBuilder.loadTexts:
    artemBridgeAutoConfigTable.setStatus("current")
_ArtemBridgeAutoConfigEntry_Object = MibTableRow
artemBridgeAutoConfigEntry = _ArtemBridgeAutoConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 5, 1)
)
artemBridgeAutoConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    artemBridgeAutoConfigEntry.setStatus("current")


class _ArtemBridgeLinkLockState_Type(TruthValue):
    """Custom type artemBridgeLinkLockState based on TruthValue"""


_ArtemBridgeLinkLockState_Object = MibTableColumn
artemBridgeLinkLockState = _ArtemBridgeLinkLockState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 5, 1, 1),
    _ArtemBridgeLinkLockState_Type()
)
artemBridgeLinkLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgeLinkLockState.setStatus("current")


class _ArtemBridgeLinkConfigScanState_Type(Integer32):
    """Custom type artemBridgeLinkConfigScanState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 0),
          ("scanning", 1))
    )


_ArtemBridgeLinkConfigScanState_Type.__name__ = "Integer32"
_ArtemBridgeLinkConfigScanState_Object = MibTableColumn
artemBridgeLinkConfigScanState = _ArtemBridgeLinkConfigScanState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 5, 1, 2),
    _ArtemBridgeLinkConfigScanState_Type()
)
artemBridgeLinkConfigScanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgeLinkConfigScanState.setStatus("current")
_ArtemBridgePeersTable_Object = MibTable
artemBridgePeersTable = _ArtemBridgePeersTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6)
)
if mibBuilder.loadTexts:
    artemBridgePeersTable.setStatus("current")
_ArtemBridgePeersEntry_Object = MibTableRow
artemBridgePeersEntry = _ArtemBridgePeersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1)
)
artemBridgePeersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerIndex"),
)
if mibBuilder.loadTexts:
    artemBridgePeersEntry.setStatus("current")


class _ArtemBridgePeerIndex_Type(Integer32):
    """Custom type artemBridgePeerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemBridgePeerIndex_Type.__name__ = "Integer32"
_ArtemBridgePeerIndex_Object = MibTableColumn
artemBridgePeerIndex = _ArtemBridgePeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 1),
    _ArtemBridgePeerIndex_Type()
)
artemBridgePeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemBridgePeerIndex.setStatus("current")


class _ArtemBridgePeerLinkAliasName_Type(OctetString):
    """Custom type artemBridgePeerLinkAliasName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ArtemBridgePeerLinkAliasName_Type.__name__ = "OctetString"
_ArtemBridgePeerLinkAliasName_Object = MibTableColumn
artemBridgePeerLinkAliasName = _ArtemBridgePeerLinkAliasName_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 2),
    _ArtemBridgePeerLinkAliasName_Type()
)
artemBridgePeerLinkAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerLinkAliasName.setStatus("current")


class _ArtemBridgePeerCompointName_Type(OctetString):
    """Custom type artemBridgePeerCompointName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ArtemBridgePeerCompointName_Type.__name__ = "OctetString"
_ArtemBridgePeerCompointName_Object = MibTableColumn
artemBridgePeerCompointName = _ArtemBridgePeerCompointName_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 3),
    _ArtemBridgePeerCompointName_Type()
)
artemBridgePeerCompointName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerCompointName.setStatus("current")
_ArtemBridgePeerRSSI_Type = ArtemRSSI
_ArtemBridgePeerRSSI_Object = MibTableColumn
artemBridgePeerRSSI = _ArtemBridgePeerRSSI_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 4),
    _ArtemBridgePeerRSSI_Type()
)
artemBridgePeerRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerRSSI.setStatus("current")
if mibBuilder.loadTexts:
    artemBridgePeerRSSI.setUnits("dBm")
_ArtemBridgePeerLinkAdminStatus_Type = TruthValue
_ArtemBridgePeerLinkAdminStatus_Object = MibTableColumn
artemBridgePeerLinkAdminStatus = _ArtemBridgePeerLinkAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 5),
    _ArtemBridgePeerLinkAdminStatus_Type()
)
artemBridgePeerLinkAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerLinkAdminStatus.setStatus("current")
_ArtemBridgePeerLockState_Type = TruthValue
_ArtemBridgePeerLockState_Object = MibTableColumn
artemBridgePeerLockState = _ArtemBridgePeerLockState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 6),
    _ArtemBridgePeerLockState_Type()
)
artemBridgePeerLockState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerLockState.setStatus("current")
_ArtemBridgePeerCompointMacAddress_Type = MacAddress
_ArtemBridgePeerCompointMacAddress_Object = MibTableColumn
artemBridgePeerCompointMacAddress = _ArtemBridgePeerCompointMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 7),
    _ArtemBridgePeerCompointMacAddress_Type()
)
artemBridgePeerCompointMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerCompointMacAddress.setStatus("current")
_ArtemBridgePeerRadioMacAddress_Type = MacAddress
_ArtemBridgePeerRadioMacAddress_Object = MibTableColumn
artemBridgePeerRadioMacAddress = _ArtemBridgePeerRadioMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 8),
    _ArtemBridgePeerRadioMacAddress_Type()
)
artemBridgePeerRadioMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerRadioMacAddress.setStatus("current")


class _ArtemBridgePeerConfigSetupState_Type(Integer32):
    """Custom type artemBridgePeerConfigSetupState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 0),
          ("setup", 1))
    )


_ArtemBridgePeerConfigSetupState_Type.__name__ = "Integer32"
_ArtemBridgePeerConfigSetupState_Object = MibTableColumn
artemBridgePeerConfigSetupState = _ArtemBridgePeerConfigSetupState_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 9),
    _ArtemBridgePeerConfigSetupState_Type()
)
artemBridgePeerConfigSetupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemBridgePeerConfigSetupState.setStatus("current")


class _ArtemBridgePeerConfigSetupResult_Type(Integer32):
    """Custom type artemBridgePeerConfigSetupResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("deviceError", 4),
          ("internalError", 9),
          ("invalidPortID", 3),
          ("invalidTag", 5),
          ("locked", 2),
          ("noError", 0),
          ("notFound", 8),
          ("outOfBuffers", 7),
          ("receivedNAK", 10),
          ("timeout", 6),
          ("unknownCommand", 1))
    )


_ArtemBridgePeerConfigSetupResult_Type.__name__ = "Integer32"
_ArtemBridgePeerConfigSetupResult_Object = MibTableColumn
artemBridgePeerConfigSetupResult = _ArtemBridgePeerConfigSetupResult_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 6, 1, 10),
    _ArtemBridgePeerConfigSetupResult_Type()
)
artemBridgePeerConfigSetupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemBridgePeerConfigSetupResult.setStatus("current")
_ArtemLinkTestTable_Object = MibTable
artemLinkTestTable = _ArtemLinkTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7)
)
if mibBuilder.loadTexts:
    artemLinkTestTable.setStatus("current")
_ArtemLinkTestEntry_Object = MibTableRow
artemLinkTestEntry = _ArtemLinkTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1)
)
artemLinkTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    artemLinkTestEntry.setStatus("current")
_ArtemLinkTestSignalLocal_Type = ArtemRSSI
_ArtemLinkTestSignalLocal_Object = MibTableColumn
artemLinkTestSignalLocal = _ArtemLinkTestSignalLocal_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 1),
    _ArtemLinkTestSignalLocal_Type()
)
artemLinkTestSignalLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestSignalLocal.setStatus("current")
_ArtemLinkTestSignalRemote_Type = ArtemRSSI
_ArtemLinkTestSignalRemote_Object = MibTableColumn
artemLinkTestSignalRemote = _ArtemLinkTestSignalRemote_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 2),
    _ArtemLinkTestSignalRemote_Type()
)
artemLinkTestSignalRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestSignalRemote.setStatus("current")
_ArtemLinkTestNoiseLocal_Type = ArtemRSSI
_ArtemLinkTestNoiseLocal_Object = MibTableColumn
artemLinkTestNoiseLocal = _ArtemLinkTestNoiseLocal_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 3),
    _ArtemLinkTestNoiseLocal_Type()
)
artemLinkTestNoiseLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestNoiseLocal.setStatus("current")
if mibBuilder.loadTexts:
    artemLinkTestNoiseLocal.setUnits("dBm")
_ArtemLinkTestNoiseRemote_Type = ArtemRSSI
_ArtemLinkTestNoiseRemote_Object = MibTableColumn
artemLinkTestNoiseRemote = _ArtemLinkTestNoiseRemote_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 4),
    _ArtemLinkTestNoiseRemote_Type()
)
artemLinkTestNoiseRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestNoiseRemote.setStatus("current")
if mibBuilder.loadTexts:
    artemLinkTestNoiseRemote.setUnits("dBm")


class _ArtemLinkTestSNRLocal_Type(Integer32):
    """Custom type artemLinkTestSNRLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_ArtemLinkTestSNRLocal_Type.__name__ = "Integer32"
_ArtemLinkTestSNRLocal_Object = MibTableColumn
artemLinkTestSNRLocal = _ArtemLinkTestSNRLocal_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 5),
    _ArtemLinkTestSNRLocal_Type()
)
artemLinkTestSNRLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestSNRLocal.setStatus("current")
if mibBuilder.loadTexts:
    artemLinkTestSNRLocal.setUnits("dB")


class _ArtemLinkTestSNRRemote_Type(Integer32):
    """Custom type artemLinkTestSNRRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_ArtemLinkTestSNRRemote_Type.__name__ = "Integer32"
_ArtemLinkTestSNRRemote_Object = MibTableColumn
artemLinkTestSNRRemote = _ArtemLinkTestSNRRemote_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 6),
    _ArtemLinkTestSNRRemote_Type()
)
artemLinkTestSNRRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestSNRRemote.setStatus("current")
if mibBuilder.loadTexts:
    artemLinkTestSNRRemote.setUnits("dB")
_ArtemLinkTestFramesTransmitted_Type = Counter32
_ArtemLinkTestFramesTransmitted_Object = MibTableColumn
artemLinkTestFramesTransmitted = _ArtemLinkTestFramesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 7),
    _ArtemLinkTestFramesTransmitted_Type()
)
artemLinkTestFramesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestFramesTransmitted.setStatus("current")
_ArtemLinkTestFramesReceived_Type = Counter32
_ArtemLinkTestFramesReceived_Object = MibTableColumn
artemLinkTestFramesReceived = _ArtemLinkTestFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 8),
    _ArtemLinkTestFramesReceived_Type()
)
artemLinkTestFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestFramesReceived.setStatus("current")
_ArtemLinkTestFramesLost_Type = Counter32
_ArtemLinkTestFramesLost_Object = MibTableColumn
artemLinkTestFramesLost = _ArtemLinkTestFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 9),
    _ArtemLinkTestFramesLost_Type()
)
artemLinkTestFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestFramesLost.setStatus("current")
_ArtemLinkTestRxFrames54_Type = Counter32
_ArtemLinkTestRxFrames54_Object = MibTableColumn
artemLinkTestRxFrames54 = _ArtemLinkTestRxFrames54_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 10),
    _ArtemLinkTestRxFrames54_Type()
)
artemLinkTestRxFrames54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames54.setStatus("current")
_ArtemLinkTestRxFrames48_Type = Counter32
_ArtemLinkTestRxFrames48_Object = MibTableColumn
artemLinkTestRxFrames48 = _ArtemLinkTestRxFrames48_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 11),
    _ArtemLinkTestRxFrames48_Type()
)
artemLinkTestRxFrames48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames48.setStatus("current")
_ArtemLinkTestRxFrames36_Type = Counter32
_ArtemLinkTestRxFrames36_Object = MibTableColumn
artemLinkTestRxFrames36 = _ArtemLinkTestRxFrames36_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 12),
    _ArtemLinkTestRxFrames36_Type()
)
artemLinkTestRxFrames36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames36.setStatus("current")
_ArtemLinkTestRxFrames24_Type = Counter32
_ArtemLinkTestRxFrames24_Object = MibTableColumn
artemLinkTestRxFrames24 = _ArtemLinkTestRxFrames24_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 13),
    _ArtemLinkTestRxFrames24_Type()
)
artemLinkTestRxFrames24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames24.setStatus("current")
_ArtemLinkTestRxFrames18_Type = Counter32
_ArtemLinkTestRxFrames18_Object = MibTableColumn
artemLinkTestRxFrames18 = _ArtemLinkTestRxFrames18_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 14),
    _ArtemLinkTestRxFrames18_Type()
)
artemLinkTestRxFrames18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames18.setStatus("current")
_ArtemLinkTestRxFrames12_Type = Counter32
_ArtemLinkTestRxFrames12_Object = MibTableColumn
artemLinkTestRxFrames12 = _ArtemLinkTestRxFrames12_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 15),
    _ArtemLinkTestRxFrames12_Type()
)
artemLinkTestRxFrames12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames12.setStatus("current")
_ArtemLinkTestRxFrames11_Type = Counter32
_ArtemLinkTestRxFrames11_Object = MibTableColumn
artemLinkTestRxFrames11 = _ArtemLinkTestRxFrames11_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 16),
    _ArtemLinkTestRxFrames11_Type()
)
artemLinkTestRxFrames11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames11.setStatus("current")
_ArtemLinkTestRxFrames9_Type = Counter32
_ArtemLinkTestRxFrames9_Object = MibTableColumn
artemLinkTestRxFrames9 = _ArtemLinkTestRxFrames9_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 17),
    _ArtemLinkTestRxFrames9_Type()
)
artemLinkTestRxFrames9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames9.setStatus("current")
_ArtemLinkTestRxFrames6_Type = Counter32
_ArtemLinkTestRxFrames6_Object = MibTableColumn
artemLinkTestRxFrames6 = _ArtemLinkTestRxFrames6_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 18),
    _ArtemLinkTestRxFrames6_Type()
)
artemLinkTestRxFrames6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames6.setStatus("current")
_ArtemLinkTestRxFrames5_Type = Counter32
_ArtemLinkTestRxFrames5_Object = MibTableColumn
artemLinkTestRxFrames5 = _ArtemLinkTestRxFrames5_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 19),
    _ArtemLinkTestRxFrames5_Type()
)
artemLinkTestRxFrames5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames5.setStatus("current")
_ArtemLinkTestRxFrames2_Type = Counter32
_ArtemLinkTestRxFrames2_Object = MibTableColumn
artemLinkTestRxFrames2 = _ArtemLinkTestRxFrames2_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 20),
    _ArtemLinkTestRxFrames2_Type()
)
artemLinkTestRxFrames2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames2.setStatus("current")
_ArtemLinkTestRxFrames1_Type = Counter32
_ArtemLinkTestRxFrames1_Object = MibTableColumn
artemLinkTestRxFrames1 = _ArtemLinkTestRxFrames1_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 7, 1, 21),
    _ArtemLinkTestRxFrames1_Type()
)
artemLinkTestRxFrames1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemLinkTestRxFrames1.setStatus("current")
_ArtemBridgeNotification_ObjectIdentity = ObjectIdentity
artemBridgeNotification = _ArtemBridgeNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 8)
)
_ArtemAP_ObjectIdentity = ObjectIdentity
artemAP = _ArtemAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2)
)
_ArtemAPServiceSetsTable_Object = MibTable
artemAPServiceSetsTable = _ArtemAPServiceSetsTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1)
)
if mibBuilder.loadTexts:
    artemAPServiceSetsTable.setStatus("current")
_ArtemAPServiceSetsEntry_Object = MibTableRow
artemAPServiceSetsEntry = _ArtemAPServiceSetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1, 1)
)
artemAPServiceSetsEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemRadioIndex"),
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemAPServiceSetIndex"),
)
if mibBuilder.loadTexts:
    artemAPServiceSetsEntry.setStatus("current")


class _ArtemAPServiceSetIndex_Type(Integer32):
    """Custom type artemAPServiceSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemAPServiceSetIndex_Type.__name__ = "Integer32"
_ArtemAPServiceSetIndex_Object = MibTableColumn
artemAPServiceSetIndex = _ArtemAPServiceSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1, 1, 1),
    _ArtemAPServiceSetIndex_Type()
)
artemAPServiceSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemAPServiceSetIndex.setStatus("current")
_ArtemAPServiceSetsRowStatus_Type = RowStatus
_ArtemAPServiceSetsRowStatus_Object = MibTableColumn
artemAPServiceSetsRowStatus = _ArtemAPServiceSetsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1, 1, 2),
    _ArtemAPServiceSetsRowStatus_Type()
)
artemAPServiceSetsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemAPServiceSetsRowStatus.setStatus("current")


class _ArtemAPIfIndex_Type(Integer32):
    """Custom type artemAPIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemAPIfIndex_Type.__name__ = "Integer32"
_ArtemAPIfIndex_Object = MibTableColumn
artemAPIfIndex = _ArtemAPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1, 1, 3),
    _ArtemAPIfIndex_Type()
)
artemAPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemAPIfIndex.setStatus("current")


class _ArtemAPServiceSetAdminStatus_Type(TruthValue):
    """Custom type artemAPServiceSetAdminStatus based on TruthValue"""


_ArtemAPServiceSetAdminStatus_Object = MibTableColumn
artemAPServiceSetAdminStatus = _ArtemAPServiceSetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 1, 1, 4),
    _ArtemAPServiceSetAdminStatus_Type()
)
artemAPServiceSetAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    artemAPServiceSetAdminStatus.setStatus("current")
_ArtemAPNotification_ObjectIdentity = ObjectIdentity
artemAPNotification = _ArtemAPNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 9)
)
_ArtemRadioParametersTable_Object = MibTable
artemRadioParametersTable = _ArtemRadioParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3)
)
if mibBuilder.loadTexts:
    artemRadioParametersTable.setStatus("current")
_ArtemRadioParametersEntry_Object = MibTableRow
artemRadioParametersEntry = _ArtemRadioParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1)
)
artemRadioParametersEntry.setIndexNames(
    (0, "ARTEM-COMPOINT-WLAN-MIB", "artemRadioIndex"),
)
if mibBuilder.loadTexts:
    artemRadioParametersEntry.setStatus("current")


class _ArtemRadioIndex_Type(Integer32):
    """Custom type artemRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemRadioIndex_Type.__name__ = "Integer32"
_ArtemRadioIndex_Object = MibTableColumn
artemRadioIndex = _ArtemRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 1),
    _ArtemRadioIndex_Type()
)
artemRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    artemRadioIndex.setStatus("current")


class _ArtemRadioChannel_Type(Integer32):
    """Custom type artemRadioChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_ArtemRadioChannel_Type.__name__ = "Integer32"
_ArtemRadioChannel_Object = MibTableColumn
artemRadioChannel = _ArtemRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 2),
    _ArtemRadioChannel_Type()
)
artemRadioChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioChannel.setStatus("current")


class _ArtemRadioSpeedMode_Type(Integer32):
    """Custom type artemRadioSpeedMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5,
              6,
              9,
              11,
              12,
              18,
              24,
              36,
              48,
              54)
        )
    )
    namedValues = NamedValues(
        *(("autoFallback", 0),
          ("fixed11Mbps", 11),
          ("fixed12Mbps", 12),
          ("fixed18Mbps", 18),
          ("fixed1Mbps", 1),
          ("fixed24Mbps", 24),
          ("fixed2Mpbs", 2),
          ("fixed36Mbps", 36),
          ("fixed48Mbps", 48),
          ("fixed54Mbps", 54),
          ("fixed5Mbps", 5),
          ("fixed6Mbps", 6),
          ("fixed9Mbps", 9))
    )


_ArtemRadioSpeedMode_Type.__name__ = "Integer32"
_ArtemRadioSpeedMode_Object = MibTableColumn
artemRadioSpeedMode = _ArtemRadioSpeedMode_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 3),
    _ArtemRadioSpeedMode_Type()
)
artemRadioSpeedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioSpeedMode.setStatus("current")


class _ArtemRadioTxPower_Type(Integer32):
    """Custom type artemRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ArtemRadioTxPower_Type.__name__ = "Integer32"
_ArtemRadioTxPower_Object = MibTableColumn
artemRadioTxPower = _ArtemRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 4),
    _ArtemRadioTxPower_Type()
)
artemRadioTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioTxPower.setStatus("current")
if mibBuilder.loadTexts:
    artemRadioTxPower.setUnits("dBm")


class _ArtemRadioAntennaDiversity_Type(Integer32):
    """Custom type artemRadioAntennaDiversity based on Integer32"""
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
        *(("both", 3),
          ("none", 0),
          ("receive", 1),
          ("transmit", 2))
    )


_ArtemRadioAntennaDiversity_Type.__name__ = "Integer32"
_ArtemRadioAntennaDiversity_Object = MibTableColumn
artemRadioAntennaDiversity = _ArtemRadioAntennaDiversity_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 5),
    _ArtemRadioAntennaDiversity_Type()
)
artemRadioAntennaDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioAntennaDiversity.setStatus("current")


class _ArtemRadioNitroMode_Type(TruthValue):
    """Custom type artemRadioNitroMode based on TruthValue"""


_ArtemRadioNitroMode_Object = MibTableColumn
artemRadioNitroMode = _ArtemRadioNitroMode_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 6),
    _ArtemRadioNitroMode_Type()
)
artemRadioNitroMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioNitroMode.setStatus("current")


class _ArtemRadioAckWindow_Type(Integer32):
    """Custom type artemRadioAckWindow based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 199),
    )


_ArtemRadioAckWindow_Type.__name__ = "Integer32"
_ArtemRadioAckWindow_Object = MibTableColumn
artemRadioAckWindow = _ArtemRadioAckWindow_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 7),
    _ArtemRadioAckWindow_Type()
)
artemRadioAckWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioAckWindow.setStatus("current")
if mibBuilder.loadTexts:
    artemRadioAckWindow.setUnits("microseconds")


class _ArtemRadioWwrMode_Type(Integer32):
    """Custom type artemRadioWwrMode based on Integer32"""
    defaultValue = 2

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
        *(("none", 0),
          ("wwr11d", 1),
          ("wwr11dhFlexible", 2),
          ("wwr11dhStrict", 3))
    )


_ArtemRadioWwrMode_Type.__name__ = "Integer32"
_ArtemRadioWwrMode_Object = MibTableColumn
artemRadioWwrMode = _ArtemRadioWwrMode_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 8),
    _ArtemRadioWwrMode_Type()
)
artemRadioWwrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioWwrMode.setStatus("current")


class _ArtemRadioOperatingMode_Type(Integer32):
    """Custom type artemRadioOperatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 1),
          ("bridge", 2),
          ("doubleBridge", 3))
    )


_ArtemRadioOperatingMode_Type.__name__ = "Integer32"
_ArtemRadioOperatingMode_Object = MibTableColumn
artemRadioOperatingMode = _ArtemRadioOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 3, 1, 9),
    _ArtemRadioOperatingMode_Type()
)
artemRadioOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    artemRadioOperatingMode.setStatus("current")
_ArtemInterfaceRadioTable_Object = MibTable
artemInterfaceRadioTable = _ArtemInterfaceRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 4)
)
if mibBuilder.loadTexts:
    artemInterfaceRadioTable.setStatus("current")
_ArtemInterfaceRadioEntry_Object = MibTableRow
artemInterfaceRadioEntry = _ArtemInterfaceRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 4, 1)
)
artemInterfaceRadioEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    artemInterfaceRadioEntry.setStatus("current")


class _ArtemWLANRadioIndex_Type(Integer32):
    """Custom type artemWLANRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ArtemWLANRadioIndex_Type.__name__ = "Integer32"
_ArtemWLANRadioIndex_Object = MibTableColumn
artemWLANRadioIndex = _ArtemWLANRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 4280, 5, 4, 1, 1),
    _ArtemWLANRadioIndex_Type()
)
artemWLANRadioIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    artemWLANRadioIndex.setStatus("current")
_ArtemWLANNotification_ObjectIdentity = ObjectIdentity
artemWLANNotification = _ArtemWLANNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4280, 5, 8)
)

# Managed Objects groups

artemBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 9)
)
artemBridgeGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkRowStatus"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkIfIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkAdminStatus"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkAliasName"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkCurrentSpeed"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkPartnerRadioMacAddress"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkOperStatus"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkLockState"))
)
if mibBuilder.loadTexts:
    artemBridgeGroup.setStatus("current")

artemBridgePrivacyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 10)
)
artemBridgePrivacyGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePrivacyMode"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePrivacyAutoKey"))
)
if mibBuilder.loadTexts:
    artemBridgePrivacyGroup.setStatus("current")

artemBridgePeersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 11)
)
artemBridgePeersGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerLinkAliasName"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerCompointName"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerRSSI"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerLinkAdminStatus"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerLockState"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerCompointMacAddress"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerRadioMacAddress"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerConfigSetupState"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerConfigSetupResult"))
)
if mibBuilder.loadTexts:
    artemBridgePeersGroup.setStatus("current")

artemBridgeLinkTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 12)
)
artemBridgeLinkTestGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestSignalLocal"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestSignalRemote"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestNoiseLocal"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestNoiseRemote"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestSNRLocal"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestSNRRemote"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestFramesTransmitted"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestFramesReceived"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestFramesLost"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames54"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames48"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames36"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames24"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames18"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames12"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames11"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames9"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames6"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames5"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames2"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemLinkTestRxFrames1"))
)
if mibBuilder.loadTexts:
    artemBridgeLinkTestGroup.setStatus("current")

artemAPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 2, 10)
)
artemAPGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemAPServiceSetsRowStatus"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemAPIfIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemAPServiceSetAdminStatus"))
)
if mibBuilder.loadTexts:
    artemAPGroup.setStatus("current")

artemWLANGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 9)
)
artemWLANGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemRadioChannel"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioSpeedMode"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioTxPower"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioAntennaDiversity"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioNitroMode"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioAckWindow"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioWwrMode"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemRadioOperatingMode"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemWLANRadioIndex"))
)
if mibBuilder.loadTexts:
    artemWLANGroup.setStatus("current")


# Notification objects

artemBridgeLinkOperState = NotificationType(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 8, 1)
)
artemBridgeLinkOperState.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkOperStatus"))
)
if mibBuilder.loadTexts:
    artemBridgeLinkOperState.setStatus(
        "current"
    )

artemBridgeLinkConfigScan = NotificationType(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 8, 2)
)
artemBridgeLinkConfigScan.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkConfigScanState"))
)
if mibBuilder.loadTexts:
    artemBridgeLinkConfigScan.setStatus(
        "current"
    )

artemBridgePeerConfigSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 8, 3)
)
artemBridgePeerConfigSetup.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerConfigSetupState"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerConfigSetupResult"))
)
if mibBuilder.loadTexts:
    artemBridgePeerConfigSetup.setStatus(
        "current"
    )

artemBridgeLinkLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 8, 4)
)
artemBridgeLinkLock.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkLockState"))
)
if mibBuilder.loadTexts:
    artemBridgeLinkLock.setStatus(
        "current"
    )


# Notifications groups

artemBridgeLinkNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4280, 5, 1, 13)
)
artemBridgeLinkNotificationGroup.setObjects(
      *(("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkOperState"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkConfigScan"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgePeerConfigSetup"),
        ("ARTEM-COMPOINT-WLAN-MIB", "artemBridgeLinkLock"))
)
if mibBuilder.loadTexts:
    artemBridgeLinkNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARTEM-COMPOINT-WLAN-MIB",
    **{"ArtemRSSI": ArtemRSSI,
       "artem": artem,
       "artemWLAN": artemWLAN,
       "artemBridge": artemBridge,
       "artemBridgeConfigScanTimeout": artemBridgeConfigScanTimeout,
       "artemBridgeConfigSetupTimeout": artemBridgeConfigSetupTimeout,
       "artemBridgeLinksTable": artemBridgeLinksTable,
       "artemBridgeLinksEntry": artemBridgeLinksEntry,
       "artemBridgeLinkIndex": artemBridgeLinkIndex,
       "artemBridgeLinkRowStatus": artemBridgeLinkRowStatus,
       "artemBridgeLinkIfIndex": artemBridgeLinkIfIndex,
       "artemBridgeLinkAdminStatus": artemBridgeLinkAdminStatus,
       "artemBridgeLinkAliasName": artemBridgeLinkAliasName,
       "artemBridgeLinkCurrentSpeed": artemBridgeLinkCurrentSpeed,
       "artemBridgeLinkPartnerRadioMacAddress": artemBridgeLinkPartnerRadioMacAddress,
       "artemBridgeLinkOperStatus": artemBridgeLinkOperStatus,
       "artemBridgePrivacyTable": artemBridgePrivacyTable,
       "artemBridgePrivacyEntry": artemBridgePrivacyEntry,
       "artemBridgePrivacyMode": artemBridgePrivacyMode,
       "artemBridgePrivacyAutoKey": artemBridgePrivacyAutoKey,
       "artemBridgeAutoConfigTable": artemBridgeAutoConfigTable,
       "artemBridgeAutoConfigEntry": artemBridgeAutoConfigEntry,
       "artemBridgeLinkLockState": artemBridgeLinkLockState,
       "artemBridgeLinkConfigScanState": artemBridgeLinkConfigScanState,
       "artemBridgePeersTable": artemBridgePeersTable,
       "artemBridgePeersEntry": artemBridgePeersEntry,
       "artemBridgePeerIndex": artemBridgePeerIndex,
       "artemBridgePeerLinkAliasName": artemBridgePeerLinkAliasName,
       "artemBridgePeerCompointName": artemBridgePeerCompointName,
       "artemBridgePeerRSSI": artemBridgePeerRSSI,
       "artemBridgePeerLinkAdminStatus": artemBridgePeerLinkAdminStatus,
       "artemBridgePeerLockState": artemBridgePeerLockState,
       "artemBridgePeerCompointMacAddress": artemBridgePeerCompointMacAddress,
       "artemBridgePeerRadioMacAddress": artemBridgePeerRadioMacAddress,
       "artemBridgePeerConfigSetupState": artemBridgePeerConfigSetupState,
       "artemBridgePeerConfigSetupResult": artemBridgePeerConfigSetupResult,
       "artemLinkTestTable": artemLinkTestTable,
       "artemLinkTestEntry": artemLinkTestEntry,
       "artemLinkTestSignalLocal": artemLinkTestSignalLocal,
       "artemLinkTestSignalRemote": artemLinkTestSignalRemote,
       "artemLinkTestNoiseLocal": artemLinkTestNoiseLocal,
       "artemLinkTestNoiseRemote": artemLinkTestNoiseRemote,
       "artemLinkTestSNRLocal": artemLinkTestSNRLocal,
       "artemLinkTestSNRRemote": artemLinkTestSNRRemote,
       "artemLinkTestFramesTransmitted": artemLinkTestFramesTransmitted,
       "artemLinkTestFramesReceived": artemLinkTestFramesReceived,
       "artemLinkTestFramesLost": artemLinkTestFramesLost,
       "artemLinkTestRxFrames54": artemLinkTestRxFrames54,
       "artemLinkTestRxFrames48": artemLinkTestRxFrames48,
       "artemLinkTestRxFrames36": artemLinkTestRxFrames36,
       "artemLinkTestRxFrames24": artemLinkTestRxFrames24,
       "artemLinkTestRxFrames18": artemLinkTestRxFrames18,
       "artemLinkTestRxFrames12": artemLinkTestRxFrames12,
       "artemLinkTestRxFrames11": artemLinkTestRxFrames11,
       "artemLinkTestRxFrames9": artemLinkTestRxFrames9,
       "artemLinkTestRxFrames6": artemLinkTestRxFrames6,
       "artemLinkTestRxFrames5": artemLinkTestRxFrames5,
       "artemLinkTestRxFrames2": artemLinkTestRxFrames2,
       "artemLinkTestRxFrames1": artemLinkTestRxFrames1,
       "artemBridgeNotification": artemBridgeNotification,
       "artemBridgeLinkOperState": artemBridgeLinkOperState,
       "artemBridgeLinkConfigScan": artemBridgeLinkConfigScan,
       "artemBridgePeerConfigSetup": artemBridgePeerConfigSetup,
       "artemBridgeLinkLock": artemBridgeLinkLock,
       "artemBridgeGroup": artemBridgeGroup,
       "artemBridgePrivacyGroup": artemBridgePrivacyGroup,
       "artemBridgePeersGroup": artemBridgePeersGroup,
       "artemBridgeLinkTestGroup": artemBridgeLinkTestGroup,
       "artemBridgeLinkNotificationGroup": artemBridgeLinkNotificationGroup,
       "artemAP": artemAP,
       "artemAPServiceSetsTable": artemAPServiceSetsTable,
       "artemAPServiceSetsEntry": artemAPServiceSetsEntry,
       "artemAPServiceSetIndex": artemAPServiceSetIndex,
       "artemAPServiceSetsRowStatus": artemAPServiceSetsRowStatus,
       "artemAPIfIndex": artemAPIfIndex,
       "artemAPServiceSetAdminStatus": artemAPServiceSetAdminStatus,
       "artemAPNotification": artemAPNotification,
       "artemAPGroup": artemAPGroup,
       "artemRadioParametersTable": artemRadioParametersTable,
       "artemRadioParametersEntry": artemRadioParametersEntry,
       "artemRadioIndex": artemRadioIndex,
       "artemRadioChannel": artemRadioChannel,
       "artemRadioSpeedMode": artemRadioSpeedMode,
       "artemRadioTxPower": artemRadioTxPower,
       "artemRadioAntennaDiversity": artemRadioAntennaDiversity,
       "artemRadioNitroMode": artemRadioNitroMode,
       "artemRadioAckWindow": artemRadioAckWindow,
       "artemRadioWwrMode": artemRadioWwrMode,
       "artemRadioOperatingMode": artemRadioOperatingMode,
       "artemInterfaceRadioTable": artemInterfaceRadioTable,
       "artemInterfaceRadioEntry": artemInterfaceRadioEntry,
       "artemWLANRadioIndex": artemWLANRadioIndex,
       "artemWLANNotification": artemWLANNotification,
       "artemWLANGroup": artemWLANGroup}
)
