# SNMP MIB module (CXSnaLinkConversionModule-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXSnaLinkConversionModule-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:52 2024
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

(Alias,
 SapIndex,
 cxSnalc) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "SapIndex",
    "cxSnalc")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SnalcMibLevel_Type(Integer32):
    """Custom type snalcMibLevel based on Integer32"""
    defaultValue = 0


_SnalcMibLevel_Object = MibScalar
snalcMibLevel = _SnalcMibLevel_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 9),
    _SnalcMibLevel_Type()
)
snalcMibLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcMibLevel.setStatus("mandatory")
_SnalcSapTable_Object = MibTable
snalcSapTable = _SnalcSapTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10)
)
if mibBuilder.loadTexts:
    snalcSapTable.setStatus("mandatory")
_SnalcSapEntry_Object = MibTableRow
snalcSapEntry = _SnalcSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1)
)
snalcSapEntry.setIndexNames(
    (0, "CXSnaLinkConversionModule-MIB", "snalcSapNumber"),
)
if mibBuilder.loadTexts:
    snalcSapEntry.setStatus("mandatory")
_SnalcSapNumber_Type = SapIndex
_SnalcSapNumber_Object = MibTableColumn
snalcSapNumber = _SnalcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1, 1),
    _SnalcSapNumber_Type()
)
snalcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcSapNumber.setStatus("mandatory")


class _SnalcSapRowStatus_Type(Integer32):
    """Custom type snalcSapRowStatus based on Integer32"""
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


_SnalcSapRowStatus_Type.__name__ = "Integer32"
_SnalcSapRowStatus_Object = MibTableColumn
snalcSapRowStatus = _SnalcSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1, 2),
    _SnalcSapRowStatus_Type()
)
snalcSapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcSapRowStatus.setStatus("mandatory")
_SnalcSapAlias_Type = Alias
_SnalcSapAlias_Object = MibTableColumn
snalcSapAlias = _SnalcSapAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1, 3),
    _SnalcSapAlias_Type()
)
snalcSapAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcSapAlias.setStatus("mandatory")
_SnalcSapCompanionAlias_Type = Alias
_SnalcSapCompanionAlias_Object = MibTableColumn
snalcSapCompanionAlias = _SnalcSapCompanionAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1, 4),
    _SnalcSapCompanionAlias_Type()
)
snalcSapCompanionAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcSapCompanionAlias.setStatus("mandatory")


class _SnalcSapState_Type(Integer32):
    """Custom type snalcSapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("offLine", 1),
          ("unbound", 2))
    )


_SnalcSapState_Type.__name__ = "Integer32"
_SnalcSapState_Object = MibTableColumn
snalcSapState = _SnalcSapState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 10, 1, 6),
    _SnalcSapState_Type()
)
snalcSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcSapState.setStatus("mandatory")
_SnalcCrossConnectTable_Object = MibTable
snalcCrossConnectTable = _SnalcCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11)
)
if mibBuilder.loadTexts:
    snalcCrossConnectTable.setStatus("mandatory")
_SnalcCrossConnectEntry_Object = MibTableRow
snalcCrossConnectEntry = _SnalcCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1)
)
snalcCrossConnectEntry.setIndexNames(
    (0, "CXSnaLinkConversionModule-MIB", "snalcCrossConnectSrcSapNumber"),
    (0, "CXSnaLinkConversionModule-MIB", "snalcCrossConnectSrcLinkAddrIndex"),
    (0, "CXSnaLinkConversionModule-MIB", "snalcCrossConnectDstSapNumber"),
    (0, "CXSnaLinkConversionModule-MIB", "snalcCrossConnectDstLinkAddrIndex"),
)
if mibBuilder.loadTexts:
    snalcCrossConnectEntry.setStatus("mandatory")
_SnalcCrossConnectSrcSapNumber_Type = SapIndex
_SnalcCrossConnectSrcSapNumber_Object = MibTableColumn
snalcCrossConnectSrcSapNumber = _SnalcCrossConnectSrcSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 1),
    _SnalcCrossConnectSrcSapNumber_Type()
)
snalcCrossConnectSrcSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectSrcSapNumber.setStatus("mandatory")


class _SnalcCrossConnectSrcLinkAddrIndex_Type(Integer32):
    """Custom type snalcCrossConnectSrcLinkAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnalcCrossConnectSrcLinkAddrIndex_Type.__name__ = "Integer32"
