# SNMP MIB module (RUCKUS-WLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RUCKUS-WLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:51 2024
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
 IpAddress,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "IpAddress",
    "ifIndex")

(ruckusCommonWLANModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonWLANModule")

(RuckusAdminStatus,
 RuckusRadioMode,
 RuckusSSID,
 RuckusWEPKey,
 RuckusWPAPassPhrase,
 RuckusdB) = mibBuilder.importSymbols(
    "RUCKUS-TC-MIB",
    "RuckusAdminStatus",
    "RuckusRadioMode",
    "RuckusSSID",
    "RuckusWEPKey",
    "RuckusWPAPassPhrase",
    "RuckusdB")

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

ruckusWLANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusWLANObjects_ObjectIdentity = ObjectIdentity
ruckusWLANObjects = _RuckusWLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1)
)
_RuckusWLANInfo_ObjectIdentity = ObjectIdentity
ruckusWLANInfo = _RuckusWLANInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1)
)
_RuckusWLANTable_Object = MibTable
ruckusWLANTable = _RuckusWLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusWLANTable.setStatus("current")
_RuckusWLANEntry_Object = MibTableRow
ruckusWLANEntry = _RuckusWLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1)
)
ruckusWLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANEntry.setStatus("current")
_RuckusWLANSSID_Type = RuckusSSID
_RuckusWLANSSID_Object = MibTableColumn
ruckusWLANSSID = _RuckusWLANSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 1),
    _RuckusWLANSSID_Type()
)
ruckusWLANSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANSSID.setStatus("current")
_RuckusWLANBSSID_Type = MacAddress
_RuckusWLANBSSID_Object = MibTableColumn
ruckusWLANBSSID = _RuckusWLANBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 2),
    _RuckusWLANBSSID_Type()
)
ruckusWLANBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANBSSID.setStatus("current")


class _RuckusWLANBSSType_Type(Integer32):
    """Custom type ruckusWLANBSSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("independent", 3),
          ("master", 2),
          ("station", 1))
    )


_RuckusWLANBSSType_Type.__name__ = "Integer32"
_RuckusWLANBSSType_Object = MibTableColumn
ruckusWLANBSSType = _RuckusWLANBSSType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 3),
    _RuckusWLANBSSType_Type()
)
ruckusWLANBSSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANBSSType.setStatus("current")


class _RuckusWLANOperationalRateSet_Type(OctetString):
    """Custom type ruckusWLANOperationalRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RuckusWLANOperationalRateSet_Type.__name__ = "OctetString"
_RuckusWLANOperationalRateSet_Object = MibTableColumn
ruckusWLANOperationalRateSet = _RuckusWLANOperationalRateSet_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 4),
    _RuckusWLANOperationalRateSet_Type()
)
ruckusWLANOperationalRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANOperationalRateSet.setStatus("current")


class _RuckusWLANBeaconPeriod_Type(Integer32):
    """Custom type ruckusWLANBeaconPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_RuckusWLANBeaconPeriod_Type.__name__ = "Integer32"
_RuckusWLANBeaconPeriod_Object = MibTableColumn
ruckusWLANBeaconPeriod = _RuckusWLANBeaconPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 5),
    _RuckusWLANBeaconPeriod_Type()
)
ruckusWLANBeaconPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANBeaconPeriod.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANBeaconPeriod.setUnits("milli seconds")


class _RuckusWLANDTIMPeriod_Type(Integer32):
    """Custom type ruckusWLANDTIMPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RuckusWLANDTIMPeriod_Type.__name__ = "Integer32"
_RuckusWLANDTIMPeriod_Object = MibTableColumn
ruckusWLANDTIMPeriod = _RuckusWLANDTIMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 6),
    _RuckusWLANDTIMPeriod_Type()
)
ruckusWLANDTIMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANDTIMPeriod.setStatus("current")


class _RuckusWLANRTSThreshold_Type(Integer32):
    """Custom type ruckusWLANRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_RuckusWLANRTSThreshold_Type.__name__ = "Integer32"
_RuckusWLANRTSThreshold_Object = MibTableColumn
ruckusWLANRTSThreshold = _RuckusWLANRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 7),
    _RuckusWLANRTSThreshold_Type()
)
ruckusWLANRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANRTSThreshold.setStatus("current")


class _RuckusWLANFragmentationThreshold_Type(Integer32):
    """Custom type ruckusWLANFragmentationThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_RuckusWLANFragmentationThreshold_Type.__name__ = "Integer32"
_RuckusWLANFragmentationThreshold_Object = MibTableColumn
ruckusWLANFragmentationThreshold = _RuckusWLANFragmentationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 8),
    _RuckusWLANFragmentationThreshold_Type()
)
ruckusWLANFragmentationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANFragmentationThreshold.setStatus("current")
_RuckusWLANRadioMode_Type = RuckusRadioMode
_RuckusWLANRadioMode_Object = MibTableColumn
ruckusWLANRadioMode = _RuckusWLANRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 9),
    _RuckusWLANRadioMode_Type()
)
ruckusWLANRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANRadioMode.setStatus("current")


class _RuckusWLANChannel_Type(Integer32):
    """Custom type ruckusWLANChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_RuckusWLANChannel_Type.__name__ = "Integer32"
_RuckusWLANChannel_Object = MibTableColumn
ruckusWLANChannel = _RuckusWLANChannel_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 10),
    _RuckusWLANChannel_Type()
)
ruckusWLANChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANChannel.setStatus("current")


class _RuckusWLANWDSEnable_Type(TruthValue):
    """Custom type ruckusWLANWDSEnable based on TruthValue"""


_RuckusWLANWDSEnable_Object = MibTableColumn
ruckusWLANWDSEnable = _RuckusWLANWDSEnable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 11),
    _RuckusWLANWDSEnable_Type()
)
ruckusWLANWDSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWDSEnable.setStatus("current")


class _RuckusWLANAdminStatus_Type(Integer32):
    """Custom type ruckusWLANAdminStatus based on Integer32"""
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


_RuckusWLANAdminStatus_Type.__name__ = "Integer32"
_RuckusWLANAdminStatus_Object = MibTableColumn
ruckusWLANAdminStatus = _RuckusWLANAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 12),
    _RuckusWLANAdminStatus_Type()
)
ruckusWLANAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANAdminStatus.setStatus("current")


class _RuckusWLANProtectionMode_Type(Integer32):
    """Custom type ruckusWLANProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsOnly", 2),
          ("ctsRts", 3),
          ("none", 1))
    )


_RuckusWLANProtectionMode_Type.__name__ = "Integer32"
_RuckusWLANProtectionMode_Object = MibTableColumn
ruckusWLANProtectionMode = _RuckusWLANProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 13),
    _RuckusWLANProtectionMode_Type()
)
ruckusWLANProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANProtectionMode.setStatus("current")


class _RuckusWLANName_Type(OctetString):
    """Custom type ruckusWLANName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_RuckusWLANName_Type.__name__ = "OctetString"
_RuckusWLANName_Object = MibTableColumn
ruckusWLANName = _RuckusWLANName_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 14),
    _RuckusWLANName_Type()
)
ruckusWLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANName.setStatus("current")


class _RuckusWLANSSIDBcastDisable_Type(TruthValue):
    """Custom type ruckusWLANSSIDBcastDisable based on TruthValue"""


_RuckusWLANSSIDBcastDisable_Object = MibTableColumn
ruckusWLANSSIDBcastDisable = _RuckusWLANSSIDBcastDisable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 15),
    _RuckusWLANSSIDBcastDisable_Type()
)
ruckusWLANSSIDBcastDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANSSIDBcastDisable.setStatus("current")


class _RuckusWLANVlanID_Type(Integer32):
    """Custom type ruckusWLANVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RuckusWLANVlanID_Type.__name__ = "Integer32"
_RuckusWLANVlanID_Object = MibTableColumn
ruckusWLANVlanID = _RuckusWLANVlanID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 16),
    _RuckusWLANVlanID_Type()
)
ruckusWLANVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANVlanID.setStatus("current")


class _RuckusWLANIGMPSnooping_Type(Integer32):
    """Custom type ruckusWLANIGMPSnooping based on Integer32"""
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


