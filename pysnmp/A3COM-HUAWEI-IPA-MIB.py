# SNMP MIB module (A3COM-HUAWEI-IPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-IPA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:10 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

h3cIpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_H3cIpaGlobalStats_ObjectIdentity = ObjectIdentity
h3cIpaGlobalStats = _H3cIpaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1)
)


class _H3cIpaGlobalEnable_Type(Integer32):
    """Custom type h3cIpaGlobalEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_H3cIpaGlobalEnable_Type.__name__ = "Integer32"
_H3cIpaGlobalEnable_Object = MibScalar
h3cIpaGlobalEnable = _H3cIpaGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 1),
    _H3cIpaGlobalEnable_Type()
)
h3cIpaGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaGlobalEnable.setStatus("current")


class _H3cIpaTimeOutSeconds_Type(Integer32):
    """Custom type h3cIpaTimeOutSeconds based on Integer32"""
    defaultValue = 43200


_H3cIpaTimeOutSeconds_Object = MibScalar
h3cIpaTimeOutSeconds = _H3cIpaTimeOutSeconds_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 2),
    _H3cIpaTimeOutSeconds_Type()
)
h3cIpaTimeOutSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaTimeOutSeconds.setStatus("current")


class _H3cIpaIntListMaxItemNum_Type(Integer32):
    """Custom type h3cIpaIntListMaxItemNum based on Integer32"""
    defaultValue = 512


_H3cIpaIntListMaxItemNum_Object = MibScalar
h3cIpaIntListMaxItemNum = _H3cIpaIntListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 3),
    _H3cIpaIntListMaxItemNum_Type()
)
h3cIpaIntListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaIntListMaxItemNum.setStatus("current")


class _H3cIpaExtListMaxItemNum_Type(Integer32):
    """Custom type h3cIpaExtListMaxItemNum based on Integer32"""
    defaultValue = 0


_H3cIpaExtListMaxItemNum_Object = MibScalar
h3cIpaExtListMaxItemNum = _H3cIpaExtListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 4),
    _H3cIpaExtListMaxItemNum_Type()
)
h3cIpaExtListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaExtListMaxItemNum.setStatus("current")
_H3cIpaFWListMaxItemNum_Type = Integer32
_H3cIpaFWListMaxItemNum_Object = MibScalar
h3cIpaFWListMaxItemNum = _H3cIpaFWListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 5),
    _H3cIpaFWListMaxItemNum_Type()
)
h3cIpaFWListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaFWListMaxItemNum.setStatus("current")
_H3cIpaAccountListMaxItemNum_Type = Integer32
_H3cIpaAccountListMaxItemNum_Object = MibScalar
h3cIpaAccountListMaxItemNum = _H3cIpaAccountListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 6),
    _H3cIpaAccountListMaxItemNum_Type()
)
h3cIpaAccountListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaAccountListMaxItemNum.setStatus("current")
_H3cIpaAccountListNextIndex_Type = Integer32
_H3cIpaAccountListNextIndex_Object = MibScalar
h3cIpaAccountListNextIndex = _H3cIpaAccountListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 7),
    _H3cIpaAccountListNextIndex_Type()
)
h3cIpaAccountListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaAccountListNextIndex.setStatus("current")


class _H3cIpaListCleaningFlag_Type(Integer32):
    """Custom type h3cIpaListCleaningFlag based on Integer32"""
    defaultValue = 1

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
        *(("cleaningAll", 2),
          ("cleaningExtList", 4),
          ("cleaningFWList", 5),
          ("cleaningIntList", 3),
          ("idle", 1))
    )


_H3cIpaListCleaningFlag_Type.__name__ = "Integer32"
_H3cIpaListCleaningFlag_Object = MibScalar
h3cIpaListCleaningFlag = _H3cIpaListCleaningFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 1, 8),
    _H3cIpaListCleaningFlag_Type()
)
h3cIpaListCleaningFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaListCleaningFlag.setStatus("current")
_H3cIpaIfConfigTable_Object = MibTable
h3cIpaIfConfigTable = _H3cIpaIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2)
)
if mibBuilder.loadTexts:
    h3cIpaIfConfigTable.setStatus("current")
_H3cIpaIfConfigEntry_Object = MibTableRow
h3cIpaIfConfigEntry = _H3cIpaIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1)
)
h3cIpaIfConfigEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    h3cIpaIfConfigEntry.setStatus("current")
_H3cIpaIfConfigIfIndex_Type = InterfaceIndex
_H3cIpaIfConfigIfIndex_Object = MibTableColumn
h3cIpaIfConfigIfIndex = _H3cIpaIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 1),
    _H3cIpaIfConfigIfIndex_Type()
)
h3cIpaIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaIfConfigIfIndex.setStatus("current")


class _H3cIpaIfConfigInEnable_Type(Integer32):
    """Custom type h3cIpaIfConfigInEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_H3cIpaIfConfigInEnable_Type.__name__ = "Integer32"
