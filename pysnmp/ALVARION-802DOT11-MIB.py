# SNMP MIB module (ALVARION-802DOT11-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALVARION-802DOT11-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:38:28 2024
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

(alvarionMgmtV2,) = mibBuilder.importSymbols(
    "ALVARION-SMI",
    "alvarionMgmtV2")

(AlvarionDataRate,
 AlvarionNotificationEnable,
 AlvarionRadioType,
 AlvarionSSIDOrNone) = mibBuilder.importSymbols(
    "ALVARION-TC",
    "AlvarionDataRate",
    "AlvarionNotificationEnable",
    "AlvarionRadioType",
    "AlvarionSSIDOrNone")

(coVirtualAccessPointConfigEntry,
 coVirtualApSSID) = mibBuilder.importSymbols(
    "ALVARION-VIRTUAL-AP-MIB",
    "coVirtualAccessPointConfigEntry",
    "coVirtualApSSID")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifDescr",
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

alvarion802dot11 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class WEPKeytype(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
        ValueSizeConstraint(13, 13),
    )



# MIB Managed Objects in the order of their OIDs

_CoDot11ap_ObjectIdentity = ObjectIdentity
coDot11ap = _CoDot11ap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1)
)
_CoDot11AccessPointConfigTable_Object = MibTable
coDot11AccessPointConfigTable = _CoDot11AccessPointConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1)
)
if mibBuilder.loadTexts:
    coDot11AccessPointConfigTable.setStatus("current")
_CoDot11AccessPointConfigEntry_Object = MibTableRow
coDot11AccessPointConfigEntry = _CoDot11AccessPointConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    coDot11AccessPointConfigEntry.setStatus("current")
_CoDot11RelayBetweenStation_Type = TruthValue
_CoDot11RelayBetweenStation_Object = MibTableColumn
coDot11RelayBetweenStation = _CoDot11RelayBetweenStation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 1),
    _CoDot11RelayBetweenStation_Type()
)
coDot11RelayBetweenStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11RelayBetweenStation.setStatus("current")


class _CoDot11BeaconPeriod_Type(Integer32):
    """Custom type coDot11BeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CoDot11BeaconPeriod_Type.__name__ = "Integer32"
_CoDot11BeaconPeriod_Object = MibTableColumn
coDot11BeaconPeriod = _CoDot11BeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 2),
    _CoDot11BeaconPeriod_Type()
)
coDot11BeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11BeaconPeriod.setStatus("current")


class _CoDot11DTIMPeriod_Type(Integer32):
    """Custom type coDot11DTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11DTIMPeriod_Type.__name__ = "Integer32"
_CoDot11DTIMPeriod_Object = MibTableColumn
coDot11DTIMPeriod = _CoDot11DTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 3),
    _CoDot11DTIMPeriod_Type()
)
coDot11DTIMPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11DTIMPeriod.setStatus("current")
_CoDot11PrivacyOptionImplemented_Type = TruthValue
_CoDot11PrivacyOptionImplemented_Object = MibTableColumn
coDot11PrivacyOptionImplemented = _CoDot11PrivacyOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 4),
    _CoDot11PrivacyOptionImplemented_Type()
)
coDot11PrivacyOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PrivacyOptionImplemented.setStatus("current")
_CoDot11RSNAOptionImplemented_Type = TruthValue
_CoDot11RSNAOptionImplemented_Object = MibTableColumn
coDot11RSNAOptionImplemented = _CoDot11RSNAOptionImplemented_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 5),
    _CoDot11RSNAOptionImplemented_Type()
)
coDot11RSNAOptionImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAOptionImplemented.setStatus("current")
_CoDot11NumberOfUsers_Type = Unsigned32
_CoDot11NumberOfUsers_Object = MibTableColumn
coDot11NumberOfUsers = _CoDot11NumberOfUsers_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 6),
    _CoDot11NumberOfUsers_Type()
)
coDot11NumberOfUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11NumberOfUsers.setStatus("current")
_CoDot11AddToAssociationNotification_Type = TruthValue
_CoDot11AddToAssociationNotification_Object = MibTableColumn
coDot11AddToAssociationNotification = _CoDot11AddToAssociationNotification_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 7),
    _CoDot11AddToAssociationNotification_Type()
)
coDot11AddToAssociationNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AddToAssociationNotification.setStatus("current")


class _CoDot11PhyTxPowerAdminLevel_Type(Integer32):
    """Custom type coDot11PhyTxPowerAdminLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CoDot11PhyTxPowerAdminLevel_Type.__name__ = "Integer32"
_CoDot11PhyTxPowerAdminLevel_Object = MibTableColumn
coDot11PhyTxPowerAdminLevel = _CoDot11PhyTxPowerAdminLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 8),
    _CoDot11PhyTxPowerAdminLevel_Type()
)
coDot11PhyTxPowerAdminLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11PhyTxPowerAdminLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11PhyTxPowerAdminLevel.setUnits("dBm")


class _CoDot11PhyTxPowerOperLevel_Type(Integer32):
    """Custom type coDot11PhyTxPowerOperLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_CoDot11PhyTxPowerOperLevel_Type.__name__ = "Integer32"
_CoDot11PhyTxPowerOperLevel_Object = MibTableColumn
coDot11PhyTxPowerOperLevel = _CoDot11PhyTxPowerOperLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 9),
    _CoDot11PhyTxPowerOperLevel_Type()
)
coDot11PhyTxPowerOperLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PhyTxPowerOperLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11PhyTxPowerOperLevel.setUnits("dBm")


class _CoDot11CurrentSNRLevel_Type(Integer32):
    """Custom type coDot11CurrentSNRLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDot11CurrentSNRLevel_Type.__name__ = "Integer32"
_CoDot11CurrentSNRLevel_Object = MibTableColumn
coDot11CurrentSNRLevel = _CoDot11CurrentSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 10),
    _CoDot11CurrentSNRLevel_Type()
)
coDot11CurrentSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentSNRLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11CurrentSNRLevel.setUnits("dBm")
_CoDot11BSSID_Type = MacAddress
_CoDot11BSSID_Object = MibTableColumn
coDot11BSSID = _CoDot11BSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 11),
    _CoDot11BSSID_Type()
)
coDot11BSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11BSSID.setStatus("current")
_CoDot11AdminMinimumDataRate_Type = AlvarionDataRate
_CoDot11AdminMinimumDataRate_Object = MibTableColumn
coDot11AdminMinimumDataRate = _CoDot11AdminMinimumDataRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 12),
    _CoDot11AdminMinimumDataRate_Type()
)
coDot11AdminMinimumDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AdminMinimumDataRate.setStatus("current")
_CoDot11AdminMaximumDataRate_Type = AlvarionDataRate
_CoDot11AdminMaximumDataRate_Object = MibTableColumn
coDot11AdminMaximumDataRate = _CoDot11AdminMaximumDataRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 1, 1, 13),
    _CoDot11AdminMaximumDataRate_Type()
)
coDot11AdminMaximumDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AdminMaximumDataRate.setStatus("current")
_CoDot11AuthenticationAlgorithmsTable_Object = MibTable
coDot11AuthenticationAlgorithmsTable = _CoDot11AuthenticationAlgorithmsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 2)
)
if mibBuilder.loadTexts:
    coDot11AuthenticationAlgorithmsTable.setStatus("current")
_CoDot11AuthenticationAlgorithmsEntry_Object = MibTableRow
coDot11AuthenticationAlgorithmsEntry = _CoDot11AuthenticationAlgorithmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 2, 1)
)
coDot11AuthenticationAlgorithmsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11AuthenticationAlgorithmsIndex"),
)
if mibBuilder.loadTexts:
    coDot11AuthenticationAlgorithmsEntry.setStatus("current")


class _CoDot11AuthenticationAlgorithmsIndex_Type(Integer32):
    """Custom type coDot11AuthenticationAlgorithmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDot11AuthenticationAlgorithmsIndex_Type.__name__ = "Integer32"
_CoDot11AuthenticationAlgorithmsIndex_Object = MibTableColumn
coDot11AuthenticationAlgorithmsIndex = _CoDot11AuthenticationAlgorithmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 2, 1, 1),
    _CoDot11AuthenticationAlgorithmsIndex_Type()
)
coDot11AuthenticationAlgorithmsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11AuthenticationAlgorithmsIndex.setStatus("current")


class _CoDot11AuthenticationAlgorithm_Type(Integer32):
    """Custom type coDot11AuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("openSystem", 1),
          ("sharedKey", 2))
    )


_CoDot11AuthenticationAlgorithm_Type.__name__ = "Integer32"
_CoDot11AuthenticationAlgorithm_Object = MibTableColumn
coDot11AuthenticationAlgorithm = _CoDot11AuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 2, 1, 2),
    _CoDot11AuthenticationAlgorithm_Type()
)
coDot11AuthenticationAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11AuthenticationAlgorithm.setStatus("current")
_CoDot11AuthenticationAlgorithmsEnable_Type = TruthValue
_CoDot11AuthenticationAlgorithmsEnable_Object = MibTableColumn
coDot11AuthenticationAlgorithmsEnable = _CoDot11AuthenticationAlgorithmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 2, 1, 3),
    _CoDot11AuthenticationAlgorithmsEnable_Type()
)
coDot11AuthenticationAlgorithmsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11AuthenticationAlgorithmsEnable.setStatus("current")
_CoDot11WEPDefaultKeysTable_Object = MibTable
coDot11WEPDefaultKeysTable = _CoDot11WEPDefaultKeysTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3)
)
if mibBuilder.loadTexts:
    coDot11WEPDefaultKeysTable.setStatus("current")
_CoDot11WEPDefaultKeysEntry_Object = MibTableRow
coDot11WEPDefaultKeysEntry = _CoDot11WEPDefaultKeysEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    coDot11WEPDefaultKeysEntry.setStatus("current")
_CoDot11WEPDefaultKey1Value_Type = WEPKeytype
_CoDot11WEPDefaultKey1Value_Object = MibTableColumn
coDot11WEPDefaultKey1Value = _CoDot11WEPDefaultKey1Value_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3, 1, 1),
    _CoDot11WEPDefaultKey1Value_Type()
)
coDot11WEPDefaultKey1Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WEPDefaultKey1Value.setStatus("current")
_CoDot11WEPDefaultKey2Value_Type = WEPKeytype
_CoDot11WEPDefaultKey2Value_Object = MibTableColumn
coDot11WEPDefaultKey2Value = _CoDot11WEPDefaultKey2Value_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3, 1, 2),
    _CoDot11WEPDefaultKey2Value_Type()
)
coDot11WEPDefaultKey2Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WEPDefaultKey2Value.setStatus("current")
_CoDot11WEPDefaultKey3Value_Type = WEPKeytype
_CoDot11WEPDefaultKey3Value_Object = MibTableColumn
coDot11WEPDefaultKey3Value = _CoDot11WEPDefaultKey3Value_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3, 1, 3),
    _CoDot11WEPDefaultKey3Value_Type()
)
coDot11WEPDefaultKey3Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WEPDefaultKey3Value.setStatus("current")
_CoDot11WEPDefaultKey4Value_Type = WEPKeytype
_CoDot11WEPDefaultKey4Value_Object = MibTableColumn
coDot11WEPDefaultKey4Value = _CoDot11WEPDefaultKey4Value_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 3, 1, 4),
    _CoDot11WEPDefaultKey4Value_Type()
)
coDot11WEPDefaultKey4Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WEPDefaultKey4Value.setStatus("current")
_CoDot11PrivacyTable_Object = MibTable
coDot11PrivacyTable = _CoDot11PrivacyTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4)
)
if mibBuilder.loadTexts:
    coDot11PrivacyTable.setStatus("current")
_CoDot11PrivacyEntry_Object = MibTableRow
coDot11PrivacyEntry = _CoDot11PrivacyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    coDot11PrivacyEntry.setStatus("current")
_CoDot11PrivacyInvoked_Type = TruthValue
_CoDot11PrivacyInvoked_Object = MibTableColumn
coDot11PrivacyInvoked = _CoDot11PrivacyInvoked_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 1),
    _CoDot11PrivacyInvoked_Type()
)
coDot11PrivacyInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PrivacyInvoked.setStatus("current")


class _CoDot11WEPDefaultKeyID_Type(Integer32):
    """Custom type coDot11WEPDefaultKeyID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_CoDot11WEPDefaultKeyID_Type.__name__ = "Integer32"
_CoDot11WEPDefaultKeyID_Object = MibTableColumn
coDot11WEPDefaultKeyID = _CoDot11WEPDefaultKeyID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 2),
    _CoDot11WEPDefaultKeyID_Type()
)
coDot11WEPDefaultKeyID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WEPDefaultKeyID.setStatus("current")
_CoDot11ExcludeUnencrypted_Type = TruthValue
_CoDot11ExcludeUnencrypted_Object = MibTableColumn
coDot11ExcludeUnencrypted = _CoDot11ExcludeUnencrypted_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 3),
    _CoDot11ExcludeUnencrypted_Type()
)
coDot11ExcludeUnencrypted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ExcludeUnencrypted.setStatus("current")
_CoDot11WEPICVErrorCount_Type = Counter32
_CoDot11WEPICVErrorCount_Object = MibTableColumn
coDot11WEPICVErrorCount = _CoDot11WEPICVErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 4),
    _CoDot11WEPICVErrorCount_Type()
)
coDot11WEPICVErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WEPICVErrorCount.setStatus("current")
_CoDot11WEPExcludedCount_Type = Counter32
_CoDot11WEPExcludedCount_Object = MibTableColumn
coDot11WEPExcludedCount = _CoDot11WEPExcludedCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 5),
    _CoDot11WEPExcludedCount_Type()
)
coDot11WEPExcludedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WEPExcludedCount.setStatus("current")
_CoDot11RSNAEnabled_Type = TruthValue
_CoDot11RSNAEnabled_Object = MibTableColumn
coDot11RSNAEnabled = _CoDot11RSNAEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 4, 1, 6),
    _CoDot11RSNAEnabled_Type()
)
coDot11RSNAEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAEnabled.setStatus("current")
_CoDot11AssociationTable_Object = MibTable
coDot11AssociationTable = _CoDot11AssociationTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5)
)
if mibBuilder.loadTexts:
    coDot11AssociationTable.setStatus("current")
