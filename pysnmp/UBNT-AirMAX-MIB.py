# SNMP MIB module (UBNT-AirMAX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/UBNT-AirMAX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:17 2024
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

(ubntAirosGroups,
 ubntMIB) = mibBuilder.importSymbols(
    "UBNT-MIB",
    "ubntAirosGroups",
    "ubntMIB")


# MODULE-IDENTITY

ubntAirMAX = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4)
)
ubntAirMAX.setRevisions(
        ("2015-09-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UbntRadioTable_Object = MibTable
ubntRadioTable = _UbntRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ubntRadioTable.setStatus("current")
_UbntRadioEntry_Object = MibTableRow
ubntRadioEntry = _UbntRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1)
)
ubntRadioEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntRadioIndex"),
)
if mibBuilder.loadTexts:
    ubntRadioEntry.setStatus("current")


class _UbntRadioIndex_Type(Integer32):
    """Custom type ubntRadioIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioIndex_Type.__name__ = "Integer32"
_UbntRadioIndex_Object = MibTableColumn
ubntRadioIndex = _UbntRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 1),
    _UbntRadioIndex_Type()
)
ubntRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntRadioIndex.setStatus("current")


class _UbntRadioMode_Type(Integer32):
    """Custom type ubntRadioMode based on Integer32"""
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
        *(("ap", 2),
          ("aprepeater", 3),
          ("apwds", 4),
          ("sta", 1))
    )


_UbntRadioMode_Type.__name__ = "Integer32"
_UbntRadioMode_Object = MibTableColumn
ubntRadioMode = _UbntRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 2),
    _UbntRadioMode_Type()
)
ubntRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioMode.setStatus("current")
_UbntRadioCCode_Type = Integer32
_UbntRadioCCode_Object = MibTableColumn
ubntRadioCCode = _UbntRadioCCode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 3),
    _UbntRadioCCode_Type()
)
ubntRadioCCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioCCode.setStatus("current")


class _UbntRadioFreq_Type(Integer32):
    """Custom type ubntRadioFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioFreq_Type.__name__ = "Integer32"
_UbntRadioFreq_Object = MibTableColumn
ubntRadioFreq = _UbntRadioFreq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 4),
    _UbntRadioFreq_Type()
)
ubntRadioFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioFreq.setStatus("current")
_UbntRadioDfsEnabled_Type = TruthValue
_UbntRadioDfsEnabled_Object = MibTableColumn
ubntRadioDfsEnabled = _UbntRadioDfsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 5),
    _UbntRadioDfsEnabled_Type()
)
ubntRadioDfsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioDfsEnabled.setStatus("current")


class _UbntRadioTxPower_Type(Integer32):
    """Custom type ubntRadioTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioTxPower_Type.__name__ = "Integer32"
_UbntRadioTxPower_Object = MibTableColumn
ubntRadioTxPower = _UbntRadioTxPower_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 6),
    _UbntRadioTxPower_Type()
)
ubntRadioTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioTxPower.setStatus("current")


class _UbntRadioDistance_Type(Integer32):
    """Custom type ubntRadioDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntRadioDistance_Type.__name__ = "Integer32"
_UbntRadioDistance_Object = MibTableColumn
ubntRadioDistance = _UbntRadioDistance_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 7),
    _UbntRadioDistance_Type()
)
ubntRadioDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioDistance.setStatus("current")


class _UbntRadioChainmask_Type(Integer32):
    """Custom type ubntRadioChainmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioChainmask_Type.__name__ = "Integer32"
_UbntRadioChainmask_Object = MibTableColumn
ubntRadioChainmask = _UbntRadioChainmask_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 8),
    _UbntRadioChainmask_Type()
)
ubntRadioChainmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioChainmask.setStatus("current")
_UbntRadioAntenna_Type = DisplayString
_UbntRadioAntenna_Object = MibTableColumn
ubntRadioAntenna = _UbntRadioAntenna_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 1, 1, 9),
    _UbntRadioAntenna_Type()
)
ubntRadioAntenna.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioAntenna.setStatus("current")
_UbntRadioRssiTable_Object = MibTable
ubntRadioRssiTable = _UbntRadioRssiTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2)
)
if mibBuilder.loadTexts:
    ubntRadioRssiTable.setStatus("current")
_UbntRadioRssiEntry_Object = MibTableRow
ubntRadioRssiEntry = _UbntRadioRssiEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1)
)
ubntRadioRssiEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntRadioIndex"),
    (0, "UBNT-AirMAX-MIB", "ubntRadioRssiIndex"),
)
if mibBuilder.loadTexts:
    ubntRadioRssiEntry.setStatus("current")


class _UbntRadioRssiIndex_Type(Integer32):
    """Custom type ubntRadioRssiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntRadioRssiIndex_Type.__name__ = "Integer32"
