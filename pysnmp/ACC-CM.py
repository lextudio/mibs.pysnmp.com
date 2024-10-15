# SNMP MIB module (ACC-CM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-CM
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:00 2024
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

(ifName,) = mibBuilder.importSymbols(
    "ACC-FAKE",
    "ifName")

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

(accServiceProfileName,) = mibBuilder.importSymbols(
    "ACC-SERVICEPROFILE",
    "accServiceProfileName")

(accIfName,
 accTrapLogSeqNum) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accIfName",
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

_AccCmGroup_ObjectIdentity = ObjectIdentity
accCmGroup = _AccCmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64)
)
_AccCmCallTable_Object = MibTable
accCmCallTable = _AccCmCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1)
)
if mibBuilder.loadTexts:
    accCmCallTable.setStatus("mandatory")
_AccCmCallTableEntry_Object = MibTableRow
accCmCallTableEntry = _AccCmCallTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1)
)
accCmCallTableEntry.setIndexNames(
    (0, "ACC-CM", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    accCmCallTableEntry.setStatus("mandatory")
_AccCmCallIndex_Type = Integer32
_AccCmCallIndex_Object = MibTableColumn
accCmCallIndex = _AccCmCallIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 1),
    _AccCmCallIndex_Type()
)
accCmCallIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallIndex.setStatus("mandatory")
_AccCmCallInfc_Type = OctetString
_AccCmCallInfc_Object = MibTableColumn
accCmCallInfc = _AccCmCallInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 2),
    _AccCmCallInfc_Type()
)
accCmCallInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallInfc.setStatus("mandatory")


class _AccCmDmType_Type(Integer32):
    """Custom type accCmDmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dl2", 4),
          ("isdn", 1),
          ("none", 9),
          ("pstn", 2),
          ("tunnel", 3))
    )


_AccCmDmType_Type.__name__ = "Integer32"
_AccCmDmType_Object = MibTableColumn
accCmDmType = _AccCmDmType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 3),
    _AccCmDmType_Type()
)
accCmDmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmDmType.setStatus("mandatory")
_AccCmEmIndex_Type = OctetString
_AccCmEmIndex_Object = MibTableColumn
accCmEmIndex = _AccCmEmIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 4),
    _AccCmEmIndex_Type()
)
accCmEmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEmIndex.setStatus("mandatory")


class _AccCmEmType_Type(Integer32):
    """Custom type accCmEmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("modem", 2),
          ("none", 9),
          ("pots", 3))
    )


_AccCmEmType_Type.__name__ = "Integer32"
_AccCmEmType_Object = MibTableColumn
accCmEmType = _AccCmEmType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 5),
    _AccCmEmType_Type()
)
accCmEmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEmType.setStatus("mandatory")
_AccCmEmRsrc_Type = OctetString
_AccCmEmRsrc_Object = MibTableColumn
accCmEmRsrc = _AccCmEmRsrc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 6),
    _AccCmEmRsrc_Type()
)
accCmEmRsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEmRsrc.setStatus("mandatory")
_AccCmCallDirn_Type = Integer32
_AccCmCallDirn_Object = MibTableColumn
accCmCallDirn = _AccCmCallDirn_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 7),
    _AccCmCallDirn_Type()
)
accCmCallDirn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallDirn.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 1, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_AccCmTable_Object = MibTable
accCmTable = _AccCmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 2)
)
if mibBuilder.loadTexts:
    accCmTable.setStatus("mandatory")
_AccCmTableEntry_Object = MibTableRow
accCmTableEntry = _AccCmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 2, 1)
)
accCmTableEntry.setIndexNames(
    (0, "ACC-CM", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    accCmTableEntry.setStatus("mandatory")
_AccCmMsgLevel_Type = Integer32
_AccCmMsgLevel_Object = MibTableColumn
accCmMsgLevel = _AccCmMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 2, 1, 1),
    _AccCmMsgLevel_Type()
)
accCmMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCmMsgLevel.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 2, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_AccCmInfcParmTable_Object = MibTable
accCmInfcParmTable = _AccCmInfcParmTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 3)
)
if mibBuilder.loadTexts:
    accCmInfcParmTable.setStatus("mandatory")
_AccCmInfcParmTableEntry_Object = MibTableRow
accCmInfcParmTableEntry = _AccCmInfcParmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 3, 1)
)
accCmInfcParmTableEntry.setIndexNames(
    (0, "ACC-CM", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    accCmInfcParmTableEntry.setStatus("mandatory")
_AccCmInfc_Type = Integer32
_AccCmInfc_Object = MibTableColumn
accCmInfc = _AccCmInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 3, 1, 1),
    _AccCmInfc_Type()
)
accCmInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmInfc.setStatus("mandatory")
_AccCmInfcMsgLevel_Type = Integer32
_AccCmInfcMsgLevel_Object = MibTableColumn
accCmInfcMsgLevel = _AccCmInfcMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 3, 1, 2),
    _AccCmInfcMsgLevel_Type()
)
accCmInfcMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accCmInfcMsgLevel.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 3, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_AccCmCompCallTable_Object = MibTable
accCmCompCallTable = _AccCmCompCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4)
)
if mibBuilder.loadTexts:
    accCmCompCallTable.setStatus("mandatory")
