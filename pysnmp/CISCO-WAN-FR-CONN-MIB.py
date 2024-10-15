# SNMP MIB module (CISCO-WAN-FR-CONN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WAN-FR-CONN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:02 2024
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

(frChan,
 frameRelay) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "frChan",
    "frameRelay")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoWanFrConnMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 47)
)
ciscoWanFrConnMIB.setRevisions(
        ("2002-09-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrChanCnfGrp_ObjectIdentity = ObjectIdentity
frChanCnfGrp = _FrChanCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1)
)
_FrChanCnfGrpTable_Object = MibTable
frChanCnfGrpTable = _FrChanCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    frChanCnfGrpTable.setStatus("current")
_FrChanCnfGrpEntry_Object = MibTableRow
frChanCnfGrpEntry = _FrChanCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1)
)
frChanCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-MIB", "chanNum"),
)
if mibBuilder.loadTexts:
    frChanCnfGrpEntry.setStatus("current")


class _ChanNum_Type(Integer32):
    """Custom type chanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ChanNum_Type.__name__ = "Integer32"
_ChanNum_Object = MibTableColumn
chanNum = _ChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 1),
    _ChanNum_Type()
)
chanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanNum.setStatus("current")


class _ChanRowStatus_Type(Integer32):
    """Custom type chanRowStatus based on Integer32"""
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
        *(("add", 1),
          ("del", 2),
          ("mod", 3),
          ("outOfService", 4))
    )


_ChanRowStatus_Type.__name__ = "Integer32"
_ChanRowStatus_Object = MibTableColumn
chanRowStatus = _ChanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 2),
    _ChanRowStatus_Type()
)
chanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanRowStatus.setStatus("current")
_ChanPortNum_Type = Integer32
_ChanPortNum_Object = MibTableColumn
chanPortNum = _ChanPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 3),
    _ChanPortNum_Type()
)
chanPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanPortNum.setStatus("current")


class _DLCI_Type(Integer32):
    """Custom type dLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DLCI_Type.__name__ = "Integer32"
_DLCI_Object = MibTableColumn
dLCI = _DLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 4),
    _DLCI_Type()
)
dLCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dLCI.setStatus("current")


class _EgressQSelect_Type(Integer32):
    """Custom type egressQSelect based on Integer32"""
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
        *(("highPriority", 1),
          ("lowPriority", 2),
          ("notSupported", 3))
    )


_EgressQSelect_Type.__name__ = "Integer32"
_EgressQSelect_Object = MibTableColumn
egressQSelect = _EgressQSelect_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 5),
    _EgressQSelect_Type()
)
egressQSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressQSelect.setStatus("current")


class _IngressQDepth_Type(Integer32):
    """Custom type ingressQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4510, 2097151),
    )


_IngressQDepth_Type.__name__ = "Integer32"
_IngressQDepth_Object = MibTableColumn
ingressQDepth = _IngressQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 6),
    _IngressQDepth_Type()
)
ingressQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressQDepth.setStatus("current")


class _IngressQECNThresh_Type(Integer32):
    """Custom type ingressQECNThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_IngressQECNThresh_Type.__name__ = "Integer32"
_IngressQECNThresh_Object = MibTableColumn
ingressQECNThresh = _IngressQECNThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 7),
    _IngressQECNThresh_Type()
)
ingressQECNThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressQECNThresh.setStatus("current")


class _IngressQDEThresh_Type(Integer32):
    """Custom type ingressQDEThresh based on Integer32"""
    defaultValue = 32767

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_IngressQDEThresh_Type.__name__ = "Integer32"
_IngressQDEThresh_Object = MibTableColumn
ingressQDEThresh = _IngressQDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 8),
    _IngressQDEThresh_Type()
)
ingressQDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressQDEThresh.setStatus("current")


class _EgressQDepth_Type(Integer32):
    """Custom type egressQDepth based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_EgressQDepth_Type.__name__ = "Integer32"
_EgressQDepth_Object = MibTableColumn
egressQDepth = _EgressQDepth_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 9),
    _EgressQDepth_Type()
)
egressQDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressQDepth.setStatus("current")


class _EgressQDEThresh_Type(Integer32):
    """Custom type egressQDEThresh based on Integer32"""
    defaultValue = 32767

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_EgressQDEThresh_Type.__name__ = "Integer32"
_EgressQDEThresh_Object = MibTableColumn
egressQDEThresh = _EgressQDEThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 10),
    _EgressQDEThresh_Type()
)
egressQDEThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressQDEThresh.setStatus("current")


class _EgressQECNThresh_Type(Integer32):
    """Custom type egressQECNThresh based on Integer32"""
    defaultValue = 6553

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_EgressQECNThresh_Type.__name__ = "Integer32"
_EgressQECNThresh_Object = MibTableColumn
egressQECNThresh = _EgressQECNThresh_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 11),
    _EgressQECNThresh_Type()
)
egressQECNThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressQECNThresh.setStatus("current")


class _DeTaggingEnable_Type(Integer32):
    """Custom type deTaggingEnable based on Integer32"""
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


_DeTaggingEnable_Type.__name__ = "Integer32"
_DeTaggingEnable_Object = MibTableColumn
deTaggingEnable = _DeTaggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 12),
    _DeTaggingEnable_Type()
)
deTaggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deTaggingEnable.setStatus("current")


class _Cir_Type(Integer32):
    """Custom type cir based on Integer32"""
    defaultValue = 2400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_Cir_Type.__name__ = "Integer32"
_Cir_Object = MibTableColumn
cir = _Cir_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 13),
    _Cir_Type()
)
cir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cir.setStatus("current")
if mibBuilder.loadTexts:
    cir.setUnits("bps")


class _Bc_Type(Integer32):
    """Custom type bc based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_Bc_Type.__name__ = "Integer32"
_Bc_Object = MibTableColumn
bc = _Bc_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 14),
    _Bc_Type()
)
bc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bc.setStatus("current")
if mibBuilder.loadTexts:
    bc.setUnits("bytes")


class _Be_Type(Integer32):
    """Custom type be based on Integer32"""
    defaultValue = 5100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_Be_Type.__name__ = "Integer32"
_Be_Object = MibTableColumn
be = _Be_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 15),
    _Be_Type()
)
be.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    be.setStatus("current")
if mibBuilder.loadTexts:
    be.setUnits("bytes")


class _Ibs_Type(Integer32):
    """Custom type ibs based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2097151),
    )


_Ibs_Type.__name__ = "Integer32"
_Ibs_Object = MibTableColumn
ibs = _Ibs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 16),
    _Ibs_Type()
)
ibs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ibs.setStatus("current")


class _ForeSightEnable_Type(Integer32):
    """Custom type foreSightEnable based on Integer32"""
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


_ForeSightEnable_Type.__name__ = "Integer32"
_ForeSightEnable_Object = MibTableColumn
foreSightEnable = _ForeSightEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 17),
    _ForeSightEnable_Type()
)
foreSightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    foreSightEnable.setStatus("current")


class _Qir_Type(Integer32):
    """Custom type qir based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 6400000),
    )


