# SNMP MIB module (BayNetworks-BPKG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BayNetworks-BPKG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:18 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfBacPktGenGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBacPktGenGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBacPktGenBase_ObjectIdentity = ObjectIdentity
wfBacPktGenBase = _WfBacPktGenBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1)
)


class _WfBacPktGenDelete_Type(Integer32):
    """Custom type wfBacPktGenDelete based on Integer32"""
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


_WfBacPktGenDelete_Type.__name__ = "Integer32"
_WfBacPktGenDelete_Object = MibScalar
wfBacPktGenDelete = _WfBacPktGenDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 1),
    _WfBacPktGenDelete_Type()
)
wfBacPktGenDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenDelete.setStatus("mandatory")


class _WfBacPktGenDisable_Type(Integer32):
    """Custom type wfBacPktGenDisable based on Integer32"""
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


_WfBacPktGenDisable_Type.__name__ = "Integer32"
_WfBacPktGenDisable_Object = MibScalar
wfBacPktGenDisable = _WfBacPktGenDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 2),
    _WfBacPktGenDisable_Type()
)
wfBacPktGenDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenDisable.setStatus("mandatory")


class _WfBacPktGenState_Type(Integer32):
    """Custom type wfBacPktGenState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBacPktGenState_Type.__name__ = "Integer32"
_WfBacPktGenState_Object = MibScalar
wfBacPktGenState = _WfBacPktGenState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 3),
    _WfBacPktGenState_Type()
)
wfBacPktGenState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenState.setStatus("mandatory")
_WfBacPktGenTxTabSum_Type = Counter32
_WfBacPktGenTxTabSum_Object = MibScalar
wfBacPktGenTxTabSum = _WfBacPktGenTxTabSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 4),
    _WfBacPktGenTxTabSum_Type()
)
wfBacPktGenTxTabSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenTxTabSum.setStatus("mandatory")
_WfBacPktGenRxTabSum_Type = Counter32
_WfBacPktGenRxTabSum_Object = MibScalar
wfBacPktGenRxTabSum = _WfBacPktGenRxTabSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 5),
    _WfBacPktGenRxTabSum_Type()
)
wfBacPktGenRxTabSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenRxTabSum.setStatus("mandatory")
_WfBacPktGenCxpTable_Object = MibTable
wfBacPktGenCxpTable = _WfBacPktGenCxpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wfBacPktGenCxpTable.setStatus("mandatory")
_WfBacPktGenCxpEntry_Object = MibTableRow
wfBacPktGenCxpEntry = _WfBacPktGenCxpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1)
)
wfBacPktGenCxpEntry.setIndexNames(
    (0, "BayNetworks-BPKG-MIB", "wfBacPktGenCxpId"),
)
if mibBuilder.loadTexts:
    wfBacPktGenCxpEntry.setStatus("mandatory")


class _WfBacPktGenCxpDelete_Type(Integer32):
    """Custom type wfBacPktGenCxpDelete based on Integer32"""
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


_WfBacPktGenCxpDelete_Type.__name__ = "Integer32"
_WfBacPktGenCxpDelete_Object = MibTableColumn
wfBacPktGenCxpDelete = _WfBacPktGenCxpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 1),
    _WfBacPktGenCxpDelete_Type()
)
wfBacPktGenCxpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenCxpDelete.setStatus("mandatory")


class _WfBacPktGenCxpId_Type(Integer32):
    """Custom type wfBacPktGenCxpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 8),
    )


_WfBacPktGenCxpId_Type.__name__ = "Integer32"
_WfBacPktGenCxpId_Object = MibTableColumn
wfBacPktGenCxpId = _WfBacPktGenCxpId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 2),
    _WfBacPktGenCxpId_Type()
)
wfBacPktGenCxpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenCxpId.setStatus("mandatory")
_WfBacPktGenStreamMask_Type = Counter32
_WfBacPktGenStreamMask_Object = MibTableColumn
wfBacPktGenStreamMask = _WfBacPktGenStreamMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 3),
    _WfBacPktGenStreamMask_Type()
)
wfBacPktGenStreamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenStreamMask.setStatus("mandatory")
_WfBacPktGenPktSeed_ObjectIdentity = ObjectIdentity
wfBacPktGenPktSeed = _WfBacPktGenPktSeed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3)
)


