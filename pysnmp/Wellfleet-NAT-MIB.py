# SNMP MIB module (Wellfleet-NAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-NAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:45 2024
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

(wfNatGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfNatGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfNatBase_ObjectIdentity = ObjectIdentity
wfNatBase = _WfNatBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1)
)


class _WfNatBaseDelete_Type(Integer32):
    """Custom type wfNatBaseDelete based on Integer32"""
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


_WfNatBaseDelete_Type.__name__ = "Integer32"
_WfNatBaseDelete_Object = MibScalar
wfNatBaseDelete = _WfNatBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 1),
    _WfNatBaseDelete_Type()
)
wfNatBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseDelete.setStatus("mandatory")


class _WfNatBaseDisable_Type(Integer32):
    """Custom type wfNatBaseDisable based on Integer32"""
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


_WfNatBaseDisable_Type.__name__ = "Integer32"
_WfNatBaseDisable_Object = MibScalar
wfNatBaseDisable = _WfNatBaseDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 2),
    _WfNatBaseDisable_Type()
)
wfNatBaseDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseDisable.setStatus("mandatory")


class _WfNatBaseState_Type(Integer32):
    """Custom type wfNatBaseState based on Integer32"""
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
        *(("down", 3),
          ("init", 2),
          ("not-present", 4),
          ("up", 1))
    )


_WfNatBaseState_Type.__name__ = "Integer32"
_WfNatBaseState_Object = MibScalar
wfNatBaseState = _WfNatBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 3),
    _WfNatBaseState_Type()
)
wfNatBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatBaseState.setStatus("mandatory")


class _WfNatBaseSoloistSlotMask_Type(Gauge32):
    """Custom type wfNatBaseSoloistSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfNatBaseSoloistSlotMask_Object = MibScalar
wfNatBaseSoloistSlotMask = _WfNatBaseSoloistSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 4),
    _WfNatBaseSoloistSlotMask_Type()
)
wfNatBaseSoloistSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSoloistSlotMask.setStatus("mandatory")


class _WfNatBaseSoloistSlot_Type(Integer32):
    """Custom type wfNatBaseSoloistSlot based on Integer32"""
    defaultValue = 0


_WfNatBaseSoloistSlot_Object = MibScalar
wfNatBaseSoloistSlot = _WfNatBaseSoloistSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 5),
    _WfNatBaseSoloistSlot_Type()
)
wfNatBaseSoloistSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatBaseSoloistSlot.setStatus("mandatory")


class _WfNatBaseLogMask_Type(Integer32):
    """Custom type wfNatBaseLogMask based on Integer32"""
    defaultValue = 0


_WfNatBaseLogMask_Object = MibScalar
wfNatBaseLogMask = _WfNatBaseLogMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 6),
    _WfNatBaseLogMask_Type()
)
wfNatBaseLogMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseLogMask.setStatus("mandatory")


class _WfNatBaseMapTimeout_Type(Integer32):
    """Custom type wfNatBaseMapTimeout based on Integer32"""
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


_WfNatBaseMapTimeout_Type.__name__ = "Integer32"
_WfNatBaseMapTimeout_Object = MibScalar
wfNatBaseMapTimeout = _WfNatBaseMapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 7),
    _WfNatBaseMapTimeout_Type()
)
wfNatBaseMapTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseMapTimeout.setStatus("mandatory")


class _WfNatBaseMapMaxTimeout_Type(Integer32):
    """Custom type wfNatBaseMapMaxTimeout based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfNatBaseMapMaxTimeout_Type.__name__ = "Integer32"
_WfNatBaseMapMaxTimeout_Object = MibScalar
wfNatBaseMapMaxTimeout = _WfNatBaseMapMaxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 8),
    _WfNatBaseMapMaxTimeout_Type()
)
wfNatBaseMapMaxTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseMapMaxTimeout.setStatus("mandatory")


class _WfNatBaseMapDynMapsCount_Type(Gauge32):
    """Custom type wfNatBaseMapDynMapsCount based on Gauge32"""
    defaultValue = 0


_WfNatBaseMapDynMapsCount_Object = MibScalar
wfNatBaseMapDynMapsCount = _WfNatBaseMapDynMapsCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 9),
    _WfNatBaseMapDynMapsCount_Type()
)
wfNatBaseMapDynMapsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatBaseMapDynMapsCount.setStatus("mandatory")


class _WfNatBaseFtpSessionCount_Type(Gauge32):
    """Custom type wfNatBaseFtpSessionCount based on Gauge32"""
    defaultValue = 0


_WfNatBaseFtpSessionCount_Object = MibScalar
wfNatBaseFtpSessionCount = _WfNatBaseFtpSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 10),
    _WfNatBaseFtpSessionCount_Type()
)
wfNatBaseFtpSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatBaseFtpSessionCount.setStatus("mandatory")


class _WfNatBaseNto1TrTotCount_Type(Gauge32):
    """Custom type wfNatBaseNto1TrTotCount based on Gauge32"""
    defaultValue = 0


_WfNatBaseNto1TrTotCount_Object = MibScalar
wfNatBaseNto1TrTotCount = _WfNatBaseNto1TrTotCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 11),
    _WfNatBaseNto1TrTotCount_Type()
)
wfNatBaseNto1TrTotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatBaseNto1TrTotCount.setStatus("mandatory")


class _WfNatBaseSynchronization_Type(Integer32):
    """Custom type wfNatBaseSynchronization based on Integer32"""
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


_WfNatBaseSynchronization_Type.__name__ = "Integer32"
_WfNatBaseSynchronization_Object = MibScalar
wfNatBaseSynchronization = _WfNatBaseSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 12),
    _WfNatBaseSynchronization_Type()
)
wfNatBaseSynchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynchronization.setStatus("mandatory")
_WfNatBaseSynRouterID_Type = IpAddress
_WfNatBaseSynRouterID_Object = MibScalar
wfNatBaseSynRouterID = _WfNatBaseSynRouterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 13),
    _WfNatBaseSynRouterID_Type()
)
wfNatBaseSynRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynRouterID.setStatus("mandatory")


class _WfNatBaseSynPort_Type(Integer32):
    """Custom type wfNatBaseSynPort based on Integer32"""
    defaultValue = 670


_WfNatBaseSynPort_Object = MibScalar
wfNatBaseSynPort = _WfNatBaseSynPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 14),
    _WfNatBaseSynPort_Type()
)
wfNatBaseSynPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynPort.setStatus("mandatory")


class _WfNatBaseSynKeepAlvInterval_Type(Integer32):
    """Custom type wfNatBaseSynKeepAlvInterval based on Integer32"""
    defaultValue = 120


_WfNatBaseSynKeepAlvInterval_Object = MibScalar
wfNatBaseSynKeepAlvInterval = _WfNatBaseSynKeepAlvInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 15),
    _WfNatBaseSynKeepAlvInterval_Type()
)
wfNatBaseSynKeepAlvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynKeepAlvInterval.setStatus("mandatory")


class _WfNatBaseSynKeepAlvTimer_Type(Integer32):
    """Custom type wfNatBaseSynKeepAlvTimer based on Integer32"""
    defaultValue = 3


_WfNatBaseSynKeepAlvTimer_Object = MibScalar
wfNatBaseSynKeepAlvTimer = _WfNatBaseSynKeepAlvTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 16),
    _WfNatBaseSynKeepAlvTimer_Type()
)
wfNatBaseSynKeepAlvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynKeepAlvTimer.setStatus("mandatory")


class _WfNatBaseSynKeepAlvRetries_Type(Integer32):
    """Custom type wfNatBaseSynKeepAlvRetries based on Integer32"""
    defaultValue = 5


_WfNatBaseSynKeepAlvRetries_Object = MibScalar
wfNatBaseSynKeepAlvRetries = _WfNatBaseSynKeepAlvRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 17),
    _WfNatBaseSynKeepAlvRetries_Type()
)
wfNatBaseSynKeepAlvRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseSynKeepAlvRetries.setStatus("mandatory")


class _WfNatBaseLocalToLocalEnable_Type(Integer32):
    """Custom type wfNatBaseLocalToLocalEnable based on Integer32"""
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


_WfNatBaseLocalToLocalEnable_Type.__name__ = "Integer32"
_WfNatBaseLocalToLocalEnable_Object = MibScalar
wfNatBaseLocalToLocalEnable = _WfNatBaseLocalToLocalEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 18),
    _WfNatBaseLocalToLocalEnable_Type()
)
wfNatBaseLocalToLocalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseLocalToLocalEnable.setStatus("mandatory")


