# SNMP MIB module (HH3C-POWER-ETH-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-POWER-ETH-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:31 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cPowerEthernetExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14)
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

_Hh3cPsePortTable_Object = MibTable
hh3cPsePortTable = _Hh3cPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1)
)
if mibBuilder.loadTexts:
    hh3cPsePortTable.setStatus("current")
_Hh3cPsePortEntry_Object = MibTableRow
hh3cPsePortEntry = _Hh3cPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1)
)
hh3cPsePortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    hh3cPsePortEntry.setStatus("current")
_Hh3cPsePortFaultDescription_Type = DisplayString
_Hh3cPsePortFaultDescription_Object = MibTableColumn
hh3cPsePortFaultDescription = _Hh3cPsePortFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 2),
    _Hh3cPsePortFaultDescription_Type()
)
hh3cPsePortFaultDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePortFaultDescription.setStatus("current")
_Hh3cPsePortPeakPower_Type = Integer32
_Hh3cPsePortPeakPower_Object = MibTableColumn
hh3cPsePortPeakPower = _Hh3cPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 3),
    _Hh3cPsePortPeakPower_Type()
)
hh3cPsePortPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePortPeakPower.setStatus("current")
_Hh3cPsePortAveragePower_Type = Integer32
_Hh3cPsePortAveragePower_Object = MibTableColumn
hh3cPsePortAveragePower = _Hh3cPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 4),
    _Hh3cPsePortAveragePower_Type()
)
hh3cPsePortAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePortAveragePower.setStatus("current")
_Hh3cPsePortCurrentPower_Type = Integer32
_Hh3cPsePortCurrentPower_Object = MibTableColumn
hh3cPsePortCurrentPower = _Hh3cPsePortCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 5),
    _Hh3cPsePortCurrentPower_Type()
)
hh3cPsePortCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPsePortCurrentPower.setStatus("current")
_Hh3cPsePortPowerLimit_Type = Integer32
_Hh3cPsePortPowerLimit_Object = MibTableColumn
hh3cPsePortPowerLimit = _Hh3cPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 6),
    _Hh3cPsePortPowerLimit_Type()
)
hh3cPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePortPowerLimit.setStatus("current")


class _Hh3cPsePortProfileIndex_Type(Integer32):
    """Custom type hh3cPsePortProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cPsePortProfileIndex_Type.__name__ = "Integer32"
_Hh3cPsePortProfileIndex_Object = MibTableColumn
hh3cPsePortProfileIndex = _Hh3cPsePortProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 1, 1, 7),
    _Hh3cPsePortProfileIndex_Type()
)
hh3cPsePortProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePortProfileIndex.setStatus("current")
_Hh3cMainPseTable_Object = MibTable
hh3cMainPseTable = _Hh3cMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2)
)
if mibBuilder.loadTexts:
    hh3cMainPseTable.setStatus("current")
_Hh3cMainPseEntry_Object = MibTableRow
hh3cMainPseEntry = _Hh3cMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1)
)
hh3cMainPseEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cMainPseEntry.setStatus("current")
_Hh3cMainPsePowerLimit_Type = Integer32
_Hh3cMainPsePowerLimit_Object = MibTableColumn
hh3cMainPsePowerLimit = _Hh3cMainPsePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 1),
    _Hh3cMainPsePowerLimit_Type()
)
hh3cMainPsePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPsePowerLimit.setStatus("current")
_Hh3cMainPseAveragePower_Type = Integer32
_Hh3cMainPseAveragePower_Object = MibTableColumn
hh3cMainPseAveragePower = _Hh3cMainPseAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 2),
    _Hh3cMainPseAveragePower_Type()
)
hh3cMainPseAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPseAveragePower.setStatus("current")
_Hh3cMainPsePeakPower_Type = Integer32
_Hh3cMainPsePeakPower_Object = MibTableColumn
hh3cMainPsePeakPower = _Hh3cMainPsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 3),
    _Hh3cMainPsePeakPower_Type()
)
hh3cMainPsePeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPsePeakPower.setStatus("current")
_Hh3cMainGuaranteedPowerRemaining_Type = Integer32
_Hh3cMainGuaranteedPowerRemaining_Object = MibTableColumn
hh3cMainGuaranteedPowerRemaining = _Hh3cMainGuaranteedPowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 4),
    _Hh3cMainGuaranteedPowerRemaining_Type()
)
hh3cMainGuaranteedPowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMainGuaranteedPowerRemaining.setStatus("current")


class _Hh3cMainPsePriorityMode_Type(Integer32):
    """Custom type hh3cMainPsePriorityMode based on Integer32"""
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


_Hh3cMainPsePriorityMode_Type.__name__ = "Integer32"
_Hh3cMainPsePriorityMode_Object = MibTableColumn
hh3cMainPsePriorityMode = _Hh3cMainPsePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 5),
    _Hh3cMainPsePriorityMode_Type()
)
hh3cMainPsePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPsePriorityMode.setStatus("current")


class _Hh3cMainPseLegacy_Type(Integer32):
    """Custom type hh3cMainPseLegacy based on Integer32"""
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


_Hh3cMainPseLegacy_Type.__name__ = "Integer32"
_Hh3cMainPseLegacy_Object = MibTableColumn
hh3cMainPseLegacy = _Hh3cMainPseLegacy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 6),
    _Hh3cMainPseLegacy_Type()
)
hh3cMainPseLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPseLegacy.setStatus("current")


class _Hh3cMainPsePowerPriority_Type(Integer32):
    """Custom type hh3cMainPsePowerPriority based on Integer32"""
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


_Hh3cMainPsePowerPriority_Type.__name__ = "Integer32"
_Hh3cMainPsePowerPriority_Object = MibTableColumn
hh3cMainPsePowerPriority = _Hh3cMainPsePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 2, 1, 7),
    _Hh3cMainPsePowerPriority_Type()
)
hh3cMainPsePowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMainPsePowerPriority.setStatus("current")


class _Hh3cPseAutoDetectActive_Type(Integer32):
    """Custom type hh3cPseAutoDetectActive based on Integer32"""
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


_Hh3cPseAutoDetectActive_Type.__name__ = "Integer32"
_Hh3cPseAutoDetectActive_Object = MibScalar
hh3cPseAutoDetectActive = _Hh3cPseAutoDetectActive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 3),
    _Hh3cPseAutoDetectActive_Type()
)
hh3cPseAutoDetectActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPseAutoDetectActive.setStatus("current")
_Hh3cPseComformance_ObjectIdentity = ObjectIdentity
hh3cPseComformance = _Hh3cPseComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4)
)
_Hh3cPseCompliances_ObjectIdentity = ObjectIdentity
hh3cPseCompliances = _Hh3cPseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 1)
)
_Hh3cPseGroup_ObjectIdentity = ObjectIdentity
hh3cPseGroup = _Hh3cPseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2)
)
_Hh3cPsePowerMaxValue_Type = Integer32
_Hh3cPsePowerMaxValue_Object = MibScalar
hh3cPsePowerMaxValue = _Hh3cPsePowerMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 5),
    _Hh3cPsePowerMaxValue_Type()
)
hh3cPsePowerMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePowerMaxValue.setStatus("current")
_Hh3cpseportNotification_ObjectIdentity = ObjectIdentity
hh3cpseportNotification = _Hh3cpseportNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6)
)
_Hh3cPseProfilesTable_Object = MibTable
hh3cPseProfilesTable = _Hh3cPseProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7)
)
if mibBuilder.loadTexts:
    hh3cPseProfilesTable.setStatus("current")
_Hh3cPseProfilesEntry_Object = MibTableRow
hh3cPseProfilesEntry = _Hh3cPseProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1)
)
hh3cPseProfilesEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileIndex"),
)
if mibBuilder.loadTexts:
    hh3cPseProfilesEntry.setStatus("current")


class _Hh3cPseProfileIndex_Type(Integer32):
    """Custom type hh3cPseProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cPseProfileIndex_Type.__name__ = "Integer32"
