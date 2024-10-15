# SNMP MIB module (H3C-POWER-ETH-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-POWER-ETH-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:09 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cPowerEthernetExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14)
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

_H3cPsePortTable_Object = MibTable
h3cPsePortTable = _H3cPsePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1)
)
if mibBuilder.loadTexts:
    h3cPsePortTable.setStatus("current")
_H3cPsePortEntry_Object = MibTableRow
h3cPsePortEntry = _H3cPsePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1)
)
h3cPsePortEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"),
    (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"),
)
if mibBuilder.loadTexts:
    h3cPsePortEntry.setStatus("current")
_H3cPsePortFaultDescription_Type = DisplayString
_H3cPsePortFaultDescription_Object = MibTableColumn
h3cPsePortFaultDescription = _H3cPsePortFaultDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 2),
    _H3cPsePortFaultDescription_Type()
)
h3cPsePortFaultDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePortFaultDescription.setStatus("current")
_H3cPsePortPeakPower_Type = Integer32
_H3cPsePortPeakPower_Object = MibTableColumn
h3cPsePortPeakPower = _H3cPsePortPeakPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 3),
    _H3cPsePortPeakPower_Type()
)
h3cPsePortPeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePortPeakPower.setStatus("current")
_H3cPsePortAveragePower_Type = Integer32
_H3cPsePortAveragePower_Object = MibTableColumn
h3cPsePortAveragePower = _H3cPsePortAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 4),
    _H3cPsePortAveragePower_Type()
)
h3cPsePortAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePortAveragePower.setStatus("current")
_H3cPsePortCurrentPower_Type = Integer32
_H3cPsePortCurrentPower_Object = MibTableColumn
h3cPsePortCurrentPower = _H3cPsePortCurrentPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 5),
    _H3cPsePortCurrentPower_Type()
)
h3cPsePortCurrentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPsePortCurrentPower.setStatus("current")
_H3cPsePortPowerLimit_Type = Integer32
_H3cPsePortPowerLimit_Object = MibTableColumn
h3cPsePortPowerLimit = _H3cPsePortPowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 6),
    _H3cPsePortPowerLimit_Type()
)
h3cPsePortPowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePortPowerLimit.setStatus("current")


class _H3cPsePortProfileIndex_Type(Integer32):
    """Custom type h3cPsePortProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cPsePortProfileIndex_Type.__name__ = "Integer32"
_H3cPsePortProfileIndex_Object = MibTableColumn
h3cPsePortProfileIndex = _H3cPsePortProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 1, 1, 7),
    _H3cPsePortProfileIndex_Type()
)
h3cPsePortProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePortProfileIndex.setStatus("current")
_H3cMainPseTable_Object = MibTable
h3cMainPseTable = _H3cMainPseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2)
)
if mibBuilder.loadTexts:
    h3cMainPseTable.setStatus("current")
_H3cMainPseEntry_Object = MibTableRow
h3cMainPseEntry = _H3cMainPseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1)
)
h3cMainPseEntry.setIndexNames(
    (0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"),
)
if mibBuilder.loadTexts:
    h3cMainPseEntry.setStatus("current")
_H3cMainPsePowerLimit_Type = Integer32
_H3cMainPsePowerLimit_Object = MibTableColumn
h3cMainPsePowerLimit = _H3cMainPsePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 1),
    _H3cMainPsePowerLimit_Type()
)
h3cMainPsePowerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPsePowerLimit.setStatus("current")
_H3cMainPseAveragePower_Type = Integer32
_H3cMainPseAveragePower_Object = MibTableColumn
h3cMainPseAveragePower = _H3cMainPseAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 2),
    _H3cMainPseAveragePower_Type()
)
h3cMainPseAveragePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPseAveragePower.setStatus("current")
_H3cMainPsePeakPower_Type = Integer32
_H3cMainPsePeakPower_Object = MibTableColumn
h3cMainPsePeakPower = _H3cMainPsePeakPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 3),
    _H3cMainPsePeakPower_Type()
)
h3cMainPsePeakPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPsePeakPower.setStatus("current")
_H3cMainGuaranteedPowerRemaining_Type = Integer32
_H3cMainGuaranteedPowerRemaining_Object = MibTableColumn
h3cMainGuaranteedPowerRemaining = _H3cMainGuaranteedPowerRemaining_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 4),
    _H3cMainGuaranteedPowerRemaining_Type()
)
h3cMainGuaranteedPowerRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMainGuaranteedPowerRemaining.setStatus("current")


class _H3cMainPsePriorityMode_Type(Integer32):
    """Custom type h3cMainPsePriorityMode based on Integer32"""
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


_H3cMainPsePriorityMode_Type.__name__ = "Integer32"
_H3cMainPsePriorityMode_Object = MibTableColumn
h3cMainPsePriorityMode = _H3cMainPsePriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 5),
    _H3cMainPsePriorityMode_Type()
)
h3cMainPsePriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPsePriorityMode.setStatus("current")


class _H3cMainPseLegacy_Type(Integer32):
    """Custom type h3cMainPseLegacy based on Integer32"""
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


_H3cMainPseLegacy_Type.__name__ = "Integer32"
_H3cMainPseLegacy_Object = MibTableColumn
h3cMainPseLegacy = _H3cMainPseLegacy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 6),
    _H3cMainPseLegacy_Type()
)
h3cMainPseLegacy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPseLegacy.setStatus("current")


class _H3cMainPsePowerPriority_Type(Integer32):
    """Custom type h3cMainPsePowerPriority based on Integer32"""
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


_H3cMainPsePowerPriority_Type.__name__ = "Integer32"
_H3cMainPsePowerPriority_Object = MibTableColumn
h3cMainPsePowerPriority = _H3cMainPsePowerPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 2, 1, 7),
    _H3cMainPsePowerPriority_Type()
)
h3cMainPsePowerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMainPsePowerPriority.setStatus("current")


class _H3cPseAutoDetectActive_Type(Integer32):
    """Custom type h3cPseAutoDetectActive based on Integer32"""
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


_H3cPseAutoDetectActive_Type.__name__ = "Integer32"
_H3cPseAutoDetectActive_Object = MibScalar
h3cPseAutoDetectActive = _H3cPseAutoDetectActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 3),
    _H3cPseAutoDetectActive_Type()
)
h3cPseAutoDetectActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPseAutoDetectActive.setStatus("current")
_H3cPseComformance_ObjectIdentity = ObjectIdentity
h3cPseComformance = _H3cPseComformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4)
)
_H3cPseCompliances_ObjectIdentity = ObjectIdentity
h3cPseCompliances = _H3cPseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 1)
)
_H3cPseGroup_ObjectIdentity = ObjectIdentity
h3cPseGroup = _H3cPseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2)
)
_H3cPsePowerMaxValue_Type = Integer32
_H3cPsePowerMaxValue_Object = MibScalar
h3cPsePowerMaxValue = _H3cPsePowerMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 5),
    _H3cPsePowerMaxValue_Type()
)
h3cPsePowerMaxValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePowerMaxValue.setStatus("current")
_H3cpseportNotification_ObjectIdentity = ObjectIdentity
h3cpseportNotification = _H3cpseportNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6)
)
_H3cPseProfilesTable_Object = MibTable
h3cPseProfilesTable = _H3cPseProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7)
)
if mibBuilder.loadTexts:
    h3cPseProfilesTable.setStatus("current")
_H3cPseProfilesEntry_Object = MibTableRow
h3cPseProfilesEntry = _H3cPseProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1)
)
h3cPseProfilesEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPseProfileIndex"),
)
if mibBuilder.loadTexts:
    h3cPseProfilesEntry.setStatus("current")


class _H3cPseProfileIndex_Type(Integer32):
    """Custom type h3cPseProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cPseProfileIndex_Type.__name__ = "Integer32"
