# SNMP MIB module (TERAWAVE-teraU-ds3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraU-ds3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:21 2024
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
 enterprises,
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
    "enterprises",
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

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_TeraUDs3Group_ObjectIdentity = ObjectIdentity
teraUDs3Group = _TeraUDs3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 15)
)
_TeraUds3ConfigTable_Object = MibTable
teraUds3ConfigTable = _TeraUds3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1)
)
if mibBuilder.loadTexts:
    teraUds3ConfigTable.setStatus("mandatory")
_TeraUds3ConfigTableEntry_Object = MibTableRow
teraUds3ConfigTableEntry = _TeraUds3ConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1)
)
teraUds3ConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"),
)
if mibBuilder.loadTexts:
    teraUds3ConfigTableEntry.setStatus("mandatory")
_TeraUds3LineIndex_Type = Integer32
_TeraUds3LineIndex_Object = MibTableColumn
teraUds3LineIndex = _TeraUds3LineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 1),
    _TeraUds3LineIndex_Type()
)
teraUds3LineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3LineIndex.setStatus("mandatory")


class _TeraUds3TimeElasped_Type(Integer32):
    """Custom type teraUds3TimeElasped based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_TeraUds3TimeElasped_Type.__name__ = "Integer32"
_TeraUds3TimeElasped_Object = MibTableColumn
teraUds3TimeElasped = _TeraUds3TimeElasped_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 2),
    _TeraUds3TimeElasped_Type()
)
teraUds3TimeElasped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3TimeElasped.setStatus("mandatory")


class _TeraUds3ValidIntervals_Type(Integer32):
    """Custom type teraUds3ValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_TeraUds3ValidIntervals_Type.__name__ = "Integer32"
_TeraUds3ValidIntervals_Object = MibTableColumn
teraUds3ValidIntervals = _TeraUds3ValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 3),
    _TeraUds3ValidIntervals_Type()
)
teraUds3ValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ValidIntervals.setStatus("mandatory")


class _TeraUds3LineType_Type(Integer32):
    """Custom type teraUds3LineType based on Integer32"""
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
        *(("cbitParity", 2),
          ("e3-G-751", 3),
          ("e3-G-832", 4),
          ("m23", 1))
    )


_TeraUds3LineType_Type.__name__ = "Integer32"
_TeraUds3LineType_Object = MibTableColumn
teraUds3LineType = _TeraUds3LineType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 4),
    _TeraUds3LineType_Type()
)
teraUds3LineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3LineType.setStatus("mandatory")


class _TeraUds3ATMMapping_Type(Integer32):
    """Custom type teraUds3ATMMapping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct-Mapping", 2),
          ("pLCP", 1))
    )


_TeraUds3ATMMapping_Type.__name__ = "Integer32"
_TeraUds3ATMMapping_Object = MibTableColumn
teraUds3ATMMapping = _TeraUds3ATMMapping_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 5),
    _TeraUds3ATMMapping_Type()
)
teraUds3ATMMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3ATMMapping.setStatus("mandatory")


class _TeraUds3LineCoding_Type(Integer32):
    """Custom type teraUds3LineCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b3ZS", 2),
          ("hDB3", 3),
          ("other", 1))
    )


_TeraUds3LineCoding_Type.__name__ = "Integer32"
_TeraUds3LineCoding_Object = MibTableColumn
teraUds3LineCoding = _TeraUds3LineCoding_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 6),
    _TeraUds3LineCoding_Type()
)
teraUds3LineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3LineCoding.setStatus("mandatory")
_TeraUds3CircuitIdentifier_Type = OctetString
_TeraUds3CircuitIdentifier_Object = MibTableColumn
teraUds3CircuitIdentifier = _TeraUds3CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 7),
    _TeraUds3CircuitIdentifier_Type()
)
teraUds3CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3CircuitIdentifier.setStatus("mandatory")


class _TeraUds3LoopbackConfig_Type(Integer32):
    """Custom type teraUds3LoopbackConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              32)
        )
    )
    namedValues = NamedValues(
        *(("equipped", 32),
          ("facility", 4),
          ("noLoop", 1))
    )


_TeraUds3LoopbackConfig_Type.__name__ = "Integer32"
_TeraUds3LoopbackConfig_Object = MibTableColumn
teraUds3LoopbackConfig = _TeraUds3LoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 8),
    _TeraUds3LoopbackConfig_Type()
)
teraUds3LoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3LoopbackConfig.setStatus("mandatory")


class _TeraUds3LineStatus_Type(Integer32):
    """Custom type teraUds3LineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("lOF", 32),
          ("lOS", 64),
          ("loopbackState", 128),
          ("netEquipOOS", 2048),
          ("noAlarm", 1),
          ("otherFailure", 512),
          ("rcvAIS", 8),
          ("rcvRAIFailure", 2),
          ("rcvTestCode", 256),
          ("unavailSigState", 1024),
          ("xmitAIS", 16),
          ("xmtRAIAlarm", 4))
    )


_TeraUds3LineStatus_Type.__name__ = "Integer32"
_TeraUds3LineStatus_Object = MibTableColumn
teraUds3LineStatus = _TeraUds3LineStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 9),
    _TeraUds3LineStatus_Type()
)
teraUds3LineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3LineStatus.setStatus("mandatory")


class _TeraUds3TransmitClockSource_Type(Integer32):
    """Custom type teraUds3TransmitClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localTiming", 2),
          ("loopTiming", 1),
          ("throughTiming", 3))
    )


_TeraUds3TransmitClockSource_Type.__name__ = "Integer32"
_TeraUds3TransmitClockSource_Object = MibTableColumn
teraUds3TransmitClockSource = _TeraUds3TransmitClockSource_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 10),
    _TeraUds3TransmitClockSource_Type()
)
teraUds3TransmitClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3TransmitClockSource.setStatus("mandatory")


class _TeraUds3InvalidIntervals_Type(Integer32):
    """Custom type teraUds3InvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_TeraUds3InvalidIntervals_Type.__name__ = "Integer32"
