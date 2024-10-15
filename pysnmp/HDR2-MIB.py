# SNMP MIB module (HDR2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HDR2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:04 2024
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4)
)
_Hdr2_ObjectIdentity = ObjectIdentity
hdr2 = _Hdr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4, 48)
)
_Hdr2Cfg_ObjectIdentity = ObjectIdentity
hdr2Cfg = _Hdr2Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1)
)
_Hdr2CfgTable_Object = MibTable
hdr2CfgTable = _Hdr2CfgTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1)
)
if mibBuilder.loadTexts:
    hdr2CfgTable.setStatus("mandatory")
_Hdr2CfgEntry_Object = MibTableRow
hdr2CfgEntry = _Hdr2CfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1)
)
hdr2CfgEntry.setIndexNames(
    (0, "HDR2-MIB", "hdr2CfgIndex"),
)
if mibBuilder.loadTexts:
    hdr2CfgEntry.setStatus("mandatory")
_Hdr2CfgIndex_Type = Integer32
_Hdr2CfgIndex_Object = MibTableColumn
hdr2CfgIndex = _Hdr2CfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 1),
    _Hdr2CfgIndex_Type()
)
hdr2CfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdr2CfgIndex.setStatus("mandatory")


class _Hdr2CfgRegSigType_Type(Integer32):
    """Custom type hdr2CfgRegSigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r2MFC", 1),
          ("r2MFSC", 2))
    )


_Hdr2CfgRegSigType_Type.__name__ = "Integer32"
_Hdr2CfgRegSigType_Object = MibTableColumn
hdr2CfgRegSigType = _Hdr2CfgRegSigType_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 2),
    _Hdr2CfgRegSigType_Type()
)
hdr2CfgRegSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgRegSigType.setStatus("mandatory")


class _Hdr2CfgAnumIden_Type(Integer32):
    """Custom type hdr2CfgAnumIden based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgAnumIden_Type.__name__ = "Integer32"
_Hdr2CfgAnumIden_Object = MibTableColumn
hdr2CfgAnumIden = _Hdr2CfgAnumIden_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 3),
    _Hdr2CfgAnumIden_Type()
)
hdr2CfgAnumIden.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgAnumIden.setStatus("mandatory")


class _Hdr2CfgForcedRel_Type(Integer32):
    """Custom type hdr2CfgForcedRel based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgForcedRel_Type.__name__ = "Integer32"
_Hdr2CfgForcedRel_Object = MibTableColumn
hdr2CfgForcedRel = _Hdr2CfgForcedRel_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 4),
    _Hdr2CfgForcedRel_Type()
)
hdr2CfgForcedRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgForcedRel.setStatus("mandatory")


class _Hdr2CfgLastBDigTout_Type(Integer32):
    """Custom type hdr2CfgLastBDigTout based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Hdr2CfgLastBDigTout_Type.__name__ = "Integer32"
_Hdr2CfgLastBDigTout_Object = MibTableColumn
hdr2CfgLastBDigTout = _Hdr2CfgLastBDigTout_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 5),
    _Hdr2CfgLastBDigTout_Type()
)
hdr2CfgLastBDigTout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgLastBDigTout.setStatus("mandatory")


class _Hdr2CfgAddrComplete_Type(Integer32):
    """Custom type hdr2CfgAddrComplete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a3", 1),
          ("a5", 2),
          ("a6", 3))
    )


_Hdr2CfgAddrComplete_Type.__name__ = "Integer32"
_Hdr2CfgAddrComplete_Object = MibTableColumn
hdr2CfgAddrComplete = _Hdr2CfgAddrComplete_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 6),
    _Hdr2CfgAddrComplete_Type()
)
hdr2CfgAddrComplete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgAddrComplete.setStatus("mandatory")


class _Hdr2CfgEndBparty_Type(Integer32):
    """Custom type hdr2CfgEndBparty based on Integer32"""
    defaultValue = 2

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


_Hdr2CfgEndBparty_Type.__name__ = "Integer32"
_Hdr2CfgEndBparty_Object = MibTableColumn
hdr2CfgEndBparty = _Hdr2CfgEndBparty_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 7),
    _Hdr2CfgEndBparty_Type()
)
hdr2CfgEndBparty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgEndBparty.setStatus("mandatory")


class _Hdr2CfgAlawMulaw_Type(Integer32):
    """Custom type hdr2CfgAlawMulaw based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aLAW", 1),
          ("auto", 3),
          ("mULAW", 2))
    )


_Hdr2CfgAlawMulaw_Type.__name__ = "Integer32"
_Hdr2CfgAlawMulaw_Object = MibTableColumn
hdr2CfgAlawMulaw = _Hdr2CfgAlawMulaw_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 8),
    _Hdr2CfgAlawMulaw_Type()
)
hdr2CfgAlawMulaw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgAlawMulaw.setStatus("mandatory")