_H3cPseProfileIndex_Object = MibTableColumn
h3cPseProfileIndex = _H3cPseProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 1),
    _H3cPseProfileIndex_Type()
)
h3cPseProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cPseProfileIndex.setStatus("current")


class _H3cPseProfileName_Type(DisplayString):
    """Custom type h3cPseProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_H3cPseProfileName_Type.__name__ = "DisplayString"
_H3cPseProfileName_Object = MibTableColumn
h3cPseProfileName = _H3cPseProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 2),
    _H3cPseProfileName_Type()
)
h3cPseProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfileName.setStatus("current")


class _H3cPseProfilePowerMode_Type(Integer32):
    """Custom type h3cPseProfilePowerMode based on Integer32"""
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


_H3cPseProfilePowerMode_Type.__name__ = "Integer32"
_H3cPseProfilePowerMode_Object = MibTableColumn
h3cPseProfilePowerMode = _H3cPseProfilePowerMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 3),
    _H3cPseProfilePowerMode_Type()
)
h3cPseProfilePowerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfilePowerMode.setStatus("current")


class _H3cPseProfilePowerLimit_Type(Integer32):
    """Custom type h3cPseProfilePowerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15400),
    )


_H3cPseProfilePowerLimit_Type.__name__ = "Integer32"
_H3cPseProfilePowerLimit_Object = MibTableColumn
h3cPseProfilePowerLimit = _H3cPseProfilePowerLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 4),
    _H3cPseProfilePowerLimit_Type()
)
h3cPseProfilePowerLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfilePowerLimit.setStatus("current")


class _H3cPseProfilePriority_Type(Integer32):
    """Custom type h3cPseProfilePriority based on Integer32"""
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


_H3cPseProfilePriority_Type.__name__ = "Integer32"
_H3cPseProfilePriority_Object = MibTableColumn
h3cPseProfilePriority = _H3cPseProfilePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 5),
    _H3cPseProfilePriority_Type()
)
h3cPseProfilePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfilePriority.setStatus("current")


class _H3cPseProfilePairs_Type(Integer32):
    """Custom type h3cPseProfilePairs based on Integer32"""
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


_H3cPseProfilePairs_Type.__name__ = "Integer32"
_H3cPseProfilePairs_Object = MibTableColumn
h3cPseProfilePairs = _H3cPseProfilePairs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 6),
    _H3cPseProfilePairs_Type()
)
h3cPseProfilePairs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfilePairs.setStatus("current")
_H3cPseProfileApplyNum_Type = Integer32
_H3cPseProfileApplyNum_Object = MibTableColumn
h3cPseProfileApplyNum = _H3cPseProfileApplyNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 7),
    _H3cPseProfileApplyNum_Type()
)
h3cPseProfileApplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPseProfileApplyNum.setStatus("current")
_H3cPseProfileRowStatus_Type = RowStatus
_H3cPseProfileRowStatus_Object = MibTableColumn
h3cPseProfileRowStatus = _H3cPseProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 7, 1, 8),
    _H3cPseProfileRowStatus_Type()
)
h3cPseProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cPseProfileRowStatus.setStatus("current")
_H3cPOEPowerObjects_ObjectIdentity = ObjectIdentity
h3cPOEPowerObjects = _H3cPOEPowerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8)
)
_H3cPOEThresholdLimitObjs_ObjectIdentity = ObjectIdentity
h3cPOEThresholdLimitObjs = _H3cPOEThresholdLimitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 1)
)


class _H3cPOEThresholdACMimimum_Type(OctetString):
    """Custom type h3cPOEThresholdACMimimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEThresholdACMimimum_Type.__name__ = "OctetString"
_H3cPOEThresholdACMimimum_Object = MibScalar
h3cPOEThresholdACMimimum = _H3cPOEThresholdACMimimum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 1, 1),
    _H3cPOEThresholdACMimimum_Type()
)
h3cPOEThresholdACMimimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPOEThresholdACMimimum.setStatus("current")


class _H3cPOEThresholdACMaximum_Type(OctetString):
    """Custom type h3cPOEThresholdACMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEThresholdACMaximum_Type.__name__ = "OctetString"
_H3cPOEThresholdACMaximum_Object = MibScalar
h3cPOEThresholdACMaximum = _H3cPOEThresholdACMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 1, 2),
    _H3cPOEThresholdACMaximum_Type()
)
h3cPOEThresholdACMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPOEThresholdACMaximum.setStatus("current")


class _H3cPOEThresholdDCMinimum_Type(OctetString):
    """Custom type h3cPOEThresholdDCMinimum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEThresholdDCMinimum_Type.__name__ = "OctetString"
_H3cPOEThresholdDCMinimum_Object = MibScalar
h3cPOEThresholdDCMinimum = _H3cPOEThresholdDCMinimum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 1, 3),
    _H3cPOEThresholdDCMinimum_Type()
)
h3cPOEThresholdDCMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPOEThresholdDCMinimum.setStatus("current")


class _H3cPOEThresholdDCMaximum_Type(OctetString):
    """Custom type h3cPOEThresholdDCMaximum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEThresholdDCMaximum_Type.__name__ = "OctetString"