_CoDot11AssociationEntry_Object = MibTableRow
coDot11AssociationEntry = _CoDot11AssociationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1)
)
coDot11AssociationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11AssociationIndex"),
)
if mibBuilder.loadTexts:
    coDot11AssociationEntry.setStatus("current")


class _CoDot11AssociationIndex_Type(Integer32):
    """Custom type coDot11AssociationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDot11AssociationIndex_Type.__name__ = "Integer32"
_CoDot11AssociationIndex_Object = MibTableColumn
coDot11AssociationIndex = _CoDot11AssociationIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 1),
    _CoDot11AssociationIndex_Type()
)
coDot11AssociationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11AssociationIndex.setStatus("current")
_CoDot11StationMACAddress_Type = MacAddress
_CoDot11StationMACAddress_Object = MibTableColumn
coDot11StationMACAddress = _CoDot11StationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 2),
    _CoDot11StationMACAddress_Type()
)
coDot11StationMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationMACAddress.setStatus("current")
_CoDot11StationConnectTime_Type = Counter32
_CoDot11StationConnectTime_Object = MibTableColumn
coDot11StationConnectTime = _CoDot11StationConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 3),
    _CoDot11StationConnectTime_Type()
)
coDot11StationConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    coDot11StationConnectTime.setUnits("seconds")
_CoDot11SignalLevel_Type = Integer32
_CoDot11SignalLevel_Object = MibTableColumn
coDot11SignalLevel = _CoDot11SignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 4),
    _CoDot11SignalLevel_Type()
)
coDot11SignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11SignalLevel.setUnits("dBm")
_CoDot11NoiseLevel_Type = Integer32
_CoDot11NoiseLevel_Object = MibTableColumn
coDot11NoiseLevel = _CoDot11NoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 5),
    _CoDot11NoiseLevel_Type()
)
coDot11NoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11NoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11NoiseLevel.setUnits("dBm")
_CoDot11SNR_Type = Integer32
_CoDot11SNR_Object = MibTableColumn
coDot11SNR = _CoDot11SNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 6),
    _CoDot11SNR_Type()
)
coDot11SNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SNR.setStatus("current")
_CoDot11PktsRate1_Type = Counter32
_CoDot11PktsRate1_Object = MibTableColumn
coDot11PktsRate1 = _CoDot11PktsRate1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 7),
    _CoDot11PktsRate1_Type()
)
coDot11PktsRate1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate1.setStatus("current")
_CoDot11PktsRate2_Type = Counter32
_CoDot11PktsRate2_Object = MibTableColumn
coDot11PktsRate2 = _CoDot11PktsRate2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 8),
    _CoDot11PktsRate2_Type()
)
coDot11PktsRate2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate2.setStatus("current")
_CoDot11PktsRate5dot5_Type = Counter32
_CoDot11PktsRate5dot5_Object = MibTableColumn
coDot11PktsRate5dot5 = _CoDot11PktsRate5dot5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 9),
    _CoDot11PktsRate5dot5_Type()
)
coDot11PktsRate5dot5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate5dot5.setStatus("current")
_CoDot11PktsRate11_Type = Counter32
_CoDot11PktsRate11_Object = MibTableColumn
coDot11PktsRate11 = _CoDot11PktsRate11_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 10),
    _CoDot11PktsRate11_Type()
)
coDot11PktsRate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate11.setStatus("current")
_CoDot11PktsRate6_Type = Counter32
_CoDot11PktsRate6_Object = MibTableColumn
coDot11PktsRate6 = _CoDot11PktsRate6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 11),
    _CoDot11PktsRate6_Type()
)
coDot11PktsRate6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate6.setStatus("current")
_CoDot11PktsRate9_Type = Counter32
_CoDot11PktsRate9_Object = MibTableColumn
coDot11PktsRate9 = _CoDot11PktsRate9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 12),
    _CoDot11PktsRate9_Type()
)
coDot11PktsRate9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate9.setStatus("current")
_CoDot11PktsRate12_Type = Counter32
_CoDot11PktsRate12_Object = MibTableColumn
coDot11PktsRate12 = _CoDot11PktsRate12_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 13),
    _CoDot11PktsRate12_Type()
)
coDot11PktsRate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate12.setStatus("current")
_CoDot11PktsRate18_Type = Counter32
_CoDot11PktsRate18_Object = MibTableColumn
coDot11PktsRate18 = _CoDot11PktsRate18_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 14),
    _CoDot11PktsRate18_Type()
)
coDot11PktsRate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate18.setStatus("current")
_CoDot11PktsRate24_Type = Counter32
_CoDot11PktsRate24_Object = MibTableColumn
coDot11PktsRate24 = _CoDot11PktsRate24_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 15),
    _CoDot11PktsRate24_Type()
)
coDot11PktsRate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate24.setStatus("current")
_CoDot11PktsRate36_Type = Counter32
_CoDot11PktsRate36_Object = MibTableColumn
coDot11PktsRate36 = _CoDot11PktsRate36_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 16),
    _CoDot11PktsRate36_Type()
)
coDot11PktsRate36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate36.setStatus("current")
_CoDot11PktsRate48_Type = Counter32
_CoDot11PktsRate48_Object = MibTableColumn
coDot11PktsRate48 = _CoDot11PktsRate48_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 17),
    _CoDot11PktsRate48_Type()
)
coDot11PktsRate48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate48.setStatus("current")
_CoDot11PktsRate54_Type = Counter32
_CoDot11PktsRate54_Object = MibTableColumn
coDot11PktsRate54 = _CoDot11PktsRate54_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 18),
    _CoDot11PktsRate54_Type()
)
coDot11PktsRate54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PktsRate54.setStatus("current")
_CoDot11TransmitRate_Type = Unsigned32
_CoDot11TransmitRate_Object = MibTableColumn
coDot11TransmitRate = _CoDot11TransmitRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 19),
    _CoDot11TransmitRate_Type()
)
coDot11TransmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11TransmitRate.setStatus("current")
_CoDot11ReceiveRate_Type = Unsigned32
_CoDot11ReceiveRate_Object = MibTableColumn
coDot11ReceiveRate = _CoDot11ReceiveRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 20),
    _CoDot11ReceiveRate_Type()
)
coDot11ReceiveRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ReceiveRate.setStatus("current")
_CoDot11InPkts_Type = Counter32
_CoDot11InPkts_Object = MibTableColumn
coDot11InPkts = _CoDot11InPkts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 21),
    _CoDot11InPkts_Type()
)
coDot11InPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11InPkts.setStatus("current")
_CoDot11OutPkts_Type = Counter32
_CoDot11OutPkts_Object = MibTableColumn
coDot11OutPkts = _CoDot11OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 22),
    _CoDot11OutPkts_Type()
)
coDot11OutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11OutPkts.setStatus("current")
_CoDot11InOctets_Type = Counter32
_CoDot11InOctets_Object = MibTableColumn
coDot11InOctets = _CoDot11InOctets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 23),
    _CoDot11InOctets_Type()
)
coDot11InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11InOctets.setStatus("current")
_CoDot11OutOctets_Type = Counter32
_CoDot11OutOctets_Object = MibTableColumn
coDot11OutOctets = _CoDot11OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 24),
    _CoDot11OutOctets_Type()
)
coDot11OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11OutOctets.setStatus("current")
_CoDot11StationSSID_Type = AlvarionSSIDOrNone
_CoDot11StationSSID_Object = MibTableColumn
coDot11StationSSID = _CoDot11StationSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 25),
    _CoDot11StationSSID_Type()
)
coDot11StationSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationSSID.setStatus("current")


class _CoDot11StationName_Type(OctetString):
    """Custom type coDot11StationName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CoDot11StationName_Type.__name__ = "OctetString"
_CoDot11StationName_Object = MibTableColumn
coDot11StationName = _CoDot11StationName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 26),
    _CoDot11StationName_Type()
)
coDot11StationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationName.setStatus("current")
_CoDot11StationIPAddress_Type = IpAddress
_CoDot11StationIPAddress_Object = MibTableColumn
coDot11StationIPAddress = _CoDot11StationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 27),
    _CoDot11StationIPAddress_Type()
)
coDot11StationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationIPAddress.setStatus("current")


class _CoDot11StationVLAN_Type(Integer32):
    """Custom type coDot11StationVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_CoDot11StationVLAN_Type.__name__ = "Integer32"
_CoDot11StationVLAN_Object = MibTableColumn
coDot11StationVLAN = _CoDot11StationVLAN_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 28),
    _CoDot11StationVLAN_Type()
)
coDot11StationVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationVLAN.setStatus("current")
_CoDot11StationLocalInterface_Type = InterfaceIndex
_CoDot11StationLocalInterface_Object = MibTableColumn
coDot11StationLocalInterface = _CoDot11StationLocalInterface_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 5, 1, 29),
    _CoDot11StationLocalInterface_Type()
)
coDot11StationLocalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11StationLocalInterface.setStatus("current")
_CoDot11WDSPortTable_Object = MibTable
coDot11WDSPortTable = _CoDot11WDSPortTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6)
)
if mibBuilder.loadTexts:
    coDot11WDSPortTable.setStatus("current")
_CoDot11WDSPortEntry_Object = MibTableRow
coDot11WDSPortEntry = _CoDot11WDSPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1)
)
coDot11WDSPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11WDSPortIndex"),
)
if mibBuilder.loadTexts:
    coDot11WDSPortEntry.setStatus("current")


class _CoDot11WDSPortIndex_Type(Integer32):
    """Custom type coDot11WDSPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_CoDot11WDSPortIndex_Type.__name__ = "Integer32"
_CoDot11WDSPortIndex_Object = MibTableColumn
coDot11WDSPortIndex = _CoDot11WDSPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 1),
    _CoDot11WDSPortIndex_Type()
)
coDot11WDSPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11WDSPortIndex.setStatus("current")
_CoDot11WDSPortMacAddress_Type = MacAddress
_CoDot11WDSPortMacAddress_Object = MibTableColumn
coDot11WDSPortMacAddress = _CoDot11WDSPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 2),
    _CoDot11WDSPortMacAddress_Type()
)
coDot11WDSPortMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11WDSPortMacAddress.setStatus("current")
_CoDot11WDSPortCurrentRate_Type = Unsigned32
_CoDot11WDSPortCurrentRate_Object = MibTableColumn
coDot11WDSPortCurrentRate = _CoDot11WDSPortCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 3),
    _CoDot11WDSPortCurrentRate_Type()
)
coDot11WDSPortCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortCurrentRate.setStatus("current")
_CoDot11WDSPortSNRLevel_Type = Integer32
_CoDot11WDSPortSNRLevel_Object = MibTableColumn
coDot11WDSPortSNRLevel = _CoDot11WDSPortSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 4),
    _CoDot11WDSPortSNRLevel_Type()
)
coDot11WDSPortSNRLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortSNRLevel.setStatus("current")
_CoDot11WDSPortTxPackets_Type = Counter32
_CoDot11WDSPortTxPackets_Object = MibTableColumn
coDot11WDSPortTxPackets = _CoDot11WDSPortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 5),
    _CoDot11WDSPortTxPackets_Type()
)
coDot11WDSPortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortTxPackets.setStatus("current")
_CoDot11WDSPortTxDropped_Type = Counter32
_CoDot11WDSPortTxDropped_Object = MibTableColumn
coDot11WDSPortTxDropped = _CoDot11WDSPortTxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 6),
    _CoDot11WDSPortTxDropped_Type()
)
coDot11WDSPortTxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortTxDropped.setStatus("current")
_CoDot11WDSPortTxErrors_Type = Counter32
_CoDot11WDSPortTxErrors_Object = MibTableColumn
coDot11WDSPortTxErrors = _CoDot11WDSPortTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 7),
    _CoDot11WDSPortTxErrors_Type()
)
coDot11WDSPortTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortTxErrors.setStatus("current")
_CoDot11WDSPortRxPackets_Type = Counter32
_CoDot11WDSPortRxPackets_Object = MibTableColumn
coDot11WDSPortRxPackets = _CoDot11WDSPortRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 8),
    _CoDot11WDSPortRxPackets_Type()
)
coDot11WDSPortRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortRxPackets.setStatus("current")
_CoDot11WDSPortRxDropped_Type = Counter32
_CoDot11WDSPortRxDropped_Object = MibTableColumn
coDot11WDSPortRxDropped = _CoDot11WDSPortRxDropped_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 9),
    _CoDot11WDSPortRxDropped_Type()
)
coDot11WDSPortRxDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortRxDropped.setStatus("current")
_CoDot11WDSPortRxErrors_Type = Counter32
_CoDot11WDSPortRxErrors_Object = MibTableColumn
coDot11WDSPortRxErrors = _CoDot11WDSPortRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 6, 1, 10),
    _CoDot11WDSPortRxErrors_Type()
)
coDot11WDSPortRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WDSPortRxErrors.setStatus("current")
_CoDot11ScanTable_Object = MibTable
coDot11ScanTable = _CoDot11ScanTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7)
)
if mibBuilder.loadTexts:
    coDot11ScanTable.setStatus("current")
