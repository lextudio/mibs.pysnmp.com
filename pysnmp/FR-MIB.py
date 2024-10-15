# SNMP MIB module (FR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:17 2024
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

(nnbundleId,) = mibBuilder.importSymbols(
    "BUNDLE-MIB",
    "nnbundleId")

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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


# MODULE-IDENTITY

nnfrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16)
)
nnfrMib.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnfrTable_Object = MibTable
nnfrTable = _NnfrTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    nnfrTable.setStatus("current")
_NnfrTableEntry_Object = MibTableRow
nnfrTableEntry = _NnfrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1)
)
nnfrTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nnfrTableEntry.setStatus("current")


class _NnfrIfEnable_Type(TruthValue):
    """Custom type nnfrIfEnable based on TruthValue"""


_NnfrIfEnable_Object = MibTableColumn
nnfrIfEnable = _NnfrIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 1),
    _NnfrIfEnable_Type()
)
nnfrIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrIfEnable.setStatus("current")


class _NnfrEnablePvcAll_Type(TruthValue):
    """Custom type nnfrEnablePvcAll based on TruthValue"""


_NnfrEnablePvcAll_Object = MibTableColumn
nnfrEnablePvcAll = _NnfrEnablePvcAll_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 2),
    _NnfrEnablePvcAll_Type()
)
nnfrEnablePvcAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrEnablePvcAll.setStatus("current")


class _NnfrFrameSize_Type(Integer32):
    """Custom type nnfrFrameSize based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_NnfrFrameSize_Type.__name__ = "Integer32"
_NnfrFrameSize_Object = MibTableColumn
nnfrFrameSize = _NnfrFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 3),
    _NnfrFrameSize_Type()
)
nnfrFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrFrameSize.setStatus("current")
if mibBuilder.loadTexts:
    nnfrFrameSize.setUnits("bytes")


class _NnfrIfType_Type(Integer32):
    """Custom type nnfrIfType based on Integer32"""
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


_NnfrIfType_Type.__name__ = "Integer32"
_NnfrIfType_Object = MibTableColumn
nnfrIfType = _NnfrIfType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 4),
    _NnfrIfType_Type()
)
nnfrIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrIfType.setStatus("current")


class _NnfrLmiType_Type(Integer32):
    """Custom type nnfrLmiType based on Integer32"""
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


_NnfrLmiType_Type.__name__ = "Integer32"
_NnfrLmiType_Object = MibTableColumn
nnfrLmiType = _NnfrLmiType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 5),
    _NnfrLmiType_Type()
)
nnfrLmiType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiType.setStatus("current")


class _NnfrLmiDceN392_Type(Integer32):
    """Custom type nnfrLmiDceN392 based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnfrLmiDceN392_Type.__name__ = "Integer32"
_NnfrLmiDceN392_Object = MibTableColumn
nnfrLmiDceN392 = _NnfrLmiDceN392_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 6),
    _NnfrLmiDceN392_Type()
)
nnfrLmiDceN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiDceN392.setStatus("current")


class _NnfrLmiDceN393_Type(Integer32):
    """Custom type nnfrLmiDceN393 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnfrLmiDceN393_Type.__name__ = "Integer32"
_NnfrLmiDceN393_Object = MibTableColumn
nnfrLmiDceN393 = _NnfrLmiDceN393_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 7),
    _NnfrLmiDceN393_Type()
)
nnfrLmiDceN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiDceN393.setStatus("current")


class _NnfrLmiDteN392_Type(Integer32):
    """Custom type nnfrLmiDteN392 based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnfrLmiDteN392_Type.__name__ = "Integer32"
_NnfrLmiDteN392_Object = MibTableColumn
nnfrLmiDteN392 = _NnfrLmiDteN392_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 8),
    _NnfrLmiDteN392_Type()
)
nnfrLmiDteN392.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiDteN392.setStatus("current")


class _NnfrLmiDteN393_Type(Integer32):
    """Custom type nnfrLmiDteN393 based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnfrLmiDteN393_Type.__name__ = "Integer32"
_NnfrLmiDteN393_Object = MibTableColumn
nnfrLmiDteN393 = _NnfrLmiDteN393_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 9),
    _NnfrLmiDteN393_Type()
)
nnfrLmiDteN393.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiDteN393.setStatus("current")


class _NnfrLmiDteN391_Type(Integer32):
    """Custom type nnfrLmiDteN391 based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NnfrLmiDteN391_Type.__name__ = "Integer32"
_NnfrLmiDteN391_Object = MibTableColumn
nnfrLmiDteN391 = _NnfrLmiDteN391_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 10),
    _NnfrLmiDteN391_Type()
)
nnfrLmiDteN391.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiDteN391.setStatus("current")


class _NnfrLmiKeepalive_Type(Integer32):
    """Custom type nnfrLmiKeepalive based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_NnfrLmiKeepalive_Type.__name__ = "Integer32"
_NnfrLmiKeepalive_Object = MibTableColumn
nnfrLmiKeepalive = _NnfrLmiKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 11),
    _NnfrLmiKeepalive_Type()
)
nnfrLmiKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrLmiKeepalive.setStatus("current")


class _NnmfrAckMsgTimer_Type(Integer32):
    """Custom type nnmfrAckMsgTimer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NnmfrAckMsgTimer_Type.__name__ = "Integer32"
_NnmfrAckMsgTimer_Object = MibTableColumn
nnmfrAckMsgTimer = _NnmfrAckMsgTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 12),
    _NnmfrAckMsgTimer_Type()
)
nnmfrAckMsgTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrAckMsgTimer.setStatus("current")


class _NnmfrAckMsgMaxRetry_Type(Integer32):
    """Custom type nnmfrAckMsgMaxRetry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_NnmfrAckMsgMaxRetry_Type.__name__ = "Integer32"
_NnmfrAckMsgMaxRetry_Object = MibTableColumn
nnmfrAckMsgMaxRetry = _NnmfrAckMsgMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 13),
    _NnmfrAckMsgMaxRetry_Type()
)
nnmfrAckMsgMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrAckMsgMaxRetry.setStatus("current")


class _NnmfrClass_Type(Integer32):
    """Custom type nnmfrClass based on Integer32"""
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


_NnmfrClass_Type.__name__ = "Integer32"
_NnmfrClass_Object = MibTableColumn
nnmfrClass = _NnmfrClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 14),
    _NnmfrClass_Type()
)
nnmfrClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrClass.setStatus("current")


class _NnmfrClassThreshold_Type(Integer32):
    """Custom type nnmfrClassThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_NnmfrClassThreshold_Type.__name__ = "Integer32"
