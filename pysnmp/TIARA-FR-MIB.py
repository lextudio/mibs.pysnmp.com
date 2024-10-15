# SNMP MIB module (TIARA-FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:33 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(bundleId,) = mibBuilder.importSymbols(
    "TIARA-BUNDLE-MIB",
    "bundleId")

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraFrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16)
)
tiaraFrMib.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FrTable_Object = MibTable
frTable = _FrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1)
)
if mibBuilder.loadTexts:
    frTable.setStatus("current")
_FrTableEntry_Object = MibTableRow
frTableEntry = _FrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1)
)
frTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    frTableEntry.setStatus("current")


class _FrIfEnable_Type(TruthValue):
    """Custom type frIfEnable based on TruthValue"""


_FrIfEnable_Object = MibTableColumn
frIfEnable = _FrIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 1),
    _FrIfEnable_Type()
)
frIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIfEnable.setStatus("current")


class _FrEnablePvcAll_Type(TruthValue):
    """Custom type frEnablePvcAll based on TruthValue"""


_FrEnablePvcAll_Object = MibTableColumn
frEnablePvcAll = _FrEnablePvcAll_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 2),
    _FrEnablePvcAll_Type()
)
frEnablePvcAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frEnablePvcAll.setStatus("current")


class _FrFrameSize_Type(Integer32):
    """Custom type frFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_FrFrameSize_Type.__name__ = "Integer32"
_FrFrameSize_Object = MibTableColumn
frFrameSize = _FrFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 3),
    _FrFrameSize_Type()
)
frFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    frFrameSize.setUnits("bytes")


class _FrIfType_Type(Integer32):
    """Custom type frIfType based on Integer32"""
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
        *(("dce", 1),
          ("dte", 2),
          ("nni", 3))
    )


_FrIfType_Type.__name__ = "Integer32"
_FrIfType_Object = MibTableColumn
frIfType = _FrIfType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 4),
    _FrIfType_Type()
)
frIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frIfType.setStatus("current")


class _FrLmiType_Type(Integer32):
    """Custom type frLmiType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 3),
          ("cisco", 2),
          ("none", 0),
          ("q933a", 4))
    )


_FrLmiType_Type.__name__ = "Integer32"
_FrLmiType_Object = MibTableColumn
frLmiType = _FrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 5),
    _FrLmiType_Type()
)
frLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiType.setStatus("current")


class _FrLmiDceN392_Type(Integer32):
    """Custom type frLmiDceN392 based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiDceN392_Type.__name__ = "Integer32"
_FrLmiDceN392_Object = MibTableColumn
frLmiDceN392 = _FrLmiDceN392_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 6),
    _FrLmiDceN392_Type()
)
frLmiDceN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiDceN392.setStatus("current")


class _FrLmiDceN393_Type(Integer32):
    """Custom type frLmiDceN393 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiDceN393_Type.__name__ = "Integer32"
_FrLmiDceN393_Object = MibTableColumn
frLmiDceN393 = _FrLmiDceN393_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 7),
    _FrLmiDceN393_Type()
)
frLmiDceN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiDceN393.setStatus("current")


class _FrLmiDteN392_Type(Integer32):
    """Custom type frLmiDteN392 based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiDteN392_Type.__name__ = "Integer32"
_FrLmiDteN392_Object = MibTableColumn
frLmiDteN392 = _FrLmiDteN392_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 8),
    _FrLmiDteN392_Type()
)
frLmiDteN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiDteN392.setStatus("current")


class _FrLmiDteN393_Type(Integer32):
    """Custom type frLmiDteN393 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrLmiDteN393_Type.__name__ = "Integer32"
_FrLmiDteN393_Object = MibTableColumn
frLmiDteN393 = _FrLmiDteN393_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 9),
    _FrLmiDteN393_Type()
)
frLmiDteN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiDteN393.setStatus("current")