_RuckusWLANIGMPSnooping_Type.__name__ = "Integer32"
_RuckusWLANIGMPSnooping_Object = MibTableColumn
ruckusWLANIGMPSnooping = _RuckusWLANIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 1, 1, 25),
    _RuckusWLANIGMPSnooping_Type()
)
ruckusWLANIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANIGMPSnooping.setStatus("current")
_RuckusWLANSuppDataRatesTxTable_Object = MibTable
ruckusWLANSuppDataRatesTxTable = _RuckusWLANSuppDataRatesTxTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesTxTable.setStatus("current")
_RuckusWLANSuppDataRatesTxEntry_Object = MibTableRow
ruckusWLANSuppDataRatesTxEntry = _RuckusWLANSuppDataRatesTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 2, 1)
)
ruckusWLANSuppDataRatesTxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANSuppDataRatesTxIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesTxEntry.setStatus("current")
_RuckusWLANSuppDataRatesTxIndex_Type = Integer32
_RuckusWLANSuppDataRatesTxIndex_Object = MibTableColumn
ruckusWLANSuppDataRatesTxIndex = _RuckusWLANSuppDataRatesTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 2, 1, 1),
    _RuckusWLANSuppDataRatesTxIndex_Type()
)
ruckusWLANSuppDataRatesTxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesTxIndex.setStatus("current")
_RuckusWLANSuppDataRatesTxValue_Type = DisplayString
_RuckusWLANSuppDataRatesTxValue_Object = MibTableColumn
ruckusWLANSuppDataRatesTxValue = _RuckusWLANSuppDataRatesTxValue_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 2, 1, 2),
    _RuckusWLANSuppDataRatesTxValue_Type()
)
ruckusWLANSuppDataRatesTxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesTxValue.setStatus("current")
_RuckusWLANSuppDataRatesRxTable_Object = MibTable
ruckusWLANSuppDataRatesRxTable = _RuckusWLANSuppDataRatesRxTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesRxTable.setStatus("current")
_RuckusWLANSuppDataRatesRxEntry_Object = MibTableRow
ruckusWLANSuppDataRatesRxEntry = _RuckusWLANSuppDataRatesRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 3, 1)
)
ruckusWLANSuppDataRatesRxEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANSuppDataRatesRxIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesRxEntry.setStatus("current")
_RuckusWLANSuppDataRatesRxIndex_Type = Integer32
_RuckusWLANSuppDataRatesRxIndex_Object = MibTableColumn
ruckusWLANSuppDataRatesRxIndex = _RuckusWLANSuppDataRatesRxIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 3, 1, 1),
    _RuckusWLANSuppDataRatesRxIndex_Type()
)
ruckusWLANSuppDataRatesRxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesRxIndex.setStatus("current")
_RuckusWLANSuppDataRatesRxValue_Type = DisplayString
_RuckusWLANSuppDataRatesRxValue_Object = MibTableColumn
ruckusWLANSuppDataRatesRxValue = _RuckusWLANSuppDataRatesRxValue_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 3, 1, 2),
    _RuckusWLANSuppDataRatesRxValue_Type()
)
ruckusWLANSuppDataRatesRxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANSuppDataRatesRxValue.setStatus("current")
_RuckusWLANStatsTable_Object = MibTable
ruckusWLANStatsTable = _RuckusWLANStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ruckusWLANStatsTable.setStatus("current")
_RuckusWLANStatsEntry_Object = MibTableRow
ruckusWLANStatsEntry = _RuckusWLANStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1)
)
ruckusWLANStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANStatsEntry.setStatus("current")
_RuckusWLANStatsSSID_Type = RuckusSSID
_RuckusWLANStatsSSID_Object = MibTableColumn
ruckusWLANStatsSSID = _RuckusWLANStatsSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 1),
    _RuckusWLANStatsSSID_Type()
)
ruckusWLANStatsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsSSID.setStatus("current")
_RuckusWLANStatsBSSID_Type = MacAddress
_RuckusWLANStatsBSSID_Object = MibTableColumn
ruckusWLANStatsBSSID = _RuckusWLANStatsBSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 2),
    _RuckusWLANStatsBSSID_Type()
)
ruckusWLANStatsBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsBSSID.setStatus("current")
_RuckusWLANStatsNumSta_Type = Counter32
_RuckusWLANStatsNumSta_Object = MibTableColumn
ruckusWLANStatsNumSta = _RuckusWLANStatsNumSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 3),
    _RuckusWLANStatsNumSta_Type()
)
ruckusWLANStatsNumSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumSta.setStatus("current")
_RuckusWLANStatsNumAuthSta_Type = Counter32
_RuckusWLANStatsNumAuthSta_Object = MibTableColumn
ruckusWLANStatsNumAuthSta = _RuckusWLANStatsNumAuthSta_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 4),
    _RuckusWLANStatsNumAuthSta_Type()
)
ruckusWLANStatsNumAuthSta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAuthSta.setStatus("current")
_RuckusWLANStatsNumAuthReq_Type = Counter32
_RuckusWLANStatsNumAuthReq_Object = MibTableColumn
ruckusWLANStatsNumAuthReq = _RuckusWLANStatsNumAuthReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 5),
    _RuckusWLANStatsNumAuthReq_Type()
)
ruckusWLANStatsNumAuthReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAuthReq.setStatus("current")
_RuckusWLANStatsNumAuthResp_Type = Counter32
_RuckusWLANStatsNumAuthResp_Object = MibTableColumn
ruckusWLANStatsNumAuthResp = _RuckusWLANStatsNumAuthResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 6),
    _RuckusWLANStatsNumAuthResp_Type()
)
ruckusWLANStatsNumAuthResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAuthResp.setStatus("current")
_RuckusWLANStatsNumAuthSuccess_Type = Counter32
_RuckusWLANStatsNumAuthSuccess_Object = MibTableColumn
ruckusWLANStatsNumAuthSuccess = _RuckusWLANStatsNumAuthSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 7),
    _RuckusWLANStatsNumAuthSuccess_Type()
)
ruckusWLANStatsNumAuthSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAuthSuccess.setStatus("current")
_RuckusWLANStatsNumAuthFail_Type = Counter32
_RuckusWLANStatsNumAuthFail_Object = MibTableColumn
ruckusWLANStatsNumAuthFail = _RuckusWLANStatsNumAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 8),
    _RuckusWLANStatsNumAuthFail_Type()
)
ruckusWLANStatsNumAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAuthFail.setStatus("current")
_RuckusWLANStatsNumAssocReq_Type = Counter32
_RuckusWLANStatsNumAssocReq_Object = MibTableColumn
ruckusWLANStatsNumAssocReq = _RuckusWLANStatsNumAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 9),
    _RuckusWLANStatsNumAssocReq_Type()
)
ruckusWLANStatsNumAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAssocReq.setStatus("current")
_RuckusWLANStatsNumAssocResp_Type = Counter32
_RuckusWLANStatsNumAssocResp_Object = MibTableColumn
ruckusWLANStatsNumAssocResp = _RuckusWLANStatsNumAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 10),
    _RuckusWLANStatsNumAssocResp_Type()
)
ruckusWLANStatsNumAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAssocResp.setStatus("current")
_RuckusWLANStatsNumReAssocReq_Type = Counter32
_RuckusWLANStatsNumReAssocReq_Object = MibTableColumn
ruckusWLANStatsNumReAssocReq = _RuckusWLANStatsNumReAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 11),
    _RuckusWLANStatsNumReAssocReq_Type()
)
ruckusWLANStatsNumReAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumReAssocReq.setStatus("current")
_RuckusWLANStatsNumReAssocResp_Type = Counter32
_RuckusWLANStatsNumReAssocResp_Object = MibTableColumn
ruckusWLANStatsNumReAssocResp = _RuckusWLANStatsNumReAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 12),
    _RuckusWLANStatsNumReAssocResp_Type()
)
ruckusWLANStatsNumReAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumReAssocResp.setStatus("current")
_RuckusWLANStatsNumAssocSuccess_Type = Counter32
_RuckusWLANStatsNumAssocSuccess_Object = MibTableColumn
ruckusWLANStatsNumAssocSuccess = _RuckusWLANStatsNumAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 13),
    _RuckusWLANStatsNumAssocSuccess_Type()
)
ruckusWLANStatsNumAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAssocSuccess.setStatus("current")
_RuckusWLANStatsNumAssocFail_Type = Counter32
_RuckusWLANStatsNumAssocFail_Object = MibTableColumn
ruckusWLANStatsNumAssocFail = _RuckusWLANStatsNumAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 14),
    _RuckusWLANStatsNumAssocFail_Type()
)
ruckusWLANStatsNumAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsNumAssocFail.setStatus("current")
_RuckusWLANStatsAssocFailRate_Type = Unsigned32
_RuckusWLANStatsAssocFailRate_Object = MibTableColumn
ruckusWLANStatsAssocFailRate = _RuckusWLANStatsAssocFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 15),
    _RuckusWLANStatsAssocFailRate_Type()
)
ruckusWLANStatsAssocFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsAssocFailRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsAssocFailRate.setUnits("percentage")
_RuckusWLANStatsAuthFailRate_Type = Unsigned32
_RuckusWLANStatsAuthFailRate_Object = MibTableColumn
ruckusWLANStatsAuthFailRate = _RuckusWLANStatsAuthFailRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 16),
    _RuckusWLANStatsAuthFailRate_Type()
)
ruckusWLANStatsAuthFailRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsAuthFailRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsAuthFailRate.setUnits("percentage")
_RuckusWLANStatsAssocSuccessRate_Type = Unsigned32
_RuckusWLANStatsAssocSuccessRate_Object = MibTableColumn
ruckusWLANStatsAssocSuccessRate = _RuckusWLANStatsAssocSuccessRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 17),
    _RuckusWLANStatsAssocSuccessRate_Type()
)
ruckusWLANStatsAssocSuccessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsAssocSuccessRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsAssocSuccessRate.setUnits("percentage")
_RuckusWLANStatsRxDataFrames_Type = Counter32
_RuckusWLANStatsRxDataFrames_Object = MibTableColumn
ruckusWLANStatsRxDataFrames = _RuckusWLANStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 18),
    _RuckusWLANStatsRxDataFrames_Type()
)
ruckusWLANStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDataFrames.setStatus("current")
_RuckusWLANStatsRxMgmtFrames_Type = Counter32
_RuckusWLANStatsRxMgmtFrames_Object = MibTableColumn
ruckusWLANStatsRxMgmtFrames = _RuckusWLANStatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 19),
    _RuckusWLANStatsRxMgmtFrames_Type()
)
ruckusWLANStatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxMgmtFrames.setStatus("current")
_RuckusWLANStatsRxCtrlFrames_Type = Counter32
_RuckusWLANStatsRxCtrlFrames_Object = MibTableColumn
ruckusWLANStatsRxCtrlFrames = _RuckusWLANStatsRxCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 20),
    _RuckusWLANStatsRxCtrlFrames_Type()
)
ruckusWLANStatsRxCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxCtrlFrames.setStatus("current")
_RuckusWLANStatsRxUnicastFrames_Type = Counter32
_RuckusWLANStatsRxUnicastFrames_Object = MibTableColumn
ruckusWLANStatsRxUnicastFrames = _RuckusWLANStatsRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 21),
    _RuckusWLANStatsRxUnicastFrames_Type()
)
ruckusWLANStatsRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxUnicastFrames.setStatus("current")
_RuckusWLANStatsRxMulticastFrames_Type = Counter32
_RuckusWLANStatsRxMulticastFrames_Object = MibTableColumn
ruckusWLANStatsRxMulticastFrames = _RuckusWLANStatsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 22),
    _RuckusWLANStatsRxMulticastFrames_Type()
)
ruckusWLANStatsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxMulticastFrames.setStatus("current")
_RuckusWLANStatsRxBroadcastFrames_Type = Counter32
_RuckusWLANStatsRxBroadcastFrames_Object = MibTableColumn
ruckusWLANStatsRxBroadcastFrames = _RuckusWLANStatsRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 23),
    _RuckusWLANStatsRxBroadcastFrames_Type()
)
ruckusWLANStatsRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxBroadcastFrames.setStatus("current")
_RuckusWLANStatsRxBytes_Type = Counter32
_RuckusWLANStatsRxBytes_Object = MibTableColumn
ruckusWLANStatsRxBytes = _RuckusWLANStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 24),
    _RuckusWLANStatsRxBytes_Type()
)
ruckusWLANStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxBytes.setStatus("current")
_RuckusWLANStatsRxDup_Type = Counter32
_RuckusWLANStatsRxDup_Object = MibTableColumn
ruckusWLANStatsRxDup = _RuckusWLANStatsRxDup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 25),
    _RuckusWLANStatsRxDup_Type()
)
ruckusWLANStatsRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDup.setStatus("current")
_RuckusWLANStatsRxNoPrivacy_Type = Counter32
_RuckusWLANStatsRxNoPrivacy_Object = MibTableColumn
ruckusWLANStatsRxNoPrivacy = _RuckusWLANStatsRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 26),
    _RuckusWLANStatsRxNoPrivacy_Type()
)
ruckusWLANStatsRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxNoPrivacy.setStatus("current")
_RuckusWLANStatsRxWEPFail_Type = Counter32
_RuckusWLANStatsRxWEPFail_Object = MibTableColumn
ruckusWLANStatsRxWEPFail = _RuckusWLANStatsRxWEPFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 27),
    _RuckusWLANStatsRxWEPFail_Type()
)
ruckusWLANStatsRxWEPFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxWEPFail.setStatus("current")
_RuckusWLANStatsRxDecryptCRCError_Type = Counter32
_RuckusWLANStatsRxDecryptCRCError_Object = MibTableColumn
ruckusWLANStatsRxDecryptCRCError = _RuckusWLANStatsRxDecryptCRCError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 28),
    _RuckusWLANStatsRxDecryptCRCError_Type()
)
ruckusWLANStatsRxDecryptCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDecryptCRCError.setStatus("current")
_RuckusWLANStatsRxMICError_Type = Counter32
_RuckusWLANStatsRxMICError_Object = MibTableColumn
ruckusWLANStatsRxMICError = _RuckusWLANStatsRxMICError_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 29),
    _RuckusWLANStatsRxMICError_Type()
)
ruckusWLANStatsRxMICError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxMICError.setStatus("current")
_RuckusWLANStatsRxDrops_Type = Counter32
_RuckusWLANStatsRxDrops_Object = MibTableColumn
ruckusWLANStatsRxDrops = _RuckusWLANStatsRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 30),
    _RuckusWLANStatsRxDrops_Type()
)
ruckusWLANStatsRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDrops.setStatus("current")
_RuckusWLANStatsRxErrors_Type = Counter32
_RuckusWLANStatsRxErrors_Object = MibTableColumn
ruckusWLANStatsRxErrors = _RuckusWLANStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 31),
    _RuckusWLANStatsRxErrors_Type()
)
ruckusWLANStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxErrors.setStatus("current")
_RuckusWLANStatsRxFrames_Type = Counter32
_RuckusWLANStatsRxFrames_Object = MibTableColumn
ruckusWLANStatsRxFrames = _RuckusWLANStatsRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 32),
    _RuckusWLANStatsRxFrames_Type()
)
ruckusWLANStatsRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxFrames.setStatus("current")
_RuckusWLANStatsRxDropRate_Type = Unsigned32
_RuckusWLANStatsRxDropRate_Object = MibTableColumn
ruckusWLANStatsRxDropRate = _RuckusWLANStatsRxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 33),
    _RuckusWLANStatsRxDropRate_Type()
)
ruckusWLANStatsRxDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDropRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsRxDropRate.setUnits("percentage")
_RuckusWLANStatsTxDataFrames_Type = Counter32
_RuckusWLANStatsTxDataFrames_Object = MibTableColumn
ruckusWLANStatsTxDataFrames = _RuckusWLANStatsTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 34),
    _RuckusWLANStatsTxDataFrames_Type()
)
ruckusWLANStatsTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxDataFrames.setStatus("current")
_RuckusWLANStatsTxMgmtFrames_Type = Counter32
_RuckusWLANStatsTxMgmtFrames_Object = MibTableColumn
ruckusWLANStatsTxMgmtFrames = _RuckusWLANStatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 35),
    _RuckusWLANStatsTxMgmtFrames_Type()
)
ruckusWLANStatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxMgmtFrames.setStatus("current")
_RuckusWLANStatsTxUnicastFrames_Type = Counter32
_RuckusWLANStatsTxUnicastFrames_Object = MibTableColumn
ruckusWLANStatsTxUnicastFrames = _RuckusWLANStatsTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 36),
    _RuckusWLANStatsTxUnicastFrames_Type()
)
ruckusWLANStatsTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxUnicastFrames.setStatus("current")
_RuckusWLANStatsTxMulticastFrames_Type = Counter32
_RuckusWLANStatsTxMulticastFrames_Object = MibTableColumn
ruckusWLANStatsTxMulticastFrames = _RuckusWLANStatsTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 37),
    _RuckusWLANStatsTxMulticastFrames_Type()
)
ruckusWLANStatsTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxMulticastFrames.setStatus("current")
_RuckusWLANStatsTxBroadcastFrames_Type = Counter32
_RuckusWLANStatsTxBroadcastFrames_Object = MibTableColumn
ruckusWLANStatsTxBroadcastFrames = _RuckusWLANStatsTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 38),
    _RuckusWLANStatsTxBroadcastFrames_Type()
)
ruckusWLANStatsTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxBroadcastFrames.setStatus("current")
_RuckusWLANStatsTxBytes_Type = Counter32
_RuckusWLANStatsTxBytes_Object = MibTableColumn
ruckusWLANStatsTxBytes = _RuckusWLANStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 39),
    _RuckusWLANStatsTxBytes_Type()
)
ruckusWLANStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxBytes.setStatus("current")
_RuckusWLANStatsTxDrops_Type = Counter32
_RuckusWLANStatsTxDrops_Object = MibTableColumn
ruckusWLANStatsTxDrops = _RuckusWLANStatsTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 40),
    _RuckusWLANStatsTxDrops_Type()
)
ruckusWLANStatsTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxDrops.setStatus("current")
_RuckusWLANStatsTxErrors_Type = Counter32
_RuckusWLANStatsTxErrors_Object = MibTableColumn
ruckusWLANStatsTxErrors = _RuckusWLANStatsTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 41),
    _RuckusWLANStatsTxErrors_Type()
)
ruckusWLANStatsTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxErrors.setStatus("current")
_RuckusWLANStatsTxFrames_Type = Counter32
_RuckusWLANStatsTxFrames_Object = MibTableColumn
ruckusWLANStatsTxFrames = _RuckusWLANStatsTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 42),
    _RuckusWLANStatsTxFrames_Type()
)
ruckusWLANStatsTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsTxFrames.setStatus("current")
_RuckusWLANStatsPeriodRxErrorRate_Type = Unsigned32
_RuckusWLANStatsPeriodRxErrorRate_Object = MibTableColumn
ruckusWLANStatsPeriodRxErrorRate = _RuckusWLANStatsPeriodRxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 43),
    _RuckusWLANStatsPeriodRxErrorRate_Type()
)
ruckusWLANStatsPeriodRxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodRxErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodRxErrorRate.setUnits("percentage")
_RuckusWLANStatsPeriodTxErrorRate_Type = Unsigned32
_RuckusWLANStatsPeriodTxErrorRate_Object = MibTableColumn
ruckusWLANStatsPeriodTxErrorRate = _RuckusWLANStatsPeriodTxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 44),
    _RuckusWLANStatsPeriodTxErrorRate_Type()
)
ruckusWLANStatsPeriodTxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodTxErrorRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodTxErrorRate.setUnits("percentage")
_RuckusWLANStatsPeriodAssocReq_Type = Counter32
_RuckusWLANStatsPeriodAssocReq_Object = MibTableColumn
ruckusWLANStatsPeriodAssocReq = _RuckusWLANStatsPeriodAssocReq_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 45),
    _RuckusWLANStatsPeriodAssocReq_Type()
)
ruckusWLANStatsPeriodAssocReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodAssocReq.setStatus("current")
_RuckusWLANStatsPeriodAssocResp_Type = Counter32
_RuckusWLANStatsPeriodAssocResp_Object = MibTableColumn
ruckusWLANStatsPeriodAssocResp = _RuckusWLANStatsPeriodAssocResp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 46),
    _RuckusWLANStatsPeriodAssocResp_Type()
)
ruckusWLANStatsPeriodAssocResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodAssocResp.setStatus("current")
_RuckusWLANStatsPeriodAssocSuccess_Type = Counter32
_RuckusWLANStatsPeriodAssocSuccess_Object = MibTableColumn
ruckusWLANStatsPeriodAssocSuccess = _RuckusWLANStatsPeriodAssocSuccess_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 1, 4, 1, 47),
    _RuckusWLANStatsPeriodAssocSuccess_Type()
)
ruckusWLANStatsPeriodAssocSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStatsPeriodAssocSuccess.setStatus("current")
_RuckusWLANStaInfo_ObjectIdentity = ObjectIdentity
ruckusWLANStaInfo = _RuckusWLANStaInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2)
)
_RuckusWLANStaStatsTable_Object = MibTable
ruckusWLANStaStatsTable = _RuckusWLANStaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTable.setStatus("current")
_RuckusWLANStaStatsEntry_Object = MibTableRow
ruckusWLANStaStatsEntry = _RuckusWLANStaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1)
)
ruckusWLANStaStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANStaStatsMacAddr"),
)
if mibBuilder.loadTexts:
    ruckusWLANStaStatsEntry.setStatus("current")
