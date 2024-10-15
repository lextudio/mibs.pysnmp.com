# SNMP MIB module (SYNOPTICS-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYNOPTICS-ETHERNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:03 2024
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(S3ModuleType,
 s3000Ethernet) = mibBuilder.importSymbols(
    "SYNOPTICS-COMMON-MIB",
    "S3ModuleType",
    "s3000Ethernet")

(SnpxBackplaneType,
 SnpxChassisType) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "SnpxBackplaneType",
    "SnpxChassisType")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S3000EnetConcentrator_ObjectIdentity = ObjectIdentity
s3000EnetConcentrator = _S3000EnetConcentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1)
)


class _S3EnetConcRetimingStatus_Type(Integer32):
    """Custom type s3EnetConcRetimingStatus based on Integer32"""
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


_S3EnetConcRetimingStatus_Type.__name__ = "Integer32"
_S3EnetConcRetimingStatus_Object = MibScalar
s3EnetConcRetimingStatus = _S3EnetConcRetimingStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 1),
    _S3EnetConcRetimingStatus_Type()
)
s3EnetConcRetimingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetConcRetimingStatus.setStatus("mandatory")
_S3EnetConcFrmsRxOk_Type = Counter32
_S3EnetConcFrmsRxOk_Object = MibScalar
s3EnetConcFrmsRxOk = _S3EnetConcFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 2),
    _S3EnetConcFrmsRxOk_Type()
)
s3EnetConcFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcFrmsRxOk.setStatus("mandatory")
_S3EnetConcOctetsRxOk_Type = Counter32
_S3EnetConcOctetsRxOk_Object = MibScalar
s3EnetConcOctetsRxOk = _S3EnetConcOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 3),
    _S3EnetConcOctetsRxOk_Type()
)
s3EnetConcOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcOctetsRxOk.setStatus("mandatory")
_S3EnetConcMcastFrmsRxOk_Type = Counter32
_S3EnetConcMcastFrmsRxOk_Object = MibScalar
s3EnetConcMcastFrmsRxOk = _S3EnetConcMcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 4),
    _S3EnetConcMcastFrmsRxOk_Type()
)
s3EnetConcMcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcMcastFrmsRxOk.setStatus("mandatory")
_S3EnetConcBcastFrmsRxOk_Type = Counter32
_S3EnetConcBcastFrmsRxOk_Object = MibScalar
s3EnetConcBcastFrmsRxOk = _S3EnetConcBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 5),
    _S3EnetConcBcastFrmsRxOk_Type()
)
s3EnetConcBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcBcastFrmsRxOk.setStatus("mandatory")
_S3EnetConcColls_Type = Counter32
_S3EnetConcColls_Object = MibScalar
s3EnetConcColls = _S3EnetConcColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 6),
    _S3EnetConcColls_Type()
)
s3EnetConcColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcColls.setStatus("mandatory")
_S3EnetConcTooLongErrors_Type = Counter32
_S3EnetConcTooLongErrors_Object = MibScalar
s3EnetConcTooLongErrors = _S3EnetConcTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 7),
    _S3EnetConcTooLongErrors_Type()
)
s3EnetConcTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcTooLongErrors.setStatus("mandatory")
_S3EnetConcRuntErrors_Type = Counter32
_S3EnetConcRuntErrors_Object = MibScalar
s3EnetConcRuntErrors = _S3EnetConcRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 8),
    _S3EnetConcRuntErrors_Type()
)
s3EnetConcRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcRuntErrors.setStatus("mandatory")
_S3EnetConcFragErrors_Type = Counter32
_S3EnetConcFragErrors_Object = MibScalar
s3EnetConcFragErrors = _S3EnetConcFragErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 9),
    _S3EnetConcFragErrors_Type()
)
s3EnetConcFragErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcFragErrors.setStatus("mandatory")
_S3EnetConcAlignErrors_Type = Counter32
_S3EnetConcAlignErrors_Object = MibScalar
s3EnetConcAlignErrors = _S3EnetConcAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 10),
    _S3EnetConcAlignErrors_Type()
)
s3EnetConcAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcAlignErrors.setStatus("mandatory")
_S3EnetConcFcsErrors_Type = Counter32
_S3EnetConcFcsErrors_Object = MibScalar
s3EnetConcFcsErrors = _S3EnetConcFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 11),
    _S3EnetConcFcsErrors_Type()
)
s3EnetConcFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcFcsErrors.setStatus("mandatory")
_S3EnetConcLateCollErrors_Type = Counter32
_S3EnetConcLateCollErrors_Object = MibScalar
s3EnetConcLateCollErrors = _S3EnetConcLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 12),
    _S3EnetConcLateCollErrors_Type()
)
s3EnetConcLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcLateCollErrors.setStatus("mandatory")


class _S3EnetConcSecureStatus_Type(Integer32):
    """Custom type s3EnetConcSecureStatus based on Integer32"""
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
        *(("concSecureOff", 5),
          ("concSecureOn", 2),
          ("other", 1),
          ("portCheckOn", 3),
          ("slotCheckOn", 4))
    )


_S3EnetConcSecureStatus_Type.__name__ = "Integer32"
_S3EnetConcSecureStatus_Object = MibScalar
s3EnetConcSecureStatus = _S3EnetConcSecureStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 13),
    _S3EnetConcSecureStatus_Type()
)
s3EnetConcSecureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetConcSecureStatus.setStatus("mandatory")


class _S3EnetConcAuthAction_Type(Integer32):
    """Custom type s3EnetConcAuthAction based on Integer32"""
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
        *(("noAction", 2),
          ("other", 1),
          ("partition", 4),
          ("sendTrap", 3),
          ("sendTrapPartition", 5))
    )


_S3EnetConcAuthAction_Type.__name__ = "Integer32"
_S3EnetConcAuthAction_Object = MibScalar
s3EnetConcAuthAction = _S3EnetConcAuthAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 14),
    _S3EnetConcAuthAction_Type()
)
s3EnetConcAuthAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetConcAuthAction.setStatus("mandatory")


class _S3EnetConcSecurityLock_Type(Integer32):
    """Custom type s3EnetConcSecurityLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 2),
          ("notLocked", 3),
          ("other", 1))
    )


_S3EnetConcSecurityLock_Type.__name__ = "Integer32"
_S3EnetConcSecurityLock_Object = MibScalar
s3EnetConcSecurityLock = _S3EnetConcSecurityLock_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 15),
    _S3EnetConcSecurityLock_Type()
)
s3EnetConcSecurityLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcSecurityLock.setStatus("mandatory")


class _S3EnetConcEnetChan_Type(Integer32):
    """Custom type s3EnetConcEnetChan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enetA", 2),
          ("enetB", 3),
          ("other", 1))
    )


_S3EnetConcEnetChan_Type.__name__ = "Integer32"
_S3EnetConcEnetChan_Object = MibScalar
s3EnetConcEnetChan = _S3EnetConcEnetChan_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 1, 16),
    _S3EnetConcEnetChan_Type()
)
s3EnetConcEnetChan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcEnetChan.setStatus("mandatory")
_S3000EnetBoard_ObjectIdentity = ObjectIdentity
s3000EnetBoard = _S3000EnetBoard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2)
)
_S3EnetBoardTable_Object = MibTable
s3EnetBoardTable = _S3EnetBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    s3EnetBoardTable.setStatus("mandatory")
_S3EnetBoardEntry_Object = MibTableRow
s3EnetBoardEntry = _S3EnetBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1)
)
s3EnetBoardEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetBoardIndex"),
)
if mibBuilder.loadTexts:
    s3EnetBoardEntry.setStatus("mandatory")
_S3EnetBoardIndex_Type = Integer32
_S3EnetBoardIndex_Object = MibTableColumn
s3EnetBoardIndex = _S3EnetBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 1),
    _S3EnetBoardIndex_Type()
)
s3EnetBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardIndex.setStatus("mandatory")


class _S3EnetBoardType_Type(Integer32):
    """Custom type s3EnetBoardType based on Integer32"""
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
              16,
              17,
              18,
              24,
              25,
              26,
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("empty", 1),
          ("m3301", 16),
          ("m3302", 3),
          ("m3304-ST", 4),
          ("m3305", 5),
          ("m3307", 17),
          ("m3307A", 37),
          ("m3308", 6),
          ("m3308A", 38),
          ("m3313", 7),
          ("m3313M", 8),
          ("m3314-ST", 9),
          ("m3314M-ST", 10),
          ("m331x", 26),
          ("m3323", 11),
          ("m3323S", 35),
          ("m3324-ST", 12),
          ("m3324S-ST", 36),
          ("m3356", 18),
          ("m3383", 24),
          ("m3384", 25),
          ("m3386", 32),
          ("m3394", 33),
          ("m3395", 34),
          ("other", 2))
    )


_S3EnetBoardType_Type.__name__ = "Integer32"
_S3EnetBoardType_Object = MibTableColumn
s3EnetBoardType = _S3EnetBoardType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 2),
    _S3EnetBoardType_Type()
)
s3EnetBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardType.setStatus("obsolete")
_S3EnetBoardHwVer_Type = Integer32
_S3EnetBoardHwVer_Object = MibTableColumn
s3EnetBoardHwVer = _S3EnetBoardHwVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 3),
    _S3EnetBoardHwVer_Type()
)
s3EnetBoardHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardHwVer.setStatus("obsolete")


class _S3EnetBoardStatus_Type(Integer32):
    """Custom type s3EnetBoardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_S3EnetBoardStatus_Type.__name__ = "Integer32"
_S3EnetBoardStatus_Object = MibTableColumn
s3EnetBoardStatus = _S3EnetBoardStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 4),
    _S3EnetBoardStatus_Type()
)
s3EnetBoardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardStatus.setStatus("obsolete")


class _S3EnetBoardReset_Type(Integer32):
    """Custom type s3EnetBoardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_S3EnetBoardReset_Type.__name__ = "Integer32"
_S3EnetBoardReset_Object = MibTableColumn
s3EnetBoardReset = _S3EnetBoardReset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 5),
    _S3EnetBoardReset_Type()
)
s3EnetBoardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetBoardReset.setStatus("obsolete")


class _S3EnetBoardPartStatus_Type(Integer32):
    """Custom type s3EnetBoardPartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("partition", 2))
    )


_S3EnetBoardPartStatus_Type.__name__ = "Integer32"
_S3EnetBoardPartStatus_Object = MibTableColumn
s3EnetBoardPartStatus = _S3EnetBoardPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 6),
    _S3EnetBoardPartStatus_Type()
)
s3EnetBoardPartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetBoardPartStatus.setStatus("obsolete")


class _S3EnetBoardNmCntlStatus_Type(Integer32):
    """Custom type s3EnetBoardNmCntlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nmControl", 2),
          ("notNmControl", 1))
    )


_S3EnetBoardNmCntlStatus_Type.__name__ = "Integer32"
_S3EnetBoardNmCntlStatus_Object = MibTableColumn
s3EnetBoardNmCntlStatus = _S3EnetBoardNmCntlStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 7),
    _S3EnetBoardNmCntlStatus_Type()
)
s3EnetBoardNmCntlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardNmCntlStatus.setStatus("obsolete")


class _S3EnetBoardPsStatus_Type(Integer32):
    """Custom type s3EnetBoardPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("ok", 1))
    )


_S3EnetBoardPsStatus_Type.__name__ = "Integer32"
_S3EnetBoardPsStatus_Object = MibTableColumn
s3EnetBoardPsStatus = _S3EnetBoardPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 8),
    _S3EnetBoardPsStatus_Type()
)
s3EnetBoardPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardPsStatus.setStatus("obsolete")
_S3EnetBoardFrmsRxOk_Type = Counter32
_S3EnetBoardFrmsRxOk_Object = MibTableColumn
s3EnetBoardFrmsRxOk = _S3EnetBoardFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 9),
    _S3EnetBoardFrmsRxOk_Type()
)
s3EnetBoardFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardFrmsRxOk.setStatus("mandatory")
_S3EnetBoardOctetsRxOk_Type = Counter32
_S3EnetBoardOctetsRxOk_Object = MibTableColumn
s3EnetBoardOctetsRxOk = _S3EnetBoardOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 10),
    _S3EnetBoardOctetsRxOk_Type()
)
s3EnetBoardOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardOctetsRxOk.setStatus("mandatory")
_S3EnetBoardMcastFrmsRxOk_Type = Counter32
_S3EnetBoardMcastFrmsRxOk_Object = MibTableColumn
s3EnetBoardMcastFrmsRxOk = _S3EnetBoardMcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 11),
    _S3EnetBoardMcastFrmsRxOk_Type()
)
s3EnetBoardMcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardMcastFrmsRxOk.setStatus("mandatory")
_S3EnetBoardBcastFrmsRxOk_Type = Counter32
_S3EnetBoardBcastFrmsRxOk_Object = MibTableColumn
s3EnetBoardBcastFrmsRxOk = _S3EnetBoardBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 12),
    _S3EnetBoardBcastFrmsRxOk_Type()
)
s3EnetBoardBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardBcastFrmsRxOk.setStatus("mandatory")
_S3EnetBoardColls_Type = Counter32
_S3EnetBoardColls_Object = MibTableColumn
s3EnetBoardColls = _S3EnetBoardColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 13),
    _S3EnetBoardColls_Type()
)
s3EnetBoardColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardColls.setStatus("mandatory")
_S3EnetBoardTooLongErrors_Type = Counter32
_S3EnetBoardTooLongErrors_Object = MibTableColumn
s3EnetBoardTooLongErrors = _S3EnetBoardTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 14),
    _S3EnetBoardTooLongErrors_Type()
)
s3EnetBoardTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardTooLongErrors.setStatus("mandatory")
_S3EnetBoardRuntErrors_Type = Counter32
_S3EnetBoardRuntErrors_Object = MibTableColumn
s3EnetBoardRuntErrors = _S3EnetBoardRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 15),
    _S3EnetBoardRuntErrors_Type()
)
s3EnetBoardRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardRuntErrors.setStatus("mandatory")
_S3EnetBoardAlignErrors_Type = Counter32
_S3EnetBoardAlignErrors_Object = MibTableColumn
s3EnetBoardAlignErrors = _S3EnetBoardAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 16),
    _S3EnetBoardAlignErrors_Type()
)
s3EnetBoardAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardAlignErrors.setStatus("mandatory")
_S3EnetBoardFcsErrors_Type = Counter32
_S3EnetBoardFcsErrors_Object = MibTableColumn
s3EnetBoardFcsErrors = _S3EnetBoardFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 17),
    _S3EnetBoardFcsErrors_Type()
)
s3EnetBoardFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardFcsErrors.setStatus("mandatory")
_S3EnetBoardLateCollErrors_Type = Counter32
_S3EnetBoardLateCollErrors_Object = MibTableColumn
s3EnetBoardLateCollErrors = _S3EnetBoardLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 18),
    _S3EnetBoardLateCollErrors_Type()
)
s3EnetBoardLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardLateCollErrors.setStatus("mandatory")


class _S3EnetBoardAuthStatus_Type(Integer32):
    """Custom type s3EnetBoardAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3EnetBoardAuthStatus_Type.__name__ = "Integer32"
_S3EnetBoardAuthStatus_Object = MibTableColumn
s3EnetBoardAuthStatus = _S3EnetBoardAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 19),
    _S3EnetBoardAuthStatus_Type()
)
s3EnetBoardAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetBoardAuthStatus.setStatus("mandatory")


class _S3EnetBoardAuthAction_Type(Integer32):
    """Custom type s3EnetBoardAuthAction based on Integer32"""
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
        *(("noAction", 2),
          ("other", 1),
          ("partition", 4),
          ("sendTrap", 3),
          ("sendTrapPartition", 5))
    )


_S3EnetBoardAuthAction_Type.__name__ = "Integer32"
_S3EnetBoardAuthAction_Object = MibTableColumn
s3EnetBoardAuthAction = _S3EnetBoardAuthAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 20),
    _S3EnetBoardAuthAction_Type()
)
s3EnetBoardAuthAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetBoardAuthAction.setStatus("mandatory")
_S3EnetBoardUpStamp_Type = TimeTicks
_S3EnetBoardUpStamp_Object = MibTableColumn
s3EnetBoardUpStamp = _S3EnetBoardUpStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 1, 1, 21),
    _S3EnetBoardUpStamp_Type()
)
s3EnetBoardUpStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardUpStamp.setStatus("mandatory")
_S3000EnetLocBridge_ObjectIdentity = ObjectIdentity
s3000EnetLocBridge = _S3000EnetLocBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2)
)
_S3EnetLocBridgeSlotTable_Object = MibTable
s3EnetLocBridgeSlotTable = _S3EnetLocBridgeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    s3EnetLocBridgeSlotTable.setStatus("mandatory")
_S3EnetLocBridgeEntry_Object = MibTableRow
s3EnetLocBridgeEntry = _S3EnetLocBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1)
)
s3EnetLocBridgeEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetLocBridgeIndex"),
)
if mibBuilder.loadTexts:
    s3EnetLocBridgeEntry.setStatus("mandatory")
_S3EnetLocBridgeIndex_Type = Integer32
_S3EnetLocBridgeIndex_Object = MibTableColumn
s3EnetLocBridgeIndex = _S3EnetLocBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 1),
    _S3EnetLocBridgeIndex_Type()
)
s3EnetLocBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgeIndex.setStatus("mandatory")


class _S3EnetLocBridgeDescr_Type(DisplayString):
    """Custom type s3EnetLocBridgeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S3EnetLocBridgeDescr_Type.__name__ = "DisplayString"
_S3EnetLocBridgeDescr_Object = MibTableColumn
s3EnetLocBridgeDescr = _S3EnetLocBridgeDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 2),
    _S3EnetLocBridgeDescr_Type()
)
s3EnetLocBridgeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgeDescr.setStatus("mandatory")
_S3EnetLocBridgePortCount_Type = Integer32
_S3EnetLocBridgePortCount_Object = MibTableColumn
s3EnetLocBridgePortCount = _S3EnetLocBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 3),
    _S3EnetLocBridgePortCount_Type()
)
s3EnetLocBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortCount.setStatus("mandatory")


class _S3EnetLocBridgeDiagSts_Type(OctetString):
    """Custom type s3EnetLocBridgeDiagSts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S3EnetLocBridgeDiagSts_Type.__name__ = "OctetString"
_S3EnetLocBridgeDiagSts_Object = MibTableColumn
s3EnetLocBridgeDiagSts = _S3EnetLocBridgeDiagSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 4),
    _S3EnetLocBridgeDiagSts_Type()
)
s3EnetLocBridgeDiagSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgeDiagSts.setStatus("mandatory")


class _S3EnetLocBridgeBootSts_Type(Integer32):
    """Custom type s3EnetLocBridgeBootSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReqstToBoot", 3),
          ("other", 1),
          ("reqstToBoot", 2))
    )


_S3EnetLocBridgeBootSts_Type.__name__ = "Integer32"
_S3EnetLocBridgeBootSts_Object = MibTableColumn
s3EnetLocBridgeBootSts = _S3EnetLocBridgeBootSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 5),
    _S3EnetLocBridgeBootSts_Type()
)
s3EnetLocBridgeBootSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgeBootSts.setStatus("mandatory")


class _S3EnetLocBridgeStandbySts_Type(Integer32):
    """Custom type s3EnetLocBridgeStandbySts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notStandby", 3),
          ("other", 1),
          ("standby", 2))
    )


_S3EnetLocBridgeStandbySts_Type.__name__ = "Integer32"
_S3EnetLocBridgeStandbySts_Object = MibTableColumn
s3EnetLocBridgeStandbySts = _S3EnetLocBridgeStandbySts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 1, 1, 6),
    _S3EnetLocBridgeStandbySts_Type()
)
s3EnetLocBridgeStandbySts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgeStandbySts.setStatus("mandatory")
_S3EnetLocBridgePortTable_Object = MibTable
s3EnetLocBridgePortTable = _S3EnetLocBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    s3EnetLocBridgePortTable.setStatus("mandatory")
_S3EnetLocBridgePortEntry_Object = MibTableRow
s3EnetLocBridgePortEntry = _S3EnetLocBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1)
)
s3EnetLocBridgePortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetLocBridgePortSlotIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetLocBridgePortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetLocBridgePortEntry.setStatus("mandatory")
_S3EnetLocBridgePortSlotIndex_Type = Integer32
_S3EnetLocBridgePortSlotIndex_Object = MibTableColumn
s3EnetLocBridgePortSlotIndex = _S3EnetLocBridgePortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 1),
    _S3EnetLocBridgePortSlotIndex_Type()
)
s3EnetLocBridgePortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortSlotIndex.setStatus("mandatory")
_S3EnetLocBridgePortIndex_Type = Integer32
_S3EnetLocBridgePortIndex_Object = MibTableColumn
s3EnetLocBridgePortIndex = _S3EnetLocBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 2),
    _S3EnetLocBridgePortIndex_Type()
)
s3EnetLocBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortIndex.setStatus("mandatory")
_S3EnetLocBridgePortMdaId_Type = Integer32
_S3EnetLocBridgePortMdaId_Object = MibTableColumn
s3EnetLocBridgePortMdaId = _S3EnetLocBridgePortMdaId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 3),
    _S3EnetLocBridgePortMdaId_Type()
)
s3EnetLocBridgePortMdaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortMdaId.setStatus("mandatory")


