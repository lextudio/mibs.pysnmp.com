# SNMP MIB module (COMPEX-IN3000) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPEX-IN3000
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:50 2024
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

_Compex_ObjectIdentity = ObjectIdentity
compex = _Compex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426)
)
_In3000_ObjectIdentity = ObjectIdentity
in3000 = _In3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1)
)
_HubTypes_ObjectIdentity = ObjectIdentity
hubTypes = _HubTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 1)
)
_Tp3000_ObjectIdentity = ObjectIdentity
tp3000 = _Tp3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 1, 1)
)
_Rp3000_ObjectIdentity = ObjectIdentity
rp3000 = _Rp3000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 1, 2)
)
_ProductInfo_ObjectIdentity = ObjectIdentity
productInfo = _ProductInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 2)
)


class _ProductName_Type(DisplayString):
    """Custom type productName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ProductName_Type.__name__ = "DisplayString"
_ProductName_Object = MibScalar
productName = _ProductName_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 1),
    _ProductName_Type()
)
productName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productName.setStatus("mandatory")


class _ProductVersion_Type(DisplayString):
    """Custom type productVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProductVersion_Type.__name__ = "DisplayString"
_ProductVersion_Object = MibScalar
productVersion = _ProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 2),
    _ProductVersion_Type()
)
productVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productVersion.setStatus("mandatory")


class _ReleasedDate_Type(DisplayString):
    """Custom type releasedDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ReleasedDate_Type.__name__ = "DisplayString"
_ReleasedDate_Object = MibScalar
releasedDate = _ReleasedDate_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 3),
    _ReleasedDate_Type()
)
releasedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    releasedDate.setStatus("mandatory")


class _CompexAddress_Type(DisplayString):
    """Custom type compexAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CompexAddress_Type.__name__ = "DisplayString"
_CompexAddress_Object = MibScalar
compexAddress = _CompexAddress_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 4),
    _CompexAddress_Type()
)
compexAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compexAddress.setStatus("mandatory")


class _CompexPhone_Type(DisplayString):
    """Custom type compexPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CompexPhone_Type.__name__ = "DisplayString"
_CompexPhone_Object = MibScalar
compexPhone = _CompexPhone_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 5),
    _CompexPhone_Type()
)
compexPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compexPhone.setStatus("mandatory")
_CompexImage_Type = OctetString
_CompexImage_Object = MibScalar
compexImage = _CompexImage_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 6),
    _CompexImage_Type()
)
compexImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compexImage.setStatus("mandatory")


class _CompexMyAccess_Type(Integer32):
    """Custom type compexMyAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_CompexMyAccess_Type.__name__ = "Integer32"
_CompexMyAccess_Object = MibScalar
compexMyAccess = _CompexMyAccess_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 7),
    _CompexMyAccess_Type()
)
compexMyAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    compexMyAccess.setStatus("mandatory")
_DevTeamTable_Object = MibTable
devTeamTable = _DevTeamTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 8)
)
if mibBuilder.loadTexts:
    devTeamTable.setStatus("mandatory")
_DevTeamEntry_Object = MibTableRow
devTeamEntry = _DevTeamEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 8, 1)
)
devTeamEntry.setIndexNames(
    (0, "COMPEX-IN3000", "cpId"),
)
if mibBuilder.loadTexts:
    devTeamEntry.setStatus("mandatory")
_CpId_Type = Integer32
_CpId_Object = MibTableColumn
cpId = _CpId_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 8, 1, 1),
    _CpId_Type()
)
cpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpId.setStatus("mandatory")


class _CpName_Type(DisplayString):
    """Custom type cpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CpName_Type.__name__ = "DisplayString"
_CpName_Object = MibTableColumn
cpName = _CpName_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 2, 8, 1, 2),
    _CpName_Type()
)
cpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpName.setStatus("mandatory")
_CommunityInfo_ObjectIdentity = ObjectIdentity
communityInfo = _CommunityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 3)
)
_CommunityTable_Object = MibTable
communityTable = _CommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 3, 1)
)
if mibBuilder.loadTexts:
    communityTable.setStatus("mandatory")
_CommunityEntry_Object = MibTableRow
communityEntry = _CommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 3, 1, 1)
)
communityEntry.setIndexNames(
    (0, "COMPEX-IN3000", "communityInstance"),
)
if mibBuilder.loadTexts:
    communityEntry.setStatus("mandatory")


class _CommunityInstance_Type(Integer32):
    """Custom type communityInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CommunityInstance_Type.__name__ = "Integer32"
_CommunityInstance_Object = MibTableColumn
communityInstance = _CommunityInstance_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 3, 1, 1, 1),
    _CommunityInstance_Type()
)
communityInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    communityInstance.setStatus("mandatory")


class _CommunityString_Type(DisplayString):
    """Custom type communityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CommunityString_Type.__name__ = "DisplayString"
_CommunityString_Object = MibTableColumn
communityString = _CommunityString_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 3, 1, 1, 2),
    _CommunityString_Type()
)
communityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityString.setStatus("mandatory")


class _CommunityCapability_Type(Integer32):
    """Custom type communityCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("clear", 99),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_CommunityCapability_Type.__name__ = "Integer32"
_CommunityCapability_Object = MibTableColumn
communityCapability = _CommunityCapability_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 3, 1, 1, 3),
    _CommunityCapability_Type()
)
communityCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    communityCapability.setStatus("mandatory")
_TrapInfo_ObjectIdentity = ObjectIdentity
trapInfo = _TrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 4)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 4, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 4, 1, 1)
)
trapEntry.setIndexNames(
    (0, "COMPEX-IN3000", "trapDest"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")
_TrapDest_Type = IpAddress
_TrapDest_Object = MibTableColumn
trapDest = _TrapDest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 4, 1, 1, 1),
    _TrapDest_Type()
)
trapDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDest.setStatus("mandatory")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 2),
          ("ok", 1))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 4, 1, 1, 2),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("mandatory")
_In3000StatsRptr_ObjectIdentity = ObjectIdentity
in3000StatsRptr = _In3000StatsRptr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 5)
)
_RptrFifoColls_Type = Counter32
_RptrFifoColls_Object = MibScalar
rptrFifoColls = _RptrFifoColls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 1),
    _RptrFifoColls_Type()
)
rptrFifoColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrFifoColls.setStatus("mandatory")
_RptrShortWoPort_Type = Counter32
_RptrShortWoPort_Object = MibScalar
rptrShortWoPort = _RptrShortWoPort_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 2),
    _RptrShortWoPort_Type()
)
rptrShortWoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrShortWoPort.setStatus("mandatory")
_RptrNoStatsDsgntr_Type = Counter32
_RptrNoStatsDsgntr_Object = MibScalar
rptrNoStatsDsgntr = _RptrNoStatsDsgntr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 3),
    _RptrNoStatsDsgntr_Type()
)
rptrNoStatsDsgntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNoStatsDsgntr.setStatus("mandatory")
_RptrInvalidDesgntr_Type = Counter32
_RptrInvalidDesgntr_Object = MibScalar
rptrInvalidDesgntr = _RptrInvalidDesgntr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 4),
    _RptrInvalidDesgntr_Type()
)
rptrInvalidDesgntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInvalidDesgntr.setStatus("mandatory")
_RptrPortIDwoPacket_Type = Counter32
_RptrPortIDwoPacket_Object = MibScalar
rptrPortIDwoPacket = _RptrPortIDwoPacket_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 5),
    _RptrPortIDwoPacket_Type()
)
rptrPortIDwoPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrPortIDwoPacket.setStatus("mandatory")
_RptrOverflows_Type = Counter32
_RptrOverflows_Object = MibScalar
rptrOverflows = _RptrOverflows_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 6),
    _RptrOverflows_Type()
)
rptrOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrOverflows.setStatus("mandatory")
_RptrNoFreeBuffers_Type = Counter32
_RptrNoFreeBuffers_Object = MibScalar
rptrNoFreeBuffers = _RptrNoFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 7),
    _RptrNoFreeBuffers_Type()
)
rptrNoFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNoFreeBuffers.setStatus("mandatory")
_RptrTxTimeouts_Type = Counter32
_RptrTxTimeouts_Object = MibScalar
rptrTxTimeouts = _RptrTxTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 8),
    _RptrTxTimeouts_Type()
)
rptrTxTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrTxTimeouts.setStatus("mandatory")
_RptrNICTxCollisions_Type = Counter32
_RptrNICTxCollisions_Object = MibScalar
rptrNICTxCollisions = _RptrNICTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 9),
    _RptrNICTxCollisions_Type()
)
rptrNICTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNICTxCollisions.setStatus("mandatory")
_RptrNICTxFifoUruns_Type = Counter32
_RptrNICTxFifoUruns_Object = MibScalar
rptrNICTxFifoUruns = _RptrNICTxFifoUruns_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 10),
    _RptrNICTxFifoUruns_Type()
)
rptrNICTxFifoUruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNICTxFifoUruns.setStatus("mandatory")
_RptrNICTxCDHrtbts_Type = Counter32
_RptrNICTxCDHrtbts_Object = MibScalar
rptrNICTxCDHrtbts = _RptrNICTxCDHrtbts_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 11),
    _RptrNICTxCDHrtbts_Type()
)
rptrNICTxCDHrtbts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNICTxCDHrtbts.setStatus("mandatory")
_RptrNICTxOutWinCls_Type = Counter32
_RptrNICTxOutWinCls_Object = MibScalar
rptrNICTxOutWinCls = _RptrNICTxOutWinCls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 12),
    _RptrNICTxOutWinCls_Type()
)
rptrNICTxOutWinCls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNICTxOutWinCls.setStatus("mandatory")
_RptrNICCarrierLost_Type = Counter32
_RptrNICCarrierLost_Object = MibScalar
rptrNICCarrierLost = _RptrNICCarrierLost_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 13),
    _RptrNICCarrierLost_Type()
)
rptrNICCarrierLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrNICCarrierLost.setStatus("mandatory")
_RptrInNoRxBuf_Type = Counter32
_RptrInNoRxBuf_Object = MibScalar
rptrInNoRxBuf = _RptrInNoRxBuf_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 5, 14),
    _RptrInNoRxBuf_Type()
)
rptrInNoRxBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rptrInNoRxBuf.setStatus("mandatory")
_In3000StatsGroup_ObjectIdentity = ObjectIdentity
in3000StatsGroup = _In3000StatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 6)
)
_GroupOctetsTable_Object = MibTable
groupOctetsTable = _GroupOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1)
)
if mibBuilder.loadTexts:
    groupOctetsTable.setStatus("mandatory")