_RuckusWLANStaStatsMacAddr_Type = MacAddress
_RuckusWLANStaStatsMacAddr_Object = MibTableColumn
ruckusWLANStaStatsMacAddr = _RuckusWLANStaStatsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 1),
    _RuckusWLANStaStatsMacAddr_Type()
)
ruckusWLANStaStatsMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsMacAddr.setStatus("current")
_RuckusWLANStaStatsSSID_Type = RuckusSSID
_RuckusWLANStaStatsSSID_Object = MibTableColumn
ruckusWLANStaStatsSSID = _RuckusWLANStaStatsSSID_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 2),
    _RuckusWLANStaStatsSSID_Type()
)
ruckusWLANStaStatsSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsSSID.setStatus("current")
_RuckusWLANStaStatsRxDataFrames_Type = Counter32
_RuckusWLANStaStatsRxDataFrames_Object = MibTableColumn
ruckusWLANStaStatsRxDataFrames = _RuckusWLANStaStatsRxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 3),
    _RuckusWLANStaStatsRxDataFrames_Type()
)
ruckusWLANStaStatsRxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxDataFrames.setStatus("current")
_RuckusWLANStaStatsRxMgmtFrames_Type = Counter32
_RuckusWLANStaStatsRxMgmtFrames_Object = MibTableColumn
ruckusWLANStaStatsRxMgmtFrames = _RuckusWLANStaStatsRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 4),
    _RuckusWLANStaStatsRxMgmtFrames_Type()
)
ruckusWLANStaStatsRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxMgmtFrames.setStatus("current")
_RuckusWLANStaStatsRxCtrlFrames_Type = Counter32
_RuckusWLANStaStatsRxCtrlFrames_Object = MibTableColumn
ruckusWLANStaStatsRxCtrlFrames = _RuckusWLANStaStatsRxCtrlFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 5),
    _RuckusWLANStaStatsRxCtrlFrames_Type()
)
ruckusWLANStaStatsRxCtrlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxCtrlFrames.setStatus("current")
_RuckusWLANStaStatsRxUnicastFrames_Type = Counter32
_RuckusWLANStaStatsRxUnicastFrames_Object = MibTableColumn
ruckusWLANStaStatsRxUnicastFrames = _RuckusWLANStaStatsRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 6),
    _RuckusWLANStaStatsRxUnicastFrames_Type()
)
ruckusWLANStaStatsRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxUnicastFrames.setStatus("current")
_RuckusWLANStaStatsRxMulticastFrames_Type = Counter32
_RuckusWLANStaStatsRxMulticastFrames_Object = MibTableColumn
ruckusWLANStaStatsRxMulticastFrames = _RuckusWLANStaStatsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 7),
    _RuckusWLANStaStatsRxMulticastFrames_Type()
)
ruckusWLANStaStatsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxMulticastFrames.setStatus("current")
_RuckusWLANStaStatsRxBytes_Type = Counter32
_RuckusWLANStaStatsRxBytes_Object = MibTableColumn
ruckusWLANStaStatsRxBytes = _RuckusWLANStaStatsRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 8),
    _RuckusWLANStaStatsRxBytes_Type()
)
ruckusWLANStaStatsRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxBytes.setStatus("current")
_RuckusWLANStaStatsRxDup_Type = Counter32
_RuckusWLANStaStatsRxDup_Object = MibTableColumn
ruckusWLANStaStatsRxDup = _RuckusWLANStaStatsRxDup_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 9),
    _RuckusWLANStaStatsRxDup_Type()
)
ruckusWLANStaStatsRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxDup.setStatus("current")
_RuckusWLANStaStatsRxNoPrivacy_Type = Counter32
_RuckusWLANStaStatsRxNoPrivacy_Object = MibTableColumn
ruckusWLANStaStatsRxNoPrivacy = _RuckusWLANStaStatsRxNoPrivacy_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 10),
    _RuckusWLANStaStatsRxNoPrivacy_Type()
)
ruckusWLANStaStatsRxNoPrivacy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxNoPrivacy.setStatus("current")
_RuckusWLANStaStatsRxWEPFail_Type = Counter32
_RuckusWLANStaStatsRxWEPFail_Object = MibTableColumn
ruckusWLANStaStatsRxWEPFail = _RuckusWLANStaStatsRxWEPFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 11),
    _RuckusWLANStaStatsRxWEPFail_Type()
)
ruckusWLANStaStatsRxWEPFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxWEPFail.setStatus("current")
_RuckusWLANStaStatsRxDemicFail_Type = Counter32
_RuckusWLANStaStatsRxDemicFail_Object = MibTableColumn
ruckusWLANStaStatsRxDemicFail = _RuckusWLANStaStatsRxDemicFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 12),
    _RuckusWLANStaStatsRxDemicFail_Type()
)
ruckusWLANStaStatsRxDemicFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxDemicFail.setStatus("current")
_RuckusWLANStaStatsTxDecap_Type = Counter32
_RuckusWLANStaStatsTxDecap_Object = MibTableColumn
ruckusWLANStaStatsTxDecap = _RuckusWLANStaStatsTxDecap_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 13),
    _RuckusWLANStaStatsTxDecap_Type()
)
ruckusWLANStaStatsTxDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxDecap.setStatus("current")
_RuckusWLANStaStatsRxDefrag_Type = Counter32
_RuckusWLANStaStatsRxDefrag_Object = MibTableColumn
ruckusWLANStaStatsRxDefrag = _RuckusWLANStaStatsRxDefrag_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 14),
    _RuckusWLANStaStatsRxDefrag_Type()
)
ruckusWLANStaStatsRxDefrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxDefrag.setStatus("current")
_RuckusWLANStaStatsTxDataFrames_Type = Counter32
_RuckusWLANStaStatsTxDataFrames_Object = MibTableColumn
ruckusWLANStaStatsTxDataFrames = _RuckusWLANStaStatsTxDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 15),
    _RuckusWLANStaStatsTxDataFrames_Type()
)
ruckusWLANStaStatsTxDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxDataFrames.setStatus("current")
_RuckusWLANStaStatsTxMgmtFrames_Type = Counter32
_RuckusWLANStaStatsTxMgmtFrames_Object = MibTableColumn
ruckusWLANStaStatsTxMgmtFrames = _RuckusWLANStaStatsTxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 16),
    _RuckusWLANStaStatsTxMgmtFrames_Type()
)
ruckusWLANStaStatsTxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxMgmtFrames.setStatus("current")
_RuckusWLANStaStatsTxUnicastFrames_Type = Counter32
_RuckusWLANStaStatsTxUnicastFrames_Object = MibTableColumn
ruckusWLANStaStatsTxUnicastFrames = _RuckusWLANStaStatsTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 17),
    _RuckusWLANStaStatsTxUnicastFrames_Type()
)
ruckusWLANStaStatsTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxUnicastFrames.setStatus("current")
_RuckusWLANStaStatsTxMulticastFrames_Type = Counter32
_RuckusWLANStaStatsTxMulticastFrames_Object = MibTableColumn
ruckusWLANStaStatsTxMulticastFrames = _RuckusWLANStaStatsTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 18),
    _RuckusWLANStaStatsTxMulticastFrames_Type()
)
ruckusWLANStaStatsTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxMulticastFrames.setStatus("current")
_RuckusWLANStaStatsTxBytes_Type = Counter32
_RuckusWLANStaStatsTxBytes_Object = MibTableColumn
ruckusWLANStaStatsTxBytes = _RuckusWLANStaStatsTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 19),
    _RuckusWLANStaStatsTxBytes_Type()
)
ruckusWLANStaStatsTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxBytes.setStatus("current")
_RuckusWLANStaStatsTxAssoc_Type = Counter32
_RuckusWLANStaStatsTxAssoc_Object = MibTableColumn
ruckusWLANStaStatsTxAssoc = _RuckusWLANStaStatsTxAssoc_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 20),
    _RuckusWLANStaStatsTxAssoc_Type()
)
ruckusWLANStaStatsTxAssoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxAssoc.setStatus("current")
_RuckusWLANStaStatsTxAssocFail_Type = Counter32
_RuckusWLANStaStatsTxAssocFail_Object = MibTableColumn
ruckusWLANStaStatsTxAssocFail = _RuckusWLANStaStatsTxAssocFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 21),
    _RuckusWLANStaStatsTxAssocFail_Type()
)
ruckusWLANStaStatsTxAssocFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxAssocFail.setStatus("current")
_RuckusWLANStaStatsTxAuth_Type = Counter32
_RuckusWLANStaStatsTxAuth_Object = MibTableColumn
ruckusWLANStaStatsTxAuth = _RuckusWLANStaStatsTxAuth_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 22),
    _RuckusWLANStaStatsTxAuth_Type()
)
ruckusWLANStaStatsTxAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxAuth.setStatus("current")
_RuckusWLANStaStatsTxAuthFail_Type = Counter32
_RuckusWLANStaStatsTxAuthFail_Object = MibTableColumn
ruckusWLANStaStatsTxAuthFail = _RuckusWLANStaStatsTxAuthFail_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 23),
    _RuckusWLANStaStatsTxAuthFail_Type()
)
ruckusWLANStaStatsTxAuthFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxAuthFail.setStatus("current")
_RuckusWLANStaStatsRSSI_Type = Counter32
_RuckusWLANStaStatsRSSI_Object = MibTableColumn
ruckusWLANStaStatsRSSI = _RuckusWLANStaStatsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 24),
    _RuckusWLANStaStatsRSSI_Type()
)
ruckusWLANStaStatsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRSSI.setStatus("current")
_RuckusWLANStaStatsTxRxBytes_Type = Counter32
_RuckusWLANStaStatsTxRxBytes_Object = MibTableColumn
ruckusWLANStaStatsTxRxBytes = _RuckusWLANStaStatsTxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 25),
    _RuckusWLANStaStatsTxRxBytes_Type()
)
ruckusWLANStaStatsTxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxRxBytes.setStatus("current")
_RuckusWLANStaStatsTxRate_Type = Unsigned32
_RuckusWLANStaStatsTxRate_Object = MibTableColumn
ruckusWLANStaStatsTxRate = _RuckusWLANStaStatsTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 26),
    _RuckusWLANStaStatsTxRate_Type()
)
ruckusWLANStaStatsTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxRate.setUnits("Bps")
_RuckusWLANStaStatsRxRate_Type = Unsigned32
_RuckusWLANStaStatsRxRate_Object = MibTableColumn
ruckusWLANStaStatsRxRate = _RuckusWLANStaStatsRxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 27),
    _RuckusWLANStaStatsRxRate_Type()
)
ruckusWLANStaStatsRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxRate.setStatus("current")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsRxRate.setUnits("Bps")
_RuckusWLANStaStatsTxDropRate_Type = Unsigned32
_RuckusWLANStaStatsTxDropRate_Object = MibTableColumn
ruckusWLANStaStatsTxDropRate = _RuckusWLANStaStatsTxDropRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 1, 1, 28),
    _RuckusWLANStaStatsTxDropRate_Type()
)
ruckusWLANStaStatsTxDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaStatsTxDropRate.setStatus("current")
_RuckusWLANStaTable_Object = MibTable
ruckusWLANStaTable = _RuckusWLANStaTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ruckusWLANStaTable.setStatus("current")
_RuckusWLANStaEntry_Object = MibTableRow
ruckusWLANStaEntry = _RuckusWLANStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1)
)
ruckusWLANStaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANStaAddr"),
)
if mibBuilder.loadTexts:
    ruckusWLANStaEntry.setStatus("current")