_H3cPOEThresholdDCMaximum_Object = MibScalar
h3cPOEThresholdDCMaximum = _H3cPOEThresholdDCMaximum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 1, 4),
    _H3cPOEThresholdDCMaximum_Type()
)
h3cPOEThresholdDCMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPOEThresholdDCMaximum.setStatus("current")
_H3cPOESupModuleInfoObjs_ObjectIdentity = ObjectIdentity
h3cPOESupModuleInfoObjs = _H3cPOESupModuleInfoObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2)
)


class _H3cPOEPowerType_Type(OctetString):
    """Custom type h3cPOEPowerType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cPOEPowerType_Type.__name__ = "OctetString"
_H3cPOEPowerType_Object = MibScalar
h3cPOEPowerType = _H3cPOEPowerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 1),
    _H3cPOEPowerType_Type()
)
h3cPOEPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEPowerType.setStatus("current")
_H3cPOEPowerModuleNum_Type = Integer32
_H3cPOEPowerModuleNum_Object = MibScalar
h3cPOEPowerModuleNum = _H3cPOEPowerModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 2),
    _H3cPOEPowerModuleNum_Type()
)
h3cPOEPowerModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEPowerModuleNum.setStatus("current")


class _H3cPOESupervisionModuleName_Type(OctetString):
    """Custom type h3cPOESupervisionModuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cPOESupervisionModuleName_Type.__name__ = "OctetString"
_H3cPOESupervisionModuleName_Object = MibScalar
h3cPOESupervisionModuleName = _H3cPOESupervisionModuleName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 3),
    _H3cPOESupervisionModuleName_Type()
)
h3cPOESupervisionModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESupervisionModuleName.setStatus("current")
_H3cPOESMMajorVersion_Type = Integer32
_H3cPOESMMajorVersion_Object = MibScalar
h3cPOESMMajorVersion = _H3cPOESMMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 4),
    _H3cPOESMMajorVersion_Type()
)
h3cPOESMMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESMMajorVersion.setStatus("current")
_H3cPOESMMinorVersion_Type = Integer32
_H3cPOESMMinorVersion_Object = MibScalar
h3cPOESMMinorVersion = _H3cPOESMMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 5),
    _H3cPOESMMinorVersion_Type()
)
h3cPOESMMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESMMinorVersion.setStatus("current")


class _H3cPOESMFactorName_Type(OctetString):
    """Custom type h3cPOESMFactorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cPOESMFactorName_Type.__name__ = "OctetString"
_H3cPOESMFactorName_Object = MibScalar
h3cPOESMFactorName = _H3cPOESMFactorName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 6),
    _H3cPOESMFactorName_Type()
)
h3cPOESMFactorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESMFactorName.setStatus("current")
_H3cPOEModuleInfoTable_Object = MibTable
h3cPOEModuleInfoTable = _H3cPOEModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7)
)
if mibBuilder.loadTexts:
    h3cPOEModuleInfoTable.setStatus("current")
_H3cPOEModuleInfoEntry_Object = MibTableRow
h3cPOEModuleInfoEntry = _H3cPOEModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7, 1)
)
h3cPOEModuleInfoEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleIndex"),
)
if mibBuilder.loadTexts:
    h3cPOEModuleInfoEntry.setStatus("current")


class _H3cPOEModuleIndex_Type(Integer32):
    """Custom type h3cPOEModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOEModuleIndex_Type.__name__ = "Integer32"
_H3cPOEModuleIndex_Object = MibTableColumn
h3cPOEModuleIndex = _H3cPOEModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7, 1, 1),
    _H3cPOEModuleIndex_Type()
)
h3cPOEModuleIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOEModuleIndex.setStatus("current")
_H3cPOEModuleID_Type = Integer32
_H3cPOEModuleID_Object = MibTableColumn
h3cPOEModuleID = _H3cPOEModuleID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7, 1, 2),
    _H3cPOEModuleID_Type()
)
h3cPOEModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleID.setStatus("current")
_H3cPOEModuleInfoPower_Type = Integer32
_H3cPOEModuleInfoPower_Object = MibTableColumn
h3cPOEModuleInfoPower = _H3cPOEModuleInfoPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7, 1, 3),
    _H3cPOEModuleInfoPower_Type()
)
h3cPOEModuleInfoPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleInfoPower.setStatus("current")


class _H3cPOEModuleHardVerInfo_Type(OctetString):
    """Custom type h3cPOEModuleHardVerInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_H3cPOEModuleHardVerInfo_Type.__name__ = "OctetString"
_H3cPOEModuleHardVerInfo_Object = MibTableColumn
h3cPOEModuleHardVerInfo = _H3cPOEModuleHardVerInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 2, 7, 1, 4),
    _H3cPOEModuleHardVerInfo_Type()
)
h3cPOEModuleHardVerInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleHardVerInfo.setStatus("current")
_H3cPOEDCOutStateObjects_ObjectIdentity = ObjectIdentity
h3cPOEDCOutStateObjects = _H3cPOEDCOutStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3)
)
_H3cPOEDCOutStateModuleNum_Type = Integer32
_H3cPOEDCOutStateModuleNum_Object = MibScalar
h3cPOEDCOutStateModuleNum = _H3cPOEDCOutStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3, 1),
    _H3cPOEDCOutStateModuleNum_Type()
)
h3cPOEDCOutStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEDCOutStateModuleNum.setStatus("current")
_H3cPOEDCOutStateTable_Object = MibTable
h3cPOEDCOutStateTable = _H3cPOEDCOutStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3, 2)
)
if mibBuilder.loadTexts:
    h3cPOEDCOutStateTable.setStatus("current")
_H3cPOEDCOutStateEntry_Object = MibTableRow
h3cPOEDCOutStateEntry = _H3cPOEDCOutStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3, 2, 1)
)
h3cPOEDCOutStateEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutStateIndex"),
)
if mibBuilder.loadTexts:
    h3cPOEDCOutStateEntry.setStatus("current")


class _H3cPOEDCOutStateIndex_Type(Integer32):
    """Custom type h3cPOEDCOutStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOEDCOutStateIndex_Type.__name__ = "Integer32"
