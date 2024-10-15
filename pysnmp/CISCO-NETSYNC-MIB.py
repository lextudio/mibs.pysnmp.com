# SNMP MIB module (CISCO-NETSYNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-NETSYNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:11 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoNetsyncMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761)
)
ciscoNetsyncMIB.setRevisions(
        ("2010-10-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoNetsyncIfType(Integer32, TextualConvention):
    status = "current"
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("netsyncIfTypeAtm", 9),
          ("netsyncIfTypeController", 7),
          ("netsyncIfTypeEthernet", 3),
          ("netsyncIfTypeExt", 6),
          ("netsyncIfTypeGps", 8),
          ("netsyncIfTypeInternal", 2),
          ("netsyncIfTypeSonet", 4),
          ("netsyncIfTypeTop", 5),
          ("netsyncIfTypeUnknown", 1))
    )



class CiscoNetsyncNetworkOption(Integer32, TextualConvention):
    status = "current"
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
        *(("netsyncNetworkOption1", 2),
          ("netsyncNetworkOption2Gen1", 3),
          ("netsyncNetworkOption2Gen2", 4),
          ("netsyncNetworkOption3", 5),
          ("netsyncNetworkOptionInvalid", 6),
          ("netsyncNetworkOptionUnknown", 1))
    )



class CiscoNetsyncEECOption(Integer32, TextualConvention):
    status = "current"
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
        *(("netsyncEECOption1", 2),
          ("netsyncEECOption2", 3),
          ("netsyncEECOptionInvalid", 4),
          ("netsyncEECOptionUnknown", 1))
    )



class CiscoNetsyncQLMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("netsyncQLModeQlDisabled", 2),
          ("netsyncQLModeQlEnabled", 3),
          ("netsyncQLModeUnknown", 1))
    )



class CiscoNetsyncClockMode(Integer32, TextualConvention):
    status = "current"
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
        *(("netsyncClockModeFreerun", 2),
          ("netsyncClockModeHoldover", 3),
          ("netsyncClockModeLocked", 4),
          ("netsyncClockModeUnknown", 1))
    )



class CiscoNetsyncQualityLevel(Integer32, TextualConvention):
    status = "current"
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("netsyncQualityLevelDNU", 2),
          ("netsyncQualityLevelDUS", 3),
          ("netsyncQualityLevelFAILED", 4),
          ("netsyncQualityLevelINV0", 5),
          ("netsyncQualityLevelINV1", 6),
          ("netsyncQualityLevelINV10", 15),
          ("netsyncQualityLevelINV11", 16),
          ("netsyncQualityLevelINV12", 17),
          ("netsyncQualityLevelINV13", 18),
          ("netsyncQualityLevelINV14", 19),
          ("netsyncQualityLevelINV15", 20),
          ("netsyncQualityLevelINV2", 7),
          ("netsyncQualityLevelINV3", 8),
          ("netsyncQualityLevelINV4", 9),
          ("netsyncQualityLevelINV5", 10),
          ("netsyncQualityLevelINV6", 11),
          ("netsyncQualityLevelINV7", 12),
          ("netsyncQualityLevelINV8", 13),
          ("netsyncQualityLevelINV9", 14),
          ("netsyncQualityLevelNSUPP", 21),
          ("netsyncQualityLevelNULL", 1),
          ("netsyncQualityLevelPRC", 22),
          ("netsyncQualityLevelPROV", 23),
          ("netsyncQualityLevelPRS", 24),
          ("netsyncQualityLevelSEC", 25),
          ("netsyncQualityLevelSMC", 26),
          ("netsyncQualityLevelSSUA", 27),
          ("netsyncQualityLevelSSUB", 28),
          ("netsyncQualityLevelST2", 29),
          ("netsyncQualityLevelST3", 30),
          ("netsyncQualityLevelST3E", 31),
          ("netsyncQualityLevelST4", 32),
          ("netsyncQualityLevelSTU", 33),
          ("netsyncQualityLevelTNC", 34),
          ("netsyncQualityLevelUNC", 35),
          ("netsyncQualityLevelUNK", 36))
    )



class CiscoNetsyncSSMCap(Integer32, TextualConvention):
    status = "current"
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
        *(("netsyncSSMCapInvalid", 5),
          ("netsyncSSMCapNone", 1),
          ("netsyncSSMCapRx", 4),
          ("netsyncSSMCapTx", 3),
          ("netsyncSSMCapTxRx", 2))
    )



class CiscoNetsyncESMCCap(Integer32, TextualConvention):
    status = "current"
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
        *(("netsyncESMCCapInvalid", 5),
          ("netsyncESMCCapNone", 1),
          ("netsyncESMCCapRx", 4),
          ("netsyncESMCCapTx", 3),
          ("netsyncESMCCapTxRx", 2))
    )



class CiscoNetsyncAlarmInfo(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoNetsyncMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBNotifs = _CiscoNetsyncMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 0)
)
_CiscoNetsyncMIBObjects_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBObjects = _CiscoNetsyncMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1)
)
_CiscoNetsyncMIBTables_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBTables = _CiscoNetsyncMIBTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1)
)
_CnsClkSelGlobalTable_Object = MibTable
cnsClkSelGlobalTable = _CnsClkSelGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cnsClkSelGlobalTable.setStatus("current")
_CnsClkSelGlobalEntry_Object = MibTableRow
cnsClkSelGlobalEntry = _CnsClkSelGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1)
)
cnsClkSelGlobalEntry.setIndexNames(
    (0, "CISCO-NETSYNC-MIB", "cnsClkSelGloProcIndex"),
)
if mibBuilder.loadTexts:
    cnsClkSelGlobalEntry.setStatus("current")