_Qir_Type.__name__ = "Integer32"
_Qir_Object = MibTableColumn
qir = _Qir_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 18),
    _Qir_Type()
)
qir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qir.setStatus("current")
if mibBuilder.loadTexts:
    qir.setUnits("fastpackets-per-second")


class _Mir_Type(Integer32):
    """Custom type mir based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 6400000),
    )


_Mir_Type.__name__ = "Integer32"
_Mir_Object = MibTableColumn
mir = _Mir_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 19),
    _Mir_Type()
)
mir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mir.setStatus("current")
if mibBuilder.loadTexts:
    mir.setUnits("fastpackets-per-second")


class _Pir_Type(Integer32):
    """Custom type pir based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 6400000),
    )


_Pir_Type.__name__ = "Integer32"
_Pir_Object = MibTableColumn
pir = _Pir_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 20),
    _Pir_Type()
)
pir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pir.setStatus("current")
if mibBuilder.loadTexts:
    pir.setUnits("fastpackets-per-second")


class _ChanLocRmtLpbkState_Type(Integer32):
    """Custom type chanLocRmtLpbkState based on Integer32"""
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


_ChanLocRmtLpbkState_Type.__name__ = "Integer32"
_ChanLocRmtLpbkState_Object = MibTableColumn
chanLocRmtLpbkState = _ChanLocRmtLpbkState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 21),
    _ChanLocRmtLpbkState_Type()
)
chanLocRmtLpbkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanLocRmtLpbkState.setStatus("current")


class _ChanTestType_Type(Integer32):
    """Custom type chanTestType based on Integer32"""
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
        *(("notest", 3),
          ("testcon", 1),
          ("testdelay", 2))
    )


_ChanTestType_Type.__name__ = "Integer32"
_ChanTestType_Object = MibTableColumn
chanTestType = _ChanTestType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 22),
    _ChanTestType_Type()
)
chanTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanTestType.setStatus("current")


class _ChanTestState_Type(Integer32):
    """Custom type chanTestState based on Integer32"""
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
        *(("failed", 2),
          ("inprogress", 3),
          ("notinprogress", 4),
          ("passed", 1))
    )


_ChanTestState_Type.__name__ = "Integer32"
_ChanTestState_Object = MibTableColumn
chanTestState = _ChanTestState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 23),
    _ChanTestState_Type()
)
chanTestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanTestState.setStatus("current")


class _ChanRTDResult_Type(Integer32):
    """Custom type chanRTDResult based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChanRTDResult_Type.__name__ = "Integer32"
_ChanRTDResult_Object = MibTableColumn
chanRTDResult = _ChanRTDResult_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 24),
    _ChanRTDResult_Type()
)
chanRTDResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanRTDResult.setStatus("current")


class _ChanType_Type(Integer32):
    """Custom type chanType based on Integer32"""
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
        *(("frFUNI", 4),
          ("frForward", 5),
          ("frNIW", 1),
          ("frNIWReplace", 6),
          ("frSIW-translate", 3),
          ("frSIW-transparent", 2))
    )


_ChanType_Type.__name__ = "Integer32"
_ChanType_Object = MibTableColumn
chanType = _ChanType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 25),
    _ChanType_Type()
)
chanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanType.setStatus("current")


class _ChanFECNconfig_Type(Integer32):
    """Custom type chanFECNconfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapEFCI", 1),
          ("setEFCIzero", 2))
    )


_ChanFECNconfig_Type.__name__ = "Integer32"
_ChanFECNconfig_Object = MibTableColumn
chanFECNconfig = _ChanFECNconfig_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 26),
    _ChanFECNconfig_Type()
)
chanFECNconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanFECNconfig.setStatus("current")


class _ChanDEtoCLPmap_Type(Integer32):
    """Custom type chanDEtoCLPmap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mapCLP", 1),
          ("setCLPone", 3),
          ("setCLPzero", 2))
    )


_ChanDEtoCLPmap_Type.__name__ = "Integer32"
_ChanDEtoCLPmap_Object = MibTableColumn
chanDEtoCLPmap = _ChanDEtoCLPmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 27),
    _ChanDEtoCLPmap_Type()
)
chanDEtoCLPmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanDEtoCLPmap.setStatus("current")


class _ChanCLPtoDEmap_Type(Integer32):
    """Custom type chanCLPtoDEmap based on Integer32"""
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
        *(("ignoreCLP", 4),
          ("mapDE", 1),
          ("setDEone", 3),
          ("setDEzero", 2))
    )


_ChanCLPtoDEmap_Type.__name__ = "Integer32"
_ChanCLPtoDEmap_Object = MibTableColumn
chanCLPtoDEmap = _ChanCLPtoDEmap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 28),
    _ChanCLPtoDEmap_Type()
)
chanCLPtoDEmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanCLPtoDEmap.setStatus("current")


class _ChanIngrPercentUtil_Type(Integer32):
    """Custom type chanIngrPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChanIngrPercentUtil_Type.__name__ = "Integer32"
_ChanIngrPercentUtil_Object = MibTableColumn
chanIngrPercentUtil = _ChanIngrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 29),
    _ChanIngrPercentUtil_Type()
)
chanIngrPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanIngrPercentUtil.setStatus("current")
if mibBuilder.loadTexts:
    chanIngrPercentUtil.setUnits("percentage")


class _ChanEgrPercentUtil_Type(Integer32):
    """Custom type chanEgrPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ChanEgrPercentUtil_Type.__name__ = "Integer32"
_ChanEgrPercentUtil_Object = MibTableColumn
chanEgrPercentUtil = _ChanEgrPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 30),
    _ChanEgrPercentUtil_Type()
)
chanEgrPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanEgrPercentUtil.setStatus("current")
if mibBuilder.loadTexts:
    chanEgrPercentUtil.setUnits("percentage")


class _ChanEgrSrvRate_Type(Integer32):
    """Custom type chanEgrSrvRate based on Integer32"""
    defaultValue = 2400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 52000000),
    )


_ChanEgrSrvRate_Type.__name__ = "Integer32"
_ChanEgrSrvRate_Object = MibTableColumn
chanEgrSrvRate = _ChanEgrSrvRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 31),
    _ChanEgrSrvRate_Type()
)
chanEgrSrvRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanEgrSrvRate.setStatus("current")


class _ChanOvrSubOvrRide_Type(Integer32):
    """Custom type chanOvrSubOvrRide based on Integer32"""
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


_ChanOvrSubOvrRide_Type.__name__ = "Integer32"
_ChanOvrSubOvrRide_Object = MibTableColumn
chanOvrSubOvrRide = _ChanOvrSubOvrRide_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 32),
    _ChanOvrSubOvrRide_Type()
)
chanOvrSubOvrRide.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanOvrSubOvrRide.setStatus("current")


class _ChanFrConnType_Type(Integer32):
    """Custom type chanFrConnType based on Integer32"""
    defaultValue = 1

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
        *(("par", 4),
          ("pnni", 5),
          ("pvc", 1),
          ("spvc", 3),
          ("svc", 2),
          ("tag", 6))
    )


_ChanFrConnType_Type.__name__ = "Integer32"
_ChanFrConnType_Object = MibTableColumn
chanFrConnType = _ChanFrConnType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 33),
    _ChanFrConnType_Type()
)
chanFrConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanFrConnType.setStatus("current")
_FrCDRNumber_Type = Integer32
_FrCDRNumber_Object = MibTableColumn
frCDRNumber = _FrCDRNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 34),
    _FrCDRNumber_Type()
)
frCDRNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frCDRNumber.setStatus("current")


class _FrLocalVpi_Type(Integer32):
    """Custom type frLocalVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLocalVpi_Type.__name__ = "Integer32"