class _Hdr2CfgLineSigType_Type(Integer32):
    """Custom type hdr2CfgLineSigType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("p7DIG", 2),
          ("r2DIG", 1),
          ("r2EandM", 3))
    )


_Hdr2CfgLineSigType_Type.__name__ = "Integer32"
_Hdr2CfgLineSigType_Object = MibTableColumn
hdr2CfgLineSigType = _Hdr2CfgLineSigType_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 9),
    _Hdr2CfgLineSigType_Type()
)
hdr2CfgLineSigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgLineSigType.setStatus("mandatory")


class _Hdr2CfgProjID_Type(Integer32):
    """Custom type hdr2CfgProjID based on Integer32"""
    defaultValue = 1

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("argentina", 2),
          ("australia", 3),
          ("brazil", 4),
          ("chile", 5),
          ("china", 6),
          ("colombia", 7),
          ("iTU-T", 1),
          ("india", 8),
          ("korea", 9),
          ("malaysia", 10),
          ("mexico", 11),
          ("newZealand", 12),
          ("philippines", 13),
          ("sweden", 14),
          ("venezuela", 15))
    )


_Hdr2CfgProjID_Type.__name__ = "Integer32"
_Hdr2CfgProjID_Object = MibTableColumn
hdr2CfgProjID = _Hdr2CfgProjID_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 10),
    _Hdr2CfgProjID_Type()
)
hdr2CfgProjID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgProjID.setStatus("mandatory")


class _Hdr2CfgSeizeAck_Type(Integer32):
    """Custom type hdr2CfgSeizeAck based on Integer32"""
    defaultValue = 2

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


_Hdr2CfgSeizeAck_Type.__name__ = "Integer32"
_Hdr2CfgSeizeAck_Object = MibTableColumn
hdr2CfgSeizeAck = _Hdr2CfgSeizeAck_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 11),
    _Hdr2CfgSeizeAck_Type()
)
hdr2CfgSeizeAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSeizeAck.setStatus("mandatory")


class _Hdr2CfgAnumBnum_Type(Integer32):
    """Custom type hdr2CfgAnumBnum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36),
    )


_Hdr2CfgAnumBnum_Type.__name__ = "Integer32"
_Hdr2CfgAnumBnum_Object = MibTableColumn
hdr2CfgAnumBnum = _Hdr2CfgAnumBnum_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 12),
    _Hdr2CfgAnumBnum_Type()
)
hdr2CfgAnumBnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgAnumBnum.setStatus("mandatory")


class _Hdr2CfgSubBusy_Type(Integer32):
    """Custom type hdr2CfgSubBusy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b2", 1),
          ("b3", 2))
    )


_Hdr2CfgSubBusy_Type.__name__ = "Integer32"
_Hdr2CfgSubBusy_Object = MibTableColumn
hdr2CfgSubBusy = _Hdr2CfgSubBusy_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 13),
    _Hdr2CfgSubBusy_Type()
)
hdr2CfgSubBusy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSubBusy.setStatus("mandatory")


class _Hdr2CfgSndCallingPtyCatgy_Type(Integer32):
    """Custom type hdr2CfgSndCallingPtyCatgy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a5", 1),
          ("a6", 2))
    )


_Hdr2CfgSndCallingPtyCatgy_Type.__name__ = "Integer32"
_Hdr2CfgSndCallingPtyCatgy_Object = MibTableColumn
hdr2CfgSndCallingPtyCatgy = _Hdr2CfgSndCallingPtyCatgy_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 14),
    _Hdr2CfgSndCallingPtyCatgy_Type()
)
hdr2CfgSndCallingPtyCatgy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndCallingPtyCatgy.setStatus("mandatory")


class _Hdr2CfgLineDirection_Type(Integer32):
    """Custom type hdr2CfgLineDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_Hdr2CfgLineDirection_Type.__name__ = "Integer32"
_Hdr2CfgLineDirection_Object = MibTableColumn
hdr2CfgLineDirection = _Hdr2CfgLineDirection_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 15),
    _Hdr2CfgLineDirection_Type()
)
hdr2CfgLineDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgLineDirection.setStatus("mandatory")


class _Hdr2CfgPersistentOverride_Type(Integer32):
    """Custom type hdr2CfgPersistentOverride based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hdr2CfgPersistentOverride_Type.__name__ = "Integer32"
_Hdr2CfgPersistentOverride_Object = MibTableColumn
hdr2CfgPersistentOverride = _Hdr2CfgPersistentOverride_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 16),
    _Hdr2CfgPersistentOverride_Type()
)
hdr2CfgPersistentOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgPersistentOverride.setStatus("mandatory")


class _Hdr2CfgWrongNumber_Type(Integer32):
    """Custom type hdr2CfgWrongNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b5", 1),
          ("b7", 2))
    )


_Hdr2CfgWrongNumber_Type.__name__ = "Integer32"
_Hdr2CfgWrongNumber_Object = MibTableColumn
hdr2CfgWrongNumber = _Hdr2CfgWrongNumber_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 17),
    _Hdr2CfgWrongNumber_Type()
)
hdr2CfgWrongNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgWrongNumber.setStatus("mandatory")


class _Hdr2CfgIncomingCpc_Type(Integer32):
    """Custom type hdr2CfgIncomingCpc based on Integer32"""
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
        *(("analog", 1),
          ("digital", 2),
          ("maintanace", 3),
          ("test", 4))
    )


_Hdr2CfgIncomingCpc_Type.__name__ = "Integer32"
_Hdr2CfgIncomingCpc_Object = MibTableColumn
hdr2CfgIncomingCpc = _Hdr2CfgIncomingCpc_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 18),
    _Hdr2CfgIncomingCpc_Type()
)
hdr2CfgIncomingCpc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgIncomingCpc.setStatus("mandatory")


class _Hdr2CfgRegSigStatus_Type(Integer32):
    """Custom type hdr2CfgRegSigStatus based on Integer32"""
    defaultValue = 2

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


_Hdr2CfgRegSigStatus_Type.__name__ = "Integer32"
_Hdr2CfgRegSigStatus_Object = MibTableColumn
hdr2CfgRegSigStatus = _Hdr2CfgRegSigStatus_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 19),
    _Hdr2CfgRegSigStatus_Type()
)
hdr2CfgRegSigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgRegSigStatus.setStatus("mandatory")


class _Hdr2CfgUnusedAbcd_Type(Integer32):
    """Custom type hdr2CfgUnusedAbcd based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hdr2CfgUnusedAbcd_Type.__name__ = "Integer32"