_H3cPOEDCOutStateIndex_Object = MibTableColumn
h3cPOEDCOutStateIndex = _H3cPOEDCOutStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3, 2, 1, 1),
    _H3cPOEDCOutStateIndex_Type()
)
h3cPOEDCOutStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOEDCOutStateIndex.setStatus("current")
_H3cPOEDCOutDCVolAlarm_Type = DCAlarmState
_H3cPOEDCOutDCVolAlarm_Object = MibTableColumn
h3cPOEDCOutDCVolAlarm = _H3cPOEDCOutDCVolAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 3, 2, 1, 2),
    _H3cPOEDCOutDCVolAlarm_Type()
)
h3cPOEDCOutDCVolAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEDCOutDCVolAlarm.setStatus("current")
_H3cPOEDCOutInfoObjects_ObjectIdentity = ObjectIdentity
h3cPOEDCOutInfoObjects = _H3cPOEDCOutInfoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4)
)
_H3cPOEDCOutCurNum_Type = Integer32
_H3cPOEDCOutCurNum_Object = MibScalar
h3cPOEDCOutCurNum = _H3cPOEDCOutCurNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 1),
    _H3cPOEDCOutCurNum_Type()
)
h3cPOEDCOutCurNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEDCOutCurNum.setStatus("current")
_H3cPOEDCOutInfoTable_Object = MibTable
h3cPOEDCOutInfoTable = _H3cPOEDCOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 2)
)
if mibBuilder.loadTexts:
    h3cPOEDCOutInfoTable.setStatus("current")
_H3cPOEDCOutInfoEntry_Object = MibTableRow
h3cPOEDCOutInfoEntry = _H3cPOEDCOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 2, 1)
)
h3cPOEDCOutInfoEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutInfoIndex"),
)
if mibBuilder.loadTexts:
    h3cPOEDCOutInfoEntry.setStatus("current")


class _H3cPOEDCOutInfoIndex_Type(Integer32):
    """Custom type h3cPOEDCOutInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOEDCOutInfoIndex_Type.__name__ = "Integer32"
_H3cPOEDCOutInfoIndex_Object = MibTableColumn
h3cPOEDCOutInfoIndex = _H3cPOEDCOutInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 2, 1, 1),
    _H3cPOEDCOutInfoIndex_Type()
)
h3cPOEDCOutInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOEDCOutInfoIndex.setStatus("current")


class _H3cPOEDCOutVol_Type(OctetString):
    """Custom type h3cPOEDCOutVol based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEDCOutVol_Type.__name__ = "OctetString"
_H3cPOEDCOutVol_Object = MibTableColumn
h3cPOEDCOutVol = _H3cPOEDCOutVol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 2, 1, 2),
    _H3cPOEDCOutVol_Type()
)
h3cPOEDCOutVol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEDCOutVol.setStatus("current")


class _H3cPOEDCOutInfoLoadCur_Type(OctetString):
    """Custom type h3cPOEDCOutInfoLoadCur based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_H3cPOEDCOutInfoLoadCur_Type.__name__ = "OctetString"
_H3cPOEDCOutInfoLoadCur_Object = MibTableColumn
h3cPOEDCOutInfoLoadCur = _H3cPOEDCOutInfoLoadCur_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 4, 2, 1, 3),
    _H3cPOEDCOutInfoLoadCur_Type()
)
h3cPOEDCOutInfoLoadCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEDCOutInfoLoadCur.setStatus("current")
_H3cPOEACSwitchStateModuleObjs_ObjectIdentity = ObjectIdentity
h3cPOEACSwitchStateModuleObjs = _H3cPOEACSwitchStateModuleObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5)
)
_H3cPOEACSwitchStateModuleNum_Type = Integer32
_H3cPOEACSwitchStateModuleNum_Object = MibScalar
h3cPOEACSwitchStateModuleNum = _H3cPOEACSwitchStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5, 1),
    _H3cPOEACSwitchStateModuleNum_Type()
)
h3cPOEACSwitchStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEACSwitchStateModuleNum.setStatus("current")
_H3cPOEACSwitchStateTable_Object = MibTable
h3cPOEACSwitchStateTable = _H3cPOEACSwitchStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5, 2)
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchStateTable.setStatus("current")
_H3cPOEACSwitchStateEntry_Object = MibTableRow
h3cPOEACSwitchStateEntry = _H3cPOEACSwitchStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5, 2, 1)
)
h3cPOEACSwitchStateEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOEACSwitchStateIndex"),
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchStateEntry.setStatus("current")


class _H3cPOEACSwitchStateIndex_Type(Integer32):
    """Custom type h3cPOEACSwitchStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOEACSwitchStateIndex_Type.__name__ = "Integer32"
_H3cPOEACSwitchStateIndex_Object = MibTableColumn
h3cPOEACSwitchStateIndex = _H3cPOEACSwitchStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5, 2, 1, 1),
    _H3cPOEACSwitchStateIndex_Type()
)
h3cPOEACSwitchStateIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOEACSwitchStateIndex.setStatus("current")
_H3cPOEACSwitchState_Type = SwitchState
_H3cPOEACSwitchState_Object = MibTableColumn
h3cPOEACSwitchState = _H3cPOEACSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 5, 2, 1, 2),
    _H3cPOEACSwitchState_Type()
)
h3cPOEACSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEACSwitchState.setStatus("current")
_H3cPOEInCurStateObjects_ObjectIdentity = ObjectIdentity
h3cPOEInCurStateObjects = _H3cPOEInCurStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6)
)
_H3cPOEInCurStateModuleNum_Type = Integer32
_H3cPOEInCurStateModuleNum_Object = MibScalar
h3cPOEInCurStateModuleNum = _H3cPOEInCurStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 1),
    _H3cPOEInCurStateModuleNum_Type()
)
h3cPOEInCurStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEInCurStateModuleNum.setStatus("current")
_H3cPOEInCurAState_Type = ACAlarmState
_H3cPOEInCurAState_Object = MibScalar
h3cPOEInCurAState = _H3cPOEInCurAState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 2),
    _H3cPOEInCurAState_Type()
)
h3cPOEInCurAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEInCurAState.setStatus("current")
_H3cPOEInCurBState_Type = ACAlarmState
_H3cPOEInCurBState_Object = MibScalar
h3cPOEInCurBState = _H3cPOEInCurBState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 3),
    _H3cPOEInCurBState_Type()
)
h3cPOEInCurBState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEInCurBState.setStatus("current")
_H3cPOEInCurCState_Type = ACAlarmState
_H3cPOEInCurCState_Object = MibScalar
h3cPOEInCurCState = _H3cPOEInCurCState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 4),
    _H3cPOEInCurCState_Type()
)
h3cPOEInCurCState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEInCurCState.setStatus("current")
_H3cPOESwitchStateVolExTable_Object = MibTable
h3cPOESwitchStateVolExTable = _H3cPOESwitchStateVolExTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5)
)
if mibBuilder.loadTexts:
    h3cPOESwitchStateVolExTable.setStatus("current")