_UbntRadioRssiIndex_Object = MibTableColumn
ubntRadioRssiIndex = _UbntRadioRssiIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 1),
    _UbntRadioRssiIndex_Type()
)
ubntRadioRssiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntRadioRssiIndex.setStatus("current")
_UbntRadioRssi_Type = Integer32
_UbntRadioRssi_Object = MibTableColumn
ubntRadioRssi = _UbntRadioRssi_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 2),
    _UbntRadioRssi_Type()
)
ubntRadioRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssi.setStatus("current")
_UbntRadioRssiMgmt_Type = Integer32
_UbntRadioRssiMgmt_Object = MibTableColumn
ubntRadioRssiMgmt = _UbntRadioRssiMgmt_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 3),
    _UbntRadioRssiMgmt_Type()
)
ubntRadioRssiMgmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssiMgmt.setStatus("current")
_UbntRadioRssiExt_Type = Integer32
_UbntRadioRssiExt_Object = MibTableColumn
ubntRadioRssiExt = _UbntRadioRssiExt_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 2, 1, 4),
    _UbntRadioRssiExt_Type()
)
ubntRadioRssiExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntRadioRssiExt.setStatus("current")
_UbntAirSyncTable_Object = MibTable
ubntAirSyncTable = _UbntAirSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ubntAirSyncTable.setStatus("current")
_UbntAirSyncEntry_Object = MibTableRow
ubntAirSyncEntry = _UbntAirSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1)
)
ubntAirSyncEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntAirSyncIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirSyncEntry.setStatus("current")


class _UbntAirSyncIfIndex_Type(Integer32):
    """Custom type ubntAirSyncIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirSyncIfIndex_Type.__name__ = "Integer32"
_UbntAirSyncIfIndex_Object = MibTableColumn
ubntAirSyncIfIndex = _UbntAirSyncIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 1),
    _UbntAirSyncIfIndex_Type()
)
ubntAirSyncIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirSyncIfIndex.setStatus("current")


class _UbntAirSyncMode_Type(Integer32):
    """Custom type ubntAirSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("master", 1),
          ("slave", 2))
    )


_UbntAirSyncMode_Type.__name__ = "Integer32"
_UbntAirSyncMode_Object = MibTableColumn
ubntAirSyncMode = _UbntAirSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 2),
    _UbntAirSyncMode_Type()
)
ubntAirSyncMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncMode.setStatus("current")


class _UbntAirSyncCount_Type(Integer32):
    """Custom type ubntAirSyncCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UbntAirSyncCount_Type.__name__ = "Integer32"
_UbntAirSyncCount_Object = MibTableColumn
ubntAirSyncCount = _UbntAirSyncCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 3),
    _UbntAirSyncCount_Type()
)
ubntAirSyncCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncCount.setStatus("current")


class _UbntAirSyncDownUtil_Type(Integer32):
    """Custom type ubntAirSyncDownUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirSyncDownUtil_Type.__name__ = "Integer32"
_UbntAirSyncDownUtil_Object = MibTableColumn
ubntAirSyncDownUtil = _UbntAirSyncDownUtil_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 4),
    _UbntAirSyncDownUtil_Type()
)
ubntAirSyncDownUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncDownUtil.setStatus("current")


