# SNMP MIB module (H3C-VOGENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VOGENERAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:44 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cVoice")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cVoiceGeneral = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1)
)
h3cVoiceGeneral.setRevisions(
        ("2005-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoiceGeneralObjects_ObjectIdentity = ObjectIdentity
h3cVoiceGeneralObjects = _H3cVoiceGeneralObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1)
)


class _H3cVoGeneralJitterLen_Type(Integer32):
    """Custom type h3cVoGeneralJitterLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_H3cVoGeneralJitterLen_Type.__name__ = "Integer32"
_H3cVoGeneralJitterLen_Object = MibScalar
h3cVoGeneralJitterLen = _H3cVoGeneralJitterLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 1),
    _H3cVoGeneralJitterLen_Type()
)
h3cVoGeneralJitterLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralJitterLen.setStatus("current")


class _H3cVoGeneralMatchPolicy_Type(Integer32):
    """Custom type h3cVoGeneralMatchPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_H3cVoGeneralMatchPolicy_Type.__name__ = "Integer32"
_H3cVoGeneralMatchPolicy_Object = MibScalar
h3cVoGeneralMatchPolicy = _H3cVoGeneralMatchPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 2),
    _H3cVoGeneralMatchPolicy_Type()
)
h3cVoGeneralMatchPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralMatchPolicy.setStatus("current")


class _H3cVoGeneralDataStatistics_Type(Integer32):
    """Custom type h3cVoGeneralDataStatistics based on Integer32"""
    defaultValue = 2

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


_H3cVoGeneralDataStatistics_Type.__name__ = "Integer32"
_H3cVoGeneralDataStatistics_Object = MibScalar
h3cVoGeneralDataStatistics = _H3cVoGeneralDataStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 5),
    _H3cVoGeneralDataStatistics_Type()
)
h3cVoGeneralDataStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralDataStatistics.setStatus("current")
_H3cVoGeneralDialTerminator_Type = OctetString
_H3cVoGeneralDialTerminator_Object = MibScalar
h3cVoGeneralDialTerminator = _H3cVoGeneralDialTerminator_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 7),
    _H3cVoGeneralDialTerminator_Type()
)
h3cVoGeneralDialTerminator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralDialTerminator.setStatus("current")


