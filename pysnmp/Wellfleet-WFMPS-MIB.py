# SNMP MIB module (Wellfleet-WFMPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-WFMPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:31 2024
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

(wfmpsObjects,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfmpsObjects")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfmpsEntryTable_Object = MibTable
wfmpsEntryTable = _WfmpsEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1)
)
if mibBuilder.loadTexts:
    wfmpsEntryTable.setStatus("mandatory")
_WfmpsEntry_Object = MibTableRow
wfmpsEntry = _WfmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1)
)
wfmpsEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsSlot"),
)
if mibBuilder.loadTexts:
    wfmpsEntry.setStatus("mandatory")


class _WfmpsDelete_Type(Integer32):
    """Custom type wfmpsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfmpsDelete_Type.__name__ = "Integer32"
_WfmpsDelete_Object = MibTableColumn
wfmpsDelete = _WfmpsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 1),
    _WfmpsDelete_Type()
)
wfmpsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDelete.setStatus("mandatory")


class _WfmpsDisable_Type(Integer32):
    """Custom type wfmpsDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsDisable_Type.__name__ = "Integer32"
_WfmpsDisable_Object = MibTableColumn
wfmpsDisable = _WfmpsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 2),
    _WfmpsDisable_Type()
)
wfmpsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDisable.setStatus("mandatory")
_WfmpsSlot_Type = Integer32
_WfmpsSlot_Object = MibTableColumn
wfmpsSlot = _WfmpsSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 3),
    _WfmpsSlot_Type()
)
wfmpsSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsSlot.setStatus("mandatory")
_WfmpsCct_Type = Integer32
_WfmpsCct_Object = MibTableColumn
wfmpsCct = _WfmpsCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 4),
    _WfmpsCct_Type()
)
wfmpsCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsCct.setStatus("mandatory")


class _WfmpsCacheIpOverRide_Type(Integer32):
    """Custom type wfmpsCacheIpOverRide based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfmpsCacheIpOverRide_Type.__name__ = "Integer32"
_WfmpsCacheIpOverRide_Object = MibTableColumn
wfmpsCacheIpOverRide = _WfmpsCacheIpOverRide_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 5),
    _WfmpsCacheIpOverRide_Type()
)
wfmpsCacheIpOverRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsCacheIpOverRide.setStatus("mandatory")


class _WfmpsCacheReverifyTimer_Type(Integer32):
    """Custom type wfmpsCacheReverifyTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              180,
              240,
              300,
              600,
              900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("timer120", 120),
          ("timer1200", 1200),
          ("timer180", 180),
          ("timer240", 240),
          ("timer300", 300),
          ("timer600", 600),
          ("timer900", 900),
          ("timeroff", 1))
    )


_WfmpsCacheReverifyTimer_Type.__name__ = "Integer32"
_WfmpsCacheReverifyTimer_Object = MibTableColumn
wfmpsCacheReverifyTimer = _WfmpsCacheReverifyTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 6),
    _WfmpsCacheReverifyTimer_Type()
)
wfmpsCacheReverifyTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsCacheReverifyTimer.setStatus("mandatory")


class _WfmpsAddrGenerateMode_Type(Integer32):
    """Custom type wfmpsAddrGenerateMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_WfmpsAddrGenerateMode_Type.__name__ = "Integer32"
_WfmpsAddrGenerateMode_Object = MibTableColumn
wfmpsAddrGenerateMode = _WfmpsAddrGenerateMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 1, 1, 7),
    _WfmpsAddrGenerateMode_Type()
)
wfmpsAddrGenerateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsAddrGenerateMode.setStatus("mandatory")
_WfmpsConfigTable_Object = MibTable
wfmpsConfigTable = _WfmpsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2)
)
if mibBuilder.loadTexts:
    wfmpsConfigTable.setStatus("mandatory")
_WfmpsConfigEntry_Object = MibTableRow
wfmpsConfigEntry = _WfmpsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1)
)
wfmpsConfigEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsCnfSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsCnfIndex"),
)
if mibBuilder.loadTexts:
    wfmpsConfigEntry.setStatus("mandatory")


class _WfmpsCnfDelete_Type(Integer32):
    """Custom type wfmpsCnfDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfmpsCnfDelete_Type.__name__ = "Integer32"
_WfmpsCnfDelete_Object = MibTableColumn
wfmpsCnfDelete = _WfmpsCnfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 1),
    _WfmpsCnfDelete_Type()
)
wfmpsCnfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsCnfDelete.setStatus("mandatory")


class _WfmpsRowStatus_Type(Integer32):
    """Custom type wfmpsRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsRowStatus_Type.__name__ = "Integer32"
_WfmpsRowStatus_Object = MibTableColumn
wfmpsRowStatus = _WfmpsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 2),
    _WfmpsRowStatus_Type()
)
wfmpsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsRowStatus.setStatus("mandatory")
_WfmpsCnfIndex_Type = Integer32
_WfmpsCnfIndex_Object = MibTableColumn
wfmpsCnfIndex = _WfmpsCnfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 3),
    _WfmpsCnfIndex_Type()
)
wfmpsCnfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsCnfIndex.setStatus("mandatory")


class _WfmpsConfigMode_Type(Integer32):
    """Custom type wfmpsConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_WfmpsConfigMode_Type.__name__ = "Integer32"
_WfmpsConfigMode_Object = MibTableColumn
wfmpsConfigMode = _WfmpsConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 4),
    _WfmpsConfigMode_Type()
)
wfmpsConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsConfigMode.setStatus("mandatory")


class _WfmpsCtrlAtmAddr_Type(OctetString):
    """Custom type wfmpsCtrlAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfmpsCtrlAtmAddr_Type.__name__ = "OctetString"
_WfmpsCtrlAtmAddr_Object = MibTableColumn
wfmpsCtrlAtmAddr = _WfmpsCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 5),
    _WfmpsCtrlAtmAddr_Type()
)
wfmpsCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsCtrlAtmAddr.setStatus("mandatory")


class _WfmpsKeepAliveTime_Type(Integer32):
    """Custom type wfmpsKeepAliveTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WfmpsKeepAliveTime_Type.__name__ = "Integer32"
_WfmpsKeepAliveTime_Object = MibTableColumn
wfmpsKeepAliveTime = _WfmpsKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 6),
    _WfmpsKeepAliveTime_Type()
)
wfmpsKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsKeepAliveTime.setStatus("mandatory")


class _WfmpsKeepAliveLifeTime_Type(Integer32):
    """Custom type wfmpsKeepAliveLifeTime based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_WfmpsKeepAliveLifeTime_Type.__name__ = "Integer32"
_WfmpsKeepAliveLifeTime_Object = MibTableColumn
wfmpsKeepAliveLifeTime = _WfmpsKeepAliveLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 7),
    _WfmpsKeepAliveLifeTime_Type()
)
wfmpsKeepAliveLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsKeepAliveLifeTime.setStatus("mandatory")


class _WfmpsInitialRetryTime_Type(Integer32):
    """Custom type wfmpsInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WfmpsInitialRetryTime_Type.__name__ = "Integer32"
_WfmpsInitialRetryTime_Object = MibTableColumn
wfmpsInitialRetryTime = _WfmpsInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 8),
    _WfmpsInitialRetryTime_Type()
)
wfmpsInitialRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsInitialRetryTime.setStatus("mandatory")


class _WfmpsRetryTimeMaximum_Type(Integer32):
    """Custom type wfmpsRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_WfmpsRetryTimeMaximum_Type.__name__ = "Integer32"
_WfmpsRetryTimeMaximum_Object = MibTableColumn
wfmpsRetryTimeMaximum = _WfmpsRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 9),
    _WfmpsRetryTimeMaximum_Type()
)
wfmpsRetryTimeMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsRetryTimeMaximum.setStatus("mandatory")


class _WfmpsGiveupTime_Type(Integer32):
    """Custom type wfmpsGiveupTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_WfmpsGiveupTime_Type.__name__ = "Integer32"