_H3cIpaIfConfigInEnable_Object = MibTableColumn
h3cIpaIfConfigInEnable = _H3cIpaIfConfigInEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 2),
    _H3cIpaIfConfigInEnable_Type()
)
h3cIpaIfConfigInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaIfConfigInEnable.setStatus("current")


class _H3cIpaIfConfigOutEnable_Type(Integer32):
    """Custom type h3cIpaIfConfigOutEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_H3cIpaIfConfigOutEnable_Type.__name__ = "Integer32"
_H3cIpaIfConfigOutEnable_Object = MibTableColumn
h3cIpaIfConfigOutEnable = _H3cIpaIfConfigOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 3),
    _H3cIpaIfConfigOutEnable_Type()
)
h3cIpaIfConfigOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaIfConfigOutEnable.setStatus("current")


class _H3cIpaIfConfigFWEnable_Type(Integer32):
    """Custom type h3cIpaIfConfigFWEnable based on Integer32"""
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
        *(("bidirection", 4),
          ("inbound", 2),
          ("nodirection", 1),
          ("outbound", 3))
    )


_H3cIpaIfConfigFWEnable_Type.__name__ = "Integer32"
_H3cIpaIfConfigFWEnable_Object = MibTableColumn
h3cIpaIfConfigFWEnable = _H3cIpaIfConfigFWEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 2, 1, 4),
    _H3cIpaIfConfigFWEnable_Type()
)
h3cIpaIfConfigFWEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cIpaIfConfigFWEnable.setStatus("current")
_H3cIpaAccountListTable_Object = MibTable
h3cIpaAccountListTable = _H3cIpaAccountListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3)
)
if mibBuilder.loadTexts:
    h3cIpaAccountListTable.setStatus("current")
_H3cIpaAccountListEntry_Object = MibTableRow
h3cIpaAccountListEntry = _H3cIpaAccountListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1)
)
h3cIpaAccountListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaAccountListIndex"),
)
if mibBuilder.loadTexts:
    h3cIpaAccountListEntry.setStatus("current")


class _H3cIpaAccountListIndex_Type(Integer32):
    """Custom type h3cIpaAccountListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cIpaAccountListIndex_Type.__name__ = "Integer32"
_H3cIpaAccountListIndex_Object = MibTableColumn
h3cIpaAccountListIndex = _H3cIpaAccountListIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 1),
    _H3cIpaAccountListIndex_Type()
)
h3cIpaAccountListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaAccountListIndex.setStatus("current")
_H3cIpaAccountListIpAddr_Type = IpAddress
_H3cIpaAccountListIpAddr_Object = MibTableColumn
h3cIpaAccountListIpAddr = _H3cIpaAccountListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 2),
    _H3cIpaAccountListIpAddr_Type()
)
h3cIpaAccountListIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpaAccountListIpAddr.setStatus("current")
_H3cIpaAccountListIpMask_Type = IpAddress
_H3cIpaAccountListIpMask_Object = MibTableColumn
h3cIpaAccountListIpMask = _H3cIpaAccountListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 3),
    _H3cIpaAccountListIpMask_Type()
)
h3cIpaAccountListIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpaAccountListIpMask.setStatus("current")
_H3cIpaAccountListRowStatus_Type = RowStatus
_H3cIpaAccountListRowStatus_Object = MibTableColumn
h3cIpaAccountListRowStatus = _H3cIpaAccountListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 3, 1, 4),
    _H3cIpaAccountListRowStatus_Type()
)
h3cIpaAccountListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cIpaAccountListRowStatus.setStatus("current")
_H3cIpaIntListTable_Object = MibTable
h3cIpaIntListTable = _H3cIpaIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4)
)
if mibBuilder.loadTexts:
    h3cIpaIntListTable.setStatus("current")
