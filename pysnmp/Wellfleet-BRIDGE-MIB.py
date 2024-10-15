# SNMP MIB module (Wellfleet-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:54 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfBridgeGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBridgeGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBrLearning_ObjectIdentity = ObjectIdentity
wfBrLearning = _WfBrLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1)
)
_WfBrTp_ObjectIdentity = ObjectIdentity
wfBrTp = _WfBrTp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1)
)


class _WfBrTpBaseDelete_Type(Integer32):
    """Custom type wfBrTpBaseDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBrTpBaseDelete_Type.__name__ = "Integer32"
_WfBrTpBaseDelete_Object = MibScalar
wfBrTpBaseDelete = _WfBrTpBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 1),
    _WfBrTpBaseDelete_Type()
)
wfBrTpBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseDelete.setStatus("mandatory")


class _WfBrTpBaseEnable_Type(Integer32):
    """Custom type wfBrTpBaseEnable based on Integer32"""
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


_WfBrTpBaseEnable_Type.__name__ = "Integer32"
_WfBrTpBaseEnable_Object = MibScalar
wfBrTpBaseEnable = _WfBrTpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 2),
    _WfBrTpBaseEnable_Type()
)
wfBrTpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseEnable.setStatus("mandatory")


class _WfBrTpBaseState_Type(Integer32):
    """Custom type wfBrTpBaseState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrTpBaseState_Type.__name__ = "Integer32"
_WfBrTpBaseState_Object = MibScalar
wfBrTpBaseState = _WfBrTpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 3),
    _WfBrTpBaseState_Type()
)
wfBrTpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseState.setStatus("mandatory")
_WfBrTpBaseFDBEntries_Type = Counter32
_WfBrTpBaseFDBEntries_Object = MibScalar
wfBrTpBaseFDBEntries = _WfBrTpBaseFDBEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 4),
    _WfBrTpBaseFDBEntries_Type()
)
wfBrTpBaseFDBEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFDBEntries.setStatus("mandatory")


class _WfBrTpBaseFDBSize_Type(Integer32):
    """Custom type wfBrTpBaseFDBSize based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1024,
              2048,
              4096,
              8192,
              16384,
              32768,
              65536,
              131072)
        )
    )
    namedValues = NamedValues(
        *(("size1024", 1024),
          ("size131072", 131072),
          ("size16384", 16384),
          ("size2048", 2048),
          ("size32768", 32768),
          ("size4096", 4096),
          ("size65536", 65536),
          ("size8192", 8192))
    )


_WfBrTpBaseFDBSize_Type.__name__ = "Integer32"
_WfBrTpBaseFDBSize_Object = MibScalar
wfBrTpBaseFDBSize = _WfBrTpBaseFDBSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 5),
    _WfBrTpBaseFDBSize_Type()
)
wfBrTpBaseFDBSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseFDBSize.setStatus("mandatory")


class _WfBrTpBaseFDBEnable_Type(Integer32):
    """Custom type wfBrTpBaseFDBEnable based on Integer32"""
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


_WfBrTpBaseFDBEnable_Type.__name__ = "Integer32"
_WfBrTpBaseFDBEnable_Object = MibScalar
wfBrTpBaseFDBEnable = _WfBrTpBaseFDBEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 6),
    _WfBrTpBaseFDBEnable_Type()
)
wfBrTpBaseFDBEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseFDBEnable.setStatus("mandatory")


class _WfBrTpBaseFlushFwdTbl_Type(Integer32):
    """Custom type wfBrTpBaseFlushFwdTbl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flushed", 1),
          ("noflushed", 2))
    )