class _CnsClkSelGloProcIndex_Type(Unsigned32):
    """Custom type cnsClkSelGloProcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsClkSelGloProcIndex_Type.__name__ = "Unsigned32"
_CnsClkSelGloProcIndex_Object = MibTableColumn
cnsClkSelGloProcIndex = _CnsClkSelGloProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 1),
    _CnsClkSelGloProcIndex_Type()
)
cnsClkSelGloProcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnsClkSelGloProcIndex.setStatus("current")
_CnsClkSelGlobProcessMode_Type = CiscoNetsyncQLMode
_CnsClkSelGlobProcessMode_Object = MibTableColumn
cnsClkSelGlobProcessMode = _CnsClkSelGlobProcessMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 2),
    _CnsClkSelGlobProcessMode_Type()
)
cnsClkSelGlobProcessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobProcessMode.setStatus("current")
_CnsClkSelGlobClockMode_Type = CiscoNetsyncClockMode
_CnsClkSelGlobClockMode_Object = MibTableColumn
cnsClkSelGlobClockMode = _CnsClkSelGlobClockMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 3),
    _CnsClkSelGlobClockMode_Type()
)
cnsClkSelGlobClockMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobClockMode.setStatus("current")


class _CnsClkSelGlobNetsyncEnable_Type(TruthValue):
    """Custom type cnsClkSelGlobNetsyncEnable based on TruthValue"""


_CnsClkSelGlobNetsyncEnable_Object = MibTableColumn
cnsClkSelGlobNetsyncEnable = _CnsClkSelGlobNetsyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 4),
    _CnsClkSelGlobNetsyncEnable_Type()
)
cnsClkSelGlobNetsyncEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobNetsyncEnable.setStatus("current")


class _CnsClkSelGlobRevertiveMode_Type(TruthValue):
    """Custom type cnsClkSelGlobRevertiveMode based on TruthValue"""


_CnsClkSelGlobRevertiveMode_Object = MibTableColumn
cnsClkSelGlobRevertiveMode = _CnsClkSelGlobRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 5),
    _CnsClkSelGlobRevertiveMode_Type()
)
cnsClkSelGlobRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobRevertiveMode.setStatus("current")


class _CnsClkSelGlobESMCMode_Type(TruthValue):
    """Custom type cnsClkSelGlobESMCMode based on TruthValue"""


_CnsClkSelGlobESMCMode_Object = MibTableColumn
cnsClkSelGlobESMCMode = _CnsClkSelGlobESMCMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 6),
    _CnsClkSelGlobESMCMode_Type()
)
cnsClkSelGlobESMCMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobESMCMode.setStatus("current")


class _CnsClkSelGlobEECOption_Type(CiscoNetsyncEECOption):
    """Custom type cnsClkSelGlobEECOption based on CiscoNetsyncEECOption"""


_CnsClkSelGlobEECOption_Object = MibTableColumn
cnsClkSelGlobEECOption = _CnsClkSelGlobEECOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 7),
    _CnsClkSelGlobEECOption_Type()
)
cnsClkSelGlobEECOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobEECOption.setStatus("current")


class _CnsClkSelGlobNetworkOption_Type(CiscoNetsyncNetworkOption):
    """Custom type cnsClkSelGlobNetworkOption based on CiscoNetsyncNetworkOption"""


_CnsClkSelGlobNetworkOption_Object = MibTableColumn
cnsClkSelGlobNetworkOption = _CnsClkSelGlobNetworkOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 8),
    _CnsClkSelGlobNetworkOption_Type()
)
cnsClkSelGlobNetworkOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobNetworkOption.setStatus("current")


class _CnsClkSelGlobHoldoffTime_Type(Unsigned32):
    """Custom type cnsClkSelGlobHoldoffTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsClkSelGlobHoldoffTime_Type.__name__ = "Unsigned32"
_CnsClkSelGlobHoldoffTime_Object = MibTableColumn
cnsClkSelGlobHoldoffTime = _CnsClkSelGlobHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 9),
    _CnsClkSelGlobHoldoffTime_Type()
)
cnsClkSelGlobHoldoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobHoldoffTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsClkSelGlobHoldoffTime.setUnits("milliseconds")


class _CnsClkSelGlobWtrTime_Type(Unsigned32):
    """Custom type cnsClkSelGlobWtrTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsClkSelGlobWtrTime_Type.__name__ = "Unsigned32"
_CnsClkSelGlobWtrTime_Object = MibTableColumn
cnsClkSelGlobWtrTime = _CnsClkSelGlobWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 10),
    _CnsClkSelGlobWtrTime_Type()
)
cnsClkSelGlobWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsClkSelGlobWtrTime.setUnits("seconds")


class _CnsClkSelGlobNofSources_Type(Unsigned32):
    """Custom type cnsClkSelGlobNofSources based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CnsClkSelGlobNofSources_Type.__name__ = "Unsigned32"
_CnsClkSelGlobNofSources_Object = MibTableColumn
cnsClkSelGlobNofSources = _CnsClkSelGlobNofSources_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 11),
    _CnsClkSelGlobNofSources_Type()
)
cnsClkSelGlobNofSources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobNofSources.setStatus("current")
if mibBuilder.loadTexts:
    cnsClkSelGlobNofSources.setUnits("clock sources")
_CnsClkSelGlobLastHoldoverSeconds_Type = Gauge32
_CnsClkSelGlobLastHoldoverSeconds_Object = MibTableColumn
cnsClkSelGlobLastHoldoverSeconds = _CnsClkSelGlobLastHoldoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 12),
    _CnsClkSelGlobLastHoldoverSeconds_Type()
)
cnsClkSelGlobLastHoldoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobLastHoldoverSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cnsClkSelGlobLastHoldoverSeconds.setUnits("seconds")
_CnsClkSelGlobCurrHoldoverSeconds_Type = Gauge32
_CnsClkSelGlobCurrHoldoverSeconds_Object = MibTableColumn
cnsClkSelGlobCurrHoldoverSeconds = _CnsClkSelGlobCurrHoldoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 1, 1, 13),
    _CnsClkSelGlobCurrHoldoverSeconds_Type()
)
cnsClkSelGlobCurrHoldoverSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsClkSelGlobCurrHoldoverSeconds.setStatus("current")
if mibBuilder.loadTexts:
    cnsClkSelGlobCurrHoldoverSeconds.setUnits("seconds")
_CnsSelectedInputSourceTable_Object = MibTable
cnsSelectedInputSourceTable = _CnsSelectedInputSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cnsSelectedInputSourceTable.setStatus("current")
_CnsSelectedInputSourceEntry_Object = MibTableRow
cnsSelectedInputSourceEntry = _CnsSelectedInputSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1)
)
cnsSelectedInputSourceEntry.setIndexNames(
    (0, "CISCO-NETSYNC-MIB", "cnsSelInpSrcNetsyncIndex"),
)
if mibBuilder.loadTexts:
    cnsSelectedInputSourceEntry.setStatus("current")