class _S3EnetLocBridgePortIf_Type(Integer32):
    """Custom type s3EnetLocBridgePortIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etherEther", 2),
          ("etherTokenRing", 3),
          ("other", 1))
    )


_S3EnetLocBridgePortIf_Type.__name__ = "Integer32"
_S3EnetLocBridgePortIf_Object = MibTableColumn
s3EnetLocBridgePortIf = _S3EnetLocBridgePortIf_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 4),
    _S3EnetLocBridgePortIf_Type()
)
s3EnetLocBridgePortIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortIf.setStatus("mandatory")


class _S3EnetLocBridgePortDescr_Type(DisplayString):
    """Custom type s3EnetLocBridgePortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S3EnetLocBridgePortDescr_Type.__name__ = "DisplayString"
_S3EnetLocBridgePortDescr_Object = MibTableColumn
s3EnetLocBridgePortDescr = _S3EnetLocBridgePortDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 5),
    _S3EnetLocBridgePortDescr_Type()
)
s3EnetLocBridgePortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortDescr.setStatus("mandatory")


class _S3EnetLocBridgePortOpSts_Type(Integer32):
    """Custom type s3EnetLocBridgePortOpSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notStandby", 3),
          ("other", 1),
          ("standby", 2))
    )


_S3EnetLocBridgePortOpSts_Type.__name__ = "Integer32"
_S3EnetLocBridgePortOpSts_Object = MibTableColumn
s3EnetLocBridgePortOpSts = _S3EnetLocBridgePortOpSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 2, 2, 1, 6),
    _S3EnetLocBridgePortOpSts_Type()
)
s3EnetLocBridgePortOpSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetLocBridgePortOpSts.setStatus("mandatory")
_S3000EnetRemBridge_ObjectIdentity = ObjectIdentity
s3000EnetRemBridge = _S3000EnetRemBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3)
)
_S3EnetRemBridgeSlotTable_Object = MibTable
s3EnetRemBridgeSlotTable = _S3EnetRemBridgeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    s3EnetRemBridgeSlotTable.setStatus("mandatory")
_S3EnetRemBridgeEntry_Object = MibTableRow
s3EnetRemBridgeEntry = _S3EnetRemBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1)
)
s3EnetRemBridgeEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRemBridgeIndex"),
)
if mibBuilder.loadTexts:
    s3EnetRemBridgeEntry.setStatus("mandatory")
_S3EnetRemBridgeIndex_Type = Integer32
_S3EnetRemBridgeIndex_Object = MibTableColumn
s3EnetRemBridgeIndex = _S3EnetRemBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 1),
    _S3EnetRemBridgeIndex_Type()
)
s3EnetRemBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgeIndex.setStatus("mandatory")


class _S3EnetRemBridgeDescr_Type(DisplayString):
    """Custom type s3EnetRemBridgeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S3EnetRemBridgeDescr_Type.__name__ = "DisplayString"
_S3EnetRemBridgeDescr_Object = MibTableColumn
s3EnetRemBridgeDescr = _S3EnetRemBridgeDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 2),
    _S3EnetRemBridgeDescr_Type()
)
s3EnetRemBridgeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgeDescr.setStatus("mandatory")
_S3EnetRemBridgePortCount_Type = Integer32
_S3EnetRemBridgePortCount_Object = MibTableColumn
s3EnetRemBridgePortCount = _S3EnetRemBridgePortCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 3),
    _S3EnetRemBridgePortCount_Type()
)
s3EnetRemBridgePortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortCount.setStatus("mandatory")


class _S3EnetRemBridgeDiagSts_Type(OctetString):
    """Custom type s3EnetRemBridgeDiagSts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S3EnetRemBridgeDiagSts_Type.__name__ = "OctetString"
_S3EnetRemBridgeDiagSts_Object = MibTableColumn
s3EnetRemBridgeDiagSts = _S3EnetRemBridgeDiagSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 4),
    _S3EnetRemBridgeDiagSts_Type()
)
s3EnetRemBridgeDiagSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgeDiagSts.setStatus("mandatory")


class _S3EnetRemBridgeBootSts_Type(Integer32):
    """Custom type s3EnetRemBridgeBootSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notReqstToBoot", 3),
          ("other", 1),
          ("reqstToBoot", 2))
    )


_S3EnetRemBridgeBootSts_Type.__name__ = "Integer32"
_S3EnetRemBridgeBootSts_Object = MibTableColumn
s3EnetRemBridgeBootSts = _S3EnetRemBridgeBootSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 5),
    _S3EnetRemBridgeBootSts_Type()
)
s3EnetRemBridgeBootSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgeBootSts.setStatus("mandatory")


class _S3EnetRemBridgeStandbySts_Type(Integer32):
    """Custom type s3EnetRemBridgeStandbySts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notStandby", 3),
          ("other", 1),
          ("standby", 2))
    )


_S3EnetRemBridgeStandbySts_Type.__name__ = "Integer32"
_S3EnetRemBridgeStandbySts_Object = MibTableColumn
s3EnetRemBridgeStandbySts = _S3EnetRemBridgeStandbySts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 1, 1, 6),
    _S3EnetRemBridgeStandbySts_Type()
)
s3EnetRemBridgeStandbySts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgeStandbySts.setStatus("mandatory")
_S3EnetRemBridgePortTable_Object = MibTable
s3EnetRemBridgePortTable = _S3EnetRemBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    s3EnetRemBridgePortTable.setStatus("mandatory")
_S3EnetRemBridgePortEntry_Object = MibTableRow
s3EnetRemBridgePortEntry = _S3EnetRemBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1)
)
s3EnetRemBridgePortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRemBridgePortSlotIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRemBridgePortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetRemBridgePortEntry.setStatus("mandatory")
_S3EnetRemBridgePortSlotIndex_Type = Integer32
_S3EnetRemBridgePortSlotIndex_Object = MibTableColumn
s3EnetRemBridgePortSlotIndex = _S3EnetRemBridgePortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 1),
    _S3EnetRemBridgePortSlotIndex_Type()
)
s3EnetRemBridgePortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortSlotIndex.setStatus("mandatory")
_S3EnetRemBridgePortIndex_Type = Integer32
_S3EnetRemBridgePortIndex_Object = MibTableColumn
s3EnetRemBridgePortIndex = _S3EnetRemBridgePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 2),
    _S3EnetRemBridgePortIndex_Type()
)
s3EnetRemBridgePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortIndex.setStatus("mandatory")


class _S3EnetRemBridgePortMdaId_Type(Integer32):
    """Custom type s3EnetRemBridgePortMdaId based on Integer32"""
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
        *(("ethernet", 2),
          ("g703", 8),
          ("other", 1),
          ("rs232", 5),
          ("rs449", 6),
          ("t1", 9),
          ("v35", 7),
          ("x21Barrier", 3),
          ("x21Unbarrier", 4))
    )


_S3EnetRemBridgePortMdaId_Type.__name__ = "Integer32"
_S3EnetRemBridgePortMdaId_Object = MibTableColumn
s3EnetRemBridgePortMdaId = _S3EnetRemBridgePortMdaId_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 3),
    _S3EnetRemBridgePortMdaId_Type()
)
s3EnetRemBridgePortMdaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortMdaId.setStatus("mandatory")


class _S3EnetRemBridgePortDescr_Type(DisplayString):
    """Custom type s3EnetRemBridgePortDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S3EnetRemBridgePortDescr_Type.__name__ = "DisplayString"
_S3EnetRemBridgePortDescr_Object = MibTableColumn
s3EnetRemBridgePortDescr = _S3EnetRemBridgePortDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 4),
    _S3EnetRemBridgePortDescr_Type()
)
s3EnetRemBridgePortDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortDescr.setStatus("mandatory")


class _S3EnetRemBridgePortOpSts_Type(Integer32):
    """Custom type s3EnetRemBridgePortOpSts based on Integer32"""
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
        *(("noLink", 4),
          ("operational", 3),
          ("other", 1),
          ("standby", 2))
    )


_S3EnetRemBridgePortOpSts_Type.__name__ = "Integer32"
_S3EnetRemBridgePortOpSts_Object = MibTableColumn
s3EnetRemBridgePortOpSts = _S3EnetRemBridgePortOpSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 5),
    _S3EnetRemBridgePortOpSts_Type()
)
s3EnetRemBridgePortOpSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortOpSts.setStatus("mandatory")


class _S3EnetRemBridgePortRdySnd_Type(Integer32):
    """Custom type s3EnetRemBridgePortRdySnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRdySnd", 3),
          ("other", 1),
          ("rdySnd", 2))
    )


_S3EnetRemBridgePortRdySnd_Type.__name__ = "Integer32"
_S3EnetRemBridgePortRdySnd_Object = MibTableColumn
s3EnetRemBridgePortRdySnd = _S3EnetRemBridgePortRdySnd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 6),
    _S3EnetRemBridgePortRdySnd_Type()
)
s3EnetRemBridgePortRdySnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortRdySnd.setStatus("mandatory")


class _S3EnetRemBridgePortClrSnd_Type(Integer32):
    """Custom type s3EnetRemBridgePortClrSnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clrSnd", 2),
          ("notClrSnd", 3),
          ("other", 1))
    )


_S3EnetRemBridgePortClrSnd_Type.__name__ = "Integer32"
_S3EnetRemBridgePortClrSnd_Object = MibTableColumn
s3EnetRemBridgePortClrSnd = _S3EnetRemBridgePortClrSnd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 7),
    _S3EnetRemBridgePortClrSnd_Type()
)
s3EnetRemBridgePortClrSnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortClrSnd.setStatus("mandatory")


class _S3EnetRemBridgePortCarDt_Type(Integer32):
    """Custom type s3EnetRemBridgePortCarDt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("carDt", 2),
          ("noCarDt", 3),
          ("other", 1))
    )


_S3EnetRemBridgePortCarDt_Type.__name__ = "Integer32"
_S3EnetRemBridgePortCarDt_Object = MibTableColumn
s3EnetRemBridgePortCarDt = _S3EnetRemBridgePortCarDt_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 3, 2, 1, 8),
    _S3EnetRemBridgePortCarDt_Type()
)
s3EnetRemBridgePortCarDt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRemBridgePortCarDt.setStatus("mandatory")
_S3000EnetRouter_ObjectIdentity = ObjectIdentity
s3000EnetRouter = _S3000EnetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4)
)
_S3EnetRouterSlotTable_Object = MibTable
s3EnetRouterSlotTable = _S3EnetRouterSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    s3EnetRouterSlotTable.setStatus("mandatory")
_S3EnetRouterEntry_Object = MibTableRow
s3EnetRouterEntry = _S3EnetRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1, 1)
)
s3EnetRouterEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRouterIndex"),
)
if mibBuilder.loadTexts:
    s3EnetRouterEntry.setStatus("mandatory")
_S3EnetRouterIndex_Type = Integer32
_S3EnetRouterIndex_Object = MibTableColumn
s3EnetRouterIndex = _S3EnetRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1, 1, 1),
    _S3EnetRouterIndex_Type()
)
s3EnetRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRouterIndex.setStatus("mandatory")


class _S3EnetRouterDescr_Type(DisplayString):
    """Custom type s3EnetRouterDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_S3EnetRouterDescr_Type.__name__ = "DisplayString"
_S3EnetRouterDescr_Object = MibTableColumn
s3EnetRouterDescr = _S3EnetRouterDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1, 1, 2),
    _S3EnetRouterDescr_Type()
)
s3EnetRouterDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRouterDescr.setStatus("mandatory")


class _S3EnetRouterDiagSts_Type(OctetString):
    """Custom type s3EnetRouterDiagSts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_S3EnetRouterDiagSts_Type.__name__ = "OctetString"
_S3EnetRouterDiagSts_Object = MibTableColumn
s3EnetRouterDiagSts = _S3EnetRouterDiagSts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1, 1, 3),
    _S3EnetRouterDiagSts_Type()
)
s3EnetRouterDiagSts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRouterDiagSts.setStatus("mandatory")


class _S3EnetRouterStandbySts_Type(Integer32):
    """Custom type s3EnetRouterStandbySts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notStandby", 3),
          ("other", 1),
          ("standby", 2))
    )


_S3EnetRouterStandbySts_Type.__name__ = "Integer32"
_S3EnetRouterStandbySts_Object = MibTableColumn
s3EnetRouterStandbySts = _S3EnetRouterStandbySts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 4, 1, 1, 4),
    _S3EnetRouterStandbySts_Type()
)
s3EnetRouterStandbySts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRouterStandbySts.setStatus("mandatory")
_S3EnetCommonBoardTable_Object = MibTable
s3EnetCommonBoardTable = _S3EnetCommonBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5)
)
if mibBuilder.loadTexts:
    s3EnetCommonBoardTable.setStatus("mandatory")
_S3EnetCommonBoardEntry_Object = MibTableRow
s3EnetCommonBoardEntry = _S3EnetCommonBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5, 1)
)
s3EnetCommonBoardEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetCommonBoardIndex"),
)
if mibBuilder.loadTexts:
    s3EnetCommonBoardEntry.setStatus("mandatory")
_S3EnetCommonBoardIndex_Type = Integer32
_S3EnetCommonBoardIndex_Object = MibTableColumn
s3EnetCommonBoardIndex = _S3EnetCommonBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5, 1, 1),
    _S3EnetCommonBoardIndex_Type()
)
s3EnetCommonBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonBoardIndex.setStatus("mandatory")


class _S3EnetCommonBoardEnetAB_Type(Integer32):
    """Custom type s3EnetCommonBoardEnetAB based on Integer32"""
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
        *(("enetA", 2),
          ("enetAandEnetB", 4),
          ("enetB", 3),
          ("other", 1))
    )


_S3EnetCommonBoardEnetAB_Type.__name__ = "Integer32"
_S3EnetCommonBoardEnetAB_Object = MibTableColumn
s3EnetCommonBoardEnetAB = _S3EnetCommonBoardEnetAB_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5, 1, 2),
    _S3EnetCommonBoardEnetAB_Type()
)
s3EnetCommonBoardEnetAB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetCommonBoardEnetAB.setStatus("mandatory")


class _S3EnetCommonBoardChanSwitch_Type(Integer32):
    """Custom type s3EnetCommonBoardChanSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSwitchCapable", 3),
          ("other", 1),
          ("switchCapable", 2))
    )


_S3EnetCommonBoardChanSwitch_Type.__name__ = "Integer32"
_S3EnetCommonBoardChanSwitch_Object = MibTableColumn
s3EnetCommonBoardChanSwitch = _S3EnetCommonBoardChanSwitch_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5, 1, 3),
    _S3EnetCommonBoardChanSwitch_Type()
)
s3EnetCommonBoardChanSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonBoardChanSwitch.setStatus("mandatory")


class _S3EnetCommonBoardRedund_Type(Integer32):
    """Custom type s3EnetCommonBoardRedund based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRedundCapable", 3),
          ("other", 1),
          ("redundCapable", 2))
    )


_S3EnetCommonBoardRedund_Type.__name__ = "Integer32"
_S3EnetCommonBoardRedund_Object = MibTableColumn
s3EnetCommonBoardRedund = _S3EnetCommonBoardRedund_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 2, 5, 1, 4),
    _S3EnetCommonBoardRedund_Type()
)
s3EnetCommonBoardRedund.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonBoardRedund.setStatus("mandatory")
_S3000EnetPort_ObjectIdentity = ObjectIdentity
s3000EnetPort = _S3000EnetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3)
)
_S3EnetPortTable_Object = MibTable
s3EnetPortTable = _S3EnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    s3EnetPortTable.setStatus("mandatory")
_S3EnetPortEntry_Object = MibTableRow
s3EnetPortEntry = _S3EnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1)
)
s3EnetPortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetPortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetPortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetPortEntry.setStatus("mandatory")
_S3EnetPortBoardIndex_Type = Integer32
_S3EnetPortBoardIndex_Object = MibTableColumn
s3EnetPortBoardIndex = _S3EnetPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 1),
    _S3EnetPortBoardIndex_Type()
)
s3EnetPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortBoardIndex.setStatus("mandatory")
_S3EnetPortIndex_Type = Integer32
_S3EnetPortIndex_Object = MibTableColumn
s3EnetPortIndex = _S3EnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 2),
    _S3EnetPortIndex_Type()
)
s3EnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortIndex.setStatus("mandatory")


class _S3EnetPortLinkStatus_Type(Integer32):
    """Custom type s3EnetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("other", 3))
    )


_S3EnetPortLinkStatus_Type.__name__ = "Integer32"
_S3EnetPortLinkStatus_Object = MibTableColumn
s3EnetPortLinkStatus = _S3EnetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 3),
    _S3EnetPortLinkStatus_Type()
)
s3EnetPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortLinkStatus.setStatus("deprecated")


class _S3EnetPortPartStatus_Type(Integer32):
    """Custom type s3EnetPortPartStatus based on Integer32"""
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
        *(("autoPartition", 3),
          ("enabled", 1),
          ("latSecPartition", 5),
          ("partition", 2),
          ("timedPartition", 4))
    )


_S3EnetPortPartStatus_Type.__name__ = "Integer32"
_S3EnetPortPartStatus_Object = MibTableColumn
s3EnetPortPartStatus = _S3EnetPortPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 4),
    _S3EnetPortPartStatus_Type()
)
s3EnetPortPartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortPartStatus.setStatus("deprecated")


class _S3EnetPortJabberStatus_Type(Integer32):
    """Custom type s3EnetPortJabberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jabbering", 2),
          ("ok", 1))
    )


_S3EnetPortJabberStatus_Type.__name__ = "Integer32"
_S3EnetPortJabberStatus_Object = MibTableColumn
s3EnetPortJabberStatus = _S3EnetPortJabberStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 5),
    _S3EnetPortJabberStatus_Type()
)
s3EnetPortJabberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortJabberStatus.setStatus("mandatory")
_S3EnetPortFrmsRxOk_Type = Counter32
_S3EnetPortFrmsRxOk_Object = MibTableColumn
s3EnetPortFrmsRxOk = _S3EnetPortFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 6),
    _S3EnetPortFrmsRxOk_Type()
)
s3EnetPortFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortFrmsRxOk.setStatus("mandatory")
_S3EnetPortOctetsRxOk_Type = Counter32
_S3EnetPortOctetsRxOk_Object = MibTableColumn
s3EnetPortOctetsRxOk = _S3EnetPortOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 7),
    _S3EnetPortOctetsRxOk_Type()
)
s3EnetPortOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortOctetsRxOk.setStatus("mandatory")
_S3EnetPortMcastFrmsRxOk_Type = Counter32
_S3EnetPortMcastFrmsRxOk_Object = MibTableColumn
s3EnetPortMcastFrmsRxOk = _S3EnetPortMcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 8),
    _S3EnetPortMcastFrmsRxOk_Type()
)
s3EnetPortMcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortMcastFrmsRxOk.setStatus("mandatory")
_S3EnetPortBcastFrmsRxOk_Type = Counter32
_S3EnetPortBcastFrmsRxOk_Object = MibTableColumn
s3EnetPortBcastFrmsRxOk = _S3EnetPortBcastFrmsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 9),
    _S3EnetPortBcastFrmsRxOk_Type()
)
s3EnetPortBcastFrmsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortBcastFrmsRxOk.setStatus("mandatory")
_S3EnetPortColls_Type = Counter32
_S3EnetPortColls_Object = MibTableColumn
s3EnetPortColls = _S3EnetPortColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 10),
    _S3EnetPortColls_Type()
)
s3EnetPortColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortColls.setStatus("mandatory")
_S3EnetPortTooLongErrors_Type = Counter32
_S3EnetPortTooLongErrors_Object = MibTableColumn
s3EnetPortTooLongErrors = _S3EnetPortTooLongErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 11),
    _S3EnetPortTooLongErrors_Type()
)
s3EnetPortTooLongErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortTooLongErrors.setStatus("mandatory")
_S3EnetPortRuntErrors_Type = Counter32
_S3EnetPortRuntErrors_Object = MibTableColumn
s3EnetPortRuntErrors = _S3EnetPortRuntErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 12),
    _S3EnetPortRuntErrors_Type()
)
s3EnetPortRuntErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortRuntErrors.setStatus("mandatory")
_S3EnetPortAlignErrors_Type = Counter32
_S3EnetPortAlignErrors_Object = MibTableColumn
s3EnetPortAlignErrors = _S3EnetPortAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 13),
    _S3EnetPortAlignErrors_Type()
)
s3EnetPortAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortAlignErrors.setStatus("mandatory")
_S3EnetPortFcsErrors_Type = Counter32
_S3EnetPortFcsErrors_Object = MibTableColumn
s3EnetPortFcsErrors = _S3EnetPortFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 14),
    _S3EnetPortFcsErrors_Type()
)
s3EnetPortFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortFcsErrors.setStatus("mandatory")
_S3EnetPortLateCollErrors_Type = Counter32
_S3EnetPortLateCollErrors_Object = MibTableColumn
s3EnetPortLateCollErrors = _S3EnetPortLateCollErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 15),
    _S3EnetPortLateCollErrors_Type()
)
s3EnetPortLateCollErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortLateCollErrors.setStatus("mandatory")


class _S3EnetPortAuthStatus_Type(Integer32):
    """Custom type s3EnetPortAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3EnetPortAuthStatus_Type.__name__ = "Integer32"
_S3EnetPortAuthStatus_Object = MibTableColumn
s3EnetPortAuthStatus = _S3EnetPortAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 16),
    _S3EnetPortAuthStatus_Type()
)
s3EnetPortAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortAuthStatus.setStatus("mandatory")


class _S3EnetPortAuthAction_Type(Integer32):
    """Custom type s3EnetPortAuthAction based on Integer32"""
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
        *(("noAction", 2),
          ("other", 1),
          ("partition", 4),
          ("sendTrap", 3),
          ("sendTrapPartition", 5))
    )


_S3EnetPortAuthAction_Type.__name__ = "Integer32"
_S3EnetPortAuthAction_Object = MibTableColumn
s3EnetPortAuthAction = _S3EnetPortAuthAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 17),
    _S3EnetPortAuthAction_Type()
)
s3EnetPortAuthAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortAuthAction.setStatus("mandatory")
_S3EnetPortPartTime_Type = TimeTicks
_S3EnetPortPartTime_Object = MibTableColumn
s3EnetPortPartTime = _S3EnetPortPartTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 18),
    _S3EnetPortPartTime_Type()
)
s3EnetPortPartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortPartTime.setStatus("deprecated")


class _S3EnetPortType_Type(Integer32):
    """Custom type s3EnetPortType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("bnc", 5),
          ("foirl", 6),
          ("other", 1),
          ("switch", 8),
          ("switchMdi", 9),
          ("tenBaseFL", 7),
          ("tenBaseFLRedund", 10),
          ("tenBaseT", 2),
          ("tenBaseTMdi", 3))
    )