_WfmpsGiveupTime_Object = MibTableColumn
wfmpsGiveupTime = _WfmpsGiveupTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 10),
    _WfmpsGiveupTime_Type()
)
wfmpsGiveupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsGiveupTime.setStatus("mandatory")


class _WfmpsDefaultHoldingTime_Type(Integer32):
    """Custom type wfmpsDefaultHoldingTime based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfmpsDefaultHoldingTime_Type.__name__ = "Integer32"
_WfmpsDefaultHoldingTime_Object = MibTableColumn
wfmpsDefaultHoldingTime = _WfmpsDefaultHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 11),
    _WfmpsDefaultHoldingTime_Type()
)
wfmpsDefaultHoldingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDefaultHoldingTime.setStatus("mandatory")
_WfmpsCnfSlot_Type = Integer32
_WfmpsCnfSlot_Object = MibTableColumn
wfmpsCnfSlot = _WfmpsCnfSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 12),
    _WfmpsCnfSlot_Type()
)
wfmpsCnfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsCnfSlot.setStatus("mandatory")


class _WfmpsInitialCacheSize_Type(Integer32):
    """Custom type wfmpsInitialCacheSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 500),
    )


_WfmpsInitialCacheSize_Type.__name__ = "Integer32"
_WfmpsInitialCacheSize_Object = MibTableColumn
wfmpsInitialCacheSize = _WfmpsInitialCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 13),
    _WfmpsInitialCacheSize_Type()
)
wfmpsInitialCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsInitialCacheSize.setStatus("mandatory")


class _WfmpsMaxCacheSize_Type(Integer32):
    """Custom type wfmpsMaxCacheSize based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000),
    )


_WfmpsMaxCacheSize_Type.__name__ = "Integer32"
_WfmpsMaxCacheSize_Object = MibTableColumn
wfmpsMaxCacheSize = _WfmpsMaxCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 14),
    _WfmpsMaxCacheSize_Type()
)
wfmpsMaxCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMaxCacheSize.setStatus("mandatory")


class _WfmpsLECSAddress_Type(OctetString):
    """Custom type wfmpsLECSAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfmpsLECSAddress_Type.__name__ = "OctetString"
_WfmpsLECSAddress_Object = MibTableColumn
wfmpsLECSAddress = _WfmpsLECSAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 15),
    _WfmpsLECSAddress_Type()
)
wfmpsLECSAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsLECSAddress.setStatus("mandatory")


class _WfmpsDebugMsgLevel_Type(Integer32):
    """Custom type wfmpsDebugMsgLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WfmpsDebugMsgLevel_Type.__name__ = "Integer32"
_WfmpsDebugMsgLevel_Object = MibTableColumn
wfmpsDebugMsgLevel = _WfmpsDebugMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 16),
    _WfmpsDebugMsgLevel_Type()
)
wfmpsDebugMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugMsgLevel.setStatus("mandatory")
_WfmpsConfigMpsName_Type = DisplayString
_WfmpsConfigMpsName_Object = MibTableColumn
wfmpsConfigMpsName = _WfmpsConfigMpsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 2, 1, 17),
    _WfmpsConfigMpsName_Type()
)
wfmpsConfigMpsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsConfigMpsName.setStatus("mandatory")
_WfmpsActualTable_Object = MibTable
wfmpsActualTable = _WfmpsActualTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3)
)
if mibBuilder.loadTexts:
    wfmpsActualTable.setStatus("mandatory")
_WfmpsActualEntry_Object = MibTableRow
wfmpsActualEntry = _WfmpsActualEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1)
)
wfmpsActualEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsActSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsActIndex"),
)
if mibBuilder.loadTexts:
    wfmpsActualEntry.setStatus("mandatory")
_WfmpsActIndex_Type = Integer32
_WfmpsActIndex_Object = MibTableColumn
wfmpsActIndex = _WfmpsActIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 1),
    _WfmpsActIndex_Type()
)
wfmpsActIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActIndex.setStatus("mandatory")


class _WfmpsActualState_Type(Integer32):
    """Custom type wfmpsActualState based on Integer32"""
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
        *(("down", 4),
          ("initialState", 2),
          ("unknown", 3),
          ("up", 1))
    )


_WfmpsActualState_Type.__name__ = "Integer32"
_WfmpsActualState_Object = MibTableColumn
wfmpsActualState = _WfmpsActualState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 2),
    _WfmpsActualState_Type()
)
wfmpsActualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualState.setStatus("mandatory")
_WfmpsDiscontinuityTime_Type = TimeTicks
_WfmpsDiscontinuityTime_Object = MibTableColumn
wfmpsDiscontinuityTime = _WfmpsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 3),
    _WfmpsDiscontinuityTime_Type()
)
wfmpsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsDiscontinuityTime.setStatus("mandatory")


class _WfmpsActualConfigMode_Type(Integer32):
    """Custom type wfmpsActualConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_WfmpsActualConfigMode_Type.__name__ = "Integer32"
_WfmpsActualConfigMode_Object = MibTableColumn
wfmpsActualConfigMode = _WfmpsActualConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 4),
    _WfmpsActualConfigMode_Type()
)
wfmpsActualConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualConfigMode.setStatus("mandatory")
_WfmpsActualKeepAlive_Type = Integer32
_WfmpsActualKeepAlive_Object = MibTableColumn
wfmpsActualKeepAlive = _WfmpsActualKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 5),
    _WfmpsActualKeepAlive_Type()
)
wfmpsActualKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualKeepAlive.setStatus("mandatory")
_WfmpsActualKeepAliveLifeTime_Type = Integer32
_WfmpsActualKeepAliveLifeTime_Object = MibTableColumn
wfmpsActualKeepAliveLifeTime = _WfmpsActualKeepAliveLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 6),
    _WfmpsActualKeepAliveLifeTime_Type()
)
wfmpsActualKeepAliveLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualKeepAliveLifeTime.setStatus("mandatory")


class _WfmpsActualInitialRetryTime_Type(Integer32):
    """Custom type wfmpsActualInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_WfmpsActualInitialRetryTime_Type.__name__ = "Integer32"
_WfmpsActualInitialRetryTime_Object = MibTableColumn
wfmpsActualInitialRetryTime = _WfmpsActualInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 7),
    _WfmpsActualInitialRetryTime_Type()
)
wfmpsActualInitialRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualInitialRetryTime.setStatus("mandatory")


class _WfmpsActualRetryTimeMaximum_Type(Integer32):
    """Custom type wfmpsActualRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_WfmpsActualRetryTimeMaximum_Type.__name__ = "Integer32"
_WfmpsActualRetryTimeMaximum_Object = MibTableColumn
wfmpsActualRetryTimeMaximum = _WfmpsActualRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 8),
    _WfmpsActualRetryTimeMaximum_Type()
)
wfmpsActualRetryTimeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualRetryTimeMaximum.setStatus("mandatory")


class _WfmpsActualGiveupTime_Type(Integer32):
    """Custom type wfmpsActualGiveupTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_WfmpsActualGiveupTime_Type.__name__ = "Integer32"
_WfmpsActualGiveupTime_Object = MibTableColumn
wfmpsActualGiveupTime = _WfmpsActualGiveupTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 9),
    _WfmpsActualGiveupTime_Type()
)
wfmpsActualGiveupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualGiveupTime.setStatus("mandatory")


class _WfmpsActualDefaultHoldingTime_Type(Integer32):
    """Custom type wfmpsActualDefaultHoldingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_WfmpsActualDefaultHoldingTime_Type.__name__ = "Integer32"