class _FrLmiDteN391_Type(Integer32):
    """Custom type frLmiDteN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrLmiDteN391_Type.__name__ = "Integer32"
_FrLmiDteN391_Object = MibTableColumn
frLmiDteN391 = _FrLmiDteN391_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 10),
    _FrLmiDteN391_Type()
)
frLmiDteN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiDteN391.setStatus("current")


class _FrLmiKeepalive_Type(Integer32):
    """Custom type frLmiKeepalive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_FrLmiKeepalive_Type.__name__ = "Integer32"
_FrLmiKeepalive_Object = MibTableColumn
frLmiKeepalive = _FrLmiKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 11),
    _FrLmiKeepalive_Type()
)
frLmiKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frLmiKeepalive.setStatus("current")


class _MfrAckMsgTimer_Type(Integer32):
    """Custom type mfrAckMsgTimer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MfrAckMsgTimer_Type.__name__ = "Integer32"
_MfrAckMsgTimer_Object = MibTableColumn
mfrAckMsgTimer = _MfrAckMsgTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 12),
    _MfrAckMsgTimer_Type()
)
mfrAckMsgTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrAckMsgTimer.setStatus("current")


class _MfrAckMsgMaxRetry_Type(Integer32):
    """Custom type mfrAckMsgMaxRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_MfrAckMsgMaxRetry_Type.__name__ = "Integer32"
_MfrAckMsgMaxRetry_Object = MibTableColumn
mfrAckMsgMaxRetry = _MfrAckMsgMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 13),
    _MfrAckMsgMaxRetry_Type()
)
mfrAckMsgMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrAckMsgMaxRetry.setStatus("current")


class _MfrClass_Type(Integer32):
    """Custom type mfrClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("classA", 1),
          ("classB", 2),
          ("classC", 3))
    )


_MfrClass_Type.__name__ = "Integer32"
_MfrClass_Object = MibTableColumn
mfrClass = _MfrClass_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 14),
    _MfrClass_Type()
)
mfrClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrClass.setStatus("current")


class _MfrClassThreshold_Type(Integer32):
    """Custom type mfrClassThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_MfrClassThreshold_Type.__name__ = "Integer32"
_MfrClassThreshold_Object = MibTableColumn
mfrClassThreshold = _MfrClassThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 15),
    _MfrClassThreshold_Type()
)
mfrClassThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrClassThreshold.setStatus("current")


class _MfrFrameSize_Type(Integer32):
    """Custom type mfrFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_MfrFrameSize_Type.__name__ = "Integer32"
_MfrFrameSize_Object = MibTableColumn
mfrFrameSize = _MfrFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 16),
    _MfrFrameSize_Type()
)
mfrFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrFrameSize.setStatus("current")


class _MfrHelloTimer_Type(Integer32):
    """Custom type mfrHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_MfrHelloTimer_Type.__name__ = "Integer32"
_MfrHelloTimer_Object = MibTableColumn
mfrHelloTimer = _MfrHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 17),
    _MfrHelloTimer_Type()
)
mfrHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrHelloTimer.setStatus("current")


class _MfrSegThreshold_Type(Integer32):
    """Custom type mfrSegThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_MfrSegThreshold_Type.__name__ = "Integer32"
_MfrSegThreshold_Object = MibTableColumn
mfrSegThreshold = _MfrSegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 18),
    _MfrSegThreshold_Type()
)
mfrSegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrSegThreshold.setStatus("current")


class _MfrDiffDelay_Type(Integer32):
    """Custom type mfrDiffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 128),
    )


_MfrDiffDelay_Type.__name__ = "Integer32"
_MfrDiffDelay_Object = MibTableColumn
mfrDiffDelay = _MfrDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 1, 1, 19),
    _MfrDiffDelay_Type()
)
mfrDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mfrDiffDelay.setStatus("current")
_FrPvcTable_Object = MibTable
frPvcTable = _FrPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2)
)
if mibBuilder.loadTexts:
    frPvcTable.setStatus("current")
_FrPvcTableEntry_Object = MibTableRow
frPvcTableEntry = _FrPvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1)
)
frPvcTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
    (0, "TIARA-FR-MIB", "frPvcDlci"),
)
if mibBuilder.loadTexts:
    frPvcTableEntry.setStatus("current")