_SnalcCrossConnectSrcLinkAddrIndex_Object = MibTableColumn
snalcCrossConnectSrcLinkAddrIndex = _SnalcCrossConnectSrcLinkAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 2),
    _SnalcCrossConnectSrcLinkAddrIndex_Type()
)
snalcCrossConnectSrcLinkAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectSrcLinkAddrIndex.setStatus("mandatory")
_SnalcCrossConnectDstSapNumber_Type = SapIndex
_SnalcCrossConnectDstSapNumber_Object = MibTableColumn
snalcCrossConnectDstSapNumber = _SnalcCrossConnectDstSapNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 3),
    _SnalcCrossConnectDstSapNumber_Type()
)
snalcCrossConnectDstSapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectDstSapNumber.setStatus("mandatory")


class _SnalcCrossConnectDstLinkAddrIndex_Type(Integer32):
    """Custom type snalcCrossConnectDstLinkAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnalcCrossConnectDstLinkAddrIndex_Type.__name__ = "Integer32"
_SnalcCrossConnectDstLinkAddrIndex_Object = MibTableColumn
snalcCrossConnectDstLinkAddrIndex = _SnalcCrossConnectDstLinkAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 4),
    _SnalcCrossConnectDstLinkAddrIndex_Type()
)
snalcCrossConnectDstLinkAddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectDstLinkAddrIndex.setStatus("mandatory")


class _SnalcCrossConnectRowStatus_Type(Integer32):
    """Custom type snalcCrossConnectRowStatus based on Integer32"""
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


_SnalcCrossConnectRowStatus_Type.__name__ = "Integer32"
_SnalcCrossConnectRowStatus_Object = MibTableColumn
snalcCrossConnectRowStatus = _SnalcCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 5),
    _SnalcCrossConnectRowStatus_Type()
)
snalcCrossConnectRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectRowStatus.setStatus("mandatory")


class _SnalcCrossConnectPuId_Type(OctetString):
    """Custom type snalcCrossConnectPuId based on OctetString"""
    defaultHexValue = "00000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnalcCrossConnectPuId_Type.__name__ = "OctetString"
_SnalcCrossConnectPuId_Object = MibTableColumn
snalcCrossConnectPuId = _SnalcCrossConnectPuId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 6),
    _SnalcCrossConnectPuId_Type()
)
snalcCrossConnectPuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectPuId.setStatus("mandatory")


class _SnalcCrossConnectMaxRetries_Type(Integer32):
    """Custom type snalcCrossConnectMaxRetries based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnalcCrossConnectMaxRetries_Type.__name__ = "Integer32"
_SnalcCrossConnectMaxRetries_Object = MibTableColumn
snalcCrossConnectMaxRetries = _SnalcCrossConnectMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 7),
    _SnalcCrossConnectMaxRetries_Type()
)
snalcCrossConnectMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectMaxRetries.setStatus("mandatory")


class _SnalcCrossConnectConnectInterval_Type(Integer32):
    """Custom type snalcCrossConnectConnectInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnalcCrossConnectConnectInterval_Type.__name__ = "Integer32"
_SnalcCrossConnectConnectInterval_Object = MibTableColumn
snalcCrossConnectConnectInterval = _SnalcCrossConnectConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 8),
    _SnalcCrossConnectConnectInterval_Type()
)
snalcCrossConnectConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectConnectInterval.setStatus("mandatory")


class _SnalcCrossConnectSlowConnectThreshold_Type(Integer32):
    """Custom type snalcCrossConnectSlowConnectThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_SnalcCrossConnectSlowConnectThreshold_Type.__name__ = "Integer32"