class _WfNatBaseInstallUniPrivAddr_Type(Integer32):
    """Custom type wfNatBaseInstallUniPrivAddr based on Integer32"""
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


_WfNatBaseInstallUniPrivAddr_Type.__name__ = "Integer32"
_WfNatBaseInstallUniPrivAddr_Object = MibScalar
wfNatBaseInstallUniPrivAddr = _WfNatBaseInstallUniPrivAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 1, 19),
    _WfNatBaseInstallUniPrivAddr_Type()
)
wfNatBaseInstallUniPrivAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatBaseInstallUniPrivAddr.setStatus("mandatory")
_WfNatAddrRangeTable_Object = MibTable
wfNatAddrRangeTable = _WfNatAddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2)
)
if mibBuilder.loadTexts:
    wfNatAddrRangeTable.setStatus("mandatory")
_WfNatAddrRangeEntry_Object = MibTableRow
wfNatAddrRangeEntry = _WfNatAddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2, 1)
)
wfNatAddrRangeEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatAddrRangeAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatAddrRangePrefixLen"),
)
if mibBuilder.loadTexts:
    wfNatAddrRangeEntry.setStatus("mandatory")


class _WfNatAddrRangeDelete_Type(Integer32):
    """Custom type wfNatAddrRangeDelete based on Integer32"""
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


_WfNatAddrRangeDelete_Type.__name__ = "Integer32"
_WfNatAddrRangeDelete_Object = MibTableColumn
wfNatAddrRangeDelete = _WfNatAddrRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2, 1, 1),
    _WfNatAddrRangeDelete_Type()
)
wfNatAddrRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddrRangeDelete.setStatus("mandatory")


class _WfNatAddrRangeDisable_Type(Integer32):
    """Custom type wfNatAddrRangeDisable based on Integer32"""
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


_WfNatAddrRangeDisable_Type.__name__ = "Integer32"
_WfNatAddrRangeDisable_Object = MibTableColumn
wfNatAddrRangeDisable = _WfNatAddrRangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2, 1, 2),
    _WfNatAddrRangeDisable_Type()
)
wfNatAddrRangeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddrRangeDisable.setStatus("mandatory")
_WfNatAddrRangeAddress_Type = IpAddress
_WfNatAddrRangeAddress_Object = MibTableColumn
wfNatAddrRangeAddress = _WfNatAddrRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2, 1, 3),
    _WfNatAddrRangeAddress_Type()
)
wfNatAddrRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddrRangeAddress.setStatus("mandatory")
_WfNatAddrRangePrefixLen_Type = Integer32
_WfNatAddrRangePrefixLen_Object = MibTableColumn
wfNatAddrRangePrefixLen = _WfNatAddrRangePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 2, 1, 4),
    _WfNatAddrRangePrefixLen_Type()
)
wfNatAddrRangePrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddrRangePrefixLen.setStatus("mandatory")
_WfNatLocalAddrRangeTable_Object = MibTable
wfNatLocalAddrRangeTable = _WfNatLocalAddrRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeTable.setStatus("mandatory")
_WfNatLocalAddrRangeEntry_Object = MibTableRow
wfNatLocalAddrRangeEntry = _WfNatLocalAddrRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1)
)
wfNatLocalAddrRangeEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatLocalAddrRangeAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatLocalAddrRangePrefixLen"),
)
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeEntry.setStatus("mandatory")


class _WfNatLocalAddrRangeDelete_Type(Integer32):
    """Custom type wfNatLocalAddrRangeDelete based on Integer32"""
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


_WfNatLocalAddrRangeDelete_Type.__name__ = "Integer32"
_WfNatLocalAddrRangeDelete_Object = MibTableColumn
wfNatLocalAddrRangeDelete = _WfNatLocalAddrRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1, 1),
    _WfNatLocalAddrRangeDelete_Type()
)
wfNatLocalAddrRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeDelete.setStatus("mandatory")


class _WfNatLocalAddrRangeDisable_Type(Integer32):
    """Custom type wfNatLocalAddrRangeDisable based on Integer32"""
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


_WfNatLocalAddrRangeDisable_Type.__name__ = "Integer32"
_WfNatLocalAddrRangeDisable_Object = MibTableColumn
wfNatLocalAddrRangeDisable = _WfNatLocalAddrRangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1, 2),
    _WfNatLocalAddrRangeDisable_Type()
)
wfNatLocalAddrRangeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeDisable.setStatus("mandatory")
_WfNatLocalAddrRangeAddress_Type = IpAddress
_WfNatLocalAddrRangeAddress_Object = MibTableColumn
wfNatLocalAddrRangeAddress = _WfNatLocalAddrRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1, 3),
    _WfNatLocalAddrRangeAddress_Type()
)
wfNatLocalAddrRangeAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeAddress.setStatus("mandatory")
_WfNatLocalAddrRangePrefixLen_Type = Integer32
_WfNatLocalAddrRangePrefixLen_Object = MibTableColumn
wfNatLocalAddrRangePrefixLen = _WfNatLocalAddrRangePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1, 4),
    _WfNatLocalAddrRangePrefixLen_Type()
)
wfNatLocalAddrRangePrefixLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatLocalAddrRangePrefixLen.setStatus("mandatory")


class _WfNatLocalAddrRangeNto1Addr_Type(IpAddress):
    """Custom type wfNatLocalAddrRangeNto1Addr based on IpAddress"""
    defaultValue = 0


_WfNatLocalAddrRangeNto1Addr_Object = MibTableColumn
wfNatLocalAddrRangeNto1Addr = _WfNatLocalAddrRangeNto1Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 3, 1, 5),
    _WfNatLocalAddrRangeNto1Addr_Type()
)
wfNatLocalAddrRangeNto1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatLocalAddrRangeNto1Addr.setStatus("mandatory")
_WfNatStaticMapTable_Object = MibTable
wfNatStaticMapTable = _WfNatStaticMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4)
)
if mibBuilder.loadTexts:
    wfNatStaticMapTable.setStatus("mandatory")
_WfNatStaticMapEntry_Object = MibTableRow
wfNatStaticMapEntry = _WfNatStaticMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1)
)
wfNatStaticMapEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMapLocalAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMapGlobalAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMapProtocol"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMapLocalPort"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMapGlobalPort"),
)
if mibBuilder.loadTexts:
    wfNatStaticMapEntry.setStatus("mandatory")


class _WfNatStaticMapDelete_Type(Integer32):
    """Custom type wfNatStaticMapDelete based on Integer32"""
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


_WfNatStaticMapDelete_Type.__name__ = "Integer32"
_WfNatStaticMapDelete_Object = MibTableColumn
wfNatStaticMapDelete = _WfNatStaticMapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 1),
    _WfNatStaticMapDelete_Type()
)
wfNatStaticMapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapDelete.setStatus("mandatory")


class _WfNatStaticMapDisable_Type(Integer32):
    """Custom type wfNatStaticMapDisable based on Integer32"""
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


_WfNatStaticMapDisable_Type.__name__ = "Integer32"
_WfNatStaticMapDisable_Object = MibTableColumn
wfNatStaticMapDisable = _WfNatStaticMapDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 2),
    _WfNatStaticMapDisable_Type()
)
wfNatStaticMapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapDisable.setStatus("mandatory")
_WfNatStaticMapLocalAddress_Type = IpAddress
_WfNatStaticMapLocalAddress_Object = MibTableColumn
wfNatStaticMapLocalAddress = _WfNatStaticMapLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 3),
    _WfNatStaticMapLocalAddress_Type()
)
wfNatStaticMapLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapLocalAddress.setStatus("mandatory")
_WfNatStaticMapGlobalAddress_Type = IpAddress
_WfNatStaticMapGlobalAddress_Object = MibTableColumn
wfNatStaticMapGlobalAddress = _WfNatStaticMapGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 4),
    _WfNatStaticMapGlobalAddress_Type()
)
wfNatStaticMapGlobalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapGlobalAddress.setStatus("mandatory")
_WfNatStaticMapProtocol_Type = Integer32
_WfNatStaticMapProtocol_Object = MibTableColumn
wfNatStaticMapProtocol = _WfNatStaticMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 5),
    _WfNatStaticMapProtocol_Type()
)
wfNatStaticMapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapProtocol.setStatus("mandatory")
_WfNatStaticMapLocalPort_Type = Integer32
_WfNatStaticMapLocalPort_Object = MibTableColumn
wfNatStaticMapLocalPort = _WfNatStaticMapLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 6),
    _WfNatStaticMapLocalPort_Type()
)
wfNatStaticMapLocalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapLocalPort.setStatus("mandatory")
_WfNatStaticMapGlobalPort_Type = Integer32
_WfNatStaticMapGlobalPort_Object = MibTableColumn
wfNatStaticMapGlobalPort = _WfNatStaticMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 4, 1, 7),
    _WfNatStaticMapGlobalPort_Type()
)
wfNatStaticMapGlobalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMapGlobalPort.setStatus("mandatory")
_WfNatMapTable_Object = MibTable
wfNatMapTable = _WfNatMapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5)
)
if mibBuilder.loadTexts:
    wfNatMapTable.setStatus("mandatory")