class _FrPvcDlci_Type(Integer32):
    """Custom type frPvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_FrPvcDlci_Type.__name__ = "Integer32"
_FrPvcDlci_Object = MibTableColumn
frPvcDlci = _FrPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 1),
    _FrPvcDlci_Type()
)
frPvcDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    frPvcDlci.setStatus("current")


class _FrPvcEnable_Type(TruthValue):
    """Custom type frPvcEnable based on TruthValue"""


_FrPvcEnable_Object = MibTableColumn
frPvcEnable = _FrPvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 2),
    _FrPvcEnable_Type()
)
frPvcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcEnable.setStatus("current")
_FrPvcDescr_Type = DisplayString
_FrPvcDescr_Object = MibTableColumn
frPvcDescr = _FrPvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 3),
    _FrPvcDescr_Type()
)
frPvcDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcDescr.setStatus("current")
_FrPvcIpAddr_Type = IpAddress
_FrPvcIpAddr_Object = MibTableColumn
frPvcIpAddr = _FrPvcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 4),
    _FrPvcIpAddr_Type()
)
frPvcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcIpAddr.setStatus("current")
_FrPvcIpSubnetMask_Type = IpAddress
_FrPvcIpSubnetMask_Object = MibTableColumn
frPvcIpSubnetMask = _FrPvcIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 5),
    _FrPvcIpSubnetMask_Type()
)
frPvcIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcIpSubnetMask.setStatus("current")
_FrPvcSrcForwardingPrimary_Type = IpAddress
_FrPvcSrcForwardingPrimary_Object = MibTableColumn
frPvcSrcForwardingPrimary = _FrPvcSrcForwardingPrimary_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 6),
    _FrPvcSrcForwardingPrimary_Type()
)
frPvcSrcForwardingPrimary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcSrcForwardingPrimary.setStatus("current")
_FrPvcSrcForwardingSecondary_Type = IpAddress
_FrPvcSrcForwardingSecondary_Object = MibTableColumn
frPvcSrcForwardingSecondary = _FrPvcSrcForwardingSecondary_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 7),
    _FrPvcSrcForwardingSecondary_Type()
)
frPvcSrcForwardingSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcSrcForwardingSecondary.setStatus("current")
_FrPvcRemoteIpAddr_Type = IpAddress
_FrPvcRemoteIpAddr_Object = MibTableColumn
frPvcRemoteIpAddr = _FrPvcRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 8),
    _FrPvcRemoteIpAddr_Type()
)
frPvcRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcRemoteIpAddr.setStatus("current")


class _FrPvcPolicingEnable_Type(Integer32):
    """Custom type frPvcPolicingEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("standard", 2))
    )


_FrPvcPolicingEnable_Type.__name__ = "Integer32"
_FrPvcPolicingEnable_Object = MibTableColumn
frPvcPolicingEnable = _FrPvcPolicingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 9),
    _FrPvcPolicingEnable_Type()
)
frPvcPolicingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcPolicingEnable.setStatus("current")


class _FrPvcPolicingDe_Type(TruthValue):
    """Custom type frPvcPolicingDe based on TruthValue"""


_FrPvcPolicingDe_Object = MibTableColumn
frPvcPolicingDe = _FrPvcPolicingDe_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 10),
    _FrPvcPolicingDe_Type()
)
frPvcPolicingDe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcPolicingDe.setStatus("current")
_FrPvcPolicingCir_Type = Integer32
_FrPvcPolicingCir_Object = MibTableColumn
frPvcPolicingCir = _FrPvcPolicingCir_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 11),
    _FrPvcPolicingCir_Type()
)
frPvcPolicingCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcPolicingCir.setStatus("current")
if mibBuilder.loadTexts:
    frPvcPolicingCir.setUnits("bps")
_FrPvcPolicingBc_Type = Integer32
_FrPvcPolicingBc_Object = MibTableColumn
frPvcPolicingBc = _FrPvcPolicingBc_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 12),
    _FrPvcPolicingBc_Type()
)
frPvcPolicingBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcPolicingBc.setStatus("current")
if mibBuilder.loadTexts:
    frPvcPolicingBc.setUnits("bps")