class _WfBacPktGenSeedPkts_Type(Integer32):
    """Custom type wfBacPktGenSeedPkts based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("seedpackets", 1),
          ("unseedpackets", 2))
    )


_WfBacPktGenSeedPkts_Type.__name__ = "Integer32"
_WfBacPktGenSeedPkts_Object = MibScalar
wfBacPktGenSeedPkts = _WfBacPktGenSeedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3, 1),
    _WfBacPktGenSeedPkts_Type()
)
wfBacPktGenSeedPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenSeedPkts.setStatus("mandatory")


class _WfBacPktGenPktSeedState_Type(Integer32):
    """Custom type wfBacPktGenPktSeedState based on Integer32"""
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
        *(("idle", 4),
          ("operationstarted", 3),
          ("packetseeded", 1),
          ("packetunseeded", 2))
    )


_WfBacPktGenPktSeedState_Type.__name__ = "Integer32"
_WfBacPktGenPktSeedState_Object = MibScalar
wfBacPktGenPktSeedState = _WfBacPktGenPktSeedState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3, 2),
    _WfBacPktGenPktSeedState_Type()
)
wfBacPktGenPktSeedState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenPktSeedState.setStatus("mandatory")
_WfBacPktGenCxpGlobal_ObjectIdentity = ObjectIdentity
wfBacPktGenCxpGlobal = _WfBacPktGenCxpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4)
)


class _WfBacPktGenCxpGlobalDelete_Type(Integer32):
    """Custom type wfBacPktGenCxpGlobalDelete based on Integer32"""
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


_WfBacPktGenCxpGlobalDelete_Type.__name__ = "Integer32"
_WfBacPktGenCxpGlobalDelete_Object = MibScalar
wfBacPktGenCxpGlobalDelete = _WfBacPktGenCxpGlobalDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 1),
    _WfBacPktGenCxpGlobalDelete_Type()
)
wfBacPktGenCxpGlobalDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenCxpGlobalDelete.setStatus("mandatory")
_WfBacPktGenGlobalStreamMask_Type = Counter32
_WfBacPktGenGlobalStreamMask_Object = MibScalar
wfBacPktGenGlobalStreamMask = _WfBacPktGenGlobalStreamMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 2),
    _WfBacPktGenGlobalStreamMask_Type()
)
wfBacPktGenGlobalStreamMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenGlobalStreamMask.setStatus("mandatory")


class _WfBacPktGenGlobalRecActive_Type(Integer32):
    """Custom type wfBacPktGenGlobalRecActive based on Integer32"""
    defaultValue = 2

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


_WfBacPktGenGlobalRecActive_Type.__name__ = "Integer32"
_WfBacPktGenGlobalRecActive_Object = MibScalar
wfBacPktGenGlobalRecActive = _WfBacPktGenGlobalRecActive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 3),
    _WfBacPktGenGlobalRecActive_Type()
)
wfBacPktGenGlobalRecActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenGlobalRecActive.setStatus("mandatory")
_WfBacPktGenCctTable_Object = MibTable
wfBacPktGenCctTable = _WfBacPktGenCctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5)
)
if mibBuilder.loadTexts:
    wfBacPktGenCctTable.setStatus("mandatory")
_WfBacPktGenCctEntry_Object = MibTableRow
wfBacPktGenCctEntry = _WfBacPktGenCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1)
)
wfBacPktGenCctEntry.setIndexNames(
    (0, "BayNetworks-BPKG-MIB", "wfBacPktGenCctNumber"),
)
if mibBuilder.loadTexts:
    wfBacPktGenCctEntry.setStatus("mandatory")


class _WfBacPktGenCctDelete_Type(Integer32):
    """Custom type wfBacPktGenCctDelete based on Integer32"""
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


_WfBacPktGenCctDelete_Type.__name__ = "Integer32"
_WfBacPktGenCctDelete_Object = MibTableColumn
wfBacPktGenCctDelete = _WfBacPktGenCctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 1),
    _WfBacPktGenCctDelete_Type()
)
wfBacPktGenCctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenCctDelete.setStatus("mandatory")
_WfBacPktGenCctNumber_Type = Integer32
_WfBacPktGenCctNumber_Object = MibTableColumn
wfBacPktGenCctNumber = _WfBacPktGenCctNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 2),
    _WfBacPktGenCctNumber_Type()
)
wfBacPktGenCctNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenCctNumber.setStatus("mandatory")


class _WfBacPktGenCctState_Type(Integer32):
    """Custom type wfBacPktGenCctState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfBacPktGenCctState_Type.__name__ = "Integer32"
