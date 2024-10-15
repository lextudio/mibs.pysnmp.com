# SNMP MIB module (ACC-MULTILINK) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-MULTILINK
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:37 2024
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

(ifOperStatus,) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "ifOperStatus")

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AccMultilink_ObjectIdentity = ObjectIdentity
accMultilink = _AccMultilink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9)
)
_AccMultilinkParameterTable_Object = MibTable
accMultilinkParameterTable = _AccMultilinkParameterTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    accMultilinkParameterTable.setStatus("mandatory")
_AccMultilinkParameterEntry_Object = MibTableRow
accMultilinkParameterEntry = _AccMultilinkParameterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1)
)
accMultilinkParameterEntry.setIndexNames(
    (0, "ACC-MULTILINK", "accMultilinkParameterIndex"),
)
if mibBuilder.loadTexts:
    accMultilinkParameterEntry.setStatus("mandatory")
_AccMultilinkParameterIndex_Type = Integer32
_AccMultilinkParameterIndex_Object = MibTableColumn
accMultilinkParameterIndex = _AccMultilinkParameterIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 1),
    _AccMultilinkParameterIndex_Type()
)
accMultilinkParameterIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterIndex.setStatus("mandatory")
_AccMultilinkParameterIfIndex_Type = Integer32
_AccMultilinkParameterIfIndex_Object = MibTableColumn
accMultilinkParameterIfIndex = _AccMultilinkParameterIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 2),
    _AccMultilinkParameterIfIndex_Type()
)
accMultilinkParameterIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterIfIndex.setStatus("mandatory")


class _AccMultilinkParameterMessageLevel_Type(Integer32):
    """Custom type accMultilinkParameterMessageLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AccMultilinkParameterMessageLevel_Type.__name__ = "Integer32"
_AccMultilinkParameterMessageLevel_Object = MibTableColumn
accMultilinkParameterMessageLevel = _AccMultilinkParameterMessageLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 3),
    _AccMultilinkParameterMessageLevel_Type()
)
accMultilinkParameterMessageLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterMessageLevel.setStatus("mandatory")


class _AccMultilinkParameterAdminState_Type(Integer32):
    """Custom type accMultilinkParameterAdminState based on Integer32"""
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


_AccMultilinkParameterAdminState_Type.__name__ = "Integer32"
_AccMultilinkParameterAdminState_Object = MibTableColumn
accMultilinkParameterAdminState = _AccMultilinkParameterAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 5),
    _AccMultilinkParameterAdminState_Type()
)
accMultilinkParameterAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterAdminState.setStatus("mandatory")


class _AccMultilinkParameterOperState_Type(Integer32):
    """Custom type accMultilinkParameterOperState based on Integer32"""
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
        *(("disabled", 6),
          ("down", 1),
          ("seq-received-ok", 3),
          ("seq-send-ok", 4),
          ("starting", 2),
          ("up", 5))
    )


_AccMultilinkParameterOperState_Type.__name__ = "Integer32"
_AccMultilinkParameterOperState_Object = MibTableColumn
accMultilinkParameterOperState = _AccMultilinkParameterOperState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 6),
    _AccMultilinkParameterOperState_Type()
)
accMultilinkParameterOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkParameterOperState.setStatus("mandatory")


class _AccMultilinkParameterEncapsulation_Type(Integer32):
    """Custom type accMultilinkParameterEncapsulation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acc", 1),
          ("acc-new", 3),
          ("ietf-ppp", 2))
    )


_AccMultilinkParameterEncapsulation_Type.__name__ = "Integer32"
_AccMultilinkParameterEncapsulation_Object = MibTableColumn
accMultilinkParameterEncapsulation = _AccMultilinkParameterEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 7),
    _AccMultilinkParameterEncapsulation_Type()
)
accMultilinkParameterEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterEncapsulation.setStatus("mandatory")