_Hdr2CfgUnusedAbcd_Object = MibTableColumn
hdr2CfgUnusedAbcd = _Hdr2CfgUnusedAbcd_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 20),
    _Hdr2CfgUnusedAbcd_Type()
)
hdr2CfgUnusedAbcd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgUnusedAbcd.setStatus("mandatory")


class _Hdr2CfgBlkToBlk_Type(Integer32):
    """Custom type hdr2CfgBlkToBlk based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgBlkToBlk_Type.__name__ = "Integer32"
_Hdr2CfgBlkToBlk_Object = MibTableColumn
hdr2CfgBlkToBlk = _Hdr2CfgBlkToBlk_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 21),
    _Hdr2CfgBlkToBlk_Type()
)
hdr2CfgBlkToBlk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgBlkToBlk.setStatus("mandatory")


class _Hdr2CfgDelayLos_Type(Integer32):
    """Custom type hdr2CfgDelayLos based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Hdr2CfgDelayLos_Type.__name__ = "Integer32"
_Hdr2CfgDelayLos_Object = MibTableColumn
hdr2CfgDelayLos = _Hdr2CfgDelayLos_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 22),
    _Hdr2CfgDelayLos_Type()
)
hdr2CfgDelayLos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgDelayLos.setStatus("mandatory")


class _Hdr2CfgInGlare_Type(Integer32):
    """Custom type hdr2CfgInGlare based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgInGlare_Type.__name__ = "Integer32"
_Hdr2CfgInGlare_Object = MibTableColumn
hdr2CfgInGlare = _Hdr2CfgInGlare_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 23),
    _Hdr2CfgInGlare_Type()
)
hdr2CfgInGlare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgInGlare.setStatus("mandatory")


class _Hdr2CfgClrCall_Type(Integer32):
    """Custom type hdr2CfgClrCall based on Integer32"""
    defaultValue = 2

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


_Hdr2CfgClrCall_Type.__name__ = "Integer32"
_Hdr2CfgClrCall_Object = MibTableColumn
hdr2CfgClrCall = _Hdr2CfgClrCall_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 24),
    _Hdr2CfgClrCall_Type()
)
hdr2CfgClrCall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgClrCall.setStatus("mandatory")


class _Hdr2CfgANumQry_Type(Integer32):
    """Custom type hdr2CfgANumQry based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgANumQry_Type.__name__ = "Integer32"
_Hdr2CfgANumQry_Object = MibTableColumn
hdr2CfgANumQry = _Hdr2CfgANumQry_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 25),
    _Hdr2CfgANumQry_Type()
)
hdr2CfgANumQry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgANumQry.setStatus("mandatory")


class _Hdr2CfgANumNAv_Type(Integer32):
    """Custom type hdr2CfgANumNAv based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgANumNAv_Type.__name__ = "Integer32"
_Hdr2CfgANumNAv_Object = MibTableColumn
hdr2CfgANumNAv = _Hdr2CfgANumNAv_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 26),
    _Hdr2CfgANumNAv_Type()
)
hdr2CfgANumNAv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgANumNAv.setStatus("mandatory")


class _Hdr2CfgANumReq_Type(Integer32):
    """Custom type hdr2CfgANumReq based on Integer32"""
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
        *(("c1", 1),
          ("c5", 2),
          ("c6", 3),
          ("c9", 4))
    )


_Hdr2CfgANumReq_Type.__name__ = "Integer32"
_Hdr2CfgANumReq_Object = MibTableColumn
hdr2CfgANumReq = _Hdr2CfgANumReq_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 27),
    _Hdr2CfgANumReq_Type()
)
hdr2CfgANumReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgANumReq.setStatus("mandatory")


class _Hdr2CfgClrFwd_Type(Integer32):
    """Custom type hdr2CfgClrFwd based on Integer32"""
    defaultValue = 1

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


_Hdr2CfgClrFwd_Type.__name__ = "Integer32"
_Hdr2CfgClrFwd_Object = MibTableColumn
hdr2CfgClrFwd = _Hdr2CfgClrFwd_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 28),
    _Hdr2CfgClrFwd_Type()
)
hdr2CfgClrFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgClrFwd.setStatus("mandatory")


class _Hdr2CfgRelGuard_Type(Integer32):
    """Custom type hdr2CfgRelGuard based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Hdr2CfgRelGuard_Type.__name__ = "Integer32"