_S3EnetPortType_Type.__name__ = "Integer32"
_S3EnetPortType_Object = MibTableColumn
s3EnetPortType = _S3EnetPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 19),
    _S3EnetPortType_Type()
)
s3EnetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortType.setStatus("deprecated")


class _S3EnetPortInterconStatus_Type(Integer32):
    """Custom type s3EnetPortInterconStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interconnect", 2),
          ("other", 1))
    )


_S3EnetPortInterconStatus_Type.__name__ = "Integer32"
_S3EnetPortInterconStatus_Object = MibTableColumn
s3EnetPortInterconStatus = _S3EnetPortInterconStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 20),
    _S3EnetPortInterconStatus_Type()
)
s3EnetPortInterconStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortInterconStatus.setStatus("mandatory")


class _S3EnetPortAddrCollect_Type(Integer32):
    """Custom type s3EnetPortAddrCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysCollect", 3),
          ("default", 1),
          ("neverCollect", 2))
    )


_S3EnetPortAddrCollect_Type.__name__ = "Integer32"
_S3EnetPortAddrCollect_Object = MibTableColumn
s3EnetPortAddrCollect = _S3EnetPortAddrCollect_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 21),
    _S3EnetPortAddrCollect_Type()
)
s3EnetPortAddrCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortAddrCollect.setStatus("mandatory")


class _S3EnetPortAddrLearnMode_Type(Integer32):
    """Custom type s3EnetPortAddrLearnMode based on Integer32"""
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
        *(("continuousLearn", 3),
          ("noAutoLearn", 2),
          ("oneShotLearn", 4),
          ("other", 1))
    )


_S3EnetPortAddrLearnMode_Type.__name__ = "Integer32"
_S3EnetPortAddrLearnMode_Object = MibTableColumn
s3EnetPortAddrLearnMode = _S3EnetPortAddrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 22),
    _S3EnetPortAddrLearnMode_Type()
)
s3EnetPortAddrLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortAddrLearnMode.setStatus("mandatory")


class _S3EnetPortTxSecurity_Type(Integer32):
    """Custom type s3EnetPortTxSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("other", 1))
    )


_S3EnetPortTxSecurity_Type.__name__ = "Integer32"
_S3EnetPortTxSecurity_Object = MibTableColumn
s3EnetPortTxSecurity = _S3EnetPortTxSecurity_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 1, 1, 23),
    _S3EnetPortTxSecurity_Type()
)
s3EnetPortTxSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetPortTxSecurity.setStatus("mandatory")
_S3EnetCommonPortTable_Object = MibTable
s3EnetCommonPortTable = _S3EnetCommonPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    s3EnetCommonPortTable.setStatus("mandatory")
_S3EnetCommonPortEntry_Object = MibTableRow
s3EnetCommonPortEntry = _S3EnetCommonPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1)
)
s3EnetCommonPortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetCommonPortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetCommonPortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetCommonPortEntry.setStatus("mandatory")
_S3EnetCommonPortBoardIndex_Type = Integer32
_S3EnetCommonPortBoardIndex_Object = MibTableColumn
s3EnetCommonPortBoardIndex = _S3EnetCommonPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 1),
    _S3EnetCommonPortBoardIndex_Type()
)
s3EnetCommonPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonPortBoardIndex.setStatus("mandatory")
_S3EnetCommonPortIndex_Type = Integer32
_S3EnetCommonPortIndex_Object = MibTableColumn
s3EnetCommonPortIndex = _S3EnetCommonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 2),
    _S3EnetCommonPortIndex_Type()
)
s3EnetCommonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonPortIndex.setStatus("mandatory")


class _S3EnetCommonPortLinkStatus_Type(Integer32):
    """Custom type s3EnetCommonPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("other", 3))
    )


_S3EnetCommonPortLinkStatus_Type.__name__ = "Integer32"
_S3EnetCommonPortLinkStatus_Object = MibTableColumn
s3EnetCommonPortLinkStatus = _S3EnetCommonPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 3),
    _S3EnetCommonPortLinkStatus_Type()
)
s3EnetCommonPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonPortLinkStatus.setStatus("mandatory")


class _S3EnetCommonPortPartStatus_Type(Integer32):
    """Custom type s3EnetCommonPortPartStatus based on Integer32"""
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
        *(("autoPartition", 3),
          ("enabled", 1),
          ("latSecPartition", 5),
          ("partition", 2),
          ("timedPartition", 4))
    )


_S3EnetCommonPortPartStatus_Type.__name__ = "Integer32"
_S3EnetCommonPortPartStatus_Object = MibTableColumn
s3EnetCommonPortPartStatus = _S3EnetCommonPortPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 4),
    _S3EnetCommonPortPartStatus_Type()
)
s3EnetCommonPortPartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetCommonPortPartStatus.setStatus("mandatory")


class _S3EnetCommonPortType_Type(Integer32):
    """Custom type s3EnetCommonPortType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("aui", 4),
          ("bnc", 5),
          ("foirl", 6),
          ("other", 1),
          ("switch", 8),
          ("switchMdi", 9),
          ("tenBaseFL", 7),
          ("tenBaseFLRedund", 10),
          ("tenBaseT", 2),
          ("tenBaseTMdi", 3))
    )


_S3EnetCommonPortType_Type.__name__ = "Integer32"
_S3EnetCommonPortType_Object = MibTableColumn
s3EnetCommonPortType = _S3EnetCommonPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 5),
    _S3EnetCommonPortType_Type()
)
s3EnetCommonPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetCommonPortType.setStatus("mandatory")
_S3EnetCommonPortPartTime_Type = TimeTicks
_S3EnetCommonPortPartTime_Object = MibTableColumn
s3EnetCommonPortPartTime = _S3EnetCommonPortPartTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 2, 1, 6),
    _S3EnetCommonPortPartTime_Type()
)
s3EnetCommonPortPartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetCommonPortPartTime.setStatus("mandatory")
_S3EnetRedPortTable_Object = MibTable
s3EnetRedPortTable = _S3EnetRedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    s3EnetRedPortTable.setStatus("mandatory")
_S3EnetRedPortEntry_Object = MibTableRow
s3EnetRedPortEntry = _S3EnetRedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1)
)
s3EnetRedPortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRedPortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetRedPortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetRedPortEntry.setStatus("mandatory")
_S3EnetRedPortBoardIndex_Type = Integer32
_S3EnetRedPortBoardIndex_Object = MibTableColumn
s3EnetRedPortBoardIndex = _S3EnetRedPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 1),
    _S3EnetRedPortBoardIndex_Type()
)
s3EnetRedPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortBoardIndex.setStatus("mandatory")
_S3EnetRedPortIndex_Type = Integer32
_S3EnetRedPortIndex_Object = MibTableColumn
s3EnetRedPortIndex = _S3EnetRedPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 2),
    _S3EnetRedPortIndex_Type()
)
s3EnetRedPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortIndex.setStatus("mandatory")


class _S3EnetRedPortRedundMode_Type(Integer32):
    """Custom type s3EnetRedPortRedundMode based on Integer32"""
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
        *(("hwActive", 2),
          ("hwStandby", 3),
          ("standAlone", 1),
          ("swActive", 4),
          ("swStandby", 5))
    )


_S3EnetRedPortRedundMode_Type.__name__ = "Integer32"
_S3EnetRedPortRedundMode_Object = MibTableColumn
s3EnetRedPortRedundMode = _S3EnetRedPortRedundMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 3),
    _S3EnetRedPortRedundMode_Type()
)
s3EnetRedPortRedundMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetRedPortRedundMode.setStatus("mandatory")


class _S3EnetRedPortOperStatus_Type(Integer32):
    """Custom type s3EnetRedPortOperStatus based on Integer32"""
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
        *(("localFault", 3),
          ("ok", 2),
          ("other", 1),
          ("remoteFault", 4))
    )


_S3EnetRedPortOperStatus_Type.__name__ = "Integer32"
_S3EnetRedPortOperStatus_Object = MibTableColumn
s3EnetRedPortOperStatus = _S3EnetRedPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 4),
    _S3EnetRedPortOperStatus_Type()
)
s3EnetRedPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortOperStatus.setStatus("mandatory")


class _S3EnetRedPortRemoteOperStatus_Type(Integer32):
    """Custom type s3EnetRedPortRemoteOperStatus based on Integer32"""
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
        *(("snpxFLFBRemFltCpblPortUp", 2),
          ("snpxFLRemFltCpblPortUp", 1),
          ("snpxRemFltCpblPortFault", 5),
          ("tenBaseFBPortFault", 6),
          ("tenBaseFBPortUp", 4),
          ("tenBaseFLPortUp", 3),
          ("unknown", 7))
    )


_S3EnetRedPortRemoteOperStatus_Type.__name__ = "Integer32"
_S3EnetRedPortRemoteOperStatus_Object = MibTableColumn
s3EnetRedPortRemoteOperStatus = _S3EnetRedPortRemoteOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 5),
    _S3EnetRedPortRemoteOperStatus_Type()
)
s3EnetRedPortRemoteOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortRemoteOperStatus.setStatus("mandatory")
_S3EnetRedPortCompanionSlotNo_Type = Integer32
_S3EnetRedPortCompanionSlotNo_Object = MibTableColumn
s3EnetRedPortCompanionSlotNo = _S3EnetRedPortCompanionSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 6),
    _S3EnetRedPortCompanionSlotNo_Type()
)
s3EnetRedPortCompanionSlotNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetRedPortCompanionSlotNo.setStatus("mandatory")
_S3EnetRedPortCompanionPortNo_Type = Integer32
_S3EnetRedPortCompanionPortNo_Object = MibTableColumn
s3EnetRedPortCompanionPortNo = _S3EnetRedPortCompanionPortNo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 7),
    _S3EnetRedPortCompanionPortNo_Type()
)
s3EnetRedPortCompanionPortNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetRedPortCompanionPortNo.setStatus("mandatory")


class _S3EnetRedPortSwitchoverStatus_Type(Integer32):
    """Custom type s3EnetRedPortSwitchoverStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("timedSwitchover", 2))
    )


_S3EnetRedPortSwitchoverStatus_Type.__name__ = "Integer32"
_S3EnetRedPortSwitchoverStatus_Object = MibTableColumn
s3EnetRedPortSwitchoverStatus = _S3EnetRedPortSwitchoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 8),
    _S3EnetRedPortSwitchoverStatus_Type()
)
s3EnetRedPortSwitchoverStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetRedPortSwitchoverStatus.setStatus("mandatory")


class _S3EnetRedPortSwitchoverTime_Type(TimeTicks):
    """Custom type s3EnetRedPortSwitchoverTime based on TimeTicks"""
    defaultValue = 0


_S3EnetRedPortSwitchoverTime_Object = MibTableColumn
s3EnetRedPortSwitchoverTime = _S3EnetRedPortSwitchoverTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 9),
    _S3EnetRedPortSwitchoverTime_Type()
)
s3EnetRedPortSwitchoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetRedPortSwitchoverTime.setStatus("mandatory")


class _S3EnetRedPortCapability_Type(Integer32):
    """Custom type s3EnetRedPortCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hwRedOnly", 1),
          ("notRedunCapable", 3),
          ("swRedOnly", 2))
    )


_S3EnetRedPortCapability_Type.__name__ = "Integer32"
_S3EnetRedPortCapability_Object = MibTableColumn
s3EnetRedPortCapability = _S3EnetRedPortCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 3, 1, 10),
    _S3EnetRedPortCapability_Type()
)
s3EnetRedPortCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortCapability.setStatus("mandatory")
_S3EnetRedPortLastChg_Type = TimeTicks
_S3EnetRedPortLastChg_Object = MibScalar
s3EnetRedPortLastChg = _S3EnetRedPortLastChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 3, 4),
    _S3EnetRedPortLastChg_Type()
)
s3EnetRedPortLastChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetRedPortLastChg.setStatus("mandatory")
_S3000EnetNmm_ObjectIdentity = ObjectIdentity
s3000EnetNmm = _S3000EnetNmm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4)
)


class _S3EnetNmmType_Type(Integer32):
    """Custom type s3EnetNmmType based on Integer32"""
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
        *(("m3138", 6),
          ("m3313", 2),
          ("m3313M", 3),
          ("m3314-ST", 4),
          ("m3314M-ST", 5),
          ("other", 1))
    )


_S3EnetNmmType_Type.__name__ = "Integer32"
_S3EnetNmmType_Object = MibScalar
s3EnetNmmType = _S3EnetNmmType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 1),
    _S3EnetNmmType_Type()
)
s3EnetNmmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmType.setStatus("obsolete")
_S3EnetNmmMdaHwVer_Type = Integer32
_S3EnetNmmMdaHwVer_Object = MibScalar
s3EnetNmmMdaHwVer = _S3EnetNmmMdaHwVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 2),
    _S3EnetNmmMdaHwVer_Type()
)
s3EnetNmmMdaHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmMdaHwVer.setStatus("obsolete")
_S3EnetNmmFwVer_Type = Integer32
_S3EnetNmmFwVer_Object = MibScalar
s3EnetNmmFwVer = _S3EnetNmmFwVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 3),
    _S3EnetNmmFwVer_Type()
)
s3EnetNmmFwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmFwVer.setStatus("obsolete")
_S3EnetNmmSwMajorVer_Type = Integer32
_S3EnetNmmSwMajorVer_Object = MibScalar
s3EnetNmmSwMajorVer = _S3EnetNmmSwMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 4),
    _S3EnetNmmSwMajorVer_Type()
)
s3EnetNmmSwMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmSwMajorVer.setStatus("obsolete")
_S3EnetNmmSwMinorVer_Type = Integer32
_S3EnetNmmSwMinorVer_Object = MibScalar
s3EnetNmmSwMinorVer = _S3EnetNmmSwMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 5),
    _S3EnetNmmSwMinorVer_Type()
)
s3EnetNmmSwMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmSwMinorVer.setStatus("obsolete")


class _S3EnetNmmStatus_Type(Integer32):
    """Custom type s3EnetNmmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_S3EnetNmmStatus_Type.__name__ = "Integer32"
_S3EnetNmmStatus_Object = MibScalar
s3EnetNmmStatus = _S3EnetNmmStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 6),
    _S3EnetNmmStatus_Type()
)
s3EnetNmmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmStatus.setStatus("obsolete")


class _S3EnetNmmMode_Type(Integer32):
    """Custom type s3EnetNmmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_S3EnetNmmMode_Type.__name__ = "Integer32"
_S3EnetNmmMode_Object = MibScalar
s3EnetNmmMode = _S3EnetNmmMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 7),
    _S3EnetNmmMode_Type()
)
s3EnetNmmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmMode.setStatus("obsolete")


class _S3EnetNmmReset_Type(Integer32):
    """Custom type s3EnetNmmReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notreset", 1),
          ("reset", 2))
    )


_S3EnetNmmReset_Type.__name__ = "Integer32"
_S3EnetNmmReset_Object = MibScalar
s3EnetNmmReset = _S3EnetNmmReset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 8),
    _S3EnetNmmReset_Type()
)
s3EnetNmmReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmReset.setStatus("obsolete")


class _S3EnetNmmRestart_Type(Integer32):
    """Custom type s3EnetNmmRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notrestart", 1),
          ("restart", 2))
    )


_S3EnetNmmRestart_Type.__name__ = "Integer32"
_S3EnetNmmRestart_Object = MibScalar
s3EnetNmmRestart = _S3EnetNmmRestart_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 9),
    _S3EnetNmmRestart_Type()
)
s3EnetNmmRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmRestart.setStatus("obsolete")
_S3EnetNmmIpAddr_Type = IpAddress
_S3EnetNmmIpAddr_Object = MibScalar
s3EnetNmmIpAddr = _S3EnetNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 10),
    _S3EnetNmmIpAddr_Type()
)
s3EnetNmmIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmIpAddr.setStatus("obsolete")
_S3EnetNmmNetMask_Type = IpAddress
_S3EnetNmmNetMask_Object = MibScalar
s3EnetNmmNetMask = _S3EnetNmmNetMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 11),
    _S3EnetNmmNetMask_Type()
)
s3EnetNmmNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmNetMask.setStatus("obsolete")
_S3EnetNmmDefaultGateway_Type = IpAddress
_S3EnetNmmDefaultGateway_Object = MibScalar
s3EnetNmmDefaultGateway = _S3EnetNmmDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 12),
    _S3EnetNmmDefaultGateway_Type()
)
s3EnetNmmDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmDefaultGateway.setStatus("obsolete")
_S3EnetNmmFileServerAddr_Type = IpAddress
_S3EnetNmmFileServerAddr_Object = MibScalar
s3EnetNmmFileServerAddr = _S3EnetNmmFileServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 13),
    _S3EnetNmmFileServerAddr_Type()
)
s3EnetNmmFileServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmFileServerAddr.setStatus("obsolete")


class _S3EnetNmmBootFile_Type(OctetString):
    """Custom type s3EnetNmmBootFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S3EnetNmmBootFile_Type.__name__ = "OctetString"
_S3EnetNmmBootFile_Object = MibScalar
s3EnetNmmBootFile = _S3EnetNmmBootFile_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 14),
    _S3EnetNmmBootFile_Type()
)
s3EnetNmmBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmBootFile.setStatus("obsolete")


class _S3EnetNmmBootMode_Type(Integer32):
    """Custom type s3EnetNmmBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("eeprom", 1))
    )


_S3EnetNmmBootMode_Type.__name__ = "Integer32"
_S3EnetNmmBootMode_Object = MibScalar
s3EnetNmmBootMode = _S3EnetNmmBootMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 15),
    _S3EnetNmmBootMode_Type()
)
s3EnetNmmBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmBootMode.setStatus("obsolete")


class _S3EnetNmmWriteEeprom_Type(Integer32):
    """Custom type s3EnetNmmWriteEeprom based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notWriteEeprom", 1),
          ("writeEeprom", 2))
    )


_S3EnetNmmWriteEeprom_Type.__name__ = "Integer32"
_S3EnetNmmWriteEeprom_Object = MibScalar
s3EnetNmmWriteEeprom = _S3EnetNmmWriteEeprom_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 16),
    _S3EnetNmmWriteEeprom_Type()
)
s3EnetNmmWriteEeprom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmWriteEeprom.setStatus("obsolete")
_S3EnetNmmBaudRate_Type = Gauge32
_S3EnetNmmBaudRate_Object = MibScalar
s3EnetNmmBaudRate = _S3EnetNmmBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 17),
    _S3EnetNmmBaudRate_Type()
)
s3EnetNmmBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetNmmBaudRate.setStatus("obsolete")


class _S3EnetNmmInitString_Type(OctetString):
    """Custom type s3EnetNmmInitString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S3EnetNmmInitString_Type.__name__ = "OctetString"
_S3EnetNmmInitString_Object = MibScalar
s3EnetNmmInitString = _S3EnetNmmInitString_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 18),
    _S3EnetNmmInitString_Type()
)
s3EnetNmmInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmInitString.setStatus("obsolete")


class _S3EnetNmmLocation_Type(OctetString):
    """Custom type s3EnetNmmLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_S3EnetNmmLocation_Type.__name__ = "OctetString"
_S3EnetNmmLocation_Object = MibScalar
s3EnetNmmLocation = _S3EnetNmmLocation_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 19),
    _S3EnetNmmLocation_Type()
)
s3EnetNmmLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmLocation.setStatus("obsolete")
_S3EnetNmmTrapServerTable_Object = MibTable
s3EnetNmmTrapServerTable = _S3EnetNmmTrapServerTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 20)
)
if mibBuilder.loadTexts:
    s3EnetNmmTrapServerTable.setStatus("obsolete")
_S3EnetNmmTrapServerEntry_Object = MibTableRow
s3EnetNmmTrapServerEntry = _S3EnetNmmTrapServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 20, 1)
)
s3EnetNmmTrapServerEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetNmmTrapServerAddress"),
)
if mibBuilder.loadTexts:
    s3EnetNmmTrapServerEntry.setStatus("obsolete")


class _S3EnetNmmTrapType_Type(Integer32):
    """Custom type s3EnetNmmTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1))
    )


_S3EnetNmmTrapType_Type.__name__ = "Integer32"
_S3EnetNmmTrapType_Object = MibTableColumn
s3EnetNmmTrapType = _S3EnetNmmTrapType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 20, 1, 1),
    _S3EnetNmmTrapType_Type()
)
s3EnetNmmTrapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmTrapType.setStatus("obsolete")
_S3EnetNmmTrapServerAddress_Type = IpAddress
_S3EnetNmmTrapServerAddress_Object = MibTableColumn
s3EnetNmmTrapServerAddress = _S3EnetNmmTrapServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 20, 1, 2),
    _S3EnetNmmTrapServerAddress_Type()
)
s3EnetNmmTrapServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmTrapServerAddress.setStatus("obsolete")


class _S3EnetNmmTrapServerComm_Type(OctetString):
    """Custom type s3EnetNmmTrapServerComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_S3EnetNmmTrapServerComm_Type.__name__ = "OctetString"