_WfNatMapEntry_Object = MibTableRow
wfNatMapEntry = _WfNatMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1)
)
wfNatMapEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatMapLocalAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatMapGlobalAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatMapProtocol"),
    (0, "Wellfleet-NAT-MIB", "wfNatMapLocalPort"),
    (0, "Wellfleet-NAT-MIB", "wfNatMapGlobalPort"),
)
if mibBuilder.loadTexts:
    wfNatMapEntry.setStatus("mandatory")
_WfNatMapLocalAddress_Type = IpAddress
_WfNatMapLocalAddress_Object = MibTableColumn
wfNatMapLocalAddress = _WfNatMapLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 1),
    _WfNatMapLocalAddress_Type()
)
wfNatMapLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapLocalAddress.setStatus("mandatory")
_WfNatMapGlobalAddress_Type = IpAddress
_WfNatMapGlobalAddress_Object = MibTableColumn
wfNatMapGlobalAddress = _WfNatMapGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 2),
    _WfNatMapGlobalAddress_Type()
)
wfNatMapGlobalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapGlobalAddress.setStatus("mandatory")
_WfNatMapProtocol_Type = Integer32
_WfNatMapProtocol_Object = MibTableColumn
wfNatMapProtocol = _WfNatMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 3),
    _WfNatMapProtocol_Type()
)
wfNatMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapProtocol.setStatus("mandatory")
_WfNatMapLocalPort_Type = Integer32
_WfNatMapLocalPort_Object = MibTableColumn
wfNatMapLocalPort = _WfNatMapLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 4),
    _WfNatMapLocalPort_Type()
)
wfNatMapLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapLocalPort.setStatus("mandatory")
_WfNatMapGlobalPort_Type = Integer32
_WfNatMapGlobalPort_Object = MibTableColumn
wfNatMapGlobalPort = _WfNatMapGlobalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 5),
    _WfNatMapGlobalPort_Type()
)
wfNatMapGlobalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapGlobalPort.setStatus("mandatory")
_WfNatMapTxCount_Type = Counter32
_WfNatMapTxCount_Object = MibTableColumn
wfNatMapTxCount = _WfNatMapTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 6),
    _WfNatMapTxCount_Type()
)
wfNatMapTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapTxCount.setStatus("mandatory")
_WfNatMapRxCount_Type = Counter32
_WfNatMapRxCount_Object = MibTableColumn
wfNatMapRxCount = _WfNatMapRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 7),
    _WfNatMapRxCount_Type()
)
wfNatMapRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapRxCount.setStatus("mandatory")
_WfNatMapTimeout_Type = Counter32
_WfNatMapTimeout_Object = MibTableColumn
wfNatMapTimeout = _WfNatMapTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 8),
    _WfNatMapTimeout_Type()
)
wfNatMapTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapTimeout.setStatus("mandatory")


class _WfNatMapMode_Type(Integer32):
    """Custom type wfNatMapMode based on Integer32"""
    defaultValue = 0


_WfNatMapMode_Object = MibTableColumn
wfNatMapMode = _WfNatMapMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 5, 1, 9),
    _WfNatMapMode_Type()
)
wfNatMapMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMapMode.setStatus("mandatory")
_WfNatIfTable_Object = MibTable
wfNatIfTable = _WfNatIfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6)
)
if mibBuilder.loadTexts:
    wfNatIfTable.setStatus("mandatory")
_WfNatIfEntry_Object = MibTableRow
wfNatIfEntry = _WfNatIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1)
)
wfNatIfEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatIfIpAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatIfCircuit"),
)
if mibBuilder.loadTexts:
    wfNatIfEntry.setStatus("mandatory")


class _WfNatIfDelete_Type(Integer32):
    """Custom type wfNatIfDelete based on Integer32"""
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


_WfNatIfDelete_Type.__name__ = "Integer32"
_WfNatIfDelete_Object = MibTableColumn
wfNatIfDelete = _WfNatIfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 1),
    _WfNatIfDelete_Type()
)
wfNatIfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIfDelete.setStatus("mandatory")


class _WfNatIfDisable_Type(Integer32):
    """Custom type wfNatIfDisable based on Integer32"""
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


_WfNatIfDisable_Type.__name__ = "Integer32"
_WfNatIfDisable_Object = MibTableColumn
wfNatIfDisable = _WfNatIfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 2),
    _WfNatIfDisable_Type()
)
wfNatIfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIfDisable.setStatus("mandatory")
_WfNatIfIpAddress_Type = IpAddress
_WfNatIfIpAddress_Object = MibTableColumn
wfNatIfIpAddress = _WfNatIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 3),
    _WfNatIfIpAddress_Type()
)
wfNatIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIfIpAddress.setStatus("mandatory")
_WfNatIfCircuit_Type = Integer32
_WfNatIfCircuit_Object = MibTableColumn
wfNatIfCircuit = _WfNatIfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 4),
    _WfNatIfCircuit_Type()
)
wfNatIfCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIfCircuit.setStatus("mandatory")


class _WfNatIfType_Type(Integer32):
    """Custom type wfNatIfType based on Integer32"""
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
        *(("biDirectional", 3),
          ("uniDirInbound", 1),
          ("uniDirOutbound", 2))
    )


_WfNatIfType_Type.__name__ = "Integer32"
_WfNatIfType_Object = MibTableColumn
wfNatIfType = _WfNatIfType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 5),
    _WfNatIfType_Type()
)
wfNatIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIfType.setStatus("mandatory")


class _WfNatIfState_Type(Integer32):
    """Custom type wfNatIfState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfNatIfState_Type.__name__ = "Integer32"
_WfNatIfState_Object = MibTableColumn
wfNatIfState = _WfNatIfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 6),
    _WfNatIfState_Type()
)
wfNatIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIfState.setStatus("mandatory")
_WfNatIfTxCount_Type = Counter32
_WfNatIfTxCount_Object = MibTableColumn
wfNatIfTxCount = _WfNatIfTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 7),
    _WfNatIfTxCount_Type()
)
wfNatIfTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIfTxCount.setStatus("mandatory")
_WfNatIfRxCount_Type = Counter32
_WfNatIfRxCount_Object = MibTableColumn
wfNatIfRxCount = _WfNatIfRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 8),
    _WfNatIfRxCount_Type()
)
wfNatIfRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIfRxCount.setStatus("mandatory")
_WfNatIfPktDropCount_Type = Counter32
_WfNatIfPktDropCount_Object = MibTableColumn
wfNatIfPktDropCount = _WfNatIfPktDropCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 9),
    _WfNatIfPktDropCount_Type()
)
wfNatIfPktDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIfPktDropCount.setStatus("mandatory")
_WfNatIfDomain_Type = DisplayString
_WfNatIfDomain_Object = MibTableColumn
wfNatIfDomain = _WfNatIfDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 6, 1, 10),
    _WfNatIfDomain_Type()
)
wfNatIfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIfDomain.setStatus("mandatory")
_WfNatSynPeerTable_Object = MibTable
wfNatSynPeerTable = _WfNatSynPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7)
)
if mibBuilder.loadTexts:
    wfNatSynPeerTable.setStatus("mandatory")
_WfNatSynPeerEntry_Object = MibTableRow
wfNatSynPeerEntry = _WfNatSynPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1)
)
wfNatSynPeerEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatSynPeerRouterID"),
)
if mibBuilder.loadTexts:
    wfNatSynPeerEntry.setStatus("mandatory")


class _WfNatSynPeerDelete_Type(Integer32):
    """Custom type wfNatSynPeerDelete based on Integer32"""
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


_WfNatSynPeerDelete_Type.__name__ = "Integer32"
_WfNatSynPeerDelete_Object = MibTableColumn
wfNatSynPeerDelete = _WfNatSynPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 1),
    _WfNatSynPeerDelete_Type()
)
wfNatSynPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSynPeerDelete.setStatus("mandatory")


class _WfNatSynPeerDisable_Type(Integer32):
    """Custom type wfNatSynPeerDisable based on Integer32"""
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


_WfNatSynPeerDisable_Type.__name__ = "Integer32"
_WfNatSynPeerDisable_Object = MibTableColumn
wfNatSynPeerDisable = _WfNatSynPeerDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 2),
    _WfNatSynPeerDisable_Type()
)
wfNatSynPeerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSynPeerDisable.setStatus("mandatory")


class _WfNatSynPeerState_Type(Integer32):
    """Custom type wfNatSynPeerState based on Integer32"""
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
        *(("down", 4),
          ("established", 3),
          ("init", 2),
          ("not-present", 1))
    )


_WfNatSynPeerState_Type.__name__ = "Integer32"
_WfNatSynPeerState_Object = MibTableColumn
wfNatSynPeerState = _WfNatSynPeerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 3),
    _WfNatSynPeerState_Type()
)
wfNatSynPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSynPeerState.setStatus("mandatory")


class _WfNatSynPeerConnType_Type(Integer32):
    """Custom type wfNatSynPeerConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfNatSynPeerConnType_Type.__name__ = "Integer32"