_SnalcCrossConnectSlowConnectThreshold_Object = MibTableColumn
snalcCrossConnectSlowConnectThreshold = _SnalcCrossConnectSlowConnectThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 9),
    _SnalcCrossConnectSlowConnectThreshold_Type()
)
snalcCrossConnectSlowConnectThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectSlowConnectThreshold.setStatus("mandatory")


class _SnalcCrossConnectSlowConnectInterval_Type(Integer32):
    """Custom type snalcCrossConnectSlowConnectInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnalcCrossConnectSlowConnectInterval_Type.__name__ = "Integer32"
_SnalcCrossConnectSlowConnectInterval_Object = MibTableColumn
snalcCrossConnectSlowConnectInterval = _SnalcCrossConnectSlowConnectInterval_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 10),
    _SnalcCrossConnectSlowConnectInterval_Type()
)
snalcCrossConnectSlowConnectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectSlowConnectInterval.setStatus("mandatory")


class _SnalcCrossConnectWaitContactTimer_Type(Integer32):
    """Custom type snalcCrossConnectWaitContactTimer based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnalcCrossConnectWaitContactTimer_Type.__name__ = "Integer32"
_SnalcCrossConnectWaitContactTimer_Object = MibTableColumn
snalcCrossConnectWaitContactTimer = _SnalcCrossConnectWaitContactTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 11),
    _SnalcCrossConnectWaitContactTimer_Type()
)
snalcCrossConnectWaitContactTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectWaitContactTimer.setStatus("mandatory")


class _SnalcCrossConnectConnectMethod_Type(Integer32):
    """Custom type snalcCrossConnectConnectMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("endToEnd", 2),
          ("local", 1))
    )


_SnalcCrossConnectConnectMethod_Type.__name__ = "Integer32"
_SnalcCrossConnectConnectMethod_Object = MibTableColumn
snalcCrossConnectConnectMethod = _SnalcCrossConnectConnectMethod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 12),
    _SnalcCrossConnectConnectMethod_Type()
)
snalcCrossConnectConnectMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectConnectMethod.setStatus("mandatory")


class _SnalcCrossConnectAdminStatus_Type(Integer32):
    """Custom type snalcCrossConnectAdminStatus based on Integer32"""
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


_SnalcCrossConnectAdminStatus_Type.__name__ = "Integer32"
_SnalcCrossConnectAdminStatus_Object = MibTableColumn
snalcCrossConnectAdminStatus = _SnalcCrossConnectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 13),
    _SnalcCrossConnectAdminStatus_Type()
)
snalcCrossConnectAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectAdminStatus.setStatus("mandatory")


class _SnalcCrossConnectSrcOperStatus_Type(Integer32):
    """Custom type snalcCrossConnectSrcOperStatus based on Integer32"""
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
        *(("associated", 10),
          ("connecting", 3),
          ("data", 15),
          ("delayConnect", 9),
          ("disconnecting", 11),
          ("failed", 14),
          ("linkDisconnecting", 12),
          ("notConnected", 2),
          ("offLine", 1),
          ("sendXid", 7),
          ("setMode", 5),
          ("waitDisconnect", 13),
          ("waitPartner", 6),
          ("waitSetMode", 8),
          ("waitXid", 4))
    )


_SnalcCrossConnectSrcOperStatus_Type.__name__ = "Integer32"
_SnalcCrossConnectSrcOperStatus_Object = MibTableColumn
snalcCrossConnectSrcOperStatus = _SnalcCrossConnectSrcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 14),
    _SnalcCrossConnectSrcOperStatus_Type()
)
snalcCrossConnectSrcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectSrcOperStatus.setStatus("mandatory")


class _SnalcCrossConnectDstOperStatus_Type(Integer32):
    """Custom type snalcCrossConnectDstOperStatus based on Integer32"""
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
        *(("associated", 10),
          ("connecting", 3),
          ("data", 15),
          ("delayConnect", 9),
          ("disconnecting", 11),
          ("failed", 14),
          ("linkDisconnecting", 12),
          ("notConnected", 2),
          ("offLine", 1),
          ("sendXid", 7),
          ("setMode", 5),
          ("waitDisconnect", 13),
          ("waitPartner", 6),
          ("waitSetMode", 8),
          ("waitXid", 4))
    )


_SnalcCrossConnectDstOperStatus_Type.__name__ = "Integer32"
_SnalcCrossConnectDstOperStatus_Object = MibTableColumn
snalcCrossConnectDstOperStatus = _SnalcCrossConnectDstOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 15),
    _SnalcCrossConnectDstOperStatus_Type()
)
snalcCrossConnectDstOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snalcCrossConnectDstOperStatus.setStatus("mandatory")


class _SnalcCrossConnectXidTransparent_Type(Integer32):
    """Custom type snalcCrossConnectXidTransparent based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonTransparent", 1),
          ("transparent", 2))
    )