_GroupOctetsEntry_Object = MibTableRow
groupOctetsEntry = _GroupOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1)
)
groupOctetsEntry.setIndexNames(
    (0, "COMPEX-IN3000", "gsoGroupIndex"),
)
if mibBuilder.loadTexts:
    groupOctetsEntry.setStatus("mandatory")
_GsoGroupIndex_Type = Integer32
_GsoGroupIndex_Object = MibTableColumn
gsoGroupIndex = _GsoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 1),
    _GsoGroupIndex_Type()
)
gsoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoGroupIndex.setStatus("mandatory")
_GsoHostOctetsRxOk_Type = Counter32
_GsoHostOctetsRxOk_Object = MibTableColumn
gsoHostOctetsRxOk = _GsoHostOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 2),
    _GsoHostOctetsRxOk_Type()
)
gsoHostOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoHostOctetsRxOk.setStatus("mandatory")
_GsoHostOctetsRxErr_Type = Counter32
_GsoHostOctetsRxErr_Object = MibTableColumn
gsoHostOctetsRxErr = _GsoHostOctetsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 3),
    _GsoHostOctetsRxErr_Type()
)
gsoHostOctetsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoHostOctetsRxErr.setStatus("mandatory")
_GsoOctetsRxOk_Type = Counter32
_GsoOctetsRxOk_Object = MibTableColumn
gsoOctetsRxOk = _GsoOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 4),
    _GsoOctetsRxOk_Type()
)
gsoOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoOctetsRxOk.setStatus("mandatory")
_GsoOctetsRxErr_Type = Counter32
_GsoOctetsRxErr_Object = MibTableColumn
gsoOctetsRxErr = _GsoOctetsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 5),
    _GsoOctetsRxErr_Type()
)
gsoOctetsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoOctetsRxErr.setStatus("mandatory")
_Gsobkt64Ok_Type = Counter32
_Gsobkt64Ok_Object = MibTableColumn
gsobkt64Ok = _Gsobkt64Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 6),
    _Gsobkt64Ok_Type()
)
gsobkt64Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt64Ok.setStatus("mandatory")
_Gsobkt64Err_Type = Counter32
_Gsobkt64Err_Object = MibTableColumn
gsobkt64Err = _Gsobkt64Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 7),
    _Gsobkt64Err_Type()
)
gsobkt64Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt64Err.setStatus("mandatory")
_Gsobkt65to127Ok_Type = Counter32
_Gsobkt65to127Ok_Object = MibTableColumn
gsobkt65to127Ok = _Gsobkt65to127Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 8),
    _Gsobkt65to127Ok_Type()
)
gsobkt65to127Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt65to127Ok.setStatus("mandatory")
_Gsobkt65to127Err_Type = Counter32
_Gsobkt65to127Err_Object = MibTableColumn
gsobkt65to127Err = _Gsobkt65to127Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 9),
    _Gsobkt65to127Err_Type()
)
gsobkt65to127Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt65to127Err.setStatus("mandatory")
_Gsobkt128to255Ok_Type = Counter32
_Gsobkt128to255Ok_Object = MibTableColumn
gsobkt128to255Ok = _Gsobkt128to255Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 10),
    _Gsobkt128to255Ok_Type()
)
gsobkt128to255Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt128to255Ok.setStatus("mandatory")
_Gsobkt128to255Err_Type = Counter32
_Gsobkt128to255Err_Object = MibTableColumn
gsobkt128to255Err = _Gsobkt128to255Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 11),
    _Gsobkt128to255Err_Type()
)
gsobkt128to255Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt128to255Err.setStatus("mandatory")
_Gsobkt256to511Ok_Type = Counter32
_Gsobkt256to511Ok_Object = MibTableColumn
gsobkt256to511Ok = _Gsobkt256to511Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 12),
    _Gsobkt256to511Ok_Type()
)
gsobkt256to511Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt256to511Ok.setStatus("mandatory")
_Gsobkt256to511Err_Type = Counter32
_Gsobkt256to511Err_Object = MibTableColumn
gsobkt256to511Err = _Gsobkt256to511Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 13),
    _Gsobkt256to511Err_Type()
)
gsobkt256to511Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt256to511Err.setStatus("mandatory")
_Gsobkt512to1023Ok_Type = Counter32
_Gsobkt512to1023Ok_Object = MibTableColumn
gsobkt512to1023Ok = _Gsobkt512to1023Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 14),
    _Gsobkt512to1023Ok_Type()
)
gsobkt512to1023Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt512to1023Ok.setStatus("mandatory")
_Gsobkt512to1023Err_Type = Counter32
_Gsobkt512to1023Err_Object = MibTableColumn
gsobkt512to1023Err = _Gsobkt512to1023Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 15),
    _Gsobkt512to1023Err_Type()
)
gsobkt512to1023Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt512to1023Err.setStatus("mandatory")
_Gsobkt1024to1518Ok_Type = Counter32
_Gsobkt1024to1518Ok_Object = MibTableColumn
gsobkt1024to1518Ok = _Gsobkt1024to1518Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 16),
    _Gsobkt1024to1518Ok_Type()
)
gsobkt1024to1518Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt1024to1518Ok.setStatus("mandatory")
_Gsobkt1024to1518Err_Type = Counter32
_Gsobkt1024to1518Err_Object = MibTableColumn
gsobkt1024to1518Err = _Gsobkt1024to1518Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 17),
    _Gsobkt1024to1518Err_Type()
)
gsobkt1024to1518Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsobkt1024to1518Err.setStatus("mandatory")
_GsoRuntPacketsOk_Type = Counter32
_GsoRuntPacketsOk_Object = MibTableColumn
gsoRuntPacketsOk = _GsoRuntPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 18),
    _GsoRuntPacketsOk_Type()
)
gsoRuntPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoRuntPacketsOk.setStatus("mandatory")
_GsoRuntPacketsErr_Type = Counter32
_GsoRuntPacketsErr_Object = MibTableColumn
gsoRuntPacketsErr = _GsoRuntPacketsErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 19),
    _GsoRuntPacketsErr_Type()
)
gsoRuntPacketsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoRuntPacketsErr.setStatus("mandatory")
_GsoPacketsTooBigOk_Type = Counter32
_GsoPacketsTooBigOk_Object = MibTableColumn
gsoPacketsTooBigOk = _GsoPacketsTooBigOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 20),
    _GsoPacketsTooBigOk_Type()
)
gsoPacketsTooBigOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoPacketsTooBigOk.setStatus("mandatory")
_GsoPacketsTooBigErr_Type = Counter32
_GsoPacketsTooBigErr_Object = MibTableColumn
gsoPacketsTooBigErr = _GsoPacketsTooBigErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 1, 1, 21),
    _GsoPacketsTooBigErr_Type()
)
gsoPacketsTooBigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsoPacketsTooBigErr.setStatus("mandatory")
_GroupPacketTable_Object = MibTable
groupPacketTable = _GroupPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2)
)
if mibBuilder.loadTexts:
    groupPacketTable.setStatus("mandatory")
_GroupPacketEntry_Object = MibTableRow
groupPacketEntry = _GroupPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1)
)
groupPacketEntry.setIndexNames(
    (0, "COMPEX-IN3000", "gspGroupIndex"),
)
if mibBuilder.loadTexts:
    groupPacketEntry.setStatus("mandatory")
_GspGroupIndex_Type = Integer32
_GspGroupIndex_Object = MibTableColumn
gspGroupIndex = _GspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 1),
    _GspGroupIndex_Type()
)
gspGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspGroupIndex.setStatus("mandatory")
_GspPacketsRxOk_Type = Counter32
_GspPacketsRxOk_Object = MibTableColumn
gspPacketsRxOk = _GspPacketsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 2),
    _GspPacketsRxOk_Type()
)
gspPacketsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspPacketsRxOk.setStatus("mandatory")
_GspPacketsRxErr_Type = Counter32
_GspPacketsRxErr_Object = MibTableColumn
gspPacketsRxErr = _GspPacketsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 3),
    _GspPacketsRxErr_Type()
)
gspPacketsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspPacketsRxErr.setStatus("mandatory")
_GspPhysicalOk_Type = Counter32
_GspPhysicalOk_Object = MibTableColumn
gspPhysicalOk = _GspPhysicalOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 4),
    _GspPhysicalOk_Type()
)
gspPhysicalOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspPhysicalOk.setStatus("mandatory")
_GspPhysicalErr_Type = Counter32
_GspPhysicalErr_Object = MibTableColumn
gspPhysicalErr = _GspPhysicalErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 5),
    _GspPhysicalErr_Type()
)
gspPhysicalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspPhysicalErr.setStatus("mandatory")
_GspMulticastOk_Type = Counter32
_GspMulticastOk_Object = MibTableColumn
gspMulticastOk = _GspMulticastOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 6),
    _GspMulticastOk_Type()
)
gspMulticastOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspMulticastOk.setStatus("mandatory")
_GspMulticastErr_Type = Counter32
_GspMulticastErr_Object = MibTableColumn
gspMulticastErr = _GspMulticastErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 7),
    _GspMulticastErr_Type()
)
gspMulticastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspMulticastErr.setStatus("mandatory")
_GspBroadcastOk_Type = Counter32
_GspBroadcastOk_Object = MibTableColumn
gspBroadcastOk = _GspBroadcastOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 8),
    _GspBroadcastOk_Type()
)
gspBroadcastOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspBroadcastOk.setStatus("mandatory")
_GspBroadcastErr_Type = Counter32
_GspBroadcastErr_Object = MibTableColumn
gspBroadcastErr = _GspBroadcastErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 9),
    _GspBroadcastErr_Type()
)
gspBroadcastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspBroadcastErr.setStatus("mandatory")
_GspHostPhysicalOk_Type = Counter32
_GspHostPhysicalOk_Object = MibTableColumn
gspHostPhysicalOk = _GspHostPhysicalOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 10),
    _GspHostPhysicalOk_Type()
)
gspHostPhysicalOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspHostPhysicalOk.setStatus("mandatory")
_GspHostPhysicalErr_Type = Counter32
_GspHostPhysicalErr_Object = MibTableColumn
gspHostPhysicalErr = _GspHostPhysicalErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 2, 1, 11),
    _GspHostPhysicalErr_Type()
)
gspHostPhysicalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gspHostPhysicalErr.setStatus("mandatory")
_GroupMiscTable_Object = MibTable
groupMiscTable = _GroupMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3)
)
if mibBuilder.loadTexts:
    groupMiscTable.setStatus("mandatory")
_GroupMiscEntry_Object = MibTableRow
groupMiscEntry = _GroupMiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1)
)
groupMiscEntry.setIndexNames(
    (0, "COMPEX-IN3000", "gsmGroupIndex"),
)
if mibBuilder.loadTexts:
    groupMiscEntry.setStatus("mandatory")