_Hh3cPseProfileIndex_Object = MibTableColumn
hh3cPseProfileIndex = _Hh3cPseProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 1),
    _Hh3cPseProfileIndex_Type()
)
hh3cPseProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPseProfileIndex.setStatus("current")


class _Hh3cPseProfileName_Type(DisplayString):
    """Custom type hh3cPseProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cPseProfileName_Type.__name__ = "DisplayString"
_Hh3cPseProfileName_Object = MibTableColumn
hh3cPseProfileName = _Hh3cPseProfileName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 2),
    _Hh3cPseProfileName_Type()
)
hh3cPseProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfileName.setStatus("current")


class _Hh3cPseProfilePowerMode_Type(Integer32):
    """Custom type hh3cPseProfilePowerMode based on Integer32"""
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


_Hh3cPseProfilePowerMode_Type.__name__ = "Integer32"
_Hh3cPseProfilePowerMode_Object = MibTableColumn
hh3cPseProfilePowerMode = _Hh3cPseProfilePowerMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 3),
    _Hh3cPseProfilePowerMode_Type()
)
hh3cPseProfilePowerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfilePowerMode.setStatus("current")


class _Hh3cPseProfilePowerLimit_Type(Integer32):
    """Custom type hh3cPseProfilePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15400),
    )


_Hh3cPseProfilePowerLimit_Type.__name__ = "Integer32"
_Hh3cPseProfilePowerLimit_Object = MibTableColumn
hh3cPseProfilePowerLimit = _Hh3cPseProfilePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 4),
    _Hh3cPseProfilePowerLimit_Type()
)
hh3cPseProfilePowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfilePowerLimit.setStatus("current")


class _Hh3cPseProfilePriority_Type(Integer32):
    """Custom type hh3cPseProfilePriority based on Integer32"""
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


_Hh3cPseProfilePriority_Type.__name__ = "Integer32"
_Hh3cPseProfilePriority_Object = MibTableColumn
hh3cPseProfilePriority = _Hh3cPseProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 5),
    _Hh3cPseProfilePriority_Type()
)
hh3cPseProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfilePriority.setStatus("current")


class _Hh3cPseProfilePairs_Type(Integer32):
    """Custom type hh3cPseProfilePairs based on Integer32"""
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


_Hh3cPseProfilePairs_Type.__name__ = "Integer32"
_Hh3cPseProfilePairs_Object = MibTableColumn
hh3cPseProfilePairs = _Hh3cPseProfilePairs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 6),
    _Hh3cPseProfilePairs_Type()
)
hh3cPseProfilePairs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfilePairs.setStatus("current")
_Hh3cPseProfileApplyNum_Type = Integer32
_Hh3cPseProfileApplyNum_Object = MibTableColumn
hh3cPseProfileApplyNum = _Hh3cPseProfileApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 7),
    _Hh3cPseProfileApplyNum_Type()
)
hh3cPseProfileApplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPseProfileApplyNum.setStatus("current")
_Hh3cPseProfileRowStatus_Type = RowStatus
_Hh3cPseProfileRowStatus_Object = MibTableColumn
hh3cPseProfileRowStatus = _Hh3cPseProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 7, 1, 8),
    _Hh3cPseProfileRowStatus_Type()
)
hh3cPseProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPseProfileRowStatus.setStatus("current")
_Hh3cPOEPowerObjects_ObjectIdentity = ObjectIdentity
hh3cPOEPowerObjects = _Hh3cPOEPowerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8)
)
_Hh3cPOEThresholdLimitObjs_ObjectIdentity = ObjectIdentity
hh3cPOEThresholdLimitObjs = _Hh3cPOEThresholdLimitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1)
)


class _Hh3cPOEThresholdACMimimum_Type(OctetString):
    """Custom type hh3cPOEThresholdACMimimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEThresholdACMimimum_Type.__name__ = "OctetString"
_Hh3cPOEThresholdACMimimum_Object = MibScalar
hh3cPOEThresholdACMimimum = _Hh3cPOEThresholdACMimimum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 1),
    _Hh3cPOEThresholdACMimimum_Type()
)
hh3cPOEThresholdACMimimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPOEThresholdACMimimum.setStatus("current")


class _Hh3cPOEThresholdACMaximum_Type(OctetString):
    """Custom type hh3cPOEThresholdACMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEThresholdACMaximum_Type.__name__ = "OctetString"
_Hh3cPOEThresholdACMaximum_Object = MibScalar
hh3cPOEThresholdACMaximum = _Hh3cPOEThresholdACMaximum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 2),
    _Hh3cPOEThresholdACMaximum_Type()
)
hh3cPOEThresholdACMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPOEThresholdACMaximum.setStatus("current")


class _Hh3cPOEThresholdDCMinimum_Type(OctetString):
    """Custom type hh3cPOEThresholdDCMinimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEThresholdDCMinimum_Type.__name__ = "OctetString"
_Hh3cPOEThresholdDCMinimum_Object = MibScalar
hh3cPOEThresholdDCMinimum = _Hh3cPOEThresholdDCMinimum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 3),
    _Hh3cPOEThresholdDCMinimum_Type()
)
hh3cPOEThresholdDCMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPOEThresholdDCMinimum.setStatus("current")


class _Hh3cPOEThresholdDCMaximum_Type(OctetString):
    """Custom type hh3cPOEThresholdDCMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEThresholdDCMaximum_Type.__name__ = "OctetString"