_TeraUds3InvalidIntervals_Object = MibTableColumn
teraUds3InvalidIntervals = _TeraUds3InvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 11),
    _TeraUds3InvalidIntervals_Type()
)
teraUds3InvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3InvalidIntervals.setStatus("mandatory")


class _TeraUds3LineLength_Type(Integer32):
    """Custom type teraUds3LineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ft-250", 1),
          ("ft-450", 2))
    )


_TeraUds3LineLength_Type.__name__ = "Integer32"
_TeraUds3LineLength_Object = MibTableColumn
teraUds3LineLength = _TeraUds3LineLength_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 12),
    _TeraUds3LineLength_Type()
)
teraUds3LineLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3LineLength.setStatus("mandatory")


class _TeraUds3LoopbackStatus_Type(Integer32):
    """Custom type teraUds3LoopbackStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              64)
        )
    )
    namedValues = NamedValues(
        *(("farEndLineLoopback", 64),
          ("nearEndLineLoopback", 4),
          ("nearEndPayloadLoopback", 2),
          ("noLoopback", 1))
    )


_TeraUds3LoopbackStatus_Type.__name__ = "Integer32"
_TeraUds3LoopbackStatus_Object = MibTableColumn
teraUds3LoopbackStatus = _TeraUds3LoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 13),
    _TeraUds3LoopbackStatus_Type()
)
teraUds3LoopbackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3LoopbackStatus.setStatus("mandatory")


class _TeraUds3FarEndLineLoopbackTimeout_Type(Integer32):
    """Custom type teraUds3FarEndLineLoopbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 71581),
    )


_TeraUds3FarEndLineLoopbackTimeout_Type.__name__ = "Integer32"
_TeraUds3FarEndLineLoopbackTimeout_Object = MibTableColumn
teraUds3FarEndLineLoopbackTimeout = _TeraUds3FarEndLineLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 14),
    _TeraUds3FarEndLineLoopbackTimeout_Type()
)
teraUds3FarEndLineLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3FarEndLineLoopbackTimeout.setStatus("mandatory")


class _TeraUds3SendFarEndLoopback_Type(Integer32):
    """Custom type teraUds3SendFarEndLoopback based on Integer32"""
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
        *(("cancelLoopback", 4),
          ("none", 1),
          ("sendDisable", 3),
          ("sendEnable", 2))
    )


_TeraUds3SendFarEndLoopback_Type.__name__ = "Integer32"
_TeraUds3SendFarEndLoopback_Object = MibTableColumn
teraUds3SendFarEndLoopback = _TeraUds3SendFarEndLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 1, 1, 15),
    _TeraUds3SendFarEndLoopback_Type()
)
teraUds3SendFarEndLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3SendFarEndLoopback.setStatus("mandatory")
_TeraUds3BERTConfigTable_Object = MibTable
teraUds3BERTConfigTable = _TeraUds3BERTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2)
)
if mibBuilder.loadTexts:
    teraUds3BERTConfigTable.setStatus("mandatory")
_TeraUds3BERTConfigTableEntry_Object = MibTableRow
teraUds3BERTConfigTableEntry = _TeraUds3BERTConfigTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1)
)
teraUds3BERTConfigTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"),
)
if mibBuilder.loadTexts:
    teraUds3BERTConfigTableEntry.setStatus("mandatory")


class _TeraUds3BERTPattern_Type(Integer32):
    """Custom type teraUds3BERTPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("qRSS", 3),
          ("user", 2))
    )


_TeraUds3BERTPattern_Type.__name__ = "Integer32"
_TeraUds3BERTPattern_Object = MibTableColumn
teraUds3BERTPattern = _TeraUds3BERTPattern_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 1),
    _TeraUds3BERTPattern_Type()
)
teraUds3BERTPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3BERTPattern.setStatus("mandatory")
_TeraUds3BERTUserPattern_Type = OctetString
_TeraUds3BERTUserPattern_Object = MibTableColumn
teraUds3BERTUserPattern = _TeraUds3BERTUserPattern_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 2),
    _TeraUds3BERTUserPattern_Type()
)
teraUds3BERTUserPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3BERTUserPattern.setStatus("mandatory")


class _TeraUds3BERTSyncInfo_Type(Integer32):
    """Custom type teraUds3BERTSyncInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("n-a", 1),
          ("no", 3),
          ("yes", 2))
    )


_TeraUds3BERTSyncInfo_Type.__name__ = "Integer32"
_TeraUds3BERTSyncInfo_Object = MibTableColumn
teraUds3BERTSyncInfo = _TeraUds3BERTSyncInfo_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 3),
    _TeraUds3BERTSyncInfo_Type()
)
teraUds3BERTSyncInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3BERTSyncInfo.setStatus("mandatory")
_TeraUds3BERT_ES_Type = Counter32
_TeraUds3BERT_ES_Object = MibScalar
teraUds3BERT_ES = _TeraUds3BERT_ES_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 4),
    _TeraUds3BERT_ES_Type()
)
teraUds3BERT_ES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3BERT_ES.setStatus("mandatory")
_TeraUds3BERT_BES_Type = Counter32
_TeraUds3BERT_BES_Object = MibScalar
teraUds3BERT_BES = _TeraUds3BERT_BES_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 5),
    _TeraUds3BERT_BES_Type()
)
teraUds3BERT_BES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3BERT_BES.setStatus("mandatory")
_TeraUds3BERT_BER_Type = Counter32
_TeraUds3BERT_BER_Object = MibScalar
teraUds3BERT_BER = _TeraUds3BERT_BER_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 2, 1, 6),
    _TeraUds3BERT_BER_Type()
)
teraUds3BERT_BER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3BERT_BER.setStatus("mandatory")
_TeraUds3ExtendTotalTable_Object = MibTable
teraUds3ExtendTotalTable = _TeraUds3ExtendTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3)
)
if mibBuilder.loadTexts:
    teraUds3ExtendTotalTable.setStatus("mandatory")
_TeraUds3ExtendTotalTableEntry_Object = MibTableRow
teraUds3ExtendTotalTableEntry = _TeraUds3ExtendTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1)
)
teraUds3ExtendTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3ExtendTotalIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3ExtendTotalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3ExtendTotalTableEntry.setStatus("mandatory")
_TeraUds3ExtendTotalIndex_Type = Integer32
_TeraUds3ExtendTotalIndex_Object = MibTableColumn
teraUds3ExtendTotalIndex = _TeraUds3ExtendTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 1),
    _TeraUds3ExtendTotalIndex_Type()
)
teraUds3ExtendTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalIndex.setStatus("mandatory")


class _TeraUds3ExtendTotalNumber_Type(Integer32):
    """Custom type teraUds3ExtendTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraUds3ExtendTotalNumber_Type.__name__ = "Integer32"
