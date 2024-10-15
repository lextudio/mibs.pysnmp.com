# SNMP MIB module (HPN-ICF-POWER-ETH-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-POWER-ETH-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:30 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(pethMainPseGroupIndex,
 pethPsePortDetectionStatus,
 pethPsePortGroupIndex,
 pethPsePortIndex) = mibBuilder.importSymbols(
    "POWER-ETHERNET-MIB",
    "pethMainPseGroupIndex",
    "pethPsePortDetectionStatus",
    "pethPsePortGroupIndex",
    "pethPsePortIndex")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfPowerEthernetExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14)
)


# Types definitions



class ACAlarmState(Integer32):
    """Custom type ACAlarmState based on Integer32"""
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
        *(("aboveLimit", 3),
          ("fuseBroken", 5),
          ("lackPhrase", 4),
          ("normal", 1),
          ("otherError", 7),
          ("switchOff", 6),
          ("underLimit", 2))
    )





class DCAlarmState(Integer32):
    """Custom type DCAlarmState based on Integer32"""
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
        *(("aboveLimit", 3),
          ("fuseBroken", 4),
          ("normal", 1),
          ("otherError", 6),
          ("switchOff", 5),
          ("underLimit", 2))
    )





class SwitchState(Integer32):
    """Custom type SwitchState based on Integer32"""
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
        *(("highVoltInput", 3),
          ("lowVoltInput", 4),
          ("off", 2),
          ("on", 1))
    )





class ModuleAlarmState(Integer32):
    """Custom type ModuleAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("normal", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfPsePortTable_Object = MibTable
hpnicfPsePortTable = _HpnicfPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1)
)
if mibBuilder.loadTexts:
    hpnicfPsePortTable.setStatus("current")
_HpnicfPsePortEntry_Object = MibTableRow
hpnicfPsePortEntry = _HpnicfPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1)
)
hpnicfPsePortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPsePortEntry.setStatus("current")
_HpnicfPsePortFaultDescription_Type = DisplayString
_HpnicfPsePortFaultDescription_Object = MibTableColumn
hpnicfPsePortFaultDescription = _HpnicfPsePortFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 2),
    _HpnicfPsePortFaultDescription_Type()
)
hpnicfPsePortFaultDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePortFaultDescription.setStatus("current")
_HpnicfPsePortPeakPower_Type = Integer32
_HpnicfPsePortPeakPower_Object = MibTableColumn
hpnicfPsePortPeakPower = _HpnicfPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 3),
    _HpnicfPsePortPeakPower_Type()
)
hpnicfPsePortPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePortPeakPower.setStatus("current")
_HpnicfPsePortAveragePower_Type = Integer32
_HpnicfPsePortAveragePower_Object = MibTableColumn
hpnicfPsePortAveragePower = _HpnicfPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 4),
    _HpnicfPsePortAveragePower_Type()
)
hpnicfPsePortAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePortAveragePower.setStatus("current")
_HpnicfPsePortCurrentPower_Type = Integer32
_HpnicfPsePortCurrentPower_Object = MibTableColumn
hpnicfPsePortCurrentPower = _HpnicfPsePortCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 5),
    _HpnicfPsePortCurrentPower_Type()
)
hpnicfPsePortCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPsePortCurrentPower.setStatus("current")
_HpnicfPsePortPowerLimit_Type = Integer32
_HpnicfPsePortPowerLimit_Object = MibTableColumn
hpnicfPsePortPowerLimit = _HpnicfPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 6),
    _HpnicfPsePortPowerLimit_Type()
)
hpnicfPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePortPowerLimit.setStatus("current")


class _HpnicfPsePortProfileIndex_Type(Integer32):
    """Custom type hpnicfPsePortProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfPsePortProfileIndex_Type.__name__ = "Integer32"
_HpnicfPsePortProfileIndex_Object = MibTableColumn
hpnicfPsePortProfileIndex = _HpnicfPsePortProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 1, 1, 7),
    _HpnicfPsePortProfileIndex_Type()
)
hpnicfPsePortProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePortProfileIndex.setStatus("current")
_HpnicfMainPseTable_Object = MibTable
hpnicfMainPseTable = _HpnicfMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2)
)
if mibBuilder.loadTexts:
    hpnicfMainPseTable.setStatus("current")
_HpnicfMainPseEntry_Object = MibTableRow
hpnicfMainPseEntry = _HpnicfMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1)
)
hpnicfMainPseEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMainPseEntry.setStatus("current")
_HpnicfMainPsePowerLimit_Type = Integer32
_HpnicfMainPsePowerLimit_Object = MibTableColumn
hpnicfMainPsePowerLimit = _HpnicfMainPsePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 1),
    _HpnicfMainPsePowerLimit_Type()
)
hpnicfMainPsePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPsePowerLimit.setStatus("current")
_HpnicfMainPseAveragePower_Type = Integer32
_HpnicfMainPseAveragePower_Object = MibTableColumn
hpnicfMainPseAveragePower = _HpnicfMainPseAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 2),
    _HpnicfMainPseAveragePower_Type()
)
hpnicfMainPseAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPseAveragePower.setStatus("current")
_HpnicfMainPsePeakPower_Type = Integer32
_HpnicfMainPsePeakPower_Object = MibTableColumn
hpnicfMainPsePeakPower = _HpnicfMainPsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 3),
    _HpnicfMainPsePeakPower_Type()
)
hpnicfMainPsePeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPsePeakPower.setStatus("current")
_HpnicfMainGuaranteedPowerRemaining_Type = Integer32
_HpnicfMainGuaranteedPowerRemaining_Object = MibTableColumn
hpnicfMainGuaranteedPowerRemaining = _HpnicfMainGuaranteedPowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 4),
    _HpnicfMainGuaranteedPowerRemaining_Type()
)
hpnicfMainGuaranteedPowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMainGuaranteedPowerRemaining.setStatus("current")


class _HpnicfMainPsePriorityMode_Type(Integer32):
    """Custom type hpnicfMainPsePriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disconnection", 0),
          ("non-disconnection", 1))
    )


_HpnicfMainPsePriorityMode_Type.__name__ = "Integer32"
_HpnicfMainPsePriorityMode_Object = MibTableColumn
hpnicfMainPsePriorityMode = _HpnicfMainPsePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 5),
    _HpnicfMainPsePriorityMode_Type()
)
hpnicfMainPsePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPsePriorityMode.setStatus("current")


class _HpnicfMainPseLegacy_Type(Integer32):
    """Custom type hpnicfMainPseLegacy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_HpnicfMainPseLegacy_Type.__name__ = "Integer32"
_HpnicfMainPseLegacy_Object = MibTableColumn
hpnicfMainPseLegacy = _HpnicfMainPseLegacy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 6),
    _HpnicfMainPseLegacy_Type()
)
hpnicfMainPseLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPseLegacy.setStatus("current")