_Hdr2CfgRelGuard_Object = MibTableColumn
hdr2CfgRelGuard = _Hdr2CfgRelGuard_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 29),
    _Hdr2CfgRelGuard_Type()
)
hdr2CfgRelGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgRelGuard.setStatus("mandatory")


class _Hdr2CfgPIClrBck_Type(Integer32):
    """Custom type hdr2CfgPIClrBck based on Integer32"""
    defaultValue = 2

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


_Hdr2CfgPIClrBck_Type.__name__ = "Integer32"
_Hdr2CfgPIClrBck_Object = MibTableColumn
hdr2CfgPIClrBck = _Hdr2CfgPIClrBck_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 30),
    _Hdr2CfgPIClrBck_Type()
)
hdr2CfgPIClrBck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgPIClrBck.setStatus("mandatory")


class _Hdr2CfgDelayAns_Type(Integer32):
    """Custom type hdr2CfgDelayAns based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2000),
    )


_Hdr2CfgDelayAns_Type.__name__ = "Integer32"
_Hdr2CfgDelayAns_Object = MibTableColumn
hdr2CfgDelayAns = _Hdr2CfgDelayAns_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 31),
    _Hdr2CfgDelayAns_Type()
)
hdr2CfgDelayAns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgDelayAns.setStatus("mandatory")


class _Hdr2CfgBNumLen_Type(Integer32):
    """Custom type hdr2CfgBNumLen based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 36),
    )


_Hdr2CfgBNumLen_Type.__name__ = "Integer32"
_Hdr2CfgBNumLen_Object = MibTableColumn
hdr2CfgBNumLen = _Hdr2CfgBNumLen_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 32),
    _Hdr2CfgBNumLen_Type()
)
hdr2CfgBNumLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgBNumLen.setStatus("mandatory")


class _Hdr2CfgActBTout_Type(Integer32):
    """Custom type hdr2CfgActBTout based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("b-number", 1),
          ("error", 2))
    )


_Hdr2CfgActBTout_Type.__name__ = "Integer32"
_Hdr2CfgActBTout_Object = MibTableColumn
hdr2CfgActBTout = _Hdr2CfgActBTout_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 33),
    _Hdr2CfgActBTout_Type()
)
hdr2CfgActBTout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgActBTout.setStatus("mandatory")


class _Hdr2CfgInSubFree_Type(Integer32):
    """Custom type hdr2CfgInSubFree based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b1", 1),
          ("b5", 2),
          ("b6", 3))
    )


_Hdr2CfgInSubFree_Type.__name__ = "Integer32"
_Hdr2CfgInSubFree_Object = MibTableColumn
hdr2CfgInSubFree = _Hdr2CfgInSubFree_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 34),
    _Hdr2CfgInSubFree_Type()
)
hdr2CfgInSubFree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgInSubFree.setStatus("mandatory")


class _Hdr2CfgBNumNFnd_Type(Integer32):
    """Custom type hdr2CfgBNumNFnd based on Integer32"""
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
        *(("acceptAllCalls", 1),
          ("acceptAllCallsAnalog", 4),
          ("acceptAllCallsAsDigital", 3),
          ("rejectAllCalls", 2))
    )


_Hdr2CfgBNumNFnd_Type.__name__ = "Integer32"
_Hdr2CfgBNumNFnd_Object = MibTableColumn
hdr2CfgBNumNFnd = _Hdr2CfgBNumNFnd_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 35),
    _Hdr2CfgBNumNFnd_Type()
)
hdr2CfgBNumNFnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgBNumNFnd.setStatus("mandatory")


class _Hdr2CfgSndBNumN_Type(Integer32):
    """Custom type hdr2CfgSndBNumN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a10", 2),
          ("a9", 1))
    )


_Hdr2CfgSndBNumN_Type.__name__ = "Integer32"
_Hdr2CfgSndBNumN_Object = MibTableColumn
hdr2CfgSndBNumN = _Hdr2CfgSndBNumN_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 36),
    _Hdr2CfgSndBNumN_Type()
)
hdr2CfgSndBNumN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndBNumN.setStatus("mandatory")


class _Hdr2CfgSndBNumN1_Type(Integer32):
    """Custom type hdr2CfgSndBNumN1 based on Integer32"""
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
        *(("a10", 4),
          ("a2", 1),
          ("a8", 2),
          ("a9", 3))
    )


_Hdr2CfgSndBNumN1_Type.__name__ = "Integer32"
_Hdr2CfgSndBNumN1_Object = MibTableColumn
hdr2CfgSndBNumN1 = _Hdr2CfgSndBNumN1_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 37),
    _Hdr2CfgSndBNumN1_Type()
)
hdr2CfgSndBNumN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndBNumN1.setStatus("mandatory")


class _Hdr2CfgSndBNumN2_Type(Integer32):
    """Custom type hdr2CfgSndBNumN2 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a7", 1),
          ("a9", 2))
    )


_Hdr2CfgSndBNumN2_Type.__name__ = "Integer32"
_Hdr2CfgSndBNumN2_Object = MibTableColumn
hdr2CfgSndBNumN2 = _Hdr2CfgSndBNumN2_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 38),
    _Hdr2CfgSndBNumN2_Type()
)
hdr2CfgSndBNumN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndBNumN2.setStatus("mandatory")


