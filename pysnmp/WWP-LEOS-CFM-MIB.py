# SNMP MIB module (WWP-LEOS-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-CFM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:47 2024
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosCfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35)
)
wwpLeosCfmMIB.setRevisions(
        ("2012-04-11 00:00",
         "2012-02-03 00:00",
         "2011-07-26 00:00",
         "2011-05-31 00:00",
         "2011-01-31 00:00",
         "2010-07-15 00:00",
         "2009-11-16 00:00",
         "2009-09-04 17:00",
         "2009-08-06 19:00",
         "2009-07-30 19:00",
         "2008-11-14 17:00",
         "2008-10-23 17:00",
         "2007-10-24 17:00",
         "2006-04-18 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmMAID(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )



class CfmDisplayString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )



class EthType(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )



class SendState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 3),
          ("clear", 2),
          ("none", 99),
          ("send", 1))
    )



class Dot1agCfmMaintDomainNameType(Integer32, TextualConvention):
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
        *(("charString", 4),
          ("dnsLikeName", 2),
          ("macAddressAndUint", 3),
          ("none", 1))
    )



class Dot1agCfmMaintDomainName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 43),
    )



class Dot1agCfmMaintAssocNameType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("charString", 2),
          ("iccBased", 32),
          ("primaryVid", 1),
          ("rfc2865VpnId", 4),
          ("unsignedInt16", 3))
    )



class Dot1agCfmMaintAssocName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 45),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosCfmMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosCfmMIBObjects = _WwpLeosCfmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1)
)
_WwpLeosCfmGlobal_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobal = _WwpLeosCfmGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1)
)


class _WwpLeosCfmState_Type(Integer32):
    """Custom type wwpLeosCfmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmState_Type.__name__ = "Integer32"
_WwpLeosCfmState_Object = MibScalar
wwpLeosCfmState = _WwpLeosCfmState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 1),
    _WwpLeosCfmState_Type()
)
wwpLeosCfmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmState.setStatus("current")
_WwpLeosCfmEtherType_Type = EthType
_WwpLeosCfmEtherType_Object = MibScalar
wwpLeosCfmEtherType = _WwpLeosCfmEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 2),
    _WwpLeosCfmEtherType_Type()
)
wwpLeosCfmEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmEtherType.setStatus("current")
_WwpLeosCfmMEPHoldTime_Type = Integer32
_WwpLeosCfmMEPHoldTime_Object = MibScalar
wwpLeosCfmMEPHoldTime = _WwpLeosCfmMEPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 3),
    _WwpLeosCfmMEPHoldTime_Type()
)
wwpLeosCfmMEPHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPHoldTime.setStatus("current")
_WwpLeosCfmCcmAvailable_Type = Counter32
_WwpLeosCfmCcmAvailable_Object = MibScalar
wwpLeosCfmCcmAvailable = _WwpLeosCfmCcmAvailable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 4),
    _WwpLeosCfmCcmAvailable_Type()
)
wwpLeosCfmCcmAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmCcmAvailable.setStatus("current")
_WwpLeosCfmY1731EtherType_Type = EthType
_WwpLeosCfmY1731EtherType_Object = MibScalar
wwpLeosCfmY1731EtherType = _WwpLeosCfmY1731EtherType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 5),
    _WwpLeosCfmY1731EtherType_Type()
)
wwpLeosCfmY1731EtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmY1731EtherType.setStatus("current")


class _WwpLeosCfmL2LoopDetectState_Type(Integer32):
    """Custom type wwpLeosCfmL2LoopDetectState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WwpLeosCfmL2LoopDetectState_Type.__name__ = "Integer32"
_WwpLeosCfmL2LoopDetectState_Object = MibScalar
wwpLeosCfmL2LoopDetectState = _WwpLeosCfmL2LoopDetectState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 6),
    _WwpLeosCfmL2LoopDetectState_Type()
)
wwpLeosCfmL2LoopDetectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmL2LoopDetectState.setStatus("current")


class _WwpLeosCfmDot1adStrict_Type(Integer32):
    """Custom type wwpLeosCfmDot1adStrict based on Integer32"""
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


_WwpLeosCfmDot1adStrict_Type.__name__ = "Integer32"
_WwpLeosCfmDot1adStrict_Object = MibScalar
wwpLeosCfmDot1adStrict = _WwpLeosCfmDot1adStrict_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 7),
    _WwpLeosCfmDot1adStrict_Type()
)
wwpLeosCfmDot1adStrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmDot1adStrict.setStatus("current")


class _WwpLeosCfmMipLevelEnforcement_Type(Integer32):
    """Custom type wwpLeosCfmMipLevelEnforcement based on Integer32"""
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


_WwpLeosCfmMipLevelEnforcement_Type.__name__ = "Integer32"
_WwpLeosCfmMipLevelEnforcement_Object = MibScalar
wwpLeosCfmMipLevelEnforcement = _WwpLeosCfmMipLevelEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 8),
    _WwpLeosCfmMipLevelEnforcement_Type()
)
wwpLeosCfmMipLevelEnforcement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMipLevelEnforcement.setStatus("current")


class _WwpLeosCfmMipCcmDbState_Type(Integer32):
    """Custom type wwpLeosCfmMipCcmDbState based on Integer32"""
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


_WwpLeosCfmMipCcmDbState_Type.__name__ = "Integer32"
_WwpLeosCfmMipCcmDbState_Object = MibScalar
wwpLeosCfmMipCcmDbState = _WwpLeosCfmMipCcmDbState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 9),
    _WwpLeosCfmMipCcmDbState_Type()
)
wwpLeosCfmMipCcmDbState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCcmDbState.setStatus("current")
_WwpLeosCfmLBMDefaultCount_Type = Integer32
_WwpLeosCfmLBMDefaultCount_Object = MibScalar
wwpLeosCfmLBMDefaultCount = _WwpLeosCfmLBMDefaultCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 10),
    _WwpLeosCfmLBMDefaultCount_Type()
)
wwpLeosCfmLBMDefaultCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmLBMDefaultCount.setStatus("deprecated")
_WwpLeosCfmLBMDefaultInterval_Type = Integer32
_WwpLeosCfmLBMDefaultInterval_Object = MibScalar
wwpLeosCfmLBMDefaultInterval = _WwpLeosCfmLBMDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 11),
    _WwpLeosCfmLBMDefaultInterval_Type()
)
wwpLeosCfmLBMDefaultInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmLBMDefaultInterval.setStatus("deprecated")
_WwpLeosCfmLBMDefaultTimeout_Type = Integer32
_WwpLeosCfmLBMDefaultTimeout_Object = MibScalar
wwpLeosCfmLBMDefaultTimeout = _WwpLeosCfmLBMDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 12),
    _WwpLeosCfmLBMDefaultTimeout_Type()
)
wwpLeosCfmLBMDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmLBMDefaultTimeout.setStatus("deprecated")


class _WwpLeosCfmFrameClassifierMode_Type(Integer32):
    """Custom type wwpLeosCfmFrameClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etype", 1),
          ("etypeMd", 2))
    )


_WwpLeosCfmFrameClassifierMode_Type.__name__ = "Integer32"
_WwpLeosCfmFrameClassifierMode_Object = MibScalar
wwpLeosCfmFrameClassifierMode = _WwpLeosCfmFrameClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 13),
    _WwpLeosCfmFrameClassifierMode_Type()
)
wwpLeosCfmFrameClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameClassifierMode.setStatus("deprecated")
_WwpLeosCfmGlobalLBMDefaultCount_Type = Integer32
_WwpLeosCfmGlobalLBMDefaultCount_Object = MibScalar
wwpLeosCfmGlobalLBMDefaultCount = _WwpLeosCfmGlobalLBMDefaultCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 16),
    _WwpLeosCfmGlobalLBMDefaultCount_Type()
)
wwpLeosCfmGlobalLBMDefaultCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLBMDefaultCount.setStatus("current")
_WwpLeosCfmGlobalLBMDefaultInterval_Type = Integer32
_WwpLeosCfmGlobalLBMDefaultInterval_Object = MibScalar
wwpLeosCfmGlobalLBMDefaultInterval = _WwpLeosCfmGlobalLBMDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 17),
    _WwpLeosCfmGlobalLBMDefaultInterval_Type()
)
wwpLeosCfmGlobalLBMDefaultInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLBMDefaultInterval.setStatus("current")
_WwpLeosCfmGlobalLBMDefaultTimeout_Type = Integer32
_WwpLeosCfmGlobalLBMDefaultTimeout_Object = MibScalar
wwpLeosCfmGlobalLBMDefaultTimeout = _WwpLeosCfmGlobalLBMDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 18),
    _WwpLeosCfmGlobalLBMDefaultTimeout_Type()
)
wwpLeosCfmGlobalLBMDefaultTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLBMDefaultTimeout.setStatus("current")


class _WwpLeosCfmGlobalFrameClassifierMode_Type(Integer32):
    """Custom type wwpLeosCfmGlobalFrameClassifierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("etype", 1),
          ("etypeMd", 2))
    )


_WwpLeosCfmGlobalFrameClassifierMode_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalFrameClassifierMode_Object = MibScalar
wwpLeosCfmGlobalFrameClassifierMode = _WwpLeosCfmGlobalFrameClassifierMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 19),
    _WwpLeosCfmGlobalFrameClassifierMode_Type()
)
wwpLeosCfmGlobalFrameClassifierMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameClassifierMode.setStatus("current")
_WwpLeosCfmGlobalFrameBudget_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalFrameBudget = _WwpLeosCfmGlobalFrameBudget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24)
)
_WwpLeosCfmGlobalControlModuleFrameBudget_Type = Counter32
_WwpLeosCfmGlobalControlModuleFrameBudget_Object = MibScalar
wwpLeosCfmGlobalControlModuleFrameBudget = _WwpLeosCfmGlobalControlModuleFrameBudget_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24, 1),
    _WwpLeosCfmGlobalControlModuleFrameBudget_Type()
)
wwpLeosCfmGlobalControlModuleFrameBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalControlModuleFrameBudget.setStatus("current")
_WwpLeosCfmGlobalFrameBudgetTable_Object = MibTable
wwpLeosCfmGlobalFrameBudgetTable = _WwpLeosCfmGlobalFrameBudgetTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24, 2)
)
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameBudgetTable.setStatus("current")
_WwpLeosCfmGlobalFrameBudgetEntry_Object = MibTableRow
wwpLeosCfmGlobalFrameBudgetEntry = _WwpLeosCfmGlobalFrameBudgetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24, 2, 1)
)
wwpLeosCfmGlobalFrameBudgetEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmGlobalFrameBudgetSlotIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameBudgetEntry.setStatus("current")
_WwpLeosCfmGlobalFrameBudgetSlotIndex_Type = Unsigned32
_WwpLeosCfmGlobalFrameBudgetSlotIndex_Object = MibTableColumn
wwpLeosCfmGlobalFrameBudgetSlotIndex = _WwpLeosCfmGlobalFrameBudgetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24, 2, 1, 1),
    _WwpLeosCfmGlobalFrameBudgetSlotIndex_Type()
)
wwpLeosCfmGlobalFrameBudgetSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameBudgetSlotIndex.setStatus("current")
_WwpLeosCfmGlobalFrameBudgetValue_Type = Counter32
_WwpLeosCfmGlobalFrameBudgetValue_Object = MibTableColumn
wwpLeosCfmGlobalFrameBudgetValue = _WwpLeosCfmGlobalFrameBudgetValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 24, 2, 1, 2),
    _WwpLeosCfmGlobalFrameBudgetValue_Type()
)
wwpLeosCfmGlobalFrameBudgetValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameBudgetValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalFrameBudgetValue.setUnits("frames/sec")
_WwpLeosCfmGlobalStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalStats = _WwpLeosCfmGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25)
)
_WwpLeosCfmStatsTotalTx_Type = Counter64
_WwpLeosCfmStatsTotalTx_Object = MibScalar
wwpLeosCfmStatsTotalTx = _WwpLeosCfmStatsTotalTx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 1),
    _WwpLeosCfmStatsTotalTx_Type()
)
wwpLeosCfmStatsTotalTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsTotalTx.setStatus("current")
_WwpLeosCfmStatsTotalRx_Type = Counter64
_WwpLeosCfmStatsTotalRx_Object = MibScalar
wwpLeosCfmStatsTotalRx = _WwpLeosCfmStatsTotalRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 2),
    _WwpLeosCfmStatsTotalRx_Type()
)
wwpLeosCfmStatsTotalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsTotalRx.setStatus("current")
_WwpLeosCfmStatsTxFloodedFrames_Type = Counter64
_WwpLeosCfmStatsTxFloodedFrames_Object = MibScalar
wwpLeosCfmStatsTxFloodedFrames = _WwpLeosCfmStatsTxFloodedFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 3),
    _WwpLeosCfmStatsTxFloodedFrames_Type()
)
wwpLeosCfmStatsTxFloodedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsTxFloodedFrames.setStatus("current")
_WwpLeosCfmStatsTxFloodedIgnoredStpState_Type = Counter64
_WwpLeosCfmStatsTxFloodedIgnoredStpState_Object = MibScalar
wwpLeosCfmStatsTxFloodedIgnoredStpState = _WwpLeosCfmStatsTxFloodedIgnoredStpState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 4),
    _WwpLeosCfmStatsTxFloodedIgnoredStpState_Type()
)
wwpLeosCfmStatsTxFloodedIgnoredStpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsTxFloodedIgnoredStpState.setStatus("current")
_WwpLeosCfmStatsRxTotalValidFrames_Type = Counter64
_WwpLeosCfmStatsRxTotalValidFrames_Object = MibScalar
wwpLeosCfmStatsRxTotalValidFrames = _WwpLeosCfmStatsRxTotalValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 5),
    _WwpLeosCfmStatsRxTotalValidFrames_Type()
)
wwpLeosCfmStatsRxTotalValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsRxTotalValidFrames.setStatus("current")
_WwpLeosCfmStatsRxTotalNotValidatedFrames_Type = Counter64
_WwpLeosCfmStatsRxTotalNotValidatedFrames_Object = MibScalar
wwpLeosCfmStatsRxTotalNotValidatedFrames = _WwpLeosCfmStatsRxTotalNotValidatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 6),
    _WwpLeosCfmStatsRxTotalNotValidatedFrames_Type()
)
wwpLeosCfmStatsRxTotalNotValidatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsRxTotalNotValidatedFrames.setStatus("current")
_WwpLeosCfmStatsRxTotalInValidFrames_Type = Counter64
_WwpLeosCfmStatsRxTotalInValidFrames_Object = MibScalar
wwpLeosCfmStatsRxTotalInValidFrames = _WwpLeosCfmStatsRxTotalInValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 7),
    _WwpLeosCfmStatsRxTotalInValidFrames_Type()
)
wwpLeosCfmStatsRxTotalInValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmStatsRxTotalInValidFrames.setStatus("current")
_WwpLeosCfmTotalRxInvalidMessageOverflow_Type = Counter64
_WwpLeosCfmTotalRxInvalidMessageOverflow_Object = MibScalar
wwpLeosCfmTotalRxInvalidMessageOverflow = _WwpLeosCfmTotalRxInvalidMessageOverflow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 8),
    _WwpLeosCfmTotalRxInvalidMessageOverflow_Type()
)
wwpLeosCfmTotalRxInvalidMessageOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidMessageOverflow.setStatus("current")
_WwpLeosCfmTotalRxInvalidPortStatusTLV_Type = Counter64
_WwpLeosCfmTotalRxInvalidPortStatusTLV_Object = MibScalar
wwpLeosCfmTotalRxInvalidPortStatusTLV = _WwpLeosCfmTotalRxInvalidPortStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 9),
    _WwpLeosCfmTotalRxInvalidPortStatusTLV_Type()
)
wwpLeosCfmTotalRxInvalidPortStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidPortStatusTLV.setStatus("current")
_WwpLeosCfmTotalRxInvalidInterfaceStatusTLV_Type = Counter64
_WwpLeosCfmTotalRxInvalidInterfaceStatusTLV_Object = MibScalar
wwpLeosCfmTotalRxInvalidInterfaceStatusTLV = _WwpLeosCfmTotalRxInvalidInterfaceStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 10),
    _WwpLeosCfmTotalRxInvalidInterfaceStatusTLV_Type()
)
wwpLeosCfmTotalRxInvalidInterfaceStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidInterfaceStatusTLV.setStatus("current")
_WwpLeosCfmTotalRxInvalidSenderIDTLV_Type = Counter64
_WwpLeosCfmTotalRxInvalidSenderIDTLV_Object = MibScalar
wwpLeosCfmTotalRxInvalidSenderIDTLV = _WwpLeosCfmTotalRxInvalidSenderIDTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 11),
    _WwpLeosCfmTotalRxInvalidSenderIDTLV_Type()
)
wwpLeosCfmTotalRxInvalidSenderIDTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidSenderIDTLV.setStatus("current")
_WwpLeosCfmRxAdminDisableDropped_Type = Counter64
_WwpLeosCfmRxAdminDisableDropped_Object = MibScalar
wwpLeosCfmRxAdminDisableDropped = _WwpLeosCfmRxAdminDisableDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 12),
    _WwpLeosCfmRxAdminDisableDropped_Type()
)
wwpLeosCfmRxAdminDisableDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRxAdminDisableDropped.setStatus("current")
_WwpLesoCfmRxInvalidEtypeDropped_Type = Counter64
_WwpLesoCfmRxInvalidEtypeDropped_Object = MibScalar
wwpLesoCfmRxInvalidEtypeDropped = _WwpLesoCfmRxInvalidEtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 13),
    _WwpLesoCfmRxInvalidEtypeDropped_Type()
)
wwpLesoCfmRxInvalidEtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLesoCfmRxInvalidEtypeDropped.setStatus("current")
_WwpLeosCfmRxInvalidOpCodeDropped_Type = Counter64
_WwpLeosCfmRxInvalidOpCodeDropped_Object = MibScalar
wwpLeosCfmRxInvalidOpCodeDropped = _WwpLeosCfmRxInvalidOpCodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 14),
    _WwpLeosCfmRxInvalidOpCodeDropped_Type()
)
wwpLeosCfmRxInvalidOpCodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRxInvalidOpCodeDropped.setStatus("current")
_WwpLeosCfmRxSTPStateNotForwardingDropped_Type = Counter64
_WwpLeosCfmRxSTPStateNotForwardingDropped_Object = MibScalar
wwpLeosCfmRxSTPStateNotForwardingDropped = _WwpLeosCfmRxSTPStateNotForwardingDropped_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 15),
    _WwpLeosCfmRxSTPStateNotForwardingDropped_Type()
)
wwpLeosCfmRxSTPStateNotForwardingDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRxSTPStateNotForwardingDropped.setStatus("current")


class _WwpLeosCfmGlobalStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmGlobalStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmGlobalStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalStatsClear_Object = MibScalar
wwpLeosCfmGlobalStatsClear = _WwpLeosCfmGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 16),
    _WwpLeosCfmGlobalStatsClear_Type()
)
wwpLeosCfmGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalStatsClear.setStatus("current")


class _WwpLeosCfmGlobalLoopbackMsgStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmGlobalLoopbackMsgStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmGlobalLoopbackMsgStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalLoopbackMsgStatsClear_Object = MibScalar
wwpLeosCfmGlobalLoopbackMsgStatsClear = _WwpLeosCfmGlobalLoopbackMsgStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 17),
    _WwpLeosCfmGlobalLoopbackMsgStatsClear_Type()
)
wwpLeosCfmGlobalLoopbackMsgStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLoopbackMsgStatsClear.setStatus("current")


class _WwpLeosCfmGlobalLinkTraceMsgStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmGlobalLinkTraceMsgStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmGlobalLinkTraceMsgStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalLinkTraceMsgStatsClear_Object = MibScalar
wwpLeosCfmGlobalLinkTraceMsgStatsClear = _WwpLeosCfmGlobalLinkTraceMsgStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 18),
    _WwpLeosCfmGlobalLinkTraceMsgStatsClear_Type()
)
wwpLeosCfmGlobalLinkTraceMsgStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLinkTraceMsgStatsClear.setStatus("current")


class _WwpLeosCfmGlobalDelayMeasurementMsgStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmGlobalDelayMeasurementMsgStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmGlobalDelayMeasurementMsgStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalDelayMeasurementMsgStatsClear_Object = MibScalar
wwpLeosCfmGlobalDelayMeasurementMsgStatsClear = _WwpLeosCfmGlobalDelayMeasurementMsgStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 19),
    _WwpLeosCfmGlobalDelayMeasurementMsgStatsClear_Type()
)
wwpLeosCfmGlobalDelayMeasurementMsgStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalDelayMeasurementMsgStatsClear.setStatus("current")


class _WwpLeosCfmGlobalLossMeasurementMsgStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmGlobalLossMeasurementMsgStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmGlobalLossMeasurementMsgStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmGlobalLossMeasurementMsgStatsClear_Object = MibScalar
wwpLeosCfmGlobalLossMeasurementMsgStatsClear = _WwpLeosCfmGlobalLossMeasurementMsgStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 20),
    _WwpLeosCfmGlobalLossMeasurementMsgStatsClear_Type()
)
wwpLeosCfmGlobalLossMeasurementMsgStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmGlobalLossMeasurementMsgStatsClear.setStatus("current")
_WwpLeosCfmTotalRxDropBlockedOppositeMep_Type = Counter64
_WwpLeosCfmTotalRxDropBlockedOppositeMep_Object = MibScalar
wwpLeosCfmTotalRxDropBlockedOppositeMep = _WwpLeosCfmTotalRxDropBlockedOppositeMep_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 21),
    _WwpLeosCfmTotalRxDropBlockedOppositeMep_Type()
)
wwpLeosCfmTotalRxDropBlockedOppositeMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxDropBlockedOppositeMep.setStatus("current")
_WwpLeosCfmGlobalCCMStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalCCMStats = _WwpLeosCfmGlobalCCMStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26)
)
_WwpLeosCfmTotalTxCCM_Type = Counter64
_WwpLeosCfmTotalTxCCM_Object = MibScalar
wwpLeosCfmTotalTxCCM = _WwpLeosCfmTotalTxCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 1),
    _WwpLeosCfmTotalTxCCM_Type()
)
wwpLeosCfmTotalTxCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxCCM.setStatus("current")
_WwpLeosCfmTotalTxCCMFlooded_Type = Counter64
_WwpLeosCfmTotalTxCCMFlooded_Object = MibScalar
wwpLeosCfmTotalTxCCMFlooded = _WwpLeosCfmTotalTxCCMFlooded_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 2),
    _WwpLeosCfmTotalTxCCMFlooded_Type()
)
wwpLeosCfmTotalTxCCMFlooded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxCCMFlooded.setStatus("current")
_WwpLeosCfmTotalRxValidCCM_Type = Counter64
_WwpLeosCfmTotalRxValidCCM_Object = MibScalar
wwpLeosCfmTotalRxValidCCM = _WwpLeosCfmTotalRxValidCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 3),
    _WwpLeosCfmTotalRxValidCCM_Type()
)
wwpLeosCfmTotalRxValidCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxValidCCM.setStatus("current")
_WwpLeosCfmTotalRxCCMInSequence_Type = Counter64
_WwpLeosCfmTotalRxCCMInSequence_Object = MibScalar
wwpLeosCfmTotalRxCCMInSequence = _WwpLeosCfmTotalRxCCMInSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 4),
    _WwpLeosCfmTotalRxCCMInSequence_Type()
)
wwpLeosCfmTotalRxCCMInSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxCCMInSequence.setStatus("current")
_WwpLeosCfmTotalRxCCMSequenceError_Type = Counter64
_WwpLeosCfmTotalRxCCMSequenceError_Object = MibScalar
wwpLeosCfmTotalRxCCMSequenceError = _WwpLeosCfmTotalRxCCMSequenceError_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 5),
    _WwpLeosCfmTotalRxCCMSequenceError_Type()
)
wwpLeosCfmTotalRxCCMSequenceError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxCCMSequenceError.setStatus("current")
_WwpLeosCfmTotalCCMRxMDLevelXcon_Type = Counter64
_WwpLeosCfmTotalCCMRxMDLevelXcon_Object = MibScalar
wwpLeosCfmTotalCCMRxMDLevelXcon = _WwpLeosCfmTotalCCMRxMDLevelXcon_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 6),
    _WwpLeosCfmTotalCCMRxMDLevelXcon_Type()
)
wwpLeosCfmTotalCCMRxMDLevelXcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalCCMRxMDLevelXcon.setStatus("current")
_WwpLeosCfmTotalCCMRxMAIDXcon_Type = Counter64
_WwpLeosCfmTotalCCMRxMAIDXcon_Object = MibScalar
wwpLeosCfmTotalCCMRxMAIDXcon = _WwpLeosCfmTotalCCMRxMAIDXcon_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 7),
    _WwpLeosCfmTotalCCMRxMAIDXcon_Type()
)
wwpLeosCfmTotalCCMRxMAIDXcon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalCCMRxMAIDXcon.setStatus("current")
_WwpLeosCfmTotalRxCCMErrorOnMepId_Type = Counter64
_WwpLeosCfmTotalRxCCMErrorOnMepId_Object = MibScalar
wwpLeosCfmTotalRxCCMErrorOnMepId = _WwpLeosCfmTotalRxCCMErrorOnMepId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 8),
    _WwpLeosCfmTotalRxCCMErrorOnMepId_Type()
)
wwpLeosCfmTotalRxCCMErrorOnMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxCCMErrorOnMepId.setStatus("current")
_WwpLeosCfmTotalRxCCMIntervalError_Type = Counter64
_WwpLeosCfmTotalRxCCMIntervalError_Object = MibScalar
wwpLeosCfmTotalRxCCMIntervalError = _WwpLeosCfmTotalRxCCMIntervalError_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 9),
    _WwpLeosCfmTotalRxCCMIntervalError_Type()
)
wwpLeosCfmTotalRxCCMIntervalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxCCMIntervalError.setStatus("current")
_WwpLeosCfmTotalRxInvalidCCM_Type = Counter64
_WwpLeosCfmTotalRxInvalidCCM_Object = MibScalar
wwpLeosCfmTotalRxInvalidCCM = _WwpLeosCfmTotalRxInvalidCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 26, 10),
    _WwpLeosCfmTotalRxInvalidCCM_Type()
)
wwpLeosCfmTotalRxInvalidCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidCCM.setStatus("current")
_WwpLeosCfmGlobalLoopbackStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalLoopbackStats = _WwpLeosCfmGlobalLoopbackStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27)
)
_WwpLeosCfmTotalTxLBM_Type = Counter64
_WwpLeosCfmTotalTxLBM_Object = MibScalar
wwpLeosCfmTotalTxLBM = _WwpLeosCfmTotalTxLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 1),
    _WwpLeosCfmTotalTxLBM_Type()
)
wwpLeosCfmTotalTxLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLBM.setStatus("current")
_WwpLeosCfmTotalTxLBR_Type = Counter64
_WwpLeosCfmTotalTxLBR_Object = MibScalar
wwpLeosCfmTotalTxLBR = _WwpLeosCfmTotalTxLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 2),
    _WwpLeosCfmTotalTxLBR_Type()
)
wwpLeosCfmTotalTxLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLBR.setStatus("current")
_WwpLeosCfmTotalRxInOderLBR_Type = Counter64
_WwpLeosCfmTotalRxInOderLBR_Object = MibScalar
wwpLeosCfmTotalRxInOderLBR = _WwpLeosCfmTotalRxInOderLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 3),
    _WwpLeosCfmTotalRxInOderLBR_Type()
)
wwpLeosCfmTotalRxInOderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInOderLBR.setStatus("current")
_WwpLeosCfmTotalRxOOOLBR_Type = Counter64
_WwpLeosCfmTotalRxOOOLBR_Object = MibScalar
wwpLeosCfmTotalRxOOOLBR = _WwpLeosCfmTotalRxOOOLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 4),
    _WwpLeosCfmTotalRxOOOLBR_Type()
)
wwpLeosCfmTotalRxOOOLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxOOOLBR.setStatus("current")
_WwpLeosCfmTotalRxContentMismatchLBR_Type = Counter64
_WwpLeosCfmTotalRxContentMismatchLBR_Object = MibScalar
wwpLeosCfmTotalRxContentMismatchLBR = _WwpLeosCfmTotalRxContentMismatchLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 5),
    _WwpLeosCfmTotalRxContentMismatchLBR_Type()
)
wwpLeosCfmTotalRxContentMismatchLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxContentMismatchLBR.setStatus("current")
_WwpLeosCfmTotalRxUnexpectedLBR_Type = Counter64
_WwpLeosCfmTotalRxUnexpectedLBR_Object = MibScalar
wwpLeosCfmTotalRxUnexpectedLBR = _WwpLeosCfmTotalRxUnexpectedLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 6),
    _WwpLeosCfmTotalRxUnexpectedLBR_Type()
)
wwpLeosCfmTotalRxUnexpectedLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxUnexpectedLBR.setStatus("current")
_WwpLeosCfmTotalRxInvalidLBR_Type = Counter64
_WwpLeosCfmTotalRxInvalidLBR_Object = MibScalar
wwpLeosCfmTotalRxInvalidLBR = _WwpLeosCfmTotalRxInvalidLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 7),
    _WwpLeosCfmTotalRxInvalidLBR_Type()
)
wwpLeosCfmTotalRxInvalidLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidLBR.setStatus("current")
_WwpLeosCfmTotalRxvalidLBM_Type = Counter64
_WwpLeosCfmTotalRxvalidLBM_Object = MibScalar
wwpLeosCfmTotalRxvalidLBM = _WwpLeosCfmTotalRxvalidLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 8),
    _WwpLeosCfmTotalRxvalidLBM_Type()
)
wwpLeosCfmTotalRxvalidLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxvalidLBM.setStatus("current")
_WwpLeosCfmTotalRxInvalidLBM_Type = Counter64
_WwpLeosCfmTotalRxInvalidLBM_Object = MibScalar
wwpLeosCfmTotalRxInvalidLBM = _WwpLeosCfmTotalRxInvalidLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 27, 9),
    _WwpLeosCfmTotalRxInvalidLBM_Type()
)
wwpLeosCfmTotalRxInvalidLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidLBM.setStatus("current")
_WwpLeosCfmGlobalLinkTraceStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalLinkTraceStats = _WwpLeosCfmGlobalLinkTraceStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28)
)
_WwpLeosCfmTotalTxLTM_Type = Counter64
_WwpLeosCfmTotalTxLTM_Object = MibScalar
wwpLeosCfmTotalTxLTM = _WwpLeosCfmTotalTxLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 1),
    _WwpLeosCfmTotalTxLTM_Type()
)
wwpLeosCfmTotalTxLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLTM.setStatus("current")
_WwpLeosCfmTotalTxLTR_Type = Counter64
_WwpLeosCfmTotalTxLTR_Object = MibScalar
wwpLeosCfmTotalTxLTR = _WwpLeosCfmTotalTxLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 2),
    _WwpLeosCfmTotalTxLTR_Type()
)
wwpLeosCfmTotalTxLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLTR.setStatus("current")
_WwpLeosCfmTotalRxValidLTM_Type = Counter64
_WwpLeosCfmTotalRxValidLTM_Object = MibScalar
wwpLeosCfmTotalRxValidLTM = _WwpLeosCfmTotalRxValidLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 3),
    _WwpLeosCfmTotalRxValidLTM_Type()
)
wwpLeosCfmTotalRxValidLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxValidLTM.setStatus("current")
_WwpLeosCfmTotalRxValidLTR_Type = Counter64
_WwpLeosCfmTotalRxValidLTR_Object = MibScalar
wwpLeosCfmTotalRxValidLTR = _WwpLeosCfmTotalRxValidLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 4),
    _WwpLeosCfmTotalRxValidLTR_Type()
)
wwpLeosCfmTotalRxValidLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxValidLTR.setStatus("current")
_WwpLeosCfmTotalRxUnexpectedLTR_Type = Counter64
_WwpLeosCfmTotalRxUnexpectedLTR_Object = MibScalar
wwpLeosCfmTotalRxUnexpectedLTR = _WwpLeosCfmTotalRxUnexpectedLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 5),
    _WwpLeosCfmTotalRxUnexpectedLTR_Type()
)
wwpLeosCfmTotalRxUnexpectedLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxUnexpectedLTR.setStatus("current")
_WwpLeosCfmTotalRxInvalidLTR_Type = Counter64
_WwpLeosCfmTotalRxInvalidLTR_Object = MibScalar
wwpLeosCfmTotalRxInvalidLTR = _WwpLeosCfmTotalRxInvalidLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 6),
    _WwpLeosCfmTotalRxInvalidLTR_Type()
)
wwpLeosCfmTotalRxInvalidLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidLTR.setStatus("current")
_WwpLeosCfmInvalidLTRRelayAction_Type = Counter64
_WwpLeosCfmInvalidLTRRelayAction_Object = MibScalar
wwpLeosCfmInvalidLTRRelayAction = _WwpLeosCfmInvalidLTRRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 7),
    _WwpLeosCfmInvalidLTRRelayAction_Type()
)
wwpLeosCfmInvalidLTRRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmInvalidLTRRelayAction.setStatus("current")
_WwpLeosCfmTotalRxInvalidLTM_Type = Counter64
_WwpLeosCfmTotalRxInvalidLTM_Object = MibScalar
wwpLeosCfmTotalRxInvalidLTM = _WwpLeosCfmTotalRxInvalidLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 8),
    _WwpLeosCfmTotalRxInvalidLTM_Type()
)
wwpLeosCfmTotalRxInvalidLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxInvalidLTM.setStatus("current")
_WwpLeosCfmRxUnresolvedLTM_Type = Counter64
_WwpLeosCfmRxUnresolvedLTM_Object = MibScalar
wwpLeosCfmRxUnresolvedLTM = _WwpLeosCfmRxUnresolvedLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 28, 9),
    _WwpLeosCfmRxUnresolvedLTM_Type()
)
wwpLeosCfmRxUnresolvedLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRxUnresolvedLTM.setStatus("current")
_WwpLeosCfmGlobalDelayMeasurementStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalDelayMeasurementStats = _WwpLeosCfmGlobalDelayMeasurementStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 29)
)
_WwpLeosCfmTotalTxDMM_Type = Counter64
_WwpLeosCfmTotalTxDMM_Object = MibScalar
wwpLeosCfmTotalTxDMM = _WwpLeosCfmTotalTxDMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 29, 1),
    _WwpLeosCfmTotalTxDMM_Type()
)
wwpLeosCfmTotalTxDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxDMM.setStatus("current")
_WwpLeosCfmTotalTxDMR_Type = Counter64
_WwpLeosCfmTotalTxDMR_Object = MibScalar
wwpLeosCfmTotalTxDMR = _WwpLeosCfmTotalTxDMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 29, 2),
    _WwpLeosCfmTotalTxDMR_Type()
)
wwpLeosCfmTotalTxDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxDMR.setStatus("current")
_WwpLeosCfmTotalRxDMM_Type = Counter64
_WwpLeosCfmTotalRxDMM_Object = MibScalar
wwpLeosCfmTotalRxDMM = _WwpLeosCfmTotalRxDMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 29, 3),
    _WwpLeosCfmTotalRxDMM_Type()
)
wwpLeosCfmTotalRxDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxDMM.setStatus("current")
_WwpLeosCfmTotalRxDMR_Type = Counter64
_WwpLeosCfmTotalRxDMR_Object = MibScalar
wwpLeosCfmTotalRxDMR = _WwpLeosCfmTotalRxDMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 29, 4),
    _WwpLeosCfmTotalRxDMR_Type()
)
wwpLeosCfmTotalRxDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxDMR.setStatus("current")
_WwpLeosCfmGlobalLossMeasurementStats_ObjectIdentity = ObjectIdentity
wwpLeosCfmGlobalLossMeasurementStats = _WwpLeosCfmGlobalLossMeasurementStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 30)
)
_WwpLeosCfmTotalTxLMM_Type = Counter64
_WwpLeosCfmTotalTxLMM_Object = MibScalar
wwpLeosCfmTotalTxLMM = _WwpLeosCfmTotalTxLMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 30, 1),
    _WwpLeosCfmTotalTxLMM_Type()
)
wwpLeosCfmTotalTxLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLMM.setStatus("current")
_WwpLeosCfmTotalTxLMR_Type = Counter64
_WwpLeosCfmTotalTxLMR_Object = MibScalar
wwpLeosCfmTotalTxLMR = _WwpLeosCfmTotalTxLMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 30, 2),
    _WwpLeosCfmTotalTxLMR_Type()
)
wwpLeosCfmTotalTxLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalTxLMR.setStatus("current")
_WwpLeosCfmTotalRxLMM_Type = Counter64
_WwpLeosCfmTotalRxLMM_Object = MibScalar
wwpLeosCfmTotalRxLMM = _WwpLeosCfmTotalRxLMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 30, 3),
    _WwpLeosCfmTotalRxLMM_Type()
)
wwpLeosCfmTotalRxLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxLMM.setStatus("current")
_WwpLeosCfmTotalRxLMR_Type = Counter64
_WwpLeosCfmTotalRxLMR_Object = MibScalar
wwpLeosCfmTotalRxLMR = _WwpLeosCfmTotalRxLMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 1, 25, 30, 4),
    _WwpLeosCfmTotalRxLMR_Type()
)
wwpLeosCfmTotalRxLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmTotalRxLMR.setStatus("current")
_WwpLeosCfmService_ObjectIdentity = ObjectIdentity
wwpLeosCfmService = _WwpLeosCfmService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2)
)
_WwpLeosCfmServiceTable_Object = MibTable
wwpLeosCfmServiceTable = _WwpLeosCfmServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTable.setStatus("current")
_WwpLeosCfmServiceEntry_Object = MibTableRow
wwpLeosCfmServiceEntry = _WwpLeosCfmServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1)
)
wwpLeosCfmServiceEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceEntry.setStatus("current")


class _WwpLeosCfmServiceIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmServiceIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmServiceIndex_Object = MibTableColumn
wwpLeosCfmServiceIndex = _WwpLeosCfmServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 1),
    _WwpLeosCfmServiceIndex_Type()
)
wwpLeosCfmServiceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceIndex.setStatus("current")


class _WwpLeosCfmServiceType_Type(Integer32):
    """Custom type wwpLeosCfmServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ethVs", 2),
          ("mplsVs", 1),
          ("other", 9),
          ("pbtTunnel", 4),
          ("vlan", 3),
          ("vs", 5))
    )


_WwpLeosCfmServiceType_Type.__name__ = "Integer32"
_WwpLeosCfmServiceType_Object = MibTableColumn
wwpLeosCfmServiceType = _WwpLeosCfmServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 2),
    _WwpLeosCfmServiceType_Type()
)
wwpLeosCfmServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceType.setStatus("current")


class _WwpLeosCfmServiceValue_Type(Integer32):
    """Custom type wwpLeosCfmServiceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmServiceValue_Type.__name__ = "Integer32"
_WwpLeosCfmServiceValue_Object = MibTableColumn
wwpLeosCfmServiceValue = _WwpLeosCfmServiceValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 3),
    _WwpLeosCfmServiceValue_Type()
)
wwpLeosCfmServiceValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceValue.setStatus("current")


class _WwpLeosCfmServiceAdminState_Type(Integer32):
    """Custom type wwpLeosCfmServiceAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmServiceAdminState_Type.__name__ = "Integer32"
_WwpLeosCfmServiceAdminState_Object = MibTableColumn
wwpLeosCfmServiceAdminState = _WwpLeosCfmServiceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 4),
    _WwpLeosCfmServiceAdminState_Type()
)
wwpLeosCfmServiceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceAdminState.setStatus("current")


class _WwpLeosCfmServiceOperState_Type(Integer32):
    """Custom type wwpLeosCfmServiceOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmServiceOperState_Type.__name__ = "Integer32"
_WwpLeosCfmServiceOperState_Object = MibTableColumn
wwpLeosCfmServiceOperState = _WwpLeosCfmServiceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 5),
    _WwpLeosCfmServiceOperState_Type()
)
wwpLeosCfmServiceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceOperState.setStatus("current")


class _WwpLeosCfmServiceAlarmTime_Type(Integer32):
    """Custom type wwpLeosCfmServiceAlarmTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_WwpLeosCfmServiceAlarmTime_Type.__name__ = "Integer32"
_WwpLeosCfmServiceAlarmTime_Object = MibTableColumn
wwpLeosCfmServiceAlarmTime = _WwpLeosCfmServiceAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 6),
    _WwpLeosCfmServiceAlarmTime_Type()
)
wwpLeosCfmServiceAlarmTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceAlarmTime.setStatus("current")


class _WwpLeosCfmServiceCCMInterval_Type(Integer32):
    """Custom type wwpLeosCfmServiceCCMInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmServiceCCMInterval_Type.__name__ = "Integer32"
_WwpLeosCfmServiceCCMInterval_Object = MibTableColumn
wwpLeosCfmServiceCCMInterval = _WwpLeosCfmServiceCCMInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 7),
    _WwpLeosCfmServiceCCMInterval_Type()
)
wwpLeosCfmServiceCCMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCCMInterval.setStatus("current")


class _WwpLeosCfmServiceName_Type(DisplayString):
    """Custom type wwpLeosCfmServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmServiceName_Type.__name__ = "DisplayString"
_WwpLeosCfmServiceName_Object = MibTableColumn
wwpLeosCfmServiceName = _WwpLeosCfmServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 9),
    _WwpLeosCfmServiceName_Type()
)
wwpLeosCfmServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceName.setStatus("current")


class _WwpLeosCfmServiceMdLevel_Type(Integer32):
    """Custom type wwpLeosCfmServiceMdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmServiceMdLevel_Type.__name__ = "Integer32"
_WwpLeosCfmServiceMdLevel_Object = MibTableColumn
wwpLeosCfmServiceMdLevel = _WwpLeosCfmServiceMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 10),
    _WwpLeosCfmServiceMdLevel_Type()
)
wwpLeosCfmServiceMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMdLevel.setStatus("current")


class _WwpLeosCfmServiceResetTime_Type(Integer32):
    """Custom type wwpLeosCfmServiceResetTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 36000),
    )


_WwpLeosCfmServiceResetTime_Type.__name__ = "Integer32"
_WwpLeosCfmServiceResetTime_Object = MibTableColumn
wwpLeosCfmServiceResetTime = _WwpLeosCfmServiceResetTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 11),
    _WwpLeosCfmServiceResetTime_Type()
)
wwpLeosCfmServiceResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceResetTime.setStatus("current")
_WwpLeosCfmServiceLastFaultCCM_Type = CfmDisplayString
_WwpLeosCfmServiceLastFaultCCM_Object = MibTableColumn
wwpLeosCfmServiceLastFaultCCM = _WwpLeosCfmServiceLastFaultCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 12),
    _WwpLeosCfmServiceLastFaultCCM_Type()
)
wwpLeosCfmServiceLastFaultCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceLastFaultCCM.setStatus("current")
_WwpLeosCfmServiceRMEPFailureFlag_Type = TruthValue
_WwpLeosCfmServiceRMEPFailureFlag_Object = MibTableColumn
wwpLeosCfmServiceRMEPFailureFlag = _WwpLeosCfmServiceRMEPFailureFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 13),
    _WwpLeosCfmServiceRMEPFailureFlag_Type()
)
wwpLeosCfmServiceRMEPFailureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRMEPFailureFlag.setStatus("current")
_WwpLeosCfmServiceCCMErrorFlag_Type = TruthValue
_WwpLeosCfmServiceCCMErrorFlag_Object = MibTableColumn
wwpLeosCfmServiceCCMErrorFlag = _WwpLeosCfmServiceCCMErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 14),
    _WwpLeosCfmServiceCCMErrorFlag_Type()
)
wwpLeosCfmServiceCCMErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCCMErrorFlag.setStatus("current")
_WwpLeosCfmServiceCrossConnectErrorFlag_Type = TruthValue
_WwpLeosCfmServiceCrossConnectErrorFlag_Object = MibTableColumn
wwpLeosCfmServiceCrossConnectErrorFlag = _WwpLeosCfmServiceCrossConnectErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 15),
    _WwpLeosCfmServiceCrossConnectErrorFlag_Type()
)
wwpLeosCfmServiceCrossConnectErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCrossConnectErrorFlag.setStatus("current")
_WwpLeosCfmServiceNumMEP_Type = Counter32
_WwpLeosCfmServiceNumMEP_Object = MibTableColumn
wwpLeosCfmServiceNumMEP = _WwpLeosCfmServiceNumMEP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 16),
    _WwpLeosCfmServiceNumMEP_Type()
)
wwpLeosCfmServiceNumMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceNumMEP.setStatus("current")
_WwpLeosCfmServiceNumRemoteMEP_Type = Counter32
_WwpLeosCfmServiceNumRemoteMEP_Object = MibTableColumn
wwpLeosCfmServiceNumRemoteMEP = _WwpLeosCfmServiceNumRemoteMEP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 17),
    _WwpLeosCfmServiceNumRemoteMEP_Type()
)
wwpLeosCfmServiceNumRemoteMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceNumRemoteMEP.setStatus("current")
_WwpLeosCfmServiceNumActiveMEP_Type = Counter32
_WwpLeosCfmServiceNumActiveMEP_Object = MibTableColumn
wwpLeosCfmServiceNumActiveMEP = _WwpLeosCfmServiceNumActiveMEP_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 18),
    _WwpLeosCfmServiceNumActiveMEP_Type()
)
wwpLeosCfmServiceNumActiveMEP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceNumActiveMEP.setStatus("current")
_WwpLeosCfmServiceStatus_Type = RowStatus
_WwpLeosCfmServiceStatus_Object = MibTableColumn
wwpLeosCfmServiceStatus = _WwpLeosCfmServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 19),
    _WwpLeosCfmServiceStatus_Type()
)
wwpLeosCfmServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceStatus.setStatus("current")


class _WwpLeosCfmServiceNextMepId_Type(Unsigned32):
    """Custom type wwpLeosCfmServiceNextMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmServiceNextMepId_Type.__name__ = "Unsigned32"
_WwpLeosCfmServiceNextMepId_Object = MibTableColumn
wwpLeosCfmServiceNextMepId = _WwpLeosCfmServiceNextMepId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 20),
    _WwpLeosCfmServiceNextMepId_Type()
)
wwpLeosCfmServiceNextMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceNextMepId.setStatus("current")


class _WwpLeosCfmServiceAlarmPriority_Type(Unsigned32):
    """Custom type wwpLeosCfmServiceAlarmPriority based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WwpLeosCfmServiceAlarmPriority_Type.__name__ = "Unsigned32"
_WwpLeosCfmServiceAlarmPriority_Object = MibTableColumn
wwpLeosCfmServiceAlarmPriority = _WwpLeosCfmServiceAlarmPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 21),
    _WwpLeosCfmServiceAlarmPriority_Type()
)
wwpLeosCfmServiceAlarmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceAlarmPriority.setStatus("current")


class _WwpLeosCfmServiceNumCCMForFault_Type(Unsigned32):
    """Custom type wwpLeosCfmServiceNumCCMForFault based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosCfmServiceNumCCMForFault_Type.__name__ = "Unsigned32"
_WwpLeosCfmServiceNumCCMForFault_Object = MibTableColumn
wwpLeosCfmServiceNumCCMForFault = _WwpLeosCfmServiceNumCCMForFault_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 22),
    _WwpLeosCfmServiceNumCCMForFault_Type()
)
wwpLeosCfmServiceNumCCMForFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceNumCCMForFault.setStatus("current")


class _WwpLeosCfmServiceDMMInterval_Type(Integer32):
    """Custom type wwpLeosCfmServiceDMMInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WwpLeosCfmServiceDMMInterval_Type.__name__ = "Integer32"
_WwpLeosCfmServiceDMMInterval_Object = MibTableColumn
wwpLeosCfmServiceDMMInterval = _WwpLeosCfmServiceDMMInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 23),
    _WwpLeosCfmServiceDMMInterval_Type()
)
wwpLeosCfmServiceDMMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceDMMInterval.setStatus("current")


class _WwpLeosCfmServiceLMMInterval_Type(Integer32):
    """Custom type wwpLeosCfmServiceLMMInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_WwpLeosCfmServiceLMMInterval_Type.__name__ = "Integer32"
_WwpLeosCfmServiceLMMInterval_Object = MibTableColumn
wwpLeosCfmServiceLMMInterval = _WwpLeosCfmServiceLMMInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 24),
    _WwpLeosCfmServiceLMMInterval_Type()
)
wwpLeosCfmServiceLMMInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceLMMInterval.setStatus("current")


class _WwpLeosCfmServiceCCMLossStatsState_Type(Integer32):
    """Custom type wwpLeosCfmServiceCCMLossStatsState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmServiceCCMLossStatsState_Type.__name__ = "Integer32"
_WwpLeosCfmServiceCCMLossStatsState_Object = MibTableColumn
wwpLeosCfmServiceCCMLossStatsState = _WwpLeosCfmServiceCCMLossStatsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 25),
    _WwpLeosCfmServiceCCMLossStatsState_Type()
)
wwpLeosCfmServiceCCMLossStatsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCCMLossStatsState.setStatus("current")


class _WwpLeosCfmServiceCCMLossBucketInterval_Type(Integer32):
    """Custom type wwpLeosCfmServiceCCMLossBucketInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WwpLeosCfmServiceCCMLossBucketInterval_Type.__name__ = "Integer32"
_WwpLeosCfmServiceCCMLossBucketInterval_Object = MibTableColumn
wwpLeosCfmServiceCCMLossBucketInterval = _WwpLeosCfmServiceCCMLossBucketInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 26),
    _WwpLeosCfmServiceCCMLossBucketInterval_Type()
)
wwpLeosCfmServiceCCMLossBucketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCCMLossBucketInterval.setStatus("current")


class _WwpLeosCfmServiceRemoteMepDiscovery_Type(Integer32):
    """Custom type wwpLeosCfmServiceRemoteMepDiscovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmServiceRemoteMepDiscovery_Type.__name__ = "Integer32"
_WwpLeosCfmServiceRemoteMepDiscovery_Object = MibTableColumn
wwpLeosCfmServiceRemoteMepDiscovery = _WwpLeosCfmServiceRemoteMepDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 27),
    _WwpLeosCfmServiceRemoteMepDiscovery_Type()
)
wwpLeosCfmServiceRemoteMepDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRemoteMepDiscovery.setStatus("current")
_WwpLeosCfmServiceY1731_Type = TruthValue
_WwpLeosCfmServiceY1731_Object = MibTableColumn
wwpLeosCfmServiceY1731 = _WwpLeosCfmServiceY1731_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 28),
    _WwpLeosCfmServiceY1731_Type()
)
wwpLeosCfmServiceY1731.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceY1731.setStatus("current")
_WwpLeosCfmServiceAccelerated_Type = TruthValue
_WwpLeosCfmServiceAccelerated_Object = MibTableColumn
wwpLeosCfmServiceAccelerated = _WwpLeosCfmServiceAccelerated_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 49),
    _WwpLeosCfmServiceAccelerated_Type()
)
wwpLeosCfmServiceAccelerated.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceAccelerated.setStatus("current")


class _WwpLeosCfmServiceTlvSenderIdType_Type(Integer32):
    """Custom type wwpLeosCfmServiceTlvSenderIdType based on Integer32"""
    defaultValue = 2

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
        *(("chassis", 2),
          ("chassisManage", 4),
          ("manage", 3),
          ("none", 1))
    )


_WwpLeosCfmServiceTlvSenderIdType_Type.__name__ = "Integer32"
_WwpLeosCfmServiceTlvSenderIdType_Object = MibTableColumn
wwpLeosCfmServiceTlvSenderIdType = _WwpLeosCfmServiceTlvSenderIdType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 50),
    _WwpLeosCfmServiceTlvSenderIdType_Type()
)
wwpLeosCfmServiceTlvSenderIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTlvSenderIdType.setStatus("current")


class _WwpLeosCfmServiceRMEPHoldTime_Type(Unsigned32):
    """Custom type wwpLeosCfmServiceRMEPHoldTime based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_WwpLeosCfmServiceRMEPHoldTime_Type.__name__ = "Unsigned32"
_WwpLeosCfmServiceRMEPHoldTime_Object = MibTableColumn
wwpLeosCfmServiceRMEPHoldTime = _WwpLeosCfmServiceRMEPHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 51),
    _WwpLeosCfmServiceRMEPHoldTime_Type()
)
wwpLeosCfmServiceRMEPHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRMEPHoldTime.setStatus("current")


class _WwpLeosCfmServiceCCMTxState_Type(Integer32):
    """Custom type wwpLeosCfmServiceCCMTxState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmServiceCCMTxState_Type.__name__ = "Integer32"
_WwpLeosCfmServiceCCMTxState_Object = MibTableColumn
wwpLeosCfmServiceCCMTxState = _WwpLeosCfmServiceCCMTxState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 52),
    _WwpLeosCfmServiceCCMTxState_Type()
)
wwpLeosCfmServiceCCMTxState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCCMTxState.setStatus("current")
_WwpLeosCfmServicePortStatusFlag_Type = TruthValue
_WwpLeosCfmServicePortStatusFlag_Object = MibTableColumn
wwpLeosCfmServicePortStatusFlag = _WwpLeosCfmServicePortStatusFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 53),
    _WwpLeosCfmServicePortStatusFlag_Type()
)
wwpLeosCfmServicePortStatusFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServicePortStatusFlag.setStatus("current")
_WwpLeosCfmServiceRDIFlag_Type = TruthValue
_WwpLeosCfmServiceRDIFlag_Object = MibTableColumn
wwpLeosCfmServiceRDIFlag = _WwpLeosCfmServiceRDIFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 54),
    _WwpLeosCfmServiceRDIFlag_Type()
)
wwpLeosCfmServiceRDIFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRDIFlag.setStatus("current")
_WwpLeosCfmServiceInstabilityFlag_Type = TruthValue
_WwpLeosCfmServiceInstabilityFlag_Object = MibTableColumn
wwpLeosCfmServiceInstabilityFlag = _WwpLeosCfmServiceInstabilityFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 55),
    _WwpLeosCfmServiceInstabilityFlag_Type()
)
wwpLeosCfmServiceInstabilityFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceInstabilityFlag.setStatus("current")
_WwpLeosCfmServiceRMEPAging_Type = TruthValue
_WwpLeosCfmServiceRMEPAging_Object = MibTableColumn
wwpLeosCfmServiceRMEPAging = _WwpLeosCfmServiceRMEPAging_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 56),
    _WwpLeosCfmServiceRMEPAging_Type()
)
wwpLeosCfmServiceRMEPAging.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRMEPAging.setStatus("current")


class _WwpLeosCfmServiceDefaultMEPType_Type(Integer32):
    """Custom type wwpLeosCfmServiceDefaultMEPType based on Integer32"""
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


_WwpLeosCfmServiceDefaultMEPType_Type.__name__ = "Integer32"
_WwpLeosCfmServiceDefaultMEPType_Object = MibTableColumn
wwpLeosCfmServiceDefaultMEPType = _WwpLeosCfmServiceDefaultMEPType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 57),
    _WwpLeosCfmServiceDefaultMEPType_Type()
)
wwpLeosCfmServiceDefaultMEPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceDefaultMEPType.setStatus("deprecated")
_WwpLeosCfmServiceMAID_Type = CfmMAID
_WwpLeosCfmServiceMAID_Object = MibTableColumn
wwpLeosCfmServiceMAID = _WwpLeosCfmServiceMAID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 58),
    _WwpLeosCfmServiceMAID_Type()
)
wwpLeosCfmServiceMAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMAID.setStatus("deprecated")
_WwpLeosCfmServiceMdIndex_Type = Unsigned32
_WwpLeosCfmServiceMdIndex_Object = MibTableColumn
wwpLeosCfmServiceMdIndex = _WwpLeosCfmServiceMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 59),
    _WwpLeosCfmServiceMdIndex_Type()
)
wwpLeosCfmServiceMdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMdIndex.setStatus("deprecated")
_WwpLeosCfmServiceMaintAssocNameType_Type = Dot1agCfmMaintAssocNameType
_WwpLeosCfmServiceMaintAssocNameType_Object = MibTableColumn
wwpLeosCfmServiceMaintAssocNameType = _WwpLeosCfmServiceMaintAssocNameType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 60),
    _WwpLeosCfmServiceMaintAssocNameType_Type()
)
wwpLeosCfmServiceMaintAssocNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMaintAssocNameType.setStatus("deprecated")
_WwpLeosCfmServiceMaintAssocName_Type = Dot1agCfmMaintAssocName
_WwpLeosCfmServiceMaintAssocName_Object = MibTableColumn
wwpLeosCfmServiceMaintAssocName = _WwpLeosCfmServiceMaintAssocName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 61),
    _WwpLeosCfmServiceMaintAssocName_Type()
)
wwpLeosCfmServiceMaintAssocName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMaintAssocName.setStatus("deprecated")
_WwpLeosCfmServiceMulticastDa_Type = TruthValue
_WwpLeosCfmServiceMulticastDa_Object = MibTableColumn
wwpLeosCfmServiceMulticastDa = _WwpLeosCfmServiceMulticastDa_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 65),
    _WwpLeosCfmServiceMulticastDa_Type()
)
wwpLeosCfmServiceMulticastDa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceMulticastDa.setStatus("current")
_WwpLeosCfmServiceChargedAgainstGlobalFrameBudget_Type = TruthValue
_WwpLeosCfmServiceChargedAgainstGlobalFrameBudget_Object = MibTableColumn
wwpLeosCfmServiceChargedAgainstGlobalFrameBudget = _WwpLeosCfmServiceChargedAgainstGlobalFrameBudget_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 71),
    _WwpLeosCfmServiceChargedAgainstGlobalFrameBudget_Type()
)
wwpLeosCfmServiceChargedAgainstGlobalFrameBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceChargedAgainstGlobalFrameBudget.setStatus("current")


class _WwpLeosCfmServiceCfmDefaultMEPType_Type(Integer32):
    """Custom type wwpLeosCfmServiceCfmDefaultMEPType based on Integer32"""
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


_WwpLeosCfmServiceCfmDefaultMEPType_Type.__name__ = "Integer32"
_WwpLeosCfmServiceCfmDefaultMEPType_Object = MibTableColumn
wwpLeosCfmServiceCfmDefaultMEPType = _WwpLeosCfmServiceCfmDefaultMEPType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 72),
    _WwpLeosCfmServiceCfmDefaultMEPType_Type()
)
wwpLeosCfmServiceCfmDefaultMEPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmDefaultMEPType.setStatus("current")
_WwpLeosCfmServiceCfmMAID_Type = CfmMAID
_WwpLeosCfmServiceCfmMAID_Object = MibTableColumn
wwpLeosCfmServiceCfmMAID = _WwpLeosCfmServiceCfmMAID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 73),
    _WwpLeosCfmServiceCfmMAID_Type()
)
wwpLeosCfmServiceCfmMAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmMAID.setStatus("current")
_WwpLeosCfmServiceCfmMdIndex_Type = Unsigned32
_WwpLeosCfmServiceCfmMdIndex_Object = MibTableColumn
wwpLeosCfmServiceCfmMdIndex = _WwpLeosCfmServiceCfmMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 74),
    _WwpLeosCfmServiceCfmMdIndex_Type()
)
wwpLeosCfmServiceCfmMdIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmMdIndex.setStatus("current")
_WwpLeosCfmServiceCfmMaintAssocNameType_Type = Dot1agCfmMaintAssocNameType
_WwpLeosCfmServiceCfmMaintAssocNameType_Object = MibTableColumn
wwpLeosCfmServiceCfmMaintAssocNameType = _WwpLeosCfmServiceCfmMaintAssocNameType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 75),
    _WwpLeosCfmServiceCfmMaintAssocNameType_Type()
)
wwpLeosCfmServiceCfmMaintAssocNameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmMaintAssocNameType.setStatus("current")
_WwpLeosCfmServiceCfmMaintAssocName_Type = Dot1agCfmMaintAssocName
_WwpLeosCfmServiceCfmMaintAssocName_Object = MibTableColumn
wwpLeosCfmServiceCfmMaintAssocName = _WwpLeosCfmServiceCfmMaintAssocName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 76),
    _WwpLeosCfmServiceCfmMaintAssocName_Type()
)
wwpLeosCfmServiceCfmMaintAssocName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmMaintAssocName.setStatus("current")
_WwpLeosCfmServiceCfmControlModuleFrameBudget_Type = Counter32
_WwpLeosCfmServiceCfmControlModuleFrameBudget_Object = MibTableColumn
wwpLeosCfmServiceCfmControlModuleFrameBudget = _WwpLeosCfmServiceCfmControlModuleFrameBudget_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 1, 1, 77),
    _WwpLeosCfmServiceCfmControlModuleFrameBudget_Type()
)
wwpLeosCfmServiceCfmControlModuleFrameBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceCfmControlModuleFrameBudget.setStatus("current")
_WwpLeosCfmServiceFaultTable_Object = MibTable
wwpLeosCfmServiceFaultTable = _WwpLeosCfmServiceFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultTable.setStatus("current")
_WwpLeosCfmServiceFaultEntry_Object = MibTableRow
wwpLeosCfmServiceFaultEntry = _WwpLeosCfmServiceFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1)
)
wwpLeosCfmServiceFaultEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultEntry.setStatus("current")
_WwpLeosCfmServiceFaultTime_Type = TimeTicks
_WwpLeosCfmServiceFaultTime_Object = MibTableColumn
wwpLeosCfmServiceFaultTime = _WwpLeosCfmServiceFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 1),
    _WwpLeosCfmServiceFaultTime_Type()
)
wwpLeosCfmServiceFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultTime.setStatus("current")


class _WwpLeosCfmServiceFaultType_Type(Integer32):
    """Custom type wwpLeosCfmServiceFaultType based on Integer32"""
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
        *(("errorCCMDefect", 5),
          ("instability", 7),
          ("none", 1),
          ("someMACStatusDefect", 3),
          ("someRDIDefect", 2),
          ("someRMEPCCMDefect", 4),
          ("xconCCMDefect", 6))
    )


_WwpLeosCfmServiceFaultType_Type.__name__ = "Integer32"
_WwpLeosCfmServiceFaultType_Object = MibTableColumn
wwpLeosCfmServiceFaultType = _WwpLeosCfmServiceFaultType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 2),
    _WwpLeosCfmServiceFaultType_Type()
)
wwpLeosCfmServiceFaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultType.setStatus("current")
_WwpLeosCfmServiceFaultDesc_Type = DisplayString
_WwpLeosCfmServiceFaultDesc_Object = MibTableColumn
wwpLeosCfmServiceFaultDesc = _WwpLeosCfmServiceFaultDesc_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 3),
    _WwpLeosCfmServiceFaultDesc_Type()
)
wwpLeosCfmServiceFaultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultDesc.setStatus("current")


class _WwpLeosCfmServiceFaultMep_Type(Integer32):
    """Custom type wwpLeosCfmServiceFaultMep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmServiceFaultMep_Type.__name__ = "Integer32"
_WwpLeosCfmServiceFaultMep_Object = MibTableColumn
wwpLeosCfmServiceFaultMep = _WwpLeosCfmServiceFaultMep_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 4),
    _WwpLeosCfmServiceFaultMep_Type()
)
wwpLeosCfmServiceFaultMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFaultMep.setStatus("current")


class _WwpLeosCfmServiceVlan_Type(Integer32):
    """Custom type wwpLeosCfmServiceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmServiceVlan_Type.__name__ = "Integer32"
_WwpLeosCfmServiceVlan_Object = MibTableColumn
wwpLeosCfmServiceVlan = _WwpLeosCfmServiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 5),
    _WwpLeosCfmServiceVlan_Type()
)
wwpLeosCfmServiceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceVlan.setStatus("current")


class _WwpLeosCfmServiceVsPbtName_Type(DisplayString):
    """Custom type wwpLeosCfmServiceVsPbtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmServiceVsPbtName_Type.__name__ = "DisplayString"
_WwpLeosCfmServiceVsPbtName_Object = MibTableColumn
wwpLeosCfmServiceVsPbtName = _WwpLeosCfmServiceVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 2, 1, 50),
    _WwpLeosCfmServiceVsPbtName_Type()
)
wwpLeosCfmServiceVsPbtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceVsPbtName.setStatus("current")
_WwpLeosCfmServiceStatisticsTable_Object = MibTable
wwpLeosCfmServiceStatisticsTable = _WwpLeosCfmServiceStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceStatisticsTable.setStatus("current")
_WwpLeosCfmServiceStatisticsEntry_Object = MibTableRow
wwpLeosCfmServiceStatisticsEntry = _WwpLeosCfmServiceStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1)
)
wwpLeosCfmServiceStatisticsEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceStatisticsEntry.setStatus("current")
_WwpLeosCfmServiceRxTotalValidFrames_Type = Counter64
_WwpLeosCfmServiceRxTotalValidFrames_Object = MibTableColumn
wwpLeosCfmServiceRxTotalValidFrames = _WwpLeosCfmServiceRxTotalValidFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 1),
    _WwpLeosCfmServiceRxTotalValidFrames_Type()
)
wwpLeosCfmServiceRxTotalValidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRxTotalValidFrames.setStatus("current")
_WwpLeosCfmServiceRxTotalInvalidFrames_Type = Counter64
_WwpLeosCfmServiceRxTotalInvalidFrames_Object = MibTableColumn
wwpLeosCfmServiceRxTotalInvalidFrames = _WwpLeosCfmServiceRxTotalInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 2),
    _WwpLeosCfmServiceRxTotalInvalidFrames_Type()
)
wwpLeosCfmServiceRxTotalInvalidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceRxTotalInvalidFrames.setStatus("current")
_WwpLeosCfmServiceInvalidMessageOverflow_Type = Counter64
_WwpLeosCfmServiceInvalidMessageOverflow_Object = MibTableColumn
wwpLeosCfmServiceInvalidMessageOverflow = _WwpLeosCfmServiceInvalidMessageOverflow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 3),
    _WwpLeosCfmServiceInvalidMessageOverflow_Type()
)
wwpLeosCfmServiceInvalidMessageOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceInvalidMessageOverflow.setStatus("current")
_WwpLeosCfmServiceInvalidPortStatusTLV_Type = Counter64
_WwpLeosCfmServiceInvalidPortStatusTLV_Object = MibTableColumn
wwpLeosCfmServiceInvalidPortStatusTLV = _WwpLeosCfmServiceInvalidPortStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 4),
    _WwpLeosCfmServiceInvalidPortStatusTLV_Type()
)
wwpLeosCfmServiceInvalidPortStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceInvalidPortStatusTLV.setStatus("current")
_WwpLeosCfmServiceInvalidInterfaceStatusTLV_Type = Counter64
_WwpLeosCfmServiceInvalidInterfaceStatusTLV_Object = MibTableColumn
wwpLeosCfmServiceInvalidInterfaceStatusTLV = _WwpLeosCfmServiceInvalidInterfaceStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 5),
    _WwpLeosCfmServiceInvalidInterfaceStatusTLV_Type()
)
wwpLeosCfmServiceInvalidInterfaceStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceInvalidInterfaceStatusTLV.setStatus("current")
_WwpLeosCfmServiceInvalidSenderIDTLV_Type = Counter64
_WwpLeosCfmServiceInvalidSenderIDTLV_Object = MibTableColumn
wwpLeosCfmServiceInvalidSenderIDTLV = _WwpLeosCfmServiceInvalidSenderIDTLV_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 6),
    _WwpLeosCfmServiceInvalidSenderIDTLV_Type()
)
wwpLeosCfmServiceInvalidSenderIDTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceInvalidSenderIDTLV.setStatus("current")
_WwpLeosCfmServiceTxTotalCCM_Type = Counter64
_WwpLeosCfmServiceTxTotalCCM_Object = MibTableColumn
wwpLeosCfmServiceTxTotalCCM = _WwpLeosCfmServiceTxTotalCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 7),
    _WwpLeosCfmServiceTxTotalCCM_Type()
)
wwpLeosCfmServiceTxTotalCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTxTotalCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxValidCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxValidCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxValidCCM = _WwpLeosCfmServiceTotalRxValidCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 8),
    _WwpLeosCfmServiceTotalRxValidCCM_Type()
)
wwpLeosCfmServiceTotalRxValidCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxValidCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxInSequenceCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxInSequenceCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInSequenceCCM = _WwpLeosCfmServiceTotalRxInSequenceCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 9),
    _WwpLeosCfmServiceTotalRxInSequenceCCM_Type()
)
wwpLeosCfmServiceTotalRxInSequenceCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInSequenceCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxNotInSequenceCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxNotInSequenceCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxNotInSequenceCCM = _WwpLeosCfmServiceTotalRxNotInSequenceCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 10),
    _WwpLeosCfmServiceTotalRxNotInSequenceCCM_Type()
)
wwpLeosCfmServiceTotalRxNotInSequenceCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxNotInSequenceCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxMDLevelXconCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxMDLevelXconCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxMDLevelXconCCM = _WwpLeosCfmServiceTotalRxMDLevelXconCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 11),
    _WwpLeosCfmServiceTotalRxMDLevelXconCCM_Type()
)
wwpLeosCfmServiceTotalRxMDLevelXconCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxMDLevelXconCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxMAIDXconCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxMAIDXconCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxMAIDXconCCM = _WwpLeosCfmServiceTotalRxMAIDXconCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 12),
    _WwpLeosCfmServiceTotalRxMAIDXconCCM_Type()
)
wwpLeosCfmServiceTotalRxMAIDXconCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxMAIDXconCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxMEPIDErrorCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxMEPIDErrorCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxMEPIDErrorCCM = _WwpLeosCfmServiceTotalRxMEPIDErrorCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 13),
    _WwpLeosCfmServiceTotalRxMEPIDErrorCCM_Type()
)
wwpLeosCfmServiceTotalRxMEPIDErrorCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxMEPIDErrorCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxCCMIntervalErrorCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxCCMIntervalErrorCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxCCMIntervalErrorCCM = _WwpLeosCfmServiceTotalRxCCMIntervalErrorCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 14),
    _WwpLeosCfmServiceTotalRxCCMIntervalErrorCCM_Type()
)
wwpLeosCfmServiceTotalRxCCMIntervalErrorCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxCCMIntervalErrorCCM.setStatus("current")
_WwpLeosCfmServiceTotalRxInvalidCCM_Type = Counter64
_WwpLeosCfmServiceTotalRxInvalidCCM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInvalidCCM = _WwpLeosCfmServiceTotalRxInvalidCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 15),
    _WwpLeosCfmServiceTotalRxInvalidCCM_Type()
)
wwpLeosCfmServiceTotalRxInvalidCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInvalidCCM.setStatus("current")
_WwpLeosCfmServiceTotalTxLTM_Type = Counter64
_WwpLeosCfmServiceTotalTxLTM_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLTM = _WwpLeosCfmServiceTotalTxLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 16),
    _WwpLeosCfmServiceTotalTxLTM_Type()
)
wwpLeosCfmServiceTotalTxLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLTM.setStatus("current")
_WwpLeosCfmServiceTotalTxLTR_Type = Counter64
_WwpLeosCfmServiceTotalTxLTR_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLTR = _WwpLeosCfmServiceTotalTxLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 17),
    _WwpLeosCfmServiceTotalTxLTR_Type()
)
wwpLeosCfmServiceTotalTxLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLTR.setStatus("current")
_WwpLeosCfmServiceTotalRxValidLTR_Type = Counter64
_WwpLeosCfmServiceTotalRxValidLTR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxValidLTR = _WwpLeosCfmServiceTotalRxValidLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 18),
    _WwpLeosCfmServiceTotalRxValidLTR_Type()
)
wwpLeosCfmServiceTotalRxValidLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxValidLTR.setStatus("current")
_WwpLeosCfmServiceTotalRxUnexpectedLTR_Type = Counter64
_WwpLeosCfmServiceTotalRxUnexpectedLTR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxUnexpectedLTR = _WwpLeosCfmServiceTotalRxUnexpectedLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 19),
    _WwpLeosCfmServiceTotalRxUnexpectedLTR_Type()
)
wwpLeosCfmServiceTotalRxUnexpectedLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxUnexpectedLTR.setStatus("current")
_WwpLeosCfmServiceTotalRxInvalidLTR_Type = Counter64
_WwpLeosCfmServiceTotalRxInvalidLTR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInvalidLTR = _WwpLeosCfmServiceTotalRxInvalidLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 20),
    _WwpLeosCfmServiceTotalRxInvalidLTR_Type()
)
wwpLeosCfmServiceTotalRxInvalidLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInvalidLTR.setStatus("current")
_WwpLeosCfmServiceTotalRxInvalidRelayActionLTR_Type = Counter64
_WwpLeosCfmServiceTotalRxInvalidRelayActionLTR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInvalidRelayActionLTR = _WwpLeosCfmServiceTotalRxInvalidRelayActionLTR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 21),
    _WwpLeosCfmServiceTotalRxInvalidRelayActionLTR_Type()
)
wwpLeosCfmServiceTotalRxInvalidRelayActionLTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInvalidRelayActionLTR.setStatus("current")
_WwpLeosCfmServiceTotalRxValidLTM_Type = Counter64
_WwpLeosCfmServiceTotalRxValidLTM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxValidLTM = _WwpLeosCfmServiceTotalRxValidLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 22),
    _WwpLeosCfmServiceTotalRxValidLTM_Type()
)
wwpLeosCfmServiceTotalRxValidLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxValidLTM.setStatus("current")
_WwpLeosCfmServiceTotalTxInvalidLTM_Type = Counter64
_WwpLeosCfmServiceTotalTxInvalidLTM_Object = MibTableColumn
wwpLeosCfmServiceTotalTxInvalidLTM = _WwpLeosCfmServiceTotalTxInvalidLTM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 23),
    _WwpLeosCfmServiceTotalTxInvalidLTM_Type()
)
wwpLeosCfmServiceTotalTxInvalidLTM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxInvalidLTM.setStatus("current")
_WwpLeosCfmServiceTotalTxLBM_Type = Counter64
_WwpLeosCfmServiceTotalTxLBM_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLBM = _WwpLeosCfmServiceTotalTxLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 24),
    _WwpLeosCfmServiceTotalTxLBM_Type()
)
wwpLeosCfmServiceTotalTxLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLBM.setStatus("current")
_WwpLeosCfmServiceTotalTxLBR_Type = Counter64
_WwpLeosCfmServiceTotalTxLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLBR = _WwpLeosCfmServiceTotalTxLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 25),
    _WwpLeosCfmServiceTotalTxLBR_Type()
)
wwpLeosCfmServiceTotalTxLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxInorderLBR_Type = Counter64
_WwpLeosCfmServiceTotalRxInorderLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInorderLBR = _WwpLeosCfmServiceTotalRxInorderLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 26),
    _WwpLeosCfmServiceTotalRxInorderLBR_Type()
)
wwpLeosCfmServiceTotalRxInorderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInorderLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxOutOfOrderLBR_Type = Counter64
_WwpLeosCfmServiceTotalRxOutOfOrderLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxOutOfOrderLBR = _WwpLeosCfmServiceTotalRxOutOfOrderLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 27),
    _WwpLeosCfmServiceTotalRxOutOfOrderLBR_Type()
)
wwpLeosCfmServiceTotalRxOutOfOrderLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxOutOfOrderLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxContentMismatchLBR_Type = Counter64
_WwpLeosCfmServiceTotalRxContentMismatchLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxContentMismatchLBR = _WwpLeosCfmServiceTotalRxContentMismatchLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 28),
    _WwpLeosCfmServiceTotalRxContentMismatchLBR_Type()
)
wwpLeosCfmServiceTotalRxContentMismatchLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxContentMismatchLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxUnexpectedLBR_Type = Counter64
_WwpLeosCfmServiceTotalRxUnexpectedLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxUnexpectedLBR = _WwpLeosCfmServiceTotalRxUnexpectedLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 29),
    _WwpLeosCfmServiceTotalRxUnexpectedLBR_Type()
)
wwpLeosCfmServiceTotalRxUnexpectedLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxUnexpectedLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxInvalidLBR_Type = Counter64
_WwpLeosCfmServiceTotalRxInvalidLBR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInvalidLBR = _WwpLeosCfmServiceTotalRxInvalidLBR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 30),
    _WwpLeosCfmServiceTotalRxInvalidLBR_Type()
)
wwpLeosCfmServiceTotalRxInvalidLBR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInvalidLBR.setStatus("current")
_WwpLeosCfmServiceTotalRxValidLBM_Type = Counter64
_WwpLeosCfmServiceTotalRxValidLBM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxValidLBM = _WwpLeosCfmServiceTotalRxValidLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 31),
    _WwpLeosCfmServiceTotalRxValidLBM_Type()
)
wwpLeosCfmServiceTotalRxValidLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxValidLBM.setStatus("current")
_WwpLeosCfmServiceTotalRxInvalidLBM_Type = Counter64
_WwpLeosCfmServiceTotalRxInvalidLBM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxInvalidLBM = _WwpLeosCfmServiceTotalRxInvalidLBM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 32),
    _WwpLeosCfmServiceTotalRxInvalidLBM_Type()
)
wwpLeosCfmServiceTotalRxInvalidLBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxInvalidLBM.setStatus("current")
_WwpLeosCfmServiceTotalTxDMM_Type = Counter64
_WwpLeosCfmServiceTotalTxDMM_Object = MibTableColumn
wwpLeosCfmServiceTotalTxDMM = _WwpLeosCfmServiceTotalTxDMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 33),
    _WwpLeosCfmServiceTotalTxDMM_Type()
)
wwpLeosCfmServiceTotalTxDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxDMM.setStatus("current")
_WwpLeosCfmServiceTotalTxDMR_Type = Counter64
_WwpLeosCfmServiceTotalTxDMR_Object = MibTableColumn
wwpLeosCfmServiceTotalTxDMR = _WwpLeosCfmServiceTotalTxDMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 34),
    _WwpLeosCfmServiceTotalTxDMR_Type()
)
wwpLeosCfmServiceTotalTxDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxDMR.setStatus("current")
_WwpLeosCfmServiceTotalRxDMM_Type = Counter64
_WwpLeosCfmServiceTotalRxDMM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxDMM = _WwpLeosCfmServiceTotalRxDMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 35),
    _WwpLeosCfmServiceTotalRxDMM_Type()
)
wwpLeosCfmServiceTotalRxDMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxDMM.setStatus("current")
_WwpLeosCfmServiceTotalRxDMR_Type = Counter64
_WwpLeosCfmServiceTotalRxDMR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxDMR = _WwpLeosCfmServiceTotalRxDMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 36),
    _WwpLeosCfmServiceTotalRxDMR_Type()
)
wwpLeosCfmServiceTotalRxDMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxDMR.setStatus("current")
_WwpLeosCfmServiceTotalTxLMM_Type = Counter64
_WwpLeosCfmServiceTotalTxLMM_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLMM = _WwpLeosCfmServiceTotalTxLMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 37),
    _WwpLeosCfmServiceTotalTxLMM_Type()
)
wwpLeosCfmServiceTotalTxLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLMM.setStatus("current")
_WwpLeosCfmServiceTotalTxLMR_Type = Counter64
_WwpLeosCfmServiceTotalTxLMR_Object = MibTableColumn
wwpLeosCfmServiceTotalTxLMR = _WwpLeosCfmServiceTotalTxLMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 38),
    _WwpLeosCfmServiceTotalTxLMR_Type()
)
wwpLeosCfmServiceTotalTxLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalTxLMR.setStatus("current")
_WwpLeosCfmServiceTotalRxLMM_Type = Counter64
_WwpLeosCfmServiceTotalRxLMM_Object = MibTableColumn
wwpLeosCfmServiceTotalRxLMM = _WwpLeosCfmServiceTotalRxLMM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 39),
    _WwpLeosCfmServiceTotalRxLMM_Type()
)
wwpLeosCfmServiceTotalRxLMM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxLMM.setStatus("current")
_WwpLeosCfmServiceTotalRxLMR_Type = Counter64
_WwpLeosCfmServiceTotalRxLMR_Object = MibTableColumn
wwpLeosCfmServiceTotalRxLMR = _WwpLeosCfmServiceTotalRxLMR_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 40),
    _WwpLeosCfmServiceTotalRxLMR_Type()
)
wwpLeosCfmServiceTotalRxLMR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceTotalRxLMR.setStatus("current")


class _WwpLeosCfmServiceStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmServiceStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmServiceStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmServiceStatsClear_Object = MibTableColumn
wwpLeosCfmServiceStatsClear = _WwpLeosCfmServiceStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 3, 1, 41),
    _WwpLeosCfmServiceStatsClear_Type()
)
wwpLeosCfmServiceStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceStatsClear.setStatus("current")


class _WwpLeosCfmServiceClearStats_Type(Integer32):
    """Custom type wwpLeosCfmServiceClearStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmServiceClearStats_Type.__name__ = "Integer32"
_WwpLeosCfmServiceClearStats_Object = MibScalar
wwpLeosCfmServiceClearStats = _WwpLeosCfmServiceClearStats_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 2, 4),
    _WwpLeosCfmServiceClearStats_Type()
)
wwpLeosCfmServiceClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceClearStats.setStatus("current")
_WwpLeosCfmMIP_ObjectIdentity = ObjectIdentity
wwpLeosCfmMIP = _WwpLeosCfmMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3)
)
_WwpLeosCfmMipTable_Object = MibTable
wwpLeosCfmMipTable = _WwpLeosCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmMipTable.setStatus("current")
_WwpLeosCfmMipEntry_Object = MibTableRow
wwpLeosCfmMipEntry = _WwpLeosCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1, 1)
)
wwpLeosCfmMipEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmMipVid"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmMipPort"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmMipEntry.setStatus("current")


class _WwpLeosCfmMipVid_Type(Integer32):
    """Custom type wwpLeosCfmMipVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosCfmMipVid_Type.__name__ = "Integer32"
_WwpLeosCfmMipVid_Object = MibTableColumn
wwpLeosCfmMipVid = _WwpLeosCfmMipVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1, 1, 1),
    _WwpLeosCfmMipVid_Type()
)
wwpLeosCfmMipVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipVid.setStatus("current")


class _WwpLeosCfmMipPort_Type(Integer32):
    """Custom type wwpLeosCfmMipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmMipPort_Type.__name__ = "Integer32"
_WwpLeosCfmMipPort_Object = MibTableColumn
wwpLeosCfmMipPort = _WwpLeosCfmMipPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1, 1, 2),
    _WwpLeosCfmMipPort_Type()
)
wwpLeosCfmMipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipPort.setStatus("current")


class _WwpLeosCfmMipLevel_Type(Integer32):
    """Custom type wwpLeosCfmMipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmMipLevel_Type.__name__ = "Integer32"
_WwpLeosCfmMipLevel_Object = MibTableColumn
wwpLeosCfmMipLevel = _WwpLeosCfmMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1, 1, 3),
    _WwpLeosCfmMipLevel_Type()
)
wwpLeosCfmMipLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMipLevel.setStatus("current")
_WwpLeosCfmMipStatus_Type = RowStatus
_WwpLeosCfmMipStatus_Object = MibTableColumn
wwpLeosCfmMipStatus = _WwpLeosCfmMipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 3, 1, 1, 4),
    _WwpLeosCfmMipStatus_Type()
)
wwpLeosCfmMipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMipStatus.setStatus("current")
_WwpLeosCfmLinkTrace_ObjectIdentity = ObjectIdentity
wwpLeosCfmLinkTrace = _WwpLeosCfmLinkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4)
)
_WwpLeosCfmLinkTraceMsgTable_Object = MibTable
wwpLeosCfmLinkTraceMsgTable = _WwpLeosCfmLinkTraceMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTable.setStatus("current")
_WwpLeosCfmLinkTraceMsgEntry_Object = MibTableRow
wwpLeosCfmLinkTraceMsgEntry = _WwpLeosCfmLinkTraceMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1)
)
wwpLeosCfmLinkTraceMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmLinkTraceMsgPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgEntry.setStatus("current")


class _WwpLeosCfmLinkTraceMsgPortId_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmLinkTraceMsgPortId_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgPortId_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgPortId = _WwpLeosCfmLinkTraceMsgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 1),
    _WwpLeosCfmLinkTraceMsgPortId_Type()
)
wwpLeosCfmLinkTraceMsgPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgPortId.setStatus("current")


class _WwpLeosCfmLinkTraceMsgTargetMEPID_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgTargetMEPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmLinkTraceMsgTargetMEPID_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgTargetMEPID = _WwpLeosCfmLinkTraceMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 2),
    _WwpLeosCfmLinkTraceMsgTargetMEPID_Type()
)
wwpLeosCfmLinkTraceMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTargetMEPID.setStatus("current")
_WwpLeosCfmLinkTraceMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmLinkTraceMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgTargetMacAddr = _WwpLeosCfmLinkTraceMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 3),
    _WwpLeosCfmLinkTraceMsgTargetMacAddr_Type()
)
wwpLeosCfmLinkTraceMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmLinkTraceMsgTTL_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosCfmLinkTraceMsgTTL_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgTTL_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgTTL = _WwpLeosCfmLinkTraceMsgTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 4),
    _WwpLeosCfmLinkTraceMsgTTL_Type()
)
wwpLeosCfmLinkTraceMsgTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTTL.setStatus("current")
_WwpLeosCfmLinkTraceMsgSequenceNumber_Type = Integer32
_WwpLeosCfmLinkTraceMsgSequenceNumber_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgSequenceNumber = _WwpLeosCfmLinkTraceMsgSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 5),
    _WwpLeosCfmLinkTraceMsgSequenceNumber_Type()
)
wwpLeosCfmLinkTraceMsgSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgSequenceNumber.setStatus("current")
_WwpLeosCfmLinkTraceMsgRowStatus_Type = RowStatus
_WwpLeosCfmLinkTraceMsgRowStatus_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgRowStatus = _WwpLeosCfmLinkTraceMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 6),
    _WwpLeosCfmLinkTraceMsgRowStatus_Type()
)
wwpLeosCfmLinkTraceMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgRowStatus.setStatus("current")


class _WwpLeosCfmLinkTraceMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmLinkTraceMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgPriority_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgPriority = _WwpLeosCfmLinkTraceMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 7),
    _WwpLeosCfmLinkTraceMsgPriority_Type()
)
wwpLeosCfmLinkTraceMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgPriority.setStatus("current")


class _WwpLeosCfmLinkTraceMsgServiceName_Type(DisplayString):
    """Custom type wwpLeosCfmLinkTraceMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmLinkTraceMsgServiceName_Type.__name__ = "DisplayString"
_WwpLeosCfmLinkTraceMsgServiceName_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgServiceName = _WwpLeosCfmLinkTraceMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 50),
    _WwpLeosCfmLinkTraceMsgServiceName_Type()
)
wwpLeosCfmLinkTraceMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgServiceName.setStatus("current")


class _WwpLeosCfmLinkTraceMsgSubPortName_Type(DisplayString):
    """Custom type wwpLeosCfmLinkTraceMsgSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmLinkTraceMsgSubPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmLinkTraceMsgSubPortName_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgSubPortName = _WwpLeosCfmLinkTraceMsgSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 52),
    _WwpLeosCfmLinkTraceMsgSubPortName_Type()
)
wwpLeosCfmLinkTraceMsgSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgSubPortName.setStatus("current")
_WwpLeosCfmLinkTraceMsgVsIndex_Type = Unsigned32
_WwpLeosCfmLinkTraceMsgVsIndex_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgVsIndex = _WwpLeosCfmLinkTraceMsgVsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 53),
    _WwpLeosCfmLinkTraceMsgVsIndex_Type()
)
wwpLeosCfmLinkTraceMsgVsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgVsIndex.setStatus("current")
_WwpLeosCfmLinkTraceMsgTotalTxLtm_Type = Unsigned32
_WwpLeosCfmLinkTraceMsgTotalTxLtm_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgTotalTxLtm = _WwpLeosCfmLinkTraceMsgTotalTxLtm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 54),
    _WwpLeosCfmLinkTraceMsgTotalTxLtm_Type()
)
wwpLeosCfmLinkTraceMsgTotalTxLtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTotalTxLtm.setStatus("current")
_WwpLeosCfmLinkTraceMsgTotalRxLtr_Type = Unsigned32
_WwpLeosCfmLinkTraceMsgTotalRxLtr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgTotalRxLtr = _WwpLeosCfmLinkTraceMsgTotalRxLtr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 1, 1, 55),
    _WwpLeosCfmLinkTraceMsgTotalRxLtr_Type()
)
wwpLeosCfmLinkTraceMsgTotalRxLtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgTotalRxLtr.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyTable_Object = MibTable
wwpLeosCfmLinkTraceMsgReplyTable = _WwpLeosCfmLinkTraceMsgReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyTable.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyEntry_Object = MibTableRow
wwpLeosCfmLinkTraceMsgReplyEntry = _WwpLeosCfmLinkTraceMsgReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1)
)
wwpLeosCfmLinkTraceMsgReplyEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmLinkTraceMsgPortId"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmLinkTraceMsgReplyTTL"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmLinkTraceMsgReplyTTLIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyEntry.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyTTL_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosCfmLinkTraceMsgReplyTTL_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyTTL_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyTTL = _WwpLeosCfmLinkTraceMsgReplyTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 1),
    _WwpLeosCfmLinkTraceMsgReplyTTL_Type()
)
wwpLeosCfmLinkTraceMsgReplyTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyTTL.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyTTLIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyTTLIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmLinkTraceMsgReplyTTLIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmLinkTraceMsgReplyTTLIndex_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyTTLIndex = _WwpLeosCfmLinkTraceMsgReplyTTLIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 2),
    _WwpLeosCfmLinkTraceMsgReplyTTLIndex_Type()
)
wwpLeosCfmLinkTraceMsgReplyTTLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyTTLIndex.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplySequenceNumber_Type = Integer32
_WwpLeosCfmLinkTraceMsgReplySequenceNumber_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplySequenceNumber = _WwpLeosCfmLinkTraceMsgReplySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 3),
    _WwpLeosCfmLinkTraceMsgReplySequenceNumber_Type()
)
wwpLeosCfmLinkTraceMsgReplySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplySequenceNumber.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyMPMacAddr_Type = MacAddress
_WwpLeosCfmLinkTraceMsgReplyMPMacAddr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyMPMacAddr = _WwpLeosCfmLinkTraceMsgReplyMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 4),
    _WwpLeosCfmLinkTraceMsgReplyMPMacAddr_Type()
)
wwpLeosCfmLinkTraceMsgReplyMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyMPMacAddr.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyMEPID_Type = Integer32
_WwpLeosCfmLinkTraceMsgReplyMEPID_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyMEPID = _WwpLeosCfmLinkTraceMsgReplyMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 5),
    _WwpLeosCfmLinkTraceMsgReplyMEPID_Type()
)
wwpLeosCfmLinkTraceMsgReplyMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyMEPID.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyTargetMacAddr_Type = MacAddress
_WwpLeosCfmLinkTraceMsgReplyTargetMacAddr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyTargetMacAddr = _WwpLeosCfmLinkTraceMsgReplyTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 6),
    _WwpLeosCfmLinkTraceMsgReplyTargetMacAddr_Type()
)
wwpLeosCfmLinkTraceMsgReplyTargetMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyTargetMacAddr.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyRelayAction_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyRelayAction based on Integer32"""
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
        *(("fdb", 3),
          ("hit", 6),
          ("invalid", 1),
          ("mpdb", 4),
          ("noLearn", 5),
          ("unknown", 2))
    )


_WwpLeosCfmLinkTraceMsgReplyRelayAction_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyRelayAction_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyRelayAction = _WwpLeosCfmLinkTraceMsgReplyRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 7),
    _WwpLeosCfmLinkTraceMsgReplyRelayAction_Type()
)
wwpLeosCfmLinkTraceMsgReplyRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyRelayAction.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyIngressPort_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyIngressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmLinkTraceMsgReplyIngressPort_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyIngressPort_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyIngressPort = _WwpLeosCfmLinkTraceMsgReplyIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 8),
    _WwpLeosCfmLinkTraceMsgReplyIngressPort_Type()
)
wwpLeosCfmLinkTraceMsgReplyIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyIngressPort.setStatus("obsolete")


class _WwpLeosCfmLinkTraceMsgReplyIngressAction_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyIngressAction based on Integer32"""
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
        *(("blocked", 2),
          ("down", 4),
          ("none", 5),
          ("ok", 1),
          ("vid", 3))
    )


_WwpLeosCfmLinkTraceMsgReplyIngressAction_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyIngressAction_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyIngressAction = _WwpLeosCfmLinkTraceMsgReplyIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 9),
    _WwpLeosCfmLinkTraceMsgReplyIngressAction_Type()
)
wwpLeosCfmLinkTraceMsgReplyIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyIngressAction.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyEgressPort_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmLinkTraceMsgReplyEgressPort_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyEgressPort_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyEgressPort = _WwpLeosCfmLinkTraceMsgReplyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 10),
    _WwpLeosCfmLinkTraceMsgReplyEgressPort_Type()
)
wwpLeosCfmLinkTraceMsgReplyEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyEgressPort.setStatus("obsolete")


class _WwpLeosCfmLinkTraceMsgReplyEgressAction_Type(Integer32):
    """Custom type wwpLeosCfmLinkTraceMsgReplyEgressAction based on Integer32"""
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
        *(("blocked", 4),
          ("down", 3),
          ("none", 1),
          ("ok", 6),
          ("ttl", 2),
          ("vid", 5))
    )


_WwpLeosCfmLinkTraceMsgReplyEgressAction_Type.__name__ = "Integer32"
_WwpLeosCfmLinkTraceMsgReplyEgressAction_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyEgressAction = _WwpLeosCfmLinkTraceMsgReplyEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 11),
    _WwpLeosCfmLinkTraceMsgReplyEgressAction_Type()
)
wwpLeosCfmLinkTraceMsgReplyEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyEgressAction.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyIngressPortStr_Type(DisplayString):
    """Custom type wwpLeosCfmLinkTraceMsgReplyIngressPortStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_WwpLeosCfmLinkTraceMsgReplyIngressPortStr_Type.__name__ = "DisplayString"
_WwpLeosCfmLinkTraceMsgReplyIngressPortStr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyIngressPortStr = _WwpLeosCfmLinkTraceMsgReplyIngressPortStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 12),
    _WwpLeosCfmLinkTraceMsgReplyIngressPortStr_Type()
)
wwpLeosCfmLinkTraceMsgReplyIngressPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyIngressPortStr.setStatus("current")


class _WwpLeosCfmLinkTraceMsgReplyEgressPortStr_Type(DisplayString):
    """Custom type wwpLeosCfmLinkTraceMsgReplyEgressPortStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_WwpLeosCfmLinkTraceMsgReplyEgressPortStr_Type.__name__ = "DisplayString"
_WwpLeosCfmLinkTraceMsgReplyEgressPortStr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyEgressPortStr = _WwpLeosCfmLinkTraceMsgReplyEgressPortStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 13),
    _WwpLeosCfmLinkTraceMsgReplyEgressPortStr_Type()
)
wwpLeosCfmLinkTraceMsgReplyEgressPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyEgressPortStr.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyIngressMacAddr_Type = MacAddress
_WwpLeosCfmLinkTraceMsgReplyIngressMacAddr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyIngressMacAddr = _WwpLeosCfmLinkTraceMsgReplyIngressMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 50),
    _WwpLeosCfmLinkTraceMsgReplyIngressMacAddr_Type()
)
wwpLeosCfmLinkTraceMsgReplyIngressMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyIngressMacAddr.setStatus("current")
_WwpLeosCfmLinkTraceMsgReplyEgressMacAddr_Type = MacAddress
_WwpLeosCfmLinkTraceMsgReplyEgressMacAddr_Object = MibTableColumn
wwpLeosCfmLinkTraceMsgReplyEgressMacAddr = _WwpLeosCfmLinkTraceMsgReplyEgressMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 4, 2, 1, 51),
    _WwpLeosCfmLinkTraceMsgReplyEgressMacAddr_Type()
)
wwpLeosCfmLinkTraceMsgReplyEgressMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLinkTraceMsgReplyEgressMacAddr.setStatus("current")
_WwpLeosCfmLoopback_ObjectIdentity = ObjectIdentity
wwpLeosCfmLoopback = _WwpLeosCfmLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5)
)
_WwpLeosCfmLoopbackMsgTable_Object = MibTable
wwpLeosCfmLoopbackMsgTable = _WwpLeosCfmLoopbackMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgTable.setStatus("current")
_WwpLeosCfmLoopbackMsgEntry_Object = MibTableRow
wwpLeosCfmLoopbackMsgEntry = _WwpLeosCfmLoopbackMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1)
)
wwpLeosCfmLoopbackMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmLoopbackMsgPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgEntry.setStatus("current")


class _WwpLeosCfmLoopbackMsgPortId_Type(Integer32):
    """Custom type wwpLeosCfmLoopbackMsgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmLoopbackMsgPortId_Type.__name__ = "Integer32"
_WwpLeosCfmLoopbackMsgPortId_Object = MibTableColumn
wwpLeosCfmLoopbackMsgPortId = _WwpLeosCfmLoopbackMsgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 1),
    _WwpLeosCfmLoopbackMsgPortId_Type()
)
wwpLeosCfmLoopbackMsgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgPortId.setStatus("current")


class _WwpLeosCfmLoopbackMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmLoopbackMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmLoopbackMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmLoopbackMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmLoopbackMsgTargetMEPID = _WwpLeosCfmLoopbackMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 2),
    _WwpLeosCfmLoopbackMsgTargetMEPID_Type()
)
wwpLeosCfmLoopbackMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgTargetMEPID.setStatus("current")
_WwpLeosCfmLoopbackMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmLoopbackMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmLoopbackMsgTargetMacAddr = _WwpLeosCfmLoopbackMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 3),
    _WwpLeosCfmLoopbackMsgTargetMacAddr_Type()
)
wwpLeosCfmLoopbackMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmLoopbackMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmLoopbackMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosCfmLoopbackMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmLoopbackMsgCount_Object = MibTableColumn
wwpLeosCfmLoopbackMsgCount = _WwpLeosCfmLoopbackMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 4),
    _WwpLeosCfmLoopbackMsgCount_Type()
)
wwpLeosCfmLoopbackMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgCount.setStatus("current")


class _WwpLeosCfmLoopbackMsgData_Type(DisplayString):
    """Custom type wwpLeosCfmLoopbackMsgData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_WwpLeosCfmLoopbackMsgData_Type.__name__ = "DisplayString"
_WwpLeosCfmLoopbackMsgData_Object = MibTableColumn
wwpLeosCfmLoopbackMsgData = _WwpLeosCfmLoopbackMsgData_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 5),
    _WwpLeosCfmLoopbackMsgData_Type()
)
wwpLeosCfmLoopbackMsgData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgData.setStatus("current")


class _WwpLeosCfmLoopbackMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmLoopbackMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmLoopbackMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmLoopbackMsgPriority_Object = MibTableColumn
wwpLeosCfmLoopbackMsgPriority = _WwpLeosCfmLoopbackMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 6),
    _WwpLeosCfmLoopbackMsgPriority_Type()
)
wwpLeosCfmLoopbackMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgPriority.setStatus("current")
_WwpLeosCfmLoopbackMsgRowStatus_Type = RowStatus
_WwpLeosCfmLoopbackMsgRowStatus_Object = MibTableColumn
wwpLeosCfmLoopbackMsgRowStatus = _WwpLeosCfmLoopbackMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 7),
    _WwpLeosCfmLoopbackMsgRowStatus_Type()
)
wwpLeosCfmLoopbackMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgRowStatus.setStatus("current")


class _WwpLeosCfmLoopbackMsgDefaultInterval_Type(Integer32):
    """Custom type wwpLeosCfmLoopbackMsgDefaultInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_WwpLeosCfmLoopbackMsgDefaultInterval_Type.__name__ = "Integer32"
_WwpLeosCfmLoopbackMsgDefaultInterval_Object = MibTableColumn
wwpLeosCfmLoopbackMsgDefaultInterval = _WwpLeosCfmLoopbackMsgDefaultInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 8),
    _WwpLeosCfmLoopbackMsgDefaultInterval_Type()
)
wwpLeosCfmLoopbackMsgDefaultInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgDefaultInterval.setStatus("current")


class _WwpLeosCfmLoopbackMsgDefaultTimeout_Type(Integer32):
    """Custom type wwpLeosCfmLoopbackMsgDefaultTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10000),
    )


_WwpLeosCfmLoopbackMsgDefaultTimeout_Type.__name__ = "Integer32"
_WwpLeosCfmLoopbackMsgDefaultTimeout_Object = MibTableColumn
wwpLeosCfmLoopbackMsgDefaultTimeout = _WwpLeosCfmLoopbackMsgDefaultTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 5, 1, 1, 9),
    _WwpLeosCfmLoopbackMsgDefaultTimeout_Type()
)
wwpLeosCfmLoopbackMsgDefaultTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmLoopbackMsgDefaultTimeout.setStatus("current")
_WwpLeosCfmMaintenance_ObjectIdentity = ObjectIdentity
wwpLeosCfmMaintenance = _WwpLeosCfmMaintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6)
)
_WwpLeosCfmMaintenanceDomainTable_Object = MibTable
wwpLeosCfmMaintenanceDomainTable = _WwpLeosCfmMaintenanceDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainTable.setStatus("current")
_WwpLeosCfmMaintenanceDomainEntry_Object = MibTableRow
wwpLeosCfmMaintenanceDomainEntry = _WwpLeosCfmMaintenanceDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1)
)
wwpLeosCfmMaintenanceDomainEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmMaintenanceDomainIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainEntry.setStatus("current")
_WwpLeosCfmMaintenanceDomainIndex_Type = Unsigned32
_WwpLeosCfmMaintenanceDomainIndex_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainIndex = _WwpLeosCfmMaintenanceDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 1),
    _WwpLeosCfmMaintenanceDomainIndex_Type()
)
wwpLeosCfmMaintenanceDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainIndex.setStatus("current")


class _WwpLeosCfmMaintenanceDomainLevel_Type(Integer32):
    """Custom type wwpLeosCfmMaintenanceDomainLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmMaintenanceDomainLevel_Type.__name__ = "Integer32"
_WwpLeosCfmMaintenanceDomainLevel_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainLevel = _WwpLeosCfmMaintenanceDomainLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 2),
    _WwpLeosCfmMaintenanceDomainLevel_Type()
)
wwpLeosCfmMaintenanceDomainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainLevel.setStatus("current")


class _WwpLeosCfmMaintenanceDomainName_Type(DisplayString):
    """Custom type wwpLeosCfmMaintenanceDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmMaintenanceDomainName_Type.__name__ = "DisplayString"
_WwpLeosCfmMaintenanceDomainName_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainName = _WwpLeosCfmMaintenanceDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 3),
    _WwpLeosCfmMaintenanceDomainName_Type()
)
wwpLeosCfmMaintenanceDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainName.setStatus("current")
_WwpLeosCfmMaintenanceDomainServiceCount_Type = Unsigned32
_WwpLeosCfmMaintenanceDomainServiceCount_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainServiceCount = _WwpLeosCfmMaintenanceDomainServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 4),
    _WwpLeosCfmMaintenanceDomainServiceCount_Type()
)
wwpLeosCfmMaintenanceDomainServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainServiceCount.setStatus("current")


class _WwpLeosCfmMaintenanceDomainMdFormat_Type(Dot1agCfmMaintDomainNameType):
    """Custom type wwpLeosCfmMaintenanceDomainMdFormat based on Dot1agCfmMaintDomainNameType"""


_WwpLeosCfmMaintenanceDomainMdFormat_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainMdFormat = _WwpLeosCfmMaintenanceDomainMdFormat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 5),
    _WwpLeosCfmMaintenanceDomainMdFormat_Type()
)
wwpLeosCfmMaintenanceDomainMdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainMdFormat.setStatus("current")
_WwpLeosCfmMaintenanceDomainMdName_Type = Dot1agCfmMaintDomainName
_WwpLeosCfmMaintenanceDomainMdName_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainMdName = _WwpLeosCfmMaintenanceDomainMdName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 6),
    _WwpLeosCfmMaintenanceDomainMdName_Type()
)
wwpLeosCfmMaintenanceDomainMdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainMdName.setStatus("current")
_WwpLeosCfmMaintenanceDomainStatus_Type = RowStatus
_WwpLeosCfmMaintenanceDomainStatus_Object = MibTableColumn
wwpLeosCfmMaintenanceDomainStatus = _WwpLeosCfmMaintenanceDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 6, 1, 1, 7),
    _WwpLeosCfmMaintenanceDomainStatus_Type()
)
wwpLeosCfmMaintenanceDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMaintenanceDomainStatus.setStatus("current")
_WwpLeosCfmMEP_ObjectIdentity = ObjectIdentity
wwpLeosCfmMEP = _WwpLeosCfmMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7)
)
_WwpLeosCfmMEPTable_Object = MibTable
wwpLeosCfmMEPTable = _WwpLeosCfmMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmMEPTable.setStatus("current")
_WwpLeosCfmMEPEntry_Object = MibTableRow
wwpLeosCfmMEPEntry = _WwpLeosCfmMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1)
)
wwpLeosCfmMEPEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmMEPPort"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmMEPEntry.setStatus("current")


class _WwpLeosCfmMEPPort_Type(Integer32):
    """Custom type wwpLeosCfmMEPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmMEPPort_Type.__name__ = "Integer32"
_WwpLeosCfmMEPPort_Object = MibTableColumn
wwpLeosCfmMEPPort = _WwpLeosCfmMEPPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 1),
    _WwpLeosCfmMEPPort_Type()
)
wwpLeosCfmMEPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPPort.setStatus("current")


class _WwpLeosCfmMEPAdminState_Type(Integer32):
    """Custom type wwpLeosCfmMEPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmMEPAdminState_Type.__name__ = "Integer32"
_WwpLeosCfmMEPAdminState_Object = MibTableColumn
wwpLeosCfmMEPAdminState = _WwpLeosCfmMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 2),
    _WwpLeosCfmMEPAdminState_Type()
)
wwpLeosCfmMEPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPAdminState.setStatus("current")


class _WwpLeosCfmMEPOperState_Type(Integer32):
    """Custom type wwpLeosCfmMEPOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmMEPOperState_Type.__name__ = "Integer32"
_WwpLeosCfmMEPOperState_Object = MibTableColumn
wwpLeosCfmMEPOperState = _WwpLeosCfmMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 3),
    _WwpLeosCfmMEPOperState_Type()
)
wwpLeosCfmMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPOperState.setStatus("obsolete")


class _WwpLeosCfmMEPDirection_Type(Integer32):
    """Custom type wwpLeosCfmMEPDirection based on Integer32"""
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


_WwpLeosCfmMEPDirection_Type.__name__ = "Integer32"
_WwpLeosCfmMEPDirection_Object = MibTableColumn
wwpLeosCfmMEPDirection = _WwpLeosCfmMEPDirection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 4),
    _WwpLeosCfmMEPDirection_Type()
)
wwpLeosCfmMEPDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDirection.setStatus("current")


class _WwpLeosCfmMEPCCMState_Type(Integer32):
    """Custom type wwpLeosCfmMEPCCMState based on Integer32"""
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


_WwpLeosCfmMEPCCMState_Type.__name__ = "Integer32"
_WwpLeosCfmMEPCCMState_Object = MibTableColumn
wwpLeosCfmMEPCCMState = _WwpLeosCfmMEPCCMState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 5),
    _WwpLeosCfmMEPCCMState_Type()
)
wwpLeosCfmMEPCCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPCCMState.setStatus("current")


class _WwpLeosCfmMEPCCMPriority_Type(Integer32):
    """Custom type wwpLeosCfmMEPCCMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmMEPCCMPriority_Type.__name__ = "Integer32"
_WwpLeosCfmMEPCCMPriority_Object = MibTableColumn
wwpLeosCfmMEPCCMPriority = _WwpLeosCfmMEPCCMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 6),
    _WwpLeosCfmMEPCCMPriority_Type()
)
wwpLeosCfmMEPCCMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPCCMPriority.setStatus("current")


class _WwpLeosCfmMEPLTMPriority_Type(Integer32):
    """Custom type wwpLeosCfmMEPLTMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmMEPLTMPriority_Type.__name__ = "Integer32"
_WwpLeosCfmMEPLTMPriority_Object = MibTableColumn
wwpLeosCfmMEPLTMPriority = _WwpLeosCfmMEPLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 7),
    _WwpLeosCfmMEPLTMPriority_Type()
)
wwpLeosCfmMEPLTMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLTMPriority.setStatus("obsolete")


class _WwpLeosCfmMEPId_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmMEPId_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPId_Object = MibTableColumn
wwpLeosCfmMEPId = _WwpLeosCfmMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 8),
    _WwpLeosCfmMEPId_Type()
)
wwpLeosCfmMEPId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPId.setStatus("current")
_WwpLeosCfmMEPMacAddr_Type = MacAddress
_WwpLeosCfmMEPMacAddr_Object = MibTableColumn
wwpLeosCfmMEPMacAddr = _WwpLeosCfmMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 9),
    _WwpLeosCfmMEPMacAddr_Type()
)
wwpLeosCfmMEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPMacAddr.setStatus("current")
_WwpLeosCfmMEPNextLbmSeqNumber_Type = Counter32
_WwpLeosCfmMEPNextLbmSeqNumber_Object = MibTableColumn
wwpLeosCfmMEPNextLbmSeqNumber = _WwpLeosCfmMEPNextLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 10),
    _WwpLeosCfmMEPNextLbmSeqNumber_Type()
)
wwpLeosCfmMEPNextLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNextLbmSeqNumber.setStatus("current")
_WwpLeosCfmMEPRxValidInOrderLoopbackReply_Type = Counter32
_WwpLeosCfmMEPRxValidInOrderLoopbackReply_Object = MibTableColumn
wwpLeosCfmMEPRxValidInOrderLoopbackReply = _WwpLeosCfmMEPRxValidInOrderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 11),
    _WwpLeosCfmMEPRxValidInOrderLoopbackReply_Type()
)
wwpLeosCfmMEPRxValidInOrderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPRxValidInOrderLoopbackReply.setStatus("current")
_WwpLeosCfmMEPRxValidOutOrderLoopbackReply_Type = Counter32
_WwpLeosCfmMEPRxValidOutOrderLoopbackReply_Object = MibTableColumn
wwpLeosCfmMEPRxValidOutOrderLoopbackReply = _WwpLeosCfmMEPRxValidOutOrderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 12),
    _WwpLeosCfmMEPRxValidOutOrderLoopbackReply_Type()
)
wwpLeosCfmMEPRxValidOutOrderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPRxValidOutOrderLoopbackReply.setStatus("current")
_WwpLeosCfmMEPNextLTMSeqNumber_Type = Counter32
_WwpLeosCfmMEPNextLTMSeqNumber_Object = MibTableColumn
wwpLeosCfmMEPNextLTMSeqNumber = _WwpLeosCfmMEPNextLTMSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 13),
    _WwpLeosCfmMEPNextLTMSeqNumber_Type()
)
wwpLeosCfmMEPNextLTMSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNextLTMSeqNumber.setStatus("current")
_WwpLeosCfmMEPNumLoopbackRepliesTxmt_Type = Counter32
_WwpLeosCfmMEPNumLoopbackRepliesTxmt_Object = MibTableColumn
wwpLeosCfmMEPNumLoopbackRepliesTxmt = _WwpLeosCfmMEPNumLoopbackRepliesTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 14),
    _WwpLeosCfmMEPNumLoopbackRepliesTxmt_Type()
)
wwpLeosCfmMEPNumLoopbackRepliesTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLoopbackRepliesTxmt.setStatus("current")
_WwpLeosCfmMEPNumLTMReceived_Type = Counter32
_WwpLeosCfmMEPNumLTMReceived_Object = MibTableColumn
wwpLeosCfmMEPNumLTMReceived = _WwpLeosCfmMEPNumLTMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 15),
    _WwpLeosCfmMEPNumLTMReceived_Type()
)
wwpLeosCfmMEPNumLTMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLTMReceived.setStatus("current")
_WwpLeosCfmMEPNumLTMTxmt_Type = Counter32
_WwpLeosCfmMEPNumLTMTxmt_Object = MibTableColumn
wwpLeosCfmMEPNumLTMTxmt = _WwpLeosCfmMEPNumLTMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 16),
    _WwpLeosCfmMEPNumLTMTxmt_Type()
)
wwpLeosCfmMEPNumLTMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLTMTxmt.setStatus("current")
_WwpLeosCfmMEPNumCCMTxmt_Type = Counter32
_WwpLeosCfmMEPNumCCMTxmt_Object = MibTableColumn
wwpLeosCfmMEPNumCCMTxmt = _WwpLeosCfmMEPNumCCMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 17),
    _WwpLeosCfmMEPNumCCMTxmt_Type()
)
wwpLeosCfmMEPNumCCMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumCCMTxmt.setStatus("current")
_WwpLeosCfmMEPRowStatus_Type = RowStatus
_WwpLeosCfmMEPRowStatus_Object = MibTableColumn
wwpLeosCfmMEPRowStatus = _WwpLeosCfmMEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 18),
    _WwpLeosCfmMEPRowStatus_Type()
)
wwpLeosCfmMEPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPRowStatus.setStatus("current")
_WwpLeosCfmMEPNumDMMSent_Type = Counter32
_WwpLeosCfmMEPNumDMMSent_Object = MibTableColumn
wwpLeosCfmMEPNumDMMSent = _WwpLeosCfmMEPNumDMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 19),
    _WwpLeosCfmMEPNumDMMSent_Type()
)
wwpLeosCfmMEPNumDMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumDMMSent.setStatus("current")
_WwpLeosCfmMEPDMMDelay_Type = Counter32
_WwpLeosCfmMEPDMMDelay_Object = MibTableColumn
wwpLeosCfmMEPDMMDelay = _WwpLeosCfmMEPDMMDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 20),
    _WwpLeosCfmMEPDMMDelay_Type()
)
wwpLeosCfmMEPDMMDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMDelay.setStatus("current")
_WwpLeosCfmMEPDMMJitter_Type = Counter32
_WwpLeosCfmMEPDMMJitter_Object = MibTableColumn
wwpLeosCfmMEPDMMJitter = _WwpLeosCfmMEPDMMJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 21),
    _WwpLeosCfmMEPDMMJitter_Type()
)
wwpLeosCfmMEPDMMJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMJitter.setStatus("current")
_WwpLeosCfmMEPNumLMMSent_Type = Counter32
_WwpLeosCfmMEPNumLMMSent_Object = MibTableColumn
wwpLeosCfmMEPNumLMMSent = _WwpLeosCfmMEPNumLMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 22),
    _WwpLeosCfmMEPNumLMMSent_Type()
)
wwpLeosCfmMEPNumLMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLMMSent.setStatus("current")
_WwpLeosCfmMEPLMMFrameLossNear_Type = Counter32
_WwpLeosCfmMEPLMMFrameLossNear_Object = MibTableColumn
wwpLeosCfmMEPLMMFrameLossNear = _WwpLeosCfmMEPLMMFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 23),
    _WwpLeosCfmMEPLMMFrameLossNear_Type()
)
wwpLeosCfmMEPLMMFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLMMFrameLossNear.setStatus("current")
_WwpLeosCfmMEPLMMFrameLossFar_Type = Counter32
_WwpLeosCfmMEPLMMFrameLossFar_Object = MibTableColumn
wwpLeosCfmMEPLMMFrameLossFar = _WwpLeosCfmMEPLMMFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 24),
    _WwpLeosCfmMEPLMMFrameLossFar_Type()
)
wwpLeosCfmMEPLMMFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLMMFrameLossFar.setStatus("current")
_WwpLeosCfmMEPNumLMRReceived_Type = Counter32
_WwpLeosCfmMEPNumLMRReceived_Object = MibTableColumn
wwpLeosCfmMEPNumLMRReceived = _WwpLeosCfmMEPNumLMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 25),
    _WwpLeosCfmMEPNumLMRReceived_Type()
)
wwpLeosCfmMEPNumLMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLMRReceived.setStatus("current")
_WwpLeosCfmMEPNumDMRReceived_Type = Counter32
_WwpLeosCfmMEPNumDMRReceived_Object = MibTableColumn
wwpLeosCfmMEPNumDMRReceived = _WwpLeosCfmMEPNumDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 26),
    _WwpLeosCfmMEPNumDMRReceived_Type()
)
wwpLeosCfmMEPNumDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumDMRReceived.setStatus("current")
_WwpLeosCfmMEPDMMMinDelay_Type = Counter32
_WwpLeosCfmMEPDMMMinDelay_Object = MibTableColumn
wwpLeosCfmMEPDMMMinDelay = _WwpLeosCfmMEPDMMMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 27),
    _WwpLeosCfmMEPDMMMinDelay_Type()
)
wwpLeosCfmMEPDMMMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMMinDelay.setStatus("current")
_WwpLeosCfmMEPDMMMaxDelay_Type = Counter32
_WwpLeosCfmMEPDMMMaxDelay_Object = MibTableColumn
wwpLeosCfmMEPDMMMaxDelay = _WwpLeosCfmMEPDMMMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 28),
    _WwpLeosCfmMEPDMMMaxDelay_Type()
)
wwpLeosCfmMEPDMMMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMMaxDelay.setStatus("current")
_WwpLeosCfmMEPDMMMinJitter_Type = Counter32
_WwpLeosCfmMEPDMMMinJitter_Object = MibTableColumn
wwpLeosCfmMEPDMMMinJitter = _WwpLeosCfmMEPDMMMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 29),
    _WwpLeosCfmMEPDMMMinJitter_Type()
)
wwpLeosCfmMEPDMMMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMMinJitter.setStatus("current")
_WwpLeosCfmMEPDMMMaxJitter_Type = Counter32
_WwpLeosCfmMEPDMMMaxJitter_Object = MibTableColumn
wwpLeosCfmMEPDMMMaxJitter = _WwpLeosCfmMEPDMMMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 30),
    _WwpLeosCfmMEPDMMMaxJitter_Type()
)
wwpLeosCfmMEPDMMMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPDMMMaxJitter.setStatus("current")


class _WwpLeosCfmMEPServiceName_Type(DisplayString):
    """Custom type wwpLeosCfmMEPServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmMEPServiceName_Type.__name__ = "DisplayString"
_WwpLeosCfmMEPServiceName_Object = MibTableColumn
wwpLeosCfmMEPServiceName = _WwpLeosCfmMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 50),
    _WwpLeosCfmMEPServiceName_Type()
)
wwpLeosCfmMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPServiceName.setStatus("current")


class _WwpLeosCfmMEPSubPortName_Type(DisplayString):
    """Custom type wwpLeosCfmMEPSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmMEPSubPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmMEPSubPortName_Object = MibTableColumn
wwpLeosCfmMEPSubPortName = _WwpLeosCfmMEPSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 51),
    _WwpLeosCfmMEPSubPortName_Type()
)
wwpLeosCfmMEPSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPSubPortName.setStatus("current")


class _WwpLeosCfmMEPVsPbtName_Type(DisplayString):
    """Custom type wwpLeosCfmMEPVsPbtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmMEPVsPbtName_Type.__name__ = "DisplayString"
_WwpLeosCfmMEPVsPbtName_Object = MibTableColumn
wwpLeosCfmMEPVsPbtName = _WwpLeosCfmMEPVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 52),
    _WwpLeosCfmMEPVsPbtName_Type()
)
wwpLeosCfmMEPVsPbtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPVsPbtName.setStatus("current")


class _WwpLeosCfmMEPLogicalPortName_Type(DisplayString):
    """Custom type wwpLeosCfmMEPLogicalPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmMEPLogicalPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmMEPLogicalPortName_Object = MibTableColumn
wwpLeosCfmMEPLogicalPortName = _WwpLeosCfmMEPLogicalPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 53),
    _WwpLeosCfmMEPLogicalPortName_Type()
)
wwpLeosCfmMEPLogicalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLogicalPortName.setStatus("current")
_WwpLeosCfmMEPSubPortIndex_Type = Unsigned32
_WwpLeosCfmMEPSubPortIndex_Object = MibTableColumn
wwpLeosCfmMEPSubPortIndex = _WwpLeosCfmMEPSubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 54),
    _WwpLeosCfmMEPSubPortIndex_Type()
)
wwpLeosCfmMEPSubPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPSubPortIndex.setStatus("current")


class _WwpLeosCfmMEPEncapsulation_Type(Integer32):
    """Custom type wwpLeosCfmMEPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1d", 1),
          ("pbtCfmEncap", 2))
    )


_WwpLeosCfmMEPEncapsulation_Type.__name__ = "Integer32"
_WwpLeosCfmMEPEncapsulation_Object = MibTableColumn
wwpLeosCfmMEPEncapsulation = _WwpLeosCfmMEPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 55),
    _WwpLeosCfmMEPEncapsulation_Type()
)
wwpLeosCfmMEPEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPEncapsulation.setStatus("current")


class _WwpLeosCfmMEPLeadPortBayIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPLeadPortBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmMEPLeadPortBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPLeadPortBayIndex_Object = MibTableColumn
wwpLeosCfmMEPLeadPortBayIndex = _WwpLeosCfmMEPLeadPortBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 56),
    _WwpLeosCfmMEPLeadPortBayIndex_Type()
)
wwpLeosCfmMEPLeadPortBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLeadPortBayIndex.setStatus("current")


class _WwpLeosCfmMEPLeadPortShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPLeadPortShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmMEPLeadPortShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPLeadPortShelfIndex_Object = MibTableColumn
wwpLeosCfmMEPLeadPortShelfIndex = _WwpLeosCfmMEPLeadPortShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 57),
    _WwpLeosCfmMEPLeadPortShelfIndex_Type()
)
wwpLeosCfmMEPLeadPortShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLeadPortShelfIndex.setStatus("current")


class _WwpLeosCfmMEPLeadPortModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPLeadPortModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosCfmMEPLeadPortModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPLeadPortModuleIndex_Object = MibTableColumn
wwpLeosCfmMEPLeadPortModuleIndex = _WwpLeosCfmMEPLeadPortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 58),
    _WwpLeosCfmMEPLeadPortModuleIndex_Type()
)
wwpLeosCfmMEPLeadPortModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPLeadPortModuleIndex.setStatus("current")


class _WwpLeosCfmMEPPBTBvid_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPPBTBvid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmMEPPBTBvid_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPPBTBvid_Object = MibTableColumn
wwpLeosCfmMEPPBTBvid = _WwpLeosCfmMEPPBTBvid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 59),
    _WwpLeosCfmMEPPBTBvid_Type()
)
wwpLeosCfmMEPPBTBvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPPBTBvid.setStatus("current")


class _WwpLeosCfmMEPPBTEtype_Type(Unsigned32):
    """Custom type wwpLeosCfmMEPPBTEtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmMEPPBTEtype_Type.__name__ = "Unsigned32"
_WwpLeosCfmMEPPBTEtype_Object = MibTableColumn
wwpLeosCfmMEPPBTEtype = _WwpLeosCfmMEPPBTEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 60),
    _WwpLeosCfmMEPPBTEtype_Type()
)
wwpLeosCfmMEPPBTEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPPBTEtype.setStatus("current")
_WwpLeosCfmMEPNumLbmTxmt_Type = Counter32
_WwpLeosCfmMEPNumLbmTxmt_Object = MibTableColumn
wwpLeosCfmMEPNumLbmTxmt = _WwpLeosCfmMEPNumLbmTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 61),
    _WwpLeosCfmMEPNumLbmTxmt_Type()
)
wwpLeosCfmMEPNumLbmTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLbmTxmt.setStatus("current")
_WwpLeosCfmMEPNumLbmReceived_Type = Counter32
_WwpLeosCfmMEPNumLbmReceived_Object = MibTableColumn
wwpLeosCfmMEPNumLbmReceived = _WwpLeosCfmMEPNumLbmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 62),
    _WwpLeosCfmMEPNumLbmReceived_Type()
)
wwpLeosCfmMEPNumLbmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLbmReceived.setStatus("current")
_WwpLeosCfmMEPNumLoopbackRepliesReceived_Type = Counter32
_WwpLeosCfmMEPNumLoopbackRepliesReceived_Object = MibTableColumn
wwpLeosCfmMEPNumLoopbackRepliesReceived = _WwpLeosCfmMEPNumLoopbackRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 63),
    _WwpLeosCfmMEPNumLoopbackRepliesReceived_Type()
)
wwpLeosCfmMEPNumLoopbackRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLoopbackRepliesReceived.setStatus("current")
_WwpLeosCfmMEPNumLTRepliesTxmt_Type = Counter32
_WwpLeosCfmMEPNumLTRepliesTxmt_Object = MibTableColumn
wwpLeosCfmMEPNumLTRepliesTxmt = _WwpLeosCfmMEPNumLTRepliesTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 64),
    _WwpLeosCfmMEPNumLTRepliesTxmt_Type()
)
wwpLeosCfmMEPNumLTRepliesTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLTRepliesTxmt.setStatus("current")
_WwpLeosCfmMEPNumLTRepliesReceived_Type = Counter32
_WwpLeosCfmMEPNumLTRepliesReceived_Object = MibTableColumn
wwpLeosCfmMEPNumLTRepliesReceived = _WwpLeosCfmMEPNumLTRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 65),
    _WwpLeosCfmMEPNumLTRepliesReceived_Type()
)
wwpLeosCfmMEPNumLTRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumLTRepliesReceived.setStatus("current")
_WwpLeosCfmMEPNumUnexpectedLTRepliesReceived_Type = Counter32
_WwpLeosCfmMEPNumUnexpectedLTRepliesReceived_Object = MibTableColumn
wwpLeosCfmMEPNumUnexpectedLTRepliesReceived = _WwpLeosCfmMEPNumUnexpectedLTRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 66),
    _WwpLeosCfmMEPNumUnexpectedLTRepliesReceived_Type()
)
wwpLeosCfmMEPNumUnexpectedLTRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumUnexpectedLTRepliesReceived.setStatus("current")
_WwpLeosCfmMEPNumCCMReceived_Type = Counter32
_WwpLeosCfmMEPNumCCMReceived_Object = MibTableColumn
wwpLeosCfmMEPNumCCMReceived = _WwpLeosCfmMEPNumCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 7, 1, 1, 67),
    _WwpLeosCfmMEPNumCCMReceived_Type()
)
wwpLeosCfmMEPNumCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMEPNumCCMReceived.setStatus("current")
_WwpLeosCfmRemoteMEP_ObjectIdentity = ObjectIdentity
wwpLeosCfmRemoteMEP = _WwpLeosCfmRemoteMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8)
)
_WwpLeosCfmRemoteMEPTable_Object = MibTable
wwpLeosCfmRemoteMEPTable = _WwpLeosCfmRemoteMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPTable.setStatus("current")
_WwpLeosCfmRemoteMEPEntry_Object = MibTableRow
wwpLeosCfmRemoteMEPEntry = _WwpLeosCfmRemoteMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1)
)
wwpLeosCfmRemoteMEPEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPID"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPEntry.setStatus("current")


class _WwpLeosCfmRemoteMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosCfmRemoteMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPID_Object = MibTableColumn
wwpLeosCfmRemoteMEPID = _WwpLeosCfmRemoteMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 1),
    _WwpLeosCfmRemoteMEPID_Type()
)
wwpLeosCfmRemoteMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPID.setStatus("current")


class _WwpLeosCfmRemoteMEPAdminState_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmRemoteMEPAdminState_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPAdminState_Object = MibTableColumn
wwpLeosCfmRemoteMEPAdminState = _WwpLeosCfmRemoteMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 2),
    _WwpLeosCfmRemoteMEPAdminState_Type()
)
wwpLeosCfmRemoteMEPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPAdminState.setStatus("current")


class _WwpLeosCfmRemoteMEPOperState_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPOperState based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("hold", 3),
          ("holdLocked", 4))
    )


_WwpLeosCfmRemoteMEPOperState_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPOperState_Object = MibTableColumn
wwpLeosCfmRemoteMEPOperState = _WwpLeosCfmRemoteMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 3),
    _WwpLeosCfmRemoteMEPOperState_Type()
)
wwpLeosCfmRemoteMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPOperState.setStatus("current")
_WwpLeosCfmRemoteMEPTime_Type = TimeTicks
_WwpLeosCfmRemoteMEPTime_Object = MibTableColumn
wwpLeosCfmRemoteMEPTime = _WwpLeosCfmRemoteMEPTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 4),
    _WwpLeosCfmRemoteMEPTime_Type()
)
wwpLeosCfmRemoteMEPTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPTime.setStatus("current")
_WwpLeosCfmRemoteMEPMacAddr_Type = MacAddress
_WwpLeosCfmRemoteMEPMacAddr_Object = MibTableColumn
wwpLeosCfmRemoteMEPMacAddr = _WwpLeosCfmRemoteMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 5),
    _WwpLeosCfmRemoteMEPMacAddr_Type()
)
wwpLeosCfmRemoteMEPMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPMacAddr.setStatus("current")
_WwpLeosCfmRemoteMEPKLastMacStatus_Type = TruthValue
_WwpLeosCfmRemoteMEPKLastMacStatus_Object = MibTableColumn
wwpLeosCfmRemoteMEPKLastMacStatus = _WwpLeosCfmRemoteMEPKLastMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 6),
    _WwpLeosCfmRemoteMEPKLastMacStatus_Type()
)
wwpLeosCfmRemoteMEPKLastMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPKLastMacStatus.setStatus("current")
_WwpLeosCfmRemoteMEPFailureFlag_Type = TruthValue
_WwpLeosCfmRemoteMEPFailureFlag_Object = MibTableColumn
wwpLeosCfmRemoteMEPFailureFlag = _WwpLeosCfmRemoteMEPFailureFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 7),
    _WwpLeosCfmRemoteMEPFailureFlag_Type()
)
wwpLeosCfmRemoteMEPFailureFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPFailureFlag.setStatus("current")
_WwpLeosCfmRemoteMEPCCMErrorFlag_Type = TruthValue
_WwpLeosCfmRemoteMEPCCMErrorFlag_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMErrorFlag = _WwpLeosCfmRemoteMEPCCMErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 8),
    _WwpLeosCfmRemoteMEPCCMErrorFlag_Type()
)
wwpLeosCfmRemoteMEPCCMErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMErrorFlag.setStatus("current")
_WwpLeosCfmRemoteMEPRDIErrorFlag_Type = TruthValue
_WwpLeosCfmRemoteMEPRDIErrorFlag_Object = MibTableColumn
wwpLeosCfmRemoteMEPRDIErrorFlag = _WwpLeosCfmRemoteMEPRDIErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 9),
    _WwpLeosCfmRemoteMEPRDIErrorFlag_Type()
)
wwpLeosCfmRemoteMEPRDIErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPRDIErrorFlag.setStatus("current")
_WwpLeosCfmRemoteMEPNumCCMRx_Type = Counter32
_WwpLeosCfmRemoteMEPNumCCMRx_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumCCMRx = _WwpLeosCfmRemoteMEPNumCCMRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 10),
    _WwpLeosCfmRemoteMEPNumCCMRx_Type()
)
wwpLeosCfmRemoteMEPNumCCMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumCCMRx.setStatus("current")
_WwpLeosCfmRemoteMEPNumDMMSent_Type = Counter32
_WwpLeosCfmRemoteMEPNumDMMSent_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumDMMSent = _WwpLeosCfmRemoteMEPNumDMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 11),
    _WwpLeosCfmRemoteMEPNumDMMSent_Type()
)
wwpLeosCfmRemoteMEPNumDMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumDMMSent.setStatus("current")
_WwpLeosCfmRemoteMEPDelay_Type = Counter32
_WwpLeosCfmRemoteMEPDelay_Object = MibTableColumn
wwpLeosCfmRemoteMEPDelay = _WwpLeosCfmRemoteMEPDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 12),
    _WwpLeosCfmRemoteMEPDelay_Type()
)
wwpLeosCfmRemoteMEPDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPDelay.setStatus("current")
_WwpLeosCfmRemoteMEPJitter_Type = Counter32
_WwpLeosCfmRemoteMEPJitter_Object = MibTableColumn
wwpLeosCfmRemoteMEPJitter = _WwpLeosCfmRemoteMEPJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 13),
    _WwpLeosCfmRemoteMEPJitter_Type()
)
wwpLeosCfmRemoteMEPJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPJitter.setStatus("current")
_WwpLeosCfmRemoteMEPNumLMMSent_Type = Counter32
_WwpLeosCfmRemoteMEPNumLMMSent_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumLMMSent = _WwpLeosCfmRemoteMEPNumLMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 14),
    _WwpLeosCfmRemoteMEPNumLMMSent_Type()
)
wwpLeosCfmRemoteMEPNumLMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumLMMSent.setStatus("current")
_WwpLeosCfmRemoteMEPFrameLossNear_Type = Counter32
_WwpLeosCfmRemoteMEPFrameLossNear_Object = MibTableColumn
wwpLeosCfmRemoteMEPFrameLossNear = _WwpLeosCfmRemoteMEPFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 15),
    _WwpLeosCfmRemoteMEPFrameLossNear_Type()
)
wwpLeosCfmRemoteMEPFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPFrameLossNear.setStatus("current")
_WwpLeosCfmRemoteMEPFrameLossFar_Type = Counter32
_WwpLeosCfmRemoteMEPFrameLossFar_Object = MibTableColumn
wwpLeosCfmRemoteMEPFrameLossFar = _WwpLeosCfmRemoteMEPFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 16),
    _WwpLeosCfmRemoteMEPFrameLossFar_Type()
)
wwpLeosCfmRemoteMEPFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPFrameLossFar.setStatus("current")
_WwpLeosCfmRemoteMEPNumLMRReceived_Type = Counter32
_WwpLeosCfmRemoteMEPNumLMRReceived_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumLMRReceived = _WwpLeosCfmRemoteMEPNumLMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 17),
    _WwpLeosCfmRemoteMEPNumLMRReceived_Type()
)
wwpLeosCfmRemoteMEPNumLMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumLMRReceived.setStatus("current")
_WwpLeosCfmRemoteMEPNumCCMLost_Type = Counter32
_WwpLeosCfmRemoteMEPNumCCMLost_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumCCMLost = _WwpLeosCfmRemoteMEPNumCCMLost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 18),
    _WwpLeosCfmRemoteMEPNumCCMLost_Type()
)
wwpLeosCfmRemoteMEPNumCCMLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumCCMLost.setStatus("current")
_WwpLeosCfmRemoteMEPNumDMRReceived_Type = Counter32
_WwpLeosCfmRemoteMEPNumDMRReceived_Object = MibTableColumn
wwpLeosCfmRemoteMEPNumDMRReceived = _WwpLeosCfmRemoteMEPNumDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 19),
    _WwpLeosCfmRemoteMEPNumDMRReceived_Type()
)
wwpLeosCfmRemoteMEPNumDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPNumDMRReceived.setStatus("current")


class _WwpLeosCfmRemoteMEPHoldState_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPHoldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("locked", 3))
    )


_WwpLeosCfmRemoteMEPHoldState_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPHoldState_Object = MibTableColumn
wwpLeosCfmRemoteMEPHoldState = _WwpLeosCfmRemoteMEPHoldState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 20),
    _WwpLeosCfmRemoteMEPHoldState_Type()
)
wwpLeosCfmRemoteMEPHoldState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPHoldState.setStatus("deprecated")
_WwpLeosCfmRemoteMEPRowStatus_Type = RowStatus
_WwpLeosCfmRemoteMEPRowStatus_Object = MibTableColumn
wwpLeosCfmRemoteMEPRowStatus = _WwpLeosCfmRemoteMEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 21),
    _WwpLeosCfmRemoteMEPRowStatus_Type()
)
wwpLeosCfmRemoteMEPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPRowStatus.setStatus("current")


class _WwpLeosCfmRemoteMEPCCMComment_Type(DisplayString):
    """Custom type wwpLeosCfmRemoteMEPCCMComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosCfmRemoteMEPCCMComment_Type.__name__ = "DisplayString"
_WwpLeosCfmRemoteMEPCCMComment_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMComment = _WwpLeosCfmRemoteMEPCCMComment_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 22),
    _WwpLeosCfmRemoteMEPCCMComment_Type()
)
wwpLeosCfmRemoteMEPCCMComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMComment.setStatus("current")
_WwpLeosCfmRemoteMEPBadSequence_Type = Counter32
_WwpLeosCfmRemoteMEPBadSequence_Object = MibTableColumn
wwpLeosCfmRemoteMEPBadSequence = _WwpLeosCfmRemoteMEPBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 23),
    _WwpLeosCfmRemoteMEPBadSequence_Type()
)
wwpLeosCfmRemoteMEPBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPBadSequence.setStatus("current")
_WwpLeosCfmRemoteMEPMinDelay_Type = Counter32
_WwpLeosCfmRemoteMEPMinDelay_Object = MibTableColumn
wwpLeosCfmRemoteMEPMinDelay = _WwpLeosCfmRemoteMEPMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 24),
    _WwpLeosCfmRemoteMEPMinDelay_Type()
)
wwpLeosCfmRemoteMEPMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPMinDelay.setStatus("current")
_WwpLeosCfmRemoteMEPMaxDelay_Type = Counter32
_WwpLeosCfmRemoteMEPMaxDelay_Object = MibTableColumn
wwpLeosCfmRemoteMEPMaxDelay = _WwpLeosCfmRemoteMEPMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 25),
    _WwpLeosCfmRemoteMEPMaxDelay_Type()
)
wwpLeosCfmRemoteMEPMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPMaxDelay.setStatus("current")
_WwpLeosCfmRemoteMEPMinJitter_Type = Counter32
_WwpLeosCfmRemoteMEPMinJitter_Object = MibTableColumn
wwpLeosCfmRemoteMEPMinJitter = _WwpLeosCfmRemoteMEPMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 26),
    _WwpLeosCfmRemoteMEPMinJitter_Type()
)
wwpLeosCfmRemoteMEPMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPMinJitter.setStatus("current")
_WwpLeosCfmRemoteMEPMaxJitter_Type = Counter32
_WwpLeosCfmRemoteMEPMaxJitter_Object = MibTableColumn
wwpLeosCfmRemoteMEPMaxJitter = _WwpLeosCfmRemoteMEPMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 27),
    _WwpLeosCfmRemoteMEPMaxJitter_Type()
)
wwpLeosCfmRemoteMEPMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPMaxJitter.setStatus("current")


class _WwpLeosCfmRemoteCfmMEPHoldState_Type(Integer32):
    """Custom type wwpLeosCfmRemoteCfmMEPHoldState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("lock", 3))
    )


_WwpLeosCfmRemoteCfmMEPHoldState_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteCfmMEPHoldState_Object = MibTableColumn
wwpLeosCfmRemoteCfmMEPHoldState = _WwpLeosCfmRemoteCfmMEPHoldState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 28),
    _WwpLeosCfmRemoteCfmMEPHoldState_Type()
)
wwpLeosCfmRemoteCfmMEPHoldState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteCfmMEPHoldState.setStatus("current")
_WwpLeosCfmRemoteMEPServiceClear_Type = TruthValue
_WwpLeosCfmRemoteMEPServiceClear_Object = MibTableColumn
wwpLeosCfmRemoteMEPServiceClear = _WwpLeosCfmRemoteMEPServiceClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 29),
    _WwpLeosCfmRemoteMEPServiceClear_Type()
)
wwpLeosCfmRemoteMEPServiceClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPServiceClear.setStatus("current")
_WwpLeosCfmRemoteMEPServiceStatisticsClear_Type = TruthValue
_WwpLeosCfmRemoteMEPServiceStatisticsClear_Object = MibTableColumn
wwpLeosCfmRemoteMEPServiceStatisticsClear = _WwpLeosCfmRemoteMEPServiceStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 30),
    _WwpLeosCfmRemoteMEPServiceStatisticsClear_Type()
)
wwpLeosCfmRemoteMEPServiceStatisticsClear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPServiceStatisticsClear.setStatus("current")
_WwpLeosCfmRemoteMEPAccelerated_Type = TruthValue
_WwpLeosCfmRemoteMEPAccelerated_Object = MibTableColumn
wwpLeosCfmRemoteMEPAccelerated = _WwpLeosCfmRemoteMEPAccelerated_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 49),
    _WwpLeosCfmRemoteMEPAccelerated_Type()
)
wwpLeosCfmRemoteMEPAccelerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPAccelerated.setStatus("current")


class _WwpLeosCfmRemoteMEPSubPortName_Type(DisplayString):
    """Custom type wwpLeosCfmRemoteMEPSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmRemoteMEPSubPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmRemoteMEPSubPortName_Object = MibTableColumn
wwpLeosCfmRemoteMEPSubPortName = _WwpLeosCfmRemoteMEPSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 50),
    _WwpLeosCfmRemoteMEPSubPortName_Type()
)
wwpLeosCfmRemoteMEPSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPSubPortName.setStatus("current")


class _WwpLeosCfmRemoteMEPServiceName_Type(DisplayString):
    """Custom type wwpLeosCfmRemoteMEPServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmRemoteMEPServiceName_Type.__name__ = "DisplayString"
_WwpLeosCfmRemoteMEPServiceName_Object = MibTableColumn
wwpLeosCfmRemoteMEPServiceName = _WwpLeosCfmRemoteMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 51),
    _WwpLeosCfmRemoteMEPServiceName_Type()
)
wwpLeosCfmRemoteMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPServiceName.setStatus("current")


class _WwpLeosCfmRemoteMEPBayIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmRemoteMEPBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPBayIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPBayIndex = _WwpLeosCfmRemoteMEPBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 52),
    _WwpLeosCfmRemoteMEPBayIndex_Type()
)
wwpLeosCfmRemoteMEPBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPBayIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmRemoteMEPShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPShelfIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPShelfIndex = _WwpLeosCfmRemoteMEPShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 53),
    _WwpLeosCfmRemoteMEPShelfIndex_Type()
)
wwpLeosCfmRemoteMEPShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPShelfIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosCfmRemoteMEPModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPModuleIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPModuleIndex = _WwpLeosCfmRemoteMEPModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 54),
    _WwpLeosCfmRemoteMEPModuleIndex_Type()
)
wwpLeosCfmRemoteMEPModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPModuleIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPPreviousBayIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPPreviousBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmRemoteMEPPreviousBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPPreviousBayIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPPreviousBayIndex = _WwpLeosCfmRemoteMEPPreviousBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 55),
    _WwpLeosCfmRemoteMEPPreviousBayIndex_Type()
)
wwpLeosCfmRemoteMEPPreviousBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPPreviousBayIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPPreviousShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPPreviousShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosCfmRemoteMEPPreviousShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPPreviousShelfIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPPreviousShelfIndex = _WwpLeosCfmRemoteMEPPreviousShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 56),
    _WwpLeosCfmRemoteMEPPreviousShelfIndex_Type()
)
wwpLeosCfmRemoteMEPPreviousShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPPreviousShelfIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPPreviousModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPPreviousModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosCfmRemoteMEPPreviousModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPPreviousModuleIndex_Object = MibTableColumn
wwpLeosCfmRemoteMEPPreviousModuleIndex = _WwpLeosCfmRemoteMEPPreviousModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 57),
    _WwpLeosCfmRemoteMEPPreviousModuleIndex_Type()
)
wwpLeosCfmRemoteMEPPreviousModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPPreviousModuleIndex.setStatus("current")


class _WwpLeosCfmRemoteMEPLastPortStatus_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPLastPortStatus based on Integer32"""
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
        *(("blocked", 3),
          ("none", 2),
          ("unknown", 1),
          ("up", 4))
    )


_WwpLeosCfmRemoteMEPLastPortStatus_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPLastPortStatus_Object = MibTableColumn
wwpLeosCfmRemoteMEPLastPortStatus = _WwpLeosCfmRemoteMEPLastPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 58),
    _WwpLeosCfmRemoteMEPLastPortStatus_Type()
)
wwpLeosCfmRemoteMEPLastPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPLastPortStatus.setStatus("current")


class _WwpLeosCfmRemoteMEPLastInterfaceStatus_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPLastInterfaceStatus based on Integer32"""
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
        *(("dormant", 5),
          ("down", 3),
          ("lowerLayerDown", 6),
          ("none", 1),
          ("notPresent", 7),
          ("testing", 4),
          ("up", 2))
    )


_WwpLeosCfmRemoteMEPLastInterfaceStatus_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPLastInterfaceStatus_Object = MibTableColumn
wwpLeosCfmRemoteMEPLastInterfaceStatus = _WwpLeosCfmRemoteMEPLastInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 59),
    _WwpLeosCfmRemoteMEPLastInterfaceStatus_Type()
)
wwpLeosCfmRemoteMEPLastInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPLastInterfaceStatus.setStatus("current")
_WwpLeosCfmRemoteMEPLastSeqNum_Type = Unsigned32
_WwpLeosCfmRemoteMEPLastSeqNum_Object = MibTableColumn
wwpLeosCfmRemoteMEPLastSeqNum = _WwpLeosCfmRemoteMEPLastSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 60),
    _WwpLeosCfmRemoteMEPLastSeqNum_Type()
)
wwpLeosCfmRemoteMEPLastSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPLastSeqNum.setStatus("current")
_WwpLeosCfmRemoteMEPCCMSeqErrors_Type = Unsigned32
_WwpLeosCfmRemoteMEPCCMSeqErrors_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMSeqErrors = _WwpLeosCfmRemoteMEPCCMSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 61),
    _WwpLeosCfmRemoteMEPCCMSeqErrors_Type()
)
wwpLeosCfmRemoteMEPCCMSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMSeqErrors.setStatus("current")


class _WwpLeosCfmRemoteMEPCCMLevel_Type(Integer32):
    """Custom type wwpLeosCfmRemoteMEPCCMLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WwpLeosCfmRemoteMEPCCMLevel_Type.__name__ = "Integer32"
_WwpLeosCfmRemoteMEPCCMLevel_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMLevel = _WwpLeosCfmRemoteMEPCCMLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 1, 1, 62),
    _WwpLeosCfmRemoteMEPCCMLevel_Type()
)
wwpLeosCfmRemoteMEPCCMLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMLevel.setStatus("current")
_WwpLeosCfmRemoteMEPDeleteAll_Type = TruthValue
_WwpLeosCfmRemoteMEPDeleteAll_Object = MibScalar
wwpLeosCfmRemoteMEPDeleteAll = _WwpLeosCfmRemoteMEPDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 8, 65),
    _WwpLeosCfmRemoteMEPDeleteAll_Type()
)
wwpLeosCfmRemoteMEPDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPDeleteAll.setStatus("current")
_WwpLeosCfmStack_ObjectIdentity = ObjectIdentity
wwpLeosCfmStack = _WwpLeosCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9)
)
_WwpLeosCfmPortStackTable_Object = MibTable
wwpLeosCfmPortStackTable = _WwpLeosCfmPortStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackTable.setStatus("deprecated")
_WwpLeosCfmPortStackEntry_Object = MibTableRow
wwpLeosCfmPortStackEntry = _WwpLeosCfmPortStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1)
)
wwpLeosCfmPortStackEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmPortStackPort"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmPortStackVid"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmPortStackType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmPortStackLevel"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackEntry.setStatus("deprecated")


class _WwpLeosCfmPortStackPort_Type(Integer32):
    """Custom type wwpLeosCfmPortStackPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmPortStackPort_Type.__name__ = "Integer32"
_WwpLeosCfmPortStackPort_Object = MibTableColumn
wwpLeosCfmPortStackPort = _WwpLeosCfmPortStackPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1, 1),
    _WwpLeosCfmPortStackPort_Type()
)
wwpLeosCfmPortStackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackPort.setStatus("deprecated")


class _WwpLeosCfmPortStackVid_Type(Integer32):
    """Custom type wwpLeosCfmPortStackVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmPortStackVid_Type.__name__ = "Integer32"
_WwpLeosCfmPortStackVid_Object = MibTableColumn
wwpLeosCfmPortStackVid = _WwpLeosCfmPortStackVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1, 2),
    _WwpLeosCfmPortStackVid_Type()
)
wwpLeosCfmPortStackVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackVid.setStatus("deprecated")


class _WwpLeosCfmPortStackType_Type(Integer32):
    """Custom type wwpLeosCfmPortStackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mepDown", 2),
          ("mepUp", 1),
          ("mip", 3))
    )


_WwpLeosCfmPortStackType_Type.__name__ = "Integer32"
_WwpLeosCfmPortStackType_Object = MibTableColumn
wwpLeosCfmPortStackType = _WwpLeosCfmPortStackType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1, 3),
    _WwpLeosCfmPortStackType_Type()
)
wwpLeosCfmPortStackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackType.setStatus("deprecated")


class _WwpLeosCfmPortStackLevel_Type(Unsigned32):
    """Custom type wwpLeosCfmPortStackLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmPortStackLevel_Type.__name__ = "Unsigned32"
_WwpLeosCfmPortStackLevel_Object = MibTableColumn
wwpLeosCfmPortStackLevel = _WwpLeosCfmPortStackLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1, 4),
    _WwpLeosCfmPortStackLevel_Type()
)
wwpLeosCfmPortStackLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackLevel.setStatus("deprecated")


class _WwpLeosCfmPortStackMEPId_Type(Integer32):
    """Custom type wwpLeosCfmPortStackMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosCfmPortStackMEPId_Type.__name__ = "Integer32"
_WwpLeosCfmPortStackMEPId_Object = MibTableColumn
wwpLeosCfmPortStackMEPId = _WwpLeosCfmPortStackMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 9, 1, 1, 5),
    _WwpLeosCfmPortStackMEPId_Type()
)
wwpLeosCfmPortStackMEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmPortStackMEPId.setStatus("deprecated")
_WwpLeosCfmMipCCMDb_ObjectIdentity = ObjectIdentity
wwpLeosCfmMipCCMDb = _WwpLeosCfmMipCCMDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10)
)
_WwpLeosCfmMipCCMDbTable_Object = MibTable
wwpLeosCfmMipCCMDbTable = _WwpLeosCfmMipCCMDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbTable.setStatus("current")
_WwpLeosCfmMipCCMDbEntry_Object = MibTableRow
wwpLeosCfmMipCCMDbEntry = _WwpLeosCfmMipCCMDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1)
)
wwpLeosCfmMipCCMDbEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmMipCCMDbIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbEntry.setStatus("current")


class _WwpLeosCfmMipCCMDbIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmMipCCMDbIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmMipCCMDbIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmMipCCMDbIndex_Object = MibTableColumn
wwpLeosCfmMipCCMDbIndex = _WwpLeosCfmMipCCMDbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 1),
    _WwpLeosCfmMipCCMDbIndex_Type()
)
wwpLeosCfmMipCCMDbIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbIndex.setStatus("current")


class _WwpLeosCfmMipCCMDbVid_Type(Unsigned32):
    """Custom type wwpLeosCfmMipCCMDbVid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmMipCCMDbVid_Type.__name__ = "Unsigned32"
_WwpLeosCfmMipCCMDbVid_Object = MibTableColumn
wwpLeosCfmMipCCMDbVid = _WwpLeosCfmMipCCMDbVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 2),
    _WwpLeosCfmMipCCMDbVid_Type()
)
wwpLeosCfmMipCCMDbVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbVid.setStatus("current")
_WwpLeosCfmMipCCMDbMacAddr_Type = MacAddress
_WwpLeosCfmMipCCMDbMacAddr_Object = MibTableColumn
wwpLeosCfmMipCCMDbMacAddr = _WwpLeosCfmMipCCMDbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 3),
    _WwpLeosCfmMipCCMDbMacAddr_Type()
)
wwpLeosCfmMipCCMDbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbMacAddr.setStatus("current")


class _WwpLeosCfmMipCCMDbPort_Type(Integer32):
    """Custom type wwpLeosCfmMipCCMDbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmMipCCMDbPort_Type.__name__ = "Integer32"
_WwpLeosCfmMipCCMDbPort_Object = MibTableColumn
wwpLeosCfmMipCCMDbPort = _WwpLeosCfmMipCCMDbPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 4),
    _WwpLeosCfmMipCCMDbPort_Type()
)
wwpLeosCfmMipCCMDbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbPort.setStatus("current")


class _WwpLeosCfmMipCCMDbMEPID_Type(Integer32):
    """Custom type wwpLeosCfmMipCCMDbMEPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmMipCCMDbMEPID_Type.__name__ = "Integer32"
_WwpLeosCfmMipCCMDbMEPID_Object = MibTableColumn
wwpLeosCfmMipCCMDbMEPID = _WwpLeosCfmMipCCMDbMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 5),
    _WwpLeosCfmMipCCMDbMEPID_Type()
)
wwpLeosCfmMipCCMDbMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbMEPID.setStatus("current")
_WwpLeosCfmMipCCMdbNumCCMRx_Type = Counter32
_WwpLeosCfmMipCCMdbNumCCMRx_Object = MibTableColumn
wwpLeosCfmMipCCMdbNumCCMRx = _WwpLeosCfmMipCCMdbNumCCMRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 6),
    _WwpLeosCfmMipCCMdbNumCCMRx_Type()
)
wwpLeosCfmMipCCMdbNumCCMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMdbNumCCMRx.setStatus("current")
_WwpLeosCfmMipCCMDbTime_Type = TimeTicks
_WwpLeosCfmMipCCMDbTime_Object = MibTableColumn
wwpLeosCfmMipCCMDbTime = _WwpLeosCfmMipCCMDbTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 7),
    _WwpLeosCfmMipCCMDbTime_Type()
)
wwpLeosCfmMipCCMDbTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbTime.setStatus("current")
_WwpLeosCfmMipCCMDbLastMacStatus_Type = TruthValue
_WwpLeosCfmMipCCMDbLastMacStatus_Object = MibTableColumn
wwpLeosCfmMipCCMDbLastMacStatus = _WwpLeosCfmMipCCMDbLastMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 8),
    _WwpLeosCfmMipCCMDbLastMacStatus_Type()
)
wwpLeosCfmMipCCMDbLastMacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbLastMacStatus.setStatus("current")
_WwpLeosCfmMipCCMDbRDIErrorFlag_Type = TruthValue
_WwpLeosCfmMipCCMDbRDIErrorFlag_Object = MibTableColumn
wwpLeosCfmMipCCMDbRDIErrorFlag = _WwpLeosCfmMipCCMDbRDIErrorFlag_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 10, 1, 1, 9),
    _WwpLeosCfmMipCCMDbRDIErrorFlag_Type()
)
wwpLeosCfmMipCCMDbRDIErrorFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmMipCCMDbRDIErrorFlag.setStatus("current")
_WwpLeosCfmFaultNotif_ObjectIdentity = ObjectIdentity
wwpLeosCfmFaultNotif = _WwpLeosCfmFaultNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 11)
)


class _WwpLeosCfmFaultTrapState_Type(Integer32):
    """Custom type wwpLeosCfmFaultTrapState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmFaultTrapState_Type.__name__ = "Integer32"
_WwpLeosCfmFaultTrapState_Object = MibScalar
wwpLeosCfmFaultTrapState = _WwpLeosCfmFaultTrapState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 11, 1),
    _WwpLeosCfmFaultTrapState_Type()
)
wwpLeosCfmFaultTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmFaultTrapState.setStatus("current")
_WwpLeosCfmDelay_ObjectIdentity = ObjectIdentity
wwpLeosCfmDelay = _WwpLeosCfmDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12)
)
_WwpLeosCfmDelayMsgTable_Object = MibTable
wwpLeosCfmDelayMsgTable = _WwpLeosCfmDelayMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgTable.setStatus("current")
_WwpLeosCfmDelayMsgEntry_Object = MibTableRow
wwpLeosCfmDelayMsgEntry = _WwpLeosCfmDelayMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1)
)
wwpLeosCfmDelayMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmDelayMsgPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgEntry.setStatus("current")


class _WwpLeosCfmDelayMsgPortId_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmDelayMsgPortId_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgPortId_Object = MibTableColumn
wwpLeosCfmDelayMsgPortId = _WwpLeosCfmDelayMsgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 1),
    _WwpLeosCfmDelayMsgPortId_Type()
)
wwpLeosCfmDelayMsgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgPortId.setStatus("current")


class _WwpLeosCfmDelayMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmDelayMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmDelayMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmDelayMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmDelayMsgTargetMEPID = _WwpLeosCfmDelayMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 2),
    _WwpLeosCfmDelayMsgTargetMEPID_Type()
)
wwpLeosCfmDelayMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgTargetMEPID.setStatus("current")
_WwpLeosCfmDelayMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmDelayMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmDelayMsgTargetMacAddr = _WwpLeosCfmDelayMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 3),
    _WwpLeosCfmDelayMsgTargetMacAddr_Type()
)
wwpLeosCfmDelayMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmDelayMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_WwpLeosCfmDelayMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgCount_Object = MibTableColumn
wwpLeosCfmDelayMsgCount = _WwpLeosCfmDelayMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 4),
    _WwpLeosCfmDelayMsgCount_Type()
)
wwpLeosCfmDelayMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgCount.setStatus("current")


class _WwpLeosCfmDelayMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmDelayMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgPriority_Object = MibTableColumn
wwpLeosCfmDelayMsgPriority = _WwpLeosCfmDelayMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 5),
    _WwpLeosCfmDelayMsgPriority_Type()
)
wwpLeosCfmDelayMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgPriority.setStatus("current")
_WwpLeosCfmDelayMsgRowStatus_Type = RowStatus
_WwpLeosCfmDelayMsgRowStatus_Object = MibTableColumn
wwpLeosCfmDelayMsgRowStatus = _WwpLeosCfmDelayMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 6),
    _WwpLeosCfmDelayMsgRowStatus_Type()
)
wwpLeosCfmDelayMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgRowStatus.setStatus("current")


class _WwpLeosCfmDelayMsgRepeat_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgRepeat based on Integer32"""
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


_WwpLeosCfmDelayMsgRepeat_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgRepeat_Object = MibTableColumn
wwpLeosCfmDelayMsgRepeat = _WwpLeosCfmDelayMsgRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 7),
    _WwpLeosCfmDelayMsgRepeat_Type()
)
wwpLeosCfmDelayMsgRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgRepeat.setStatus("current")


class _WwpLeosCfmDelayMsgRepeatCount_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosCfmDelayMsgRepeatCount_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgRepeatCount_Object = MibTableColumn
wwpLeosCfmDelayMsgRepeatCount = _WwpLeosCfmDelayMsgRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 8),
    _WwpLeosCfmDelayMsgRepeatCount_Type()
)
wwpLeosCfmDelayMsgRepeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgRepeatCount.setStatus("current")


class _WwpLeosCfmDelayMsgDelayThreshold_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_WwpLeosCfmDelayMsgDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgDelayThreshold_Object = MibTableColumn
wwpLeosCfmDelayMsgDelayThreshold = _WwpLeosCfmDelayMsgDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 9),
    _WwpLeosCfmDelayMsgDelayThreshold_Type()
)
wwpLeosCfmDelayMsgDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgDelayThreshold.setStatus("current")


class _WwpLeosCfmDelayMsgJitterThreshold_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_WwpLeosCfmDelayMsgJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgJitterThreshold_Object = MibTableColumn
wwpLeosCfmDelayMsgJitterThreshold = _WwpLeosCfmDelayMsgJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 10),
    _WwpLeosCfmDelayMsgJitterThreshold_Type()
)
wwpLeosCfmDelayMsgJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgJitterThreshold.setStatus("current")


class _WwpLeosCfmDelayMsgMaxDelayThreshold_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgMaxDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_WwpLeosCfmDelayMsgMaxDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgMaxDelayThreshold_Object = MibTableColumn
wwpLeosCfmDelayMsgMaxDelayThreshold = _WwpLeosCfmDelayMsgMaxDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 11),
    _WwpLeosCfmDelayMsgMaxDelayThreshold_Type()
)
wwpLeosCfmDelayMsgMaxDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgMaxDelayThreshold.setStatus("current")


class _WwpLeosCfmDelayMsgMaxJitterThreshold_Type(Integer32):
    """Custom type wwpLeosCfmDelayMsgMaxJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_WwpLeosCfmDelayMsgMaxJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmDelayMsgMaxJitterThreshold_Object = MibTableColumn
wwpLeosCfmDelayMsgMaxJitterThreshold = _WwpLeosCfmDelayMsgMaxJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 12, 1, 1, 12),
    _WwpLeosCfmDelayMsgMaxJitterThreshold_Type()
)
wwpLeosCfmDelayMsgMaxJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmDelayMsgMaxJitterThreshold.setStatus("current")
_WwpLeosCfmFrameLoss_ObjectIdentity = ObjectIdentity
wwpLeosCfmFrameLoss = _WwpLeosCfmFrameLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13)
)
_WwpLeosCfmFrameLossMsgTable_Object = MibTable
wwpLeosCfmFrameLossMsgTable = _WwpLeosCfmFrameLossMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgTable.setStatus("current")
_WwpLeosCfmFrameLossMsgEntry_Object = MibTableRow
wwpLeosCfmFrameLossMsgEntry = _WwpLeosCfmFrameLossMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1)
)
wwpLeosCfmFrameLossMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmFrameLossMsgPortId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgEntry.setStatus("current")


class _WwpLeosCfmFrameLossMsgPortId_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmFrameLossMsgPortId_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgPortId_Object = MibTableColumn
wwpLeosCfmFrameLossMsgPortId = _WwpLeosCfmFrameLossMsgPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 1),
    _WwpLeosCfmFrameLossMsgPortId_Type()
)
wwpLeosCfmFrameLossMsgPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgPortId.setStatus("current")


class _WwpLeosCfmFrameLossMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmFrameLossMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmFrameLossMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmFrameLossMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmFrameLossMsgTargetMEPID = _WwpLeosCfmFrameLossMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 2),
    _WwpLeosCfmFrameLossMsgTargetMEPID_Type()
)
wwpLeosCfmFrameLossMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgTargetMEPID.setStatus("current")
_WwpLeosCfmFrameLossMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmFrameLossMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmFrameLossMsgTargetMacAddr = _WwpLeosCfmFrameLossMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 3),
    _WwpLeosCfmFrameLossMsgTargetMacAddr_Type()
)
wwpLeosCfmFrameLossMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmFrameLossMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_WwpLeosCfmFrameLossMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgCount_Object = MibTableColumn
wwpLeosCfmFrameLossMsgCount = _WwpLeosCfmFrameLossMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 4),
    _WwpLeosCfmFrameLossMsgCount_Type()
)
wwpLeosCfmFrameLossMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgCount.setStatus("current")


class _WwpLeosCfmFrameLossMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmFrameLossMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgPriority_Object = MibTableColumn
wwpLeosCfmFrameLossMsgPriority = _WwpLeosCfmFrameLossMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 5),
    _WwpLeosCfmFrameLossMsgPriority_Type()
)
wwpLeosCfmFrameLossMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgPriority.setStatus("current")
_WwpLeosCfmFrameLossMsgRowStatus_Type = RowStatus
_WwpLeosCfmFrameLossMsgRowStatus_Object = MibTableColumn
wwpLeosCfmFrameLossMsgRowStatus = _WwpLeosCfmFrameLossMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 6),
    _WwpLeosCfmFrameLossMsgRowStatus_Type()
)
wwpLeosCfmFrameLossMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgRowStatus.setStatus("current")


class _WwpLeosCfmFrameLossMsgRepeat_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgRepeat based on Integer32"""
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


_WwpLeosCfmFrameLossMsgRepeat_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgRepeat_Object = MibTableColumn
wwpLeosCfmFrameLossMsgRepeat = _WwpLeosCfmFrameLossMsgRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 7),
    _WwpLeosCfmFrameLossMsgRepeat_Type()
)
wwpLeosCfmFrameLossMsgRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgRepeat.setStatus("current")


class _WwpLeosCfmFrameLossMsgRepeatCount_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosCfmFrameLossMsgRepeatCount_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgRepeatCount_Object = MibTableColumn
wwpLeosCfmFrameLossMsgRepeatCount = _WwpLeosCfmFrameLossMsgRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 8),
    _WwpLeosCfmFrameLossMsgRepeatCount_Type()
)
wwpLeosCfmFrameLossMsgRepeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgRepeatCount.setStatus("current")


class _WwpLeosCfmFrameLossMsgFlnThreshold_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgFlnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_WwpLeosCfmFrameLossMsgFlnThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgFlnThreshold_Object = MibTableColumn
wwpLeosCfmFrameLossMsgFlnThreshold = _WwpLeosCfmFrameLossMsgFlnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 9),
    _WwpLeosCfmFrameLossMsgFlnThreshold_Type()
)
wwpLeosCfmFrameLossMsgFlnThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgFlnThreshold.setStatus("current")


class _WwpLeosCfmFrameLossMsgFlfThreshold_Type(Integer32):
    """Custom type wwpLeosCfmFrameLossMsgFlfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_WwpLeosCfmFrameLossMsgFlfThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmFrameLossMsgFlfThreshold_Object = MibTableColumn
wwpLeosCfmFrameLossMsgFlfThreshold = _WwpLeosCfmFrameLossMsgFlfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 13, 1, 1, 10),
    _WwpLeosCfmFrameLossMsgFlfThreshold_Type()
)
wwpLeosCfmFrameLossMsgFlfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossMsgFlfThreshold.setStatus("current")
_WwpLeosCfmRemoteMEPCCMLoss_ObjectIdentity = ObjectIdentity
wwpLeosCfmRemoteMEPCCMLoss = _WwpLeosCfmRemoteMEPCCMLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 14)
)
_WwpLeosCfmRemoteMEPCCMLossTable_Object = MibTable
wwpLeosCfmRemoteMEPCCMLossTable = _WwpLeosCfmRemoteMEPCCMLossTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 14, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMLossTable.setStatus("current")
_WwpLeosCfmRemoteMEPCCMLossEntry_Object = MibTableRow
wwpLeosCfmRemoteMEPCCMLossEntry = _WwpLeosCfmRemoteMEPCCMLossEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 14, 1, 1)
)
wwpLeosCfmRemoteMEPCCMLossEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPID"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPCCMLossNum"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMLossEntry.setStatus("current")


class _WwpLeosCfmRemoteMEPCCMLossNum_Type(Unsigned32):
    """Custom type wwpLeosCfmRemoteMEPCCMLossNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_WwpLeosCfmRemoteMEPCCMLossNum_Type.__name__ = "Unsigned32"
_WwpLeosCfmRemoteMEPCCMLossNum_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMLossNum = _WwpLeosCfmRemoteMEPCCMLossNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 14, 1, 1, 1),
    _WwpLeosCfmRemoteMEPCCMLossNum_Type()
)
wwpLeosCfmRemoteMEPCCMLossNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMLossNum.setStatus("current")
_WwpLeosCfmRemoteMEPCCMLossCount_Type = Gauge32
_WwpLeosCfmRemoteMEPCCMLossCount_Object = MibTableColumn
wwpLeosCfmRemoteMEPCCMLossCount = _WwpLeosCfmRemoteMEPCCMLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 14, 1, 1, 2),
    _WwpLeosCfmRemoteMEPCCMLossCount_Type()
)
wwpLeosCfmRemoteMEPCCMLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmRemoteMEPCCMLossCount.setStatus("current")
_WwpLeosCfmExtStack_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtStack = _WwpLeosCfmExtStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15)
)
_WwpLeosCfmExtPortStackTable_Object = MibTable
wwpLeosCfmExtPortStackTable = _WwpLeosCfmExtPortStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackTable.setStatus("current")
_WwpLeosCfmExtPortStackEntry_Object = MibTableRow
wwpLeosCfmExtPortStackEntry = _WwpLeosCfmExtPortStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1)
)
wwpLeosCfmExtPortStackEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtPortStackVid"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtPortStackPort"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtPortStackType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtPortStackLevel"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackEntry.setStatus("current")


class _WwpLeosCfmExtPortStackVid_Type(Integer32):
    """Custom type wwpLeosCfmExtPortStackVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmExtPortStackVid_Type.__name__ = "Integer32"
_WwpLeosCfmExtPortStackVid_Object = MibTableColumn
wwpLeosCfmExtPortStackVid = _WwpLeosCfmExtPortStackVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1, 1),
    _WwpLeosCfmExtPortStackVid_Type()
)
wwpLeosCfmExtPortStackVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackVid.setStatus("current")


class _WwpLeosCfmExtPortStackPort_Type(Integer32):
    """Custom type wwpLeosCfmExtPortStackPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtPortStackPort_Type.__name__ = "Integer32"
_WwpLeosCfmExtPortStackPort_Object = MibTableColumn
wwpLeosCfmExtPortStackPort = _WwpLeosCfmExtPortStackPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1, 2),
    _WwpLeosCfmExtPortStackPort_Type()
)
wwpLeosCfmExtPortStackPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackPort.setStatus("current")


class _WwpLeosCfmExtPortStackType_Type(Integer32):
    """Custom type wwpLeosCfmExtPortStackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mepDown", 2),
          ("mepUp", 1),
          ("mip", 3))
    )


_WwpLeosCfmExtPortStackType_Type.__name__ = "Integer32"
_WwpLeosCfmExtPortStackType_Object = MibTableColumn
wwpLeosCfmExtPortStackType = _WwpLeosCfmExtPortStackType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1, 3),
    _WwpLeosCfmExtPortStackType_Type()
)
wwpLeosCfmExtPortStackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackType.setStatus("current")


class _WwpLeosCfmExtPortStackLevel_Type(Unsigned32):
    """Custom type wwpLeosCfmExtPortStackLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtPortStackLevel_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtPortStackLevel_Object = MibTableColumn
wwpLeosCfmExtPortStackLevel = _WwpLeosCfmExtPortStackLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1, 4),
    _WwpLeosCfmExtPortStackLevel_Type()
)
wwpLeosCfmExtPortStackLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackLevel.setStatus("current")


class _WwpLeosCfmExtPortStackMEPId_Type(Integer32):
    """Custom type wwpLeosCfmExtPortStackMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WwpLeosCfmExtPortStackMEPId_Type.__name__ = "Integer32"
_WwpLeosCfmExtPortStackMEPId_Object = MibTableColumn
wwpLeosCfmExtPortStackMEPId = _WwpLeosCfmExtPortStackMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 15, 1, 1, 5),
    _WwpLeosCfmExtPortStackMEPId_Type()
)
wwpLeosCfmExtPortStackMEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortStackMEPId.setStatus("current")
_WwpLeosCfmServiceFrameBudget_ObjectIdentity = ObjectIdentity
wwpLeosCfmServiceFrameBudget = _WwpLeosCfmServiceFrameBudget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 16)
)
_WwpLeosCfmServiceFrameBudgetTable_Object = MibTable
wwpLeosCfmServiceFrameBudgetTable = _WwpLeosCfmServiceFrameBudgetTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 16, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFrameBudgetTable.setStatus("current")
_WwpLeosCfmServiceFrameBudgetEntry_Object = MibTableRow
wwpLeosCfmServiceFrameBudgetEntry = _WwpLeosCfmServiceFrameBudgetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 16, 1, 1)
)
wwpLeosCfmServiceFrameBudgetEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmSlotIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFrameBudgetEntry.setStatus("current")


class _WwpLeosCfmSlotIndex_Type(Integer32):
    """Custom type wwpLeosCfmSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WwpLeosCfmSlotIndex_Type.__name__ = "Integer32"
_WwpLeosCfmSlotIndex_Object = MibTableColumn
wwpLeosCfmSlotIndex = _WwpLeosCfmSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 16, 1, 1, 1),
    _WwpLeosCfmSlotIndex_Type()
)
wwpLeosCfmSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmSlotIndex.setStatus("current")
_WwpLeosCfmServiceFrameBudgetSlot_Type = Counter32
_WwpLeosCfmServiceFrameBudgetSlot_Object = MibTableColumn
wwpLeosCfmServiceFrameBudgetSlot = _WwpLeosCfmServiceFrameBudgetSlot_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 16, 1, 1, 2),
    _WwpLeosCfmServiceFrameBudgetSlot_Type()
)
wwpLeosCfmServiceFrameBudgetSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFrameBudgetSlot.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosCfmServiceFrameBudgetSlot.setUnits("frames/sec")
_WwpLeosTceCfmMIBObj_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmMIBObj = _WwpLeosTceCfmMIBObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20)
)
_WwpLeosTceCfmMIP_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmMIP = _WwpLeosTceCfmMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1)
)
_WwpLeosTceCfmMipTable_Object = MibTable
wwpLeosTceCfmMipTable = _WwpLeosTceCfmMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipTable.setStatus("current")
_WwpLeosTceCfmMipEntry_Object = MibTableRow
wwpLeosTceCfmMipEntry = _WwpLeosTceCfmMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1)
)
wwpLeosTceCfmMipEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmMipLiType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmMipLiIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipEntry.setStatus("current")


class _WwpLeosTceCfmMipLiType_Type(Integer32):
    """Custom type wwpLeosTceCfmMipLiType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("mplsDynamicMtuSpokeVC", 8),
          ("mplsDynamicPeMeshVC", 4),
          ("mplsDynamicPeSpokeVC", 6),
          ("mplsStaticMtuSpokeVC", 7),
          ("mplsStaticPeMeshVC", 3),
          ("mplsStaticPeSpokeVC", 5),
          ("none", 99),
          ("pbtService", 2),
          ("subPort", 1))
    )


_WwpLeosTceCfmMipLiType_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipLiType_Object = MibTableColumn
wwpLeosTceCfmMipLiType = _WwpLeosTceCfmMipLiType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 1),
    _WwpLeosTceCfmMipLiType_Type()
)
wwpLeosTceCfmMipLiType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipLiType.setStatus("current")


class _WwpLeosTceCfmMipLiIndex_Type(Integer32):
    """Custom type wwpLeosTceCfmMipLiIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmMipLiIndex_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipLiIndex_Object = MibTableColumn
wwpLeosTceCfmMipLiIndex = _WwpLeosTceCfmMipLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 2),
    _WwpLeosTceCfmMipLiIndex_Type()
)
wwpLeosTceCfmMipLiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipLiIndex.setStatus("current")
_WwpLeosTceCfmMipPgid_Type = Unsigned32
_WwpLeosTceCfmMipPgid_Object = MibTableColumn
wwpLeosTceCfmMipPgid = _WwpLeosTceCfmMipPgid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 3),
    _WwpLeosTceCfmMipPgid_Type()
)
wwpLeosTceCfmMipPgid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipPgid.setStatus("current")


class _WwpLeosTceCfmMipBayIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMipBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmMipBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMipBayIndex_Object = MibTableColumn
wwpLeosTceCfmMipBayIndex = _WwpLeosTceCfmMipBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 4),
    _WwpLeosTceCfmMipBayIndex_Type()
)
wwpLeosTceCfmMipBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipBayIndex.setStatus("current")


class _WwpLeosTceCfmMipShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMipShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmMipShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMipShelfIndex_Object = MibTableColumn
wwpLeosTceCfmMipShelfIndex = _WwpLeosTceCfmMipShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 5),
    _WwpLeosTceCfmMipShelfIndex_Type()
)
wwpLeosTceCfmMipShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipShelfIndex.setStatus("current")


class _WwpLeosTceCfmMipModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMipModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosTceCfmMipModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMipModuleIndex_Object = MibTableColumn
wwpLeosTceCfmMipModuleIndex = _WwpLeosTceCfmMipModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 6),
    _WwpLeosTceCfmMipModuleIndex_Type()
)
wwpLeosTceCfmMipModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipModuleIndex.setStatus("current")
_WwpLeosTceCfmMipMacAddr_Type = MacAddress
_WwpLeosTceCfmMipMacAddr_Object = MibTableColumn
wwpLeosTceCfmMipMacAddr = _WwpLeosTceCfmMipMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 7),
    _WwpLeosTceCfmMipMacAddr_Type()
)
wwpLeosTceCfmMipMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipMacAddr.setStatus("current")


class _WwpLeosTceCfmMipLevel_Type(Integer32):
    """Custom type wwpLeosTceCfmMipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmMipLevel_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipLevel_Object = MibTableColumn
wwpLeosTceCfmMipLevel = _WwpLeosTceCfmMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 8),
    _WwpLeosTceCfmMipLevel_Type()
)
wwpLeosTceCfmMipLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipLevel.setStatus("current")
_WwpLeosTceCfmMipStatus_Type = RowStatus
_WwpLeosTceCfmMipStatus_Object = MibTableColumn
wwpLeosTceCfmMipStatus = _WwpLeosTceCfmMipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 9),
    _WwpLeosTceCfmMipStatus_Type()
)
wwpLeosTceCfmMipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipStatus.setStatus("current")
_WwpLeosTceCfmMipLiName_Type = DisplayString
_WwpLeosTceCfmMipLiName_Object = MibTableColumn
wwpLeosTceCfmMipLiName = _WwpLeosTceCfmMipLiName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 1, 1, 1, 10),
    _WwpLeosTceCfmMipLiName_Type()
)
wwpLeosTceCfmMipLiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipLiName.setStatus("current")
_WwpLeosTceCfmLoopback_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmLoopback = _WwpLeosTceCfmLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3)
)
_WwpLeosTceCfmLoopbackMsgTable_Object = MibTable
wwpLeosTceCfmLoopbackMsgTable = _WwpLeosTceCfmLoopbackMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTable.setStatus("current")
_WwpLeosTceCfmLoopbackMsgEntry_Object = MibTableRow
wwpLeosTceCfmLoopbackMsgEntry = _WwpLeosTceCfmLoopbackMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1)
)
wwpLeosTceCfmLoopbackMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmLoopbackMsgLocalMEPID"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgEntry.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgLocalMEPID_Type(Unsigned32):
    """Custom type wwpLeosTceCfmLoopbackMsgLocalMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmLoopbackMsgLocalMEPID_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmLoopbackMsgLocalMEPID_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgLocalMEPID = _WwpLeosTceCfmLoopbackMsgLocalMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 1),
    _WwpLeosTceCfmLoopbackMsgLocalMEPID_Type()
)
wwpLeosTceCfmLoopbackMsgLocalMEPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgLocalMEPID.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosTceCfmLoopbackMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmLoopbackMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmLoopbackMsgTargetMEPID_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTargetMEPID = _WwpLeosTceCfmLoopbackMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 2),
    _WwpLeosTceCfmLoopbackMsgTargetMEPID_Type()
)
wwpLeosTceCfmLoopbackMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTargetMEPID.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTargetMacAddr_Type = MacAddress
_WwpLeosTceCfmLoopbackMsgTargetMacAddr_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTargetMacAddr = _WwpLeosTceCfmLoopbackMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 3),
    _WwpLeosTceCfmLoopbackMsgTargetMacAddr_Type()
)
wwpLeosTceCfmLoopbackMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTargetMacAddr.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgCount_Type(Integer32):
    """Custom type wwpLeosTceCfmLoopbackMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WwpLeosTceCfmLoopbackMsgCount_Type.__name__ = "Integer32"
_WwpLeosTceCfmLoopbackMsgCount_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgCount = _WwpLeosTceCfmLoopbackMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 4),
    _WwpLeosTceCfmLoopbackMsgCount_Type()
)
wwpLeosTceCfmLoopbackMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgCount.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgData_Type(DisplayString):
    """Custom type wwpLeosTceCfmLoopbackMsgData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_WwpLeosTceCfmLoopbackMsgData_Type.__name__ = "DisplayString"
_WwpLeosTceCfmLoopbackMsgData_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgData = _WwpLeosTceCfmLoopbackMsgData_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 5),
    _WwpLeosTceCfmLoopbackMsgData_Type()
)
wwpLeosTceCfmLoopbackMsgData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgData.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgPriority_Type(Integer32):
    """Custom type wwpLeosTceCfmLoopbackMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmLoopbackMsgPriority_Type.__name__ = "Integer32"
_WwpLeosTceCfmLoopbackMsgPriority_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgPriority = _WwpLeosTceCfmLoopbackMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 6),
    _WwpLeosTceCfmLoopbackMsgPriority_Type()
)
wwpLeosTceCfmLoopbackMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgPriority.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgServiceName_Type(DisplayString):
    """Custom type wwpLeosTceCfmLoopbackMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmLoopbackMsgServiceName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmLoopbackMsgServiceName_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgServiceName = _WwpLeosTceCfmLoopbackMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 7),
    _WwpLeosTceCfmLoopbackMsgServiceName_Type()
)
wwpLeosTceCfmLoopbackMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgServiceName.setStatus("current")


class _WwpLeosTceCfmLoopbackMsgSubPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmLoopbackMsgSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmLoopbackMsgSubPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmLoopbackMsgSubPortName_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgSubPortName = _WwpLeosTceCfmLoopbackMsgSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 8),
    _WwpLeosTceCfmLoopbackMsgSubPortName_Type()
)
wwpLeosTceCfmLoopbackMsgSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgSubPortName.setStatus("current")
_WwpLeosTceCfmLoopbackMsgNextLbmTransId_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgNextLbmTransId_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgNextLbmTransId = _WwpLeosTceCfmLoopbackMsgNextLbmTransId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 9),
    _WwpLeosTceCfmLoopbackMsgNextLbmTransId_Type()
)
wwpLeosTceCfmLoopbackMsgNextLbmTransId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgNextLbmTransId.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTotalTxLbm_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgTotalTxLbm_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTotalTxLbm = _WwpLeosTceCfmLoopbackMsgTotalTxLbm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 10),
    _WwpLeosTceCfmLoopbackMsgTotalTxLbm_Type()
)
wwpLeosTceCfmLoopbackMsgTotalTxLbm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTotalTxLbm.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTotalRxLbrIo_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgTotalRxLbrIo_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTotalRxLbrIo = _WwpLeosTceCfmLoopbackMsgTotalRxLbrIo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 11),
    _WwpLeosTceCfmLoopbackMsgTotalRxLbrIo_Type()
)
wwpLeosTceCfmLoopbackMsgTotalRxLbrIo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTotalRxLbrIo.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTotalRxLbrOoo_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgTotalRxLbrOoo_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTotalRxLbrOoo = _WwpLeosTceCfmLoopbackMsgTotalRxLbrOoo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 12),
    _WwpLeosTceCfmLoopbackMsgTotalRxLbrOoo_Type()
)
wwpLeosTceCfmLoopbackMsgTotalRxLbrOoo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTotalRxLbrOoo.setStatus("current")
_WwpLeosTceCfmLoopbackMsgRowStatus_Type = RowStatus
_WwpLeosTceCfmLoopbackMsgRowStatus_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgRowStatus = _WwpLeosTceCfmLoopbackMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 13),
    _WwpLeosTceCfmLoopbackMsgRowStatus_Type()
)
wwpLeosTceCfmLoopbackMsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgRowStatus.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch = _WwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 14),
    _WwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch_Type()
)
wwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch.setStatus("current")
_WwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected_Type = Unsigned32
_WwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected_Object = MibTableColumn
wwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected = _WwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 3, 1, 1, 15),
    _WwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected_Type()
)
wwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected.setStatus("current")
_WwpLeosTceCfmStack_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmStack = _WwpLeosTceCfmStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5)
)
_WwpLeosTceCfmPortStackTable_Object = MibTable
wwpLeosTceCfmPortStackTable = _WwpLeosTceCfmPortStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackTable.setStatus("current")
_WwpLeosTceCfmPortStackEntry_Object = MibTableRow
wwpLeosTceCfmPortStackEntry = _WwpLeosTceCfmPortStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1)
)
wwpLeosTceCfmPortStackEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmPortStackServiceType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmPortStackServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmPortStackSubPortType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmPortStackSubPortIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEntry.setStatus("current")


class _WwpLeosTceCfmPortStackServiceType_Type(Integer32):
    """Custom type wwpLeosTceCfmPortStackServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pbt", 2),
          ("vs", 1))
    )


_WwpLeosTceCfmPortStackServiceType_Type.__name__ = "Integer32"
_WwpLeosTceCfmPortStackServiceType_Object = MibTableColumn
wwpLeosTceCfmPortStackServiceType = _WwpLeosTceCfmPortStackServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 1),
    _WwpLeosTceCfmPortStackServiceType_Type()
)
wwpLeosTceCfmPortStackServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackServiceType.setStatus("current")


class _WwpLeosTceCfmPortStackServiceIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmPortStackServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmPortStackServiceIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmPortStackServiceIndex_Object = MibTableColumn
wwpLeosTceCfmPortStackServiceIndex = _WwpLeosTceCfmPortStackServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 2),
    _WwpLeosTceCfmPortStackServiceIndex_Type()
)
wwpLeosTceCfmPortStackServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackServiceIndex.setStatus("current")


class _WwpLeosTceCfmPortStackSubPortType_Type(Integer32):
    """Custom type wwpLeosTceCfmPortStackSubPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("decapPbt", 3),
          ("encapPbt", 2),
          ("vs", 1))
    )


_WwpLeosTceCfmPortStackSubPortType_Type.__name__ = "Integer32"
_WwpLeosTceCfmPortStackSubPortType_Object = MibTableColumn
wwpLeosTceCfmPortStackSubPortType = _WwpLeosTceCfmPortStackSubPortType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 3),
    _WwpLeosTceCfmPortStackSubPortType_Type()
)
wwpLeosTceCfmPortStackSubPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackSubPortType.setStatus("current")
_WwpLeosTceCfmPortStackSubPortIndex_Type = Unsigned32
_WwpLeosTceCfmPortStackSubPortIndex_Object = MibTableColumn
wwpLeosTceCfmPortStackSubPortIndex = _WwpLeosTceCfmPortStackSubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 4),
    _WwpLeosTceCfmPortStackSubPortIndex_Type()
)
wwpLeosTceCfmPortStackSubPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackSubPortIndex.setStatus("current")


class _WwpLeosTceCfmPortStackSubPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmPortStackSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmPortStackSubPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmPortStackSubPortName_Object = MibTableColumn
wwpLeosTceCfmPortStackSubPortName = _WwpLeosTceCfmPortStackSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 5),
    _WwpLeosTceCfmPortStackSubPortName_Type()
)
wwpLeosTceCfmPortStackSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackSubPortName.setStatus("current")


class _WwpLeosTceCfmPortStackOperState_Type(Integer32):
    """Custom type wwpLeosTceCfmPortStackOperState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 4),
          ("enabled", 3),
          ("invalid", 2),
          ("loopbackRx", 7),
          ("loopbackTx", 6),
          ("notAuthenticated", 5),
          ("unequipped", 8),
          ("unknown", 1))
    )


_WwpLeosTceCfmPortStackOperState_Type.__name__ = "Integer32"
_WwpLeosTceCfmPortStackOperState_Object = MibTableColumn
wwpLeosTceCfmPortStackOperState = _WwpLeosTceCfmPortStackOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 6),
    _WwpLeosTceCfmPortStackOperState_Type()
)
wwpLeosTceCfmPortStackOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackOperState.setStatus("current")
_WwpLeosTceCfmPortStackPgid_Type = Unsigned32
_WwpLeosTceCfmPortStackPgid_Object = MibTableColumn
wwpLeosTceCfmPortStackPgid = _WwpLeosTceCfmPortStackPgid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 7),
    _WwpLeosTceCfmPortStackPgid_Type()
)
wwpLeosTceCfmPortStackPgid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackPgid.setStatus("current")


class _WwpLeosTceCfmPortStackBayIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmPortStackBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmPortStackBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmPortStackBayIndex_Object = MibTableColumn
wwpLeosTceCfmPortStackBayIndex = _WwpLeosTceCfmPortStackBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 8),
    _WwpLeosTceCfmPortStackBayIndex_Type()
)
wwpLeosTceCfmPortStackBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackBayIndex.setStatus("current")


class _WwpLeosTceCfmPortStackShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmPortStackShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmPortStackShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmPortStackShelfIndex_Object = MibTableColumn
wwpLeosTceCfmPortStackShelfIndex = _WwpLeosTceCfmPortStackShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 9),
    _WwpLeosTceCfmPortStackShelfIndex_Type()
)
wwpLeosTceCfmPortStackShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackShelfIndex.setStatus("current")


class _WwpLeosTceCfmPortStackModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmPortStackModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosTceCfmPortStackModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmPortStackModuleIndex_Object = MibTableColumn
wwpLeosTceCfmPortStackModuleIndex = _WwpLeosTceCfmPortStackModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 10),
    _WwpLeosTceCfmPortStackModuleIndex_Type()
)
wwpLeosTceCfmPortStackModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackModuleIndex.setStatus("current")


class _WwpLeosTceCfmPortStackVsPbtName_Type(DisplayString):
    """Custom type wwpLeosTceCfmPortStackVsPbtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosTceCfmPortStackVsPbtName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmPortStackVsPbtName_Object = MibTableColumn
wwpLeosTceCfmPortStackVsPbtName = _WwpLeosTceCfmPortStackVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 11),
    _WwpLeosTceCfmPortStackVsPbtName_Type()
)
wwpLeosTceCfmPortStackVsPbtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackVsPbtName.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagValue1_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagValue1_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagValue1 = _WwpLeosTceCfmPortStackEgressXformTagValue1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 13),
    _WwpLeosTceCfmPortStackEgressXformTagValue1_Type()
)
wwpLeosTceCfmPortStackEgressXformTagValue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagValue1.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagPriority1_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagPriority1_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagPriority1 = _WwpLeosTceCfmPortStackEgressXformTagPriority1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 14),
    _WwpLeosTceCfmPortStackEgressXformTagPriority1_Type()
)
wwpLeosTceCfmPortStackEgressXformTagPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagPriority1.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagEtype1_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagEtype1_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagEtype1 = _WwpLeosTceCfmPortStackEgressXformTagEtype1_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 15),
    _WwpLeosTceCfmPortStackEgressXformTagEtype1_Type()
)
wwpLeosTceCfmPortStackEgressXformTagEtype1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagEtype1.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagValue2_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagValue2_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagValue2 = _WwpLeosTceCfmPortStackEgressXformTagValue2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 16),
    _WwpLeosTceCfmPortStackEgressXformTagValue2_Type()
)
wwpLeosTceCfmPortStackEgressXformTagValue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagValue2.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagPriority2_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagPriority2_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagPriority2 = _WwpLeosTceCfmPortStackEgressXformTagPriority2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 17),
    _WwpLeosTceCfmPortStackEgressXformTagPriority2_Type()
)
wwpLeosTceCfmPortStackEgressXformTagPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagPriority2.setStatus("current")
_WwpLeosTceCfmPortStackEgressXformTagEtype2_Type = Unsigned32
_WwpLeosTceCfmPortStackEgressXformTagEtype2_Object = MibTableColumn
wwpLeosTceCfmPortStackEgressXformTagEtype2 = _WwpLeosTceCfmPortStackEgressXformTagEtype2_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 18),
    _WwpLeosTceCfmPortStackEgressXformTagEtype2_Type()
)
wwpLeosTceCfmPortStackEgressXformTagEtype2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackEgressXformTagEtype2.setStatus("current")
_WwpLeosTceCfmPortStackMepCount_Type = Unsigned32
_WwpLeosTceCfmPortStackMepCount_Object = MibTableColumn
wwpLeosTceCfmPortStackMepCount = _WwpLeosTceCfmPortStackMepCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 19),
    _WwpLeosTceCfmPortStackMepCount_Type()
)
wwpLeosTceCfmPortStackMepCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackMepCount.setStatus("current")
_WwpLeosTceCfmPortStackMipLevel_Type = Unsigned32
_WwpLeosTceCfmPortStackMipLevel_Object = MibTableColumn
wwpLeosTceCfmPortStackMipLevel = _WwpLeosTceCfmPortStackMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 5, 1, 1, 20),
    _WwpLeosTceCfmPortStackMipLevel_Type()
)
wwpLeosTceCfmPortStackMipLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmPortStackMipLevel.setStatus("current")
_WwpLeosTceCfmMEP_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmMEP = _WwpLeosTceCfmMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7)
)
_WwpLeosTceCfmMEPTable_Object = MibTable
wwpLeosTceCfmMEPTable = _WwpLeosTceCfmMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPTable.setStatus("current")
_WwpLeosTceCfmMEPEntry_Object = MibTableRow
wwpLeosTceCfmMEPEntry = _WwpLeosTceCfmMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1)
)
wwpLeosTceCfmMEPEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPEntry.setStatus("current")


class _WwpLeosTceCfmMEPId_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmMEPId_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPId_Object = MibTableColumn
wwpLeosTceCfmMEPId = _WwpLeosTceCfmMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 1),
    _WwpLeosTceCfmMEPId_Type()
)
wwpLeosTceCfmMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPId.setStatus("current")


class _WwpLeosTceCfmMEPAdminState_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosTceCfmMEPAdminState_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPAdminState_Object = MibTableColumn
wwpLeosTceCfmMEPAdminState = _WwpLeosTceCfmMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 2),
    _WwpLeosTceCfmMEPAdminState_Type()
)
wwpLeosTceCfmMEPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPAdminState.setStatus("current")


class _WwpLeosTceCfmMEPOperState_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosTceCfmMEPOperState_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPOperState_Object = MibTableColumn
wwpLeosTceCfmMEPOperState = _WwpLeosTceCfmMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 3),
    _WwpLeosTceCfmMEPOperState_Type()
)
wwpLeosTceCfmMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPOperState.setStatus("current")


class _WwpLeosTceCfmMEPDirection_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPDirection based on Integer32"""
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


_WwpLeosTceCfmMEPDirection_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPDirection_Object = MibTableColumn
wwpLeosTceCfmMEPDirection = _WwpLeosTceCfmMEPDirection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 4),
    _WwpLeosTceCfmMEPDirection_Type()
)
wwpLeosTceCfmMEPDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPDirection.setStatus("current")


class _WwpLeosTceCfmMEPCCMState_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPCCMState based on Integer32"""
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


_WwpLeosTceCfmMEPCCMState_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPCCMState_Object = MibTableColumn
wwpLeosTceCfmMEPCCMState = _WwpLeosTceCfmMEPCCMState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 5),
    _WwpLeosTceCfmMEPCCMState_Type()
)
wwpLeosTceCfmMEPCCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPCCMState.setStatus("current")


class _WwpLeosTceCfmMEPCCMPriority_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPCCMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmMEPCCMPriority_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPCCMPriority_Object = MibTableColumn
wwpLeosTceCfmMEPCCMPriority = _WwpLeosTceCfmMEPCCMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 6),
    _WwpLeosTceCfmMEPCCMPriority_Type()
)
wwpLeosTceCfmMEPCCMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPCCMPriority.setStatus("current")


class _WwpLeosTceCfmMEPLTMPriority_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPLTMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmMEPLTMPriority_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPLTMPriority_Object = MibTableColumn
wwpLeosTceCfmMEPLTMPriority = _WwpLeosTceCfmMEPLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 7),
    _WwpLeosTceCfmMEPLTMPriority_Type()
)
wwpLeosTceCfmMEPLTMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLTMPriority.setStatus("current")
_WwpLeosTceCfmMEPMacAddr_Type = MacAddress
_WwpLeosTceCfmMEPMacAddr_Object = MibTableColumn
wwpLeosTceCfmMEPMacAddr = _WwpLeosTceCfmMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 8),
    _WwpLeosTceCfmMEPMacAddr_Type()
)
wwpLeosTceCfmMEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPMacAddr.setStatus("current")
_WwpLeosTceCfmMEPNextLbmSeqNumber_Type = Counter32
_WwpLeosTceCfmMEPNextLbmSeqNumber_Object = MibTableColumn
wwpLeosTceCfmMEPNextLbmSeqNumber = _WwpLeosTceCfmMEPNextLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 9),
    _WwpLeosTceCfmMEPNextLbmSeqNumber_Type()
)
wwpLeosTceCfmMEPNextLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNextLbmSeqNumber.setStatus("current")
_WwpLeosTceCfmMEPRxValidInOrderLoopbackReply_Type = Counter32
_WwpLeosTceCfmMEPRxValidInOrderLoopbackReply_Object = MibTableColumn
wwpLeosTceCfmMEPRxValidInOrderLoopbackReply = _WwpLeosTceCfmMEPRxValidInOrderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 10),
    _WwpLeosTceCfmMEPRxValidInOrderLoopbackReply_Type()
)
wwpLeosTceCfmMEPRxValidInOrderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPRxValidInOrderLoopbackReply.setStatus("current")
_WwpLeosTceCfmMEPRxValidOutOrderLoopbackReply_Type = Counter32
_WwpLeosTceCfmMEPRxValidOutOrderLoopbackReply_Object = MibTableColumn
wwpLeosTceCfmMEPRxValidOutOrderLoopbackReply = _WwpLeosTceCfmMEPRxValidOutOrderLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 11),
    _WwpLeosTceCfmMEPRxValidOutOrderLoopbackReply_Type()
)
wwpLeosTceCfmMEPRxValidOutOrderLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPRxValidOutOrderLoopbackReply.setStatus("current")
_WwpLeosTceCfmMEPNextLTMSeqNumber_Type = Counter32
_WwpLeosTceCfmMEPNextLTMSeqNumber_Object = MibTableColumn
wwpLeosTceCfmMEPNextLTMSeqNumber = _WwpLeosTceCfmMEPNextLTMSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 12),
    _WwpLeosTceCfmMEPNextLTMSeqNumber_Type()
)
wwpLeosTceCfmMEPNextLTMSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNextLTMSeqNumber.setStatus("current")
_WwpLeosTceCfmMEPNumLoopbackRepliesTxmt_Type = Counter32
_WwpLeosTceCfmMEPNumLoopbackRepliesTxmt_Object = MibTableColumn
wwpLeosTceCfmMEPNumLoopbackRepliesTxmt = _WwpLeosTceCfmMEPNumLoopbackRepliesTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 13),
    _WwpLeosTceCfmMEPNumLoopbackRepliesTxmt_Type()
)
wwpLeosTceCfmMEPNumLoopbackRepliesTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLoopbackRepliesTxmt.setStatus("current")
_WwpLeosTceCfmMEPNumLTMRecevied_Type = Counter32
_WwpLeosTceCfmMEPNumLTMRecevied_Object = MibTableColumn
wwpLeosTceCfmMEPNumLTMRecevied = _WwpLeosTceCfmMEPNumLTMRecevied_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 14),
    _WwpLeosTceCfmMEPNumLTMRecevied_Type()
)
wwpLeosTceCfmMEPNumLTMRecevied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLTMRecevied.setStatus("current")
_WwpLeosTceCfmMEPNumLTMTxmt_Type = Counter32
_WwpLeosTceCfmMEPNumLTMTxmt_Object = MibTableColumn
wwpLeosTceCfmMEPNumLTMTxmt = _WwpLeosTceCfmMEPNumLTMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 15),
    _WwpLeosTceCfmMEPNumLTMTxmt_Type()
)
wwpLeosTceCfmMEPNumLTMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLTMTxmt.setStatus("current")
_WwpLeosTceCfmMEPNumCCMTxmt_Type = Counter32
_WwpLeosTceCfmMEPNumCCMTxmt_Object = MibTableColumn
wwpLeosTceCfmMEPNumCCMTxmt = _WwpLeosTceCfmMEPNumCCMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 16),
    _WwpLeosTceCfmMEPNumCCMTxmt_Type()
)
wwpLeosTceCfmMEPNumCCMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumCCMTxmt.setStatus("current")
_WwpLeosTceCfmMEPRowStatus_Type = RowStatus
_WwpLeosTceCfmMEPRowStatus_Object = MibTableColumn
wwpLeosTceCfmMEPRowStatus = _WwpLeosTceCfmMEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 17),
    _WwpLeosTceCfmMEPRowStatus_Type()
)
wwpLeosTceCfmMEPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPRowStatus.setStatus("current")
_WwpLeosTceCfmMEPNumDMMSent_Type = Counter32
_WwpLeosTceCfmMEPNumDMMSent_Object = MibTableColumn
wwpLeosTceCfmMEPNumDMMSent = _WwpLeosTceCfmMEPNumDMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 18),
    _WwpLeosTceCfmMEPNumDMMSent_Type()
)
wwpLeosTceCfmMEPNumDMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumDMMSent.setStatus("current")
_WwpLeosTceCfmMEPDMMDelay_Type = Counter32
_WwpLeosTceCfmMEPDMMDelay_Object = MibTableColumn
wwpLeosTceCfmMEPDMMDelay = _WwpLeosTceCfmMEPDMMDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 19),
    _WwpLeosTceCfmMEPDMMDelay_Type()
)
wwpLeosTceCfmMEPDMMDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPDMMDelay.setStatus("current")
_WwpLeosTceCfmMEPDMMJitter_Type = Counter32
_WwpLeosTceCfmMEPDMMJitter_Object = MibTableColumn
wwpLeosTceCfmMEPDMMJitter = _WwpLeosTceCfmMEPDMMJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 20),
    _WwpLeosTceCfmMEPDMMJitter_Type()
)
wwpLeosTceCfmMEPDMMJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPDMMJitter.setStatus("current")
_WwpLeosTceCfmMEPNumLMMSent_Type = Counter32
_WwpLeosTceCfmMEPNumLMMSent_Object = MibTableColumn
wwpLeosTceCfmMEPNumLMMSent = _WwpLeosTceCfmMEPNumLMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 21),
    _WwpLeosTceCfmMEPNumLMMSent_Type()
)
wwpLeosTceCfmMEPNumLMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLMMSent.setStatus("current")
_WwpLeosTceCfmMEPLMMFrameLossNear_Type = Counter32
_WwpLeosTceCfmMEPLMMFrameLossNear_Object = MibTableColumn
wwpLeosTceCfmMEPLMMFrameLossNear = _WwpLeosTceCfmMEPLMMFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 22),
    _WwpLeosTceCfmMEPLMMFrameLossNear_Type()
)
wwpLeosTceCfmMEPLMMFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLMMFrameLossNear.setStatus("current")
_WwpLeosTceCfmMEPLMMFrameLossFar_Type = Counter32
_WwpLeosTceCfmMEPLMMFrameLossFar_Object = MibTableColumn
wwpLeosTceCfmMEPLMMFrameLossFar = _WwpLeosTceCfmMEPLMMFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 23),
    _WwpLeosTceCfmMEPLMMFrameLossFar_Type()
)
wwpLeosTceCfmMEPLMMFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLMMFrameLossFar.setStatus("current")


class _WwpLeosTceCfmMEPLiType_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPLiType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("mplsDynamicMtuSpokeVC", 8),
          ("mplsDynamicPeMeshVC", 4),
          ("mplsDynamicPeSpokeVC", 6),
          ("mplsStaticMtuSpokeVC", 7),
          ("mplsStaticPeMeshVC", 3),
          ("mplsStaticPeSpokeVC", 5),
          ("none", 99),
          ("pbtService", 2),
          ("vs", 1))
    )


_WwpLeosTceCfmMEPLiType_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPLiType_Object = MibTableColumn
wwpLeosTceCfmMEPLiType = _WwpLeosTceCfmMEPLiType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 24),
    _WwpLeosTceCfmMEPLiType_Type()
)
wwpLeosTceCfmMEPLiType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLiType.setStatus("current")
_WwpLeosTceCfmMEPLiIndex_Type = Unsigned32
_WwpLeosTceCfmMEPLiIndex_Object = MibTableColumn
wwpLeosTceCfmMEPLiIndex = _WwpLeosTceCfmMEPLiIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 25),
    _WwpLeosTceCfmMEPLiIndex_Type()
)
wwpLeosTceCfmMEPLiIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLiIndex.setStatus("current")


class _WwpLeosTceCfmMEPServiceName_Type(DisplayString):
    """Custom type wwpLeosTceCfmMEPServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTceCfmMEPServiceName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmMEPServiceName_Object = MibTableColumn
wwpLeosTceCfmMEPServiceName = _WwpLeosTceCfmMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 50),
    _WwpLeosTceCfmMEPServiceName_Type()
)
wwpLeosTceCfmMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPServiceName.setStatus("current")


class _WwpLeosTceCfmMEPSubPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmMEPSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTceCfmMEPSubPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmMEPSubPortName_Object = MibTableColumn
wwpLeosTceCfmMEPSubPortName = _WwpLeosTceCfmMEPSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 51),
    _WwpLeosTceCfmMEPSubPortName_Type()
)
wwpLeosTceCfmMEPSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPSubPortName.setStatus("current")


class _WwpLeosTceCfmMEPVsPbtName_Type(DisplayString):
    """Custom type wwpLeosTceCfmMEPVsPbtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTceCfmMEPVsPbtName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmMEPVsPbtName_Object = MibTableColumn
wwpLeosTceCfmMEPVsPbtName = _WwpLeosTceCfmMEPVsPbtName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 52),
    _WwpLeosTceCfmMEPVsPbtName_Type()
)
wwpLeosTceCfmMEPVsPbtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPVsPbtName.setStatus("current")


class _WwpLeosTceCfmMEPLogicalPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmMEPLogicalPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosTceCfmMEPLogicalPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmMEPLogicalPortName_Object = MibTableColumn
wwpLeosTceCfmMEPLogicalPortName = _WwpLeosTceCfmMEPLogicalPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 53),
    _WwpLeosTceCfmMEPLogicalPortName_Type()
)
wwpLeosTceCfmMEPLogicalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLogicalPortName.setStatus("current")
_WwpLeosTceCfmMEPSubPortIndex_Type = Unsigned32
_WwpLeosTceCfmMEPSubPortIndex_Object = MibTableColumn
wwpLeosTceCfmMEPSubPortIndex = _WwpLeosTceCfmMEPSubPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 54),
    _WwpLeosTceCfmMEPSubPortIndex_Type()
)
wwpLeosTceCfmMEPSubPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPSubPortIndex.setStatus("current")


class _WwpLeosTceCfmMEPEncapsulation_Type(Integer32):
    """Custom type wwpLeosTceCfmMEPEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot1d", 1),
          ("pbtCfmEncap", 2))
    )


_WwpLeosTceCfmMEPEncapsulation_Type.__name__ = "Integer32"
_WwpLeosTceCfmMEPEncapsulation_Object = MibTableColumn
wwpLeosTceCfmMEPEncapsulation = _WwpLeosTceCfmMEPEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 55),
    _WwpLeosTceCfmMEPEncapsulation_Type()
)
wwpLeosTceCfmMEPEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPEncapsulation.setStatus("current")


class _WwpLeosTceCfmMEPLeadPortBayIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPLeadPortBayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmMEPLeadPortBayIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPLeadPortBayIndex_Object = MibTableColumn
wwpLeosTceCfmMEPLeadPortBayIndex = _WwpLeosTceCfmMEPLeadPortBayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 56),
    _WwpLeosTceCfmMEPLeadPortBayIndex_Type()
)
wwpLeosTceCfmMEPLeadPortBayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLeadPortBayIndex.setStatus("current")


class _WwpLeosTceCfmMEPLeadPortShelfIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPLeadPortShelfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosTceCfmMEPLeadPortShelfIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPLeadPortShelfIndex_Object = MibTableColumn
wwpLeosTceCfmMEPLeadPortShelfIndex = _WwpLeosTceCfmMEPLeadPortShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 57),
    _WwpLeosTceCfmMEPLeadPortShelfIndex_Type()
)
wwpLeosTceCfmMEPLeadPortShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLeadPortShelfIndex.setStatus("current")


class _WwpLeosTceCfmMEPLeadPortModuleIndex_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPLeadPortModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
        ValueRangeConstraint(255, 255),
    )


_WwpLeosTceCfmMEPLeadPortModuleIndex_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPLeadPortModuleIndex_Object = MibTableColumn
wwpLeosTceCfmMEPLeadPortModuleIndex = _WwpLeosTceCfmMEPLeadPortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 58),
    _WwpLeosTceCfmMEPLeadPortModuleIndex_Type()
)
wwpLeosTceCfmMEPLeadPortModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPLeadPortModuleIndex.setStatus("current")


class _WwpLeosTceCfmMEPPBTBvid_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPPBTBvid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmMEPPBTBvid_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPPBTBvid_Object = MibTableColumn
wwpLeosTceCfmMEPPBTBvid = _WwpLeosTceCfmMEPPBTBvid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 59),
    _WwpLeosTceCfmMEPPBTBvid_Type()
)
wwpLeosTceCfmMEPPBTBvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPPBTBvid.setStatus("current")


class _WwpLeosTceCfmMEPPBTEtype_Type(Unsigned32):
    """Custom type wwpLeosTceCfmMEPPBTEtype based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmMEPPBTEtype_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmMEPPBTEtype_Object = MibTableColumn
wwpLeosTceCfmMEPPBTEtype = _WwpLeosTceCfmMEPPBTEtype_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 60),
    _WwpLeosTceCfmMEPPBTEtype_Type()
)
wwpLeosTceCfmMEPPBTEtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPPBTEtype.setStatus("current")
_WwpLeosTceCfmMEPNumLbmTxmt_Type = Counter32
_WwpLeosTceCfmMEPNumLbmTxmt_Object = MibTableColumn
wwpLeosTceCfmMEPNumLbmTxmt = _WwpLeosTceCfmMEPNumLbmTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 61),
    _WwpLeosTceCfmMEPNumLbmTxmt_Type()
)
wwpLeosTceCfmMEPNumLbmTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLbmTxmt.setStatus("current")
_WwpLeosTceCfmMEPNumLbmReceived_Type = Counter32
_WwpLeosTceCfmMEPNumLbmReceived_Object = MibTableColumn
wwpLeosTceCfmMEPNumLbmReceived = _WwpLeosTceCfmMEPNumLbmReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 62),
    _WwpLeosTceCfmMEPNumLbmReceived_Type()
)
wwpLeosTceCfmMEPNumLbmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLbmReceived.setStatus("current")
_WwpLeosTceCfmMEPNumLoopbackRepliesReceived_Type = Counter32
_WwpLeosTceCfmMEPNumLoopbackRepliesReceived_Object = MibTableColumn
wwpLeosTceCfmMEPNumLoopbackRepliesReceived = _WwpLeosTceCfmMEPNumLoopbackRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 63),
    _WwpLeosTceCfmMEPNumLoopbackRepliesReceived_Type()
)
wwpLeosTceCfmMEPNumLoopbackRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLoopbackRepliesReceived.setStatus("current")
_WwpLeosTceCfmMEPNumLTRepliesTxmt_Type = Counter32
_WwpLeosTceCfmMEPNumLTRepliesTxmt_Object = MibTableColumn
wwpLeosTceCfmMEPNumLTRepliesTxmt = _WwpLeosTceCfmMEPNumLTRepliesTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 64),
    _WwpLeosTceCfmMEPNumLTRepliesTxmt_Type()
)
wwpLeosTceCfmMEPNumLTRepliesTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLTRepliesTxmt.setStatus("current")
_WwpLeosTceCfmMEPNumLTRepliesReceived_Type = Counter32
_WwpLeosTceCfmMEPNumLTRepliesReceived_Object = MibTableColumn
wwpLeosTceCfmMEPNumLTRepliesReceived = _WwpLeosTceCfmMEPNumLTRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 65),
    _WwpLeosTceCfmMEPNumLTRepliesReceived_Type()
)
wwpLeosTceCfmMEPNumLTRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumLTRepliesReceived.setStatus("current")
_WwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived_Type = Counter32
_WwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived_Object = MibTableColumn
wwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived = _WwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 66),
    _WwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived_Type()
)
wwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived.setStatus("current")
_WwpLeosTceCfmMEPNumCCMReceived_Type = Counter32
_WwpLeosTceCfmMEPNumCCMReceived_Object = MibTableColumn
wwpLeosTceCfmMEPNumCCMReceived = _WwpLeosTceCfmMEPNumCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 67),
    _WwpLeosTceCfmMEPNumCCMReceived_Type()
)
wwpLeosTceCfmMEPNumCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPNumCCMReceived.setStatus("current")
_WwpLeosTceCfmMEPRxContentMismatchLoopbackReply_Type = Counter32
_WwpLeosTceCfmMEPRxContentMismatchLoopbackReply_Object = MibTableColumn
wwpLeosTceCfmMEPRxContentMismatchLoopbackReply = _WwpLeosTceCfmMEPRxContentMismatchLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 68),
    _WwpLeosTceCfmMEPRxContentMismatchLoopbackReply_Type()
)
wwpLeosTceCfmMEPRxContentMismatchLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPRxContentMismatchLoopbackReply.setStatus("current")
_WwpLeosTceCfmMEPRxUnexpectedLoopbackReply_Type = Counter32
_WwpLeosTceCfmMEPRxUnexpectedLoopbackReply_Object = MibTableColumn
wwpLeosTceCfmMEPRxUnexpectedLoopbackReply = _WwpLeosTceCfmMEPRxUnexpectedLoopbackReply_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 7, 1, 1, 69),
    _WwpLeosTceCfmMEPRxUnexpectedLoopbackReply_Type()
)
wwpLeosTceCfmMEPRxUnexpectedLoopbackReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMEPRxUnexpectedLoopbackReply.setStatus("current")
_WwpLeosTceCfmDelay_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmDelay = _WwpLeosTceCfmDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12)
)
_WwpLeosTceCfmDelayMsgTable_Object = MibTable
wwpLeosTceCfmDelayMsgTable = _WwpLeosTceCfmDelayMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTable.setStatus("current")
_WwpLeosTceCfmDelayMsgEntry_Object = MibTableRow
wwpLeosTceCfmDelayMsgEntry = _WwpLeosTceCfmDelayMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1)
)
wwpLeosTceCfmDelayMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgEntry.setStatus("current")


class _WwpLeosTceCfmDelayMsgLocalMEPId_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmDelayMsgLocalMEPId_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgLocalMEPId_Object = MibTableColumn
wwpLeosTceCfmDelayMsgLocalMEPId = _WwpLeosTceCfmDelayMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 1),
    _WwpLeosTceCfmDelayMsgLocalMEPId_Type()
)
wwpLeosTceCfmDelayMsgLocalMEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgLocalMEPId.setStatus("current")


class _WwpLeosTceCfmDelayMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosTceCfmDelayMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmDelayMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmDelayMsgTargetMEPID_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTargetMEPID = _WwpLeosTceCfmDelayMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 2),
    _WwpLeosTceCfmDelayMsgTargetMEPID_Type()
)
wwpLeosTceCfmDelayMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTargetMEPID.setStatus("current")
_WwpLeosTceCfmDelayMsgTargetMacAddr_Type = MacAddress
_WwpLeosTceCfmDelayMsgTargetMacAddr_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTargetMacAddr = _WwpLeosTceCfmDelayMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 3),
    _WwpLeosTceCfmDelayMsgTargetMacAddr_Type()
)
wwpLeosTceCfmDelayMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTargetMacAddr.setStatus("current")


class _WwpLeosTceCfmDelayMsgCount_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 9000),
    )


_WwpLeosTceCfmDelayMsgCount_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgCount_Object = MibTableColumn
wwpLeosTceCfmDelayMsgCount = _WwpLeosTceCfmDelayMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 4),
    _WwpLeosTceCfmDelayMsgCount_Type()
)
wwpLeosTceCfmDelayMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgCount.setStatus("current")


class _WwpLeosTceCfmDelayMsgPriority_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmDelayMsgPriority_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgPriority_Object = MibTableColumn
wwpLeosTceCfmDelayMsgPriority = _WwpLeosTceCfmDelayMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 5),
    _WwpLeosTceCfmDelayMsgPriority_Type()
)
wwpLeosTceCfmDelayMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgPriority.setStatus("current")
_WwpLeosTceCfmDelayMsgRowStatus_Type = RowStatus
_WwpLeosTceCfmDelayMsgRowStatus_Object = MibTableColumn
wwpLeosTceCfmDelayMsgRowStatus = _WwpLeosTceCfmDelayMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 6),
    _WwpLeosTceCfmDelayMsgRowStatus_Type()
)
wwpLeosTceCfmDelayMsgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgRowStatus.setStatus("current")


class _WwpLeosTceCfmDelayMsgRepeatInterval_Type(Unsigned32):
    """Custom type wwpLeosTceCfmDelayMsgRepeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosTceCfmDelayMsgRepeatInterval_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmDelayMsgRepeatInterval_Object = MibTableColumn
wwpLeosTceCfmDelayMsgRepeatInterval = _WwpLeosTceCfmDelayMsgRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 40),
    _WwpLeosTceCfmDelayMsgRepeatInterval_Type()
)
wwpLeosTceCfmDelayMsgRepeatInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgRepeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgRepeatInterval.setUnits("minutes")


class _WwpLeosTceCfmDelayMsgDelayThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmDelayMsgDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgDelayThreshold_Object = MibTableColumn
wwpLeosTceCfmDelayMsgDelayThreshold = _WwpLeosTceCfmDelayMsgDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 41),
    _WwpLeosTceCfmDelayMsgDelayThreshold_Type()
)
wwpLeosTceCfmDelayMsgDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgDelayThreshold.setStatus("current")


class _WwpLeosTceCfmDelayMsgJitterThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmDelayMsgJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgJitterThreshold_Object = MibTableColumn
wwpLeosTceCfmDelayMsgJitterThreshold = _WwpLeosTceCfmDelayMsgJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 42),
    _WwpLeosTceCfmDelayMsgJitterThreshold_Type()
)
wwpLeosTceCfmDelayMsgJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgJitterThreshold.setStatus("current")


class _WwpLeosTceCfmDelayMsgServiceName_Type(DisplayString):
    """Custom type wwpLeosTceCfmDelayMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmDelayMsgServiceName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmDelayMsgServiceName_Object = MibTableColumn
wwpLeosTceCfmDelayMsgServiceName = _WwpLeosTceCfmDelayMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 43),
    _WwpLeosTceCfmDelayMsgServiceName_Type()
)
wwpLeosTceCfmDelayMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgServiceName.setStatus("current")


class _WwpLeosTceCfmDelayMsgSubPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmDelayMsgSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmDelayMsgSubPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmDelayMsgSubPortName_Object = MibTableColumn
wwpLeosTceCfmDelayMsgSubPortName = _WwpLeosTceCfmDelayMsgSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 44),
    _WwpLeosTceCfmDelayMsgSubPortName_Type()
)
wwpLeosTceCfmDelayMsgSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgSubPortName.setStatus("current")
_WwpLeosTceCfmDelayMsgDelay_Type = Unsigned32
_WwpLeosTceCfmDelayMsgDelay_Object = MibTableColumn
wwpLeosTceCfmDelayMsgDelay = _WwpLeosTceCfmDelayMsgDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 50),
    _WwpLeosTceCfmDelayMsgDelay_Type()
)
wwpLeosTceCfmDelayMsgDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgDelay.setUnits("microseconds")
_WwpLeosTceCfmDelayMsgJitter_Type = Unsigned32
_WwpLeosTceCfmDelayMsgJitter_Object = MibTableColumn
wwpLeosTceCfmDelayMsgJitter = _WwpLeosTceCfmDelayMsgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 51),
    _WwpLeosTceCfmDelayMsgJitter_Type()
)
wwpLeosTceCfmDelayMsgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgJitter.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgJitter.setUnits("microseconds")
_WwpLeosTceCfmDelayMsgTotalTxDmm_Type = Unsigned32
_WwpLeosTceCfmDelayMsgTotalTxDmm_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTotalTxDmm = _WwpLeosTceCfmDelayMsgTotalTxDmm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 52),
    _WwpLeosTceCfmDelayMsgTotalTxDmm_Type()
)
wwpLeosTceCfmDelayMsgTotalTxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTotalTxDmm.setStatus("current")
_WwpLeosTceCfmDelayMsgTotalRxDmm_Type = Unsigned32
_WwpLeosTceCfmDelayMsgTotalRxDmm_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTotalRxDmm = _WwpLeosTceCfmDelayMsgTotalRxDmm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 53),
    _WwpLeosTceCfmDelayMsgTotalRxDmm_Type()
)
wwpLeosTceCfmDelayMsgTotalRxDmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTotalRxDmm.setStatus("current")
_WwpLeosTceCfmDelayMsgTotalTxDmr_Type = Unsigned32
_WwpLeosTceCfmDelayMsgTotalTxDmr_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTotalTxDmr = _WwpLeosTceCfmDelayMsgTotalTxDmr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 54),
    _WwpLeosTceCfmDelayMsgTotalTxDmr_Type()
)
wwpLeosTceCfmDelayMsgTotalTxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTotalTxDmr.setStatus("current")
_WwpLeosTceCfmDelayMsgTotalRxDmr_Type = Unsigned32
_WwpLeosTceCfmDelayMsgTotalRxDmr_Object = MibTableColumn
wwpLeosTceCfmDelayMsgTotalRxDmr = _WwpLeosTceCfmDelayMsgTotalRxDmr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 55),
    _WwpLeosTceCfmDelayMsgTotalRxDmr_Type()
)
wwpLeosTceCfmDelayMsgTotalRxDmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgTotalRxDmr.setStatus("current")
_WwpLeosTceCfmDelayMsgAction_Type = SendState
_WwpLeosTceCfmDelayMsgAction_Object = MibTableColumn
wwpLeosTceCfmDelayMsgAction = _WwpLeosTceCfmDelayMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 56),
    _WwpLeosTceCfmDelayMsgAction_Type()
)
wwpLeosTceCfmDelayMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgAction.setStatus("current")
_WwpLeosTceCfmDelayMsgMaxDelay_Type = Unsigned32
_WwpLeosTceCfmDelayMsgMaxDelay_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMaxDelay = _WwpLeosTceCfmDelayMsgMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 57),
    _WwpLeosTceCfmDelayMsgMaxDelay_Type()
)
wwpLeosTceCfmDelayMsgMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxDelay.setUnits("microseconds")
_WwpLeosTceCfmDelayMsgMaxJitter_Type = Unsigned32
_WwpLeosTceCfmDelayMsgMaxJitter_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMaxJitter = _WwpLeosTceCfmDelayMsgMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 58),
    _WwpLeosTceCfmDelayMsgMaxJitter_Type()
)
wwpLeosTceCfmDelayMsgMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxJitter.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxJitter.setUnits("microseconds")


class _WwpLeosTceCfmDelayMsgMaxDelayThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgMaxDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmDelayMsgMaxDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgMaxDelayThreshold_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMaxDelayThreshold = _WwpLeosTceCfmDelayMsgMaxDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 59),
    _WwpLeosTceCfmDelayMsgMaxDelayThreshold_Type()
)
wwpLeosTceCfmDelayMsgMaxDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxDelayThreshold.setStatus("current")


class _WwpLeosTceCfmDelayMsgMaxJitterThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmDelayMsgMaxJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmDelayMsgMaxJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmDelayMsgMaxJitterThreshold_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMaxJitterThreshold = _WwpLeosTceCfmDelayMsgMaxJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 60),
    _WwpLeosTceCfmDelayMsgMaxJitterThreshold_Type()
)
wwpLeosTceCfmDelayMsgMaxJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMaxJitterThreshold.setStatus("current")
_WwpLeosTceCfmDelayMsgMinDelay_Type = Unsigned32
_WwpLeosTceCfmDelayMsgMinDelay_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMinDelay = _WwpLeosTceCfmDelayMsgMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 61),
    _WwpLeosTceCfmDelayMsgMinDelay_Type()
)
wwpLeosTceCfmDelayMsgMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMinDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMinDelay.setUnits("microseconds")
_WwpLeosTceCfmDelayMsgMinJitter_Type = Unsigned32
_WwpLeosTceCfmDelayMsgMinJitter_Object = MibTableColumn
wwpLeosTceCfmDelayMsgMinJitter = _WwpLeosTceCfmDelayMsgMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 12, 1, 1, 62),
    _WwpLeosTceCfmDelayMsgMinJitter_Type()
)
wwpLeosTceCfmDelayMsgMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMinJitter.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmDelayMsgMinJitter.setUnits("microseconds")
_WwpLeosTceCfmFrameLoss_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmFrameLoss = _WwpLeosTceCfmFrameLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13)
)
_WwpLeosTceCfmFrameLossMsgTable_Object = MibTable
wwpLeosTceCfmFrameLossMsgTable = _WwpLeosTceCfmFrameLossMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTable.setStatus("current")
_WwpLeosTceCfmFrameLossMsgEntry_Object = MibTableRow
wwpLeosTceCfmFrameLossMsgEntry = _WwpLeosTceCfmFrameLossMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1)
)
wwpLeosTceCfmFrameLossMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgEntry.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgLocalMEPId_Type(Integer32):
    """Custom type wwpLeosTceCfmFrameLossMsgLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosTceCfmFrameLossMsgLocalMEPId_Type.__name__ = "Integer32"
_WwpLeosTceCfmFrameLossMsgLocalMEPId_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgLocalMEPId = _WwpLeosTceCfmFrameLossMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 1),
    _WwpLeosTceCfmFrameLossMsgLocalMEPId_Type()
)
wwpLeosTceCfmFrameLossMsgLocalMEPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgLocalMEPId.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosTceCfmFrameLossMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmFrameLossMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmFrameLossMsgTargetMEPID_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTargetMEPID = _WwpLeosTceCfmFrameLossMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 2),
    _WwpLeosTceCfmFrameLossMsgTargetMEPID_Type()
)
wwpLeosTceCfmFrameLossMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTargetMEPID.setStatus("current")
_WwpLeosTceCfmFrameLossMsgTargetMacAddr_Type = MacAddress
_WwpLeosTceCfmFrameLossMsgTargetMacAddr_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTargetMacAddr = _WwpLeosTceCfmFrameLossMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 3),
    _WwpLeosTceCfmFrameLossMsgTargetMacAddr_Type()
)
wwpLeosTceCfmFrameLossMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTargetMacAddr.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgCount_Type(Integer32):
    """Custom type wwpLeosTceCfmFrameLossMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_WwpLeosTceCfmFrameLossMsgCount_Type.__name__ = "Integer32"
_WwpLeosTceCfmFrameLossMsgCount_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgCount = _WwpLeosTceCfmFrameLossMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 4),
    _WwpLeosTceCfmFrameLossMsgCount_Type()
)
wwpLeosTceCfmFrameLossMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgCount.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgPriority_Type(Integer32):
    """Custom type wwpLeosTceCfmFrameLossMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmFrameLossMsgPriority_Type.__name__ = "Integer32"
_WwpLeosTceCfmFrameLossMsgPriority_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgPriority = _WwpLeosTceCfmFrameLossMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 5),
    _WwpLeosTceCfmFrameLossMsgPriority_Type()
)
wwpLeosTceCfmFrameLossMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgPriority.setStatus("current")
_WwpLeosTceCfmFrameLossMsgRowStatus_Type = RowStatus
_WwpLeosTceCfmFrameLossMsgRowStatus_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgRowStatus = _WwpLeosTceCfmFrameLossMsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 6),
    _WwpLeosTceCfmFrameLossMsgRowStatus_Type()
)
wwpLeosTceCfmFrameLossMsgRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgRowStatus.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgRepeatInterval_Type(Unsigned32):
    """Custom type wwpLeosTceCfmFrameLossMsgRepeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosTceCfmFrameLossMsgRepeatInterval_Type.__name__ = "Unsigned32"
_WwpLeosTceCfmFrameLossMsgRepeatInterval_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgRepeatInterval = _WwpLeosTceCfmFrameLossMsgRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 50),
    _WwpLeosTceCfmFrameLossMsgRepeatInterval_Type()
)
wwpLeosTceCfmFrameLossMsgRepeatInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgRepeatInterval.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgRepeatInterval.setUnits("minutes")


class _WwpLeosTceCfmFrameLossMsgNearLossThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmFrameLossMsgNearLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WwpLeosTceCfmFrameLossMsgNearLossThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmFrameLossMsgNearLossThreshold_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgNearLossThreshold = _WwpLeosTceCfmFrameLossMsgNearLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 51),
    _WwpLeosTceCfmFrameLossMsgNearLossThreshold_Type()
)
wwpLeosTceCfmFrameLossMsgNearLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgNearLossThreshold.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgFarLossThreshold_Type(Integer32):
    """Custom type wwpLeosTceCfmFrameLossMsgFarLossThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WwpLeosTceCfmFrameLossMsgFarLossThreshold_Type.__name__ = "Integer32"
_WwpLeosTceCfmFrameLossMsgFarLossThreshold_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgFarLossThreshold = _WwpLeosTceCfmFrameLossMsgFarLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 52),
    _WwpLeosTceCfmFrameLossMsgFarLossThreshold_Type()
)
wwpLeosTceCfmFrameLossMsgFarLossThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgFarLossThreshold.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgServiceName_Type(DisplayString):
    """Custom type wwpLeosTceCfmFrameLossMsgServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmFrameLossMsgServiceName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmFrameLossMsgServiceName_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgServiceName = _WwpLeosTceCfmFrameLossMsgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 53),
    _WwpLeosTceCfmFrameLossMsgServiceName_Type()
)
wwpLeosTceCfmFrameLossMsgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgServiceName.setStatus("current")


class _WwpLeosTceCfmFrameLossMsgSubPortName_Type(DisplayString):
    """Custom type wwpLeosTceCfmFrameLossMsgSubPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosTceCfmFrameLossMsgSubPortName_Type.__name__ = "DisplayString"
_WwpLeosTceCfmFrameLossMsgSubPortName_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgSubPortName = _WwpLeosTceCfmFrameLossMsgSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 54),
    _WwpLeosTceCfmFrameLossMsgSubPortName_Type()
)
wwpLeosTceCfmFrameLossMsgSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgSubPortName.setStatus("current")
_WwpLeosTceCfmFrameLossMsgFrameLossNear_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgFrameLossNear_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgFrameLossNear = _WwpLeosTceCfmFrameLossMsgFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 55),
    _WwpLeosTceCfmFrameLossMsgFrameLossNear_Type()
)
wwpLeosTceCfmFrameLossMsgFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgFrameLossNear.setStatus("current")
_WwpLeosTceCfmFrameLossMsgFrameLossFar_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgFrameLossFar_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgFrameLossFar = _WwpLeosTceCfmFrameLossMsgFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 56),
    _WwpLeosTceCfmFrameLossMsgFrameLossFar_Type()
)
wwpLeosTceCfmFrameLossMsgFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgFrameLossFar.setStatus("current")
_WwpLeosTceCfmFrameLossMsgTotalTxLmm_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgTotalTxLmm_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTotalTxLmm = _WwpLeosTceCfmFrameLossMsgTotalTxLmm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 57),
    _WwpLeosTceCfmFrameLossMsgTotalTxLmm_Type()
)
wwpLeosTceCfmFrameLossMsgTotalTxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTotalTxLmm.setStatus("current")
_WwpLeosTceCfmFrameLossMsgTotalRxLmm_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgTotalRxLmm_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTotalRxLmm = _WwpLeosTceCfmFrameLossMsgTotalRxLmm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 58),
    _WwpLeosTceCfmFrameLossMsgTotalRxLmm_Type()
)
wwpLeosTceCfmFrameLossMsgTotalRxLmm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTotalRxLmm.setStatus("current")
_WwpLeosTceCfmFrameLossMsgTotalTxLmr_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgTotalTxLmr_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTotalTxLmr = _WwpLeosTceCfmFrameLossMsgTotalTxLmr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 59),
    _WwpLeosTceCfmFrameLossMsgTotalTxLmr_Type()
)
wwpLeosTceCfmFrameLossMsgTotalTxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTotalTxLmr.setStatus("current")
_WwpLeosTceCfmFrameLossMsgTotalRxLmr_Type = Unsigned32
_WwpLeosTceCfmFrameLossMsgTotalRxLmr_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgTotalRxLmr = _WwpLeosTceCfmFrameLossMsgTotalRxLmr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 60),
    _WwpLeosTceCfmFrameLossMsgTotalRxLmr_Type()
)
wwpLeosTceCfmFrameLossMsgTotalRxLmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgTotalRxLmr.setStatus("current")
_WwpLeosTceCfmFrameLossMsgAction_Type = SendState
_WwpLeosTceCfmFrameLossMsgAction_Object = MibTableColumn
wwpLeosTceCfmFrameLossMsgAction = _WwpLeosTceCfmFrameLossMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 13, 1, 1, 61),
    _WwpLeosTceCfmFrameLossMsgAction_Type()
)
wwpLeosTceCfmFrameLossMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosTceCfmFrameLossMsgAction.setStatus("current")
_WwpLeosTceCfmMipCCMDb_ObjectIdentity = ObjectIdentity
wwpLeosTceCfmMipCCMDb = _WwpLeosTceCfmMipCCMDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14)
)
_WwpLeosTceCfmMipCCMDbTable_Object = MibTable
wwpLeosTceCfmMipCCMDbTable = _WwpLeosTceCfmMipCCMDbTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1)
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbTable.setStatus("current")
_WwpLeosTceCfmMipCCMDbEntry_Object = MibTableRow
wwpLeosTceCfmMipCCMDbEntry = _WwpLeosTceCfmMipCCMDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1)
)
wwpLeosTceCfmMipCCMDbEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosTceCfmMipCCMDbIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbEntry.setStatus("current")
_WwpLeosTceCfmMipCCMDbIndex_Type = Unsigned32
_WwpLeosTceCfmMipCCMDbIndex_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbIndex = _WwpLeosTceCfmMipCCMDbIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 1),
    _WwpLeosTceCfmMipCCMDbIndex_Type()
)
wwpLeosTceCfmMipCCMDbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbIndex.setStatus("current")
_WwpLeosTceCfmMipCCMDbMacAddr_Type = MacAddress
_WwpLeosTceCfmMipCCMDbMacAddr_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbMacAddr = _WwpLeosTceCfmMipCCMDbMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 2),
    _WwpLeosTceCfmMipCCMDbMacAddr_Type()
)
wwpLeosTceCfmMipCCMDbMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbMacAddr.setStatus("current")
_WwpLeosTceCfmMipCCMDbServiceName_Type = DisplayString
_WwpLeosTceCfmMipCCMDbServiceName_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbServiceName = _WwpLeosTceCfmMipCCMDbServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 3),
    _WwpLeosTceCfmMipCCMDbServiceName_Type()
)
wwpLeosTceCfmMipCCMDbServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbServiceName.setStatus("current")
_WwpLeosTceCfmMipCCMDbSubPortName_Type = DisplayString
_WwpLeosTceCfmMipCCMDbSubPortName_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbSubPortName = _WwpLeosTceCfmMipCCMDbSubPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 4),
    _WwpLeosTceCfmMipCCMDbSubPortName_Type()
)
wwpLeosTceCfmMipCCMDbSubPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbSubPortName.setStatus("current")
_WwpLeosTceCfmMipCCMdbNumCCMRx_Type = Counter32
_WwpLeosTceCfmMipCCMdbNumCCMRx_Object = MibTableColumn
wwpLeosTceCfmMipCCMdbNumCCMRx = _WwpLeosTceCfmMipCCMdbNumCCMRx_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 5),
    _WwpLeosTceCfmMipCCMdbNumCCMRx_Type()
)
wwpLeosTceCfmMipCCMdbNumCCMRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMdbNumCCMRx.setStatus("current")
_WwpLeosTceCfmMipCCMDbCCMRxTime_Type = Unsigned32
_WwpLeosTceCfmMipCCMDbCCMRxTime_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbCCMRxTime = _WwpLeosTceCfmMipCCMDbCCMRxTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 6),
    _WwpLeosTceCfmMipCCMDbCCMRxTime_Type()
)
wwpLeosTceCfmMipCCMDbCCMRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbCCMRxTime.setStatus("current")


class _WwpLeosTceCfmMipCCMDbLevel_Type(Integer32):
    """Custom type wwpLeosTceCfmMipCCMDbLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosTceCfmMipCCMDbLevel_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipCCMDbLevel_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbLevel = _WwpLeosTceCfmMipCCMDbLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 7),
    _WwpLeosTceCfmMipCCMDbLevel_Type()
)
wwpLeosTceCfmMipCCMDbLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbLevel.setStatus("current")


class _WwpLeosTceCfmMipCCMDbMEPID_Type(Integer32):
    """Custom type wwpLeosTceCfmMipCCMDbMEPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosTceCfmMipCCMDbMEPID_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipCCMDbMEPID_Object = MibTableColumn
wwpLeosTceCfmMipCCMDbMEPID = _WwpLeosTceCfmMipCCMDbMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 8),
    _WwpLeosTceCfmMipCCMDbMEPID_Type()
)
wwpLeosTceCfmMipCCMDbMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipCCMDbMEPID.setStatus("current")


class _WwpLeosTceCfmMipRDI_Type(Integer32):
    """Custom type wwpLeosTceCfmMipRDI based on Integer32"""
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


_WwpLeosTceCfmMipRDI_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipRDI_Object = MibTableColumn
wwpLeosTceCfmMipRDI = _WwpLeosTceCfmMipRDI_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 9),
    _WwpLeosTceCfmMipRDI_Type()
)
wwpLeosTceCfmMipRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipRDI.setStatus("current")


class _WwpLeosTceCfmMipLastPortStatus_Type(Integer32):
    """Custom type wwpLeosTceCfmMipLastPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("none", 99),
          ("up", 2))
    )


_WwpLeosTceCfmMipLastPortStatus_Type.__name__ = "Integer32"
_WwpLeosTceCfmMipLastPortStatus_Object = MibTableColumn
wwpLeosTceCfmMipLastPortStatus = _WwpLeosTceCfmMipLastPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 20, 14, 1, 1, 10),
    _WwpLeosTceCfmMipLastPortStatus_Type()
)
wwpLeosTceCfmMipLastPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosTceCfmMipLastPortStatus.setStatus("current")
_WwpLeosCfmExtMIBObj_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtMIBObj = _WwpLeosCfmExtMIBObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21)
)
_WwpLeosCfmExtLoopback_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtLoopback = _WwpLeosCfmExtLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3)
)
_WwpLeosCfmExtLoopbackMsgTable_Object = MibTable
wwpLeosCfmExtLoopbackMsgTable = _WwpLeosCfmExtLoopbackMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgTable.setStatus("current")
_WwpLeosCfmExtLoopbackMsgEntry_Object = MibTableRow
wwpLeosCfmExtLoopbackMsgEntry = _WwpLeosCfmExtLoopbackMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1)
)
wwpLeosCfmExtLoopbackMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtLoopbackMsgLocalMEPID"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgEntry.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgLocalMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmExtLoopbackMsgLocalMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtLoopbackMsgLocalMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtLoopbackMsgLocalMEPID_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgLocalMEPID = _WwpLeosCfmExtLoopbackMsgLocalMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 1),
    _WwpLeosCfmExtLoopbackMsgLocalMEPID_Type()
)
wwpLeosCfmExtLoopbackMsgLocalMEPID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgLocalMEPID.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmExtLoopbackMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtLoopbackMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtLoopbackMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgTargetMEPID = _WwpLeosCfmExtLoopbackMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 2),
    _WwpLeosCfmExtLoopbackMsgTargetMEPID_Type()
)
wwpLeosCfmExtLoopbackMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgTargetMEPID.setStatus("current")
_WwpLeosCfmExtLoopbackMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmExtLoopbackMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgTargetMacAddr = _WwpLeosCfmExtLoopbackMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 3),
    _WwpLeosCfmExtLoopbackMsgTargetMacAddr_Type()
)
wwpLeosCfmExtLoopbackMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmExtLoopbackMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_WwpLeosCfmExtLoopbackMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmExtLoopbackMsgCount_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgCount = _WwpLeosCfmExtLoopbackMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 4),
    _WwpLeosCfmExtLoopbackMsgCount_Type()
)
wwpLeosCfmExtLoopbackMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgCount.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgData_Type(DisplayString):
    """Custom type wwpLeosCfmExtLoopbackMsgData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 127),
    )


_WwpLeosCfmExtLoopbackMsgData_Type.__name__ = "DisplayString"
_WwpLeosCfmExtLoopbackMsgData_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgData = _WwpLeosCfmExtLoopbackMsgData_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 5),
    _WwpLeosCfmExtLoopbackMsgData_Type()
)
wwpLeosCfmExtLoopbackMsgData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgData.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtLoopbackMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtLoopbackMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtLoopbackMsgPriority_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgPriority = _WwpLeosCfmExtLoopbackMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 6),
    _WwpLeosCfmExtLoopbackMsgPriority_Type()
)
wwpLeosCfmExtLoopbackMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgPriority.setStatus("current")
_WwpLeosCfmExtLoopbackMsgAction_Type = SendState
_WwpLeosCfmExtLoopbackMsgAction_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgAction = _WwpLeosCfmExtLoopbackMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 7),
    _WwpLeosCfmExtLoopbackMsgAction_Type()
)
wwpLeosCfmExtLoopbackMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgAction.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgInterval_Type(Integer32):
    """Custom type wwpLeosCfmExtLoopbackMsgInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_WwpLeosCfmExtLoopbackMsgInterval_Type.__name__ = "Integer32"
_WwpLeosCfmExtLoopbackMsgInterval_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgInterval = _WwpLeosCfmExtLoopbackMsgInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 8),
    _WwpLeosCfmExtLoopbackMsgInterval_Type()
)
wwpLeosCfmExtLoopbackMsgInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgInterval.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgTimeout_Type(Integer32):
    """Custom type wwpLeosCfmExtLoopbackMsgTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10000),
    )


_WwpLeosCfmExtLoopbackMsgTimeout_Type.__name__ = "Integer32"
_WwpLeosCfmExtLoopbackMsgTimeout_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgTimeout = _WwpLeosCfmExtLoopbackMsgTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 9),
    _WwpLeosCfmExtLoopbackMsgTimeout_Type()
)
wwpLeosCfmExtLoopbackMsgTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgTimeout.setStatus("current")


class _WwpLeosCfmExtLoopbackMsgLoss_Type(Integer32):
    """Custom type wwpLeosCfmExtLoopbackMsgLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3000),
    )


_WwpLeosCfmExtLoopbackMsgLoss_Type.__name__ = "Integer32"
_WwpLeosCfmExtLoopbackMsgLoss_Object = MibTableColumn
wwpLeosCfmExtLoopbackMsgLoss = _WwpLeosCfmExtLoopbackMsgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 3, 1, 1, 10),
    _WwpLeosCfmExtLoopbackMsgLoss_Type()
)
wwpLeosCfmExtLoopbackMsgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLoopbackMsgLoss.setStatus("current")
_WwpLeosCfmExtMEP_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtMEP = _WwpLeosCfmExtMEP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7)
)
_WwpLeosCfmExtMEPTable_Object = MibTable
wwpLeosCfmExtMEPTable = _WwpLeosCfmExtMEPTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPTable.setStatus("current")
_WwpLeosCfmExtMEPEntry_Object = MibTableRow
wwpLeosCfmExtMEPEntry = _WwpLeosCfmExtMEPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1)
)
wwpLeosCfmExtMEPEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPEntry.setStatus("current")


class _WwpLeosCfmExtMEPId_Type(Unsigned32):
    """Custom type wwpLeosCfmExtMEPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtMEPId_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtMEPId_Object = MibTableColumn
wwpLeosCfmExtMEPId = _WwpLeosCfmExtMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 1),
    _WwpLeosCfmExtMEPId_Type()
)
wwpLeosCfmExtMEPId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPId.setStatus("current")


class _WwpLeosCfmExtPortId_Type(Integer32):
    """Custom type wwpLeosCfmExtPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtPortId_Type.__name__ = "Integer32"
_WwpLeosCfmExtPortId_Object = MibTableColumn
wwpLeosCfmExtPortId = _WwpLeosCfmExtPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 2),
    _WwpLeosCfmExtPortId_Type()
)
wwpLeosCfmExtPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtPortId.setStatus("current")


class _WwpLeosCfmExtVlanId_Type(Integer32):
    """Custom type wwpLeosCfmExtVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosCfmExtVlanId_Type.__name__ = "Integer32"
_WwpLeosCfmExtVlanId_Object = MibTableColumn
wwpLeosCfmExtVlanId = _WwpLeosCfmExtVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 3),
    _WwpLeosCfmExtVlanId_Type()
)
wwpLeosCfmExtVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtVlanId.setStatus("current")


class _WwpLeosCfmExtMEPAdminState_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmExtMEPAdminState_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPAdminState_Object = MibTableColumn
wwpLeosCfmExtMEPAdminState = _WwpLeosCfmExtMEPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 4),
    _WwpLeosCfmExtMEPAdminState_Type()
)
wwpLeosCfmExtMEPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPAdminState.setStatus("current")


class _WwpLeosCfmExtMEPOperState_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosCfmExtMEPOperState_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPOperState_Object = MibTableColumn
wwpLeosCfmExtMEPOperState = _WwpLeosCfmExtMEPOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 5),
    _WwpLeosCfmExtMEPOperState_Type()
)
wwpLeosCfmExtMEPOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPOperState.setStatus("current")


class _WwpLeosCfmExtMEPDirection_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDirection based on Integer32"""
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


_WwpLeosCfmExtMEPDirection_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDirection_Object = MibTableColumn
wwpLeosCfmExtMEPDirection = _WwpLeosCfmExtMEPDirection_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 6),
    _WwpLeosCfmExtMEPDirection_Type()
)
wwpLeosCfmExtMEPDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDirection.setStatus("current")


class _WwpLeosCfmExtMEPCCMState_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPCCMState based on Integer32"""
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


_WwpLeosCfmExtMEPCCMState_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPCCMState_Object = MibTableColumn
wwpLeosCfmExtMEPCCMState = _WwpLeosCfmExtMEPCCMState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 7),
    _WwpLeosCfmExtMEPCCMState_Type()
)
wwpLeosCfmExtMEPCCMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPCCMState.setStatus("current")


class _WwpLeosCfmExtMEPCCMPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPCCMPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMEPCCMPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPCCMPriority_Object = MibTableColumn
wwpLeosCfmExtMEPCCMPriority = _WwpLeosCfmExtMEPCCMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 8),
    _WwpLeosCfmExtMEPCCMPriority_Type()
)
wwpLeosCfmExtMEPCCMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPCCMPriority.setStatus("current")


class _WwpLeosCfmExtMEPLTMPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPLTMPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMEPLTMPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPLTMPriority_Object = MibTableColumn
wwpLeosCfmExtMEPLTMPriority = _WwpLeosCfmExtMEPLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 9),
    _WwpLeosCfmExtMEPLTMPriority_Type()
)
wwpLeosCfmExtMEPLTMPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLTMPriority.setStatus("current")
_WwpLeosCfmExtMEPMacAddr_Type = MacAddress
_WwpLeosCfmExtMEPMacAddr_Object = MibTableColumn
wwpLeosCfmExtMEPMacAddr = _WwpLeosCfmExtMEPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 10),
    _WwpLeosCfmExtMEPMacAddr_Type()
)
wwpLeosCfmExtMEPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPMacAddr.setStatus("current")
_WwpLeosCfmExtMEPNextLbmSeqNumber_Type = Counter32
_WwpLeosCfmExtMEPNextLbmSeqNumber_Object = MibTableColumn
wwpLeosCfmExtMEPNextLbmSeqNumber = _WwpLeosCfmExtMEPNextLbmSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 11),
    _WwpLeosCfmExtMEPNextLbmSeqNumber_Type()
)
wwpLeosCfmExtMEPNextLbmSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPNextLbmSeqNumber.setStatus("current")
_WwpLeosCfmExtMEPNextLTMSeqNumber_Type = Counter32
_WwpLeosCfmExtMEPNextLTMSeqNumber_Object = MibTableColumn
wwpLeosCfmExtMEPNextLTMSeqNumber = _WwpLeosCfmExtMEPNextLTMSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 12),
    _WwpLeosCfmExtMEPNextLTMSeqNumber_Type()
)
wwpLeosCfmExtMEPNextLTMSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPNextLTMSeqNumber.setStatus("current")
_WwpLeosCfmExtMEPRowStatus_Type = RowStatus
_WwpLeosCfmExtMEPRowStatus_Object = MibTableColumn
wwpLeosCfmExtMEPRowStatus = _WwpLeosCfmExtMEPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 13),
    _WwpLeosCfmExtMEPRowStatus_Type()
)
wwpLeosCfmExtMEPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPRowStatus.setStatus("current")
_WwpLeosCfmExtMEPDMMDelay_Type = Counter32
_WwpLeosCfmExtMEPDMMDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDMMDelay = _WwpLeosCfmExtMEPDMMDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 14),
    _WwpLeosCfmExtMEPDMMDelay_Type()
)
wwpLeosCfmExtMEPDMMDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMDelay.setStatus("current")
_WwpLeosCfmExtMEPDMMJitter_Type = Counter32
_WwpLeosCfmExtMEPDMMJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDMMJitter = _WwpLeosCfmExtMEPDMMJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 15),
    _WwpLeosCfmExtMEPDMMJitter_Type()
)
wwpLeosCfmExtMEPDMMJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMJitter.setStatus("current")
_WwpLeosCfmExtMEPLMMFrameLossNear_Type = Counter32
_WwpLeosCfmExtMEPLMMFrameLossNear_Object = MibTableColumn
wwpLeosCfmExtMEPLMMFrameLossNear = _WwpLeosCfmExtMEPLMMFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 16),
    _WwpLeosCfmExtMEPLMMFrameLossNear_Type()
)
wwpLeosCfmExtMEPLMMFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLMMFrameLossNear.setStatus("current")
_WwpLeosCfmExtMEPLMMFrameLossFar_Type = Counter32
_WwpLeosCfmExtMEPLMMFrameLossFar_Object = MibTableColumn
wwpLeosCfmExtMEPLMMFrameLossFar = _WwpLeosCfmExtMEPLMMFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 17),
    _WwpLeosCfmExtMEPLMMFrameLossFar_Type()
)
wwpLeosCfmExtMEPLMMFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLMMFrameLossFar.setStatus("current")


class _WwpLeosCfmExtMEPServiceName_Type(DisplayString):
    """Custom type wwpLeosCfmExtMEPServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmExtMEPServiceName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtMEPServiceName_Object = MibTableColumn
wwpLeosCfmExtMEPServiceName = _WwpLeosCfmExtMEPServiceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 50),
    _WwpLeosCfmExtMEPServiceName_Type()
)
wwpLeosCfmExtMEPServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPServiceName.setStatus("current")


class _WwpLeosCfmExtMEPInterfaceName_Type(DisplayString):
    """Custom type wwpLeosCfmExtMEPInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmExtMEPInterfaceName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtMEPInterfaceName_Object = MibTableColumn
wwpLeosCfmExtMEPInterfaceName = _WwpLeosCfmExtMEPInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 51),
    _WwpLeosCfmExtMEPInterfaceName_Type()
)
wwpLeosCfmExtMEPInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPInterfaceName.setStatus("current")


class _WwpLeosCfmExtMEPServiceInstanceName_Type(DisplayString):
    """Custom type wwpLeosCfmExtMEPServiceInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmExtMEPServiceInstanceName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtMEPServiceInstanceName_Object = MibTableColumn
wwpLeosCfmExtMEPServiceInstanceName = _WwpLeosCfmExtMEPServiceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 52),
    _WwpLeosCfmExtMEPServiceInstanceName_Type()
)
wwpLeosCfmExtMEPServiceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPServiceInstanceName.setStatus("current")


class _WwpLeosCfmExtMEPLogicalPortName_Type(DisplayString):
    """Custom type wwpLeosCfmExtMEPLogicalPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_WwpLeosCfmExtMEPLogicalPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtMEPLogicalPortName_Object = MibTableColumn
wwpLeosCfmExtMEPLogicalPortName = _WwpLeosCfmExtMEPLogicalPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 53),
    _WwpLeosCfmExtMEPLogicalPortName_Type()
)
wwpLeosCfmExtMEPLogicalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLogicalPortName.setStatus("current")


class _WwpLeosCfmExtMEPTagMode_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPTagMode based on Integer32"""
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


_WwpLeosCfmExtMEPTagMode_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPTagMode_Object = MibTableColumn
wwpLeosCfmExtMEPTagMode = _WwpLeosCfmExtMEPTagMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 54),
    _WwpLeosCfmExtMEPTagMode_Type()
)
wwpLeosCfmExtMEPTagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPTagMode.setStatus("current")


class _WwpLeosCfmExtMEPTagVID_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPTagVID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_WwpLeosCfmExtMEPTagVID_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPTagVID_Object = MibTableColumn
wwpLeosCfmExtMEPTagVID = _WwpLeosCfmExtMEPTagVID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 55),
    _WwpLeosCfmExtMEPTagVID_Type()
)
wwpLeosCfmExtMEPTagVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPTagVID.setStatus("current")


class _WwpLeosCfmExtMEPTagPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPTagPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMEPTagPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPTagPriority_Object = MibTableColumn
wwpLeosCfmExtMEPTagPriority = _WwpLeosCfmExtMEPTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 56),
    _WwpLeosCfmExtMEPTagPriority_Type()
)
wwpLeosCfmExtMEPTagPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPTagPriority.setStatus("current")
_WwpLeosCfmExtMEPLMMBadSequence_Type = Counter32
_WwpLeosCfmExtMEPLMMBadSequence_Object = MibTableColumn
wwpLeosCfmExtMEPLMMBadSequence = _WwpLeosCfmExtMEPLMMBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 57),
    _WwpLeosCfmExtMEPLMMBadSequence_Type()
)
wwpLeosCfmExtMEPLMMBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLMMBadSequence.setStatus("current")


class _WwpLeosCfmExtMEPCCMComment_Type(DisplayString):
    """Custom type wwpLeosCfmExtMEPCCMComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosCfmExtMEPCCMComment_Type.__name__ = "DisplayString"
_WwpLeosCfmExtMEPCCMComment_Object = MibTableColumn
wwpLeosCfmExtMEPCCMComment = _WwpLeosCfmExtMEPCCMComment_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 58),
    _WwpLeosCfmExtMEPCCMComment_Type()
)
wwpLeosCfmExtMEPCCMComment.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPCCMComment.setStatus("current")
_WwpLeosCfmExtMEPLMMMissingSequence_Type = Counter32
_WwpLeosCfmExtMEPLMMMissingSequence_Object = MibTableColumn
wwpLeosCfmExtMEPLMMMissingSequence = _WwpLeosCfmExtMEPLMMMissingSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 59),
    _WwpLeosCfmExtMEPLMMMissingSequence_Type()
)
wwpLeosCfmExtMEPLMMMissingSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLMMMissingSequence.setStatus("current")
_WwpLeosCfmExtMEPBlockOppositeFaultCurrent_Type = Counter32
_WwpLeosCfmExtMEPBlockOppositeFaultCurrent_Object = MibTableColumn
wwpLeosCfmExtMEPBlockOppositeFaultCurrent = _WwpLeosCfmExtMEPBlockOppositeFaultCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 60),
    _WwpLeosCfmExtMEPBlockOppositeFaultCurrent_Type()
)
wwpLeosCfmExtMEPBlockOppositeFaultCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPBlockOppositeFaultCurrent.setStatus("current")
_WwpLeosCfmExtMEPBlockOppositeFaultThreshold_Type = Unsigned32
_WwpLeosCfmExtMEPBlockOppositeFaultThreshold_Object = MibTableColumn
wwpLeosCfmExtMEPBlockOppositeFaultThreshold = _WwpLeosCfmExtMEPBlockOppositeFaultThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 61),
    _WwpLeosCfmExtMEPBlockOppositeFaultThreshold_Type()
)
wwpLeosCfmExtMEPBlockOppositeFaultThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPBlockOppositeFaultThreshold.setStatus("current")


class _WwpLeosCfmExtMEPBlockOppositeFaultTime_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPBlockOppositeFaultTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_WwpLeosCfmExtMEPBlockOppositeFaultTime_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPBlockOppositeFaultTime_Object = MibTableColumn
wwpLeosCfmExtMEPBlockOppositeFaultTime = _WwpLeosCfmExtMEPBlockOppositeFaultTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 62),
    _WwpLeosCfmExtMEPBlockOppositeFaultTime_Type()
)
wwpLeosCfmExtMEPBlockOppositeFaultTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPBlockOppositeFaultTime.setStatus("current")
_WwpLeosCfmExtMEPDMMMinDelay_Type = Counter32
_WwpLeosCfmExtMEPDMMMinDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDMMMinDelay = _WwpLeosCfmExtMEPDMMMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 63),
    _WwpLeosCfmExtMEPDMMMinDelay_Type()
)
wwpLeosCfmExtMEPDMMMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMMinDelay.setStatus("current")
_WwpLeosCfmExtMEPDMMMaxDelay_Type = Counter32
_WwpLeosCfmExtMEPDMMMaxDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDMMMaxDelay = _WwpLeosCfmExtMEPDMMMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 64),
    _WwpLeosCfmExtMEPDMMMaxDelay_Type()
)
wwpLeosCfmExtMEPDMMMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMMaxDelay.setStatus("current")
_WwpLeosCfmExtMEPDMMMinJitter_Type = Counter32
_WwpLeosCfmExtMEPDMMMinJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDMMMinJitter = _WwpLeosCfmExtMEPDMMMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 65),
    _WwpLeosCfmExtMEPDMMMinJitter_Type()
)
wwpLeosCfmExtMEPDMMMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMMinJitter.setStatus("current")
_WwpLeosCfmExtMEPDMMMaxJitter_Type = Counter32
_WwpLeosCfmExtMEPDMMMaxJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDMMMaxJitter = _WwpLeosCfmExtMEPDMMMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 66),
    _WwpLeosCfmExtMEPDMMMaxJitter_Type()
)
wwpLeosCfmExtMEPDMMMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDMMMaxJitter.setStatus("current")
_WwpLeosCfmExtMEPAccelerated_Type = TruthValue
_WwpLeosCfmExtMEPAccelerated_Object = MibTableColumn
wwpLeosCfmExtMEPAccelerated = _WwpLeosCfmExtMEPAccelerated_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 1, 1, 67),
    _WwpLeosCfmExtMEPAccelerated_Type()
)
wwpLeosCfmExtMEPAccelerated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPAccelerated.setStatus("current")
_WwpLeosCfmExtMEPStatsTable_Object = MibTable
wwpLeosCfmExtMEPStatsTable = _WwpLeosCfmExtMEPStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsTable.setStatus("current")
_WwpLeosCfmExtMEPStatsEntry_Object = MibTableRow
wwpLeosCfmExtMEPStatsEntry = _WwpLeosCfmExtMEPStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1)
)
wwpLeosCfmExtMEPStatsEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsEntry.setStatus("current")
_WwpLeosCfmExtMEPStatsTotalValidFramesReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsTotalValidFramesReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsTotalValidFramesReceived = _WwpLeosCfmExtMEPStatsTotalValidFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 1),
    _WwpLeosCfmExtMEPStatsTotalValidFramesReceived_Type()
)
wwpLeosCfmExtMEPStatsTotalValidFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsTotalValidFramesReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsTotalInvalidFramesReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsTotalInvalidFramesReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsTotalInvalidFramesReceived = _WwpLeosCfmExtMEPStatsTotalInvalidFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 2),
    _WwpLeosCfmExtMEPStatsTotalInvalidFramesReceived_Type()
)
wwpLeosCfmExtMEPStatsTotalInvalidFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsTotalInvalidFramesReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived = _WwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 3),
    _WwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived_Type()
)
wwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived = _WwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 4),
    _WwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived = _WwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 5),
    _WwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived = _WwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 6),
    _WwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsCCMTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsCCMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsCCMTxmt = _WwpLeosCfmExtMEPStatsCCMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 7),
    _WwpLeosCfmExtMEPStatsCCMTxmt_Type()
)
wwpLeosCfmExtMEPStatsCCMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsCCMTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsValidCCMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsValidCCMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsValidCCMReceived = _WwpLeosCfmExtMEPStatsValidCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 8),
    _WwpLeosCfmExtMEPStatsValidCCMReceived_Type()
)
wwpLeosCfmExtMEPStatsValidCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsValidCCMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsCCMInSequenceReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsCCMInSequenceReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsCCMInSequenceReceived = _WwpLeosCfmExtMEPStatsCCMInSequenceReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 9),
    _WwpLeosCfmExtMEPStatsCCMInSequenceReceived_Type()
)
wwpLeosCfmExtMEPStatsCCMInSequenceReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsCCMInSequenceReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived = _WwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 10),
    _WwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived_Type()
)
wwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsMDLevelXconCCMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsMDLevelXconCCMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsMDLevelXconCCMReceived = _WwpLeosCfmExtMEPStatsMDLevelXconCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 11),
    _WwpLeosCfmExtMEPStatsMDLevelXconCCMReceived_Type()
)
wwpLeosCfmExtMEPStatsMDLevelXconCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsMDLevelXconCCMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsMAIDXconCCMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsMAIDXconCCMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsMAIDXconCCMReceived = _WwpLeosCfmExtMEPStatsMAIDXconCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 12),
    _WwpLeosCfmExtMEPStatsMAIDXconCCMReceived_Type()
)
wwpLeosCfmExtMEPStatsMAIDXconCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsMAIDXconCCMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsIntervalErrorCCMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsIntervalErrorCCMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsIntervalErrorCCMReceived = _WwpLeosCfmExtMEPStatsIntervalErrorCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 13),
    _WwpLeosCfmExtMEPStatsIntervalErrorCCMReceived_Type()
)
wwpLeosCfmExtMEPStatsIntervalErrorCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsIntervalErrorCCMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsRxInvalidCCM_Type = Counter64
_WwpLeosCfmExtMEPStatsRxInvalidCCM_Object = MibTableColumn
wwpLeosCfmExtMEPStatsRxInvalidCCM = _WwpLeosCfmExtMEPStatsRxInvalidCCM_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 14),
    _WwpLeosCfmExtMEPStatsRxInvalidCCM_Type()
)
wwpLeosCfmExtMEPStatsRxInvalidCCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsRxInvalidCCM.setStatus("current")
_WwpLeosCfmExtMEPStatsLBMTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLBMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLBMTxmt = _WwpLeosCfmExtMEPStatsLBMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 15),
    _WwpLeosCfmExtMEPStatsLBMTxmt_Type()
)
wwpLeosCfmExtMEPStatsLBMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLBMTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsLBRTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLBRTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLBRTxmt = _WwpLeosCfmExtMEPStatsLBRTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 16),
    _WwpLeosCfmExtMEPStatsLBRTxmt_Type()
)
wwpLeosCfmExtMEPStatsLBRTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLBRTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsInOrderLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInOrderLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInOrderLBRReceived = _WwpLeosCfmExtMEPStatsInOrderLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 17),
    _WwpLeosCfmExtMEPStatsInOrderLBRReceived_Type()
)
wwpLeosCfmExtMEPStatsInOrderLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInOrderLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsOutOfOrderLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsOutOfOrderLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsOutOfOrderLBRReceived = _WwpLeosCfmExtMEPStatsOutOfOrderLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 18),
    _WwpLeosCfmExtMEPStatsOutOfOrderLBRReceived_Type()
)
wwpLeosCfmExtMEPStatsOutOfOrderLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsOutOfOrderLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsContentMismatchLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsContentMismatchLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsContentMismatchLBRReceived = _WwpLeosCfmExtMEPStatsContentMismatchLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 19),
    _WwpLeosCfmExtMEPStatsContentMismatchLBRReceived_Type()
)
wwpLeosCfmExtMEPStatsContentMismatchLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsContentMismatchLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsUnexpectedLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsUnexpectedLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsUnexpectedLBRReceived = _WwpLeosCfmExtMEPStatsUnexpectedLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 20),
    _WwpLeosCfmExtMEPStatsUnexpectedLBRReceived_Type()
)
wwpLeosCfmExtMEPStatsUnexpectedLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsUnexpectedLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidLBRReceived = _WwpLeosCfmExtMEPStatsInvalidLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 21),
    _WwpLeosCfmExtMEPStatsInvalidLBRReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsLTMTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLTMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLTMTxmt = _WwpLeosCfmExtMEPStatsLTMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 22),
    _WwpLeosCfmExtMEPStatsLTMTxmt_Type()
)
wwpLeosCfmExtMEPStatsLTMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLTMTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsValidLTMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsValidLTMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsValidLTMReceived = _WwpLeosCfmExtMEPStatsValidLTMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 23),
    _WwpLeosCfmExtMEPStatsValidLTMReceived_Type()
)
wwpLeosCfmExtMEPStatsValidLTMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsValidLTMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsTotalInvalidLTMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsTotalInvalidLTMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsTotalInvalidLTMReceived = _WwpLeosCfmExtMEPStatsTotalInvalidLTMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 24),
    _WwpLeosCfmExtMEPStatsTotalInvalidLTMReceived_Type()
)
wwpLeosCfmExtMEPStatsTotalInvalidLTMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsTotalInvalidLTMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidLTRAction_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidLTRAction_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidLTRAction = _WwpLeosCfmExtMEPStatsInvalidLTRAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 25),
    _WwpLeosCfmExtMEPStatsInvalidLTRAction_Type()
)
wwpLeosCfmExtMEPStatsInvalidLTRAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidLTRAction.setStatus("current")
_WwpLeosCfmExtMEPStatsLTRTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLTRTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLTRTxmt = _WwpLeosCfmExtMEPStatsLTRTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 26),
    _WwpLeosCfmExtMEPStatsLTRTxmt_Type()
)
wwpLeosCfmExtMEPStatsLTRTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLTRTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsLTRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsLTRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLTRReceived = _WwpLeosCfmExtMEPStatsLTRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 27),
    _WwpLeosCfmExtMEPStatsLTRReceived_Type()
)
wwpLeosCfmExtMEPStatsLTRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLTRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsDMMTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsDMMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsDMMTxmt = _WwpLeosCfmExtMEPStatsDMMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 28),
    _WwpLeosCfmExtMEPStatsDMMTxmt_Type()
)
wwpLeosCfmExtMEPStatsDMMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsDMMTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsDMMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsDMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsDMMReceived = _WwpLeosCfmExtMEPStatsDMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 29),
    _WwpLeosCfmExtMEPStatsDMMReceived_Type()
)
wwpLeosCfmExtMEPStatsDMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsDMMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsDMRTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsDMRTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsDMRTxmt = _WwpLeosCfmExtMEPStatsDMRTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 30),
    _WwpLeosCfmExtMEPStatsDMRTxmt_Type()
)
wwpLeosCfmExtMEPStatsDMRTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsDMRTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsDMRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsDMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsDMRReceived = _WwpLeosCfmExtMEPStatsDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 31),
    _WwpLeosCfmExtMEPStatsDMRReceived_Type()
)
wwpLeosCfmExtMEPStatsDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsDMRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsDMReplyTimeout_Type = Counter64
_WwpLeosCfmExtMEPStatsDMReplyTimeout_Object = MibTableColumn
wwpLeosCfmExtMEPStatsDMReplyTimeout = _WwpLeosCfmExtMEPStatsDMReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 32),
    _WwpLeosCfmExtMEPStatsDMReplyTimeout_Type()
)
wwpLeosCfmExtMEPStatsDMReplyTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsDMReplyTimeout.setStatus("current")
_WwpLeosCfmExtMEPStatsLMMTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLMMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLMMTxmt = _WwpLeosCfmExtMEPStatsLMMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 33),
    _WwpLeosCfmExtMEPStatsLMMTxmt_Type()
)
wwpLeosCfmExtMEPStatsLMMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLMMTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsLMMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsLMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLMMReceived = _WwpLeosCfmExtMEPStatsLMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 34),
    _WwpLeosCfmExtMEPStatsLMMReceived_Type()
)
wwpLeosCfmExtMEPStatsLMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLMMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsLMRTxmt_Type = Counter64
_WwpLeosCfmExtMEPStatsLMRTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLMRTxmt = _WwpLeosCfmExtMEPStatsLMRTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 35),
    _WwpLeosCfmExtMEPStatsLMRTxmt_Type()
)
wwpLeosCfmExtMEPStatsLMRTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLMRTxmt.setStatus("current")
_WwpLeosCfmExtMEPStatsLMRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsLMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLMRReceived = _WwpLeosCfmExtMEPStatsLMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 36),
    _WwpLeosCfmExtMEPStatsLMRReceived_Type()
)
wwpLeosCfmExtMEPStatsLMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLMRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsLMRTimeout_Type = Counter64
_WwpLeosCfmExtMEPStatsLMRTimeout_Object = MibTableColumn
wwpLeosCfmExtMEPStatsLMRTimeout = _WwpLeosCfmExtMEPStatsLMRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 37),
    _WwpLeosCfmExtMEPStatsLMRTimeout_Type()
)
wwpLeosCfmExtMEPStatsLMRTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsLMRTimeout.setStatus("current")
_WwpLeosCfmExtMEPStatsMepIdErrorCCMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsMepIdErrorCCMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsMepIdErrorCCMReceived = _WwpLeosCfmExtMEPStatsMepIdErrorCCMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 38),
    _WwpLeosCfmExtMEPStatsMepIdErrorCCMReceived_Type()
)
wwpLeosCfmExtMEPStatsMepIdErrorCCMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsMepIdErrorCCMReceived.setStatus("current")


class _WwpLeosCfmExtMEPStatsClear_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPStatsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmExtMEPStatsClear_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPStatsClear_Object = MibTableColumn
wwpLeosCfmExtMEPStatsClear = _WwpLeosCfmExtMEPStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 40),
    _WwpLeosCfmExtMEPStatsClear_Type()
)
wwpLeosCfmExtMEPStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsClear.setStatus("current")
_WwpLeosCfmExtMEPStatsValidLBMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsValidLBMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsValidLBMReceived = _WwpLeosCfmExtMEPStatsValidLBMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 41),
    _WwpLeosCfmExtMEPStatsValidLBMReceived_Type()
)
wwpLeosCfmExtMEPStatsValidLBMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsValidLBMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidLBMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidLBMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidLBMReceived = _WwpLeosCfmExtMEPStatsInvalidLBMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 42),
    _WwpLeosCfmExtMEPStatsInvalidLBMReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidLBMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidLBMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsUnexpectedLTRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsUnexpectedLTRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsUnexpectedLTRReceived = _WwpLeosCfmExtMEPStatsUnexpectedLTRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 43),
    _WwpLeosCfmExtMEPStatsUnexpectedLTRReceived_Type()
)
wwpLeosCfmExtMEPStatsUnexpectedLTRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsUnexpectedLTRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidDMMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidDMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidDMMReceived = _WwpLeosCfmExtMEPStatsInvalidDMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 44),
    _WwpLeosCfmExtMEPStatsInvalidDMMReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidDMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidDMMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidDMRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidDMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidDMRReceived = _WwpLeosCfmExtMEPStatsInvalidDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 45),
    _WwpLeosCfmExtMEPStatsInvalidDMRReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidDMRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsUnexpectedDMRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsUnexpectedDMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsUnexpectedDMRReceived = _WwpLeosCfmExtMEPStatsUnexpectedDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 46),
    _WwpLeosCfmExtMEPStatsUnexpectedDMRReceived_Type()
)
wwpLeosCfmExtMEPStatsUnexpectedDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsUnexpectedDMRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidLMMReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidLMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidLMMReceived = _WwpLeosCfmExtMEPStatsInvalidLMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 47),
    _WwpLeosCfmExtMEPStatsInvalidLMMReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidLMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidLMMReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidLMRReceived_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidLMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidLMRReceived = _WwpLeosCfmExtMEPStatsInvalidLMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 48),
    _WwpLeosCfmExtMEPStatsInvalidLMRReceived_Type()
)
wwpLeosCfmExtMEPStatsInvalidLMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidLMRReceived.setStatus("current")
_WwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep_Type = Counter64
_WwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep_Object = MibTableColumn
wwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep = _WwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 2, 1, 49),
    _WwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep_Type()
)
wwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep.setStatus("current")
_WwpLeosCfmExtMEPLastStatsTable_Object = MibTable
wwpLeosCfmExtMEPLastStatsTable = _WwpLeosCfmExtMEPLastStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsTable.setStatus("current")
_WwpLeosCfmExtMEPLastStatsEntry_Object = MibTableRow
wwpLeosCfmExtMEPLastStatsEntry = _WwpLeosCfmExtMEPLastStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1)
)
wwpLeosCfmExtMEPLastStatsEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsEntry.setStatus("current")
_WwpLeosCfmExtMEPLastStatsPriority_Type = Counter64
_WwpLeosCfmExtMEPLastStatsPriority_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsPriority = _WwpLeosCfmExtMEPLastStatsPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 1),
    _WwpLeosCfmExtMEPLastStatsPriority_Type()
)
wwpLeosCfmExtMEPLastStatsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsPriority.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLBMCount_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLBMCount_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLBMCount = _WwpLeosCfmExtMEPLastStatsLBMCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 2),
    _WwpLeosCfmExtMEPLastStatsLBMCount_Type()
)
wwpLeosCfmExtMEPLastStatsLBMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLBMCount.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLBMSent_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLBMSent_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLBMSent = _WwpLeosCfmExtMEPLastStatsLBMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 3),
    _WwpLeosCfmExtMEPLastStatsLBMSent_Type()
)
wwpLeosCfmExtMEPLastStatsLBMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLBMSent.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLBMToSend_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLBMToSend_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLBMToSend = _WwpLeosCfmExtMEPLastStatsLBMToSend_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 4),
    _WwpLeosCfmExtMEPLastStatsLBMToSend_Type()
)
wwpLeosCfmExtMEPLastStatsLBMToSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLBMToSend.setStatus("current")
_WwpLeosCfmExtMEPLastStatsInOrderLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPLastStatsInOrderLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsInOrderLBRReceived = _WwpLeosCfmExtMEPLastStatsInOrderLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 5),
    _WwpLeosCfmExtMEPLastStatsInOrderLBRReceived_Type()
)
wwpLeosCfmExtMEPLastStatsInOrderLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsInOrderLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived_Type = Counter64
_WwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived = _WwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 6),
    _WwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived_Type()
)
wwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMPriority_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMPriority_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMPriority = _WwpLeosCfmExtMEPLastStatsDMMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 7),
    _WwpLeosCfmExtMEPLastStatsDMMPriority_Type()
)
wwpLeosCfmExtMEPLastStatsDMMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMPriority.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMTxmt_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMTxmt_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMTxmt = _WwpLeosCfmExtMEPLastStatsDMMTxmt_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 8),
    _WwpLeosCfmExtMEPLastStatsDMMTxmt_Type()
)
wwpLeosCfmExtMEPLastStatsDMMTxmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMTxmt.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMReceived_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMReceived = _WwpLeosCfmExtMEPLastStatsDMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 9),
    _WwpLeosCfmExtMEPLastStatsDMMReceived_Type()
)
wwpLeosCfmExtMEPLastStatsDMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMReceived.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMDelay_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMDelay_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMDelay = _WwpLeosCfmExtMEPLastStatsDMMDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 10),
    _WwpLeosCfmExtMEPLastStatsDMMDelay_Type()
)
wwpLeosCfmExtMEPLastStatsDMMDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMDelay.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMJitter_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMJitter_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMJitter = _WwpLeosCfmExtMEPLastStatsDMMJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 11),
    _WwpLeosCfmExtMEPLastStatsDMMJitter_Type()
)
wwpLeosCfmExtMEPLastStatsDMMJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMJitter.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLMMPriority_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLMMPriority_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLMMPriority = _WwpLeosCfmExtMEPLastStatsLMMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 12),
    _WwpLeosCfmExtMEPLastStatsLMMPriority_Type()
)
wwpLeosCfmExtMEPLastStatsLMMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLMMPriority.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLMMTxtm_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLMMTxtm_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLMMTxtm = _WwpLeosCfmExtMEPLastStatsLMMTxtm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 13),
    _WwpLeosCfmExtMEPLastStatsLMMTxtm_Type()
)
wwpLeosCfmExtMEPLastStatsLMMTxtm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLMMTxtm.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLMMReceived_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLMMReceived_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLMMReceived = _WwpLeosCfmExtMEPLastStatsLMMReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 14),
    _WwpLeosCfmExtMEPLastStatsLMMReceived_Type()
)
wwpLeosCfmExtMEPLastStatsLMMReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLMMReceived.setStatus("current")
_WwpLeosCfmExtMEPLastStatsFrameLossNear_Type = Counter64
_WwpLeosCfmExtMEPLastStatsFrameLossNear_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsFrameLossNear = _WwpLeosCfmExtMEPLastStatsFrameLossNear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 15),
    _WwpLeosCfmExtMEPLastStatsFrameLossNear_Type()
)
wwpLeosCfmExtMEPLastStatsFrameLossNear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsFrameLossNear.setStatus("current")
_WwpLeosCfmExtMEPLastStatsFrameLossFar_Type = Counter64
_WwpLeosCfmExtMEPLastStatsFrameLossFar_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsFrameLossFar = _WwpLeosCfmExtMEPLastStatsFrameLossFar_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 16),
    _WwpLeosCfmExtMEPLastStatsFrameLossFar_Type()
)
wwpLeosCfmExtMEPLastStatsFrameLossFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsFrameLossFar.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLTMPriority_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLTMPriority_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLTMPriority = _WwpLeosCfmExtMEPLastStatsLTMPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 17),
    _WwpLeosCfmExtMEPLastStatsLTMPriority_Type()
)
wwpLeosCfmExtMEPLastStatsLTMPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLTMPriority.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLTMSequenceNo_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLTMSequenceNo_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLTMSequenceNo = _WwpLeosCfmExtMEPLastStatsLTMSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 18),
    _WwpLeosCfmExtMEPLastStatsLTMSequenceNo_Type()
)
wwpLeosCfmExtMEPLastStatsLTMSequenceNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLTMSequenceNo.setStatus("current")
_WwpLeosCfmExtMEPLastStatsLTMInitialTTL_Type = Counter64
_WwpLeosCfmExtMEPLastStatsLTMInitialTTL_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsLTMInitialTTL = _WwpLeosCfmExtMEPLastStatsLTMInitialTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 19),
    _WwpLeosCfmExtMEPLastStatsLTMInitialTTL_Type()
)
wwpLeosCfmExtMEPLastStatsLTMInitialTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsLTMInitialTTL.setStatus("current")
_WwpLeosCfmExtMEPLastStatsFrameLossBadSequence_Type = Counter64
_WwpLeosCfmExtMEPLastStatsFrameLossBadSequence_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsFrameLossBadSequence = _WwpLeosCfmExtMEPLastStatsFrameLossBadSequence_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 20),
    _WwpLeosCfmExtMEPLastStatsFrameLossBadSequence_Type()
)
wwpLeosCfmExtMEPLastStatsFrameLossBadSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsFrameLossBadSequence.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMMinDelay_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMMinDelay_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMMinDelay = _WwpLeosCfmExtMEPLastStatsDMMMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 21),
    _WwpLeosCfmExtMEPLastStatsDMMMinDelay_Type()
)
wwpLeosCfmExtMEPLastStatsDMMMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMMinDelay.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMMaxDelay_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMMaxDelay_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMMaxDelay = _WwpLeosCfmExtMEPLastStatsDMMMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 22),
    _WwpLeosCfmExtMEPLastStatsDMMMaxDelay_Type()
)
wwpLeosCfmExtMEPLastStatsDMMMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMMaxDelay.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMMinJitter_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMMinJitter_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMMinJitter = _WwpLeosCfmExtMEPLastStatsDMMMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 23),
    _WwpLeosCfmExtMEPLastStatsDMMMinJitter_Type()
)
wwpLeosCfmExtMEPLastStatsDMMMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMMinJitter.setStatus("current")
_WwpLeosCfmExtMEPLastStatsDMMMaxJitter_Type = Counter64
_WwpLeosCfmExtMEPLastStatsDMMMaxJitter_Object = MibTableColumn
wwpLeosCfmExtMEPLastStatsDMMMaxJitter = _WwpLeosCfmExtMEPLastStatsDMMMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 3, 1, 24),
    _WwpLeosCfmExtMEPLastStatsDMMMaxJitter_Type()
)
wwpLeosCfmExtMEPLastStatsDMMMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPLastStatsDMMMaxJitter.setStatus("current")


class _WwpLeosCfmExtMEPClearStatistics_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPClearStatistics based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmExtMEPClearStatistics_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPClearStatistics_Object = MibScalar
wwpLeosCfmExtMEPClearStatistics = _WwpLeosCfmExtMEPClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 4),
    _WwpLeosCfmExtMEPClearStatistics_Type()
)
wwpLeosCfmExtMEPClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPClearStatistics.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryTable_Object = MibTable
wwpLeosCfmExtMEPDelayHistoryTable = _WwpLeosCfmExtMEPDelayHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryTable.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryEntry_Object = MibTableRow
wwpLeosCfmExtMEPDelayHistoryEntry = _WwpLeosCfmExtMEPDelayHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1)
)
wwpLeosCfmExtMEPDelayHistoryEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPDelayHistoryIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryEntry.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryIndex_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosCfmExtMEPDelayHistoryIndex_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDelayHistoryIndex_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryIndex = _WwpLeosCfmExtMEPDelayHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 1),
    _WwpLeosCfmExtMEPDelayHistoryIndex_Type()
)
wwpLeosCfmExtMEPDelayHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryIndex.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryStatus_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryStatus based on Integer32"""
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
        *(("canceled", 3),
          ("done", 2),
          ("running", 1),
          ("timeout", 4))
    )


_WwpLeosCfmExtMEPDelayHistoryStatus_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDelayHistoryStatus_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryStatus = _WwpLeosCfmExtMEPDelayHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 2),
    _WwpLeosCfmExtMEPDelayHistoryStatus_Type()
)
wwpLeosCfmExtMEPDelayHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryStatus.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryInterval_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMEPDelayHistoryInterval_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDelayHistoryInterval_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryInterval = _WwpLeosCfmExtMEPDelayHistoryInterval_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 3),
    _WwpLeosCfmExtMEPDelayHistoryInterval_Type()
)
wwpLeosCfmExtMEPDelayHistoryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryInterval.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMEPDelayHistoryPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDelayHistoryPriority_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryPriority = _WwpLeosCfmExtMEPDelayHistoryPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 4),
    _WwpLeosCfmExtMEPDelayHistoryPriority_Type()
)
wwpLeosCfmExtMEPDelayHistoryPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryPriority.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryMEPId_Type(Unsigned32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryMEPId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtMEPDelayHistoryMEPId_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtMEPDelayHistoryMEPId_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryMEPId = _WwpLeosCfmExtMEPDelayHistoryMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 5),
    _WwpLeosCfmExtMEPDelayHistoryMEPId_Type()
)
wwpLeosCfmExtMEPDelayHistoryMEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryMEPId.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryNumDMMSent_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryNumDMMSent_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryNumDMMSent = _WwpLeosCfmExtMEPDelayHistoryNumDMMSent_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 6),
    _WwpLeosCfmExtMEPDelayHistoryNumDMMSent_Type()
)
wwpLeosCfmExtMEPDelayHistoryNumDMMSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryNumDMMSent.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryNumDMRReceived_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryNumDMRReceived_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryNumDMRReceived = _WwpLeosCfmExtMEPDelayHistoryNumDMRReceived_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 7),
    _WwpLeosCfmExtMEPDelayHistoryNumDMRReceived_Type()
)
wwpLeosCfmExtMEPDelayHistoryNumDMRReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryNumDMRReceived.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryMinDelay_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryMinDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryMinDelay = _WwpLeosCfmExtMEPDelayHistoryMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 8),
    _WwpLeosCfmExtMEPDelayHistoryMinDelay_Type()
)
wwpLeosCfmExtMEPDelayHistoryMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryMinDelay.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryAveDelay_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryAveDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryAveDelay = _WwpLeosCfmExtMEPDelayHistoryAveDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 9),
    _WwpLeosCfmExtMEPDelayHistoryAveDelay_Type()
)
wwpLeosCfmExtMEPDelayHistoryAveDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryAveDelay.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryMaxDelay_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryMaxDelay_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryMaxDelay = _WwpLeosCfmExtMEPDelayHistoryMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 10),
    _WwpLeosCfmExtMEPDelayHistoryMaxDelay_Type()
)
wwpLeosCfmExtMEPDelayHistoryMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryMaxDelay.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryMinJitter_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryMinJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryMinJitter = _WwpLeosCfmExtMEPDelayHistoryMinJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 11),
    _WwpLeosCfmExtMEPDelayHistoryMinJitter_Type()
)
wwpLeosCfmExtMEPDelayHistoryMinJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryMinJitter.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryAveJitter_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryAveJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryAveJitter = _WwpLeosCfmExtMEPDelayHistoryAveJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 12),
    _WwpLeosCfmExtMEPDelayHistoryAveJitter_Type()
)
wwpLeosCfmExtMEPDelayHistoryAveJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryAveJitter.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryMaxJitter_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryMaxJitter_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryMaxJitter = _WwpLeosCfmExtMEPDelayHistoryMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 13),
    _WwpLeosCfmExtMEPDelayHistoryMaxJitter_Type()
)
wwpLeosCfmExtMEPDelayHistoryMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryMaxJitter.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryStartTime_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryStartTime_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryStartTime = _WwpLeosCfmExtMEPDelayHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 14),
    _WwpLeosCfmExtMEPDelayHistoryStartTime_Type()
)
wwpLeosCfmExtMEPDelayHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryStartTime.setStatus("current")
_WwpLeosCfmExtMEPDelayHistoryStopTime_Type = Unsigned32
_WwpLeosCfmExtMEPDelayHistoryStopTime_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryStopTime = _WwpLeosCfmExtMEPDelayHistoryStopTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 15),
    _WwpLeosCfmExtMEPDelayHistoryStopTime_Type()
)
wwpLeosCfmExtMEPDelayHistoryStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryStopTime.setStatus("current")


class _WwpLeosCfmExtMEPDelayHistoryClear_Type(Integer32):
    """Custom type wwpLeosCfmExtMEPDelayHistoryClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("none", 2))
    )


_WwpLeosCfmExtMEPDelayHistoryClear_Type.__name__ = "Integer32"
_WwpLeosCfmExtMEPDelayHistoryClear_Object = MibTableColumn
wwpLeosCfmExtMEPDelayHistoryClear = _WwpLeosCfmExtMEPDelayHistoryClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 7, 5, 1, 16),
    _WwpLeosCfmExtMEPDelayHistoryClear_Type()
)
wwpLeosCfmExtMEPDelayHistoryClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMEPDelayHistoryClear.setStatus("current")
_WwpLeosCfmExtLinkTrace_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtLinkTrace = _WwpLeosCfmExtLinkTrace_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8)
)
_WwpLeosCfmExtLinkTraceMsgTable_Object = MibTable
wwpLeosCfmExtLinkTraceMsgTable = _WwpLeosCfmExtLinkTraceMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgTable.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgEntry_Object = MibTableRow
wwpLeosCfmExtLinkTraceMsgEntry = _WwpLeosCfmExtLinkTraceMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1)
)
wwpLeosCfmExtLinkTraceMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtLinkTraceMsgLocalMepID"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgEntry.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgLocalMepID_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgLocalMepID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtLinkTraceMsgLocalMepID_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgLocalMepID_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgLocalMepID = _WwpLeosCfmExtLinkTraceMsgLocalMepID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 1),
    _WwpLeosCfmExtLinkTraceMsgLocalMepID_Type()
)
wwpLeosCfmExtLinkTraceMsgLocalMepID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgLocalMepID.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgTargetMEPID_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgTargetMEPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtLinkTraceMsgTargetMEPID_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgTargetMEPID = _WwpLeosCfmExtLinkTraceMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 2),
    _WwpLeosCfmExtLinkTraceMsgTargetMEPID_Type()
)
wwpLeosCfmExtLinkTraceMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgTargetMEPID.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmExtLinkTraceMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgTargetMacAddr = _WwpLeosCfmExtLinkTraceMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 3),
    _WwpLeosCfmExtLinkTraceMsgTargetMacAddr_Type()
)
wwpLeosCfmExtLinkTraceMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgTTL_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosCfmExtLinkTraceMsgTTL_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgTTL_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgTTL = _WwpLeosCfmExtLinkTraceMsgTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 4),
    _WwpLeosCfmExtLinkTraceMsgTTL_Type()
)
wwpLeosCfmExtLinkTraceMsgTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgTTL.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgSequenceNumber_Type = Integer32
_WwpLeosCfmExtLinkTraceMsgSequenceNumber_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgSequenceNumber = _WwpLeosCfmExtLinkTraceMsgSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 5),
    _WwpLeosCfmExtLinkTraceMsgSequenceNumber_Type()
)
wwpLeosCfmExtLinkTraceMsgSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgSequenceNumber.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtLinkTraceMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgPriority_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgPriority = _WwpLeosCfmExtLinkTraceMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 6),
    _WwpLeosCfmExtLinkTraceMsgPriority_Type()
)
wwpLeosCfmExtLinkTraceMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgPriority.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgAction_Type = SendState
_WwpLeosCfmExtLinkTraceMsgAction_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgAction = _WwpLeosCfmExtLinkTraceMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 1, 1, 7),
    _WwpLeosCfmExtLinkTraceMsgAction_Type()
)
wwpLeosCfmExtLinkTraceMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgAction.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplyTable_Object = MibTable
wwpLeosCfmExtLinkTraceMsgReplyTable = _WwpLeosCfmExtLinkTraceMsgReplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyTable.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplyEntry_Object = MibTableRow
wwpLeosCfmExtLinkTraceMsgReplyEntry = _WwpLeosCfmExtLinkTraceMsgReplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1)
)
wwpLeosCfmExtLinkTraceMsgReplyEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtLinkTraceMsgLocalMepID"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtLinkTraceMsgReplyTTL"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtLinkTraceMsgReplyTTLIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyEntry.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyTTL_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WwpLeosCfmExtLinkTraceMsgReplyTTL_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyTTL_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyTTL = _WwpLeosCfmExtLinkTraceMsgReplyTTL_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 1),
    _WwpLeosCfmExtLinkTraceMsgReplyTTL_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyTTL.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyTTLIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyTTLIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24576),
    )


_WwpLeosCfmExtLinkTraceMsgReplyTTLIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtLinkTraceMsgReplyTTLIndex_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyTTLIndex = _WwpLeosCfmExtLinkTraceMsgReplyTTLIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 2),
    _WwpLeosCfmExtLinkTraceMsgReplyTTLIndex_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyTTLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyTTLIndex.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplySequenceNumber_Type = Integer32
_WwpLeosCfmExtLinkTraceMsgReplySequenceNumber_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplySequenceNumber = _WwpLeosCfmExtLinkTraceMsgReplySequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 3),
    _WwpLeosCfmExtLinkTraceMsgReplySequenceNumber_Type()
)
wwpLeosCfmExtLinkTraceMsgReplySequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplySequenceNumber.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplyMPMacAddr_Type = MacAddress
_WwpLeosCfmExtLinkTraceMsgReplyMPMacAddr_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyMPMacAddr = _WwpLeosCfmExtLinkTraceMsgReplyMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 4),
    _WwpLeosCfmExtLinkTraceMsgReplyMPMacAddr_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyMPMacAddr.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplyMEPID_Type = Integer32
_WwpLeosCfmExtLinkTraceMsgReplyMEPID_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyMEPID = _WwpLeosCfmExtLinkTraceMsgReplyMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 5),
    _WwpLeosCfmExtLinkTraceMsgReplyMEPID_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyMEPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyMEPID.setStatus("current")
_WwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr_Type = MacAddress
_WwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr = _WwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 6),
    _WwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyRelayAction_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyRelayAction based on Integer32"""
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
        *(("fdb", 3),
          ("hit", 6),
          ("invalid", 1),
          ("mpdb", 4),
          ("noLearn", 5),
          ("unknown", 2))
    )


_WwpLeosCfmExtLinkTraceMsgReplyRelayAction_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyRelayAction_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyRelayAction = _WwpLeosCfmExtLinkTraceMsgReplyRelayAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 7),
    _WwpLeosCfmExtLinkTraceMsgReplyRelayAction_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyRelayAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyRelayAction.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyIngressPort_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyIngressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtLinkTraceMsgReplyIngressPort_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyIngressPort_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyIngressPort = _WwpLeosCfmExtLinkTraceMsgReplyIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 8),
    _WwpLeosCfmExtLinkTraceMsgReplyIngressPort_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyIngressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyIngressPort.setStatus("obsolete")


class _WwpLeosCfmExtLinkTraceMsgReplyIngressAction_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyIngressAction based on Integer32"""
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
        *(("blocked", 2),
          ("down", 4),
          ("none", 5),
          ("ok", 1),
          ("vid", 3))
    )


_WwpLeosCfmExtLinkTraceMsgReplyIngressAction_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyIngressAction_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyIngressAction = _WwpLeosCfmExtLinkTraceMsgReplyIngressAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 9),
    _WwpLeosCfmExtLinkTraceMsgReplyIngressAction_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyIngressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyIngressAction.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyEgressPort_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyEgressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtLinkTraceMsgReplyEgressPort_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyEgressPort_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyEgressPort = _WwpLeosCfmExtLinkTraceMsgReplyEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 10),
    _WwpLeosCfmExtLinkTraceMsgReplyEgressPort_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyEgressPort.setStatus("obsolete")


class _WwpLeosCfmExtLinkTraceMsgReplyEgressAction_Type(Integer32):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyEgressAction based on Integer32"""
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
        *(("blocked", 4),
          ("down", 3),
          ("none", 1),
          ("ok", 6),
          ("ttl", 2),
          ("vid", 5))
    )


_WwpLeosCfmExtLinkTraceMsgReplyEgressAction_Type.__name__ = "Integer32"
_WwpLeosCfmExtLinkTraceMsgReplyEgressAction_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyEgressAction = _WwpLeosCfmExtLinkTraceMsgReplyEgressAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 11),
    _WwpLeosCfmExtLinkTraceMsgReplyEgressAction_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyEgressAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyEgressAction.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyIngressPortStr_Type(DisplayString):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_WwpLeosCfmExtLinkTraceMsgReplyIngressPortStr_Type.__name__ = "DisplayString"
_WwpLeosCfmExtLinkTraceMsgReplyIngressPortStr_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr = _WwpLeosCfmExtLinkTraceMsgReplyIngressPortStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 12),
    _WwpLeosCfmExtLinkTraceMsgReplyIngressPortStr_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr.setStatus("current")


class _WwpLeosCfmExtLinkTraceMsgReplyEgressPortStr_Type(DisplayString):
    """Custom type wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_WwpLeosCfmExtLinkTraceMsgReplyEgressPortStr_Type.__name__ = "DisplayString"
_WwpLeosCfmExtLinkTraceMsgReplyEgressPortStr_Object = MibTableColumn
wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr = _WwpLeosCfmExtLinkTraceMsgReplyEgressPortStr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 8, 2, 1, 13),
    _WwpLeosCfmExtLinkTraceMsgReplyEgressPortStr_Type()
)
wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr.setStatus("current")
_WwpLeosCfmExtDelay_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtDelay = _WwpLeosCfmExtDelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12)
)
_WwpLeosCfmExtDelayMsgTable_Object = MibTable
wwpLeosCfmExtDelayMsgTable = _WwpLeosCfmExtDelayMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgTable.setStatus("current")
_WwpLeosCfmExtDelayMsgEntry_Object = MibTableRow
wwpLeosCfmExtDelayMsgEntry = _WwpLeosCfmExtDelayMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1)
)
wwpLeosCfmExtDelayMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtDelayMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgEntry.setStatus("current")


class _WwpLeosCfmExtDelayMsgLocalMEPId_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtDelayMsgLocalMEPId_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgLocalMEPId_Object = MibTableColumn
wwpLeosCfmExtDelayMsgLocalMEPId = _WwpLeosCfmExtDelayMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 1),
    _WwpLeosCfmExtDelayMsgLocalMEPId_Type()
)
wwpLeosCfmExtDelayMsgLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgLocalMEPId.setStatus("current")


class _WwpLeosCfmExtDelayMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmExtDelayMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtDelayMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtDelayMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmExtDelayMsgTargetMEPID = _WwpLeosCfmExtDelayMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 2),
    _WwpLeosCfmExtDelayMsgTargetMEPID_Type()
)
wwpLeosCfmExtDelayMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgTargetMEPID.setStatus("current")
_WwpLeosCfmExtDelayMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmExtDelayMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmExtDelayMsgTargetMacAddr = _WwpLeosCfmExtDelayMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 3),
    _WwpLeosCfmExtDelayMsgTargetMacAddr_Type()
)
wwpLeosCfmExtDelayMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmExtDelayMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2, 600),
    )


_WwpLeosCfmExtDelayMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgCount_Object = MibTableColumn
wwpLeosCfmExtDelayMsgCount = _WwpLeosCfmExtDelayMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 4),
    _WwpLeosCfmExtDelayMsgCount_Type()
)
wwpLeosCfmExtDelayMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgCount.setStatus("current")


class _WwpLeosCfmExtDelayMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtDelayMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgPriority_Object = MibTableColumn
wwpLeosCfmExtDelayMsgPriority = _WwpLeosCfmExtDelayMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 5),
    _WwpLeosCfmExtDelayMsgPriority_Type()
)
wwpLeosCfmExtDelayMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgPriority.setStatus("current")


class _WwpLeosCfmExtDelayMsgRepeat_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgRepeat based on Integer32"""
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


_WwpLeosCfmExtDelayMsgRepeat_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgRepeat_Object = MibTableColumn
wwpLeosCfmExtDelayMsgRepeat = _WwpLeosCfmExtDelayMsgRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 8),
    _WwpLeosCfmExtDelayMsgRepeat_Type()
)
wwpLeosCfmExtDelayMsgRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgRepeat.setStatus("current")


class _WwpLeosCfmExtDelayMsgRepeatCount_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosCfmExtDelayMsgRepeatCount_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgRepeatCount_Object = MibTableColumn
wwpLeosCfmExtDelayMsgRepeatCount = _WwpLeosCfmExtDelayMsgRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 9),
    _WwpLeosCfmExtDelayMsgRepeatCount_Type()
)
wwpLeosCfmExtDelayMsgRepeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgRepeatCount.setStatus("current")


class _WwpLeosCfmExtDelayMsgDelayThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_WwpLeosCfmExtDelayMsgDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgDelayThreshold_Object = MibTableColumn
wwpLeosCfmExtDelayMsgDelayThreshold = _WwpLeosCfmExtDelayMsgDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 41),
    _WwpLeosCfmExtDelayMsgDelayThreshold_Type()
)
wwpLeosCfmExtDelayMsgDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgDelayThreshold.setStatus("current")


class _WwpLeosCfmExtDelayMsgJitterThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_WwpLeosCfmExtDelayMsgJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgJitterThreshold_Object = MibTableColumn
wwpLeosCfmExtDelayMsgJitterThreshold = _WwpLeosCfmExtDelayMsgJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 42),
    _WwpLeosCfmExtDelayMsgJitterThreshold_Type()
)
wwpLeosCfmExtDelayMsgJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgJitterThreshold.setStatus("current")
_WwpLeosCfmExtDelayMsgAction_Type = SendState
_WwpLeosCfmExtDelayMsgAction_Object = MibTableColumn
wwpLeosCfmExtDelayMsgAction = _WwpLeosCfmExtDelayMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 43),
    _WwpLeosCfmExtDelayMsgAction_Type()
)
wwpLeosCfmExtDelayMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgAction.setStatus("current")


class _WwpLeosCfmExtDelayMsgMaxDelayThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgMaxDelayThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_WwpLeosCfmExtDelayMsgMaxDelayThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgMaxDelayThreshold_Object = MibTableColumn
wwpLeosCfmExtDelayMsgMaxDelayThreshold = _WwpLeosCfmExtDelayMsgMaxDelayThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 44),
    _WwpLeosCfmExtDelayMsgMaxDelayThreshold_Type()
)
wwpLeosCfmExtDelayMsgMaxDelayThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgMaxDelayThreshold.setStatus("current")


class _WwpLeosCfmExtDelayMsgMaxJitterThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtDelayMsgMaxJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_WwpLeosCfmExtDelayMsgMaxJitterThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtDelayMsgMaxJitterThreshold_Object = MibTableColumn
wwpLeosCfmExtDelayMsgMaxJitterThreshold = _WwpLeosCfmExtDelayMsgMaxJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 12, 1, 1, 45),
    _WwpLeosCfmExtDelayMsgMaxJitterThreshold_Type()
)
wwpLeosCfmExtDelayMsgMaxJitterThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayMsgMaxJitterThreshold.setStatus("current")
_WwpLeosCfmExtFrameLoss_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtFrameLoss = _WwpLeosCfmExtFrameLoss_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13)
)
_WwpLeosCfmExtFrameLossMsgTable_Object = MibTable
wwpLeosCfmExtFrameLossMsgTable = _WwpLeosCfmExtFrameLossMsgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgTable.setStatus("current")
_WwpLeosCfmExtFrameLossMsgEntry_Object = MibTableRow
wwpLeosCfmExtFrameLossMsgEntry = _WwpLeosCfmExtFrameLossMsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1)
)
wwpLeosCfmExtFrameLossMsgEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtFrameLossMsgLocalMEPId"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgEntry.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgLocalMEPId_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgLocalMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtFrameLossMsgLocalMEPId_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgLocalMEPId_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgLocalMEPId = _WwpLeosCfmExtFrameLossMsgLocalMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 1),
    _WwpLeosCfmExtFrameLossMsgLocalMEPId_Type()
)
wwpLeosCfmExtFrameLossMsgLocalMEPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgLocalMEPId.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgTargetMEPID_Type(Unsigned32):
    """Custom type wwpLeosCfmExtFrameLossMsgTargetMEPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtFrameLossMsgTargetMEPID_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtFrameLossMsgTargetMEPID_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgTargetMEPID = _WwpLeosCfmExtFrameLossMsgTargetMEPID_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 2),
    _WwpLeosCfmExtFrameLossMsgTargetMEPID_Type()
)
wwpLeosCfmExtFrameLossMsgTargetMEPID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgTargetMEPID.setStatus("current")
_WwpLeosCfmExtFrameLossMsgTargetMacAddr_Type = MacAddress
_WwpLeosCfmExtFrameLossMsgTargetMacAddr_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgTargetMacAddr = _WwpLeosCfmExtFrameLossMsgTargetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 3),
    _WwpLeosCfmExtFrameLossMsgTargetMacAddr_Type()
)
wwpLeosCfmExtFrameLossMsgTargetMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgTargetMacAddr.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgCount_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 600),
    )


_WwpLeosCfmExtFrameLossMsgCount_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgCount_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgCount = _WwpLeosCfmExtFrameLossMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 4),
    _WwpLeosCfmExtFrameLossMsgCount_Type()
)
wwpLeosCfmExtFrameLossMsgCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgCount.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgPriority_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtFrameLossMsgPriority_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgPriority_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgPriority = _WwpLeosCfmExtFrameLossMsgPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 5),
    _WwpLeosCfmExtFrameLossMsgPriority_Type()
)
wwpLeosCfmExtFrameLossMsgPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgPriority.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgRepeat_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgRepeat based on Integer32"""
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


_WwpLeosCfmExtFrameLossMsgRepeat_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgRepeat_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgRepeat = _WwpLeosCfmExtFrameLossMsgRepeat_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 8),
    _WwpLeosCfmExtFrameLossMsgRepeat_Type()
)
wwpLeosCfmExtFrameLossMsgRepeat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgRepeat.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgRepeatCount_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgRepeatCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WwpLeosCfmExtFrameLossMsgRepeatCount_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgRepeatCount_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgRepeatCount = _WwpLeosCfmExtFrameLossMsgRepeatCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 9),
    _WwpLeosCfmExtFrameLossMsgRepeatCount_Type()
)
wwpLeosCfmExtFrameLossMsgRepeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgRepeatCount.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgFlnThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgFlnThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_WwpLeosCfmExtFrameLossMsgFlnThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgFlnThreshold_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgFlnThreshold = _WwpLeosCfmExtFrameLossMsgFlnThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 10),
    _WwpLeosCfmExtFrameLossMsgFlnThreshold_Type()
)
wwpLeosCfmExtFrameLossMsgFlnThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgFlnThreshold.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgFlfThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgFlfThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_WwpLeosCfmExtFrameLossMsgFlfThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgFlfThreshold_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgFlfThreshold = _WwpLeosCfmExtFrameLossMsgFlfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 11),
    _WwpLeosCfmExtFrameLossMsgFlfThreshold_Type()
)
wwpLeosCfmExtFrameLossMsgFlfThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgFlfThreshold.setStatus("current")
_WwpLeosCfmExtFrameLossMsgAction_Type = SendState
_WwpLeosCfmExtFrameLossMsgAction_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgAction = _WwpLeosCfmExtFrameLossMsgAction_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 12),
    _WwpLeosCfmExtFrameLossMsgAction_Type()
)
wwpLeosCfmExtFrameLossMsgAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgAction.setStatus("current")


class _WwpLeosCfmExtFrameLossMsgSeqThreshold_Type(Integer32):
    """Custom type wwpLeosCfmExtFrameLossMsgSeqThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 600),
    )


_WwpLeosCfmExtFrameLossMsgSeqThreshold_Type.__name__ = "Integer32"
_WwpLeosCfmExtFrameLossMsgSeqThreshold_Object = MibTableColumn
wwpLeosCfmExtFrameLossMsgSeqThreshold = _WwpLeosCfmExtFrameLossMsgSeqThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 13, 1, 1, 13),
    _WwpLeosCfmExtFrameLossMsgSeqThreshold_Type()
)
wwpLeosCfmExtFrameLossMsgSeqThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossMsgSeqThreshold.setStatus("current")
_WwpLeosCfmExtInterfaceStack_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtInterfaceStack = _WwpLeosCfmExtInterfaceStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14)
)
_WwpLeosCfmExtInterfaceStackTable_Object = MibTable
wwpLeosCfmExtInterfaceStackTable = _WwpLeosCfmExtInterfaceStackTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackTable.setStatus("current")
_WwpLeosCfmExtInterfaceStackEntry_Object = MibTableRow
wwpLeosCfmExtInterfaceStackEntry = _WwpLeosCfmExtInterfaceStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1)
)
wwpLeosCfmExtInterfaceStackEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackServiceInstanceType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackServiceInstanceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackInterfaceType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackInterfaceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackStackType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceStackLevel"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackEntry.setStatus("current")


class _WwpLeosCfmExtInterfaceStackServiceInstanceType_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackServiceInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethVs", 1),
          ("pbtTunnel", 3),
          ("vlan", 2))
    )


_WwpLeosCfmExtInterfaceStackServiceInstanceType_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackServiceInstanceType_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackServiceInstanceType = _WwpLeosCfmExtInterfaceStackServiceInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 1),
    _WwpLeosCfmExtInterfaceStackServiceInstanceType_Type()
)
wwpLeosCfmExtInterfaceStackServiceInstanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackServiceInstanceType.setStatus("current")


class _WwpLeosCfmExtInterfaceStackServiceInstanceIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmExtInterfaceStackServiceInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtInterfaceStackServiceInstanceIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtInterfaceStackServiceInstanceIndex_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackServiceInstanceIndex = _WwpLeosCfmExtInterfaceStackServiceInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 2),
    _WwpLeosCfmExtInterfaceStackServiceInstanceIndex_Type()
)
wwpLeosCfmExtInterfaceStackServiceInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackServiceInstanceIndex.setStatus("current")


class _WwpLeosCfmExtInterfaceStackInterfaceType_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("logicalPort", 1),
          ("none", 99),
          ("pbtDecap", 3),
          ("pbtEncap", 2))
    )


_WwpLeosCfmExtInterfaceStackInterfaceType_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackInterfaceType_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackInterfaceType = _WwpLeosCfmExtInterfaceStackInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 3),
    _WwpLeosCfmExtInterfaceStackInterfaceType_Type()
)
wwpLeosCfmExtInterfaceStackInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackInterfaceType.setStatus("current")
_WwpLeosCfmExtInterfaceStackInterfaceIndex_Type = Unsigned32
_WwpLeosCfmExtInterfaceStackInterfaceIndex_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackInterfaceIndex = _WwpLeosCfmExtInterfaceStackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 4),
    _WwpLeosCfmExtInterfaceStackInterfaceIndex_Type()
)
wwpLeosCfmExtInterfaceStackInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackInterfaceIndex.setStatus("current")


class _WwpLeosCfmExtInterfaceStackLevel_Type(Unsigned32):
    """Custom type wwpLeosCfmExtInterfaceStackLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtInterfaceStackLevel_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtInterfaceStackLevel_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackLevel = _WwpLeosCfmExtInterfaceStackLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 5),
    _WwpLeosCfmExtInterfaceStackLevel_Type()
)
wwpLeosCfmExtInterfaceStackLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackLevel.setStatus("current")


class _WwpLeosCfmExtInterfaceStackStackType_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackStackType based on Integer32"""
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
        *(("mepDown", 2),
          ("mepUp", 1),
          ("mipDown", 4),
          ("mipUp", 3))
    )


_WwpLeosCfmExtInterfaceStackStackType_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackStackType_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackStackType = _WwpLeosCfmExtInterfaceStackStackType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 6),
    _WwpLeosCfmExtInterfaceStackStackType_Type()
)
wwpLeosCfmExtInterfaceStackStackType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackStackType.setStatus("current")


class _WwpLeosCfmExtInterfaceStackInterfaceName_Type(DisplayString):
    """Custom type wwpLeosCfmExtInterfaceStackInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmExtInterfaceStackInterfaceName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtInterfaceStackInterfaceName_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackInterfaceName = _WwpLeosCfmExtInterfaceStackInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 7),
    _WwpLeosCfmExtInterfaceStackInterfaceName_Type()
)
wwpLeosCfmExtInterfaceStackInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackInterfaceName.setStatus("current")


class _WwpLeosCfmExtInterfaceStackServiceInstanceName_Type(DisplayString):
    """Custom type wwpLeosCfmExtInterfaceStackServiceInstanceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmExtInterfaceStackServiceInstanceName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtInterfaceStackServiceInstanceName_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackServiceInstanceName = _WwpLeosCfmExtInterfaceStackServiceInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 8),
    _WwpLeosCfmExtInterfaceStackServiceInstanceName_Type()
)
wwpLeosCfmExtInterfaceStackServiceInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackServiceInstanceName.setStatus("current")


class _WwpLeosCfmExtInterfaceStackPortName_Type(DisplayString):
    """Custom type wwpLeosCfmExtInterfaceStackPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_WwpLeosCfmExtInterfaceStackPortName_Type.__name__ = "DisplayString"
_WwpLeosCfmExtInterfaceStackPortName_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackPortName = _WwpLeosCfmExtInterfaceStackPortName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 9),
    _WwpLeosCfmExtInterfaceStackPortName_Type()
)
wwpLeosCfmExtInterfaceStackPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackPortName.setStatus("current")


class _WwpLeosCfmExtInterfaceStackOperState_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackOperState based on Integer32"""
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


_WwpLeosCfmExtInterfaceStackOperState_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackOperState_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackOperState = _WwpLeosCfmExtInterfaceStackOperState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 10),
    _WwpLeosCfmExtInterfaceStackOperState_Type()
)
wwpLeosCfmExtInterfaceStackOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackOperState.setStatus("current")


class _WwpLeosCfmExtInterfaceStackVid_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_WwpLeosCfmExtInterfaceStackVid_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackVid_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackVid = _WwpLeosCfmExtInterfaceStackVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 11),
    _WwpLeosCfmExtInterfaceStackVid_Type()
)
wwpLeosCfmExtInterfaceStackVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackVid.setStatus("current")
_WwpLeosCfmExtInterfaceStackPgid_Type = Unsigned32
_WwpLeosCfmExtInterfaceStackPgid_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackPgid = _WwpLeosCfmExtInterfaceStackPgid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 12),
    _WwpLeosCfmExtInterfaceStackPgid_Type()
)
wwpLeosCfmExtInterfaceStackPgid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackPgid.setStatus("current")


class _WwpLeosCfmExtInterfaceStackMEPId_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceStackMEPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WwpLeosCfmExtInterfaceStackMEPId_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceStackMEPId_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackMEPId = _WwpLeosCfmExtInterfaceStackMEPId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 13),
    _WwpLeosCfmExtInterfaceStackMEPId_Type()
)
wwpLeosCfmExtInterfaceStackMEPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackMEPId.setStatus("current")
_WwpLeosCfmExtInterfaceStackMacAddress_Type = MacAddress
_WwpLeosCfmExtInterfaceStackMacAddress_Object = MibTableColumn
wwpLeosCfmExtInterfaceStackMacAddress = _WwpLeosCfmExtInterfaceStackMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 14, 1, 1, 14),
    _WwpLeosCfmExtInterfaceStackMacAddress_Type()
)
wwpLeosCfmExtInterfaceStackMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceStackMacAddress.setStatus("current")
_WwpLeosCfmExtMIP_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtMIP = _WwpLeosCfmExtMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15)
)
_WwpLeosCfmExtMipTable_Object = MibTable
wwpLeosCfmExtMipTable = _WwpLeosCfmExtMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipTable.setStatus("current")
_WwpLeosCfmExtMipEntry_Object = MibTableRow
wwpLeosCfmExtMipEntry = _WwpLeosCfmExtMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1, 1)
)
wwpLeosCfmExtMipEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMipVid"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMipPort"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMipLevel"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipEntry.setStatus("current")


class _WwpLeosCfmExtMipVid_Type(Integer32):
    """Custom type wwpLeosCfmExtMipVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24576),
    )


_WwpLeosCfmExtMipVid_Type.__name__ = "Integer32"
_WwpLeosCfmExtMipVid_Object = MibTableColumn
wwpLeosCfmExtMipVid = _WwpLeosCfmExtMipVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1, 1, 1),
    _WwpLeosCfmExtMipVid_Type()
)
wwpLeosCfmExtMipVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipVid.setStatus("current")


class _WwpLeosCfmExtMipPort_Type(Integer32):
    """Custom type wwpLeosCfmExtMipPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtMipPort_Type.__name__ = "Integer32"
_WwpLeosCfmExtMipPort_Object = MibTableColumn
wwpLeosCfmExtMipPort = _WwpLeosCfmExtMipPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1, 1, 2),
    _WwpLeosCfmExtMipPort_Type()
)
wwpLeosCfmExtMipPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipPort.setStatus("current")


class _WwpLeosCfmExtMipLevel_Type(Integer32):
    """Custom type wwpLeosCfmExtMipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtMipLevel_Type.__name__ = "Integer32"
_WwpLeosCfmExtMipLevel_Object = MibTableColumn
wwpLeosCfmExtMipLevel = _WwpLeosCfmExtMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1, 1, 3),
    _WwpLeosCfmExtMipLevel_Type()
)
wwpLeosCfmExtMipLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipLevel.setStatus("current")
_WwpLeosCfmExtMipStatus_Type = RowStatus
_WwpLeosCfmExtMipStatus_Object = MibTableColumn
wwpLeosCfmExtMipStatus = _WwpLeosCfmExtMipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 15, 1, 1, 4),
    _WwpLeosCfmExtMipStatus_Type()
)
wwpLeosCfmExtMipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtMipStatus.setStatus("current")
_WwpLeosCfmExtInterfaceMIP_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtInterfaceMIP = _WwpLeosCfmExtInterfaceMIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16)
)
_WwpLeosCfmExtInterfaceMipTable_Object = MibTable
wwpLeosCfmExtInterfaceMipTable = _WwpLeosCfmExtInterfaceMipTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipTable.setStatus("current")
_WwpLeosCfmExtInterfaceMipEntry_Object = MibTableRow
wwpLeosCfmExtInterfaceMipEntry = _WwpLeosCfmExtInterfaceMipEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1)
)
wwpLeosCfmExtInterfaceMipEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipServiceInstanceType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipServiceInstanceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipInterfaceType"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipInterfaceIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipInterfaceSubIndex"),
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtInterfaceMipLevel"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipEntry.setStatus("current")


class _WwpLeosCfmExtInterfaceMipServiceInstanceType_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceMipServiceInstanceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethVs", 1),
          ("pbtTunnel", 3),
          ("vlan", 2))
    )


_WwpLeosCfmExtInterfaceMipServiceInstanceType_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceMipServiceInstanceType_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipServiceInstanceType = _WwpLeosCfmExtInterfaceMipServiceInstanceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 1),
    _WwpLeosCfmExtInterfaceMipServiceInstanceType_Type()
)
wwpLeosCfmExtInterfaceMipServiceInstanceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipServiceInstanceType.setStatus("current")


class _WwpLeosCfmExtInterfaceMipServiceInstanceIndex_Type(Unsigned32):
    """Custom type wwpLeosCfmExtInterfaceMipServiceInstanceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosCfmExtInterfaceMipServiceInstanceIndex_Type.__name__ = "Unsigned32"
_WwpLeosCfmExtInterfaceMipServiceInstanceIndex_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipServiceInstanceIndex = _WwpLeosCfmExtInterfaceMipServiceInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 2),
    _WwpLeosCfmExtInterfaceMipServiceInstanceIndex_Type()
)
wwpLeosCfmExtInterfaceMipServiceInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipServiceInstanceIndex.setStatus("current")


class _WwpLeosCfmExtInterfaceMipInterfaceType_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceMipInterfaceType based on Integer32"""
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
        *(("none", 0),
          ("pbtDecap", 3),
          ("pbtEncap", 2),
          ("portVlan", 1))
    )


_WwpLeosCfmExtInterfaceMipInterfaceType_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceMipInterfaceType_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipInterfaceType = _WwpLeosCfmExtInterfaceMipInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 3),
    _WwpLeosCfmExtInterfaceMipInterfaceType_Type()
)
wwpLeosCfmExtInterfaceMipInterfaceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipInterfaceType.setStatus("current")
_WwpLeosCfmExtInterfaceMipInterfaceIndex_Type = Unsigned32
_WwpLeosCfmExtInterfaceMipInterfaceIndex_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipInterfaceIndex = _WwpLeosCfmExtInterfaceMipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 4),
    _WwpLeosCfmExtInterfaceMipInterfaceIndex_Type()
)
wwpLeosCfmExtInterfaceMipInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipInterfaceIndex.setStatus("current")
_WwpLeosCfmExtInterfaceMipInterfaceSubIndex_Type = Unsigned32
_WwpLeosCfmExtInterfaceMipInterfaceSubIndex_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipInterfaceSubIndex = _WwpLeosCfmExtInterfaceMipInterfaceSubIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 5),
    _WwpLeosCfmExtInterfaceMipInterfaceSubIndex_Type()
)
wwpLeosCfmExtInterfaceMipInterfaceSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipInterfaceSubIndex.setStatus("current")


class _WwpLeosCfmExtInterfaceMipLevel_Type(Integer32):
    """Custom type wwpLeosCfmExtInterfaceMipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosCfmExtInterfaceMipLevel_Type.__name__ = "Integer32"
_WwpLeosCfmExtInterfaceMipLevel_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipLevel = _WwpLeosCfmExtInterfaceMipLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 6),
    _WwpLeosCfmExtInterfaceMipLevel_Type()
)
wwpLeosCfmExtInterfaceMipLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipLevel.setStatus("current")
_WwpLeosCfmExtInterfaceMipStatus_Type = RowStatus
_WwpLeosCfmExtInterfaceMipStatus_Object = MibTableColumn
wwpLeosCfmExtInterfaceMipStatus = _WwpLeosCfmExtInterfaceMipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 16, 1, 1, 7),
    _WwpLeosCfmExtInterfaceMipStatus_Type()
)
wwpLeosCfmExtInterfaceMipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosCfmExtInterfaceMipStatus.setStatus("current")
_WwpLeosCfmExtOamPort_ObjectIdentity = ObjectIdentity
wwpLeosCfmExtOamPort = _WwpLeosCfmExtOamPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 17)
)
_WwpLeosCfmExtOamPortTable_Object = MibTable
wwpLeosCfmExtOamPortTable = _WwpLeosCfmExtOamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 17, 1)
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtOamPortTable.setStatus("current")
_WwpLeosCfmExtOamPortEntry_Object = MibTableRow
wwpLeosCfmExtOamPortEntry = _WwpLeosCfmExtOamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 17, 1, 1)
)
wwpLeosCfmExtOamPortEntry.setIndexNames(
    (0, "WWP-LEOS-CFM-MIB", "wwpLeosCfmExtOamPortIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtOamPortEntry.setStatus("current")


class _WwpLeosCfmExtOamPortIndex_Type(Integer32):
    """Custom type wwpLeosCfmExtOamPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3072),
    )


_WwpLeosCfmExtOamPortIndex_Type.__name__ = "Integer32"
_WwpLeosCfmExtOamPortIndex_Object = MibTableColumn
wwpLeosCfmExtOamPortIndex = _WwpLeosCfmExtOamPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 17, 1, 1, 1),
    _WwpLeosCfmExtOamPortIndex_Type()
)
wwpLeosCfmExtOamPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosCfmExtOamPortIndex.setStatus("current")
_WwpLeosCfmExtOamPortSupported_Type = TruthValue
_WwpLeosCfmExtOamPortSupported_Object = MibTableColumn
wwpLeosCfmExtOamPortSupported = _WwpLeosCfmExtOamPortSupported_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 1, 21, 17, 1, 1, 2),
    _WwpLeosCfmExtOamPortSupported_Type()
)
wwpLeosCfmExtOamPortSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosCfmExtOamPortSupported.setStatus("current")
_WwpLeosCfmNotifMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosCfmNotifMIBNotificationPrefix = _WwpLeosCfmNotifMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2)
)
_WwpLeosCfmNotifMIBNotification_ObjectIdentity = ObjectIdentity
wwpLeosCfmNotifMIBNotification = _WwpLeosCfmNotifMIBNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0)
)
_WwpLeosCfmMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosCfmMIBConformance = _WwpLeosCfmMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 3)
)
_WwpLeosCfmMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosCfmMIBCompliances = _WwpLeosCfmMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 3, 1)
)
_WwpLeosCfmMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosCfmMIBGroups = _WwpLeosCfmMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosCfmFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 1)
)
wwpLeosCfmFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultTime"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultDesc"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultMep"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmPbtFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 2)
)
wwpLeosCfmPbtFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceValue"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceAdminState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceOperState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultTime"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultDesc"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmPbtFaultTrap.setStatus(
        "deprecated"
    )

wwpLeosCfmDelayFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 3)
)
wwpLeosCfmDelayFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPDelay"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmDelayMsgDelayThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmDelayFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmJitterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 4)
)
wwpLeosCfmJitterFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPJitter"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmDelayMsgJitterThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmJitterFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmFrameLossNearFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 5)
)
wwpLeosCfmFrameLossNearFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPFrameLossNear"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmFrameLossMsgFlnThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossNearFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmFrameLossFarFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 6)
)
wwpLeosCfmFrameLossFarFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPFrameLossFar"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmFrameLossMsgFlfThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmFrameLossFarFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmExtDelayFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 7)
)
wwpLeosCfmExtDelayFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPDelay"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtDelayMsgDelayThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtDelayFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmExtJitterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 8)
)
wwpLeosCfmExtJitterFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPJitter"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtDelayMsgJitterThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtJitterFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmExtFrameLossNearFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 9)
)
wwpLeosCfmExtFrameLossNearFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPFrameLossNear"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtFrameLossMsgFlnThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossNearFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 10)
)
wwpLeosCfmFaultTrapSet.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceValue"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceAdminState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceOperState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultTime"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultDesc"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultMep"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVsPbtName"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmFaultTrapSet.setStatus(
        "current"
    )

wwpLeosCfmFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 11)
)
wwpLeosCfmFaultTrapClear.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceValue"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceAdminState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceOperState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVsPbtName"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmFaultTrapClear.setStatus(
        "current"
    )

wwpLeosCfmDmmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 12)
)
wwpLeosCfmDmmTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgLocalMEPId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgDelayThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgDelay"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgJitterThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgJitter"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgMaxJitterThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgMaxJitter"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgMaxDelayThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmDelayMsgMaxDelay"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmDmmTrap.setStatus(
        "current"
    )

wwpLeosCfmLmmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 13)
)
wwpLeosCfmLmmTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgLocalMEPId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgNearLossThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgFrameLossNear"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgFarLossThreshold"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosTceCfmFrameLossMsgFrameLossFar"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmLmmTrap.setStatus(
        "current"
    )

wwpLeosCfmExtFrameLossFarFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 20)
)
wwpLeosCfmExtFrameLossFarFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmRemoteMEPFrameLossFar"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtFrameLossMsgFlfThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFrameLossFarFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmExtFaultTrapSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 21)
)
wwpLeosCfmExtFaultTrapSet.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceValue"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceAdminState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceOperState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultTime"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultDesc"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultMep"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFaultTrapSet.setStatus(
        "current"
    )

wwpLeosCfmExtFaultTrapClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 22)
)
wwpLeosCfmExtFaultTrapClear.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceValue"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceAdminState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceOperState"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultTime"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultType"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultDesc"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceFaultMep"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmExtFaultTrapClear.setStatus(
        "current"
    )

wwpLeosCfmBadSequenceFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 23)
)
wwpLeosCfmBadSequenceFaultTrap.setObjects(
      *(("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceVlan"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPLMMBadSequence"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtFrameLossMsgSeqThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmBadSequenceFaultTrap.setStatus(
        "current"
    )

wwpLeosCfmBlockOppositeMEPSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 24)
)
wwpLeosCfmBlockOppositeMEPSetTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceCfmMAID"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtVlanId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPTagVID"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPBlockOppositeFaultCurrent"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmBlockOppositeMEPSetTrap.setStatus(
        "current"
    )

wwpLeosCfmBlockOppositeMEPClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 35, 2, 0, 25)
)
wwpLeosCfmBlockOppositeMEPClearTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceMdLevel"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmServiceCfmMAID"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtVlanId"),
        ("WWP-LEOS-CFM-MIB", "wwpLeosCfmExtMEPTagVID"))
)
if mibBuilder.loadTexts:
    wwpLeosCfmBlockOppositeMEPClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-CFM-MIB",
    **{"CfmMAID": CfmMAID,
       "CfmDisplayString": CfmDisplayString,
       "EthType": EthType,
       "SendState": SendState,
       "Dot1agCfmMaintDomainNameType": Dot1agCfmMaintDomainNameType,
       "Dot1agCfmMaintDomainName": Dot1agCfmMaintDomainName,
       "Dot1agCfmMaintAssocNameType": Dot1agCfmMaintAssocNameType,
       "Dot1agCfmMaintAssocName": Dot1agCfmMaintAssocName,
       "wwpLeosCfmMIB": wwpLeosCfmMIB,
       "wwpLeosCfmMIBObjects": wwpLeosCfmMIBObjects,
       "wwpLeosCfmGlobal": wwpLeosCfmGlobal,
       "wwpLeosCfmState": wwpLeosCfmState,
       "wwpLeosCfmEtherType": wwpLeosCfmEtherType,
       "wwpLeosCfmMEPHoldTime": wwpLeosCfmMEPHoldTime,
       "wwpLeosCfmCcmAvailable": wwpLeosCfmCcmAvailable,
       "wwpLeosCfmY1731EtherType": wwpLeosCfmY1731EtherType,
       "wwpLeosCfmL2LoopDetectState": wwpLeosCfmL2LoopDetectState,
       "wwpLeosCfmDot1adStrict": wwpLeosCfmDot1adStrict,
       "wwpLeosCfmMipLevelEnforcement": wwpLeosCfmMipLevelEnforcement,
       "wwpLeosCfmMipCcmDbState": wwpLeosCfmMipCcmDbState,
       "wwpLeosCfmLBMDefaultCount": wwpLeosCfmLBMDefaultCount,
       "wwpLeosCfmLBMDefaultInterval": wwpLeosCfmLBMDefaultInterval,
       "wwpLeosCfmLBMDefaultTimeout": wwpLeosCfmLBMDefaultTimeout,
       "wwpLeosCfmFrameClassifierMode": wwpLeosCfmFrameClassifierMode,
       "wwpLeosCfmGlobalLBMDefaultCount": wwpLeosCfmGlobalLBMDefaultCount,
       "wwpLeosCfmGlobalLBMDefaultInterval": wwpLeosCfmGlobalLBMDefaultInterval,
       "wwpLeosCfmGlobalLBMDefaultTimeout": wwpLeosCfmGlobalLBMDefaultTimeout,
       "wwpLeosCfmGlobalFrameClassifierMode": wwpLeosCfmGlobalFrameClassifierMode,
       "wwpLeosCfmGlobalFrameBudget": wwpLeosCfmGlobalFrameBudget,
       "wwpLeosCfmGlobalControlModuleFrameBudget": wwpLeosCfmGlobalControlModuleFrameBudget,
       "wwpLeosCfmGlobalFrameBudgetTable": wwpLeosCfmGlobalFrameBudgetTable,
       "wwpLeosCfmGlobalFrameBudgetEntry": wwpLeosCfmGlobalFrameBudgetEntry,
       "wwpLeosCfmGlobalFrameBudgetSlotIndex": wwpLeosCfmGlobalFrameBudgetSlotIndex,
       "wwpLeosCfmGlobalFrameBudgetValue": wwpLeosCfmGlobalFrameBudgetValue,
       "wwpLeosCfmGlobalStats": wwpLeosCfmGlobalStats,
       "wwpLeosCfmStatsTotalTx": wwpLeosCfmStatsTotalTx,
       "wwpLeosCfmStatsTotalRx": wwpLeosCfmStatsTotalRx,
       "wwpLeosCfmStatsTxFloodedFrames": wwpLeosCfmStatsTxFloodedFrames,
       "wwpLeosCfmStatsTxFloodedIgnoredStpState": wwpLeosCfmStatsTxFloodedIgnoredStpState,
       "wwpLeosCfmStatsRxTotalValidFrames": wwpLeosCfmStatsRxTotalValidFrames,
       "wwpLeosCfmStatsRxTotalNotValidatedFrames": wwpLeosCfmStatsRxTotalNotValidatedFrames,
       "wwpLeosCfmStatsRxTotalInValidFrames": wwpLeosCfmStatsRxTotalInValidFrames,
       "wwpLeosCfmTotalRxInvalidMessageOverflow": wwpLeosCfmTotalRxInvalidMessageOverflow,
       "wwpLeosCfmTotalRxInvalidPortStatusTLV": wwpLeosCfmTotalRxInvalidPortStatusTLV,
       "wwpLeosCfmTotalRxInvalidInterfaceStatusTLV": wwpLeosCfmTotalRxInvalidInterfaceStatusTLV,
       "wwpLeosCfmTotalRxInvalidSenderIDTLV": wwpLeosCfmTotalRxInvalidSenderIDTLV,
       "wwpLeosCfmRxAdminDisableDropped": wwpLeosCfmRxAdminDisableDropped,
       "wwpLesoCfmRxInvalidEtypeDropped": wwpLesoCfmRxInvalidEtypeDropped,
       "wwpLeosCfmRxInvalidOpCodeDropped": wwpLeosCfmRxInvalidOpCodeDropped,
       "wwpLeosCfmRxSTPStateNotForwardingDropped": wwpLeosCfmRxSTPStateNotForwardingDropped,
       "wwpLeosCfmGlobalStatsClear": wwpLeosCfmGlobalStatsClear,
       "wwpLeosCfmGlobalLoopbackMsgStatsClear": wwpLeosCfmGlobalLoopbackMsgStatsClear,
       "wwpLeosCfmGlobalLinkTraceMsgStatsClear": wwpLeosCfmGlobalLinkTraceMsgStatsClear,
       "wwpLeosCfmGlobalDelayMeasurementMsgStatsClear": wwpLeosCfmGlobalDelayMeasurementMsgStatsClear,
       "wwpLeosCfmGlobalLossMeasurementMsgStatsClear": wwpLeosCfmGlobalLossMeasurementMsgStatsClear,
       "wwpLeosCfmTotalRxDropBlockedOppositeMep": wwpLeosCfmTotalRxDropBlockedOppositeMep,
       "wwpLeosCfmGlobalCCMStats": wwpLeosCfmGlobalCCMStats,
       "wwpLeosCfmTotalTxCCM": wwpLeosCfmTotalTxCCM,
       "wwpLeosCfmTotalTxCCMFlooded": wwpLeosCfmTotalTxCCMFlooded,
       "wwpLeosCfmTotalRxValidCCM": wwpLeosCfmTotalRxValidCCM,
       "wwpLeosCfmTotalRxCCMInSequence": wwpLeosCfmTotalRxCCMInSequence,
       "wwpLeosCfmTotalRxCCMSequenceError": wwpLeosCfmTotalRxCCMSequenceError,
       "wwpLeosCfmTotalCCMRxMDLevelXcon": wwpLeosCfmTotalCCMRxMDLevelXcon,
       "wwpLeosCfmTotalCCMRxMAIDXcon": wwpLeosCfmTotalCCMRxMAIDXcon,
       "wwpLeosCfmTotalRxCCMErrorOnMepId": wwpLeosCfmTotalRxCCMErrorOnMepId,
       "wwpLeosCfmTotalRxCCMIntervalError": wwpLeosCfmTotalRxCCMIntervalError,
       "wwpLeosCfmTotalRxInvalidCCM": wwpLeosCfmTotalRxInvalidCCM,
       "wwpLeosCfmGlobalLoopbackStats": wwpLeosCfmGlobalLoopbackStats,
       "wwpLeosCfmTotalTxLBM": wwpLeosCfmTotalTxLBM,
       "wwpLeosCfmTotalTxLBR": wwpLeosCfmTotalTxLBR,
       "wwpLeosCfmTotalRxInOderLBR": wwpLeosCfmTotalRxInOderLBR,
       "wwpLeosCfmTotalRxOOOLBR": wwpLeosCfmTotalRxOOOLBR,
       "wwpLeosCfmTotalRxContentMismatchLBR": wwpLeosCfmTotalRxContentMismatchLBR,
       "wwpLeosCfmTotalRxUnexpectedLBR": wwpLeosCfmTotalRxUnexpectedLBR,
       "wwpLeosCfmTotalRxInvalidLBR": wwpLeosCfmTotalRxInvalidLBR,
       "wwpLeosCfmTotalRxvalidLBM": wwpLeosCfmTotalRxvalidLBM,
       "wwpLeosCfmTotalRxInvalidLBM": wwpLeosCfmTotalRxInvalidLBM,
       "wwpLeosCfmGlobalLinkTraceStats": wwpLeosCfmGlobalLinkTraceStats,
       "wwpLeosCfmTotalTxLTM": wwpLeosCfmTotalTxLTM,
       "wwpLeosCfmTotalTxLTR": wwpLeosCfmTotalTxLTR,
       "wwpLeosCfmTotalRxValidLTM": wwpLeosCfmTotalRxValidLTM,
       "wwpLeosCfmTotalRxValidLTR": wwpLeosCfmTotalRxValidLTR,
       "wwpLeosCfmTotalRxUnexpectedLTR": wwpLeosCfmTotalRxUnexpectedLTR,
       "wwpLeosCfmTotalRxInvalidLTR": wwpLeosCfmTotalRxInvalidLTR,
       "wwpLeosCfmInvalidLTRRelayAction": wwpLeosCfmInvalidLTRRelayAction,
       "wwpLeosCfmTotalRxInvalidLTM": wwpLeosCfmTotalRxInvalidLTM,
       "wwpLeosCfmRxUnresolvedLTM": wwpLeosCfmRxUnresolvedLTM,
       "wwpLeosCfmGlobalDelayMeasurementStats": wwpLeosCfmGlobalDelayMeasurementStats,
       "wwpLeosCfmTotalTxDMM": wwpLeosCfmTotalTxDMM,
       "wwpLeosCfmTotalTxDMR": wwpLeosCfmTotalTxDMR,
       "wwpLeosCfmTotalRxDMM": wwpLeosCfmTotalRxDMM,
       "wwpLeosCfmTotalRxDMR": wwpLeosCfmTotalRxDMR,
       "wwpLeosCfmGlobalLossMeasurementStats": wwpLeosCfmGlobalLossMeasurementStats,
       "wwpLeosCfmTotalTxLMM": wwpLeosCfmTotalTxLMM,
       "wwpLeosCfmTotalTxLMR": wwpLeosCfmTotalTxLMR,
       "wwpLeosCfmTotalRxLMM": wwpLeosCfmTotalRxLMM,
       "wwpLeosCfmTotalRxLMR": wwpLeosCfmTotalRxLMR,
       "wwpLeosCfmService": wwpLeosCfmService,
       "wwpLeosCfmServiceTable": wwpLeosCfmServiceTable,
       "wwpLeosCfmServiceEntry": wwpLeosCfmServiceEntry,
       "wwpLeosCfmServiceIndex": wwpLeosCfmServiceIndex,
       "wwpLeosCfmServiceType": wwpLeosCfmServiceType,
       "wwpLeosCfmServiceValue": wwpLeosCfmServiceValue,
       "wwpLeosCfmServiceAdminState": wwpLeosCfmServiceAdminState,
       "wwpLeosCfmServiceOperState": wwpLeosCfmServiceOperState,
       "wwpLeosCfmServiceAlarmTime": wwpLeosCfmServiceAlarmTime,
       "wwpLeosCfmServiceCCMInterval": wwpLeosCfmServiceCCMInterval,
       "wwpLeosCfmServiceName": wwpLeosCfmServiceName,
       "wwpLeosCfmServiceMdLevel": wwpLeosCfmServiceMdLevel,
       "wwpLeosCfmServiceResetTime": wwpLeosCfmServiceResetTime,
       "wwpLeosCfmServiceLastFaultCCM": wwpLeosCfmServiceLastFaultCCM,
       "wwpLeosCfmServiceRMEPFailureFlag": wwpLeosCfmServiceRMEPFailureFlag,
       "wwpLeosCfmServiceCCMErrorFlag": wwpLeosCfmServiceCCMErrorFlag,
       "wwpLeosCfmServiceCrossConnectErrorFlag": wwpLeosCfmServiceCrossConnectErrorFlag,
       "wwpLeosCfmServiceNumMEP": wwpLeosCfmServiceNumMEP,
       "wwpLeosCfmServiceNumRemoteMEP": wwpLeosCfmServiceNumRemoteMEP,
       "wwpLeosCfmServiceNumActiveMEP": wwpLeosCfmServiceNumActiveMEP,
       "wwpLeosCfmServiceStatus": wwpLeosCfmServiceStatus,
       "wwpLeosCfmServiceNextMepId": wwpLeosCfmServiceNextMepId,
       "wwpLeosCfmServiceAlarmPriority": wwpLeosCfmServiceAlarmPriority,
       "wwpLeosCfmServiceNumCCMForFault": wwpLeosCfmServiceNumCCMForFault,
       "wwpLeosCfmServiceDMMInterval": wwpLeosCfmServiceDMMInterval,
       "wwpLeosCfmServiceLMMInterval": wwpLeosCfmServiceLMMInterval,
       "wwpLeosCfmServiceCCMLossStatsState": wwpLeosCfmServiceCCMLossStatsState,
       "wwpLeosCfmServiceCCMLossBucketInterval": wwpLeosCfmServiceCCMLossBucketInterval,
       "wwpLeosCfmServiceRemoteMepDiscovery": wwpLeosCfmServiceRemoteMepDiscovery,
       "wwpLeosCfmServiceY1731": wwpLeosCfmServiceY1731,
       "wwpLeosCfmServiceAccelerated": wwpLeosCfmServiceAccelerated,
       "wwpLeosCfmServiceTlvSenderIdType": wwpLeosCfmServiceTlvSenderIdType,
       "wwpLeosCfmServiceRMEPHoldTime": wwpLeosCfmServiceRMEPHoldTime,
       "wwpLeosCfmServiceCCMTxState": wwpLeosCfmServiceCCMTxState,
       "wwpLeosCfmServicePortStatusFlag": wwpLeosCfmServicePortStatusFlag,
       "wwpLeosCfmServiceRDIFlag": wwpLeosCfmServiceRDIFlag,
       "wwpLeosCfmServiceInstabilityFlag": wwpLeosCfmServiceInstabilityFlag,
       "wwpLeosCfmServiceRMEPAging": wwpLeosCfmServiceRMEPAging,
       "wwpLeosCfmServiceDefaultMEPType": wwpLeosCfmServiceDefaultMEPType,
       "wwpLeosCfmServiceMAID": wwpLeosCfmServiceMAID,
       "wwpLeosCfmServiceMdIndex": wwpLeosCfmServiceMdIndex,
       "wwpLeosCfmServiceMaintAssocNameType": wwpLeosCfmServiceMaintAssocNameType,
       "wwpLeosCfmServiceMaintAssocName": wwpLeosCfmServiceMaintAssocName,
       "wwpLeosCfmServiceMulticastDa": wwpLeosCfmServiceMulticastDa,
       "wwpLeosCfmServiceChargedAgainstGlobalFrameBudget": wwpLeosCfmServiceChargedAgainstGlobalFrameBudget,
       "wwpLeosCfmServiceCfmDefaultMEPType": wwpLeosCfmServiceCfmDefaultMEPType,
       "wwpLeosCfmServiceCfmMAID": wwpLeosCfmServiceCfmMAID,
       "wwpLeosCfmServiceCfmMdIndex": wwpLeosCfmServiceCfmMdIndex,
       "wwpLeosCfmServiceCfmMaintAssocNameType": wwpLeosCfmServiceCfmMaintAssocNameType,
       "wwpLeosCfmServiceCfmMaintAssocName": wwpLeosCfmServiceCfmMaintAssocName,
       "wwpLeosCfmServiceCfmControlModuleFrameBudget": wwpLeosCfmServiceCfmControlModuleFrameBudget,
       "wwpLeosCfmServiceFaultTable": wwpLeosCfmServiceFaultTable,
       "wwpLeosCfmServiceFaultEntry": wwpLeosCfmServiceFaultEntry,
       "wwpLeosCfmServiceFaultTime": wwpLeosCfmServiceFaultTime,
       "wwpLeosCfmServiceFaultType": wwpLeosCfmServiceFaultType,
       "wwpLeosCfmServiceFaultDesc": wwpLeosCfmServiceFaultDesc,
       "wwpLeosCfmServiceFaultMep": wwpLeosCfmServiceFaultMep,
       "wwpLeosCfmServiceVlan": wwpLeosCfmServiceVlan,
       "wwpLeosCfmServiceVsPbtName": wwpLeosCfmServiceVsPbtName,
       "wwpLeosCfmServiceStatisticsTable": wwpLeosCfmServiceStatisticsTable,
       "wwpLeosCfmServiceStatisticsEntry": wwpLeosCfmServiceStatisticsEntry,
       "wwpLeosCfmServiceRxTotalValidFrames": wwpLeosCfmServiceRxTotalValidFrames,
       "wwpLeosCfmServiceRxTotalInvalidFrames": wwpLeosCfmServiceRxTotalInvalidFrames,
       "wwpLeosCfmServiceInvalidMessageOverflow": wwpLeosCfmServiceInvalidMessageOverflow,
       "wwpLeosCfmServiceInvalidPortStatusTLV": wwpLeosCfmServiceInvalidPortStatusTLV,
       "wwpLeosCfmServiceInvalidInterfaceStatusTLV": wwpLeosCfmServiceInvalidInterfaceStatusTLV,
       "wwpLeosCfmServiceInvalidSenderIDTLV": wwpLeosCfmServiceInvalidSenderIDTLV,
       "wwpLeosCfmServiceTxTotalCCM": wwpLeosCfmServiceTxTotalCCM,
       "wwpLeosCfmServiceTotalRxValidCCM": wwpLeosCfmServiceTotalRxValidCCM,
       "wwpLeosCfmServiceTotalRxInSequenceCCM": wwpLeosCfmServiceTotalRxInSequenceCCM,
       "wwpLeosCfmServiceTotalRxNotInSequenceCCM": wwpLeosCfmServiceTotalRxNotInSequenceCCM,
       "wwpLeosCfmServiceTotalRxMDLevelXconCCM": wwpLeosCfmServiceTotalRxMDLevelXconCCM,
       "wwpLeosCfmServiceTotalRxMAIDXconCCM": wwpLeosCfmServiceTotalRxMAIDXconCCM,
       "wwpLeosCfmServiceTotalRxMEPIDErrorCCM": wwpLeosCfmServiceTotalRxMEPIDErrorCCM,
       "wwpLeosCfmServiceTotalRxCCMIntervalErrorCCM": wwpLeosCfmServiceTotalRxCCMIntervalErrorCCM,
       "wwpLeosCfmServiceTotalRxInvalidCCM": wwpLeosCfmServiceTotalRxInvalidCCM,
       "wwpLeosCfmServiceTotalTxLTM": wwpLeosCfmServiceTotalTxLTM,
       "wwpLeosCfmServiceTotalTxLTR": wwpLeosCfmServiceTotalTxLTR,
       "wwpLeosCfmServiceTotalRxValidLTR": wwpLeosCfmServiceTotalRxValidLTR,
       "wwpLeosCfmServiceTotalRxUnexpectedLTR": wwpLeosCfmServiceTotalRxUnexpectedLTR,
       "wwpLeosCfmServiceTotalRxInvalidLTR": wwpLeosCfmServiceTotalRxInvalidLTR,
       "wwpLeosCfmServiceTotalRxInvalidRelayActionLTR": wwpLeosCfmServiceTotalRxInvalidRelayActionLTR,
       "wwpLeosCfmServiceTotalRxValidLTM": wwpLeosCfmServiceTotalRxValidLTM,
       "wwpLeosCfmServiceTotalTxInvalidLTM": wwpLeosCfmServiceTotalTxInvalidLTM,
       "wwpLeosCfmServiceTotalTxLBM": wwpLeosCfmServiceTotalTxLBM,
       "wwpLeosCfmServiceTotalTxLBR": wwpLeosCfmServiceTotalTxLBR,
       "wwpLeosCfmServiceTotalRxInorderLBR": wwpLeosCfmServiceTotalRxInorderLBR,
       "wwpLeosCfmServiceTotalRxOutOfOrderLBR": wwpLeosCfmServiceTotalRxOutOfOrderLBR,
       "wwpLeosCfmServiceTotalRxContentMismatchLBR": wwpLeosCfmServiceTotalRxContentMismatchLBR,
       "wwpLeosCfmServiceTotalRxUnexpectedLBR": wwpLeosCfmServiceTotalRxUnexpectedLBR,
       "wwpLeosCfmServiceTotalRxInvalidLBR": wwpLeosCfmServiceTotalRxInvalidLBR,
       "wwpLeosCfmServiceTotalRxValidLBM": wwpLeosCfmServiceTotalRxValidLBM,
       "wwpLeosCfmServiceTotalRxInvalidLBM": wwpLeosCfmServiceTotalRxInvalidLBM,
       "wwpLeosCfmServiceTotalTxDMM": wwpLeosCfmServiceTotalTxDMM,
       "wwpLeosCfmServiceTotalTxDMR": wwpLeosCfmServiceTotalTxDMR,
       "wwpLeosCfmServiceTotalRxDMM": wwpLeosCfmServiceTotalRxDMM,
       "wwpLeosCfmServiceTotalRxDMR": wwpLeosCfmServiceTotalRxDMR,
       "wwpLeosCfmServiceTotalTxLMM": wwpLeosCfmServiceTotalTxLMM,
       "wwpLeosCfmServiceTotalTxLMR": wwpLeosCfmServiceTotalTxLMR,
       "wwpLeosCfmServiceTotalRxLMM": wwpLeosCfmServiceTotalRxLMM,
       "wwpLeosCfmServiceTotalRxLMR": wwpLeosCfmServiceTotalRxLMR,
       "wwpLeosCfmServiceStatsClear": wwpLeosCfmServiceStatsClear,
       "wwpLeosCfmServiceClearStats": wwpLeosCfmServiceClearStats,
       "wwpLeosCfmMIP": wwpLeosCfmMIP,
       "wwpLeosCfmMipTable": wwpLeosCfmMipTable,
       "wwpLeosCfmMipEntry": wwpLeosCfmMipEntry,
       "wwpLeosCfmMipVid": wwpLeosCfmMipVid,
       "wwpLeosCfmMipPort": wwpLeosCfmMipPort,
       "wwpLeosCfmMipLevel": wwpLeosCfmMipLevel,
       "wwpLeosCfmMipStatus": wwpLeosCfmMipStatus,
       "wwpLeosCfmLinkTrace": wwpLeosCfmLinkTrace,
       "wwpLeosCfmLinkTraceMsgTable": wwpLeosCfmLinkTraceMsgTable,
       "wwpLeosCfmLinkTraceMsgEntry": wwpLeosCfmLinkTraceMsgEntry,
       "wwpLeosCfmLinkTraceMsgPortId": wwpLeosCfmLinkTraceMsgPortId,
       "wwpLeosCfmLinkTraceMsgTargetMEPID": wwpLeosCfmLinkTraceMsgTargetMEPID,
       "wwpLeosCfmLinkTraceMsgTargetMacAddr": wwpLeosCfmLinkTraceMsgTargetMacAddr,
       "wwpLeosCfmLinkTraceMsgTTL": wwpLeosCfmLinkTraceMsgTTL,
       "wwpLeosCfmLinkTraceMsgSequenceNumber": wwpLeosCfmLinkTraceMsgSequenceNumber,
       "wwpLeosCfmLinkTraceMsgRowStatus": wwpLeosCfmLinkTraceMsgRowStatus,
       "wwpLeosCfmLinkTraceMsgPriority": wwpLeosCfmLinkTraceMsgPriority,
       "wwpLeosCfmLinkTraceMsgServiceName": wwpLeosCfmLinkTraceMsgServiceName,
       "wwpLeosCfmLinkTraceMsgSubPortName": wwpLeosCfmLinkTraceMsgSubPortName,
       "wwpLeosCfmLinkTraceMsgVsIndex": wwpLeosCfmLinkTraceMsgVsIndex,
       "wwpLeosCfmLinkTraceMsgTotalTxLtm": wwpLeosCfmLinkTraceMsgTotalTxLtm,
       "wwpLeosCfmLinkTraceMsgTotalRxLtr": wwpLeosCfmLinkTraceMsgTotalRxLtr,
       "wwpLeosCfmLinkTraceMsgReplyTable": wwpLeosCfmLinkTraceMsgReplyTable,
       "wwpLeosCfmLinkTraceMsgReplyEntry": wwpLeosCfmLinkTraceMsgReplyEntry,
       "wwpLeosCfmLinkTraceMsgReplyTTL": wwpLeosCfmLinkTraceMsgReplyTTL,
       "wwpLeosCfmLinkTraceMsgReplyTTLIndex": wwpLeosCfmLinkTraceMsgReplyTTLIndex,
       "wwpLeosCfmLinkTraceMsgReplySequenceNumber": wwpLeosCfmLinkTraceMsgReplySequenceNumber,
       "wwpLeosCfmLinkTraceMsgReplyMPMacAddr": wwpLeosCfmLinkTraceMsgReplyMPMacAddr,
       "wwpLeosCfmLinkTraceMsgReplyMEPID": wwpLeosCfmLinkTraceMsgReplyMEPID,
       "wwpLeosCfmLinkTraceMsgReplyTargetMacAddr": wwpLeosCfmLinkTraceMsgReplyTargetMacAddr,
       "wwpLeosCfmLinkTraceMsgReplyRelayAction": wwpLeosCfmLinkTraceMsgReplyRelayAction,
       "wwpLeosCfmLinkTraceMsgReplyIngressPort": wwpLeosCfmLinkTraceMsgReplyIngressPort,
       "wwpLeosCfmLinkTraceMsgReplyIngressAction": wwpLeosCfmLinkTraceMsgReplyIngressAction,
       "wwpLeosCfmLinkTraceMsgReplyEgressPort": wwpLeosCfmLinkTraceMsgReplyEgressPort,
       "wwpLeosCfmLinkTraceMsgReplyEgressAction": wwpLeosCfmLinkTraceMsgReplyEgressAction,
       "wwpLeosCfmLinkTraceMsgReplyIngressPortStr": wwpLeosCfmLinkTraceMsgReplyIngressPortStr,
       "wwpLeosCfmLinkTraceMsgReplyEgressPortStr": wwpLeosCfmLinkTraceMsgReplyEgressPortStr,
       "wwpLeosCfmLinkTraceMsgReplyIngressMacAddr": wwpLeosCfmLinkTraceMsgReplyIngressMacAddr,
       "wwpLeosCfmLinkTraceMsgReplyEgressMacAddr": wwpLeosCfmLinkTraceMsgReplyEgressMacAddr,
       "wwpLeosCfmLoopback": wwpLeosCfmLoopback,
       "wwpLeosCfmLoopbackMsgTable": wwpLeosCfmLoopbackMsgTable,
       "wwpLeosCfmLoopbackMsgEntry": wwpLeosCfmLoopbackMsgEntry,
       "wwpLeosCfmLoopbackMsgPortId": wwpLeosCfmLoopbackMsgPortId,
       "wwpLeosCfmLoopbackMsgTargetMEPID": wwpLeosCfmLoopbackMsgTargetMEPID,
       "wwpLeosCfmLoopbackMsgTargetMacAddr": wwpLeosCfmLoopbackMsgTargetMacAddr,
       "wwpLeosCfmLoopbackMsgCount": wwpLeosCfmLoopbackMsgCount,
       "wwpLeosCfmLoopbackMsgData": wwpLeosCfmLoopbackMsgData,
       "wwpLeosCfmLoopbackMsgPriority": wwpLeosCfmLoopbackMsgPriority,
       "wwpLeosCfmLoopbackMsgRowStatus": wwpLeosCfmLoopbackMsgRowStatus,
       "wwpLeosCfmLoopbackMsgDefaultInterval": wwpLeosCfmLoopbackMsgDefaultInterval,
       "wwpLeosCfmLoopbackMsgDefaultTimeout": wwpLeosCfmLoopbackMsgDefaultTimeout,
       "wwpLeosCfmMaintenance": wwpLeosCfmMaintenance,
       "wwpLeosCfmMaintenanceDomainTable": wwpLeosCfmMaintenanceDomainTable,
       "wwpLeosCfmMaintenanceDomainEntry": wwpLeosCfmMaintenanceDomainEntry,
       "wwpLeosCfmMaintenanceDomainIndex": wwpLeosCfmMaintenanceDomainIndex,
       "wwpLeosCfmMaintenanceDomainLevel": wwpLeosCfmMaintenanceDomainLevel,
       "wwpLeosCfmMaintenanceDomainName": wwpLeosCfmMaintenanceDomainName,
       "wwpLeosCfmMaintenanceDomainServiceCount": wwpLeosCfmMaintenanceDomainServiceCount,
       "wwpLeosCfmMaintenanceDomainMdFormat": wwpLeosCfmMaintenanceDomainMdFormat,
       "wwpLeosCfmMaintenanceDomainMdName": wwpLeosCfmMaintenanceDomainMdName,
       "wwpLeosCfmMaintenanceDomainStatus": wwpLeosCfmMaintenanceDomainStatus,
       "wwpLeosCfmMEP": wwpLeosCfmMEP,
       "wwpLeosCfmMEPTable": wwpLeosCfmMEPTable,
       "wwpLeosCfmMEPEntry": wwpLeosCfmMEPEntry,
       "wwpLeosCfmMEPPort": wwpLeosCfmMEPPort,
       "wwpLeosCfmMEPAdminState": wwpLeosCfmMEPAdminState,
       "wwpLeosCfmMEPOperState": wwpLeosCfmMEPOperState,
       "wwpLeosCfmMEPDirection": wwpLeosCfmMEPDirection,
       "wwpLeosCfmMEPCCMState": wwpLeosCfmMEPCCMState,
       "wwpLeosCfmMEPCCMPriority": wwpLeosCfmMEPCCMPriority,
       "wwpLeosCfmMEPLTMPriority": wwpLeosCfmMEPLTMPriority,
       "wwpLeosCfmMEPId": wwpLeosCfmMEPId,
       "wwpLeosCfmMEPMacAddr": wwpLeosCfmMEPMacAddr,
       "wwpLeosCfmMEPNextLbmSeqNumber": wwpLeosCfmMEPNextLbmSeqNumber,
       "wwpLeosCfmMEPRxValidInOrderLoopbackReply": wwpLeosCfmMEPRxValidInOrderLoopbackReply,
       "wwpLeosCfmMEPRxValidOutOrderLoopbackReply": wwpLeosCfmMEPRxValidOutOrderLoopbackReply,
       "wwpLeosCfmMEPNextLTMSeqNumber": wwpLeosCfmMEPNextLTMSeqNumber,
       "wwpLeosCfmMEPNumLoopbackRepliesTxmt": wwpLeosCfmMEPNumLoopbackRepliesTxmt,
       "wwpLeosCfmMEPNumLTMReceived": wwpLeosCfmMEPNumLTMReceived,
       "wwpLeosCfmMEPNumLTMTxmt": wwpLeosCfmMEPNumLTMTxmt,
       "wwpLeosCfmMEPNumCCMTxmt": wwpLeosCfmMEPNumCCMTxmt,
       "wwpLeosCfmMEPRowStatus": wwpLeosCfmMEPRowStatus,
       "wwpLeosCfmMEPNumDMMSent": wwpLeosCfmMEPNumDMMSent,
       "wwpLeosCfmMEPDMMDelay": wwpLeosCfmMEPDMMDelay,
       "wwpLeosCfmMEPDMMJitter": wwpLeosCfmMEPDMMJitter,
       "wwpLeosCfmMEPNumLMMSent": wwpLeosCfmMEPNumLMMSent,
       "wwpLeosCfmMEPLMMFrameLossNear": wwpLeosCfmMEPLMMFrameLossNear,
       "wwpLeosCfmMEPLMMFrameLossFar": wwpLeosCfmMEPLMMFrameLossFar,
       "wwpLeosCfmMEPNumLMRReceived": wwpLeosCfmMEPNumLMRReceived,
       "wwpLeosCfmMEPNumDMRReceived": wwpLeosCfmMEPNumDMRReceived,
       "wwpLeosCfmMEPDMMMinDelay": wwpLeosCfmMEPDMMMinDelay,
       "wwpLeosCfmMEPDMMMaxDelay": wwpLeosCfmMEPDMMMaxDelay,
       "wwpLeosCfmMEPDMMMinJitter": wwpLeosCfmMEPDMMMinJitter,
       "wwpLeosCfmMEPDMMMaxJitter": wwpLeosCfmMEPDMMMaxJitter,
       "wwpLeosCfmMEPServiceName": wwpLeosCfmMEPServiceName,
       "wwpLeosCfmMEPSubPortName": wwpLeosCfmMEPSubPortName,
       "wwpLeosCfmMEPVsPbtName": wwpLeosCfmMEPVsPbtName,
       "wwpLeosCfmMEPLogicalPortName": wwpLeosCfmMEPLogicalPortName,
       "wwpLeosCfmMEPSubPortIndex": wwpLeosCfmMEPSubPortIndex,
       "wwpLeosCfmMEPEncapsulation": wwpLeosCfmMEPEncapsulation,
       "wwpLeosCfmMEPLeadPortBayIndex": wwpLeosCfmMEPLeadPortBayIndex,
       "wwpLeosCfmMEPLeadPortShelfIndex": wwpLeosCfmMEPLeadPortShelfIndex,
       "wwpLeosCfmMEPLeadPortModuleIndex": wwpLeosCfmMEPLeadPortModuleIndex,
       "wwpLeosCfmMEPPBTBvid": wwpLeosCfmMEPPBTBvid,
       "wwpLeosCfmMEPPBTEtype": wwpLeosCfmMEPPBTEtype,
       "wwpLeosCfmMEPNumLbmTxmt": wwpLeosCfmMEPNumLbmTxmt,
       "wwpLeosCfmMEPNumLbmReceived": wwpLeosCfmMEPNumLbmReceived,
       "wwpLeosCfmMEPNumLoopbackRepliesReceived": wwpLeosCfmMEPNumLoopbackRepliesReceived,
       "wwpLeosCfmMEPNumLTRepliesTxmt": wwpLeosCfmMEPNumLTRepliesTxmt,
       "wwpLeosCfmMEPNumLTRepliesReceived": wwpLeosCfmMEPNumLTRepliesReceived,
       "wwpLeosCfmMEPNumUnexpectedLTRepliesReceived": wwpLeosCfmMEPNumUnexpectedLTRepliesReceived,
       "wwpLeosCfmMEPNumCCMReceived": wwpLeosCfmMEPNumCCMReceived,
       "wwpLeosCfmRemoteMEP": wwpLeosCfmRemoteMEP,
       "wwpLeosCfmRemoteMEPTable": wwpLeosCfmRemoteMEPTable,
       "wwpLeosCfmRemoteMEPEntry": wwpLeosCfmRemoteMEPEntry,
       "wwpLeosCfmRemoteMEPID": wwpLeosCfmRemoteMEPID,
       "wwpLeosCfmRemoteMEPAdminState": wwpLeosCfmRemoteMEPAdminState,
       "wwpLeosCfmRemoteMEPOperState": wwpLeosCfmRemoteMEPOperState,
       "wwpLeosCfmRemoteMEPTime": wwpLeosCfmRemoteMEPTime,
       "wwpLeosCfmRemoteMEPMacAddr": wwpLeosCfmRemoteMEPMacAddr,
       "wwpLeosCfmRemoteMEPKLastMacStatus": wwpLeosCfmRemoteMEPKLastMacStatus,
       "wwpLeosCfmRemoteMEPFailureFlag": wwpLeosCfmRemoteMEPFailureFlag,
       "wwpLeosCfmRemoteMEPCCMErrorFlag": wwpLeosCfmRemoteMEPCCMErrorFlag,
       "wwpLeosCfmRemoteMEPRDIErrorFlag": wwpLeosCfmRemoteMEPRDIErrorFlag,
       "wwpLeosCfmRemoteMEPNumCCMRx": wwpLeosCfmRemoteMEPNumCCMRx,
       "wwpLeosCfmRemoteMEPNumDMMSent": wwpLeosCfmRemoteMEPNumDMMSent,
       "wwpLeosCfmRemoteMEPDelay": wwpLeosCfmRemoteMEPDelay,
       "wwpLeosCfmRemoteMEPJitter": wwpLeosCfmRemoteMEPJitter,
       "wwpLeosCfmRemoteMEPNumLMMSent": wwpLeosCfmRemoteMEPNumLMMSent,
       "wwpLeosCfmRemoteMEPFrameLossNear": wwpLeosCfmRemoteMEPFrameLossNear,
       "wwpLeosCfmRemoteMEPFrameLossFar": wwpLeosCfmRemoteMEPFrameLossFar,
       "wwpLeosCfmRemoteMEPNumLMRReceived": wwpLeosCfmRemoteMEPNumLMRReceived,
       "wwpLeosCfmRemoteMEPNumCCMLost": wwpLeosCfmRemoteMEPNumCCMLost,
       "wwpLeosCfmRemoteMEPNumDMRReceived": wwpLeosCfmRemoteMEPNumDMRReceived,
       "wwpLeosCfmRemoteMEPHoldState": wwpLeosCfmRemoteMEPHoldState,
       "wwpLeosCfmRemoteMEPRowStatus": wwpLeosCfmRemoteMEPRowStatus,
       "wwpLeosCfmRemoteMEPCCMComment": wwpLeosCfmRemoteMEPCCMComment,
       "wwpLeosCfmRemoteMEPBadSequence": wwpLeosCfmRemoteMEPBadSequence,
       "wwpLeosCfmRemoteMEPMinDelay": wwpLeosCfmRemoteMEPMinDelay,
       "wwpLeosCfmRemoteMEPMaxDelay": wwpLeosCfmRemoteMEPMaxDelay,
       "wwpLeosCfmRemoteMEPMinJitter": wwpLeosCfmRemoteMEPMinJitter,
       "wwpLeosCfmRemoteMEPMaxJitter": wwpLeosCfmRemoteMEPMaxJitter,
       "wwpLeosCfmRemoteCfmMEPHoldState": wwpLeosCfmRemoteCfmMEPHoldState,
       "wwpLeosCfmRemoteMEPServiceClear": wwpLeosCfmRemoteMEPServiceClear,
       "wwpLeosCfmRemoteMEPServiceStatisticsClear": wwpLeosCfmRemoteMEPServiceStatisticsClear,
       "wwpLeosCfmRemoteMEPAccelerated": wwpLeosCfmRemoteMEPAccelerated,
       "wwpLeosCfmRemoteMEPSubPortName": wwpLeosCfmRemoteMEPSubPortName,
       "wwpLeosCfmRemoteMEPServiceName": wwpLeosCfmRemoteMEPServiceName,
       "wwpLeosCfmRemoteMEPBayIndex": wwpLeosCfmRemoteMEPBayIndex,
       "wwpLeosCfmRemoteMEPShelfIndex": wwpLeosCfmRemoteMEPShelfIndex,
       "wwpLeosCfmRemoteMEPModuleIndex": wwpLeosCfmRemoteMEPModuleIndex,
       "wwpLeosCfmRemoteMEPPreviousBayIndex": wwpLeosCfmRemoteMEPPreviousBayIndex,
       "wwpLeosCfmRemoteMEPPreviousShelfIndex": wwpLeosCfmRemoteMEPPreviousShelfIndex,
       "wwpLeosCfmRemoteMEPPreviousModuleIndex": wwpLeosCfmRemoteMEPPreviousModuleIndex,
       "wwpLeosCfmRemoteMEPLastPortStatus": wwpLeosCfmRemoteMEPLastPortStatus,
       "wwpLeosCfmRemoteMEPLastInterfaceStatus": wwpLeosCfmRemoteMEPLastInterfaceStatus,
       "wwpLeosCfmRemoteMEPLastSeqNum": wwpLeosCfmRemoteMEPLastSeqNum,
       "wwpLeosCfmRemoteMEPCCMSeqErrors": wwpLeosCfmRemoteMEPCCMSeqErrors,
       "wwpLeosCfmRemoteMEPCCMLevel": wwpLeosCfmRemoteMEPCCMLevel,
       "wwpLeosCfmRemoteMEPDeleteAll": wwpLeosCfmRemoteMEPDeleteAll,
       "wwpLeosCfmStack": wwpLeosCfmStack,
       "wwpLeosCfmPortStackTable": wwpLeosCfmPortStackTable,
       "wwpLeosCfmPortStackEntry": wwpLeosCfmPortStackEntry,
       "wwpLeosCfmPortStackPort": wwpLeosCfmPortStackPort,
       "wwpLeosCfmPortStackVid": wwpLeosCfmPortStackVid,
       "wwpLeosCfmPortStackType": wwpLeosCfmPortStackType,
       "wwpLeosCfmPortStackLevel": wwpLeosCfmPortStackLevel,
       "wwpLeosCfmPortStackMEPId": wwpLeosCfmPortStackMEPId,
       "wwpLeosCfmMipCCMDb": wwpLeosCfmMipCCMDb,
       "wwpLeosCfmMipCCMDbTable": wwpLeosCfmMipCCMDbTable,
       "wwpLeosCfmMipCCMDbEntry": wwpLeosCfmMipCCMDbEntry,
       "wwpLeosCfmMipCCMDbIndex": wwpLeosCfmMipCCMDbIndex,
       "wwpLeosCfmMipCCMDbVid": wwpLeosCfmMipCCMDbVid,
       "wwpLeosCfmMipCCMDbMacAddr": wwpLeosCfmMipCCMDbMacAddr,
       "wwpLeosCfmMipCCMDbPort": wwpLeosCfmMipCCMDbPort,
       "wwpLeosCfmMipCCMDbMEPID": wwpLeosCfmMipCCMDbMEPID,
       "wwpLeosCfmMipCCMdbNumCCMRx": wwpLeosCfmMipCCMdbNumCCMRx,
       "wwpLeosCfmMipCCMDbTime": wwpLeosCfmMipCCMDbTime,
       "wwpLeosCfmMipCCMDbLastMacStatus": wwpLeosCfmMipCCMDbLastMacStatus,
       "wwpLeosCfmMipCCMDbRDIErrorFlag": wwpLeosCfmMipCCMDbRDIErrorFlag,
       "wwpLeosCfmFaultNotif": wwpLeosCfmFaultNotif,
       "wwpLeosCfmFaultTrapState": wwpLeosCfmFaultTrapState,
       "wwpLeosCfmDelay": wwpLeosCfmDelay,
       "wwpLeosCfmDelayMsgTable": wwpLeosCfmDelayMsgTable,
       "wwpLeosCfmDelayMsgEntry": wwpLeosCfmDelayMsgEntry,
       "wwpLeosCfmDelayMsgPortId": wwpLeosCfmDelayMsgPortId,
       "wwpLeosCfmDelayMsgTargetMEPID": wwpLeosCfmDelayMsgTargetMEPID,
       "wwpLeosCfmDelayMsgTargetMacAddr": wwpLeosCfmDelayMsgTargetMacAddr,
       "wwpLeosCfmDelayMsgCount": wwpLeosCfmDelayMsgCount,
       "wwpLeosCfmDelayMsgPriority": wwpLeosCfmDelayMsgPriority,
       "wwpLeosCfmDelayMsgRowStatus": wwpLeosCfmDelayMsgRowStatus,
       "wwpLeosCfmDelayMsgRepeat": wwpLeosCfmDelayMsgRepeat,
       "wwpLeosCfmDelayMsgRepeatCount": wwpLeosCfmDelayMsgRepeatCount,
       "wwpLeosCfmDelayMsgDelayThreshold": wwpLeosCfmDelayMsgDelayThreshold,
       "wwpLeosCfmDelayMsgJitterThreshold": wwpLeosCfmDelayMsgJitterThreshold,
       "wwpLeosCfmDelayMsgMaxDelayThreshold": wwpLeosCfmDelayMsgMaxDelayThreshold,
       "wwpLeosCfmDelayMsgMaxJitterThreshold": wwpLeosCfmDelayMsgMaxJitterThreshold,
       "wwpLeosCfmFrameLoss": wwpLeosCfmFrameLoss,
       "wwpLeosCfmFrameLossMsgTable": wwpLeosCfmFrameLossMsgTable,
       "wwpLeosCfmFrameLossMsgEntry": wwpLeosCfmFrameLossMsgEntry,
       "wwpLeosCfmFrameLossMsgPortId": wwpLeosCfmFrameLossMsgPortId,
       "wwpLeosCfmFrameLossMsgTargetMEPID": wwpLeosCfmFrameLossMsgTargetMEPID,
       "wwpLeosCfmFrameLossMsgTargetMacAddr": wwpLeosCfmFrameLossMsgTargetMacAddr,
       "wwpLeosCfmFrameLossMsgCount": wwpLeosCfmFrameLossMsgCount,
       "wwpLeosCfmFrameLossMsgPriority": wwpLeosCfmFrameLossMsgPriority,
       "wwpLeosCfmFrameLossMsgRowStatus": wwpLeosCfmFrameLossMsgRowStatus,
       "wwpLeosCfmFrameLossMsgRepeat": wwpLeosCfmFrameLossMsgRepeat,
       "wwpLeosCfmFrameLossMsgRepeatCount": wwpLeosCfmFrameLossMsgRepeatCount,
       "wwpLeosCfmFrameLossMsgFlnThreshold": wwpLeosCfmFrameLossMsgFlnThreshold,
       "wwpLeosCfmFrameLossMsgFlfThreshold": wwpLeosCfmFrameLossMsgFlfThreshold,
       "wwpLeosCfmRemoteMEPCCMLoss": wwpLeosCfmRemoteMEPCCMLoss,
       "wwpLeosCfmRemoteMEPCCMLossTable": wwpLeosCfmRemoteMEPCCMLossTable,
       "wwpLeosCfmRemoteMEPCCMLossEntry": wwpLeosCfmRemoteMEPCCMLossEntry,
       "wwpLeosCfmRemoteMEPCCMLossNum": wwpLeosCfmRemoteMEPCCMLossNum,
       "wwpLeosCfmRemoteMEPCCMLossCount": wwpLeosCfmRemoteMEPCCMLossCount,
       "wwpLeosCfmExtStack": wwpLeosCfmExtStack,
       "wwpLeosCfmExtPortStackTable": wwpLeosCfmExtPortStackTable,
       "wwpLeosCfmExtPortStackEntry": wwpLeosCfmExtPortStackEntry,
       "wwpLeosCfmExtPortStackVid": wwpLeosCfmExtPortStackVid,
       "wwpLeosCfmExtPortStackPort": wwpLeosCfmExtPortStackPort,
       "wwpLeosCfmExtPortStackType": wwpLeosCfmExtPortStackType,
       "wwpLeosCfmExtPortStackLevel": wwpLeosCfmExtPortStackLevel,
       "wwpLeosCfmExtPortStackMEPId": wwpLeosCfmExtPortStackMEPId,
       "wwpLeosCfmServiceFrameBudget": wwpLeosCfmServiceFrameBudget,
       "wwpLeosCfmServiceFrameBudgetTable": wwpLeosCfmServiceFrameBudgetTable,
       "wwpLeosCfmServiceFrameBudgetEntry": wwpLeosCfmServiceFrameBudgetEntry,
       "wwpLeosCfmSlotIndex": wwpLeosCfmSlotIndex,
       "wwpLeosCfmServiceFrameBudgetSlot": wwpLeosCfmServiceFrameBudgetSlot,
       "wwpLeosTceCfmMIBObj": wwpLeosTceCfmMIBObj,
       "wwpLeosTceCfmMIP": wwpLeosTceCfmMIP,
       "wwpLeosTceCfmMipTable": wwpLeosTceCfmMipTable,
       "wwpLeosTceCfmMipEntry": wwpLeosTceCfmMipEntry,
       "wwpLeosTceCfmMipLiType": wwpLeosTceCfmMipLiType,
       "wwpLeosTceCfmMipLiIndex": wwpLeosTceCfmMipLiIndex,
       "wwpLeosTceCfmMipPgid": wwpLeosTceCfmMipPgid,
       "wwpLeosTceCfmMipBayIndex": wwpLeosTceCfmMipBayIndex,
       "wwpLeosTceCfmMipShelfIndex": wwpLeosTceCfmMipShelfIndex,
       "wwpLeosTceCfmMipModuleIndex": wwpLeosTceCfmMipModuleIndex,
       "wwpLeosTceCfmMipMacAddr": wwpLeosTceCfmMipMacAddr,
       "wwpLeosTceCfmMipLevel": wwpLeosTceCfmMipLevel,
       "wwpLeosTceCfmMipStatus": wwpLeosTceCfmMipStatus,
       "wwpLeosTceCfmMipLiName": wwpLeosTceCfmMipLiName,
       "wwpLeosTceCfmLoopback": wwpLeosTceCfmLoopback,
       "wwpLeosTceCfmLoopbackMsgTable": wwpLeosTceCfmLoopbackMsgTable,
       "wwpLeosTceCfmLoopbackMsgEntry": wwpLeosTceCfmLoopbackMsgEntry,
       "wwpLeosTceCfmLoopbackMsgLocalMEPID": wwpLeosTceCfmLoopbackMsgLocalMEPID,
       "wwpLeosTceCfmLoopbackMsgTargetMEPID": wwpLeosTceCfmLoopbackMsgTargetMEPID,
       "wwpLeosTceCfmLoopbackMsgTargetMacAddr": wwpLeosTceCfmLoopbackMsgTargetMacAddr,
       "wwpLeosTceCfmLoopbackMsgCount": wwpLeosTceCfmLoopbackMsgCount,
       "wwpLeosTceCfmLoopbackMsgData": wwpLeosTceCfmLoopbackMsgData,
       "wwpLeosTceCfmLoopbackMsgPriority": wwpLeosTceCfmLoopbackMsgPriority,
       "wwpLeosTceCfmLoopbackMsgServiceName": wwpLeosTceCfmLoopbackMsgServiceName,
       "wwpLeosTceCfmLoopbackMsgSubPortName": wwpLeosTceCfmLoopbackMsgSubPortName,
       "wwpLeosTceCfmLoopbackMsgNextLbmTransId": wwpLeosTceCfmLoopbackMsgNextLbmTransId,
       "wwpLeosTceCfmLoopbackMsgTotalTxLbm": wwpLeosTceCfmLoopbackMsgTotalTxLbm,
       "wwpLeosTceCfmLoopbackMsgTotalRxLbrIo": wwpLeosTceCfmLoopbackMsgTotalRxLbrIo,
       "wwpLeosTceCfmLoopbackMsgTotalRxLbrOoo": wwpLeosTceCfmLoopbackMsgTotalRxLbrOoo,
       "wwpLeosTceCfmLoopbackMsgRowStatus": wwpLeosTceCfmLoopbackMsgRowStatus,
       "wwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch": wwpLeosTceCfmLoopbackMsgTotalRxLbrContentMismatch,
       "wwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected": wwpLeosTceCfmLoopbackMsgTotalRxLbrUnexpected,
       "wwpLeosTceCfmStack": wwpLeosTceCfmStack,
       "wwpLeosTceCfmPortStackTable": wwpLeosTceCfmPortStackTable,
       "wwpLeosTceCfmPortStackEntry": wwpLeosTceCfmPortStackEntry,
       "wwpLeosTceCfmPortStackServiceType": wwpLeosTceCfmPortStackServiceType,
       "wwpLeosTceCfmPortStackServiceIndex": wwpLeosTceCfmPortStackServiceIndex,
       "wwpLeosTceCfmPortStackSubPortType": wwpLeosTceCfmPortStackSubPortType,
       "wwpLeosTceCfmPortStackSubPortIndex": wwpLeosTceCfmPortStackSubPortIndex,
       "wwpLeosTceCfmPortStackSubPortName": wwpLeosTceCfmPortStackSubPortName,
       "wwpLeosTceCfmPortStackOperState": wwpLeosTceCfmPortStackOperState,
       "wwpLeosTceCfmPortStackPgid": wwpLeosTceCfmPortStackPgid,
       "wwpLeosTceCfmPortStackBayIndex": wwpLeosTceCfmPortStackBayIndex,
       "wwpLeosTceCfmPortStackShelfIndex": wwpLeosTceCfmPortStackShelfIndex,
       "wwpLeosTceCfmPortStackModuleIndex": wwpLeosTceCfmPortStackModuleIndex,
       "wwpLeosTceCfmPortStackVsPbtName": wwpLeosTceCfmPortStackVsPbtName,
       "wwpLeosTceCfmPortStackEgressXformTagValue1": wwpLeosTceCfmPortStackEgressXformTagValue1,
       "wwpLeosTceCfmPortStackEgressXformTagPriority1": wwpLeosTceCfmPortStackEgressXformTagPriority1,
       "wwpLeosTceCfmPortStackEgressXformTagEtype1": wwpLeosTceCfmPortStackEgressXformTagEtype1,
       "wwpLeosTceCfmPortStackEgressXformTagValue2": wwpLeosTceCfmPortStackEgressXformTagValue2,
       "wwpLeosTceCfmPortStackEgressXformTagPriority2": wwpLeosTceCfmPortStackEgressXformTagPriority2,
       "wwpLeosTceCfmPortStackEgressXformTagEtype2": wwpLeosTceCfmPortStackEgressXformTagEtype2,
       "wwpLeosTceCfmPortStackMepCount": wwpLeosTceCfmPortStackMepCount,
       "wwpLeosTceCfmPortStackMipLevel": wwpLeosTceCfmPortStackMipLevel,
       "wwpLeosTceCfmMEP": wwpLeosTceCfmMEP,
       "wwpLeosTceCfmMEPTable": wwpLeosTceCfmMEPTable,
       "wwpLeosTceCfmMEPEntry": wwpLeosTceCfmMEPEntry,
       "wwpLeosTceCfmMEPId": wwpLeosTceCfmMEPId,
       "wwpLeosTceCfmMEPAdminState": wwpLeosTceCfmMEPAdminState,
       "wwpLeosTceCfmMEPOperState": wwpLeosTceCfmMEPOperState,
       "wwpLeosTceCfmMEPDirection": wwpLeosTceCfmMEPDirection,
       "wwpLeosTceCfmMEPCCMState": wwpLeosTceCfmMEPCCMState,
       "wwpLeosTceCfmMEPCCMPriority": wwpLeosTceCfmMEPCCMPriority,
       "wwpLeosTceCfmMEPLTMPriority": wwpLeosTceCfmMEPLTMPriority,
       "wwpLeosTceCfmMEPMacAddr": wwpLeosTceCfmMEPMacAddr,
       "wwpLeosTceCfmMEPNextLbmSeqNumber": wwpLeosTceCfmMEPNextLbmSeqNumber,
       "wwpLeosTceCfmMEPRxValidInOrderLoopbackReply": wwpLeosTceCfmMEPRxValidInOrderLoopbackReply,
       "wwpLeosTceCfmMEPRxValidOutOrderLoopbackReply": wwpLeosTceCfmMEPRxValidOutOrderLoopbackReply,
       "wwpLeosTceCfmMEPNextLTMSeqNumber": wwpLeosTceCfmMEPNextLTMSeqNumber,
       "wwpLeosTceCfmMEPNumLoopbackRepliesTxmt": wwpLeosTceCfmMEPNumLoopbackRepliesTxmt,
       "wwpLeosTceCfmMEPNumLTMRecevied": wwpLeosTceCfmMEPNumLTMRecevied,
       "wwpLeosTceCfmMEPNumLTMTxmt": wwpLeosTceCfmMEPNumLTMTxmt,
       "wwpLeosTceCfmMEPNumCCMTxmt": wwpLeosTceCfmMEPNumCCMTxmt,
       "wwpLeosTceCfmMEPRowStatus": wwpLeosTceCfmMEPRowStatus,
       "wwpLeosTceCfmMEPNumDMMSent": wwpLeosTceCfmMEPNumDMMSent,
       "wwpLeosTceCfmMEPDMMDelay": wwpLeosTceCfmMEPDMMDelay,
       "wwpLeosTceCfmMEPDMMJitter": wwpLeosTceCfmMEPDMMJitter,
       "wwpLeosTceCfmMEPNumLMMSent": wwpLeosTceCfmMEPNumLMMSent,
       "wwpLeosTceCfmMEPLMMFrameLossNear": wwpLeosTceCfmMEPLMMFrameLossNear,
       "wwpLeosTceCfmMEPLMMFrameLossFar": wwpLeosTceCfmMEPLMMFrameLossFar,
       "wwpLeosTceCfmMEPLiType": wwpLeosTceCfmMEPLiType,
       "wwpLeosTceCfmMEPLiIndex": wwpLeosTceCfmMEPLiIndex,
       "wwpLeosTceCfmMEPServiceName": wwpLeosTceCfmMEPServiceName,
       "wwpLeosTceCfmMEPSubPortName": wwpLeosTceCfmMEPSubPortName,
       "wwpLeosTceCfmMEPVsPbtName": wwpLeosTceCfmMEPVsPbtName,
       "wwpLeosTceCfmMEPLogicalPortName": wwpLeosTceCfmMEPLogicalPortName,
       "wwpLeosTceCfmMEPSubPortIndex": wwpLeosTceCfmMEPSubPortIndex,
       "wwpLeosTceCfmMEPEncapsulation": wwpLeosTceCfmMEPEncapsulation,
       "wwpLeosTceCfmMEPLeadPortBayIndex": wwpLeosTceCfmMEPLeadPortBayIndex,
       "wwpLeosTceCfmMEPLeadPortShelfIndex": wwpLeosTceCfmMEPLeadPortShelfIndex,
       "wwpLeosTceCfmMEPLeadPortModuleIndex": wwpLeosTceCfmMEPLeadPortModuleIndex,
       "wwpLeosTceCfmMEPPBTBvid": wwpLeosTceCfmMEPPBTBvid,
       "wwpLeosTceCfmMEPPBTEtype": wwpLeosTceCfmMEPPBTEtype,
       "wwpLeosTceCfmMEPNumLbmTxmt": wwpLeosTceCfmMEPNumLbmTxmt,
       "wwpLeosTceCfmMEPNumLbmReceived": wwpLeosTceCfmMEPNumLbmReceived,
       "wwpLeosTceCfmMEPNumLoopbackRepliesReceived": wwpLeosTceCfmMEPNumLoopbackRepliesReceived,
       "wwpLeosTceCfmMEPNumLTRepliesTxmt": wwpLeosTceCfmMEPNumLTRepliesTxmt,
       "wwpLeosTceCfmMEPNumLTRepliesReceived": wwpLeosTceCfmMEPNumLTRepliesReceived,
       "wwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived": wwpLeosTceCfmMEPNumUnexpectedLTRepliesReceived,
       "wwpLeosTceCfmMEPNumCCMReceived": wwpLeosTceCfmMEPNumCCMReceived,
       "wwpLeosTceCfmMEPRxContentMismatchLoopbackReply": wwpLeosTceCfmMEPRxContentMismatchLoopbackReply,
       "wwpLeosTceCfmMEPRxUnexpectedLoopbackReply": wwpLeosTceCfmMEPRxUnexpectedLoopbackReply,
       "wwpLeosTceCfmDelay": wwpLeosTceCfmDelay,
       "wwpLeosTceCfmDelayMsgTable": wwpLeosTceCfmDelayMsgTable,
       "wwpLeosTceCfmDelayMsgEntry": wwpLeosTceCfmDelayMsgEntry,
       "wwpLeosTceCfmDelayMsgLocalMEPId": wwpLeosTceCfmDelayMsgLocalMEPId,
       "wwpLeosTceCfmDelayMsgTargetMEPID": wwpLeosTceCfmDelayMsgTargetMEPID,
       "wwpLeosTceCfmDelayMsgTargetMacAddr": wwpLeosTceCfmDelayMsgTargetMacAddr,
       "wwpLeosTceCfmDelayMsgCount": wwpLeosTceCfmDelayMsgCount,
       "wwpLeosTceCfmDelayMsgPriority": wwpLeosTceCfmDelayMsgPriority,
       "wwpLeosTceCfmDelayMsgRowStatus": wwpLeosTceCfmDelayMsgRowStatus,
       "wwpLeosTceCfmDelayMsgRepeatInterval": wwpLeosTceCfmDelayMsgRepeatInterval,
       "wwpLeosTceCfmDelayMsgDelayThreshold": wwpLeosTceCfmDelayMsgDelayThreshold,
       "wwpLeosTceCfmDelayMsgJitterThreshold": wwpLeosTceCfmDelayMsgJitterThreshold,
       "wwpLeosTceCfmDelayMsgServiceName": wwpLeosTceCfmDelayMsgServiceName,
       "wwpLeosTceCfmDelayMsgSubPortName": wwpLeosTceCfmDelayMsgSubPortName,
       "wwpLeosTceCfmDelayMsgDelay": wwpLeosTceCfmDelayMsgDelay,
       "wwpLeosTceCfmDelayMsgJitter": wwpLeosTceCfmDelayMsgJitter,
       "wwpLeosTceCfmDelayMsgTotalTxDmm": wwpLeosTceCfmDelayMsgTotalTxDmm,
       "wwpLeosTceCfmDelayMsgTotalRxDmm": wwpLeosTceCfmDelayMsgTotalRxDmm,
       "wwpLeosTceCfmDelayMsgTotalTxDmr": wwpLeosTceCfmDelayMsgTotalTxDmr,
       "wwpLeosTceCfmDelayMsgTotalRxDmr": wwpLeosTceCfmDelayMsgTotalRxDmr,
       "wwpLeosTceCfmDelayMsgAction": wwpLeosTceCfmDelayMsgAction,
       "wwpLeosTceCfmDelayMsgMaxDelay": wwpLeosTceCfmDelayMsgMaxDelay,
       "wwpLeosTceCfmDelayMsgMaxJitter": wwpLeosTceCfmDelayMsgMaxJitter,
       "wwpLeosTceCfmDelayMsgMaxDelayThreshold": wwpLeosTceCfmDelayMsgMaxDelayThreshold,
       "wwpLeosTceCfmDelayMsgMaxJitterThreshold": wwpLeosTceCfmDelayMsgMaxJitterThreshold,
       "wwpLeosTceCfmDelayMsgMinDelay": wwpLeosTceCfmDelayMsgMinDelay,
       "wwpLeosTceCfmDelayMsgMinJitter": wwpLeosTceCfmDelayMsgMinJitter,
       "wwpLeosTceCfmFrameLoss": wwpLeosTceCfmFrameLoss,
       "wwpLeosTceCfmFrameLossMsgTable": wwpLeosTceCfmFrameLossMsgTable,
       "wwpLeosTceCfmFrameLossMsgEntry": wwpLeosTceCfmFrameLossMsgEntry,
       "wwpLeosTceCfmFrameLossMsgLocalMEPId": wwpLeosTceCfmFrameLossMsgLocalMEPId,
       "wwpLeosTceCfmFrameLossMsgTargetMEPID": wwpLeosTceCfmFrameLossMsgTargetMEPID,
       "wwpLeosTceCfmFrameLossMsgTargetMacAddr": wwpLeosTceCfmFrameLossMsgTargetMacAddr,
       "wwpLeosTceCfmFrameLossMsgCount": wwpLeosTceCfmFrameLossMsgCount,
       "wwpLeosTceCfmFrameLossMsgPriority": wwpLeosTceCfmFrameLossMsgPriority,
       "wwpLeosTceCfmFrameLossMsgRowStatus": wwpLeosTceCfmFrameLossMsgRowStatus,
       "wwpLeosTceCfmFrameLossMsgRepeatInterval": wwpLeosTceCfmFrameLossMsgRepeatInterval,
       "wwpLeosTceCfmFrameLossMsgNearLossThreshold": wwpLeosTceCfmFrameLossMsgNearLossThreshold,
       "wwpLeosTceCfmFrameLossMsgFarLossThreshold": wwpLeosTceCfmFrameLossMsgFarLossThreshold,
       "wwpLeosTceCfmFrameLossMsgServiceName": wwpLeosTceCfmFrameLossMsgServiceName,
       "wwpLeosTceCfmFrameLossMsgSubPortName": wwpLeosTceCfmFrameLossMsgSubPortName,
       "wwpLeosTceCfmFrameLossMsgFrameLossNear": wwpLeosTceCfmFrameLossMsgFrameLossNear,
       "wwpLeosTceCfmFrameLossMsgFrameLossFar": wwpLeosTceCfmFrameLossMsgFrameLossFar,
       "wwpLeosTceCfmFrameLossMsgTotalTxLmm": wwpLeosTceCfmFrameLossMsgTotalTxLmm,
       "wwpLeosTceCfmFrameLossMsgTotalRxLmm": wwpLeosTceCfmFrameLossMsgTotalRxLmm,
       "wwpLeosTceCfmFrameLossMsgTotalTxLmr": wwpLeosTceCfmFrameLossMsgTotalTxLmr,
       "wwpLeosTceCfmFrameLossMsgTotalRxLmr": wwpLeosTceCfmFrameLossMsgTotalRxLmr,
       "wwpLeosTceCfmFrameLossMsgAction": wwpLeosTceCfmFrameLossMsgAction,
       "wwpLeosTceCfmMipCCMDb": wwpLeosTceCfmMipCCMDb,
       "wwpLeosTceCfmMipCCMDbTable": wwpLeosTceCfmMipCCMDbTable,
       "wwpLeosTceCfmMipCCMDbEntry": wwpLeosTceCfmMipCCMDbEntry,
       "wwpLeosTceCfmMipCCMDbIndex": wwpLeosTceCfmMipCCMDbIndex,
       "wwpLeosTceCfmMipCCMDbMacAddr": wwpLeosTceCfmMipCCMDbMacAddr,
       "wwpLeosTceCfmMipCCMDbServiceName": wwpLeosTceCfmMipCCMDbServiceName,
       "wwpLeosTceCfmMipCCMDbSubPortName": wwpLeosTceCfmMipCCMDbSubPortName,
       "wwpLeosTceCfmMipCCMdbNumCCMRx": wwpLeosTceCfmMipCCMdbNumCCMRx,
       "wwpLeosTceCfmMipCCMDbCCMRxTime": wwpLeosTceCfmMipCCMDbCCMRxTime,
       "wwpLeosTceCfmMipCCMDbLevel": wwpLeosTceCfmMipCCMDbLevel,
       "wwpLeosTceCfmMipCCMDbMEPID": wwpLeosTceCfmMipCCMDbMEPID,
       "wwpLeosTceCfmMipRDI": wwpLeosTceCfmMipRDI,
       "wwpLeosTceCfmMipLastPortStatus": wwpLeosTceCfmMipLastPortStatus,
       "wwpLeosCfmExtMIBObj": wwpLeosCfmExtMIBObj,
       "wwpLeosCfmExtLoopback": wwpLeosCfmExtLoopback,
       "wwpLeosCfmExtLoopbackMsgTable": wwpLeosCfmExtLoopbackMsgTable,
       "wwpLeosCfmExtLoopbackMsgEntry": wwpLeosCfmExtLoopbackMsgEntry,
       "wwpLeosCfmExtLoopbackMsgLocalMEPID": wwpLeosCfmExtLoopbackMsgLocalMEPID,
       "wwpLeosCfmExtLoopbackMsgTargetMEPID": wwpLeosCfmExtLoopbackMsgTargetMEPID,
       "wwpLeosCfmExtLoopbackMsgTargetMacAddr": wwpLeosCfmExtLoopbackMsgTargetMacAddr,
       "wwpLeosCfmExtLoopbackMsgCount": wwpLeosCfmExtLoopbackMsgCount,
       "wwpLeosCfmExtLoopbackMsgData": wwpLeosCfmExtLoopbackMsgData,
       "wwpLeosCfmExtLoopbackMsgPriority": wwpLeosCfmExtLoopbackMsgPriority,
       "wwpLeosCfmExtLoopbackMsgAction": wwpLeosCfmExtLoopbackMsgAction,
       "wwpLeosCfmExtLoopbackMsgInterval": wwpLeosCfmExtLoopbackMsgInterval,
       "wwpLeosCfmExtLoopbackMsgTimeout": wwpLeosCfmExtLoopbackMsgTimeout,
       "wwpLeosCfmExtLoopbackMsgLoss": wwpLeosCfmExtLoopbackMsgLoss,
       "wwpLeosCfmExtMEP": wwpLeosCfmExtMEP,
       "wwpLeosCfmExtMEPTable": wwpLeosCfmExtMEPTable,
       "wwpLeosCfmExtMEPEntry": wwpLeosCfmExtMEPEntry,
       "wwpLeosCfmExtMEPId": wwpLeosCfmExtMEPId,
       "wwpLeosCfmExtPortId": wwpLeosCfmExtPortId,
       "wwpLeosCfmExtVlanId": wwpLeosCfmExtVlanId,
       "wwpLeosCfmExtMEPAdminState": wwpLeosCfmExtMEPAdminState,
       "wwpLeosCfmExtMEPOperState": wwpLeosCfmExtMEPOperState,
       "wwpLeosCfmExtMEPDirection": wwpLeosCfmExtMEPDirection,
       "wwpLeosCfmExtMEPCCMState": wwpLeosCfmExtMEPCCMState,
       "wwpLeosCfmExtMEPCCMPriority": wwpLeosCfmExtMEPCCMPriority,
       "wwpLeosCfmExtMEPLTMPriority": wwpLeosCfmExtMEPLTMPriority,
       "wwpLeosCfmExtMEPMacAddr": wwpLeosCfmExtMEPMacAddr,
       "wwpLeosCfmExtMEPNextLbmSeqNumber": wwpLeosCfmExtMEPNextLbmSeqNumber,
       "wwpLeosCfmExtMEPNextLTMSeqNumber": wwpLeosCfmExtMEPNextLTMSeqNumber,
       "wwpLeosCfmExtMEPRowStatus": wwpLeosCfmExtMEPRowStatus,
       "wwpLeosCfmExtMEPDMMDelay": wwpLeosCfmExtMEPDMMDelay,
       "wwpLeosCfmExtMEPDMMJitter": wwpLeosCfmExtMEPDMMJitter,
       "wwpLeosCfmExtMEPLMMFrameLossNear": wwpLeosCfmExtMEPLMMFrameLossNear,
       "wwpLeosCfmExtMEPLMMFrameLossFar": wwpLeosCfmExtMEPLMMFrameLossFar,
       "wwpLeosCfmExtMEPServiceName": wwpLeosCfmExtMEPServiceName,
       "wwpLeosCfmExtMEPInterfaceName": wwpLeosCfmExtMEPInterfaceName,
       "wwpLeosCfmExtMEPServiceInstanceName": wwpLeosCfmExtMEPServiceInstanceName,
       "wwpLeosCfmExtMEPLogicalPortName": wwpLeosCfmExtMEPLogicalPortName,
       "wwpLeosCfmExtMEPTagMode": wwpLeosCfmExtMEPTagMode,
       "wwpLeosCfmExtMEPTagVID": wwpLeosCfmExtMEPTagVID,
       "wwpLeosCfmExtMEPTagPriority": wwpLeosCfmExtMEPTagPriority,
       "wwpLeosCfmExtMEPLMMBadSequence": wwpLeosCfmExtMEPLMMBadSequence,
       "wwpLeosCfmExtMEPCCMComment": wwpLeosCfmExtMEPCCMComment,
       "wwpLeosCfmExtMEPLMMMissingSequence": wwpLeosCfmExtMEPLMMMissingSequence,
       "wwpLeosCfmExtMEPBlockOppositeFaultCurrent": wwpLeosCfmExtMEPBlockOppositeFaultCurrent,
       "wwpLeosCfmExtMEPBlockOppositeFaultThreshold": wwpLeosCfmExtMEPBlockOppositeFaultThreshold,
       "wwpLeosCfmExtMEPBlockOppositeFaultTime": wwpLeosCfmExtMEPBlockOppositeFaultTime,
       "wwpLeosCfmExtMEPDMMMinDelay": wwpLeosCfmExtMEPDMMMinDelay,
       "wwpLeosCfmExtMEPDMMMaxDelay": wwpLeosCfmExtMEPDMMMaxDelay,
       "wwpLeosCfmExtMEPDMMMinJitter": wwpLeosCfmExtMEPDMMMinJitter,
       "wwpLeosCfmExtMEPDMMMaxJitter": wwpLeosCfmExtMEPDMMMaxJitter,
       "wwpLeosCfmExtMEPAccelerated": wwpLeosCfmExtMEPAccelerated,
       "wwpLeosCfmExtMEPStatsTable": wwpLeosCfmExtMEPStatsTable,
       "wwpLeosCfmExtMEPStatsEntry": wwpLeosCfmExtMEPStatsEntry,
       "wwpLeosCfmExtMEPStatsTotalValidFramesReceived": wwpLeosCfmExtMEPStatsTotalValidFramesReceived,
       "wwpLeosCfmExtMEPStatsTotalInvalidFramesReceived": wwpLeosCfmExtMEPStatsTotalInvalidFramesReceived,
       "wwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived": wwpLeosCfmExtMEPStatsTotalInvalidMessageOverflowReceived,
       "wwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived": wwpLeosCfmExtMEPStatsInvalidPortStatusTLVReceived,
       "wwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived": wwpLeosCfmExtMEPStatsInvalidInterfaceStatusTLVReceived,
       "wwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived": wwpLeosCfmExtMEPStatsInvalidSenderIDTLVReceived,
       "wwpLeosCfmExtMEPStatsCCMTxmt": wwpLeosCfmExtMEPStatsCCMTxmt,
       "wwpLeosCfmExtMEPStatsValidCCMReceived": wwpLeosCfmExtMEPStatsValidCCMReceived,
       "wwpLeosCfmExtMEPStatsCCMInSequenceReceived": wwpLeosCfmExtMEPStatsCCMInSequenceReceived,
       "wwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived": wwpLeosCfmExtMEPStatsCCMSequenceErrorsReceived,
       "wwpLeosCfmExtMEPStatsMDLevelXconCCMReceived": wwpLeosCfmExtMEPStatsMDLevelXconCCMReceived,
       "wwpLeosCfmExtMEPStatsMAIDXconCCMReceived": wwpLeosCfmExtMEPStatsMAIDXconCCMReceived,
       "wwpLeosCfmExtMEPStatsIntervalErrorCCMReceived": wwpLeosCfmExtMEPStatsIntervalErrorCCMReceived,
       "wwpLeosCfmExtMEPStatsRxInvalidCCM": wwpLeosCfmExtMEPStatsRxInvalidCCM,
       "wwpLeosCfmExtMEPStatsLBMTxmt": wwpLeosCfmExtMEPStatsLBMTxmt,
       "wwpLeosCfmExtMEPStatsLBRTxmt": wwpLeosCfmExtMEPStatsLBRTxmt,
       "wwpLeosCfmExtMEPStatsInOrderLBRReceived": wwpLeosCfmExtMEPStatsInOrderLBRReceived,
       "wwpLeosCfmExtMEPStatsOutOfOrderLBRReceived": wwpLeosCfmExtMEPStatsOutOfOrderLBRReceived,
       "wwpLeosCfmExtMEPStatsContentMismatchLBRReceived": wwpLeosCfmExtMEPStatsContentMismatchLBRReceived,
       "wwpLeosCfmExtMEPStatsUnexpectedLBRReceived": wwpLeosCfmExtMEPStatsUnexpectedLBRReceived,
       "wwpLeosCfmExtMEPStatsInvalidLBRReceived": wwpLeosCfmExtMEPStatsInvalidLBRReceived,
       "wwpLeosCfmExtMEPStatsLTMTxmt": wwpLeosCfmExtMEPStatsLTMTxmt,
       "wwpLeosCfmExtMEPStatsValidLTMReceived": wwpLeosCfmExtMEPStatsValidLTMReceived,
       "wwpLeosCfmExtMEPStatsTotalInvalidLTMReceived": wwpLeosCfmExtMEPStatsTotalInvalidLTMReceived,
       "wwpLeosCfmExtMEPStatsInvalidLTRAction": wwpLeosCfmExtMEPStatsInvalidLTRAction,
       "wwpLeosCfmExtMEPStatsLTRTxmt": wwpLeosCfmExtMEPStatsLTRTxmt,
       "wwpLeosCfmExtMEPStatsLTRReceived": wwpLeosCfmExtMEPStatsLTRReceived,
       "wwpLeosCfmExtMEPStatsDMMTxmt": wwpLeosCfmExtMEPStatsDMMTxmt,
       "wwpLeosCfmExtMEPStatsDMMReceived": wwpLeosCfmExtMEPStatsDMMReceived,
       "wwpLeosCfmExtMEPStatsDMRTxmt": wwpLeosCfmExtMEPStatsDMRTxmt,
       "wwpLeosCfmExtMEPStatsDMRReceived": wwpLeosCfmExtMEPStatsDMRReceived,
       "wwpLeosCfmExtMEPStatsDMReplyTimeout": wwpLeosCfmExtMEPStatsDMReplyTimeout,
       "wwpLeosCfmExtMEPStatsLMMTxmt": wwpLeosCfmExtMEPStatsLMMTxmt,
       "wwpLeosCfmExtMEPStatsLMMReceived": wwpLeosCfmExtMEPStatsLMMReceived,
       "wwpLeosCfmExtMEPStatsLMRTxmt": wwpLeosCfmExtMEPStatsLMRTxmt,
       "wwpLeosCfmExtMEPStatsLMRReceived": wwpLeosCfmExtMEPStatsLMRReceived,
       "wwpLeosCfmExtMEPStatsLMRTimeout": wwpLeosCfmExtMEPStatsLMRTimeout,
       "wwpLeosCfmExtMEPStatsMepIdErrorCCMReceived": wwpLeosCfmExtMEPStatsMepIdErrorCCMReceived,
       "wwpLeosCfmExtMEPStatsClear": wwpLeosCfmExtMEPStatsClear,
       "wwpLeosCfmExtMEPStatsValidLBMReceived": wwpLeosCfmExtMEPStatsValidLBMReceived,
       "wwpLeosCfmExtMEPStatsInvalidLBMReceived": wwpLeosCfmExtMEPStatsInvalidLBMReceived,
       "wwpLeosCfmExtMEPStatsUnexpectedLTRReceived": wwpLeosCfmExtMEPStatsUnexpectedLTRReceived,
       "wwpLeosCfmExtMEPStatsInvalidDMMReceived": wwpLeosCfmExtMEPStatsInvalidDMMReceived,
       "wwpLeosCfmExtMEPStatsInvalidDMRReceived": wwpLeosCfmExtMEPStatsInvalidDMRReceived,
       "wwpLeosCfmExtMEPStatsUnexpectedDMRReceived": wwpLeosCfmExtMEPStatsUnexpectedDMRReceived,
       "wwpLeosCfmExtMEPStatsInvalidLMMReceived": wwpLeosCfmExtMEPStatsInvalidLMMReceived,
       "wwpLeosCfmExtMEPStatsInvalidLMRReceived": wwpLeosCfmExtMEPStatsInvalidLMRReceived,
       "wwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep": wwpLeosCfmExtMEPStatsInvalidBlockedOppositeMep,
       "wwpLeosCfmExtMEPLastStatsTable": wwpLeosCfmExtMEPLastStatsTable,
       "wwpLeosCfmExtMEPLastStatsEntry": wwpLeosCfmExtMEPLastStatsEntry,
       "wwpLeosCfmExtMEPLastStatsPriority": wwpLeosCfmExtMEPLastStatsPriority,
       "wwpLeosCfmExtMEPLastStatsLBMCount": wwpLeosCfmExtMEPLastStatsLBMCount,
       "wwpLeosCfmExtMEPLastStatsLBMSent": wwpLeosCfmExtMEPLastStatsLBMSent,
       "wwpLeosCfmExtMEPLastStatsLBMToSend": wwpLeosCfmExtMEPLastStatsLBMToSend,
       "wwpLeosCfmExtMEPLastStatsInOrderLBRReceived": wwpLeosCfmExtMEPLastStatsInOrderLBRReceived,
       "wwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived": wwpLeosCfmExtMEPLastStatsOutOfOrderLBRReceived,
       "wwpLeosCfmExtMEPLastStatsDMMPriority": wwpLeosCfmExtMEPLastStatsDMMPriority,
       "wwpLeosCfmExtMEPLastStatsDMMTxmt": wwpLeosCfmExtMEPLastStatsDMMTxmt,
       "wwpLeosCfmExtMEPLastStatsDMMReceived": wwpLeosCfmExtMEPLastStatsDMMReceived,
       "wwpLeosCfmExtMEPLastStatsDMMDelay": wwpLeosCfmExtMEPLastStatsDMMDelay,
       "wwpLeosCfmExtMEPLastStatsDMMJitter": wwpLeosCfmExtMEPLastStatsDMMJitter,
       "wwpLeosCfmExtMEPLastStatsLMMPriority": wwpLeosCfmExtMEPLastStatsLMMPriority,
       "wwpLeosCfmExtMEPLastStatsLMMTxtm": wwpLeosCfmExtMEPLastStatsLMMTxtm,
       "wwpLeosCfmExtMEPLastStatsLMMReceived": wwpLeosCfmExtMEPLastStatsLMMReceived,
       "wwpLeosCfmExtMEPLastStatsFrameLossNear": wwpLeosCfmExtMEPLastStatsFrameLossNear,
       "wwpLeosCfmExtMEPLastStatsFrameLossFar": wwpLeosCfmExtMEPLastStatsFrameLossFar,
       "wwpLeosCfmExtMEPLastStatsLTMPriority": wwpLeosCfmExtMEPLastStatsLTMPriority,
       "wwpLeosCfmExtMEPLastStatsLTMSequenceNo": wwpLeosCfmExtMEPLastStatsLTMSequenceNo,
       "wwpLeosCfmExtMEPLastStatsLTMInitialTTL": wwpLeosCfmExtMEPLastStatsLTMInitialTTL,
       "wwpLeosCfmExtMEPLastStatsFrameLossBadSequence": wwpLeosCfmExtMEPLastStatsFrameLossBadSequence,
       "wwpLeosCfmExtMEPLastStatsDMMMinDelay": wwpLeosCfmExtMEPLastStatsDMMMinDelay,
       "wwpLeosCfmExtMEPLastStatsDMMMaxDelay": wwpLeosCfmExtMEPLastStatsDMMMaxDelay,
       "wwpLeosCfmExtMEPLastStatsDMMMinJitter": wwpLeosCfmExtMEPLastStatsDMMMinJitter,
       "wwpLeosCfmExtMEPLastStatsDMMMaxJitter": wwpLeosCfmExtMEPLastStatsDMMMaxJitter,
       "wwpLeosCfmExtMEPClearStatistics": wwpLeosCfmExtMEPClearStatistics,
       "wwpLeosCfmExtMEPDelayHistoryTable": wwpLeosCfmExtMEPDelayHistoryTable,
       "wwpLeosCfmExtMEPDelayHistoryEntry": wwpLeosCfmExtMEPDelayHistoryEntry,
       "wwpLeosCfmExtMEPDelayHistoryIndex": wwpLeosCfmExtMEPDelayHistoryIndex,
       "wwpLeosCfmExtMEPDelayHistoryStatus": wwpLeosCfmExtMEPDelayHistoryStatus,
       "wwpLeosCfmExtMEPDelayHistoryInterval": wwpLeosCfmExtMEPDelayHistoryInterval,
       "wwpLeosCfmExtMEPDelayHistoryPriority": wwpLeosCfmExtMEPDelayHistoryPriority,
       "wwpLeosCfmExtMEPDelayHistoryMEPId": wwpLeosCfmExtMEPDelayHistoryMEPId,
       "wwpLeosCfmExtMEPDelayHistoryNumDMMSent": wwpLeosCfmExtMEPDelayHistoryNumDMMSent,
       "wwpLeosCfmExtMEPDelayHistoryNumDMRReceived": wwpLeosCfmExtMEPDelayHistoryNumDMRReceived,
       "wwpLeosCfmExtMEPDelayHistoryMinDelay": wwpLeosCfmExtMEPDelayHistoryMinDelay,
       "wwpLeosCfmExtMEPDelayHistoryAveDelay": wwpLeosCfmExtMEPDelayHistoryAveDelay,
       "wwpLeosCfmExtMEPDelayHistoryMaxDelay": wwpLeosCfmExtMEPDelayHistoryMaxDelay,
       "wwpLeosCfmExtMEPDelayHistoryMinJitter": wwpLeosCfmExtMEPDelayHistoryMinJitter,
       "wwpLeosCfmExtMEPDelayHistoryAveJitter": wwpLeosCfmExtMEPDelayHistoryAveJitter,
       "wwpLeosCfmExtMEPDelayHistoryMaxJitter": wwpLeosCfmExtMEPDelayHistoryMaxJitter,
       "wwpLeosCfmExtMEPDelayHistoryStartTime": wwpLeosCfmExtMEPDelayHistoryStartTime,
       "wwpLeosCfmExtMEPDelayHistoryStopTime": wwpLeosCfmExtMEPDelayHistoryStopTime,
       "wwpLeosCfmExtMEPDelayHistoryClear": wwpLeosCfmExtMEPDelayHistoryClear,
       "wwpLeosCfmExtLinkTrace": wwpLeosCfmExtLinkTrace,
       "wwpLeosCfmExtLinkTraceMsgTable": wwpLeosCfmExtLinkTraceMsgTable,
       "wwpLeosCfmExtLinkTraceMsgEntry": wwpLeosCfmExtLinkTraceMsgEntry,
       "wwpLeosCfmExtLinkTraceMsgLocalMepID": wwpLeosCfmExtLinkTraceMsgLocalMepID,
       "wwpLeosCfmExtLinkTraceMsgTargetMEPID": wwpLeosCfmExtLinkTraceMsgTargetMEPID,
       "wwpLeosCfmExtLinkTraceMsgTargetMacAddr": wwpLeosCfmExtLinkTraceMsgTargetMacAddr,
       "wwpLeosCfmExtLinkTraceMsgTTL": wwpLeosCfmExtLinkTraceMsgTTL,
       "wwpLeosCfmExtLinkTraceMsgSequenceNumber": wwpLeosCfmExtLinkTraceMsgSequenceNumber,
       "wwpLeosCfmExtLinkTraceMsgPriority": wwpLeosCfmExtLinkTraceMsgPriority,
       "wwpLeosCfmExtLinkTraceMsgAction": wwpLeosCfmExtLinkTraceMsgAction,
       "wwpLeosCfmExtLinkTraceMsgReplyTable": wwpLeosCfmExtLinkTraceMsgReplyTable,
       "wwpLeosCfmExtLinkTraceMsgReplyEntry": wwpLeosCfmExtLinkTraceMsgReplyEntry,
       "wwpLeosCfmExtLinkTraceMsgReplyTTL": wwpLeosCfmExtLinkTraceMsgReplyTTL,
       "wwpLeosCfmExtLinkTraceMsgReplyTTLIndex": wwpLeosCfmExtLinkTraceMsgReplyTTLIndex,
       "wwpLeosCfmExtLinkTraceMsgReplySequenceNumber": wwpLeosCfmExtLinkTraceMsgReplySequenceNumber,
       "wwpLeosCfmExtLinkTraceMsgReplyMPMacAddr": wwpLeosCfmExtLinkTraceMsgReplyMPMacAddr,
       "wwpLeosCfmExtLinkTraceMsgReplyMEPID": wwpLeosCfmExtLinkTraceMsgReplyMEPID,
       "wwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr": wwpLeosCfmExtLinkTraceMsgReplyTargetMacAddr,
       "wwpLeosCfmExtLinkTraceMsgReplyRelayAction": wwpLeosCfmExtLinkTraceMsgReplyRelayAction,
       "wwpLeosCfmExtLinkTraceMsgReplyIngressPort": wwpLeosCfmExtLinkTraceMsgReplyIngressPort,
       "wwpLeosCfmExtLinkTraceMsgReplyIngressAction": wwpLeosCfmExtLinkTraceMsgReplyIngressAction,
       "wwpLeosCfmExtLinkTraceMsgReplyEgressPort": wwpLeosCfmExtLinkTraceMsgReplyEgressPort,
       "wwpLeosCfmExtLinkTraceMsgReplyEgressAction": wwpLeosCfmExtLinkTraceMsgReplyEgressAction,
       "wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr": wwpLeosCfmExtLinkTraceMsgReplyIngressPortStr,
       "wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr": wwpLeosCfmExtLinkTraceMsgReplyEgressPortStr,
       "wwpLeosCfmExtDelay": wwpLeosCfmExtDelay,
       "wwpLeosCfmExtDelayMsgTable": wwpLeosCfmExtDelayMsgTable,
       "wwpLeosCfmExtDelayMsgEntry": wwpLeosCfmExtDelayMsgEntry,
       "wwpLeosCfmExtDelayMsgLocalMEPId": wwpLeosCfmExtDelayMsgLocalMEPId,
       "wwpLeosCfmExtDelayMsgTargetMEPID": wwpLeosCfmExtDelayMsgTargetMEPID,
       "wwpLeosCfmExtDelayMsgTargetMacAddr": wwpLeosCfmExtDelayMsgTargetMacAddr,
       "wwpLeosCfmExtDelayMsgCount": wwpLeosCfmExtDelayMsgCount,
       "wwpLeosCfmExtDelayMsgPriority": wwpLeosCfmExtDelayMsgPriority,
       "wwpLeosCfmExtDelayMsgRepeat": wwpLeosCfmExtDelayMsgRepeat,
       "wwpLeosCfmExtDelayMsgRepeatCount": wwpLeosCfmExtDelayMsgRepeatCount,
       "wwpLeosCfmExtDelayMsgDelayThreshold": wwpLeosCfmExtDelayMsgDelayThreshold,
       "wwpLeosCfmExtDelayMsgJitterThreshold": wwpLeosCfmExtDelayMsgJitterThreshold,
       "wwpLeosCfmExtDelayMsgAction": wwpLeosCfmExtDelayMsgAction,
       "wwpLeosCfmExtDelayMsgMaxDelayThreshold": wwpLeosCfmExtDelayMsgMaxDelayThreshold,
       "wwpLeosCfmExtDelayMsgMaxJitterThreshold": wwpLeosCfmExtDelayMsgMaxJitterThreshold,
       "wwpLeosCfmExtFrameLoss": wwpLeosCfmExtFrameLoss,
       "wwpLeosCfmExtFrameLossMsgTable": wwpLeosCfmExtFrameLossMsgTable,
       "wwpLeosCfmExtFrameLossMsgEntry": wwpLeosCfmExtFrameLossMsgEntry,
       "wwpLeosCfmExtFrameLossMsgLocalMEPId": wwpLeosCfmExtFrameLossMsgLocalMEPId,
       "wwpLeosCfmExtFrameLossMsgTargetMEPID": wwpLeosCfmExtFrameLossMsgTargetMEPID,
       "wwpLeosCfmExtFrameLossMsgTargetMacAddr": wwpLeosCfmExtFrameLossMsgTargetMacAddr,
       "wwpLeosCfmExtFrameLossMsgCount": wwpLeosCfmExtFrameLossMsgCount,
       "wwpLeosCfmExtFrameLossMsgPriority": wwpLeosCfmExtFrameLossMsgPriority,
       "wwpLeosCfmExtFrameLossMsgRepeat": wwpLeosCfmExtFrameLossMsgRepeat,
       "wwpLeosCfmExtFrameLossMsgRepeatCount": wwpLeosCfmExtFrameLossMsgRepeatCount,
       "wwpLeosCfmExtFrameLossMsgFlnThreshold": wwpLeosCfmExtFrameLossMsgFlnThreshold,
       "wwpLeosCfmExtFrameLossMsgFlfThreshold": wwpLeosCfmExtFrameLossMsgFlfThreshold,
       "wwpLeosCfmExtFrameLossMsgAction": wwpLeosCfmExtFrameLossMsgAction,
       "wwpLeosCfmExtFrameLossMsgSeqThreshold": wwpLeosCfmExtFrameLossMsgSeqThreshold,
       "wwpLeosCfmExtInterfaceStack": wwpLeosCfmExtInterfaceStack,
       "wwpLeosCfmExtInterfaceStackTable": wwpLeosCfmExtInterfaceStackTable,
       "wwpLeosCfmExtInterfaceStackEntry": wwpLeosCfmExtInterfaceStackEntry,
       "wwpLeosCfmExtInterfaceStackServiceInstanceType": wwpLeosCfmExtInterfaceStackServiceInstanceType,
       "wwpLeosCfmExtInterfaceStackServiceInstanceIndex": wwpLeosCfmExtInterfaceStackServiceInstanceIndex,
       "wwpLeosCfmExtInterfaceStackInterfaceType": wwpLeosCfmExtInterfaceStackInterfaceType,
       "wwpLeosCfmExtInterfaceStackInterfaceIndex": wwpLeosCfmExtInterfaceStackInterfaceIndex,
       "wwpLeosCfmExtInterfaceStackLevel": wwpLeosCfmExtInterfaceStackLevel,
       "wwpLeosCfmExtInterfaceStackStackType": wwpLeosCfmExtInterfaceStackStackType,
       "wwpLeosCfmExtInterfaceStackInterfaceName": wwpLeosCfmExtInterfaceStackInterfaceName,
       "wwpLeosCfmExtInterfaceStackServiceInstanceName": wwpLeosCfmExtInterfaceStackServiceInstanceName,
       "wwpLeosCfmExtInterfaceStackPortName": wwpLeosCfmExtInterfaceStackPortName,
       "wwpLeosCfmExtInterfaceStackOperState": wwpLeosCfmExtInterfaceStackOperState,
       "wwpLeosCfmExtInterfaceStackVid": wwpLeosCfmExtInterfaceStackVid,
       "wwpLeosCfmExtInterfaceStackPgid": wwpLeosCfmExtInterfaceStackPgid,
       "wwpLeosCfmExtInterfaceStackMEPId": wwpLeosCfmExtInterfaceStackMEPId,
       "wwpLeosCfmExtInterfaceStackMacAddress": wwpLeosCfmExtInterfaceStackMacAddress,
       "wwpLeosCfmExtMIP": wwpLeosCfmExtMIP,
       "wwpLeosCfmExtMipTable": wwpLeosCfmExtMipTable,
       "wwpLeosCfmExtMipEntry": wwpLeosCfmExtMipEntry,
       "wwpLeosCfmExtMipVid": wwpLeosCfmExtMipVid,
       "wwpLeosCfmExtMipPort": wwpLeosCfmExtMipPort,
       "wwpLeosCfmExtMipLevel": wwpLeosCfmExtMipLevel,
       "wwpLeosCfmExtMipStatus": wwpLeosCfmExtMipStatus,
       "wwpLeosCfmExtInterfaceMIP": wwpLeosCfmExtInterfaceMIP,
       "wwpLeosCfmExtInterfaceMipTable": wwpLeosCfmExtInterfaceMipTable,
       "wwpLeosCfmExtInterfaceMipEntry": wwpLeosCfmExtInterfaceMipEntry,
       "wwpLeosCfmExtInterfaceMipServiceInstanceType": wwpLeosCfmExtInterfaceMipServiceInstanceType,
       "wwpLeosCfmExtInterfaceMipServiceInstanceIndex": wwpLeosCfmExtInterfaceMipServiceInstanceIndex,
       "wwpLeosCfmExtInterfaceMipInterfaceType": wwpLeosCfmExtInterfaceMipInterfaceType,
       "wwpLeosCfmExtInterfaceMipInterfaceIndex": wwpLeosCfmExtInterfaceMipInterfaceIndex,
       "wwpLeosCfmExtInterfaceMipInterfaceSubIndex": wwpLeosCfmExtInterfaceMipInterfaceSubIndex,
       "wwpLeosCfmExtInterfaceMipLevel": wwpLeosCfmExtInterfaceMipLevel,
       "wwpLeosCfmExtInterfaceMipStatus": wwpLeosCfmExtInterfaceMipStatus,
       "wwpLeosCfmExtOamPort": wwpLeosCfmExtOamPort,
       "wwpLeosCfmExtOamPortTable": wwpLeosCfmExtOamPortTable,
       "wwpLeosCfmExtOamPortEntry": wwpLeosCfmExtOamPortEntry,
       "wwpLeosCfmExtOamPortIndex": wwpLeosCfmExtOamPortIndex,
       "wwpLeosCfmExtOamPortSupported": wwpLeosCfmExtOamPortSupported,
       "wwpLeosCfmNotifMIBNotificationPrefix": wwpLeosCfmNotifMIBNotificationPrefix,
       "wwpLeosCfmNotifMIBNotification": wwpLeosCfmNotifMIBNotification,
       "wwpLeosCfmFaultTrap": wwpLeosCfmFaultTrap,
       "wwpLeosCfmPbtFaultTrap": wwpLeosCfmPbtFaultTrap,
       "wwpLeosCfmDelayFaultTrap": wwpLeosCfmDelayFaultTrap,
       "wwpLeosCfmJitterFaultTrap": wwpLeosCfmJitterFaultTrap,
       "wwpLeosCfmFrameLossNearFaultTrap": wwpLeosCfmFrameLossNearFaultTrap,
       "wwpLeosCfmFrameLossFarFaultTrap": wwpLeosCfmFrameLossFarFaultTrap,
       "wwpLeosCfmExtDelayFaultTrap": wwpLeosCfmExtDelayFaultTrap,
       "wwpLeosCfmExtJitterFaultTrap": wwpLeosCfmExtJitterFaultTrap,
       "wwpLeosCfmExtFrameLossNearFaultTrap": wwpLeosCfmExtFrameLossNearFaultTrap,
       "wwpLeosCfmFaultTrapSet": wwpLeosCfmFaultTrapSet,
       "wwpLeosCfmFaultTrapClear": wwpLeosCfmFaultTrapClear,
       "wwpLeosCfmDmmTrap": wwpLeosCfmDmmTrap,
       "wwpLeosCfmLmmTrap": wwpLeosCfmLmmTrap,
       "wwpLeosCfmExtFrameLossFarFaultTrap": wwpLeosCfmExtFrameLossFarFaultTrap,
       "wwpLeosCfmExtFaultTrapSet": wwpLeosCfmExtFaultTrapSet,
       "wwpLeosCfmExtFaultTrapClear": wwpLeosCfmExtFaultTrapClear,
       "wwpLeosCfmBadSequenceFaultTrap": wwpLeosCfmBadSequenceFaultTrap,
       "wwpLeosCfmBlockOppositeMEPSetTrap": wwpLeosCfmBlockOppositeMEPSetTrap,
       "wwpLeosCfmBlockOppositeMEPClearTrap": wwpLeosCfmBlockOppositeMEPClearTrap,
       "wwpLeosCfmMIBConformance": wwpLeosCfmMIBConformance,
       "wwpLeosCfmMIBCompliances": wwpLeosCfmMIBCompliances,
       "wwpLeosCfmMIBGroups": wwpLeosCfmMIBGroups}
)