_WfNatSynPeerConnType_Object = MibTableColumn
wfNatSynPeerConnType = _WfNatSynPeerConnType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 4),
    _WfNatSynPeerConnType_Type()
)
wfNatSynPeerConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSynPeerConnType.setStatus("mandatory")
_WfNatSynPeerRouterID_Type = IpAddress
_WfNatSynPeerRouterID_Object = MibTableColumn
wfNatSynPeerRouterID = _WfNatSynPeerRouterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 5),
    _WfNatSynPeerRouterID_Type()
)
wfNatSynPeerRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSynPeerRouterID.setStatus("mandatory")
_WfNatSynPeerAddress_Type = IpAddress
_WfNatSynPeerAddress_Object = MibTableColumn
wfNatSynPeerAddress = _WfNatSynPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 6),
    _WfNatSynPeerAddress_Type()
)
wfNatSynPeerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSynPeerAddress.setStatus("mandatory")
_WfNatSynPeerTransSent_Type = Integer32
_WfNatSynPeerTransSent_Object = MibTableColumn
wfNatSynPeerTransSent = _WfNatSynPeerTransSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 7),
    _WfNatSynPeerTransSent_Type()
)
wfNatSynPeerTransSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSynPeerTransSent.setStatus("mandatory")
_WfNatSynPeerTransRecd_Type = Integer32
_WfNatSynPeerTransRecd_Object = MibTableColumn
wfNatSynPeerTransRecd = _WfNatSynPeerTransRecd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 7, 1, 8),
    _WfNatSynPeerTransRecd_Type()
)
wfNatSynPeerTransRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSynPeerTransRecd.setStatus("mandatory")
_WfNatAddressRangeTable_Object = MibTable
wfNatAddressRangeTable = _WfNatAddressRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8)
)
if mibBuilder.loadTexts:
    wfNatAddressRangeTable.setStatus("mandatory")
_WfNatAddressRangeEntry_Object = MibTableRow
wfNatAddressRangeEntry = _WfNatAddressRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1)
)
wfNatAddressRangeEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatAddressRangeAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatAddressRangePrefixLen"),
    (0, "Wellfleet-NAT-MIB", "wfNatAddressRangeIndex"),
)
if mibBuilder.loadTexts:
    wfNatAddressRangeEntry.setStatus("mandatory")


class _WfNatAddressRangeDelete_Type(Integer32):
    """Custom type wfNatAddressRangeDelete based on Integer32"""
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


_WfNatAddressRangeDelete_Type.__name__ = "Integer32"
_WfNatAddressRangeDelete_Object = MibTableColumn
wfNatAddressRangeDelete = _WfNatAddressRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 1),
    _WfNatAddressRangeDelete_Type()
)
wfNatAddressRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeDelete.setStatus("mandatory")


class _WfNatAddressRangeDisable_Type(Integer32):
    """Custom type wfNatAddressRangeDisable based on Integer32"""
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


_WfNatAddressRangeDisable_Type.__name__ = "Integer32"
_WfNatAddressRangeDisable_Object = MibTableColumn
wfNatAddressRangeDisable = _WfNatAddressRangeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 2),
    _WfNatAddressRangeDisable_Type()
)
wfNatAddressRangeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeDisable.setStatus("mandatory")
_WfNatAddressRangeAddress_Type = IpAddress
_WfNatAddressRangeAddress_Object = MibTableColumn
wfNatAddressRangeAddress = _WfNatAddressRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 3),
    _WfNatAddressRangeAddress_Type()
)
wfNatAddressRangeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatAddressRangeAddress.setStatus("mandatory")


class _WfNatAddressRangePrefixLen_Type(Integer32):
    """Custom type wfNatAddressRangePrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfNatAddressRangePrefixLen_Type.__name__ = "Integer32"
_WfNatAddressRangePrefixLen_Object = MibTableColumn
wfNatAddressRangePrefixLen = _WfNatAddressRangePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 4),
    _WfNatAddressRangePrefixLen_Type()
)
wfNatAddressRangePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatAddressRangePrefixLen.setStatus("mandatory")
_WfNatAddressRangeIndex_Type = Integer32
_WfNatAddressRangeIndex_Object = MibTableColumn
wfNatAddressRangeIndex = _WfNatAddressRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 5),
    _WfNatAddressRangeIndex_Type()
)
wfNatAddressRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatAddressRangeIndex.setStatus("mandatory")


class _WfNatAddressRangeNto1Addr_Type(IpAddress):
    """Custom type wfNatAddressRangeNto1Addr based on IpAddress"""
    defaultValue = 0


_WfNatAddressRangeNto1Addr_Object = MibTableColumn
wfNatAddressRangeNto1Addr = _WfNatAddressRangeNto1Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 6),
    _WfNatAddressRangeNto1Addr_Type()
)
wfNatAddressRangeNto1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeNto1Addr.setStatus("mandatory")


class _WfNatAddressRangeType_Type(Integer32):
    """Custom type wfNatAddressRangeType based on Integer32"""
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
        *(("domainSrcAddrFilter", 3),
          ("domainTransPool", 4),
          ("sourceAddrFilter", 1),
          ("translationPool", 2))
    )


_WfNatAddressRangeType_Type.__name__ = "Integer32"
_WfNatAddressRangeType_Object = MibTableColumn
wfNatAddressRangeType = _WfNatAddressRangeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 7),
    _WfNatAddressRangeType_Type()
)
wfNatAddressRangeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeType.setStatus("mandatory")
_WfNatAddressRangeDomain_Type = DisplayString
_WfNatAddressRangeDomain_Object = MibTableColumn
wfNatAddressRangeDomain = _WfNatAddressRangeDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 8),
    _WfNatAddressRangeDomain_Type()
)
wfNatAddressRangeDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeDomain.setStatus("mandatory")


class _WfNatAddressRangeTransPool_Type(Integer32):
    """Custom type wfNatAddressRangeTransPool based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_WfNatAddressRangeTransPool_Type.__name__ = "Integer32"
_WfNatAddressRangeTransPool_Object = MibTableColumn
wfNatAddressRangeTransPool = _WfNatAddressRangeTransPool_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 9),
    _WfNatAddressRangeTransPool_Type()
)
wfNatAddressRangeTransPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeTransPool.setStatus("mandatory")


class _WfNatAddressRangeStaticNextHop_Type(IpAddress):
    """Custom type wfNatAddressRangeStaticNextHop based on IpAddress"""
    defaultValue = 0


_WfNatAddressRangeStaticNextHop_Object = MibTableColumn
wfNatAddressRangeStaticNextHop = _WfNatAddressRangeStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 10),
    _WfNatAddressRangeStaticNextHop_Type()
)
wfNatAddressRangeStaticNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeStaticNextHop.setStatus("mandatory")


class _WfNatAddressRangeUnnumCct_Type(Integer32):
    """Custom type wfNatAddressRangeUnnumCct based on Integer32"""
    defaultValue = 0