class _Hdr2CfgSndBNumN3_Type(Integer32):
    """Custom type hdr2CfgSndBNumN3 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a10", 2),
          ("a8", 1))
    )


_Hdr2CfgSndBNumN3_Type.__name__ = "Integer32"
_Hdr2CfgSndBNumN3_Object = MibTableColumn
hdr2CfgSndBNumN3 = _Hdr2CfgSndBNumN3_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 39),
    _Hdr2CfgSndBNumN3_Type()
)
hdr2CfgSndBNumN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndBNumN3.setStatus("mandatory")


class _Hdr2CfgSndFBNum_Type(Integer32):
    """Custom type hdr2CfgSndFBNum based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("a10", 3),
          ("a2", 1),
          ("a9", 2))
    )


_Hdr2CfgSndFBNum_Type.__name__ = "Integer32"
_Hdr2CfgSndFBNum_Object = MibTableColumn
hdr2CfgSndFBNum = _Hdr2CfgSndFBNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 40),
    _Hdr2CfgSndFBNum_Type()
)
hdr2CfgSndFBNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgSndFBNum.setStatus("mandatory")


class _Hdr2CfgDumANum_Type(DisplayString):
    """Custom type hdr2CfgDumANum based on DisplayString"""
    defaultValue = OctetString("1234")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 36),
    )


_Hdr2CfgDumANum_Type.__name__ = "DisplayString"
_Hdr2CfgDumANum_Object = MibTableColumn
hdr2CfgDumANum = _Hdr2CfgDumANum_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 41),
    _Hdr2CfgDumANum_Type()
)
hdr2CfgDumANum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgDumANum.setStatus("mandatory")


class _Hdr2CfgEndANum_Type(Integer32):
    """Custom type hdr2CfgEndANum based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iii-12", 1),
          ("iii-15", 2))
    )


_Hdr2CfgEndANum_Type.__name__ = "Integer32"
_Hdr2CfgEndANum_Object = MibTableColumn
hdr2CfgEndANum = _Hdr2CfgEndANum_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 42),
    _Hdr2CfgEndANum_Type()
)
hdr2CfgEndANum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgEndANum.setStatus("mandatory")


class _Hdr2CfgOutCatAnalog_Type(Integer32):
    """Custom type hdr2CfgOutCatAnalog based on Integer32"""
    defaultValue = 1

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ii-1", 1),
          ("ii-10", 10),
          ("ii-11", 11),
          ("ii-12", 12),
          ("ii-13", 13),
          ("ii-14", 14),
          ("ii-15", 15),
          ("ii-2", 2),
          ("ii-3", 3),
          ("ii-4", 4),
          ("ii-5", 5),
          ("ii-6", 6),
          ("ii-7", 7),
          ("ii-8", 8),
          ("ii-9", 9))
    )


_Hdr2CfgOutCatAnalog_Type.__name__ = "Integer32"
_Hdr2CfgOutCatAnalog_Object = MibTableColumn
hdr2CfgOutCatAnalog = _Hdr2CfgOutCatAnalog_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 43),
    _Hdr2CfgOutCatAnalog_Type()
)
hdr2CfgOutCatAnalog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgOutCatAnalog.setStatus("mandatory")


class _Hdr2CfgOutCatDigital_Type(Integer32):
    """Custom type hdr2CfgOutCatDigital based on Integer32"""
    defaultValue = 6

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ii-1", 1),
          ("ii-10", 10),
          ("ii-11", 11),
          ("ii-12", 12),
          ("ii-13", 13),
          ("ii-14", 14),
          ("ii-15", 15),
          ("ii-2", 2),
          ("ii-3", 3),
          ("ii-4", 4),
          ("ii-5", 5),
          ("ii-6", 6),
          ("ii-7", 7),
          ("ii-8", 8),
          ("ii-9", 9))
    )


_Hdr2CfgOutCatDigital_Type.__name__ = "Integer32"
_Hdr2CfgOutCatDigital_Object = MibTableColumn
hdr2CfgOutCatDigital = _Hdr2CfgOutCatDigital_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 44),
    _Hdr2CfgOutCatDigital_Type()
)
hdr2CfgOutCatDigital.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgOutCatDigital.setStatus("mandatory")


class _Hdr2CfgOutCatTest_Type(Integer32):
    """Custom type hdr2CfgOutCatTest based on Integer32"""
    defaultValue = 13

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ii-1", 1),
          ("ii-10", 10),
          ("ii-11", 11),
          ("ii-12", 12),
          ("ii-13", 13),
          ("ii-14", 14),
          ("ii-15", 15),
          ("ii-2", 2),
          ("ii-3", 3),
          ("ii-4", 4),
          ("ii-5", 5),
          ("ii-6", 6),
          ("ii-7", 7),
          ("ii-8", 8),
          ("ii-9", 9))
    )


_Hdr2CfgOutCatTest_Type.__name__ = "Integer32"
_Hdr2CfgOutCatTest_Object = MibTableColumn
hdr2CfgOutCatTest = _Hdr2CfgOutCatTest_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 45),
    _Hdr2CfgOutCatTest_Type()
)
hdr2CfgOutCatTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgOutCatTest.setStatus("mandatory")


class _Hdr2CfgOutCatMaintenance_Type(Integer32):
    """Custom type hdr2CfgOutCatMaintenance based on Integer32"""
    defaultValue = 3

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
              15)
        )
    )
    namedValues = NamedValues(
        *(("ii-1", 1),
          ("ii-10", 10),
          ("ii-11", 11),
          ("ii-12", 12),
          ("ii-13", 13),
          ("ii-14", 14),
          ("ii-15", 15),
          ("ii-2", 2),
          ("ii-3", 3),
          ("ii-4", 4),
          ("ii-5", 5),
          ("ii-6", 6),
          ("ii-7", 7),
          ("ii-8", 8),
          ("ii-9", 9))
    )


_Hdr2CfgOutCatMaintenance_Type.__name__ = "Integer32"
_Hdr2CfgOutCatMaintenance_Object = MibTableColumn
hdr2CfgOutCatMaintenance = _Hdr2CfgOutCatMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 1, 1, 1, 46),
    _Hdr2CfgOutCatMaintenance_Type()
)
hdr2CfgOutCatMaintenance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2CfgOutCatMaintenance.setStatus("mandatory")
_Hdr2InCatMap_ObjectIdentity = ObjectIdentity
hdr2InCatMap = _Hdr2InCatMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2)
)
_Hdr2InCatMapTable_Object = MibTable
hdr2InCatMapTable = _Hdr2InCatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2, 1)
)
if mibBuilder.loadTexts:
    hdr2InCatMapTable.setStatus("mandatory")
_Hdr2InCatMapEntry_Object = MibTableRow
hdr2InCatMapEntry = _Hdr2InCatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2, 1, 1)
)
hdr2InCatMapEntry.setIndexNames(
    (0, "HDR2-MIB", "hdr2InCatMapIndex"),
    (0, "HDR2-MIB", "hdr2InCatMapSigNum"),
)
if mibBuilder.loadTexts:
    hdr2InCatMapEntry.setStatus("mandatory")
_Hdr2InCatMapIndex_Type = Integer32
_Hdr2InCatMapIndex_Object = MibTableColumn
hdr2InCatMapIndex = _Hdr2InCatMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2, 1, 1, 1),
    _Hdr2InCatMapIndex_Type()
)
hdr2InCatMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdr2InCatMapIndex.setStatus("mandatory")


class _Hdr2InCatMapSigNum_Type(Integer32):
    """Custom type hdr2InCatMapSigNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hdr2InCatMapSigNum_Type.__name__ = "Integer32"