_TeraUds3ExtendTotalNumber_Object = MibTableColumn
teraUds3ExtendTotalNumber = _TeraUds3ExtendTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 2),
    _TeraUds3ExtendTotalNumber_Type()
)
teraUds3ExtendTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalNumber.setStatus("mandatory")
_TeraUds3ExtendTotalPESs_Type = Gauge32
_TeraUds3ExtendTotalPESs_Object = MibTableColumn
teraUds3ExtendTotalPESs = _TeraUds3ExtendTotalPESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 3),
    _TeraUds3ExtendTotalPESs_Type()
)
teraUds3ExtendTotalPESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalPESs.setStatus("mandatory")
_TeraUds3ExtendTotalPSESs_Type = Gauge32
_TeraUds3ExtendTotalPSESs_Object = MibTableColumn
teraUds3ExtendTotalPSESs = _TeraUds3ExtendTotalPSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 4),
    _TeraUds3ExtendTotalPSESs_Type()
)
teraUds3ExtendTotalPSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalPSESs.setStatus("mandatory")
_TeraUds3ExtendTotalSEFSs_Type = Gauge32
_TeraUds3ExtendTotalSEFSs_Object = MibTableColumn
teraUds3ExtendTotalSEFSs = _TeraUds3ExtendTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 5),
    _TeraUds3ExtendTotalSEFSs_Type()
)
teraUds3ExtendTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalSEFSs.setStatus("mandatory")
_TeraUds3ExtendTotalUASs_Type = Gauge32
_TeraUds3ExtendTotalUASs_Object = MibTableColumn
teraUds3ExtendTotalUASs = _TeraUds3ExtendTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 6),
    _TeraUds3ExtendTotalUASs_Type()
)
teraUds3ExtendTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalUASs.setStatus("mandatory")
_TeraUds3ExtendTotalLCVs_Type = Gauge32
_TeraUds3ExtendTotalLCVs_Object = MibTableColumn
teraUds3ExtendTotalLCVs = _TeraUds3ExtendTotalLCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 7),
    _TeraUds3ExtendTotalLCVs_Type()
)
teraUds3ExtendTotalLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalLCVs.setStatus("mandatory")
_TeraUds3ExtendTotalPCVs_Type = Gauge32
_TeraUds3ExtendTotalPCVs_Object = MibTableColumn
teraUds3ExtendTotalPCVs = _TeraUds3ExtendTotalPCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 8),
    _TeraUds3ExtendTotalPCVs_Type()
)
teraUds3ExtendTotalPCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalPCVs.setStatus("mandatory")
_TeraUds3ExtendTotalLESs_Type = Gauge32
_TeraUds3ExtendTotalLESs_Object = MibTableColumn
teraUds3ExtendTotalLESs = _TeraUds3ExtendTotalLESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 9),
    _TeraUds3ExtendTotalLESs_Type()
)
teraUds3ExtendTotalLESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalLESs.setStatus("mandatory")
_TeraUds3ExtendTotalCCVs_Type = Gauge32
_TeraUds3ExtendTotalCCVs_Object = MibTableColumn
teraUds3ExtendTotalCCVs = _TeraUds3ExtendTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 10),
    _TeraUds3ExtendTotalCCVs_Type()
)
teraUds3ExtendTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalCCVs.setStatus("mandatory")
_TeraUds3ExtendTotalCESs_Type = Gauge32
_TeraUds3ExtendTotalCESs_Object = MibTableColumn
teraUds3ExtendTotalCESs = _TeraUds3ExtendTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 11),
    _TeraUds3ExtendTotalCESs_Type()
)
teraUds3ExtendTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalCESs.setStatus("mandatory")
_TeraUds3ExtendTotalCSESs_Type = Gauge32
_TeraUds3ExtendTotalCSESs_Object = MibTableColumn
teraUds3ExtendTotalCSESs = _TeraUds3ExtendTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 12),
    _TeraUds3ExtendTotalCSESs_Type()
)
teraUds3ExtendTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalCSESs.setStatus("mandatory")
_TeraUds3ExtendTotalValidData_Type = Integer32
_TeraUds3ExtendTotalValidData_Object = MibTableColumn
teraUds3ExtendTotalValidData = _TeraUds3ExtendTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 3, 1, 13),
    _TeraUds3ExtendTotalValidData_Type()
)
teraUds3ExtendTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3ExtendTotalValidData.setStatus("mandatory")
_TeraUds3FarEndExtendTotalTable_Object = MibTable
teraUds3FarEndExtendTotalTable = _TeraUds3FarEndExtendTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4)
)
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalTable.setStatus("mandatory")
_TeraUds3FarEndExtendTotalTableEntry_Object = MibTableRow
teraUds3FarEndExtendTotalTableEntry = _TeraUds3FarEndExtendTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1)
)
teraUds3FarEndExtendTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3FarEndExtendTotalIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3FarEndExtendTotalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalTableEntry.setStatus("mandatory")
_TeraUds3FarEndExtendTotalIndex_Type = Integer32
_TeraUds3FarEndExtendTotalIndex_Object = MibTableColumn
teraUds3FarEndExtendTotalIndex = _TeraUds3FarEndExtendTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 1),
    _TeraUds3FarEndExtendTotalIndex_Type()
)
teraUds3FarEndExtendTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalIndex.setStatus("mandatory")