_CoDot11ScanEntry_Object = MibTableRow
coDot11ScanEntry = _CoDot11ScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1)
)
coDot11ScanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11ScanIndex"),
)
if mibBuilder.loadTexts:
    coDot11ScanEntry.setStatus("current")


class _CoDot11ScanIndex_Type(Integer32):
    """Custom type coDot11ScanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDot11ScanIndex_Type.__name__ = "Integer32"
_CoDot11ScanIndex_Object = MibTableColumn
coDot11ScanIndex = _CoDot11ScanIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 1),
    _CoDot11ScanIndex_Type()
)
coDot11ScanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11ScanIndex.setStatus("current")
_CoDot11ScanMacAddress_Type = MacAddress
_CoDot11ScanMacAddress_Object = MibTableColumn
coDot11ScanMacAddress = _CoDot11ScanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 2),
    _CoDot11ScanMacAddress_Type()
)
coDot11ScanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanMacAddress.setStatus("current")


class _CoDot11ScanChannel_Type(Integer32):
    """Custom type coDot11ScanChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDot11ScanChannel_Type.__name__ = "Integer32"
_CoDot11ScanChannel_Object = MibTableColumn
coDot11ScanChannel = _CoDot11ScanChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 3),
    _CoDot11ScanChannel_Type()
)
coDot11ScanChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanChannel.setStatus("current")
_CoDot11ScanSSID_Type = AlvarionSSIDOrNone
_CoDot11ScanSSID_Object = MibTableColumn
coDot11ScanSSID = _CoDot11ScanSSID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 4),
    _CoDot11ScanSSID_Type()
)
coDot11ScanSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanSSID.setStatus("current")
_CoDot11ScanSignalLevel_Type = Integer32
_CoDot11ScanSignalLevel_Object = MibTableColumn
coDot11ScanSignalLevel = _CoDot11ScanSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 5),
    _CoDot11ScanSignalLevel_Type()
)
coDot11ScanSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11ScanSignalLevel.setUnits("dBm")
_CoDot11ScanNoiseLevel_Type = Integer32
_CoDot11ScanNoiseLevel_Object = MibTableColumn
coDot11ScanNoiseLevel = _CoDot11ScanNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 6),
    _CoDot11ScanNoiseLevel_Type()
)
coDot11ScanNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanNoiseLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11ScanNoiseLevel.setUnits("dBm")
_CoDot11ScanSNR_Type = Integer32
_CoDot11ScanSNR_Object = MibTableColumn
coDot11ScanSNR = _CoDot11ScanSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 7),
    _CoDot11ScanSNR_Type()
)
coDot11ScanSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanSNR.setStatus("current")


class _CoDot11ScanStatus_Type(Integer32):
    """Custom type coDot11ScanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authorized", 1),
          ("unauthorized", 2),
          ("unknown", 0))
    )


_CoDot11ScanStatus_Type.__name__ = "Integer32"
_CoDot11ScanStatus_Object = MibTableColumn
coDot11ScanStatus = _CoDot11ScanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 8),
    _CoDot11ScanStatus_Type()
)
coDot11ScanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanStatus.setStatus("current")


class _CoDot11ScanPHYType_Type(Integer32):
    """Custom type coDot11ScanPHYType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11g", 3))
    )


_CoDot11ScanPHYType_Type.__name__ = "Integer32"
_CoDot11ScanPHYType_Object = MibTableColumn
coDot11ScanPHYType = _CoDot11ScanPHYType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 9),
    _CoDot11ScanPHYType_Type()
)
coDot11ScanPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanPHYType.setStatus("current")
_CoDot11ScanInactivityTime_Type = TimeTicks
_CoDot11ScanInactivityTime_Object = MibTableColumn
coDot11ScanInactivityTime = _CoDot11ScanInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 7, 1, 10),
    _CoDot11ScanInactivityTime_Type()
)
coDot11ScanInactivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ScanInactivityTime.setStatus("current")


class _CoDot11ScanEnabled_Type(Integer32):
    """Custom type coDot11ScanEnabled based on Integer32"""
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


_CoDot11ScanEnabled_Type.__name__ = "Integer32"
_CoDot11ScanEnabled_Object = MibScalar
coDot11ScanEnabled = _CoDot11ScanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 8),
    _CoDot11ScanEnabled_Type()
)
coDot11ScanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11ScanEnabled.setStatus("current")


class _CoDot11ScanPeriodicity_Type(Integer32):
    """Custom type coDot11ScanPeriodicity based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_CoDot11ScanPeriodicity_Type.__name__ = "Integer32"
_CoDot11ScanPeriodicity_Object = MibScalar
coDot11ScanPeriodicity = _CoDot11ScanPeriodicity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 9),
    _CoDot11ScanPeriodicity_Type()
)
coDot11ScanPeriodicity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11ScanPeriodicity.setStatus("current")
if mibBuilder.loadTexts:
    coDot11ScanPeriodicity.setUnits("seconds")
_CoDot11ScanAuthorizedListURL_Type = DisplayString
_CoDot11ScanAuthorizedListURL_Object = MibScalar
coDot11ScanAuthorizedListURL = _CoDot11ScanAuthorizedListURL_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 10),
    _CoDot11ScanAuthorizedListURL_Type()
)
coDot11ScanAuthorizedListURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11ScanAuthorizedListURL.setStatus("current")


class _CoDot11UnauthorizedAPNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDot11UnauthorizedAPNotificationEnabled based on AlvarionNotificationEnable"""


_CoDot11UnauthorizedAPNotificationEnabled_Object = MibScalar
coDot11UnauthorizedAPNotificationEnabled = _CoDot11UnauthorizedAPNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 11),
    _CoDot11UnauthorizedAPNotificationEnabled_Type()
)
coDot11UnauthorizedAPNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11UnauthorizedAPNotificationEnabled.setStatus("current")


class _CoDot11UnauthorizedAPNotificationInterval_Type(Integer32):
    """Custom type coDot11UnauthorizedAPNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_CoDot11UnauthorizedAPNotificationInterval_Type.__name__ = "Integer32"
_CoDot11UnauthorizedAPNotificationInterval_Object = MibScalar
coDot11UnauthorizedAPNotificationInterval = _CoDot11UnauthorizedAPNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 12),
    _CoDot11UnauthorizedAPNotificationInterval_Type()
)
coDot11UnauthorizedAPNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11UnauthorizedAPNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    coDot11UnauthorizedAPNotificationInterval.setUnits("minutes")


class _CoDot11AssociationNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDot11AssociationNotificationEnabled based on AlvarionNotificationEnable"""


_CoDot11AssociationNotificationEnabled_Object = MibScalar
coDot11AssociationNotificationEnabled = _CoDot11AssociationNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 13),
    _CoDot11AssociationNotificationEnabled_Type()
)
coDot11AssociationNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AssociationNotificationEnabled.setStatus("current")


class _CoDot11AssociationNotificationInterval_Type(Integer32):
    """Custom type coDot11AssociationNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CoDot11AssociationNotificationInterval_Type.__name__ = "Integer32"
_CoDot11AssociationNotificationInterval_Object = MibScalar
coDot11AssociationNotificationInterval = _CoDot11AssociationNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 1, 14),
    _CoDot11AssociationNotificationInterval_Type()
)
coDot11AssociationNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AssociationNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    coDot11AssociationNotificationInterval.setUnits("minutes")
_CoDot11mac_ObjectIdentity = ObjectIdentity
coDot11mac = _CoDot11mac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2)
)
_CoDot11OperationTable_Object = MibTable
coDot11OperationTable = _CoDot11OperationTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1)
)
if mibBuilder.loadTexts:
    coDot11OperationTable.setStatus("current")
_CoDot11OperationEntry_Object = MibTableRow
coDot11OperationEntry = _CoDot11OperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1)
)
coDot11OperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11OperationEntry.setStatus("current")
_CoDot11MACAddress_Type = MacAddress
_CoDot11MACAddress_Object = MibTableColumn
coDot11MACAddress = _CoDot11MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 1),
    _CoDot11MACAddress_Type()
)
coDot11MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MACAddress.setStatus("current")


class _CoDot11RTSThreshold_Type(Integer32):
    """Custom type coDot11RTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1540),
        ValueRangeConstraint(2347, 2347),
    )


_CoDot11RTSThreshold_Type.__name__ = "Integer32"
_CoDot11RTSThreshold_Object = MibTableColumn
coDot11RTSThreshold = _CoDot11RTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 2),
    _CoDot11RTSThreshold_Type()
)
coDot11RTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11RTSThreshold.setStatus("current")


class _CoDot11ShortRetryLimit_Type(Integer32):
    """Custom type coDot11ShortRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11ShortRetryLimit_Type.__name__ = "Integer32"
_CoDot11ShortRetryLimit_Object = MibTableColumn
coDot11ShortRetryLimit = _CoDot11ShortRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 3),
    _CoDot11ShortRetryLimit_Type()
)
coDot11ShortRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ShortRetryLimit.setStatus("current")


class _CoDot11LongRetryLimit_Type(Integer32):
    """Custom type coDot11LongRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11LongRetryLimit_Type.__name__ = "Integer32"
_CoDot11LongRetryLimit_Object = MibTableColumn
coDot11LongRetryLimit = _CoDot11LongRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 4),
    _CoDot11LongRetryLimit_Type()
)
coDot11LongRetryLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11LongRetryLimit.setStatus("current")


class _CoDot11FragmentationThreshold_Type(Integer32):
    """Custom type coDot11FragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_CoDot11FragmentationThreshold_Type.__name__ = "Integer32"
_CoDot11FragmentationThreshold_Object = MibTableColumn
coDot11FragmentationThreshold = _CoDot11FragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 5),
    _CoDot11FragmentationThreshold_Type()
)
coDot11FragmentationThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11FragmentationThreshold.setStatus("current")


class _CoDot11MaxTransmitMSDULifetime_Type(Unsigned32):
    """Custom type coDot11MaxTransmitMSDULifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CoDot11MaxTransmitMSDULifetime_Type.__name__ = "Unsigned32"
_CoDot11MaxTransmitMSDULifetime_Object = MibTableColumn
coDot11MaxTransmitMSDULifetime = _CoDot11MaxTransmitMSDULifetime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 6),
    _CoDot11MaxTransmitMSDULifetime_Type()
)
coDot11MaxTransmitMSDULifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MaxTransmitMSDULifetime.setStatus("current")


class _CoDot11MaxReceiveLifetime_Type(Unsigned32):
    """Custom type coDot11MaxReceiveLifetime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CoDot11MaxReceiveLifetime_Type.__name__ = "Unsigned32"
_CoDot11MaxReceiveLifetime_Object = MibTableColumn
coDot11MaxReceiveLifetime = _CoDot11MaxReceiveLifetime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 7),
    _CoDot11MaxReceiveLifetime_Type()
)
coDot11MaxReceiveLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MaxReceiveLifetime.setStatus("current")


class _CoDot11ManufacturerID_Type(DisplayString):
    """Custom type coDot11ManufacturerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CoDot11ManufacturerID_Type.__name__ = "DisplayString"
_CoDot11ManufacturerID_Object = MibTableColumn
coDot11ManufacturerID = _CoDot11ManufacturerID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 8),
    _CoDot11ManufacturerID_Type()
)
coDot11ManufacturerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ManufacturerID.setStatus("current")