_WfBrTpBaseFlushFwdTbl_Type.__name__ = "Integer32"
_WfBrTpBaseFlushFwdTbl_Object = MibScalar
wfBrTpBaseFlushFwdTbl = _WfBrTpBaseFlushFwdTbl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 7),
    _WfBrTpBaseFlushFwdTbl_Type()
)
wfBrTpBaseFlushFwdTbl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpBaseFlushFwdTbl.setStatus("mandatory")
_WfBrTpBaseFDBPortChange_Type = Counter32
_WfBrTpBaseFDBPortChange_Object = MibScalar
wfBrTpBaseFDBPortChange = _WfBrTpBaseFDBPortChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 1, 8),
    _WfBrTpBaseFDBPortChange_Type()
)
wfBrTpBaseFDBPortChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFDBPortChange.setStatus("mandatory")
_WfBrTpFdbTable_Object = MibTable
wfBrTpFdbTable = _WfBrTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    wfBrTpFdbTable.setStatus("mandatory")
_WfBrTpFdbEntry_Object = MibTableRow
wfBrTpFdbEntry = _WfBrTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1)
)
wfBrTpFdbEntry.setIndexNames(
    (0, "Wellfleet-BRIDGE-MIB", "wfBrTpBaseFdbAddress"),
)
if mibBuilder.loadTexts:
    wfBrTpFdbEntry.setStatus("mandatory")


class _WfBrTpBaseFdbAddress_Type(OctetString):
    """Custom type wfBrTpBaseFdbAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfBrTpBaseFdbAddress_Type.__name__ = "OctetString"
_WfBrTpBaseFdbAddress_Object = MibTableColumn
wfBrTpBaseFdbAddress = _WfBrTpBaseFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 1),
    _WfBrTpBaseFdbAddress_Type()
)
wfBrTpBaseFdbAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbAddress.setStatus("mandatory")
_WfBrTpBaseFdbPort_Type = Integer32
_WfBrTpBaseFdbPort_Object = MibTableColumn
wfBrTpBaseFdbPort = _WfBrTpBaseFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 2),
    _WfBrTpBaseFdbPort_Type()
)
wfBrTpBaseFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbPort.setStatus("mandatory")


class _WfBrTpBaseFdbStatus_Type(Integer32):
    """Custom type wfBrTpBaseFdbStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            3
        )
    )
    namedValues = NamedValues(
        ("learned", 3)
    )


_WfBrTpBaseFdbStatus_Type.__name__ = "Integer32"
_WfBrTpBaseFdbStatus_Object = MibTableColumn
wfBrTpBaseFdbStatus = _WfBrTpBaseFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 2, 1, 3),
    _WfBrTpBaseFdbStatus_Type()
)
wfBrTpBaseFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpBaseFdbStatus.setStatus("mandatory")
_WfBrTpAggrStats_ObjectIdentity = ObjectIdentity
wfBrTpAggrStats = _WfBrTpAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 3)
)
_WfBrTpAggrInPkts_Type = Counter32
_WfBrTpAggrInPkts_Object = MibScalar
wfBrTpAggrInPkts = _WfBrTpAggrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 3, 1),
    _WfBrTpAggrInPkts_Type()
)
wfBrTpAggrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpAggrInPkts.setStatus("mandatory")
_WfBrTpAggrOutPkts_Type = Counter32
_WfBrTpAggrOutPkts_Object = MibScalar
wfBrTpAggrOutPkts = _WfBrTpAggrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 3, 2),
    _WfBrTpAggrOutPkts_Type()
)
wfBrTpAggrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpAggrOutPkts.setStatus("mandatory")
_WfBrTpAggrDiscardPkts_Type = Counter32
_WfBrTpAggrDiscardPkts_Object = MibScalar
wfBrTpAggrDiscardPkts = _WfBrTpAggrDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 1, 3, 3),
    _WfBrTpAggrDiscardPkts_Type()
)
wfBrTpAggrDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpAggrDiscardPkts.setStatus("mandatory")
_WfBrTpInterfaceTable_Object = MibTable
wfBrTpInterfaceTable = _WfBrTpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    wfBrTpInterfaceTable.setStatus("mandatory")
_WfBrTpInterfaceEntry_Object = MibTableRow
wfBrTpInterfaceEntry = _WfBrTpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1)
)
wfBrTpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-BRIDGE-MIB", "wfBrTpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrTpInterfaceEntry.setStatus("mandatory")