class _HpnicfMainPsePowerPriority_Type(Integer32):
    """Custom type hpnicfMainPsePowerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_HpnicfMainPsePowerPriority_Type.__name__ = "Integer32"
_HpnicfMainPsePowerPriority_Object = MibTableColumn
hpnicfMainPsePowerPriority = _HpnicfMainPsePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 2, 1, 7),
    _HpnicfMainPsePowerPriority_Type()
)
hpnicfMainPsePowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMainPsePowerPriority.setStatus("current")


class _HpnicfPseAutoDetectActive_Type(Integer32):
    """Custom type hpnicfPseAutoDetectActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_HpnicfPseAutoDetectActive_Type.__name__ = "Integer32"
_HpnicfPseAutoDetectActive_Object = MibScalar
hpnicfPseAutoDetectActive = _HpnicfPseAutoDetectActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 3),
    _HpnicfPseAutoDetectActive_Type()
)
hpnicfPseAutoDetectActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPseAutoDetectActive.setStatus("current")
_HpnicfPseComformance_ObjectIdentity = ObjectIdentity
hpnicfPseComformance = _HpnicfPseComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4)
)
_HpnicfPseCompliances_ObjectIdentity = ObjectIdentity
hpnicfPseCompliances = _HpnicfPseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 1)
)
_HpnicfPseGroup_ObjectIdentity = ObjectIdentity
hpnicfPseGroup = _HpnicfPseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2)
)
_HpnicfPsePowerMaxValue_Type = Integer32
_HpnicfPsePowerMaxValue_Object = MibScalar
hpnicfPsePowerMaxValue = _HpnicfPsePowerMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 5),
    _HpnicfPsePowerMaxValue_Type()
)
hpnicfPsePowerMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePowerMaxValue.setStatus("current")
_HpnicfpseportNotification_ObjectIdentity = ObjectIdentity
hpnicfpseportNotification = _HpnicfpseportNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6)
)
_HpnicfPseProfilesTable_Object = MibTable
hpnicfPseProfilesTable = _HpnicfPseProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7)
)
if mibBuilder.loadTexts:
    hpnicfPseProfilesTable.setStatus("current")
_HpnicfPseProfilesEntry_Object = MibTableRow
hpnicfPseProfilesEntry = _HpnicfPseProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1)
)
hpnicfPseProfilesEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfileIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPseProfilesEntry.setStatus("current")


class _HpnicfPseProfileIndex_Type(Integer32):
    """Custom type hpnicfPseProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfPseProfileIndex_Type.__name__ = "Integer32"
_HpnicfPseProfileIndex_Object = MibTableColumn
hpnicfPseProfileIndex = _HpnicfPseProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 1),
    _HpnicfPseProfileIndex_Type()
)
hpnicfPseProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPseProfileIndex.setStatus("current")


class _HpnicfPseProfileName_Type(DisplayString):
    """Custom type hpnicfPseProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_HpnicfPseProfileName_Type.__name__ = "DisplayString"
_HpnicfPseProfileName_Object = MibTableColumn
hpnicfPseProfileName = _HpnicfPseProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 2),
    _HpnicfPseProfileName_Type()
)
hpnicfPseProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfileName.setStatus("current")


class _HpnicfPseProfilePowerMode_Type(Integer32):
    """Custom type hpnicfPseProfilePowerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerDisabled", 1),
          ("powerEnabled", 2))
    )


_HpnicfPseProfilePowerMode_Type.__name__ = "Integer32"
_HpnicfPseProfilePowerMode_Object = MibTableColumn
hpnicfPseProfilePowerMode = _HpnicfPseProfilePowerMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 3),
    _HpnicfPseProfilePowerMode_Type()
)
hpnicfPseProfilePowerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfilePowerMode.setStatus("current")


class _HpnicfPseProfilePowerLimit_Type(Integer32):
    """Custom type hpnicfPseProfilePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15400),
    )


_HpnicfPseProfilePowerLimit_Type.__name__ = "Integer32"
_HpnicfPseProfilePowerLimit_Object = MibTableColumn
hpnicfPseProfilePowerLimit = _HpnicfPseProfilePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 4),
    _HpnicfPseProfilePowerLimit_Type()
)
hpnicfPseProfilePowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfilePowerLimit.setStatus("current")


class _HpnicfPseProfilePriority_Type(Integer32):
    """Custom type hpnicfPseProfilePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("high", 2),
          ("low", 3))
    )


_HpnicfPseProfilePriority_Type.__name__ = "Integer32"
_HpnicfPseProfilePriority_Object = MibTableColumn
hpnicfPseProfilePriority = _HpnicfPseProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 5),
    _HpnicfPseProfilePriority_Type()
)
hpnicfPseProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfilePriority.setStatus("current")


class _HpnicfPseProfilePairs_Type(Integer32):
    """Custom type hpnicfPseProfilePairs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("signal", 1),
          ("spare", 2))
    )


_HpnicfPseProfilePairs_Type.__name__ = "Integer32"
_HpnicfPseProfilePairs_Object = MibTableColumn
hpnicfPseProfilePairs = _HpnicfPseProfilePairs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 6),
    _HpnicfPseProfilePairs_Type()
)
hpnicfPseProfilePairs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfilePairs.setStatus("current")
_HpnicfPseProfileApplyNum_Type = Integer32
_HpnicfPseProfileApplyNum_Object = MibTableColumn
hpnicfPseProfileApplyNum = _HpnicfPseProfileApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 7),
    _HpnicfPseProfileApplyNum_Type()
)
hpnicfPseProfileApplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPseProfileApplyNum.setStatus("current")
_HpnicfPseProfileRowStatus_Type = RowStatus
_HpnicfPseProfileRowStatus_Object = MibTableColumn
hpnicfPseProfileRowStatus = _HpnicfPseProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 7, 1, 8),
    _HpnicfPseProfileRowStatus_Type()
)
hpnicfPseProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPseProfileRowStatus.setStatus("current")
_HpnicfPOEPowerObjects_ObjectIdentity = ObjectIdentity
hpnicfPOEPowerObjects = _HpnicfPOEPowerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8)
)
_HpnicfPOEThresholdLimitObjs_ObjectIdentity = ObjectIdentity
hpnicfPOEThresholdLimitObjs = _HpnicfPOEThresholdLimitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 1)
)


class _HpnicfPOEThresholdACMimimum_Type(OctetString):
    """Custom type hpnicfPOEThresholdACMimimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEThresholdACMimimum_Type.__name__ = "OctetString"
_HpnicfPOEThresholdACMimimum_Object = MibScalar
hpnicfPOEThresholdACMimimum = _HpnicfPOEThresholdACMimimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 1, 1),
    _HpnicfPOEThresholdACMimimum_Type()
)
hpnicfPOEThresholdACMimimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPOEThresholdACMimimum.setStatus("current")


class _HpnicfPOEThresholdACMaximum_Type(OctetString):
    """Custom type hpnicfPOEThresholdACMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEThresholdACMaximum_Type.__name__ = "OctetString"