_GsmGroupIndex_Type = Integer32
_GsmGroupIndex_Object = MibTableColumn
gsmGroupIndex = _GsmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 1),
    _GsmGroupIndex_Type()
)
gsmGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmGroupIndex.setStatus("mandatory")
_GsmNumPorts_Type = Integer32
_GsmNumPorts_Object = MibTableColumn
gsmNumPorts = _GsmNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 2),
    _GsmNumPorts_Type()
)
gsmNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmNumPorts.setStatus("mandatory")


class _GsmName_Type(DisplayString):
    """Custom type gsmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_GsmName_Type.__name__ = "DisplayString"
_GsmName_Object = MibTableColumn
gsmName = _GsmName_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 3),
    _GsmName_Type()
)
gsmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gsmName.setStatus("mandatory")


class _GsmType_Type(Integer32):
    """Custom type gsmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rp3000", 2),
          ("tp3000", 1),
          ("unknown", 3))
    )


_GsmType_Type.__name__ = "Integer32"
_GsmType_Object = MibTableColumn
gsmType = _GsmType_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 4),
    _GsmType_Type()
)
gsmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmType.setStatus("mandatory")
_GsmNumLinkUp_Type = Gauge32
_GsmNumLinkUp_Object = MibTableColumn
gsmNumLinkUp = _GsmNumLinkUp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 5),
    _GsmNumLinkUp_Type()
)
gsmNumLinkUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmNumLinkUp.setStatus("mandatory")
_GsmNumLinkPulses_Type = Gauge32
_GsmNumLinkPulses_Object = MibTableColumn
gsmNumLinkPulses = _GsmNumLinkPulses_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 6),
    _GsmNumLinkPulses_Type()
)
gsmNumLinkPulses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmNumLinkPulses.setStatus("mandatory")
_GsmCollisions_Type = Counter32
_GsmCollisions_Object = MibTableColumn
gsmCollisions = _GsmCollisions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 7),
    _GsmCollisions_Type()
)
gsmCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCollisions.setStatus("mandatory")
_GsmLateCollisions_Type = Counter32
_GsmLateCollisions_Object = MibTableColumn
gsmLateCollisions = _GsmLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 8),
    _GsmLateCollisions_Type()
)
gsmLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmLateCollisions.setStatus("mandatory")
_GsmPartitions_Type = Counter32
_GsmPartitions_Object = MibTableColumn
gsmPartitions = _GsmPartitions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 9),
    _GsmPartitions_Type()
)
gsmPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmPartitions.setStatus("mandatory")
_GsmJabbers_Type = Counter32
_GsmJabbers_Object = MibTableColumn
gsmJabbers = _GsmJabbers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 10),
    _GsmJabbers_Type()
)
gsmJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmJabbers.setStatus("mandatory")
_GsmShortFragments_Type = Counter32
_GsmShortFragments_Object = MibTableColumn
gsmShortFragments = _GsmShortFragments_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 11),
    _GsmShortFragments_Type()
)
gsmShortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmShortFragments.setStatus("mandatory")
_GsmCrcFae_Type = Counter32
_GsmCrcFae_Object = MibTableColumn
gsmCrcFae = _GsmCrcFae_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 12),
    _GsmCrcFae_Type()
)
gsmCrcFae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCrcFae.setStatus("mandatory")
_GsmCrc_Type = Counter32
_GsmCrc_Object = MibTableColumn
gsmCrc = _GsmCrc_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 13),
    _GsmCrc_Type()
)
gsmCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmCrc.setStatus("mandatory")
_GsmFifoOverrun_Type = Counter32
_GsmFifoOverrun_Object = MibTableColumn
gsmFifoOverrun = _GsmFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 14),
    _GsmFifoOverrun_Type()
)
gsmFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmFifoOverrun.setStatus("mandatory")
_GsmDeferring_Type = Counter32
_GsmDeferring_Object = MibTableColumn
gsmDeferring = _GsmDeferring_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 6, 3, 1, 15),
    _GsmDeferring_Type()
)
gsmDeferring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmDeferring.setStatus("mandatory")
_In3000StatsPort_ObjectIdentity = ObjectIdentity
in3000StatsPort = _In3000StatsPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 7)
)
_PortOctetsTable_Object = MibTable
portOctetsTable = _PortOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1)
)
if mibBuilder.loadTexts:
    portOctetsTable.setStatus("mandatory")
_PortOctetsEntry_Object = MibTableRow
portOctetsEntry = _PortOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1)
)
portOctetsEntry.setIndexNames(
    (0, "COMPEX-IN3000", "psoGroupIndex"),
    (0, "COMPEX-IN3000", "psoPortIndex"),
)
if mibBuilder.loadTexts:
    portOctetsEntry.setStatus("mandatory")
_PsoGroupIndex_Type = Integer32
_PsoGroupIndex_Object = MibTableColumn
psoGroupIndex = _PsoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 1),
    _PsoGroupIndex_Type()
)
psoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoGroupIndex.setStatus("mandatory")
_PsoPortIndex_Type = Integer32
_PsoPortIndex_Object = MibTableColumn
psoPortIndex = _PsoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 2),
    _PsoPortIndex_Type()
)
psoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoPortIndex.setStatus("mandatory")
_PsoHostOctetsRxOk_Type = Counter32
_PsoHostOctetsRxOk_Object = MibTableColumn
psoHostOctetsRxOk = _PsoHostOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 3),
    _PsoHostOctetsRxOk_Type()
)
psoHostOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoHostOctetsRxOk.setStatus("mandatory")
_PsoHostOctetsRxErr_Type = Counter32
_PsoHostOctetsRxErr_Object = MibTableColumn
psoHostOctetsRxErr = _PsoHostOctetsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 4),
    _PsoHostOctetsRxErr_Type()
)
psoHostOctetsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoHostOctetsRxErr.setStatus("mandatory")
_PsoOctetsRxOk_Type = Counter32
_PsoOctetsRxOk_Object = MibTableColumn
psoOctetsRxOk = _PsoOctetsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 5),
    _PsoOctetsRxOk_Type()
)
psoOctetsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoOctetsRxOk.setStatus("mandatory")
_PsoOctetsRxErr_Type = Counter32
_PsoOctetsRxErr_Object = MibTableColumn
psoOctetsRxErr = _PsoOctetsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 6),
    _PsoOctetsRxErr_Type()
)
psoOctetsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoOctetsRxErr.setStatus("mandatory")
_Psobkt64Ok_Type = Counter32
_Psobkt64Ok_Object = MibTableColumn
psobkt64Ok = _Psobkt64Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 7),
    _Psobkt64Ok_Type()
)
psobkt64Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt64Ok.setStatus("mandatory")
_Psobkt64Err_Type = Counter32
_Psobkt64Err_Object = MibTableColumn
psobkt64Err = _Psobkt64Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 8),
    _Psobkt64Err_Type()
)
psobkt64Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt64Err.setStatus("mandatory")
_Psobkt65to127Ok_Type = Counter32
_Psobkt65to127Ok_Object = MibTableColumn
psobkt65to127Ok = _Psobkt65to127Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 9),
    _Psobkt65to127Ok_Type()
)
psobkt65to127Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt65to127Ok.setStatus("mandatory")
_Psobkt65to127Err_Type = Counter32
_Psobkt65to127Err_Object = MibTableColumn
psobkt65to127Err = _Psobkt65to127Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 10),
    _Psobkt65to127Err_Type()
)
psobkt65to127Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt65to127Err.setStatus("mandatory")
_Psobkt128to255Ok_Type = Counter32
_Psobkt128to255Ok_Object = MibTableColumn
psobkt128to255Ok = _Psobkt128to255Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 11),
    _Psobkt128to255Ok_Type()
)
psobkt128to255Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt128to255Ok.setStatus("mandatory")
_Psobkt128to255Err_Type = Counter32
_Psobkt128to255Err_Object = MibTableColumn
psobkt128to255Err = _Psobkt128to255Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 12),
    _Psobkt128to255Err_Type()
)
psobkt128to255Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt128to255Err.setStatus("mandatory")
_Psobkt256to511Ok_Type = Counter32
_Psobkt256to511Ok_Object = MibTableColumn
psobkt256to511Ok = _Psobkt256to511Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 13),
    _Psobkt256to511Ok_Type()
)
psobkt256to511Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt256to511Ok.setStatus("mandatory")
_Psobkt256to511Err_Type = Counter32
_Psobkt256to511Err_Object = MibTableColumn
psobkt256to511Err = _Psobkt256to511Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 14),
    _Psobkt256to511Err_Type()
)
psobkt256to511Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt256to511Err.setStatus("mandatory")
_Psobkt512to1023Ok_Type = Counter32
_Psobkt512to1023Ok_Object = MibTableColumn
psobkt512to1023Ok = _Psobkt512to1023Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 15),
    _Psobkt512to1023Ok_Type()
)
psobkt512to1023Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt512to1023Ok.setStatus("mandatory")
_Psobkt512to1023Err_Type = Counter32
_Psobkt512to1023Err_Object = MibTableColumn
psobkt512to1023Err = _Psobkt512to1023Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 16),
    _Psobkt512to1023Err_Type()
)
psobkt512to1023Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt512to1023Err.setStatus("mandatory")
_Psobkt1024to1518Ok_Type = Counter32
_Psobkt1024to1518Ok_Object = MibTableColumn
psobkt1024to1518Ok = _Psobkt1024to1518Ok_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 17),
    _Psobkt1024to1518Ok_Type()
)
psobkt1024to1518Ok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt1024to1518Ok.setStatus("mandatory")
_Psobkt1024to1518Err_Type = Counter32
_Psobkt1024to1518Err_Object = MibTableColumn
psobkt1024to1518Err = _Psobkt1024to1518Err_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 18),
    _Psobkt1024to1518Err_Type()
)
psobkt1024to1518Err.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psobkt1024to1518Err.setStatus("mandatory")
_PsoRuntPacketsOk_Type = Counter32
_PsoRuntPacketsOk_Object = MibTableColumn
psoRuntPacketsOk = _PsoRuntPacketsOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 19),
    _PsoRuntPacketsOk_Type()
)
psoRuntPacketsOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoRuntPacketsOk.setStatus("mandatory")
_PsoRuntPacketsErr_Type = Counter32
_PsoRuntPacketsErr_Object = MibTableColumn
psoRuntPacketsErr = _PsoRuntPacketsErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 20),
    _PsoRuntPacketsErr_Type()
)
psoRuntPacketsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoRuntPacketsErr.setStatus("mandatory")
_PsoPacketsTooBigOk_Type = Counter32
_PsoPacketsTooBigOk_Object = MibTableColumn
psoPacketsTooBigOk = _PsoPacketsTooBigOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 21),
    _PsoPacketsTooBigOk_Type()
)
psoPacketsTooBigOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoPacketsTooBigOk.setStatus("mandatory")
_PsoPacketsTooBigErr_Type = Counter32
_PsoPacketsTooBigErr_Object = MibTableColumn
psoPacketsTooBigErr = _PsoPacketsTooBigErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 1, 1, 22),
    _PsoPacketsTooBigErr_Type()
)
psoPacketsTooBigErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psoPacketsTooBigErr.setStatus("mandatory")
_PortPacketTable_Object = MibTable
portPacketTable = _PortPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2)
)
if mibBuilder.loadTexts:
    portPacketTable.setStatus("mandatory")