_Hdr2InCatMapSigNum_Object = MibTableColumn
hdr2InCatMapSigNum = _Hdr2InCatMapSigNum_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2, 1, 1, 2),
    _Hdr2InCatMapSigNum_Type()
)
hdr2InCatMapSigNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdr2InCatMapSigNum.setStatus("mandatory")


class _Hdr2InCatMapCallType_Type(Integer32):
    """Custom type hdr2InCatMapCallType based on Integer32"""
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
        *(("analog", 1),
          ("digital", 2),
          ("maintenance", 4),
          ("test", 3))
    )


_Hdr2InCatMapCallType_Type.__name__ = "Integer32"
_Hdr2InCatMapCallType_Object = MibTableColumn
hdr2InCatMapCallType = _Hdr2InCatMapCallType_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 2, 1, 1, 3),
    _Hdr2InCatMapCallType_Type()
)
hdr2InCatMapCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2InCatMapCallType.setStatus("mandatory")
_Hdr2Pte_ObjectIdentity = ObjectIdentity
hdr2Pte = _Hdr2Pte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3)
)
_Hdr2PteTable_Object = MibTable
hdr2PteTable = _Hdr2PteTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1)
)
if mibBuilder.loadTexts:
    hdr2PteTable.setStatus("mandatory")
_Hdr2PteEntry_Object = MibTableRow
hdr2PteEntry = _Hdr2PteEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1)
)
hdr2PteEntry.setIndexNames(
    (0, "HDR2-MIB", "hdr2PteIndex"),
)
if mibBuilder.loadTexts:
    hdr2PteEntry.setStatus("mandatory")
_Hdr2PteIndex_Type = Integer32
_Hdr2PteIndex_Object = MibTableColumn
hdr2PteIndex = _Hdr2PteIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1, 1),
    _Hdr2PteIndex_Type()
)
hdr2PteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdr2PteIndex.setStatus("mandatory")


class _Hdr2PteMultiFrame_Type(Integer32):
    """Custom type hdr2PteMultiFrame based on Integer32"""
    defaultValue = 4

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
        *(("disableAll", 1),
          ("enableAll", 4),
          ("enableSysLogOnly", 3),
          ("enableTrapOnly", 2))
    )


_Hdr2PteMultiFrame_Type.__name__ = "Integer32"
_Hdr2PteMultiFrame_Object = MibTableColumn
hdr2PteMultiFrame = _Hdr2PteMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1, 2),
    _Hdr2PteMultiFrame_Type()
)
hdr2PteMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2PteMultiFrame.setStatus("mandatory")


class _Hdr2PteMultiFrameClr_Type(Integer32):
    """Custom type hdr2PteMultiFrameClr based on Integer32"""
    defaultValue = 4

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
        *(("disableAll", 1),
          ("enableAll", 4),
          ("enableSysLogOnly", 3),
          ("enableTrapOnly", 2))
    )