_HpnicfPOEThresholdACMaximum_Object = MibScalar
hpnicfPOEThresholdACMaximum = _HpnicfPOEThresholdACMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 1, 2),
    _HpnicfPOEThresholdACMaximum_Type()
)
hpnicfPOEThresholdACMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPOEThresholdACMaximum.setStatus("current")


class _HpnicfPOEThresholdDCMinimum_Type(OctetString):
    """Custom type hpnicfPOEThresholdDCMinimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEThresholdDCMinimum_Type.__name__ = "OctetString"
_HpnicfPOEThresholdDCMinimum_Object = MibScalar
hpnicfPOEThresholdDCMinimum = _HpnicfPOEThresholdDCMinimum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 1, 3),
    _HpnicfPOEThresholdDCMinimum_Type()
)
hpnicfPOEThresholdDCMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPOEThresholdDCMinimum.setStatus("current")


class _HpnicfPOEThresholdDCMaximum_Type(OctetString):
    """Custom type hpnicfPOEThresholdDCMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEThresholdDCMaximum_Type.__name__ = "OctetString"
_HpnicfPOEThresholdDCMaximum_Object = MibScalar
hpnicfPOEThresholdDCMaximum = _HpnicfPOEThresholdDCMaximum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 1, 4),
    _HpnicfPOEThresholdDCMaximum_Type()
)
hpnicfPOEThresholdDCMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPOEThresholdDCMaximum.setStatus("current")
_HpnicfPOESupModuleInfoObjs_ObjectIdentity = ObjectIdentity
hpnicfPOESupModuleInfoObjs = _HpnicfPOESupModuleInfoObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2)
)


class _HpnicfPOEPowerType_Type(OctetString):
    """Custom type hpnicfPOEPowerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfPOEPowerType_Type.__name__ = "OctetString"
_HpnicfPOEPowerType_Object = MibScalar
hpnicfPOEPowerType = _HpnicfPOEPowerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 1),
    _HpnicfPOEPowerType_Type()
)
hpnicfPOEPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEPowerType.setStatus("current")
_HpnicfPOEPowerModuleNum_Type = Integer32
_HpnicfPOEPowerModuleNum_Object = MibScalar
hpnicfPOEPowerModuleNum = _HpnicfPOEPowerModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 2),
    _HpnicfPOEPowerModuleNum_Type()
)
hpnicfPOEPowerModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEPowerModuleNum.setStatus("current")


class _HpnicfPOESupervisionModuleName_Type(OctetString):
    """Custom type hpnicfPOESupervisionModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfPOESupervisionModuleName_Type.__name__ = "OctetString"
_HpnicfPOESupervisionModuleName_Object = MibScalar
hpnicfPOESupervisionModuleName = _HpnicfPOESupervisionModuleName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 3),
    _HpnicfPOESupervisionModuleName_Type()
)
hpnicfPOESupervisionModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESupervisionModuleName.setStatus("current")
_HpnicfPOESMMajorVersion_Type = Integer32
_HpnicfPOESMMajorVersion_Object = MibScalar
hpnicfPOESMMajorVersion = _HpnicfPOESMMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 4),
    _HpnicfPOESMMajorVersion_Type()
)
hpnicfPOESMMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESMMajorVersion.setStatus("current")
_HpnicfPOESMMinorVersion_Type = Integer32
_HpnicfPOESMMinorVersion_Object = MibScalar
hpnicfPOESMMinorVersion = _HpnicfPOESMMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 5),
    _HpnicfPOESMMinorVersion_Type()
)
hpnicfPOESMMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESMMinorVersion.setStatus("current")


class _HpnicfPOESMFactorName_Type(OctetString):
    """Custom type hpnicfPOESMFactorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfPOESMFactorName_Type.__name__ = "OctetString"
_HpnicfPOESMFactorName_Object = MibScalar
hpnicfPOESMFactorName = _HpnicfPOESMFactorName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 6),
    _HpnicfPOESMFactorName_Type()
)
hpnicfPOESMFactorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESMFactorName.setStatus("current")
_HpnicfPOEModuleInfoTable_Object = MibTable
hpnicfPOEModuleInfoTable = _HpnicfPOEModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfPOEModuleInfoTable.setStatus("current")
_HpnicfPOEModuleInfoEntry_Object = MibTableRow
hpnicfPOEModuleInfoEntry = _HpnicfPOEModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7, 1)
)
hpnicfPOEModuleInfoEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOEModuleInfoEntry.setStatus("current")


class _HpnicfPOEModuleIndex_Type(Integer32):
    """Custom type hpnicfPOEModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOEModuleIndex_Type.__name__ = "Integer32"
_HpnicfPOEModuleIndex_Object = MibTableColumn
hpnicfPOEModuleIndex = _HpnicfPOEModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7, 1, 1),
    _HpnicfPOEModuleIndex_Type()
)
hpnicfPOEModuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOEModuleIndex.setStatus("current")
_HpnicfPOEModuleID_Type = Integer32
_HpnicfPOEModuleID_Object = MibTableColumn
hpnicfPOEModuleID = _HpnicfPOEModuleID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7, 1, 2),
    _HpnicfPOEModuleID_Type()
)
hpnicfPOEModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleID.setStatus("current")
_HpnicfPOEModuleInfoPower_Type = Integer32
_HpnicfPOEModuleInfoPower_Object = MibTableColumn
hpnicfPOEModuleInfoPower = _HpnicfPOEModuleInfoPower_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7, 1, 3),
    _HpnicfPOEModuleInfoPower_Type()
)
hpnicfPOEModuleInfoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleInfoPower.setStatus("current")


class _HpnicfPOEModuleHardVerInfo_Type(OctetString):
    """Custom type hpnicfPOEModuleHardVerInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_HpnicfPOEModuleHardVerInfo_Type.__name__ = "OctetString"
_HpnicfPOEModuleHardVerInfo_Object = MibTableColumn
hpnicfPOEModuleHardVerInfo = _HpnicfPOEModuleHardVerInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 2, 7, 1, 4),
    _HpnicfPOEModuleHardVerInfo_Type()
)
hpnicfPOEModuleHardVerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleHardVerInfo.setStatus("current")
_HpnicfPOEDCOutStateObjects_ObjectIdentity = ObjectIdentity
hpnicfPOEDCOutStateObjects = _HpnicfPOEDCOutStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3)
)
_HpnicfPOEDCOutStateModuleNum_Type = Integer32
_HpnicfPOEDCOutStateModuleNum_Object = MibScalar
hpnicfPOEDCOutStateModuleNum = _HpnicfPOEDCOutStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3, 1),
    _HpnicfPOEDCOutStateModuleNum_Type()
)
hpnicfPOEDCOutStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutStateModuleNum.setStatus("current")
_HpnicfPOEDCOutStateTable_Object = MibTable
hpnicfPOEDCOutStateTable = _HpnicfPOEDCOutStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfPOEDCOutStateTable.setStatus("current")
_HpnicfPOEDCOutStateEntry_Object = MibTableRow
hpnicfPOEDCOutStateEntry = _HpnicfPOEDCOutStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3, 2, 1)
)
hpnicfPOEDCOutStateEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutStateIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOEDCOutStateEntry.setStatus("current")


class _HpnicfPOEDCOutStateIndex_Type(Integer32):
    """Custom type hpnicfPOEDCOutStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOEDCOutStateIndex_Type.__name__ = "Integer32"