class _UbntAirSyncUpUtil_Type(Integer32):
    """Custom type ubntAirSyncUpUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirSyncUpUtil_Type.__name__ = "Integer32"
_UbntAirSyncUpUtil_Object = MibTableColumn
ubntAirSyncUpUtil = _UbntAirSyncUpUtil_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 3, 1, 5),
    _UbntAirSyncUpUtil_Type()
)
ubntAirSyncUpUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSyncUpUtil.setStatus("current")
_UbntAirSelTable_Object = MibTable
ubntAirSelTable = _UbntAirSelTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4)
)
if mibBuilder.loadTexts:
    ubntAirSelTable.setStatus("current")
_UbntAirSelEntry_Object = MibTableRow
ubntAirSelEntry = _UbntAirSelEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1)
)
ubntAirSelEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntAirSelIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirSelEntry.setStatus("current")


class _UbntAirSelIfIndex_Type(Integer32):
    """Custom type ubntAirSelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirSelIfIndex_Type.__name__ = "Integer32"
_UbntAirSelIfIndex_Object = MibTableColumn
ubntAirSelIfIndex = _UbntAirSelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 1),
    _UbntAirSelIfIndex_Type()
)
ubntAirSelIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirSelIfIndex.setStatus("current")
_UbntAirSelEnabled_Type = TruthValue
_UbntAirSelEnabled_Object = MibTableColumn
ubntAirSelEnabled = _UbntAirSelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 2),
    _UbntAirSelEnabled_Type()
)
ubntAirSelEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSelEnabled.setStatus("current")


class _UbntAirSelInterval_Type(Integer32):
    """Custom type ubntAirSelInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UbntAirSelInterval_Type.__name__ = "Integer32"
_UbntAirSelInterval_Object = MibTableColumn
ubntAirSelInterval = _UbntAirSelInterval_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 4, 1, 3),
    _UbntAirSelInterval_Type()
)
ubntAirSelInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirSelInterval.setStatus("current")
_UbntWlStatTable_Object = MibTable
ubntWlStatTable = _UbntWlStatTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ubntWlStatTable.setStatus("current")
_UbntWlStatEntry_Object = MibTableRow
ubntWlStatEntry = _UbntWlStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1)
)
ubntWlStatEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntWlStatIndex"),
)
if mibBuilder.loadTexts:
    ubntWlStatEntry.setStatus("current")


class _UbntWlStatIndex_Type(Integer32):
    """Custom type ubntWlStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntWlStatIndex_Type.__name__ = "Integer32"