_RuckusWLANStaAddr_Type = MacAddress
_RuckusWLANStaAddr_Object = MibTableColumn
ruckusWLANStaAddr = _RuckusWLANStaAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 1),
    _RuckusWLANStaAddr_Type()
)
ruckusWLANStaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaAddr.setStatus("current")
_RuckusWLANStaRssi_Type = Unsigned32
_RuckusWLANStaRssi_Object = MibTableColumn
ruckusWLANStaRssi = _RuckusWLANStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 2),
    _RuckusWLANStaRssi_Type()
)
ruckusWLANStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRssi.setStatus("current")
_RuckusWLANStaErp_Type = Unsigned32
_RuckusWLANStaErp_Object = MibTableColumn
ruckusWLANStaErp = _RuckusWLANStaErp_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 3),
    _RuckusWLANStaErp_Type()
)
ruckusWLANStaErp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaErp.setStatus("current")
_RuckusWLANState_Type = Unsigned32
_RuckusWLANState_Object = MibTableColumn
ruckusWLANState = _RuckusWLANState_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 4),
    _RuckusWLANState_Type()
)
ruckusWLANState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANState.setStatus("current")
_RuckusWLANStaCapInfo_Type = Unsigned32
_RuckusWLANStaCapInfo_Object = MibTableColumn
ruckusWLANStaCapInfo = _RuckusWLANStaCapInfo_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 5),
    _RuckusWLANStaCapInfo_Type()
)
ruckusWLANStaCapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaCapInfo.setStatus("current")
_RuckusWLANStaAssocid_Type = Unsigned32
_RuckusWLANStaAssocid_Object = MibTableColumn
ruckusWLANStaAssocid = _RuckusWLANStaAssocid_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 6),
    _RuckusWLANStaAssocid_Type()
)
ruckusWLANStaAssocid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaAssocid.setStatus("current")
_RuckusWLANStaOpMode_Type = Unsigned32
_RuckusWLANStaOpMode_Object = MibTableColumn
ruckusWLANStaOpMode = _RuckusWLANStaOpMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 7),
    _RuckusWLANStaOpMode_Type()
)
ruckusWLANStaOpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaOpMode.setStatus("current")
_RuckusWLANStaIdle_Type = Unsigned32
_RuckusWLANStaIdle_Object = MibTableColumn
ruckusWLANStaIdle = _RuckusWLANStaIdle_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 8),
    _RuckusWLANStaIdle_Type()
)
ruckusWLANStaIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaIdle.setStatus("current")