_HpnicfPOEDCOutStateIndex_Object = MibTableColumn
hpnicfPOEDCOutStateIndex = _HpnicfPOEDCOutStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3, 2, 1, 1),
    _HpnicfPOEDCOutStateIndex_Type()
)
hpnicfPOEDCOutStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutStateIndex.setStatus("current")
_HpnicfPOEDCOutDCVolAlarm_Type = DCAlarmState
_HpnicfPOEDCOutDCVolAlarm_Object = MibTableColumn
hpnicfPOEDCOutDCVolAlarm = _HpnicfPOEDCOutDCVolAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 3, 2, 1, 2),
    _HpnicfPOEDCOutDCVolAlarm_Type()
)
hpnicfPOEDCOutDCVolAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutDCVolAlarm.setStatus("current")
_HpnicfPOEDCOutInfoObjects_ObjectIdentity = ObjectIdentity
hpnicfPOEDCOutInfoObjects = _HpnicfPOEDCOutInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4)
)
_HpnicfPOEDCOutCurNum_Type = Integer32
_HpnicfPOEDCOutCurNum_Object = MibScalar
hpnicfPOEDCOutCurNum = _HpnicfPOEDCOutCurNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 1),
    _HpnicfPOEDCOutCurNum_Type()
)
hpnicfPOEDCOutCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutCurNum.setStatus("current")
_HpnicfPOEDCOutInfoTable_Object = MibTable
hpnicfPOEDCOutInfoTable = _HpnicfPOEDCOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 2)
)
if mibBuilder.loadTexts:
    hpnicfPOEDCOutInfoTable.setStatus("current")
_HpnicfPOEDCOutInfoEntry_Object = MibTableRow
hpnicfPOEDCOutInfoEntry = _HpnicfPOEDCOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 2, 1)
)
hpnicfPOEDCOutInfoEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutInfoIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOEDCOutInfoEntry.setStatus("current")


class _HpnicfPOEDCOutInfoIndex_Type(Integer32):
    """Custom type hpnicfPOEDCOutInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOEDCOutInfoIndex_Type.__name__ = "Integer32"
_HpnicfPOEDCOutInfoIndex_Object = MibTableColumn
hpnicfPOEDCOutInfoIndex = _HpnicfPOEDCOutInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 2, 1, 1),
    _HpnicfPOEDCOutInfoIndex_Type()
)
hpnicfPOEDCOutInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutInfoIndex.setStatus("current")


class _HpnicfPOEDCOutVol_Type(OctetString):
    """Custom type hpnicfPOEDCOutVol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEDCOutVol_Type.__name__ = "OctetString"
_HpnicfPOEDCOutVol_Object = MibTableColumn
hpnicfPOEDCOutVol = _HpnicfPOEDCOutVol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 2, 1, 2),
    _HpnicfPOEDCOutVol_Type()
)
hpnicfPOEDCOutVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutVol.setStatus("current")


class _HpnicfPOEDCOutInfoLoadCur_Type(OctetString):
    """Custom type hpnicfPOEDCOutInfoLoadCur based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_HpnicfPOEDCOutInfoLoadCur_Type.__name__ = "OctetString"
_HpnicfPOEDCOutInfoLoadCur_Object = MibTableColumn
hpnicfPOEDCOutInfoLoadCur = _HpnicfPOEDCOutInfoLoadCur_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 4, 2, 1, 3),
    _HpnicfPOEDCOutInfoLoadCur_Type()
)
hpnicfPOEDCOutInfoLoadCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEDCOutInfoLoadCur.setStatus("current")
_HpnicfPOEACSwitchStateModuleObjs_ObjectIdentity = ObjectIdentity
hpnicfPOEACSwitchStateModuleObjs = _HpnicfPOEACSwitchStateModuleObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5)
)
_HpnicfPOEACSwitchStateModuleNum_Type = Integer32
_HpnicfPOEACSwitchStateModuleNum_Object = MibScalar
hpnicfPOEACSwitchStateModuleNum = _HpnicfPOEACSwitchStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5, 1),
    _HpnicfPOEACSwitchStateModuleNum_Type()
)
hpnicfPOEACSwitchStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchStateModuleNum.setStatus("current")
_HpnicfPOEACSwitchStateTable_Object = MibTable
hpnicfPOEACSwitchStateTable = _HpnicfPOEACSwitchStateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5, 2)
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchStateTable.setStatus("current")
_HpnicfPOEACSwitchStateEntry_Object = MibTableRow
hpnicfPOEACSwitchStateEntry = _HpnicfPOEACSwitchStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5, 2, 1)
)
hpnicfPOEACSwitchStateEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEACSwitchStateIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchStateEntry.setStatus("current")


class _HpnicfPOEACSwitchStateIndex_Type(Integer32):
    """Custom type hpnicfPOEACSwitchStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOEACSwitchStateIndex_Type.__name__ = "Integer32"
_HpnicfPOEACSwitchStateIndex_Object = MibTableColumn
hpnicfPOEACSwitchStateIndex = _HpnicfPOEACSwitchStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5, 2, 1, 1),
    _HpnicfPOEACSwitchStateIndex_Type()
)
hpnicfPOEACSwitchStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchStateIndex.setStatus("current")
_HpnicfPOEACSwitchState_Type = SwitchState
_HpnicfPOEACSwitchState_Object = MibTableColumn
hpnicfPOEACSwitchState = _HpnicfPOEACSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 5, 2, 1, 2),
    _HpnicfPOEACSwitchState_Type()
)
hpnicfPOEACSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchState.setStatus("current")
_HpnicfPOEInCurStateObjects_ObjectIdentity = ObjectIdentity
hpnicfPOEInCurStateObjects = _HpnicfPOEInCurStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6)
)
_HpnicfPOEInCurStateModuleNum_Type = Integer32
_HpnicfPOEInCurStateModuleNum_Object = MibScalar
hpnicfPOEInCurStateModuleNum = _HpnicfPOEInCurStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 1),
    _HpnicfPOEInCurStateModuleNum_Type()
)
hpnicfPOEInCurStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEInCurStateModuleNum.setStatus("current")
_HpnicfPOEInCurAState_Type = ACAlarmState
_HpnicfPOEInCurAState_Object = MibScalar
hpnicfPOEInCurAState = _HpnicfPOEInCurAState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 2),
    _HpnicfPOEInCurAState_Type()
)
hpnicfPOEInCurAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEInCurAState.setStatus("current")
_HpnicfPOEInCurBState_Type = ACAlarmState
_HpnicfPOEInCurBState_Object = MibScalar
hpnicfPOEInCurBState = _HpnicfPOEInCurBState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 3),
    _HpnicfPOEInCurBState_Type()
)
hpnicfPOEInCurBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEInCurBState.setStatus("current")
_HpnicfPOEInCurCState_Type = ACAlarmState
_HpnicfPOEInCurCState_Object = MibScalar
hpnicfPOEInCurCState = _HpnicfPOEInCurCState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 4),
    _HpnicfPOEInCurCState_Type()
)
hpnicfPOEInCurCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEInCurCState.setStatus("current")
_HpnicfPOESwitchStateVolExTable_Object = MibTable
hpnicfPOESwitchStateVolExTable = _HpnicfPOESwitchStateVolExTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5)
)
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateVolExTable.setStatus("current")
_HpnicfPOESwitchStateVolExEntry_Object = MibTableRow
hpnicfPOESwitchStateVolExEntry = _HpnicfPOESwitchStateVolExEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5, 1)
)
hpnicfPOESwitchStateVolExEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateVolExIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateVolExEntry.setStatus("current")