_AccCmCompCallEntry_Object = MibTableRow
accCmCompCallEntry = _AccCmCompCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1)
)
accCmCompCallEntry.setIndexNames(
    (0, "ACC-CM", "accCmCallIdent"),
)
if mibBuilder.loadTexts:
    accCmCompCallEntry.setStatus("mandatory")
_AccCmCallIdent_Type = Integer32
_AccCmCallIdent_Object = MibTableColumn
accCmCallIdent = _AccCmCallIdent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 1),
    _AccCmCallIdent_Type()
)
accCmCallIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallIdent.setStatus("mandatory")


class _AccCmCallSegment_Type(Integer32):
    """Custom type accCmCallSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("permanent", 3))
    )


_AccCmCallSegment_Type.__name__ = "Integer32"
_AccCmCallSegment_Object = MibTableColumn
accCmCallSegment = _AccCmCallSegment_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 2),
    _AccCmCallSegment_Type()
)
accCmCallSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallSegment.setStatus("mandatory")


class _AccCmCallDisposition_Type(Integer32):
    """Custom type accCmCallDisposition based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 6),
          ("authorized", 3),
          ("configured", 4),
          ("disconnected", 9),
          ("permanent", 11),
          ("received", 1),
          ("rejected", 5),
          ("released", 10),
          ("returned", 8),
          ("switched", 7),
          ("validated", 2))
    )


_AccCmCallDisposition_Type.__name__ = "Integer32"
_AccCmCallDisposition_Object = MibTableColumn
accCmCallDisposition = _AccCmCallDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 3),
    _AccCmCallDisposition_Type()
)
accCmCallDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallDisposition.setStatus("mandatory")


class _AccCmCallType_Type(Integer32):
    """Custom type accCmCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              24,
              32,
              48,
              64,
              128,
              256,
              263,
              455,
              134217727,
              134217728)
        )
    )
    namedValues = NamedValues(
        *(("audio", 48),
          ("audio3", 16),
          ("audio7", 32),
          ("circuit", 134217727),
          ("cm56", 2),
          ("cm64", 1),
          ("data", 455),
          ("modem", 24),
          ("multirate", 128),
          ("nband", 263),
          ("packet", 134217728),
          ("rdi", 4),
          ("speech", 8),
          ("udi", 3),
          ("v-110", 256),
          ("wideband", 64))
    )


_AccCmCallType_Type.__name__ = "Integer32"
_AccCmCallType_Object = MibTableColumn
accCmCallType = _AccCmCallType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 4),
    _AccCmCallType_Type()
)
accCmCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallType.setStatus("mandatory")
_AccCmServiceProfile_Type = OctetString
_AccCmServiceProfile_Object = MibTableColumn
accCmServiceProfile = _AccCmServiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 5),
    _AccCmServiceProfile_Type()
)
accCmServiceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmServiceProfile.setStatus("mandatory")


class _AccCmPayloadStatus_Type(Integer32):
    """Custom type accCmPayloadStatus based on Integer32"""
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
        *(("deferred", 2),
          ("established", 4),
          ("establishing", 3),
          ("released", 1),
          ("releasing", 5))
    )


_AccCmPayloadStatus_Type.__name__ = "Integer32"
_AccCmPayloadStatus_Object = MibTableColumn
accCmPayloadStatus = _AccCmPayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 6),
    _AccCmPayloadStatus_Type()
)
accCmPayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmPayloadStatus.setStatus("mandatory")
_AccCmDialInfc_Type = Integer32
_AccCmDialInfc_Object = MibTableColumn
accCmDialInfc = _AccCmDialInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 7),
    _AccCmDialInfc_Type()
)
accCmDialInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmDialInfc.setStatus("mandatory")


class _AccCmDialType_Type(Integer32):
    """Custom type accCmDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dl2", 4),
          ("isdn", 1),
          ("none", 9),
          ("pstn", 2),
          ("ss7", 6),
          ("tunnel", 3),
          ("vna", 5))
    )


_AccCmDialType_Type.__name__ = "Integer32"
_AccCmDialType_Object = MibTableColumn
accCmDialType = _AccCmDialType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 8),
    _AccCmDialType_Type()
)
accCmDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmDialType.setStatus("mandatory")