class _RuckusWLANStaRates_Type(OctetString):
    """Custom type ruckusWLANStaRates based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_RuckusWLANStaRates_Type.__name__ = "OctetString"
_RuckusWLANStaRates_Object = MibTableColumn
ruckusWLANStaRates = _RuckusWLANStaRates_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 9),
    _RuckusWLANStaRates_Type()
)
ruckusWLANStaRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRates.setStatus("current")


class _RuckusWLANStaIpaddr_Type(OctetString):
    """Custom type ruckusWLANStaIpaddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusWLANStaIpaddr_Type.__name__ = "OctetString"
_RuckusWLANStaIpaddr_Object = MibTableColumn
ruckusWLANStaIpaddr = _RuckusWLANStaIpaddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 16),
    _RuckusWLANStaIpaddr_Type()
)
ruckusWLANStaIpaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaIpaddr.setStatus("current")
_RuckusWLANStaAuthMode_Type = OctetString
_RuckusWLANStaAuthMode_Object = MibTableColumn
ruckusWLANStaAuthMode = _RuckusWLANStaAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 2, 1, 20),
    _RuckusWLANStaAuthMode_Type()
)
ruckusWLANStaAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaAuthMode.setStatus("current")
_RuckusWLANStaMQTable_Object = MibTable
ruckusWLANStaMQTable = _RuckusWLANStaMQTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ruckusWLANStaMQTable.setStatus("current")
_RuckusWLANStaMQEntry_Object = MibTableRow
ruckusWLANStaMQEntry = _RuckusWLANStaMQEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1)
)
ruckusWLANStaMQEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANStaMQAddr"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANStaMQQIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANStaMQEntry.setStatus("current")
_RuckusWLANStaMQAddr_Type = MacAddress
_RuckusWLANStaMQAddr_Object = MibTableColumn
ruckusWLANStaMQAddr = _RuckusWLANStaMQAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 1),
    _RuckusWLANStaMQAddr_Type()
)
ruckusWLANStaMQAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANStaMQAddr.setStatus("current")


