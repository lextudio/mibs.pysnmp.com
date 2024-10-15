# SNMP MIB module (BSUSTATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BSUSTATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:46 2024
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

(bsu,) = mibBuilder.importSymbols(
    "ANIROOT-MIB",
    "bsu")

(aniBsuWirelessPort,) = mibBuilder.importSymbols(
    "BSUWIRELESSIF-MIB",
    "aniBsuWirelessPort")

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


# MODULE-IDENTITY

aniBsuStatus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _AniBsuStatusBootState_Type(Integer32):
    """Custom type aniBsuStatusBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("configf-req-sent", 3),
          ("dhcpc-req-sent", 2),
          ("operational", 6),
          ("standby", 7),
          ("starting", 1),
          ("wait-for-tod", 4),
          ("wait-for-wss", 5))
    )


_AniBsuStatusBootState_Type.__name__ = "Integer32"
_AniBsuStatusBootState_Object = MibScalar
aniBsuStatusBootState = _AniBsuStatusBootState_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 1),
    _AniBsuStatusBootState_Type()
)
aniBsuStatusBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusBootState.setStatus("current")


class _AniBsuStatusSysUpTime_Type(DisplayString):
    """Custom type aniBsuStatusSysUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_AniBsuStatusSysUpTime_Type.__name__ = "DisplayString"
_AniBsuStatusSysUpTime_Object = MibScalar
aniBsuStatusSysUpTime = _AniBsuStatusSysUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 2),
    _AniBsuStatusSysUpTime_Type()
)
aniBsuStatusSysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusSysUpTime.setStatus("current")
_AniBsuStatusNumPortsConf_Type = Integer32
_AniBsuStatusNumPortsConf_Object = MibScalar
aniBsuStatusNumPortsConf = _AniBsuStatusNumPortsConf_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 3),
    _AniBsuStatusNumPortsConf_Type()
)
aniBsuStatusNumPortsConf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusNumPortsConf.setStatus("current")
_AniBsuStatusNumPortsPresent_Type = Integer32
_AniBsuStatusNumPortsPresent_Object = MibScalar
aniBsuStatusNumPortsPresent = _AniBsuStatusNumPortsPresent_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 4),
    _AniBsuStatusNumPortsPresent_Type()
)
aniBsuStatusNumPortsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusNumPortsPresent.setStatus("current")


class _AniBsuStatusSuCounts_Type(Integer32):
    """Custom type aniBsuStatusSuCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6144),
    )


_AniBsuStatusSuCounts_Type.__name__ = "Integer32"
_AniBsuStatusSuCounts_Object = MibScalar
aniBsuStatusSuCounts = _AniBsuStatusSuCounts_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 5),
    _AniBsuStatusSuCounts_Type()
)
aniBsuStatusSuCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusSuCounts.setStatus("current")


class _AniBsuStatusCellName_Type(DisplayString):
    """Custom type aniBsuStatusCellName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AniBsuStatusCellName_Type.__name__ = "DisplayString"
_AniBsuStatusCellName_Object = MibScalar
aniBsuStatusCellName = _AniBsuStatusCellName_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 6),
    _AniBsuStatusCellName_Type()
)
aniBsuStatusCellName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusCellName.setStatus("current")


class _AniBsuStatusCellRadius_Type(Integer32):
    """Custom type aniBsuStatusCellRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10000,
              20000,
              30000,
              40000,
              50000,
              60000,
              70000,
              80000,
              90000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("radius100km", 100000),
          ("radius10km", 10000),
          ("radius20km", 20000),
          ("radius30km", 30000),
          ("radius40km", 40000),
          ("radius50km", 50000),
          ("radius60km", 60000),
          ("radius70km", 70000),
          ("radius80km", 80000),
          ("radius90km", 90000))
    )


_AniBsuStatusCellRadius_Type.__name__ = "Integer32"
_AniBsuStatusCellRadius_Object = MibScalar
aniBsuStatusCellRadius = _AniBsuStatusCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 7),
    _AniBsuStatusCellRadius_Type()
)
aniBsuStatusCellRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusCellRadius.setStatus("current")


class _AniBsuStatusSyncTimingRef_Type(Integer32):
    """Custom type aniBsuStatusSyncTimingRef based on Integer32"""
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
        *(("external", 2),
          ("internal", 1),
          ("not-applicable", 3))
    )


_AniBsuStatusSyncTimingRef_Type.__name__ = "Integer32"
_AniBsuStatusSyncTimingRef_Object = MibScalar
aniBsuStatusSyncTimingRef = _AniBsuStatusSyncTimingRef_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 8),
    _AniBsuStatusSyncTimingRef_Type()
)
aniBsuStatusSyncTimingRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusSyncTimingRef.setStatus("current")


class _AniBsuStatusRipFlag_Type(Integer32):
    """Custom type aniBsuStatusRipFlag based on Integer32"""
    defaultValue = 1

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


_AniBsuStatusRipFlag_Type.__name__ = "Integer32"
_AniBsuStatusRipFlag_Object = MibScalar
aniBsuStatusRipFlag = _AniBsuStatusRipFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 9),
    _AniBsuStatusRipFlag_Type()
)
aniBsuStatusRipFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRipFlag.setStatus("current")


class _AniBsuStatusMode_Type(Integer32):
    """Custom type aniBsuStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 2),
          ("router", 1),
          ("vlan", 3))
    )