_PortPacketEntry_Object = MibTableRow
portPacketEntry = _PortPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1)
)
portPacketEntry.setIndexNames(
    (0, "COMPEX-IN3000", "pspGroupIndex"),
    (0, "COMPEX-IN3000", "pspPortIndex"),
)
if mibBuilder.loadTexts:
    portPacketEntry.setStatus("mandatory")
_PspGroupIndex_Type = Integer32
_PspGroupIndex_Object = MibTableColumn
pspGroupIndex = _PspGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 1),
    _PspGroupIndex_Type()
)
pspGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspGroupIndex.setStatus("mandatory")
_PspPortIndex_Type = Integer32
_PspPortIndex_Object = MibTableColumn
pspPortIndex = _PspPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 2),
    _PspPortIndex_Type()
)
pspPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspPortIndex.setStatus("mandatory")
_PspPacketsRxOk_Type = Counter32
_PspPacketsRxOk_Object = MibTableColumn
pspPacketsRxOk = _PspPacketsRxOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 3),
    _PspPacketsRxOk_Type()
)
pspPacketsRxOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspPacketsRxOk.setStatus("mandatory")
_PspPacketsRxErr_Type = Counter32
_PspPacketsRxErr_Object = MibTableColumn
pspPacketsRxErr = _PspPacketsRxErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 4),
    _PspPacketsRxErr_Type()
)
pspPacketsRxErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspPacketsRxErr.setStatus("mandatory")
_PspPhysicalOk_Type = Counter32
_PspPhysicalOk_Object = MibTableColumn
pspPhysicalOk = _PspPhysicalOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 5),
    _PspPhysicalOk_Type()
)
pspPhysicalOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspPhysicalOk.setStatus("mandatory")
_PspPhysicalErr_Type = Counter32
_PspPhysicalErr_Object = MibTableColumn
pspPhysicalErr = _PspPhysicalErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 6),
    _PspPhysicalErr_Type()
)
pspPhysicalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspPhysicalErr.setStatus("mandatory")
_PspMulticastOk_Type = Counter32
_PspMulticastOk_Object = MibTableColumn
pspMulticastOk = _PspMulticastOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 7),
    _PspMulticastOk_Type()
)
pspMulticastOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspMulticastOk.setStatus("mandatory")
_PspMulticastErr_Type = Counter32
_PspMulticastErr_Object = MibTableColumn
pspMulticastErr = _PspMulticastErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 8),
    _PspMulticastErr_Type()
)
pspMulticastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspMulticastErr.setStatus("mandatory")
_PspBroadcastOk_Type = Counter32
_PspBroadcastOk_Object = MibTableColumn
pspBroadcastOk = _PspBroadcastOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 9),
    _PspBroadcastOk_Type()
)
pspBroadcastOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspBroadcastOk.setStatus("mandatory")
_PspBroadcastErr_Type = Counter32
_PspBroadcastErr_Object = MibTableColumn
pspBroadcastErr = _PspBroadcastErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 10),
    _PspBroadcastErr_Type()
)
pspBroadcastErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspBroadcastErr.setStatus("mandatory")
_PspHostPhysicalOk_Type = Counter32
_PspHostPhysicalOk_Object = MibTableColumn
pspHostPhysicalOk = _PspHostPhysicalOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 11),
    _PspHostPhysicalOk_Type()
)
pspHostPhysicalOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspHostPhysicalOk.setStatus("mandatory")
_PspHostPhysicalErr_Type = Counter32
_PspHostPhysicalErr_Object = MibTableColumn
pspHostPhysicalErr = _PspHostPhysicalErr_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 2, 1, 12),
    _PspHostPhysicalErr_Type()
)
pspHostPhysicalErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pspHostPhysicalErr.setStatus("mandatory")
_PortMiscTable_Object = MibTable
portMiscTable = _PortMiscTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3)
)
if mibBuilder.loadTexts:
    portMiscTable.setStatus("mandatory")
_PortMiscEntry_Object = MibTableRow
portMiscEntry = _PortMiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1)
)
portMiscEntry.setIndexNames(
    (0, "COMPEX-IN3000", "psmGroupIndex"),
    (0, "COMPEX-IN3000", "psmPortIndex"),
)
if mibBuilder.loadTexts:
    portMiscEntry.setStatus("mandatory")
_PsmGroupIndex_Type = Integer32
_PsmGroupIndex_Object = MibTableColumn
psmGroupIndex = _PsmGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 1),
    _PsmGroupIndex_Type()
)
psmGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmGroupIndex.setStatus("mandatory")
_PsmPortIndex_Type = Integer32
_PsmPortIndex_Object = MibTableColumn
psmPortIndex = _PsmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 2),
    _PsmPortIndex_Type()
)
psmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmPortIndex.setStatus("mandatory")


class _PsmName_Type(DisplayString):
    """Custom type psmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_PsmName_Type.__name__ = "DisplayString"
_PsmName_Object = MibTableColumn
psmName = _PsmName_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 3),
    _PsmName_Type()
)
psmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psmName.setStatus("mandatory")


class _PsmType_Type(Integer32):
    """Custom type psmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aui-bnc", 2),
          ("tenBaseT", 1),
          ("unknown", 3))
    )


_PsmType_Type.__name__ = "Integer32"
_PsmType_Object = MibTableColumn
psmType = _PsmType_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 4),
    _PsmType_Type()
)
psmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmType.setStatus("mandatory")


class _PsmLinkState_Type(Integer32):
    """Custom type psmLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unsupported", 3),
          ("up", 1))
    )


_PsmLinkState_Type.__name__ = "Integer32"
_PsmLinkState_Object = MibTableColumn
psmLinkState = _PsmLinkState_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 5),
    _PsmLinkState_Type()
)
psmLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmLinkState.setStatus("mandatory")


class _PsmLinkPulses_Type(Integer32):
    """Custom type psmLinkPulses based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("unsupported", 3))
    )


_PsmLinkPulses_Type.__name__ = "Integer32"
_PsmLinkPulses_Object = MibTableColumn
psmLinkPulses = _PsmLinkPulses_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 6),
    _PsmLinkPulses_Type()
)
psmLinkPulses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psmLinkPulses.setStatus("mandatory")
_PsmCollisions_Type = Counter32
_PsmCollisions_Object = MibTableColumn
psmCollisions = _PsmCollisions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 7),
    _PsmCollisions_Type()
)
psmCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmCollisions.setStatus("mandatory")
_PsmLateCollisions_Type = Counter32
_PsmLateCollisions_Object = MibTableColumn
psmLateCollisions = _PsmLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 8),
    _PsmLateCollisions_Type()
)
psmLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmLateCollisions.setStatus("mandatory")
_PsmPartitions_Type = Counter32
_PsmPartitions_Object = MibTableColumn
psmPartitions = _PsmPartitions_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 9),
    _PsmPartitions_Type()
)
psmPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmPartitions.setStatus("mandatory")
_PsmJabbers_Type = Counter32
_PsmJabbers_Object = MibTableColumn
psmJabbers = _PsmJabbers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 10),
    _PsmJabbers_Type()
)
psmJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmJabbers.setStatus("mandatory")
_PsmShortFragments_Type = Counter32
_PsmShortFragments_Object = MibTableColumn
psmShortFragments = _PsmShortFragments_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 11),
    _PsmShortFragments_Type()
)
psmShortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmShortFragments.setStatus("mandatory")
_PsmCrcFae_Type = Counter32
_PsmCrcFae_Object = MibTableColumn
psmCrcFae = _PsmCrcFae_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 12),
    _PsmCrcFae_Type()
)
psmCrcFae.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmCrcFae.setStatus("mandatory")
_PsmCrc_Type = Counter32
_PsmCrc_Object = MibTableColumn
psmCrc = _PsmCrc_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 13),
    _PsmCrc_Type()
)
psmCrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmCrc.setStatus("mandatory")
_PsmFifoOverrun_Type = Counter32
_PsmFifoOverrun_Object = MibTableColumn
psmFifoOverrun = _PsmFifoOverrun_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 14),
    _PsmFifoOverrun_Type()
)
psmFifoOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmFifoOverrun.setStatus("mandatory")
_PsmDeferring_Type = Counter32
_PsmDeferring_Object = MibTableColumn
psmDeferring = _PsmDeferring_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 7, 3, 1, 15),
    _PsmDeferring_Type()
)
psmDeferring.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psmDeferring.setStatus("mandatory")
_In3000StatsMemory_ObjectIdentity = ObjectIdentity
in3000StatsMemory = _In3000StatsMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 8)
)
_InitHeapSize_Type = Integer32
_InitHeapSize_Object = MibScalar
initHeapSize = _InitHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 1),
    _InitHeapSize_Type()
)
initHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    initHeapSize.setStatus("mandatory")
_UsedHeap_Type = Gauge32
_UsedHeap_Object = MibScalar
usedHeap = _UsedHeap_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 2),
    _UsedHeap_Type()
)
usedHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedHeap.setStatus("mandatory")
_FreeHeap_Type = Gauge32
_FreeHeap_Object = MibScalar
freeHeap = _FreeHeap_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 3),
    _FreeHeap_Type()
)
freeHeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeHeap.setStatus("mandatory")