class _CnsSelInpSrcNetsyncIndex_Type(Unsigned32):
    """Custom type cnsSelInpSrcNetsyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnsSelInpSrcNetsyncIndex_Type.__name__ = "Unsigned32"
_CnsSelInpSrcNetsyncIndex_Object = MibTableColumn
cnsSelInpSrcNetsyncIndex = _CnsSelInpSrcNetsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 1),
    _CnsSelInpSrcNetsyncIndex_Type()
)
cnsSelInpSrcNetsyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnsSelInpSrcNetsyncIndex.setStatus("current")


class _CnsSelInpSrcName_Type(SnmpAdminString):
    """Custom type cnsSelInpSrcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnsSelInpSrcName_Type.__name__ = "SnmpAdminString"
_CnsSelInpSrcName_Object = MibTableColumn
cnsSelInpSrcName = _CnsSelInpSrcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 2),
    _CnsSelInpSrcName_Type()
)
cnsSelInpSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcName.setStatus("current")
_CnsSelInpSrcIntfType_Type = CiscoNetsyncIfType
_CnsSelInpSrcIntfType_Object = MibTableColumn
cnsSelInpSrcIntfType = _CnsSelInpSrcIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 3),
    _CnsSelInpSrcIntfType_Type()
)
cnsSelInpSrcIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcIntfType.setStatus("current")
_CnsSelInpSrcQualityLevel_Type = CiscoNetsyncQualityLevel
_CnsSelInpSrcQualityLevel_Object = MibTableColumn
cnsSelInpSrcQualityLevel = _CnsSelInpSrcQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 4),
    _CnsSelInpSrcQualityLevel_Type()
)
cnsSelInpSrcQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcQualityLevel.setStatus("current")


class _CnsSelInpSrcPriority_Type(Unsigned32):
    """Custom type cnsSelInpSrcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnsSelInpSrcPriority_Type.__name__ = "Unsigned32"
_CnsSelInpSrcPriority_Object = MibTableColumn
cnsSelInpSrcPriority = _CnsSelInpSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 5),
    _CnsSelInpSrcPriority_Type()
)
cnsSelInpSrcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcPriority.setStatus("current")
_CnsSelInpSrcTimestamp_Type = TimeStamp
_CnsSelInpSrcTimestamp_Object = MibTableColumn
cnsSelInpSrcTimestamp = _CnsSelInpSrcTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 6),
    _CnsSelInpSrcTimestamp_Type()
)
cnsSelInpSrcTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcTimestamp.setStatus("current")
_CnsSelInpSrcFSW_Type = TruthValue
_CnsSelInpSrcFSW_Object = MibTableColumn
cnsSelInpSrcFSW = _CnsSelInpSrcFSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 7),
    _CnsSelInpSrcFSW_Type()
)
cnsSelInpSrcFSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcFSW.setStatus("current")
_CnsSelInpSrcMSW_Type = TruthValue
_CnsSelInpSrcMSW_Object = MibTableColumn
cnsSelInpSrcMSW = _CnsSelInpSrcMSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 2, 1, 8),
    _CnsSelInpSrcMSW_Type()
)
cnsSelInpSrcMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsSelInpSrcMSW.setStatus("current")
_CnsInputSourceTable_Object = MibTable
cnsInputSourceTable = _CnsInputSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cnsInputSourceTable.setStatus("current")
_CnsInputSourceEntry_Object = MibTableRow
cnsInputSourceEntry = _CnsInputSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1)
)
cnsInputSourceEntry.setIndexNames(
    (0, "CISCO-NETSYNC-MIB", "cnsInpSrcNetsyncIndex"),
)
if mibBuilder.loadTexts:
    cnsInputSourceEntry.setStatus("current")


class _CnsInpSrcNetsyncIndex_Type(Unsigned32):
    """Custom type cnsInpSrcNetsyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnsInpSrcNetsyncIndex_Type.__name__ = "Unsigned32"
_CnsInpSrcNetsyncIndex_Object = MibTableColumn
cnsInpSrcNetsyncIndex = _CnsInpSrcNetsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 1),
    _CnsInpSrcNetsyncIndex_Type()
)
cnsInpSrcNetsyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnsInpSrcNetsyncIndex.setStatus("current")


class _CnsInpSrcName_Type(SnmpAdminString):
    """Custom type cnsInpSrcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnsInpSrcName_Type.__name__ = "SnmpAdminString"
_CnsInpSrcName_Object = MibTableColumn
cnsInpSrcName = _CnsInpSrcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 2),
    _CnsInpSrcName_Type()
)
cnsInpSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcName.setStatus("current")
_CnsInpSrcIntfType_Type = CiscoNetsyncIfType
_CnsInpSrcIntfType_Object = MibTableColumn
cnsInpSrcIntfType = _CnsInpSrcIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 3),
    _CnsInpSrcIntfType_Type()
)
cnsInpSrcIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcIntfType.setStatus("current")


class _CnsInpSrcPriority_Type(Unsigned32):
    """Custom type cnsInpSrcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnsInpSrcPriority_Type.__name__ = "Unsigned32"
_CnsInpSrcPriority_Object = MibTableColumn
cnsInpSrcPriority = _CnsInpSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 4),
    _CnsInpSrcPriority_Type()
)
cnsInpSrcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcPriority.setStatus("current")
_CnsInpSrcESMCCap_Type = CiscoNetsyncESMCCap
_CnsInpSrcESMCCap_Object = MibTableColumn
cnsInpSrcESMCCap = _CnsInpSrcESMCCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 5),
    _CnsInpSrcESMCCap_Type()
)
cnsInpSrcESMCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcESMCCap.setStatus("current")
_CnsInpSrcSSMCap_Type = CiscoNetsyncSSMCap
_CnsInpSrcSSMCap_Object = MibTableColumn
cnsInpSrcSSMCap = _CnsInpSrcSSMCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 6),
    _CnsInpSrcSSMCap_Type()
)
cnsInpSrcSSMCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcSSMCap.setStatus("current")
_CnsInpSrcQualityLevelTxCfg_Type = CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelTxCfg_Object = MibTableColumn
cnsInpSrcQualityLevelTxCfg = _CnsInpSrcQualityLevelTxCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 7),
    _CnsInpSrcQualityLevelTxCfg_Type()
)
cnsInpSrcQualityLevelTxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcQualityLevelTxCfg.setStatus("current")
_CnsInpSrcQualityLevelRxCfg_Type = CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelRxCfg_Object = MibTableColumn
cnsInpSrcQualityLevelRxCfg = _CnsInpSrcQualityLevelRxCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 8),
    _CnsInpSrcQualityLevelRxCfg_Type()
)
cnsInpSrcQualityLevelRxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcQualityLevelRxCfg.setStatus("current")
_CnsInpSrcQualityLevelTx_Type = CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelTx_Object = MibTableColumn
cnsInpSrcQualityLevelTx = _CnsInpSrcQualityLevelTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 9),
    _CnsInpSrcQualityLevelTx_Type()
)
cnsInpSrcQualityLevelTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcQualityLevelTx.setStatus("current")
_CnsInpSrcQualityLevelRx_Type = CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevelRx_Object = MibTableColumn
cnsInpSrcQualityLevelRx = _CnsInpSrcQualityLevelRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 10),
    _CnsInpSrcQualityLevelRx_Type()
)
cnsInpSrcQualityLevelRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcQualityLevelRx.setStatus("current")
_CnsInpSrcQualityLevel_Type = CiscoNetsyncQualityLevel
_CnsInpSrcQualityLevel_Object = MibTableColumn
cnsInpSrcQualityLevel = _CnsInpSrcQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 11),
    _CnsInpSrcQualityLevel_Type()
)
cnsInpSrcQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcQualityLevel.setStatus("current")