class _H3cVoGeneralCallStart_Type(Integer32):
    """Custom type h3cVoGeneralCallStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2))
    )


_H3cVoGeneralCallStart_Type.__name__ = "Integer32"
_H3cVoGeneralCallStart_Object = MibScalar
h3cVoGeneralCallStart = _H3cVoGeneralCallStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 8),
    _H3cVoGeneralCallStart_Type()
)
h3cVoGeneralCallStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralCallStart.setStatus("current")


class _H3cVoGeneralCalledTunnel_Type(Integer32):
    """Custom type h3cVoGeneralCalledTunnel based on Integer32"""
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


_H3cVoGeneralCalledTunnel_Type.__name__ = "Integer32"
_H3cVoGeneralCalledTunnel_Object = MibScalar
h3cVoGeneralCalledTunnel = _H3cVoGeneralCalledTunnel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 9),
    _H3cVoGeneralCalledTunnel_Type()
)
h3cVoGeneralCalledTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralCalledTunnel.setStatus("current")


class _H3cVoGeneralSpecialService_Type(Integer32):
    """Custom type h3cVoGeneralSpecialService based on Integer32"""
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


_H3cVoGeneralSpecialService_Type.__name__ = "Integer32"
_H3cVoGeneralSpecialService_Object = MibScalar
h3cVoGeneralSpecialService = _H3cVoGeneralSpecialService_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 10),
    _H3cVoGeneralSpecialService_Type()
)
h3cVoGeneralSpecialService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralSpecialService.setStatus("current")
_H3cVoGeneralPeerSearchStop_Type = Integer32
_H3cVoGeneralPeerSearchStop_Object = MibScalar
h3cVoGeneralPeerSearchStop = _H3cVoGeneralPeerSearchStop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 12),
    _H3cVoGeneralPeerSearchStop_Type()
)
h3cVoGeneralPeerSearchStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralPeerSearchStop.setStatus("current")


class _H3cVoGeneralPeerSelectOrderRule_Type(Integer32):
    """Custom type h3cVoGeneralPeerSelectOrderRule based on Integer32"""
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
              25)
        )
    )
    namedValues = NamedValues(
        *(("el", 21),
          ("elp", 3),
          ("elr", 4),
          ("ep", 20),
          ("epl", 2),
          ("epr", 1),
          ("er", 13),
          ("explicitMatch", 16),
          ("le", 24),
          ("lep", 9),
          ("ler", 10),
          ("longestNoUse", 19),
          ("lp", 25),
          ("lpe", 11),
          ("lpr", 12),
          ("lr", 15),
          ("pe", 22),
          ("pel", 6),
          ("per", 5),
          ("pl", 23),
          ("ple", 7),
          ("plr", 8),
          ("pr", 14),
          ("priority", 17),
          ("random", 18))
    )


_H3cVoGeneralPeerSelectOrderRule_Type.__name__ = "Integer32"
_H3cVoGeneralPeerSelectOrderRule_Object = MibScalar
h3cVoGeneralPeerSelectOrderRule = _H3cVoGeneralPeerSelectOrderRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 13),
    _H3cVoGeneralPeerSelectOrderRule_Type()
)
h3cVoGeneralPeerSelectOrderRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralPeerSelectOrderRule.setStatus("current")


class _H3cVoGeneralPeerSelectTypePriority_Type(Integer32):
    """Custom type h3cVoGeneralPeerSelectTypePriority based on Integer32"""
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
        *(("noneType", 1),
          ("potsVofrVoip", 5),
          ("potsVoipVofr", 4),
          ("vofrPotsVoip", 6),
          ("vofrVoipPots", 7),
          ("voipPotsVofr", 2),
          ("voipVofrPots", 3))
    )


_H3cVoGeneralPeerSelectTypePriority_Type.__name__ = "Integer32"
_H3cVoGeneralPeerSelectTypePriority_Object = MibScalar
h3cVoGeneralPeerSelectTypePriority = _H3cVoGeneralPeerSelectTypePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 14),
    _H3cVoGeneralPeerSelectTypePriority_Type()
)
h3cVoGeneralPeerSelectTypePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralPeerSelectTypePriority.setStatus("current")


class _H3cVoGeneralDscpSignal_Type(Integer32):
    """Custom type h3cVoGeneralDscpSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cVoGeneralDscpSignal_Type.__name__ = "Integer32"
_H3cVoGeneralDscpSignal_Object = MibScalar
h3cVoGeneralDscpSignal = _H3cVoGeneralDscpSignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 15),
    _H3cVoGeneralDscpSignal_Type()
)
h3cVoGeneralDscpSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralDscpSignal.setStatus("current")


class _H3cVoGeneralDscpMedia_Type(Integer32):
    """Custom type h3cVoGeneralDscpMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_H3cVoGeneralDscpMedia_Type.__name__ = "Integer32"
_H3cVoGeneralDscpMedia_Object = MibScalar
h3cVoGeneralDscpMedia = _H3cVoGeneralDscpMedia_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 1, 16),
    _H3cVoGeneralDscpMedia_Type()
)
h3cVoGeneralDscpMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoGeneralDscpMedia.setStatus("current")
_H3cVoiceNumberSubstGroup_ObjectIdentity = ObjectIdentity
h3cVoiceNumberSubstGroup = _H3cVoiceNumberSubstGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4)
)
_H3cVoNumSubstTable_Object = MibTable
h3cVoNumSubstTable = _H3cVoNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cVoNumSubstTable.setStatus("current")
_H3cVoNumSubstEntry_Object = MibTableRow
h3cVoNumSubstEntry = _H3cVoNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1, 1)
)
h3cVoNumSubstEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoNumSubstIndex"),
)
if mibBuilder.loadTexts:
    h3cVoNumSubstEntry.setStatus("current")


class _H3cVoNumSubstIndex_Type(Integer32):
    """Custom type h3cVoNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoNumSubstIndex_Type.__name__ = "Integer32"