class _FrPvcPolicingBe_Type(Integer32):
    """Custom type frPvcPolicingBe based on Integer32"""
    defaultValue = 0


_FrPvcPolicingBe_Object = MibTableColumn
frPvcPolicingBe = _FrPvcPolicingBe_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 13),
    _FrPvcPolicingBe_Type()
)
frPvcPolicingBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcPolicingBe.setStatus("current")
_FrPvcShapingCir_Type = Integer32
_FrPvcShapingCir_Object = MibTableColumn
frPvcShapingCir = _FrPvcShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 14),
    _FrPvcShapingCir_Type()
)
frPvcShapingCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcShapingCir.setStatus("current")
if mibBuilder.loadTexts:
    frPvcShapingCir.setUnits("bps")
_FrPvcShapingBcMax_Type = Integer32
_FrPvcShapingBcMax_Object = MibTableColumn
frPvcShapingBcMax = _FrPvcShapingBcMax_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 15),
    _FrPvcShapingBcMax_Type()
)
frPvcShapingBcMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcShapingBcMax.setStatus("current")
if mibBuilder.loadTexts:
    frPvcShapingBcMax.setUnits("bps")
_FrPvcShapingBcMin_Type = Integer32
_FrPvcShapingBcMin_Object = MibTableColumn
frPvcShapingBcMin = _FrPvcShapingBcMin_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 16),
    _FrPvcShapingBcMin_Type()
)
frPvcShapingBcMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcShapingBcMin.setStatus("current")
if mibBuilder.loadTexts:
    frPvcShapingBcMin.setUnits("bps")


class _FrPvcShapingBe_Type(Integer32):
    """Custom type frPvcShapingBe based on Integer32"""
    defaultValue = 0


_FrPvcShapingBe_Object = MibTableColumn
frPvcShapingBe = _FrPvcShapingBe_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 17),
    _FrPvcShapingBe_Type()
)
frPvcShapingBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcShapingBe.setStatus("current")
_FrPvcDlciForSwitching_Type = Integer32
_FrPvcDlciForSwitching_Object = MibTableColumn
frPvcDlciForSwitching = _FrPvcDlciForSwitching_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 18),
    _FrPvcDlciForSwitching_Type()
)
frPvcDlciForSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcDlciForSwitching.setStatus("current")
_FrPvcBundleNameForSwitching_Type = DisplayString
_FrPvcBundleNameForSwitching_Object = MibTableColumn
frPvcBundleNameForSwitching = _FrPvcBundleNameForSwitching_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 19),
    _FrPvcBundleNameForSwitching_Type()
)
frPvcBundleNameForSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcBundleNameForSwitching.setStatus("current")
_FrPvcRowStatus_Type = RowStatus
_FrPvcRowStatus_Object = MibTableColumn
frPvcRowStatus = _FrPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 2, 1, 20),
    _FrPvcRowStatus_Type()
)
frPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frPvcRowStatus.setStatus("current")
_FrStatsTable_Object = MibTable
frStatsTable = _FrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3)
)
if mibBuilder.loadTexts:
    frStatsTable.setStatus("current")
_FrStatsTableEntry_Object = MibTableRow
frStatsTableEntry = _FrStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1)
)
frStatsTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
)
if mibBuilder.loadTexts:
    frStatsTableEntry.setStatus("current")