_WfmpsActualDefaultHoldingTime_Object = MibTableColumn
wfmpsActualDefaultHoldingTime = _WfmpsActualDefaultHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 10),
    _WfmpsActualDefaultHoldingTime_Type()
)
wfmpsActualDefaultHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualDefaultHoldingTime.setStatus("mandatory")
_WfmpsActSlot_Type = Integer32
_WfmpsActSlot_Object = MibTableColumn
wfmpsActSlot = _WfmpsActSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 11),
    _WfmpsActSlot_Type()
)
wfmpsActSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActSlot.setStatus("mandatory")


class _WfmpsActualCtrlAtmAddr_Type(OctetString):
    """Custom type wfmpsActualCtrlAtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_WfmpsActualCtrlAtmAddr_Type.__name__ = "OctetString"
_WfmpsActualCtrlAtmAddr_Object = MibTableColumn
wfmpsActualCtrlAtmAddr = _WfmpsActualCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 3, 1, 12),
    _WfmpsActualCtrlAtmAddr_Type()
)
wfmpsActualCtrlAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsActualCtrlAtmAddr.setStatus("mandatory")
_WfmpsStatisticsTable_Object = MibTable
wfmpsStatisticsTable = _WfmpsStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4)
)
if mibBuilder.loadTexts:
    wfmpsStatisticsTable.setStatus("mandatory")
_WfmpsStatisticsEntry_Object = MibTableRow
wfmpsStatisticsEntry = _WfmpsStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1)
)
wfmpsStatisticsEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsStatSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsStatIndex"),
)
if mibBuilder.loadTexts:
    wfmpsStatisticsEntry.setStatus("mandatory")
_WfmpsStatIndex_Type = Integer32
_WfmpsStatIndex_Object = MibTableColumn
wfmpsStatIndex = _WfmpsStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 1),
    _WfmpsStatIndex_Type()
)
wfmpsStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatIndex.setStatus("mandatory")
_WfmpsStatRxMpoaResolveRequests_Type = Counter32
_WfmpsStatRxMpoaResolveRequests_Object = MibTableColumn
wfmpsStatRxMpoaResolveRequests = _WfmpsStatRxMpoaResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 2),
    _WfmpsStatRxMpoaResolveRequests_Type()
)
wfmpsStatRxMpoaResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaResolveRequests.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyAcks_Type = Counter32
_WfmpsStatTxMpoaResolveReplyAcks_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyAcks = _WfmpsStatTxMpoaResolveReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 3),
    _WfmpsStatTxMpoaResolveReplyAcks_Type()
)
wfmpsStatTxMpoaResolveReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyAcks.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyInsufECResources_Type = Counter32
_WfmpsStatTxMpoaResolveReplyInsufECResources_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyInsufECResources = _WfmpsStatTxMpoaResolveReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 4),
    _WfmpsStatTxMpoaResolveReplyInsufECResources_Type()
)
wfmpsStatTxMpoaResolveReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyInsufECResources.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyInsufSCResources_Type = Counter32
_WfmpsStatTxMpoaResolveReplyInsufSCResources_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyInsufSCResources = _WfmpsStatTxMpoaResolveReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 5),
    _WfmpsStatTxMpoaResolveReplyInsufSCResources_Type()
)
wfmpsStatTxMpoaResolveReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyInsufSCResources.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyInsufEitherResources_Type = Counter32
_WfmpsStatTxMpoaResolveReplyInsufEitherResources_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyInsufEitherResources = _WfmpsStatTxMpoaResolveReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 6),
    _WfmpsStatTxMpoaResolveReplyInsufEitherResources_Type()
)
wfmpsStatTxMpoaResolveReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyInsufEitherResources.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyUnsupportedInetProt_Type = Counter32
_WfmpsStatTxMpoaResolveReplyUnsupportedInetProt_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyUnsupportedInetProt = _WfmpsStatTxMpoaResolveReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 7),
    _WfmpsStatTxMpoaResolveReplyUnsupportedInetProt_Type()
)
wfmpsStatTxMpoaResolveReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyUnsupportedInetProt.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Type = Counter32
_WfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps = _WfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 8),
    _WfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps_Type()
)
wfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyUnspecifiedOther_Type = Counter32
_WfmpsStatTxMpoaResolveReplyUnspecifiedOther_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyUnspecifiedOther = _WfmpsStatTxMpoaResolveReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 9),
    _WfmpsStatTxMpoaResolveReplyUnspecifiedOther_Type()
)
wfmpsStatTxMpoaResolveReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyUnspecifiedOther.setStatus("mandatory")
_WfmpsStatTxMpoaResolveReplyOther_Type = Counter32
_WfmpsStatTxMpoaResolveReplyOther_Object = MibTableColumn
wfmpsStatTxMpoaResolveReplyOther = _WfmpsStatTxMpoaResolveReplyOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 10),
    _WfmpsStatTxMpoaResolveReplyOther_Type()
)
wfmpsStatTxMpoaResolveReplyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaResolveReplyOther.setStatus("mandatory")
_WfmpsStatGiveupTimeExpireds_Type = Counter32
_WfmpsStatGiveupTimeExpireds_Object = MibTableColumn
wfmpsStatGiveupTimeExpireds = _WfmpsStatGiveupTimeExpireds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 11),
    _WfmpsStatGiveupTimeExpireds_Type()
)
wfmpsStatGiveupTimeExpireds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatGiveupTimeExpireds.setStatus("mandatory")
_WfmpsStatTxMpoaImpRequests_Type = Counter32
_WfmpsStatTxMpoaImpRequests_Object = MibTableColumn
wfmpsStatTxMpoaImpRequests = _WfmpsStatTxMpoaImpRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 12),
    _WfmpsStatTxMpoaImpRequests_Type()
)
wfmpsStatTxMpoaImpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaImpRequests.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyAcks_Type = Counter32
_WfmpsStatRxMpoaImpReplyAcks_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyAcks = _WfmpsStatRxMpoaImpReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 13),
    _WfmpsStatRxMpoaImpReplyAcks_Type()
)
wfmpsStatRxMpoaImpReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyAcks.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyInsufECResources_Type = Counter32
_WfmpsStatRxMpoaImpReplyInsufECResources_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyInsufECResources = _WfmpsStatRxMpoaImpReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 14),
    _WfmpsStatRxMpoaImpReplyInsufECResources_Type()
)
wfmpsStatRxMpoaImpReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyInsufECResources.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyInsufSCResources_Type = Counter32
_WfmpsStatRxMpoaImpReplyInsufSCResources_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyInsufSCResources = _WfmpsStatRxMpoaImpReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 15),
    _WfmpsStatRxMpoaImpReplyInsufSCResources_Type()
)
wfmpsStatRxMpoaImpReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyInsufSCResources.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyInsufEitherResources_Type = Counter32
_WfmpsStatRxMpoaImpReplyInsufEitherResources_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyInsufEitherResources = _WfmpsStatRxMpoaImpReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 16),
    _WfmpsStatRxMpoaImpReplyInsufEitherResources_Type()
)
wfmpsStatRxMpoaImpReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyInsufEitherResources.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyUnsupportedInetProt_Type = Counter32
_WfmpsStatRxMpoaImpReplyUnsupportedInetProt_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyUnsupportedInetProt = _WfmpsStatRxMpoaImpReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 17),
    _WfmpsStatRxMpoaImpReplyUnsupportedInetProt_Type()
)
wfmpsStatRxMpoaImpReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyUnsupportedInetProt.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyUnsupportedMacEncaps_Type = Counter32
_WfmpsStatRxMpoaImpReplyUnsupportedMacEncaps_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyUnsupportedMacEncaps = _WfmpsStatRxMpoaImpReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 18),
    _WfmpsStatRxMpoaImpReplyUnsupportedMacEncaps_Type()
)
wfmpsStatRxMpoaImpReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyUnsupportedMacEncaps.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyUnspecifiedOther_Type = Counter32
_WfmpsStatRxMpoaImpReplyUnspecifiedOther_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyUnspecifiedOther = _WfmpsStatRxMpoaImpReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 19),
    _WfmpsStatRxMpoaImpReplyUnspecifiedOther_Type()
)
wfmpsStatRxMpoaImpReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyUnspecifiedOther.setStatus("mandatory")
_WfmpsStatRxMpoaImpReplyOther_Type = Counter32
_WfmpsStatRxMpoaImpReplyOther_Object = MibTableColumn
wfmpsStatRxMpoaImpReplyOther = _WfmpsStatRxMpoaImpReplyOther_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 20),
    _WfmpsStatRxMpoaImpReplyOther_Type()
)
wfmpsStatRxMpoaImpReplyOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaImpReplyOther.setStatus("mandatory")
_WfmpsStatRxMpoaEgressCachePurgeRequests_Type = Counter32
_WfmpsStatRxMpoaEgressCachePurgeRequests_Object = MibTableColumn
wfmpsStatRxMpoaEgressCachePurgeRequests = _WfmpsStatRxMpoaEgressCachePurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 21),
    _WfmpsStatRxMpoaEgressCachePurgeRequests_Type()
)
wfmpsStatRxMpoaEgressCachePurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxMpoaEgressCachePurgeRequests.setStatus("mandatory")
_WfmpsStatTxMpoaEgressCachePurgeReplies_Type = Counter32
_WfmpsStatTxMpoaEgressCachePurgeReplies_Object = MibTableColumn
wfmpsStatTxMpoaEgressCachePurgeReplies = _WfmpsStatTxMpoaEgressCachePurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 22),
    _WfmpsStatTxMpoaEgressCachePurgeReplies_Type()
)
wfmpsStatTxMpoaEgressCachePurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaEgressCachePurgeReplies.setStatus("mandatory")
_WfmpsStatTxMpoaTriggers_Type = Counter32
_WfmpsStatTxMpoaTriggers_Object = MibTableColumn
wfmpsStatTxMpoaTriggers = _WfmpsStatTxMpoaTriggers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 23),
    _WfmpsStatTxMpoaTriggers_Type()
)
wfmpsStatTxMpoaTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxMpoaTriggers.setStatus("mandatory")
_WfmpsStatTxNhrpResolveRequests_Type = Counter32
_WfmpsStatTxNhrpResolveRequests_Object = MibTableColumn
wfmpsStatTxNhrpResolveRequests = _WfmpsStatTxNhrpResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 24),
    _WfmpsStatTxNhrpResolveRequests_Type()
)
wfmpsStatTxNhrpResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxNhrpResolveRequests.setStatus("mandatory")
_WfmpsStatRxNhrpResolveReplies_Type = Counter32
_WfmpsStatRxNhrpResolveReplies_Object = MibTableColumn
wfmpsStatRxNhrpResolveReplies = _WfmpsStatRxNhrpResolveReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 25),
    _WfmpsStatRxNhrpResolveReplies_Type()
)
wfmpsStatRxNhrpResolveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxNhrpResolveReplies.setStatus("mandatory")
_WfmpsStatRxNhrpResolveRequests_Type = Counter32
_WfmpsStatRxNhrpResolveRequests_Object = MibTableColumn
wfmpsStatRxNhrpResolveRequests = _WfmpsStatRxNhrpResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 26),
    _WfmpsStatRxNhrpResolveRequests_Type()
)
wfmpsStatRxNhrpResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatRxNhrpResolveRequests.setStatus("mandatory")
_WfmpsStatTxNhrpResolveReplies_Type = Counter32
_WfmpsStatTxNhrpResolveReplies_Object = MibTableColumn
wfmpsStatTxNhrpResolveReplies = _WfmpsStatTxNhrpResolveReplies_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 27),
    _WfmpsStatTxNhrpResolveReplies_Type()
)
wfmpsStatTxNhrpResolveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatTxNhrpResolveReplies.setStatus("mandatory")
_WfmpsStatSlot_Type = Integer32
_WfmpsStatSlot_Object = MibTableColumn
wfmpsStatSlot = _WfmpsStatSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 4, 1, 28),
    _WfmpsStatSlot_Type()
)
wfmpsStatSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsStatSlot.setStatus("mandatory")
_WfmpsProtocolTable_Object = MibTable
wfmpsProtocolTable = _WfmpsProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5)
)
if mibBuilder.loadTexts:
    wfmpsProtocolTable.setStatus("mandatory")
_WfmpsProtocolEntry_Object = MibTableRow
wfmpsProtocolEntry = _WfmpsProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1)
)
wfmpsProtocolEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsProtSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsProtIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsInternetworkLayerProtocol"),
)
if mibBuilder.loadTexts:
    wfmpsProtocolEntry.setStatus("mandatory")


class _WfmpsProtocolDelete_Type(Integer32):
    """Custom type wfmpsProtocolDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfmpsProtocolDelete_Type.__name__ = "Integer32"