_Hh3cPOEThresholdDCMaximum_Object = MibScalar
hh3cPOEThresholdDCMaximum = _Hh3cPOEThresholdDCMaximum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 1, 4),
    _Hh3cPOEThresholdDCMaximum_Type()
)
hh3cPOEThresholdDCMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPOEThresholdDCMaximum.setStatus("current")
_Hh3cPOESupModuleInfoObjs_ObjectIdentity = ObjectIdentity
hh3cPOESupModuleInfoObjs = _Hh3cPOESupModuleInfoObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2)
)


class _Hh3cPOEPowerType_Type(OctetString):
    """Custom type hh3cPOEPowerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cPOEPowerType_Type.__name__ = "OctetString"
_Hh3cPOEPowerType_Object = MibScalar
hh3cPOEPowerType = _Hh3cPOEPowerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 1),
    _Hh3cPOEPowerType_Type()
)
hh3cPOEPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEPowerType.setStatus("current")
_Hh3cPOEPowerModuleNum_Type = Integer32
_Hh3cPOEPowerModuleNum_Object = MibScalar
hh3cPOEPowerModuleNum = _Hh3cPOEPowerModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 2),
    _Hh3cPOEPowerModuleNum_Type()
)
hh3cPOEPowerModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEPowerModuleNum.setStatus("current")


class _Hh3cPOESupervisionModuleName_Type(OctetString):
    """Custom type hh3cPOESupervisionModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cPOESupervisionModuleName_Type.__name__ = "OctetString"
_Hh3cPOESupervisionModuleName_Object = MibScalar
hh3cPOESupervisionModuleName = _Hh3cPOESupervisionModuleName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 3),
    _Hh3cPOESupervisionModuleName_Type()
)
hh3cPOESupervisionModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESupervisionModuleName.setStatus("current")
_Hh3cPOESMMajorVersion_Type = Integer32
_Hh3cPOESMMajorVersion_Object = MibScalar
hh3cPOESMMajorVersion = _Hh3cPOESMMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 4),
    _Hh3cPOESMMajorVersion_Type()
)
hh3cPOESMMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESMMajorVersion.setStatus("current")
_Hh3cPOESMMinorVersion_Type = Integer32
_Hh3cPOESMMinorVersion_Object = MibScalar
hh3cPOESMMinorVersion = _Hh3cPOESMMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 5),
    _Hh3cPOESMMinorVersion_Type()
)
hh3cPOESMMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESMMinorVersion.setStatus("current")


class _Hh3cPOESMFactorName_Type(OctetString):
    """Custom type hh3cPOESMFactorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cPOESMFactorName_Type.__name__ = "OctetString"
_Hh3cPOESMFactorName_Object = MibScalar
hh3cPOESMFactorName = _Hh3cPOESMFactorName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 6),
    _Hh3cPOESMFactorName_Type()
)
hh3cPOESMFactorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESMFactorName.setStatus("current")
_Hh3cPOEModuleInfoTable_Object = MibTable
hh3cPOEModuleInfoTable = _Hh3cPOEModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cPOEModuleInfoTable.setStatus("current")
_Hh3cPOEModuleInfoEntry_Object = MibTableRow
hh3cPOEModuleInfoEntry = _Hh3cPOEModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1)
)
hh3cPOEModuleInfoEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOEModuleInfoEntry.setStatus("current")


class _Hh3cPOEModuleIndex_Type(Integer32):
    """Custom type hh3cPOEModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOEModuleIndex_Type.__name__ = "Integer32"
_Hh3cPOEModuleIndex_Object = MibTableColumn
hh3cPOEModuleIndex = _Hh3cPOEModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 1),
    _Hh3cPOEModuleIndex_Type()
)
hh3cPOEModuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOEModuleIndex.setStatus("current")
_Hh3cPOEModuleID_Type = Integer32
_Hh3cPOEModuleID_Object = MibTableColumn
hh3cPOEModuleID = _Hh3cPOEModuleID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 2),
    _Hh3cPOEModuleID_Type()
)
hh3cPOEModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleID.setStatus("current")
_Hh3cPOEModuleInfoPower_Type = Integer32
_Hh3cPOEModuleInfoPower_Object = MibTableColumn
hh3cPOEModuleInfoPower = _Hh3cPOEModuleInfoPower_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 3),
    _Hh3cPOEModuleInfoPower_Type()
)
hh3cPOEModuleInfoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleInfoPower.setStatus("current")


class _Hh3cPOEModuleHardVerInfo_Type(OctetString):
    """Custom type hh3cPOEModuleHardVerInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_Hh3cPOEModuleHardVerInfo_Type.__name__ = "OctetString"
_Hh3cPOEModuleHardVerInfo_Object = MibTableColumn
hh3cPOEModuleHardVerInfo = _Hh3cPOEModuleHardVerInfo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 2, 7, 1, 4),
    _Hh3cPOEModuleHardVerInfo_Type()
)
hh3cPOEModuleHardVerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleHardVerInfo.setStatus("current")
_Hh3cPOEDCOutStateObjects_ObjectIdentity = ObjectIdentity
hh3cPOEDCOutStateObjects = _Hh3cPOEDCOutStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3)
)
_Hh3cPOEDCOutStateModuleNum_Type = Integer32
_Hh3cPOEDCOutStateModuleNum_Object = MibScalar
hh3cPOEDCOutStateModuleNum = _Hh3cPOEDCOutStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 1),
    _Hh3cPOEDCOutStateModuleNum_Type()
)
hh3cPOEDCOutStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEDCOutStateModuleNum.setStatus("current")
_Hh3cPOEDCOutStateTable_Object = MibTable
hh3cPOEDCOutStateTable = _Hh3cPOEDCOutStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cPOEDCOutStateTable.setStatus("current")
_Hh3cPOEDCOutStateEntry_Object = MibTableRow
hh3cPOEDCOutStateEntry = _Hh3cPOEDCOutStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1)
)
hh3cPOEDCOutStateEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOEDCOutStateEntry.setStatus("current")


class _Hh3cPOEDCOutStateIndex_Type(Integer32):
    """Custom type hh3cPOEDCOutStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOEDCOutStateIndex_Type.__name__ = "Integer32"