_H3cVoNumSubstIndex_Object = MibTableColumn
h3cVoNumSubstIndex = _H3cVoNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1, 1, 1),
    _H3cVoNumSubstIndex_Type()
)
h3cVoNumSubstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoNumSubstIndex.setStatus("current")
_H3cVoNumSubstFirstRule_Type = Integer32
_H3cVoNumSubstFirstRule_Object = MibTableColumn
h3cVoNumSubstFirstRule = _H3cVoNumSubstFirstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1, 1, 2),
    _H3cVoNumSubstFirstRule_Type()
)
h3cVoNumSubstFirstRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstFirstRule.setStatus("current")


class _H3cVoNumSubstDotMatchRule_Type(Integer32):
    """Custom type h3cVoNumSubstDotMatchRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("endOnly", 1),
          ("leftRight", 2),
          ("rightLeft", 3))
    )


_H3cVoNumSubstDotMatchRule_Type.__name__ = "Integer32"
_H3cVoNumSubstDotMatchRule_Object = MibTableColumn
h3cVoNumSubstDotMatchRule = _H3cVoNumSubstDotMatchRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1, 1, 3),
    _H3cVoNumSubstDotMatchRule_Type()
)
h3cVoNumSubstDotMatchRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstDotMatchRule.setStatus("current")
_H3cVoNumSubstRowStatus_Type = RowStatus
_H3cVoNumSubstRowStatus_Object = MibTableColumn
h3cVoNumSubstRowStatus = _H3cVoNumSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 1, 1, 4),
    _H3cVoNumSubstRowStatus_Type()
)
h3cVoNumSubstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstRowStatus.setStatus("current")
_H3cVoNumSubstRuleTable_Object = MibTable
h3cVoNumSubstRuleTable = _H3cVoNumSubstRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleTable.setStatus("current")
_H3cVoNumSubstRuleEntry_Object = MibTableRow
h3cVoNumSubstRuleEntry = _H3cVoNumSubstRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2, 1)
)
h3cVoNumSubstRuleEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoNumSubstIndex"),
    (0, "H3C-VOGENERAL-MIB", "h3cVoNumSubstRuleIndex"),
)
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleEntry.setStatus("current")


class _H3cVoNumSubstRuleIndex_Type(Integer32):
    """Custom type h3cVoNumSubstRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_H3cVoNumSubstRuleIndex_Type.__name__ = "Integer32"
_H3cVoNumSubstRuleIndex_Object = MibTableColumn
h3cVoNumSubstRuleIndex = _H3cVoNumSubstRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2, 1, 1),
    _H3cVoNumSubstRuleIndex_Type()
)
h3cVoNumSubstRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleIndex.setStatus("current")
_H3cVoNumSubstRuleInputFormat_Type = OctetString
_H3cVoNumSubstRuleInputFormat_Object = MibTableColumn
h3cVoNumSubstRuleInputFormat = _H3cVoNumSubstRuleInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2, 1, 2),
    _H3cVoNumSubstRuleInputFormat_Type()
)
h3cVoNumSubstRuleInputFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleInputFormat.setStatus("current")
_H3cVoNumSubstRuleOutputFormat_Type = OctetString
_H3cVoNumSubstRuleOutputFormat_Object = MibTableColumn
h3cVoNumSubstRuleOutputFormat = _H3cVoNumSubstRuleOutputFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2, 1, 3),
    _H3cVoNumSubstRuleOutputFormat_Type()
)
h3cVoNumSubstRuleOutputFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleOutputFormat.setStatus("current")
_H3cVoNumSubstRuleRowStatus_Type = RowStatus
_H3cVoNumSubstRuleRowStatus_Object = MibTableColumn
h3cVoNumSubstRuleRowStatus = _H3cVoNumSubstRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 4, 2, 1, 4),
    _H3cVoNumSubstRuleRowStatus_Type()
)
h3cVoNumSubstRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoNumSubstRuleRowStatus.setStatus("current")
_H3cVoMaxCallTable_Object = MibTable
h3cVoMaxCallTable = _H3cVoMaxCallTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 5)
)
if mibBuilder.loadTexts:
    h3cVoMaxCallTable.setStatus("current")