_NnmfrClassThreshold_Object = MibTableColumn
nnmfrClassThreshold = _NnmfrClassThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 15),
    _NnmfrClassThreshold_Type()
)
nnmfrClassThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrClassThreshold.setStatus("current")


class _NnmfrFrameSize_Type(Integer32):
    """Custom type nnmfrFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_NnmfrFrameSize_Type.__name__ = "Integer32"
_NnmfrFrameSize_Object = MibTableColumn
nnmfrFrameSize = _NnmfrFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 16),
    _NnmfrFrameSize_Type()
)
nnmfrFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrFrameSize.setStatus("current")


class _NnmfrHelloTimer_Type(Integer32):
    """Custom type nnmfrHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_NnmfrHelloTimer_Type.__name__ = "Integer32"
_NnmfrHelloTimer_Object = MibTableColumn
nnmfrHelloTimer = _NnmfrHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 17),
    _NnmfrHelloTimer_Type()
)
nnmfrHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrHelloTimer.setStatus("current")


class _NnmfrSegThreshold_Type(Integer32):
    """Custom type nnmfrSegThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_NnmfrSegThreshold_Type.__name__ = "Integer32"
_NnmfrSegThreshold_Object = MibTableColumn
nnmfrSegThreshold = _NnmfrSegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 18),
    _NnmfrSegThreshold_Type()
)
nnmfrSegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrSegThreshold.setStatus("current")


class _NnmfrDiffDelay_Type(Integer32):
    """Custom type nnmfrDiffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 128),
    )


_NnmfrDiffDelay_Type.__name__ = "Integer32"
_NnmfrDiffDelay_Object = MibTableColumn
nnmfrDiffDelay = _NnmfrDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 1, 1, 19),
    _NnmfrDiffDelay_Type()
)
nnmfrDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnmfrDiffDelay.setStatus("current")
_NnfrPvcTable_Object = MibTable
nnfrPvcTable = _NnfrPvcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2)
)
if mibBuilder.loadTexts:
    nnfrPvcTable.setStatus("current")
_NnfrPvcTableEntry_Object = MibTableRow
nnfrPvcTableEntry = _NnfrPvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1)
)
nnfrPvcTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
    (0, "FR-MIB", "nnfrPvcDlci"),
)
if mibBuilder.loadTexts:
    nnfrPvcTableEntry.setStatus("current")