class _CoDot11ProductID_Type(DisplayString):
    """Custom type coDot11ProductID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CoDot11ProductID_Type.__name__ = "DisplayString"
_CoDot11ProductID_Object = MibTableColumn
coDot11ProductID = _CoDot11ProductID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 9),
    _CoDot11ProductID_Type()
)
coDot11ProductID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ProductID.setStatus("current")
_CoDot11RadioType_Type = AlvarionRadioType
_CoDot11RadioType_Object = MibTableColumn
coDot11RadioType = _CoDot11RadioType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 1, 1, 10),
    _CoDot11RadioType_Type()
)
coDot11RadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RadioType.setStatus("current")
_CoDot11CountersTable_Object = MibTable
coDot11CountersTable = _CoDot11CountersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2)
)
if mibBuilder.loadTexts:
    coDot11CountersTable.setStatus("current")
_CoDot11CountersEntry_Object = MibTableRow
coDot11CountersEntry = _CoDot11CountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1)
)
coDot11CountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11CountersEntry.setStatus("current")
_CoDot11TransmittedFragmentCount_Type = Counter32
_CoDot11TransmittedFragmentCount_Object = MibTableColumn
coDot11TransmittedFragmentCount = _CoDot11TransmittedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 1),
    _CoDot11TransmittedFragmentCount_Type()
)
coDot11TransmittedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11TransmittedFragmentCount.setStatus("current")
_CoDot11MulticastTransmittedFrameCount_Type = Counter32
_CoDot11MulticastTransmittedFrameCount_Object = MibTableColumn
coDot11MulticastTransmittedFrameCount = _CoDot11MulticastTransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 2),
    _CoDot11MulticastTransmittedFrameCount_Type()
)
coDot11MulticastTransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MulticastTransmittedFrameCount.setStatus("current")
_CoDot11FailedCount_Type = Counter32
_CoDot11FailedCount_Object = MibTableColumn
coDot11FailedCount = _CoDot11FailedCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 3),
    _CoDot11FailedCount_Type()
)
coDot11FailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11FailedCount.setStatus("current")
_CoDot11RetryCount_Type = Counter32
_CoDot11RetryCount_Object = MibTableColumn
coDot11RetryCount = _CoDot11RetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 4),
    _CoDot11RetryCount_Type()
)
coDot11RetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RetryCount.setStatus("current")
_CoDot11MultipleRetryCount_Type = Counter32
_CoDot11MultipleRetryCount_Object = MibTableColumn
coDot11MultipleRetryCount = _CoDot11MultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 5),
    _CoDot11MultipleRetryCount_Type()
)
coDot11MultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MultipleRetryCount.setStatus("current")
_CoDot11FrameDuplicateCount_Type = Counter32
_CoDot11FrameDuplicateCount_Object = MibTableColumn
coDot11FrameDuplicateCount = _CoDot11FrameDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 6),
    _CoDot11FrameDuplicateCount_Type()
)
coDot11FrameDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11FrameDuplicateCount.setStatus("current")
_CoDot11RTSSuccessCount_Type = Counter32
_CoDot11RTSSuccessCount_Object = MibTableColumn
coDot11RTSSuccessCount = _CoDot11RTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 7),
    _CoDot11RTSSuccessCount_Type()
)
coDot11RTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RTSSuccessCount.setStatus("current")
_CoDot11RTSFailureCount_Type = Counter32
_CoDot11RTSFailureCount_Object = MibTableColumn
coDot11RTSFailureCount = _CoDot11RTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 8),
    _CoDot11RTSFailureCount_Type()
)
coDot11RTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RTSFailureCount.setStatus("current")
_CoDot11ACKFailureCount_Type = Counter32
_CoDot11ACKFailureCount_Object = MibTableColumn
coDot11ACKFailureCount = _CoDot11ACKFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 9),
    _CoDot11ACKFailureCount_Type()
)
coDot11ACKFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ACKFailureCount.setStatus("current")
_CoDot11ReceivedFragmentCount_Type = Counter32
_CoDot11ReceivedFragmentCount_Object = MibTableColumn
coDot11ReceivedFragmentCount = _CoDot11ReceivedFragmentCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 10),
    _CoDot11ReceivedFragmentCount_Type()
)
coDot11ReceivedFragmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11ReceivedFragmentCount.setStatus("current")
_CoDot11MulticastReceivedFrameCount_Type = Counter32
_CoDot11MulticastReceivedFrameCount_Object = MibTableColumn
coDot11MulticastReceivedFrameCount = _CoDot11MulticastReceivedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 11),
    _CoDot11MulticastReceivedFrameCount_Type()
)
coDot11MulticastReceivedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11MulticastReceivedFrameCount.setStatus("current")
_CoDot11FCSErrorCount_Type = Counter32
_CoDot11FCSErrorCount_Object = MibTableColumn
coDot11FCSErrorCount = _CoDot11FCSErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 12),
    _CoDot11FCSErrorCount_Type()
)
coDot11FCSErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11FCSErrorCount.setStatus("current")
_CoDot11TransmittedFrameCount_Type = Counter32
_CoDot11TransmittedFrameCount_Object = MibTableColumn
coDot11TransmittedFrameCount = _CoDot11TransmittedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 13),
    _CoDot11TransmittedFrameCount_Type()
)
coDot11TransmittedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11TransmittedFrameCount.setStatus("current")
_CoDot11WEPUndecryptableCount_Type = Counter32
_CoDot11WEPUndecryptableCount_Object = MibTableColumn
coDot11WEPUndecryptableCount = _CoDot11WEPUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 2, 2, 1, 14),
    _CoDot11WEPUndecryptableCount_Type()
)
coDot11WEPUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11WEPUndecryptableCount.setStatus("current")
_CoDot11phy_ObjectIdentity = ObjectIdentity
coDot11phy = _CoDot11phy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3)
)
_CoDot11PhyOperationTable_Object = MibTable
coDot11PhyOperationTable = _CoDot11PhyOperationTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1)
)
if mibBuilder.loadTexts:
    coDot11PhyOperationTable.setStatus("current")
_CoDot11PhyOperationEntry_Object = MibTableRow
coDot11PhyOperationEntry = _CoDot11PhyOperationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1)
)
coDot11PhyOperationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11PhyOperationEntry.setStatus("current")


class _CoDot11PHYType_Type(Integer32):
    """Custom type coDot11PHYType based on Integer32"""
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
        *(("dsss", 2),
          ("fhss", 1),
          ("irbaseband", 3),
          ("ofdm", 4))
    )


_CoDot11PHYType_Type.__name__ = "Integer32"
_CoDot11PHYType_Object = MibTableColumn
coDot11PHYType = _CoDot11PHYType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 1),
    _CoDot11PHYType_Type()
)
coDot11PHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PHYType.setStatus("current")
_CoDot11CurrentRegDomain_Type = Integer32
_CoDot11CurrentRegDomain_Object = MibTableColumn
coDot11CurrentRegDomain = _CoDot11CurrentRegDomain_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 2),
    _CoDot11CurrentRegDomain_Type()
)
coDot11CurrentRegDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentRegDomain.setStatus("current")


class _CoDot11TempType_Type(Integer32):
    """Custom type coDot11TempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tempType1", 1),
          ("tempType2", 2))
    )


_CoDot11TempType_Type.__name__ = "Integer32"
_CoDot11TempType_Object = MibTableColumn
coDot11TempType = _CoDot11TempType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 3),
    _CoDot11TempType_Type()
)
coDot11TempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11TempType.setStatus("current")
_CoDot11CurrentOperFrequency_Type = Unsigned32
_CoDot11CurrentOperFrequency_Object = MibTableColumn
coDot11CurrentOperFrequency = _CoDot11CurrentOperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 4),
    _CoDot11CurrentOperFrequency_Type()
)
coDot11CurrentOperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentOperFrequency.setStatus("current")


class _CoDot11CurrentOperPHYType_Type(Integer32):
    """Custom type coDot11CurrentOperPHYType based on Integer32"""
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
        *(("ieee802dot11a", 1),
          ("ieee802dot11b", 2),
          ("ieee802dot11bAndg", 4),
          ("ieee802dot11g", 3))
    )


_CoDot11CurrentOperPHYType_Type.__name__ = "Integer32"
_CoDot11CurrentOperPHYType_Object = MibTableColumn
coDot11CurrentOperPHYType = _CoDot11CurrentOperPHYType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 5),
    _CoDot11CurrentOperPHYType_Type()
)
coDot11CurrentOperPHYType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentOperPHYType.setStatus("current")


class _CoDot11Sensitivity_Type(Integer32):
    """Custom type coDot11Sensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("large", 1),
          ("medium", 2),
          ("small", 3))
    )


_CoDot11Sensitivity_Type.__name__ = "Integer32"
_CoDot11Sensitivity_Object = MibTableColumn
coDot11Sensitivity = _CoDot11Sensitivity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 6),
    _CoDot11Sensitivity_Type()
)
coDot11Sensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11Sensitivity.setStatus("current")
_CoDot11RadioEnabled_Type = TruthValue
_CoDot11RadioEnabled_Object = MibTableColumn
coDot11RadioEnabled = _CoDot11RadioEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 7),
    _CoDot11RadioEnabled_Type()
)
coDot11RadioEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11RadioEnabled.setStatus("current")


class _CoDot11OperatingMode_Type(Integer32):
    """Custom type coDot11OperatingMode based on Integer32"""
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
        *(("accessPointAndWirelessLinks", 1),
          ("accessPointOnly", 2),
          ("monitor", 4),
          ("wirelessLinksOnly", 3))
    )


_CoDot11OperatingMode_Type.__name__ = "Integer32"
_CoDot11OperatingMode_Object = MibTableColumn
coDot11OperatingMode = _CoDot11OperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 8),
    _CoDot11OperatingMode_Type()
)
coDot11OperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11OperatingMode.setStatus("current")
_CoDot11AutoChannelEnabled_Type = TruthValue
_CoDot11AutoChannelEnabled_Object = MibTableColumn
coDot11AutoChannelEnabled = _CoDot11AutoChannelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 9),
    _CoDot11AutoChannelEnabled_Type()
)
coDot11AutoChannelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AutoChannelEnabled.setStatus("current")


class _CoDot11AutoChannelInterval_Type(Integer32):
    """Custom type coDot11AutoChannelInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              60,
              120,
              240,
              480,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("eightHours", 480),
          ("fourHours", 240),
          ("oneHour", 60),
          ("timeOfDay", 1),
          ("tweentyFourHours", 1440),
          ("twelveHours", 720),
          ("twoHours", 120))
    )


_CoDot11AutoChannelInterval_Type.__name__ = "Integer32"
_CoDot11AutoChannelInterval_Object = MibTableColumn
coDot11AutoChannelInterval = _CoDot11AutoChannelInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 10),
    _CoDot11AutoChannelInterval_Type()
)
coDot11AutoChannelInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AutoChannelInterval.setStatus("current")
_CoDot11AutoPowerEnabled_Type = TruthValue
_CoDot11AutoPowerEnabled_Object = MibTableColumn
coDot11AutoPowerEnabled = _CoDot11AutoPowerEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 11),
    _CoDot11AutoPowerEnabled_Type()
)
coDot11AutoPowerEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AutoPowerEnabled.setStatus("current")


class _CoDot11AutoPowerInterval_Type(Integer32):
    """Custom type coDot11AutoPowerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(60,
              120,
              240,
              480,
              720,
              1440)
        )
    )
    namedValues = NamedValues(
        *(("eightHours", 480),
          ("fourHours", 240),
          ("oneHour", 60),
          ("tweentyFourHours", 1440),
          ("twelveHours", 720),
          ("twoHours", 120))
    )


_CoDot11AutoPowerInterval_Type.__name__ = "Integer32"
_CoDot11AutoPowerInterval_Object = MibTableColumn
coDot11AutoPowerInterval = _CoDot11AutoPowerInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 1, 1, 12),
    _CoDot11AutoPowerInterval_Type()
)
coDot11AutoPowerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11AutoPowerInterval.setStatus("current")
_CoDot11PhyAntennaTable_Object = MibTable
coDot11PhyAntennaTable = _CoDot11PhyAntennaTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 2)
)
if mibBuilder.loadTexts:
    coDot11PhyAntennaTable.setStatus("current")
_CoDot11PhyAntennaEntry_Object = MibTableRow
coDot11PhyAntennaEntry = _CoDot11PhyAntennaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 2, 1)
)
coDot11PhyAntennaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11PhyAntennaEntry.setStatus("current")


class _CoDot11CurrentTxAntenna_Type(Integer32):
    """Custom type coDot11CurrentTxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11CurrentTxAntenna_Type.__name__ = "Integer32"
_CoDot11CurrentTxAntenna_Object = MibTableColumn
coDot11CurrentTxAntenna = _CoDot11CurrentTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 2, 1, 1),
    _CoDot11CurrentTxAntenna_Type()
)
coDot11CurrentTxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentTxAntenna.setStatus("current")


class _CoDot11DiversitySupport_Type(Integer32):
    """Custom type coDot11DiversitySupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("fixedlist", 1),
          ("notsupported", 2))
    )


_CoDot11DiversitySupport_Type.__name__ = "Integer32"
_CoDot11DiversitySupport_Object = MibTableColumn
coDot11DiversitySupport = _CoDot11DiversitySupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 2, 1, 2),
    _CoDot11DiversitySupport_Type()
)
coDot11DiversitySupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11DiversitySupport.setStatus("current")


class _CoDot11CurrentRxAntenna_Type(Integer32):
    """Custom type coDot11CurrentRxAntenna based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11CurrentRxAntenna_Type.__name__ = "Integer32"
_CoDot11CurrentRxAntenna_Object = MibTableColumn
coDot11CurrentRxAntenna = _CoDot11CurrentRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 2, 1, 3),
    _CoDot11CurrentRxAntenna_Type()
)
coDot11CurrentRxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentRxAntenna.setStatus("current")
_CoDot11PhyConfigTable_Object = MibTable
coDot11PhyConfigTable = _CoDot11PhyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 3)
)
if mibBuilder.loadTexts:
    coDot11PhyConfigTable.setStatus("current")
_CoDot11PhyConfigEntry_Object = MibTableRow
coDot11PhyConfigEntry = _CoDot11PhyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 3, 1)
)
coDot11PhyConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11PhyConfigEntry.setStatus("current")


class _CoDot11PhyAdminStatus_Type(Integer32):
    """Custom type coDot11PhyAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CoDot11PhyAdminStatus_Type.__name__ = "Integer32"
_CoDot11PhyAdminStatus_Object = MibTableColumn
coDot11PhyAdminStatus = _CoDot11PhyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 3, 1, 1),
    _CoDot11PhyAdminStatus_Type()
)
coDot11PhyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11PhyAdminStatus.setStatus("current")


class _CoDot11PhyOperStatus_Type(Integer32):
    """Custom type coDot11PhyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CoDot11PhyOperStatus_Type.__name__ = "Integer32"
_CoDot11PhyOperStatus_Object = MibTableColumn
coDot11PhyOperStatus = _CoDot11PhyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 3, 1, 2),
    _CoDot11PhyOperStatus_Type()
)
coDot11PhyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11PhyOperStatus.setStatus("current")
_CoDot11PhyDSSSTable_Object = MibTable
coDot11PhyDSSSTable = _CoDot11PhyDSSSTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 4)
)
if mibBuilder.loadTexts:
    coDot11PhyDSSSTable.setStatus("current")
_CoDot11PhyDSSSEntry_Object = MibTableRow
coDot11PhyDSSSEntry = _CoDot11PhyDSSSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 4, 1)
)
coDot11PhyDSSSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11PhyDSSSEntry.setStatus("current")