_H3cIpaIntListEntry_Object = MibTableRow
h3cIpaIntListEntry = _H3cIpaIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1)
)
h3cIpaIntListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListIpSrc"),
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListIpDst"),
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaIntListProtocol"),
)
if mibBuilder.loadTexts:
    h3cIpaIntListEntry.setStatus("current")
_H3cIpaIntListIpSrc_Type = IpAddress
_H3cIpaIntListIpSrc_Object = MibTableColumn
h3cIpaIntListIpSrc = _H3cIpaIntListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 1),
    _H3cIpaIntListIpSrc_Type()
)
h3cIpaIntListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaIntListIpSrc.setStatus("current")
_H3cIpaIntListIpDst_Type = IpAddress
_H3cIpaIntListIpDst_Object = MibTableColumn
h3cIpaIntListIpDst = _H3cIpaIntListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 2),
    _H3cIpaIntListIpDst_Type()
)
h3cIpaIntListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaIntListIpDst.setStatus("current")


class _H3cIpaIntListProtocol_Type(Integer32):
    """Custom type h3cIpaIntListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIpaIntListProtocol_Type.__name__ = "Integer32"
_H3cIpaIntListProtocol_Object = MibTableColumn
h3cIpaIntListProtocol = _H3cIpaIntListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 3),
    _H3cIpaIntListProtocol_Type()
)
h3cIpaIntListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaIntListProtocol.setStatus("current")
_H3cIpaIntListInPackets_Type = Counter32
_H3cIpaIntListInPackets_Object = MibTableColumn
h3cIpaIntListInPackets = _H3cIpaIntListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 4),
    _H3cIpaIntListInPackets_Type()
)
h3cIpaIntListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaIntListInPackets.setStatus("current")
_H3cIpaIntListInBytes_Type = Counter64
_H3cIpaIntListInBytes_Object = MibTableColumn
h3cIpaIntListInBytes = _H3cIpaIntListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 5),
    _H3cIpaIntListInBytes_Type()
)
h3cIpaIntListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaIntListInBytes.setStatus("current")
_H3cIpaIntListOutPackets_Type = Counter32
_H3cIpaIntListOutPackets_Object = MibTableColumn
h3cIpaIntListOutPackets = _H3cIpaIntListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 6),
    _H3cIpaIntListOutPackets_Type()
)
h3cIpaIntListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaIntListOutPackets.setStatus("current")
_H3cIpaIntListOutBytes_Type = Counter64
_H3cIpaIntListOutBytes_Object = MibTableColumn
h3cIpaIntListOutBytes = _H3cIpaIntListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 4, 1, 7),
    _H3cIpaIntListOutBytes_Type()
)
h3cIpaIntListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaIntListOutBytes.setStatus("current")
_H3cIpaExtListTable_Object = MibTable
h3cIpaExtListTable = _H3cIpaExtListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5)
)
if mibBuilder.loadTexts:
    h3cIpaExtListTable.setStatus("current")
_H3cIpaExtListEntry_Object = MibTableRow
h3cIpaExtListEntry = _H3cIpaExtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1)
)
h3cIpaExtListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListIpSrc"),
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListIpDst"),
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaExtListProtocol"),
)
if mibBuilder.loadTexts:
    h3cIpaExtListEntry.setStatus("current")
_H3cIpaExtListIpSrc_Type = IpAddress
_H3cIpaExtListIpSrc_Object = MibTableColumn
h3cIpaExtListIpSrc = _H3cIpaExtListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 1),
    _H3cIpaExtListIpSrc_Type()
)
h3cIpaExtListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaExtListIpSrc.setStatus("current")
_H3cIpaExtListIpDst_Type = IpAddress
_H3cIpaExtListIpDst_Object = MibTableColumn
h3cIpaExtListIpDst = _H3cIpaExtListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 2),
    _H3cIpaExtListIpDst_Type()
)
h3cIpaExtListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaExtListIpDst.setStatus("current")


class _H3cIpaExtListProtocol_Type(Integer32):
    """Custom type h3cIpaExtListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_H3cIpaExtListProtocol_Type.__name__ = "Integer32"