_H3cPOESwitchStateVolExEntry_Object = MibTableRow
h3cPOESwitchStateVolExEntry = _H3cPOESwitchStateVolExEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5, 1)
)
h3cPOESwitchStateVolExEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateVolExIndex"),
)
if mibBuilder.loadTexts:
    h3cPOESwitchStateVolExEntry.setStatus("current")


class _H3cPOESwitchStateVolExIndex_Type(Integer32):
    """Custom type h3cPOESwitchStateVolExIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOESwitchStateVolExIndex_Type.__name__ = "Integer32"
_H3cPOESwitchStateVolExIndex_Object = MibTableColumn
h3cPOESwitchStateVolExIndex = _H3cPOESwitchStateVolExIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5, 1, 1),
    _H3cPOESwitchStateVolExIndex_Type()
)
h3cPOESwitchStateVolExIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOESwitchStateVolExIndex.setStatus("current")
_H3cPOESwitchStateInVolAB_Type = ACAlarmState
_H3cPOESwitchStateInVolAB_Object = MibTableColumn
h3cPOESwitchStateInVolAB = _H3cPOESwitchStateInVolAB_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5, 1, 2),
    _H3cPOESwitchStateInVolAB_Type()
)
h3cPOESwitchStateInVolAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESwitchStateInVolAB.setStatus("current")
_H3cPOESwitchStateInVolBC_Type = ACAlarmState
_H3cPOESwitchStateInVolBC_Object = MibTableColumn
h3cPOESwitchStateInVolBC = _H3cPOESwitchStateInVolBC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5, 1, 3),
    _H3cPOESwitchStateInVolBC_Type()
)
h3cPOESwitchStateInVolBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESwitchStateInVolBC.setStatus("current")
_H3cPOESwitchStateInVolCA_Type = ACAlarmState
_H3cPOESwitchStateInVolCA_Object = MibTableColumn
h3cPOESwitchStateInVolCA = _H3cPOESwitchStateInVolCA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 6, 5, 1, 4),
    _H3cPOESwitchStateInVolCA_Type()
)
h3cPOESwitchStateInVolCA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOESwitchStateInVolCA.setStatus("current")
_H3cPOEAlarmStateObjects_ObjectIdentity = ObjectIdentity
h3cPOEAlarmStateObjects = _H3cPOEAlarmStateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7)
)
_H3cPOEAlarmStateModuleNum_Type = Integer32
_H3cPOEAlarmStateModuleNum_Object = MibScalar
h3cPOEAlarmStateModuleNum = _H3cPOEAlarmStateModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 1),
    _H3cPOEAlarmStateModuleNum_Type()
)
h3cPOEAlarmStateModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEAlarmStateModuleNum.setStatus("current")
_H3cPOEAlarmStateInfoTable_Object = MibTable
h3cPOEAlarmStateInfoTable = _H3cPOEAlarmStateInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2)
)
if mibBuilder.loadTexts:
    h3cPOEAlarmStateInfoTable.setStatus("current")
_H3cPOEAlarmStateInfoEntry_Object = MibTableRow
h3cPOEAlarmStateInfoEntry = _H3cPOEAlarmStateInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1)
)
h3cPOEAlarmStateInfoEntry.setIndexNames(
    (0, "H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
)
if mibBuilder.loadTexts:
    h3cPOEAlarmStateInfoEntry.setStatus("current")


class _H3cPOEAlarmModuleInfoIndex_Type(Integer32):
    """Custom type h3cPOEAlarmModuleInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cPOEAlarmModuleInfoIndex_Type.__name__ = "Integer32"
_H3cPOEAlarmModuleInfoIndex_Object = MibTableColumn
h3cPOEAlarmModuleInfoIndex = _H3cPOEAlarmModuleInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 1),
    _H3cPOEAlarmModuleInfoIndex_Type()
)
h3cPOEAlarmModuleInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cPOEAlarmModuleInfoIndex.setStatus("current")
_H3cPOEModuleDisconnect_Type = ModuleAlarmState
_H3cPOEModuleDisconnect_Object = MibTableColumn
h3cPOEModuleDisconnect = _H3cPOEModuleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 2),
    _H3cPOEModuleDisconnect_Type()
)
h3cPOEModuleDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleDisconnect.setStatus("current")
_H3cPOEModuleInputError_Type = ModuleAlarmState
_H3cPOEModuleInputError_Object = MibTableColumn
h3cPOEModuleInputError = _H3cPOEModuleInputError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 3),
    _H3cPOEModuleInputError_Type()
)
h3cPOEModuleInputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleInputError.setStatus("current")
_H3cPOEModuleOutputError_Type = ModuleAlarmState
_H3cPOEModuleOutputError_Object = MibTableColumn
h3cPOEModuleOutputError = _H3cPOEModuleOutputError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 4),
    _H3cPOEModuleOutputError_Type()
)
h3cPOEModuleOutputError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleOutputError.setStatus("current")
_H3cPOEModuleOverVoltage_Type = ModuleAlarmState
_H3cPOEModuleOverVoltage_Object = MibTableColumn
h3cPOEModuleOverVoltage = _H3cPOEModuleOverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 5),
    _H3cPOEModuleOverVoltage_Type()
)
h3cPOEModuleOverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleOverVoltage.setStatus("current")
_H3cPOEModuleOverTemp_Type = ModuleAlarmState
_H3cPOEModuleOverTemp_Object = MibTableColumn
h3cPOEModuleOverTemp = _H3cPOEModuleOverTemp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 6),
    _H3cPOEModuleOverTemp_Type()
)
h3cPOEModuleOverTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleOverTemp.setStatus("current")
_H3cPOEModuleFanError_Type = ModuleAlarmState
_H3cPOEModuleFanError_Object = MibTableColumn
h3cPOEModuleFanError = _H3cPOEModuleFanError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 7),
    _H3cPOEModuleFanError_Type()
)
h3cPOEModuleFanError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleFanError.setStatus("current")
_H3cPOEModuleShutdown_Type = ModuleAlarmState
_H3cPOEModuleShutdown_Object = MibTableColumn
h3cPOEModuleShutdown = _H3cPOEModuleShutdown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 8),
    _H3cPOEModuleShutdown_Type()
)
h3cPOEModuleShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleShutdown.setStatus("current")
_H3cPOEModuleCurRestricted_Type = ModuleAlarmState
_H3cPOEModuleCurRestricted_Object = MibTableColumn
h3cPOEModuleCurRestricted = _H3cPOEModuleCurRestricted_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 8, 7, 2, 1, 9),
    _H3cPOEModuleCurRestricted_Type()
)
h3cPOEModuleCurRestricted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cPOEModuleCurRestricted.setStatus("current")