class _CoDot11CurrentChannel_Type(Integer32):
    """Custom type coDot11CurrentChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_CoDot11CurrentChannel_Type.__name__ = "Integer32"
_CoDot11CurrentChannel_Object = MibTableColumn
coDot11CurrentChannel = _CoDot11CurrentChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 4, 1, 1),
    _CoDot11CurrentChannel_Type()
)
coDot11CurrentChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11CurrentChannel.setStatus("current")


class _CoDot11CCAModeSupported_Type(Integer32):
    """Custom type coDot11CCAModeSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CoDot11CCAModeSupported_Type.__name__ = "Integer32"
_CoDot11CCAModeSupported_Object = MibTableColumn
coDot11CCAModeSupported = _CoDot11CCAModeSupported_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 4, 1, 2),
    _CoDot11CCAModeSupported_Type()
)
coDot11CCAModeSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CCAModeSupported.setStatus("current")


class _CoDot11CurrentCCAMode_Type(Integer32):
    """Custom type coDot11CurrentCCAMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("csonly", 2),
          ("edandcs", 4),
          ("edonly", 1))
    )


_CoDot11CurrentCCAMode_Type.__name__ = "Integer32"
_CoDot11CurrentCCAMode_Object = MibTableColumn
coDot11CurrentCCAMode = _CoDot11CurrentCCAMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 4, 1, 3),
    _CoDot11CurrentCCAMode_Type()
)
coDot11CurrentCCAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CurrentCCAMode.setStatus("current")
_CoDot11RegDomainsSupportedTable_Object = MibTable
coDot11RegDomainsSupportedTable = _CoDot11RegDomainsSupportedTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 5)
)
if mibBuilder.loadTexts:
    coDot11RegDomainsSupportedTable.setStatus("current")
_CoDot11RegDomainsSupportedEntry_Object = MibTableRow
coDot11RegDomainsSupportedEntry = _CoDot11RegDomainsSupportedEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 5, 1)
)
coDot11RegDomainsSupportedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11RegDomainsSupportIndex"),
)
if mibBuilder.loadTexts:
    coDot11RegDomainsSupportedEntry.setStatus("current")


class _CoDot11RegDomainsSupportIndex_Type(Integer32):
    """Custom type coDot11RegDomainsSupportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CoDot11RegDomainsSupportIndex_Type.__name__ = "Integer32"
_CoDot11RegDomainsSupportIndex_Object = MibTableColumn
coDot11RegDomainsSupportIndex = _CoDot11RegDomainsSupportIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 5, 1, 1),
    _CoDot11RegDomainsSupportIndex_Type()
)
coDot11RegDomainsSupportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11RegDomainsSupportIndex.setStatus("current")


class _CoDot11RegDomainsSupportValue_Type(Integer32):
    """Custom type coDot11RegDomainsSupportValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              49,
              50,
              65)
        )
    )
    namedValues = NamedValues(
        *(("doc", 32),
          ("etsi", 48),
          ("fcc", 16),
          ("france", 50),
          ("japan", 65),
          ("spain", 49))
    )


_CoDot11RegDomainsSupportValue_Type.__name__ = "Integer32"
_CoDot11RegDomainsSupportValue_Object = MibTableColumn
coDot11RegDomainsSupportValue = _CoDot11RegDomainsSupportValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 5, 1, 2),
    _CoDot11RegDomainsSupportValue_Type()
)
coDot11RegDomainsSupportValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RegDomainsSupportValue.setStatus("current")
_CoDot11AntennasListTable_Object = MibTable
coDot11AntennasListTable = _CoDot11AntennasListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6)
)
if mibBuilder.loadTexts:
    coDot11AntennasListTable.setStatus("current")
_CoDot11AntennasListEntry_Object = MibTableRow
coDot11AntennasListEntry = _CoDot11AntennasListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6, 1)
)
coDot11AntennasListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11AntennaListIndex"),
)
if mibBuilder.loadTexts:
    coDot11AntennasListEntry.setStatus("current")


class _CoDot11AntennaListIndex_Type(Integer32):
    """Custom type coDot11AntennaListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CoDot11AntennaListIndex_Type.__name__ = "Integer32"
_CoDot11AntennaListIndex_Object = MibTableColumn
coDot11AntennaListIndex = _CoDot11AntennaListIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6, 1, 1),
    _CoDot11AntennaListIndex_Type()
)
coDot11AntennaListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11AntennaListIndex.setStatus("current")
_CoDot11SupportedTxAntenna_Type = TruthValue
_CoDot11SupportedTxAntenna_Object = MibTableColumn
coDot11SupportedTxAntenna = _CoDot11SupportedTxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6, 1, 2),
    _CoDot11SupportedTxAntenna_Type()
)
coDot11SupportedTxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SupportedTxAntenna.setStatus("current")
_CoDot11SupportedRxAntenna_Type = TruthValue
_CoDot11SupportedRxAntenna_Object = MibTableColumn
coDot11SupportedRxAntenna = _CoDot11SupportedRxAntenna_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6, 1, 3),
    _CoDot11SupportedRxAntenna_Type()
)
coDot11SupportedRxAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SupportedRxAntenna.setStatus("current")
_CoDot11DiversitySelectionRx_Type = TruthValue
_CoDot11DiversitySelectionRx_Object = MibTableColumn
coDot11DiversitySelectionRx = _CoDot11DiversitySelectionRx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 6, 1, 4),
    _CoDot11DiversitySelectionRx_Type()
)
coDot11DiversitySelectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11DiversitySelectionRx.setStatus("current")
_CoDot11SupportedDataRatesTxTable_Object = MibTable
coDot11SupportedDataRatesTxTable = _CoDot11SupportedDataRatesTxTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 7)
)
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesTxTable.setStatus("current")
_CoDot11SupportedDataRatesTxEntry_Object = MibTableRow
coDot11SupportedDataRatesTxEntry = _CoDot11SupportedDataRatesTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 7, 1)
)
coDot11SupportedDataRatesTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11SupportedDataRatesTxIndex"),
)
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesTxEntry.setStatus("current")


class _CoDot11SupportedDataRatesTxIndex_Type(Integer32):
    """Custom type coDot11SupportedDataRatesTxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CoDot11SupportedDataRatesTxIndex_Type.__name__ = "Integer32"
_CoDot11SupportedDataRatesTxIndex_Object = MibTableColumn
coDot11SupportedDataRatesTxIndex = _CoDot11SupportedDataRatesTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 7, 1, 1),
    _CoDot11SupportedDataRatesTxIndex_Type()
)
coDot11SupportedDataRatesTxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesTxIndex.setStatus("current")


class _CoDot11SupportedDataRatesTxValue_Type(Integer32):
    """Custom type coDot11SupportedDataRatesTxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_CoDot11SupportedDataRatesTxValue_Type.__name__ = "Integer32"
_CoDot11SupportedDataRatesTxValue_Object = MibTableColumn
coDot11SupportedDataRatesTxValue = _CoDot11SupportedDataRatesTxValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 7, 1, 2),
    _CoDot11SupportedDataRatesTxValue_Type()
)
coDot11SupportedDataRatesTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesTxValue.setStatus("current")
_CoDot11SupportedDataRatesRxTable_Object = MibTable
coDot11SupportedDataRatesRxTable = _CoDot11SupportedDataRatesRxTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 8)
)
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesRxTable.setStatus("current")
_CoDot11SupportedDataRatesRxEntry_Object = MibTableRow
coDot11SupportedDataRatesRxEntry = _CoDot11SupportedDataRatesRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 8, 1)
)
coDot11SupportedDataRatesRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ALVARION-802DOT11-MIB", "coDot11SupportedDataRatesRxIndex"),
)
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesRxEntry.setStatus("current")


class _CoDot11SupportedDataRatesRxIndex_Type(Integer32):
    """Custom type coDot11SupportedDataRatesRxIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_CoDot11SupportedDataRatesRxIndex_Type.__name__ = "Integer32"
_CoDot11SupportedDataRatesRxIndex_Object = MibTableColumn
coDot11SupportedDataRatesRxIndex = _CoDot11SupportedDataRatesRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 8, 1, 1),
    _CoDot11SupportedDataRatesRxIndex_Type()
)
coDot11SupportedDataRatesRxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesRxIndex.setStatus("current")


class _CoDot11SupportedDataRatesRxValue_Type(Integer32):
    """Custom type coDot11SupportedDataRatesRxValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 127),
    )


_CoDot11SupportedDataRatesRxValue_Type.__name__ = "Integer32"
_CoDot11SupportedDataRatesRxValue_Object = MibTableColumn
coDot11SupportedDataRatesRxValue = _CoDot11SupportedDataRatesRxValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 8, 1, 2),
    _CoDot11SupportedDataRatesRxValue_Type()
)
coDot11SupportedDataRatesRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11SupportedDataRatesRxValue.setStatus("current")
_CoDot11PhyOFDMTable_Object = MibTable
coDot11PhyOFDMTable = _CoDot11PhyOFDMTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 9)
)
if mibBuilder.loadTexts:
    coDot11PhyOFDMTable.setStatus("current")
_CoDot11PhyOFDMEntry_Object = MibTableRow
coDot11PhyOFDMEntry = _CoDot11PhyOFDMEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 9, 1)
)
coDot11PhyOFDMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    coDot11PhyOFDMEntry.setStatus("current")


class _CoDot11CurrentFrequency_Type(Integer32):
    """Custom type coDot11CurrentFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CoDot11CurrentFrequency_Type.__name__ = "Integer32"
_CoDot11CurrentFrequency_Object = MibTableColumn
coDot11CurrentFrequency = _CoDot11CurrentFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 9, 1, 1),
    _CoDot11CurrentFrequency_Type()
)
coDot11CurrentFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11CurrentFrequency.setStatus("current")
_CoDot11TIThreshold_Type = Integer32
_CoDot11TIThreshold_Object = MibTableColumn
coDot11TIThreshold = _CoDot11TIThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 9, 1, 2),
    _CoDot11TIThreshold_Type()
)
coDot11TIThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11TIThreshold.setStatus("current")


class _CoDot11FrequencyBandsSupported_Type(Integer32):
    """Custom type coDot11FrequencyBandsSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_CoDot11FrequencyBandsSupported_Type.__name__ = "Integer32"
_CoDot11FrequencyBandsSupported_Object = MibTableColumn
coDot11FrequencyBandsSupported = _CoDot11FrequencyBandsSupported_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 9, 1, 3),
    _CoDot11FrequencyBandsSupported_Type()
)
coDot11FrequencyBandsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11FrequencyBandsSupported.setStatus("current")


class _CoDot11MinimumSNRLevel_Type(Integer32):
    """Custom type coDot11MinimumSNRLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 92),
    )


_CoDot11MinimumSNRLevel_Type.__name__ = "Integer32"
_CoDot11MinimumSNRLevel_Object = MibScalar
coDot11MinimumSNRLevel = _CoDot11MinimumSNRLevel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 10),
    _CoDot11MinimumSNRLevel_Type()
)
coDot11MinimumSNRLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11MinimumSNRLevel.setStatus("current")
if mibBuilder.loadTexts:
    coDot11MinimumSNRLevel.setUnits("dBm")


class _CoDot11SNRLevelNotificationEnabled_Type(AlvarionNotificationEnable):
    """Custom type coDot11SNRLevelNotificationEnabled based on AlvarionNotificationEnable"""


_CoDot11SNRLevelNotificationEnabled_Object = MibScalar
coDot11SNRLevelNotificationEnabled = _CoDot11SNRLevelNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 11),
    _CoDot11SNRLevelNotificationEnabled_Type()
)
coDot11SNRLevelNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11SNRLevelNotificationEnabled.setStatus("current")


class _CoDot11SNRLevelNotificationInterval_Type(Integer32):
    """Custom type coDot11SNRLevelNotificationInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_CoDot11SNRLevelNotificationInterval_Type.__name__ = "Integer32"
_CoDot11SNRLevelNotificationInterval_Object = MibScalar
coDot11SNRLevelNotificationInterval = _CoDot11SNRLevelNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 12),
    _CoDot11SNRLevelNotificationInterval_Type()
)
coDot11SNRLevelNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coDot11SNRLevelNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    coDot11SNRLevelNotificationInterval.setUnits("minutes")