_H3cIpaExtListProtocol_Object = MibTableColumn
h3cIpaExtListProtocol = _H3cIpaExtListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 3),
    _H3cIpaExtListProtocol_Type()
)
h3cIpaExtListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaExtListProtocol.setStatus("current")
_H3cIpaExtListInPackets_Type = Counter32
_H3cIpaExtListInPackets_Object = MibTableColumn
h3cIpaExtListInPackets = _H3cIpaExtListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 4),
    _H3cIpaExtListInPackets_Type()
)
h3cIpaExtListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaExtListInPackets.setStatus("current")
_H3cIpaExtListInBytes_Type = Counter64
_H3cIpaExtListInBytes_Object = MibTableColumn
h3cIpaExtListInBytes = _H3cIpaExtListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 5),
    _H3cIpaExtListInBytes_Type()
)
h3cIpaExtListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaExtListInBytes.setStatus("current")
_H3cIpaExtListOutPackets_Type = Counter32
_H3cIpaExtListOutPackets_Object = MibTableColumn
h3cIpaExtListOutPackets = _H3cIpaExtListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 6),
    _H3cIpaExtListOutPackets_Type()
)
h3cIpaExtListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaExtListOutPackets.setStatus("current")
_H3cIpaExtListOutBytes_Type = Counter64
_H3cIpaExtListOutBytes_Object = MibTableColumn
h3cIpaExtListOutBytes = _H3cIpaExtListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 5, 1, 7),
    _H3cIpaExtListOutBytes_Type()
)
h3cIpaExtListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaExtListOutBytes.setStatus("current")
_H3cIpaFWListTable_Object = MibTable
h3cIpaFWListTable = _H3cIpaFWListTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6)
)
if mibBuilder.loadTexts:
    h3cIpaFWListTable.setStatus("current")
_H3cIpaFWListEntry_Object = MibTableRow
h3cIpaFWListEntry = _H3cIpaFWListEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1)
)
h3cIpaFWListEntry.setIndexNames(
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaFWListIpSrc"),
    (0, "A3COM-HUAWEI-IPA-MIB", "h3cIpaFWListIpDst"),
)
if mibBuilder.loadTexts:
    h3cIpaFWListEntry.setStatus("current")