class _CnsInpSrcHoldoffTime_Type(Unsigned32):
    """Custom type cnsInpSrcHoldoffTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsInpSrcHoldoffTime_Type.__name__ = "Unsigned32"
_CnsInpSrcHoldoffTime_Object = MibTableColumn
cnsInpSrcHoldoffTime = _CnsInpSrcHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 12),
    _CnsInpSrcHoldoffTime_Type()
)
cnsInpSrcHoldoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcHoldoffTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsInpSrcHoldoffTime.setUnits("milliseconds")


class _CnsInpSrcWtrTime_Type(Unsigned32):
    """Custom type cnsInpSrcWtrTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsInpSrcWtrTime_Type.__name__ = "Unsigned32"
_CnsInpSrcWtrTime_Object = MibTableColumn
cnsInpSrcWtrTime = _CnsInpSrcWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 13),
    _CnsInpSrcWtrTime_Type()
)
cnsInpSrcWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsInpSrcWtrTime.setUnits("Seconds")
_CnsInpSrcLockout_Type = TruthValue
_CnsInpSrcLockout_Object = MibTableColumn
cnsInpSrcLockout = _CnsInpSrcLockout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 14),
    _CnsInpSrcLockout_Type()
)
cnsInpSrcLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcLockout.setStatus("current")
_CnsInpSrcSignalFailure_Type = TruthValue
_CnsInpSrcSignalFailure_Object = MibTableColumn
cnsInpSrcSignalFailure = _CnsInpSrcSignalFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 15),
    _CnsInpSrcSignalFailure_Type()
)
cnsInpSrcSignalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcSignalFailure.setStatus("current")
_CnsInpSrcAlarm_Type = TruthValue
_CnsInpSrcAlarm_Object = MibTableColumn
cnsInpSrcAlarm = _CnsInpSrcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 16),
    _CnsInpSrcAlarm_Type()
)
cnsInpSrcAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcAlarm.setStatus("current")
_CnsInpSrcAlarmInfo_Type = CiscoNetsyncAlarmInfo
_CnsInpSrcAlarmInfo_Object = MibTableColumn
cnsInpSrcAlarmInfo = _CnsInpSrcAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 17),
    _CnsInpSrcAlarmInfo_Type()
)
cnsInpSrcAlarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcAlarmInfo.setStatus("current")
_CnsInpSrcFSW_Type = TruthValue
_CnsInpSrcFSW_Object = MibTableColumn
cnsInpSrcFSW = _CnsInpSrcFSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 18),
    _CnsInpSrcFSW_Type()
)
cnsInpSrcFSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcFSW.setStatus("current")
_CnsInpSrcMSW_Type = TruthValue
_CnsInpSrcMSW_Object = MibTableColumn
cnsInpSrcMSW = _CnsInpSrcMSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 3, 1, 19),
    _CnsInpSrcMSW_Type()
)
cnsInpSrcMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsInpSrcMSW.setStatus("current")
_CnsExtOutputTable_Object = MibTable
cnsExtOutputTable = _CnsExtOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cnsExtOutputTable.setStatus("current")
_CnsExtOutputEntry_Object = MibTableRow
cnsExtOutputEntry = _CnsExtOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1)
)
cnsExtOutputEntry.setIndexNames(
    (0, "CISCO-NETSYNC-MIB", "cnsExtOutListIndex"),
)
if mibBuilder.loadTexts:
    cnsExtOutputEntry.setStatus("current")


class _CnsExtOutListIndex_Type(Unsigned32):
    """Custom type cnsExtOutListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnsExtOutListIndex_Type.__name__ = "Unsigned32"
_CnsExtOutListIndex_Object = MibTableColumn
cnsExtOutListIndex = _CnsExtOutListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 1),
    _CnsExtOutListIndex_Type()
)
cnsExtOutListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnsExtOutListIndex.setStatus("current")


class _CnsExtOutSelNetsyncIndex_Type(Unsigned32):
    """Custom type cnsExtOutSelNetsyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnsExtOutSelNetsyncIndex_Type.__name__ = "Unsigned32"
_CnsExtOutSelNetsyncIndex_Object = MibTableColumn
cnsExtOutSelNetsyncIndex = _CnsExtOutSelNetsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 2),
    _CnsExtOutSelNetsyncIndex_Type()
)
cnsExtOutSelNetsyncIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutSelNetsyncIndex.setStatus("current")


class _CnsExtOutName_Type(SnmpAdminString):
    """Custom type cnsExtOutName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnsExtOutName_Type.__name__ = "SnmpAdminString"
_CnsExtOutName_Object = MibTableColumn
cnsExtOutName = _CnsExtOutName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 3),
    _CnsExtOutName_Type()
)
cnsExtOutName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutName.setStatus("current")
_CnsExtOutIntfType_Type = CiscoNetsyncIfType
_CnsExtOutIntfType_Object = MibTableColumn
cnsExtOutIntfType = _CnsExtOutIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 4),
    _CnsExtOutIntfType_Type()
)
cnsExtOutIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutIntfType.setStatus("current")
_CnsExtOutQualityLevel_Type = CiscoNetsyncQualityLevel
_CnsExtOutQualityLevel_Object = MibTableColumn
cnsExtOutQualityLevel = _CnsExtOutQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 5),
    _CnsExtOutQualityLevel_Type()
)
cnsExtOutQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutQualityLevel.setStatus("current")


class _CnsExtOutPriority_Type(Unsigned32):
    """Custom type cnsExtOutPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnsExtOutPriority_Type.__name__ = "Unsigned32"