_FrStatsFramesRx_Type = Counter32
_FrStatsFramesRx_Object = MibTableColumn
frStatsFramesRx = _FrStatsFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 1),
    _FrStatsFramesRx_Type()
)
frStatsFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsFramesRx.setStatus("current")
_FrStatsInvFramesRx_Type = Counter32
_FrStatsInvFramesRx_Object = MibTableColumn
frStatsInvFramesRx = _FrStatsInvFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 2),
    _FrStatsInvFramesRx_Type()
)
frStatsInvFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsInvFramesRx.setStatus("current")
_FrStatsFECNsRx_Type = Counter32
_FrStatsFECNsRx_Object = MibTableColumn
frStatsFECNsRx = _FrStatsFECNsRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 3),
    _FrStatsFECNsRx_Type()
)
frStatsFECNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsFECNsRx.setStatus("current")
_FrStatsBECNsRx_Type = Counter32
_FrStatsBECNsRx_Object = MibTableColumn
frStatsBECNsRx = _FrStatsBECNsRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 4),
    _FrStatsBECNsRx_Type()
)
frStatsBECNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsBECNsRx.setStatus("current")
_FrStatsShortFramesRx_Type = Counter32
_FrStatsShortFramesRx_Object = MibTableColumn
frStatsShortFramesRx = _FrStatsShortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 5),
    _FrStatsShortFramesRx_Type()
)
frStatsShortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsShortFramesRx.setStatus("current")
_FrStatsLongFramesRx_Type = Counter32
_FrStatsLongFramesRx_Object = MibTableColumn
frStatsLongFramesRx = _FrStatsLongFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 6),
    _FrStatsLongFramesRx_Type()
)
frStatsLongFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsLongFramesRx.setStatus("current")
_FrStatsInvDLCIsRx_Type = Counter32
_FrStatsInvDLCIsRx_Object = MibTableColumn
frStatsInvDLCIsRx = _FrStatsInvDLCIsRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 7),
    _FrStatsInvDLCIsRx_Type()
)
frStatsInvDLCIsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsInvDLCIsRx.setStatus("current")
_FrStatsUnknownDLCIsRx_Type = Counter32
_FrStatsUnknownDLCIsRx_Object = MibTableColumn
frStatsUnknownDLCIsRx = _FrStatsUnknownDLCIsRx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 8),
    _FrStatsUnknownDLCIsRx_Type()
)
frStatsUnknownDLCIsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsUnknownDLCIsRx.setStatus("current")
_FrStatsFramesTx_Type = Counter32
_FrStatsFramesTx_Object = MibTableColumn
frStatsFramesTx = _FrStatsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 3, 1, 9),
    _FrStatsFramesTx_Type()
)
frStatsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frStatsFramesTx.setStatus("current")
_FrPvcStatsTable_Object = MibTable
frPvcStatsTable = _FrPvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4)
)
if mibBuilder.loadTexts:
    frPvcStatsTable.setStatus("current")
_FrPvcStatsTableEntry_Object = MibTableRow
frPvcStatsTableEntry = _FrPvcStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1)
)
frPvcStatsTableEntry.setIndexNames(
    (0, "TIARA-BUNDLE-MIB", "bundleId"),
    (0, "TIARA-FR-MIB", "frPvcDlci"),
)
if mibBuilder.loadTexts:
    frPvcStatsTableEntry.setStatus("current")