class _TeraUds3FarEndExtendTotalNumber_Type(Integer32):
    """Custom type teraUds3FarEndExtendTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraUds3FarEndExtendTotalNumber_Type.__name__ = "Integer32"
_TeraUds3FarEndExtendTotalNumber_Object = MibTableColumn
teraUds3FarEndExtendTotalNumber = _TeraUds3FarEndExtendTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 2),
    _TeraUds3FarEndExtendTotalNumber_Type()
)
teraUds3FarEndExtendTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalNumber.setStatus("mandatory")
_TeraUds3FarEndExtendTotalCESs_Type = Gauge32
_TeraUds3FarEndExtendTotalCESs_Object = MibTableColumn
teraUds3FarEndExtendTotalCESs = _TeraUds3FarEndExtendTotalCESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 3),
    _TeraUds3FarEndExtendTotalCESs_Type()
)
teraUds3FarEndExtendTotalCESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalCESs.setStatus("mandatory")
_TeraUds3FarEndExtendTotalCSESs_Type = Gauge32
_TeraUds3FarEndExtendTotalCSESs_Object = MibTableColumn
teraUds3FarEndExtendTotalCSESs = _TeraUds3FarEndExtendTotalCSESs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 4),
    _TeraUds3FarEndExtendTotalCSESs_Type()
)
teraUds3FarEndExtendTotalCSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalCSESs.setStatus("mandatory")
_TeraUds3FarEndExtendTotalCCVs_Type = Gauge32
_TeraUds3FarEndExtendTotalCCVs_Object = MibTableColumn
teraUds3FarEndExtendTotalCCVs = _TeraUds3FarEndExtendTotalCCVs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 5),
    _TeraUds3FarEndExtendTotalCCVs_Type()
)
teraUds3FarEndExtendTotalCCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalCCVs.setStatus("mandatory")
_TeraUds3FarEndExtendTotalUASs_Type = Gauge32
_TeraUds3FarEndExtendTotalUASs_Object = MibTableColumn
teraUds3FarEndExtendTotalUASs = _TeraUds3FarEndExtendTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 6),
    _TeraUds3FarEndExtendTotalUASs_Type()
)
teraUds3FarEndExtendTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalUASs.setStatus("mandatory")
_TeraUds3FarEndExtendTotalValidData_Type = Integer32
_TeraUds3FarEndExtendTotalValidData_Object = MibTableColumn
teraUds3FarEndExtendTotalValidData = _TeraUds3FarEndExtendTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 4, 1, 7),
    _TeraUds3FarEndExtendTotalValidData_Type()
)
teraUds3FarEndExtendTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3FarEndExtendTotalValidData.setStatus("mandatory")
_TeraUds3atmInterfacePlcpIntervalTable_Object = MibTable
teraUds3atmInterfacePlcpIntervalTable = _TeraUds3atmInterfacePlcpIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalTable.setStatus("mandatory")
_TeraUds3atmInterfacePlcpIntervalTableEntry_Object = MibTableRow
teraUds3atmInterfacePlcpIntervalTableEntry = _TeraUds3atmInterfacePlcpIntervalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1)
)
teraUds3atmInterfacePlcpIntervalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfacePlcpIntervalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalTableEntry.setStatus("mandatory")


class _TeraUds3atmInterfacePlcpIntervalNumber_Type(Integer32):
    """Custom type teraUds3atmInterfacePlcpIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeraUds3atmInterfacePlcpIntervalNumber_Type.__name__ = "Integer32"
_TeraUds3atmInterfacePlcpIntervalNumber_Object = MibTableColumn
teraUds3atmInterfacePlcpIntervalNumber = _TeraUds3atmInterfacePlcpIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 1),
    _TeraUds3atmInterfacePlcpIntervalNumber_Type()
)
teraUds3atmInterfacePlcpIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalNumber.setStatus("mandatory")
_TeraUds3atmInterfacePlcpIntervalSEFSs_Type = Counter32
_TeraUds3atmInterfacePlcpIntervalSEFSs_Object = MibTableColumn
teraUds3atmInterfacePlcpIntervalSEFSs = _TeraUds3atmInterfacePlcpIntervalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 2),
    _TeraUds3atmInterfacePlcpIntervalSEFSs_Type()
)
teraUds3atmInterfacePlcpIntervalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalSEFSs.setStatus("mandatory")


class _TeraUds3atmInterfacePlcpIntervalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfacePlcpIntervalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incomingLOF", 2),
          ("noAlarm", 0),
          ("receivedFarEndAlarm", 1))
    )


_TeraUds3atmInterfacePlcpIntervalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfacePlcpIntervalAlarmState_Object = MibTableColumn
teraUds3atmInterfacePlcpIntervalAlarmState = _TeraUds3atmInterfacePlcpIntervalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 3),
    _TeraUds3atmInterfacePlcpIntervalAlarmState_Type()
)
teraUds3atmInterfacePlcpIntervalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfacePlcpIntervalUASs_Type = Counter32
_TeraUds3atmInterfacePlcpIntervalUASs_Object = MibTableColumn
teraUds3atmInterfacePlcpIntervalUASs = _TeraUds3atmInterfacePlcpIntervalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 4),
    _TeraUds3atmInterfacePlcpIntervalUASs_Type()
)
teraUds3atmInterfacePlcpIntervalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalUASs.setStatus("mandatory")
_TeraUds3atmInterfacePlcpIntervalValidData_Type = Integer32
_TeraUds3atmInterfacePlcpIntervalValidData_Object = MibTableColumn
teraUds3atmInterfacePlcpIntervalValidData = _TeraUds3atmInterfacePlcpIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 5, 1, 5),
    _TeraUds3atmInterfacePlcpIntervalValidData_Type()
)
teraUds3atmInterfacePlcpIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpIntervalValidData.setStatus("mandatory")
_TeraUds3atmInterfacePlcpTotalTable_Object = MibTable
teraUds3atmInterfacePlcpTotalTable = _TeraUds3atmInterfacePlcpTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 6)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpTotalTable.setStatus("mandatory")
_TeraUds3atmInterfacePlcpTotalTableEntry_Object = MibTableRow
teraUds3atmInterfacePlcpTotalTableEntry = _TeraUds3atmInterfacePlcpTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 6, 1)
)
teraUds3atmInterfacePlcpTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpTotalTableEntry.setStatus("mandatory")
_TeraUds3atmInterfacePlcpTotalSEFSs_Type = Counter32
_TeraUds3atmInterfacePlcpTotalSEFSs_Object = MibTableColumn
teraUds3atmInterfacePlcpTotalSEFSs = _TeraUds3atmInterfacePlcpTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 1),
    _TeraUds3atmInterfacePlcpTotalSEFSs_Type()
)
teraUds3atmInterfacePlcpTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpTotalSEFSs.setStatus("mandatory")


class _TeraUds3atmInterfacePlcpTotalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfacePlcpTotalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incomingLOF", 2),
          ("noAlarm", 0),
          ("receivedFarEndAlarm", 1))
    )


_TeraUds3atmInterfacePlcpTotalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfacePlcpTotalAlarmState_Object = MibTableColumn
teraUds3atmInterfacePlcpTotalAlarmState = _TeraUds3atmInterfacePlcpTotalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 2),
    _TeraUds3atmInterfacePlcpTotalAlarmState_Type()
)
teraUds3atmInterfacePlcpTotalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpTotalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfacePlcpTotalUASs_Type = Counter32
_TeraUds3atmInterfacePlcpTotalUASs_Object = MibTableColumn
teraUds3atmInterfacePlcpTotalUASs = _TeraUds3atmInterfacePlcpTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 6, 1, 3),
    _TeraUds3atmInterfacePlcpTotalUASs_Type()
)
teraUds3atmInterfacePlcpTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpTotalUASs.setStatus("mandatory")
_TeraUds3atmInterfacePlcpExtendTotalTable_Object = MibTable
teraUds3atmInterfacePlcpExtendTotalTable = _TeraUds3atmInterfacePlcpExtendTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalTable.setStatus("mandatory")
_TeraUds3atmInterfacePlcpExtendTotalTableEntry_Object = MibTableRow
teraUds3atmInterfacePlcpExtendTotalTableEntry = _TeraUds3atmInterfacePlcpExtendTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1)
)
teraUds3atmInterfacePlcpExtendTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfacePlcpExtendTotalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalTableEntry.setStatus("mandatory")


class _TeraUds3atmInterfacePlcpExtendTotalNumber_Type(Integer32):
    """Custom type teraUds3atmInterfacePlcpExtendTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraUds3atmInterfacePlcpExtendTotalNumber_Type.__name__ = "Integer32"
_TeraUds3atmInterfacePlcpExtendTotalNumber_Object = MibTableColumn
teraUds3atmInterfacePlcpExtendTotalNumber = _TeraUds3atmInterfacePlcpExtendTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 1),
    _TeraUds3atmInterfacePlcpExtendTotalNumber_Type()
)
teraUds3atmInterfacePlcpExtendTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalNumber.setStatus("mandatory")
_TeraUds3atmInterfacePlcpExtendTotalSEFSs_Type = Counter32
_TeraUds3atmInterfacePlcpExtendTotalSEFSs_Object = MibTableColumn
teraUds3atmInterfacePlcpExtendTotalSEFSs = _TeraUds3atmInterfacePlcpExtendTotalSEFSs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 2),
    _TeraUds3atmInterfacePlcpExtendTotalSEFSs_Type()
)
teraUds3atmInterfacePlcpExtendTotalSEFSs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalSEFSs.setStatus("mandatory")


class _TeraUds3atmInterfacePlcpExtendTotalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfacePlcpExtendTotalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("incomingLOF", 2),
          ("noAlarm", 0),
          ("receivedFarEndAlarm", 1))
    )


_TeraUds3atmInterfacePlcpExtendTotalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfacePlcpExtendTotalAlarmState_Object = MibTableColumn
teraUds3atmInterfacePlcpExtendTotalAlarmState = _TeraUds3atmInterfacePlcpExtendTotalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 3),
    _TeraUds3atmInterfacePlcpExtendTotalAlarmState_Type()
)
teraUds3atmInterfacePlcpExtendTotalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfacePlcpExtendTotalUASs_Type = Counter32
_TeraUds3atmInterfacePlcpExtendTotalUASs_Object = MibTableColumn
teraUds3atmInterfacePlcpExtendTotalUASs = _TeraUds3atmInterfacePlcpExtendTotalUASs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 4),
    _TeraUds3atmInterfacePlcpExtendTotalUASs_Type()
)
teraUds3atmInterfacePlcpExtendTotalUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalUASs.setStatus("mandatory")
_TeraUds3atmInterfacePlcpExtendTotalValidData_Type = Integer32
_TeraUds3atmInterfacePlcpExtendTotalValidData_Object = MibTableColumn
teraUds3atmInterfacePlcpExtendTotalValidData = _TeraUds3atmInterfacePlcpExtendTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 7, 1, 5),
    _TeraUds3atmInterfacePlcpExtendTotalValidData_Type()
)
teraUds3atmInterfacePlcpExtendTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfacePlcpExtendTotalValidData.setStatus("mandatory")
_TeraUds3atmInterfaceTCIntervalTable_Object = MibTable
teraUds3atmInterfaceTCIntervalTable = _TeraUds3atmInterfaceTCIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalTable.setStatus("mandatory")
_TeraUds3atmInterfaceTCIntervalTableEntry_Object = MibTableRow
teraUds3atmInterfaceTCIntervalTableEntry = _TeraUds3atmInterfaceTCIntervalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8, 1)
)
teraUds3atmInterfaceTCIntervalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfaceTCIntervalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalTableEntry.setStatus("mandatory")


class _TeraUds3atmInterfaceTCIntervalNumber_Type(Integer32):
    """Custom type teraUds3atmInterfaceTCIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_TeraUds3atmInterfaceTCIntervalNumber_Type.__name__ = "Integer32"