_FrLocalVpi_Object = MibTableColumn
frLocalVpi = _FrLocalVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 35),
    _FrLocalVpi_Type()
)
frLocalVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLocalVpi.setStatus("current")


class _FrLocalVci_Type(Integer32):
    """Custom type frLocalVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrLocalVci_Type.__name__ = "Integer32"
_FrLocalVci_Object = MibTableColumn
frLocalVci = _FrLocalVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 36),
    _FrLocalVci_Type()
)
frLocalVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frLocalVci.setStatus("current")


class _FrLocalNSAP_Type(OctetString):
    """Custom type frLocalNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FrLocalNSAP_Type.__name__ = "OctetString"
_FrLocalNSAP_Object = MibTableColumn
frLocalNSAP = _FrLocalNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 37),
    _FrLocalNSAP_Type()
)
frLocalNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLocalNSAP.setStatus("current")


class _FrRemoteVpi_Type(Integer32):
    """Custom type frRemoteVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrRemoteVpi_Type.__name__ = "Integer32"
_FrRemoteVpi_Object = MibTableColumn
frRemoteVpi = _FrRemoteVpi_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 38),
    _FrRemoteVpi_Type()
)
frRemoteVpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frRemoteVpi.setStatus("current")


class _FrRemoteVci_Type(Integer32):
    """Custom type frRemoteVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrRemoteVci_Type.__name__ = "Integer32"
_FrRemoteVci_Object = MibTableColumn
frRemoteVci = _FrRemoteVci_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 39),
    _FrRemoteVci_Type()
)
frRemoteVci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frRemoteVci.setStatus("current")


class _FrRemoteNSAP_Type(OctetString):
    """Custom type frRemoteNSAP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_FrRemoteNSAP_Type.__name__ = "OctetString"
_FrRemoteNSAP_Object = MibTableColumn
frRemoteNSAP = _FrRemoteNSAP_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 40),
    _FrRemoteNSAP_Type()
)
frRemoteNSAP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frRemoteNSAP.setStatus("current")


class _FrMastership_Type(Integer32):
    """Custom type frMastership based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("unknown", 3))
    )


_FrMastership_Type.__name__ = "Integer32"
_FrMastership_Object = MibTableColumn
frMastership = _FrMastership_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 41),
    _FrMastership_Type()
)
frMastership.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMastership.setStatus("current")


class _FrVpcFlag_Type(Integer32):
    """Custom type frVpcFlag based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vcc", 2),
          ("vpc", 1))
    )


_FrVpcFlag_Type.__name__ = "Integer32"
_FrVpcFlag_Object = MibTableColumn
frVpcFlag = _FrVpcFlag_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 42),
    _FrVpcFlag_Type()
)
frVpcFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frVpcFlag.setStatus("current")


class _FrConnServiceType_Type(Integer32):
    """Custom type frConnServiceType based on Integer32"""
    defaultValue = 5

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
              32)
        )
    )
    namedValues = NamedValues(
        *(("abrfst", 7),
          ("abrstd", 6),
          ("atfr", 5),
          ("cbr", 1),
          ("cbr1", 21),
          ("cbr2", 31),
          ("cbr3", 32),
          ("notUsed", 3),
          ("stdabr", 30),
          ("ubr", 4),
          ("ubr1", 28),
          ("ubr2", 29),
          ("vbr", 2),
          ("vbr1nrt", 25),
          ("vbr1rt", 22),
          ("vbr2nrt", 26),
          ("vbr2rt", 23),
          ("vbr3nrt", 27),
          ("vbr3rt", 24),
          ("vbrrt", 8))
    )


_FrConnServiceType_Type.__name__ = "Integer32"
_FrConnServiceType_Object = MibTableColumn
frConnServiceType = _FrConnServiceType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 43),
    _FrConnServiceType_Type()
)
frConnServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnServiceType.setStatus("current")


class _FrRoutingPriority_Type(Integer32):
    """Custom type frRoutingPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FrRoutingPriority_Type.__name__ = "Integer32"
_FrRoutingPriority_Object = MibTableColumn
frRoutingPriority = _FrRoutingPriority_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 44),
    _FrRoutingPriority_Type()
)
frRoutingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frRoutingPriority.setStatus("current")


class _FrMaxCost_Type(Integer32):
    """Custom type frMaxCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrMaxCost_Type.__name__ = "Integer32"
_FrMaxCost_Object = MibTableColumn
frMaxCost = _FrMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 45),
    _FrMaxCost_Type()
)
frMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frMaxCost.setStatus("current")


class _FrRestrictTrunkType_Type(Integer32):
    """Custom type frRestrictTrunkType based on Integer32"""
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
        *(("norestriction", 1),
          ("sateliteTrunk", 3),
          ("terrestrialTrunk", 2))
    )


_FrRestrictTrunkType_Type.__name__ = "Integer32"
_FrRestrictTrunkType_Object = MibTableColumn
frRestrictTrunkType = _FrRestrictTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 46),
    _FrRestrictTrunkType_Type()
)
frRestrictTrunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frRestrictTrunkType.setStatus("current")
_FrConnPCR_Type = Integer32
_FrConnPCR_Object = MibTableColumn
frConnPCR = _FrConnPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 47),
    _FrConnPCR_Type()
)
frConnPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnPCR.setStatus("current")
_FrConnRemotePCR_Type = Integer32
_FrConnRemotePCR_Object = MibTableColumn
frConnRemotePCR = _FrConnRemotePCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 48),
    _FrConnRemotePCR_Type()
)
frConnRemotePCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnRemotePCR.setStatus("current")
_FrConnMCR_Type = Integer32
_FrConnMCR_Object = MibTableColumn
frConnMCR = _FrConnMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 49),
    _FrConnMCR_Type()
)
frConnMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnMCR.setStatus("current")
_FrConnRemoteMCR_Type = Integer32
_FrConnRemoteMCR_Object = MibTableColumn
frConnRemoteMCR = _FrConnRemoteMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 50),
    _FrConnRemoteMCR_Type()
)
frConnRemoteMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnRemoteMCR.setStatus("current")


class _FrConnPercentUtil_Type(Integer32):
    """Custom type frConnPercentUtil based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrConnPercentUtil_Type.__name__ = "Integer32"