class _AccCmDialState_Type(Integer32):
    """Custom type accCmDialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              17,
              19,
              25,
              99)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 7),
          ("answered", 8),
          ("busy", 99),
          ("connected", 10),
          ("delivered", 4),
          ("disconn-ind", 12),
          ("disconn-req", 11),
          ("initiated", 1),
          ("offered", 6),
          ("proceeding", 3),
          ("receiving", 25),
          ("releasing", 19),
          ("resume", 17),
          ("routing", 9),
          ("sending", 2),
          ("suspend", 15))
    )


_AccCmDialState_Type.__name__ = "Integer32"
_AccCmDialState_Object = MibTableColumn
accCmDialState = _AccCmDialState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 9),
    _AccCmDialState_Type()
)
accCmDialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmDialState.setStatus("mandatory")
_AccCmEndpointInfc_Type = Integer32
_AccCmEndpointInfc_Object = MibTableColumn
accCmEndpointInfc = _AccCmEndpointInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 10),
    _AccCmEndpointInfc_Type()
)
accCmEndpointInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEndpointInfc.setStatus("mandatory")


class _AccCmEndpointType_Type(Integer32):
    """Custom type accCmEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              127)
        )
    )
    namedValues = NamedValues(
        *(("g-711a", 4),
          ("g-711mu", 3),
          ("g-729a", 5),
          ("hdlc", 1),
          ("modem", 2),
          ("none", 127))
    )


_AccCmEndpointType_Type.__name__ = "Integer32"
_AccCmEndpointType_Object = MibTableColumn
accCmEndpointType = _AccCmEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 11),
    _AccCmEndpointType_Type()
)
accCmEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEndpointType.setStatus("mandatory")


class _AccCmEndpointState_Type(Integer32):
    """Custom type accCmEndpointState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 6),
          ("answered", 7),
          ("assigned", 3),
          ("assigning", 2),
          ("converse", 8),
          ("ready", 5),
          ("released", 1),
          ("releasing", 11),
          ("resume", 10),
          ("setup", 4),
          ("suspend", 9))
    )


_AccCmEndpointState_Type.__name__ = "Integer32"
_AccCmEndpointState_Object = MibTableColumn
accCmEndpointState = _AccCmEndpointState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 12),
    _AccCmEndpointState_Type()
)
accCmEndpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmEndpointState.setStatus("mandatory")
_AccCmCalledNumber_Type = OctetString
_AccCmCalledNumber_Object = MibTableColumn
accCmCalledNumber = _AccCmCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 13),
    _AccCmCalledNumber_Type()
)
accCmCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCalledNumber.setStatus("mandatory")
_AccCmCallingNumber_Type = OctetString
_AccCmCallingNumber_Object = MibTableColumn
accCmCallingNumber = _AccCmCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 14),
    _AccCmCallingNumber_Type()
)
accCmCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallingNumber.setStatus("mandatory")
_AccCmCallDuration_Type = TimeTicks
_AccCmCallDuration_Object = MibTableColumn
accCmCallDuration = _AccCmCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 4, 1, 15),
    _AccCmCallDuration_Type()
)
accCmCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmCallDuration.setStatus("mandatory")
_AccCmNsCallTable_Object = MibTable
accCmNsCallTable = _AccCmNsCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5)
)
if mibBuilder.loadTexts:
    accCmNsCallTable.setStatus("mandatory")
_AccCmNsCallEntry_Object = MibTableRow
accCmNsCallEntry = _AccCmNsCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1)
)
accCmNsCallEntry.setIndexNames(
    (0, "ACC-CM", "accCmNsCallIdent"),
)
if mibBuilder.loadTexts:
    accCmNsCallEntry.setStatus("mandatory")
_AccCmNsCallIdent_Type = Integer32
_AccCmNsCallIdent_Object = MibTableColumn
accCmNsCallIdent = _AccCmNsCallIdent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 1),
    _AccCmNsCallIdent_Type()
)
accCmNsCallIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallIdent.setStatus("mandatory")


class _AccCmNsCallSegment_Type(Integer32):
    """Custom type accCmNsCallSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("permanent", 3))
    )


_AccCmNsCallSegment_Type.__name__ = "Integer32"
_AccCmNsCallSegment_Object = MibTableColumn
accCmNsCallSegment = _AccCmNsCallSegment_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 2),
    _AccCmNsCallSegment_Type()
)
accCmNsCallSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallSegment.setStatus("mandatory")