class _HeapStatus_Type(Integer32):
    """Custom type heapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOk", 2),
          ("ok", 1))
    )


_HeapStatus_Type.__name__ = "Integer32"
_HeapStatus_Object = MibScalar
heapStatus = _HeapStatus_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 4),
    _HeapStatus_Type()
)
heapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heapStatus.setStatus("mandatory")
_MallocCalls_Type = Counter32
_MallocCalls_Object = MibScalar
mallocCalls = _MallocCalls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 5),
    _MallocCalls_Type()
)
mallocCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mallocCalls.setStatus("mandatory")
_ReallocCalls_Type = Counter32
_ReallocCalls_Object = MibScalar
reallocCalls = _ReallocCalls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 6),
    _ReallocCalls_Type()
)
reallocCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    reallocCalls.setStatus("mandatory")
_CallocCalls_Type = Counter32
_CallocCalls_Object = MibScalar
callocCalls = _CallocCalls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 7),
    _CallocCalls_Type()
)
callocCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callocCalls.setStatus("mandatory")
_FreeCalls_Type = Counter32
_FreeCalls_Object = MibScalar
freeCalls = _FreeCalls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 8),
    _FreeCalls_Type()
)
freeCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeCalls.setStatus("mandatory")
_NoMemoryAvailable_Type = Counter32
_NoMemoryAvailable_Object = MibScalar
noMemoryAvailable = _NoMemoryAvailable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 9),
    _NoMemoryAvailable_Type()
)
noMemoryAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    noMemoryAvailable.setStatus("mandatory")
_MnodeCoalesces_Type = Counter32
_MnodeCoalesces_Object = MibScalar
mnodeCoalesces = _MnodeCoalesces_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 10),
    _MnodeCoalesces_Type()
)
mnodeCoalesces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mnodeCoalesces.setStatus("mandatory")
_CoalesceMemCalls_Type = Counter32
_CoalesceMemCalls_Object = MibScalar
coalesceMemCalls = _CoalesceMemCalls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 11),
    _CoalesceMemCalls_Type()
)
coalesceMemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coalesceMemCalls.setStatus("mandatory")
_CoalesceThreshold_Type = Integer32
_CoalesceThreshold_Object = MibScalar
coalesceThreshold = _CoalesceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 8, 12),
    _CoalesceThreshold_Type()
)
coalesceThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coalesceThreshold.setStatus("mandatory")
_In3000StatsIcmp_ObjectIdentity = ObjectIdentity
in3000StatsIcmp = _In3000StatsIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 9)
)
_InUnknownTypes_Type = Counter32
_InUnknownTypes_Object = MibScalar
inUnknownTypes = _InUnknownTypes_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 9, 1),
    _InUnknownTypes_Type()
)
inUnknownTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inUnknownTypes.setStatus("mandatory")
_BufferPoolEmpty_Type = Counter32
_BufferPoolEmpty_Object = MibScalar
bufferPoolEmpty = _BufferPoolEmpty_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 9, 2),
    _BufferPoolEmpty_Type()
)
bufferPoolEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferPoolEmpty.setStatus("mandatory")
_DataBufferTooSmall_Type = Counter32
_DataBufferTooSmall_Object = MibScalar
dataBufferTooSmall = _DataBufferTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 9, 3),
    _DataBufferTooSmall_Type()
)
dataBufferTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dataBufferTooSmall.setStatus("mandatory")
_In3000StatsOS_ObjectIdentity = ObjectIdentity
in3000StatsOS = _In3000StatsOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 10)
)
_ThreadCreateReq_Type = Counter32
_ThreadCreateReq_Object = MibScalar
threadCreateReq = _ThreadCreateReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 1),
    _ThreadCreateReq_Type()
)
threadCreateReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadCreateReq.setStatus("mandatory")
_ThreadCreateOk_Type = Counter32
_ThreadCreateOk_Object = MibScalar
threadCreateOk = _ThreadCreateOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 2),
    _ThreadCreateOk_Type()
)
threadCreateOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadCreateOk.setStatus("mandatory")
_ThreadCreateFail_Type = Counter32
_ThreadCreateFail_Object = MibScalar
threadCreateFail = _ThreadCreateFail_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 3),
    _ThreadCreateFail_Type()
)
threadCreateFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadCreateFail.setStatus("mandatory")
_ThreadTableFull_Type = Counter32
_ThreadTableFull_Object = MibScalar
threadTableFull = _ThreadTableFull_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 4),
    _ThreadTableFull_Type()
)
threadTableFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadTableFull.setStatus("mandatory")
_ThreadKill_Type = Counter32
_ThreadKill_Object = MibScalar
threadKill = _ThreadKill_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 5),
    _ThreadKill_Type()
)
threadKill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threadKill.setStatus("mandatory")
_ThreadMaximum_Type = Integer32
_ThreadMaximum_Object = MibScalar
threadMaximum = _ThreadMaximum_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 6),
    _ThreadMaximum_Type()
)
threadMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    threadMaximum.setStatus("mandatory")
_DefaultStackSize_Type = Integer32
_DefaultStackSize_Object = MibScalar
defaultStackSize = _DefaultStackSize_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 7),
    _DefaultStackSize_Type()
)
defaultStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultStackSize.setStatus("mandatory")
_DefaultTimeSlice_Type = Integer32
_DefaultTimeSlice_Object = MibScalar
defaultTimeSlice = _DefaultTimeSlice_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 8),
    _DefaultTimeSlice_Type()
)
defaultTimeSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultTimeSlice.setStatus("mandatory")
_BogusInterrupts_Type = Counter32
_BogusInterrupts_Object = MibScalar
bogusInterrupts = _BogusInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 9),
    _BogusInterrupts_Type()
)
bogusInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bogusInterrupts.setStatus("mandatory")
_DivideError_Type = Counter32
_DivideError_Object = MibScalar
divideError = _DivideError_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 10),
    _DivideError_Type()
)
divideError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    divideError.setStatus("mandatory")
_SingleStep_Type = Counter32
_SingleStep_Object = MibScalar
singleStep = _SingleStep_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 11),
    _SingleStep_Type()
)
singleStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    singleStep.setStatus("mandatory")
_Breakpoint_Type = Counter32
_Breakpoint_Object = MibScalar
breakpoint = _Breakpoint_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 12),
    _Breakpoint_Type()
)
breakpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    breakpoint.setStatus("mandatory")
_InterruptOverflow_Type = Counter32
_InterruptOverflow_Object = MibScalar
interruptOverflow = _InterruptOverflow_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 13),
    _InterruptOverflow_Type()
)
interruptOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interruptOverflow.setStatus("mandatory")
_ArrayBoundsCheck_Type = Counter32
_ArrayBoundsCheck_Object = MibScalar
arrayBoundsCheck = _ArrayBoundsCheck_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 14),
    _ArrayBoundsCheck_Type()
)
arrayBoundsCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrayBoundsCheck.setStatus("mandatory")
_InvalidOpcode_Type = Counter32
_InvalidOpcode_Object = MibScalar
invalidOpcode = _InvalidOpcode_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 15),
    _InvalidOpcode_Type()
)
invalidOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    invalidOpcode.setStatus("mandatory")
_EscapeOpcode_Type = Counter32
_EscapeOpcode_Object = MibScalar
escapeOpcode = _EscapeOpcode_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 16),
    _EscapeOpcode_Type()
)
escapeOpcode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    escapeOpcode.setStatus("mandatory")
_CoprocessorFault_Type = Counter32
_CoprocessorFault_Object = MibScalar
coprocessorFault = _CoprocessorFault_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 17),
    _CoprocessorFault_Type()
)
coprocessorFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coprocessorFault.setStatus("mandatory")
_ThreadTable_Object = MibTable
threadTable = _ThreadTable_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18)
)
if mibBuilder.loadTexts:
    threadTable.setStatus("mandatory")
_ThreadEntry_Object = MibTableRow
threadEntry = _ThreadEntry_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1)
)
threadEntry.setIndexNames(
    (0, "COMPEX-IN3000", "tid"),
)
if mibBuilder.loadTexts:
    threadEntry.setStatus("mandatory")
_Tid_Type = Integer32
_Tid_Object = MibTableColumn
tid = _Tid_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 1),
    _Tid_Type()
)
tid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tid.setStatus("mandatory")


class _Name_Type(DisplayString):
    """Custom type name based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Name_Type.__name__ = "DisplayString"
_Name_Object = MibTableColumn
name = _Name_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 2),
    _Name_Type()
)
name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    name.setStatus("mandatory")
_Priority_Type = Integer32
_Priority_Object = MibTableColumn
priority = _Priority_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 3),
    _Priority_Type()
)
priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    priority.setStatus("mandatory")
_MuxCount_Type = Integer32
_MuxCount_Object = MibTableColumn
muxCount = _MuxCount_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 4),
    _MuxCount_Type()
)
muxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    muxCount.setStatus("mandatory")


class _Status_Type(Integer32):
    """Custom type status based on Integer32"""
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
        *(("blocked", 4),
          ("dead", 5),
          ("killed", 2),
          ("queued", 3),
          ("running", 1))
    )


_Status_Type.__name__ = "Integer32"
_Status_Object = MibTableColumn
status = _Status_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 5),
    _Status_Type()
)
status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    status.setStatus("mandatory")
_StackSize_Type = Integer32
_StackSize_Object = MibTableColumn
stackSize = _StackSize_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 10, 18, 1, 6),
    _StackSize_Type()
)
stackSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackSize.setStatus("mandatory")
_In3000StatsArp_ObjectIdentity = ObjectIdentity
in3000StatsArp = _In3000StatsArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 11)
)
_ArpInReqs_Type = Counter32
_ArpInReqs_Object = MibScalar
arpInReqs = _ArpInReqs_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 1),
    _ArpInReqs_Type()
)
arpInReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInReqs.setStatus("mandatory")
_ArpInRpls_Type = Counter32
_ArpInRpls_Object = MibScalar
arpInRpls = _ArpInRpls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 2),
    _ArpInRpls_Type()
)
arpInRpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpInRpls.setStatus("mandatory")
_ArpOutReqs_Type = Counter32
_ArpOutReqs_Object = MibScalar
arpOutReqs = _ArpOutReqs_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 3),
    _ArpOutReqs_Type()
)
arpOutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpOutReqs.setStatus("mandatory")
_ArpOutRpls_Type = Counter32
_ArpOutRpls_Object = MibScalar
arpOutRpls = _ArpOutRpls_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 4),
    _ArpOutRpls_Type()
)
arpOutRpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpOutRpls.setStatus("mandatory")
_ArpGetReqs_Type = Counter32
_ArpGetReqs_Object = MibScalar
arpGetReqs = _ArpGetReqs_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 5),
    _ArpGetReqs_Type()
)
arpGetReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpGetReqs.setStatus("mandatory")
_ArpPutReqs_Type = Counter32
_ArpPutReqs_Object = MibScalar
arpPutReqs = _ArpPutReqs_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 6),
    _ArpPutReqs_Type()
)
arpPutReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpPutReqs.setStatus("mandatory")
_ArpDeadEntries_Type = Counter32
_ArpDeadEntries_Object = MibScalar
arpDeadEntries = _ArpDeadEntries_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 7),
    _ArpDeadEntries_Type()
)
arpDeadEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpDeadEntries.setStatus("mandatory")


class _ArpCacheSize_Type(Integer32):
    """Custom type arpCacheSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_ArpCacheSize_Type.__name__ = "Integer32"
_ArpCacheSize_Object = MibScalar
arpCacheSize = _ArpCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 8),
    _ArpCacheSize_Type()
)
arpCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheSize.setStatus("mandatory")


class _ArpEntryTimeout_Type(Integer32):
    """Custom type arpEntryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60480),
    )