_FrConnPercentUtil_Object = MibTableColumn
frConnPercentUtil = _FrConnPercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 51),
    _FrConnPercentUtil_Type()
)
frConnPercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnPercentUtil.setStatus("current")


class _FrConnRemotePercentUtil_Type(Integer32):
    """Custom type frConnRemotePercentUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FrConnRemotePercentUtil_Type.__name__ = "Integer32"
_FrConnRemotePercentUtil_Object = MibTableColumn
frConnRemotePercentUtil = _FrConnRemotePercentUtil_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 52),
    _FrConnRemotePercentUtil_Type()
)
frConnRemotePercentUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnRemotePercentUtil.setStatus("current")


class _FrConnForeSightEnable_Type(Integer32):
    """Custom type frConnForeSightEnable based on Integer32"""
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


_FrConnForeSightEnable_Type.__name__ = "Integer32"
_FrConnForeSightEnable_Object = MibTableColumn
frConnForeSightEnable = _FrConnForeSightEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 53),
    _FrConnForeSightEnable_Type()
)
frConnForeSightEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnForeSightEnable.setStatus("current")


class _FrConnFGCRAEnable_Type(Integer32):
    """Custom type frConnFGCRAEnable based on Integer32"""
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


_FrConnFGCRAEnable_Type.__name__ = "Integer32"
_FrConnFGCRAEnable_Object = MibTableColumn
frConnFGCRAEnable = _FrConnFGCRAEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 54),
    _FrConnFGCRAEnable_Type()
)
frConnFGCRAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnFGCRAEnable.setStatus("current")


class _ChanServType_Type(Integer32):
    """Custom type chanServType based on Integer32"""
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
        *(("aBR", 4),
          ("highpriority", 1),
          ("nrtVBR", 3),
          ("queue6", 6),
          ("queue7", 7),
          ("queue8", 8),
          ("rtVBR", 2),
          ("stdABR", 9),
          ("uBR", 5))
    )


_ChanServType_Type.__name__ = "Integer32"
_ChanServType_Object = MibTableColumn
chanServType = _ChanServType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 55),
    _ChanServType_Type()
)
chanServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanServType.setStatus("current")


class _ChanServiceRateOverride_Type(Integer32):
    """Custom type chanServiceRateOverride based on Integer32"""
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


_ChanServiceRateOverride_Type.__name__ = "Integer32"
_ChanServiceRateOverride_Object = MibTableColumn
chanServiceRateOverride = _ChanServiceRateOverride_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 56),
    _ChanServiceRateOverride_Type()
)
chanServiceRateOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanServiceRateOverride.setStatus("current")


class _ChanServiceRate_Type(Integer32):
    """Custom type chanServiceRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(160, 6400000),
    )


_ChanServiceRate_Type.__name__ = "Integer32"
_ChanServiceRate_Object = MibTableColumn
chanServiceRate = _ChanServiceRate_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 57),
    _ChanServiceRate_Type()
)
chanServiceRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanServiceRate.setStatus("current")


class _ZeroCirConEir_Type(Integer32):
    """Custom type zeroCirConEir based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 52000000),
    )


_ZeroCirConEir_Type.__name__ = "Integer32"
_ZeroCirConEir_Object = MibTableColumn
zeroCirConEir = _ZeroCirConEir_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 58),
    _ZeroCirConEir_Type()
)
zeroCirConEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zeroCirConEir.setStatus("current")


class _ChanReroute_Type(Integer32):
    """Custom type chanReroute based on Integer32"""
    defaultValue = 2

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


_ChanReroute_Type.__name__ = "Integer32"
_ChanReroute_Object = MibTableColumn
chanReroute = _ChanReroute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 59),
    _ChanReroute_Type()
)
chanReroute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chanReroute.setStatus("current")
_FrConnSCR_Type = Integer32
_FrConnSCR_Object = MibTableColumn
frConnSCR = _FrConnSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 60),
    _FrConnSCR_Type()
)
frConnSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnSCR.setStatus("current")
_FrConnRemoteSCR_Type = Integer32
_FrConnRemoteSCR_Object = MibTableColumn
frConnRemoteSCR = _FrConnRemoteSCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 61),
    _FrConnRemoteSCR_Type()
)
frConnRemoteSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnRemoteSCR.setStatus("current")


class _FrConnTemplateId_Type(Integer32):
    """Custom type frConnTemplateId based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17),
    )


_FrConnTemplateId_Type.__name__ = "Integer32"
_FrConnTemplateId_Object = MibTableColumn
frConnTemplateId = _FrConnTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 62),
    _FrConnTemplateId_Type()
)
frConnTemplateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnTemplateId.setStatus("current")


class _FrConnAdminStatus_Type(Integer32):
    """Custom type frConnAdminStatus based on Integer32"""
    defaultValue = 2

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


_FrConnAdminStatus_Type.__name__ = "Integer32"
_FrConnAdminStatus_Object = MibTableColumn
frConnAdminStatus = _FrConnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 63),
    _FrConnAdminStatus_Type()
)
frConnAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnAdminStatus.setStatus("current")
_FrChanCnfChangeCount_Type = Counter32
_FrChanCnfChangeCount_Object = MibTableColumn
frChanCnfChangeCount = _FrChanCnfChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 64),
    _FrChanCnfChangeCount_Type()
)
frChanCnfChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frChanCnfChangeCount.setStatus("current")


class _FrChanCnfIgnoreIncomingDE_Type(Integer32):
    """Custom type frChanCnfIgnoreIncomingDE based on Integer32"""
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


_FrChanCnfIgnoreIncomingDE_Type.__name__ = "Integer32"
_FrChanCnfIgnoreIncomingDE_Object = MibTableColumn
frChanCnfIgnoreIncomingDE = _FrChanCnfIgnoreIncomingDE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 65),
    _FrChanCnfIgnoreIncomingDE_Type()
)
frChanCnfIgnoreIncomingDE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanCnfIgnoreIncomingDE.setStatus("current")


class _FrChanOamCCEnable_Type(Integer32):
    """Custom type frChanOamCCEnable based on Integer32"""
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


_FrChanOamCCEnable_Type.__name__ = "Integer32"
_FrChanOamCCEnable_Object = MibTableColumn
frChanOamCCEnable = _FrChanOamCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 66),
    _FrChanOamCCEnable_Type()
)
frChanOamCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanOamCCEnable.setStatus("current")


class _FrChanStatsEnable_Type(Integer32):
    """Custom type frChanStatsEnable based on Integer32"""
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


_FrChanStatsEnable_Type.__name__ = "Integer32"
_FrChanStatsEnable_Object = MibTableColumn
frChanStatsEnable = _FrChanStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 67),
    _FrChanStatsEnable_Type()
)
frChanStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanStatsEnable.setStatus("current")