_Hdr2PteMultiFrameClr_Type.__name__ = "Integer32"
_Hdr2PteMultiFrameClr_Object = MibTableColumn
hdr2PteMultiFrameClr = _Hdr2PteMultiFrameClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1, 3),
    _Hdr2PteMultiFrameClr_Type()
)
hdr2PteMultiFrameClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2PteMultiFrameClr.setStatus("mandatory")


class _Hdr2PteRemMultiFrame_Type(Integer32):
    """Custom type hdr2PteRemMultiFrame based on Integer32"""
    defaultValue = 4

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
        *(("disableAll", 1),
          ("enableAll", 4),
          ("enableSysLogOnly", 3),
          ("enableTrapOnly", 2))
    )


_Hdr2PteRemMultiFrame_Type.__name__ = "Integer32"
_Hdr2PteRemMultiFrame_Object = MibTableColumn
hdr2PteRemMultiFrame = _Hdr2PteRemMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1, 4),
    _Hdr2PteRemMultiFrame_Type()
)
hdr2PteRemMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2PteRemMultiFrame.setStatus("mandatory")


class _Hdr2PteRemMultiFrameClr_Type(Integer32):
    """Custom type hdr2PteRemMultiFrameClr based on Integer32"""
    defaultValue = 4

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
        *(("disableAll", 1),
          ("enableAll", 4),
          ("enableSysLogOnly", 3),
          ("enableTrapOnly", 2))
    )


_Hdr2PteRemMultiFrameClr_Type.__name__ = "Integer32"
_Hdr2PteRemMultiFrameClr_Object = MibTableColumn
hdr2PteRemMultiFrameClr = _Hdr2PteRemMultiFrameClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 3, 1, 1, 5),
    _Hdr2PteRemMultiFrameClr_Type()
)
hdr2PteRemMultiFrameClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2PteRemMultiFrameClr.setStatus("mandatory")
_Hdr2Te_ObjectIdentity = ObjectIdentity
hdr2Te = _Hdr2Te_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4)
)
_Hdr2TeTable_Object = MibTable
hdr2TeTable = _Hdr2TeTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1)
)
if mibBuilder.loadTexts:
    hdr2TeTable.setStatus("mandatory")
_Hdr2TeEntry_Object = MibTableRow
hdr2TeEntry = _Hdr2TeEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1)
)
hdr2TeEntry.setIndexNames(
    (0, "HDR2-MIB", "hdr2TeIndex"),
)
if mibBuilder.loadTexts:
    hdr2TeEntry.setStatus("mandatory")
_Hdr2TeIndex_Type = Integer32
_Hdr2TeIndex_Object = MibTableColumn
hdr2TeIndex = _Hdr2TeIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1, 1),
    _Hdr2TeIndex_Type()
)
hdr2TeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hdr2TeIndex.setStatus("mandatory")


class _Hdr2TeMultiFrame_Type(Integer32):
    """Custom type hdr2TeMultiFrame based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Hdr2TeMultiFrame_Type.__name__ = "Integer32"
_Hdr2TeMultiFrame_Object = MibTableColumn
hdr2TeMultiFrame = _Hdr2TeMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1, 2),
    _Hdr2TeMultiFrame_Type()
)
hdr2TeMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2TeMultiFrame.setStatus("mandatory")


class _Hdr2TeMultiFrameClr_Type(Integer32):
    """Custom type hdr2TeMultiFrameClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Hdr2TeMultiFrameClr_Type.__name__ = "Integer32"
_Hdr2TeMultiFrameClr_Object = MibTableColumn
hdr2TeMultiFrameClr = _Hdr2TeMultiFrameClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1, 3),
    _Hdr2TeMultiFrameClr_Type()
)
hdr2TeMultiFrameClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2TeMultiFrameClr.setStatus("mandatory")