_WfNatAddressRangeUnnumCct_Object = MibTableColumn
wfNatAddressRangeUnnumCct = _WfNatAddressRangeUnnumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 8, 1, 11),
    _WfNatAddressRangeUnnumCct_Type()
)
wfNatAddressRangeUnnumCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatAddressRangeUnnumCct.setStatus("mandatory")
_WfNatStaticMappingTable_Object = MibTable
wfNatStaticMappingTable = _WfNatStaticMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9)
)
if mibBuilder.loadTexts:
    wfNatStaticMappingTable.setStatus("mandatory")
_WfNatStaticMappingEntry_Object = MibTableRow
wfNatStaticMappingEntry = _WfNatStaticMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1)
)
wfNatStaticMappingEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMappingTransAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMappingProtocol"),
    (0, "Wellfleet-NAT-MIB", "wfNatStaticMappingTransPort"),
)
if mibBuilder.loadTexts:
    wfNatStaticMappingEntry.setStatus("mandatory")


class _WfNatStaticMappingDelete_Type(Integer32):
    """Custom type wfNatStaticMappingDelete based on Integer32"""
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


_WfNatStaticMappingDelete_Type.__name__ = "Integer32"
_WfNatStaticMappingDelete_Object = MibTableColumn
wfNatStaticMappingDelete = _WfNatStaticMappingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 1),
    _WfNatStaticMappingDelete_Type()
)
wfNatStaticMappingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingDelete.setStatus("mandatory")


class _WfNatStaticMappingDisable_Type(Integer32):
    """Custom type wfNatStaticMappingDisable based on Integer32"""
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


_WfNatStaticMappingDisable_Type.__name__ = "Integer32"
_WfNatStaticMappingDisable_Object = MibTableColumn
wfNatStaticMappingDisable = _WfNatStaticMappingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 2),
    _WfNatStaticMappingDisable_Type()
)
wfNatStaticMappingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingDisable.setStatus("mandatory")
_WfNatStaticMappingOrigAddress_Type = IpAddress
_WfNatStaticMappingOrigAddress_Object = MibTableColumn
wfNatStaticMappingOrigAddress = _WfNatStaticMappingOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 3),
    _WfNatStaticMappingOrigAddress_Type()
)
wfNatStaticMappingOrigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingOrigAddress.setStatus("mandatory")
_WfNatStaticMappingTransAddress_Type = IpAddress
_WfNatStaticMappingTransAddress_Object = MibTableColumn
wfNatStaticMappingTransAddress = _WfNatStaticMappingTransAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 4),
    _WfNatStaticMappingTransAddress_Type()
)
wfNatStaticMappingTransAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatStaticMappingTransAddress.setStatus("mandatory")
_WfNatStaticMappingProtocol_Type = Integer32
_WfNatStaticMappingProtocol_Object = MibTableColumn
wfNatStaticMappingProtocol = _WfNatStaticMappingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 5),
    _WfNatStaticMappingProtocol_Type()
)
wfNatStaticMappingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatStaticMappingProtocol.setStatus("mandatory")
_WfNatStaticMappingOrigPort_Type = Integer32
_WfNatStaticMappingOrigPort_Object = MibTableColumn
wfNatStaticMappingOrigPort = _WfNatStaticMappingOrigPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 6),
    _WfNatStaticMappingOrigPort_Type()
)
wfNatStaticMappingOrigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingOrigPort.setStatus("mandatory")
_WfNatStaticMappingTransPort_Type = Integer32
_WfNatStaticMappingTransPort_Object = MibTableColumn
wfNatStaticMappingTransPort = _WfNatStaticMappingTransPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 7),
    _WfNatStaticMappingTransPort_Type()
)
wfNatStaticMappingTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatStaticMappingTransPort.setStatus("mandatory")


class _WfNatStaticMappingInDomain_Type(DisplayString):
    """Custom type wfNatStaticMappingInDomain based on DisplayString"""
    defaultValue = OctetString("private")


_WfNatStaticMappingInDomain_Object = MibTableColumn
wfNatStaticMappingInDomain = _WfNatStaticMappingInDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 8),
    _WfNatStaticMappingInDomain_Type()
)
wfNatStaticMappingInDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingInDomain.setStatus("mandatory")


class _WfNatStaticMappingOutDomain_Type(DisplayString):
    """Custom type wfNatStaticMappingOutDomain based on DisplayString"""
    defaultValue = OctetString("public")


_WfNatStaticMappingOutDomain_Object = MibTableColumn
wfNatStaticMappingOutDomain = _WfNatStaticMappingOutDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 9),
    _WfNatStaticMappingOutDomain_Type()
)
wfNatStaticMappingOutDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingOutDomain.setStatus("mandatory")


class _WfNatStaticMappingStaticNextHop_Type(IpAddress):
    """Custom type wfNatStaticMappingStaticNextHop based on IpAddress"""
    defaultValue = 0


_WfNatStaticMappingStaticNextHop_Object = MibTableColumn
wfNatStaticMappingStaticNextHop = _WfNatStaticMappingStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 10),
    _WfNatStaticMappingStaticNextHop_Type()
)
wfNatStaticMappingStaticNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingStaticNextHop.setStatus("mandatory")


class _WfNatStaticMappingUnnumCct_Type(Integer32):
    """Custom type wfNatStaticMappingUnnumCct based on Integer32"""
    defaultValue = 0


_WfNatStaticMappingUnnumCct_Object = MibTableColumn
wfNatStaticMappingUnnumCct = _WfNatStaticMappingUnnumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 9, 1, 11),
    _WfNatStaticMappingUnnumCct_Type()
)
wfNatStaticMappingUnnumCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatStaticMappingUnnumCct.setStatus("mandatory")
_WfNatMappingTable_Object = MibTable
wfNatMappingTable = _WfNatMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10)
)
if mibBuilder.loadTexts:
    wfNatMappingTable.setStatus("mandatory")
_WfNatMappingEntry_Object = MibTableRow
wfNatMappingEntry = _WfNatMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1)
)
wfNatMappingEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatMappingTransAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatMappingProtocol"),
    (0, "Wellfleet-NAT-MIB", "wfNatMappingTransPort"),
)
if mibBuilder.loadTexts:
    wfNatMappingEntry.setStatus("mandatory")
_WfNatMappingOrigAddress_Type = IpAddress
_WfNatMappingOrigAddress_Object = MibTableColumn
wfNatMappingOrigAddress = _WfNatMappingOrigAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 1),
    _WfNatMappingOrigAddress_Type()
)
wfNatMappingOrigAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingOrigAddress.setStatus("mandatory")
_WfNatMappingTransAddress_Type = IpAddress
_WfNatMappingTransAddress_Object = MibTableColumn
wfNatMappingTransAddress = _WfNatMappingTransAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 2),
    _WfNatMappingTransAddress_Type()
)
wfNatMappingTransAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingTransAddress.setStatus("mandatory")
_WfNatMappingProtocol_Type = Integer32
_WfNatMappingProtocol_Object = MibTableColumn
wfNatMappingProtocol = _WfNatMappingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 3),
    _WfNatMappingProtocol_Type()
)
wfNatMappingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingProtocol.setStatus("mandatory")
_WfNatMappingOrigPort_Type = Integer32
_WfNatMappingOrigPort_Object = MibTableColumn
wfNatMappingOrigPort = _WfNatMappingOrigPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 4),
    _WfNatMappingOrigPort_Type()
)
wfNatMappingOrigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingOrigPort.setStatus("mandatory")
_WfNatMappingTransPort_Type = Integer32
_WfNatMappingTransPort_Object = MibTableColumn
wfNatMappingTransPort = _WfNatMappingTransPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 5),
    _WfNatMappingTransPort_Type()
)
wfNatMappingTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingTransPort.setStatus("mandatory")
_WfNatMappingTxCount_Type = Counter32
_WfNatMappingTxCount_Object = MibTableColumn
wfNatMappingTxCount = _WfNatMappingTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 6),
    _WfNatMappingTxCount_Type()
)
wfNatMappingTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingTxCount.setStatus("mandatory")
_WfNatMappingRxCount_Type = Counter32
_WfNatMappingRxCount_Object = MibTableColumn
wfNatMappingRxCount = _WfNatMappingRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 7),
    _WfNatMappingRxCount_Type()
)
wfNatMappingRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingRxCount.setStatus("mandatory")
_WfNatMappingTimeout_Type = Counter32
_WfNatMappingTimeout_Object = MibTableColumn
wfNatMappingTimeout = _WfNatMappingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 8),
    _WfNatMappingTimeout_Type()
)
wfNatMappingTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingTimeout.setStatus("mandatory")