class _AccCmNsCallDisposition_Type(Integer32):
    """Custom type accCmNsCallDisposition based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 6),
          ("authorized", 3),
          ("configured", 4),
          ("disconnected", 9),
          ("permanent", 11),
          ("received", 1),
          ("rejected", 5),
          ("released", 10),
          ("returned", 8),
          ("switched", 7),
          ("validated", 2))
    )


_AccCmNsCallDisposition_Type.__name__ = "Integer32"
_AccCmNsCallDisposition_Object = MibTableColumn
accCmNsCallDisposition = _AccCmNsCallDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 3),
    _AccCmNsCallDisposition_Type()
)
accCmNsCallDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallDisposition.setStatus("mandatory")


class _AccCmNsCallType_Type(Integer32):
    """Custom type accCmNsCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              24,
              32,
              48,
              64,
              128,
              256,
              263,
              455,
              134217727,
              134217728)
        )
    )
    namedValues = NamedValues(
        *(("audio", 48),
          ("audio3", 16),
          ("audio7", 32),
          ("circuit", 134217727),
          ("cm56", 2),
          ("cm64", 1),
          ("data", 455),
          ("modem", 24),
          ("multirate", 128),
          ("nband", 263),
          ("packet", 134217728),
          ("rdi", 4),
          ("speech", 8),
          ("udi", 3),
          ("v-110", 256),
          ("wideband", 64))
    )


_AccCmNsCallType_Type.__name__ = "Integer32"
_AccCmNsCallType_Object = MibTableColumn
accCmNsCallType = _AccCmNsCallType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 4),
    _AccCmNsCallType_Type()
)
accCmNsCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallType.setStatus("mandatory")
_AccCmNsServiceProfile_Type = OctetString
_AccCmNsServiceProfile_Object = MibTableColumn
accCmNsServiceProfile = _AccCmNsServiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 5),
    _AccCmNsServiceProfile_Type()
)
accCmNsServiceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsServiceProfile.setStatus("mandatory")


class _AccCmNsPayloadStatus_Type(Integer32):
    """Custom type accCmNsPayloadStatus based on Integer32"""
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
        *(("deferred", 2),
          ("established", 4),
          ("establishing", 3),
          ("released", 1),
          ("releasing", 5))
    )


_AccCmNsPayloadStatus_Type.__name__ = "Integer32"
_AccCmNsPayloadStatus_Object = MibTableColumn
accCmNsPayloadStatus = _AccCmNsPayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 6),
    _AccCmNsPayloadStatus_Type()
)
accCmNsPayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsPayloadStatus.setStatus("mandatory")
_AccCmNsDialInfc_Type = Integer32
_AccCmNsDialInfc_Object = MibTableColumn
accCmNsDialInfc = _AccCmNsDialInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 7),
    _AccCmNsDialInfc_Type()
)
accCmNsDialInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsDialInfc.setStatus("mandatory")


class _AccCmNsDialType_Type(Integer32):
    """Custom type accCmNsDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              127)
        )
    )
    namedValues = NamedValues(
        *(("dl2", 4),
          ("isdn", 1),
          ("none", 127),
          ("pstn", 2),
          ("ss7", 6),
          ("tunnel", 3),
          ("vna", 5))
    )


_AccCmNsDialType_Type.__name__ = "Integer32"
_AccCmNsDialType_Object = MibTableColumn
accCmNsDialType = _AccCmNsDialType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 8),
    _AccCmNsDialType_Type()
)
accCmNsDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsDialType.setStatus("mandatory")


class _AccCmNsDialState_Type(Integer32):
    """Custom type accCmNsDialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              17,
              19,
              25,
              99)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 7),
          ("answered", 8),
          ("busy", 99),
          ("connected", 10),
          ("delivered", 4),
          ("disconn-ind", 12),
          ("disconn-req", 11),
          ("initiated", 1),
          ("offered", 6),
          ("proceeding", 3),
          ("receiving", 25),
          ("releasing", 19),
          ("resume", 17),
          ("routing", 9),
          ("sending", 2),
          ("suspend", 15))
    )


_AccCmNsDialState_Type.__name__ = "Integer32"
_AccCmNsDialState_Object = MibTableColumn
accCmNsDialState = _AccCmNsDialState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 9),
    _AccCmNsDialState_Type()
)
accCmNsDialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsDialState.setStatus("mandatory")
_AccCmNsEndpointInfc_Type = Integer32
_AccCmNsEndpointInfc_Object = MibTableColumn
accCmNsEndpointInfc = _AccCmNsEndpointInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 10),
    _AccCmNsEndpointInfc_Type()
)
accCmNsEndpointInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsEndpointInfc.setStatus("mandatory")


class _AccCmNsEndpointType_Type(Integer32):
    """Custom type accCmNsEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              127)
        )
    )
    namedValues = NamedValues(
        *(("g-711a", 4),
          ("g-711mu", 3),
          ("g-729a", 5),
          ("hdlc", 1),
          ("modem", 2),
          ("none", 127))
    )


_AccCmNsEndpointType_Type.__name__ = "Integer32"
_AccCmNsEndpointType_Object = MibTableColumn
accCmNsEndpointType = _AccCmNsEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 11),
    _AccCmNsEndpointType_Type()
)
accCmNsEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsEndpointType.setStatus("mandatory")


class _AccCmNsEndpointState_Type(Integer32):
    """Custom type accCmNsEndpointState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 6),
          ("answered", 7),
          ("assigned", 3),
          ("assigning", 2),
          ("converse", 8),
          ("ready", 5),
          ("released", 1),
          ("releasing", 11),
          ("resume", 10),
          ("setup", 4),
          ("suspend", 9))
    )