_AniBsuStatusMode_Type.__name__ = "Integer32"
_AniBsuStatusMode_Object = MibScalar
aniBsuStatusMode = _AniBsuStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 10),
    _AniBsuStatusMode_Type()
)
aniBsuStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusMode.setStatus("current")
_AniBsuStatusRadioTable_Object = MibTable
aniBsuStatusRadioTable = _AniBsuStatusRadioTable_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11)
)
if mibBuilder.loadTexts:
    aniBsuStatusRadioTable.setStatus("current")
_AniBsuStatusRadioEntry_Object = MibTableRow
aniBsuStatusRadioEntry = _AniBsuStatusRadioEntry_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1)
)
aniBsuStatusRadioEntry.setIndexNames(
    (0, "BSUWIRELESSIF-MIB", "aniBsuWirelessPort"),
)
if mibBuilder.loadTexts:
    aniBsuStatusRadioEntry.setStatus("current")


class _AniBsuStatusRadioSerialNum_Type(DisplayString):
    """Custom type aniBsuStatusRadioSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AniBsuStatusRadioSerialNum_Type.__name__ = "DisplayString"
_AniBsuStatusRadioSerialNum_Object = MibTableColumn
aniBsuStatusRadioSerialNum = _AniBsuStatusRadioSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 1),
    _AniBsuStatusRadioSerialNum_Type()
)
aniBsuStatusRadioSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioSerialNum.setStatus("current")
_AniBsuStatusRadioFrequency_Type = DisplayString
_AniBsuStatusRadioFrequency_Object = MibTableColumn
aniBsuStatusRadioFrequency = _AniBsuStatusRadioFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 2),
    _AniBsuStatusRadioFrequency_Type()
)
aniBsuStatusRadioFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioFrequency.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuStatusRadioFrequency.setUnits("MHz")


class _AniBsuStatusRadioBand_Type(Integer32):
    """Custom type aniBsuStatusRadioBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("etsi-3-5GHz-100", 8),
          ("etsi-3-5GHz-50", 7),
          ("fdd-3-5GHz", 11),
          ("general-2-6GHz", 5),
          ("general-3-5GHz", 6),
          ("general-5-3GHz", 12),
          ("general-5-8GHz", 3),
          ("ism-5-8GHz", 10),
          ("mmds-2-6GHz", 4),
          ("unii-5-3GHz", 1),
          ("unii-5-8GHz", 2))
    )


_AniBsuStatusRadioBand_Type.__name__ = "Integer32"
_AniBsuStatusRadioBand_Object = MibTableColumn
aniBsuStatusRadioBand = _AniBsuStatusRadioBand_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 3),
    _AniBsuStatusRadioBand_Type()
)
aniBsuStatusRadioBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioBand.setStatus("current")
_AniBsuStatusRadioEepromRev_Type = DisplayString
_AniBsuStatusRadioEepromRev_Object = MibTableColumn
aniBsuStatusRadioEepromRev = _AniBsuStatusRadioEepromRev_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 4),
    _AniBsuStatusRadioEepromRev_Type()
)
aniBsuStatusRadioEepromRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioEepromRev.setStatus("current")


class _AniBsuStatusRadioVRFlag_Type(Integer32):
    """Custom type aniBsuStatusRadioVRFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-operational", 2),
          ("operational", 1))
    )


_AniBsuStatusRadioVRFlag_Type.__name__ = "Integer32"
_AniBsuStatusRadioVRFlag_Object = MibTableColumn
aniBsuStatusRadioVRFlag = _AniBsuStatusRadioVRFlag_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 5),
    _AniBsuStatusRadioVRFlag_Type()
)
aniBsuStatusRadioVRFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioVRFlag.setStatus("current")


class _AniBsuStatusRadioSynth1Lock_Type(Integer32):
    """Custom type aniBsuStatusRadioSynth1Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("not-locked", 1))
    )


_AniBsuStatusRadioSynth1Lock_Type.__name__ = "Integer32"
_AniBsuStatusRadioSynth1Lock_Object = MibTableColumn
aniBsuStatusRadioSynth1Lock = _AniBsuStatusRadioSynth1Lock_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 6),
    _AniBsuStatusRadioSynth1Lock_Type()
)
aniBsuStatusRadioSynth1Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioSynth1Lock.setStatus("current")