class _HpnicfPOESwitchStateVolExIndex_Type(Integer32):
    """Custom type hpnicfPOESwitchStateVolExIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOESwitchStateVolExIndex_Type.__name__ = "Integer32"
_HpnicfPOESwitchStateVolExIndex_Object = MibTableColumn
hpnicfPOESwitchStateVolExIndex = _HpnicfPOESwitchStateVolExIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5, 1, 1),
    _HpnicfPOESwitchStateVolExIndex_Type()
)
hpnicfPOESwitchStateVolExIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateVolExIndex.setStatus("current")
_HpnicfPOESwitchStateInVolAB_Type = ACAlarmState
_HpnicfPOESwitchStateInVolAB_Object = MibTableColumn
hpnicfPOESwitchStateInVolAB = _HpnicfPOESwitchStateInVolAB_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5, 1, 2),
    _HpnicfPOESwitchStateInVolAB_Type()
)
hpnicfPOESwitchStateInVolAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateInVolAB.setStatus("current")
_HpnicfPOESwitchStateInVolBC_Type = ACAlarmState
_HpnicfPOESwitchStateInVolBC_Object = MibTableColumn
hpnicfPOESwitchStateInVolBC = _HpnicfPOESwitchStateInVolBC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5, 1, 3),
    _HpnicfPOESwitchStateInVolBC_Type()
)
hpnicfPOESwitchStateInVolBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateInVolBC.setStatus("current")
_HpnicfPOESwitchStateInVolCA_Type = ACAlarmState
_HpnicfPOESwitchStateInVolCA_Object = MibTableColumn
hpnicfPOESwitchStateInVolCA = _HpnicfPOESwitchStateInVolCA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 6, 5, 1, 4),
    _HpnicfPOESwitchStateInVolCA_Type()
)
hpnicfPOESwitchStateInVolCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOESwitchStateInVolCA.setStatus("current")
_HpnicfPOEAlarmStateObjects_ObjectIdentity = ObjectIdentity
hpnicfPOEAlarmStateObjects = _HpnicfPOEAlarmStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7)
)
_HpnicfPOEAlarmStateModuleNum_Type = Integer32
_HpnicfPOEAlarmStateModuleNum_Object = MibScalar
hpnicfPOEAlarmStateModuleNum = _HpnicfPOEAlarmStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 1),
    _HpnicfPOEAlarmStateModuleNum_Type()
)
hpnicfPOEAlarmStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEAlarmStateModuleNum.setStatus("current")
_HpnicfPOEAlarmStateInfoTable_Object = MibTable
hpnicfPOEAlarmStateInfoTable = _HpnicfPOEAlarmStateInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hpnicfPOEAlarmStateInfoTable.setStatus("current")
_HpnicfPOEAlarmStateInfoEntry_Object = MibTableRow
hpnicfPOEAlarmStateInfoEntry = _HpnicfPOEAlarmStateInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1)
)
hpnicfPOEAlarmStateInfoEntry.setIndexNames(
    (0, "HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPOEAlarmStateInfoEntry.setStatus("current")


class _HpnicfPOEAlarmModuleInfoIndex_Type(Integer32):
    """Custom type hpnicfPOEAlarmModuleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfPOEAlarmModuleInfoIndex_Type.__name__ = "Integer32"
_HpnicfPOEAlarmModuleInfoIndex_Object = MibTableColumn
hpnicfPOEAlarmModuleInfoIndex = _HpnicfPOEAlarmModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 1),
    _HpnicfPOEAlarmModuleInfoIndex_Type()
)
hpnicfPOEAlarmModuleInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpnicfPOEAlarmModuleInfoIndex.setStatus("current")
_HpnicfPOEModuleDisconnect_Type = ModuleAlarmState
_HpnicfPOEModuleDisconnect_Object = MibTableColumn
hpnicfPOEModuleDisconnect = _HpnicfPOEModuleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 2),
    _HpnicfPOEModuleDisconnect_Type()
)
hpnicfPOEModuleDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleDisconnect.setStatus("current")
_HpnicfPOEModuleInputError_Type = ModuleAlarmState
_HpnicfPOEModuleInputError_Object = MibTableColumn
hpnicfPOEModuleInputError = _HpnicfPOEModuleInputError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 3),
    _HpnicfPOEModuleInputError_Type()
)
hpnicfPOEModuleInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleInputError.setStatus("current")
_HpnicfPOEModuleOutputError_Type = ModuleAlarmState
_HpnicfPOEModuleOutputError_Object = MibTableColumn
hpnicfPOEModuleOutputError = _HpnicfPOEModuleOutputError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 4),
    _HpnicfPOEModuleOutputError_Type()
)
hpnicfPOEModuleOutputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleOutputError.setStatus("current")
_HpnicfPOEModuleOverVoltage_Type = ModuleAlarmState
_HpnicfPOEModuleOverVoltage_Object = MibTableColumn
hpnicfPOEModuleOverVoltage = _HpnicfPOEModuleOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 5),
    _HpnicfPOEModuleOverVoltage_Type()
)
hpnicfPOEModuleOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleOverVoltage.setStatus("current")
_HpnicfPOEModuleOverTemp_Type = ModuleAlarmState
_HpnicfPOEModuleOverTemp_Object = MibTableColumn
hpnicfPOEModuleOverTemp = _HpnicfPOEModuleOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 6),
    _HpnicfPOEModuleOverTemp_Type()
)
hpnicfPOEModuleOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleOverTemp.setStatus("current")
_HpnicfPOEModuleFanError_Type = ModuleAlarmState
_HpnicfPOEModuleFanError_Object = MibTableColumn
hpnicfPOEModuleFanError = _HpnicfPOEModuleFanError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 7),
    _HpnicfPOEModuleFanError_Type()
)
hpnicfPOEModuleFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleFanError.setStatus("current")
_HpnicfPOEModuleShutdown_Type = ModuleAlarmState
_HpnicfPOEModuleShutdown_Object = MibTableColumn
hpnicfPOEModuleShutdown = _HpnicfPOEModuleShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 8),
    _HpnicfPOEModuleShutdown_Type()
)
hpnicfPOEModuleShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleShutdown.setStatus("current")
_HpnicfPOEModuleCurRestricted_Type = ModuleAlarmState
_HpnicfPOEModuleCurRestricted_Object = MibTableColumn
hpnicfPOEModuleCurRestricted = _HpnicfPOEModuleCurRestricted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 8, 7, 2, 1, 9),
    _HpnicfPOEModuleCurRestricted_Type()
)
hpnicfPOEModuleCurRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfPOEModuleCurRestricted.setStatus("current")