class _FrChanLocalLpbkEnable_Type(Integer32):
    """Custom type frChanLocalLpbkEnable based on Integer32"""
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


_FrChanLocalLpbkEnable_Type.__name__ = "Integer32"
_FrChanLocalLpbkEnable_Object = MibTableColumn
frChanLocalLpbkEnable = _FrChanLocalLpbkEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 68),
    _FrChanLocalLpbkEnable_Type()
)
frChanLocalLpbkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanLocalLpbkEnable.setStatus("current")


class _FrChanUpcEnable_Type(Integer32):
    """Custom type frChanUpcEnable based on Integer32"""
    defaultValue = 1

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


_FrChanUpcEnable_Type.__name__ = "Integer32"
_FrChanUpcEnable_Object = MibTableColumn
frChanUpcEnable = _FrChanUpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 69),
    _FrChanUpcEnable_Type()
)
frChanUpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanUpcEnable.setStatus("current")


class _FrChanSlaveType_Type(Integer32):
    """Custom type frChanSlaveType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonPersistentSlave", 2),
          ("persistentSlave", 1))
    )


_FrChanSlaveType_Type.__name__ = "Integer32"
_FrChanSlaveType_Object = MibTableColumn
frChanSlaveType = _FrChanSlaveType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 70),
    _FrChanSlaveType_Type()
)
frChanSlaveType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanSlaveType.setStatus("current")


class _FrConnRemoteMBS_Type(Integer32):
    """Custom type frConnRemoteMBS based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000000),
    )


_FrConnRemoteMBS_Type.__name__ = "Integer32"
_FrConnRemoteMBS_Object = MibTableColumn
frConnRemoteMBS = _FrConnRemoteMBS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 71),
    _FrConnRemoteMBS_Type()
)
frConnRemoteMBS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frConnRemoteMBS.setStatus("current")


class _FrChanPrefRouteId_Type(Integer32):
    """Custom type frChanPrefRouteId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FrChanPrefRouteId_Type.__name__ = "Integer32"
_FrChanPrefRouteId_Object = MibTableColumn
frChanPrefRouteId = _FrChanPrefRouteId_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 72),
    _FrChanPrefRouteId_Type()
)
frChanPrefRouteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanPrefRouteId.setStatus("current")


class _FrChanDirectRoute_Type(TruthValue):
    """Custom type frChanDirectRoute based on TruthValue"""


_FrChanDirectRoute_Object = MibTableColumn
frChanDirectRoute = _FrChanDirectRoute_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 1, 1, 73),
    _FrChanDirectRoute_Type()
)
frChanDirectRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frChanDirectRoute.setStatus("current")


class _ChanNumNextAvailable_Type(Integer32):
    """Custom type chanNumNextAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2147483647),
    )


_ChanNumNextAvailable_Type.__name__ = "Integer32"
_ChanNumNextAvailable_Object = MibScalar
chanNumNextAvailable = _ChanNumNextAvailable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 2),
    _ChanNumNextAvailable_Type()
)
chanNumNextAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanNumNextAvailable.setStatus("current")
_FrstdABRCnfGrpTable_Object = MibTable
frstdABRCnfGrpTable = _FrstdABRCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3)
)
if mibBuilder.loadTexts:
    frstdABRCnfGrpTable.setStatus("current")
_FrstdABRCnfGrpEntry_Object = MibTableRow
frstdABRCnfGrpEntry = _FrstdABRCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1)
)
frstdABRCnfGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-MIB", "frstdABRcnfChanNum"),
)
if mibBuilder.loadTexts:
    frstdABRCnfGrpEntry.setStatus("current")


class _FrstdABRcnfChanNum_Type(Integer32):
    """Custom type frstdABRcnfChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FrstdABRcnfChanNum_Type.__name__ = "Integer32"
_FrstdABRcnfChanNum_Object = MibTableColumn
frstdABRcnfChanNum = _FrstdABRcnfChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 1),
    _FrstdABRcnfChanNum_Type()
)
frstdABRcnfChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frstdABRcnfChanNum.setStatus("current")


class _FrstdABRTBE_Type(Integer32):
    """Custom type frstdABRTBE based on Integer32"""
    defaultValue = 16777215

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FrstdABRTBE_Type.__name__ = "Integer32"
_FrstdABRTBE_Object = MibTableColumn
frstdABRTBE = _FrstdABRTBE_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 2),
    _FrstdABRTBE_Type()
)
frstdABRTBE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRTBE.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRTBE.setUnits("cells")


class _FrstdABRFRTT_Type(Integer32):
    """Custom type frstdABRFRTT based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16700),
    )


_FrstdABRFRTT_Type.__name__ = "Integer32"
_FrstdABRFRTT_Object = MibTableColumn
frstdABRFRTT = _FrstdABRFRTT_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 3),
    _FrstdABRFRTT_Type()
)
frstdABRFRTT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRFRTT.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRFRTT.setUnits("milli-seconds")


class _FrstdABRRDF_Type(Integer32):
    """Custom type frstdABRRDF based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_FrstdABRRDF_Type.__name__ = "Integer32"
_FrstdABRRDF_Object = MibTableColumn
frstdABRRDF = _FrstdABRRDF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 4),
    _FrstdABRRDF_Type()
)
frstdABRRDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRRDF.setStatus("current")


class _FrstdABRRIF_Type(Integer32):
    """Custom type frstdABRRIF based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32768),
    )


_FrstdABRRIF_Type.__name__ = "Integer32"
_FrstdABRRIF_Object = MibTableColumn
frstdABRRIF = _FrstdABRRIF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 5),
    _FrstdABRRIF_Type()
)
frstdABRRIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRRIF.setStatus("current")


class _FrstdABRNrm_Type(Integer32):
    """Custom type frstdABRNrm based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 256),
    )


_FrstdABRNrm_Type.__name__ = "Integer32"
_FrstdABRNrm_Object = MibTableColumn
frstdABRNrm = _FrstdABRNrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 6),
    _FrstdABRNrm_Type()
)
frstdABRNrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRNrm.setStatus("current")


class _FrstdABRTrm_Type(Integer32):
    """Custom type frstdABRTrm based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 255),
    )


_FrstdABRTrm_Type.__name__ = "Integer32"
_FrstdABRTrm_Object = MibTableColumn
frstdABRTrm = _FrstdABRTrm_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 7),
    _FrstdABRTrm_Type()
)
frstdABRTrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRTrm.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRTrm.setUnits("milli-seconds")


class _FrstdABRCDF_Type(Integer32):
    """Custom type frstdABRCDF based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_FrstdABRCDF_Type.__name__ = "Integer32"
_FrstdABRCDF_Object = MibTableColumn
frstdABRCDF = _FrstdABRCDF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 8),
    _FrstdABRCDF_Type()
)
frstdABRCDF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRCDF.setStatus("current")


class _FrstdABRADTF_Type(Integer32):
    """Custom type frstdABRADTF based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10230),
    )