_WfmpsProtocolDelete_Object = MibTableColumn
wfmpsProtocolDelete = _WfmpsProtocolDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 1),
    _WfmpsProtocolDelete_Type()
)
wfmpsProtocolDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsProtocolDelete.setStatus("mandatory")


class _WfmpsProtocolRowStatus_Type(Integer32):
    """Custom type wfmpsProtocolRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsProtocolRowStatus_Type.__name__ = "Integer32"
_WfmpsProtocolRowStatus_Object = MibTableColumn
wfmpsProtocolRowStatus = _WfmpsProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 2),
    _WfmpsProtocolRowStatus_Type()
)
wfmpsProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsProtocolRowStatus.setStatus("mandatory")
_WfmpsProtIndex_Type = Integer32
_WfmpsProtIndex_Object = MibTableColumn
wfmpsProtIndex = _WfmpsProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 3),
    _WfmpsProtIndex_Type()
)
wfmpsProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsProtIndex.setStatus("mandatory")
_WfmpsInternetworkLayerProtocol_Type = OctetString
_WfmpsInternetworkLayerProtocol_Object = MibTableColumn
wfmpsInternetworkLayerProtocol = _WfmpsInternetworkLayerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 4),
    _WfmpsInternetworkLayerProtocol_Type()
)
wfmpsInternetworkLayerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsInternetworkLayerProtocol.setStatus("mandatory")
_WfmpsLECSValue_Type = Integer32
_WfmpsLECSValue_Object = MibTableColumn
wfmpsLECSValue = _WfmpsLECSValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 5),
    _WfmpsLECSValue_Type()
)
wfmpsLECSValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsLECSValue.setStatus("mandatory")
_WfmpsProtSlot_Type = Integer32
_WfmpsProtSlot_Object = MibTableColumn
wfmpsProtSlot = _WfmpsProtSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 5, 1, 6),
    _WfmpsProtSlot_Type()
)
wfmpsProtSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsProtSlot.setStatus("mandatory")
_WfmpsMappingTable_Object = MibTable
wfmpsMappingTable = _WfmpsMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6)
)
if mibBuilder.loadTexts:
    wfmpsMappingTable.setStatus("mandatory")
_WfmpsMappingEntry_Object = MibTableRow
wfmpsMappingEntry = _WfmpsMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1)
)
wfmpsMappingEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpslecIndex"),
)
if mibBuilder.loadTexts:
    wfmpsMappingEntry.setStatus("mandatory")


class _WfmpsMappingDelete_Type(Integer32):
    """Custom type wfmpsMappingDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfmpsMappingDelete_Type.__name__ = "Integer32"