class _AniBsuStatusRadioSynth2Lock_Type(Integer32):
    """Custom type aniBsuStatusRadioSynth2Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("not-locked", 1))
    )


_AniBsuStatusRadioSynth2Lock_Type.__name__ = "Integer32"
_AniBsuStatusRadioSynth2Lock_Object = MibTableColumn
aniBsuStatusRadioSynth2Lock = _AniBsuStatusRadioSynth2Lock_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 7),
    _AniBsuStatusRadioSynth2Lock_Type()
)
aniBsuStatusRadioSynth2Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioSynth2Lock.setStatus("current")
_AniBsuStatusRadioTxGain_Type = DisplayString
_AniBsuStatusRadioTxGain_Object = MibTableColumn
aniBsuStatusRadioTxGain = _AniBsuStatusRadioTxGain_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 8),
    _AniBsuStatusRadioTxGain_Type()
)
aniBsuStatusRadioTxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioTxGain.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuStatusRadioTxGain.setUnits("dB")


class _AniBsuStatusRadioRxGain_Type(Integer32):
    """Custom type aniBsuStatusRadioRxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 45),
    )


_AniBsuStatusRadioRxGain_Type.__name__ = "Integer32"
_AniBsuStatusRadioRxGain_Object = MibTableColumn
aniBsuStatusRadioRxGain = _AniBsuStatusRadioRxGain_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 9),
    _AniBsuStatusRadioRxGain_Type()
)
aniBsuStatusRadioRxGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioRxGain.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuStatusRadioRxGain.setUnits("dB")
_AniBsuStatusRadioCurrentTxMaxPower_Type = DisplayString
_AniBsuStatusRadioCurrentTxMaxPower_Object = MibTableColumn
aniBsuStatusRadioCurrentTxMaxPower = _AniBsuStatusRadioCurrentTxMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 10),
    _AniBsuStatusRadioCurrentTxMaxPower_Type()
)
aniBsuStatusRadioCurrentTxMaxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioCurrentTxMaxPower.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuStatusRadioCurrentTxMaxPower.setUnits("dBm")
_AniBsuStatusRadioIfCableLoss_Type = DisplayString
_AniBsuStatusRadioIfCableLoss_Object = MibTableColumn
aniBsuStatusRadioIfCableLoss = _AniBsuStatusRadioIfCableLoss_Object(
    (1, 3, 6, 1, 4, 1, 4325, 3, 1, 11, 1, 11),
    _AniBsuStatusRadioIfCableLoss_Type()
)
aniBsuStatusRadioIfCableLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aniBsuStatusRadioIfCableLoss.setStatus("current")
if mibBuilder.loadTexts:
    aniBsuStatusRadioIfCableLoss.setUnits("dB")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BSUSTATUS-MIB",
    **{"aniBsuStatus": aniBsuStatus,
       "aniBsuStatusBootState": aniBsuStatusBootState,
       "aniBsuStatusSysUpTime": aniBsuStatusSysUpTime,
       "aniBsuStatusNumPortsConf": aniBsuStatusNumPortsConf,
       "aniBsuStatusNumPortsPresent": aniBsuStatusNumPortsPresent,
       "aniBsuStatusSuCounts": aniBsuStatusSuCounts,
       "aniBsuStatusCellName": aniBsuStatusCellName,
       "aniBsuStatusCellRadius": aniBsuStatusCellRadius,
       "aniBsuStatusSyncTimingRef": aniBsuStatusSyncTimingRef,
       "aniBsuStatusRipFlag": aniBsuStatusRipFlag,
       "aniBsuStatusMode": aniBsuStatusMode,
       "aniBsuStatusRadioTable": aniBsuStatusRadioTable,
       "aniBsuStatusRadioEntry": aniBsuStatusRadioEntry,
       "aniBsuStatusRadioSerialNum": aniBsuStatusRadioSerialNum,
       "aniBsuStatusRadioFrequency": aniBsuStatusRadioFrequency,
       "aniBsuStatusRadioBand": aniBsuStatusRadioBand,
       "aniBsuStatusRadioEepromRev": aniBsuStatusRadioEepromRev,
       "aniBsuStatusRadioVRFlag": aniBsuStatusRadioVRFlag,
       "aniBsuStatusRadioSynth1Lock": aniBsuStatusRadioSynth1Lock,
       "aniBsuStatusRadioSynth2Lock": aniBsuStatusRadioSynth2Lock,
       "aniBsuStatusRadioTxGain": aniBsuStatusRadioTxGain,
       "aniBsuStatusRadioRxGain": aniBsuStatusRadioRxGain,
       "aniBsuStatusRadioCurrentTxMaxPower": aniBsuStatusRadioCurrentTxMaxPower,
       "aniBsuStatusRadioIfCableLoss": aniBsuStatusRadioIfCableLoss}
)