_TeraUds3atmInterfaceTCIntervalNumber_Object = MibTableColumn
teraUds3atmInterfaceTCIntervalNumber = _TeraUds3atmInterfaceTCIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 1),
    _TeraUds3atmInterfaceTCIntervalNumber_Type()
)
teraUds3atmInterfaceTCIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalNumber.setStatus("mandatory")
_TeraUds3atmInterfaceTCIntervalOCDEvents_Type = Counter32
_TeraUds3atmInterfaceTCIntervalOCDEvents_Object = MibTableColumn
teraUds3atmInterfaceTCIntervalOCDEvents = _TeraUds3atmInterfaceTCIntervalOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 2),
    _TeraUds3atmInterfaceTCIntervalOCDEvents_Type()
)
teraUds3atmInterfaceTCIntervalOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalOCDEvents.setStatus("mandatory")


class _TeraUds3atmInterfaceTCIntervalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfaceTCIntervalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdFailure", 2),
          ("noAlarm", 1))
    )


_TeraUds3atmInterfaceTCIntervalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfaceTCIntervalAlarmState_Object = MibTableColumn
teraUds3atmInterfaceTCIntervalAlarmState = _TeraUds3atmInterfaceTCIntervalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 3),
    _TeraUds3atmInterfaceTCIntervalAlarmState_Type()
)
teraUds3atmInterfaceTCIntervalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfaceTCIntervalValidData_Type = Integer32
_TeraUds3atmInterfaceTCIntervalValidData_Object = MibTableColumn
teraUds3atmInterfaceTCIntervalValidData = _TeraUds3atmInterfaceTCIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 8, 1, 4),
    _TeraUds3atmInterfaceTCIntervalValidData_Type()
)
teraUds3atmInterfaceTCIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCIntervalValidData.setStatus("mandatory")
_TeraUds3atmInterfaceTCTotalTable_Object = MibTable
teraUds3atmInterfaceTCTotalTable = _TeraUds3atmInterfaceTCTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 9)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCTotalTable.setStatus("mandatory")
_TeraUds3atmInterfaceTCTotalTableEntry_Object = MibTableRow
teraUds3atmInterfaceTCTotalTableEntry = _TeraUds3atmInterfaceTCTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 9, 1)
)
teraUds3atmInterfaceTCTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCTotalTableEntry.setStatus("mandatory")
_TeraUds3atmInterfaceTCTotalOCDEvents_Type = Counter32
_TeraUds3atmInterfaceTCTotalOCDEvents_Object = MibTableColumn
teraUds3atmInterfaceTCTotalOCDEvents = _TeraUds3atmInterfaceTCTotalOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 9, 1, 1),
    _TeraUds3atmInterfaceTCTotalOCDEvents_Type()
)
teraUds3atmInterfaceTCTotalOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCTotalOCDEvents.setStatus("mandatory")


class _TeraUds3atmInterfaceTCTotalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfaceTCTotalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdFailure", 2),
          ("noAlarm", 1))
    )


_TeraUds3atmInterfaceTCTotalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfaceTCTotalAlarmState_Object = MibTableColumn
teraUds3atmInterfaceTCTotalAlarmState = _TeraUds3atmInterfaceTCTotalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 9, 1, 2),
    _TeraUds3atmInterfaceTCTotalAlarmState_Type()
)
teraUds3atmInterfaceTCTotalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCTotalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfaceTCExtendTotalTable_Object = MibTable
teraUds3atmInterfaceTCExtendTotalTable = _TeraUds3atmInterfaceTCExtendTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10)
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalTable.setStatus("mandatory")
_TeraUds3atmInterfaceTCExtendTotalTableEntry_Object = MibTableRow
teraUds3atmInterfaceTCExtendTotalTableEntry = _TeraUds3atmInterfaceTCExtendTotalTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10, 1)
)
teraUds3atmInterfaceTCExtendTotalTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "ifIndex"),
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3atmInterfaceTCExtendTotalNumber"),
)
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalTableEntry.setStatus("mandatory")


class _TeraUds3atmInterfaceTCExtendTotalNumber_Type(Integer32):
    """Custom type teraUds3atmInterfaceTCExtendTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_TeraUds3atmInterfaceTCExtendTotalNumber_Type.__name__ = "Integer32"
_TeraUds3atmInterfaceTCExtendTotalNumber_Object = MibTableColumn
teraUds3atmInterfaceTCExtendTotalNumber = _TeraUds3atmInterfaceTCExtendTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 1),
    _TeraUds3atmInterfaceTCExtendTotalNumber_Type()
)
teraUds3atmInterfaceTCExtendTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalNumber.setStatus("mandatory")
_TeraUds3atmInterfaceTCExtendTotalOCDEvents_Type = Counter32
_TeraUds3atmInterfaceTCExtendTotalOCDEvents_Object = MibTableColumn
teraUds3atmInterfaceTCExtendTotalOCDEvents = _TeraUds3atmInterfaceTCExtendTotalOCDEvents_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 2),
    _TeraUds3atmInterfaceTCExtendTotalOCDEvents_Type()
)
teraUds3atmInterfaceTCExtendTotalOCDEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalOCDEvents.setStatus("mandatory")


class _TeraUds3atmInterfaceTCExtendTotalAlarmState_Type(Integer32):
    """Custom type teraUds3atmInterfaceTCExtendTotalAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lcdFailure", 2),
          ("noAlarm", 1))
    )