class _HpnicfPsePolicyMode_Type(Integer32):
    """Custom type hpnicfPsePolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("priority", 2))
    )


_HpnicfPsePolicyMode_Type.__name__ = "Integer32"
_HpnicfPsePolicyMode_Object = MibScalar
hpnicfPsePolicyMode = _HpnicfPsePolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 9),
    _HpnicfPsePolicyMode_Type()
)
hpnicfPsePolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPsePolicyMode.setStatus("current")


class _HpnicfPDPolicyMode_Type(Integer32):
    """Custom type hpnicfPDPolicyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("priority", 2))
    )


_HpnicfPDPolicyMode_Type.__name__ = "Integer32"
_HpnicfPDPolicyMode_Object = MibScalar
hpnicfPDPolicyMode = _HpnicfPDPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 10),
    _HpnicfPDPolicyMode_Type()
)
hpnicfPDPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfPDPolicyMode.setStatus("current")

# Managed Objects groups

hpnicfPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 1)
)
hpnicfPsePortGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortProfileIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortPowerLimit"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortCurrentPower"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortAveragePower"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortPeakPower"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePortFaultDescription"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfMainPsePriorityMode"))
)
if mibBuilder.loadTexts:
    hpnicfPsePortGroup.setStatus("current")

hpnicfMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 2)
)
hpnicfMainPseGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfMainPsePowerLimit"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfMainPseAveragePower"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfMainPsePeakPower"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfMainGuaranteedPowerRemaining"))
)
if mibBuilder.loadTexts:
    hpnicfMainPseGroup.setStatus("current")

hpnicfPseScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 3)
)
hpnicfPseScalarGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseAutoDetectActive"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePowerMaxValue"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPsePolicyMode"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPDPolicyMode"))
)
if mibBuilder.loadTexts:
    hpnicfPseScalarGroup.setStatus("current")

hpnicfPsePDNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 4)
)
hpnicfPsePDNotificationGroup.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfpsePDChangeNotification")
)
if mibBuilder.loadTexts:
    hpnicfPsePDNotificationGroup.setStatus("current")

hpnicfPseProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 5)
)
hpnicfPseProfilesGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfileName"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfilePowerMode"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfilePowerLimit"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfilePriority"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfilePairs"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfileApplyNum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPseProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hpnicfPseProfilesGroup.setStatus("current")

hpnicfPOEPowerThresholdLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 6)
)
hpnicfPOEPowerThresholdLimitGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEThresholdACMimimum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEThresholdACMaximum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEThresholdDCMinimum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEThresholdDCMaximum"))
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerThresholdLimitGroup.setStatus("current")

hpnicfPOEPowerSupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 7)
)
hpnicfPOEPowerSupInfoGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEPowerType"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEPowerModuleNum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESupervisionModuleName"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESMMajorVersion"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESMMinorVersion"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESMFactorName"))
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerSupInfoGroup.setStatus("current")

hpnicfPOEPowerDCOutStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 8)
)
hpnicfPOEPowerDCOutStateGroup.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutStateModuleNum")
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerDCOutStateGroup.setStatus("current")

hpnicfPOEPowerDCOutInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 9)
)
hpnicfPOEPowerDCOutInfoGroup.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutCurNum")
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerDCOutInfoGroup.setStatus("current")

hpnicfPOEPowerACSwitchStateModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 10)
)
hpnicfPOEPowerACSwitchStateModuleGroup.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEACSwitchStateModuleNum")
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerACSwitchStateModuleGroup.setStatus("current")

hpnicfPOEPowerInCurStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 11)
)
hpnicfPOEPowerInCurStateGroup.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurStateModuleNum"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurAState"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurBState"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurCState"))
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerInCurStateGroup.setStatus("current")

hpnicfPOEPowerAlarmStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 2, 12)
)
hpnicfPOEPowerAlarmStateGroup.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmStateModuleNum")
)
if mibBuilder.loadTexts:
    hpnicfPOEPowerAlarmStateGroup.setStatus("current")


# Notification objects

hpnicfpsePDChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 1)
)
hpnicfpsePDChangeNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    hpnicfpsePDChangeNotification.setStatus(
        "current"
    )

hpnicfPOEDisconnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 2)
)
hpnicfPOEDisconnectNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleDisconnect"))
)
if mibBuilder.loadTexts:
    hpnicfPOEDisconnectNotification.setStatus(
        "current"
    )

hpnicfPOEInputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 3)
)
hpnicfPOEInputErrorNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleInputError"))
)
if mibBuilder.loadTexts:
    hpnicfPOEInputErrorNotification.setStatus(
        "current"
    )

hpnicfPOEOutputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 4)
)
hpnicfPOEOutputErrorNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleOutputError"))
)
if mibBuilder.loadTexts:
    hpnicfPOEOutputErrorNotification.setStatus(
        "current"
    )

hpnicfPOEOverVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 5)
)
hpnicfPOEOverVoltageNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleOverVoltage"))
)
if mibBuilder.loadTexts:
    hpnicfPOEOverVoltageNotification.setStatus(
        "current"
    )

hpnicfPOEOverTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 6)
)
hpnicfPOEOverTempNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleOverTemp"))
)
if mibBuilder.loadTexts:
    hpnicfPOEOverTempNotification.setStatus(
        "current"
    )

hpnicfPOEFanErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 7)
)
hpnicfPOEFanErrorNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleFanError"))
)
if mibBuilder.loadTexts:
    hpnicfPOEFanErrorNotification.setStatus(
        "current"
    )

hpnicfPOEModuleShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 8)
)
hpnicfPOEModuleShutdownNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleShutdown"))
)
if mibBuilder.loadTexts:
    hpnicfPOEModuleShutdownNotification.setStatus(
        "current"
    )

hpnicfPOECurRestrictedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 9)
)
hpnicfPOECurRestrictedNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEAlarmModuleInfoIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEModuleCurRestricted"))
)
if mibBuilder.loadTexts:
    hpnicfPOECurRestrictedNotification.setStatus(
        "current"
    )

hpnicfPOEACSwitchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 10)
)
hpnicfPOEACSwitchNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEACSwitchStateIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEACSwitchState"))
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchNotification.setStatus(
        "current"
    )

hpnicfPOEACInCurANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 11)
)
hpnicfPOEACInCurANotification.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurAState")
)
if mibBuilder.loadTexts:
    hpnicfPOEACInCurANotification.setStatus(
        "current"
    )

hpnicfPOEACInCurBNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 12)
)
hpnicfPOEACInCurBNotification.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurBState")
)
if mibBuilder.loadTexts:
    hpnicfPOEACInCurBNotification.setStatus(
        "current"
    )

hpnicfPOEACInCurCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 13)
)
hpnicfPOEACInCurCNotification.setObjects(
    ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEInCurCState")
)
if mibBuilder.loadTexts:
    hpnicfPOEACInCurCNotification.setStatus(
        "current"
    )

hpnicfPOEACSwitchVolABNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 14)
)
hpnicfPOEACSwitchVolABNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateVolExIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateInVolAB"))
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchVolABNotification.setStatus(
        "current"
    )

hpnicfPOEACSwitchVolBCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 15)
)
hpnicfPOEACSwitchVolBCNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateVolExIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateInVolBC"))
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchVolBCNotification.setStatus(
        "current"
    )

hpnicfPOEACSwitchVolCANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 16)
)
hpnicfPOEACSwitchVolCANotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateVolExIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOESwitchStateInVolCA"))
)
if mibBuilder.loadTexts:
    hpnicfPOEACSwitchVolCANotification.setStatus(
        "current"
    )

hpnicfPOEDCOutVolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 17)
)
hpnicfPOEDCOutVolNotification.setObjects(
      *(("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutStateIndex"),
        ("HPN-ICF-POWER-ETH-EXT-MIB", "hpnicfPOEDCOutDCVolAlarm"))
)
if mibBuilder.loadTexts:
    hpnicfPOEDCOutVolNotification.setStatus(
        "current"
    )

hpnicfPOEShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 6, 18)
)
if mibBuilder.loadTexts:
    hpnicfPOEShutdownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hpnicfPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfPseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-POWER-ETH-EXT-MIB",
    **{"ACAlarmState": ACAlarmState,
       "DCAlarmState": DCAlarmState,
       "SwitchState": SwitchState,
       "ModuleAlarmState": ModuleAlarmState,
       "hpnicfPowerEthernetExt": hpnicfPowerEthernetExt,
       "hpnicfPsePortTable": hpnicfPsePortTable,
       "hpnicfPsePortEntry": hpnicfPsePortEntry,
       "hpnicfPsePortFaultDescription": hpnicfPsePortFaultDescription,
       "hpnicfPsePortPeakPower": hpnicfPsePortPeakPower,
       "hpnicfPsePortAveragePower": hpnicfPsePortAveragePower,
       "hpnicfPsePortCurrentPower": hpnicfPsePortCurrentPower,
       "hpnicfPsePortPowerLimit": hpnicfPsePortPowerLimit,
       "hpnicfPsePortProfileIndex": hpnicfPsePortProfileIndex,
       "hpnicfMainPseTable": hpnicfMainPseTable,
       "hpnicfMainPseEntry": hpnicfMainPseEntry,
       "hpnicfMainPsePowerLimit": hpnicfMainPsePowerLimit,
       "hpnicfMainPseAveragePower": hpnicfMainPseAveragePower,
       "hpnicfMainPsePeakPower": hpnicfMainPsePeakPower,
       "hpnicfMainGuaranteedPowerRemaining": hpnicfMainGuaranteedPowerRemaining,
       "hpnicfMainPsePriorityMode": hpnicfMainPsePriorityMode,
       "hpnicfMainPseLegacy": hpnicfMainPseLegacy,
       "hpnicfMainPsePowerPriority": hpnicfMainPsePowerPriority,
       "hpnicfPseAutoDetectActive": hpnicfPseAutoDetectActive,
       "hpnicfPseComformance": hpnicfPseComformance,
       "hpnicfPseCompliances": hpnicfPseCompliances,
       "hpnicfPseCompliance": hpnicfPseCompliance,
       "hpnicfPseGroup": hpnicfPseGroup,
       "hpnicfPsePortGroup": hpnicfPsePortGroup,
       "hpnicfMainPseGroup": hpnicfMainPseGroup,
       "hpnicfPseScalarGroup": hpnicfPseScalarGroup,
       "hpnicfPsePDNotificationGroup": hpnicfPsePDNotificationGroup,
       "hpnicfPseProfilesGroup": hpnicfPseProfilesGroup,
       "hpnicfPOEPowerThresholdLimitGroup": hpnicfPOEPowerThresholdLimitGroup,
       "hpnicfPOEPowerSupInfoGroup": hpnicfPOEPowerSupInfoGroup,
       "hpnicfPOEPowerDCOutStateGroup": hpnicfPOEPowerDCOutStateGroup,
       "hpnicfPOEPowerDCOutInfoGroup": hpnicfPOEPowerDCOutInfoGroup,
       "hpnicfPOEPowerACSwitchStateModuleGroup": hpnicfPOEPowerACSwitchStateModuleGroup,
       "hpnicfPOEPowerInCurStateGroup": hpnicfPOEPowerInCurStateGroup,
       "hpnicfPOEPowerAlarmStateGroup": hpnicfPOEPowerAlarmStateGroup,
       "hpnicfPsePowerMaxValue": hpnicfPsePowerMaxValue,
       "hpnicfpseportNotification": hpnicfpseportNotification,
       "hpnicfpsePDChangeNotification": hpnicfpsePDChangeNotification,
       "hpnicfPOEDisconnectNotification": hpnicfPOEDisconnectNotification,
       "hpnicfPOEInputErrorNotification": hpnicfPOEInputErrorNotification,
       "hpnicfPOEOutputErrorNotification": hpnicfPOEOutputErrorNotification,
       "hpnicfPOEOverVoltageNotification": hpnicfPOEOverVoltageNotification,
       "hpnicfPOEOverTempNotification": hpnicfPOEOverTempNotification,
       "hpnicfPOEFanErrorNotification": hpnicfPOEFanErrorNotification,
       "hpnicfPOEModuleShutdownNotification": hpnicfPOEModuleShutdownNotification,
       "hpnicfPOECurRestrictedNotification": hpnicfPOECurRestrictedNotification,
       "hpnicfPOEACSwitchNotification": hpnicfPOEACSwitchNotification,
       "hpnicfPOEACInCurANotification": hpnicfPOEACInCurANotification,
       "hpnicfPOEACInCurBNotification": hpnicfPOEACInCurBNotification,
       "hpnicfPOEACInCurCNotification": hpnicfPOEACInCurCNotification,
       "hpnicfPOEACSwitchVolABNotification": hpnicfPOEACSwitchVolABNotification,
       "hpnicfPOEACSwitchVolBCNotification": hpnicfPOEACSwitchVolBCNotification,
       "hpnicfPOEACSwitchVolCANotification": hpnicfPOEACSwitchVolCANotification,
       "hpnicfPOEDCOutVolNotification": hpnicfPOEDCOutVolNotification,
       "hpnicfPOEShutdownNotification": hpnicfPOEShutdownNotification,
       "hpnicfPseProfilesTable": hpnicfPseProfilesTable,
       "hpnicfPseProfilesEntry": hpnicfPseProfilesEntry,
       "hpnicfPseProfileIndex": hpnicfPseProfileIndex,
       "hpnicfPseProfileName": hpnicfPseProfileName,
       "hpnicfPseProfilePowerMode": hpnicfPseProfilePowerMode,
       "hpnicfPseProfilePowerLimit": hpnicfPseProfilePowerLimit,
       "hpnicfPseProfilePriority": hpnicfPseProfilePriority,
       "hpnicfPseProfilePairs": hpnicfPseProfilePairs,
       "hpnicfPseProfileApplyNum": hpnicfPseProfileApplyNum,
       "hpnicfPseProfileRowStatus": hpnicfPseProfileRowStatus,
       "hpnicfPOEPowerObjects": hpnicfPOEPowerObjects,
       "hpnicfPOEThresholdLimitObjs": hpnicfPOEThresholdLimitObjs,
       "hpnicfPOEThresholdACMimimum": hpnicfPOEThresholdACMimimum,
       "hpnicfPOEThresholdACMaximum": hpnicfPOEThresholdACMaximum,
       "hpnicfPOEThresholdDCMinimum": hpnicfPOEThresholdDCMinimum,
       "hpnicfPOEThresholdDCMaximum": hpnicfPOEThresholdDCMaximum,
       "hpnicfPOESupModuleInfoObjs": hpnicfPOESupModuleInfoObjs,
       "hpnicfPOEPowerType": hpnicfPOEPowerType,
       "hpnicfPOEPowerModuleNum": hpnicfPOEPowerModuleNum,
       "hpnicfPOESupervisionModuleName": hpnicfPOESupervisionModuleName,
       "hpnicfPOESMMajorVersion": hpnicfPOESMMajorVersion,
       "hpnicfPOESMMinorVersion": hpnicfPOESMMinorVersion,
       "hpnicfPOESMFactorName": hpnicfPOESMFactorName,
       "hpnicfPOEModuleInfoTable": hpnicfPOEModuleInfoTable,
       "hpnicfPOEModuleInfoEntry": hpnicfPOEModuleInfoEntry,
       "hpnicfPOEModuleIndex": hpnicfPOEModuleIndex,
       "hpnicfPOEModuleID": hpnicfPOEModuleID,
       "hpnicfPOEModuleInfoPower": hpnicfPOEModuleInfoPower,
       "hpnicfPOEModuleHardVerInfo": hpnicfPOEModuleHardVerInfo,
       "hpnicfPOEDCOutStateObjects": hpnicfPOEDCOutStateObjects,
       "hpnicfPOEDCOutStateModuleNum": hpnicfPOEDCOutStateModuleNum,
       "hpnicfPOEDCOutStateTable": hpnicfPOEDCOutStateTable,
       "hpnicfPOEDCOutStateEntry": hpnicfPOEDCOutStateEntry,
       "hpnicfPOEDCOutStateIndex": hpnicfPOEDCOutStateIndex,
       "hpnicfPOEDCOutDCVolAlarm": hpnicfPOEDCOutDCVolAlarm,
       "hpnicfPOEDCOutInfoObjects": hpnicfPOEDCOutInfoObjects,
       "hpnicfPOEDCOutCurNum": hpnicfPOEDCOutCurNum,
       "hpnicfPOEDCOutInfoTable": hpnicfPOEDCOutInfoTable,
       "hpnicfPOEDCOutInfoEntry": hpnicfPOEDCOutInfoEntry,
       "hpnicfPOEDCOutInfoIndex": hpnicfPOEDCOutInfoIndex,
       "hpnicfPOEDCOutVol": hpnicfPOEDCOutVol,
       "hpnicfPOEDCOutInfoLoadCur": hpnicfPOEDCOutInfoLoadCur,
       "hpnicfPOEACSwitchStateModuleObjs": hpnicfPOEACSwitchStateModuleObjs,
       "hpnicfPOEACSwitchStateModuleNum": hpnicfPOEACSwitchStateModuleNum,
       "hpnicfPOEACSwitchStateTable": hpnicfPOEACSwitchStateTable,
       "hpnicfPOEACSwitchStateEntry": hpnicfPOEACSwitchStateEntry,
       "hpnicfPOEACSwitchStateIndex": hpnicfPOEACSwitchStateIndex,
       "hpnicfPOEACSwitchState": hpnicfPOEACSwitchState,
       "hpnicfPOEInCurStateObjects": hpnicfPOEInCurStateObjects,
       "hpnicfPOEInCurStateModuleNum": hpnicfPOEInCurStateModuleNum,
       "hpnicfPOEInCurAState": hpnicfPOEInCurAState,
       "hpnicfPOEInCurBState": hpnicfPOEInCurBState,
       "hpnicfPOEInCurCState": hpnicfPOEInCurCState,
       "hpnicfPOESwitchStateVolExTable": hpnicfPOESwitchStateVolExTable,
       "hpnicfPOESwitchStateVolExEntry": hpnicfPOESwitchStateVolExEntry,
       "hpnicfPOESwitchStateVolExIndex": hpnicfPOESwitchStateVolExIndex,
       "hpnicfPOESwitchStateInVolAB": hpnicfPOESwitchStateInVolAB,
       "hpnicfPOESwitchStateInVolBC": hpnicfPOESwitchStateInVolBC,
       "hpnicfPOESwitchStateInVolCA": hpnicfPOESwitchStateInVolCA,
       "hpnicfPOEAlarmStateObjects": hpnicfPOEAlarmStateObjects,
       "hpnicfPOEAlarmStateModuleNum": hpnicfPOEAlarmStateModuleNum,
       "hpnicfPOEAlarmStateInfoTable": hpnicfPOEAlarmStateInfoTable,
       "hpnicfPOEAlarmStateInfoEntry": hpnicfPOEAlarmStateInfoEntry,
       "hpnicfPOEAlarmModuleInfoIndex": hpnicfPOEAlarmModuleInfoIndex,
       "hpnicfPOEModuleDisconnect": hpnicfPOEModuleDisconnect,
       "hpnicfPOEModuleInputError": hpnicfPOEModuleInputError,
       "hpnicfPOEModuleOutputError": hpnicfPOEModuleOutputError,
       "hpnicfPOEModuleOverVoltage": hpnicfPOEModuleOverVoltage,
       "hpnicfPOEModuleOverTemp": hpnicfPOEModuleOverTemp,
       "hpnicfPOEModuleFanError": hpnicfPOEModuleFanError,
       "hpnicfPOEModuleShutdown": hpnicfPOEModuleShutdown,
       "hpnicfPOEModuleCurRestricted": hpnicfPOEModuleCurRestricted,
       "hpnicfPsePolicyMode": hpnicfPsePolicyMode,
       "hpnicfPDPolicyMode": hpnicfPDPolicyMode}
)