class _AccMultilinkParameterContents_Type(Integer32):
    """Custom type accMultilinkParameterContents based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccMultilinkParameterContents_Type.__name__ = "Integer32"
_AccMultilinkParameterContents_Object = MibTableColumn
accMultilinkParameterContents = _AccMultilinkParameterContents_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 8),
    _AccMultilinkParameterContents_Type()
)
accMultilinkParameterContents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterContents.setStatus("mandatory")
_AccMultilinkParameterPhysicalPort_Type = DisplayString
_AccMultilinkParameterPhysicalPort_Object = MibTableColumn
accMultilinkParameterPhysicalPort = _AccMultilinkParameterPhysicalPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 9),
    _AccMultilinkParameterPhysicalPort_Type()
)
accMultilinkParameterPhysicalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkParameterPhysicalPort.setStatus("mandatory")


class _AccMultilinkParameterCongeToCall_Type(Integer32):
    """Custom type accMultilinkParameterCongeToCall based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 101),
    )


_AccMultilinkParameterCongeToCall_Type.__name__ = "Integer32"
_AccMultilinkParameterCongeToCall_Object = MibTableColumn
accMultilinkParameterCongeToCall = _AccMultilinkParameterCongeToCall_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 10),
    _AccMultilinkParameterCongeToCall_Type()
)
accMultilinkParameterCongeToCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterCongeToCall.setStatus("mandatory")


class _AccMultilinkParameterCongeToClear_Type(Integer32):
    """Custom type accMultilinkParameterCongeToClear based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AccMultilinkParameterCongeToClear_Type.__name__ = "Integer32"
_AccMultilinkParameterCongeToClear_Object = MibTableColumn
accMultilinkParameterCongeToClear = _AccMultilinkParameterCongeToClear_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 11),
    _AccMultilinkParameterCongeToClear_Type()
)
accMultilinkParameterCongeToClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterCongeToClear.setStatus("mandatory")


class _AccMultilinkParameterDampingFactor_Type(Integer32):
    """Custom type accMultilinkParameterDampingFactor based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AccMultilinkParameterDampingFactor_Type.__name__ = "Integer32"
_AccMultilinkParameterDampingFactor_Object = MibTableColumn
accMultilinkParameterDampingFactor = _AccMultilinkParameterDampingFactor_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 12),
    _AccMultilinkParameterDampingFactor_Type()
)
accMultilinkParameterDampingFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterDampingFactor.setStatus("mandatory")


class _AccMultilinkParameterFragmentSize_Type(Integer32):
    """Custom type accMultilinkParameterFragmentSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AccMultilinkParameterFragmentSize_Type.__name__ = "Integer32"
_AccMultilinkParameterFragmentSize_Object = MibTableColumn
accMultilinkParameterFragmentSize = _AccMultilinkParameterFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 13),
    _AccMultilinkParameterFragmentSize_Type()
)
accMultilinkParameterFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterFragmentSize.setStatus("mandatory")


class _AccMultilinkParameterMppAdminState_Type(Integer32):
    """Custom type accMultilinkParameterMppAdminState based on Integer32"""
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


_AccMultilinkParameterMppAdminState_Type.__name__ = "Integer32"
_AccMultilinkParameterMppAdminState_Object = MibTableColumn
accMultilinkParameterMppAdminState = _AccMultilinkParameterMppAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 14),
    _AccMultilinkParameterMppAdminState_Type()
)
accMultilinkParameterMppAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterMppAdminState.setStatus("deprecated")


class _AccMultilinkParameterBWprotocol_Type(Integer32):
    """Custom type accMultilinkParameterBWprotocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AccMultilinkParameterBWprotocol_Type.__name__ = "Integer32"
_AccMultilinkParameterBWprotocol_Object = MibTableColumn
accMultilinkParameterBWprotocol = _AccMultilinkParameterBWprotocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 15),
    _AccMultilinkParameterBWprotocol_Type()
)
accMultilinkParameterBWprotocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterBWprotocol.setStatus("mandatory")