class _CoDot11CountryCode_Type(Integer32):
    """Custom type coDot11CountryCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8,
              12,
              31,
              32,
              36,
              40,
              48,
              51,
              56,
              68,
              76,
              84,
              96,
              100,
              112,
              124,
              152,
              156,
              158,
              170,
              188,
              191,
              196,
              203,
              208,
              214,
              218,
              222,
              233,
              246,
              250,
              268,
              276,
              300,
              320,
              340,
              344,
              348,
              352,
              356,
              360,
              364,
              372,
              376,
              380,
              392,
              393,
              395,
              396,
              397,
              398,
              400,
              404,
              408,
              410,
              414,
              422,
              428,
              438,
              440,
              442,
              446,
              458,
              484,
              492,
              504,
              512,
              528,
              554,
              578,
              586,
              591,
              604,
              608,
              616,
              620,
              630,
              634,
              642,
              643,
              682,
              702,
              703,
              704,
              705,
              710,
              716,
              724,
              752,
              756,
              760,
              764,
              780,
              784,
              788,
              792,
              804,
              807,
              818,
              826,
              827,
              840,
              858,
              860,
              862,
              887)
        )
    )
    namedValues = NamedValues(
        *(("albania", 8),
          ("algeria", 12),
          ("argentina", 32),
          ("armenia", 51),
          ("australia", 36),
          ("austria", 40),
          ("azerbaijan", 31),
          ("bahrain", 48),
          ("belarus", 112),
          ("belgium", 56),
          ("belize", 84),
          ("bolivia", 68),
          ("brazil", 76),
          ("bruneiDarussalam", 96),
          ("bulgaria", 100),
          ("canada", 124),
          ("chile", 152),
          ("china", 156),
          ("colombia", 170),
          ("costaRica", 188),
          ("croatia", 191),
          ("cyprus", 196),
          ("czechRepublic", 203),
          ("denmark", 208),
          ("dominicanRepublic", 214),
          ("ecuador", 218),
          ("egypt", 818),
          ("elSalvador", 222),
          ("estonia", 233),
          ("finland", 246),
          ("france", 250),
          ("georgia", 268),
          ("germany", 276),
          ("greece", 300),
          ("guatemala", 320),
          ("honduras", 340),
          ("hongkong", 344),
          ("hungary", 348),
          ("iceland", 352),
          ("india", 356),
          ("indonesia", 360),
          ("iran", 364),
          ("ireland", 372),
          ("israel", 376),
          ("italy", 380),
          ("japanClient", 397),
          ("japanJ52", 395),
          ("japanJ5280211j", 396),
          ("japanW52W53", 392),
          ("japanW52W53J52", 393),
          ("jordan", 400),
          ("kazakhstan", 398),
          ("kenya", 404),
          ("kuwait", 414),
          ("latvia", 428),
          ("lebanon", 422),
          ("liechtenstein", 438),
          ("lithuania", 440),
          ("luxembourg", 442),
          ("macau", 446),
          ("macedonia", 807),
          ("malaysia", 458),
          ("mexico", 484),
          ("monaco", 492),
          ("morocco", 504),
          ("netherlands", 528),
          ("newZealand", 554),
          ("northKorea", 408),
          ("norway", 578),
          ("oman", 512),
          ("pakistan", 586),
          ("panama", 591),
          ("peru", 604),
          ("philippines", 608),
          ("poland", 616),
          ("portugal", 620),
          ("puertoRico", 630),
          ("qatar", 634),
          ("romania", 642),
          ("russianFederation", 643),
          ("saudiArabia", 682),
          ("singapore", 702),
          ("slovakia", 703),
          ("slovenia", 705),
          ("southAfrica", 710),
          ("southKorea", 410),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("syria", 760),
          ("taiwan", 158),
          ("thailand", 764),
          ("trinidadAndTobago", 780),
          ("tunisia", 788),
          ("turkey", 792),
          ("ukraine", 804),
          ("unitedArabEmirates", 784),
          ("unitedKingdom", 826),
          ("unitedKingdom58GHz", 827),
          ("unitedStates", 840),
          ("uruguay", 858),
          ("uzbekistan", 860),
          ("venezuela", 862),
          ("vietNam", 704),
          ("world", 1),
          ("yemen", 887),
          ("zimbabwe", 716))
    )


_CoDot11CountryCode_Type.__name__ = "Integer32"
_CoDot11CountryCode_Object = MibScalar
coDot11CountryCode = _CoDot11CountryCode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 3, 13),
    _CoDot11CountryCode_Type()
)
coDot11CountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11CountryCode.setStatus("current")
_CoDot11RSNAStatsTable_Object = MibTable
coDot11RSNAStatsTable = _CoDot11RSNAStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4)
)
if mibBuilder.loadTexts:
    coDot11RSNAStatsTable.setStatus("current")
_CoDot11RSNAStatsEntry_Object = MibTableRow
coDot11RSNAStatsEntry = _CoDot11RSNAStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1)
)
if mibBuilder.loadTexts:
    coDot11RSNAStatsEntry.setStatus("current")


class _CoDot11RSNAStatsVersion_Type(Unsigned32):
    """Custom type coDot11RSNAStatsVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CoDot11RSNAStatsVersion_Type.__name__ = "Unsigned32"
_CoDot11RSNAStatsVersion_Object = MibTableColumn
coDot11RSNAStatsVersion = _CoDot11RSNAStatsVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 2),
    _CoDot11RSNAStatsVersion_Type()
)
coDot11RSNAStatsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsVersion.setStatus("current")