_FrstdABRADTF_Type.__name__ = "Integer32"
_FrstdABRADTF_Object = MibTableColumn
frstdABRADTF = _FrstdABRADTF_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 9),
    _FrstdABRADTF_Type()
)
frstdABRADTF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRADTF.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRADTF.setUnits("milli-seconds")


class _FrstdABRICR_Type(Integer32):
    """Custom type frstdABRICR based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400000),
    )


_FrstdABRICR_Type.__name__ = "Integer32"
_FrstdABRICR_Object = MibTableColumn
frstdABRICR = _FrstdABRICR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 10),
    _FrstdABRICR_Type()
)
frstdABRICR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRICR.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRICR.setUnits("cells-per-second")


class _FrstdABRMCR_Type(Integer32):
    """Custom type frstdABRMCR based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400000),
    )


_FrstdABRMCR_Type.__name__ = "Integer32"
_FrstdABRMCR_Object = MibTableColumn
frstdABRMCR = _FrstdABRMCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 11),
    _FrstdABRMCR_Type()
)
frstdABRMCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRMCR.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRMCR.setUnits("cells-per-second")


class _FrstdABRPCR_Type(Integer32):
    """Custom type frstdABRPCR based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 400000),
    )


_FrstdABRPCR_Type.__name__ = "Integer32"
_FrstdABRPCR_Object = MibTableColumn
frstdABRPCR = _FrstdABRPCR_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 1, 3, 1, 12),
    _FrstdABRPCR_Type()
)
frstdABRPCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frstdABRPCR.setStatus("current")
if mibBuilder.loadTexts:
    frstdABRPCR.setUnits("cells-per-second")
_FrChanStateGrp_ObjectIdentity = ObjectIdentity
frChanStateGrp = _FrChanStateGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2)
)
_FrChanStateGrpTable_Object = MibTable
frChanStateGrpTable = _FrChanStateGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    frChanStateGrpTable.setStatus("current")
_FrChanStateGrpEntry_Object = MibTableRow
frChanStateGrpEntry = _FrChanStateGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1)
)
frChanStateGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-MIB", "stateChanNum"),
)
if mibBuilder.loadTexts:
    frChanStateGrpEntry.setStatus("current")


class _StateChanNum_Type(Integer32):
    """Custom type stateChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_StateChanNum_Type.__name__ = "Integer32"
_StateChanNum_Object = MibTableColumn
stateChanNum = _StateChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 1),
    _StateChanNum_Type()
)
stateChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stateChanNum.setStatus("current")


class _ChanState_Type(Integer32):
    """Custom type chanState based on Integer32"""
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
        *(("alarm", 3),
          ("failed", 4),
          ("notConfigured", 1),
          ("okay", 2))
    )


_ChanState_Type.__name__ = "Integer32"
_ChanState_Object = MibTableColumn
chanState = _ChanState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 2),
    _ChanState_Type()
)
chanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanState.setStatus("current")


class _XmtAbitState_Type(Integer32):
    """Custom type xmtAbitState based on Integer32"""
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
          ("sendingAequal0", 3),
          ("sendingAequal1", 2))
    )


_XmtAbitState_Type.__name__ = "Integer32"
_XmtAbitState_Object = MibTableColumn
xmtAbitState = _XmtAbitState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 3),
    _XmtAbitState_Type()
)
xmtAbitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtAbitState.setStatus("current")


class _RcvAbitState_Type(Integer32):
    """Custom type rcvAbitState based on Integer32"""
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
          ("rcvingAequal0", 3),
          ("rcvingAequal1", 2))
    )


_RcvAbitState_Type.__name__ = "Integer32"
_RcvAbitState_Object = MibTableColumn
rcvAbitState = _RcvAbitState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 4),
    _RcvAbitState_Type()
)
rcvAbitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvAbitState.setStatus("current")


class _XmtATMState_Type(Integer32):
    """Custom type xmtATMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSending", 1),
          ("sendingAIS", 2),
          ("sendingFERF", 3))
    )


_XmtATMState_Type.__name__ = "Integer32"
_XmtATMState_Object = MibTableColumn
xmtATMState = _XmtATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 5),
    _XmtATMState_Type()
)
xmtATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xmtATMState.setStatus("current")


class _RcvATMState_Type(Integer32):
    """Custom type rcvATMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRcving", 1),
          ("rcvingAIS", 2),
          ("rcvingFERF", 3))
    )


_RcvATMState_Type.__name__ = "Integer32"
_RcvATMState_Object = MibTableColumn
rcvATMState = _RcvATMState_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 6),
    _RcvATMState_Type()
)
rcvATMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvATMState.setStatus("current")


class _ChanStatusBitMap_Type(Integer32):
    """Custom type chanStatusBitMap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ChanStatusBitMap_Type.__name__ = "Integer32"
_ChanStatusBitMap_Object = MibTableColumn
chanStatusBitMap = _ChanStatusBitMap_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 2, 2, 1, 1, 7),
    _ChanStatusBitMap_Type()
)
chanStatusBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chanStatusBitMap.setStatus("current")
_FrEndPtMapGrp_ObjectIdentity = ObjectIdentity
frEndPtMapGrp = _FrEndPtMapGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3)
)
_FrEndPtMapGrpTable_Object = MibTable
frEndPtMapGrpTable = _FrEndPtMapGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    frEndPtMapGrpTable.setStatus("current")
_FrEndPtMapGrpEntry_Object = MibTableRow
frEndPtMapGrpEntry = _FrEndPtMapGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1, 1)
)
frEndPtMapGrpEntry.setIndexNames(
    (0, "CISCO-WAN-FR-CONN-MIB", "endPortNum"),
    (0, "CISCO-WAN-FR-CONN-MIB", "endDLCI"),
)
if mibBuilder.loadTexts:
    frEndPtMapGrpEntry.setStatus("current")


class _EndPortNum_Type(Integer32):
    """Custom type endPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EndPortNum_Type.__name__ = "Integer32"
_EndPortNum_Object = MibTableColumn
endPortNum = _EndPortNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1, 1, 1),
    _EndPortNum_Type()
)
endPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endPortNum.setStatus("current")


class _EndDLCI_Type(Integer32):
    """Custom type endDLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_EndDLCI_Type.__name__ = "Integer32"
_EndDLCI_Object = MibTableColumn
endDLCI = _EndDLCI_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1, 1, 2),
    _EndDLCI_Type()
)
endDLCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endDLCI.setStatus("current")


class _EndChanNum_Type(Integer32):
    """Custom type endChanNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EndChanNum_Type.__name__ = "Integer32"
_EndChanNum_Object = MibTableColumn
endChanNum = _EndChanNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1, 1, 3),
    _EndChanNum_Type()
)
endChanNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endChanNum.setStatus("current")