class _AccMultilinkParameterBWprotocolOpSt_Type(Integer32):
    """Custom type accMultilinkParameterBWprotocolOpSt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AccMultilinkParameterBWprotocolOpSt_Type.__name__ = "Integer32"
_AccMultilinkParameterBWprotocolOpSt_Object = MibTableColumn
accMultilinkParameterBWprotocolOpSt = _AccMultilinkParameterBWprotocolOpSt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 1, 1, 16),
    _AccMultilinkParameterBWprotocolOpSt_Type()
)
accMultilinkParameterBWprotocolOpSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterBWprotocolOpSt.setStatus("mandatory")
_AccMlTable_Object = MibTable
accMlTable = _AccMlTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    accMlTable.setStatus("mandatory")
_AccMlEntry_Object = MibTableRow
accMlEntry = _AccMlEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2, 1)
)
accMlEntry.setIndexNames(
    (0, "ACC-MULTILINK", "ifIndex"),
)
if mibBuilder.loadTexts:
    accMlEntry.setStatus("mandatory")


class _AccMlAdminStatus_Type(Integer32):
    """Custom type accMlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1),
          ("undefined", 3))
    )


_AccMlAdminStatus_Type.__name__ = "Integer32"
_AccMlAdminStatus_Object = MibTableColumn
accMlAdminStatus = _AccMlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 2, 1, 7),
    _AccMlAdminStatus_Type()
)
accMlAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMlAdminStatus.setStatus("mandatory")
_AccMultilinkStatTable_Object = MibTable
accMultilinkStatTable = _AccMultilinkStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3)
)
if mibBuilder.loadTexts:
    accMultilinkStatTable.setStatus("mandatory")
_AccMultilinkStatEntry_Object = MibTableRow
accMultilinkStatEntry = _AccMultilinkStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1)
)
accMultilinkStatEntry.setIndexNames(
    (0, "ACC-MULTILINK", "accMultilinkStatIndex"),
)
if mibBuilder.loadTexts:
    accMultilinkStatEntry.setStatus("mandatory")