_H3cVoMaxCallEntry_Object = MibTableRow
h3cVoMaxCallEntry = _H3cVoMaxCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 5, 1)
)
h3cVoMaxCallEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoMaxCallTableIndex"),
)
if mibBuilder.loadTexts:
    h3cVoMaxCallEntry.setStatus("current")


class _H3cVoMaxCallTableIndex_Type(Integer32):
    """Custom type h3cVoMaxCallTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoMaxCallTableIndex_Type.__name__ = "Integer32"
_H3cVoMaxCallTableIndex_Object = MibTableColumn
h3cVoMaxCallTableIndex = _H3cVoMaxCallTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 5, 1, 1),
    _H3cVoMaxCallTableIndex_Type()
)
h3cVoMaxCallTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoMaxCallTableIndex.setStatus("current")


class _H3cVoMaxCallValue_Type(Integer32):
    """Custom type h3cVoMaxCallValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_H3cVoMaxCallValue_Type.__name__ = "Integer32"
_H3cVoMaxCallValue_Object = MibTableColumn
h3cVoMaxCallValue = _H3cVoMaxCallValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 5, 1, 2),
    _H3cVoMaxCallValue_Type()
)
h3cVoMaxCallValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoMaxCallValue.setStatus("current")
_H3cVoMaxCallTableRowStatus_Type = RowStatus
_H3cVoMaxCallTableRowStatus_Object = MibTableColumn
h3cVoMaxCallTableRowStatus = _H3cVoMaxCallTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 5, 1, 3),
    _H3cVoMaxCallTableRowStatus_Type()
)
h3cVoMaxCallTableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoMaxCallTableRowStatus.setStatus("current")
_H3cVoInCallingNumSubstTable_Object = MibTable
h3cVoInCallingNumSubstTable = _H3cVoInCallingNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 6)
)
if mibBuilder.loadTexts:
    h3cVoInCallingNumSubstTable.setStatus("current")
_H3cVoInCallingNumSubstEntry_Object = MibTableRow
h3cVoInCallingNumSubstEntry = _H3cVoInCallingNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 6, 1)
)
h3cVoInCallingNumSubstEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoInCallingNumSubstIndex"),
)
if mibBuilder.loadTexts:
    h3cVoInCallingNumSubstEntry.setStatus("current")


class _H3cVoInCallingNumSubstIndex_Type(Integer32):
    """Custom type h3cVoInCallingNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoInCallingNumSubstIndex_Type.__name__ = "Integer32"
_H3cVoInCallingNumSubstIndex_Object = MibTableColumn
h3cVoInCallingNumSubstIndex = _H3cVoInCallingNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 6, 1, 1),
    _H3cVoInCallingNumSubstIndex_Type()
)
h3cVoInCallingNumSubstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoInCallingNumSubstIndex.setStatus("current")
_H3cVoInCallingSubstRowStatus_Type = RowStatus
_H3cVoInCallingSubstRowStatus_Object = MibTableColumn
h3cVoInCallingSubstRowStatus = _H3cVoInCallingSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 6, 1, 2),
    _H3cVoInCallingSubstRowStatus_Type()
)
h3cVoInCallingSubstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoInCallingSubstRowStatus.setStatus("current")
_H3cVoInCalledNumSubstTable_Object = MibTable
h3cVoInCalledNumSubstTable = _H3cVoInCalledNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 7)
)
if mibBuilder.loadTexts:
    h3cVoInCalledNumSubstTable.setStatus("current")
_H3cVoInCalledNumSubstEntry_Object = MibTableRow
h3cVoInCalledNumSubstEntry = _H3cVoInCalledNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 7, 1)
)
h3cVoInCalledNumSubstEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoInCalledNumSubstIndex"),
)
if mibBuilder.loadTexts:
    h3cVoInCalledNumSubstEntry.setStatus("current")


class _H3cVoInCalledNumSubstIndex_Type(Integer32):
    """Custom type h3cVoInCalledNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoInCalledNumSubstIndex_Type.__name__ = "Integer32"