_WfmpsMappingDelete_Object = MibTableColumn
wfmpsMappingDelete = _WfmpsMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1, 1),
    _WfmpsMappingDelete_Type()
)
wfmpsMappingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMappingDelete.setStatus("mandatory")


class _WfmpsMappingRowStatus_Type(Integer32):
    """Custom type wfmpsMappingRowStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsMappingRowStatus_Type.__name__ = "Integer32"
_WfmpsMappingRowStatus_Object = MibTableColumn
wfmpsMappingRowStatus = _WfmpsMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1, 2),
    _WfmpsMappingRowStatus_Type()
)
wfmpsMappingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMappingRowStatus.setStatus("mandatory")
_WfmpslecIndex_Type = Integer32
_WfmpslecIndex_Object = MibTableColumn
wfmpslecIndex = _WfmpslecIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1, 3),
    _WfmpslecIndex_Type()
)
wfmpslecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpslecIndex.setStatus("mandatory")
_WfmpsMapIndex_Type = Integer32
_WfmpsMapIndex_Object = MibTableColumn
wfmpsMapIndex = _WfmpsMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1, 4),
    _WfmpsMapIndex_Type()
)
wfmpsMapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMapIndex.setStatus("mandatory")
_WfmpsMapSlot_Type = Integer32
_WfmpsMapSlot_Object = MibTableColumn
wfmpsMapSlot = _WfmpsMapSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 6, 1, 5),
    _WfmpsMapSlot_Type()
)
wfmpsMapSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMapSlot.setStatus("mandatory")
_WfmpsIngressCacheTable_Object = MibTable
wfmpsIngressCacheTable = _WfmpsIngressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7)
)
if mibBuilder.loadTexts:
    wfmpsIngressCacheTable.setStatus("mandatory")
_WfmpsIngressCacheEntry_Object = MibTableRow
wfmpsIngressCacheEntry = _WfmpsIngressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1)
)
wfmpsIngressCacheEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsIngressSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsIngressIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsIngressMpcIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsIngressCacheDestInternetworkAddrType"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsIngressCacheDestAddr"),
)
if mibBuilder.loadTexts:
    wfmpsIngressCacheEntry.setStatus("mandatory")
_WfmpsIngressIndex_Type = Integer32
_WfmpsIngressIndex_Object = MibTableColumn
wfmpsIngressIndex = _WfmpsIngressIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 1),
    _WfmpsIngressIndex_Type()
)
wfmpsIngressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressIndex.setStatus("mandatory")
_WfmpsIngressMpcIndex_Type = Integer32
_WfmpsIngressMpcIndex_Object = MibTableColumn
wfmpsIngressMpcIndex = _WfmpsIngressMpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 2),
    _WfmpsIngressMpcIndex_Type()
)
wfmpsIngressMpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressMpcIndex.setStatus("mandatory")
_WfmpsIngressCacheDestInternetworkAddrType_Type = Integer32
_WfmpsIngressCacheDestInternetworkAddrType_Object = MibTableColumn
wfmpsIngressCacheDestInternetworkAddrType = _WfmpsIngressCacheDestInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 3),
    _WfmpsIngressCacheDestInternetworkAddrType_Type()
)
wfmpsIngressCacheDestInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheDestInternetworkAddrType.setStatus("mandatory")


class _WfmpsIngressCacheDestAddr_Type(OctetString):
    """Custom type wfmpsIngressCacheDestAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfmpsIngressCacheDestAddr_Type.__name__ = "OctetString"
_WfmpsIngressCacheDestAddr_Object = MibTableColumn
wfmpsIngressCacheDestAddr = _WfmpsIngressCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 4),
    _WfmpsIngressCacheDestAddr_Type()
)
wfmpsIngressCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheDestAddr.setStatus("mandatory")
_WfmpsIngressCachePrefixLen_Type = Integer32
_WfmpsIngressCachePrefixLen_Object = MibTableColumn
wfmpsIngressCachePrefixLen = _WfmpsIngressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 5),
    _WfmpsIngressCachePrefixLen_Type()
)
wfmpsIngressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCachePrefixLen.setStatus("mandatory")


class _WfmpsIngressCacheState_Type(Integer32):
    """Custom type wfmpsIngressCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_WfmpsIngressCacheState_Type.__name__ = "Integer32"
_WfmpsIngressCacheState_Object = MibTableColumn
wfmpsIngressCacheState = _WfmpsIngressCacheState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 6),
    _WfmpsIngressCacheState_Type()
)
wfmpsIngressCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheState.setStatus("mandatory")
_WfmpsIngressCacheSrcInternetworkAddrType_Type = Integer32
_WfmpsIngressCacheSrcInternetworkAddrType_Object = MibTableColumn
wfmpsIngressCacheSrcInternetworkAddrType = _WfmpsIngressCacheSrcInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 7),
    _WfmpsIngressCacheSrcInternetworkAddrType_Type()
)
wfmpsIngressCacheSrcInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheSrcInternetworkAddrType.setStatus("mandatory")
_WfmpsIngressCacheSrcAddr_Type = OctetString
_WfmpsIngressCacheSrcAddr_Object = MibTableColumn
wfmpsIngressCacheSrcAddr = _WfmpsIngressCacheSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 8),
    _WfmpsIngressCacheSrcAddr_Type()
)
wfmpsIngressCacheSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheSrcAddr.setStatus("mandatory")
_WfmpsIngressCacheSourceMpcAtmAddr_Type = OctetString
_WfmpsIngressCacheSourceMpcAtmAddr_Object = MibTableColumn
wfmpsIngressCacheSourceMpcAtmAddr = _WfmpsIngressCacheSourceMpcAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 9),
    _WfmpsIngressCacheSourceMpcAtmAddr_Type()
)
wfmpsIngressCacheSourceMpcAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheSourceMpcAtmAddr.setStatus("mandatory")
_WfmpsIngressCacheResolvedAtmAddr_Type = OctetString
_WfmpsIngressCacheResolvedAtmAddr_Object = MibTableColumn
wfmpsIngressCacheResolvedAtmAddr = _WfmpsIngressCacheResolvedAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 10),
    _WfmpsIngressCacheResolvedAtmAddr_Type()
)
wfmpsIngressCacheResolvedAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheResolvedAtmAddr.setStatus("mandatory")
_WfmpsIngressCacheHoldTime_Type = Integer32
_WfmpsIngressCacheHoldTime_Object = MibTableColumn
wfmpsIngressCacheHoldTime = _WfmpsIngressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 11),
    _WfmpsIngressCacheHoldTime_Type()
)
wfmpsIngressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheHoldTime.setStatus("mandatory")
_WfmpsIngressCacheMpoaRequestId_Type = Integer32
_WfmpsIngressCacheMpoaRequestId_Object = MibTableColumn
wfmpsIngressCacheMpoaRequestId = _WfmpsIngressCacheMpoaRequestId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 12),
    _WfmpsIngressCacheMpoaRequestId_Type()
)
wfmpsIngressCacheMpoaRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheMpoaRequestId.setStatus("mandatory")
_WfmpsIngressCacheNhrpRequestId_Type = Integer32
_WfmpsIngressCacheNhrpRequestId_Object = MibTableColumn
wfmpsIngressCacheNhrpRequestId = _WfmpsIngressCacheNhrpRequestId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 13),
    _WfmpsIngressCacheNhrpRequestId_Type()
)
wfmpsIngressCacheNhrpRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheNhrpRequestId.setStatus("mandatory")
_WfmpsIngressCacheServiceCategory_Type = Integer32
_WfmpsIngressCacheServiceCategory_Object = MibTableColumn
wfmpsIngressCacheServiceCategory = _WfmpsIngressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 14),
    _WfmpsIngressCacheServiceCategory_Type()
)
wfmpsIngressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressCacheServiceCategory.setStatus("mandatory")
_WfmpsIngressSlot_Type = Integer32
_WfmpsIngressSlot_Object = MibTableColumn
wfmpsIngressSlot = _WfmpsIngressSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 7, 1, 15),
    _WfmpsIngressSlot_Type()
)
wfmpsIngressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsIngressSlot.setStatus("mandatory")
_WfmpsEgressCacheTable_Object = MibTable
wfmpsEgressCacheTable = _WfmpsEgressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8)
)
if mibBuilder.loadTexts:
    wfmpsEgressCacheTable.setStatus("mandatory")
_WfmpsEgressCacheEntry_Object = MibTableRow
wfmpsEgressCacheEntry = _WfmpsEgressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1)
)
wfmpsEgressCacheEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsEgressSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsEgressIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsEgressMpcIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsEgressCacheId"),
)
if mibBuilder.loadTexts:
    wfmpsEgressCacheEntry.setStatus("mandatory")
_WfmpsEgressIndex_Type = Integer32
_WfmpsEgressIndex_Object = MibTableColumn
wfmpsEgressIndex = _WfmpsEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 1),
    _WfmpsEgressIndex_Type()
)
wfmpsEgressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressIndex.setStatus("mandatory")
_WfmpsEgressMpcIndex_Type = Integer32
_WfmpsEgressMpcIndex_Object = MibTableColumn
wfmpsEgressMpcIndex = _WfmpsEgressMpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 2),
    _WfmpsEgressMpcIndex_Type()
)
wfmpsEgressMpcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressMpcIndex.setStatus("mandatory")
_WfmpsEgressCacheId_Type = Integer32
_WfmpsEgressCacheId_Object = MibTableColumn
wfmpsEgressCacheId = _WfmpsEgressCacheId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 3),
    _WfmpsEgressCacheId_Type()
)
wfmpsEgressCacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheId.setStatus("mandatory")
_WfmpsEgressCacheHoldTime_Type = Integer32
_WfmpsEgressCacheHoldTime_Object = MibTableColumn
wfmpsEgressCacheHoldTime = _WfmpsEgressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 4),
    _WfmpsEgressCacheHoldTime_Type()
)
wfmpsEgressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheHoldTime.setStatus("mandatory")


class _WfmpsEgressCacheState_Type(Integer32):
    """Custom type wfmpsEgressCacheState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_WfmpsEgressCacheState_Type.__name__ = "Integer32"