class _WfBrTpInterfaceDelete_Type(Integer32):
    """Custom type wfBrTpInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBrTpInterfaceDelete_Type.__name__ = "Integer32"
_WfBrTpInterfaceDelete_Object = MibTableColumn
wfBrTpInterfaceDelete = _WfBrTpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 1),
    _WfBrTpInterfaceDelete_Type()
)
wfBrTpInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpInterfaceDelete.setStatus("mandatory")


class _WfBrTpInterfaceEnable_Type(Integer32):
    """Custom type wfBrTpInterfaceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              17,
              33)
        )
    )
    namedValues = NamedValues(
        *(("circuitdump", 33),
          ("disabled", 2),
          ("enabled", 1),
          ("fwdtbldump", 17))
    )


_WfBrTpInterfaceEnable_Type.__name__ = "Integer32"
_WfBrTpInterfaceEnable_Object = MibTableColumn
wfBrTpInterfaceEnable = _WfBrTpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 2),
    _WfBrTpInterfaceEnable_Type()
)
wfBrTpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpInterfaceEnable.setStatus("mandatory")


class _WfBrTpInterfaceState_Type(Integer32):
    """Custom type wfBrTpInterfaceState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrTpInterfaceState_Type.__name__ = "Integer32"
_WfBrTpInterfaceState_Object = MibTableColumn
wfBrTpInterfaceState = _WfBrTpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 3),
    _WfBrTpInterfaceState_Type()
)
wfBrTpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceState.setStatus("mandatory")
_WfBrTpInterfaceCircuit_Type = Integer32
_WfBrTpInterfaceCircuit_Object = MibTableColumn
wfBrTpInterfaceCircuit = _WfBrTpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 4),
    _WfBrTpInterfaceCircuit_Type()
)
wfBrTpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceCircuit.setStatus("mandatory")
_WfBrTpInterfaceMaxInfo_Type = Integer32
_WfBrTpInterfaceMaxInfo_Object = MibTableColumn
wfBrTpInterfaceMaxInfo = _WfBrTpInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 5),
    _WfBrTpInterfaceMaxInfo_Type()
)
wfBrTpInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceMaxInfo.setStatus("mandatory")
_WfBrTpInterfaceInFrames_Type = Counter32
_WfBrTpInterfaceInFrames_Object = MibTableColumn
wfBrTpInterfaceInFrames = _WfBrTpInterfaceInFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 6),
    _WfBrTpInterfaceInFrames_Type()
)
wfBrTpInterfaceInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceInFrames.setStatus("mandatory")
_WfBrTpInterfaceOutFrames_Type = Counter32
_WfBrTpInterfaceOutFrames_Object = MibTableColumn
wfBrTpInterfaceOutFrames = _WfBrTpInterfaceOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 7),
    _WfBrTpInterfaceOutFrames_Type()
)
wfBrTpInterfaceOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceOutFrames.setStatus("mandatory")
_WfBrTpInterfaceInDiscards_Type = Counter32
_WfBrTpInterfaceInDiscards_Object = MibTableColumn
wfBrTpInterfaceInDiscards = _WfBrTpInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 8),
    _WfBrTpInterfaceInDiscards_Type()
)
wfBrTpInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTpInterfaceInDiscards.setStatus("mandatory")


class _WfBrTpInterfaceTranslationDisable_Type(Integer32):
    """Custom type wfBrTpInterfaceTranslationDisable based on Integer32"""
    defaultValue = 2

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


_WfBrTpInterfaceTranslationDisable_Type.__name__ = "Integer32"
_WfBrTpInterfaceTranslationDisable_Object = MibTableColumn
wfBrTpInterfaceTranslationDisable = _WfBrTpInterfaceTranslationDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 3, 1, 9),
    _WfBrTpInterfaceTranslationDisable_Type()
)
wfBrTpInterfaceTranslationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTpInterfaceTranslationDisable.setStatus("mandatory")
_WfBrTrafficFilterTable_Object = MibTable
wfBrTrafficFilterTable = _WfBrTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    wfBrTrafficFilterTable.setStatus("mandatory")
_WfBrTrafficFilterEntry_Object = MibTableRow
wfBrTrafficFilterEntry = _WfBrTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1)
)
wfBrTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-BRIDGE-MIB", "wfBrTrafficFilterCircuit"),
    (0, "Wellfleet-BRIDGE-MIB", "wfBrTrafficFilterRuleNumber"),
    (0, "Wellfleet-BRIDGE-MIB", "wfBrTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfBrTrafficFilterEntry.setStatus("mandatory")


class _WfBrTrafficFilterCreate_Type(Integer32):
    """Custom type wfBrTrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfBrTrafficFilterCreate_Type.__name__ = "Integer32"