_WfBacPktGenCctState_Object = MibTableColumn
wfBacPktGenCctState = _WfBacPktGenCctState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 3),
    _WfBacPktGenCctState_Type()
)
wfBacPktGenCctState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenCctState.setStatus("mandatory")
_WfBacPktGenCctName_Type = DisplayString
_WfBacPktGenCctName_Object = MibTableColumn
wfBacPktGenCctName = _WfBacPktGenCctName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 4),
    _WfBacPktGenCctName_Type()
)
wfBacPktGenCctName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenCctName.setStatus("mandatory")
_WfBacPktGenPktFile_ObjectIdentity = ObjectIdentity
wfBacPktGenPktFile = _WfBacPktGenPktFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6)
)


class _WfBacPktGenPktFileAppend_Type(Integer32):
    """Custom type wfBacPktGenPktFileAppend based on Integer32"""
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


_WfBacPktGenPktFileAppend_Type.__name__ = "Integer32"
_WfBacPktGenPktFileAppend_Object = MibScalar
wfBacPktGenPktFileAppend = _WfBacPktGenPktFileAppend_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6, 1),
    _WfBacPktGenPktFileAppend_Type()
)
wfBacPktGenPktFileAppend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenPktFileAppend.setStatus("mandatory")
_WfBacPktGenPktFileName_Type = DisplayString
_WfBacPktGenPktFileName_Object = MibScalar
wfBacPktGenPktFileName = _WfBacPktGenPktFileName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6, 2),
    _WfBacPktGenPktFileName_Type()
)
wfBacPktGenPktFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktFileName.setStatus("mandatory")
_WfBacPktGenPktGrpTable_Object = MibTable
wfBacPktGenPktGrpTable = _WfBacPktGenPktGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpTable.setStatus("mandatory")
_WfBacPktGenPktGrpEntry_Object = MibTableRow
wfBacPktGenPktGrpEntry = _WfBacPktGenPktGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1)
)
wfBacPktGenPktGrpEntry.setIndexNames(
    (0, "BayNetworks-BPKG-MIB", "wfBacPktGenPktGrpNumber"),
)
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpEntry.setStatus("mandatory")
_WfBacPktGenPktGrpNumber_Type = Integer32
_WfBacPktGenPktGrpNumber_Object = MibTableColumn
wfBacPktGenPktGrpNumber = _WfBacPktGenPktGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 1),
    _WfBacPktGenPktGrpNumber_Type()
)
wfBacPktGenPktGrpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpNumber.setStatus("mandatory")
_WfBacPktGenPktGrpDelay1_Type = Integer32
_WfBacPktGenPktGrpDelay1_Object = MibTableColumn
wfBacPktGenPktGrpDelay1 = _WfBacPktGenPktGrpDelay1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 2),
    _WfBacPktGenPktGrpDelay1_Type()
)
wfBacPktGenPktGrpDelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpDelay1.setStatus("mandatory")
_WfBacPktGenPktGrpDelay2_Type = Integer32
_WfBacPktGenPktGrpDelay2_Object = MibTableColumn
wfBacPktGenPktGrpDelay2 = _WfBacPktGenPktGrpDelay2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 3),
    _WfBacPktGenPktGrpDelay2_Type()
)
wfBacPktGenPktGrpDelay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpDelay2.setStatus("mandatory")
_WfBacPktGenPktGrpDelay3_Type = Integer32
_WfBacPktGenPktGrpDelay3_Object = MibTableColumn
wfBacPktGenPktGrpDelay3 = _WfBacPktGenPktGrpDelay3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 4),
    _WfBacPktGenPktGrpDelay3_Type()
)
wfBacPktGenPktGrpDelay3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpDelay3.setStatus("mandatory")
_WfBacPktGenPktGrpDelay4_Type = Integer32
_WfBacPktGenPktGrpDelay4_Object = MibTableColumn
wfBacPktGenPktGrpDelay4 = _WfBacPktGenPktGrpDelay4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 5),
    _WfBacPktGenPktGrpDelay4_Type()
)
wfBacPktGenPktGrpDelay4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpDelay4.setStatus("mandatory")
_WfBacPktGenPktGrpCount1_Type = Integer32
_WfBacPktGenPktGrpCount1_Object = MibTableColumn
wfBacPktGenPktGrpCount1 = _WfBacPktGenPktGrpCount1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 6),
    _WfBacPktGenPktGrpCount1_Type()
)
wfBacPktGenPktGrpCount1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpCount1.setStatus("mandatory")
_WfBacPktGenPktGrpCount2_Type = Integer32
_WfBacPktGenPktGrpCount2_Object = MibTableColumn
wfBacPktGenPktGrpCount2 = _WfBacPktGenPktGrpCount2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 7),
    _WfBacPktGenPktGrpCount2_Type()
)
wfBacPktGenPktGrpCount2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpCount2.setStatus("mandatory")
_WfBacPktGenPktGrpCount3_Type = Integer32
_WfBacPktGenPktGrpCount3_Object = MibTableColumn
wfBacPktGenPktGrpCount3 = _WfBacPktGenPktGrpCount3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 8),
    _WfBacPktGenPktGrpCount3_Type()
)
wfBacPktGenPktGrpCount3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpCount3.setStatus("mandatory")
_WfBacPktGenPktGrpCount4_Type = Integer32
_WfBacPktGenPktGrpCount4_Object = MibTableColumn
wfBacPktGenPktGrpCount4 = _WfBacPktGenPktGrpCount4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 9),
    _WfBacPktGenPktGrpCount4_Type()
)
wfBacPktGenPktGrpCount4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpCount4.setStatus("mandatory")
_WfBacPktGenPktSeedSum_Type = Counter32
_WfBacPktGenPktSeedSum_Object = MibTableColumn
wfBacPktGenPktSeedSum = _WfBacPktGenPktSeedSum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 10),
    _WfBacPktGenPktSeedSum_Type()
)
wfBacPktGenPktSeedSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenPktSeedSum.setStatus("mandatory")
_WfBacPktGenPktGrpCxp_Type = Integer32
_WfBacPktGenPktGrpCxp_Object = MibTableColumn
wfBacPktGenPktGrpCxp = _WfBacPktGenPktGrpCxp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 11),
    _WfBacPktGenPktGrpCxp_Type()
)
wfBacPktGenPktGrpCxp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenPktGrpCxp.setStatus("mandatory")
_WfBacPktGenStrmCtrlTable_Object = MibTable
wfBacPktGenStrmCtrlTable = _WfBacPktGenStrmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8)
)
if mibBuilder.loadTexts:
    wfBacPktGenStrmCtrlTable.setStatus("mandatory")