_Hh3cPOEDCOutStateIndex_Object = MibTableColumn
hh3cPOEDCOutStateIndex = _Hh3cPOEDCOutStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1, 1),
    _Hh3cPOEDCOutStateIndex_Type()
)
hh3cPOEDCOutStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOEDCOutStateIndex.setStatus("current")
_Hh3cPOEDCOutDCVolAlarm_Type = DCAlarmState
_Hh3cPOEDCOutDCVolAlarm_Object = MibTableColumn
hh3cPOEDCOutDCVolAlarm = _Hh3cPOEDCOutDCVolAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 3, 2, 1, 2),
    _Hh3cPOEDCOutDCVolAlarm_Type()
)
hh3cPOEDCOutDCVolAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEDCOutDCVolAlarm.setStatus("current")
_Hh3cPOEDCOutInfoObjects_ObjectIdentity = ObjectIdentity
hh3cPOEDCOutInfoObjects = _Hh3cPOEDCOutInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4)
)
_Hh3cPOEDCOutCurNum_Type = Integer32
_Hh3cPOEDCOutCurNum_Object = MibScalar
hh3cPOEDCOutCurNum = _Hh3cPOEDCOutCurNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 1),
    _Hh3cPOEDCOutCurNum_Type()
)
hh3cPOEDCOutCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEDCOutCurNum.setStatus("current")
_Hh3cPOEDCOutInfoTable_Object = MibTable
hh3cPOEDCOutInfoTable = _Hh3cPOEDCOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2)
)
if mibBuilder.loadTexts:
    hh3cPOEDCOutInfoTable.setStatus("current")
_Hh3cPOEDCOutInfoEntry_Object = MibTableRow
hh3cPOEDCOutInfoEntry = _Hh3cPOEDCOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1)
)
hh3cPOEDCOutInfoEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutInfoIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOEDCOutInfoEntry.setStatus("current")


class _Hh3cPOEDCOutInfoIndex_Type(Integer32):
    """Custom type hh3cPOEDCOutInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOEDCOutInfoIndex_Type.__name__ = "Integer32"
_Hh3cPOEDCOutInfoIndex_Object = MibTableColumn
hh3cPOEDCOutInfoIndex = _Hh3cPOEDCOutInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 1),
    _Hh3cPOEDCOutInfoIndex_Type()
)
hh3cPOEDCOutInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOEDCOutInfoIndex.setStatus("current")


class _Hh3cPOEDCOutVol_Type(OctetString):
    """Custom type hh3cPOEDCOutVol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEDCOutVol_Type.__name__ = "OctetString"
_Hh3cPOEDCOutVol_Object = MibTableColumn
hh3cPOEDCOutVol = _Hh3cPOEDCOutVol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 2),
    _Hh3cPOEDCOutVol_Type()
)
hh3cPOEDCOutVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEDCOutVol.setStatus("current")


class _Hh3cPOEDCOutInfoLoadCur_Type(OctetString):
    """Custom type hh3cPOEDCOutInfoLoadCur based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_Hh3cPOEDCOutInfoLoadCur_Type.__name__ = "OctetString"
_Hh3cPOEDCOutInfoLoadCur_Object = MibTableColumn
hh3cPOEDCOutInfoLoadCur = _Hh3cPOEDCOutInfoLoadCur_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 4, 2, 1, 3),
    _Hh3cPOEDCOutInfoLoadCur_Type()
)
hh3cPOEDCOutInfoLoadCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEDCOutInfoLoadCur.setStatus("current")
_Hh3cPOEACSwitchStateModuleObjs_ObjectIdentity = ObjectIdentity
hh3cPOEACSwitchStateModuleObjs = _Hh3cPOEACSwitchStateModuleObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5)
)
_Hh3cPOEACSwitchStateModuleNum_Type = Integer32
_Hh3cPOEACSwitchStateModuleNum_Object = MibScalar
hh3cPOEACSwitchStateModuleNum = _Hh3cPOEACSwitchStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 1),
    _Hh3cPOEACSwitchStateModuleNum_Type()
)
hh3cPOEACSwitchStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEACSwitchStateModuleNum.setStatus("current")
_Hh3cPOEACSwitchStateTable_Object = MibTable
hh3cPOEACSwitchStateTable = _Hh3cPOEACSwitchStateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2)
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchStateTable.setStatus("current")
_Hh3cPOEACSwitchStateEntry_Object = MibTableRow
hh3cPOEACSwitchStateEntry = _Hh3cPOEACSwitchStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1)
)
hh3cPOEACSwitchStateEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchStateEntry.setStatus("current")


class _Hh3cPOEACSwitchStateIndex_Type(Integer32):
    """Custom type hh3cPOEACSwitchStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOEACSwitchStateIndex_Type.__name__ = "Integer32"
_Hh3cPOEACSwitchStateIndex_Object = MibTableColumn
hh3cPOEACSwitchStateIndex = _Hh3cPOEACSwitchStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1, 1),
    _Hh3cPOEACSwitchStateIndex_Type()
)
hh3cPOEACSwitchStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOEACSwitchStateIndex.setStatus("current")
_Hh3cPOEACSwitchState_Type = SwitchState
_Hh3cPOEACSwitchState_Object = MibTableColumn
hh3cPOEACSwitchState = _Hh3cPOEACSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 5, 2, 1, 2),
    _Hh3cPOEACSwitchState_Type()
)
hh3cPOEACSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEACSwitchState.setStatus("current")
_Hh3cPOEInCurStateObjects_ObjectIdentity = ObjectIdentity
hh3cPOEInCurStateObjects = _Hh3cPOEInCurStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6)
)
_Hh3cPOEInCurStateModuleNum_Type = Integer32
_Hh3cPOEInCurStateModuleNum_Object = MibScalar
hh3cPOEInCurStateModuleNum = _Hh3cPOEInCurStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 1),
    _Hh3cPOEInCurStateModuleNum_Type()
)
hh3cPOEInCurStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEInCurStateModuleNum.setStatus("current")
_Hh3cPOEInCurAState_Type = ACAlarmState
_Hh3cPOEInCurAState_Object = MibScalar
hh3cPOEInCurAState = _Hh3cPOEInCurAState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 2),
    _Hh3cPOEInCurAState_Type()
)
hh3cPOEInCurAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEInCurAState.setStatus("current")
_Hh3cPOEInCurBState_Type = ACAlarmState
_Hh3cPOEInCurBState_Object = MibScalar
hh3cPOEInCurBState = _Hh3cPOEInCurBState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 3),
    _Hh3cPOEInCurBState_Type()
)
hh3cPOEInCurBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEInCurBState.setStatus("current")
_Hh3cPOEInCurCState_Type = ACAlarmState
_Hh3cPOEInCurCState_Object = MibScalar
hh3cPOEInCurCState = _Hh3cPOEInCurCState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 4),
    _Hh3cPOEInCurCState_Type()
)
hh3cPOEInCurCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEInCurCState.setStatus("current")
_Hh3cPOESwitchStateVolExTable_Object = MibTable
hh3cPOESwitchStateVolExTable = _Hh3cPOESwitchStateVolExTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5)
)
if mibBuilder.loadTexts:
    hh3cPOESwitchStateVolExTable.setStatus("current")