class _NnfrPvcDlci_Type(Integer32):
    """Custom type nnfrPvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NnfrPvcDlci_Type.__name__ = "Integer32"
_NnfrPvcDlci_Object = MibTableColumn
nnfrPvcDlci = _NnfrPvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 1),
    _NnfrPvcDlci_Type()
)
nnfrPvcDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnfrPvcDlci.setStatus("current")


class _NnfrPvcEnable_Type(TruthValue):
    """Custom type nnfrPvcEnable based on TruthValue"""


_NnfrPvcEnable_Object = MibTableColumn
nnfrPvcEnable = _NnfrPvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 2),
    _NnfrPvcEnable_Type()
)
nnfrPvcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcEnable.setStatus("current")
_NnfrPvcDescr_Type = DisplayString
_NnfrPvcDescr_Object = MibTableColumn
nnfrPvcDescr = _NnfrPvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 3),
    _NnfrPvcDescr_Type()
)
nnfrPvcDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcDescr.setStatus("current")
_NnfrPvcIpAddr_Type = IpAddress
_NnfrPvcIpAddr_Object = MibTableColumn
nnfrPvcIpAddr = _NnfrPvcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 4),
    _NnfrPvcIpAddr_Type()
)
nnfrPvcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcIpAddr.setStatus("current")
_NnfrPvcIpSubnetMask_Type = IpAddress
_NnfrPvcIpSubnetMask_Object = MibTableColumn
nnfrPvcIpSubnetMask = _NnfrPvcIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 5),
    _NnfrPvcIpSubnetMask_Type()
)
nnfrPvcIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcIpSubnetMask.setStatus("current")
_NnfrPvcRemoteIpAddr_Type = IpAddress
_NnfrPvcRemoteIpAddr_Object = MibTableColumn
nnfrPvcRemoteIpAddr = _NnfrPvcRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 6),
    _NnfrPvcRemoteIpAddr_Type()
)
nnfrPvcRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcRemoteIpAddr.setStatus("current")


class _NnfrPvcPolicingEnable_Type(Integer32):
    """Custom type nnfrPvcPolicingEnable based on Integer32"""
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


_NnfrPvcPolicingEnable_Type.__name__ = "Integer32"
_NnfrPvcPolicingEnable_Object = MibTableColumn
nnfrPvcPolicingEnable = _NnfrPvcPolicingEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 7),
    _NnfrPvcPolicingEnable_Type()
)
nnfrPvcPolicingEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcPolicingEnable.setStatus("current")


class _NnfrPvcPolicingDe_Type(TruthValue):
    """Custom type nnfrPvcPolicingDe based on TruthValue"""


_NnfrPvcPolicingDe_Object = MibTableColumn
nnfrPvcPolicingDe = _NnfrPvcPolicingDe_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 8),
    _NnfrPvcPolicingDe_Type()
)
nnfrPvcPolicingDe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcPolicingDe.setStatus("current")
_NnfrPvcPolicingCir_Type = Integer32
_NnfrPvcPolicingCir_Object = MibTableColumn
nnfrPvcPolicingCir = _NnfrPvcPolicingCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 9),
    _NnfrPvcPolicingCir_Type()
)
nnfrPvcPolicingCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcPolicingCir.setStatus("current")
if mibBuilder.loadTexts:
    nnfrPvcPolicingCir.setUnits("bps")
_NnfrPvcPolicingBc_Type = Integer32
_NnfrPvcPolicingBc_Object = MibTableColumn
nnfrPvcPolicingBc = _NnfrPvcPolicingBc_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 10),
    _NnfrPvcPolicingBc_Type()
)
nnfrPvcPolicingBc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcPolicingBc.setStatus("current")
if mibBuilder.loadTexts:
    nnfrPvcPolicingBc.setUnits("bps")


class _NnfrPvcPolicingBe_Type(Integer32):
    """Custom type nnfrPvcPolicingBe based on Integer32"""
    defaultValue = 0


_NnfrPvcPolicingBe_Object = MibTableColumn
nnfrPvcPolicingBe = _NnfrPvcPolicingBe_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 11),
    _NnfrPvcPolicingBe_Type()
)
nnfrPvcPolicingBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcPolicingBe.setStatus("current")
_NnfrPvcShapingCir_Type = Integer32
_NnfrPvcShapingCir_Object = MibTableColumn
nnfrPvcShapingCir = _NnfrPvcShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 12),
    _NnfrPvcShapingCir_Type()
)
nnfrPvcShapingCir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcShapingCir.setStatus("current")
if mibBuilder.loadTexts:
    nnfrPvcShapingCir.setUnits("bps")
_NnfrPvcShapingBcMax_Type = Integer32
_NnfrPvcShapingBcMax_Object = MibTableColumn
nnfrPvcShapingBcMax = _NnfrPvcShapingBcMax_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 13),
    _NnfrPvcShapingBcMax_Type()
)
nnfrPvcShapingBcMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcShapingBcMax.setStatus("current")
if mibBuilder.loadTexts:
    nnfrPvcShapingBcMax.setUnits("bps")
_NnfrPvcShapingBcMin_Type = Integer32
_NnfrPvcShapingBcMin_Object = MibTableColumn
nnfrPvcShapingBcMin = _NnfrPvcShapingBcMin_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 14),
    _NnfrPvcShapingBcMin_Type()
)
nnfrPvcShapingBcMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcShapingBcMin.setStatus("current")
if mibBuilder.loadTexts:
    nnfrPvcShapingBcMin.setUnits("bps")


class _NnfrPvcShapingBe_Type(Integer32):
    """Custom type nnfrPvcShapingBe based on Integer32"""
    defaultValue = 0


_NnfrPvcShapingBe_Object = MibTableColumn
nnfrPvcShapingBe = _NnfrPvcShapingBe_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 15),
    _NnfrPvcShapingBe_Type()
)
nnfrPvcShapingBe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcShapingBe.setStatus("current")
_NnfrPvcDlciForSwitching_Type = Integer32
_NnfrPvcDlciForSwitching_Object = MibTableColumn
nnfrPvcDlciForSwitching = _NnfrPvcDlciForSwitching_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 16),
    _NnfrPvcDlciForSwitching_Type()
)
nnfrPvcDlciForSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcDlciForSwitching.setStatus("current")
_NnfrPvcBundleNameForSwitching_Type = DisplayString
_NnfrPvcBundleNameForSwitching_Object = MibTableColumn
nnfrPvcBundleNameForSwitching = _NnfrPvcBundleNameForSwitching_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 17),
    _NnfrPvcBundleNameForSwitching_Type()
)
nnfrPvcBundleNameForSwitching.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcBundleNameForSwitching.setStatus("current")
_NnfrPvcRowStatus_Type = RowStatus
_NnfrPvcRowStatus_Object = MibTableColumn
nnfrPvcRowStatus = _NnfrPvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 2, 1, 18),
    _NnfrPvcRowStatus_Type()
)
nnfrPvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrPvcRowStatus.setStatus("current")
_NnfrStatsTable_Object = MibTable
nnfrStatsTable = _NnfrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3)
)
if mibBuilder.loadTexts:
    nnfrStatsTable.setStatus("current")
_NnfrStatsTableEntry_Object = MibTableRow
nnfrStatsTableEntry = _NnfrStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1)
)
nnfrStatsTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
)
if mibBuilder.loadTexts:
    nnfrStatsTableEntry.setStatus("current")
_NnfrStatsFramesRx_Type = Counter32
_NnfrStatsFramesRx_Object = MibTableColumn
nnfrStatsFramesRx = _NnfrStatsFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 1),
    _NnfrStatsFramesRx_Type()
)
nnfrStatsFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsFramesRx.setStatus("current")
_NnfrStatsInvFramesRx_Type = Counter32
_NnfrStatsInvFramesRx_Object = MibTableColumn
nnfrStatsInvFramesRx = _NnfrStatsInvFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 2),
    _NnfrStatsInvFramesRx_Type()
)
nnfrStatsInvFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsInvFramesRx.setStatus("current")
_NnfrStatsFECNsRx_Type = Counter32
_NnfrStatsFECNsRx_Object = MibTableColumn
nnfrStatsFECNsRx = _NnfrStatsFECNsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 3),
    _NnfrStatsFECNsRx_Type()
)
nnfrStatsFECNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsFECNsRx.setStatus("current")
_NnfrStatsBECNsRx_Type = Counter32
_NnfrStatsBECNsRx_Object = MibTableColumn
nnfrStatsBECNsRx = _NnfrStatsBECNsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 4),
    _NnfrStatsBECNsRx_Type()
)
nnfrStatsBECNsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsBECNsRx.setStatus("current")
_NnfrStatsShortFramesRx_Type = Counter32
_NnfrStatsShortFramesRx_Object = MibTableColumn
nnfrStatsShortFramesRx = _NnfrStatsShortFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 5),
    _NnfrStatsShortFramesRx_Type()
)
nnfrStatsShortFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsShortFramesRx.setStatus("current")
_NnfrStatsLongFramesRx_Type = Counter32
_NnfrStatsLongFramesRx_Object = MibTableColumn
nnfrStatsLongFramesRx = _NnfrStatsLongFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 6),
    _NnfrStatsLongFramesRx_Type()
)
nnfrStatsLongFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsLongFramesRx.setStatus("current")
_NnfrStatsInvDLCIsRx_Type = Counter32
_NnfrStatsInvDLCIsRx_Object = MibTableColumn
nnfrStatsInvDLCIsRx = _NnfrStatsInvDLCIsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 7),
    _NnfrStatsInvDLCIsRx_Type()
)
nnfrStatsInvDLCIsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsInvDLCIsRx.setStatus("current")
_NnfrStatsUnknownDLCIsRx_Type = Counter32
_NnfrStatsUnknownDLCIsRx_Object = MibTableColumn
nnfrStatsUnknownDLCIsRx = _NnfrStatsUnknownDLCIsRx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 8),
    _NnfrStatsUnknownDLCIsRx_Type()
)
nnfrStatsUnknownDLCIsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsUnknownDLCIsRx.setStatus("current")
_NnfrStatsFramesTx_Type = Counter32
_NnfrStatsFramesTx_Object = MibTableColumn
nnfrStatsFramesTx = _NnfrStatsFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 3, 1, 9),
    _NnfrStatsFramesTx_Type()
)
nnfrStatsFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrStatsFramesTx.setStatus("current")
_NnfrPvcStatsTable_Object = MibTable
nnfrPvcStatsTable = _NnfrPvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4)
)
if mibBuilder.loadTexts:
    nnfrPvcStatsTable.setStatus("current")
_NnfrPvcStatsTableEntry_Object = MibTableRow
nnfrPvcStatsTableEntry = _NnfrPvcStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1)
)
nnfrPvcStatsTableEntry.setIndexNames(
    (0, "BUNDLE-MIB", "nnbundleId"),
    (0, "FR-MIB", "nnfrPvcDlci"),
)
if mibBuilder.loadTexts:
    nnfrPvcStatsTableEntry.setStatus("current")
_NnfrPvcStatsBytesRxLastBootOrClear_Type = Counter32
_NnfrPvcStatsBytesRxLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsBytesRxLastBootOrClear = _NnfrPvcStatsBytesRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 1),
    _NnfrPvcStatsBytesRxLastBootOrClear_Type()
)
nnfrPvcStatsBytesRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsBytesRxLastBootOrClear.setStatus("current")
_NnfrPvcStatsBytesTxLastBootOrClear_Type = Counter32
_NnfrPvcStatsBytesTxLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsBytesTxLastBootOrClear = _NnfrPvcStatsBytesTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 2),
    _NnfrPvcStatsBytesTxLastBootOrClear_Type()
)
nnfrPvcStatsBytesTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsBytesTxLastBootOrClear.setStatus("current")
_NnfrPvcStatsPktsRxLastBootOrClear_Type = Counter32
_NnfrPvcStatsPktsRxLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsPktsRxLastBootOrClear = _NnfrPvcStatsPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 3),
    _NnfrPvcStatsPktsRxLastBootOrClear_Type()
)
nnfrPvcStatsPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsPktsRxLastBootOrClear.setStatus("current")
_NnfrPvcStatsPktsTxLastBootOrClear_Type = Counter32
_NnfrPvcStatsPktsTxLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsPktsTxLastBootOrClear = _NnfrPvcStatsPktsTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 4),
    _NnfrPvcStatsPktsTxLastBootOrClear_Type()
)
nnfrPvcStatsPktsTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsPktsTxLastBootOrClear.setStatus("current")
_NnfrPvcStatsErrPktsRxLastBootOrClear_Type = Counter32
_NnfrPvcStatsErrPktsRxLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsErrPktsRxLastBootOrClear = _NnfrPvcStatsErrPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 5),
    _NnfrPvcStatsErrPktsRxLastBootOrClear_Type()
)
nnfrPvcStatsErrPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsErrPktsRxLastBootOrClear.setStatus("current")
_NnfrPvcStatsUpDownStatesLastBootOrClear_Type = Counter32
_NnfrPvcStatsUpDownStatesLastBootOrClear_Object = MibTableColumn
nnfrPvcStatsUpDownStatesLastBootOrClear = _NnfrPvcStatsUpDownStatesLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 6),
    _NnfrPvcStatsUpDownStatesLastBootOrClear_Type()
)
nnfrPvcStatsUpDownStatesLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsUpDownStatesLastBootOrClear.setStatus("current")
_NnfrPvcStatsBytesRxLastFiveMins_Type = Counter32
_NnfrPvcStatsBytesRxLastFiveMins_Object = MibTableColumn
nnfrPvcStatsBytesRxLastFiveMins = _NnfrPvcStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 7),
    _NnfrPvcStatsBytesRxLastFiveMins_Type()
)
nnfrPvcStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsBytesRxLastFiveMins.setStatus("current")
_NnfrPvcStatsBytesTxLastFiveMins_Type = Counter32
_NnfrPvcStatsBytesTxLastFiveMins_Object = MibTableColumn
nnfrPvcStatsBytesTxLastFiveMins = _NnfrPvcStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 8),
    _NnfrPvcStatsBytesTxLastFiveMins_Type()
)
nnfrPvcStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsBytesTxLastFiveMins.setStatus("current")
_NnfrPvcStatsPktsRxLastFiveMins_Type = Counter32
_NnfrPvcStatsPktsRxLastFiveMins_Object = MibTableColumn
nnfrPvcStatsPktsRxLastFiveMins = _NnfrPvcStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 9),
    _NnfrPvcStatsPktsRxLastFiveMins_Type()
)
nnfrPvcStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsPktsRxLastFiveMins.setStatus("current")
_NnfrPvcStatsPktsTxLastFiveMins_Type = Counter32
_NnfrPvcStatsPktsTxLastFiveMins_Object = MibTableColumn
nnfrPvcStatsPktsTxLastFiveMins = _NnfrPvcStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 10),
    _NnfrPvcStatsPktsTxLastFiveMins_Type()
)
nnfrPvcStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsPktsTxLastFiveMins.setStatus("current")
_NnfrPvcStatsErrPktsRxLastFiveMins_Type = Counter32
_NnfrPvcStatsErrPktsRxLastFiveMins_Object = MibTableColumn
nnfrPvcStatsErrPktsRxLastFiveMins = _NnfrPvcStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 11),
    _NnfrPvcStatsErrPktsRxLastFiveMins_Type()
)
nnfrPvcStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsErrPktsRxLastFiveMins.setStatus("current")
_NnfrPvcStatsUpDownStatesLastFiveMins_Type = Counter32
_NnfrPvcStatsUpDownStatesLastFiveMins_Object = MibTableColumn
nnfrPvcStatsUpDownStatesLastFiveMins = _NnfrPvcStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 4, 1, 12),
    _NnfrPvcStatsUpDownStatesLastFiveMins_Type()
)
nnfrPvcStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrPvcStatsUpDownStatesLastFiveMins.setStatus("current")
_NnfrAvcTable_Object = MibTable
nnfrAvcTable = _NnfrAvcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5)
)
if mibBuilder.loadTexts:
    nnfrAvcTable.setStatus("current")
_NnfrAvcTableEntry_Object = MibTableRow
nnfrAvcTableEntry = _NnfrAvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1)
)
nnfrAvcTableEntry.setIndexNames(
    (0, "FR-MIB", "nnfrAvcId"),
)
if mibBuilder.loadTexts:
    nnfrAvcTableEntry.setStatus("current")
_NnfrAvcId_Type = Integer32
_NnfrAvcId_Object = MibTableColumn
nnfrAvcId = _NnfrAvcId_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 1),
    _NnfrAvcId_Type()
)
nnfrAvcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nnfrAvcId.setStatus("current")


class _NnfrAvcDlci_Type(Integer32):
    """Custom type nnfrAvcDlci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 991),
    )


