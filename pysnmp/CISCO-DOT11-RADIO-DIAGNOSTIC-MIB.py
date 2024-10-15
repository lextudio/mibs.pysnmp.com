# SNMP MIB module (CISCO-DOT11-RADIO-DIAGNOSTIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-RADIO-DIAGNOSTIC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:57 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11RadioDiagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105)
)
ciscoDot11RadioDiagMIB.setRevisions(
        ("2003-12-23 00:00",
         "2003-05-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CDot11RadioDiagMIBNotifs_ObjectIdentity = ObjectIdentity
cDot11RadioDiagMIBNotifs = _CDot11RadioDiagMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 0)
)
_CDot11RadioDiagMIBObjects_ObjectIdentity = ObjectIdentity
cDot11RadioDiagMIBObjects = _CDot11RadioDiagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1)
)
_CDot11RadioDiagConfigGlobal_ObjectIdentity = ObjectIdentity
cDot11RadioDiagConfigGlobal = _CDot11RadioDiagConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1)
)
_CDot11RadioDiagTable_Object = MibTable
cDot11RadioDiagTable = _CDot11RadioDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11RadioDiagTable.setStatus("current")
_CDot11RadioDiagEntry_Object = MibTableRow
cDot11RadioDiagEntry = _CDot11RadioDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1)
)
cDot11RadioDiagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cDot11RadioDiagEntry.setStatus("current")


class _CDot11RadioDiagTempChannel_Type(Unsigned32):
    """Custom type cDot11RadioDiagTempChannel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
        ValueRangeConstraint(34, 34),
        ValueRangeConstraint(36, 36),
        ValueRangeConstraint(38, 38),
        ValueRangeConstraint(40, 40),
        ValueRangeConstraint(42, 42),
        ValueRangeConstraint(44, 44),
        ValueRangeConstraint(46, 46),
        ValueRangeConstraint(48, 48),
        ValueRangeConstraint(52, 52),
        ValueRangeConstraint(56, 56),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(64, 64),
        ValueRangeConstraint(100, 100),
        ValueRangeConstraint(104, 104),
        ValueRangeConstraint(108, 108),
        ValueRangeConstraint(112, 112),
        ValueRangeConstraint(116, 116),
        ValueRangeConstraint(120, 120),
        ValueRangeConstraint(124, 124),
        ValueRangeConstraint(128, 128),
        ValueRangeConstraint(132, 132),
        ValueRangeConstraint(136, 136),
        ValueRangeConstraint(140, 140),
        ValueRangeConstraint(149, 149),
        ValueRangeConstraint(153, 153),
        ValueRangeConstraint(157, 157),
        ValueRangeConstraint(161, 161),
    )


_CDot11RadioDiagTempChannel_Type.__name__ = "Unsigned32"
_CDot11RadioDiagTempChannel_Object = MibTableColumn
cDot11RadioDiagTempChannel = _CDot11RadioDiagTempChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 1),
    _CDot11RadioDiagTempChannel_Type()
)
cDot11RadioDiagTempChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagTempChannel.setStatus("current")


class _CDot11RadioDiagTempTxPowerLevel_Type(Unsigned32):
    """Custom type cDot11RadioDiagTempTxPowerLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CDot11RadioDiagTempTxPowerLevel_Type.__name__ = "Unsigned32"
_CDot11RadioDiagTempTxPowerLevel_Object = MibTableColumn
cDot11RadioDiagTempTxPowerLevel = _CDot11RadioDiagTempTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 2),
    _CDot11RadioDiagTempTxPowerLevel_Type()
)
cDot11RadioDiagTempTxPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagTempTxPowerLevel.setStatus("current")


class _CDot11RadioDiagMode_Type(Integer32):
    """Custom type cDot11RadioDiagMode based on Integer32"""
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
        *(("apRadioDiscovery", 2),
          ("normal", 1),
          ("siteSurveyNonTempSettings", 4),
          ("siteSurveyTempSettings", 3))
    )


_CDot11RadioDiagMode_Type.__name__ = "Integer32"
_CDot11RadioDiagMode_Object = MibTableColumn
cDot11RadioDiagMode = _CDot11RadioDiagMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 3),
    _CDot11RadioDiagMode_Type()
)
cDot11RadioDiagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagMode.setStatus("current")


class _CDot11RadioDiagSettingsEnabled_Type(TruthValue):
    """Custom type cDot11RadioDiagSettingsEnabled based on TruthValue"""


_CDot11RadioDiagSettingsEnabled_Object = MibTableColumn
cDot11RadioDiagSettingsEnabled = _CDot11RadioDiagSettingsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 4),
    _CDot11RadioDiagSettingsEnabled_Type()
)
cDot11RadioDiagSettingsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagSettingsEnabled.setStatus("current")