_TeraUds3atmInterfaceTCExtendTotalAlarmState_Type.__name__ = "Integer32"
_TeraUds3atmInterfaceTCExtendTotalAlarmState_Object = MibTableColumn
teraUds3atmInterfaceTCExtendTotalAlarmState = _TeraUds3atmInterfaceTCExtendTotalAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 3),
    _TeraUds3atmInterfaceTCExtendTotalAlarmState_Type()
)
teraUds3atmInterfaceTCExtendTotalAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalAlarmState.setStatus("mandatory")
_TeraUds3atmInterfaceTCExtendTotalValidData_Type = Integer32
_TeraUds3atmInterfaceTCExtendTotalValidData_Object = MibTableColumn
teraUds3atmInterfaceTCExtendTotalValidData = _TeraUds3atmInterfaceTCExtendTotalValidData_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 10, 1, 4),
    _TeraUds3atmInterfaceTCExtendTotalValidData_Type()
)
teraUds3atmInterfaceTCExtendTotalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraUds3atmInterfaceTCExtendTotalValidData.setStatus("mandatory")
_TeraUds3PMControlTable_Object = MibTable
teraUds3PMControlTable = _TeraUds3PMControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 11)
)
if mibBuilder.loadTexts:
    teraUds3PMControlTable.setStatus("mandatory")
_TeraUds3PMControlTableEntry_Object = MibTableRow
teraUds3PMControlTableEntry = _TeraUds3PMControlTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 11, 1)
)
teraUds3PMControlTableEntry.setIndexNames(
    (0, "TERAWAVE-teraU-ds3-MIB", "teraUds3LineIndex"),
)
if mibBuilder.loadTexts:
    teraUds3PMControlTableEntry.setStatus("mandatory")