_ArpEntryTimeout_Type.__name__ = "Integer32"
_ArpEntryTimeout_Object = MibScalar
arpEntryTimeout = _ArpEntryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 9),
    _ArpEntryTimeout_Type()
)
arpEntryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpEntryTimeout.setStatus("mandatory")


class _ArpNumRetries_Type(Integer32):
    """Custom type arpNumRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ArpNumRetries_Type.__name__ = "Integer32"
_ArpNumRetries_Object = MibScalar
arpNumRetries = _ArpNumRetries_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 10),
    _ArpNumRetries_Type()
)
arpNumRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpNumRetries.setStatus("mandatory")


class _ArpReplyTimeout_Type(Integer32):
    """Custom type arpReplyTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65000),
    )


_ArpReplyTimeout_Type.__name__ = "Integer32"
_ArpReplyTimeout_Object = MibScalar
arpReplyTimeout = _ArpReplyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 11, 11),
    _ArpReplyTimeout_Type()
)
arpReplyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpReplyTimeout.setStatus("mandatory")
_In3000StatsIp_ObjectIdentity = ObjectIdentity
in3000StatsIp = _In3000StatsIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 12)
)
_InHdrTooSmall_Type = Counter32
_InHdrTooSmall_Object = MibScalar
inHdrTooSmall = _InHdrTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 1),
    _InHdrTooSmall_Type()
)
inHdrTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHdrTooSmall.setStatus("mandatory")
_InHdrBadVersion_Type = Counter32
_InHdrBadVersion_Object = MibScalar
inHdrBadVersion = _InHdrBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 2),
    _InHdrBadVersion_Type()
)
inHdrBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHdrBadVersion.setStatus("mandatory")
_InHdrBadCheckSum_Type = Counter32
_InHdrBadCheckSum_Object = MibScalar
inHdrBadCheckSum = _InHdrBadCheckSum_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 3),
    _InHdrBadCheckSum_Type()
)
inHdrBadCheckSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHdrBadCheckSum.setStatus("mandatory")
_InHdrBadOption_Type = Counter32
_InHdrBadOption_Object = MibScalar
inHdrBadOption = _InHdrBadOption_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 4),
    _InHdrBadOption_Type()
)
inHdrBadOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inHdrBadOption.setStatus("mandatory")
_InDataNotAllocated_Type = Counter32
_InDataNotAllocated_Object = MibScalar
inDataNotAllocated = _InDataNotAllocated_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 5),
    _InDataNotAllocated_Type()
)
inDataNotAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inDataNotAllocated.setStatus("mandatory")
_InNoPacketBuffers_Type = Counter32
_InNoPacketBuffers_Object = MibScalar
inNoPacketBuffers = _InNoPacketBuffers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 6),
    _InNoPacketBuffers_Type()
)
inNoPacketBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inNoPacketBuffers.setStatus("mandatory")
_OutNoPacketBuffers_Type = Counter32
_OutNoPacketBuffers_Object = MibScalar
outNoPacketBuffers = _OutNoPacketBuffers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 7),
    _OutNoPacketBuffers_Type()
)
outNoPacketBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outNoPacketBuffers.setStatus("mandatory")
_OutBadTransmits_Type = Counter32
_OutBadTransmits_Object = MibScalar
outBadTransmits = _OutBadTransmits_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 8),
    _OutBadTransmits_Type()
)
outBadTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBadTransmits.setStatus("mandatory")
_OutAddrNotResolved_Type = Counter32
_OutAddrNotResolved_Object = MibScalar
outAddrNotResolved = _OutAddrNotResolved_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 9),
    _OutAddrNotResolved_Type()
)
outAddrNotResolved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outAddrNotResolved.setStatus("mandatory")
_ReasmTimeout_Type = Integer32
_ReasmTimeout_Object = MibScalar
reasmTimeout = _ReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 12, 10),
    _ReasmTimeout_Type()
)
reasmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reasmTimeout.setStatus("mandatory")
_In3000StatsHmi_ObjectIdentity = ObjectIdentity
in3000StatsHmi = _In3000StatsHmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 13)
)
_HmiReqs_Type = Counter32
_HmiReqs_Object = MibScalar
hmiReqs = _HmiReqs_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 1),
    _HmiReqs_Type()
)
hmiReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiReqs.setStatus("mandatory")
_HmiResp_Type = Counter32
_HmiResp_Object = MibScalar
hmiResp = _HmiResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 2),
    _HmiResp_Type()
)
hmiResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiResp.setStatus("mandatory")
_HmiError_Type = Counter32
_HmiError_Object = MibScalar
hmiError = _HmiError_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 3),
    _HmiError_Type()
)
hmiError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiError.setStatus("mandatory")
_HmiAckOk_Type = Counter32
_HmiAckOk_Object = MibScalar
hmiAckOk = _HmiAckOk_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 4),
    _HmiAckOk_Type()
)
hmiAckOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiAckOk.setStatus("mandatory")
_HmiAckBad_Type = Counter32
_HmiAckBad_Object = MibScalar
hmiAckBad = _HmiAckBad_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 5),
    _HmiAckBad_Type()
)
hmiAckBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiAckBad.setStatus("mandatory")
_HmiTrap_Type = Counter32
_HmiTrap_Object = MibScalar
hmiTrap = _HmiTrap_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 6),
    _HmiTrap_Type()
)
hmiTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiTrap.setStatus("mandatory")
_HmiIdReq_Type = Counter32
_HmiIdReq_Object = MibScalar
hmiIdReq = _HmiIdReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 7),
    _HmiIdReq_Type()
)
hmiIdReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiIdReq.setStatus("mandatory")
_HmiGetInfoReq_Type = Counter32
_HmiGetInfoReq_Object = MibScalar
hmiGetInfoReq = _HmiGetInfoReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 8),
    _HmiGetInfoReq_Type()
)
hmiGetInfoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiGetInfoReq.setStatus("mandatory")
_HmiSelftestReq_Type = Counter32
_HmiSelftestReq_Object = MibScalar
hmiSelftestReq = _HmiSelftestReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 9),
    _HmiSelftestReq_Type()
)
hmiSelftestReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiSelftestReq.setStatus("mandatory")
_HmiPortEnableReq_Type = Counter32
_HmiPortEnableReq_Object = MibScalar
hmiPortEnableReq = _HmiPortEnableReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 10),
    _HmiPortEnableReq_Type()
)
hmiPortEnableReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortEnableReq.setStatus("mandatory")
_HmiPortDisableReq_Type = Counter32
_HmiPortDisableReq_Object = MibScalar
hmiPortDisableReq = _HmiPortDisableReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 11),
    _HmiPortDisableReq_Type()
)
hmiPortDisableReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortDisableReq.setStatus("mandatory")
_HmiStatusReq_Type = Counter32
_HmiStatusReq_Object = MibScalar
hmiStatusReq = _HmiStatusReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 12),
    _HmiStatusReq_Type()
)
hmiStatusReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiStatusReq.setStatus("mandatory")
_HmiRepeaterReq_Type = Counter32
_HmiRepeaterReq_Object = MibScalar
hmiRepeaterReq = _HmiRepeaterReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 13),
    _HmiRepeaterReq_Type()
)
hmiRepeaterReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiRepeaterReq.setStatus("mandatory")
_HmiPortObjectsReq_Type = Counter32
_HmiPortObjectsReq_Object = MibScalar
hmiPortObjectsReq = _HmiPortObjectsReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 14),
    _HmiPortObjectsReq_Type()
)
hmiPortObjectsReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortObjectsReq.setStatus("mandatory")
_HmiPortChangesReq_Type = Counter32
_HmiPortChangesReq_Object = MibScalar
hmiPortChangesReq = _HmiPortChangesReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 15),
    _HmiPortChangesReq_Type()
)
hmiPortChangesReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortChangesReq.setStatus("mandatory")
_HmiSelfTestStatReq_Type = Counter32
_HmiSelfTestStatReq_Object = MibScalar
hmiSelfTestStatReq = _HmiSelfTestStatReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 16),
    _HmiSelfTestStatReq_Type()
)
hmiSelfTestStatReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiSelfTestStatReq.setStatus("mandatory")
_HmiDebugOnReq_Type = Counter32
_HmiDebugOnReq_Object = MibScalar
hmiDebugOnReq = _HmiDebugOnReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 17),
    _HmiDebugOnReq_Type()
)
hmiDebugOnReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiDebugOnReq.setStatus("mandatory")
_HmiDebugOffReq_Type = Counter32
_HmiDebugOffReq_Object = MibScalar
hmiDebugOffReq = _HmiDebugOffReq_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 18),
    _HmiDebugOffReq_Type()
)
hmiDebugOffReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiDebugOffReq.setStatus("mandatory")
_HmiGetInfoResp_Type = Counter32
_HmiGetInfoResp_Object = MibScalar
hmiGetInfoResp = _HmiGetInfoResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 19),
    _HmiGetInfoResp_Type()
)
hmiGetInfoResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiGetInfoResp.setStatus("mandatory")
_HmiSelfTestResp_Type = Counter32
_HmiSelfTestResp_Object = MibScalar
hmiSelfTestResp = _HmiSelfTestResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 20),
    _HmiSelfTestResp_Type()
)
hmiSelfTestResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiSelfTestResp.setStatus("mandatory")
_HmiStatusResp_Type = Counter32
_HmiStatusResp_Object = MibScalar
hmiStatusResp = _HmiStatusResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 21),
    _HmiStatusResp_Type()
)
hmiStatusResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiStatusResp.setStatus("mandatory")
_HmiRepeaterResp_Type = Counter32
_HmiRepeaterResp_Object = MibScalar
hmiRepeaterResp = _HmiRepeaterResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 22),
    _HmiRepeaterResp_Type()
)
hmiRepeaterResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiRepeaterResp.setStatus("mandatory")
_HmiPortObjectsResp_Type = Counter32
_HmiPortObjectsResp_Object = MibScalar
hmiPortObjectsResp = _HmiPortObjectsResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 23),
    _HmiPortObjectsResp_Type()
)
hmiPortObjectsResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortObjectsResp.setStatus("mandatory")
_HmiPortChangesResp_Type = Counter32
_HmiPortChangesResp_Object = MibScalar
hmiPortChangesResp = _HmiPortChangesResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 24),
    _HmiPortChangesResp_Type()
)
hmiPortChangesResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiPortChangesResp.setStatus("mandatory")
_HmiSelfTestStatResp_Type = Counter32
_HmiSelfTestStatResp_Object = MibScalar
hmiSelfTestStatResp = _HmiSelfTestStatResp_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 13, 25),
    _HmiSelfTestStatResp_Type()
)
hmiSelfTestStatResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hmiSelfTestStatResp.setStatus("mandatory")
_In3000StatsUart_ObjectIdentity = ObjectIdentity
in3000StatsUart = _In3000StatsUart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 14)
)
_UartInOctets_Type = Counter32
_UartInOctets_Object = MibScalar
uartInOctets = _UartInOctets_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 1),
    _UartInOctets_Type()
)
uartInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartInOctets.setStatus("mandatory")
_UartOutOctets_Type = Counter32
_UartOutOctets_Object = MibScalar
uartOutOctets = _UartOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 2),
    _UartOutOctets_Type()
)
uartOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartOutOctets.setStatus("mandatory")
_UartInDelivers_Type = Counter32
_UartInDelivers_Object = MibScalar
uartInDelivers = _UartInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 3),
    _UartInDelivers_Type()
)
uartInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartInDelivers.setStatus("mandatory")
_UartOutDelivers_Type = Counter32
_UartOutDelivers_Object = MibScalar
uartOutDelivers = _UartOutDelivers_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 4),
    _UartOutDelivers_Type()
)
uartOutDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartOutDelivers.setStatus("mandatory")