class _WfNatMappingMode_Type(Integer32):
    """Custom type wfNatMappingMode based on Integer32"""
    defaultValue = 0


_WfNatMappingMode_Object = MibTableColumn
wfNatMappingMode = _WfNatMappingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 9),
    _WfNatMappingMode_Type()
)
wfNatMappingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingMode.setStatus("mandatory")
_WfNatMappingInDomain_Type = DisplayString
_WfNatMappingInDomain_Object = MibTableColumn
wfNatMappingInDomain = _WfNatMappingInDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 10),
    _WfNatMappingInDomain_Type()
)
wfNatMappingInDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingInDomain.setStatus("mandatory")
_WfNatMappingOutDomain_Type = DisplayString
_WfNatMappingOutDomain_Object = MibTableColumn
wfNatMappingOutDomain = _WfNatMappingOutDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 10, 1, 11),
    _WfNatMappingOutDomain_Type()
)
wfNatMappingOutDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatMappingOutDomain.setStatus("mandatory")
_WfNatIntfTable_Object = MibTable
wfNatIntfTable = _WfNatIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11)
)
if mibBuilder.loadTexts:
    wfNatIntfTable.setStatus("mandatory")
_WfNatIntfEntry_Object = MibTableRow
wfNatIntfEntry = _WfNatIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1)
)
wfNatIntfEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatIntfIpAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatIntfCircuit"),
)
if mibBuilder.loadTexts:
    wfNatIntfEntry.setStatus("mandatory")


class _WfNatIntfDelete_Type(Integer32):
    """Custom type wfNatIntfDelete based on Integer32"""
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


_WfNatIntfDelete_Type.__name__ = "Integer32"
_WfNatIntfDelete_Object = MibTableColumn
wfNatIntfDelete = _WfNatIntfDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 1),
    _WfNatIntfDelete_Type()
)
wfNatIntfDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIntfDelete.setStatus("mandatory")


class _WfNatIntfDisable_Type(Integer32):
    """Custom type wfNatIntfDisable based on Integer32"""
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


_WfNatIntfDisable_Type.__name__ = "Integer32"
_WfNatIntfDisable_Object = MibTableColumn
wfNatIntfDisable = _WfNatIntfDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 2),
    _WfNatIntfDisable_Type()
)
wfNatIntfDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIntfDisable.setStatus("mandatory")
_WfNatIntfIpAddress_Type = IpAddress
_WfNatIntfIpAddress_Object = MibTableColumn
wfNatIntfIpAddress = _WfNatIntfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 3),
    _WfNatIntfIpAddress_Type()
)
wfNatIntfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIntfIpAddress.setStatus("mandatory")
_WfNatIntfCircuit_Type = Integer32
_WfNatIntfCircuit_Object = MibTableColumn
wfNatIntfCircuit = _WfNatIntfCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 4),
    _WfNatIntfCircuit_Type()
)
wfNatIntfCircuit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIntfCircuit.setStatus("mandatory")


class _WfNatIntfDomain_Type(DisplayString):
    """Custom type wfNatIntfDomain based on DisplayString"""
    defaultValue = OctetString("private")


_WfNatIntfDomain_Object = MibTableColumn
wfNatIntfDomain = _WfNatIntfDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 5),
    _WfNatIntfDomain_Type()
)
wfNatIntfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatIntfDomain.setStatus("mandatory")


class _WfNatIntfState_Type(Integer32):
    """Custom type wfNatIntfState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("up", 1))
    )


_WfNatIntfState_Type.__name__ = "Integer32"
_WfNatIntfState_Object = MibTableColumn
wfNatIntfState = _WfNatIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 6),
    _WfNatIntfState_Type()
)
wfNatIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIntfState.setStatus("mandatory")
_WfNatIntfTxCount_Type = Counter32
_WfNatIntfTxCount_Object = MibTableColumn
wfNatIntfTxCount = _WfNatIntfTxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 7),
    _WfNatIntfTxCount_Type()
)
wfNatIntfTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIntfTxCount.setStatus("mandatory")
_WfNatIntfRxCount_Type = Counter32
_WfNatIntfRxCount_Object = MibTableColumn
wfNatIntfRxCount = _WfNatIntfRxCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 8),
    _WfNatIntfRxCount_Type()
)
wfNatIntfRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIntfRxCount.setStatus("mandatory")
_WfNatIntfPktDropCount_Type = Counter32
_WfNatIntfPktDropCount_Object = MibTableColumn
wfNatIntfPktDropCount = _WfNatIntfPktDropCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 11, 1, 9),
    _WfNatIntfPktDropCount_Type()
)
wfNatIntfPktDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatIntfPktDropCount.setStatus("mandatory")
_WfNatSrcAddressFilterTable_Object = MibTable
wfNatSrcAddressFilterTable = _WfNatSrcAddressFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12)
)
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterTable.setStatus("mandatory")
_WfNatSrcAddressFilterEntry_Object = MibTableRow
wfNatSrcAddressFilterEntry = _WfNatSrcAddressFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1)
)
wfNatSrcAddressFilterEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatSrcAddressFilterAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatSrcAddressFilterPrefixLen"),
    (0, "Wellfleet-NAT-MIB", "wfNatSrcAddressFilterIndex"),
)
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterEntry.setStatus("mandatory")


class _WfNatSrcAddressFilterDelete_Type(Integer32):
    """Custom type wfNatSrcAddressFilterDelete based on Integer32"""
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


_WfNatSrcAddressFilterDelete_Type.__name__ = "Integer32"
_WfNatSrcAddressFilterDelete_Object = MibTableColumn
wfNatSrcAddressFilterDelete = _WfNatSrcAddressFilterDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 1),
    _WfNatSrcAddressFilterDelete_Type()
)
wfNatSrcAddressFilterDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterDelete.setStatus("mandatory")


class _WfNatSrcAddressFilterDisable_Type(Integer32):
    """Custom type wfNatSrcAddressFilterDisable based on Integer32"""
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


_WfNatSrcAddressFilterDisable_Type.__name__ = "Integer32"
_WfNatSrcAddressFilterDisable_Object = MibTableColumn
wfNatSrcAddressFilterDisable = _WfNatSrcAddressFilterDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 2),
    _WfNatSrcAddressFilterDisable_Type()
)
wfNatSrcAddressFilterDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterDisable.setStatus("mandatory")
_WfNatSrcAddressFilterAddress_Type = IpAddress
_WfNatSrcAddressFilterAddress_Object = MibTableColumn
wfNatSrcAddressFilterAddress = _WfNatSrcAddressFilterAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 3),
    _WfNatSrcAddressFilterAddress_Type()
)
wfNatSrcAddressFilterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterAddress.setStatus("mandatory")


class _WfNatSrcAddressFilterPrefixLen_Type(Integer32):
    """Custom type wfNatSrcAddressFilterPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfNatSrcAddressFilterPrefixLen_Type.__name__ = "Integer32"
_WfNatSrcAddressFilterPrefixLen_Object = MibTableColumn
wfNatSrcAddressFilterPrefixLen = _WfNatSrcAddressFilterPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 4),
    _WfNatSrcAddressFilterPrefixLen_Type()
)
wfNatSrcAddressFilterPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterPrefixLen.setStatus("mandatory")
_WfNatSrcAddressFilterIndex_Type = Integer32
_WfNatSrcAddressFilterIndex_Object = MibTableColumn
wfNatSrcAddressFilterIndex = _WfNatSrcAddressFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 5),
    _WfNatSrcAddressFilterIndex_Type()
)
wfNatSrcAddressFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterIndex.setStatus("mandatory")


class _WfNatSrcAddressFilterNto1Addr_Type(IpAddress):
    """Custom type wfNatSrcAddressFilterNto1Addr based on IpAddress"""
    defaultValue = 0


_WfNatSrcAddressFilterNto1Addr_Object = MibTableColumn
wfNatSrcAddressFilterNto1Addr = _WfNatSrcAddressFilterNto1Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 6),
    _WfNatSrcAddressFilterNto1Addr_Type()
)
wfNatSrcAddressFilterNto1Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterNto1Addr.setStatus("mandatory")


class _WfNatSrcAddressFilterDomain_Type(DisplayString):
    """Custom type wfNatSrcAddressFilterDomain based on DisplayString"""
    defaultValue = OctetString("private")