_WfmpsEgressCacheState_Object = MibTableColumn
wfmpsEgressCacheState = _WfmpsEgressCacheState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 5),
    _WfmpsEgressCacheState_Type()
)
wfmpsEgressCacheState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheState.setStatus("mandatory")
_WfmpsEgressCacheDataLinkHeader_Type = OctetString
_WfmpsEgressCacheDataLinkHeader_Object = MibTableColumn
wfmpsEgressCacheDataLinkHeader = _WfmpsEgressCacheDataLinkHeader_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 6),
    _WfmpsEgressCacheDataLinkHeader_Type()
)
wfmpsEgressCacheDataLinkHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheDataLinkHeader.setStatus("mandatory")
_WfmpsEgressCacheElanId_Type = Integer32
_WfmpsEgressCacheElanId_Object = MibTableColumn
wfmpsEgressCacheElanId = _WfmpsEgressCacheElanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 7),
    _WfmpsEgressCacheElanId_Type()
)
wfmpsEgressCacheElanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheElanId.setStatus("mandatory")
_WfmpsEgressCacheSourceClientAtmAddr_Type = OctetString
_WfmpsEgressCacheSourceClientAtmAddr_Object = MibTableColumn
wfmpsEgressCacheSourceClientAtmAddr = _WfmpsEgressCacheSourceClientAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 8),
    _WfmpsEgressCacheSourceClientAtmAddr_Type()
)
wfmpsEgressCacheSourceClientAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheSourceClientAtmAddr.setStatus("mandatory")
_WfmpsEgressCacheNhrpRequestId_Type = Integer32
_WfmpsEgressCacheNhrpRequestId_Object = MibTableColumn
wfmpsEgressCacheNhrpRequestId = _WfmpsEgressCacheNhrpRequestId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 9),
    _WfmpsEgressCacheNhrpRequestId_Type()
)
wfmpsEgressCacheNhrpRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheNhrpRequestId.setStatus("mandatory")
_WfmpsEgressCacheMpoaRequestId_Type = Integer32
_WfmpsEgressCacheMpoaRequestId_Object = MibTableColumn
wfmpsEgressCacheMpoaRequestId = _WfmpsEgressCacheMpoaRequestId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 10),
    _WfmpsEgressCacheMpoaRequestId_Type()
)
wfmpsEgressCacheMpoaRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheMpoaRequestId.setStatus("mandatory")
_WfmpsEgressCacheServiceCategory_Type = Integer32
_WfmpsEgressCacheServiceCategory_Object = MibTableColumn
wfmpsEgressCacheServiceCategory = _WfmpsEgressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 11),
    _WfmpsEgressCacheServiceCategory_Type()
)
wfmpsEgressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheServiceCategory.setStatus("mandatory")
_WfmpsEgressCacheNextHopInternetworkAddrType_Type = Integer32
_WfmpsEgressCacheNextHopInternetworkAddrType_Object = MibTableColumn
wfmpsEgressCacheNextHopInternetworkAddrType = _WfmpsEgressCacheNextHopInternetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 12),
    _WfmpsEgressCacheNextHopInternetworkAddrType_Type()
)
wfmpsEgressCacheNextHopInternetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheNextHopInternetworkAddrType.setStatus("mandatory")
_WfmpsEgressCacheNextHopAddr_Type = OctetString
_WfmpsEgressCacheNextHopAddr_Object = MibTableColumn
wfmpsEgressCacheNextHopAddr = _WfmpsEgressCacheNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 13),
    _WfmpsEgressCacheNextHopAddr_Type()
)
wfmpsEgressCacheNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressCacheNextHopAddr.setStatus("mandatory")
_WfmpsEgressSlot_Type = Integer32
_WfmpsEgressSlot_Object = MibTableColumn
wfmpsEgressSlot = _WfmpsEgressSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 8, 1, 14),
    _WfmpsEgressSlot_Type()
)
wfmpsEgressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsEgressSlot.setStatus("mandatory")
_WfmpsMpcTable_Object = MibTable
wfmpsMpcTable = _WfmpsMpcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9)
)
if mibBuilder.loadTexts:
    wfmpsMpcTable.setStatus("mandatory")
_WfmpsMpcEntry_Object = MibTableRow
wfmpsMpcEntry = _WfmpsMpcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9, 1)
)
wfmpsMpcEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsMpcSlot"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsMpsIndex"),
    (0, "Wellfleet-WFMPS-MIB", "wfmpsMpcIndex"),
)
if mibBuilder.loadTexts:
    wfmpsMpcEntry.setStatus("mandatory")
_WfmpsMpsIndex_Type = Integer32
_WfmpsMpsIndex_Object = MibTableColumn
wfmpsMpsIndex = _WfmpsMpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9, 1, 1),
    _WfmpsMpsIndex_Type()
)
wfmpsMpsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsMpsIndex.setStatus("mandatory")
_WfmpsMpcIndex_Type = Integer32
_WfmpsMpcIndex_Object = MibTableColumn
wfmpsMpcIndex = _WfmpsMpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9, 1, 2),
    _WfmpsMpcIndex_Type()
)
wfmpsMpcIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMpcIndex.setStatus("mandatory")
_WfmpsMpcCtrlAtmAddr_Type = OctetString
_WfmpsMpcCtrlAtmAddr_Object = MibTableColumn
wfmpsMpcCtrlAtmAddr = _WfmpsMpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9, 1, 3),
    _WfmpsMpcCtrlAtmAddr_Type()
)
wfmpsMpcCtrlAtmAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMpcCtrlAtmAddr.setStatus("mandatory")
_WfmpsMpcSlot_Type = Integer32
_WfmpsMpcSlot_Object = MibTableColumn
wfmpsMpcSlot = _WfmpsMpcSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 9, 1, 4),
    _WfmpsMpcSlot_Type()
)
wfmpsMpcSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsMpcSlot.setStatus("mandatory")
_WfmpsDebugTable_Object = MibTable
wfmpsDebugTable = _WfmpsDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10)
)
if mibBuilder.loadTexts:
    wfmpsDebugTable.setStatus("mandatory")