class _RuckusWLANStaMQQIndex_Type(Integer32):
    """Custom type ruckusWLANStaMQQIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusWLANStaMQQIndex_Type.__name__ = "Integer32"
_RuckusWLANStaMQQIndex_Object = MibTableColumn
ruckusWLANStaMQQIndex = _RuckusWLANStaMQQIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 2),
    _RuckusWLANStaMQQIndex_Type()
)
ruckusWLANStaMQQIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANStaMQQIndex.setStatus("current")
_RuckusWLANStaMQPktsQueued_Type = Unsigned32
_RuckusWLANStaMQPktsQueued_Object = MibTableColumn
ruckusWLANStaMQPktsQueued = _RuckusWLANStaMQPktsQueued_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 3),
    _RuckusWLANStaMQPktsQueued_Type()
)
ruckusWLANStaMQPktsQueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQPktsQueued.setStatus("current")
_RuckusWLANStaMQNumEnqueued_Type = Unsigned32
_RuckusWLANStaMQNumEnqueued_Object = MibTableColumn
ruckusWLANStaMQNumEnqueued = _RuckusWLANStaMQNumEnqueued_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 4),
    _RuckusWLANStaMQNumEnqueued_Type()
)
ruckusWLANStaMQNumEnqueued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQNumEnqueued.setStatus("current")
_RuckusWLANStaMQNumDequeued_Type = Unsigned32
_RuckusWLANStaMQNumDequeued_Object = MibTableColumn
ruckusWLANStaMQNumDequeued = _RuckusWLANStaMQNumDequeued_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 5),
    _RuckusWLANStaMQNumDequeued_Type()
)
ruckusWLANStaMQNumDequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQNumDequeued.setStatus("current")
_RuckusWLANStaMQNumRequeued_Type = Unsigned32
_RuckusWLANStaMQNumRequeued_Object = MibTableColumn
ruckusWLANStaMQNumRequeued = _RuckusWLANStaMQNumRequeued_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 6),
    _RuckusWLANStaMQNumRequeued_Type()
)
ruckusWLANStaMQNumRequeued.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQNumRequeued.setStatus("current")
_RuckusWLANStaMQNumDropped_Type = Unsigned32
_RuckusWLANStaMQNumDropped_Object = MibTableColumn
ruckusWLANStaMQNumDropped = _RuckusWLANStaMQNumDropped_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 7),
    _RuckusWLANStaMQNumDropped_Type()
)
ruckusWLANStaMQNumDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQNumDropped.setStatus("current")
_RuckusWLANStaMQNumDeactivateQueue_Type = Unsigned32
_RuckusWLANStaMQNumDeactivateQueue_Object = MibTableColumn
ruckusWLANStaMQNumDeactivateQueue = _RuckusWLANStaMQNumDeactivateQueue_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 8),
    _RuckusWLANStaMQNumDeactivateQueue_Type()
)
ruckusWLANStaMQNumDeactivateQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQNumDeactivateQueue.setStatus("current")
_RuckusWLANStaMQAveIpg_Type = Unsigned32
_RuckusWLANStaMQAveIpg_Object = MibTableColumn
ruckusWLANStaMQAveIpg = _RuckusWLANStaMQAveIpg_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 9),
    _RuckusWLANStaMQAveIpg_Type()
)
ruckusWLANStaMQAveIpg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQAveIpg.setStatus("current")
_RuckusWLANStaMQMinIpg_Type = Unsigned32
_RuckusWLANStaMQMinIpg_Object = MibTableColumn
ruckusWLANStaMQMinIpg = _RuckusWLANStaMQMinIpg_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 10),
    _RuckusWLANStaMQMinIpg_Type()
)
ruckusWLANStaMQMinIpg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQMinIpg.setStatus("current")
_RuckusWLANStaMQMaxIpg_Type = Unsigned32
_RuckusWLANStaMQMaxIpg_Object = MibTableColumn
ruckusWLANStaMQMaxIpg = _RuckusWLANStaMQMaxIpg_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 11),
    _RuckusWLANStaMQMaxIpg_Type()
)
ruckusWLANStaMQMaxIpg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQMaxIpg.setStatus("current")
_RuckusWLANStaMQAveTxLatency_Type = Unsigned32
_RuckusWLANStaMQAveTxLatency_Object = MibTableColumn
ruckusWLANStaMQAveTxLatency = _RuckusWLANStaMQAveTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 12),
    _RuckusWLANStaMQAveTxLatency_Type()
)
ruckusWLANStaMQAveTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQAveTxLatency.setStatus("current")
_RuckusWLANStaMQMinTxLatency_Type = Unsigned32
_RuckusWLANStaMQMinTxLatency_Object = MibTableColumn
ruckusWLANStaMQMinTxLatency = _RuckusWLANStaMQMinTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 13),
    _RuckusWLANStaMQMinTxLatency_Type()
)
ruckusWLANStaMQMinTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQMinTxLatency.setStatus("current")
_RuckusWLANStaMQMaxTxLatency_Type = Unsigned32
_RuckusWLANStaMQMaxTxLatency_Object = MibTableColumn
ruckusWLANStaMQMaxTxLatency = _RuckusWLANStaMQMaxTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 3, 1, 14),
    _RuckusWLANStaMQMaxTxLatency_Type()
)
ruckusWLANStaMQMaxTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaMQMaxTxLatency.setStatus("current")
_RuckusWLANStaRksTable_Object = MibTable
ruckusWLANStaRksTable = _RuckusWLANStaRksTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ruckusWLANStaRksTable.setStatus("current")
_RuckusWLANStaRksEntry_Object = MibTableRow
ruckusWLANStaRksEntry = _RuckusWLANStaRksEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1)
)
ruckusWLANStaRksEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANStaRksAddr"),
)
if mibBuilder.loadTexts:
    ruckusWLANStaRksEntry.setStatus("current")
_RuckusWLANStaRksAddr_Type = MacAddress
_RuckusWLANStaRksAddr_Object = MibTableColumn
ruckusWLANStaRksAddr = _RuckusWLANStaRksAddr_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 1),
    _RuckusWLANStaRksAddr_Type()
)
ruckusWLANStaRksAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANStaRksAddr.setStatus("current")
_RuckusWLANStaRksRxGoodFrames_Type = Unsigned32
_RuckusWLANStaRksRxGoodFrames_Object = MibTableColumn
ruckusWLANStaRksRxGoodFrames = _RuckusWLANStaRksRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 2),
    _RuckusWLANStaRksRxGoodFrames_Type()
)
ruckusWLANStaRksRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksRxGoodFrames.setStatus("current")
_RuckusWLANStaRksRxCrcErrors_Type = Unsigned32
_RuckusWLANStaRksRxCrcErrors_Object = MibTableColumn
ruckusWLANStaRksRxCrcErrors = _RuckusWLANStaRksRxCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 3),
    _RuckusWLANStaRksRxCrcErrors_Type()
)
ruckusWLANStaRksRxCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksRxCrcErrors.setStatus("current")
_RuckusWLANStaRksTxGoodFrames_Type = Unsigned32
_RuckusWLANStaRksTxGoodFrames_Object = MibTableColumn
ruckusWLANStaRksTxGoodFrames = _RuckusWLANStaRksTxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 4),
    _RuckusWLANStaRksTxGoodFrames_Type()
)
ruckusWLANStaRksTxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxGoodFrames.setStatus("current")
_RuckusWLANStaRksTxRetries_Type = Unsigned32
_RuckusWLANStaRksTxRetries_Object = MibTableColumn
ruckusWLANStaRksTxRetries = _RuckusWLANStaRksTxRetries_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 5),
    _RuckusWLANStaRksTxRetries_Type()
)
ruckusWLANStaRksTxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxRetries.setStatus("current")
_RuckusWLANStaRksTxDiscardExRetries_Type = Unsigned32
_RuckusWLANStaRksTxDiscardExRetries_Object = MibTableColumn
ruckusWLANStaRksTxDiscardExRetries = _RuckusWLANStaRksTxDiscardExRetries_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 6),
    _RuckusWLANStaRksTxDiscardExRetries_Type()
)
ruckusWLANStaRksTxDiscardExRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxDiscardExRetries.setStatus("current")
_RuckusWLANStaRksTxRate_Type = Unsigned32
_RuckusWLANStaRksTxRate_Object = MibTableColumn
ruckusWLANStaRksTxRate = _RuckusWLANStaRksTxRate_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 7),
    _RuckusWLANStaRksTxRate_Type()
)
ruckusWLANStaRksTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxRate.setStatus("current")
_RuckusWLANStaRksTxKbps_Type = Unsigned32
_RuckusWLANStaRksTxKbps_Object = MibTableColumn
ruckusWLANStaRksTxKbps = _RuckusWLANStaRksTxKbps_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 8),
    _RuckusWLANStaRksTxKbps_Type()
)
ruckusWLANStaRksTxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxKbps.setStatus("current")
_RuckusWLANStaRksTxPer_Type = Unsigned32
_RuckusWLANStaRksTxPer_Object = MibTableColumn
ruckusWLANStaRksTxPer = _RuckusWLANStaRksTxPer_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 9),
    _RuckusWLANStaRksTxPer_Type()
)
ruckusWLANStaRksTxPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxPer.setStatus("current")
_RuckusWLANStaRksTxRssi_Type = RuckusdB
_RuckusWLANStaRksTxRssi_Object = MibTableColumn
ruckusWLANStaRksTxRssi = _RuckusWLANStaRksTxRssi_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 2, 4, 1, 10),
    _RuckusWLANStaRksTxRssi_Type()
)
ruckusWLANStaRksTxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusWLANStaRksTxRssi.setStatus("current")
_RuckusWLANSecurityInfo_ObjectIdentity = ObjectIdentity
ruckusWLANSecurityInfo = _RuckusWLANSecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3)
)
_RuckusWLANSecurityTable_Object = MibTable
ruckusWLANSecurityTable = _RuckusWLANSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ruckusWLANSecurityTable.setStatus("current")
_RuckusWLANSecurityEntry_Object = MibTableRow
ruckusWLANSecurityEntry = _RuckusWLANSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 1, 1)
)
ruckusWLANSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANSecurityEntry.setStatus("current")


class _RuckusWLANSecurityMode_Type(Integer32):
    """Custom type ruckusWLANSecurityMode based on Integer32"""
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
        *(("none", 1),
          ("wep", 2),
          ("wpa", 3))
    )


_RuckusWLANSecurityMode_Type.__name__ = "Integer32"
_RuckusWLANSecurityMode_Object = MibTableColumn
ruckusWLANSecurityMode = _RuckusWLANSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 1, 1, 5),
    _RuckusWLANSecurityMode_Type()
)
ruckusWLANSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANSecurityMode.setStatus("current")


class _RuckusWLANSecurityAuthMode_Type(Integer32):
    """Custom type ruckusWLANSecurityAuthMode based on Integer32"""
    defaultValue = 1

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
        *(("auto", 3),
          ("open", 1),
          ("wep-shared", 2),
          ("wpa-eap-802-1x", 4))
    )


_RuckusWLANSecurityAuthMode_Type.__name__ = "Integer32"
_RuckusWLANSecurityAuthMode_Object = MibTableColumn
ruckusWLANSecurityAuthMode = _RuckusWLANSecurityAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 1, 1, 8),
    _RuckusWLANSecurityAuthMode_Type()
)
ruckusWLANSecurityAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANSecurityAuthMode.setStatus("current")


class _RuckusWLANSecurityEncryMode_Type(Integer32):
    """Custom type ruckusWLANSecurityEncryMode based on Integer32"""
    defaultValue = 1

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
        *(("aes", 3),
          ("auto", 4),
          ("none", 1),
          ("tkip", 2))
    )


_RuckusWLANSecurityEncryMode_Type.__name__ = "Integer32"
_RuckusWLANSecurityEncryMode_Object = MibTableColumn
ruckusWLANSecurityEncryMode = _RuckusWLANSecurityEncryMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 1, 1, 10),
    _RuckusWLANSecurityEncryMode_Type()
)
ruckusWLANSecurityEncryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANSecurityEncryMode.setStatus("current")
_RuckusWLANWEPTable_Object = MibTable
ruckusWLANWEPTable = _RuckusWLANWEPTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ruckusWLANWEPTable.setStatus("current")
_RuckusWLANWEPEntry_Object = MibTableRow
ruckusWLANWEPEntry = _RuckusWLANWEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 2, 1)
)
ruckusWLANWEPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANWEPEntry.setStatus("current")


class _RuckusWLANWEPEncryLenType_Type(Integer32):
    """Custom type ruckusWLANWEPEncryLenType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bit-128", 2),
          ("bit-64", 1))
    )


_RuckusWLANWEPEncryLenType_Type.__name__ = "Integer32"
_RuckusWLANWEPEncryLenType_Object = MibTableColumn
ruckusWLANWEPEncryLenType = _RuckusWLANWEPEncryLenType_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 2, 1, 6),
    _RuckusWLANWEPEncryLenType_Type()
)
ruckusWLANWEPEncryLenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWEPEncryLenType.setStatus("current")


class _RuckusWLANWEPKeyIndex_Type(Integer32):
    """Custom type ruckusWLANWEPKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RuckusWLANWEPKeyIndex_Type.__name__ = "Integer32"
_RuckusWLANWEPKeyIndex_Object = MibTableColumn
ruckusWLANWEPKeyIndex = _RuckusWLANWEPKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 2, 1, 8),
    _RuckusWLANWEPKeyIndex_Type()
)
ruckusWLANWEPKeyIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWEPKeyIndex.setStatus("current")


class _RuckusWLANWEPKey_Type(DisplayString):
    """Custom type ruckusWLANWEPKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 32),
    )


_RuckusWLANWEPKey_Type.__name__ = "DisplayString"
_RuckusWLANWEPKey_Object = MibTableColumn
ruckusWLANWEPKey = _RuckusWLANWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 2, 1, 9),
    _RuckusWLANWEPKey_Type()
)
ruckusWLANWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWEPKey.setStatus("current")
_RuckusWLANWPATable_Object = MibTable
ruckusWLANWPATable = _RuckusWLANWPATable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    ruckusWLANWPATable.setStatus("current")
_RuckusWLANWPAEntry_Object = MibTableRow
ruckusWLANWPAEntry = _RuckusWLANWPAEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3, 1)
)
ruckusWLANWPAEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ruckusWLANWPAEntry.setStatus("current")


class _RuckusWLANWPAVersion_Type(Integer32):
    """Custom type ruckusWLANWPAVersion based on Integer32"""
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
        *(("auto", 3),
          ("wpa", 1),
          ("wpa2", 2))
    )


_RuckusWLANWPAVersion_Type.__name__ = "Integer32"
_RuckusWLANWPAVersion_Object = MibTableColumn
ruckusWLANWPAVersion = _RuckusWLANWPAVersion_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3, 1, 5),
    _RuckusWLANWPAVersion_Type()
)
ruckusWLANWPAVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWPAVersion.setStatus("current")