class _H3cPsePolicyMode_Type(Integer32):
    """Custom type h3cPsePolicyMode based on Integer32"""
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


_H3cPsePolicyMode_Type.__name__ = "Integer32"
_H3cPsePolicyMode_Object = MibScalar
h3cPsePolicyMode = _H3cPsePolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 9),
    _H3cPsePolicyMode_Type()
)
h3cPsePolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPsePolicyMode.setStatus("current")


class _H3cPDPolicyMode_Type(Integer32):
    """Custom type h3cPDPolicyMode based on Integer32"""
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


_H3cPDPolicyMode_Type.__name__ = "Integer32"
_H3cPDPolicyMode_Object = MibScalar
h3cPDPolicyMode = _H3cPDPolicyMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 10),
    _H3cPDPolicyMode_Type()
)
h3cPDPolicyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cPDPolicyMode.setStatus("current")

# Managed Objects groups

h3cPsePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 1)
)
h3cPsePortGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPsePortProfileIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePortPowerLimit"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePortCurrentPower"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePortAveragePower"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePortPeakPower"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePortFaultDescription"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cMainPsePriorityMode"))
)
if mibBuilder.loadTexts:
    h3cPsePortGroup.setStatus("current")

h3cMainPseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 2)
)
h3cMainPseGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cMainPsePowerLimit"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cMainPseAveragePower"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cMainPsePeakPower"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cMainGuaranteedPowerRemaining"))
)
if mibBuilder.loadTexts:
    h3cMainPseGroup.setStatus("current")

h3cPseScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 3)
)
h3cPseScalarGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPseAutoDetectActive"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePowerMaxValue"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPsePolicyMode"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPDPolicyMode"))
)
if mibBuilder.loadTexts:
    h3cPseScalarGroup.setStatus("current")

h3cPsePDNotificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 4)
)
h3cPsePDNotificationGroup.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cpsePDChangeNotification")
)
if mibBuilder.loadTexts:
    h3cPsePDNotificationGroup.setStatus("current")

h3cPseProfilesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 5)
)
h3cPseProfilesGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPseProfileName"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfilePowerMode"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfilePowerLimit"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfilePriority"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfilePairs"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfileApplyNum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPseProfileRowStatus"))
)
if mibBuilder.loadTexts:
    h3cPseProfilesGroup.setStatus("current")

h3cPOEPowerThresholdLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 6)
)
h3cPOEPowerThresholdLimitGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEThresholdACMimimum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEThresholdACMaximum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEThresholdDCMinimum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEThresholdDCMaximum"))
)
if mibBuilder.loadTexts:
    h3cPOEPowerThresholdLimitGroup.setStatus("current")

h3cPOEPowerSupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 7)
)
h3cPOEPowerSupInfoGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEPowerType"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEPowerModuleNum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESupervisionModuleName"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESMMajorVersion"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESMMinorVersion"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESMFactorName"))
)
if mibBuilder.loadTexts:
    h3cPOEPowerSupInfoGroup.setStatus("current")

h3cPOEPowerDCOutStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 8)
)
h3cPOEPowerDCOutStateGroup.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutStateModuleNum")
)
if mibBuilder.loadTexts:
    h3cPOEPowerDCOutStateGroup.setStatus("current")

h3cPOEPowerDCOutInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 9)
)
h3cPOEPowerDCOutInfoGroup.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutCurNum")
)
if mibBuilder.loadTexts:
    h3cPOEPowerDCOutInfoGroup.setStatus("current")

h3cPOEPowerACSwitchStateModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 10)
)
h3cPOEPowerACSwitchStateModuleGroup.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEACSwitchStateModuleNum")
)
if mibBuilder.loadTexts:
    h3cPOEPowerACSwitchStateModuleGroup.setStatus("current")

h3cPOEPowerInCurStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 11)
)
h3cPOEPowerInCurStateGroup.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurStateModuleNum"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurAState"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurBState"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurCState"))
)
if mibBuilder.loadTexts:
    h3cPOEPowerInCurStateGroup.setStatus("current")

h3cPOEPowerAlarmStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 2, 12)
)
h3cPOEPowerAlarmStateGroup.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmStateModuleNum")
)
if mibBuilder.loadTexts:
    h3cPOEPowerAlarmStateGroup.setStatus("current")


# Notification objects

h3cpsePDChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 1)
)
h3cpsePDChangeNotification.setObjects(
    ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus")
)
if mibBuilder.loadTexts:
    h3cpsePDChangeNotification.setStatus(
        "current"
    )

h3cPOEDisconnectNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 2)
)
h3cPOEDisconnectNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleDisconnect"))
)
if mibBuilder.loadTexts:
    h3cPOEDisconnectNotification.setStatus(
        "current"
    )

h3cPOEInputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 3)
)
h3cPOEInputErrorNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleInputError"))
)
if mibBuilder.loadTexts:
    h3cPOEInputErrorNotification.setStatus(
        "current"
    )

h3cPOEOutputErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 4)
)
h3cPOEOutputErrorNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleOutputError"))
)
if mibBuilder.loadTexts:
    h3cPOEOutputErrorNotification.setStatus(
        "current"
    )

h3cPOEOverVoltageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 5)
)
h3cPOEOverVoltageNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleOverVoltage"))
)
if mibBuilder.loadTexts:
    h3cPOEOverVoltageNotification.setStatus(
        "current"
    )

h3cPOEOverTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 6)
)
h3cPOEOverTempNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleOverTemp"))
)
if mibBuilder.loadTexts:
    h3cPOEOverTempNotification.setStatus(
        "current"
    )

h3cPOEFanErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 7)
)
h3cPOEFanErrorNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleFanError"))
)
if mibBuilder.loadTexts:
    h3cPOEFanErrorNotification.setStatus(
        "current"
    )

h3cPOEModuleShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 8)
)
h3cPOEModuleShutdownNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleShutdown"))
)
if mibBuilder.loadTexts:
    h3cPOEModuleShutdownNotification.setStatus(
        "current"
    )

h3cPOECurRestrictedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 9)
)
h3cPOECurRestrictedNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEAlarmModuleInfoIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEModuleCurRestricted"))
)
if mibBuilder.loadTexts:
    h3cPOECurRestrictedNotification.setStatus(
        "current"
    )