_S3EnetNmmTrapServerComm_Object = MibTableColumn
s3EnetNmmTrapServerComm = _S3EnetNmmTrapServerComm_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 20, 1, 3),
    _S3EnetNmmTrapServerComm_Type()
)
s3EnetNmmTrapServerComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmTrapServerComm.setStatus("obsolete")


class _S3EnetNmmAuthTrap_Type(Integer32):
    """Custom type s3EnetNmmAuthTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_S3EnetNmmAuthTrap_Type.__name__ = "Integer32"
_S3EnetNmmAuthTrap_Object = MibScalar
s3EnetNmmAuthTrap = _S3EnetNmmAuthTrap_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 4, 21),
    _S3EnetNmmAuthTrap_Type()
)
s3EnetNmmAuthTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNmmAuthTrap.setStatus("obsolete")
_S3000EnetNode_ObjectIdentity = ObjectIdentity
s3000EnetNode = _S3000EnetNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5)
)
_S3EnetShowNodesTable_Object = MibTable
s3EnetShowNodesTable = _S3EnetShowNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1)
)
if mibBuilder.loadTexts:
    s3EnetShowNodesTable.setStatus("mandatory")
_S3EnetShowNodesEntry_Object = MibTableRow
s3EnetShowNodesEntry = _S3EnetShowNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1)
)
s3EnetShowNodesEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetShowNodesSlotIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetShowNodesPortIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetShowNodesMacAddress"),
)
if mibBuilder.loadTexts:
    s3EnetShowNodesEntry.setStatus("mandatory")
_S3EnetShowNodesSlotIndex_Type = Integer32
_S3EnetShowNodesSlotIndex_Object = MibTableColumn
s3EnetShowNodesSlotIndex = _S3EnetShowNodesSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 1),
    _S3EnetShowNodesSlotIndex_Type()
)
s3EnetShowNodesSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesSlotIndex.setStatus("mandatory")
_S3EnetShowNodesPortIndex_Type = Integer32
_S3EnetShowNodesPortIndex_Object = MibTableColumn
s3EnetShowNodesPortIndex = _S3EnetShowNodesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 2),
    _S3EnetShowNodesPortIndex_Type()
)
s3EnetShowNodesPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesPortIndex.setStatus("mandatory")


class _S3EnetShowNodesMacAddress_Type(PhysAddress):
    """Custom type s3EnetShowNodesMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetShowNodesMacAddress_Type.__name__ = "PhysAddress"
_S3EnetShowNodesMacAddress_Object = MibTableColumn
s3EnetShowNodesMacAddress = _S3EnetShowNodesMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 3),
    _S3EnetShowNodesMacAddress_Type()
)
s3EnetShowNodesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesMacAddress.setStatus("mandatory")


class _S3EnetShowNodesStatus_Type(Integer32):
    """Custom type s3EnetShowNodesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_S3EnetShowNodesStatus_Type.__name__ = "Integer32"
_S3EnetShowNodesStatus_Object = MibTableColumn
s3EnetShowNodesStatus = _S3EnetShowNodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 4),
    _S3EnetShowNodesStatus_Type()
)
s3EnetShowNodesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesStatus.setStatus("mandatory")


class _S3EnetShowNodesVendorType_Type(Integer32):
    """Custom type s3EnetShowNodesVendorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("threeCom", 2))
    )


_S3EnetShowNodesVendorType_Type.__name__ = "Integer32"
_S3EnetShowNodesVendorType_Object = MibTableColumn
s3EnetShowNodesVendorType = _S3EnetShowNodesVendorType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 5),
    _S3EnetShowNodesVendorType_Type()
)
s3EnetShowNodesVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesVendorType.setStatus("deprecated")


class _S3EnetShowNodesAuthStatus_Type(Integer32):
    """Custom type s3EnetShowNodesAuthStatus based on Integer32"""
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
        *(("authorized", 4),
          ("network", 2),
          ("nmm", 3),
          ("other", 1))
    )


_S3EnetShowNodesAuthStatus_Type.__name__ = "Integer32"
_S3EnetShowNodesAuthStatus_Object = MibTableColumn
s3EnetShowNodesAuthStatus = _S3EnetShowNodesAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 1, 1, 6),
    _S3EnetShowNodesAuthStatus_Type()
)
s3EnetShowNodesAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetShowNodesAuthStatus.setStatus("mandatory")
_S3EnetNodeAgeInterval_Type = TimeTicks
_S3EnetNodeAgeInterval_Object = MibScalar
s3EnetNodeAgeInterval = _S3EnetNodeAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 2),
    _S3EnetNodeAgeInterval_Type()
)
s3EnetNodeAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetNodeAgeInterval.setStatus("mandatory")
_S3EnetFindNodesTable_Object = MibTable
s3EnetFindNodesTable = _S3EnetFindNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 3)
)
if mibBuilder.loadTexts:
    s3EnetFindNodesTable.setStatus("mandatory")
_S3EnetFindNodesEntry_Object = MibTableRow
s3EnetFindNodesEntry = _S3EnetFindNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 3, 1)
)
s3EnetFindNodesEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetFindNodesMacAddress"),
)
if mibBuilder.loadTexts:
    s3EnetFindNodesEntry.setStatus("mandatory")


class _S3EnetFindNodesMacAddress_Type(PhysAddress):
    """Custom type s3EnetFindNodesMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetFindNodesMacAddress_Type.__name__ = "PhysAddress"
_S3EnetFindNodesMacAddress_Object = MibTableColumn
s3EnetFindNodesMacAddress = _S3EnetFindNodesMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 3, 1, 1),
    _S3EnetFindNodesMacAddress_Type()
)
s3EnetFindNodesMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFindNodesMacAddress.setStatus("mandatory")
_S3EnetFindNodesSlotIndex_Type = Integer32
_S3EnetFindNodesSlotIndex_Object = MibTableColumn
s3EnetFindNodesSlotIndex = _S3EnetFindNodesSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 3, 1, 2),
    _S3EnetFindNodesSlotIndex_Type()
)
s3EnetFindNodesSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFindNodesSlotIndex.setStatus("mandatory")
_S3EnetFindNodesPortIndex_Type = Integer32
_S3EnetFindNodesPortIndex_Object = MibTableColumn
s3EnetFindNodesPortIndex = _S3EnetFindNodesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 3, 1, 3),
    _S3EnetFindNodesPortIndex_Type()
)
s3EnetFindNodesPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFindNodesPortIndex.setStatus("mandatory")
_S3EnetAuthNodesTable_Object = MibTable
s3EnetAuthNodesTable = _S3EnetAuthNodesTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4)
)
if mibBuilder.loadTexts:
    s3EnetAuthNodesTable.setStatus("mandatory")
_S3EnetAuthNodesEntry_Object = MibTableRow
s3EnetAuthNodesEntry = _S3EnetAuthNodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4, 1)
)
s3EnetAuthNodesEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetAuthNodesMacAddr"),
)
if mibBuilder.loadTexts:
    s3EnetAuthNodesEntry.setStatus("mandatory")


class _S3EnetAuthNodesMacAddr_Type(PhysAddress):
    """Custom type s3EnetAuthNodesMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetAuthNodesMacAddr_Type.__name__ = "PhysAddress"
_S3EnetAuthNodesMacAddr_Object = MibTableColumn
s3EnetAuthNodesMacAddr = _S3EnetAuthNodesMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4, 1, 1),
    _S3EnetAuthNodesMacAddr_Type()
)
s3EnetAuthNodesMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetAuthNodesMacAddr.setStatus("mandatory")
_S3EnetAuthNodesSlotIndex_Type = Integer32
_S3EnetAuthNodesSlotIndex_Object = MibTableColumn
s3EnetAuthNodesSlotIndex = _S3EnetAuthNodesSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4, 1, 2),
    _S3EnetAuthNodesSlotIndex_Type()
)
s3EnetAuthNodesSlotIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetAuthNodesSlotIndex.setStatus("mandatory")
_S3EnetAuthNodesPortIndex_Type = Integer32
_S3EnetAuthNodesPortIndex_Object = MibTableColumn
s3EnetAuthNodesPortIndex = _S3EnetAuthNodesPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4, 1, 3),
    _S3EnetAuthNodesPortIndex_Type()
)
s3EnetAuthNodesPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetAuthNodesPortIndex.setStatus("mandatory")


class _S3EnetAuthNodesStatus_Type(Integer32):
    """Custom type s3EnetAuthNodesStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_S3EnetAuthNodesStatus_Type.__name__ = "Integer32"
_S3EnetAuthNodesStatus_Object = MibTableColumn
s3EnetAuthNodesStatus = _S3EnetAuthNodesStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 4, 1, 4),
    _S3EnetAuthNodesStatus_Type()
)
s3EnetAuthNodesStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetAuthNodesStatus.setStatus("mandatory")


class _S3EnetMaxNodesPerPort_Type(Integer32):
    """Custom type s3EnetMaxNodesPerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S3EnetMaxNodesPerPort_Type.__name__ = "Integer32"
_S3EnetMaxNodesPerPort_Object = MibScalar
s3EnetMaxNodesPerPort = _S3EnetMaxNodesPerPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 5, 5),
    _S3EnetMaxNodesPerPort_Type()
)
s3EnetMaxNodesPerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetMaxNodesPerPort.setStatus("mandatory")
_S3000EnetTopology_ObjectIdentity = ObjectIdentity
s3000EnetTopology = _S3000EnetTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6)
)
_S3000EnetNmmTopology_ObjectIdentity = ObjectIdentity
s3000EnetNmmTopology = _S3000EnetNmmTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1)
)
_S3EnetTopNmmTable_Object = MibTable
s3EnetTopNmmTable = _S3EnetTopNmmTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    s3EnetTopNmmTable.setStatus("mandatory")
_S3EnetTopNmmEntry_Object = MibTableRow
s3EnetTopNmmEntry = _S3EnetTopNmmEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1)
)
s3EnetTopNmmEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmSlot"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmPort"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s3EnetTopNmmEntry.setStatus("mandatory")
_S3EnetTopNmmSlot_Type = Integer32
_S3EnetTopNmmSlot_Object = MibTableColumn
s3EnetTopNmmSlot = _S3EnetTopNmmSlot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 1),
    _S3EnetTopNmmSlot_Type()
)
s3EnetTopNmmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmSlot.setStatus("mandatory")
_S3EnetTopNmmPort_Type = Integer32
_S3EnetTopNmmPort_Object = MibTableColumn
s3EnetTopNmmPort = _S3EnetTopNmmPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 2),
    _S3EnetTopNmmPort_Type()
)
s3EnetTopNmmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmPort.setStatus("mandatory")
_S3EnetTopNmmIpAddr_Type = IpAddress
_S3EnetTopNmmIpAddr_Object = MibTableColumn
s3EnetTopNmmIpAddr = _S3EnetTopNmmIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 3),
    _S3EnetTopNmmIpAddr_Type()
)
s3EnetTopNmmIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmIpAddr.setStatus("mandatory")


class _S3EnetTopNmmMacAddr_Type(PhysAddress):
    """Custom type s3EnetTopNmmMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetTopNmmMacAddr_Type.__name__ = "PhysAddress"
_S3EnetTopNmmMacAddr_Object = MibTableColumn
s3EnetTopNmmMacAddr = _S3EnetTopNmmMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 4),
    _S3EnetTopNmmMacAddr_Type()
)
s3EnetTopNmmMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmMacAddr.setStatus("mandatory")
_S3EnetTopNmmChassisType_Type = SnpxChassisType
_S3EnetTopNmmChassisType_Object = MibTableColumn
s3EnetTopNmmChassisType = _S3EnetTopNmmChassisType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 5),
    _S3EnetTopNmmChassisType_Type()
)
s3EnetTopNmmChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmChassisType.setStatus("mandatory")
_S3EnetTopNmmBkplType_Type = SnpxBackplaneType
_S3EnetTopNmmBkplType_Object = MibTableColumn
s3EnetTopNmmBkplType = _S3EnetTopNmmBkplType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 6),
    _S3EnetTopNmmBkplType_Type()
)
s3EnetTopNmmBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmBkplType.setStatus("mandatory")


class _S3EnetTopNmmLocalSeg_Type(Integer32):
    """Custom type s3EnetTopNmmLocalSeg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_S3EnetTopNmmLocalSeg_Type.__name__ = "Integer32"
_S3EnetTopNmmLocalSeg_Object = MibTableColumn
s3EnetTopNmmLocalSeg = _S3EnetTopNmmLocalSeg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 7),
    _S3EnetTopNmmLocalSeg_Type()
)
s3EnetTopNmmLocalSeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmLocalSeg.setStatus("mandatory")
_S3EnetTopNmmNumSeen_Type = Integer32
_S3EnetTopNmmNumSeen_Object = MibTableColumn
s3EnetTopNmmNumSeen = _S3EnetTopNmmNumSeen_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 8),
    _S3EnetTopNmmNumSeen_Type()
)
s3EnetTopNmmNumSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmNumSeen.setStatus("mandatory")
_S3EnetTopNmmModuleType_Type = S3ModuleType
_S3EnetTopNmmModuleType_Object = MibTableColumn
s3EnetTopNmmModuleType = _S3EnetTopNmmModuleType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 9),
    _S3EnetTopNmmModuleType_Type()
)
s3EnetTopNmmModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmModuleType.setStatus("mandatory")
_S3EnetTopNmmNumLinks_Type = Integer32
_S3EnetTopNmmNumLinks_Object = MibTableColumn
s3EnetTopNmmNumLinks = _S3EnetTopNmmNumLinks_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 10),
    _S3EnetTopNmmNumLinks_Type()
)
s3EnetTopNmmNumLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmNumLinks.setStatus("mandatory")


class _S3EnetTopNmmChgStatus_Type(Integer32):
    """Custom type s3EnetTopNmmChgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("changed", 1),
          ("noChange", 2))
    )


_S3EnetTopNmmChgStatus_Type.__name__ = "Integer32"
_S3EnetTopNmmChgStatus_Object = MibTableColumn
s3EnetTopNmmChgStatus = _S3EnetTopNmmChgStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 1, 1, 11),
    _S3EnetTopNmmChgStatus_Type()
)
s3EnetTopNmmChgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmChgStatus.setStatus("mandatory")
_S3EnetTopNmmHelloTime_Type = TimeTicks
_S3EnetTopNmmHelloTime_Object = MibScalar
s3EnetTopNmmHelloTime = _S3EnetTopNmmHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 2),
    _S3EnetTopNmmHelloTime_Type()
)
s3EnetTopNmmHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmHelloTime.setStatus("mandatory")
_S3EnetTopNmmSubsetTable_Object = MibTable
s3EnetTopNmmSubsetTable = _S3EnetTopNmmSubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    s3EnetTopNmmSubsetTable.setStatus("mandatory")
_S3EnetTopNmmSubsetEntry_Object = MibTableRow
s3EnetTopNmmSubsetEntry = _S3EnetTopNmmSubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 3, 1)
)
s3EnetTopNmmSubsetEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmSlot"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmPort"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopNmmIpAddr"),
)
if mibBuilder.loadTexts:
    s3EnetTopNmmSubsetEntry.setStatus("mandatory")


class _S3EnetTopNmmSubset_Type(OctetString):
    """Custom type s3EnetTopNmmSubset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S3EnetTopNmmSubset_Type.__name__ = "OctetString"
_S3EnetTopNmmSubset_Object = MibTableColumn
s3EnetTopNmmSubset = _S3EnetTopNmmSubset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 1, 3, 1, 1),
    _S3EnetTopNmmSubset_Type()
)
s3EnetTopNmmSubset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmSubset.setStatus("mandatory")
_S3000EnetBridTopology_ObjectIdentity = ObjectIdentity
s3000EnetBridTopology = _S3000EnetBridTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2)
)
_S3EnetTopBridgeTable_Object = MibTable
s3EnetTopBridgeTable = _S3EnetTopBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    s3EnetTopBridgeTable.setStatus("mandatory")
_S3EnetTopBridgeEntry_Object = MibTableRow
s3EnetTopBridgeEntry = _S3EnetTopBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1)
)
s3EnetTopBridgeEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopBridgeIpAddr"),
)
if mibBuilder.loadTexts:
    s3EnetTopBridgeEntry.setStatus("mandatory")
_S3EnetTopBridgeIpAddr_Type = IpAddress
_S3EnetTopBridgeIpAddr_Object = MibTableColumn
s3EnetTopBridgeIpAddr = _S3EnetTopBridgeIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 1),
    _S3EnetTopBridgeIpAddr_Type()
)
s3EnetTopBridgeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeIpAddr.setStatus("mandatory")
_S3EnetTopBridgeNumber_Type = Integer32
_S3EnetTopBridgeNumber_Object = MibTableColumn
s3EnetTopBridgeNumber = _S3EnetTopBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 2),
    _S3EnetTopBridgeNumber_Type()
)
s3EnetTopBridgeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeNumber.setStatus("mandatory")


class _S3EnetTopBridgeMacAddr_Type(PhysAddress):
    """Custom type s3EnetTopBridgeMacAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetTopBridgeMacAddr_Type.__name__ = "PhysAddress"
_S3EnetTopBridgeMacAddr_Object = MibTableColumn
s3EnetTopBridgeMacAddr = _S3EnetTopBridgeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 3),
    _S3EnetTopBridgeMacAddr_Type()
)
s3EnetTopBridgeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeMacAddr.setStatus("mandatory")


class _S3EnetTopBridgeType_Type(Integer32):
    """Custom type s3EnetTopBridgeType based on Integer32"""
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
        *(("etherSwitch", 4),
          ("localSyn2Port", 2),
          ("other", 1),
          ("remoteSyn3Port", 3))
    )


_S3EnetTopBridgeType_Type.__name__ = "Integer32"
_S3EnetTopBridgeType_Object = MibTableColumn
s3EnetTopBridgeType = _S3EnetTopBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 4),
    _S3EnetTopBridgeType_Type()
)
s3EnetTopBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeType.setStatus("mandatory")


class _S3EnetTopBridgeStatus_Type(Integer32):
    """Custom type s3EnetTopBridgeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_S3EnetTopBridgeStatus_Type.__name__ = "Integer32"
_S3EnetTopBridgeStatus_Object = MibTableColumn
s3EnetTopBridgeStatus = _S3EnetTopBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 5),
    _S3EnetTopBridgeStatus_Type()
)
s3EnetTopBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeStatus.setStatus("mandatory")
_S3EnetTopBridgeSlotNum_Type = Integer32
_S3EnetTopBridgeSlotNum_Object = MibTableColumn
s3EnetTopBridgeSlotNum = _S3EnetTopBridgeSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 6),
    _S3EnetTopBridgeSlotNum_Type()
)
s3EnetTopBridgeSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeSlotNum.setStatus("mandatory")
_S3EnetTopBridgePortNum_Type = Integer32
_S3EnetTopBridgePortNum_Object = MibTableColumn
s3EnetTopBridgePortNum = _S3EnetTopBridgePortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 7),
    _S3EnetTopBridgePortNum_Type()
)
s3EnetTopBridgePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgePortNum.setStatus("mandatory")
_S3EnetTopBridgeModuleType_Type = S3ModuleType
_S3EnetTopBridgeModuleType_Object = MibTableColumn
s3EnetTopBridgeModuleType = _S3EnetTopBridgeModuleType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 8),
    _S3EnetTopBridgeModuleType_Type()
)
s3EnetTopBridgeModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeModuleType.setStatus("mandatory")
_S3EnetTopBridgeHelloPortNum_Type = Integer32
_S3EnetTopBridgeHelloPortNum_Object = MibTableColumn
s3EnetTopBridgeHelloPortNum = _S3EnetTopBridgeHelloPortNum_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 9),
    _S3EnetTopBridgeHelloPortNum_Type()
)
s3EnetTopBridgeHelloPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeHelloPortNum.setStatus("mandatory")


class _S3EnetTopBridgeHelloPortType_Type(Integer32):
    """Custom type s3EnetTopBridgeHelloPortType based on Integer32"""
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
        *(("ether", 2),
          ("fddi", 5),
          ("other", 1),
          ("t1", 6),
          ("tokenRing16", 4),
          ("tokenRing4", 3))
    )


_S3EnetTopBridgeHelloPortType_Type.__name__ = "Integer32"
_S3EnetTopBridgeHelloPortType_Object = MibTableColumn
s3EnetTopBridgeHelloPortType = _S3EnetTopBridgeHelloPortType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 10),
    _S3EnetTopBridgeHelloPortType_Type()
)
s3EnetTopBridgeHelloPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeHelloPortType.setStatus("mandatory")


class _S3EnetTopBridgeHelloPortStatus_Type(Integer32):
    """Custom type s3EnetTopBridgeHelloPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("other", 1),
          ("standby", 3))
    )


_S3EnetTopBridgeHelloPortStatus_Type.__name__ = "Integer32"
_S3EnetTopBridgeHelloPortStatus_Object = MibTableColumn
s3EnetTopBridgeHelloPortStatus = _S3EnetTopBridgeHelloPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 11),
    _S3EnetTopBridgeHelloPortStatus_Type()
)
s3EnetTopBridgeHelloPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeHelloPortStatus.setStatus("mandatory")


class _S3EnetTopBridgeCompBridgeMac1_Type(PhysAddress):
    """Custom type s3EnetTopBridgeCompBridgeMac1 based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetTopBridgeCompBridgeMac1_Type.__name__ = "PhysAddress"