_Hh3cPOESwitchStateVolExEntry_Object = MibTableRow
hh3cPOESwitchStateVolExEntry = _Hh3cPOESwitchStateVolExEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1)
)
hh3cPOESwitchStateVolExEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOESwitchStateVolExEntry.setStatus("current")


class _Hh3cPOESwitchStateVolExIndex_Type(Integer32):
    """Custom type hh3cPOESwitchStateVolExIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOESwitchStateVolExIndex_Type.__name__ = "Integer32"
_Hh3cPOESwitchStateVolExIndex_Object = MibTableColumn
hh3cPOESwitchStateVolExIndex = _Hh3cPOESwitchStateVolExIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 1),
    _Hh3cPOESwitchStateVolExIndex_Type()
)
hh3cPOESwitchStateVolExIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOESwitchStateVolExIndex.setStatus("current")
_Hh3cPOESwitchStateInVolAB_Type = ACAlarmState
_Hh3cPOESwitchStateInVolAB_Object = MibTableColumn
hh3cPOESwitchStateInVolAB = _Hh3cPOESwitchStateInVolAB_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 2),
    _Hh3cPOESwitchStateInVolAB_Type()
)
hh3cPOESwitchStateInVolAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESwitchStateInVolAB.setStatus("current")
_Hh3cPOESwitchStateInVolBC_Type = ACAlarmState
_Hh3cPOESwitchStateInVolBC_Object = MibTableColumn
hh3cPOESwitchStateInVolBC = _Hh3cPOESwitchStateInVolBC_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 3),
    _Hh3cPOESwitchStateInVolBC_Type()
)
hh3cPOESwitchStateInVolBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESwitchStateInVolBC.setStatus("current")
_Hh3cPOESwitchStateInVolCA_Type = ACAlarmState
_Hh3cPOESwitchStateInVolCA_Object = MibTableColumn
hh3cPOESwitchStateInVolCA = _Hh3cPOESwitchStateInVolCA_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 6, 5, 1, 4),
    _Hh3cPOESwitchStateInVolCA_Type()
)
hh3cPOESwitchStateInVolCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOESwitchStateInVolCA.setStatus("current")
_Hh3cPOEAlarmStateObjects_ObjectIdentity = ObjectIdentity
hh3cPOEAlarmStateObjects = _Hh3cPOEAlarmStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7)
)
_Hh3cPOEAlarmStateModuleNum_Type = Integer32
_Hh3cPOEAlarmStateModuleNum_Object = MibScalar
hh3cPOEAlarmStateModuleNum = _Hh3cPOEAlarmStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 1),
    _Hh3cPOEAlarmStateModuleNum_Type()
)
hh3cPOEAlarmStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEAlarmStateModuleNum.setStatus("current")
_Hh3cPOEAlarmStateInfoTable_Object = MibTable
hh3cPOEAlarmStateInfoTable = _Hh3cPOEAlarmStateInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2)
)
if mibBuilder.loadTexts:
    hh3cPOEAlarmStateInfoTable.setStatus("current")
_Hh3cPOEAlarmStateInfoEntry_Object = MibTableRow
hh3cPOEAlarmStateInfoEntry = _Hh3cPOEAlarmStateInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1)
)
hh3cPOEAlarmStateInfoEntry.setIndexNames(
    (0, "HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    hh3cPOEAlarmStateInfoEntry.setStatus("current")


class _Hh3cPOEAlarmModuleInfoIndex_Type(Integer32):
    """Custom type hh3cPOEAlarmModuleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cPOEAlarmModuleInfoIndex_Type.__name__ = "Integer32"
_Hh3cPOEAlarmModuleInfoIndex_Object = MibTableColumn
hh3cPOEAlarmModuleInfoIndex = _Hh3cPOEAlarmModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 1),
    _Hh3cPOEAlarmModuleInfoIndex_Type()
)
hh3cPOEAlarmModuleInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cPOEAlarmModuleInfoIndex.setStatus("current")
_Hh3cPOEModuleDisconnect_Type = ModuleAlarmState
_Hh3cPOEModuleDisconnect_Object = MibTableColumn
hh3cPOEModuleDisconnect = _Hh3cPOEModuleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 2),
    _Hh3cPOEModuleDisconnect_Type()
)
hh3cPOEModuleDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleDisconnect.setStatus("current")
_Hh3cPOEModuleInputError_Type = ModuleAlarmState
_Hh3cPOEModuleInputError_Object = MibTableColumn
hh3cPOEModuleInputError = _Hh3cPOEModuleInputError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 3),
    _Hh3cPOEModuleInputError_Type()
)
hh3cPOEModuleInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleInputError.setStatus("current")
_Hh3cPOEModuleOutputError_Type = ModuleAlarmState
_Hh3cPOEModuleOutputError_Object = MibTableColumn
hh3cPOEModuleOutputError = _Hh3cPOEModuleOutputError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 4),
    _Hh3cPOEModuleOutputError_Type()
)
hh3cPOEModuleOutputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleOutputError.setStatus("current")
_Hh3cPOEModuleOverVoltage_Type = ModuleAlarmState
_Hh3cPOEModuleOverVoltage_Object = MibTableColumn
hh3cPOEModuleOverVoltage = _Hh3cPOEModuleOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 5),
    _Hh3cPOEModuleOverVoltage_Type()
)
hh3cPOEModuleOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleOverVoltage.setStatus("current")
_Hh3cPOEModuleOverTemp_Type = ModuleAlarmState
_Hh3cPOEModuleOverTemp_Object = MibTableColumn
hh3cPOEModuleOverTemp = _Hh3cPOEModuleOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 6),
    _Hh3cPOEModuleOverTemp_Type()
)
hh3cPOEModuleOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleOverTemp.setStatus("current")
_Hh3cPOEModuleFanError_Type = ModuleAlarmState
_Hh3cPOEModuleFanError_Object = MibTableColumn
hh3cPOEModuleFanError = _Hh3cPOEModuleFanError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 7),
    _Hh3cPOEModuleFanError_Type()
)
hh3cPOEModuleFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleFanError.setStatus("current")
_Hh3cPOEModuleShutdown_Type = ModuleAlarmState
_Hh3cPOEModuleShutdown_Object = MibTableColumn
hh3cPOEModuleShutdown = _Hh3cPOEModuleShutdown_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 8),
    _Hh3cPOEModuleShutdown_Type()
)
hh3cPOEModuleShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleShutdown.setStatus("current")
_Hh3cPOEModuleCurRestricted_Type = ModuleAlarmState
_Hh3cPOEModuleCurRestricted_Object = MibTableColumn
hh3cPOEModuleCurRestricted = _Hh3cPOEModuleCurRestricted_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 8, 7, 2, 1, 9),
    _Hh3cPOEModuleCurRestricted_Type()
)
hh3cPOEModuleCurRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cPOEModuleCurRestricted.setStatus("current")