_AccCmNsEndpointState_Type.__name__ = "Integer32"
_AccCmNsEndpointState_Object = MibTableColumn
accCmNsEndpointState = _AccCmNsEndpointState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 12),
    _AccCmNsEndpointState_Type()
)
accCmNsEndpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsEndpointState.setStatus("mandatory")
_AccCmNsCalledNumber_Type = OctetString
_AccCmNsCalledNumber_Object = MibTableColumn
accCmNsCalledNumber = _AccCmNsCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 13),
    _AccCmNsCalledNumber_Type()
)
accCmNsCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCalledNumber.setStatus("mandatory")
_AccCmNsCallingNumber_Type = OctetString
_AccCmNsCallingNumber_Object = MibTableColumn
accCmNsCallingNumber = _AccCmNsCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 14),
    _AccCmNsCallingNumber_Type()
)
accCmNsCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallingNumber.setStatus("mandatory")
_AccCmNsCallDuration_Type = TimeTicks
_AccCmNsCallDuration_Object = MibTableColumn
accCmNsCallDuration = _AccCmNsCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 5, 1, 15),
    _AccCmNsCallDuration_Type()
)
accCmNsCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmNsCallDuration.setStatus("mandatory")
_AccCmSwCallTable_Object = MibTable
accCmSwCallTable = _AccCmSwCallTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6)
)
if mibBuilder.loadTexts:
    accCmSwCallTable.setStatus("mandatory")
_AccCmSwCallEntry_Object = MibTableRow
accCmSwCallEntry = _AccCmSwCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1)
)
accCmSwCallEntry.setIndexNames(
    (0, "ACC-CM", "accCmSwCallIdent"),
)
if mibBuilder.loadTexts:
    accCmSwCallEntry.setStatus("mandatory")
_AccCmSwCallIdent_Type = Integer32
_AccCmSwCallIdent_Object = MibTableColumn
accCmSwCallIdent = _AccCmSwCallIdent_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 1),
    _AccCmSwCallIdent_Type()
)
accCmSwCallIdent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallIdent.setStatus("mandatory")


class _AccCmSwCallSegment_Type(Integer32):
    """Custom type accCmSwCallSegment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 1),
          ("outgoing", 2),
          ("permanent", 3))
    )


_AccCmSwCallSegment_Type.__name__ = "Integer32"
_AccCmSwCallSegment_Object = MibTableColumn
accCmSwCallSegment = _AccCmSwCallSegment_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 2),
    _AccCmSwCallSegment_Type()
)
accCmSwCallSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallSegment.setStatus("mandatory")


class _AccCmSwCallDisposition_Type(Integer32):
    """Custom type accCmSwCallDisposition based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 6),
          ("authorized", 3),
          ("configured", 4),
          ("disconnected", 9),
          ("permanent", 11),
          ("received", 1),
          ("rejected", 5),
          ("released", 10),
          ("returned", 8),
          ("switched", 7),
          ("validated", 2))
    )


_AccCmSwCallDisposition_Type.__name__ = "Integer32"
_AccCmSwCallDisposition_Object = MibTableColumn
accCmSwCallDisposition = _AccCmSwCallDisposition_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 3),
    _AccCmSwCallDisposition_Type()
)
accCmSwCallDisposition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallDisposition.setStatus("mandatory")


class _AccCmSwCallType_Type(Integer32):
    """Custom type accCmSwCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              16,
              24,
              32,
              48,
              64,
              128,
              256,
              263,
              455,
              134217727,
              134217728)
        )
    )
    namedValues = NamedValues(
        *(("audio", 48),
          ("audio3", 16),
          ("audio7", 32),
          ("circuit", 134217727),
          ("cm56", 2),
          ("cm64", 1),
          ("data", 455),
          ("modem", 24),
          ("multirate", 128),
          ("nband", 263),
          ("packet", 134217728),
          ("rdi", 4),
          ("speech", 8),
          ("udi", 3),
          ("v-110", 256),
          ("wideband", 64))
    )


_AccCmSwCallType_Type.__name__ = "Integer32"
_AccCmSwCallType_Object = MibTableColumn
accCmSwCallType = _AccCmSwCallType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 4),
    _AccCmSwCallType_Type()
)
accCmSwCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallType.setStatus("mandatory")
_AccCmSwServiceProfile_Type = OctetString
_AccCmSwServiceProfile_Object = MibTableColumn
accCmSwServiceProfile = _AccCmSwServiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 5),
    _AccCmSwServiceProfile_Type()
)
accCmSwServiceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwServiceProfile.setStatus("mandatory")


class _AccCmSwPayloadStatus_Type(Integer32):
    """Custom type accCmSwPayloadStatus based on Integer32"""
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
        *(("deferred", 2),
          ("established", 4),
          ("establishing", 3),
          ("released", 1),
          ("releasing", 5))
    )


_AccCmSwPayloadStatus_Type.__name__ = "Integer32"
_AccCmSwPayloadStatus_Object = MibTableColumn
accCmSwPayloadStatus = _AccCmSwPayloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 6),
    _AccCmSwPayloadStatus_Type()
)
accCmSwPayloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwPayloadStatus.setStatus("mandatory")
_AccCmSwDialInfc_Type = Integer32
_AccCmSwDialInfc_Object = MibTableColumn
accCmSwDialInfc = _AccCmSwDialInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 7),
    _AccCmSwDialInfc_Type()
)
accCmSwDialInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwDialInfc.setStatus("mandatory")


class _AccCmSwDialType_Type(Integer32):
    """Custom type accCmSwDialType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dl2", 4),
          ("isdn", 1),
          ("none", 9),
          ("pstn", 2),
          ("ss7", 6),
          ("tunnel", 3),
          ("vna", 5))
    )