_SnalcCrossConnectXidTransparent_Type.__name__ = "Integer32"
_SnalcCrossConnectXidTransparent_Object = MibTableColumn
snalcCrossConnectXidTransparent = _SnalcCrossConnectXidTransparent_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 16),
    _SnalcCrossConnectXidTransparent_Type()
)
snalcCrossConnectXidTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectXidTransparent.setStatus("mandatory")


class _SnalcCrossConnectDataLinkType_Type(Integer32):
    """Custom type snalcCrossConnectDataLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bsc", 2),
          ("sna", 1))
    )


_SnalcCrossConnectDataLinkType_Type.__name__ = "Integer32"
_SnalcCrossConnectDataLinkType_Object = MibTableColumn
snalcCrossConnectDataLinkType = _SnalcCrossConnectDataLinkType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 35, 11, 1, 17),
    _SnalcCrossConnectDataLinkType_Type()
)
snalcCrossConnectDataLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snalcCrossConnectDataLinkType.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXSnaLinkConversionModule-MIB",
    **{"snalcMibLevel": snalcMibLevel,
       "snalcSapTable": snalcSapTable,
       "snalcSapEntry": snalcSapEntry,
       "snalcSapNumber": snalcSapNumber,
       "snalcSapRowStatus": snalcSapRowStatus,
       "snalcSapAlias": snalcSapAlias,
       "snalcSapCompanionAlias": snalcSapCompanionAlias,
       "snalcSapState": snalcSapState,
       "snalcCrossConnectTable": snalcCrossConnectTable,
       "snalcCrossConnectEntry": snalcCrossConnectEntry,
       "snalcCrossConnectSrcSapNumber": snalcCrossConnectSrcSapNumber,
       "snalcCrossConnectSrcLinkAddrIndex": snalcCrossConnectSrcLinkAddrIndex,
       "snalcCrossConnectDstSapNumber": snalcCrossConnectDstSapNumber,
       "snalcCrossConnectDstLinkAddrIndex": snalcCrossConnectDstLinkAddrIndex,
       "snalcCrossConnectRowStatus": snalcCrossConnectRowStatus,
       "snalcCrossConnectPuId": snalcCrossConnectPuId,
       "snalcCrossConnectMaxRetries": snalcCrossConnectMaxRetries,
       "snalcCrossConnectConnectInterval": snalcCrossConnectConnectInterval,
       "snalcCrossConnectSlowConnectThreshold": snalcCrossConnectSlowConnectThreshold,
       "snalcCrossConnectSlowConnectInterval": snalcCrossConnectSlowConnectInterval,
       "snalcCrossConnectWaitContactTimer": snalcCrossConnectWaitContactTimer,
       "snalcCrossConnectConnectMethod": snalcCrossConnectConnectMethod,
       "snalcCrossConnectAdminStatus": snalcCrossConnectAdminStatus,
       "snalcCrossConnectSrcOperStatus": snalcCrossConnectSrcOperStatus,
       "snalcCrossConnectDstOperStatus": snalcCrossConnectDstOperStatus,
       "snalcCrossConnectXidTransparent": snalcCrossConnectXidTransparent,
       "snalcCrossConnectDataLinkType": snalcCrossConnectDataLinkType}
)