class _UartBaudRate_Type(Integer32):
    """Custom type uartBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1200,
              2400,
              4800,
              9600,
              19200,
              38400,
              57600,
              115200)
        )
    )
    namedValues = NamedValues(
        *(("br115200", 115200),
          ("br1200", 1200),
          ("br19200", 19200),
          ("br2400", 2400),
          ("br38400", 38400),
          ("br4800", 4800),
          ("br57600", 57600),
          ("br9600", 9600))
    )


_UartBaudRate_Type.__name__ = "Integer32"
_UartBaudRate_Object = MibScalar
uartBaudRate = _UartBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 5),
    _UartBaudRate_Type()
)
uartBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartBaudRate.setStatus("mandatory")


class _UartDataBits_Type(Integer32):
    """Custom type uartDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("eight", 8),
          ("five", 5),
          ("seven", 7),
          ("six", 6))
    )


_UartDataBits_Type.__name__ = "Integer32"
_UartDataBits_Object = MibScalar
uartDataBits = _UartDataBits_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 6),
    _UartDataBits_Type()
)
uartDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uartDataBits.setStatus("mandatory")


class _UartStopBits_Type(Integer32):
    """Custom type uartStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("two", 2))
    )


_UartStopBits_Type.__name__ = "Integer32"
_UartStopBits_Object = MibScalar
uartStopBits = _UartStopBits_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 7),
    _UartStopBits_Type()
)
uartStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uartStopBits.setStatus("mandatory")


class _UartParity_Type(Integer32):
    """Custom type uartParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 1),
          ("odd", 3))
    )


_UartParity_Type.__name__ = "Integer32"
_UartParity_Object = MibScalar
uartParity = _UartParity_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 8),
    _UartParity_Type()
)
uartParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uartParity.setStatus("mandatory")


class _UartHandshaking_Type(Integer32):
    """Custom type uartHandshaking based on Integer32"""
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
          ("rtsCts", 3),
          ("xonXoff", 2))
    )


_UartHandshaking_Type.__name__ = "Integer32"
_UartHandshaking_Object = MibScalar
uartHandshaking = _UartHandshaking_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 9),
    _UartHandshaking_Type()
)
uartHandshaking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uartHandshaking.setStatus("mandatory")
_UartOverrunErrors_Type = Counter32
_UartOverrunErrors_Object = MibScalar
uartOverrunErrors = _UartOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 10),
    _UartOverrunErrors_Type()
)
uartOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartOverrunErrors.setStatus("mandatory")
_UartParityErrors_Type = Counter32
_UartParityErrors_Object = MibScalar
uartParityErrors = _UartParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 11),
    _UartParityErrors_Type()
)
uartParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartParityErrors.setStatus("mandatory")
_UartFramingErrors_Type = Counter32
_UartFramingErrors_Object = MibScalar
uartFramingErrors = _UartFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 12),
    _UartFramingErrors_Type()
)
uartFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartFramingErrors.setStatus("mandatory")
_UartBreakIndicators_Type = Counter32
_UartBreakIndicators_Object = MibScalar
uartBreakIndicators = _UartBreakIndicators_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 14, 13),
    _UartBreakIndicators_Type()
)
uartBreakIndicators.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uartBreakIndicators.setStatus("mandatory")
_In3000SelfTests_ObjectIdentity = ObjectIdentity
in3000SelfTests = _In3000SelfTests_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 426, 1, 15)
)


class _DallasTest_Type(Integer32):
    """Custom type dallasTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runTest", 3),
          ("testFailed", 2),
          ("testPass", 1))
    )


_DallasTest_Type.__name__ = "Integer32"
_DallasTest_Object = MibScalar
dallasTest = _DallasTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 1),
    _DallasTest_Type()
)
dallasTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dallasTest.setStatus("mandatory")


class _FlashTest_Type(Integer32):
    """Custom type flashTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runTest", 3),
          ("testFailed", 2),
          ("testPass", 1))
    )


_FlashTest_Type.__name__ = "Integer32"
_FlashTest_Object = MibScalar
flashTest = _FlashTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 2),
    _FlashTest_Type()
)
flashTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flashTest.setStatus("mandatory")


class _UartTest_Type(Integer32):
    """Custom type uartTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runTest", 3),
          ("testFailed", 2),
          ("testPass", 1))
    )


_UartTest_Type.__name__ = "Integer32"
_UartTest_Object = MibScalar
uartTest = _UartTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 3),
    _UartTest_Type()
)
uartTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uartTest.setStatus("mandatory")


class _NicTest_Type(Integer32):
    """Custom type nicTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runTest", 3),
          ("testFailed", 2),
          ("testPass", 1))
    )


_NicTest_Type.__name__ = "Integer32"
_NicTest_Object = MibScalar
nicTest = _NicTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 4),
    _NicTest_Type()
)
nicTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nicTest.setStatus("mandatory")


class _NetioTest_Type(Integer32):
    """Custom type netioTest based on Integer32"""
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
        *(("testFailed", 2),
          ("testHub1", 3),
          ("testHub2", 4),
          ("testHub3", 5),
          ("testHub4", 6),
          ("testPass", 1))
    )


_NetioTest_Type.__name__ = "Integer32"
_NetioTest_Object = MibScalar
netioTest = _NetioTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 5),
    _NetioTest_Type()
)
netioTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netioTest.setStatus("mandatory")