_S3EnetTopBridgeCompBridgeMac1_Object = MibTableColumn
s3EnetTopBridgeCompBridgeMac1 = _S3EnetTopBridgeCompBridgeMac1_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 12),
    _S3EnetTopBridgeCompBridgeMac1_Type()
)
s3EnetTopBridgeCompBridgeMac1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeCompBridgeMac1.setStatus("mandatory")


class _S3EnetTopBridgeCompBridgeMac2_Type(PhysAddress):
    """Custom type s3EnetTopBridgeCompBridgeMac2 based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetTopBridgeCompBridgeMac2_Type.__name__ = "PhysAddress"
_S3EnetTopBridgeCompBridgeMac2_Object = MibTableColumn
s3EnetTopBridgeCompBridgeMac2 = _S3EnetTopBridgeCompBridgeMac2_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 1, 1, 13),
    _S3EnetTopBridgeCompBridgeMac2_Type()
)
s3EnetTopBridgeCompBridgeMac2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeCompBridgeMac2.setStatus("mandatory")
_S3EnetTopBdgSubsetTable_Object = MibTable
s3EnetTopBdgSubsetTable = _S3EnetTopBdgSubsetTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 2)
)
if mibBuilder.loadTexts:
    s3EnetTopBdgSubsetTable.setStatus("mandatory")
_S3EnetTopBdgSubsetEntry_Object = MibTableRow
s3EnetTopBdgSubsetEntry = _S3EnetTopBdgSubsetEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 2, 1)
)
s3EnetTopBdgSubsetEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTopBridgeIpAddr"),
)
if mibBuilder.loadTexts:
    s3EnetTopBdgSubsetEntry.setStatus("mandatory")


class _S3EnetTopBdgSubset_Type(OctetString):
    """Custom type s3EnetTopBdgSubset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_S3EnetTopBdgSubset_Type.__name__ = "OctetString"
_S3EnetTopBdgSubset_Object = MibTableColumn
s3EnetTopBdgSubset = _S3EnetTopBdgSubset_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 2, 2, 1, 1),
    _S3EnetTopBdgSubset_Type()
)
s3EnetTopBdgSubset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBdgSubset.setStatus("mandatory")
_S3000EnetTopInfo_ObjectIdentity = ObjectIdentity
s3000EnetTopInfo = _S3000EnetTopInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 3)
)
_S3EnetTopNmmLstChg_Type = TimeTicks
_S3EnetTopNmmLstChg_Object = MibScalar
s3EnetTopNmmLstChg = _S3EnetTopNmmLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 3, 1),
    _S3EnetTopNmmLstChg_Type()
)
s3EnetTopNmmLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopNmmLstChg.setStatus("mandatory")
_S3EnetTopBridgeLstChg_Type = TimeTicks
_S3EnetTopBridgeLstChg_Object = MibScalar
s3EnetTopBridgeLstChg = _S3EnetTopBridgeLstChg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 6, 3, 2),
    _S3EnetTopBridgeLstChg_Type()
)
s3EnetTopBridgeLstChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTopBridgeLstChg.setStatus("mandatory")
_S3000EnetThreshold_ObjectIdentity = ObjectIdentity
s3000EnetThreshold = _S3000EnetThreshold_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8)
)
_S3EnetThreshTable_Object = MibTable
s3EnetThreshTable = _S3EnetThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1)
)
if mibBuilder.loadTexts:
    s3EnetThreshTable.setStatus("mandatory")
_S3EnetThreshEntry_Object = MibTableRow
s3EnetThreshEntry = _S3EnetThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1)
)
s3EnetThreshEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetThreshIndex"),
)
if mibBuilder.loadTexts:
    s3EnetThreshEntry.setStatus("mandatory")
_S3EnetThreshIndex_Type = Integer32
_S3EnetThreshIndex_Object = MibTableColumn
s3EnetThreshIndex = _S3EnetThreshIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 1),
    _S3EnetThreshIndex_Type()
)
s3EnetThreshIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetThreshIndex.setStatus("mandatory")


class _S3EnetThreshStatus_Type(Integer32):
    """Custom type s3EnetThreshStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("addActive", 1),
          ("delDead", 2))
    )


_S3EnetThreshStatus_Type.__name__ = "Integer32"
_S3EnetThreshStatus_Object = MibTableColumn
s3EnetThreshStatus = _S3EnetThreshStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 2),
    _S3EnetThreshStatus_Type()
)
s3EnetThreshStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshStatus.setStatus("mandatory")


class _S3EnetThreshObject_Type(Integer32):
    """Custom type s3EnetThreshObject based on Integer32"""
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
        *(("concentrator", 2),
          ("other", 1),
          ("port", 4),
          ("slot", 3))
    )


_S3EnetThreshObject_Type.__name__ = "Integer32"
_S3EnetThreshObject_Object = MibTableColumn
s3EnetThreshObject = _S3EnetThreshObject_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 3),
    _S3EnetThreshObject_Type()
)
s3EnetThreshObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshObject.setStatus("mandatory")
_S3EnetThreshSlot_Type = Integer32
_S3EnetThreshSlot_Object = MibTableColumn
s3EnetThreshSlot = _S3EnetThreshSlot_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 4),
    _S3EnetThreshSlot_Type()
)
s3EnetThreshSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshSlot.setStatus("mandatory")
_S3EnetThreshPort_Type = Integer32
_S3EnetThreshPort_Object = MibTableColumn
s3EnetThreshPort = _S3EnetThreshPort_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 5),
    _S3EnetThreshPort_Type()
)
s3EnetThreshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshPort.setStatus("mandatory")


class _S3EnetThreshType_Type(Integer32):
    """Custom type s3EnetThreshType based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("badPkts", 4),
          ("badToGoodPktRatio", 19),
          ("broadcast", 14),
          ("collBackOffErr", 22),
          ("collision", 10),
          ("colltoGoodPktRatio", 21),
          ("crcPkts", 5),
          ("dataRateMismatches", 17),
          ("fragPkts", 8),
          ("goodBytes", 2),
          ("goodPkts", 3),
          ("lateColls", 11),
          ("linkStatus", 12),
          ("misaligned", 6),
          ("multicast", 13),
          ("netErrToGoodPktRatio", 20),
          ("networkErrors", 18),
          ("other", 1),
          ("runtPkts", 7),
          ("shortEvents", 15),
          ("srcAddrChanges", 16),
          ("tooLong", 9))
    )


_S3EnetThreshType_Type.__name__ = "Integer32"
_S3EnetThreshType_Object = MibTableColumn
s3EnetThreshType = _S3EnetThreshType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 6),
    _S3EnetThreshType_Type()
)
s3EnetThreshType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshType.setStatus("mandatory")


class _S3EnetThreshCondition_Type(Integer32):
    """Custom type s3EnetThreshCondition based on Integer32"""
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
        *(("crossValue", 2),
          ("linkOff", 6),
          ("linkOn", 5),
          ("other", 1),
          ("overRate", 4),
          ("overRatio", 7),
          ("overValue", 3))
    )


_S3EnetThreshCondition_Type.__name__ = "Integer32"
_S3EnetThreshCondition_Object = MibTableColumn
s3EnetThreshCondition = _S3EnetThreshCondition_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 7),
    _S3EnetThreshCondition_Type()
)
s3EnetThreshCondition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshCondition.setStatus("mandatory")
_S3EnetThreshSetValue_Type = Integer32
_S3EnetThreshSetValue_Object = MibTableColumn
s3EnetThreshSetValue = _S3EnetThreshSetValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 8),
    _S3EnetThreshSetValue_Type()
)
s3EnetThreshSetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshSetValue.setStatus("mandatory")
_S3EnetThreshActualValue_Type = Integer32
_S3EnetThreshActualValue_Object = MibTableColumn
s3EnetThreshActualValue = _S3EnetThreshActualValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 9),
    _S3EnetThreshActualValue_Type()
)
s3EnetThreshActualValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetThreshActualValue.setStatus("mandatory")


class _S3EnetThreshAction_Type(Integer32):
    """Custom type s3EnetThreshAction based on Integer32"""
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
        *(("noAction", 2),
          ("other", 1),
          ("partSlot", 6),
          ("partSlotPort", 7),
          ("res4", 4),
          ("res5", 5),
          ("res8", 8),
          ("res9", 9),
          ("sendTrap", 3),
          ("trapPartSlot", 10),
          ("trapPartSlotPort", 11))
    )


_S3EnetThreshAction_Type.__name__ = "Integer32"
_S3EnetThreshAction_Object = MibTableColumn
s3EnetThreshAction = _S3EnetThreshAction_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 10),
    _S3EnetThreshAction_Type()
)
s3EnetThreshAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshAction.setStatus("mandatory")
_S3EnetThreshExceedCount_Type = Counter32
_S3EnetThreshExceedCount_Object = MibTableColumn
s3EnetThreshExceedCount = _S3EnetThreshExceedCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 11),
    _S3EnetThreshExceedCount_Type()
)
s3EnetThreshExceedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetThreshExceedCount.setStatus("mandatory")
_S3EnetThreshDuration_Type = TimeTicks
_S3EnetThreshDuration_Object = MibTableColumn
s3EnetThreshDuration = _S3EnetThreshDuration_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 1, 1, 12),
    _S3EnetThreshDuration_Type()
)
s3EnetThreshDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetThreshDuration.setStatus("mandatory")
_S3EnetThreshTableSize_Type = Integer32
_S3EnetThreshTableSize_Object = MibScalar
s3EnetThreshTableSize = _S3EnetThreshTableSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 8, 2),
    _S3EnetThreshTableSize_Type()
)
s3EnetThreshTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetThreshTableSize.setStatus("mandatory")
_S3000EnetSADATraffic_ObjectIdentity = ObjectIdentity
s3000EnetSADATraffic = _S3000EnetSADATraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9)
)
_S3EnetSdTrafTable_Object = MibTable
s3EnetSdTrafTable = _S3EnetSdTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1)
)
if mibBuilder.loadTexts:
    s3EnetSdTrafTable.setStatus("deprecated")
_S3EnetSdTrafEntry_Object = MibTableRow
s3EnetSdTrafEntry = _S3EnetSdTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1, 1)
)
s3EnetSdTrafEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetSdTrafMacSA"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetSdTrafMacDA"),
)
if mibBuilder.loadTexts:
    s3EnetSdTrafEntry.setStatus("deprecated")


class _S3EnetSdTrafMacSA_Type(PhysAddress):
    """Custom type s3EnetSdTrafMacSA based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetSdTrafMacSA_Type.__name__ = "PhysAddress"
_S3EnetSdTrafMacSA_Object = MibTableColumn
s3EnetSdTrafMacSA = _S3EnetSdTrafMacSA_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1, 1, 1),
    _S3EnetSdTrafMacSA_Type()
)
s3EnetSdTrafMacSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetSdTrafMacSA.setStatus("deprecated")


class _S3EnetSdTrafMacDA_Type(PhysAddress):
    """Custom type s3EnetSdTrafMacDA based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetSdTrafMacDA_Type.__name__ = "PhysAddress"
_S3EnetSdTrafMacDA_Object = MibTableColumn
s3EnetSdTrafMacDA = _S3EnetSdTrafMacDA_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1, 1, 2),
    _S3EnetSdTrafMacDA_Type()
)
s3EnetSdTrafMacDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetSdTrafMacDA.setStatus("deprecated")
_S3EnetSdTrafFrames_Type = Counter32
_S3EnetSdTrafFrames_Object = MibTableColumn
s3EnetSdTrafFrames = _S3EnetSdTrafFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1, 1, 3),
    _S3EnetSdTrafFrames_Type()
)
s3EnetSdTrafFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetSdTrafFrames.setStatus("deprecated")
_S3EnetSdTrafBytes_Type = Counter32
_S3EnetSdTrafBytes_Object = MibTableColumn
s3EnetSdTrafBytes = _S3EnetSdTrafBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 1, 1, 4),
    _S3EnetSdTrafBytes_Type()
)
s3EnetSdTrafBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetSdTrafBytes.setStatus("deprecated")
_S3EnetDsTrafTable_Object = MibTable
s3EnetDsTrafTable = _S3EnetDsTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2)
)
if mibBuilder.loadTexts:
    s3EnetDsTrafTable.setStatus("deprecated")
_S3EnetDsTrafEntry_Object = MibTableRow
s3EnetDsTrafEntry = _S3EnetDsTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2, 1)
)
s3EnetDsTrafEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetDsTrafMacDA"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetDsTrafMacSA"),
)
if mibBuilder.loadTexts:
    s3EnetDsTrafEntry.setStatus("deprecated")


class _S3EnetDsTrafMacDA_Type(PhysAddress):
    """Custom type s3EnetDsTrafMacDA based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetDsTrafMacDA_Type.__name__ = "PhysAddress"
_S3EnetDsTrafMacDA_Object = MibTableColumn
s3EnetDsTrafMacDA = _S3EnetDsTrafMacDA_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2, 1, 1),
    _S3EnetDsTrafMacDA_Type()
)
s3EnetDsTrafMacDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetDsTrafMacDA.setStatus("deprecated")


class _S3EnetDsTrafMacSA_Type(PhysAddress):
    """Custom type s3EnetDsTrafMacSA based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetDsTrafMacSA_Type.__name__ = "PhysAddress"
_S3EnetDsTrafMacSA_Object = MibTableColumn
s3EnetDsTrafMacSA = _S3EnetDsTrafMacSA_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2, 1, 2),
    _S3EnetDsTrafMacSA_Type()
)
s3EnetDsTrafMacSA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetDsTrafMacSA.setStatus("deprecated")
_S3EnetDsTrafFrames_Type = Counter32
_S3EnetDsTrafFrames_Object = MibTableColumn
s3EnetDsTrafFrames = _S3EnetDsTrafFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2, 1, 3),
    _S3EnetDsTrafFrames_Type()
)
s3EnetDsTrafFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetDsTrafFrames.setStatus("deprecated")
_S3EnetDsTrafBytes_Type = Counter32
_S3EnetDsTrafBytes_Object = MibTableColumn
s3EnetDsTrafBytes = _S3EnetDsTrafBytes_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 2, 1, 4),
    _S3EnetDsTrafBytes_Type()
)
s3EnetDsTrafBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetDsTrafBytes.setStatus("deprecated")
_S3EnetPagedTrafTable_Object = MibTable
s3EnetPagedTrafTable = _S3EnetPagedTrafTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 3)
)
if mibBuilder.loadTexts:
    s3EnetPagedTrafTable.setStatus("deprecated")
_S3EnetPagedTrafEntry_Object = MibTableRow
s3EnetPagedTrafEntry = _S3EnetPagedTrafEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 3, 1)
)
s3EnetPagedTrafEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetTrafPageNo"),
)
if mibBuilder.loadTexts:
    s3EnetPagedTrafEntry.setStatus("deprecated")
_S3EnetTrafPageNo_Type = Integer32
_S3EnetTrafPageNo_Object = MibTableColumn
s3EnetTrafPageNo = _S3EnetTrafPageNo_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 3, 1, 1),
    _S3EnetTrafPageNo_Type()
)
s3EnetTrafPageNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTrafPageNo.setStatus("deprecated")


class _S3EnetTrafPageEntries_Type(OctetString):
    """Custom type s3EnetTrafPageEntries based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 400),
    )


_S3EnetTrafPageEntries_Type.__name__ = "OctetString"
_S3EnetTrafPageEntries_Object = MibTableColumn
s3EnetTrafPageEntries = _S3EnetTrafPageEntries_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 3, 1, 2),
    _S3EnetTrafPageEntries_Type()
)
s3EnetTrafPageEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetTrafPageEntries.setStatus("deprecated")
_S3EnetTrafAgeInterval_Type = TimeTicks
_S3EnetTrafAgeInterval_Object = MibScalar
s3EnetTrafAgeInterval = _S3EnetTrafAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 9, 4),
    _S3EnetTrafAgeInterval_Type()
)
s3EnetTrafAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s3EnetTrafAgeInterval.setStatus("deprecated")
_S3000EnetPlusStatistics_ObjectIdentity = ObjectIdentity
s3000EnetPlusStatistics = _S3000EnetPlusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10)
)
_S3EnetPlusPortTable_Object = MibTable
s3EnetPlusPortTable = _S3EnetPlusPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1)
)
if mibBuilder.loadTexts:
    s3EnetPlusPortTable.setStatus("mandatory")
_S3EnetPlusPortEntry_Object = MibTableRow
s3EnetPlusPortEntry = _S3EnetPlusPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1)
)
s3EnetPlusPortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetPlusPortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetPlusPortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetPlusPortEntry.setStatus("mandatory")
_S3EnetPlusPortBoardIndex_Type = Integer32
_S3EnetPlusPortBoardIndex_Object = MibTableColumn
s3EnetPlusPortBoardIndex = _S3EnetPlusPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 1),
    _S3EnetPlusPortBoardIndex_Type()
)
s3EnetPlusPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPlusPortBoardIndex.setStatus("mandatory")
_S3EnetPlusPortIndex_Type = Integer32
_S3EnetPlusPortIndex_Object = MibTableColumn
s3EnetPlusPortIndex = _S3EnetPlusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 2),
    _S3EnetPlusPortIndex_Type()
)
s3EnetPlusPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPlusPortIndex.setStatus("mandatory")
_S3EnetPortFragments_Type = Counter32
_S3EnetPortFragments_Object = MibTableColumn
s3EnetPortFragments = _S3EnetPortFragments_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 3),
    _S3EnetPortFragments_Type()
)
s3EnetPortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortFragments.setStatus("mandatory")
_S3EnetPortShortEvents_Type = Counter32
_S3EnetPortShortEvents_Object = MibTableColumn
s3EnetPortShortEvents = _S3EnetPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 4),
    _S3EnetPortShortEvents_Type()
)
s3EnetPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortShortEvents.setStatus("mandatory")
_S3EnetPortAutoPartitions_Type = Counter32
_S3EnetPortAutoPartitions_Object = MibTableColumn
s3EnetPortAutoPartitions = _S3EnetPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 5),
    _S3EnetPortAutoPartitions_Type()
)
s3EnetPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortAutoPartitions.setStatus("mandatory")
_S3EnetPortRateMismatches_Type = Counter32
_S3EnetPortRateMismatches_Object = MibTableColumn
s3EnetPortRateMismatches = _S3EnetPortRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 6),
    _S3EnetPortRateMismatches_Type()
)
s3EnetPortRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortRateMismatches.setStatus("mandatory")
_S3EnetPortJabbers_Type = Counter32
_S3EnetPortJabbers_Object = MibTableColumn
s3EnetPortJabbers = _S3EnetPortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 7),
    _S3EnetPortJabbers_Type()
)
s3EnetPortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortJabbers.setStatus("mandatory")


class _S3EnetPortLastSrcAddr_Type(PhysAddress):
    """Custom type s3EnetPortLastSrcAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetPortLastSrcAddr_Type.__name__ = "PhysAddress"
_S3EnetPortLastSrcAddr_Object = MibTableColumn
s3EnetPortLastSrcAddr = _S3EnetPortLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 8),
    _S3EnetPortLastSrcAddr_Type()
)
s3EnetPortLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortLastSrcAddr.setStatus("mandatory")
_S3EnetPortSrcAddrChanges_Type = Counter32
_S3EnetPortSrcAddrChanges_Object = MibTableColumn
s3EnetPortSrcAddrChanges = _S3EnetPortSrcAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 1, 1, 9),
    _S3EnetPortSrcAddrChanges_Type()
)
s3EnetPortSrcAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPortSrcAddrChanges.setStatus("mandatory")
_S3EnetPlusBoardTable_Object = MibTable
s3EnetPlusBoardTable = _S3EnetPlusBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2)
)
if mibBuilder.loadTexts:
    s3EnetPlusBoardTable.setStatus("mandatory")
_S3EnetPlusBoardEntry_Object = MibTableRow
s3EnetPlusBoardEntry = _S3EnetPlusBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1)
)
s3EnetPlusBoardEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetPlusBoardIndex"),
)
if mibBuilder.loadTexts:
    s3EnetPlusBoardEntry.setStatus("mandatory")