class _Hdr2TeRemMultiFrame_Type(Integer32):
    """Custom type hdr2TeRemMultiFrame based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Hdr2TeRemMultiFrame_Type.__name__ = "Integer32"
_Hdr2TeRemMultiFrame_Object = MibTableColumn
hdr2TeRemMultiFrame = _Hdr2TeRemMultiFrame_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1, 4),
    _Hdr2TeRemMultiFrame_Type()
)
hdr2TeRemMultiFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2TeRemMultiFrame.setStatus("mandatory")


class _Hdr2TeRemMultiFrameClr_Type(Integer32):
    """Custom type hdr2TeRemMultiFrameClr based on Integer32"""
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
        *(("disableAll", 2),
          ("enableAll", 4),
          ("enableLog", 3),
          ("enableTrap", 1))
    )


_Hdr2TeRemMultiFrameClr_Type.__name__ = "Integer32"
_Hdr2TeRemMultiFrameClr_Object = MibTableColumn
hdr2TeRemMultiFrameClr = _Hdr2TeRemMultiFrameClr_Object(
    (1, 3, 6, 1, 4, 1, 429, 4, 48, 4, 1, 1, 5),
    _Hdr2TeRemMultiFrameClr_Type()
)
hdr2TeRemMultiFrameClr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hdr2TeRemMultiFrameClr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HDR2-MIB",
    **{"usr": usr,
       "common": common,
       "hdr2": hdr2,
       "hdr2Cfg": hdr2Cfg,
       "hdr2CfgTable": hdr2CfgTable,
       "hdr2CfgEntry": hdr2CfgEntry,
       "hdr2CfgIndex": hdr2CfgIndex,
       "hdr2CfgRegSigType": hdr2CfgRegSigType,
       "hdr2CfgAnumIden": hdr2CfgAnumIden,
       "hdr2CfgForcedRel": hdr2CfgForcedRel,
       "hdr2CfgLastBDigTout": hdr2CfgLastBDigTout,
       "hdr2CfgAddrComplete": hdr2CfgAddrComplete,
       "hdr2CfgEndBparty": hdr2CfgEndBparty,
       "hdr2CfgAlawMulaw": hdr2CfgAlawMulaw,
       "hdr2CfgLineSigType": hdr2CfgLineSigType,
       "hdr2CfgProjID": hdr2CfgProjID,
       "hdr2CfgSeizeAck": hdr2CfgSeizeAck,
       "hdr2CfgAnumBnum": hdr2CfgAnumBnum,
       "hdr2CfgSubBusy": hdr2CfgSubBusy,
       "hdr2CfgSndCallingPtyCatgy": hdr2CfgSndCallingPtyCatgy,
       "hdr2CfgLineDirection": hdr2CfgLineDirection,
       "hdr2CfgPersistentOverride": hdr2CfgPersistentOverride,
       "hdr2CfgWrongNumber": hdr2CfgWrongNumber,
       "hdr2CfgIncomingCpc": hdr2CfgIncomingCpc,
       "hdr2CfgRegSigStatus": hdr2CfgRegSigStatus,
       "hdr2CfgUnusedAbcd": hdr2CfgUnusedAbcd,
       "hdr2CfgBlkToBlk": hdr2CfgBlkToBlk,
       "hdr2CfgDelayLos": hdr2CfgDelayLos,
       "hdr2CfgInGlare": hdr2CfgInGlare,
       "hdr2CfgClrCall": hdr2CfgClrCall,
       "hdr2CfgANumQry": hdr2CfgANumQry,
       "hdr2CfgANumNAv": hdr2CfgANumNAv,
       "hdr2CfgANumReq": hdr2CfgANumReq,
       "hdr2CfgClrFwd": hdr2CfgClrFwd,
       "hdr2CfgRelGuard": hdr2CfgRelGuard,
       "hdr2CfgPIClrBck": hdr2CfgPIClrBck,
       "hdr2CfgDelayAns": hdr2CfgDelayAns,
       "hdr2CfgBNumLen": hdr2CfgBNumLen,
       "hdr2CfgActBTout": hdr2CfgActBTout,
       "hdr2CfgInSubFree": hdr2CfgInSubFree,
       "hdr2CfgBNumNFnd": hdr2CfgBNumNFnd,
       "hdr2CfgSndBNumN": hdr2CfgSndBNumN,
       "hdr2CfgSndBNumN1": hdr2CfgSndBNumN1,
       "hdr2CfgSndBNumN2": hdr2CfgSndBNumN2,
       "hdr2CfgSndBNumN3": hdr2CfgSndBNumN3,
       "hdr2CfgSndFBNum": hdr2CfgSndFBNum,
       "hdr2CfgDumANum": hdr2CfgDumANum,
       "hdr2CfgEndANum": hdr2CfgEndANum,
       "hdr2CfgOutCatAnalog": hdr2CfgOutCatAnalog,
       "hdr2CfgOutCatDigital": hdr2CfgOutCatDigital,
       "hdr2CfgOutCatTest": hdr2CfgOutCatTest,
       "hdr2CfgOutCatMaintenance": hdr2CfgOutCatMaintenance,
       "hdr2InCatMap": hdr2InCatMap,
       "hdr2InCatMapTable": hdr2InCatMapTable,
       "hdr2InCatMapEntry": hdr2InCatMapEntry,
       "hdr2InCatMapIndex": hdr2InCatMapIndex,
       "hdr2InCatMapSigNum": hdr2InCatMapSigNum,
       "hdr2InCatMapCallType": hdr2InCatMapCallType,
       "hdr2Pte": hdr2Pte,
       "hdr2PteTable": hdr2PteTable,
       "hdr2PteEntry": hdr2PteEntry,
       "hdr2PteIndex": hdr2PteIndex,
       "hdr2PteMultiFrame": hdr2PteMultiFrame,
       "hdr2PteMultiFrameClr": hdr2PteMultiFrameClr,
       "hdr2PteRemMultiFrame": hdr2PteRemMultiFrame,
       "hdr2PteRemMultiFrameClr": hdr2PteRemMultiFrameClr,
       "hdr2Te": hdr2Te,
       "hdr2TeTable": hdr2TeTable,
       "hdr2TeEntry": hdr2TeEntry,
       "hdr2TeIndex": hdr2TeIndex,
       "hdr2TeMultiFrame": hdr2TeMultiFrame,
       "hdr2TeMultiFrameClr": hdr2TeMultiFrameClr,
       "hdr2TeRemMultiFrame": hdr2TeRemMultiFrame,
       "hdr2TeRemMultiFrameClr": hdr2TeRemMultiFrameClr}
)