_H3cVoInCalledNumSubstIndex_Object = MibTableColumn
h3cVoInCalledNumSubstIndex = _H3cVoInCalledNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 7, 1, 1),
    _H3cVoInCalledNumSubstIndex_Type()
)
h3cVoInCalledNumSubstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoInCalledNumSubstIndex.setStatus("current")
_H3cVoInCalledSubstRowStatus_Type = RowStatus
_H3cVoInCalledSubstRowStatus_Object = MibTableColumn
h3cVoInCalledSubstRowStatus = _H3cVoInCalledSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 7, 1, 2),
    _H3cVoInCalledSubstRowStatus_Type()
)
h3cVoInCalledSubstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoInCalledSubstRowStatus.setStatus("current")
_H3cVoOutCallingNumSubstTable_Object = MibTable
h3cVoOutCallingNumSubstTable = _H3cVoOutCallingNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 8)
)
if mibBuilder.loadTexts:
    h3cVoOutCallingNumSubstTable.setStatus("current")
_H3cVoOutCallingNumSubstEntry_Object = MibTableRow
h3cVoOutCallingNumSubstEntry = _H3cVoOutCallingNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 8, 1)
)
h3cVoOutCallingNumSubstEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoOutCallingNumSubstIndex"),
)
if mibBuilder.loadTexts:
    h3cVoOutCallingNumSubstEntry.setStatus("current")


class _H3cVoOutCallingNumSubstIndex_Type(Integer32):
    """Custom type h3cVoOutCallingNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoOutCallingNumSubstIndex_Type.__name__ = "Integer32"
_H3cVoOutCallingNumSubstIndex_Object = MibTableColumn
h3cVoOutCallingNumSubstIndex = _H3cVoOutCallingNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 8, 1, 1),
    _H3cVoOutCallingNumSubstIndex_Type()
)
h3cVoOutCallingNumSubstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoOutCallingNumSubstIndex.setStatus("current")
_H3cVoOutCallingSubstRowStatus_Type = RowStatus
_H3cVoOutCallingSubstRowStatus_Object = MibTableColumn
h3cVoOutCallingSubstRowStatus = _H3cVoOutCallingSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 8, 1, 2),
    _H3cVoOutCallingSubstRowStatus_Type()
)
h3cVoOutCallingSubstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoOutCallingSubstRowStatus.setStatus("current")
_H3cVoOutCalledNumSubstTable_Object = MibTable
h3cVoOutCalledNumSubstTable = _H3cVoOutCalledNumSubstTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 9)
)
if mibBuilder.loadTexts:
    h3cVoOutCalledNumSubstTable.setStatus("current")
_H3cVoOutgoingCalledNumSubstEntry_Object = MibTableRow
h3cVoOutgoingCalledNumSubstEntry = _H3cVoOutgoingCalledNumSubstEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 9, 1)
)
h3cVoOutgoingCalledNumSubstEntry.setIndexNames(
    (0, "H3C-VOGENERAL-MIB", "h3cVoOutCalledNumSubstIndex"),
)
if mibBuilder.loadTexts:
    h3cVoOutgoingCalledNumSubstEntry.setStatus("current")


class _H3cVoOutCalledNumSubstIndex_Type(Integer32):
    """Custom type h3cVoOutCalledNumSubstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cVoOutCalledNumSubstIndex_Type.__name__ = "Integer32"