_CnsExtOutPriority_Object = MibTableColumn
cnsExtOutPriority = _CnsExtOutPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 6),
    _CnsExtOutPriority_Type()
)
cnsExtOutPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutPriority.setStatus("current")
_CnsExtOutFSW_Type = TruthValue
_CnsExtOutFSW_Object = MibTableColumn
cnsExtOutFSW = _CnsExtOutFSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 7),
    _CnsExtOutFSW_Type()
)
cnsExtOutFSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutFSW.setStatus("current")
_CnsExtOutMSW_Type = TruthValue
_CnsExtOutMSW_Object = MibTableColumn
cnsExtOutMSW = _CnsExtOutMSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 8),
    _CnsExtOutMSW_Type()
)
cnsExtOutMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutMSW.setStatus("current")
_CnsExtOutSquelch_Type = TruthValue
_CnsExtOutSquelch_Object = MibTableColumn
cnsExtOutSquelch = _CnsExtOutSquelch_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 4, 1, 9),
    _CnsExtOutSquelch_Type()
)
cnsExtOutSquelch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsExtOutSquelch.setStatus("current")
_CnsT4ClockSourceTable_Object = MibTable
cnsT4ClockSourceTable = _CnsT4ClockSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cnsT4ClockSourceTable.setStatus("current")
_CnsT4ClockSourceEntry_Object = MibTableRow
cnsT4ClockSourceEntry = _CnsT4ClockSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1)
)
cnsT4ClockSourceEntry.setIndexNames(
    (0, "CISCO-NETSYNC-MIB", "cnsExtOutListIndex"),
    (0, "CISCO-NETSYNC-MIB", "cnsT4ClkSrcNetsyncIndex"),
)
if mibBuilder.loadTexts:
    cnsT4ClockSourceEntry.setStatus("current")


class _CnsT4ClkSrcNetsyncIndex_Type(Unsigned32):
    """Custom type cnsT4ClkSrcNetsyncIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CnsT4ClkSrcNetsyncIndex_Type.__name__ = "Unsigned32"
_CnsT4ClkSrcNetsyncIndex_Object = MibTableColumn
cnsT4ClkSrcNetsyncIndex = _CnsT4ClkSrcNetsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 1),
    _CnsT4ClkSrcNetsyncIndex_Type()
)
cnsT4ClkSrcNetsyncIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnsT4ClkSrcNetsyncIndex.setStatus("current")


class _CnsT4ClkSrcName_Type(SnmpAdminString):
    """Custom type cnsT4ClkSrcName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CnsT4ClkSrcName_Type.__name__ = "SnmpAdminString"
_CnsT4ClkSrcName_Object = MibTableColumn
cnsT4ClkSrcName = _CnsT4ClkSrcName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 2),
    _CnsT4ClkSrcName_Type()
)
cnsT4ClkSrcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcName.setStatus("current")
_CnsT4ClkSrcIntfType_Type = CiscoNetsyncIfType
_CnsT4ClkSrcIntfType_Object = MibTableColumn
cnsT4ClkSrcIntfType = _CnsT4ClkSrcIntfType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 3),
    _CnsT4ClkSrcIntfType_Type()
)
cnsT4ClkSrcIntfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcIntfType.setStatus("current")


class _CnsT4ClkSrcPriority_Type(Unsigned32):
    """Custom type cnsT4ClkSrcPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CnsT4ClkSrcPriority_Type.__name__ = "Unsigned32"
_CnsT4ClkSrcPriority_Object = MibTableColumn
cnsT4ClkSrcPriority = _CnsT4ClkSrcPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 4),
    _CnsT4ClkSrcPriority_Type()
)
cnsT4ClkSrcPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcPriority.setStatus("current")
_CnsT4ClkSrcESMCCap_Type = CiscoNetsyncESMCCap
_CnsT4ClkSrcESMCCap_Object = MibTableColumn
cnsT4ClkSrcESMCCap = _CnsT4ClkSrcESMCCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 5),
    _CnsT4ClkSrcESMCCap_Type()
)
cnsT4ClkSrcESMCCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcESMCCap.setStatus("current")
_CnsT4ClkSrcSSMCap_Type = CiscoNetsyncSSMCap
_CnsT4ClkSrcSSMCap_Object = MibTableColumn
cnsT4ClkSrcSSMCap = _CnsT4ClkSrcSSMCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 6),
    _CnsT4ClkSrcSSMCap_Type()
)
cnsT4ClkSrcSSMCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcSSMCap.setStatus("current")
_CnsT4ClkSrcQualityLevelTxCfg_Type = CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelTxCfg_Object = MibTableColumn
cnsT4ClkSrcQualityLevelTxCfg = _CnsT4ClkSrcQualityLevelTxCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 7),
    _CnsT4ClkSrcQualityLevelTxCfg_Type()
)
cnsT4ClkSrcQualityLevelTxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcQualityLevelTxCfg.setStatus("current")
_CnsT4ClkSrcQualityLevelRxCfg_Type = CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelRxCfg_Object = MibTableColumn
cnsT4ClkSrcQualityLevelRxCfg = _CnsT4ClkSrcQualityLevelRxCfg_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 8),
    _CnsT4ClkSrcQualityLevelRxCfg_Type()
)
cnsT4ClkSrcQualityLevelRxCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcQualityLevelRxCfg.setStatus("current")
_CnsT4ClkSrcQualityLevelTx_Type = CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelTx_Object = MibTableColumn
cnsT4ClkSrcQualityLevelTx = _CnsT4ClkSrcQualityLevelTx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 9),
    _CnsT4ClkSrcQualityLevelTx_Type()
)
cnsT4ClkSrcQualityLevelTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcQualityLevelTx.setStatus("current")
_CnsT4ClkSrcQualityLevelRx_Type = CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevelRx_Object = MibTableColumn
cnsT4ClkSrcQualityLevelRx = _CnsT4ClkSrcQualityLevelRx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 10),
    _CnsT4ClkSrcQualityLevelRx_Type()
)
cnsT4ClkSrcQualityLevelRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcQualityLevelRx.setStatus("current")
_CnsT4ClkSrcQualityLevel_Type = CiscoNetsyncQualityLevel
_CnsT4ClkSrcQualityLevel_Object = MibTableColumn
cnsT4ClkSrcQualityLevel = _CnsT4ClkSrcQualityLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 11),
    _CnsT4ClkSrcQualityLevel_Type()
)
cnsT4ClkSrcQualityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcQualityLevel.setStatus("current")


class _CnsT4ClkSrcHoldoffTime_Type(Unsigned32):
    """Custom type cnsT4ClkSrcHoldoffTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsT4ClkSrcHoldoffTime_Type.__name__ = "Unsigned32"