_WfBacPktGenStrmCtrlEntry_Object = MibTableRow
wfBacPktGenStrmCtrlEntry = _WfBacPktGenStrmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1)
)
wfBacPktGenStrmCtrlEntry.setIndexNames(
    (0, "BayNetworks-BPKG-MIB", "wfBacPktGenStrmNumber"),
    (0, "BayNetworks-BPKG-MIB", "wfBacPktGenStrmCxp"),
)
if mibBuilder.loadTexts:
    wfBacPktGenStrmCtrlEntry.setStatus("mandatory")


class _WfBacPktGenStrmNumber_Type(Integer32):
    """Custom type wfBacPktGenStrmNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WfBacPktGenStrmNumber_Type.__name__ = "Integer32"
_WfBacPktGenStrmNumber_Object = MibTableColumn
wfBacPktGenStrmNumber = _WfBacPktGenStrmNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 1),
    _WfBacPktGenStrmNumber_Type()
)
wfBacPktGenStrmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenStrmNumber.setStatus("mandatory")


class _WfBacPktGenStrmCxp_Type(Integer32):
    """Custom type wfBacPktGenStrmCxp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 8),
    )


_WfBacPktGenStrmCxp_Type.__name__ = "Integer32"
_WfBacPktGenStrmCxp_Object = MibTableColumn
wfBacPktGenStrmCxp = _WfBacPktGenStrmCxp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 2),
    _WfBacPktGenStrmCxp_Type()
)
wfBacPktGenStrmCxp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenStrmCxp.setStatus("mandatory")