class _CoDot11RSNAStatsSelectedPairwiseCipher_Type(OctetString):
    """Custom type coDot11RSNAStatsSelectedPairwiseCipher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_CoDot11RSNAStatsSelectedPairwiseCipher_Type.__name__ = "OctetString"
_CoDot11RSNAStatsSelectedPairwiseCipher_Object = MibTableColumn
coDot11RSNAStatsSelectedPairwiseCipher = _CoDot11RSNAStatsSelectedPairwiseCipher_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 3),
    _CoDot11RSNAStatsSelectedPairwiseCipher_Type()
)
coDot11RSNAStatsSelectedPairwiseCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsSelectedPairwiseCipher.setStatus("current")
_CoDot11RSNAStatsTKIPICVErrors_Type = Counter32
_CoDot11RSNAStatsTKIPICVErrors_Object = MibTableColumn
coDot11RSNAStatsTKIPICVErrors = _CoDot11RSNAStatsTKIPICVErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 4),
    _CoDot11RSNAStatsTKIPICVErrors_Type()
)
coDot11RSNAStatsTKIPICVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsTKIPICVErrors.setStatus("current")
_CoDot11RSNAStatsTKIPLocalMICFailures_Type = Counter32
_CoDot11RSNAStatsTKIPLocalMICFailures_Object = MibTableColumn
coDot11RSNAStatsTKIPLocalMICFailures = _CoDot11RSNAStatsTKIPLocalMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 5),
    _CoDot11RSNAStatsTKIPLocalMICFailures_Type()
)
coDot11RSNAStatsTKIPLocalMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsTKIPLocalMICFailures.setStatus("current")
_CoDot11RSNAStatsTKIPRemoteMICFailures_Type = Counter32
_CoDot11RSNAStatsTKIPRemoteMICFailures_Object = MibTableColumn
coDot11RSNAStatsTKIPRemoteMICFailures = _CoDot11RSNAStatsTKIPRemoteMICFailures_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 6),
    _CoDot11RSNAStatsTKIPRemoteMICFailures_Type()
)
coDot11RSNAStatsTKIPRemoteMICFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsTKIPRemoteMICFailures.setStatus("current")
_CoDot11RSNAStatsTKIPCounterMeasuresInvoked_Type = Counter32
_CoDot11RSNAStatsTKIPCounterMeasuresInvoked_Object = MibTableColumn
coDot11RSNAStatsTKIPCounterMeasuresInvoked = _CoDot11RSNAStatsTKIPCounterMeasuresInvoked_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 7),
    _CoDot11RSNAStatsTKIPCounterMeasuresInvoked_Type()
)
coDot11RSNAStatsTKIPCounterMeasuresInvoked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsTKIPCounterMeasuresInvoked.setStatus("current")
_CoDot11RSNAStatsCCMPFormatErrors_Type = Counter32
_CoDot11RSNAStatsCCMPFormatErrors_Object = MibTableColumn
coDot11RSNAStatsCCMPFormatErrors = _CoDot11RSNAStatsCCMPFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 8),
    _CoDot11RSNAStatsCCMPFormatErrors_Type()
)
coDot11RSNAStatsCCMPFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsCCMPFormatErrors.setStatus("current")
_CoDot11RSNAStatsCCMPReplays_Type = Counter32
_CoDot11RSNAStatsCCMPReplays_Object = MibTableColumn
coDot11RSNAStatsCCMPReplays = _CoDot11RSNAStatsCCMPReplays_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 9),
    _CoDot11RSNAStatsCCMPReplays_Type()
)
coDot11RSNAStatsCCMPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsCCMPReplays.setStatus("current")
_CoDot11RSNAStatsCCMPDecryptErrors_Type = Counter32
_CoDot11RSNAStatsCCMPDecryptErrors_Object = MibTableColumn
coDot11RSNAStatsCCMPDecryptErrors = _CoDot11RSNAStatsCCMPDecryptErrors_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 10),
    _CoDot11RSNAStatsCCMPDecryptErrors_Type()
)
coDot11RSNAStatsCCMPDecryptErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsCCMPDecryptErrors.setStatus("current")
_CoDot11RSNAStatsTKIPReplays_Type = Counter32
_CoDot11RSNAStatsTKIPReplays_Object = MibTableColumn
coDot11RSNAStatsTKIPReplays = _CoDot11RSNAStatsTKIPReplays_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 11),
    _CoDot11RSNAStatsTKIPReplays_Type()
)
coDot11RSNAStatsTKIPReplays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStatsTKIPReplays.setStatus("current")
_CoDot11RSNAStats4WayHandshakeFailures_Type = Counter32
_CoDot11RSNAStats4WayHandshakeFailures_Object = MibTableColumn
coDot11RSNAStats4WayHandshakeFailures = _CoDot11RSNAStats4WayHandshakeFailures_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 4, 1, 12),
    _CoDot11RSNAStats4WayHandshakeFailures_Type()
)
coDot11RSNAStats4WayHandshakeFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coDot11RSNAStats4WayHandshakeFailures.setStatus("current")
_CoDot11ManagementMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
coDot11ManagementMIBNotificationPrefix = _CoDot11ManagementMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 5)
)
_CoDot11ManagementMIBNotifications_ObjectIdentity = ObjectIdentity
coDot11ManagementMIBNotifications = _CoDot11ManagementMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 5, 0)
)
_CoDot11Conformance_ObjectIdentity = ObjectIdentity
coDot11Conformance = _CoDot11Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6)
)
_CoDot11Groups_ObjectIdentity = ObjectIdentity
coDot11Groups = _CoDot11Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1)
)
_CoDot11Compliances_ObjectIdentity = ObjectIdentity
coDot11Compliances = _CoDot11Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 2)
)
coVirtualAccessPointConfigEntry.registerAugmentions(
    ("ALVARION-802DOT11-MIB",
     "coDot11AccessPointConfigEntry")
)
coDot11AccessPointConfigEntry.setIndexNames(*coVirtualAccessPointConfigEntry.getIndexNames())
coVirtualAccessPointConfigEntry.registerAugmentions(
    ("ALVARION-802DOT11-MIB",
     "coDot11WEPDefaultKeysEntry")
)
coDot11WEPDefaultKeysEntry.setIndexNames(*coVirtualAccessPointConfigEntry.getIndexNames())
coVirtualAccessPointConfigEntry.registerAugmentions(
    ("ALVARION-802DOT11-MIB",
     "coDot11PrivacyEntry")
)
coDot11PrivacyEntry.setIndexNames(*coVirtualAccessPointConfigEntry.getIndexNames())
coVirtualAccessPointConfigEntry.registerAugmentions(
    ("ALVARION-802DOT11-MIB",
     "coDot11RSNAStatsEntry")
)
coDot11RSNAStatsEntry.setIndexNames(*coVirtualAccessPointConfigEntry.getIndexNames())

# Managed Objects groups

coDot11APBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 1)
)
coDot11APBaseGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11RelayBetweenStation"),
        ("ALVARION-802DOT11-MIB", "coDot11PrivacyOptionImplemented"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAOptionImplemented"),
        ("ALVARION-802DOT11-MIB", "coDot11BeaconPeriod"),
        ("ALVARION-802DOT11-MIB", "coDot11DTIMPeriod"),
        ("ALVARION-802DOT11-MIB", "coDot11NumberOfUsers"),
        ("ALVARION-802DOT11-MIB", "coDot11AddToAssociationNotification"),
        ("ALVARION-802DOT11-MIB", "coDot11PhyTxPowerAdminLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11PhyTxPowerOperLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11BSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11AdminMinimumDataRate"),
        ("ALVARION-802DOT11-MIB", "coDot11AdminMaximumDataRate"))
)
if mibBuilder.loadTexts:
    coDot11APBaseGroup.setStatus("current")

coDot11APPrivacyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 2)
)
coDot11APPrivacyGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11PrivacyInvoked"),
        ("ALVARION-802DOT11-MIB", "coDot11ExcludeUnencrypted"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPICVErrorCount"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPExcludedCount"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPDefaultKeyID"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPDefaultKey1Value"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPDefaultKey2Value"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPDefaultKey3Value"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPDefaultKey4Value"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAEnabled"))
)
if mibBuilder.loadTexts:
    coDot11APPrivacyGroup.setStatus("current")

coDot11MACBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 3)
)
coDot11MACBaseGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11MACAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11RTSThreshold"),
        ("ALVARION-802DOT11-MIB", "coDot11ShortRetryLimit"),
        ("ALVARION-802DOT11-MIB", "coDot11LongRetryLimit"),
        ("ALVARION-802DOT11-MIB", "coDot11FragmentationThreshold"),
        ("ALVARION-802DOT11-MIB", "coDot11MaxTransmitMSDULifetime"),
        ("ALVARION-802DOT11-MIB", "coDot11MaxReceiveLifetime"),
        ("ALVARION-802DOT11-MIB", "coDot11ManufacturerID"),
        ("ALVARION-802DOT11-MIB", "coDot11ProductID"),
        ("ALVARION-802DOT11-MIB", "coDot11RadioType"))
)
if mibBuilder.loadTexts:
    coDot11MACBaseGroup.setStatus("current")

coDot11MACStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 4)
)
coDot11MACStatisticsGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11RetryCount"),
        ("ALVARION-802DOT11-MIB", "coDot11MultipleRetryCount"))
)
if mibBuilder.loadTexts:
    coDot11MACStatisticsGroup.setStatus("current")

coDot11SmtAuthenticationAlgorithmsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 5)
)
coDot11SmtAuthenticationAlgorithmsGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11AuthenticationAlgorithm"),
        ("ALVARION-802DOT11-MIB", "coDot11AuthenticationAlgorithmsEnable"))
)
if mibBuilder.loadTexts:
    coDot11SmtAuthenticationAlgorithmsGroup.setStatus("current")

coDot11PhyConfigComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 6)
)
coDot11PhyConfigComplianceGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11MinimumSNRLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentSNRLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11Sensitivity"),
        ("ALVARION-802DOT11-MIB", "coDot11PhyAdminStatus"),
        ("ALVARION-802DOT11-MIB", "coDot11PhyOperStatus"),
        ("ALVARION-802DOT11-MIB", "coDot11PHYType"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentRegDomain"),
        ("ALVARION-802DOT11-MIB", "coDot11TempType"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentOperFrequency"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentOperPHYType"),
        ("ALVARION-802DOT11-MIB", "coDot11RadioEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11OperatingMode"),
        ("ALVARION-802DOT11-MIB", "coDot11AutoChannelEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11AutoChannelInterval"),
        ("ALVARION-802DOT11-MIB", "coDot11AutoPowerEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11AutoPowerInterval"))
)
if mibBuilder.loadTexts:
    coDot11PhyConfigComplianceGroup.setStatus("current")

coDot11PhyConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 7)
)
coDot11PhyConfigGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11SNRLevelNotificationEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11SNRLevelNotificationInterval"),
        ("ALVARION-802DOT11-MIB", "coDot11CountryCode"))
)
if mibBuilder.loadTexts:
    coDot11PhyConfigGroup.setStatus("current")

coDot11PhyAntennaComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 8)
)
coDot11PhyAntennaComplianceGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11CurrentTxAntenna"),
        ("ALVARION-802DOT11-MIB", "coDot11DiversitySupport"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentRxAntenna"))
)
if mibBuilder.loadTexts:
    coDot11PhyAntennaComplianceGroup.setStatus("current")

coDot11PhyDSSSComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 9)
)
coDot11PhyDSSSComplianceGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11CurrentChannel"),
        ("ALVARION-802DOT11-MIB", "coDot11CCAModeSupported"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentCCAMode"))
)
if mibBuilder.loadTexts:
    coDot11PhyDSSSComplianceGroup.setStatus("current")

coDot11PhyRegDomainsSupportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 10)
)
coDot11PhyRegDomainsSupportGroup.setObjects(
    ("ALVARION-802DOT11-MIB", "coDot11RegDomainsSupportValue")
)
if mibBuilder.loadTexts:
    coDot11PhyRegDomainsSupportGroup.setStatus("current")

coDot11PhyAntennasListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 11)
)
coDot11PhyAntennasListGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11SupportedTxAntenna"),
        ("ALVARION-802DOT11-MIB", "coDot11SupportedRxAntenna"),
        ("ALVARION-802DOT11-MIB", "coDot11DiversitySelectionRx"))
)
if mibBuilder.loadTexts:
    coDot11PhyAntennasListGroup.setStatus("current")

coDot11PhyRateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 12)
)
coDot11PhyRateGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11SupportedDataRatesTxValue"),
        ("ALVARION-802DOT11-MIB", "coDot11SupportedDataRatesRxValue"))
)
if mibBuilder.loadTexts:
    coDot11PhyRateGroup.setStatus("current")

coDot11CountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 13)
)
coDot11CountersGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11TransmittedFragmentCount"),
        ("ALVARION-802DOT11-MIB", "coDot11MulticastTransmittedFrameCount"),
        ("ALVARION-802DOT11-MIB", "coDot11FailedCount"),
        ("ALVARION-802DOT11-MIB", "coDot11FrameDuplicateCount"),
        ("ALVARION-802DOT11-MIB", "coDot11RTSSuccessCount"),
        ("ALVARION-802DOT11-MIB", "coDot11RTSFailureCount"),
        ("ALVARION-802DOT11-MIB", "coDot11ACKFailureCount"),
        ("ALVARION-802DOT11-MIB", "coDot11ReceivedFragmentCount"),
        ("ALVARION-802DOT11-MIB", "coDot11MulticastReceivedFrameCount"),
        ("ALVARION-802DOT11-MIB", "coDot11FCSErrorCount"),
        ("ALVARION-802DOT11-MIB", "coDot11WEPUndecryptableCount"),
        ("ALVARION-802DOT11-MIB", "coDot11TransmittedFrameCount"))
)
if mibBuilder.loadTexts:
    coDot11CountersGroup.setStatus("current")

coDot11AssociationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 14)
)
coDot11AssociationGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11StationMACAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11StationConnectTime"),
        ("ALVARION-802DOT11-MIB", "coDot11SignalLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11NoiseLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11SNR"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate1"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate2"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate5dot5"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate6"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate9"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate11"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate12"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate18"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate24"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate36"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate48"),
        ("ALVARION-802DOT11-MIB", "coDot11PktsRate54"),
        ("ALVARION-802DOT11-MIB", "coDot11TransmitRate"),
        ("ALVARION-802DOT11-MIB", "coDot11ReceiveRate"),
        ("ALVARION-802DOT11-MIB", "coDot11InPkts"),
        ("ALVARION-802DOT11-MIB", "coDot11OutPkts"),
        ("ALVARION-802DOT11-MIB", "coDot11InOctets"),
        ("ALVARION-802DOT11-MIB", "coDot11OutOctets"),
        ("ALVARION-802DOT11-MIB", "coDot11StationSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11StationName"),
        ("ALVARION-802DOT11-MIB", "coDot11StationIPAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11StationVLAN"),
        ("ALVARION-802DOT11-MIB", "coDot11StationLocalInterface"))
)
if mibBuilder.loadTexts:
    coDot11AssociationGroup.setStatus("current")

coDot11AssociationConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 15)
)
coDot11AssociationConfigGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11AssociationNotificationEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11AssociationNotificationInterval"))
)
if mibBuilder.loadTexts:
    coDot11AssociationConfigGroup.setStatus("current")

coDot11ScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 16)
)
coDot11ScanGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11ScanMacAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanChannel"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanSignalLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanNoiseLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanSNR"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanStatus"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanPHYType"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanInactivityTime"))
)
if mibBuilder.loadTexts:
    coDot11ScanGroup.setStatus("current")

coDot11ScanConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 17)
)
coDot11ScanConfigGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11ScanEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanPeriodicity"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanAuthorizedListURL"),
        ("ALVARION-802DOT11-MIB", "coDot11UnauthorizedAPNotificationEnabled"),
        ("ALVARION-802DOT11-MIB", "coDot11UnauthorizedAPNotificationInterval"))
)
if mibBuilder.loadTexts:
    coDot11ScanConfigGroup.setStatus("current")

coDot11WDSComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 18)
)
coDot11WDSComplianceGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11WDSPortMacAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortCurrentRate"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortSNRLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortTxPackets"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortTxDropped"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortTxErrors"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortRxPackets"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortRxDropped"),
        ("ALVARION-802DOT11-MIB", "coDot11WDSPortRxErrors"))
)
if mibBuilder.loadTexts:
    coDot11WDSComplianceGroup.setStatus("current")

coDot11RSNBase = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 20)
)
coDot11RSNBase.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11RSNAStatsVersion"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsSelectedPairwiseCipher"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsTKIPICVErrors"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsTKIPLocalMICFailures"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsTKIPRemoteMICFailures"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsTKIPCounterMeasuresInvoked"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsCCMPFormatErrors"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsCCMPReplays"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsCCMPDecryptErrors"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStatsTKIPReplays"),
        ("ALVARION-802DOT11-MIB", "coDot11RSNAStats4WayHandshakeFailures"))
)
if mibBuilder.loadTexts:
    coDot11RSNBase.setStatus("current")

coDot11PhyOFDMComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 21)
)
coDot11PhyOFDMComplianceGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11CurrentFrequency"),
        ("ALVARION-802DOT11-MIB", "coDot11TIThreshold"),
        ("ALVARION-802DOT11-MIB", "coDot11FrequencyBandsSupported"))
)
if mibBuilder.loadTexts:
    coDot11PhyOFDMComplianceGroup.setStatus("current")


# Notification objects

coDot11SNRLevelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 5, 0, 1)
)
coDot11SNRLevelNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ALVARION-VIRTUAL-AP-MIB", "coVirtualApSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11CurrentSNRLevel"))
)
if mibBuilder.loadTexts:
    coDot11SNRLevelNotification.setStatus(
        "current"
    )

coDot11AssociationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 5, 0, 2)
)
coDot11AssociationNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ALVARION-802DOT11-MIB", "coDot11StationName"),
        ("ALVARION-802DOT11-MIB", "coDot11StationSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11StationIPAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11StationMACAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11SignalLevel"),
        ("ALVARION-802DOT11-MIB", "coDot11SNR"),
        ("ALVARION-802DOT11-MIB", "coDot11TransmitRate"),
        ("ALVARION-802DOT11-MIB", "coDot11NumberOfUsers"))
)
if mibBuilder.loadTexts:
    coDot11AssociationNotification.setStatus(
        "current"
    )

coDot11UnauthorizedAPNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 5, 0, 3)
)
coDot11UnauthorizedAPNotification.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanSSID"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanMacAddress"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanChannel"),
        ("ALVARION-802DOT11-MIB", "coDot11ScanPHYType"))
)
if mibBuilder.loadTexts:
    coDot11UnauthorizedAPNotification.setStatus(
        "current"
    )


# Notifications groups

coDot11NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 1, 19)
)
coDot11NotificationGroup.setObjects(
      *(("ALVARION-802DOT11-MIB", "coDot11SNRLevelNotification"),
        ("ALVARION-802DOT11-MIB", "coDot11AssociationNotification"),
        ("ALVARION-802DOT11-MIB", "coDot11UnauthorizedAPNotification"))
)
if mibBuilder.loadTexts:
    coDot11NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

coDot11Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    coDot11Compliance.setStatus(
        "current"
    )

coDot11RSNCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12394, 1, 10, 5, 4, 6, 2, 2)
)
if mibBuilder.loadTexts:
    coDot11RSNCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALVARION-802DOT11-MIB",
    **{"WEPKeytype": WEPKeytype,
       "alvarion802dot11": alvarion802dot11,
       "coDot11ap": coDot11ap,
       "coDot11AccessPointConfigTable": coDot11AccessPointConfigTable,
       "coDot11AccessPointConfigEntry": coDot11AccessPointConfigEntry,
       "coDot11RelayBetweenStation": coDot11RelayBetweenStation,
       "coDot11BeaconPeriod": coDot11BeaconPeriod,
       "coDot11DTIMPeriod": coDot11DTIMPeriod,
       "coDot11PrivacyOptionImplemented": coDot11PrivacyOptionImplemented,
       "coDot11RSNAOptionImplemented": coDot11RSNAOptionImplemented,
       "coDot11NumberOfUsers": coDot11NumberOfUsers,
       "coDot11AddToAssociationNotification": coDot11AddToAssociationNotification,
       "coDot11PhyTxPowerAdminLevel": coDot11PhyTxPowerAdminLevel,
       "coDot11PhyTxPowerOperLevel": coDot11PhyTxPowerOperLevel,
       "coDot11CurrentSNRLevel": coDot11CurrentSNRLevel,
       "coDot11BSSID": coDot11BSSID,
       "coDot11AdminMinimumDataRate": coDot11AdminMinimumDataRate,
       "coDot11AdminMaximumDataRate": coDot11AdminMaximumDataRate,
       "coDot11AuthenticationAlgorithmsTable": coDot11AuthenticationAlgorithmsTable,
       "coDot11AuthenticationAlgorithmsEntry": coDot11AuthenticationAlgorithmsEntry,
       "coDot11AuthenticationAlgorithmsIndex": coDot11AuthenticationAlgorithmsIndex,
       "coDot11AuthenticationAlgorithm": coDot11AuthenticationAlgorithm,
       "coDot11AuthenticationAlgorithmsEnable": coDot11AuthenticationAlgorithmsEnable,
       "coDot11WEPDefaultKeysTable": coDot11WEPDefaultKeysTable,
       "coDot11WEPDefaultKeysEntry": coDot11WEPDefaultKeysEntry,
       "coDot11WEPDefaultKey1Value": coDot11WEPDefaultKey1Value,
       "coDot11WEPDefaultKey2Value": coDot11WEPDefaultKey2Value,
       "coDot11WEPDefaultKey3Value": coDot11WEPDefaultKey3Value,
       "coDot11WEPDefaultKey4Value": coDot11WEPDefaultKey4Value,
       "coDot11PrivacyTable": coDot11PrivacyTable,
       "coDot11PrivacyEntry": coDot11PrivacyEntry,
       "coDot11PrivacyInvoked": coDot11PrivacyInvoked,
       "coDot11WEPDefaultKeyID": coDot11WEPDefaultKeyID,
       "coDot11ExcludeUnencrypted": coDot11ExcludeUnencrypted,
       "coDot11WEPICVErrorCount": coDot11WEPICVErrorCount,
       "coDot11WEPExcludedCount": coDot11WEPExcludedCount,
       "coDot11RSNAEnabled": coDot11RSNAEnabled,
       "coDot11AssociationTable": coDot11AssociationTable,
       "coDot11AssociationEntry": coDot11AssociationEntry,
       "coDot11AssociationIndex": coDot11AssociationIndex,
       "coDot11StationMACAddress": coDot11StationMACAddress,
       "coDot11StationConnectTime": coDot11StationConnectTime,
       "coDot11SignalLevel": coDot11SignalLevel,
       "coDot11NoiseLevel": coDot11NoiseLevel,
       "coDot11SNR": coDot11SNR,
       "coDot11PktsRate1": coDot11PktsRate1,
       "coDot11PktsRate2": coDot11PktsRate2,
       "coDot11PktsRate5dot5": coDot11PktsRate5dot5,
       "coDot11PktsRate11": coDot11PktsRate11,
       "coDot11PktsRate6": coDot11PktsRate6,
       "coDot11PktsRate9": coDot11PktsRate9,
       "coDot11PktsRate12": coDot11PktsRate12,
       "coDot11PktsRate18": coDot11PktsRate18,
       "coDot11PktsRate24": coDot11PktsRate24,
       "coDot11PktsRate36": coDot11PktsRate36,
       "coDot11PktsRate48": coDot11PktsRate48,
       "coDot11PktsRate54": coDot11PktsRate54,
       "coDot11TransmitRate": coDot11TransmitRate,
       "coDot11ReceiveRate": coDot11ReceiveRate,
       "coDot11InPkts": coDot11InPkts,
       "coDot11OutPkts": coDot11OutPkts,
       "coDot11InOctets": coDot11InOctets,
       "coDot11OutOctets": coDot11OutOctets,
       "coDot11StationSSID": coDot11StationSSID,
       "coDot11StationName": coDot11StationName,
       "coDot11StationIPAddress": coDot11StationIPAddress,
       "coDot11StationVLAN": coDot11StationVLAN,
       "coDot11StationLocalInterface": coDot11StationLocalInterface,
       "coDot11WDSPortTable": coDot11WDSPortTable,
       "coDot11WDSPortEntry": coDot11WDSPortEntry,
       "coDot11WDSPortIndex": coDot11WDSPortIndex,
       "coDot11WDSPortMacAddress": coDot11WDSPortMacAddress,
       "coDot11WDSPortCurrentRate": coDot11WDSPortCurrentRate,
       "coDot11WDSPortSNRLevel": coDot11WDSPortSNRLevel,
       "coDot11WDSPortTxPackets": coDot11WDSPortTxPackets,
       "coDot11WDSPortTxDropped": coDot11WDSPortTxDropped,
       "coDot11WDSPortTxErrors": coDot11WDSPortTxErrors,
       "coDot11WDSPortRxPackets": coDot11WDSPortRxPackets,
       "coDot11WDSPortRxDropped": coDot11WDSPortRxDropped,
       "coDot11WDSPortRxErrors": coDot11WDSPortRxErrors,
       "coDot11ScanTable": coDot11ScanTable,
       "coDot11ScanEntry": coDot11ScanEntry,
       "coDot11ScanIndex": coDot11ScanIndex,
       "coDot11ScanMacAddress": coDot11ScanMacAddress,
       "coDot11ScanChannel": coDot11ScanChannel,
       "coDot11ScanSSID": coDot11ScanSSID,
       "coDot11ScanSignalLevel": coDot11ScanSignalLevel,
       "coDot11ScanNoiseLevel": coDot11ScanNoiseLevel,
       "coDot11ScanSNR": coDot11ScanSNR,
       "coDot11ScanStatus": coDot11ScanStatus,
       "coDot11ScanPHYType": coDot11ScanPHYType,
       "coDot11ScanInactivityTime": coDot11ScanInactivityTime,
       "coDot11ScanEnabled": coDot11ScanEnabled,
       "coDot11ScanPeriodicity": coDot11ScanPeriodicity,
       "coDot11ScanAuthorizedListURL": coDot11ScanAuthorizedListURL,
       "coDot11UnauthorizedAPNotificationEnabled": coDot11UnauthorizedAPNotificationEnabled,
       "coDot11UnauthorizedAPNotificationInterval": coDot11UnauthorizedAPNotificationInterval,
       "coDot11AssociationNotificationEnabled": coDot11AssociationNotificationEnabled,
       "coDot11AssociationNotificationInterval": coDot11AssociationNotificationInterval,
       "coDot11mac": coDot11mac,
       "coDot11OperationTable": coDot11OperationTable,
       "coDot11OperationEntry": coDot11OperationEntry,
       "coDot11MACAddress": coDot11MACAddress,
       "coDot11RTSThreshold": coDot11RTSThreshold,
       "coDot11ShortRetryLimit": coDot11ShortRetryLimit,
       "coDot11LongRetryLimit": coDot11LongRetryLimit,
       "coDot11FragmentationThreshold": coDot11FragmentationThreshold,
       "coDot11MaxTransmitMSDULifetime": coDot11MaxTransmitMSDULifetime,
       "coDot11MaxReceiveLifetime": coDot11MaxReceiveLifetime,
       "coDot11ManufacturerID": coDot11ManufacturerID,
       "coDot11ProductID": coDot11ProductID,
       "coDot11RadioType": coDot11RadioType,
       "coDot11CountersTable": coDot11CountersTable,
       "coDot11CountersEntry": coDot11CountersEntry,
       "coDot11TransmittedFragmentCount": coDot11TransmittedFragmentCount,
       "coDot11MulticastTransmittedFrameCount": coDot11MulticastTransmittedFrameCount,
       "coDot11FailedCount": coDot11FailedCount,
       "coDot11RetryCount": coDot11RetryCount,
       "coDot11MultipleRetryCount": coDot11MultipleRetryCount,
       "coDot11FrameDuplicateCount": coDot11FrameDuplicateCount,
       "coDot11RTSSuccessCount": coDot11RTSSuccessCount,
       "coDot11RTSFailureCount": coDot11RTSFailureCount,
       "coDot11ACKFailureCount": coDot11ACKFailureCount,
       "coDot11ReceivedFragmentCount": coDot11ReceivedFragmentCount,
       "coDot11MulticastReceivedFrameCount": coDot11MulticastReceivedFrameCount,
       "coDot11FCSErrorCount": coDot11FCSErrorCount,
       "coDot11TransmittedFrameCount": coDot11TransmittedFrameCount,
       "coDot11WEPUndecryptableCount": coDot11WEPUndecryptableCount,
       "coDot11phy": coDot11phy,
       "coDot11PhyOperationTable": coDot11PhyOperationTable,
       "coDot11PhyOperationEntry": coDot11PhyOperationEntry,
       "coDot11PHYType": coDot11PHYType,
       "coDot11CurrentRegDomain": coDot11CurrentRegDomain,
       "coDot11TempType": coDot11TempType,
       "coDot11CurrentOperFrequency": coDot11CurrentOperFrequency,
       "coDot11CurrentOperPHYType": coDot11CurrentOperPHYType,
       "coDot11Sensitivity": coDot11Sensitivity,
       "coDot11RadioEnabled": coDot11RadioEnabled,
       "coDot11OperatingMode": coDot11OperatingMode,
       "coDot11AutoChannelEnabled": coDot11AutoChannelEnabled,
       "coDot11AutoChannelInterval": coDot11AutoChannelInterval,
       "coDot11AutoPowerEnabled": coDot11AutoPowerEnabled,
       "coDot11AutoPowerInterval": coDot11AutoPowerInterval,
       "coDot11PhyAntennaTable": coDot11PhyAntennaTable,
       "coDot11PhyAntennaEntry": coDot11PhyAntennaEntry,
       "coDot11CurrentTxAntenna": coDot11CurrentTxAntenna,
       "coDot11DiversitySupport": coDot11DiversitySupport,
       "coDot11CurrentRxAntenna": coDot11CurrentRxAntenna,
       "coDot11PhyConfigTable": coDot11PhyConfigTable,
       "coDot11PhyConfigEntry": coDot11PhyConfigEntry,
       "coDot11PhyAdminStatus": coDot11PhyAdminStatus,
       "coDot11PhyOperStatus": coDot11PhyOperStatus,
       "coDot11PhyDSSSTable": coDot11PhyDSSSTable,
       "coDot11PhyDSSSEntry": coDot11PhyDSSSEntry,
       "coDot11CurrentChannel": coDot11CurrentChannel,
       "coDot11CCAModeSupported": coDot11CCAModeSupported,
       "coDot11CurrentCCAMode": coDot11CurrentCCAMode,
       "coDot11RegDomainsSupportedTable": coDot11RegDomainsSupportedTable,
       "coDot11RegDomainsSupportedEntry": coDot11RegDomainsSupportedEntry,
       "coDot11RegDomainsSupportIndex": coDot11RegDomainsSupportIndex,
       "coDot11RegDomainsSupportValue": coDot11RegDomainsSupportValue,
       "coDot11AntennasListTable": coDot11AntennasListTable,
       "coDot11AntennasListEntry": coDot11AntennasListEntry,
       "coDot11AntennaListIndex": coDot11AntennaListIndex,
       "coDot11SupportedTxAntenna": coDot11SupportedTxAntenna,
       "coDot11SupportedRxAntenna": coDot11SupportedRxAntenna,
       "coDot11DiversitySelectionRx": coDot11DiversitySelectionRx,
       "coDot11SupportedDataRatesTxTable": coDot11SupportedDataRatesTxTable,
       "coDot11SupportedDataRatesTxEntry": coDot11SupportedDataRatesTxEntry,
       "coDot11SupportedDataRatesTxIndex": coDot11SupportedDataRatesTxIndex,
       "coDot11SupportedDataRatesTxValue": coDot11SupportedDataRatesTxValue,
       "coDot11SupportedDataRatesRxTable": coDot11SupportedDataRatesRxTable,
       "coDot11SupportedDataRatesRxEntry": coDot11SupportedDataRatesRxEntry,
       "coDot11SupportedDataRatesRxIndex": coDot11SupportedDataRatesRxIndex,
       "coDot11SupportedDataRatesRxValue": coDot11SupportedDataRatesRxValue,
       "coDot11PhyOFDMTable": coDot11PhyOFDMTable,
       "coDot11PhyOFDMEntry": coDot11PhyOFDMEntry,
       "coDot11CurrentFrequency": coDot11CurrentFrequency,
       "coDot11TIThreshold": coDot11TIThreshold,
       "coDot11FrequencyBandsSupported": coDot11FrequencyBandsSupported,
       "coDot11MinimumSNRLevel": coDot11MinimumSNRLevel,
       "coDot11SNRLevelNotificationEnabled": coDot11SNRLevelNotificationEnabled,
       "coDot11SNRLevelNotificationInterval": coDot11SNRLevelNotificationInterval,
       "coDot11CountryCode": coDot11CountryCode,
       "coDot11RSNAStatsTable": coDot11RSNAStatsTable,
       "coDot11RSNAStatsEntry": coDot11RSNAStatsEntry,
       "coDot11RSNAStatsVersion": coDot11RSNAStatsVersion,
       "coDot11RSNAStatsSelectedPairwiseCipher": coDot11RSNAStatsSelectedPairwiseCipher,
       "coDot11RSNAStatsTKIPICVErrors": coDot11RSNAStatsTKIPICVErrors,
       "coDot11RSNAStatsTKIPLocalMICFailures": coDot11RSNAStatsTKIPLocalMICFailures,
       "coDot11RSNAStatsTKIPRemoteMICFailures": coDot11RSNAStatsTKIPRemoteMICFailures,
       "coDot11RSNAStatsTKIPCounterMeasuresInvoked": coDot11RSNAStatsTKIPCounterMeasuresInvoked,
       "coDot11RSNAStatsCCMPFormatErrors": coDot11RSNAStatsCCMPFormatErrors,
       "coDot11RSNAStatsCCMPReplays": coDot11RSNAStatsCCMPReplays,
       "coDot11RSNAStatsCCMPDecryptErrors": coDot11RSNAStatsCCMPDecryptErrors,
       "coDot11RSNAStatsTKIPReplays": coDot11RSNAStatsTKIPReplays,
       "coDot11RSNAStats4WayHandshakeFailures": coDot11RSNAStats4WayHandshakeFailures,
       "coDot11ManagementMIBNotificationPrefix": coDot11ManagementMIBNotificationPrefix,
       "coDot11ManagementMIBNotifications": coDot11ManagementMIBNotifications,
       "coDot11SNRLevelNotification": coDot11SNRLevelNotification,
       "coDot11AssociationNotification": coDot11AssociationNotification,
       "coDot11UnauthorizedAPNotification": coDot11UnauthorizedAPNotification,
       "coDot11Conformance": coDot11Conformance,
       "coDot11Groups": coDot11Groups,
       "coDot11APBaseGroup": coDot11APBaseGroup,
       "coDot11APPrivacyGroup": coDot11APPrivacyGroup,
       "coDot11MACBaseGroup": coDot11MACBaseGroup,
       "coDot11MACStatisticsGroup": coDot11MACStatisticsGroup,
       "coDot11SmtAuthenticationAlgorithmsGroup": coDot11SmtAuthenticationAlgorithmsGroup,
       "coDot11PhyConfigComplianceGroup": coDot11PhyConfigComplianceGroup,
       "coDot11PhyConfigGroup": coDot11PhyConfigGroup,
       "coDot11PhyAntennaComplianceGroup": coDot11PhyAntennaComplianceGroup,
       "coDot11PhyDSSSComplianceGroup": coDot11PhyDSSSComplianceGroup,
       "coDot11PhyRegDomainsSupportGroup": coDot11PhyRegDomainsSupportGroup,
       "coDot11PhyAntennasListGroup": coDot11PhyAntennasListGroup,
       "coDot11PhyRateGroup": coDot11PhyRateGroup,
       "coDot11CountersGroup": coDot11CountersGroup,
       "coDot11AssociationGroup": coDot11AssociationGroup,
       "coDot11AssociationConfigGroup": coDot11AssociationConfigGroup,
       "coDot11ScanGroup": coDot11ScanGroup,
       "coDot11ScanConfigGroup": coDot11ScanConfigGroup,
       "coDot11WDSComplianceGroup": coDot11WDSComplianceGroup,
       "coDot11NotificationGroup": coDot11NotificationGroup,
       "coDot11RSNBase": coDot11RSNBase,
       "coDot11PhyOFDMComplianceGroup": coDot11PhyOFDMComplianceGroup,
       "coDot11Compliances": coDot11Compliances,
       "coDot11Compliance": coDot11Compliance,
       "coDot11RSNCompliance": coDot11RSNCompliance}
)