class _CDot11RadioDiagTempClientTxPower_Type(Unsigned32):
    """Custom type cDot11RadioDiagTempClientTxPower based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_CDot11RadioDiagTempClientTxPower_Type.__name__ = "Unsigned32"
_CDot11RadioDiagTempClientTxPower_Object = MibTableColumn
cDot11RadioDiagTempClientTxPower = _CDot11RadioDiagTempClientTxPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 5),
    _CDot11RadioDiagTempClientTxPower_Type()
)
cDot11RadioDiagTempClientTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagTempClientTxPower.setStatus("current")


class _CDot11RadioDiagTempDataRateSet_Type(OctetString):
    """Custom type cDot11RadioDiagTempDataRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_CDot11RadioDiagTempDataRateSet_Type.__name__ = "OctetString"
_CDot11RadioDiagTempDataRateSet_Object = MibTableColumn
cDot11RadioDiagTempDataRateSet = _CDot11RadioDiagTempDataRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 1, 1, 1, 1, 6),
    _CDot11RadioDiagTempDataRateSet_Type()
)
cDot11RadioDiagTempDataRateSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cDot11RadioDiagTempDataRateSet.setStatus("current")
_CDot11RadioDiagMIBConform_ObjectIdentity = ObjectIdentity
cDot11RadioDiagMIBConform = _CDot11RadioDiagMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2)
)
_CDot11RadioDiagMIBCompliances_ObjectIdentity = ObjectIdentity
cDot11RadioDiagMIBCompliances = _CDot11RadioDiagMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1)
)
_CDot11RadioDiagMIBGroups_ObjectIdentity = ObjectIdentity
cDot11RadioDiagMIBGroups = _CDot11RadioDiagMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2)
)

# Managed Objects groups

cDot11RadioDiagConfigGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 1)
)
cDot11RadioDiagConfigGlobalGroup.setObjects(
      *(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"))
)
if mibBuilder.loadTexts:
    cDot11RadioDiagConfigGlobalGroup.setStatus("deprecated")

cDot11RadioDiagConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 2, 2)
)
cDot11RadioDiagConfigGroupRev1.setObjects(
      *(("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempChannel"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempTxPowerLevel"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagMode"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagSettingsEnabled"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempClientTxPower"),
        ("CISCO-DOT11-RADIO-DIAGNOSTIC-MIB", "cDot11RadioDiagTempDataRateSet"))
)
if mibBuilder.loadTexts:
    cDot11RadioDiagConfigGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cDot11RadioDiagMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11RadioDiagMIBCompliance.setStatus(
        "deprecated"
    )

cDot11RadioDiagMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 105, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cDot11RadioDiagMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-RADIO-DIAGNOSTIC-MIB",
    **{"ciscoDot11RadioDiagMIB": ciscoDot11RadioDiagMIB,
       "cDot11RadioDiagMIBNotifs": cDot11RadioDiagMIBNotifs,
       "cDot11RadioDiagMIBObjects": cDot11RadioDiagMIBObjects,
       "cDot11RadioDiagConfigGlobal": cDot11RadioDiagConfigGlobal,
       "cDot11RadioDiagTable": cDot11RadioDiagTable,
       "cDot11RadioDiagEntry": cDot11RadioDiagEntry,
       "cDot11RadioDiagTempChannel": cDot11RadioDiagTempChannel,
       "cDot11RadioDiagTempTxPowerLevel": cDot11RadioDiagTempTxPowerLevel,
       "cDot11RadioDiagMode": cDot11RadioDiagMode,
       "cDot11RadioDiagSettingsEnabled": cDot11RadioDiagSettingsEnabled,
       "cDot11RadioDiagTempClientTxPower": cDot11RadioDiagTempClientTxPower,
       "cDot11RadioDiagTempDataRateSet": cDot11RadioDiagTempDataRateSet,
       "cDot11RadioDiagMIBConform": cDot11RadioDiagMIBConform,
       "cDot11RadioDiagMIBCompliances": cDot11RadioDiagMIBCompliances,
       "cDot11RadioDiagMIBCompliance": cDot11RadioDiagMIBCompliance,
       "cDot11RadioDiagMIBComplianceRev1": cDot11RadioDiagMIBComplianceRev1,
       "cDot11RadioDiagMIBGroups": cDot11RadioDiagMIBGroups,
       "cDot11RadioDiagConfigGlobalGroup": cDot11RadioDiagConfigGlobalGroup,
       "cDot11RadioDiagConfigGroupRev1": cDot11RadioDiagConfigGroupRev1}
)