_WfmpsDebugEntry_Object = MibTableRow
wfmpsDebugEntry = _WfmpsDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1)
)
wfmpsDebugEntry.setIndexNames(
    (0, "Wellfleet-WFMPS-MIB", "wfmpsDebugSlot"),
)
if mibBuilder.loadTexts:
    wfmpsDebugEntry.setStatus("mandatory")
_WfmpsDebugSlot_Type = Integer32
_WfmpsDebugSlot_Object = MibTableColumn
wfmpsDebugSlot = _WfmpsDebugSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 1),
    _WfmpsDebugSlot_Type()
)
wfmpsDebugSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfmpsDebugSlot.setStatus("mandatory")
_WfmpsDebugIndex_Type = Integer32
_WfmpsDebugIndex_Object = MibTableColumn
wfmpsDebugIndex = _WfmpsDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 2),
    _WfmpsDebugIndex_Type()
)
wfmpsDebugIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugIndex.setStatus("mandatory")


class _WfmpsDebugDestGid_Type(Integer32):
    """Custom type wfmpsDebugDestGid based on Integer32"""
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
        *(("mpsCtrl", 2),
          ("mpsMstr", 4),
          ("mpsProc", 1),
          ("mpsVCC", 3))
    )


_WfmpsDebugDestGid_Type.__name__ = "Integer32"
_WfmpsDebugDestGid_Object = MibTableColumn
wfmpsDebugDestGid = _WfmpsDebugDestGid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 3),
    _WfmpsDebugDestGid_Type()
)
wfmpsDebugDestGid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugDestGid.setStatus("mandatory")
_WfmpsDebugMsg_Type = OctetString
_WfmpsDebugMsg_Object = MibTableColumn
wfmpsDebugMsg = _WfmpsDebugMsg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 4),
    _WfmpsDebugMsg_Type()
)
wfmpsDebugMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugMsg.setStatus("mandatory")


class _WfmpsDebugSendEnable_Type(Integer32):
    """Custom type wfmpsDebugSendEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsDebugSendEnable_Type.__name__ = "Integer32"
_WfmpsDebugSendEnable_Object = MibTableColumn
wfmpsDebugSendEnable = _WfmpsDebugSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 5),
    _WfmpsDebugSendEnable_Type()
)
wfmpsDebugSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugSendEnable.setStatus("mandatory")
_WfmpsDebugSignalNum_Type = Integer32
_WfmpsDebugSignalNum_Object = MibTableColumn
wfmpsDebugSignalNum = _WfmpsDebugSignalNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 6),
    _WfmpsDebugSignalNum_Type()
)
wfmpsDebugSignalNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugSignalNum.setStatus("mandatory")


class _WfmpsDebugSignalSendEnable_Type(Integer32):
    """Custom type wfmpsDebugSignalSendEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfmpsDebugSignalSendEnable_Type.__name__ = "Integer32"