_FrPvcStatsBytesRxLastBootOrClear_Type = Counter32
_FrPvcStatsBytesRxLastBootOrClear_Object = MibTableColumn
frPvcStatsBytesRxLastBootOrClear = _FrPvcStatsBytesRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 1),
    _FrPvcStatsBytesRxLastBootOrClear_Type()
)
frPvcStatsBytesRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsBytesRxLastBootOrClear.setStatus("current")
_FrPvcStatsBytesTxLastBootOrClear_Type = Counter32
_FrPvcStatsBytesTxLastBootOrClear_Object = MibTableColumn
frPvcStatsBytesTxLastBootOrClear = _FrPvcStatsBytesTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 2),
    _FrPvcStatsBytesTxLastBootOrClear_Type()
)
frPvcStatsBytesTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsBytesTxLastBootOrClear.setStatus("current")
_FrPvcStatsPktsRxLastBootOrClear_Type = Counter32
_FrPvcStatsPktsRxLastBootOrClear_Object = MibTableColumn
frPvcStatsPktsRxLastBootOrClear = _FrPvcStatsPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 3),
    _FrPvcStatsPktsRxLastBootOrClear_Type()
)
frPvcStatsPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsPktsRxLastBootOrClear.setStatus("current")
_FrPvcStatsPktsTxLastBootOrClear_Type = Counter32
_FrPvcStatsPktsTxLastBootOrClear_Object = MibTableColumn
frPvcStatsPktsTxLastBootOrClear = _FrPvcStatsPktsTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 4),
    _FrPvcStatsPktsTxLastBootOrClear_Type()
)
frPvcStatsPktsTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsPktsTxLastBootOrClear.setStatus("current")
_FrPvcStatsErrPktsRxLastBootOrClear_Type = Counter32
_FrPvcStatsErrPktsRxLastBootOrClear_Object = MibTableColumn
frPvcStatsErrPktsRxLastBootOrClear = _FrPvcStatsErrPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 5),
    _FrPvcStatsErrPktsRxLastBootOrClear_Type()
)
frPvcStatsErrPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsErrPktsRxLastBootOrClear.setStatus("current")
_FrPvcStatsUpDownStatesLastBootOrClear_Type = Counter32
_FrPvcStatsUpDownStatesLastBootOrClear_Object = MibTableColumn
frPvcStatsUpDownStatesLastBootOrClear = _FrPvcStatsUpDownStatesLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 6),
    _FrPvcStatsUpDownStatesLastBootOrClear_Type()
)
frPvcStatsUpDownStatesLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsUpDownStatesLastBootOrClear.setStatus("current")
_FrPvcStatsBytesRxLastFiveMins_Type = Counter32
_FrPvcStatsBytesRxLastFiveMins_Object = MibTableColumn
frPvcStatsBytesRxLastFiveMins = _FrPvcStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 7),
    _FrPvcStatsBytesRxLastFiveMins_Type()
)
frPvcStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsBytesRxLastFiveMins.setStatus("current")
_FrPvcStatsBytesTxLastFiveMins_Type = Counter32
_FrPvcStatsBytesTxLastFiveMins_Object = MibTableColumn
frPvcStatsBytesTxLastFiveMins = _FrPvcStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 8),
    _FrPvcStatsBytesTxLastFiveMins_Type()
)
frPvcStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsBytesTxLastFiveMins.setStatus("current")
_FrPvcStatsPktsRxLastFiveMins_Type = Counter32
_FrPvcStatsPktsRxLastFiveMins_Object = MibTableColumn
frPvcStatsPktsRxLastFiveMins = _FrPvcStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 9),
    _FrPvcStatsPktsRxLastFiveMins_Type()
)
frPvcStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsPktsRxLastFiveMins.setStatus("current")
_FrPvcStatsPktsTxLastFiveMins_Type = Counter32
_FrPvcStatsPktsTxLastFiveMins_Object = MibTableColumn
frPvcStatsPktsTxLastFiveMins = _FrPvcStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 10),
    _FrPvcStatsPktsTxLastFiveMins_Type()
)
frPvcStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsPktsTxLastFiveMins.setStatus("current")
_FrPvcStatsErrPktsRxLastFiveMins_Type = Counter32
_FrPvcStatsErrPktsRxLastFiveMins_Object = MibTableColumn
frPvcStatsErrPktsRxLastFiveMins = _FrPvcStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 11),
    _FrPvcStatsErrPktsRxLastFiveMins_Type()
)
frPvcStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsErrPktsRxLastFiveMins.setStatus("current")
_FrPvcStatsUpDownStatesLastFiveMins_Type = Counter32
_FrPvcStatsUpDownStatesLastFiveMins_Object = MibTableColumn
frPvcStatsUpDownStatesLastFiveMins = _FrPvcStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 16, 4, 1, 12),
    _FrPvcStatsUpDownStatesLastFiveMins_Type()
)
frPvcStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frPvcStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-FR-MIB",
    **{"tiaraFrMib": tiaraFrMib,
       "frTable": frTable,
       "frTableEntry": frTableEntry,
       "frIfEnable": frIfEnable,
       "frEnablePvcAll": frEnablePvcAll,
       "frFrameSize": frFrameSize,
       "frIfType": frIfType,
       "frLmiType": frLmiType,
       "frLmiDceN392": frLmiDceN392,
       "frLmiDceN393": frLmiDceN393,
       "frLmiDteN392": frLmiDteN392,
       "frLmiDteN393": frLmiDteN393,
       "frLmiDteN391": frLmiDteN391,
       "frLmiKeepalive": frLmiKeepalive,
       "mfrAckMsgTimer": mfrAckMsgTimer,
       "mfrAckMsgMaxRetry": mfrAckMsgMaxRetry,
       "mfrClass": mfrClass,
       "mfrClassThreshold": mfrClassThreshold,
       "mfrFrameSize": mfrFrameSize,
       "mfrHelloTimer": mfrHelloTimer,
       "mfrSegThreshold": mfrSegThreshold,
       "mfrDiffDelay": mfrDiffDelay,
       "frPvcTable": frPvcTable,
       "frPvcTableEntry": frPvcTableEntry,
       "frPvcDlci": frPvcDlci,
       "frPvcEnable": frPvcEnable,
       "frPvcDescr": frPvcDescr,
       "frPvcIpAddr": frPvcIpAddr,
       "frPvcIpSubnetMask": frPvcIpSubnetMask,
       "frPvcSrcForwardingPrimary": frPvcSrcForwardingPrimary,
       "frPvcSrcForwardingSecondary": frPvcSrcForwardingSecondary,
       "frPvcRemoteIpAddr": frPvcRemoteIpAddr,
       "frPvcPolicingEnable": frPvcPolicingEnable,
       "frPvcPolicingDe": frPvcPolicingDe,
       "frPvcPolicingCir": frPvcPolicingCir,
       "frPvcPolicingBc": frPvcPolicingBc,
       "frPvcPolicingBe": frPvcPolicingBe,
       "frPvcShapingCir": frPvcShapingCir,
       "frPvcShapingBcMax": frPvcShapingBcMax,
       "frPvcShapingBcMin": frPvcShapingBcMin,
       "frPvcShapingBe": frPvcShapingBe,
       "frPvcDlciForSwitching": frPvcDlciForSwitching,
       "frPvcBundleNameForSwitching": frPvcBundleNameForSwitching,
       "frPvcRowStatus": frPvcRowStatus,
       "frStatsTable": frStatsTable,
       "frStatsTableEntry": frStatsTableEntry,
       "frStatsFramesRx": frStatsFramesRx,
       "frStatsInvFramesRx": frStatsInvFramesRx,
       "frStatsFECNsRx": frStatsFECNsRx,
       "frStatsBECNsRx": frStatsBECNsRx,
       "frStatsShortFramesRx": frStatsShortFramesRx,
       "frStatsLongFramesRx": frStatsLongFramesRx,
       "frStatsInvDLCIsRx": frStatsInvDLCIsRx,
       "frStatsUnknownDLCIsRx": frStatsUnknownDLCIsRx,
       "frStatsFramesTx": frStatsFramesTx,
       "frPvcStatsTable": frPvcStatsTable,
       "frPvcStatsTableEntry": frPvcStatsTableEntry,
       "frPvcStatsBytesRxLastBootOrClear": frPvcStatsBytesRxLastBootOrClear,
       "frPvcStatsBytesTxLastBootOrClear": frPvcStatsBytesTxLastBootOrClear,
       "frPvcStatsPktsRxLastBootOrClear": frPvcStatsPktsRxLastBootOrClear,
       "frPvcStatsPktsTxLastBootOrClear": frPvcStatsPktsTxLastBootOrClear,
       "frPvcStatsErrPktsRxLastBootOrClear": frPvcStatsErrPktsRxLastBootOrClear,
       "frPvcStatsUpDownStatesLastBootOrClear": frPvcStatsUpDownStatesLastBootOrClear,
       "frPvcStatsBytesRxLastFiveMins": frPvcStatsBytesRxLastFiveMins,
       "frPvcStatsBytesTxLastFiveMins": frPvcStatsBytesTxLastFiveMins,
       "frPvcStatsPktsRxLastFiveMins": frPvcStatsPktsRxLastFiveMins,
       "frPvcStatsPktsTxLastFiveMins": frPvcStatsPktsTxLastFiveMins,
       "frPvcStatsErrPktsRxLastFiveMins": frPvcStatsErrPktsRxLastFiveMins,
       "frPvcStatsUpDownStatesLastFiveMins": frPvcStatsUpDownStatesLastFiveMins}
)