class _RuckusWLANWPAKey_Type(DisplayString):
    """Custom type ruckusWLANWPAKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_RuckusWLANWPAKey_Type.__name__ = "DisplayString"
_RuckusWLANWPAKey_Object = MibTableColumn
ruckusWLANWPAKey = _RuckusWLANWPAKey_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3, 1, 12),
    _RuckusWLANWPAKey_Type()
)
ruckusWLANWPAKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWPAKey.setStatus("current")


class _RuckusWLANWPARadiusNasId_Type(DisplayString):
    """Custom type ruckusWLANWPARadiusNasId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusWLANWPARadiusNasId_Type.__name__ = "DisplayString"
_RuckusWLANWPARadiusNasId_Object = MibTableColumn
ruckusWLANWPARadiusNasId = _RuckusWLANWPARadiusNasId_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3, 1, 15),
    _RuckusWLANWPARadiusNasId_Type()
)
ruckusWLANWPARadiusNasId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWPARadiusNasId.setStatus("current")


class _RuckusWLANWPAReAuthenticationPeriod_Type(Integer32):
    """Custom type ruckusWLANWPAReAuthenticationPeriod based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_RuckusWLANWPAReAuthenticationPeriod_Type.__name__ = "Integer32"
_RuckusWLANWPAReAuthenticationPeriod_Object = MibTableColumn
ruckusWLANWPAReAuthenticationPeriod = _RuckusWLANWPAReAuthenticationPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 3, 1, 20),
    _RuckusWLANWPAReAuthenticationPeriod_Type()
)
ruckusWLANWPAReAuthenticationPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANWPAReAuthenticationPeriod.setStatus("current")
_RuckusWLANAAAServerTable_Object = MibTable
ruckusWLANAAAServerTable = _RuckusWLANAAAServerTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4)
)
if mibBuilder.loadTexts:
    ruckusWLANAAAServerTable.setStatus("current")
_RuckusWLANAAAServerEntry_Object = MibTableRow
ruckusWLANAAAServerEntry = _RuckusWLANAAAServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4, 1)
)
ruckusWLANAAAServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RUCKUS-WLAN-MIB", "ruckusWLANSeverMode"),
)
if mibBuilder.loadTexts:
    ruckusWLANAAAServerEntry.setStatus("current")


class _RuckusWLANSeverMode_Type(Integer32):
    """Custom type ruckusWLANSeverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("account", 2),
          ("auth", 1))
    )


_RuckusWLANSeverMode_Type.__name__ = "Integer32"
_RuckusWLANSeverMode_Object = MibTableColumn
ruckusWLANSeverMode = _RuckusWLANSeverMode_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4, 1, 2),
    _RuckusWLANSeverMode_Type()
)
ruckusWLANSeverMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusWLANSeverMode.setStatus("current")


class _RuckusWLANServerIpAddress_Type(OctetString):
    """Custom type ruckusWLANServerIpAddress based on OctetString"""
    defaultValue = 0

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 40),
    )


_RuckusWLANServerIpAddress_Type.__name__ = "OctetString"
_RuckusWLANServerIpAddress_Object = MibTableColumn
ruckusWLANServerIpAddress = _RuckusWLANServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4, 1, 10),
    _RuckusWLANServerIpAddress_Type()
)
ruckusWLANServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANServerIpAddress.setStatus("current")


class _RuckusWLANServerPort_Type(Integer32):
    """Custom type ruckusWLANServerPort based on Integer32"""
    defaultValue = 1812


_RuckusWLANServerPort_Object = MibTableColumn
ruckusWLANServerPort = _RuckusWLANServerPort_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4, 1, 12),
    _RuckusWLANServerPort_Type()
)
ruckusWLANServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANServerPort.setStatus("current")