_AccCmSwDialType_Type.__name__ = "Integer32"
_AccCmSwDialType_Object = MibTableColumn
accCmSwDialType = _AccCmSwDialType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 8),
    _AccCmSwDialType_Type()
)
accCmSwDialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwDialType.setStatus("mandatory")


class _AccCmSwDialState_Type(Integer32):
    """Custom type accCmSwDialState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              15,
              17,
              19,
              25,
              99)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 7),
          ("answered", 8),
          ("busy", 99),
          ("connected", 10),
          ("delivered", 4),
          ("disconn-ind", 12),
          ("disconn-req", 11),
          ("initiated", 1),
          ("offered", 6),
          ("proceeding", 3),
          ("receiving", 25),
          ("releasing", 19),
          ("resume", 17),
          ("routing", 9),
          ("sending", 2),
          ("suspend", 15))
    )


_AccCmSwDialState_Type.__name__ = "Integer32"
_AccCmSwDialState_Object = MibTableColumn
accCmSwDialState = _AccCmSwDialState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 9),
    _AccCmSwDialState_Type()
)
accCmSwDialState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwDialState.setStatus("mandatory")
_AccCmSwEndpointInfc_Type = Integer32
_AccCmSwEndpointInfc_Object = MibTableColumn
accCmSwEndpointInfc = _AccCmSwEndpointInfc_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 10),
    _AccCmSwEndpointInfc_Type()
)
accCmSwEndpointInfc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwEndpointInfc.setStatus("mandatory")


class _AccCmSwEndpointType_Type(Integer32):
    """Custom type accCmSwEndpointType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              127)
        )
    )
    namedValues = NamedValues(
        *(("g-711a", 4),
          ("g-711mu", 3),
          ("g-729a", 5),
          ("hdlc", 1),
          ("modem", 2),
          ("none", 127))
    )


_AccCmSwEndpointType_Type.__name__ = "Integer32"
_AccCmSwEndpointType_Object = MibTableColumn
accCmSwEndpointType = _AccCmSwEndpointType_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 11),
    _AccCmSwEndpointType_Type()
)
accCmSwEndpointType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwEndpointType.setStatus("mandatory")