class _WfBacPktGenStrmState_Type(Integer32):
    """Custom type wfBacPktGenStrmState based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("killed", 2),
          ("notpresent", 4),
          ("pktgen", 1))
    )


_WfBacPktGenStrmState_Type.__name__ = "Integer32"
_WfBacPktGenStrmState_Object = MibTableColumn
wfBacPktGenStrmState = _WfBacPktGenStrmState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 3),
    _WfBacPktGenStrmState_Type()
)
wfBacPktGenStrmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenStrmState.setStatus("mandatory")
_WfBacPktGenSetStrmPktGrp_Type = Integer32
_WfBacPktGenSetStrmPktGrp_Object = MibTableColumn
wfBacPktGenSetStrmPktGrp = _WfBacPktGenSetStrmPktGrp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 4),
    _WfBacPktGenSetStrmPktGrp_Type()
)
wfBacPktGenSetStrmPktGrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBacPktGenSetStrmPktGrp.setStatus("mandatory")
_WfBacPktGenStrmPktGrp_Type = Integer32
_WfBacPktGenStrmPktGrp_Object = MibTableColumn
wfBacPktGenStrmPktGrp = _WfBacPktGenStrmPktGrp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 5),
    _WfBacPktGenStrmPktGrp_Type()
)
wfBacPktGenStrmPktGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBacPktGenStrmPktGrp.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BayNetworks-BPKG-MIB",
    **{"wfBacPktGenBase": wfBacPktGenBase,
       "wfBacPktGenDelete": wfBacPktGenDelete,
       "wfBacPktGenDisable": wfBacPktGenDisable,
       "wfBacPktGenState": wfBacPktGenState,
       "wfBacPktGenTxTabSum": wfBacPktGenTxTabSum,
       "wfBacPktGenRxTabSum": wfBacPktGenRxTabSum,
       "wfBacPktGenCxpTable": wfBacPktGenCxpTable,
       "wfBacPktGenCxpEntry": wfBacPktGenCxpEntry,
       "wfBacPktGenCxpDelete": wfBacPktGenCxpDelete,
       "wfBacPktGenCxpId": wfBacPktGenCxpId,
       "wfBacPktGenStreamMask": wfBacPktGenStreamMask,
       "wfBacPktGenPktSeed": wfBacPktGenPktSeed,
       "wfBacPktGenSeedPkts": wfBacPktGenSeedPkts,
       "wfBacPktGenPktSeedState": wfBacPktGenPktSeedState,
       "wfBacPktGenCxpGlobal": wfBacPktGenCxpGlobal,
       "wfBacPktGenCxpGlobalDelete": wfBacPktGenCxpGlobalDelete,
       "wfBacPktGenGlobalStreamMask": wfBacPktGenGlobalStreamMask,
       "wfBacPktGenGlobalRecActive": wfBacPktGenGlobalRecActive,
       "wfBacPktGenCctTable": wfBacPktGenCctTable,
       "wfBacPktGenCctEntry": wfBacPktGenCctEntry,
       "wfBacPktGenCctDelete": wfBacPktGenCctDelete,
       "wfBacPktGenCctNumber": wfBacPktGenCctNumber,
       "wfBacPktGenCctState": wfBacPktGenCctState,
       "wfBacPktGenCctName": wfBacPktGenCctName,
       "wfBacPktGenPktFile": wfBacPktGenPktFile,
       "wfBacPktGenPktFileAppend": wfBacPktGenPktFileAppend,
       "wfBacPktGenPktFileName": wfBacPktGenPktFileName,
       "wfBacPktGenPktGrpTable": wfBacPktGenPktGrpTable,
       "wfBacPktGenPktGrpEntry": wfBacPktGenPktGrpEntry,
       "wfBacPktGenPktGrpNumber": wfBacPktGenPktGrpNumber,
       "wfBacPktGenPktGrpDelay1": wfBacPktGenPktGrpDelay1,
       "wfBacPktGenPktGrpDelay2": wfBacPktGenPktGrpDelay2,
       "wfBacPktGenPktGrpDelay3": wfBacPktGenPktGrpDelay3,
       "wfBacPktGenPktGrpDelay4": wfBacPktGenPktGrpDelay4,
       "wfBacPktGenPktGrpCount1": wfBacPktGenPktGrpCount1,
       "wfBacPktGenPktGrpCount2": wfBacPktGenPktGrpCount2,
       "wfBacPktGenPktGrpCount3": wfBacPktGenPktGrpCount3,
       "wfBacPktGenPktGrpCount4": wfBacPktGenPktGrpCount4,
       "wfBacPktGenPktSeedSum": wfBacPktGenPktSeedSum,
       "wfBacPktGenPktGrpCxp": wfBacPktGenPktGrpCxp,
       "wfBacPktGenStrmCtrlTable": wfBacPktGenStrmCtrlTable,
       "wfBacPktGenStrmCtrlEntry": wfBacPktGenStrmCtrlEntry,
       "wfBacPktGenStrmNumber": wfBacPktGenStrmNumber,
       "wfBacPktGenStrmCxp": wfBacPktGenStrmCxp,
       "wfBacPktGenStrmState": wfBacPktGenStrmState,
       "wfBacPktGenSetStrmPktGrp": wfBacPktGenSetStrmPktGrp,
       "wfBacPktGenStrmPktGrp": wfBacPktGenStrmPktGrp}
)