_H3cVoOutCalledNumSubstIndex_Object = MibTableColumn
h3cVoOutCalledNumSubstIndex = _H3cVoOutCalledNumSubstIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 9, 1, 1),
    _H3cVoOutCalledNumSubstIndex_Type()
)
h3cVoOutCalledNumSubstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cVoOutCalledNumSubstIndex.setStatus("current")
_H3cVoOutCalledSubstRowStatus_Type = RowStatus
_H3cVoOutCalledSubstRowStatus_Object = MibTableColumn
h3cVoOutCalledSubstRowStatus = _H3cVoOutCalledSubstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 39, 1, 9, 1, 2),
    _H3cVoOutCalledSubstRowStatus_Type()
)
h3cVoOutCalledSubstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cVoOutCalledSubstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VOGENERAL-MIB",
    **{"h3cVoiceGeneral": h3cVoiceGeneral,
       "h3cVoiceGeneralObjects": h3cVoiceGeneralObjects,
       "h3cVoGeneralJitterLen": h3cVoGeneralJitterLen,
       "h3cVoGeneralMatchPolicy": h3cVoGeneralMatchPolicy,
       "h3cVoGeneralDataStatistics": h3cVoGeneralDataStatistics,
       "h3cVoGeneralDialTerminator": h3cVoGeneralDialTerminator,
       "h3cVoGeneralCallStart": h3cVoGeneralCallStart,
       "h3cVoGeneralCalledTunnel": h3cVoGeneralCalledTunnel,
       "h3cVoGeneralSpecialService": h3cVoGeneralSpecialService,
       "h3cVoGeneralPeerSearchStop": h3cVoGeneralPeerSearchStop,
       "h3cVoGeneralPeerSelectOrderRule": h3cVoGeneralPeerSelectOrderRule,
       "h3cVoGeneralPeerSelectTypePriority": h3cVoGeneralPeerSelectTypePriority,
       "h3cVoGeneralDscpSignal": h3cVoGeneralDscpSignal,
       "h3cVoGeneralDscpMedia": h3cVoGeneralDscpMedia,
       "h3cVoiceNumberSubstGroup": h3cVoiceNumberSubstGroup,
       "h3cVoNumSubstTable": h3cVoNumSubstTable,
       "h3cVoNumSubstEntry": h3cVoNumSubstEntry,
       "h3cVoNumSubstIndex": h3cVoNumSubstIndex,
       "h3cVoNumSubstFirstRule": h3cVoNumSubstFirstRule,
       "h3cVoNumSubstDotMatchRule": h3cVoNumSubstDotMatchRule,
       "h3cVoNumSubstRowStatus": h3cVoNumSubstRowStatus,
       "h3cVoNumSubstRuleTable": h3cVoNumSubstRuleTable,
       "h3cVoNumSubstRuleEntry": h3cVoNumSubstRuleEntry,
       "h3cVoNumSubstRuleIndex": h3cVoNumSubstRuleIndex,
       "h3cVoNumSubstRuleInputFormat": h3cVoNumSubstRuleInputFormat,
       "h3cVoNumSubstRuleOutputFormat": h3cVoNumSubstRuleOutputFormat,
       "h3cVoNumSubstRuleRowStatus": h3cVoNumSubstRuleRowStatus,
       "h3cVoMaxCallTable": h3cVoMaxCallTable,
       "h3cVoMaxCallEntry": h3cVoMaxCallEntry,
       "h3cVoMaxCallTableIndex": h3cVoMaxCallTableIndex,
       "h3cVoMaxCallValue": h3cVoMaxCallValue,
       "h3cVoMaxCallTableRowStatus": h3cVoMaxCallTableRowStatus,
       "h3cVoInCallingNumSubstTable": h3cVoInCallingNumSubstTable,
       "h3cVoInCallingNumSubstEntry": h3cVoInCallingNumSubstEntry,
       "h3cVoInCallingNumSubstIndex": h3cVoInCallingNumSubstIndex,
       "h3cVoInCallingSubstRowStatus": h3cVoInCallingSubstRowStatus,
       "h3cVoInCalledNumSubstTable": h3cVoInCalledNumSubstTable,
       "h3cVoInCalledNumSubstEntry": h3cVoInCalledNumSubstEntry,
       "h3cVoInCalledNumSubstIndex": h3cVoInCalledNumSubstIndex,
       "h3cVoInCalledSubstRowStatus": h3cVoInCalledSubstRowStatus,
       "h3cVoOutCallingNumSubstTable": h3cVoOutCallingNumSubstTable,
       "h3cVoOutCallingNumSubstEntry": h3cVoOutCallingNumSubstEntry,
       "h3cVoOutCallingNumSubstIndex": h3cVoOutCallingNumSubstIndex,
       "h3cVoOutCallingSubstRowStatus": h3cVoOutCallingSubstRowStatus,
       "h3cVoOutCalledNumSubstTable": h3cVoOutCalledNumSubstTable,
       "h3cVoOutgoingCalledNumSubstEntry": h3cVoOutgoingCalledNumSubstEntry,
       "h3cVoOutCalledNumSubstIndex": h3cVoOutCalledNumSubstIndex,
       "h3cVoOutCalledSubstRowStatus": h3cVoOutCalledSubstRowStatus}
)