_WfBrTrafficFilterCreate_Object = MibTableColumn
wfBrTrafficFilterCreate = _WfBrTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 1),
    _WfBrTrafficFilterCreate_Type()
)
wfBrTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCreate.setStatus("mandatory")


class _WfBrTrafficFilterEnable_Type(Integer32):
    """Custom type wfBrTrafficFilterEnable based on Integer32"""
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


_WfBrTrafficFilterEnable_Type.__name__ = "Integer32"
_WfBrTrafficFilterEnable_Object = MibTableColumn
wfBrTrafficFilterEnable = _WfBrTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 2),
    _WfBrTrafficFilterEnable_Type()
)
wfBrTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterEnable.setStatus("mandatory")


class _WfBrTrafficFilterStatus_Type(Integer32):
    """Custom type wfBrTrafficFilterStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfBrTrafficFilterStatus_Type.__name__ = "Integer32"
_WfBrTrafficFilterStatus_Object = MibTableColumn
wfBrTrafficFilterStatus = _WfBrTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 3),
    _WfBrTrafficFilterStatus_Type()
)
wfBrTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterStatus.setStatus("mandatory")
_WfBrTrafficFilterCounter_Type = Counter32
_WfBrTrafficFilterCounter_Object = MibTableColumn
wfBrTrafficFilterCounter = _WfBrTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 4),
    _WfBrTrafficFilterCounter_Type()
)
wfBrTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCounter.setStatus("mandatory")
_WfBrTrafficFilterDefinition_Type = Opaque
_WfBrTrafficFilterDefinition_Object = MibTableColumn
wfBrTrafficFilterDefinition = _WfBrTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 5),
    _WfBrTrafficFilterDefinition_Type()
)
wfBrTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterDefinition.setStatus("mandatory")
_WfBrTrafficFilterReserved_Type = Integer32
_WfBrTrafficFilterReserved_Object = MibTableColumn
wfBrTrafficFilterReserved = _WfBrTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 6),
    _WfBrTrafficFilterReserved_Type()
)
wfBrTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterReserved.setStatus("mandatory")
_WfBrTrafficFilterCircuit_Type = Integer32
_WfBrTrafficFilterCircuit_Object = MibTableColumn
wfBrTrafficFilterCircuit = _WfBrTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 7),
    _WfBrTrafficFilterCircuit_Type()
)
wfBrTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterCircuit.setStatus("mandatory")
_WfBrTrafficFilterRuleNumber_Type = Integer32
_WfBrTrafficFilterRuleNumber_Object = MibTableColumn
wfBrTrafficFilterRuleNumber = _WfBrTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 8),
    _WfBrTrafficFilterRuleNumber_Type()
)
wfBrTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterRuleNumber.setStatus("mandatory")
_WfBrTrafficFilterFragment_Type = Integer32
_WfBrTrafficFilterFragment_Object = MibTableColumn
wfBrTrafficFilterFragment = _WfBrTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 9),
    _WfBrTrafficFilterFragment_Type()
)
wfBrTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrTrafficFilterFragment.setStatus("mandatory")
_WfBrTrafficFilterName_Type = DisplayString
_WfBrTrafficFilterName_Object = MibTableColumn
wfBrTrafficFilterName = _WfBrTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 1, 4, 1, 10),
    _WfBrTrafficFilterName_Type()
)
wfBrTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrTrafficFilterName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BRIDGE-MIB",
    **{"wfBrLearning": wfBrLearning,
       "wfBrTp": wfBrTp,
       "wfBrTpBaseDelete": wfBrTpBaseDelete,
       "wfBrTpBaseEnable": wfBrTpBaseEnable,
       "wfBrTpBaseState": wfBrTpBaseState,
       "wfBrTpBaseFDBEntries": wfBrTpBaseFDBEntries,
       "wfBrTpBaseFDBSize": wfBrTpBaseFDBSize,
       "wfBrTpBaseFDBEnable": wfBrTpBaseFDBEnable,
       "wfBrTpBaseFlushFwdTbl": wfBrTpBaseFlushFwdTbl,
       "wfBrTpBaseFDBPortChange": wfBrTpBaseFDBPortChange,
       "wfBrTpFdbTable": wfBrTpFdbTable,
       "wfBrTpFdbEntry": wfBrTpFdbEntry,
       "wfBrTpBaseFdbAddress": wfBrTpBaseFdbAddress,
       "wfBrTpBaseFdbPort": wfBrTpBaseFdbPort,
       "wfBrTpBaseFdbStatus": wfBrTpBaseFdbStatus,
       "wfBrTpAggrStats": wfBrTpAggrStats,
       "wfBrTpAggrInPkts": wfBrTpAggrInPkts,
       "wfBrTpAggrOutPkts": wfBrTpAggrOutPkts,
       "wfBrTpAggrDiscardPkts": wfBrTpAggrDiscardPkts,
       "wfBrTpInterfaceTable": wfBrTpInterfaceTable,
       "wfBrTpInterfaceEntry": wfBrTpInterfaceEntry,
       "wfBrTpInterfaceDelete": wfBrTpInterfaceDelete,
       "wfBrTpInterfaceEnable": wfBrTpInterfaceEnable,
       "wfBrTpInterfaceState": wfBrTpInterfaceState,
       "wfBrTpInterfaceCircuit": wfBrTpInterfaceCircuit,
       "wfBrTpInterfaceMaxInfo": wfBrTpInterfaceMaxInfo,
       "wfBrTpInterfaceInFrames": wfBrTpInterfaceInFrames,
       "wfBrTpInterfaceOutFrames": wfBrTpInterfaceOutFrames,
       "wfBrTpInterfaceInDiscards": wfBrTpInterfaceInDiscards,
       "wfBrTpInterfaceTranslationDisable": wfBrTpInterfaceTranslationDisable,
       "wfBrTrafficFilterTable": wfBrTrafficFilterTable,
       "wfBrTrafficFilterEntry": wfBrTrafficFilterEntry,
       "wfBrTrafficFilterCreate": wfBrTrafficFilterCreate,
       "wfBrTrafficFilterEnable": wfBrTrafficFilterEnable,
       "wfBrTrafficFilterStatus": wfBrTrafficFilterStatus,
       "wfBrTrafficFilterCounter": wfBrTrafficFilterCounter,
       "wfBrTrafficFilterDefinition": wfBrTrafficFilterDefinition,
       "wfBrTrafficFilterReserved": wfBrTrafficFilterReserved,
       "wfBrTrafficFilterCircuit": wfBrTrafficFilterCircuit,
       "wfBrTrafficFilterRuleNumber": wfBrTrafficFilterRuleNumber,
       "wfBrTrafficFilterFragment": wfBrTrafficFilterFragment,
       "wfBrTrafficFilterName": wfBrTrafficFilterName}
)