_NnfrAvcDlci_Type.__name__ = "Integer32"
_NnfrAvcDlci_Object = MibTableColumn
nnfrAvcDlci = _NnfrAvcDlci_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 2),
    _NnfrAvcDlci_Type()
)
nnfrAvcDlci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcDlci.setStatus("current")


class _NnfrAvcName_Type(DisplayString):
    """Custom type nnfrAvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_NnfrAvcName_Type.__name__ = "DisplayString"
_NnfrAvcName_Object = MibTableColumn
nnfrAvcName = _NnfrAvcName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 3),
    _NnfrAvcName_Type()
)
nnfrAvcName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcName.setStatus("current")


class _NnfrAvcIpAddr_Type(IpAddress):
    """Custom type nnfrAvcIpAddr based on IpAddress"""
    defaultValue = 0


_NnfrAvcIpAddr_Object = MibTableColumn
nnfrAvcIpAddr = _NnfrAvcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 4),
    _NnfrAvcIpAddr_Type()
)
nnfrAvcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcIpAddr.setStatus("current")


class _NnfrAvcIpSubnetMask_Type(IpAddress):
    """Custom type nnfrAvcIpSubnetMask based on IpAddress"""
    defaultValue = 0


_NnfrAvcIpSubnetMask_Object = MibTableColumn
nnfrAvcIpSubnetMask = _NnfrAvcIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 5),
    _NnfrAvcIpSubnetMask_Type()
)
nnfrAvcIpSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcIpSubnetMask.setStatus("current")
_NnfrAvcRemoteIpAddr_Type = IpAddress
_NnfrAvcRemoteIpAddr_Object = MibTableColumn
nnfrAvcRemoteIpAddr = _NnfrAvcRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 6),
    _NnfrAvcRemoteIpAddr_Type()
)
nnfrAvcRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcRemoteIpAddr.setStatus("current")


class _NnfrAvcClass_Type(Integer32):
    """Custom type nnfrAvcClass based on Integer32"""
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
        *(("classA", 1),
          ("classB", 2),
          ("classC", 3),
          ("classD", 4),
          ("classE", 5))
    )


_NnfrAvcClass_Type.__name__ = "Integer32"
_NnfrAvcClass_Object = MibTableColumn
nnfrAvcClass = _NnfrAvcClass_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 7),
    _NnfrAvcClass_Type()
)
nnfrAvcClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcClass.setStatus("current")
_NnfrAvcClassThreshold_Type = Integer32
_NnfrAvcClassThreshold_Object = MibTableColumn
nnfrAvcClassThreshold = _NnfrAvcClassThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 8),
    _NnfrAvcClassThreshold_Type()
)
nnfrAvcClassThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcClassThreshold.setStatus("current")


class _NnfrAvcFragmentSize_Type(Integer32):
    """Custom type nnfrAvcFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_NnfrAvcFragmentSize_Type.__name__ = "Integer32"