class _HeapTest_Type(Integer32):
    """Custom type heapTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("runTest", 3),
          ("testFailed", 2),
          ("testPass", 1))
    )


_HeapTest_Type.__name__ = "Integer32"
_HeapTest_Object = MibScalar
heapTest = _HeapTest_Object(
    (1, 3, 6, 1, 4, 1, 426, 1, 15, 6),
    _HeapTest_Type()
)
heapTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heapTest.setStatus("mandatory")

# Managed Objects groups


# Notification objects

partState = NotificationType(
    (1, 3, 6, 1, 4, 1, 426, 1, 0, 1)
)
partState.setObjects(
      *(("COMPEX-IN3000", "psmGroupIndex"),
        ("COMPEX-IN3000", "psmPortIndex"))
)
if mibBuilder.loadTexts:
    partState.setStatus(
        ""
    )

notPartState = NotificationType(
    (1, 3, 6, 1, 4, 1, 426, 1, 0, 2)
)
notPartState.setObjects(
      *(("COMPEX-IN3000", "psmGroupIndex"),
        ("COMPEX-IN3000", "psmPortIndex"))
)
if mibBuilder.loadTexts:
    notPartState.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPEX-IN3000",
    **{"compex": compex,
       "in3000": in3000,
       "partState": partState,
       "notPartState": notPartState,
       "hubTypes": hubTypes,
       "tp3000": tp3000,
       "rp3000": rp3000,
       "productInfo": productInfo,
       "productName": productName,
       "productVersion": productVersion,
       "releasedDate": releasedDate,
       "compexAddress": compexAddress,
       "compexPhone": compexPhone,
       "compexImage": compexImage,
       "compexMyAccess": compexMyAccess,
       "devTeamTable": devTeamTable,
       "devTeamEntry": devTeamEntry,
       "cpId": cpId,
       "cpName": cpName,
       "communityInfo": communityInfo,
       "communityTable": communityTable,
       "communityEntry": communityEntry,
       "communityInstance": communityInstance,
       "communityString": communityString,
       "communityCapability": communityCapability,
       "trapInfo": trapInfo,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapDest": trapDest,
       "trapStatus": trapStatus,
       "in3000StatsRptr": in3000StatsRptr,
       "rptrFifoColls": rptrFifoColls,
       "rptrShortWoPort": rptrShortWoPort,
       "rptrNoStatsDsgntr": rptrNoStatsDsgntr,
       "rptrInvalidDesgntr": rptrInvalidDesgntr,
       "rptrPortIDwoPacket": rptrPortIDwoPacket,
       "rptrOverflows": rptrOverflows,
       "rptrNoFreeBuffers": rptrNoFreeBuffers,
       "rptrTxTimeouts": rptrTxTimeouts,
       "rptrNICTxCollisions": rptrNICTxCollisions,
       "rptrNICTxFifoUruns": rptrNICTxFifoUruns,
       "rptrNICTxCDHrtbts": rptrNICTxCDHrtbts,
       "rptrNICTxOutWinCls": rptrNICTxOutWinCls,
       "rptrNICCarrierLost": rptrNICCarrierLost,
       "rptrInNoRxBuf": rptrInNoRxBuf,
       "in3000StatsGroup": in3000StatsGroup,
       "groupOctetsTable": groupOctetsTable,
       "groupOctetsEntry": groupOctetsEntry,
       "gsoGroupIndex": gsoGroupIndex,
       "gsoHostOctetsRxOk": gsoHostOctetsRxOk,
       "gsoHostOctetsRxErr": gsoHostOctetsRxErr,
       "gsoOctetsRxOk": gsoOctetsRxOk,
       "gsoOctetsRxErr": gsoOctetsRxErr,
       "gsobkt64Ok": gsobkt64Ok,
       "gsobkt64Err": gsobkt64Err,
       "gsobkt65to127Ok": gsobkt65to127Ok,
       "gsobkt65to127Err": gsobkt65to127Err,
       "gsobkt128to255Ok": gsobkt128to255Ok,
       "gsobkt128to255Err": gsobkt128to255Err,
       "gsobkt256to511Ok": gsobkt256to511Ok,
       "gsobkt256to511Err": gsobkt256to511Err,
       "gsobkt512to1023Ok": gsobkt512to1023Ok,
       "gsobkt512to1023Err": gsobkt512to1023Err,
       "gsobkt1024to1518Ok": gsobkt1024to1518Ok,
       "gsobkt1024to1518Err": gsobkt1024to1518Err,
       "gsoRuntPacketsOk": gsoRuntPacketsOk,
       "gsoRuntPacketsErr": gsoRuntPacketsErr,
       "gsoPacketsTooBigOk": gsoPacketsTooBigOk,
       "gsoPacketsTooBigErr": gsoPacketsTooBigErr,
       "groupPacketTable": groupPacketTable,
       "groupPacketEntry": groupPacketEntry,
       "gspGroupIndex": gspGroupIndex,
       "gspPacketsRxOk": gspPacketsRxOk,
       "gspPacketsRxErr": gspPacketsRxErr,
       "gspPhysicalOk": gspPhysicalOk,
       "gspPhysicalErr": gspPhysicalErr,
       "gspMulticastOk": gspMulticastOk,
       "gspMulticastErr": gspMulticastErr,
       "gspBroadcastOk": gspBroadcastOk,
       "gspBroadcastErr": gspBroadcastErr,
       "gspHostPhysicalOk": gspHostPhysicalOk,
       "gspHostPhysicalErr": gspHostPhysicalErr,
       "groupMiscTable": groupMiscTable,
       "groupMiscEntry": groupMiscEntry,
       "gsmGroupIndex": gsmGroupIndex,
       "gsmNumPorts": gsmNumPorts,
       "gsmName": gsmName,
       "gsmType": gsmType,
       "gsmNumLinkUp": gsmNumLinkUp,
       "gsmNumLinkPulses": gsmNumLinkPulses,
       "gsmCollisions": gsmCollisions,
       "gsmLateCollisions": gsmLateCollisions,
       "gsmPartitions": gsmPartitions,
       "gsmJabbers": gsmJabbers,
       "gsmShortFragments": gsmShortFragments,
       "gsmCrcFae": gsmCrcFae,
       "gsmCrc": gsmCrc,
       "gsmFifoOverrun": gsmFifoOverrun,
       "gsmDeferring": gsmDeferring,
       "in3000StatsPort": in3000StatsPort,
       "portOctetsTable": portOctetsTable,
       "portOctetsEntry": portOctetsEntry,
       "psoGroupIndex": psoGroupIndex,
       "psoPortIndex": psoPortIndex,
       "psoHostOctetsRxOk": psoHostOctetsRxOk,
       "psoHostOctetsRxErr": psoHostOctetsRxErr,
       "psoOctetsRxOk": psoOctetsRxOk,
       "psoOctetsRxErr": psoOctetsRxErr,
       "psobkt64Ok": psobkt64Ok,
       "psobkt64Err": psobkt64Err,
       "psobkt65to127Ok": psobkt65to127Ok,
       "psobkt65to127Err": psobkt65to127Err,
       "psobkt128to255Ok": psobkt128to255Ok,
       "psobkt128to255Err": psobkt128to255Err,
       "psobkt256to511Ok": psobkt256to511Ok,
       "psobkt256to511Err": psobkt256to511Err,
       "psobkt512to1023Ok": psobkt512to1023Ok,
       "psobkt512to1023Err": psobkt512to1023Err,
       "psobkt1024to1518Ok": psobkt1024to1518Ok,
       "psobkt1024to1518Err": psobkt1024to1518Err,
       "psoRuntPacketsOk": psoRuntPacketsOk,
       "psoRuntPacketsErr": psoRuntPacketsErr,
       "psoPacketsTooBigOk": psoPacketsTooBigOk,
       "psoPacketsTooBigErr": psoPacketsTooBigErr,
       "portPacketTable": portPacketTable,
       "portPacketEntry": portPacketEntry,
       "pspGroupIndex": pspGroupIndex,
       "pspPortIndex": pspPortIndex,
       "pspPacketsRxOk": pspPacketsRxOk,
       "pspPacketsRxErr": pspPacketsRxErr,
       "pspPhysicalOk": pspPhysicalOk,
       "pspPhysicalErr": pspPhysicalErr,
       "pspMulticastOk": pspMulticastOk,
       "pspMulticastErr": pspMulticastErr,
       "pspBroadcastOk": pspBroadcastOk,
       "pspBroadcastErr": pspBroadcastErr,
       "pspHostPhysicalOk": pspHostPhysicalOk,
       "pspHostPhysicalErr": pspHostPhysicalErr,
       "portMiscTable": portMiscTable,
       "portMiscEntry": portMiscEntry,
       "psmGroupIndex": psmGroupIndex,
       "psmPortIndex": psmPortIndex,
       "psmName": psmName,
       "psmType": psmType,
       "psmLinkState": psmLinkState,
       "psmLinkPulses": psmLinkPulses,
       "psmCollisions": psmCollisions,
       "psmLateCollisions": psmLateCollisions,
       "psmPartitions": psmPartitions,
       "psmJabbers": psmJabbers,
       "psmShortFragments": psmShortFragments,
       "psmCrcFae": psmCrcFae,
       "psmCrc": psmCrc,
       "psmFifoOverrun": psmFifoOverrun,
       "psmDeferring": psmDeferring,
       "in3000StatsMemory": in3000StatsMemory,
       "initHeapSize": initHeapSize,
       "usedHeap": usedHeap,
       "freeHeap": freeHeap,
       "heapStatus": heapStatus,
       "mallocCalls": mallocCalls,
       "reallocCalls": reallocCalls,
       "callocCalls": callocCalls,
       "freeCalls": freeCalls,
       "noMemoryAvailable": noMemoryAvailable,
       "mnodeCoalesces": mnodeCoalesces,
       "coalesceMemCalls": coalesceMemCalls,
       "coalesceThreshold": coalesceThreshold,
       "in3000StatsIcmp": in3000StatsIcmp,
       "inUnknownTypes": inUnknownTypes,
       "bufferPoolEmpty": bufferPoolEmpty,
       "dataBufferTooSmall": dataBufferTooSmall,
       "in3000StatsOS": in3000StatsOS,
       "threadCreateReq": threadCreateReq,
       "threadCreateOk": threadCreateOk,
       "threadCreateFail": threadCreateFail,
       "threadTableFull": threadTableFull,
       "threadKill": threadKill,
       "threadMaximum": threadMaximum,
       "defaultStackSize": defaultStackSize,
       "defaultTimeSlice": defaultTimeSlice,
       "bogusInterrupts": bogusInterrupts,
       "divideError": divideError,
       "singleStep": singleStep,
       "breakpoint": breakpoint,
       "interruptOverflow": interruptOverflow,
       "arrayBoundsCheck": arrayBoundsCheck,
       "invalidOpcode": invalidOpcode,
       "escapeOpcode": escapeOpcode,
       "coprocessorFault": coprocessorFault,
       "threadTable": threadTable,
       "threadEntry": threadEntry,
       "tid": tid,
       "name": name,
       "priority": priority,
       "muxCount": muxCount,
       "status": status,
       "stackSize": stackSize,
       "in3000StatsArp": in3000StatsArp,
       "arpInReqs": arpInReqs,
       "arpInRpls": arpInRpls,
       "arpOutReqs": arpOutReqs,
       "arpOutRpls": arpOutRpls,
       "arpGetReqs": arpGetReqs,
       "arpPutReqs": arpPutReqs,
       "arpDeadEntries": arpDeadEntries,
       "arpCacheSize": arpCacheSize,
       "arpEntryTimeout": arpEntryTimeout,
       "arpNumRetries": arpNumRetries,
       "arpReplyTimeout": arpReplyTimeout,
       "in3000StatsIp": in3000StatsIp,
       "inHdrTooSmall": inHdrTooSmall,
       "inHdrBadVersion": inHdrBadVersion,
       "inHdrBadCheckSum": inHdrBadCheckSum,
       "inHdrBadOption": inHdrBadOption,
       "inDataNotAllocated": inDataNotAllocated,
       "inNoPacketBuffers": inNoPacketBuffers,
       "outNoPacketBuffers": outNoPacketBuffers,
       "outBadTransmits": outBadTransmits,
       "outAddrNotResolved": outAddrNotResolved,
       "reasmTimeout": reasmTimeout,
       "in3000StatsHmi": in3000StatsHmi,
       "hmiReqs": hmiReqs,
       "hmiResp": hmiResp,
       "hmiError": hmiError,
       "hmiAckOk": hmiAckOk,
       "hmiAckBad": hmiAckBad,
       "hmiTrap": hmiTrap,
       "hmiIdReq": hmiIdReq,
       "hmiGetInfoReq": hmiGetInfoReq,
       "hmiSelftestReq": hmiSelftestReq,
       "hmiPortEnableReq": hmiPortEnableReq,
       "hmiPortDisableReq": hmiPortDisableReq,
       "hmiStatusReq": hmiStatusReq,
       "hmiRepeaterReq": hmiRepeaterReq,
       "hmiPortObjectsReq": hmiPortObjectsReq,
       "hmiPortChangesReq": hmiPortChangesReq,
       "hmiSelfTestStatReq": hmiSelfTestStatReq,
       "hmiDebugOnReq": hmiDebugOnReq,
       "hmiDebugOffReq": hmiDebugOffReq,
       "hmiGetInfoResp": hmiGetInfoResp,
       "hmiSelfTestResp": hmiSelfTestResp,
       "hmiStatusResp": hmiStatusResp,
       "hmiRepeaterResp": hmiRepeaterResp,
       "hmiPortObjectsResp": hmiPortObjectsResp,
       "hmiPortChangesResp": hmiPortChangesResp,
       "hmiSelfTestStatResp": hmiSelfTestStatResp,
       "in3000StatsUart": in3000StatsUart,
       "uartInOctets": uartInOctets,
       "uartOutOctets": uartOutOctets,
       "uartInDelivers": uartInDelivers,
       "uartOutDelivers": uartOutDelivers,
       "uartBaudRate": uartBaudRate,
       "uartDataBits": uartDataBits,
       "uartStopBits": uartStopBits,
       "uartParity": uartParity,
       "uartHandshaking": uartHandshaking,
       "uartOverrunErrors": uartOverrunErrors,
       "uartParityErrors": uartParityErrors,
       "uartFramingErrors": uartFramingErrors,
       "uartBreakIndicators": uartBreakIndicators,
       "in3000SelfTests": in3000SelfTests,
       "dallasTest": dallasTest,
       "flashTest": flashTest,
       "uartTest": uartTest,
       "nicTest": nicTest,
       "netioTest": netioTest,
       "heapTest": heapTest}
)