class _EndLineNum_Type(Integer32):
    """Custom type endLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EndLineNum_Type.__name__ = "Integer32"
_EndLineNum_Object = MibTableColumn
endLineNum = _EndLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 5, 1, 3, 1, 1, 4),
    _EndLineNum_Type()
)
endLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endLineNum.setStatus("current")
_CiscoWanFrConnMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWanFrConnMIBConformance = _CiscoWanFrConnMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2)
)
_CiscoWanFrConnMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWanFrConnMIBGroups = _CiscoWanFrConnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1)
)
_CiscoWanFrConnMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWanFrConnMIBCompliances = _CiscoWanFrConnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 2)
)

# Managed Objects groups

ciscoWanFrConnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 1)
)
ciscoWanFrConnGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "chanNum"),
        ("CISCO-WAN-FR-CONN-MIB", "chanRowStatus"),
        ("CISCO-WAN-FR-CONN-MIB", "chanPortNum"),
        ("CISCO-WAN-FR-CONN-MIB", "dLCI"),
        ("CISCO-WAN-FR-CONN-MIB", "egressQSelect"),
        ("CISCO-WAN-FR-CONN-MIB", "deTaggingEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "cir"),
        ("CISCO-WAN-FR-CONN-MIB", "bc"),
        ("CISCO-WAN-FR-CONN-MIB", "be"),
        ("CISCO-WAN-FR-CONN-MIB", "ibs"),
        ("CISCO-WAN-FR-CONN-MIB", "chanLocRmtLpbkState"),
        ("CISCO-WAN-FR-CONN-MIB", "chanType"),
        ("CISCO-WAN-FR-CONN-MIB", "chanFECNconfig"),
        ("CISCO-WAN-FR-CONN-MIB", "chanDEtoCLPmap"),
        ("CISCO-WAN-FR-CONN-MIB", "chanCLPtoDEmap"),
        ("CISCO-WAN-FR-CONN-MIB", "chanIngrPercentUtil"),
        ("CISCO-WAN-FR-CONN-MIB", "chanEgrPercentUtil"),
        ("CISCO-WAN-FR-CONN-MIB", "chanEgrSrvRate"),
        ("CISCO-WAN-FR-CONN-MIB", "chanOvrSubOvrRide"),
        ("CISCO-WAN-FR-CONN-MIB", "chanFrConnType"),
        ("CISCO-WAN-FR-CONN-MIB", "frCDRNumber"),
        ("CISCO-WAN-FR-CONN-MIB", "frLocalVpi"),
        ("CISCO-WAN-FR-CONN-MIB", "frLocalVci"),
        ("CISCO-WAN-FR-CONN-MIB", "frLocalNSAP"),
        ("CISCO-WAN-FR-CONN-MIB", "frRemoteVpi"),
        ("CISCO-WAN-FR-CONN-MIB", "frRemoteVci"),
        ("CISCO-WAN-FR-CONN-MIB", "frRemoteNSAP"),
        ("CISCO-WAN-FR-CONN-MIB", "frMastership"),
        ("CISCO-WAN-FR-CONN-MIB", "frVpcFlag"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnServiceType"),
        ("CISCO-WAN-FR-CONN-MIB", "frRoutingPriority"),
        ("CISCO-WAN-FR-CONN-MIB", "frMaxCost"),
        ("CISCO-WAN-FR-CONN-MIB", "frRestrictTrunkType"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnPCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnRemotePCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnMCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnRemoteMCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnPercentUtil"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnRemotePercentUtil"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnForeSightEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnFGCRAEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "chanServType"),
        ("CISCO-WAN-FR-CONN-MIB", "chanServiceRateOverride"),
        ("CISCO-WAN-FR-CONN-MIB", "chanServiceRate"),
        ("CISCO-WAN-FR-CONN-MIB", "zeroCirConEir"),
        ("CISCO-WAN-FR-CONN-MIB", "chanReroute"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnSCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnRemoteSCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnTemplateId"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnAdminStatus"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanCnfChangeCount"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanCnfIgnoreIncomingDE"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanOamCCEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanStatsEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanLocalLpbkEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanUpcEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanSlaveType"),
        ("CISCO-WAN-FR-CONN-MIB", "frConnRemoteMBS"),
        ("CISCO-WAN-FR-CONN-MIB", "chanNumNextAvailable"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanPrefRouteId"),
        ("CISCO-WAN-FR-CONN-MIB", "frChanDirectRoute"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnGroup.setStatus("current")

ciscoWanFrConnForesightGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 2)
)
ciscoWanFrConnForesightGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "foreSightEnable"),
        ("CISCO-WAN-FR-CONN-MIB", "qir"),
        ("CISCO-WAN-FR-CONN-MIB", "mir"),
        ("CISCO-WAN-FR-CONN-MIB", "pir"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnForesightGroup.setStatus("current")

ciscoWanFrConnQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 3)
)
ciscoWanFrConnQueueGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "ingressQDepth"),
        ("CISCO-WAN-FR-CONN-MIB", "ingressQDEThresh"),
        ("CISCO-WAN-FR-CONN-MIB", "ingressQECNThresh"),
        ("CISCO-WAN-FR-CONN-MIB", "egressQDepth"),
        ("CISCO-WAN-FR-CONN-MIB", "egressQDEThresh"),
        ("CISCO-WAN-FR-CONN-MIB", "egressQECNThresh"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnQueueGroup.setStatus("current")

ciscoWanFrConnTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 4)
)
ciscoWanFrConnTestGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "chanTestType"),
        ("CISCO-WAN-FR-CONN-MIB", "chanTestState"),
        ("CISCO-WAN-FR-CONN-MIB", "chanRTDResult"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnTestGroup.setStatus("current")

ciscoWanFrConnStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 5)
)
ciscoWanFrConnStateGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "stateChanNum"),
        ("CISCO-WAN-FR-CONN-MIB", "chanState"),
        ("CISCO-WAN-FR-CONN-MIB", "xmtAbitState"),
        ("CISCO-WAN-FR-CONN-MIB", "rcvAbitState"),
        ("CISCO-WAN-FR-CONN-MIB", "xmtATMState"),
        ("CISCO-WAN-FR-CONN-MIB", "rcvATMState"),
        ("CISCO-WAN-FR-CONN-MIB", "chanStatusBitMap"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnStateGroup.setStatus("current")

ciscoWanFrConnEndptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 6)
)
ciscoWanFrConnEndptGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "endPortNum"),
        ("CISCO-WAN-FR-CONN-MIB", "endDLCI"),
        ("CISCO-WAN-FR-CONN-MIB", "endChanNum"),
        ("CISCO-WAN-FR-CONN-MIB", "endLineNum"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnEndptGroup.setStatus("current")

ciscoWanFrConnABRGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 1, 7)
)
ciscoWanFrConnABRGroup.setObjects(
      *(("CISCO-WAN-FR-CONN-MIB", "frstdABRcnfChanNum"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRTBE"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRFRTT"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRRDF"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRRIF"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRNrm"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRTrm"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRCDF"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRADTF"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRICR"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRMCR"),
        ("CISCO-WAN-FR-CONN-MIB", "frstdABRPCR"))
)
if mibBuilder.loadTexts:
    ciscoWanFrConnABRGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWanFrConnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 47, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoWanFrConnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WAN-FR-CONN-MIB",
    **{"frChanCnfGrp": frChanCnfGrp,
       "frChanCnfGrpTable": frChanCnfGrpTable,
       "frChanCnfGrpEntry": frChanCnfGrpEntry,
       "chanNum": chanNum,
       "chanRowStatus": chanRowStatus,
       "chanPortNum": chanPortNum,
       "dLCI": dLCI,
       "egressQSelect": egressQSelect,
       "ingressQDepth": ingressQDepth,
       "ingressQECNThresh": ingressQECNThresh,
       "ingressQDEThresh": ingressQDEThresh,
       "egressQDepth": egressQDepth,
       "egressQDEThresh": egressQDEThresh,
       "egressQECNThresh": egressQECNThresh,
       "deTaggingEnable": deTaggingEnable,
       "cir": cir,
       "bc": bc,
       "be": be,
       "ibs": ibs,
       "foreSightEnable": foreSightEnable,
       "qir": qir,
       "mir": mir,
       "pir": pir,
       "chanLocRmtLpbkState": chanLocRmtLpbkState,
       "chanTestType": chanTestType,
       "chanTestState": chanTestState,
       "chanRTDResult": chanRTDResult,
       "chanType": chanType,
       "chanFECNconfig": chanFECNconfig,
       "chanDEtoCLPmap": chanDEtoCLPmap,
       "chanCLPtoDEmap": chanCLPtoDEmap,
       "chanIngrPercentUtil": chanIngrPercentUtil,
       "chanEgrPercentUtil": chanEgrPercentUtil,
       "chanEgrSrvRate": chanEgrSrvRate,
       "chanOvrSubOvrRide": chanOvrSubOvrRide,
       "chanFrConnType": chanFrConnType,
       "frCDRNumber": frCDRNumber,
       "frLocalVpi": frLocalVpi,
       "frLocalVci": frLocalVci,
       "frLocalNSAP": frLocalNSAP,
       "frRemoteVpi": frRemoteVpi,
       "frRemoteVci": frRemoteVci,
       "frRemoteNSAP": frRemoteNSAP,
       "frMastership": frMastership,
       "frVpcFlag": frVpcFlag,
       "frConnServiceType": frConnServiceType,
       "frRoutingPriority": frRoutingPriority,
       "frMaxCost": frMaxCost,
       "frRestrictTrunkType": frRestrictTrunkType,
       "frConnPCR": frConnPCR,
       "frConnRemotePCR": frConnRemotePCR,
       "frConnMCR": frConnMCR,
       "frConnRemoteMCR": frConnRemoteMCR,
       "frConnPercentUtil": frConnPercentUtil,
       "frConnRemotePercentUtil": frConnRemotePercentUtil,
       "frConnForeSightEnable": frConnForeSightEnable,
       "frConnFGCRAEnable": frConnFGCRAEnable,
       "chanServType": chanServType,
       "chanServiceRateOverride": chanServiceRateOverride,
       "chanServiceRate": chanServiceRate,
       "zeroCirConEir": zeroCirConEir,
       "chanReroute": chanReroute,
       "frConnSCR": frConnSCR,
       "frConnRemoteSCR": frConnRemoteSCR,
       "frConnTemplateId": frConnTemplateId,
       "frConnAdminStatus": frConnAdminStatus,
       "frChanCnfChangeCount": frChanCnfChangeCount,
       "frChanCnfIgnoreIncomingDE": frChanCnfIgnoreIncomingDE,
       "frChanOamCCEnable": frChanOamCCEnable,
       "frChanStatsEnable": frChanStatsEnable,
       "frChanLocalLpbkEnable": frChanLocalLpbkEnable,
       "frChanUpcEnable": frChanUpcEnable,
       "frChanSlaveType": frChanSlaveType,
       "frConnRemoteMBS": frConnRemoteMBS,
       "frChanPrefRouteId": frChanPrefRouteId,
       "frChanDirectRoute": frChanDirectRoute,
       "chanNumNextAvailable": chanNumNextAvailable,
       "frstdABRCnfGrpTable": frstdABRCnfGrpTable,
       "frstdABRCnfGrpEntry": frstdABRCnfGrpEntry,
       "frstdABRcnfChanNum": frstdABRcnfChanNum,
       "frstdABRTBE": frstdABRTBE,
       "frstdABRFRTT": frstdABRFRTT,
       "frstdABRRDF": frstdABRRDF,
       "frstdABRRIF": frstdABRRIF,
       "frstdABRNrm": frstdABRNrm,
       "frstdABRTrm": frstdABRTrm,
       "frstdABRCDF": frstdABRCDF,
       "frstdABRADTF": frstdABRADTF,
       "frstdABRICR": frstdABRICR,
       "frstdABRMCR": frstdABRMCR,
       "frstdABRPCR": frstdABRPCR,
       "frChanStateGrp": frChanStateGrp,
       "frChanStateGrpTable": frChanStateGrpTable,
       "frChanStateGrpEntry": frChanStateGrpEntry,
       "stateChanNum": stateChanNum,
       "chanState": chanState,
       "xmtAbitState": xmtAbitState,
       "rcvAbitState": rcvAbitState,
       "xmtATMState": xmtATMState,
       "rcvATMState": rcvATMState,
       "chanStatusBitMap": chanStatusBitMap,
       "frEndPtMapGrp": frEndPtMapGrp,
       "frEndPtMapGrpTable": frEndPtMapGrpTable,
       "frEndPtMapGrpEntry": frEndPtMapGrpEntry,
       "endPortNum": endPortNum,
       "endDLCI": endDLCI,
       "endChanNum": endChanNum,
       "endLineNum": endLineNum,
       "ciscoWanFrConnMIB": ciscoWanFrConnMIB,
       "ciscoWanFrConnMIBConformance": ciscoWanFrConnMIBConformance,
       "ciscoWanFrConnMIBGroups": ciscoWanFrConnMIBGroups,
       "ciscoWanFrConnGroup": ciscoWanFrConnGroup,
       "ciscoWanFrConnForesightGroup": ciscoWanFrConnForesightGroup,
       "ciscoWanFrConnQueueGroup": ciscoWanFrConnQueueGroup,
       "ciscoWanFrConnTestGroup": ciscoWanFrConnTestGroup,
       "ciscoWanFrConnStateGroup": ciscoWanFrConnStateGroup,
       "ciscoWanFrConnEndptGroup": ciscoWanFrConnEndptGroup,
       "ciscoWanFrConnABRGroup": ciscoWanFrConnABRGroup,
       "ciscoWanFrConnMIBCompliances": ciscoWanFrConnMIBCompliances,
       "ciscoWanFrConnCompliance": ciscoWanFrConnCompliance}
)