h3cPOEACSwitchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 10)
)
h3cPOEACSwitchNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEACSwitchStateIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEACSwitchState"))
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchNotification.setStatus(
        "current"
    )

h3cPOEACInCurANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 11)
)
h3cPOEACInCurANotification.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurAState")
)
if mibBuilder.loadTexts:
    h3cPOEACInCurANotification.setStatus(
        "current"
    )

h3cPOEACInCurBNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 12)
)
h3cPOEACInCurBNotification.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurBState")
)
if mibBuilder.loadTexts:
    h3cPOEACInCurBNotification.setStatus(
        "current"
    )

h3cPOEACInCurCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 13)
)
h3cPOEACInCurCNotification.setObjects(
    ("H3C-POWER-ETH-EXT-MIB", "h3cPOEInCurCState")
)
if mibBuilder.loadTexts:
    h3cPOEACInCurCNotification.setStatus(
        "current"
    )

h3cPOEACSwitchVolABNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 14)
)
h3cPOEACSwitchVolABNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateVolExIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateInVolAB"))
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchVolABNotification.setStatus(
        "current"
    )

h3cPOEACSwitchVolBCNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 15)
)
h3cPOEACSwitchVolBCNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateVolExIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateInVolBC"))
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchVolBCNotification.setStatus(
        "current"
    )

h3cPOEACSwitchVolCANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 16)
)
h3cPOEACSwitchVolCANotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateVolExIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOESwitchStateInVolCA"))
)
if mibBuilder.loadTexts:
    h3cPOEACSwitchVolCANotification.setStatus(
        "current"
    )

h3cPOEDCOutVolNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 17)
)
h3cPOEDCOutVolNotification.setObjects(
      *(("H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutStateIndex"),
        ("H3C-POWER-ETH-EXT-MIB", "h3cPOEDCOutDCVolAlarm"))
)
if mibBuilder.loadTexts:
    h3cPOEDCOutVolNotification.setStatus(
        "current"
    )

h3cPOEShutdownNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 6, 18)
)
if mibBuilder.loadTexts:
    h3cPOEShutdownNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