_NnfrAvcFragmentSize_Object = MibTableColumn
nnfrAvcFragmentSize = _NnfrAvcFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 9),
    _NnfrAvcFragmentSize_Type()
)
nnfrAvcFragmentSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcFragmentSize.setStatus("current")


class _NnfrAvcSegThreshold_Type(Integer32):
    """Custom type nnfrAvcSegThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(56, 4096),
    )


_NnfrAvcSegThreshold_Type.__name__ = "Integer32"
_NnfrAvcSegThreshold_Object = MibTableColumn
nnfrAvcSegThreshold = _NnfrAvcSegThreshold_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 10),
    _NnfrAvcSegThreshold_Type()
)
nnfrAvcSegThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcSegThreshold.setStatus("current")


class _NnfrAvcSequence_Type(Integer32):
    """Custom type nnfrAvcSequence based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 2),
          ("short", 1))
    )


_NnfrAvcSequence_Type.__name__ = "Integer32"
_NnfrAvcSequence_Object = MibTableColumn
nnfrAvcSequence = _NnfrAvcSequence_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 11),
    _NnfrAvcSequence_Type()
)
nnfrAvcSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcSequence.setStatus("current")


class _NnfrAvcDiffDelay_Type(Integer32):
    """Custom type nnfrAvcDiffDelay based on Integer32"""
    defaultValue = 80


_NnfrAvcDiffDelay_Object = MibTableColumn
nnfrAvcDiffDelay = _NnfrAvcDiffDelay_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 12),
    _NnfrAvcDiffDelay_Type()
)
nnfrAvcDiffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcDiffDelay.setStatus("current")