class _Hh3cPsePolicyMode_Type(Integer32):
    """Custom type hh3cPsePolicyMode based on Integer32"""
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


_Hh3cPsePolicyMode_Type.__name__ = "Integer32"
_Hh3cPsePolicyMode_Object = MibScalar
hh3cPsePolicyMode = _Hh3cPsePolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 9),
    _Hh3cPsePolicyMode_Type()
)
hh3cPsePolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPsePolicyMode.setStatus("current")


class _Hh3cPDPolicyMode_Type(Integer32):
    """Custom type hh3cPDPolicyMode based on Integer32"""
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


_Hh3cPDPolicyMode_Type.__name__ = "Integer32"
_Hh3cPDPolicyMode_Object = MibScalar
hh3cPDPolicyMode = _Hh3cPDPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 10),
    _Hh3cPDPolicyMode_Type()
)
hh3cPDPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cPDPolicyMode.setStatus("current")

# Managed Objects groups

hh3cPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 1)
)
hh3cPsePortGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortProfileIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortPowerLimit"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortCurrentPower"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortAveragePower"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortPeakPower"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePortFaultDescription"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePriorityMode"))
)
if mibBuilder.loadTexts:
    hh3cPsePortGroup.setStatus("current")

hh3cMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 2)
)
hh3cMainPseGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePowerLimit"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPseAveragePower"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainPsePeakPower"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cMainGuaranteedPowerRemaining"))
)
if mibBuilder.loadTexts:
    hh3cMainPseGroup.setStatus("current")

hh3cPseScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 3)
)
hh3cPseScalarGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPseAutoDetectActive"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePowerMaxValue"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPsePolicyMode"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPDPolicyMode"))
)
if mibBuilder.loadTexts:
    hh3cPseScalarGroup.setStatus("current")

hh3cPsePDNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 4)
)
hh3cPsePDNotificationGroup.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cpsePDChangeNotification")
)
if mibBuilder.loadTexts:
    hh3cPsePDNotificationGroup.setStatus("current")

hh3cPseProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 5)
)
hh3cPseProfilesGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileName"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePowerMode"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePowerLimit"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePriority"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfilePairs"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileApplyNum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPseProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hh3cPseProfilesGroup.setStatus("current")

hh3cPOEPowerThresholdLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 6)
)
hh3cPOEPowerThresholdLimitGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdACMimimum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdACMaximum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdDCMinimum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEThresholdDCMaximum"))
)
if mibBuilder.loadTexts:
    hh3cPOEPowerThresholdLimitGroup.setStatus("current")

hh3cPOEPowerSupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 7)
)
hh3cPOEPowerSupInfoGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEPowerType"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEPowerModuleNum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESupervisionModuleName"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMMajorVersion"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMMinorVersion"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESMFactorName"))
)
if mibBuilder.loadTexts:
    hh3cPOEPowerSupInfoGroup.setStatus("current")

hh3cPOEPowerDCOutStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 8)
)
hh3cPOEPowerDCOutStateGroup.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateModuleNum")
)
if mibBuilder.loadTexts:
    hh3cPOEPowerDCOutStateGroup.setStatus("current")

hh3cPOEPowerDCOutInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 9)
)
hh3cPOEPowerDCOutInfoGroup.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutCurNum")
)
if mibBuilder.loadTexts:
    hh3cPOEPowerDCOutInfoGroup.setStatus("current")

hh3cPOEPowerACSwitchStateModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 10)
)
hh3cPOEPowerACSwitchStateModuleGroup.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateModuleNum")
)
if mibBuilder.loadTexts:
    hh3cPOEPowerACSwitchStateModuleGroup.setStatus("current")

hh3cPOEPowerInCurStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 11)
)
hh3cPOEPowerInCurStateGroup.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurStateModuleNum"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurAState"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurBState"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurCState"))
)
if mibBuilder.loadTexts:
    hh3cPOEPowerInCurStateGroup.setStatus("current")

hh3cPOEPowerAlarmStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 2, 12)
)
hh3cPOEPowerAlarmStateGroup.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmStateModuleNum")
)
if mibBuilder.loadTexts:
    hh3cPOEPowerAlarmStateGroup.setStatus("current")


# Notification objects

hh3cpsePDChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 1)
)
hh3cpsePDChangeNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    hh3cpsePDChangeNotification.setStatus(
        "current"
    )

hh3cPOEDisconnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 2)
)
hh3cPOEDisconnectNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleDisconnect"))
)
if mibBuilder.loadTexts:
    hh3cPOEDisconnectNotification.setStatus(
        "current"
    )

hh3cPOEInputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 3)
)
hh3cPOEInputErrorNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleInputError"))
)
if mibBuilder.loadTexts:
    hh3cPOEInputErrorNotification.setStatus(
        "current"
    )

hh3cPOEOutputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 4)
)
hh3cPOEOutputErrorNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOutputError"))
)
if mibBuilder.loadTexts:
    hh3cPOEOutputErrorNotification.setStatus(
        "current"
    )

hh3cPOEOverVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 5)
)
hh3cPOEOverVoltageNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOverVoltage"))
)
if mibBuilder.loadTexts:
    hh3cPOEOverVoltageNotification.setStatus(
        "current"
    )

hh3cPOEOverTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 6)
)
hh3cPOEOverTempNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleOverTemp"))
)
if mibBuilder.loadTexts:
    hh3cPOEOverTempNotification.setStatus(
        "current"
    )

hh3cPOEFanErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 7)
)
hh3cPOEFanErrorNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleFanError"))
)
if mibBuilder.loadTexts:
    hh3cPOEFanErrorNotification.setStatus(
        "current"
    )

hh3cPOEModuleShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 8)
)
hh3cPOEModuleShutdownNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleShutdown"))
)
if mibBuilder.loadTexts:
    hh3cPOEModuleShutdownNotification.setStatus(
        "current"
    )

hh3cPOECurRestrictedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 9)
)
hh3cPOECurRestrictedNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEAlarmModuleInfoIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEModuleCurRestricted"))
)
if mibBuilder.loadTexts:
    hh3cPOECurRestrictedNotification.setStatus(
        "current"
    )

hh3cPOEACSwitchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 10)
)
hh3cPOEACSwitchNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchStateIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEACSwitchState"))
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchNotification.setStatus(
        "current"
    )