class _AccCmSwEndpointState_Type(Integer32):
    """Custom type accCmSwEndpointState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("alerting", 6),
          ("answered", 7),
          ("assigned", 3),
          ("assigning", 2),
          ("converse", 8),
          ("ready", 5),
          ("released", 1),
          ("releasing", 11),
          ("resume", 10),
          ("setup", 4),
          ("suspend", 9))
    )


_AccCmSwEndpointState_Type.__name__ = "Integer32"
_AccCmSwEndpointState_Object = MibTableColumn
accCmSwEndpointState = _AccCmSwEndpointState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 12),
    _AccCmSwEndpointState_Type()
)
accCmSwEndpointState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwEndpointState.setStatus("mandatory")
_AccCmSwCalledNumber_Type = OctetString
_AccCmSwCalledNumber_Object = MibTableColumn
accCmSwCalledNumber = _AccCmSwCalledNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 13),
    _AccCmSwCalledNumber_Type()
)
accCmSwCalledNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCalledNumber.setStatus("mandatory")
_AccCmSwCallingNumber_Type = OctetString
_AccCmSwCallingNumber_Object = MibTableColumn
accCmSwCallingNumber = _AccCmSwCallingNumber_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 14),
    _AccCmSwCallingNumber_Type()
)
accCmSwCallingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallingNumber.setStatus("mandatory")
_AccCmSwCallDuration_Type = TimeTicks
_AccCmSwCallDuration_Object = MibTableColumn
accCmSwCallDuration = _AccCmSwCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 6, 1, 15),
    _AccCmSwCallDuration_Type()
)
accCmSwCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmSwCallDuration.setStatus("mandatory")
_AccCmTraps_ObjectIdentity = ObjectIdentity
accCmTraps = _AccCmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7)
)
_AccCmTrapMsg_Type = DisplayString
_AccCmTrapMsg_Object = MibScalar
accCmTrapMsg = _AccCmTrapMsg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 1),
    _AccCmTrapMsg_Type()
)
accCmTrapMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accCmTrapMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

accCmEvntBlockedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 1)
)
accCmEvntBlockedTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmEvntBlockedTrap.setStatus(
        ""
    )

accStaleCallCntxtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 2)
)
accStaleCallCntxtTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accStaleCallCntxtTrap.setStatus(
        ""
    )

accCmUnExpectedEvntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 3)
)
accCmUnExpectedEvntTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmUnExpectedEvntTrap.setStatus(
        ""
    )

accCmEmEvntWOCntxtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 4)
)
accCmEmEvntWOCntxtTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmEmEvntWOCntxtTrap.setStatus(
        ""
    )

accCmUnXpctdEmEventTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 5)
)
accCmUnXpctdEmEventTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmUnXpctdEmEventTrap.setStatus(
        ""
    )

accCmSwitchingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 6)
)
accCmSwitchingTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmSwitchingTrap.setStatus(
        ""
    )

accCmDms1StatusIndTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 7)
)
accCmDms1StatusIndTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmDms1StatusIndTrap.setStatus(
        ""
    )

accCmSpConflictPhysPortTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 8)
)
accCmSpConflictPhysPortTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SERVICEPROFILE", "accServiceProfileName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmSpConflictPhysPortTrap.setStatus(
        ""
    )

accCmSpInconsDynTunnelingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 9)
)
accCmSpInconsDynTunnelingTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmSpInconsDynTunnelingTrap.setStatus(
        ""
    )

accCmRedundantReqTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 10)
)
accCmRedundantReqTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmRedundantReqTrap.setStatus(
        ""
    )

accCmNoMemTunnelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 11)
)
accCmNoMemTunnelTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmNoMemTunnelTrap.setStatus(
        ""
    )

accCmUnExpctdDmEvntInDmStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 12)
)
accCmUnExpctdDmEvntInDmStateTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmUnExpctdDmEvntInDmStateTrap.setStatus(
        ""
    )

accCmUnExpctdDmEvntWOCntxtTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 13)
)
accCmUnExpctdDmEvntWOCntxtTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmUnExpctdDmEvntWOCntxtTrap.setStatus(
        ""
    )

accCmPayldPathTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 14)
)
accCmPayldPathTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmPayldPathTrap.setStatus(
        ""
    )

accCmUnXpctedRelatedEvntTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 15)
)
accCmUnXpctedRelatedEvntTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmUnXpctedRelatedEvntTrap.setStatus(
        ""
    )

accCmNoPayLdPathTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 16)
)
accCmNoPayLdPathTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmNoPayLdPathTrap.setStatus(
        ""
    )

accCmForcdCallRlsStalldTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 17)
)
accCmForcdCallRlsStalldTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmForcdCallRlsStalldTrap.setStatus(
        ""
    )

accCmGrmdCallTypeInvalidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 18)
)
accCmGrmdCallTypeInvalidTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmGrmdCallTypeInvalidTrap.setStatus(
        ""
    )

accCmGrmdCallTypeAbmigsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 64, 7, 0, 19)
)
accCmGrmdCallTypeAbmigsTrap.setObjects(
      *(("ACC-CM", "accCmTrapMsg"),
        ("ACC-SYSTEM", "accIfName"),
        ("ACC-SYSTEM", "accTrapLogSeqNum"))
)
if mibBuilder.loadTexts:
    accCmGrmdCallTypeAbmigsTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-CM",
    **{"accCmGroup": accCmGroup,
       "accCmCallTable": accCmCallTable,
       "accCmCallTableEntry": accCmCallTableEntry,
       "accCmCallIndex": accCmCallIndex,
       "accCmCallInfc": accCmCallInfc,
       "accCmDmType": accCmDmType,
       "accCmEmIndex": accCmEmIndex,
       "accCmEmType": accCmEmType,
       "accCmEmRsrc": accCmEmRsrc,
       "accCmCallDirn": accCmCallDirn,
       "pysmiFakeCol1": pysmiFakeCol1,
       "accCmTable": accCmTable,
       "accCmTableEntry": accCmTableEntry,
       "accCmMsgLevel": accCmMsgLevel,
       "pysmiFakeCol2": pysmiFakeCol2,
       "accCmInfcParmTable": accCmInfcParmTable,
       "accCmInfcParmTableEntry": accCmInfcParmTableEntry,
       "accCmInfc": accCmInfc,
       "accCmInfcMsgLevel": accCmInfcMsgLevel,
       "pysmiFakeCol3": pysmiFakeCol3,
       "accCmCompCallTable": accCmCompCallTable,
       "accCmCompCallEntry": accCmCompCallEntry,
       "accCmCallIdent": accCmCallIdent,
       "accCmCallSegment": accCmCallSegment,
       "accCmCallDisposition": accCmCallDisposition,
       "accCmCallType": accCmCallType,
       "accCmServiceProfile": accCmServiceProfile,
       "accCmPayloadStatus": accCmPayloadStatus,
       "accCmDialInfc": accCmDialInfc,
       "accCmDialType": accCmDialType,
       "accCmDialState": accCmDialState,
       "accCmEndpointInfc": accCmEndpointInfc,
       "accCmEndpointType": accCmEndpointType,
       "accCmEndpointState": accCmEndpointState,
       "accCmCalledNumber": accCmCalledNumber,
       "accCmCallingNumber": accCmCallingNumber,
       "accCmCallDuration": accCmCallDuration,
       "accCmNsCallTable": accCmNsCallTable,
       "accCmNsCallEntry": accCmNsCallEntry,
       "accCmNsCallIdent": accCmNsCallIdent,
       "accCmNsCallSegment": accCmNsCallSegment,
       "accCmNsCallDisposition": accCmNsCallDisposition,
       "accCmNsCallType": accCmNsCallType,
       "accCmNsServiceProfile": accCmNsServiceProfile,
       "accCmNsPayloadStatus": accCmNsPayloadStatus,
       "accCmNsDialInfc": accCmNsDialInfc,
       "accCmNsDialType": accCmNsDialType,
       "accCmNsDialState": accCmNsDialState,
       "accCmNsEndpointInfc": accCmNsEndpointInfc,
       "accCmNsEndpointType": accCmNsEndpointType,
       "accCmNsEndpointState": accCmNsEndpointState,
       "accCmNsCalledNumber": accCmNsCalledNumber,
       "accCmNsCallingNumber": accCmNsCallingNumber,
       "accCmNsCallDuration": accCmNsCallDuration,
       "accCmSwCallTable": accCmSwCallTable,
       "accCmSwCallEntry": accCmSwCallEntry,
       "accCmSwCallIdent": accCmSwCallIdent,
       "accCmSwCallSegment": accCmSwCallSegment,
       "accCmSwCallDisposition": accCmSwCallDisposition,
       "accCmSwCallType": accCmSwCallType,
       "accCmSwServiceProfile": accCmSwServiceProfile,
       "accCmSwPayloadStatus": accCmSwPayloadStatus,
       "accCmSwDialInfc": accCmSwDialInfc,
       "accCmSwDialType": accCmSwDialType,
       "accCmSwDialState": accCmSwDialState,
       "accCmSwEndpointInfc": accCmSwEndpointInfc,
       "accCmSwEndpointType": accCmSwEndpointType,
       "accCmSwEndpointState": accCmSwEndpointState,
       "accCmSwCalledNumber": accCmSwCalledNumber,
       "accCmSwCallingNumber": accCmSwCallingNumber,
       "accCmSwCallDuration": accCmSwCallDuration,
       "accCmTraps": accCmTraps,
       "accCmEvntBlockedTrap": accCmEvntBlockedTrap,
       "accStaleCallCntxtTrap": accStaleCallCntxtTrap,
       "accCmUnExpectedEvntTrap": accCmUnExpectedEvntTrap,
       "accCmEmEvntWOCntxtTrap": accCmEmEvntWOCntxtTrap,
       "accCmUnXpctdEmEventTrap": accCmUnXpctdEmEventTrap,
       "accCmSwitchingTrap": accCmSwitchingTrap,
       "accCmDms1StatusIndTrap": accCmDms1StatusIndTrap,
       "accCmSpConflictPhysPortTrap": accCmSpConflictPhysPortTrap,
       "accCmSpInconsDynTunnelingTrap": accCmSpInconsDynTunnelingTrap,
       "accCmRedundantReqTrap": accCmRedundantReqTrap,
       "accCmNoMemTunnelTrap": accCmNoMemTunnelTrap,
       "accCmUnExpctdDmEvntInDmStateTrap": accCmUnExpctdDmEvntInDmStateTrap,
       "accCmUnExpctdDmEvntWOCntxtTrap": accCmUnExpctdDmEvntWOCntxtTrap,
       "accCmPayldPathTrap": accCmPayldPathTrap,
       "accCmUnXpctedRelatedEvntTrap": accCmUnXpctedRelatedEvntTrap,
       "accCmNoPayLdPathTrap": accCmNoPayLdPathTrap,
       "accCmForcdCallRlsStalldTrap": accCmForcdCallRlsStalldTrap,
       "accCmGrmdCallTypeInvalidTrap": accCmGrmdCallTypeInvalidTrap,
       "accCmGrmdCallTypeAbmigsTrap": accCmGrmdCallTypeAbmigsTrap,
       "accCmTrapMsg": accCmTrapMsg}
)