_S3EnetPlusBoardIndex_Type = Integer32
_S3EnetPlusBoardIndex_Object = MibTableColumn
s3EnetPlusBoardIndex = _S3EnetPlusBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 1),
    _S3EnetPlusBoardIndex_Type()
)
s3EnetPlusBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetPlusBoardIndex.setStatus("mandatory")
_S3EnetBoardFragments_Type = Counter32
_S3EnetBoardFragments_Object = MibTableColumn
s3EnetBoardFragments = _S3EnetBoardFragments_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 2),
    _S3EnetBoardFragments_Type()
)
s3EnetBoardFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardFragments.setStatus("mandatory")
_S3EnetBoardShortEvents_Type = Counter32
_S3EnetBoardShortEvents_Object = MibTableColumn
s3EnetBoardShortEvents = _S3EnetBoardShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 3),
    _S3EnetBoardShortEvents_Type()
)
s3EnetBoardShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardShortEvents.setStatus("mandatory")
_S3EnetBoardAutoPartitions_Type = Counter32
_S3EnetBoardAutoPartitions_Object = MibTableColumn
s3EnetBoardAutoPartitions = _S3EnetBoardAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 4),
    _S3EnetBoardAutoPartitions_Type()
)
s3EnetBoardAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardAutoPartitions.setStatus("mandatory")
_S3EnetBoardRateMismatches_Type = Counter32
_S3EnetBoardRateMismatches_Object = MibTableColumn
s3EnetBoardRateMismatches = _S3EnetBoardRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 5),
    _S3EnetBoardRateMismatches_Type()
)
s3EnetBoardRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardRateMismatches.setStatus("mandatory")
_S3EnetBoardJabbers_Type = Counter32
_S3EnetBoardJabbers_Object = MibTableColumn
s3EnetBoardJabbers = _S3EnetBoardJabbers_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 2, 1, 6),
    _S3EnetBoardJabbers_Type()
)
s3EnetBoardJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetBoardJabbers.setStatus("mandatory")
_S3000EnetPlusConc_ObjectIdentity = ObjectIdentity
s3000EnetPlusConc = _S3000EnetPlusConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3)
)
_S3EnetConcShortEvents_Type = Counter32
_S3EnetConcShortEvents_Object = MibScalar
s3EnetConcShortEvents = _S3EnetConcShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3, 1),
    _S3EnetConcShortEvents_Type()
)
s3EnetConcShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcShortEvents.setStatus("mandatory")
_S3EnetConcAutoPartitions_Type = Counter32
_S3EnetConcAutoPartitions_Object = MibScalar
s3EnetConcAutoPartitions = _S3EnetConcAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3, 2),
    _S3EnetConcAutoPartitions_Type()
)
s3EnetConcAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcAutoPartitions.setStatus("mandatory")
_S3EnetConcRateMismatches_Type = Counter32
_S3EnetConcRateMismatches_Object = MibScalar
s3EnetConcRateMismatches = _S3EnetConcRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3, 3),
    _S3EnetConcRateMismatches_Type()
)
s3EnetConcRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcRateMismatches.setStatus("mandatory")
_S3EnetConcJabbers_Type = Counter32
_S3EnetConcJabbers_Object = MibScalar
s3EnetConcJabbers = _S3EnetConcJabbers_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3, 4),
    _S3EnetConcJabbers_Type()
)
s3EnetConcJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcJabbers.setStatus("mandatory")
_S3EnetConcCollBackoffErrors_Type = Counter32
_S3EnetConcCollBackoffErrors_Object = MibScalar
s3EnetConcCollBackoffErrors = _S3EnetConcCollBackoffErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 10, 3, 5),
    _S3EnetConcCollBackoffErrors_Type()
)
s3EnetConcCollBackoffErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetConcCollBackoffErrors.setStatus("mandatory")
_S3000EnetFrameSizeDist_ObjectIdentity = ObjectIdentity
s3000EnetFrameSizeDist = _S3000EnetFrameSizeDist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11)
)
_S3EnetFrSizePortTable_Object = MibTable
s3EnetFrSizePortTable = _S3EnetFrSizePortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    s3EnetFrSizePortTable.setStatus("mandatory")
_S3EnetFrSizePortEntry_Object = MibTableRow
s3EnetFrSizePortEntry = _S3EnetFrSizePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1)
)
s3EnetFrSizePortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetFrSizePortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetFrSizePortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetFrSizePortEntry.setStatus("mandatory")
_S3EnetFrSizePortBoardIndex_Type = Integer32
_S3EnetFrSizePortBoardIndex_Object = MibTableColumn
s3EnetFrSizePortBoardIndex = _S3EnetFrSizePortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 1),
    _S3EnetFrSizePortBoardIndex_Type()
)
s3EnetFrSizePortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePortBoardIndex.setStatus("mandatory")
_S3EnetFrSizePortIndex_Type = Integer32
_S3EnetFrSizePortIndex_Object = MibTableColumn
s3EnetFrSizePortIndex = _S3EnetFrSizePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 2),
    _S3EnetFrSizePortIndex_Type()
)
s3EnetFrSizePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePortIndex.setStatus("mandatory")
_S3EnetFrSizePort64to127_Type = Counter32
_S3EnetFrSizePort64to127_Object = MibTableColumn
s3EnetFrSizePort64to127 = _S3EnetFrSizePort64to127_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 3),
    _S3EnetFrSizePort64to127_Type()
)
s3EnetFrSizePort64to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePort64to127.setStatus("mandatory")
_S3EnetFrSizePort128to255_Type = Counter32
_S3EnetFrSizePort128to255_Object = MibTableColumn
s3EnetFrSizePort128to255 = _S3EnetFrSizePort128to255_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 4),
    _S3EnetFrSizePort128to255_Type()
)
s3EnetFrSizePort128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePort128to255.setStatus("mandatory")
_S3EnetFrSizePort256to511_Type = Counter32
_S3EnetFrSizePort256to511_Object = MibTableColumn
s3EnetFrSizePort256to511 = _S3EnetFrSizePort256to511_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 5),
    _S3EnetFrSizePort256to511_Type()
)
s3EnetFrSizePort256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePort256to511.setStatus("mandatory")
_S3EnetFrSizePort512to1023_Type = Counter32
_S3EnetFrSizePort512to1023_Object = MibTableColumn
s3EnetFrSizePort512to1023 = _S3EnetFrSizePort512to1023_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 6),
    _S3EnetFrSizePort512to1023_Type()
)
s3EnetFrSizePort512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePort512to1023.setStatus("mandatory")
_S3EnetFrSizePort1024to1518_Type = Counter32
_S3EnetFrSizePort1024to1518_Object = MibTableColumn
s3EnetFrSizePort1024to1518 = _S3EnetFrSizePort1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 1, 1, 7),
    _S3EnetFrSizePort1024to1518_Type()
)
s3EnetFrSizePort1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizePort1024to1518.setStatus("mandatory")
_S3EnetFrSizeBoardTable_Object = MibTable
s3EnetFrSizeBoardTable = _S3EnetFrSizeBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2)
)
if mibBuilder.loadTexts:
    s3EnetFrSizeBoardTable.setStatus("mandatory")
_S3EnetFrSizeBoardEntry_Object = MibTableRow
s3EnetFrSizeBoardEntry = _S3EnetFrSizeBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1)
)
s3EnetFrSizeBoardEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetFrSizeBoardIndex"),
)
if mibBuilder.loadTexts:
    s3EnetFrSizeBoardEntry.setStatus("mandatory")
_S3EnetFrSizeBoardIndex_Type = Integer32
_S3EnetFrSizeBoardIndex_Object = MibTableColumn
s3EnetFrSizeBoardIndex = _S3EnetFrSizeBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 1),
    _S3EnetFrSizeBoardIndex_Type()
)
s3EnetFrSizeBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoardIndex.setStatus("mandatory")
_S3EnetFrSizeBoard64to127_Type = Counter32
_S3EnetFrSizeBoard64to127_Object = MibTableColumn
s3EnetFrSizeBoard64to127 = _S3EnetFrSizeBoard64to127_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 2),
    _S3EnetFrSizeBoard64to127_Type()
)
s3EnetFrSizeBoard64to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoard64to127.setStatus("mandatory")
_S3EnetFrSizeBoard128to255_Type = Counter32
_S3EnetFrSizeBoard128to255_Object = MibTableColumn
s3EnetFrSizeBoard128to255 = _S3EnetFrSizeBoard128to255_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 3),
    _S3EnetFrSizeBoard128to255_Type()
)
s3EnetFrSizeBoard128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoard128to255.setStatus("mandatory")
_S3EnetFrSizeBoard256to511_Type = Counter32
_S3EnetFrSizeBoard256to511_Object = MibTableColumn
s3EnetFrSizeBoard256to511 = _S3EnetFrSizeBoard256to511_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 4),
    _S3EnetFrSizeBoard256to511_Type()
)
s3EnetFrSizeBoard256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoard256to511.setStatus("mandatory")
_S3EnetFrSizeBoard512to1023_Type = Counter32
_S3EnetFrSizeBoard512to1023_Object = MibTableColumn
s3EnetFrSizeBoard512to1023 = _S3EnetFrSizeBoard512to1023_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 5),
    _S3EnetFrSizeBoard512to1023_Type()
)
s3EnetFrSizeBoard512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoard512to1023.setStatus("mandatory")
_S3EnetFrSizeBoard1024to1518_Type = Counter32
_S3EnetFrSizeBoard1024to1518_Object = MibTableColumn
s3EnetFrSizeBoard1024to1518 = _S3EnetFrSizeBoard1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 2, 1, 6),
    _S3EnetFrSizeBoard1024to1518_Type()
)
s3EnetFrSizeBoard1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeBoard1024to1518.setStatus("mandatory")
_S3000EnetFrameConc_ObjectIdentity = ObjectIdentity
s3000EnetFrameConc = _S3000EnetFrameConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3)
)
_S3EnetFrSizeConc64to127_Type = Counter32
_S3EnetFrSizeConc64to127_Object = MibScalar
s3EnetFrSizeConc64to127 = _S3EnetFrSizeConc64to127_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3, 1),
    _S3EnetFrSizeConc64to127_Type()
)
s3EnetFrSizeConc64to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeConc64to127.setStatus("mandatory")
_S3EnetFrSizeConc128to255_Type = Counter32
_S3EnetFrSizeConc128to255_Object = MibScalar
s3EnetFrSizeConc128to255 = _S3EnetFrSizeConc128to255_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3, 2),
    _S3EnetFrSizeConc128to255_Type()
)
s3EnetFrSizeConc128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeConc128to255.setStatus("mandatory")
_S3EnetFrSizeConc256to511_Type = Counter32
_S3EnetFrSizeConc256to511_Object = MibScalar
s3EnetFrSizeConc256to511 = _S3EnetFrSizeConc256to511_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3, 3),
    _S3EnetFrSizeConc256to511_Type()
)
s3EnetFrSizeConc256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeConc256to511.setStatus("mandatory")
_S3EnetFrSizeConc512to1023_Type = Counter32
_S3EnetFrSizeConc512to1023_Object = MibScalar
s3EnetFrSizeConc512to1023 = _S3EnetFrSizeConc512to1023_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3, 4),
    _S3EnetFrSizeConc512to1023_Type()
)
s3EnetFrSizeConc512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeConc512to1023.setStatus("mandatory")
_S3EnetFrSizeConc1024to1518_Type = Counter32
_S3EnetFrSizeConc1024to1518_Object = MibScalar
s3EnetFrSizeConc1024to1518 = _S3EnetFrSizeConc1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 11, 3, 5),
    _S3EnetFrSizeConc1024to1518_Type()
)
s3EnetFrSizeConc1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetFrSizeConc1024to1518.setStatus("mandatory")
_S3000EnetProtoTypeDist_ObjectIdentity = ObjectIdentity
s3000EnetProtoTypeDist = _S3000EnetProtoTypeDist_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12)
)
_S3EnetProtoPortTable_Object = MibTable
s3EnetProtoPortTable = _S3EnetProtoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    s3EnetProtoPortTable.setStatus("mandatory")
_S3EnetProtoPortEntry_Object = MibTableRow
s3EnetProtoPortEntry = _S3EnetProtoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1)
)
s3EnetProtoPortEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetProtoPortBoardIndex"),
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetProtoPortIndex"),
)
if mibBuilder.loadTexts:
    s3EnetProtoPortEntry.setStatus("mandatory")
_S3EnetProtoPortBoardIndex_Type = Integer32
_S3EnetProtoPortBoardIndex_Object = MibTableColumn
s3EnetProtoPortBoardIndex = _S3EnetProtoPortBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 1),
    _S3EnetProtoPortBoardIndex_Type()
)
s3EnetProtoPortBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortBoardIndex.setStatus("mandatory")
_S3EnetProtoPortIndex_Type = Integer32
_S3EnetProtoPortIndex_Object = MibTableColumn
s3EnetProtoPortIndex = _S3EnetProtoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 2),
    _S3EnetProtoPortIndex_Type()
)
s3EnetProtoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortIndex.setStatus("mandatory")
_S3EnetProtoPort8023Frames_Type = Counter32
_S3EnetProtoPort8023Frames_Object = MibTableColumn
s3EnetProtoPort8023Frames = _S3EnetProtoPort8023Frames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 3),
    _S3EnetProtoPort8023Frames_Type()
)
s3EnetProtoPort8023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPort8023Frames.setStatus("mandatory")
_S3EnetProtoPortEthernetFrames_Type = Counter32
_S3EnetProtoPortEthernetFrames_Object = MibTableColumn
s3EnetProtoPortEthernetFrames = _S3EnetProtoPortEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 4),
    _S3EnetProtoPortEthernetFrames_Type()
)
s3EnetProtoPortEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortEthernetFrames.setStatus("mandatory")
_S3EnetProtoPortOtherFrames_Type = Counter32
_S3EnetProtoPortOtherFrames_Object = MibTableColumn
s3EnetProtoPortOtherFrames = _S3EnetProtoPortOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 5),
    _S3EnetProtoPortOtherFrames_Type()
)
s3EnetProtoPortOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortOtherFrames.setStatus("mandatory")
_S3EnetProtoPortSnaFrames_Type = Counter32
_S3EnetProtoPortSnaFrames_Object = MibTableColumn
s3EnetProtoPortSnaFrames = _S3EnetProtoPortSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 6),
    _S3EnetProtoPortSnaFrames_Type()
)
s3EnetProtoPortSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortSnaFrames.setStatus("mandatory")
_S3EnetProtoPortIpFrames_Type = Counter32
_S3EnetProtoPortIpFrames_Object = MibTableColumn
s3EnetProtoPortIpFrames = _S3EnetProtoPortIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 7),
    _S3EnetProtoPortIpFrames_Type()
)
s3EnetProtoPortIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortIpFrames.setStatus("mandatory")
_S3EnetProtoPortIsoFrames_Type = Counter32
_S3EnetProtoPortIsoFrames_Object = MibTableColumn
s3EnetProtoPortIsoFrames = _S3EnetProtoPortIsoFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 8),
    _S3EnetProtoPortIsoFrames_Type()
)
s3EnetProtoPortIsoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortIsoFrames.setStatus("mandatory")
_S3EnetProtoPortArpFrames_Type = Counter32
_S3EnetProtoPortArpFrames_Object = MibTableColumn
s3EnetProtoPortArpFrames = _S3EnetProtoPortArpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 9),
    _S3EnetProtoPortArpFrames_Type()
)
s3EnetProtoPortArpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortArpFrames.setStatus("mandatory")
_S3EnetProtoPortDecIVFrames_Type = Counter32
_S3EnetProtoPortDecIVFrames_Object = MibTableColumn
s3EnetProtoPortDecIVFrames = _S3EnetProtoPortDecIVFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 10),
    _S3EnetProtoPortDecIVFrames_Type()
)
s3EnetProtoPortDecIVFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortDecIVFrames.setStatus("mandatory")
_S3EnetProtoPortDecLatFrames_Type = Counter32
_S3EnetProtoPortDecLatFrames_Object = MibTableColumn
s3EnetProtoPortDecLatFrames = _S3EnetProtoPortDecLatFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 11),
    _S3EnetProtoPortDecLatFrames_Type()
)
s3EnetProtoPortDecLatFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortDecLatFrames.setStatus("mandatory")
_S3EnetProtoPortEthTalkFrames_Type = Counter32
_S3EnetProtoPortEthTalkFrames_Object = MibTableColumn
s3EnetProtoPortEthTalkFrames = _S3EnetProtoPortEthTalkFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 12),
    _S3EnetProtoPortEthTalkFrames_Type()
)
s3EnetProtoPortEthTalkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortEthTalkFrames.setStatus("mandatory")
_S3EnetProtoPortXnsFrames_Type = Counter32
_S3EnetProtoPortXnsFrames_Object = MibTableColumn
s3EnetProtoPortXnsFrames = _S3EnetProtoPortXnsFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 13),
    _S3EnetProtoPortXnsFrames_Type()
)
s3EnetProtoPortXnsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortXnsFrames.setStatus("mandatory")
_S3EnetProtoPortIpxFrames_Type = Counter32
_S3EnetProtoPortIpxFrames_Object = MibTableColumn
s3EnetProtoPortIpxFrames = _S3EnetProtoPortIpxFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 14),
    _S3EnetProtoPortIpxFrames_Type()
)
s3EnetProtoPortIpxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortIpxFrames.setStatus("mandatory")
_S3EnetProtoPortDecLavcFrames_Type = Counter32
_S3EnetProtoPortDecLavcFrames_Object = MibTableColumn
s3EnetProtoPortDecLavcFrames = _S3EnetProtoPortDecLavcFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 15),
    _S3EnetProtoPortDecLavcFrames_Type()
)
s3EnetProtoPortDecLavcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortDecLavcFrames.setStatus("mandatory")
_S3EnetProtoPortNetBiosFrames_Type = Counter32
_S3EnetProtoPortNetBiosFrames_Object = MibTableColumn
s3EnetProtoPortNetBiosFrames = _S3EnetProtoPortNetBiosFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 16),
    _S3EnetProtoPortNetBiosFrames_Type()
)
s3EnetProtoPortNetBiosFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortNetBiosFrames.setStatus("mandatory")
_S3EnetProtoPortBrdgSpanTreeFrames_Type = Counter32
_S3EnetProtoPortBrdgSpanTreeFrames_Object = MibTableColumn
s3EnetProtoPortBrdgSpanTreeFrames = _S3EnetProtoPortBrdgSpanTreeFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 1, 1, 17),
    _S3EnetProtoPortBrdgSpanTreeFrames_Type()
)
s3EnetProtoPortBrdgSpanTreeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoPortBrdgSpanTreeFrames.setStatus("mandatory")
_S3EnetProtoBoardTable_Object = MibTable
s3EnetProtoBoardTable = _S3EnetProtoBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2)
)
if mibBuilder.loadTexts:
    s3EnetProtoBoardTable.setStatus("mandatory")
_S3EnetProtoBoardEntry_Object = MibTableRow
s3EnetProtoBoardEntry = _S3EnetProtoBoardEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1)
)
s3EnetProtoBoardEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetProtoBoardIndex"),
)
if mibBuilder.loadTexts:
    s3EnetProtoBoardEntry.setStatus("mandatory")