class _TeraUds3PMControlClearAll_Type(Integer32):
    """Custom type teraUds3PMControlClearAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("ok", 1))
    )


_TeraUds3PMControlClearAll_Type.__name__ = "Integer32"
_TeraUds3PMControlClearAll_Object = MibTableColumn
teraUds3PMControlClearAll = _TeraUds3PMControlClearAll_Object(
    (1, 3, 6, 1, 4, 1, 4513, 15, 11, 1, 1),
    _TeraUds3PMControlClearAll_Type()
)
teraUds3PMControlClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teraUds3PMControlClearAll.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraU-ds3-MIB",
    **{"terawave": terawave,
       "teraUDs3Group": teraUDs3Group,
       "teraUds3ConfigTable": teraUds3ConfigTable,
       "teraUds3ConfigTableEntry": teraUds3ConfigTableEntry,
       "teraUds3LineIndex": teraUds3LineIndex,
       "teraUds3TimeElasped": teraUds3TimeElasped,
       "teraUds3ValidIntervals": teraUds3ValidIntervals,
       "teraUds3LineType": teraUds3LineType,
       "teraUds3ATMMapping": teraUds3ATMMapping,
       "teraUds3LineCoding": teraUds3LineCoding,
       "teraUds3CircuitIdentifier": teraUds3CircuitIdentifier,
       "teraUds3LoopbackConfig": teraUds3LoopbackConfig,
       "teraUds3LineStatus": teraUds3LineStatus,
       "teraUds3TransmitClockSource": teraUds3TransmitClockSource,
       "teraUds3InvalidIntervals": teraUds3InvalidIntervals,
       "teraUds3LineLength": teraUds3LineLength,
       "teraUds3LoopbackStatus": teraUds3LoopbackStatus,
       "teraUds3FarEndLineLoopbackTimeout": teraUds3FarEndLineLoopbackTimeout,
       "teraUds3SendFarEndLoopback": teraUds3SendFarEndLoopback,
       "teraUds3BERTConfigTable": teraUds3BERTConfigTable,
       "teraUds3BERTConfigTableEntry": teraUds3BERTConfigTableEntry,
       "teraUds3BERTPattern": teraUds3BERTPattern,
       "teraUds3BERTUserPattern": teraUds3BERTUserPattern,
       "teraUds3BERTSyncInfo": teraUds3BERTSyncInfo,
       "teraUds3BERT-ES": teraUds3BERT_ES,
       "teraUds3BERT-BES": teraUds3BERT_BES,
       "teraUds3BERT-BER": teraUds3BERT_BER,
       "teraUds3ExtendTotalTable": teraUds3ExtendTotalTable,
       "teraUds3ExtendTotalTableEntry": teraUds3ExtendTotalTableEntry,
       "teraUds3ExtendTotalIndex": teraUds3ExtendTotalIndex,
       "teraUds3ExtendTotalNumber": teraUds3ExtendTotalNumber,
       "teraUds3ExtendTotalPESs": teraUds3ExtendTotalPESs,
       "teraUds3ExtendTotalPSESs": teraUds3ExtendTotalPSESs,
       "teraUds3ExtendTotalSEFSs": teraUds3ExtendTotalSEFSs,
       "teraUds3ExtendTotalUASs": teraUds3ExtendTotalUASs,
       "teraUds3ExtendTotalLCVs": teraUds3ExtendTotalLCVs,
       "teraUds3ExtendTotalPCVs": teraUds3ExtendTotalPCVs,
       "teraUds3ExtendTotalLESs": teraUds3ExtendTotalLESs,
       "teraUds3ExtendTotalCCVs": teraUds3ExtendTotalCCVs,
       "teraUds3ExtendTotalCESs": teraUds3ExtendTotalCESs,
       "teraUds3ExtendTotalCSESs": teraUds3ExtendTotalCSESs,
       "teraUds3ExtendTotalValidData": teraUds3ExtendTotalValidData,
       "teraUds3FarEndExtendTotalTable": teraUds3FarEndExtendTotalTable,
       "teraUds3FarEndExtendTotalTableEntry": teraUds3FarEndExtendTotalTableEntry,
       "teraUds3FarEndExtendTotalIndex": teraUds3FarEndExtendTotalIndex,
       "teraUds3FarEndExtendTotalNumber": teraUds3FarEndExtendTotalNumber,
       "teraUds3FarEndExtendTotalCESs": teraUds3FarEndExtendTotalCESs,
       "teraUds3FarEndExtendTotalCSESs": teraUds3FarEndExtendTotalCSESs,
       "teraUds3FarEndExtendTotalCCVs": teraUds3FarEndExtendTotalCCVs,
       "teraUds3FarEndExtendTotalUASs": teraUds3FarEndExtendTotalUASs,
       "teraUds3FarEndExtendTotalValidData": teraUds3FarEndExtendTotalValidData,
       "teraUds3atmInterfacePlcpIntervalTable": teraUds3atmInterfacePlcpIntervalTable,
       "teraUds3atmInterfacePlcpIntervalTableEntry": teraUds3atmInterfacePlcpIntervalTableEntry,
       "teraUds3atmInterfacePlcpIntervalNumber": teraUds3atmInterfacePlcpIntervalNumber,
       "teraUds3atmInterfacePlcpIntervalSEFSs": teraUds3atmInterfacePlcpIntervalSEFSs,
       "teraUds3atmInterfacePlcpIntervalAlarmState": teraUds3atmInterfacePlcpIntervalAlarmState,
       "teraUds3atmInterfacePlcpIntervalUASs": teraUds3atmInterfacePlcpIntervalUASs,
       "teraUds3atmInterfacePlcpIntervalValidData": teraUds3atmInterfacePlcpIntervalValidData,
       "teraUds3atmInterfacePlcpTotalTable": teraUds3atmInterfacePlcpTotalTable,
       "teraUds3atmInterfacePlcpTotalTableEntry": teraUds3atmInterfacePlcpTotalTableEntry,
       "teraUds3atmInterfacePlcpTotalSEFSs": teraUds3atmInterfacePlcpTotalSEFSs,
       "teraUds3atmInterfacePlcpTotalAlarmState": teraUds3atmInterfacePlcpTotalAlarmState,
       "teraUds3atmInterfacePlcpTotalUASs": teraUds3atmInterfacePlcpTotalUASs,
       "teraUds3atmInterfacePlcpExtendTotalTable": teraUds3atmInterfacePlcpExtendTotalTable,
       "teraUds3atmInterfacePlcpExtendTotalTableEntry": teraUds3atmInterfacePlcpExtendTotalTableEntry,
       "teraUds3atmInterfacePlcpExtendTotalNumber": teraUds3atmInterfacePlcpExtendTotalNumber,
       "teraUds3atmInterfacePlcpExtendTotalSEFSs": teraUds3atmInterfacePlcpExtendTotalSEFSs,
       "teraUds3atmInterfacePlcpExtendTotalAlarmState": teraUds3atmInterfacePlcpExtendTotalAlarmState,
       "teraUds3atmInterfacePlcpExtendTotalUASs": teraUds3atmInterfacePlcpExtendTotalUASs,
       "teraUds3atmInterfacePlcpExtendTotalValidData": teraUds3atmInterfacePlcpExtendTotalValidData,
       "teraUds3atmInterfaceTCIntervalTable": teraUds3atmInterfaceTCIntervalTable,
       "teraUds3atmInterfaceTCIntervalTableEntry": teraUds3atmInterfaceTCIntervalTableEntry,
       "teraUds3atmInterfaceTCIntervalNumber": teraUds3atmInterfaceTCIntervalNumber,
       "teraUds3atmInterfaceTCIntervalOCDEvents": teraUds3atmInterfaceTCIntervalOCDEvents,
       "teraUds3atmInterfaceTCIntervalAlarmState": teraUds3atmInterfaceTCIntervalAlarmState,
       "teraUds3atmInterfaceTCIntervalValidData": teraUds3atmInterfaceTCIntervalValidData,
       "teraUds3atmInterfaceTCTotalTable": teraUds3atmInterfaceTCTotalTable,
       "teraUds3atmInterfaceTCTotalTableEntry": teraUds3atmInterfaceTCTotalTableEntry,
       "teraUds3atmInterfaceTCTotalOCDEvents": teraUds3atmInterfaceTCTotalOCDEvents,
       "teraUds3atmInterfaceTCTotalAlarmState": teraUds3atmInterfaceTCTotalAlarmState,
       "teraUds3atmInterfaceTCExtendTotalTable": teraUds3atmInterfaceTCExtendTotalTable,
       "teraUds3atmInterfaceTCExtendTotalTableEntry": teraUds3atmInterfaceTCExtendTotalTableEntry,
       "teraUds3atmInterfaceTCExtendTotalNumber": teraUds3atmInterfaceTCExtendTotalNumber,
       "teraUds3atmInterfaceTCExtendTotalOCDEvents": teraUds3atmInterfaceTCExtendTotalOCDEvents,
       "teraUds3atmInterfaceTCExtendTotalAlarmState": teraUds3atmInterfaceTCExtendTotalAlarmState,
       "teraUds3atmInterfaceTCExtendTotalValidData": teraUds3atmInterfaceTCExtendTotalValidData,
       "teraUds3PMControlTable": teraUds3PMControlTable,
       "teraUds3PMControlTableEntry": teraUds3PMControlTableEntry,
       "teraUds3PMControlClearAll": teraUds3PMControlClearAll}
)