_H3cIpaFWListIpSrc_Type = IpAddress
_H3cIpaFWListIpSrc_Object = MibTableColumn
h3cIpaFWListIpSrc = _H3cIpaFWListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 1),
    _H3cIpaFWListIpSrc_Type()
)
h3cIpaFWListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaFWListIpSrc.setStatus("current")
_H3cIpaFWListIpDst_Type = IpAddress
_H3cIpaFWListIpDst_Object = MibTableColumn
h3cIpaFWListIpDst = _H3cIpaFWListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 2),
    _H3cIpaFWListIpDst_Type()
)
h3cIpaFWListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cIpaFWListIpDst.setStatus("current")
_H3cIpaFWListInPackets_Type = Counter32
_H3cIpaFWListInPackets_Object = MibTableColumn
h3cIpaFWListInPackets = _H3cIpaFWListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 3),
    _H3cIpaFWListInPackets_Type()
)
h3cIpaFWListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaFWListInPackets.setStatus("current")
_H3cIpaFWListInBytes_Type = Counter64
_H3cIpaFWListInBytes_Object = MibTableColumn
h3cIpaFWListInBytes = _H3cIpaFWListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 4),
    _H3cIpaFWListInBytes_Type()
)
h3cIpaFWListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaFWListInBytes.setStatus("current")
_H3cIpaFWListOutPackets_Type = Counter32
_H3cIpaFWListOutPackets_Object = MibTableColumn
h3cIpaFWListOutPackets = _H3cIpaFWListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 5),
    _H3cIpaFWListOutPackets_Type()
)
h3cIpaFWListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaFWListOutPackets.setStatus("current")
_H3cIpaFWListOutBytes_Type = Counter64
_H3cIpaFWListOutBytes_Object = MibTableColumn
h3cIpaFWListOutBytes = _H3cIpaFWListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 25, 6, 1, 6),
    _H3cIpaFWListOutBytes_Type()
)
h3cIpaFWListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cIpaFWListOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-IPA-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "h3cIpa": h3cIpa,
       "h3cIpaGlobalStats": h3cIpaGlobalStats,
       "h3cIpaGlobalEnable": h3cIpaGlobalEnable,
       "h3cIpaTimeOutSeconds": h3cIpaTimeOutSeconds,
       "h3cIpaIntListMaxItemNum": h3cIpaIntListMaxItemNum,
       "h3cIpaExtListMaxItemNum": h3cIpaExtListMaxItemNum,
       "h3cIpaFWListMaxItemNum": h3cIpaFWListMaxItemNum,
       "h3cIpaAccountListMaxItemNum": h3cIpaAccountListMaxItemNum,
       "h3cIpaAccountListNextIndex": h3cIpaAccountListNextIndex,
       "h3cIpaListCleaningFlag": h3cIpaListCleaningFlag,
       "h3cIpaIfConfigTable": h3cIpaIfConfigTable,
       "h3cIpaIfConfigEntry": h3cIpaIfConfigEntry,
       "h3cIpaIfConfigIfIndex": h3cIpaIfConfigIfIndex,
       "h3cIpaIfConfigInEnable": h3cIpaIfConfigInEnable,
       "h3cIpaIfConfigOutEnable": h3cIpaIfConfigOutEnable,
       "h3cIpaIfConfigFWEnable": h3cIpaIfConfigFWEnable,
       "h3cIpaAccountListTable": h3cIpaAccountListTable,
       "h3cIpaAccountListEntry": h3cIpaAccountListEntry,
       "h3cIpaAccountListIndex": h3cIpaAccountListIndex,
       "h3cIpaAccountListIpAddr": h3cIpaAccountListIpAddr,
       "h3cIpaAccountListIpMask": h3cIpaAccountListIpMask,
       "h3cIpaAccountListRowStatus": h3cIpaAccountListRowStatus,
       "h3cIpaIntListTable": h3cIpaIntListTable,
       "h3cIpaIntListEntry": h3cIpaIntListEntry,
       "h3cIpaIntListIpSrc": h3cIpaIntListIpSrc,
       "h3cIpaIntListIpDst": h3cIpaIntListIpDst,
       "h3cIpaIntListProtocol": h3cIpaIntListProtocol,
       "h3cIpaIntListInPackets": h3cIpaIntListInPackets,
       "h3cIpaIntListInBytes": h3cIpaIntListInBytes,
       "h3cIpaIntListOutPackets": h3cIpaIntListOutPackets,
       "h3cIpaIntListOutBytes": h3cIpaIntListOutBytes,
       "h3cIpaExtListTable": h3cIpaExtListTable,
       "h3cIpaExtListEntry": h3cIpaExtListEntry,
       "h3cIpaExtListIpSrc": h3cIpaExtListIpSrc,
       "h3cIpaExtListIpDst": h3cIpaExtListIpDst,
       "h3cIpaExtListProtocol": h3cIpaExtListProtocol,
       "h3cIpaExtListInPackets": h3cIpaExtListInPackets,
       "h3cIpaExtListInBytes": h3cIpaExtListInBytes,
       "h3cIpaExtListOutPackets": h3cIpaExtListOutPackets,
       "h3cIpaExtListOutBytes": h3cIpaExtListOutBytes,
       "h3cIpaFWListTable": h3cIpaFWListTable,
       "h3cIpaFWListEntry": h3cIpaFWListEntry,
       "h3cIpaFWListIpSrc": h3cIpaFWListIpSrc,
       "h3cIpaFWListIpDst": h3cIpaFWListIpDst,
       "h3cIpaFWListInPackets": h3cIpaFWListInPackets,
       "h3cIpaFWListInBytes": h3cIpaFWListInBytes,
       "h3cIpaFWListOutPackets": h3cIpaFWListOutPackets,
       "h3cIpaFWListOutBytes": h3cIpaFWListOutBytes}
)