_S3EnetProtoBoardIndex_Type = Integer32
_S3EnetProtoBoardIndex_Object = MibTableColumn
s3EnetProtoBoardIndex = _S3EnetProtoBoardIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 1),
    _S3EnetProtoBoardIndex_Type()
)
s3EnetProtoBoardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardIndex.setStatus("mandatory")
_S3EnetProtoBoard8023Frames_Type = Counter32
_S3EnetProtoBoard8023Frames_Object = MibTableColumn
s3EnetProtoBoard8023Frames = _S3EnetProtoBoard8023Frames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 2),
    _S3EnetProtoBoard8023Frames_Type()
)
s3EnetProtoBoard8023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoard8023Frames.setStatus("mandatory")
_S3EnetProtoBoardEthernetFrames_Type = Counter32
_S3EnetProtoBoardEthernetFrames_Object = MibTableColumn
s3EnetProtoBoardEthernetFrames = _S3EnetProtoBoardEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 3),
    _S3EnetProtoBoardEthernetFrames_Type()
)
s3EnetProtoBoardEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardEthernetFrames.setStatus("mandatory")
_S3EnetProtoBoardOtherFrames_Type = Counter32
_S3EnetProtoBoardOtherFrames_Object = MibTableColumn
s3EnetProtoBoardOtherFrames = _S3EnetProtoBoardOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 4),
    _S3EnetProtoBoardOtherFrames_Type()
)
s3EnetProtoBoardOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardOtherFrames.setStatus("mandatory")
_S3EnetProtoBoardSnaFrames_Type = Counter32
_S3EnetProtoBoardSnaFrames_Object = MibTableColumn
s3EnetProtoBoardSnaFrames = _S3EnetProtoBoardSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 5),
    _S3EnetProtoBoardSnaFrames_Type()
)
s3EnetProtoBoardSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardSnaFrames.setStatus("mandatory")
_S3EnetProtoBoardIpFrames_Type = Counter32
_S3EnetProtoBoardIpFrames_Object = MibTableColumn
s3EnetProtoBoardIpFrames = _S3EnetProtoBoardIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 6),
    _S3EnetProtoBoardIpFrames_Type()
)
s3EnetProtoBoardIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardIpFrames.setStatus("mandatory")
_S3EnetProtoBoardIsoFrames_Type = Counter32
_S3EnetProtoBoardIsoFrames_Object = MibTableColumn
s3EnetProtoBoardIsoFrames = _S3EnetProtoBoardIsoFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 7),
    _S3EnetProtoBoardIsoFrames_Type()
)
s3EnetProtoBoardIsoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardIsoFrames.setStatus("mandatory")
_S3EnetProtoBoardArpFrames_Type = Counter32
_S3EnetProtoBoardArpFrames_Object = MibTableColumn
s3EnetProtoBoardArpFrames = _S3EnetProtoBoardArpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 8),
    _S3EnetProtoBoardArpFrames_Type()
)
s3EnetProtoBoardArpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardArpFrames.setStatus("mandatory")
_S3EnetProtoBoardDecIVFrames_Type = Counter32
_S3EnetProtoBoardDecIVFrames_Object = MibTableColumn
s3EnetProtoBoardDecIVFrames = _S3EnetProtoBoardDecIVFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 9),
    _S3EnetProtoBoardDecIVFrames_Type()
)
s3EnetProtoBoardDecIVFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardDecIVFrames.setStatus("mandatory")
_S3EnetProtoBoardDecLatFrames_Type = Counter32
_S3EnetProtoBoardDecLatFrames_Object = MibTableColumn
s3EnetProtoBoardDecLatFrames = _S3EnetProtoBoardDecLatFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 10),
    _S3EnetProtoBoardDecLatFrames_Type()
)
s3EnetProtoBoardDecLatFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardDecLatFrames.setStatus("mandatory")
_S3EnetProtoBoardEthTalkFrames_Type = Counter32
_S3EnetProtoBoardEthTalkFrames_Object = MibTableColumn
s3EnetProtoBoardEthTalkFrames = _S3EnetProtoBoardEthTalkFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 11),
    _S3EnetProtoBoardEthTalkFrames_Type()
)
s3EnetProtoBoardEthTalkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardEthTalkFrames.setStatus("mandatory")
_S3EnetProtoBoardXnsFrames_Type = Counter32
_S3EnetProtoBoardXnsFrames_Object = MibTableColumn
s3EnetProtoBoardXnsFrames = _S3EnetProtoBoardXnsFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 12),
    _S3EnetProtoBoardXnsFrames_Type()
)
s3EnetProtoBoardXnsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardXnsFrames.setStatus("mandatory")
_S3EnetProtoBoardIpxFrames_Type = Counter32
_S3EnetProtoBoardIpxFrames_Object = MibTableColumn
s3EnetProtoBoardIpxFrames = _S3EnetProtoBoardIpxFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 13),
    _S3EnetProtoBoardIpxFrames_Type()
)
s3EnetProtoBoardIpxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardIpxFrames.setStatus("mandatory")
_S3EnetProtoBoardDecLavcFrames_Type = Counter32
_S3EnetProtoBoardDecLavcFrames_Object = MibTableColumn
s3EnetProtoBoardDecLavcFrames = _S3EnetProtoBoardDecLavcFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 14),
    _S3EnetProtoBoardDecLavcFrames_Type()
)
s3EnetProtoBoardDecLavcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardDecLavcFrames.setStatus("mandatory")
_S3EnetProtoBoardNetBiosFrames_Type = Counter32
_S3EnetProtoBoardNetBiosFrames_Object = MibTableColumn
s3EnetProtoBoardNetBiosFrames = _S3EnetProtoBoardNetBiosFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 15),
    _S3EnetProtoBoardNetBiosFrames_Type()
)
s3EnetProtoBoardNetBiosFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardNetBiosFrames.setStatus("mandatory")
_S3EnetProtoBoardBrdgSpanTreeFrames_Type = Counter32
_S3EnetProtoBoardBrdgSpanTreeFrames_Object = MibTableColumn
s3EnetProtoBoardBrdgSpanTreeFrames = _S3EnetProtoBoardBrdgSpanTreeFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 2, 1, 16),
    _S3EnetProtoBoardBrdgSpanTreeFrames_Type()
)
s3EnetProtoBoardBrdgSpanTreeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoBoardBrdgSpanTreeFrames.setStatus("mandatory")
_S3000EnetProtoConc_ObjectIdentity = ObjectIdentity
s3000EnetProtoConc = _S3000EnetProtoConc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3)
)
_S3EnetProtoConc8023Frames_Type = Counter32
_S3EnetProtoConc8023Frames_Object = MibScalar
s3EnetProtoConc8023Frames = _S3EnetProtoConc8023Frames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 1),
    _S3EnetProtoConc8023Frames_Type()
)
s3EnetProtoConc8023Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConc8023Frames.setStatus("mandatory")
_S3EnetProtoConcEthernetFrames_Type = Counter32
_S3EnetProtoConcEthernetFrames_Object = MibScalar
s3EnetProtoConcEthernetFrames = _S3EnetProtoConcEthernetFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 2),
    _S3EnetProtoConcEthernetFrames_Type()
)
s3EnetProtoConcEthernetFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcEthernetFrames.setStatus("mandatory")
_S3EnetProtoConcOtherFrames_Type = Counter32
_S3EnetProtoConcOtherFrames_Object = MibScalar
s3EnetProtoConcOtherFrames = _S3EnetProtoConcOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 3),
    _S3EnetProtoConcOtherFrames_Type()
)
s3EnetProtoConcOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcOtherFrames.setStatus("mandatory")
_S3EnetProtoConcSnaFrames_Type = Counter32
_S3EnetProtoConcSnaFrames_Object = MibScalar
s3EnetProtoConcSnaFrames = _S3EnetProtoConcSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 4),
    _S3EnetProtoConcSnaFrames_Type()
)
s3EnetProtoConcSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcSnaFrames.setStatus("mandatory")
_S3EnetProtoConcIpFrames_Type = Counter32
_S3EnetProtoConcIpFrames_Object = MibScalar
s3EnetProtoConcIpFrames = _S3EnetProtoConcIpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 5),
    _S3EnetProtoConcIpFrames_Type()
)
s3EnetProtoConcIpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcIpFrames.setStatus("mandatory")
_S3EnetProtoConcIsoFrames_Type = Counter32
_S3EnetProtoConcIsoFrames_Object = MibScalar
s3EnetProtoConcIsoFrames = _S3EnetProtoConcIsoFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 6),
    _S3EnetProtoConcIsoFrames_Type()
)
s3EnetProtoConcIsoFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcIsoFrames.setStatus("mandatory")
_S3EnetProtoConcArpFrames_Type = Counter32
_S3EnetProtoConcArpFrames_Object = MibScalar
s3EnetProtoConcArpFrames = _S3EnetProtoConcArpFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 7),
    _S3EnetProtoConcArpFrames_Type()
)
s3EnetProtoConcArpFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcArpFrames.setStatus("mandatory")
_S3EnetProtoConcDecIVFrames_Type = Counter32
_S3EnetProtoConcDecIVFrames_Object = MibScalar
s3EnetProtoConcDecIVFrames = _S3EnetProtoConcDecIVFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 8),
    _S3EnetProtoConcDecIVFrames_Type()
)
s3EnetProtoConcDecIVFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcDecIVFrames.setStatus("mandatory")
_S3EnetProtoConcDecLatFrames_Type = Counter32
_S3EnetProtoConcDecLatFrames_Object = MibScalar
s3EnetProtoConcDecLatFrames = _S3EnetProtoConcDecLatFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 9),
    _S3EnetProtoConcDecLatFrames_Type()
)
s3EnetProtoConcDecLatFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcDecLatFrames.setStatus("mandatory")
_S3EnetProtoConcEthTalkFrames_Type = Counter32
_S3EnetProtoConcEthTalkFrames_Object = MibScalar
s3EnetProtoConcEthTalkFrames = _S3EnetProtoConcEthTalkFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 10),
    _S3EnetProtoConcEthTalkFrames_Type()
)
s3EnetProtoConcEthTalkFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcEthTalkFrames.setStatus("mandatory")
_S3EnetProtoConcXnsFrames_Type = Counter32
_S3EnetProtoConcXnsFrames_Object = MibScalar
s3EnetProtoConcXnsFrames = _S3EnetProtoConcXnsFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 11),
    _S3EnetProtoConcXnsFrames_Type()
)
s3EnetProtoConcXnsFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcXnsFrames.setStatus("mandatory")
_S3EnetProtoConcIpxFrames_Type = Counter32
_S3EnetProtoConcIpxFrames_Object = MibScalar
s3EnetProtoConcIpxFrames = _S3EnetProtoConcIpxFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 12),
    _S3EnetProtoConcIpxFrames_Type()
)
s3EnetProtoConcIpxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcIpxFrames.setStatus("mandatory")
_S3EnetProtoConcDecLavcFrames_Type = Counter32
_S3EnetProtoConcDecLavcFrames_Object = MibScalar
s3EnetProtoConcDecLavcFrames = _S3EnetProtoConcDecLavcFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 13),
    _S3EnetProtoConcDecLavcFrames_Type()
)
s3EnetProtoConcDecLavcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcDecLavcFrames.setStatus("mandatory")
_S3EnetProtoConcNetBiosFrames_Type = Counter32
_S3EnetProtoConcNetBiosFrames_Object = MibScalar
s3EnetProtoConcNetBiosFrames = _S3EnetProtoConcNetBiosFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 14),
    _S3EnetProtoConcNetBiosFrames_Type()
)
s3EnetProtoConcNetBiosFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcNetBiosFrames.setStatus("mandatory")
_S3EnetProtoConcBrdgSpanTreeFrames_Type = Counter32
_S3EnetProtoConcBrdgSpanTreeFrames_Object = MibScalar
s3EnetProtoConcBrdgSpanTreeFrames = _S3EnetProtoConcBrdgSpanTreeFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 12, 3, 15),
    _S3EnetProtoConcBrdgSpanTreeFrames_Type()
)
s3EnetProtoConcBrdgSpanTreeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetProtoConcBrdgSpanTreeFrames.setStatus("mandatory")
_S3000EnetHosts_ObjectIdentity = ObjectIdentity
s3000EnetHosts = _S3000EnetHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13)
)


class _S3EnetHostTableSize_Type(Integer32):
    """Custom type s3EnetHostTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_S3EnetHostTableSize_Type.__name__ = "Integer32"
_S3EnetHostTableSize_Object = MibScalar
s3EnetHostTableSize = _S3EnetHostTableSize_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 1),
    _S3EnetHostTableSize_Type()
)
s3EnetHostTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostTableSize.setStatus("mandatory")
_S3EnetHostLastDeleteTime_Type = TimeTicks
_S3EnetHostLastDeleteTime_Object = MibScalar
s3EnetHostLastDeleteTime = _S3EnetHostLastDeleteTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 2),
    _S3EnetHostLastDeleteTime_Type()
)
s3EnetHostLastDeleteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostLastDeleteTime.setStatus("mandatory")
_S3EnetHostTable_Object = MibTable
s3EnetHostTable = _S3EnetHostTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3)
)
if mibBuilder.loadTexts:
    s3EnetHostTable.setStatus("mandatory")
_S3EnetHostEntry_Object = MibTableRow
s3EnetHostEntry = _S3EnetHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1)
)
s3EnetHostEntry.setIndexNames(
    (0, "SYNOPTICS-ETHERNET-MIB", "s3EnetHostIndex"),
)
if mibBuilder.loadTexts:
    s3EnetHostEntry.setStatus("mandatory")


class _S3EnetHostIndex_Type(Integer32):
    """Custom type s3EnetHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S3EnetHostIndex_Type.__name__ = "Integer32"
_S3EnetHostIndex_Object = MibTableColumn
s3EnetHostIndex = _S3EnetHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 1),
    _S3EnetHostIndex_Type()
)
s3EnetHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostIndex.setStatus("mandatory")


class _S3EnetHostObserveOrder_Type(Integer32):
    """Custom type s3EnetHostObserveOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_S3EnetHostObserveOrder_Type.__name__ = "Integer32"
_S3EnetHostObserveOrder_Object = MibTableColumn
s3EnetHostObserveOrder = _S3EnetHostObserveOrder_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 2),
    _S3EnetHostObserveOrder_Type()
)
s3EnetHostObserveOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostObserveOrder.setStatus("mandatory")
_S3EnetHostNetAddr_Type = OctetString
_S3EnetHostNetAddr_Object = MibTableColumn
s3EnetHostNetAddr = _S3EnetHostNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 3),
    _S3EnetHostNetAddr_Type()
)
s3EnetHostNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostNetAddr.setStatus("mandatory")


class _S3EnetHostAddrType_Type(Integer32):
    """Custom type s3EnetHostAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("other", 1))
    )


_S3EnetHostAddrType_Type.__name__ = "Integer32"
_S3EnetHostAddrType_Object = MibTableColumn
s3EnetHostAddrType = _S3EnetHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 4),
    _S3EnetHostAddrType_Type()
)
s3EnetHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostAddrType.setStatus("mandatory")