_AccMultilinkStatIndex_Type = Integer32
_AccMultilinkStatIndex_Object = MibTableColumn
accMultilinkStatIndex = _AccMultilinkStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 1),
    _AccMultilinkStatIndex_Type()
)
accMultilinkStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatIndex.setStatus("mandatory")
_AccMultilinkStatRcvInSeqs_Type = Counter32
_AccMultilinkStatRcvInSeqs_Object = MibTableColumn
accMultilinkStatRcvInSeqs = _AccMultilinkStatRcvInSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 2),
    _AccMultilinkStatRcvInSeqs_Type()
)
accMultilinkStatRcvInSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvInSeqs.setStatus("mandatory")
_AccMultilinkStatRcvOutSeqs_Type = Counter32
_AccMultilinkStatRcvOutSeqs_Object = MibTableColumn
accMultilinkStatRcvOutSeqs = _AccMultilinkStatRcvOutSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 3),
    _AccMultilinkStatRcvOutSeqs_Type()
)
accMultilinkStatRcvOutSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvOutSeqs.setStatus("mandatory")
_AccMultilinkStatRcvOutWindows_Type = Counter32
_AccMultilinkStatRcvOutWindows_Object = MibTableColumn
accMultilinkStatRcvOutWindows = _AccMultilinkStatRcvOutWindows_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 4),
    _AccMultilinkStatRcvOutWindows_Type()
)
accMultilinkStatRcvOutWindows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvOutWindows.setStatus("mandatory")
_AccMultilinkStatRcvSeqBreaks_Type = Counter32
_AccMultilinkStatRcvSeqBreaks_Object = MibTableColumn
accMultilinkStatRcvSeqBreaks = _AccMultilinkStatRcvSeqBreaks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 5),
    _AccMultilinkStatRcvSeqBreaks_Type()
)
accMultilinkStatRcvSeqBreaks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvSeqBreaks.setStatus("mandatory")
_AccMultilinkStatRcvWrongEncaps_Type = Counter32
_AccMultilinkStatRcvWrongEncaps_Object = MibTableColumn
accMultilinkStatRcvWrongEncaps = _AccMultilinkStatRcvWrongEncaps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 6),
    _AccMultilinkStatRcvWrongEncaps_Type()
)
accMultilinkStatRcvWrongEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvWrongEncaps.setStatus("mandatory")
_AccMultilinkStatRcvPendings_Type = Gauge32
_AccMultilinkStatRcvPendings_Object = MibTableColumn
accMultilinkStatRcvPendings = _AccMultilinkStatRcvPendings_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 7),
    _AccMultilinkStatRcvPendings_Type()
)
accMultilinkStatRcvPendings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvPendings.setStatus("mandatory")
_AccMultilinkStatRcvRingColls_Type = Counter32
_AccMultilinkStatRcvRingColls_Object = MibTableColumn
accMultilinkStatRcvRingColls = _AccMultilinkStatRcvRingColls_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 8),
    _AccMultilinkStatRcvRingColls_Type()
)
accMultilinkStatRcvRingColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvRingColls.setStatus("mandatory")
_AccMultilinkStatSendEncapFails_Type = Counter32
_AccMultilinkStatSendEncapFails_Object = MibTableColumn
accMultilinkStatSendEncapFails = _AccMultilinkStatSendEncapFails_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 9),
    _AccMultilinkStatSendEncapFails_Type()
)
accMultilinkStatSendEncapFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendEncapFails.setStatus("mandatory")
_AccMultilinkStatRcvMessages_Type = Counter32
_AccMultilinkStatRcvMessages_Object = MibTableColumn
accMultilinkStatRcvMessages = _AccMultilinkStatRcvMessages_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 10),
    _AccMultilinkStatRcvMessages_Type()
)
accMultilinkStatRcvMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvMessages.setStatus("mandatory")
_AccMultilinkStatRcvUnSeqs_Type = Counter32
_AccMultilinkStatRcvUnSeqs_Object = MibTableColumn
accMultilinkStatRcvUnSeqs = _AccMultilinkStatRcvUnSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 11),
    _AccMultilinkStatRcvUnSeqs_Type()
)
accMultilinkStatRcvUnSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvUnSeqs.setStatus("mandatory")
_AccMultilinkStatRcvSeqs_Type = Counter32
_AccMultilinkStatRcvSeqs_Object = MibTableColumn
accMultilinkStatRcvSeqs = _AccMultilinkStatRcvSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 12),
    _AccMultilinkStatRcvSeqs_Type()
)
accMultilinkStatRcvSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvSeqs.setStatus("mandatory")
_AccMultilinkStatSendMessages_Type = Counter32
_AccMultilinkStatSendMessages_Object = MibTableColumn
accMultilinkStatSendMessages = _AccMultilinkStatSendMessages_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 13),
    _AccMultilinkStatSendMessages_Type()
)
accMultilinkStatSendMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendMessages.setStatus("mandatory")
_AccMultilinkStatSendUnSeqs_Type = Counter32
_AccMultilinkStatSendUnSeqs_Object = MibTableColumn
accMultilinkStatSendUnSeqs = _AccMultilinkStatSendUnSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 14),
    _AccMultilinkStatSendUnSeqs_Type()
)
accMultilinkStatSendUnSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendUnSeqs.setStatus("mandatory")
_AccMultilinkStatSendSeqs_Type = Counter32
_AccMultilinkStatSendSeqs_Object = MibTableColumn
accMultilinkStatSendSeqs = _AccMultilinkStatSendSeqs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 15),
    _AccMultilinkStatSendSeqs_Type()
)
accMultilinkStatSendSeqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendSeqs.setStatus("mandatory")
_AccMultilinkStatRcvSeqNum_Type = Integer32
_AccMultilinkStatRcvSeqNum_Object = MibTableColumn
accMultilinkStatRcvSeqNum = _AccMultilinkStatRcvSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 16),
    _AccMultilinkStatRcvSeqNum_Type()
)
accMultilinkStatRcvSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvSeqNum.setStatus("mandatory")
_AccMultilinkStatSendSeqNum_Type = Integer32
_AccMultilinkStatSendSeqNum_Object = MibTableColumn
accMultilinkStatSendSeqNum = _AccMultilinkStatSendSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 17),
    _AccMultilinkStatSendSeqNum_Type()
)
accMultilinkStatSendSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendSeqNum.setStatus("mandatory")
_AccMultilinkStatSendCongSeqNum_Type = Integer32
_AccMultilinkStatSendCongSeqNum_Object = MibTableColumn
accMultilinkStatSendCongSeqNum = _AccMultilinkStatSendCongSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 18),
    _AccMultilinkStatSendCongSeqNum_Type()
)
accMultilinkStatSendCongSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendCongSeqNum.setStatus("mandatory")
_AccMultilinkStatRcvSeqWraps_Type = Counter32
_AccMultilinkStatRcvSeqWraps_Object = MibTableColumn
accMultilinkStatRcvSeqWraps = _AccMultilinkStatRcvSeqWraps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 19),
    _AccMultilinkStatRcvSeqWraps_Type()
)
accMultilinkStatRcvSeqWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatRcvSeqWraps.setStatus("mandatory")
_AccMultilinkStatSendSeqWraps_Type = Counter32
_AccMultilinkStatSendSeqWraps_Object = MibTableColumn
accMultilinkStatSendSeqWraps = _AccMultilinkStatSendSeqWraps_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 20),
    _AccMultilinkStatSendSeqWraps_Type()
)
accMultilinkStatSendSeqWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatSendSeqWraps.setStatus("mandatory")
_AccMultilinkStatTotalLinks_Type = Gauge32
_AccMultilinkStatTotalLinks_Object = MibTableColumn
accMultilinkStatTotalLinks = _AccMultilinkStatTotalLinks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 21),
    _AccMultilinkStatTotalLinks_Type()
)
accMultilinkStatTotalLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatTotalLinks.setStatus("mandatory")
_AccMultilinkStatActiveLinks_Type = Gauge32
_AccMultilinkStatActiveLinks_Object = MibTableColumn
accMultilinkStatActiveLinks = _AccMultilinkStatActiveLinks_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 22),
    _AccMultilinkStatActiveLinks_Type()
)
accMultilinkStatActiveLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatActiveLinks.setStatus("mandatory")
_AccMultilinkStatTotalBandwidth_Type = Gauge32
_AccMultilinkStatTotalBandwidth_Object = MibTableColumn
accMultilinkStatTotalBandwidth = _AccMultilinkStatTotalBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 23),
    _AccMultilinkStatTotalBandwidth_Type()
)
accMultilinkStatTotalBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatTotalBandwidth.setStatus("mandatory")
_AccMultilinkStatUsedBandwidth_Type = Gauge32
_AccMultilinkStatUsedBandwidth_Object = MibTableColumn
accMultilinkStatUsedBandwidth = _AccMultilinkStatUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 24),
    _AccMultilinkStatUsedBandwidth_Type()
)
accMultilinkStatUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatUsedBandwidth.setStatus("mandatory")
_AccMultilinkStatCallThreshold_Type = Gauge32
_AccMultilinkStatCallThreshold_Object = MibTableColumn
accMultilinkStatCallThreshold = _AccMultilinkStatCallThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 25),
    _AccMultilinkStatCallThreshold_Type()
)
accMultilinkStatCallThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatCallThreshold.setStatus("mandatory")
_AccMultilinkStatClearThreshold_Type = Gauge32
_AccMultilinkStatClearThreshold_Object = MibTableColumn
accMultilinkStatClearThreshold = _AccMultilinkStatClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 3, 1, 26),
    _AccMultilinkStatClearThreshold_Type()
)
accMultilinkStatClearThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMultilinkStatClearThreshold.setStatus("mandatory")
_AccMultilinkStackTable_Object = MibTable
accMultilinkStackTable = _AccMultilinkStackTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4)
)
if mibBuilder.loadTexts:
    accMultilinkStackTable.setStatus("mandatory")