class _RuckusWLANServerSecret_Type(OctetString):
    """Custom type ruckusWLANServerSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RuckusWLANServerSecret_Type.__name__ = "OctetString"
_RuckusWLANServerSecret_Object = MibTableColumn
ruckusWLANServerSecret = _RuckusWLANServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 1, 3, 4, 1, 15),
    _RuckusWLANServerSecret_Type()
)
ruckusWLANServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusWLANServerSecret.setStatus("current")
_RuckusWLANEvents_ObjectIdentity = ObjectIdentity
ruckusWLANEvents = _RuckusWLANEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 6, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-WLAN-MIB",
    **{"ruckusWLANMIB": ruckusWLANMIB,
       "ruckusWLANObjects": ruckusWLANObjects,
       "ruckusWLANInfo": ruckusWLANInfo,
       "ruckusWLANTable": ruckusWLANTable,
       "ruckusWLANEntry": ruckusWLANEntry,
       "ruckusWLANSSID": ruckusWLANSSID,
       "ruckusWLANBSSID": ruckusWLANBSSID,
       "ruckusWLANBSSType": ruckusWLANBSSType,
       "ruckusWLANOperationalRateSet": ruckusWLANOperationalRateSet,
       "ruckusWLANBeaconPeriod": ruckusWLANBeaconPeriod,
       "ruckusWLANDTIMPeriod": ruckusWLANDTIMPeriod,
       "ruckusWLANRTSThreshold": ruckusWLANRTSThreshold,
       "ruckusWLANFragmentationThreshold": ruckusWLANFragmentationThreshold,
       "ruckusWLANRadioMode": ruckusWLANRadioMode,
       "ruckusWLANChannel": ruckusWLANChannel,
       "ruckusWLANWDSEnable": ruckusWLANWDSEnable,
       "ruckusWLANAdminStatus": ruckusWLANAdminStatus,
       "ruckusWLANProtectionMode": ruckusWLANProtectionMode,
       "ruckusWLANName": ruckusWLANName,
       "ruckusWLANSSIDBcastDisable": ruckusWLANSSIDBcastDisable,
       "ruckusWLANVlanID": ruckusWLANVlanID,
       "ruckusWLANIGMPSnooping": ruckusWLANIGMPSnooping,
       "ruckusWLANSuppDataRatesTxTable": ruckusWLANSuppDataRatesTxTable,
       "ruckusWLANSuppDataRatesTxEntry": ruckusWLANSuppDataRatesTxEntry,
       "ruckusWLANSuppDataRatesTxIndex": ruckusWLANSuppDataRatesTxIndex,
       "ruckusWLANSuppDataRatesTxValue": ruckusWLANSuppDataRatesTxValue,
       "ruckusWLANSuppDataRatesRxTable": ruckusWLANSuppDataRatesRxTable,
       "ruckusWLANSuppDataRatesRxEntry": ruckusWLANSuppDataRatesRxEntry,
       "ruckusWLANSuppDataRatesRxIndex": ruckusWLANSuppDataRatesRxIndex,
       "ruckusWLANSuppDataRatesRxValue": ruckusWLANSuppDataRatesRxValue,
       "ruckusWLANStatsTable": ruckusWLANStatsTable,
       "ruckusWLANStatsEntry": ruckusWLANStatsEntry,
       "ruckusWLANStatsSSID": ruckusWLANStatsSSID,
       "ruckusWLANStatsBSSID": ruckusWLANStatsBSSID,
       "ruckusWLANStatsNumSta": ruckusWLANStatsNumSta,
       "ruckusWLANStatsNumAuthSta": ruckusWLANStatsNumAuthSta,
       "ruckusWLANStatsNumAuthReq": ruckusWLANStatsNumAuthReq,
       "ruckusWLANStatsNumAuthResp": ruckusWLANStatsNumAuthResp,
       "ruckusWLANStatsNumAuthSuccess": ruckusWLANStatsNumAuthSuccess,
       "ruckusWLANStatsNumAuthFail": ruckusWLANStatsNumAuthFail,
       "ruckusWLANStatsNumAssocReq": ruckusWLANStatsNumAssocReq,
       "ruckusWLANStatsNumAssocResp": ruckusWLANStatsNumAssocResp,
       "ruckusWLANStatsNumReAssocReq": ruckusWLANStatsNumReAssocReq,
       "ruckusWLANStatsNumReAssocResp": ruckusWLANStatsNumReAssocResp,
       "ruckusWLANStatsNumAssocSuccess": ruckusWLANStatsNumAssocSuccess,
       "ruckusWLANStatsNumAssocFail": ruckusWLANStatsNumAssocFail,
       "ruckusWLANStatsAssocFailRate": ruckusWLANStatsAssocFailRate,
       "ruckusWLANStatsAuthFailRate": ruckusWLANStatsAuthFailRate,
       "ruckusWLANStatsAssocSuccessRate": ruckusWLANStatsAssocSuccessRate,
       "ruckusWLANStatsRxDataFrames": ruckusWLANStatsRxDataFrames,
       "ruckusWLANStatsRxMgmtFrames": ruckusWLANStatsRxMgmtFrames,
       "ruckusWLANStatsRxCtrlFrames": ruckusWLANStatsRxCtrlFrames,
       "ruckusWLANStatsRxUnicastFrames": ruckusWLANStatsRxUnicastFrames,
       "ruckusWLANStatsRxMulticastFrames": ruckusWLANStatsRxMulticastFrames,
       "ruckusWLANStatsRxBroadcastFrames": ruckusWLANStatsRxBroadcastFrames,
       "ruckusWLANStatsRxBytes": ruckusWLANStatsRxBytes,
       "ruckusWLANStatsRxDup": ruckusWLANStatsRxDup,
       "ruckusWLANStatsRxNoPrivacy": ruckusWLANStatsRxNoPrivacy,
       "ruckusWLANStatsRxWEPFail": ruckusWLANStatsRxWEPFail,
       "ruckusWLANStatsRxDecryptCRCError": ruckusWLANStatsRxDecryptCRCError,
       "ruckusWLANStatsRxMICError": ruckusWLANStatsRxMICError,
       "ruckusWLANStatsRxDrops": ruckusWLANStatsRxDrops,
       "ruckusWLANStatsRxErrors": ruckusWLANStatsRxErrors,
       "ruckusWLANStatsRxFrames": ruckusWLANStatsRxFrames,
       "ruckusWLANStatsRxDropRate": ruckusWLANStatsRxDropRate,
       "ruckusWLANStatsTxDataFrames": ruckusWLANStatsTxDataFrames,
       "ruckusWLANStatsTxMgmtFrames": ruckusWLANStatsTxMgmtFrames,
       "ruckusWLANStatsTxUnicastFrames": ruckusWLANStatsTxUnicastFrames,
       "ruckusWLANStatsTxMulticastFrames": ruckusWLANStatsTxMulticastFrames,
       "ruckusWLANStatsTxBroadcastFrames": ruckusWLANStatsTxBroadcastFrames,
       "ruckusWLANStatsTxBytes": ruckusWLANStatsTxBytes,
       "ruckusWLANStatsTxDrops": ruckusWLANStatsTxDrops,
       "ruckusWLANStatsTxErrors": ruckusWLANStatsTxErrors,
       "ruckusWLANStatsTxFrames": ruckusWLANStatsTxFrames,
       "ruckusWLANStatsPeriodRxErrorRate": ruckusWLANStatsPeriodRxErrorRate,
       "ruckusWLANStatsPeriodTxErrorRate": ruckusWLANStatsPeriodTxErrorRate,
       "ruckusWLANStatsPeriodAssocReq": ruckusWLANStatsPeriodAssocReq,
       "ruckusWLANStatsPeriodAssocResp": ruckusWLANStatsPeriodAssocResp,
       "ruckusWLANStatsPeriodAssocSuccess": ruckusWLANStatsPeriodAssocSuccess,
       "ruckusWLANStaInfo": ruckusWLANStaInfo,
       "ruckusWLANStaStatsTable": ruckusWLANStaStatsTable,
       "ruckusWLANStaStatsEntry": ruckusWLANStaStatsEntry,
       "ruckusWLANStaStatsMacAddr": ruckusWLANStaStatsMacAddr,
       "ruckusWLANStaStatsSSID": ruckusWLANStaStatsSSID,
       "ruckusWLANStaStatsRxDataFrames": ruckusWLANStaStatsRxDataFrames,
       "ruckusWLANStaStatsRxMgmtFrames": ruckusWLANStaStatsRxMgmtFrames,
       "ruckusWLANStaStatsRxCtrlFrames": ruckusWLANStaStatsRxCtrlFrames,
       "ruckusWLANStaStatsRxUnicastFrames": ruckusWLANStaStatsRxUnicastFrames,
       "ruckusWLANStaStatsRxMulticastFrames": ruckusWLANStaStatsRxMulticastFrames,
       "ruckusWLANStaStatsRxBytes": ruckusWLANStaStatsRxBytes,
       "ruckusWLANStaStatsRxDup": ruckusWLANStaStatsRxDup,
       "ruckusWLANStaStatsRxNoPrivacy": ruckusWLANStaStatsRxNoPrivacy,
       "ruckusWLANStaStatsRxWEPFail": ruckusWLANStaStatsRxWEPFail,
       "ruckusWLANStaStatsRxDemicFail": ruckusWLANStaStatsRxDemicFail,
       "ruckusWLANStaStatsTxDecap": ruckusWLANStaStatsTxDecap,
       "ruckusWLANStaStatsRxDefrag": ruckusWLANStaStatsRxDefrag,
       "ruckusWLANStaStatsTxDataFrames": ruckusWLANStaStatsTxDataFrames,
       "ruckusWLANStaStatsTxMgmtFrames": ruckusWLANStaStatsTxMgmtFrames,
       "ruckusWLANStaStatsTxUnicastFrames": ruckusWLANStaStatsTxUnicastFrames,
       "ruckusWLANStaStatsTxMulticastFrames": ruckusWLANStaStatsTxMulticastFrames,
       "ruckusWLANStaStatsTxBytes": ruckusWLANStaStatsTxBytes,
       "ruckusWLANStaStatsTxAssoc": ruckusWLANStaStatsTxAssoc,
       "ruckusWLANStaStatsTxAssocFail": ruckusWLANStaStatsTxAssocFail,
       "ruckusWLANStaStatsTxAuth": ruckusWLANStaStatsTxAuth,
       "ruckusWLANStaStatsTxAuthFail": ruckusWLANStaStatsTxAuthFail,
       "ruckusWLANStaStatsRSSI": ruckusWLANStaStatsRSSI,
       "ruckusWLANStaStatsTxRxBytes": ruckusWLANStaStatsTxRxBytes,
       "ruckusWLANStaStatsTxRate": ruckusWLANStaStatsTxRate,
       "ruckusWLANStaStatsRxRate": ruckusWLANStaStatsRxRate,
       "ruckusWLANStaStatsTxDropRate": ruckusWLANStaStatsTxDropRate,
       "ruckusWLANStaTable": ruckusWLANStaTable,
       "ruckusWLANStaEntry": ruckusWLANStaEntry,
       "ruckusWLANStaAddr": ruckusWLANStaAddr,
       "ruckusWLANStaRssi": ruckusWLANStaRssi,
       "ruckusWLANStaErp": ruckusWLANStaErp,
       "ruckusWLANState": ruckusWLANState,
       "ruckusWLANStaCapInfo": ruckusWLANStaCapInfo,
       "ruckusWLANStaAssocid": ruckusWLANStaAssocid,
       "ruckusWLANStaOpMode": ruckusWLANStaOpMode,
       "ruckusWLANStaIdle": ruckusWLANStaIdle,
       "ruckusWLANStaRates": ruckusWLANStaRates,
       "ruckusWLANStaIpaddr": ruckusWLANStaIpaddr,
       "ruckusWLANStaAuthMode": ruckusWLANStaAuthMode,
       "ruckusWLANStaMQTable": ruckusWLANStaMQTable,
       "ruckusWLANStaMQEntry": ruckusWLANStaMQEntry,
       "ruckusWLANStaMQAddr": ruckusWLANStaMQAddr,
       "ruckusWLANStaMQQIndex": ruckusWLANStaMQQIndex,
       "ruckusWLANStaMQPktsQueued": ruckusWLANStaMQPktsQueued,
       "ruckusWLANStaMQNumEnqueued": ruckusWLANStaMQNumEnqueued,
       "ruckusWLANStaMQNumDequeued": ruckusWLANStaMQNumDequeued,
       "ruckusWLANStaMQNumRequeued": ruckusWLANStaMQNumRequeued,
       "ruckusWLANStaMQNumDropped": ruckusWLANStaMQNumDropped,
       "ruckusWLANStaMQNumDeactivateQueue": ruckusWLANStaMQNumDeactivateQueue,
       "ruckusWLANStaMQAveIpg": ruckusWLANStaMQAveIpg,
       "ruckusWLANStaMQMinIpg": ruckusWLANStaMQMinIpg,
       "ruckusWLANStaMQMaxIpg": ruckusWLANStaMQMaxIpg,
       "ruckusWLANStaMQAveTxLatency": ruckusWLANStaMQAveTxLatency,
       "ruckusWLANStaMQMinTxLatency": ruckusWLANStaMQMinTxLatency,
       "ruckusWLANStaMQMaxTxLatency": ruckusWLANStaMQMaxTxLatency,
       "ruckusWLANStaRksTable": ruckusWLANStaRksTable,
       "ruckusWLANStaRksEntry": ruckusWLANStaRksEntry,
       "ruckusWLANStaRksAddr": ruckusWLANStaRksAddr,
       "ruckusWLANStaRksRxGoodFrames": ruckusWLANStaRksRxGoodFrames,
       "ruckusWLANStaRksRxCrcErrors": ruckusWLANStaRksRxCrcErrors,
       "ruckusWLANStaRksTxGoodFrames": ruckusWLANStaRksTxGoodFrames,
       "ruckusWLANStaRksTxRetries": ruckusWLANStaRksTxRetries,
       "ruckusWLANStaRksTxDiscardExRetries": ruckusWLANStaRksTxDiscardExRetries,
       "ruckusWLANStaRksTxRate": ruckusWLANStaRksTxRate,
       "ruckusWLANStaRksTxKbps": ruckusWLANStaRksTxKbps,
       "ruckusWLANStaRksTxPer": ruckusWLANStaRksTxPer,
       "ruckusWLANStaRksTxRssi": ruckusWLANStaRksTxRssi,
       "ruckusWLANSecurityInfo": ruckusWLANSecurityInfo,
       "ruckusWLANSecurityTable": ruckusWLANSecurityTable,
       "ruckusWLANSecurityEntry": ruckusWLANSecurityEntry,
       "ruckusWLANSecurityMode": ruckusWLANSecurityMode,
       "ruckusWLANSecurityAuthMode": ruckusWLANSecurityAuthMode,
       "ruckusWLANSecurityEncryMode": ruckusWLANSecurityEncryMode,
       "ruckusWLANWEPTable": ruckusWLANWEPTable,
       "ruckusWLANWEPEntry": ruckusWLANWEPEntry,
       "ruckusWLANWEPEncryLenType": ruckusWLANWEPEncryLenType,
       "ruckusWLANWEPKeyIndex": ruckusWLANWEPKeyIndex,
       "ruckusWLANWEPKey": ruckusWLANWEPKey,
       "ruckusWLANWPATable": ruckusWLANWPATable,
       "ruckusWLANWPAEntry": ruckusWLANWPAEntry,
       "ruckusWLANWPAVersion": ruckusWLANWPAVersion,
       "ruckusWLANWPAKey": ruckusWLANWPAKey,
       "ruckusWLANWPARadiusNasId": ruckusWLANWPARadiusNasId,
       "ruckusWLANWPAReAuthenticationPeriod": ruckusWLANWPAReAuthenticationPeriod,
       "ruckusWLANAAAServerTable": ruckusWLANAAAServerTable,
       "ruckusWLANAAAServerEntry": ruckusWLANAAAServerEntry,
       "ruckusWLANSeverMode": ruckusWLANSeverMode,
       "ruckusWLANServerIpAddress": ruckusWLANServerIpAddress,
       "ruckusWLANServerPort": ruckusWLANServerPort,
       "ruckusWLANServerSecret": ruckusWLANServerSecret,
       "ruckusWLANEvents": ruckusWLANEvents}
)