class _S3EnetHostMacAddress_Type(PhysAddress):
    """Custom type s3EnetHostMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_S3EnetHostMacAddress_Type.__name__ = "PhysAddress"
_S3EnetHostMacAddress_Object = MibTableColumn
s3EnetHostMacAddress = _S3EnetHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 5),
    _S3EnetHostMacAddress_Type()
)
s3EnetHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostMacAddress.setStatus("mandatory")
_S3EnetHostSlotIndex_Type = Integer32
_S3EnetHostSlotIndex_Object = MibTableColumn
s3EnetHostSlotIndex = _S3EnetHostSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 6),
    _S3EnetHostSlotIndex_Type()
)
s3EnetHostSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostSlotIndex.setStatus("mandatory")
_S3EnetHostPortIndex_Type = Integer32
_S3EnetHostPortIndex_Object = MibTableColumn
s3EnetHostPortIndex = _S3EnetHostPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 7),
    _S3EnetHostPortIndex_Type()
)
s3EnetHostPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostPortIndex.setStatus("mandatory")


class _S3EnetHostLearnMethod_Type(Integer32):
    """Custom type s3EnetHostLearnMethod based on Integer32"""
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
        *(("arpRequest", 2),
          ("arpResponse", 3),
          ("other", 1),
          ("ripRequest", 4),
          ("ripResponse", 5))
    )


_S3EnetHostLearnMethod_Type.__name__ = "Integer32"
_S3EnetHostLearnMethod_Object = MibTableColumn
s3EnetHostLearnMethod = _S3EnetHostLearnMethod_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 8),
    _S3EnetHostLearnMethod_Type()
)
s3EnetHostLearnMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostLearnMethod.setStatus("mandatory")
_S3EnetHostTimeStamp_Type = TimeTicks
_S3EnetHostTimeStamp_Object = MibTableColumn
s3EnetHostTimeStamp = _S3EnetHostTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 3, 2, 13, 3, 1, 9),
    _S3EnetHostTimeStamp_Type()
)
s3EnetHostTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s3EnetHostTimeStamp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYNOPTICS-ETHERNET-MIB",
    **{"s3000EnetConcentrator": s3000EnetConcentrator,
       "s3EnetConcRetimingStatus": s3EnetConcRetimingStatus,
       "s3EnetConcFrmsRxOk": s3EnetConcFrmsRxOk,
       "s3EnetConcOctetsRxOk": s3EnetConcOctetsRxOk,
       "s3EnetConcMcastFrmsRxOk": s3EnetConcMcastFrmsRxOk,
       "s3EnetConcBcastFrmsRxOk": s3EnetConcBcastFrmsRxOk,
       "s3EnetConcColls": s3EnetConcColls,
       "s3EnetConcTooLongErrors": s3EnetConcTooLongErrors,
       "s3EnetConcRuntErrors": s3EnetConcRuntErrors,
       "s3EnetConcFragErrors": s3EnetConcFragErrors,
       "s3EnetConcAlignErrors": s3EnetConcAlignErrors,
       "s3EnetConcFcsErrors": s3EnetConcFcsErrors,
       "s3EnetConcLateCollErrors": s3EnetConcLateCollErrors,
       "s3EnetConcSecureStatus": s3EnetConcSecureStatus,
       "s3EnetConcAuthAction": s3EnetConcAuthAction,
       "s3EnetConcSecurityLock": s3EnetConcSecurityLock,
       "s3EnetConcEnetChan": s3EnetConcEnetChan,
       "s3000EnetBoard": s3000EnetBoard,
       "s3EnetBoardTable": s3EnetBoardTable,
       "s3EnetBoardEntry": s3EnetBoardEntry,
       "s3EnetBoardIndex": s3EnetBoardIndex,
       "s3EnetBoardType": s3EnetBoardType,
       "s3EnetBoardHwVer": s3EnetBoardHwVer,
       "s3EnetBoardStatus": s3EnetBoardStatus,
       "s3EnetBoardReset": s3EnetBoardReset,
       "s3EnetBoardPartStatus": s3EnetBoardPartStatus,
       "s3EnetBoardNmCntlStatus": s3EnetBoardNmCntlStatus,
       "s3EnetBoardPsStatus": s3EnetBoardPsStatus,
       "s3EnetBoardFrmsRxOk": s3EnetBoardFrmsRxOk,
       "s3EnetBoardOctetsRxOk": s3EnetBoardOctetsRxOk,
       "s3EnetBoardMcastFrmsRxOk": s3EnetBoardMcastFrmsRxOk,
       "s3EnetBoardBcastFrmsRxOk": s3EnetBoardBcastFrmsRxOk,
       "s3EnetBoardColls": s3EnetBoardColls,
       "s3EnetBoardTooLongErrors": s3EnetBoardTooLongErrors,
       "s3EnetBoardRuntErrors": s3EnetBoardRuntErrors,
       "s3EnetBoardAlignErrors": s3EnetBoardAlignErrors,
       "s3EnetBoardFcsErrors": s3EnetBoardFcsErrors,
       "s3EnetBoardLateCollErrors": s3EnetBoardLateCollErrors,
       "s3EnetBoardAuthStatus": s3EnetBoardAuthStatus,
       "s3EnetBoardAuthAction": s3EnetBoardAuthAction,
       "s3EnetBoardUpStamp": s3EnetBoardUpStamp,
       "s3000EnetLocBridge": s3000EnetLocBridge,
       "s3EnetLocBridgeSlotTable": s3EnetLocBridgeSlotTable,
       "s3EnetLocBridgeEntry": s3EnetLocBridgeEntry,
       "s3EnetLocBridgeIndex": s3EnetLocBridgeIndex,
       "s3EnetLocBridgeDescr": s3EnetLocBridgeDescr,
       "s3EnetLocBridgePortCount": s3EnetLocBridgePortCount,
       "s3EnetLocBridgeDiagSts": s3EnetLocBridgeDiagSts,
       "s3EnetLocBridgeBootSts": s3EnetLocBridgeBootSts,
       "s3EnetLocBridgeStandbySts": s3EnetLocBridgeStandbySts,
       "s3EnetLocBridgePortTable": s3EnetLocBridgePortTable,
       "s3EnetLocBridgePortEntry": s3EnetLocBridgePortEntry,
       "s3EnetLocBridgePortSlotIndex": s3EnetLocBridgePortSlotIndex,
       "s3EnetLocBridgePortIndex": s3EnetLocBridgePortIndex,
       "s3EnetLocBridgePortMdaId": s3EnetLocBridgePortMdaId,
       "s3EnetLocBridgePortIf": s3EnetLocBridgePortIf,
       "s3EnetLocBridgePortDescr": s3EnetLocBridgePortDescr,
       "s3EnetLocBridgePortOpSts": s3EnetLocBridgePortOpSts,
       "s3000EnetRemBridge": s3000EnetRemBridge,
       "s3EnetRemBridgeSlotTable": s3EnetRemBridgeSlotTable,
       "s3EnetRemBridgeEntry": s3EnetRemBridgeEntry,
       "s3EnetRemBridgeIndex": s3EnetRemBridgeIndex,
       "s3EnetRemBridgeDescr": s3EnetRemBridgeDescr,
       "s3EnetRemBridgePortCount": s3EnetRemBridgePortCount,
       "s3EnetRemBridgeDiagSts": s3EnetRemBridgeDiagSts,
       "s3EnetRemBridgeBootSts": s3EnetRemBridgeBootSts,
       "s3EnetRemBridgeStandbySts": s3EnetRemBridgeStandbySts,
       "s3EnetRemBridgePortTable": s3EnetRemBridgePortTable,
       "s3EnetRemBridgePortEntry": s3EnetRemBridgePortEntry,
       "s3EnetRemBridgePortSlotIndex": s3EnetRemBridgePortSlotIndex,
       "s3EnetRemBridgePortIndex": s3EnetRemBridgePortIndex,
       "s3EnetRemBridgePortMdaId": s3EnetRemBridgePortMdaId,
       "s3EnetRemBridgePortDescr": s3EnetRemBridgePortDescr,
       "s3EnetRemBridgePortOpSts": s3EnetRemBridgePortOpSts,
       "s3EnetRemBridgePortRdySnd": s3EnetRemBridgePortRdySnd,
       "s3EnetRemBridgePortClrSnd": s3EnetRemBridgePortClrSnd,
       "s3EnetRemBridgePortCarDt": s3EnetRemBridgePortCarDt,
       "s3000EnetRouter": s3000EnetRouter,
       "s3EnetRouterSlotTable": s3EnetRouterSlotTable,
       "s3EnetRouterEntry": s3EnetRouterEntry,
       "s3EnetRouterIndex": s3EnetRouterIndex,
       "s3EnetRouterDescr": s3EnetRouterDescr,
       "s3EnetRouterDiagSts": s3EnetRouterDiagSts,
       "s3EnetRouterStandbySts": s3EnetRouterStandbySts,
       "s3EnetCommonBoardTable": s3EnetCommonBoardTable,
       "s3EnetCommonBoardEntry": s3EnetCommonBoardEntry,
       "s3EnetCommonBoardIndex": s3EnetCommonBoardIndex,
       "s3EnetCommonBoardEnetAB": s3EnetCommonBoardEnetAB,
       "s3EnetCommonBoardChanSwitch": s3EnetCommonBoardChanSwitch,
       "s3EnetCommonBoardRedund": s3EnetCommonBoardRedund,
       "s3000EnetPort": s3000EnetPort,
       "s3EnetPortTable": s3EnetPortTable,
       "s3EnetPortEntry": s3EnetPortEntry,
       "s3EnetPortBoardIndex": s3EnetPortBoardIndex,
       "s3EnetPortIndex": s3EnetPortIndex,
       "s3EnetPortLinkStatus": s3EnetPortLinkStatus,
       "s3EnetPortPartStatus": s3EnetPortPartStatus,
       "s3EnetPortJabberStatus": s3EnetPortJabberStatus,
       "s3EnetPortFrmsRxOk": s3EnetPortFrmsRxOk,
       "s3EnetPortOctetsRxOk": s3EnetPortOctetsRxOk,
       "s3EnetPortMcastFrmsRxOk": s3EnetPortMcastFrmsRxOk,
       "s3EnetPortBcastFrmsRxOk": s3EnetPortBcastFrmsRxOk,
       "s3EnetPortColls": s3EnetPortColls,
       "s3EnetPortTooLongErrors": s3EnetPortTooLongErrors,
       "s3EnetPortRuntErrors": s3EnetPortRuntErrors,
       "s3EnetPortAlignErrors": s3EnetPortAlignErrors,
       "s3EnetPortFcsErrors": s3EnetPortFcsErrors,
       "s3EnetPortLateCollErrors": s3EnetPortLateCollErrors,
       "s3EnetPortAuthStatus": s3EnetPortAuthStatus,
       "s3EnetPortAuthAction": s3EnetPortAuthAction,
       "s3EnetPortPartTime": s3EnetPortPartTime,
       "s3EnetPortType": s3EnetPortType,
       "s3EnetPortInterconStatus": s3EnetPortInterconStatus,
       "s3EnetPortAddrCollect": s3EnetPortAddrCollect,
       "s3EnetPortAddrLearnMode": s3EnetPortAddrLearnMode,
       "s3EnetPortTxSecurity": s3EnetPortTxSecurity,
       "s3EnetCommonPortTable": s3EnetCommonPortTable,
       "s3EnetCommonPortEntry": s3EnetCommonPortEntry,
       "s3EnetCommonPortBoardIndex": s3EnetCommonPortBoardIndex,
       "s3EnetCommonPortIndex": s3EnetCommonPortIndex,
       "s3EnetCommonPortLinkStatus": s3EnetCommonPortLinkStatus,
       "s3EnetCommonPortPartStatus": s3EnetCommonPortPartStatus,
       "s3EnetCommonPortType": s3EnetCommonPortType,
       "s3EnetCommonPortPartTime": s3EnetCommonPortPartTime,
       "s3EnetRedPortTable": s3EnetRedPortTable,
       "s3EnetRedPortEntry": s3EnetRedPortEntry,
       "s3EnetRedPortBoardIndex": s3EnetRedPortBoardIndex,
       "s3EnetRedPortIndex": s3EnetRedPortIndex,
       "s3EnetRedPortRedundMode": s3EnetRedPortRedundMode,
       "s3EnetRedPortOperStatus": s3EnetRedPortOperStatus,
       "s3EnetRedPortRemoteOperStatus": s3EnetRedPortRemoteOperStatus,
       "s3EnetRedPortCompanionSlotNo": s3EnetRedPortCompanionSlotNo,
       "s3EnetRedPortCompanionPortNo": s3EnetRedPortCompanionPortNo,
       "s3EnetRedPortSwitchoverStatus": s3EnetRedPortSwitchoverStatus,
       "s3EnetRedPortSwitchoverTime": s3EnetRedPortSwitchoverTime,
       "s3EnetRedPortCapability": s3EnetRedPortCapability,
       "s3EnetRedPortLastChg": s3EnetRedPortLastChg,
       "s3000EnetNmm": s3000EnetNmm,
       "s3EnetNmmType": s3EnetNmmType,
       "s3EnetNmmMdaHwVer": s3EnetNmmMdaHwVer,
       "s3EnetNmmFwVer": s3EnetNmmFwVer,
       "s3EnetNmmSwMajorVer": s3EnetNmmSwMajorVer,
       "s3EnetNmmSwMinorVer": s3EnetNmmSwMinorVer,
       "s3EnetNmmStatus": s3EnetNmmStatus,
       "s3EnetNmmMode": s3EnetNmmMode,
       "s3EnetNmmReset": s3EnetNmmReset,
       "s3EnetNmmRestart": s3EnetNmmRestart,
       "s3EnetNmmIpAddr": s3EnetNmmIpAddr,
       "s3EnetNmmNetMask": s3EnetNmmNetMask,
       "s3EnetNmmDefaultGateway": s3EnetNmmDefaultGateway,
       "s3EnetNmmFileServerAddr": s3EnetNmmFileServerAddr,
       "s3EnetNmmBootFile": s3EnetNmmBootFile,
       "s3EnetNmmBootMode": s3EnetNmmBootMode,
       "s3EnetNmmWriteEeprom": s3EnetNmmWriteEeprom,
       "s3EnetNmmBaudRate": s3EnetNmmBaudRate,
       "s3EnetNmmInitString": s3EnetNmmInitString,
       "s3EnetNmmLocation": s3EnetNmmLocation,
       "s3EnetNmmTrapServerTable": s3EnetNmmTrapServerTable,
       "s3EnetNmmTrapServerEntry": s3EnetNmmTrapServerEntry,
       "s3EnetNmmTrapType": s3EnetNmmTrapType,
       "s3EnetNmmTrapServerAddress": s3EnetNmmTrapServerAddress,
       "s3EnetNmmTrapServerComm": s3EnetNmmTrapServerComm,
       "s3EnetNmmAuthTrap": s3EnetNmmAuthTrap,
       "s3000EnetNode": s3000EnetNode,
       "s3EnetShowNodesTable": s3EnetShowNodesTable,
       "s3EnetShowNodesEntry": s3EnetShowNodesEntry,
       "s3EnetShowNodesSlotIndex": s3EnetShowNodesSlotIndex,
       "s3EnetShowNodesPortIndex": s3EnetShowNodesPortIndex,
       "s3EnetShowNodesMacAddress": s3EnetShowNodesMacAddress,
       "s3EnetShowNodesStatus": s3EnetShowNodesStatus,
       "s3EnetShowNodesVendorType": s3EnetShowNodesVendorType,
       "s3EnetShowNodesAuthStatus": s3EnetShowNodesAuthStatus,
       "s3EnetNodeAgeInterval": s3EnetNodeAgeInterval,
       "s3EnetFindNodesTable": s3EnetFindNodesTable,
       "s3EnetFindNodesEntry": s3EnetFindNodesEntry,
       "s3EnetFindNodesMacAddress": s3EnetFindNodesMacAddress,
       "s3EnetFindNodesSlotIndex": s3EnetFindNodesSlotIndex,
       "s3EnetFindNodesPortIndex": s3EnetFindNodesPortIndex,
       "s3EnetAuthNodesTable": s3EnetAuthNodesTable,
       "s3EnetAuthNodesEntry": s3EnetAuthNodesEntry,
       "s3EnetAuthNodesMacAddr": s3EnetAuthNodesMacAddr,
       "s3EnetAuthNodesSlotIndex": s3EnetAuthNodesSlotIndex,
       "s3EnetAuthNodesPortIndex": s3EnetAuthNodesPortIndex,
       "s3EnetAuthNodesStatus": s3EnetAuthNodesStatus,
       "s3EnetMaxNodesPerPort": s3EnetMaxNodesPerPort,
       "s3000EnetTopology": s3000EnetTopology,
       "s3000EnetNmmTopology": s3000EnetNmmTopology,
       "s3EnetTopNmmTable": s3EnetTopNmmTable,
       "s3EnetTopNmmEntry": s3EnetTopNmmEntry,
       "s3EnetTopNmmSlot": s3EnetTopNmmSlot,
       "s3EnetTopNmmPort": s3EnetTopNmmPort,
       "s3EnetTopNmmIpAddr": s3EnetTopNmmIpAddr,
       "s3EnetTopNmmMacAddr": s3EnetTopNmmMacAddr,
       "s3EnetTopNmmChassisType": s3EnetTopNmmChassisType,
       "s3EnetTopNmmBkplType": s3EnetTopNmmBkplType,
       "s3EnetTopNmmLocalSeg": s3EnetTopNmmLocalSeg,
       "s3EnetTopNmmNumSeen": s3EnetTopNmmNumSeen,
       "s3EnetTopNmmModuleType": s3EnetTopNmmModuleType,
       "s3EnetTopNmmNumLinks": s3EnetTopNmmNumLinks,
       "s3EnetTopNmmChgStatus": s3EnetTopNmmChgStatus,
       "s3EnetTopNmmHelloTime": s3EnetTopNmmHelloTime,
       "s3EnetTopNmmSubsetTable": s3EnetTopNmmSubsetTable,
       "s3EnetTopNmmSubsetEntry": s3EnetTopNmmSubsetEntry,
       "s3EnetTopNmmSubset": s3EnetTopNmmSubset,
       "s3000EnetBridTopology": s3000EnetBridTopology,
       "s3EnetTopBridgeTable": s3EnetTopBridgeTable,
       "s3EnetTopBridgeEntry": s3EnetTopBridgeEntry,
       "s3EnetTopBridgeIpAddr": s3EnetTopBridgeIpAddr,
       "s3EnetTopBridgeNumber": s3EnetTopBridgeNumber,
       "s3EnetTopBridgeMacAddr": s3EnetTopBridgeMacAddr,
       "s3EnetTopBridgeType": s3EnetTopBridgeType,
       "s3EnetTopBridgeStatus": s3EnetTopBridgeStatus,
       "s3EnetTopBridgeSlotNum": s3EnetTopBridgeSlotNum,
       "s3EnetTopBridgePortNum": s3EnetTopBridgePortNum,
       "s3EnetTopBridgeModuleType": s3EnetTopBridgeModuleType,
       "s3EnetTopBridgeHelloPortNum": s3EnetTopBridgeHelloPortNum,
       "s3EnetTopBridgeHelloPortType": s3EnetTopBridgeHelloPortType,
       "s3EnetTopBridgeHelloPortStatus": s3EnetTopBridgeHelloPortStatus,
       "s3EnetTopBridgeCompBridgeMac1": s3EnetTopBridgeCompBridgeMac1,
       "s3EnetTopBridgeCompBridgeMac2": s3EnetTopBridgeCompBridgeMac2,
       "s3EnetTopBdgSubsetTable": s3EnetTopBdgSubsetTable,
       "s3EnetTopBdgSubsetEntry": s3EnetTopBdgSubsetEntry,
       "s3EnetTopBdgSubset": s3EnetTopBdgSubset,
       "s3000EnetTopInfo": s3000EnetTopInfo,
       "s3EnetTopNmmLstChg": s3EnetTopNmmLstChg,
       "s3EnetTopBridgeLstChg": s3EnetTopBridgeLstChg,
       "s3000EnetThreshold": s3000EnetThreshold,
       "s3EnetThreshTable": s3EnetThreshTable,
       "s3EnetThreshEntry": s3EnetThreshEntry,
       "s3EnetThreshIndex": s3EnetThreshIndex,
       "s3EnetThreshStatus": s3EnetThreshStatus,
       "s3EnetThreshObject": s3EnetThreshObject,
       "s3EnetThreshSlot": s3EnetThreshSlot,
       "s3EnetThreshPort": s3EnetThreshPort,
       "s3EnetThreshType": s3EnetThreshType,
       "s3EnetThreshCondition": s3EnetThreshCondition,
       "s3EnetThreshSetValue": s3EnetThreshSetValue,
       "s3EnetThreshActualValue": s3EnetThreshActualValue,
       "s3EnetThreshAction": s3EnetThreshAction,
       "s3EnetThreshExceedCount": s3EnetThreshExceedCount,
       "s3EnetThreshDuration": s3EnetThreshDuration,
       "s3EnetThreshTableSize": s3EnetThreshTableSize,
       "s3000EnetSADATraffic": s3000EnetSADATraffic,
       "s3EnetSdTrafTable": s3EnetSdTrafTable,
       "s3EnetSdTrafEntry": s3EnetSdTrafEntry,
       "s3EnetSdTrafMacSA": s3EnetSdTrafMacSA,
       "s3EnetSdTrafMacDA": s3EnetSdTrafMacDA,
       "s3EnetSdTrafFrames": s3EnetSdTrafFrames,
       "s3EnetSdTrafBytes": s3EnetSdTrafBytes,
       "s3EnetDsTrafTable": s3EnetDsTrafTable,
       "s3EnetDsTrafEntry": s3EnetDsTrafEntry,
       "s3EnetDsTrafMacDA": s3EnetDsTrafMacDA,
       "s3EnetDsTrafMacSA": s3EnetDsTrafMacSA,
       "s3EnetDsTrafFrames": s3EnetDsTrafFrames,
       "s3EnetDsTrafBytes": s3EnetDsTrafBytes,
       "s3EnetPagedTrafTable": s3EnetPagedTrafTable,
       "s3EnetPagedTrafEntry": s3EnetPagedTrafEntry,
       "s3EnetTrafPageNo": s3EnetTrafPageNo,
       "s3EnetTrafPageEntries": s3EnetTrafPageEntries,
       "s3EnetTrafAgeInterval": s3EnetTrafAgeInterval,
       "s3000EnetPlusStatistics": s3000EnetPlusStatistics,
       "s3EnetPlusPortTable": s3EnetPlusPortTable,
       "s3EnetPlusPortEntry": s3EnetPlusPortEntry,
       "s3EnetPlusPortBoardIndex": s3EnetPlusPortBoardIndex,
       "s3EnetPlusPortIndex": s3EnetPlusPortIndex,
       "s3EnetPortFragments": s3EnetPortFragments,
       "s3EnetPortShortEvents": s3EnetPortShortEvents,
       "s3EnetPortAutoPartitions": s3EnetPortAutoPartitions,
       "s3EnetPortRateMismatches": s3EnetPortRateMismatches,
       "s3EnetPortJabbers": s3EnetPortJabbers,
       "s3EnetPortLastSrcAddr": s3EnetPortLastSrcAddr,
       "s3EnetPortSrcAddrChanges": s3EnetPortSrcAddrChanges,
       "s3EnetPlusBoardTable": s3EnetPlusBoardTable,
       "s3EnetPlusBoardEntry": s3EnetPlusBoardEntry,
       "s3EnetPlusBoardIndex": s3EnetPlusBoardIndex,
       "s3EnetBoardFragments": s3EnetBoardFragments,
       "s3EnetBoardShortEvents": s3EnetBoardShortEvents,
       "s3EnetBoardAutoPartitions": s3EnetBoardAutoPartitions,
       "s3EnetBoardRateMismatches": s3EnetBoardRateMismatches,
       "s3EnetBoardJabbers": s3EnetBoardJabbers,
       "s3000EnetPlusConc": s3000EnetPlusConc,
       "s3EnetConcShortEvents": s3EnetConcShortEvents,
       "s3EnetConcAutoPartitions": s3EnetConcAutoPartitions,
       "s3EnetConcRateMismatches": s3EnetConcRateMismatches,
       "s3EnetConcJabbers": s3EnetConcJabbers,
       "s3EnetConcCollBackoffErrors": s3EnetConcCollBackoffErrors,
       "s3000EnetFrameSizeDist": s3000EnetFrameSizeDist,
       "s3EnetFrSizePortTable": s3EnetFrSizePortTable,
       "s3EnetFrSizePortEntry": s3EnetFrSizePortEntry,
       "s3EnetFrSizePortBoardIndex": s3EnetFrSizePortBoardIndex,
       "s3EnetFrSizePortIndex": s3EnetFrSizePortIndex,
       "s3EnetFrSizePort64to127": s3EnetFrSizePort64to127,
       "s3EnetFrSizePort128to255": s3EnetFrSizePort128to255,
       "s3EnetFrSizePort256to511": s3EnetFrSizePort256to511,
       "s3EnetFrSizePort512to1023": s3EnetFrSizePort512to1023,
       "s3EnetFrSizePort1024to1518": s3EnetFrSizePort1024to1518,
       "s3EnetFrSizeBoardTable": s3EnetFrSizeBoardTable,
       "s3EnetFrSizeBoardEntry": s3EnetFrSizeBoardEntry,
       "s3EnetFrSizeBoardIndex": s3EnetFrSizeBoardIndex,
       "s3EnetFrSizeBoard64to127": s3EnetFrSizeBoard64to127,
       "s3EnetFrSizeBoard128to255": s3EnetFrSizeBoard128to255,
       "s3EnetFrSizeBoard256to511": s3EnetFrSizeBoard256to511,
       "s3EnetFrSizeBoard512to1023": s3EnetFrSizeBoard512to1023,
       "s3EnetFrSizeBoard1024to1518": s3EnetFrSizeBoard1024to1518,
       "s3000EnetFrameConc": s3000EnetFrameConc,
       "s3EnetFrSizeConc64to127": s3EnetFrSizeConc64to127,
       "s3EnetFrSizeConc128to255": s3EnetFrSizeConc128to255,
       "s3EnetFrSizeConc256to511": s3EnetFrSizeConc256to511,
       "s3EnetFrSizeConc512to1023": s3EnetFrSizeConc512to1023,
       "s3EnetFrSizeConc1024to1518": s3EnetFrSizeConc1024to1518,
       "s3000EnetProtoTypeDist": s3000EnetProtoTypeDist,
       "s3EnetProtoPortTable": s3EnetProtoPortTable,
       "s3EnetProtoPortEntry": s3EnetProtoPortEntry,
       "s3EnetProtoPortBoardIndex": s3EnetProtoPortBoardIndex,
       "s3EnetProtoPortIndex": s3EnetProtoPortIndex,
       "s3EnetProtoPort8023Frames": s3EnetProtoPort8023Frames,
       "s3EnetProtoPortEthernetFrames": s3EnetProtoPortEthernetFrames,
       "s3EnetProtoPortOtherFrames": s3EnetProtoPortOtherFrames,
       "s3EnetProtoPortSnaFrames": s3EnetProtoPortSnaFrames,
       "s3EnetProtoPortIpFrames": s3EnetProtoPortIpFrames,
       "s3EnetProtoPortIsoFrames": s3EnetProtoPortIsoFrames,
       "s3EnetProtoPortArpFrames": s3EnetProtoPortArpFrames,
       "s3EnetProtoPortDecIVFrames": s3EnetProtoPortDecIVFrames,
       "s3EnetProtoPortDecLatFrames": s3EnetProtoPortDecLatFrames,
       "s3EnetProtoPortEthTalkFrames": s3EnetProtoPortEthTalkFrames,
       "s3EnetProtoPortXnsFrames": s3EnetProtoPortXnsFrames,
       "s3EnetProtoPortIpxFrames": s3EnetProtoPortIpxFrames,
       "s3EnetProtoPortDecLavcFrames": s3EnetProtoPortDecLavcFrames,
       "s3EnetProtoPortNetBiosFrames": s3EnetProtoPortNetBiosFrames,
       "s3EnetProtoPortBrdgSpanTreeFrames": s3EnetProtoPortBrdgSpanTreeFrames,
       "s3EnetProtoBoardTable": s3EnetProtoBoardTable,
       "s3EnetProtoBoardEntry": s3EnetProtoBoardEntry,
       "s3EnetProtoBoardIndex": s3EnetProtoBoardIndex,
       "s3EnetProtoBoard8023Frames": s3EnetProtoBoard8023Frames,
       "s3EnetProtoBoardEthernetFrames": s3EnetProtoBoardEthernetFrames,
       "s3EnetProtoBoardOtherFrames": s3EnetProtoBoardOtherFrames,
       "s3EnetProtoBoardSnaFrames": s3EnetProtoBoardSnaFrames,
       "s3EnetProtoBoardIpFrames": s3EnetProtoBoardIpFrames,
       "s3EnetProtoBoardIsoFrames": s3EnetProtoBoardIsoFrames,
       "s3EnetProtoBoardArpFrames": s3EnetProtoBoardArpFrames,
       "s3EnetProtoBoardDecIVFrames": s3EnetProtoBoardDecIVFrames,
       "s3EnetProtoBoardDecLatFrames": s3EnetProtoBoardDecLatFrames,
       "s3EnetProtoBoardEthTalkFrames": s3EnetProtoBoardEthTalkFrames,
       "s3EnetProtoBoardXnsFrames": s3EnetProtoBoardXnsFrames,
       "s3EnetProtoBoardIpxFrames": s3EnetProtoBoardIpxFrames,
       "s3EnetProtoBoardDecLavcFrames": s3EnetProtoBoardDecLavcFrames,
       "s3EnetProtoBoardNetBiosFrames": s3EnetProtoBoardNetBiosFrames,
       "s3EnetProtoBoardBrdgSpanTreeFrames": s3EnetProtoBoardBrdgSpanTreeFrames,
       "s3000EnetProtoConc": s3000EnetProtoConc,
       "s3EnetProtoConc8023Frames": s3EnetProtoConc8023Frames,
       "s3EnetProtoConcEthernetFrames": s3EnetProtoConcEthernetFrames,
       "s3EnetProtoConcOtherFrames": s3EnetProtoConcOtherFrames,
       "s3EnetProtoConcSnaFrames": s3EnetProtoConcSnaFrames,
       "s3EnetProtoConcIpFrames": s3EnetProtoConcIpFrames,
       "s3EnetProtoConcIsoFrames": s3EnetProtoConcIsoFrames,
       "s3EnetProtoConcArpFrames": s3EnetProtoConcArpFrames,
       "s3EnetProtoConcDecIVFrames": s3EnetProtoConcDecIVFrames,
       "s3EnetProtoConcDecLatFrames": s3EnetProtoConcDecLatFrames,
       "s3EnetProtoConcEthTalkFrames": s3EnetProtoConcEthTalkFrames,
       "s3EnetProtoConcXnsFrames": s3EnetProtoConcXnsFrames,
       "s3EnetProtoConcIpxFrames": s3EnetProtoConcIpxFrames,
       "s3EnetProtoConcDecLavcFrames": s3EnetProtoConcDecLavcFrames,
       "s3EnetProtoConcNetBiosFrames": s3EnetProtoConcNetBiosFrames,
       "s3EnetProtoConcBrdgSpanTreeFrames": s3EnetProtoConcBrdgSpanTreeFrames,
       "s3000EnetHosts": s3000EnetHosts,
       "s3EnetHostTableSize": s3EnetHostTableSize,
       "s3EnetHostLastDeleteTime": s3EnetHostLastDeleteTime,
       "s3EnetHostTable": s3EnetHostTable,
       "s3EnetHostEntry": s3EnetHostEntry,
       "s3EnetHostIndex": s3EnetHostIndex,
       "s3EnetHostObserveOrder": s3EnetHostObserveOrder,
       "s3EnetHostNetAddr": s3EnetHostNetAddr,
       "s3EnetHostAddrType": s3EnetHostAddrType,
       "s3EnetHostMacAddress": s3EnetHostMacAddress,
       "s3EnetHostSlotIndex": s3EnetHostSlotIndex,
       "s3EnetHostPortIndex": s3EnetHostPortIndex,
       "s3EnetHostLearnMethod": s3EnetHostLearnMethod,
       "s3EnetHostTimeStamp": s3EnetHostTimeStamp}
)