hh3cPOEACInCurANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 11)
)
hh3cPOEACInCurANotification.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurAState")
)
if mibBuilder.loadTexts:
    hh3cPOEACInCurANotification.setStatus(
        "current"
    )

hh3cPOEACInCurBNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 12)
)
hh3cPOEACInCurBNotification.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurBState")
)
if mibBuilder.loadTexts:
    hh3cPOEACInCurBNotification.setStatus(
        "current"
    )

hh3cPOEACInCurCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 13)
)
hh3cPOEACInCurCNotification.setObjects(
    ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEInCurCState")
)
if mibBuilder.loadTexts:
    hh3cPOEACInCurCNotification.setStatus(
        "current"
    )

hh3cPOEACSwitchVolABNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 14)
)
hh3cPOEACSwitchVolABNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolAB"))
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchVolABNotification.setStatus(
        "current"
    )

hh3cPOEACSwitchVolBCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 15)
)
hh3cPOEACSwitchVolBCNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolBC"))
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchVolBCNotification.setStatus(
        "current"
    )

hh3cPOEACSwitchVolCANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 16)
)
hh3cPOEACSwitchVolCANotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateVolExIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOESwitchStateInVolCA"))
)
if mibBuilder.loadTexts:
    hh3cPOEACSwitchVolCANotification.setStatus(
        "current"
    )

hh3cPOEDCOutVolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 17)
)
hh3cPOEDCOutVolNotification.setObjects(
      *(("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutStateIndex"),
        ("HH3C-POWER-ETH-EXT-MIB", "hh3cPOEDCOutDCVolAlarm"))
)
if mibBuilder.loadTexts:
    hh3cPOEDCOutVolNotification.setStatus(
        "current"
    )

hh3cPOEShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 6, 18)
)
if mibBuilder.loadTexts:
    hh3cPOEShutdownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