_WfmpsDebugSignalSendEnable_Object = MibTableColumn
wfmpsDebugSignalSendEnable = _WfmpsDebugSignalSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 10, 10, 1, 7),
    _WfmpsDebugSignalSendEnable_Type()
)
wfmpsDebugSignalSendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfmpsDebugSignalSendEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-WFMPS-MIB",
    **{"wfmpsEntryTable": wfmpsEntryTable,
       "wfmpsEntry": wfmpsEntry,
       "wfmpsDelete": wfmpsDelete,
       "wfmpsDisable": wfmpsDisable,
       "wfmpsSlot": wfmpsSlot,
       "wfmpsCct": wfmpsCct,
       "wfmpsCacheIpOverRide": wfmpsCacheIpOverRide,
       "wfmpsCacheReverifyTimer": wfmpsCacheReverifyTimer,
       "wfmpsAddrGenerateMode": wfmpsAddrGenerateMode,
       "wfmpsConfigTable": wfmpsConfigTable,
       "wfmpsConfigEntry": wfmpsConfigEntry,
       "wfmpsCnfDelete": wfmpsCnfDelete,
       "wfmpsRowStatus": wfmpsRowStatus,
       "wfmpsCnfIndex": wfmpsCnfIndex,
       "wfmpsConfigMode": wfmpsConfigMode,
       "wfmpsCtrlAtmAddr": wfmpsCtrlAtmAddr,
       "wfmpsKeepAliveTime": wfmpsKeepAliveTime,
       "wfmpsKeepAliveLifeTime": wfmpsKeepAliveLifeTime,
       "wfmpsInitialRetryTime": wfmpsInitialRetryTime,
       "wfmpsRetryTimeMaximum": wfmpsRetryTimeMaximum,
       "wfmpsGiveupTime": wfmpsGiveupTime,
       "wfmpsDefaultHoldingTime": wfmpsDefaultHoldingTime,
       "wfmpsCnfSlot": wfmpsCnfSlot,
       "wfmpsInitialCacheSize": wfmpsInitialCacheSize,
       "wfmpsMaxCacheSize": wfmpsMaxCacheSize,
       "wfmpsLECSAddress": wfmpsLECSAddress,
       "wfmpsDebugMsgLevel": wfmpsDebugMsgLevel,
       "wfmpsConfigMpsName": wfmpsConfigMpsName,
       "wfmpsActualTable": wfmpsActualTable,
       "wfmpsActualEntry": wfmpsActualEntry,
       "wfmpsActIndex": wfmpsActIndex,
       "wfmpsActualState": wfmpsActualState,
       "wfmpsDiscontinuityTime": wfmpsDiscontinuityTime,
       "wfmpsActualConfigMode": wfmpsActualConfigMode,
       "wfmpsActualKeepAlive": wfmpsActualKeepAlive,
       "wfmpsActualKeepAliveLifeTime": wfmpsActualKeepAliveLifeTime,
       "wfmpsActualInitialRetryTime": wfmpsActualInitialRetryTime,
       "wfmpsActualRetryTimeMaximum": wfmpsActualRetryTimeMaximum,
       "wfmpsActualGiveupTime": wfmpsActualGiveupTime,
       "wfmpsActualDefaultHoldingTime": wfmpsActualDefaultHoldingTime,
       "wfmpsActSlot": wfmpsActSlot,
       "wfmpsActualCtrlAtmAddr": wfmpsActualCtrlAtmAddr,
       "wfmpsStatisticsTable": wfmpsStatisticsTable,
       "wfmpsStatisticsEntry": wfmpsStatisticsEntry,
       "wfmpsStatIndex": wfmpsStatIndex,
       "wfmpsStatRxMpoaResolveRequests": wfmpsStatRxMpoaResolveRequests,
       "wfmpsStatTxMpoaResolveReplyAcks": wfmpsStatTxMpoaResolveReplyAcks,
       "wfmpsStatTxMpoaResolveReplyInsufECResources": wfmpsStatTxMpoaResolveReplyInsufECResources,
       "wfmpsStatTxMpoaResolveReplyInsufSCResources": wfmpsStatTxMpoaResolveReplyInsufSCResources,
       "wfmpsStatTxMpoaResolveReplyInsufEitherResources": wfmpsStatTxMpoaResolveReplyInsufEitherResources,
       "wfmpsStatTxMpoaResolveReplyUnsupportedInetProt": wfmpsStatTxMpoaResolveReplyUnsupportedInetProt,
       "wfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps": wfmpsStatTxMpoaResolveReplyUnsupportedMacEncaps,
       "wfmpsStatTxMpoaResolveReplyUnspecifiedOther": wfmpsStatTxMpoaResolveReplyUnspecifiedOther,
       "wfmpsStatTxMpoaResolveReplyOther": wfmpsStatTxMpoaResolveReplyOther,
       "wfmpsStatGiveupTimeExpireds": wfmpsStatGiveupTimeExpireds,
       "wfmpsStatTxMpoaImpRequests": wfmpsStatTxMpoaImpRequests,
       "wfmpsStatRxMpoaImpReplyAcks": wfmpsStatRxMpoaImpReplyAcks,
       "wfmpsStatRxMpoaImpReplyInsufECResources": wfmpsStatRxMpoaImpReplyInsufECResources,
       "wfmpsStatRxMpoaImpReplyInsufSCResources": wfmpsStatRxMpoaImpReplyInsufSCResources,
       "wfmpsStatRxMpoaImpReplyInsufEitherResources": wfmpsStatRxMpoaImpReplyInsufEitherResources,
       "wfmpsStatRxMpoaImpReplyUnsupportedInetProt": wfmpsStatRxMpoaImpReplyUnsupportedInetProt,
       "wfmpsStatRxMpoaImpReplyUnsupportedMacEncaps": wfmpsStatRxMpoaImpReplyUnsupportedMacEncaps,
       "wfmpsStatRxMpoaImpReplyUnspecifiedOther": wfmpsStatRxMpoaImpReplyUnspecifiedOther,
       "wfmpsStatRxMpoaImpReplyOther": wfmpsStatRxMpoaImpReplyOther,
       "wfmpsStatRxMpoaEgressCachePurgeRequests": wfmpsStatRxMpoaEgressCachePurgeRequests,
       "wfmpsStatTxMpoaEgressCachePurgeReplies": wfmpsStatTxMpoaEgressCachePurgeReplies,
       "wfmpsStatTxMpoaTriggers": wfmpsStatTxMpoaTriggers,
       "wfmpsStatTxNhrpResolveRequests": wfmpsStatTxNhrpResolveRequests,
       "wfmpsStatRxNhrpResolveReplies": wfmpsStatRxNhrpResolveReplies,
       "wfmpsStatRxNhrpResolveRequests": wfmpsStatRxNhrpResolveRequests,
       "wfmpsStatTxNhrpResolveReplies": wfmpsStatTxNhrpResolveReplies,
       "wfmpsStatSlot": wfmpsStatSlot,
       "wfmpsProtocolTable": wfmpsProtocolTable,
       "wfmpsProtocolEntry": wfmpsProtocolEntry,
       "wfmpsProtocolDelete": wfmpsProtocolDelete,
       "wfmpsProtocolRowStatus": wfmpsProtocolRowStatus,
       "wfmpsProtIndex": wfmpsProtIndex,
       "wfmpsInternetworkLayerProtocol": wfmpsInternetworkLayerProtocol,
       "wfmpsLECSValue": wfmpsLECSValue,
       "wfmpsProtSlot": wfmpsProtSlot,
       "wfmpsMappingTable": wfmpsMappingTable,
       "wfmpsMappingEntry": wfmpsMappingEntry,
       "wfmpsMappingDelete": wfmpsMappingDelete,
       "wfmpsMappingRowStatus": wfmpsMappingRowStatus,
       "wfmpslecIndex": wfmpslecIndex,
       "wfmpsMapIndex": wfmpsMapIndex,
       "wfmpsMapSlot": wfmpsMapSlot,
       "wfmpsIngressCacheTable": wfmpsIngressCacheTable,
       "wfmpsIngressCacheEntry": wfmpsIngressCacheEntry,
       "wfmpsIngressIndex": wfmpsIngressIndex,
       "wfmpsIngressMpcIndex": wfmpsIngressMpcIndex,
       "wfmpsIngressCacheDestInternetworkAddrType": wfmpsIngressCacheDestInternetworkAddrType,
       "wfmpsIngressCacheDestAddr": wfmpsIngressCacheDestAddr,
       "wfmpsIngressCachePrefixLen": wfmpsIngressCachePrefixLen,
       "wfmpsIngressCacheState": wfmpsIngressCacheState,
       "wfmpsIngressCacheSrcInternetworkAddrType": wfmpsIngressCacheSrcInternetworkAddrType,
       "wfmpsIngressCacheSrcAddr": wfmpsIngressCacheSrcAddr,
       "wfmpsIngressCacheSourceMpcAtmAddr": wfmpsIngressCacheSourceMpcAtmAddr,
       "wfmpsIngressCacheResolvedAtmAddr": wfmpsIngressCacheResolvedAtmAddr,
       "wfmpsIngressCacheHoldTime": wfmpsIngressCacheHoldTime,
       "wfmpsIngressCacheMpoaRequestId": wfmpsIngressCacheMpoaRequestId,
       "wfmpsIngressCacheNhrpRequestId": wfmpsIngressCacheNhrpRequestId,
       "wfmpsIngressCacheServiceCategory": wfmpsIngressCacheServiceCategory,
       "wfmpsIngressSlot": wfmpsIngressSlot,
       "wfmpsEgressCacheTable": wfmpsEgressCacheTable,
       "wfmpsEgressCacheEntry": wfmpsEgressCacheEntry,
       "wfmpsEgressIndex": wfmpsEgressIndex,
       "wfmpsEgressMpcIndex": wfmpsEgressMpcIndex,
       "wfmpsEgressCacheId": wfmpsEgressCacheId,
       "wfmpsEgressCacheHoldTime": wfmpsEgressCacheHoldTime,
       "wfmpsEgressCacheState": wfmpsEgressCacheState,
       "wfmpsEgressCacheDataLinkHeader": wfmpsEgressCacheDataLinkHeader,
       "wfmpsEgressCacheElanId": wfmpsEgressCacheElanId,
       "wfmpsEgressCacheSourceClientAtmAddr": wfmpsEgressCacheSourceClientAtmAddr,
       "wfmpsEgressCacheNhrpRequestId": wfmpsEgressCacheNhrpRequestId,
       "wfmpsEgressCacheMpoaRequestId": wfmpsEgressCacheMpoaRequestId,
       "wfmpsEgressCacheServiceCategory": wfmpsEgressCacheServiceCategory,
       "wfmpsEgressCacheNextHopInternetworkAddrType": wfmpsEgressCacheNextHopInternetworkAddrType,
       "wfmpsEgressCacheNextHopAddr": wfmpsEgressCacheNextHopAddr,
       "wfmpsEgressSlot": wfmpsEgressSlot,
       "wfmpsMpcTable": wfmpsMpcTable,
       "wfmpsMpcEntry": wfmpsMpcEntry,
       "wfmpsMpsIndex": wfmpsMpsIndex,
       "wfmpsMpcIndex": wfmpsMpcIndex,
       "wfmpsMpcCtrlAtmAddr": wfmpsMpcCtrlAtmAddr,
       "wfmpsMpcSlot": wfmpsMpcSlot,
       "wfmpsDebugTable": wfmpsDebugTable,
       "wfmpsDebugEntry": wfmpsDebugEntry,
       "wfmpsDebugSlot": wfmpsDebugSlot,
       "wfmpsDebugIndex": wfmpsDebugIndex,
       "wfmpsDebugDestGid": wfmpsDebugDestGid,
       "wfmpsDebugMsg": wfmpsDebugMsg,
       "wfmpsDebugSendEnable": wfmpsDebugSendEnable,
       "wfmpsDebugSignalNum": wfmpsDebugSignalNum,
       "wfmpsDebugSignalSendEnable": wfmpsDebugSignalSendEnable}
)