_UbntWlStatIndex_Object = MibTableColumn
ubntWlStatIndex = _UbntWlStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 1),
    _UbntWlStatIndex_Type()
)
ubntWlStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntWlStatIndex.setStatus("current")
_UbntWlStatSsid_Type = DisplayString
_UbntWlStatSsid_Object = MibTableColumn
ubntWlStatSsid = _UbntWlStatSsid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 2),
    _UbntWlStatSsid_Type()
)
ubntWlStatSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSsid.setStatus("current")
_UbntWlStatHideSsid_Type = TruthValue
_UbntWlStatHideSsid_Object = MibTableColumn
ubntWlStatHideSsid = _UbntWlStatHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 3),
    _UbntWlStatHideSsid_Type()
)
ubntWlStatHideSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatHideSsid.setStatus("current")
_UbntWlStatApMac_Type = MacAddress
_UbntWlStatApMac_Object = MibTableColumn
ubntWlStatApMac = _UbntWlStatApMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 4),
    _UbntWlStatApMac_Type()
)
ubntWlStatApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatApMac.setStatus("current")
_UbntWlStatSignal_Type = Integer32
_UbntWlStatSignal_Object = MibTableColumn
ubntWlStatSignal = _UbntWlStatSignal_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 5),
    _UbntWlStatSignal_Type()
)
ubntWlStatSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSignal.setStatus("current")
_UbntWlStatRssi_Type = Integer32
_UbntWlStatRssi_Object = MibTableColumn
ubntWlStatRssi = _UbntWlStatRssi_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 6),
    _UbntWlStatRssi_Type()
)
ubntWlStatRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatRssi.setStatus("current")
_UbntWlStatCcq_Type = Integer32
_UbntWlStatCcq_Object = MibTableColumn
ubntWlStatCcq = _UbntWlStatCcq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 7),
    _UbntWlStatCcq_Type()
)
ubntWlStatCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatCcq.setStatus("current")
_UbntWlStatNoiseFloor_Type = Integer32
_UbntWlStatNoiseFloor_Object = MibTableColumn
ubntWlStatNoiseFloor = _UbntWlStatNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 8),
    _UbntWlStatNoiseFloor_Type()
)
ubntWlStatNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatNoiseFloor.setStatus("current")
_UbntWlStatTxRate_Type = Integer32
_UbntWlStatTxRate_Object = MibTableColumn
ubntWlStatTxRate = _UbntWlStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 9),
    _UbntWlStatTxRate_Type()
)
ubntWlStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatTxRate.setStatus("current")
_UbntWlStatRxRate_Type = Integer32
_UbntWlStatRxRate_Object = MibTableColumn
ubntWlStatRxRate = _UbntWlStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 10),
    _UbntWlStatRxRate_Type()
)
ubntWlStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatRxRate.setStatus("current")
_UbntWlStatSecurity_Type = DisplayString
_UbntWlStatSecurity_Object = MibTableColumn
ubntWlStatSecurity = _UbntWlStatSecurity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 11),
    _UbntWlStatSecurity_Type()
)
ubntWlStatSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatSecurity.setStatus("current")
_UbntWlStatWdsEnabled_Type = TruthValue
_UbntWlStatWdsEnabled_Object = MibTableColumn
ubntWlStatWdsEnabled = _UbntWlStatWdsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 12),
    _UbntWlStatWdsEnabled_Type()
)
ubntWlStatWdsEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatWdsEnabled.setStatus("current")
_UbntWlStatApRepeater_Type = TruthValue
_UbntWlStatApRepeater_Object = MibTableColumn
ubntWlStatApRepeater = _UbntWlStatApRepeater_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 13),
    _UbntWlStatApRepeater_Type()
)
ubntWlStatApRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatApRepeater.setStatus("current")
_UbntWlStatChanWidth_Type = Integer32
_UbntWlStatChanWidth_Object = MibTableColumn
ubntWlStatChanWidth = _UbntWlStatChanWidth_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 14),
    _UbntWlStatChanWidth_Type()
)
ubntWlStatChanWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatChanWidth.setStatus("current")
_UbntWlStatStaCount_Type = Gauge32
_UbntWlStatStaCount_Object = MibTableColumn
ubntWlStatStaCount = _UbntWlStatStaCount_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 5, 1, 15),
    _UbntWlStatStaCount_Type()
)
ubntWlStatStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntWlStatStaCount.setStatus("current")
_UbntAirMaxTable_Object = MibTable
ubntAirMaxTable = _UbntAirMaxTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ubntAirMaxTable.setStatus("current")
_UbntAirMaxEntry_Object = MibTableRow
ubntAirMaxEntry = _UbntAirMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1)
)
ubntAirMaxEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntAirMaxIfIndex"),
)
if mibBuilder.loadTexts:
    ubntAirMaxEntry.setStatus("current")


class _UbntAirMaxIfIndex_Type(Integer32):
    """Custom type ubntAirMaxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UbntAirMaxIfIndex_Type.__name__ = "Integer32"
_UbntAirMaxIfIndex_Object = MibTableColumn
ubntAirMaxIfIndex = _UbntAirMaxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 1),
    _UbntAirMaxIfIndex_Type()
)
ubntAirMaxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntAirMaxIfIndex.setStatus("current")
_UbntAirMaxEnabled_Type = TruthValue
_UbntAirMaxEnabled_Object = MibTableColumn
ubntAirMaxEnabled = _UbntAirMaxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 2),
    _UbntAirMaxEnabled_Type()
)
ubntAirMaxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxEnabled.setStatus("current")


class _UbntAirMaxQuality_Type(Integer32):
    """Custom type ubntAirMaxQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirMaxQuality_Type.__name__ = "Integer32"
_UbntAirMaxQuality_Object = MibTableColumn
ubntAirMaxQuality = _UbntAirMaxQuality_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 3),
    _UbntAirMaxQuality_Type()
)
ubntAirMaxQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxQuality.setStatus("current")