_AccMultilinkStackEntry_Object = MibTableRow
accMultilinkStackEntry = _AccMultilinkStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1)
)
accMultilinkStackEntry.setIndexNames(
    (0, "ACC-MULTILINK", "accMultilinkStackGroup"),
    (0, "ACC-MULTILINK", "accMultilinkStackInterface"),
)
if mibBuilder.loadTexts:
    accMultilinkStackEntry.setStatus("mandatory")
_AccMultilinkStackGroup_Type = Integer32
_AccMultilinkStackGroup_Object = MibTableColumn
accMultilinkStackGroup = _AccMultilinkStackGroup_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1, 1),
    _AccMultilinkStackGroup_Type()
)
accMultilinkStackGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkStackGroup.setStatus("mandatory")
_AccMultilinkStackInterface_Type = Integer32
_AccMultilinkStackInterface_Object = MibTableColumn
accMultilinkStackInterface = _AccMultilinkStackInterface_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 4, 1, 2),
    _AccMultilinkStackInterface_Type()
)
accMultilinkStackInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkStackInterface.setStatus("mandatory")
_AccMlPppProtocolTable_Object = MibTable
accMlPppProtocolTable = _AccMlPppProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5)
)
if mibBuilder.loadTexts:
    accMlPppProtocolTable.setStatus("mandatory")