class _NnfrAvcEnhancedMode_Type(Integer32):
    """Custom type nnfrAvcEnhancedMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_NnfrAvcEnhancedMode_Type.__name__ = "Integer32"
_NnfrAvcEnhancedMode_Object = MibTableColumn
nnfrAvcEnhancedMode = _NnfrAvcEnhancedMode_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 13),
    _NnfrAvcEnhancedMode_Type()
)
nnfrAvcEnhancedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nnfrAvcEnhancedMode.setStatus("current")
_NnfrAvcNoOfCvcs_Type = Integer32
_NnfrAvcNoOfCvcs_Object = MibTableColumn
nnfrAvcNoOfCvcs = _NnfrAvcNoOfCvcs_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 14),
    _NnfrAvcNoOfCvcs_Type()
)
nnfrAvcNoOfCvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcNoOfCvcs.setStatus("current")
_NnfrAvcTotalBw_Type = Integer32
_NnfrAvcTotalBw_Object = MibTableColumn
nnfrAvcTotalBw = _NnfrAvcTotalBw_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 15),
    _NnfrAvcTotalBw_Type()
)
nnfrAvcTotalBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcTotalBw.setStatus("current")
if mibBuilder.loadTexts:
    nnfrAvcTotalBw.setUnits("kbps")


class _NnfrAvcEnable_Type(TruthValue):
    """Custom type nnfrAvcEnable based on TruthValue"""


_NnfrAvcEnable_Object = MibTableColumn
nnfrAvcEnable = _NnfrAvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 16),
    _NnfrAvcEnable_Type()
)
nnfrAvcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcEnable.setStatus("current")
_NnfrAvcRowStatus_Type = RowStatus
_NnfrAvcRowStatus_Object = MibTableColumn
nnfrAvcRowStatus = _NnfrAvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 5, 1, 17),
    _NnfrAvcRowStatus_Type()
)
nnfrAvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrAvcRowStatus.setStatus("current")
_NnfrCvcTable_Object = MibTable
nnfrCvcTable = _NnfrCvcTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 6)
)
if mibBuilder.loadTexts:
    nnfrCvcTable.setStatus("current")
_NnfrCvcTableEntry_Object = MibTableRow
nnfrCvcTableEntry = _NnfrCvcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 6, 1)
)
nnfrCvcTableEntry.setIndexNames(
    (0, "FR-MIB", "nnfrAvcId"),
    (0, "BUNDLE-MIB", "nnbundleId"),
    (0, "FR-MIB", "nnfrPvcDlci"),
)
if mibBuilder.loadTexts:
    nnfrCvcTableEntry.setStatus("current")
_NnfrCvcBundleName_Type = DisplayString
_NnfrCvcBundleName_Object = MibTableColumn
nnfrCvcBundleName = _NnfrCvcBundleName_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 6, 1, 1),
    _NnfrCvcBundleName_Type()
)
nnfrCvcBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrCvcBundleName.setStatus("current")


class _NnfrCvcEnable_Type(TruthValue):
    """Custom type nnfrCvcEnable based on TruthValue"""


_NnfrCvcEnable_Object = MibTableColumn
nnfrCvcEnable = _NnfrCvcEnable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 6, 1, 2),
    _NnfrCvcEnable_Type()
)
nnfrCvcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrCvcEnable.setStatus("current")
_NnfrCvcRowStatus_Type = RowStatus
_NnfrCvcRowStatus_Object = MibTableColumn
nnfrCvcRowStatus = _NnfrCvcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 6, 1, 3),
    _NnfrCvcRowStatus_Type()
)
nnfrCvcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    nnfrCvcRowStatus.setStatus("current")
_NnfrAvcStatsTable_Object = MibTable
nnfrAvcStatsTable = _NnfrAvcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7)
)
if mibBuilder.loadTexts:
    nnfrAvcStatsTable.setStatus("current")
_NnfrAvcStatsTableEntry_Object = MibTableRow
nnfrAvcStatsTableEntry = _NnfrAvcStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1)
)
nnfrAvcStatsTableEntry.setIndexNames(
    (0, "FR-MIB", "nnfrAvcId"),
)
if mibBuilder.loadTexts:
    nnfrAvcStatsTableEntry.setStatus("current")
_NnfrAvcStatsBytesRxLastBootOrClear_Type = Counter32
_NnfrAvcStatsBytesRxLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsBytesRxLastBootOrClear = _NnfrAvcStatsBytesRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 1),
    _NnfrAvcStatsBytesRxLastBootOrClear_Type()
)
nnfrAvcStatsBytesRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsBytesRxLastBootOrClear.setStatus("current")
_NnfrAvcStatsBytesTxLastBootOrClear_Type = Counter32
_NnfrAvcStatsBytesTxLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsBytesTxLastBootOrClear = _NnfrAvcStatsBytesTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 2),
    _NnfrAvcStatsBytesTxLastBootOrClear_Type()
)
nnfrAvcStatsBytesTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsBytesTxLastBootOrClear.setStatus("current")
_NnfrAvcStatsPktsRxLastBootOrClear_Type = Counter32
_NnfrAvcStatsPktsRxLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsPktsRxLastBootOrClear = _NnfrAvcStatsPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 3),
    _NnfrAvcStatsPktsRxLastBootOrClear_Type()
)
nnfrAvcStatsPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsPktsRxLastBootOrClear.setStatus("current")
_NnfrAvcStatsPktsTxLastBootOrClear_Type = Counter32
_NnfrAvcStatsPktsTxLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsPktsTxLastBootOrClear = _NnfrAvcStatsPktsTxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 4),
    _NnfrAvcStatsPktsTxLastBootOrClear_Type()
)
nnfrAvcStatsPktsTxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsPktsTxLastBootOrClear.setStatus("current")
_NnfrAvcStatsErrPktsRxLastBootOrClear_Type = Counter32
_NnfrAvcStatsErrPktsRxLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsErrPktsRxLastBootOrClear = _NnfrAvcStatsErrPktsRxLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 5),
    _NnfrAvcStatsErrPktsRxLastBootOrClear_Type()
)
nnfrAvcStatsErrPktsRxLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsErrPktsRxLastBootOrClear.setStatus("current")
_NnfrAvcStatsUpDownStatesLastBootOrClear_Type = Counter32
_NnfrAvcStatsUpDownStatesLastBootOrClear_Object = MibTableColumn
nnfrAvcStatsUpDownStatesLastBootOrClear = _NnfrAvcStatsUpDownStatesLastBootOrClear_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 6),
    _NnfrAvcStatsUpDownStatesLastBootOrClear_Type()
)
nnfrAvcStatsUpDownStatesLastBootOrClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsUpDownStatesLastBootOrClear.setStatus("current")
_NnfrAvcStatsBytesRxLastFiveMins_Type = Counter32
_NnfrAvcStatsBytesRxLastFiveMins_Object = MibTableColumn
nnfrAvcStatsBytesRxLastFiveMins = _NnfrAvcStatsBytesRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 7),
    _NnfrAvcStatsBytesRxLastFiveMins_Type()
)
nnfrAvcStatsBytesRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsBytesRxLastFiveMins.setStatus("current")
_NnfrAvcStatsBytesTxLastFiveMins_Type = Counter32
_NnfrAvcStatsBytesTxLastFiveMins_Object = MibTableColumn
nnfrAvcStatsBytesTxLastFiveMins = _NnfrAvcStatsBytesTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 8),
    _NnfrAvcStatsBytesTxLastFiveMins_Type()
)
nnfrAvcStatsBytesTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsBytesTxLastFiveMins.setStatus("current")
_NnfrAvcStatsPktsRxLastFiveMins_Type = Counter32
_NnfrAvcStatsPktsRxLastFiveMins_Object = MibTableColumn
nnfrAvcStatsPktsRxLastFiveMins = _NnfrAvcStatsPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 9),
    _NnfrAvcStatsPktsRxLastFiveMins_Type()
)
nnfrAvcStatsPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsPktsRxLastFiveMins.setStatus("current")
_NnfrAvcStatsPktsTxLastFiveMins_Type = Counter32
_NnfrAvcStatsPktsTxLastFiveMins_Object = MibTableColumn
nnfrAvcStatsPktsTxLastFiveMins = _NnfrAvcStatsPktsTxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 10),
    _NnfrAvcStatsPktsTxLastFiveMins_Type()
)
nnfrAvcStatsPktsTxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsPktsTxLastFiveMins.setStatus("current")
_NnfrAvcStatsErrPktsRxLastFiveMins_Type = Counter32
_NnfrAvcStatsErrPktsRxLastFiveMins_Object = MibTableColumn
nnfrAvcStatsErrPktsRxLastFiveMins = _NnfrAvcStatsErrPktsRxLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 11),
    _NnfrAvcStatsErrPktsRxLastFiveMins_Type()
)
nnfrAvcStatsErrPktsRxLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsErrPktsRxLastFiveMins.setStatus("current")
_NnfrAvcStatsUpDownStatesLastFiveMins_Type = Counter32
_NnfrAvcStatsUpDownStatesLastFiveMins_Object = MibTableColumn
nnfrAvcStatsUpDownStatesLastFiveMins = _NnfrAvcStatsUpDownStatesLastFiveMins_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 16, 7, 1, 12),
    _NnfrAvcStatsUpDownStatesLastFiveMins_Type()
)
nnfrAvcStatsUpDownStatesLastFiveMins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnfrAvcStatsUpDownStatesLastFiveMins.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FR-MIB",
    **{"nnfrMib": nnfrMib,
       "nnfrTable": nnfrTable,
       "nnfrTableEntry": nnfrTableEntry,
       "nnfrIfEnable": nnfrIfEnable,
       "nnfrEnablePvcAll": nnfrEnablePvcAll,
       "nnfrFrameSize": nnfrFrameSize,
       "nnfrIfType": nnfrIfType,
       "nnfrLmiType": nnfrLmiType,
       "nnfrLmiDceN392": nnfrLmiDceN392,
       "nnfrLmiDceN393": nnfrLmiDceN393,
       "nnfrLmiDteN392": nnfrLmiDteN392,
       "nnfrLmiDteN393": nnfrLmiDteN393,
       "nnfrLmiDteN391": nnfrLmiDteN391,
       "nnfrLmiKeepalive": nnfrLmiKeepalive,
       "nnmfrAckMsgTimer": nnmfrAckMsgTimer,
       "nnmfrAckMsgMaxRetry": nnmfrAckMsgMaxRetry,
       "nnmfrClass": nnmfrClass,
       "nnmfrClassThreshold": nnmfrClassThreshold,
       "nnmfrFrameSize": nnmfrFrameSize,
       "nnmfrHelloTimer": nnmfrHelloTimer,
       "nnmfrSegThreshold": nnmfrSegThreshold,
       "nnmfrDiffDelay": nnmfrDiffDelay,
       "nnfrPvcTable": nnfrPvcTable,
       "nnfrPvcTableEntry": nnfrPvcTableEntry,
       "nnfrPvcDlci": nnfrPvcDlci,
       "nnfrPvcEnable": nnfrPvcEnable,
       "nnfrPvcDescr": nnfrPvcDescr,
       "nnfrPvcIpAddr": nnfrPvcIpAddr,
       "nnfrPvcIpSubnetMask": nnfrPvcIpSubnetMask,
       "nnfrPvcRemoteIpAddr": nnfrPvcRemoteIpAddr,
       "nnfrPvcPolicingEnable": nnfrPvcPolicingEnable,
       "nnfrPvcPolicingDe": nnfrPvcPolicingDe,
       "nnfrPvcPolicingCir": nnfrPvcPolicingCir,
       "nnfrPvcPolicingBc": nnfrPvcPolicingBc,
       "nnfrPvcPolicingBe": nnfrPvcPolicingBe,
       "nnfrPvcShapingCir": nnfrPvcShapingCir,
       "nnfrPvcShapingBcMax": nnfrPvcShapingBcMax,
       "nnfrPvcShapingBcMin": nnfrPvcShapingBcMin,
       "nnfrPvcShapingBe": nnfrPvcShapingBe,
       "nnfrPvcDlciForSwitching": nnfrPvcDlciForSwitching,
       "nnfrPvcBundleNameForSwitching": nnfrPvcBundleNameForSwitching,
       "nnfrPvcRowStatus": nnfrPvcRowStatus,
       "nnfrStatsTable": nnfrStatsTable,
       "nnfrStatsTableEntry": nnfrStatsTableEntry,
       "nnfrStatsFramesRx": nnfrStatsFramesRx,
       "nnfrStatsInvFramesRx": nnfrStatsInvFramesRx,
       "nnfrStatsFECNsRx": nnfrStatsFECNsRx,
       "nnfrStatsBECNsRx": nnfrStatsBECNsRx,
       "nnfrStatsShortFramesRx": nnfrStatsShortFramesRx,
       "nnfrStatsLongFramesRx": nnfrStatsLongFramesRx,
       "nnfrStatsInvDLCIsRx": nnfrStatsInvDLCIsRx,
       "nnfrStatsUnknownDLCIsRx": nnfrStatsUnknownDLCIsRx,
       "nnfrStatsFramesTx": nnfrStatsFramesTx,
       "nnfrPvcStatsTable": nnfrPvcStatsTable,
       "nnfrPvcStatsTableEntry": nnfrPvcStatsTableEntry,
       "nnfrPvcStatsBytesRxLastBootOrClear": nnfrPvcStatsBytesRxLastBootOrClear,
       "nnfrPvcStatsBytesTxLastBootOrClear": nnfrPvcStatsBytesTxLastBootOrClear,
       "nnfrPvcStatsPktsRxLastBootOrClear": nnfrPvcStatsPktsRxLastBootOrClear,
       "nnfrPvcStatsPktsTxLastBootOrClear": nnfrPvcStatsPktsTxLastBootOrClear,
       "nnfrPvcStatsErrPktsRxLastBootOrClear": nnfrPvcStatsErrPktsRxLastBootOrClear,
       "nnfrPvcStatsUpDownStatesLastBootOrClear": nnfrPvcStatsUpDownStatesLastBootOrClear,
       "nnfrPvcStatsBytesRxLastFiveMins": nnfrPvcStatsBytesRxLastFiveMins,
       "nnfrPvcStatsBytesTxLastFiveMins": nnfrPvcStatsBytesTxLastFiveMins,
       "nnfrPvcStatsPktsRxLastFiveMins": nnfrPvcStatsPktsRxLastFiveMins,
       "nnfrPvcStatsPktsTxLastFiveMins": nnfrPvcStatsPktsTxLastFiveMins,
       "nnfrPvcStatsErrPktsRxLastFiveMins": nnfrPvcStatsErrPktsRxLastFiveMins,
       "nnfrPvcStatsUpDownStatesLastFiveMins": nnfrPvcStatsUpDownStatesLastFiveMins,
       "nnfrAvcTable": nnfrAvcTable,
       "nnfrAvcTableEntry": nnfrAvcTableEntry,
       "nnfrAvcId": nnfrAvcId,
       "nnfrAvcDlci": nnfrAvcDlci,
       "nnfrAvcName": nnfrAvcName,
       "nnfrAvcIpAddr": nnfrAvcIpAddr,
       "nnfrAvcIpSubnetMask": nnfrAvcIpSubnetMask,
       "nnfrAvcRemoteIpAddr": nnfrAvcRemoteIpAddr,
       "nnfrAvcClass": nnfrAvcClass,
       "nnfrAvcClassThreshold": nnfrAvcClassThreshold,
       "nnfrAvcFragmentSize": nnfrAvcFragmentSize,
       "nnfrAvcSegThreshold": nnfrAvcSegThreshold,
       "nnfrAvcSequence": nnfrAvcSequence,
       "nnfrAvcDiffDelay": nnfrAvcDiffDelay,
       "nnfrAvcEnhancedMode": nnfrAvcEnhancedMode,
       "nnfrAvcNoOfCvcs": nnfrAvcNoOfCvcs,
       "nnfrAvcTotalBw": nnfrAvcTotalBw,
       "nnfrAvcEnable": nnfrAvcEnable,
       "nnfrAvcRowStatus": nnfrAvcRowStatus,
       "nnfrCvcTable": nnfrCvcTable,
       "nnfrCvcTableEntry": nnfrCvcTableEntry,
       "nnfrCvcBundleName": nnfrCvcBundleName,
       "nnfrCvcEnable": nnfrCvcEnable,
       "nnfrCvcRowStatus": nnfrCvcRowStatus,
       "nnfrAvcStatsTable": nnfrAvcStatsTable,
       "nnfrAvcStatsTableEntry": nnfrAvcStatsTableEntry,
       "nnfrAvcStatsBytesRxLastBootOrClear": nnfrAvcStatsBytesRxLastBootOrClear,
       "nnfrAvcStatsBytesTxLastBootOrClear": nnfrAvcStatsBytesTxLastBootOrClear,
       "nnfrAvcStatsPktsRxLastBootOrClear": nnfrAvcStatsPktsRxLastBootOrClear,
       "nnfrAvcStatsPktsTxLastBootOrClear": nnfrAvcStatsPktsTxLastBootOrClear,
       "nnfrAvcStatsErrPktsRxLastBootOrClear": nnfrAvcStatsErrPktsRxLastBootOrClear,
       "nnfrAvcStatsUpDownStatesLastBootOrClear": nnfrAvcStatsUpDownStatesLastBootOrClear,
       "nnfrAvcStatsBytesRxLastFiveMins": nnfrAvcStatsBytesRxLastFiveMins,
       "nnfrAvcStatsBytesTxLastFiveMins": nnfrAvcStatsBytesTxLastFiveMins,
       "nnfrAvcStatsPktsRxLastFiveMins": nnfrAvcStatsPktsRxLastFiveMins,
       "nnfrAvcStatsPktsTxLastFiveMins": nnfrAvcStatsPktsTxLastFiveMins,
       "nnfrAvcStatsErrPktsRxLastFiveMins": nnfrAvcStatsErrPktsRxLastFiveMins,
       "nnfrAvcStatsUpDownStatesLastFiveMins": nnfrAvcStatsUpDownStatesLastFiveMins}
)