class _UbntAirMaxCapacity_Type(Integer32):
    """Custom type ubntAirMaxCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UbntAirMaxCapacity_Type.__name__ = "Integer32"
_UbntAirMaxCapacity_Object = MibTableColumn
ubntAirMaxCapacity = _UbntAirMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 4),
    _UbntAirMaxCapacity_Type()
)
ubntAirMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxCapacity.setStatus("current")


class _UbntAirMaxPriority_Type(Integer32):
    """Custom type ubntAirMaxPriority based on Integer32"""
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
        *(("high", 0),
          ("low", 2),
          ("medium", 1),
          ("none", 3))
    )


_UbntAirMaxPriority_Type.__name__ = "Integer32"
_UbntAirMaxPriority_Object = MibTableColumn
ubntAirMaxPriority = _UbntAirMaxPriority_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 5),
    _UbntAirMaxPriority_Type()
)
ubntAirMaxPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxPriority.setStatus("current")
_UbntAirMaxNoAck_Type = TruthValue
_UbntAirMaxNoAck_Object = MibTableColumn
ubntAirMaxNoAck = _UbntAirMaxNoAck_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 6, 1, 6),
    _UbntAirMaxNoAck_Type()
)
ubntAirMaxNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntAirMaxNoAck.setStatus("current")
_UbntStaTable_Object = MibTable
ubntStaTable = _UbntStaTable_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ubntStaTable.setStatus("current")
_UbntStaEntry_Object = MibTableRow
ubntStaEntry = _UbntStaEntry_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1)
)
ubntStaEntry.setIndexNames(
    (0, "UBNT-AirMAX-MIB", "ubntWlStatIndex"),
    (0, "UBNT-AirMAX-MIB", "ubntStaMac"),
)
if mibBuilder.loadTexts:
    ubntStaEntry.setStatus("current")
_UbntStaMac_Type = MacAddress
_UbntStaMac_Object = MibTableColumn
ubntStaMac = _UbntStaMac_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 1),
    _UbntStaMac_Type()
)
ubntStaMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ubntStaMac.setStatus("current")
_UbntStaName_Type = DisplayString
_UbntStaName_Object = MibTableColumn
ubntStaName = _UbntStaName_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 2),
    _UbntStaName_Type()
)
ubntStaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaName.setStatus("current")
_UbntStaSignal_Type = Integer32
_UbntStaSignal_Object = MibTableColumn
ubntStaSignal = _UbntStaSignal_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 3),
    _UbntStaSignal_Type()
)
ubntStaSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaSignal.setStatus("current")
_UbntStaNoiseFloor_Type = Integer32
_UbntStaNoiseFloor_Object = MibTableColumn
ubntStaNoiseFloor = _UbntStaNoiseFloor_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 4),
    _UbntStaNoiseFloor_Type()
)
ubntStaNoiseFloor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaNoiseFloor.setStatus("current")


class _UbntStaDistance_Type(Integer32):
    """Custom type ubntStaDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UbntStaDistance_Type.__name__ = "Integer32"