_WfNatSrcAddressFilterDomain_Object = MibTableColumn
wfNatSrcAddressFilterDomain = _WfNatSrcAddressFilterDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 7),
    _WfNatSrcAddressFilterDomain_Type()
)
wfNatSrcAddressFilterDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterDomain.setStatus("mandatory")


class _WfNatSrcAddressFilterTransPoolSelector_Type(Integer32):
    """Custom type wfNatSrcAddressFilterTransPoolSelector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_WfNatSrcAddressFilterTransPoolSelector_Type.__name__ = "Integer32"
_WfNatSrcAddressFilterTransPoolSelector_Object = MibTableColumn
wfNatSrcAddressFilterTransPoolSelector = _WfNatSrcAddressFilterTransPoolSelector_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 8),
    _WfNatSrcAddressFilterTransPoolSelector_Type()
)
wfNatSrcAddressFilterTransPoolSelector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterTransPoolSelector.setStatus("mandatory")


class _WfNatSrcAddressFilterStaticNextHop_Type(IpAddress):
    """Custom type wfNatSrcAddressFilterStaticNextHop based on IpAddress"""
    defaultValue = 0


_WfNatSrcAddressFilterStaticNextHop_Object = MibTableColumn
wfNatSrcAddressFilterStaticNextHop = _WfNatSrcAddressFilterStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 9),
    _WfNatSrcAddressFilterStaticNextHop_Type()
)
wfNatSrcAddressFilterStaticNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterStaticNextHop.setStatus("mandatory")


class _WfNatSrcAddressFilterUnnumCct_Type(Integer32):
    """Custom type wfNatSrcAddressFilterUnnumCct based on Integer32"""
    defaultValue = 0


_WfNatSrcAddressFilterUnnumCct_Object = MibTableColumn
wfNatSrcAddressFilterUnnumCct = _WfNatSrcAddressFilterUnnumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 12, 1, 10),
    _WfNatSrcAddressFilterUnnumCct_Type()
)
wfNatSrcAddressFilterUnnumCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatSrcAddressFilterUnnumCct.setStatus("mandatory")
_WfNatTranslationPoolTable_Object = MibTable
wfNatTranslationPoolTable = _WfNatTranslationPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13)
)
if mibBuilder.loadTexts:
    wfNatTranslationPoolTable.setStatus("mandatory")
_WfNatTranslationPoolEntry_Object = MibTableRow
wfNatTranslationPoolEntry = _WfNatTranslationPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1)
)
wfNatTranslationPoolEntry.setIndexNames(
    (0, "Wellfleet-NAT-MIB", "wfNatTranslationPoolAddress"),
    (0, "Wellfleet-NAT-MIB", "wfNatTranslationPoolPrefixLen"),
    (0, "Wellfleet-NAT-MIB", "wfNatTranslationPoolIndex"),
)
if mibBuilder.loadTexts:
    wfNatTranslationPoolEntry.setStatus("mandatory")


class _WfNatTranslationPoolDelete_Type(Integer32):
    """Custom type wfNatTranslationPoolDelete based on Integer32"""
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


_WfNatTranslationPoolDelete_Type.__name__ = "Integer32"
_WfNatTranslationPoolDelete_Object = MibTableColumn
wfNatTranslationPoolDelete = _WfNatTranslationPoolDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 1),
    _WfNatTranslationPoolDelete_Type()
)
wfNatTranslationPoolDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatTranslationPoolDelete.setStatus("mandatory")


class _WfNatTranslationPoolDisable_Type(Integer32):
    """Custom type wfNatTranslationPoolDisable based on Integer32"""
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


_WfNatTranslationPoolDisable_Type.__name__ = "Integer32"
_WfNatTranslationPoolDisable_Object = MibTableColumn
wfNatTranslationPoolDisable = _WfNatTranslationPoolDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 2),
    _WfNatTranslationPoolDisable_Type()
)
wfNatTranslationPoolDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatTranslationPoolDisable.setStatus("mandatory")
_WfNatTranslationPoolAddress_Type = IpAddress
_WfNatTranslationPoolAddress_Object = MibTableColumn
wfNatTranslationPoolAddress = _WfNatTranslationPoolAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 3),
    _WfNatTranslationPoolAddress_Type()
)
wfNatTranslationPoolAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatTranslationPoolAddress.setStatus("mandatory")


class _WfNatTranslationPoolPrefixLen_Type(Integer32):
    """Custom type wfNatTranslationPoolPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WfNatTranslationPoolPrefixLen_Type.__name__ = "Integer32"
_WfNatTranslationPoolPrefixLen_Object = MibTableColumn
wfNatTranslationPoolPrefixLen = _WfNatTranslationPoolPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 4),
    _WfNatTranslationPoolPrefixLen_Type()
)
wfNatTranslationPoolPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatTranslationPoolPrefixLen.setStatus("mandatory")
_WfNatTranslationPoolIndex_Type = Integer32
_WfNatTranslationPoolIndex_Object = MibTableColumn
wfNatTranslationPoolIndex = _WfNatTranslationPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 5),
    _WfNatTranslationPoolIndex_Type()
)
wfNatTranslationPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfNatTranslationPoolIndex.setStatus("mandatory")


class _WfNatTranslationPoolDomain_Type(DisplayString):
    """Custom type wfNatTranslationPoolDomain based on DisplayString"""
    defaultValue = OctetString("public")