hh3cPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25506, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cPseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-POWER-ETH-EXT-MIB",
    **{"ACAlarmState": ACAlarmState,
       "DCAlarmState": DCAlarmState,
       "SwitchState": SwitchState,
       "ModuleAlarmState": ModuleAlarmState,
       "hh3cPowerEthernetExt": hh3cPowerEthernetExt,
       "hh3cPsePortTable": hh3cPsePortTable,
       "hh3cPsePortEntry": hh3cPsePortEntry,
       "hh3cPsePortFaultDescription": hh3cPsePortFaultDescription,
       "hh3cPsePortPeakPower": hh3cPsePortPeakPower,
       "hh3cPsePortAveragePower": hh3cPsePortAveragePower,
       "hh3cPsePortCurrentPower": hh3cPsePortCurrentPower,
       "hh3cPsePortPowerLimit": hh3cPsePortPowerLimit,
       "hh3cPsePortProfileIndex": hh3cPsePortProfileIndex,
       "hh3cMainPseTable": hh3cMainPseTable,
       "hh3cMainPseEntry": hh3cMainPseEntry,
       "hh3cMainPsePowerLimit": hh3cMainPsePowerLimit,
       "hh3cMainPseAveragePower": hh3cMainPseAveragePower,
       "hh3cMainPsePeakPower": hh3cMainPsePeakPower,
       "hh3cMainGuaranteedPowerRemaining": hh3cMainGuaranteedPowerRemaining,
       "hh3cMainPsePriorityMode": hh3cMainPsePriorityMode,
       "hh3cMainPseLegacy": hh3cMainPseLegacy,
       "hh3cMainPsePowerPriority": hh3cMainPsePowerPriority,
       "hh3cPseAutoDetectActive": hh3cPseAutoDetectActive,
       "hh3cPseComformance": hh3cPseComformance,
       "hh3cPseCompliances": hh3cPseCompliances,
       "hh3cPseCompliance": hh3cPseCompliance,
       "hh3cPseGroup": hh3cPseGroup,
       "hh3cPsePortGroup": hh3cPsePortGroup,
       "hh3cMainPseGroup": hh3cMainPseGroup,
       "hh3cPseScalarGroup": hh3cPseScalarGroup,
       "hh3cPsePDNotificationGroup": hh3cPsePDNotificationGroup,
       "hh3cPseProfilesGroup": hh3cPseProfilesGroup,
       "hh3cPOEPowerThresholdLimitGroup": hh3cPOEPowerThresholdLimitGroup,
       "hh3cPOEPowerSupInfoGroup": hh3cPOEPowerSupInfoGroup,
       "hh3cPOEPowerDCOutStateGroup": hh3cPOEPowerDCOutStateGroup,
       "hh3cPOEPowerDCOutInfoGroup": hh3cPOEPowerDCOutInfoGroup,
       "hh3cPOEPowerACSwitchStateModuleGroup": hh3cPOEPowerACSwitchStateModuleGroup,
       "hh3cPOEPowerInCurStateGroup": hh3cPOEPowerInCurStateGroup,
       "hh3cPOEPowerAlarmStateGroup": hh3cPOEPowerAlarmStateGroup,
       "hh3cPsePowerMaxValue": hh3cPsePowerMaxValue,
       "hh3cpseportNotification": hh3cpseportNotification,
       "hh3cpsePDChangeNotification": hh3cpsePDChangeNotification,
       "hh3cPOEDisconnectNotification": hh3cPOEDisconnectNotification,
       "hh3cPOEInputErrorNotification": hh3cPOEInputErrorNotification,
       "hh3cPOEOutputErrorNotification": hh3cPOEOutputErrorNotification,
       "hh3cPOEOverVoltageNotification": hh3cPOEOverVoltageNotification,
       "hh3cPOEOverTempNotification": hh3cPOEOverTempNotification,
       "hh3cPOEFanErrorNotification": hh3cPOEFanErrorNotification,
       "hh3cPOEModuleShutdownNotification": hh3cPOEModuleShutdownNotification,
       "hh3cPOECurRestrictedNotification": hh3cPOECurRestrictedNotification,
       "hh3cPOEACSwitchNotification": hh3cPOEACSwitchNotification,
       "hh3cPOEACInCurANotification": hh3cPOEACInCurANotification,
       "hh3cPOEACInCurBNotification": hh3cPOEACInCurBNotification,
       "hh3cPOEACInCurCNotification": hh3cPOEACInCurCNotification,
       "hh3cPOEACSwitchVolABNotification": hh3cPOEACSwitchVolABNotification,
       "hh3cPOEACSwitchVolBCNotification": hh3cPOEACSwitchVolBCNotification,
       "hh3cPOEACSwitchVolCANotification": hh3cPOEACSwitchVolCANotification,
       "hh3cPOEDCOutVolNotification": hh3cPOEDCOutVolNotification,
       "hh3cPOEShutdownNotification": hh3cPOEShutdownNotification,
       "hh3cPseProfilesTable": hh3cPseProfilesTable,
       "hh3cPseProfilesEntry": hh3cPseProfilesEntry,
       "hh3cPseProfileIndex": hh3cPseProfileIndex,
       "hh3cPseProfileName": hh3cPseProfileName,
       "hh3cPseProfilePowerMode": hh3cPseProfilePowerMode,
       "hh3cPseProfilePowerLimit": hh3cPseProfilePowerLimit,
       "hh3cPseProfilePriority": hh3cPseProfilePriority,
       "hh3cPseProfilePairs": hh3cPseProfilePairs,
       "hh3cPseProfileApplyNum": hh3cPseProfileApplyNum,
       "hh3cPseProfileRowStatus": hh3cPseProfileRowStatus,
       "hh3cPOEPowerObjects": hh3cPOEPowerObjects,
       "hh3cPOEThresholdLimitObjs": hh3cPOEThresholdLimitObjs,
       "hh3cPOEThresholdACMimimum": hh3cPOEThresholdACMimimum,
       "hh3cPOEThresholdACMaximum": hh3cPOEThresholdACMaximum,
       "hh3cPOEThresholdDCMinimum": hh3cPOEThresholdDCMinimum,
       "hh3cPOEThresholdDCMaximum": hh3cPOEThresholdDCMaximum,
       "hh3cPOESupModuleInfoObjs": hh3cPOESupModuleInfoObjs,
       "hh3cPOEPowerType": hh3cPOEPowerType,
       "hh3cPOEPowerModuleNum": hh3cPOEPowerModuleNum,
       "hh3cPOESupervisionModuleName": hh3cPOESupervisionModuleName,
       "hh3cPOESMMajorVersion": hh3cPOESMMajorVersion,
       "hh3cPOESMMinorVersion": hh3cPOESMMinorVersion,
       "hh3cPOESMFactorName": hh3cPOESMFactorName,
       "hh3cPOEModuleInfoTable": hh3cPOEModuleInfoTable,
       "hh3cPOEModuleInfoEntry": hh3cPOEModuleInfoEntry,
       "hh3cPOEModuleIndex": hh3cPOEModuleIndex,
       "hh3cPOEModuleID": hh3cPOEModuleID,
       "hh3cPOEModuleInfoPower": hh3cPOEModuleInfoPower,
       "hh3cPOEModuleHardVerInfo": hh3cPOEModuleHardVerInfo,
       "hh3cPOEDCOutStateObjects": hh3cPOEDCOutStateObjects,
       "hh3cPOEDCOutStateModuleNum": hh3cPOEDCOutStateModuleNum,
       "hh3cPOEDCOutStateTable": hh3cPOEDCOutStateTable,
       "hh3cPOEDCOutStateEntry": hh3cPOEDCOutStateEntry,
       "hh3cPOEDCOutStateIndex": hh3cPOEDCOutStateIndex,
       "hh3cPOEDCOutDCVolAlarm": hh3cPOEDCOutDCVolAlarm,
       "hh3cPOEDCOutInfoObjects": hh3cPOEDCOutInfoObjects,
       "hh3cPOEDCOutCurNum": hh3cPOEDCOutCurNum,
       "hh3cPOEDCOutInfoTable": hh3cPOEDCOutInfoTable,
       "hh3cPOEDCOutInfoEntry": hh3cPOEDCOutInfoEntry,
       "hh3cPOEDCOutInfoIndex": hh3cPOEDCOutInfoIndex,
       "hh3cPOEDCOutVol": hh3cPOEDCOutVol,
       "hh3cPOEDCOutInfoLoadCur": hh3cPOEDCOutInfoLoadCur,
       "hh3cPOEACSwitchStateModuleObjs": hh3cPOEACSwitchStateModuleObjs,
       "hh3cPOEACSwitchStateModuleNum": hh3cPOEACSwitchStateModuleNum,
       "hh3cPOEACSwitchStateTable": hh3cPOEACSwitchStateTable,
       "hh3cPOEACSwitchStateEntry": hh3cPOEACSwitchStateEntry,
       "hh3cPOEACSwitchStateIndex": hh3cPOEACSwitchStateIndex,
       "hh3cPOEACSwitchState": hh3cPOEACSwitchState,
       "hh3cPOEInCurStateObjects": hh3cPOEInCurStateObjects,
       "hh3cPOEInCurStateModuleNum": hh3cPOEInCurStateModuleNum,
       "hh3cPOEInCurAState": hh3cPOEInCurAState,
       "hh3cPOEInCurBState": hh3cPOEInCurBState,
       "hh3cPOEInCurCState": hh3cPOEInCurCState,
       "hh3cPOESwitchStateVolExTable": hh3cPOESwitchStateVolExTable,
       "hh3cPOESwitchStateVolExEntry": hh3cPOESwitchStateVolExEntry,
       "hh3cPOESwitchStateVolExIndex": hh3cPOESwitchStateVolExIndex,
       "hh3cPOESwitchStateInVolAB": hh3cPOESwitchStateInVolAB,
       "hh3cPOESwitchStateInVolBC": hh3cPOESwitchStateInVolBC,
       "hh3cPOESwitchStateInVolCA": hh3cPOESwitchStateInVolCA,
       "hh3cPOEAlarmStateObjects": hh3cPOEAlarmStateObjects,
       "hh3cPOEAlarmStateModuleNum": hh3cPOEAlarmStateModuleNum,
       "hh3cPOEAlarmStateInfoTable": hh3cPOEAlarmStateInfoTable,
       "hh3cPOEAlarmStateInfoEntry": hh3cPOEAlarmStateInfoEntry,
       "hh3cPOEAlarmModuleInfoIndex": hh3cPOEAlarmModuleInfoIndex,
       "hh3cPOEModuleDisconnect": hh3cPOEModuleDisconnect,
       "hh3cPOEModuleInputError": hh3cPOEModuleInputError,
       "hh3cPOEModuleOutputError": hh3cPOEModuleOutputError,
       "hh3cPOEModuleOverVoltage": hh3cPOEModuleOverVoltage,
       "hh3cPOEModuleOverTemp": hh3cPOEModuleOverTemp,
       "hh3cPOEModuleFanError": hh3cPOEModuleFanError,
       "hh3cPOEModuleShutdown": hh3cPOEModuleShutdown,
       "hh3cPOEModuleCurRestricted": hh3cPOEModuleCurRestricted,
       "hh3cPsePolicyMode": hh3cPsePolicyMode,
       "hh3cPDPolicyMode": hh3cPDPolicyMode}
)