_CnsT4ClkSrcHoldoffTime_Object = MibTableColumn
cnsT4ClkSrcHoldoffTime = _CnsT4ClkSrcHoldoffTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 12),
    _CnsT4ClkSrcHoldoffTime_Type()
)
cnsT4ClkSrcHoldoffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcHoldoffTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsT4ClkSrcHoldoffTime.setUnits("milliseconds")


class _CnsT4ClkSrcWtrTime_Type(Unsigned32):
    """Custom type cnsT4ClkSrcWtrTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CnsT4ClkSrcWtrTime_Type.__name__ = "Unsigned32"
_CnsT4ClkSrcWtrTime_Object = MibTableColumn
cnsT4ClkSrcWtrTime = _CnsT4ClkSrcWtrTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 13),
    _CnsT4ClkSrcWtrTime_Type()
)
cnsT4ClkSrcWtrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcWtrTime.setStatus("current")
if mibBuilder.loadTexts:
    cnsT4ClkSrcWtrTime.setUnits("seconds")
_CnsT4ClkSrcLockout_Type = TruthValue
_CnsT4ClkSrcLockout_Object = MibTableColumn
cnsT4ClkSrcLockout = _CnsT4ClkSrcLockout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 14),
    _CnsT4ClkSrcLockout_Type()
)
cnsT4ClkSrcLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcLockout.setStatus("current")
_CnsT4ClkSrcSignalFailure_Type = TruthValue
_CnsT4ClkSrcSignalFailure_Object = MibTableColumn
cnsT4ClkSrcSignalFailure = _CnsT4ClkSrcSignalFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 15),
    _CnsT4ClkSrcSignalFailure_Type()
)
cnsT4ClkSrcSignalFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcSignalFailure.setStatus("current")
_CnsT4ClkSrcAlarm_Type = TruthValue
_CnsT4ClkSrcAlarm_Object = MibTableColumn
cnsT4ClkSrcAlarm = _CnsT4ClkSrcAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 16),
    _CnsT4ClkSrcAlarm_Type()
)
cnsT4ClkSrcAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcAlarm.setStatus("current")
_CnsT4ClkSrcAlarmInfo_Type = CiscoNetsyncAlarmInfo
_CnsT4ClkSrcAlarmInfo_Object = MibTableColumn
cnsT4ClkSrcAlarmInfo = _CnsT4ClkSrcAlarmInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 17),
    _CnsT4ClkSrcAlarmInfo_Type()
)
cnsT4ClkSrcAlarmInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcAlarmInfo.setStatus("current")
_CnsT4ClkSrcFSW_Type = TruthValue
_CnsT4ClkSrcFSW_Object = MibTableColumn
cnsT4ClkSrcFSW = _CnsT4ClkSrcFSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 18),
    _CnsT4ClkSrcFSW_Type()
)
cnsT4ClkSrcFSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcFSW.setStatus("current")
_CnsT4ClkSrcMSW_Type = TruthValue
_CnsT4ClkSrcMSW_Object = MibTableColumn
cnsT4ClkSrcMSW = _CnsT4ClkSrcMSW_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 1, 5, 1, 19),
    _CnsT4ClkSrcMSW_Type()
)
cnsT4ClkSrcMSW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnsT4ClkSrcMSW.setStatus("current")
_CnsNotifObjects_ObjectIdentity = ObjectIdentity
cnsNotifObjects = _CnsNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 2)
)
_CnsInpSrcFailClear_Type = TruthValue
_CnsInpSrcFailClear_Object = MibScalar
cnsInpSrcFailClear = _CnsInpSrcFailClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 2, 1),
    _CnsInpSrcFailClear_Type()
)
cnsInpSrcFailClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnsInpSrcFailClear.setStatus("current")
_CnsInpSrcAlarmClear_Type = TruthValue
_CnsInpSrcAlarmClear_Object = MibScalar
cnsInpSrcAlarmClear = _CnsInpSrcAlarmClear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 2, 2),
    _CnsInpSrcAlarmClear_Type()
)
cnsInpSrcAlarmClear.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cnsInpSrcAlarmClear.setStatus("current")
_CiscoNetsyncMIBNotifControl_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBNotifControl = _CiscoNetsyncMIBNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 3)
)


class _CnsMIBEnableStatusNotification_Type(TruthValue):
    """Custom type cnsMIBEnableStatusNotification based on TruthValue"""


_CnsMIBEnableStatusNotification_Object = MibScalar
cnsMIBEnableStatusNotification = _CnsMIBEnableStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 1, 3, 1),
    _CnsMIBEnableStatusNotification_Type()
)
cnsMIBEnableStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cnsMIBEnableStatusNotification.setStatus("current")
_CiscoNetsyncMIBConform_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBConform = _CiscoNetsyncMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2)
)
_CiscoNetsyncMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBCompliances = _CiscoNetsyncMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 1)
)
_CiscoNetsyncMIBGroups_ObjectIdentity = ObjectIdentity
ciscoNetsyncMIBGroups = _CiscoNetsyncMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2)
)

# Managed Objects groups

cnsClkSelGlobalObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 1)
)
cnsClkSelGlobalObjectGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsClkSelGlobProcessMode"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobClockMode"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobNetsyncEnable"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobRevertiveMode"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobESMCMode"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobEECOption"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobNetworkOption"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobHoldoffTime"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobWtrTime"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobNofSources"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobLastHoldoverSeconds"),
        ("CISCO-NETSYNC-MIB", "cnsClkSelGlobCurrHoldoverSeconds"))
)
if mibBuilder.loadTexts:
    cnsClkSelGlobalObjectGroup.setStatus("current")

cnsSelectedInputSourceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 2)
)
cnsSelectedInputSourceObjectGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsSelInpSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcTimestamp"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcFSW"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcMSW"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcPriority"))
)
if mibBuilder.loadTexts:
    cnsSelectedInputSourceObjectGroup.setStatus("current")

cnsInputSourceObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 3)
)
cnsInputSourceObjectGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsInpSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcPriority"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcESMCCap"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcSSMCap"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcQualityLevelTxCfg"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcQualityLevelRxCfg"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcQualityLevelTx"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcQualityLevelRx"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcHoldoffTime"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcWtrTime"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcLockout"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcSignalFailure"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcAlarm"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcAlarmInfo"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcFSW"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcMSW"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcAlarmClear"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcFailClear"))
)
if mibBuilder.loadTexts:
    cnsInputSourceObjectGroup.setStatus("current")

cnsExtOutputObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 4)
)
cnsExtOutputObjectGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsExtOutName"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutSelNetsyncIndex"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutPriority"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutFSW"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutMSW"),
        ("CISCO-NETSYNC-MIB", "cnsExtOutSquelch"))
)
if mibBuilder.loadTexts:
    cnsExtOutputObjectGroup.setStatus("current")

cnsT4ClkSrcObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 5)
)
cnsT4ClkSrcObjectGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsT4ClkSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcPriority"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcESMCCap"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcSSMCap"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevelTxCfg"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevelRxCfg"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevelTx"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevelRx"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcHoldoffTime"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcWtrTime"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcLockout"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcSignalFailure"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcAlarm"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcAlarmInfo"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcFSW"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcMSW"))
)
if mibBuilder.loadTexts:
    cnsT4ClkSrcObjectGroup.setStatus("current")

cnsMIBNotifEnablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 6)
)
cnsMIBNotifEnablesGroup.setObjects(
    ("CISCO-NETSYNC-MIB", "cnsMIBEnableStatusNotification")
)
if mibBuilder.loadTexts:
    cnsMIBNotifEnablesGroup.setStatus("current")


# Notification objects

ciscoNetsyncSelectedT0Clock = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 0, 1)
)
ciscoNetsyncSelectedT0Clock.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsSelInpSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsSelInpSrcPriority"))
)
if mibBuilder.loadTexts:
    ciscoNetsyncSelectedT0Clock.setStatus(
        "current"
    )

ciscoNetsyncSelectedT4Clock = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 0, 2)
)
ciscoNetsyncSelectedT4Clock.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsExtOutName"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcQualityLevel"),
        ("CISCO-NETSYNC-MIB", "cnsT4ClkSrcPriority"))
)
if mibBuilder.loadTexts:
    ciscoNetsyncSelectedT4Clock.setStatus(
        "current"
    )

ciscoNetsyncInputSignalFailureStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 0, 3)
)
ciscoNetsyncInputSignalFailureStatus.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsInpSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcFailClear"))
)
if mibBuilder.loadTexts:
    ciscoNetsyncInputSignalFailureStatus.setStatus(
        "current"
    )

ciscoNetsyncInputAlarmStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 0, 4)
)
ciscoNetsyncInputAlarmStatus.setObjects(
      *(("CISCO-NETSYNC-MIB", "cnsInpSrcName"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcIntfType"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcAlarmInfo"),
        ("CISCO-NETSYNC-MIB", "cnsInpSrcAlarmClear"))
)
if mibBuilder.loadTexts:
    ciscoNetsyncInputAlarmStatus.setStatus(
        "current"
    )


# Notifications groups

ciscoNetsyncMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 2, 7)
)
ciscoNetsyncMIBNotificationGroup.setObjects(
      *(("CISCO-NETSYNC-MIB", "ciscoNetsyncSelectedT0Clock"),
        ("CISCO-NETSYNC-MIB", "ciscoNetsyncSelectedT4Clock"),
        ("CISCO-NETSYNC-MIB", "ciscoNetsyncInputSignalFailureStatus"),
        ("CISCO-NETSYNC-MIB", "ciscoNetsyncInputAlarmStatus"))
)
if mibBuilder.loadTexts:
    ciscoNetsyncMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoNetsyncMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 761, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoNetsyncMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-NETSYNC-MIB",
    **{"CiscoNetsyncIfType": CiscoNetsyncIfType,
       "CiscoNetsyncNetworkOption": CiscoNetsyncNetworkOption,
       "CiscoNetsyncEECOption": CiscoNetsyncEECOption,
       "CiscoNetsyncQLMode": CiscoNetsyncQLMode,
       "CiscoNetsyncClockMode": CiscoNetsyncClockMode,
       "CiscoNetsyncQualityLevel": CiscoNetsyncQualityLevel,
       "CiscoNetsyncSSMCap": CiscoNetsyncSSMCap,
       "CiscoNetsyncESMCCap": CiscoNetsyncESMCCap,
       "CiscoNetsyncAlarmInfo": CiscoNetsyncAlarmInfo,
       "ciscoNetsyncMIB": ciscoNetsyncMIB,
       "ciscoNetsyncMIBNotifs": ciscoNetsyncMIBNotifs,
       "ciscoNetsyncSelectedT0Clock": ciscoNetsyncSelectedT0Clock,
       "ciscoNetsyncSelectedT4Clock": ciscoNetsyncSelectedT4Clock,
       "ciscoNetsyncInputSignalFailureStatus": ciscoNetsyncInputSignalFailureStatus,
       "ciscoNetsyncInputAlarmStatus": ciscoNetsyncInputAlarmStatus,
       "ciscoNetsyncMIBObjects": ciscoNetsyncMIBObjects,
       "ciscoNetsyncMIBTables": ciscoNetsyncMIBTables,
       "cnsClkSelGlobalTable": cnsClkSelGlobalTable,
       "cnsClkSelGlobalEntry": cnsClkSelGlobalEntry,
       "cnsClkSelGloProcIndex": cnsClkSelGloProcIndex,
       "cnsClkSelGlobProcessMode": cnsClkSelGlobProcessMode,
       "cnsClkSelGlobClockMode": cnsClkSelGlobClockMode,
       "cnsClkSelGlobNetsyncEnable": cnsClkSelGlobNetsyncEnable,
       "cnsClkSelGlobRevertiveMode": cnsClkSelGlobRevertiveMode,
       "cnsClkSelGlobESMCMode": cnsClkSelGlobESMCMode,
       "cnsClkSelGlobEECOption": cnsClkSelGlobEECOption,
       "cnsClkSelGlobNetworkOption": cnsClkSelGlobNetworkOption,
       "cnsClkSelGlobHoldoffTime": cnsClkSelGlobHoldoffTime,
       "cnsClkSelGlobWtrTime": cnsClkSelGlobWtrTime,
       "cnsClkSelGlobNofSources": cnsClkSelGlobNofSources,
       "cnsClkSelGlobLastHoldoverSeconds": cnsClkSelGlobLastHoldoverSeconds,
       "cnsClkSelGlobCurrHoldoverSeconds": cnsClkSelGlobCurrHoldoverSeconds,
       "cnsSelectedInputSourceTable": cnsSelectedInputSourceTable,
       "cnsSelectedInputSourceEntry": cnsSelectedInputSourceEntry,
       "cnsSelInpSrcNetsyncIndex": cnsSelInpSrcNetsyncIndex,
       "cnsSelInpSrcName": cnsSelInpSrcName,
       "cnsSelInpSrcIntfType": cnsSelInpSrcIntfType,
       "cnsSelInpSrcQualityLevel": cnsSelInpSrcQualityLevel,
       "cnsSelInpSrcPriority": cnsSelInpSrcPriority,
       "cnsSelInpSrcTimestamp": cnsSelInpSrcTimestamp,
       "cnsSelInpSrcFSW": cnsSelInpSrcFSW,
       "cnsSelInpSrcMSW": cnsSelInpSrcMSW,
       "cnsInputSourceTable": cnsInputSourceTable,
       "cnsInputSourceEntry": cnsInputSourceEntry,
       "cnsInpSrcNetsyncIndex": cnsInpSrcNetsyncIndex,
       "cnsInpSrcName": cnsInpSrcName,
       "cnsInpSrcIntfType": cnsInpSrcIntfType,
       "cnsInpSrcPriority": cnsInpSrcPriority,
       "cnsInpSrcESMCCap": cnsInpSrcESMCCap,
       "cnsInpSrcSSMCap": cnsInpSrcSSMCap,
       "cnsInpSrcQualityLevelTxCfg": cnsInpSrcQualityLevelTxCfg,
       "cnsInpSrcQualityLevelRxCfg": cnsInpSrcQualityLevelRxCfg,
       "cnsInpSrcQualityLevelTx": cnsInpSrcQualityLevelTx,
       "cnsInpSrcQualityLevelRx": cnsInpSrcQualityLevelRx,
       "cnsInpSrcQualityLevel": cnsInpSrcQualityLevel,
       "cnsInpSrcHoldoffTime": cnsInpSrcHoldoffTime,
       "cnsInpSrcWtrTime": cnsInpSrcWtrTime,
       "cnsInpSrcLockout": cnsInpSrcLockout,
       "cnsInpSrcSignalFailure": cnsInpSrcSignalFailure,
       "cnsInpSrcAlarm": cnsInpSrcAlarm,
       "cnsInpSrcAlarmInfo": cnsInpSrcAlarmInfo,
       "cnsInpSrcFSW": cnsInpSrcFSW,
       "cnsInpSrcMSW": cnsInpSrcMSW,
       "cnsExtOutputTable": cnsExtOutputTable,
       "cnsExtOutputEntry": cnsExtOutputEntry,
       "cnsExtOutListIndex": cnsExtOutListIndex,
       "cnsExtOutSelNetsyncIndex": cnsExtOutSelNetsyncIndex,
       "cnsExtOutName": cnsExtOutName,
       "cnsExtOutIntfType": cnsExtOutIntfType,
       "cnsExtOutQualityLevel": cnsExtOutQualityLevel,
       "cnsExtOutPriority": cnsExtOutPriority,
       "cnsExtOutFSW": cnsExtOutFSW,
       "cnsExtOutMSW": cnsExtOutMSW,
       "cnsExtOutSquelch": cnsExtOutSquelch,
       "cnsT4ClockSourceTable": cnsT4ClockSourceTable,
       "cnsT4ClockSourceEntry": cnsT4ClockSourceEntry,
       "cnsT4ClkSrcNetsyncIndex": cnsT4ClkSrcNetsyncIndex,
       "cnsT4ClkSrcName": cnsT4ClkSrcName,
       "cnsT4ClkSrcIntfType": cnsT4ClkSrcIntfType,
       "cnsT4ClkSrcPriority": cnsT4ClkSrcPriority,
       "cnsT4ClkSrcESMCCap": cnsT4ClkSrcESMCCap,
       "cnsT4ClkSrcSSMCap": cnsT4ClkSrcSSMCap,
       "cnsT4ClkSrcQualityLevelTxCfg": cnsT4ClkSrcQualityLevelTxCfg,
       "cnsT4ClkSrcQualityLevelRxCfg": cnsT4ClkSrcQualityLevelRxCfg,
       "cnsT4ClkSrcQualityLevelTx": cnsT4ClkSrcQualityLevelTx,
       "cnsT4ClkSrcQualityLevelRx": cnsT4ClkSrcQualityLevelRx,
       "cnsT4ClkSrcQualityLevel": cnsT4ClkSrcQualityLevel,
       "cnsT4ClkSrcHoldoffTime": cnsT4ClkSrcHoldoffTime,
       "cnsT4ClkSrcWtrTime": cnsT4ClkSrcWtrTime,
       "cnsT4ClkSrcLockout": cnsT4ClkSrcLockout,
       "cnsT4ClkSrcSignalFailure": cnsT4ClkSrcSignalFailure,
       "cnsT4ClkSrcAlarm": cnsT4ClkSrcAlarm,
       "cnsT4ClkSrcAlarmInfo": cnsT4ClkSrcAlarmInfo,
       "cnsT4ClkSrcFSW": cnsT4ClkSrcFSW,
       "cnsT4ClkSrcMSW": cnsT4ClkSrcMSW,
       "cnsNotifObjects": cnsNotifObjects,
       "cnsInpSrcFailClear": cnsInpSrcFailClear,
       "cnsInpSrcAlarmClear": cnsInpSrcAlarmClear,
       "ciscoNetsyncMIBNotifControl": ciscoNetsyncMIBNotifControl,
       "cnsMIBEnableStatusNotification": cnsMIBEnableStatusNotification,
       "ciscoNetsyncMIBConform": ciscoNetsyncMIBConform,
       "ciscoNetsyncMIBCompliances": ciscoNetsyncMIBCompliances,
       "ciscoNetsyncMIBCompliance": ciscoNetsyncMIBCompliance,
       "ciscoNetsyncMIBGroups": ciscoNetsyncMIBGroups,
       "cnsClkSelGlobalObjectGroup": cnsClkSelGlobalObjectGroup,
       "cnsSelectedInputSourceObjectGroup": cnsSelectedInputSourceObjectGroup,
       "cnsInputSourceObjectGroup": cnsInputSourceObjectGroup,
       "cnsExtOutputObjectGroup": cnsExtOutputObjectGroup,
       "cnsT4ClkSrcObjectGroup": cnsT4ClkSrcObjectGroup,
       "cnsMIBNotifEnablesGroup": cnsMIBNotifEnablesGroup,
       "ciscoNetsyncMIBNotificationGroup": ciscoNetsyncMIBNotificationGroup}
)
