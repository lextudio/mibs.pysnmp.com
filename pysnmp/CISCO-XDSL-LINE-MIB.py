# SNMP MIB module (CISCO-XDSL-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-XDSL-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:47 2024
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

(adslLineConfProfileEntry,) = mibBuilder.importSymbols(
    "ADSL-LINE-MIB",
    "adslLineConfProfileEntry")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoXdslLineMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 204)
)
ciscoXdslLineMIB.setRevisions(
        ("2001-02-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoXdslLineMIBObjects_ObjectIdentity = ObjectIdentity
ciscoXdslLineMIBObjects = _CiscoXdslLineMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1)
)
_CXdslLineTable_Object = MibTable
cXdslLineTable = _CXdslLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 1)
)
if mibBuilder.loadTexts:
    cXdslLineTable.setStatus("current")
_CXdslLineEntry_Object = MibTableRow
cXdslLineEntry = _CXdslLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 1, 1)
)
cXdslLineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cXdslLineEntry.setStatus("current")
_CXdslLineTimeSinceLastChange_Type = TimeTicks
_CXdslLineTimeSinceLastChange_Object = MibTableColumn
cXdslLineTimeSinceLastChange = _CXdslLineTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 1, 1, 1),
    _CXdslLineTimeSinceLastChange_Type()
)
cXdslLineTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslLineTimeSinceLastChange.setStatus("current")
_CXdslLineNoOfChanges_Type = Counter32
_CXdslLineNoOfChanges_Object = MibTableColumn
cXdslLineNoOfChanges = _CXdslLineNoOfChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 1, 1, 2),
    _CXdslLineNoOfChanges_Type()
)
cXdslLineNoOfChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslLineNoOfChanges.setStatus("current")
_CXdslTestTable_Object = MibTable
cXdslTestTable = _CXdslTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2)
)
if mibBuilder.loadTexts:
    cXdslTestTable.setStatus("current")
_CXdslTestEntry_Object = MibTableRow
cXdslTestEntry = _CXdslTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1)
)
cXdslTestEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cXdslTestEntry.setStatus("current")


class _CXdslTestStatus_Type(Integer32):
    """Custom type cXdslTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("aborted", 5),
          ("active", 2),
          ("failed", 4),
          ("inactive", 1),
          ("passed", 3))
    )


_CXdslTestStatus_Type.__name__ = "Integer32"
_CXdslTestStatus_Object = MibTableColumn
cXdslTestStatus = _CXdslTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 1),
    _CXdslTestStatus_Type()
)
cXdslTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslTestStatus.setStatus("current")


class _CXdslTestType_Type(Integer32):
    """Custom type cXdslTestType based on Integer32"""
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
        *(("bertAnalogLocal", 3),
          ("bertAnalogRemote", 5),
          ("bertDigitalLocal", 2),
          ("bertDigitalRemote", 4),
          ("none", 1),
          ("other", 6))
    )


_CXdslTestType_Type.__name__ = "Integer32"
_CXdslTestType_Object = MibTableColumn
cXdslTestType = _CXdslTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 2),
    _CXdslTestType_Type()
)
cXdslTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXdslTestType.setStatus("current")


class _CXdslTestTrigger_Type(Integer32):
    """Custom type cXdslTestTrigger based on Integer32"""
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
        *(("clear", 3),
          ("ready", 4),
          ("start", 2),
          ("stop", 1))
    )


_CXdslTestTrigger_Type.__name__ = "Integer32"
_CXdslTestTrigger_Object = MibTableColumn
cXdslTestTrigger = _CXdslTestTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 3),
    _CXdslTestTrigger_Type()
)
cXdslTestTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXdslTestTrigger.setStatus("current")


class _CXdslTestTime_Type(Integer32):
    """Custom type cXdslTestTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_CXdslTestTime_Type.__name__ = "Integer32"
_CXdslTestTime_Object = MibTableColumn
cXdslTestTime = _CXdslTestTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 4),
    _CXdslTestTime_Type()
)
cXdslTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXdslTestTime.setStatus("current")
if mibBuilder.loadTexts:
    cXdslTestTime.setUnits("minutes")


class _CXdslTestBertErrors_Type(Bits):
    """Custom type cXdslTestBertErrors based on Bits"""
    namedValues = NamedValues(
        *(("coBertAborted", 5),
          ("cpeBertAborted", 1),
          ("lostCoSync", 6),
          ("lostCpeSync", 2),
          ("noCoSync", 7),
          ("noCpeResults", 4),
          ("noCpeSync", 3),
          ("noError", 0))
    )

_CXdslTestBertErrors_Type.__name__ = "Bits"
_CXdslTestBertErrors_Object = MibTableColumn
cXdslTestBertErrors = _CXdslTestBertErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 5),
    _CXdslTestBertErrors_Type()
)
cXdslTestBertErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslTestBertErrors.setStatus("current")