_UbntStaDistance_Object = MibTableColumn
ubntStaDistance = _UbntStaDistance_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 5),
    _UbntStaDistance_Type()
)
ubntStaDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaDistance.setStatus("current")
_UbntStaCcq_Type = Integer32
_UbntStaCcq_Object = MibTableColumn
ubntStaCcq = _UbntStaCcq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 6),
    _UbntStaCcq_Type()
)
ubntStaCcq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaCcq.setStatus("current")
_UbntStaAmp_Type = Integer32
_UbntStaAmp_Object = MibTableColumn
ubntStaAmp = _UbntStaAmp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 7),
    _UbntStaAmp_Type()
)
ubntStaAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmp.setStatus("current")
_UbntStaAmq_Type = Integer32
_UbntStaAmq_Object = MibTableColumn
ubntStaAmq = _UbntStaAmq_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 8),
    _UbntStaAmq_Type()
)
ubntStaAmq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmq.setStatus("current")
_UbntStaAmc_Type = Integer32
_UbntStaAmc_Object = MibTableColumn
ubntStaAmc = _UbntStaAmc_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 9),
    _UbntStaAmc_Type()
)
ubntStaAmc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaAmc.setStatus("current")
_UbntStaLastIp_Type = IpAddress
_UbntStaLastIp_Object = MibTableColumn
ubntStaLastIp = _UbntStaLastIp_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 10),
    _UbntStaLastIp_Type()
)
ubntStaLastIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaLastIp.setStatus("current")
_UbntStaTxRate_Type = Integer32
_UbntStaTxRate_Object = MibTableColumn
ubntStaTxRate = _UbntStaTxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 11),
    _UbntStaTxRate_Type()
)
ubntStaTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxRate.setStatus("current")
_UbntStaRxRate_Type = Integer32
_UbntStaRxRate_Object = MibTableColumn
ubntStaRxRate = _UbntStaRxRate_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 12),
    _UbntStaRxRate_Type()
)
ubntStaRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxRate.setStatus("current")
_UbntStaTxBytes_Type = Counter64
_UbntStaTxBytes_Object = MibTableColumn
ubntStaTxBytes = _UbntStaTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 13),
    _UbntStaTxBytes_Type()
)
ubntStaTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxBytes.setStatus("current")
_UbntStaRxBytes_Type = Counter64
_UbntStaRxBytes_Object = MibTableColumn
ubntStaRxBytes = _UbntStaRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 14),
    _UbntStaRxBytes_Type()
)
ubntStaRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxBytes.setStatus("current")
_UbntStaConnTime_Type = TimeTicks
_UbntStaConnTime_Object = MibTableColumn
ubntStaConnTime = _UbntStaConnTime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 15),
    _UbntStaConnTime_Type()
)
ubntStaConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaConnTime.setStatus("current")
_UbntStaLocalCINR_Type = Integer32
_UbntStaLocalCINR_Object = MibTableColumn
ubntStaLocalCINR = _UbntStaLocalCINR_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 16),
    _UbntStaLocalCINR_Type()
)
ubntStaLocalCINR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaLocalCINR.setStatus("current")
_UbntStaTxCapacity_Type = Integer32
_UbntStaTxCapacity_Object = MibTableColumn
ubntStaTxCapacity = _UbntStaTxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 17),
    _UbntStaTxCapacity_Type()
)
ubntStaTxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxCapacity.setStatus("current")
_UbntStaRxCapacity_Type = Integer32
_UbntStaRxCapacity_Object = MibTableColumn
ubntStaRxCapacity = _UbntStaRxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 18),
    _UbntStaRxCapacity_Type()
)
ubntStaRxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxCapacity.setStatus("current")
_UbntStaTxAirtime_Type = Integer32
_UbntStaTxAirtime_Object = MibTableColumn
ubntStaTxAirtime = _UbntStaTxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 19),
    _UbntStaTxAirtime_Type()
)
ubntStaTxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxAirtime.setStatus("current")
_UbntStaRxAirtime_Type = Integer32
_UbntStaRxAirtime_Object = MibTableColumn
ubntStaRxAirtime = _UbntStaRxAirtime_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 20),
    _UbntStaRxAirtime_Type()
)
ubntStaRxAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaRxAirtime.setStatus("current")
_UbntStaTxLatency_Type = Integer32
_UbntStaTxLatency_Object = MibTableColumn
ubntStaTxLatency = _UbntStaTxLatency_Object(
    (1, 3, 6, 1, 4, 1, 41112, 1, 4, 7, 1, 21),
    _UbntStaTxLatency_Type()
)
ubntStaTxLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ubntStaTxLatency.setStatus("current")

# Managed Objects groups

ubntAirMAXStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 1)
)
ubntAirMAXStatusGroup.setObjects(
      *(("UBNT-AirMAX-MIB", "ubntStaName"),
        ("UBNT-AirMAX-MIB", "ubntStaSignal"),
        ("UBNT-AirMAX-MIB", "ubntStaNoiseFloor"),
        ("UBNT-AirMAX-MIB", "ubntStaDistance"),
        ("UBNT-AirMAX-MIB", "ubntStaCcq"),
        ("UBNT-AirMAX-MIB", "ubntStaAmp"),
        ("UBNT-AirMAX-MIB", "ubntStaAmq"),
        ("UBNT-AirMAX-MIB", "ubntStaAmc"),
        ("UBNT-AirMAX-MIB", "ubntStaLastIp"),
        ("UBNT-AirMAX-MIB", "ubntStaTxRate"),
        ("UBNT-AirMAX-MIB", "ubntStaRxRate"),
        ("UBNT-AirMAX-MIB", "ubntStaTxBytes"),
        ("UBNT-AirMAX-MIB", "ubntStaRxBytes"),
        ("UBNT-AirMAX-MIB", "ubntStaConnTime"),
        ("UBNT-AirMAX-MIB", "ubntStaLocalCINR"),
        ("UBNT-AirMAX-MIB", "ubntStaTxCapacity"),
        ("UBNT-AirMAX-MIB", "ubntStaRxCapacity"),
        ("UBNT-AirMAX-MIB", "ubntStaTxAirtime"),
        ("UBNT-AirMAX-MIB", "ubntStaRxAirtime"),
        ("UBNT-AirMAX-MIB", "ubntStaTxLatency"),
        ("UBNT-AirMAX-MIB", "ubntRadioMode"),
        ("UBNT-AirMAX-MIB", "ubntRadioCCode"),
        ("UBNT-AirMAX-MIB", "ubntRadioFreq"),
        ("UBNT-AirMAX-MIB", "ubntRadioDfsEnabled"),
        ("UBNT-AirMAX-MIB", "ubntRadioTxPower"),
        ("UBNT-AirMAX-MIB", "ubntRadioDistance"),
        ("UBNT-AirMAX-MIB", "ubntRadioChainmask"),
        ("UBNT-AirMAX-MIB", "ubntRadioAntenna"),
        ("UBNT-AirMAX-MIB", "ubntRadioRssi"),
        ("UBNT-AirMAX-MIB", "ubntRadioRssiMgmt"),
        ("UBNT-AirMAX-MIB", "ubntRadioRssiExt"),
        ("UBNT-AirMAX-MIB", "ubntAirMaxEnabled"),
        ("UBNT-AirMAX-MIB", "ubntAirMaxQuality"),
        ("UBNT-AirMAX-MIB", "ubntAirMaxCapacity"),
        ("UBNT-AirMAX-MIB", "ubntAirMaxPriority"),
        ("UBNT-AirMAX-MIB", "ubntAirMaxNoAck"),
        ("UBNT-AirMAX-MIB", "ubntAirSyncMode"),
        ("UBNT-AirMAX-MIB", "ubntAirSyncCount"),
        ("UBNT-AirMAX-MIB", "ubntAirSyncDownUtil"),
        ("UBNT-AirMAX-MIB", "ubntAirSyncUpUtil"),
        ("UBNT-AirMAX-MIB", "ubntAirSelEnabled"),
        ("UBNT-AirMAX-MIB", "ubntAirSelInterval"),
        ("UBNT-AirMAX-MIB", "ubntWlStatSsid"),
        ("UBNT-AirMAX-MIB", "ubntWlStatHideSsid"),
        ("UBNT-AirMAX-MIB", "ubntWlStatApMac"),
        ("UBNT-AirMAX-MIB", "ubntWlStatSignal"),
        ("UBNT-AirMAX-MIB", "ubntWlStatRssi"),
        ("UBNT-AirMAX-MIB", "ubntWlStatCcq"),
        ("UBNT-AirMAX-MIB", "ubntWlStatNoiseFloor"),
        ("UBNT-AirMAX-MIB", "ubntWlStatTxRate"),
        ("UBNT-AirMAX-MIB", "ubntWlStatRxRate"),
        ("UBNT-AirMAX-MIB", "ubntWlStatSecurity"),
        ("UBNT-AirMAX-MIB", "ubntWlStatWdsEnabled"),
        ("UBNT-AirMAX-MIB", "ubntWlStatApRepeater"),
        ("UBNT-AirMAX-MIB", "ubntWlStatChanWidth"),
        ("UBNT-AirMAX-MIB", "ubntWlStatStaCount"))
)
if mibBuilder.loadTexts:
    ubntAirMAXStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ubntAirMAXStatusCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 41112, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ubntAirMAXStatusCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UBNT-AirMAX-MIB",
    **{"ubntAirMAXStatusGroup": ubntAirMAXStatusGroup,
       "ubntAirMAXStatusCompliance": ubntAirMAXStatusCompliance,
       "ubntAirMAX": ubntAirMAX,
       "ubntRadioTable": ubntRadioTable,
       "ubntRadioEntry": ubntRadioEntry,
       "ubntRadioIndex": ubntRadioIndex,
       "ubntRadioMode": ubntRadioMode,
       "ubntRadioCCode": ubntRadioCCode,
       "ubntRadioFreq": ubntRadioFreq,
       "ubntRadioDfsEnabled": ubntRadioDfsEnabled,
       "ubntRadioTxPower": ubntRadioTxPower,
       "ubntRadioDistance": ubntRadioDistance,
       "ubntRadioChainmask": ubntRadioChainmask,
       "ubntRadioAntenna": ubntRadioAntenna,
       "ubntRadioRssiTable": ubntRadioRssiTable,
       "ubntRadioRssiEntry": ubntRadioRssiEntry,
       "ubntRadioRssiIndex": ubntRadioRssiIndex,
       "ubntRadioRssi": ubntRadioRssi,
       "ubntRadioRssiMgmt": ubntRadioRssiMgmt,
       "ubntRadioRssiExt": ubntRadioRssiExt,
       "ubntAirSyncTable": ubntAirSyncTable,
       "ubntAirSyncEntry": ubntAirSyncEntry,
       "ubntAirSyncIfIndex": ubntAirSyncIfIndex,
       "ubntAirSyncMode": ubntAirSyncMode,
       "ubntAirSyncCount": ubntAirSyncCount,
       "ubntAirSyncDownUtil": ubntAirSyncDownUtil,
       "ubntAirSyncUpUtil": ubntAirSyncUpUtil,
       "ubntAirSelTable": ubntAirSelTable,
       "ubntAirSelEntry": ubntAirSelEntry,
       "ubntAirSelIfIndex": ubntAirSelIfIndex,
       "ubntAirSelEnabled": ubntAirSelEnabled,
       "ubntAirSelInterval": ubntAirSelInterval,
       "ubntWlStatTable": ubntWlStatTable,
       "ubntWlStatEntry": ubntWlStatEntry,
       "ubntWlStatIndex": ubntWlStatIndex,
       "ubntWlStatSsid": ubntWlStatSsid,
       "ubntWlStatHideSsid": ubntWlStatHideSsid,
       "ubntWlStatApMac": ubntWlStatApMac,
       "ubntWlStatSignal": ubntWlStatSignal,
       "ubntWlStatRssi": ubntWlStatRssi,
       "ubntWlStatCcq": ubntWlStatCcq,
       "ubntWlStatNoiseFloor": ubntWlStatNoiseFloor,
       "ubntWlStatTxRate": ubntWlStatTxRate,
       "ubntWlStatRxRate": ubntWlStatRxRate,
       "ubntWlStatSecurity": ubntWlStatSecurity,
       "ubntWlStatWdsEnabled": ubntWlStatWdsEnabled,
       "ubntWlStatApRepeater": ubntWlStatApRepeater,
       "ubntWlStatChanWidth": ubntWlStatChanWidth,
       "ubntWlStatStaCount": ubntWlStatStaCount,
       "ubntAirMaxTable": ubntAirMaxTable,
       "ubntAirMaxEntry": ubntAirMaxEntry,
       "ubntAirMaxIfIndex": ubntAirMaxIfIndex,
       "ubntAirMaxEnabled": ubntAirMaxEnabled,
       "ubntAirMaxQuality": ubntAirMaxQuality,
       "ubntAirMaxCapacity": ubntAirMaxCapacity,
       "ubntAirMaxPriority": ubntAirMaxPriority,
       "ubntAirMaxNoAck": ubntAirMaxNoAck,
       "ubntStaTable": ubntStaTable,
       "ubntStaEntry": ubntStaEntry,
       "ubntStaMac": ubntStaMac,
       "ubntStaName": ubntStaName,
       "ubntStaSignal": ubntStaSignal,
       "ubntStaNoiseFloor": ubntStaNoiseFloor,
       "ubntStaDistance": ubntStaDistance,
       "ubntStaCcq": ubntStaCcq,
       "ubntStaAmp": ubntStaAmp,
       "ubntStaAmq": ubntStaAmq,
       "ubntStaAmc": ubntStaAmc,
       "ubntStaLastIp": ubntStaLastIp,
       "ubntStaTxRate": ubntStaTxRate,
       "ubntStaRxRate": ubntStaRxRate,
       "ubntStaTxBytes": ubntStaTxBytes,
       "ubntStaRxBytes": ubntStaRxBytes,
       "ubntStaConnTime": ubntStaConnTime,
       "ubntStaLocalCINR": ubntStaLocalCINR,
       "ubntStaTxCapacity": ubntStaTxCapacity,
       "ubntStaRxCapacity": ubntStaRxCapacity,
       "ubntStaTxAirtime": ubntStaTxAirtime,
       "ubntStaRxAirtime": ubntStaRxAirtime,
       "ubntStaTxLatency": ubntStaTxLatency}
)