h3cPseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    h3cPseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-POWER-ETH-EXT-MIB",
    **{"ACAlarmState": ACAlarmState,
       "DCAlarmState": DCAlarmState,
       "SwitchState": SwitchState,
       "ModuleAlarmState": ModuleAlarmState,
       "h3cPowerEthernetExt": h3cPowerEthernetExt,
       "h3cPsePortTable": h3cPsePortTable,
       "h3cPsePortEntry": h3cPsePortEntry,
       "h3cPsePortFaultDescription": h3cPsePortFaultDescription,
       "h3cPsePortPeakPower": h3cPsePortPeakPower,
       "h3cPsePortAveragePower": h3cPsePortAveragePower,
       "h3cPsePortCurrentPower": h3cPsePortCurrentPower,
       "h3cPsePortPowerLimit": h3cPsePortPowerLimit,
       "h3cPsePortProfileIndex": h3cPsePortProfileIndex,
       "h3cMainPseTable": h3cMainPseTable,
       "h3cMainPseEntry": h3cMainPseEntry,
       "h3cMainPsePowerLimit": h3cMainPsePowerLimit,
       "h3cMainPseAveragePower": h3cMainPseAveragePower,
       "h3cMainPsePeakPower": h3cMainPsePeakPower,
       "h3cMainGuaranteedPowerRemaining": h3cMainGuaranteedPowerRemaining,
       "h3cMainPsePriorityMode": h3cMainPsePriorityMode,
       "h3cMainPseLegacy": h3cMainPseLegacy,
       "h3cMainPsePowerPriority": h3cMainPsePowerPriority,
       "h3cPseAutoDetectActive": h3cPseAutoDetectActive,
       "h3cPseComformance": h3cPseComformance,
       "h3cPseCompliances": h3cPseCompliances,
       "h3cPseCompliance": h3cPseCompliance,
       "h3cPseGroup": h3cPseGroup,
       "h3cPsePortGroup": h3cPsePortGroup,
       "h3cMainPseGroup": h3cMainPseGroup,
       "h3cPseScalarGroup": h3cPseScalarGroup,
       "h3cPsePDNotificationGroup": h3cPsePDNotificationGroup,
       "h3cPseProfilesGroup": h3cPseProfilesGroup,
       "h3cPOEPowerThresholdLimitGroup": h3cPOEPowerThresholdLimitGroup,
       "h3cPOEPowerSupInfoGroup": h3cPOEPowerSupInfoGroup,
       "h3cPOEPowerDCOutStateGroup": h3cPOEPowerDCOutStateGroup,
       "h3cPOEPowerDCOutInfoGroup": h3cPOEPowerDCOutInfoGroup,
       "h3cPOEPowerACSwitchStateModuleGroup": h3cPOEPowerACSwitchStateModuleGroup,
       "h3cPOEPowerInCurStateGroup": h3cPOEPowerInCurStateGroup,
       "h3cPOEPowerAlarmStateGroup": h3cPOEPowerAlarmStateGroup,
       "h3cPsePowerMaxValue": h3cPsePowerMaxValue,
       "h3cpseportNotification": h3cpseportNotification,
       "h3cpsePDChangeNotification": h3cpsePDChangeNotification,
       "h3cPOEDisconnectNotification": h3cPOEDisconnectNotification,
       "h3cPOEInputErrorNotification": h3cPOEInputErrorNotification,
       "h3cPOEOutputErrorNotification": h3cPOEOutputErrorNotification,
       "h3cPOEOverVoltageNotification": h3cPOEOverVoltageNotification,
       "h3cPOEOverTempNotification": h3cPOEOverTempNotification,
       "h3cPOEFanErrorNotification": h3cPOEFanErrorNotification,
       "h3cPOEModuleShutdownNotification": h3cPOEModuleShutdownNotification,
       "h3cPOECurRestrictedNotification": h3cPOECurRestrictedNotification,
       "h3cPOEACSwitchNotification": h3cPOEACSwitchNotification,
       "h3cPOEACInCurANotification": h3cPOEACInCurANotification,
       "h3cPOEACInCurBNotification": h3cPOEACInCurBNotification,
       "h3cPOEACInCurCNotification": h3cPOEACInCurCNotification,
       "h3cPOEACSwitchVolABNotification": h3cPOEACSwitchVolABNotification,
       "h3cPOEACSwitchVolBCNotification": h3cPOEACSwitchVolBCNotification,
       "h3cPOEACSwitchVolCANotification": h3cPOEACSwitchVolCANotification,
       "h3cPOEDCOutVolNotification": h3cPOEDCOutVolNotification,
       "h3cPOEShutdownNotification": h3cPOEShutdownNotification,
       "h3cPseProfilesTable": h3cPseProfilesTable,
       "h3cPseProfilesEntry": h3cPseProfilesEntry,
       "h3cPseProfileIndex": h3cPseProfileIndex,
       "h3cPseProfileName": h3cPseProfileName,
       "h3cPseProfilePowerMode": h3cPseProfilePowerMode,
       "h3cPseProfilePowerLimit": h3cPseProfilePowerLimit,
       "h3cPseProfilePriority": h3cPseProfilePriority,
       "h3cPseProfilePairs": h3cPseProfilePairs,
       "h3cPseProfileApplyNum": h3cPseProfileApplyNum,
       "h3cPseProfileRowStatus": h3cPseProfileRowStatus,
       "h3cPOEPowerObjects": h3cPOEPowerObjects,
       "h3cPOEThresholdLimitObjs": h3cPOEThresholdLimitObjs,
       "h3cPOEThresholdACMimimum": h3cPOEThresholdACMimimum,
       "h3cPOEThresholdACMaximum": h3cPOEThresholdACMaximum,
       "h3cPOEThresholdDCMinimum": h3cPOEThresholdDCMinimum,
       "h3cPOEThresholdDCMaximum": h3cPOEThresholdDCMaximum,
       "h3cPOESupModuleInfoObjs": h3cPOESupModuleInfoObjs,
       "h3cPOEPowerType": h3cPOEPowerType,
       "h3cPOEPowerModuleNum": h3cPOEPowerModuleNum,
       "h3cPOESupervisionModuleName": h3cPOESupervisionModuleName,
       "h3cPOESMMajorVersion": h3cPOESMMajorVersion,
       "h3cPOESMMinorVersion": h3cPOESMMinorVersion,
       "h3cPOESMFactorName": h3cPOESMFactorName,
       "h3cPOEModuleInfoTable": h3cPOEModuleInfoTable,
       "h3cPOEModuleInfoEntry": h3cPOEModuleInfoEntry,
       "h3cPOEModuleIndex": h3cPOEModuleIndex,
       "h3cPOEModuleID": h3cPOEModuleID,
       "h3cPOEModuleInfoPower": h3cPOEModuleInfoPower,
       "h3cPOEModuleHardVerInfo": h3cPOEModuleHardVerInfo,
       "h3cPOEDCOutStateObjects": h3cPOEDCOutStateObjects,
       "h3cPOEDCOutStateModuleNum": h3cPOEDCOutStateModuleNum,
       "h3cPOEDCOutStateTable": h3cPOEDCOutStateTable,
       "h3cPOEDCOutStateEntry": h3cPOEDCOutStateEntry,
       "h3cPOEDCOutStateIndex": h3cPOEDCOutStateIndex,
       "h3cPOEDCOutDCVolAlarm": h3cPOEDCOutDCVolAlarm,
       "h3cPOEDCOutInfoObjects": h3cPOEDCOutInfoObjects,
       "h3cPOEDCOutCurNum": h3cPOEDCOutCurNum,
       "h3cPOEDCOutInfoTable": h3cPOEDCOutInfoTable,
       "h3cPOEDCOutInfoEntry": h3cPOEDCOutInfoEntry,
       "h3cPOEDCOutInfoIndex": h3cPOEDCOutInfoIndex,
       "h3cPOEDCOutVol": h3cPOEDCOutVol,
       "h3cPOEDCOutInfoLoadCur": h3cPOEDCOutInfoLoadCur,
       "h3cPOEACSwitchStateModuleObjs": h3cPOEACSwitchStateModuleObjs,
       "h3cPOEACSwitchStateModuleNum": h3cPOEACSwitchStateModuleNum,
       "h3cPOEACSwitchStateTable": h3cPOEACSwitchStateTable,
       "h3cPOEACSwitchStateEntry": h3cPOEACSwitchStateEntry,
       "h3cPOEACSwitchStateIndex": h3cPOEACSwitchStateIndex,
       "h3cPOEACSwitchState": h3cPOEACSwitchState,
       "h3cPOEInCurStateObjects": h3cPOEInCurStateObjects,
       "h3cPOEInCurStateModuleNum": h3cPOEInCurStateModuleNum,
       "h3cPOEInCurAState": h3cPOEInCurAState,
       "h3cPOEInCurBState": h3cPOEInCurBState,
       "h3cPOEInCurCState": h3cPOEInCurCState,
       "h3cPOESwitchStateVolExTable": h3cPOESwitchStateVolExTable,
       "h3cPOESwitchStateVolExEntry": h3cPOESwitchStateVolExEntry,
       "h3cPOESwitchStateVolExIndex": h3cPOESwitchStateVolExIndex,
       "h3cPOESwitchStateInVolAB": h3cPOESwitchStateInVolAB,
       "h3cPOESwitchStateInVolBC": h3cPOESwitchStateInVolBC,
       "h3cPOESwitchStateInVolCA": h3cPOESwitchStateInVolCA,
       "h3cPOEAlarmStateObjects": h3cPOEAlarmStateObjects,
       "h3cPOEAlarmStateModuleNum": h3cPOEAlarmStateModuleNum,
       "h3cPOEAlarmStateInfoTable": h3cPOEAlarmStateInfoTable,
       "h3cPOEAlarmStateInfoEntry": h3cPOEAlarmStateInfoEntry,
       "h3cPOEAlarmModuleInfoIndex": h3cPOEAlarmModuleInfoIndex,
       "h3cPOEModuleDisconnect": h3cPOEModuleDisconnect,
       "h3cPOEModuleInputError": h3cPOEModuleInputError,
       "h3cPOEModuleOutputError": h3cPOEModuleOutputError,
       "h3cPOEModuleOverVoltage": h3cPOEModuleOverVoltage,
       "h3cPOEModuleOverTemp": h3cPOEModuleOverTemp,
       "h3cPOEModuleFanError": h3cPOEModuleFanError,
       "h3cPOEModuleShutdown": h3cPOEModuleShutdown,
       "h3cPOEModuleCurRestricted": h3cPOEModuleCurRestricted,
       "h3cPsePolicyMode": h3cPsePolicyMode,
       "h3cPDPolicyMode": h3cPDPolicyMode}
)