_AccMlPppProtocolEntry_Object = MibTableRow
accMlPppProtocolEntry = _AccMlPppProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5, 1)
)
accMlPppProtocolEntry.setIndexNames(
    (0, "ACC-MULTILINK", "accMlPppIndex"),
)
if mibBuilder.loadTexts:
    accMlPppProtocolEntry.setStatus("mandatory")
_AccMlPppIndex_Type = Integer32
_AccMlPppIndex_Object = MibTableColumn
accMlPppIndex = _AccMlPppIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5, 1, 1),
    _AccMlPppIndex_Type()
)
accMlPppIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppIndex.setStatus("mandatory")
_AccMlPppProtocol_Type = Integer32
_AccMlPppProtocol_Object = MibTableColumn
accMlPppProtocol = _AccMlPppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5, 1, 2),
    _AccMlPppProtocol_Type()
)
accMlPppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppProtocol.setStatus("mandatory")


class _AccMlPppAdminStatus_Type(Integer32):
    """Custom type accMlPppAdminStatus based on Integer32"""
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


_AccMlPppAdminStatus_Type.__name__ = "Integer32"
_AccMlPppAdminStatus_Object = MibTableColumn
accMlPppAdminStatus = _AccMlPppAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5, 1, 3),
    _AccMlPppAdminStatus_Type()
)
accMlPppAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppAdminStatus.setStatus("mandatory")
_AccMlPppOperStatus_Type = Integer32
_AccMlPppOperStatus_Object = MibTableColumn
accMlPppOperStatus = _AccMlPppOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 5, 1, 4),
    _AccMlPppOperStatus_Type()
)
accMlPppOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accMlPppOperStatus.setStatus("mandatory")