_WfNatTranslationPoolDomain_Object = MibTableColumn
wfNatTranslationPoolDomain = _WfNatTranslationPoolDomain_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 7, 13, 1, 6),
    _WfNatTranslationPoolDomain_Type()
)
wfNatTranslationPoolDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfNatTranslationPoolDomain.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-NAT-MIB",
    **{"wfNatBase": wfNatBase,
       "wfNatBaseDelete": wfNatBaseDelete,
       "wfNatBaseDisable": wfNatBaseDisable,
       "wfNatBaseState": wfNatBaseState,
       "wfNatBaseSoloistSlotMask": wfNatBaseSoloistSlotMask,
       "wfNatBaseSoloistSlot": wfNatBaseSoloistSlot,
       "wfNatBaseLogMask": wfNatBaseLogMask,
       "wfNatBaseMapTimeout": wfNatBaseMapTimeout,
       "wfNatBaseMapMaxTimeout": wfNatBaseMapMaxTimeout,
       "wfNatBaseMapDynMapsCount": wfNatBaseMapDynMapsCount,
       "wfNatBaseFtpSessionCount": wfNatBaseFtpSessionCount,
       "wfNatBaseNto1TrTotCount": wfNatBaseNto1TrTotCount,
       "wfNatBaseSynchronization": wfNatBaseSynchronization,
       "wfNatBaseSynRouterID": wfNatBaseSynRouterID,
       "wfNatBaseSynPort": wfNatBaseSynPort,
       "wfNatBaseSynKeepAlvInterval": wfNatBaseSynKeepAlvInterval,
       "wfNatBaseSynKeepAlvTimer": wfNatBaseSynKeepAlvTimer,
       "wfNatBaseSynKeepAlvRetries": wfNatBaseSynKeepAlvRetries,
       "wfNatBaseLocalToLocalEnable": wfNatBaseLocalToLocalEnable,
       "wfNatBaseInstallUniPrivAddr": wfNatBaseInstallUniPrivAddr,
       "wfNatAddrRangeTable": wfNatAddrRangeTable,
       "wfNatAddrRangeEntry": wfNatAddrRangeEntry,
       "wfNatAddrRangeDelete": wfNatAddrRangeDelete,
       "wfNatAddrRangeDisable": wfNatAddrRangeDisable,
       "wfNatAddrRangeAddress": wfNatAddrRangeAddress,
       "wfNatAddrRangePrefixLen": wfNatAddrRangePrefixLen,
       "wfNatLocalAddrRangeTable": wfNatLocalAddrRangeTable,
       "wfNatLocalAddrRangeEntry": wfNatLocalAddrRangeEntry,
       "wfNatLocalAddrRangeDelete": wfNatLocalAddrRangeDelete,
       "wfNatLocalAddrRangeDisable": wfNatLocalAddrRangeDisable,
       "wfNatLocalAddrRangeAddress": wfNatLocalAddrRangeAddress,
       "wfNatLocalAddrRangePrefixLen": wfNatLocalAddrRangePrefixLen,
       "wfNatLocalAddrRangeNto1Addr": wfNatLocalAddrRangeNto1Addr,
       "wfNatStaticMapTable": wfNatStaticMapTable,
       "wfNatStaticMapEntry": wfNatStaticMapEntry,
       "wfNatStaticMapDelete": wfNatStaticMapDelete,
       "wfNatStaticMapDisable": wfNatStaticMapDisable,
       "wfNatStaticMapLocalAddress": wfNatStaticMapLocalAddress,
       "wfNatStaticMapGlobalAddress": wfNatStaticMapGlobalAddress,
       "wfNatStaticMapProtocol": wfNatStaticMapProtocol,
       "wfNatStaticMapLocalPort": wfNatStaticMapLocalPort,
       "wfNatStaticMapGlobalPort": wfNatStaticMapGlobalPort,
       "wfNatMapTable": wfNatMapTable,
       "wfNatMapEntry": wfNatMapEntry,
       "wfNatMapLocalAddress": wfNatMapLocalAddress,
       "wfNatMapGlobalAddress": wfNatMapGlobalAddress,
       "wfNatMapProtocol": wfNatMapProtocol,
       "wfNatMapLocalPort": wfNatMapLocalPort,
       "wfNatMapGlobalPort": wfNatMapGlobalPort,
       "wfNatMapTxCount": wfNatMapTxCount,
       "wfNatMapRxCount": wfNatMapRxCount,
       "wfNatMapTimeout": wfNatMapTimeout,
       "wfNatMapMode": wfNatMapMode,
       "wfNatIfTable": wfNatIfTable,
       "wfNatIfEntry": wfNatIfEntry,
       "wfNatIfDelete": wfNatIfDelete,
       "wfNatIfDisable": wfNatIfDisable,
       "wfNatIfIpAddress": wfNatIfIpAddress,
       "wfNatIfCircuit": wfNatIfCircuit,
       "wfNatIfType": wfNatIfType,
       "wfNatIfState": wfNatIfState,
       "wfNatIfTxCount": wfNatIfTxCount,
       "wfNatIfRxCount": wfNatIfRxCount,
       "wfNatIfPktDropCount": wfNatIfPktDropCount,
       "wfNatIfDomain": wfNatIfDomain,
       "wfNatSynPeerTable": wfNatSynPeerTable,
       "wfNatSynPeerEntry": wfNatSynPeerEntry,
       "wfNatSynPeerDelete": wfNatSynPeerDelete,
       "wfNatSynPeerDisable": wfNatSynPeerDisable,
       "wfNatSynPeerState": wfNatSynPeerState,
       "wfNatSynPeerConnType": wfNatSynPeerConnType,
       "wfNatSynPeerRouterID": wfNatSynPeerRouterID,
       "wfNatSynPeerAddress": wfNatSynPeerAddress,
       "wfNatSynPeerTransSent": wfNatSynPeerTransSent,
       "wfNatSynPeerTransRecd": wfNatSynPeerTransRecd,
       "wfNatAddressRangeTable": wfNatAddressRangeTable,
       "wfNatAddressRangeEntry": wfNatAddressRangeEntry,
       "wfNatAddressRangeDelete": wfNatAddressRangeDelete,
       "wfNatAddressRangeDisable": wfNatAddressRangeDisable,
       "wfNatAddressRangeAddress": wfNatAddressRangeAddress,
       "wfNatAddressRangePrefixLen": wfNatAddressRangePrefixLen,
       "wfNatAddressRangeIndex": wfNatAddressRangeIndex,
       "wfNatAddressRangeNto1Addr": wfNatAddressRangeNto1Addr,
       "wfNatAddressRangeType": wfNatAddressRangeType,
       "wfNatAddressRangeDomain": wfNatAddressRangeDomain,
       "wfNatAddressRangeTransPool": wfNatAddressRangeTransPool,
       "wfNatAddressRangeStaticNextHop": wfNatAddressRangeStaticNextHop,
       "wfNatAddressRangeUnnumCct": wfNatAddressRangeUnnumCct,
       "wfNatStaticMappingTable": wfNatStaticMappingTable,
       "wfNatStaticMappingEntry": wfNatStaticMappingEntry,
       "wfNatStaticMappingDelete": wfNatStaticMappingDelete,
       "wfNatStaticMappingDisable": wfNatStaticMappingDisable,
       "wfNatStaticMappingOrigAddress": wfNatStaticMappingOrigAddress,
       "wfNatStaticMappingTransAddress": wfNatStaticMappingTransAddress,
       "wfNatStaticMappingProtocol": wfNatStaticMappingProtocol,
       "wfNatStaticMappingOrigPort": wfNatStaticMappingOrigPort,
       "wfNatStaticMappingTransPort": wfNatStaticMappingTransPort,
       "wfNatStaticMappingInDomain": wfNatStaticMappingInDomain,
       "wfNatStaticMappingOutDomain": wfNatStaticMappingOutDomain,
       "wfNatStaticMappingStaticNextHop": wfNatStaticMappingStaticNextHop,
       "wfNatStaticMappingUnnumCct": wfNatStaticMappingUnnumCct,
       "wfNatMappingTable": wfNatMappingTable,
       "wfNatMappingEntry": wfNatMappingEntry,
       "wfNatMappingOrigAddress": wfNatMappingOrigAddress,
       "wfNatMappingTransAddress": wfNatMappingTransAddress,
       "wfNatMappingProtocol": wfNatMappingProtocol,
       "wfNatMappingOrigPort": wfNatMappingOrigPort,
       "wfNatMappingTransPort": wfNatMappingTransPort,
       "wfNatMappingTxCount": wfNatMappingTxCount,
       "wfNatMappingRxCount": wfNatMappingRxCount,
       "wfNatMappingTimeout": wfNatMappingTimeout,
       "wfNatMappingMode": wfNatMappingMode,
       "wfNatMappingInDomain": wfNatMappingInDomain,
       "wfNatMappingOutDomain": wfNatMappingOutDomain,
       "wfNatIntfTable": wfNatIntfTable,
       "wfNatIntfEntry": wfNatIntfEntry,
       "wfNatIntfDelete": wfNatIntfDelete,
       "wfNatIntfDisable": wfNatIntfDisable,
       "wfNatIntfIpAddress": wfNatIntfIpAddress,
       "wfNatIntfCircuit": wfNatIntfCircuit,
       "wfNatIntfDomain": wfNatIntfDomain,
       "wfNatIntfState": wfNatIntfState,
       "wfNatIntfTxCount": wfNatIntfTxCount,
       "wfNatIntfRxCount": wfNatIntfRxCount,
       "wfNatIntfPktDropCount": wfNatIntfPktDropCount,
       "wfNatSrcAddressFilterTable": wfNatSrcAddressFilterTable,
       "wfNatSrcAddressFilterEntry": wfNatSrcAddressFilterEntry,
       "wfNatSrcAddressFilterDelete": wfNatSrcAddressFilterDelete,
       "wfNatSrcAddressFilterDisable": wfNatSrcAddressFilterDisable,
       "wfNatSrcAddressFilterAddress": wfNatSrcAddressFilterAddress,
       "wfNatSrcAddressFilterPrefixLen": wfNatSrcAddressFilterPrefixLen,
       "wfNatSrcAddressFilterIndex": wfNatSrcAddressFilterIndex,
       "wfNatSrcAddressFilterNto1Addr": wfNatSrcAddressFilterNto1Addr,
       "wfNatSrcAddressFilterDomain": wfNatSrcAddressFilterDomain,
       "wfNatSrcAddressFilterTransPoolSelector": wfNatSrcAddressFilterTransPoolSelector,
       "wfNatSrcAddressFilterStaticNextHop": wfNatSrcAddressFilterStaticNextHop,
       "wfNatSrcAddressFilterUnnumCct": wfNatSrcAddressFilterUnnumCct,
       "wfNatTranslationPoolTable": wfNatTranslationPoolTable,
       "wfNatTranslationPoolEntry": wfNatTranslationPoolEntry,
       "wfNatTranslationPoolDelete": wfNatTranslationPoolDelete,
       "wfNatTranslationPoolDisable": wfNatTranslationPoolDisable,
       "wfNatTranslationPoolAddress": wfNatTranslationPoolAddress,
       "wfNatTranslationPoolPrefixLen": wfNatTranslationPoolPrefixLen,
       "wfNatTranslationPoolIndex": wfNatTranslationPoolIndex,
       "wfNatTranslationPoolDomain": wfNatTranslationPoolDomain}
)