class _CXdslTestBertBitErrors_Type(Unsigned32):
    """Custom type cXdslTestBertBitErrors based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CXdslTestBertBitErrors_Type.__name__ = "Unsigned32"
_CXdslTestBertBitErrors_Object = MibTableColumn
cXdslTestBertBitErrors = _CXdslTestBertBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 6),
    _CXdslTestBertBitErrors_Type()
)
cXdslTestBertBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslTestBertBitErrors.setStatus("current")


class _CXdslTestBertRunTime_Type(Integer32):
    """Custom type cXdslTestBertRunTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_CXdslTestBertRunTime_Type.__name__ = "Integer32"
_CXdslTestBertRunTime_Object = MibTableColumn
cXdslTestBertRunTime = _CXdslTestBertRunTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 7),
    _CXdslTestBertRunTime_Type()
)
cXdslTestBertRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslTestBertRunTime.setStatus("current")
if mibBuilder.loadTexts:
    cXdslTestBertRunTime.setUnits("seconds")


class _CXdslTestBertBitRate_Type(Integer32):
    """Custom type cXdslTestBertBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000000),
    )


_CXdslTestBertBitRate_Type.__name__ = "Integer32"
_CXdslTestBertBitRate_Object = MibTableColumn
cXdslTestBertBitRate = _CXdslTestBertBitRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 2, 1, 8),
    _CXdslTestBertBitRate_Type()
)
cXdslTestBertBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cXdslTestBertBitRate.setStatus("current")
if mibBuilder.loadTexts:
    cXdslTestBertBitRate.setUnits("bps")
_CXdslModeTable_Object = MibTable
cXdslModeTable = _CXdslModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 3)
)
if mibBuilder.loadTexts:
    cXdslModeTable.setStatus("current")
_CXdslModeEntry_Object = MibTableRow
cXdslModeEntry = _CXdslModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 3, 1)
)
cXdslModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cXdslModeEntry.setStatus("current")


class _CXdslModeLoopback_Type(Integer32):
    """Custom type cXdslModeLoopback based on Integer32"""
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
        *(("disabled", 1),
          ("loopbackAnalogLocal", 2),
          ("loopbackAnalogRemote", 4),
          ("loopbackDigitalLocal", 3),
          ("loopbackDigitalRemote", 5),
          ("other", 6))
    )


_CXdslModeLoopback_Type.__name__ = "Integer32"
_CXdslModeLoopback_Object = MibTableColumn
cXdslModeLoopback = _CXdslModeLoopback_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 3, 1, 1),
    _CXdslModeLoopback_Type()
)
cXdslModeLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXdslModeLoopback.setStatus("current")


class _CXdslModeSpectrum_Type(Integer32):
    """Custom type cXdslModeSpectrum based on Integer32"""
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
        *(("disabled", 1),
          ("spectrum1", 2),
          ("spectrum2", 3),
          ("spectrum3", 4),
          ("spectrum4", 5),
          ("spectrum5", 6),
          ("spectrum6", 7))
    )


_CXdslModeSpectrum_Type.__name__ = "Integer32"
_CXdslModeSpectrum_Object = MibTableColumn
cXdslModeSpectrum = _CXdslModeSpectrum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 3, 1, 2),
    _CXdslModeSpectrum_Type()
)
cXdslModeSpectrum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cXdslModeSpectrum.setStatus("current")
_CXdslLineConfProfileTable_Object = MibTable
cXdslLineConfProfileTable = _CXdslLineConfProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 4)
)
if mibBuilder.loadTexts:
    cXdslLineConfProfileTable.setStatus("current")
_CXdslLineConfProfileEntry_Object = MibTableRow
cXdslLineConfProfileEntry = _CXdslLineConfProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cXdslLineConfProfileEntry.setStatus("current")


class _CXdslLineConfPayloadScrambled_Type(TruthValue):
    """Custom type cXdslLineConfPayloadScrambled based on TruthValue"""


_CXdslLineConfPayloadScrambled_Object = MibTableColumn
cXdslLineConfPayloadScrambled = _CXdslLineConfPayloadScrambled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 4, 1, 1),
    _CXdslLineConfPayloadScrambled_Type()
)
cXdslLineConfPayloadScrambled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cXdslLineConfPayloadScrambled.setStatus("current")


class _CXdslLineConfAlarmsEnabled_Type(TruthValue):
    """Custom type cXdslLineConfAlarmsEnabled based on TruthValue"""


_CXdslLineConfAlarmsEnabled_Object = MibTableColumn
cXdslLineConfAlarmsEnabled = _CXdslLineConfAlarmsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 4, 1, 2),
    _CXdslLineConfAlarmsEnabled_Type()
)
cXdslLineConfAlarmsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cXdslLineConfAlarmsEnabled.setStatus("current")


class _CXdslLineConfLinkUpDownTrap_Type(TruthValue):
    """Custom type cXdslLineConfLinkUpDownTrap based on TruthValue"""


_CXdslLineConfLinkUpDownTrap_Object = MibTableColumn
cXdslLineConfLinkUpDownTrap = _CXdslLineConfLinkUpDownTrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 1, 4, 1, 3),
    _CXdslLineConfLinkUpDownTrap_Type()
)
cXdslLineConfLinkUpDownTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cXdslLineConfLinkUpDownTrap.setStatus("current")
_CiscoXdslLineMIBConformance_ObjectIdentity = ObjectIdentity
ciscoXdslLineMIBConformance = _CiscoXdslLineMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3)
)
_CiscoXdslLineMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoXdslLineMIBCompliances = _CiscoXdslLineMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 1)
)
_CiscoXdslLineMIBGroups_ObjectIdentity = ObjectIdentity
ciscoXdslLineMIBGroups = _CiscoXdslLineMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 2)
)
adslLineConfProfileEntry.registerAugmentions(
    ("CISCO-XDSL-LINE-MIB",
     "cXdslLineConfProfileEntry")
)
cXdslLineConfProfileEntry.setIndexNames(*adslLineConfProfileEntry.getIndexNames())

# Managed Objects groups

cXdslLineGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 2, 1)
)
cXdslLineGroup.setObjects(
      *(("CISCO-XDSL-LINE-MIB", "cXdslLineTimeSinceLastChange"),
        ("CISCO-XDSL-LINE-MIB", "cXdslLineNoOfChanges"))
)
if mibBuilder.loadTexts:
    cXdslLineGroup.setStatus("current")

cXdslLineConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 2, 2)
)
cXdslLineConfProfileGroup.setObjects(
      *(("CISCO-XDSL-LINE-MIB", "cXdslLineConfPayloadScrambled"),
        ("CISCO-XDSL-LINE-MIB", "cXdslLineConfAlarmsEnabled"),
        ("CISCO-XDSL-LINE-MIB", "cXdslLineConfLinkUpDownTrap"))
)
if mibBuilder.loadTexts:
    cXdslLineConfProfileGroup.setStatus("current")

cXdslTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 2, 3)
)
cXdslTestGroup.setObjects(
      *(("CISCO-XDSL-LINE-MIB", "cXdslTestStatus"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestType"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestTrigger"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestTime"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestBertErrors"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestBertBitErrors"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestBertRunTime"),
        ("CISCO-XDSL-LINE-MIB", "cXdslTestBertBitRate"))
)
if mibBuilder.loadTexts:
    cXdslTestGroup.setStatus("current")

cXdslModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 2, 4)
)
cXdslModeGroup.setObjects(
      *(("CISCO-XDSL-LINE-MIB", "cXdslModeLoopback"),
        ("CISCO-XDSL-LINE-MIB", "cXdslModeSpectrum"))
)
if mibBuilder.loadTexts:
    cXdslModeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoXdslLineMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 204, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoXdslLineMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-XDSL-LINE-MIB",
    **{"ciscoXdslLineMIB": ciscoXdslLineMIB,
       "ciscoXdslLineMIBObjects": ciscoXdslLineMIBObjects,
       "cXdslLineTable": cXdslLineTable,
       "cXdslLineEntry": cXdslLineEntry,
       "cXdslLineTimeSinceLastChange": cXdslLineTimeSinceLastChange,
       "cXdslLineNoOfChanges": cXdslLineNoOfChanges,
       "cXdslTestTable": cXdslTestTable,
       "cXdslTestEntry": cXdslTestEntry,
       "cXdslTestStatus": cXdslTestStatus,
       "cXdslTestType": cXdslTestType,
       "cXdslTestTrigger": cXdslTestTrigger,
       "cXdslTestTime": cXdslTestTime,
       "cXdslTestBertErrors": cXdslTestBertErrors,
       "cXdslTestBertBitErrors": cXdslTestBertBitErrors,
       "cXdslTestBertRunTime": cXdslTestBertRunTime,
       "cXdslTestBertBitRate": cXdslTestBertBitRate,
       "cXdslModeTable": cXdslModeTable,
       "cXdslModeEntry": cXdslModeEntry,
       "cXdslModeLoopback": cXdslModeLoopback,
       "cXdslModeSpectrum": cXdslModeSpectrum,
       "cXdslLineConfProfileTable": cXdslLineConfProfileTable,
       "cXdslLineConfProfileEntry": cXdslLineConfProfileEntry,
       "cXdslLineConfPayloadScrambled": cXdslLineConfPayloadScrambled,
       "cXdslLineConfAlarmsEnabled": cXdslLineConfAlarmsEnabled,
       "cXdslLineConfLinkUpDownTrap": cXdslLineConfLinkUpDownTrap,
       "ciscoXdslLineMIBConformance": ciscoXdslLineMIBConformance,
       "ciscoXdslLineMIBCompliances": ciscoXdslLineMIBCompliances,
       "ciscoXdslLineMIBCompliance": ciscoXdslLineMIBCompliance,
       "ciscoXdslLineMIBGroups": ciscoXdslLineMIBGroups,
       "cXdslLineGroup": cXdslLineGroup,
       "cXdslLineConfProfileGroup": cXdslLineConfProfileGroup,
       "cXdslTestGroup": cXdslTestGroup,
       "cXdslModeGroup": cXdslModeGroup}
)