class _AccMultilinkParameterMaxLinkCount_Type(Integer32):
    """Custom type accMultilinkParameterMaxLinkCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_AccMultilinkParameterMaxLinkCount_Type.__name__ = "Integer32"
_AccMultilinkParameterMaxLinkCount_Object = MibScalar
accMultilinkParameterMaxLinkCount = _AccMultilinkParameterMaxLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 6),
    _AccMultilinkParameterMaxLinkCount_Type()
)
accMultilinkParameterMaxLinkCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accMultilinkParameterMaxLinkCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mlStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 0, 1)
)
mlStateChange.setObjects(
      *(("ACC-MULTILINK", "accMultilinkParameterIndex"),
        ("ACC-FAKE", "ifOperStatus"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    mlStateChange.setStatus(
        ""
    )

mlInError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 0, 2)
)
mlInError.setObjects(
      *(("ACC-MULTILINK", "accMultilinkParameterIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    mlInError.setStatus(
        ""
    )

mlOutError = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 0, 3)
)
mlOutError.setObjects(
      *(("ACC-MULTILINK", "accMultilinkParameterIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    mlOutError.setStatus(
        ""
    )

mlDiscard = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 9, 0, 4)
)
mlDiscard.setObjects(
      *(("ACC-MULTILINK", "accMultilinkParameterIndex"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    mlDiscard.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-MULTILINK",
    **{"accMultilink": accMultilink,
       "mlStateChange": mlStateChange,
       "mlInError": mlInError,
       "mlOutError": mlOutError,
       "mlDiscard": mlDiscard,
       "accMultilinkParameterTable": accMultilinkParameterTable,
       "accMultilinkParameterEntry": accMultilinkParameterEntry,
       "accMultilinkParameterIndex": accMultilinkParameterIndex,
       "accMultilinkParameterIfIndex": accMultilinkParameterIfIndex,
       "accMultilinkParameterMessageLevel": accMultilinkParameterMessageLevel,
       "accMultilinkParameterAdminState": accMultilinkParameterAdminState,
       "accMultilinkParameterOperState": accMultilinkParameterOperState,
       "accMultilinkParameterEncapsulation": accMultilinkParameterEncapsulation,
       "accMultilinkParameterContents": accMultilinkParameterContents,
       "accMultilinkParameterPhysicalPort": accMultilinkParameterPhysicalPort,
       "accMultilinkParameterCongeToCall": accMultilinkParameterCongeToCall,
       "accMultilinkParameterCongeToClear": accMultilinkParameterCongeToClear,
       "accMultilinkParameterDampingFactor": accMultilinkParameterDampingFactor,
       "accMultilinkParameterFragmentSize": accMultilinkParameterFragmentSize,
       "accMultilinkParameterMppAdminState": accMultilinkParameterMppAdminState,
       "accMultilinkParameterBWprotocol": accMultilinkParameterBWprotocol,
       "accMultilinkParameterBWprotocolOpSt": accMultilinkParameterBWprotocolOpSt,
       "accMlTable": accMlTable,
       "accMlEntry": accMlEntry,
       "accMlAdminStatus": accMlAdminStatus,
       "accMultilinkStatTable": accMultilinkStatTable,
       "accMultilinkStatEntry": accMultilinkStatEntry,
       "accMultilinkStatIndex": accMultilinkStatIndex,
       "accMultilinkStatRcvInSeqs": accMultilinkStatRcvInSeqs,
       "accMultilinkStatRcvOutSeqs": accMultilinkStatRcvOutSeqs,
       "accMultilinkStatRcvOutWindows": accMultilinkStatRcvOutWindows,
       "accMultilinkStatRcvSeqBreaks": accMultilinkStatRcvSeqBreaks,
       "accMultilinkStatRcvWrongEncaps": accMultilinkStatRcvWrongEncaps,
       "accMultilinkStatRcvPendings": accMultilinkStatRcvPendings,
       "accMultilinkStatRcvRingColls": accMultilinkStatRcvRingColls,
       "accMultilinkStatSendEncapFails": accMultilinkStatSendEncapFails,
       "accMultilinkStatRcvMessages": accMultilinkStatRcvMessages,
       "accMultilinkStatRcvUnSeqs": accMultilinkStatRcvUnSeqs,
       "accMultilinkStatRcvSeqs": accMultilinkStatRcvSeqs,
       "accMultilinkStatSendMessages": accMultilinkStatSendMessages,
       "accMultilinkStatSendUnSeqs": accMultilinkStatSendUnSeqs,
       "accMultilinkStatSendSeqs": accMultilinkStatSendSeqs,
       "accMultilinkStatRcvSeqNum": accMultilinkStatRcvSeqNum,
       "accMultilinkStatSendSeqNum": accMultilinkStatSendSeqNum,
       "accMultilinkStatSendCongSeqNum": accMultilinkStatSendCongSeqNum,
       "accMultilinkStatRcvSeqWraps": accMultilinkStatRcvSeqWraps,
       "accMultilinkStatSendSeqWraps": accMultilinkStatSendSeqWraps,
       "accMultilinkStatTotalLinks": accMultilinkStatTotalLinks,
       "accMultilinkStatActiveLinks": accMultilinkStatActiveLinks,
       "accMultilinkStatTotalBandwidth": accMultilinkStatTotalBandwidth,
       "accMultilinkStatUsedBandwidth": accMultilinkStatUsedBandwidth,
       "accMultilinkStatCallThreshold": accMultilinkStatCallThreshold,
       "accMultilinkStatClearThreshold": accMultilinkStatClearThreshold,
       "accMultilinkStackTable": accMultilinkStackTable,
       "accMultilinkStackEntry": accMultilinkStackEntry,
       "accMultilinkStackGroup": accMultilinkStackGroup,
       "accMultilinkStackInterface": accMultilinkStackInterface,
       "accMlPppProtocolTable": accMlPppProtocolTable,
       "accMlPppProtocolEntry": accMlPppProtocolEntry,
       "accMlPppIndex": accMlPppIndex,
       "accMlPppProtocol": accMlPppProtocol,
       "accMlPppAdminStatus": accMlPppAdminStatus,
       "accMlPppOperStatus": accMlPppOperStatus,
       "accMultilinkParameterMaxLinkCount": accMultilinkParameterMaxLinkCount}
)
