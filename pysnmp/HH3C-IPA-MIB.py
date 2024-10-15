# SNMP MIB module (HH3C-IPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IPA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:36 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25)
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

_Hh3cIpaGlobalStats_ObjectIdentity = ObjectIdentity
hh3cIpaGlobalStats = _Hh3cIpaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1)
)


class _Hh3cIpaGlobalEnable_Type(Integer32):
    """Custom type hh3cIpaGlobalEnable based on Integer32"""
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


_Hh3cIpaGlobalEnable_Type.__name__ = "Integer32"
_Hh3cIpaGlobalEnable_Object = MibScalar
hh3cIpaGlobalEnable = _Hh3cIpaGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 1),
    _Hh3cIpaGlobalEnable_Type()
)
hh3cIpaGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaGlobalEnable.setStatus("current")


class _Hh3cIpaTimeOutSeconds_Type(Integer32):
    """Custom type hh3cIpaTimeOutSeconds based on Integer32"""
    defaultValue = 43200


_Hh3cIpaTimeOutSeconds_Object = MibScalar
hh3cIpaTimeOutSeconds = _Hh3cIpaTimeOutSeconds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 2),
    _Hh3cIpaTimeOutSeconds_Type()
)
hh3cIpaTimeOutSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaTimeOutSeconds.setStatus("current")


class _Hh3cIpaIntListMaxItemNum_Type(Integer32):
    """Custom type hh3cIpaIntListMaxItemNum based on Integer32"""
    defaultValue = 512


_Hh3cIpaIntListMaxItemNum_Object = MibScalar
hh3cIpaIntListMaxItemNum = _Hh3cIpaIntListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 3),
    _Hh3cIpaIntListMaxItemNum_Type()
)
hh3cIpaIntListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaIntListMaxItemNum.setStatus("current")


class _Hh3cIpaExtListMaxItemNum_Type(Integer32):
    """Custom type hh3cIpaExtListMaxItemNum based on Integer32"""
    defaultValue = 0


_Hh3cIpaExtListMaxItemNum_Object = MibScalar
hh3cIpaExtListMaxItemNum = _Hh3cIpaExtListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 4),
    _Hh3cIpaExtListMaxItemNum_Type()
)
hh3cIpaExtListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaExtListMaxItemNum.setStatus("current")
_Hh3cIpaFWListMaxItemNum_Type = Integer32
_Hh3cIpaFWListMaxItemNum_Object = MibScalar
hh3cIpaFWListMaxItemNum = _Hh3cIpaFWListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 5),
    _Hh3cIpaFWListMaxItemNum_Type()
)
hh3cIpaFWListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaFWListMaxItemNum.setStatus("current")
_Hh3cIpaAccountListMaxItemNum_Type = Integer32
_Hh3cIpaAccountListMaxItemNum_Object = MibScalar
hh3cIpaAccountListMaxItemNum = _Hh3cIpaAccountListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 6),
    _Hh3cIpaAccountListMaxItemNum_Type()
)
hh3cIpaAccountListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaAccountListMaxItemNum.setStatus("current")
_Hh3cIpaAccountListNextIndex_Type = Integer32
_Hh3cIpaAccountListNextIndex_Object = MibScalar
hh3cIpaAccountListNextIndex = _Hh3cIpaAccountListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 7),
    _Hh3cIpaAccountListNextIndex_Type()
)
hh3cIpaAccountListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaAccountListNextIndex.setStatus("current")


class _Hh3cIpaListCleaningFlag_Type(Integer32):
    """Custom type hh3cIpaListCleaningFlag based on Integer32"""
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


_Hh3cIpaListCleaningFlag_Type.__name__ = "Integer32"
_Hh3cIpaListCleaningFlag_Object = MibScalar
hh3cIpaListCleaningFlag = _Hh3cIpaListCleaningFlag_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 1, 8),
    _Hh3cIpaListCleaningFlag_Type()
)
hh3cIpaListCleaningFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaListCleaningFlag.setStatus("current")
_Hh3cIpaIfConfigTable_Object = MibTable
hh3cIpaIfConfigTable = _Hh3cIpaIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2)
)
if mibBuilder.loadTexts:
    hh3cIpaIfConfigTable.setStatus("current")
_Hh3cIpaIfConfigEntry_Object = MibTableRow
hh3cIpaIfConfigEntry = _Hh3cIpaIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1)
)
hh3cIpaIfConfigEntry.setIndexNames(
    (0, "HH3C-IPA-MIB", "hh3cIpaIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpaIfConfigEntry.setStatus("current")
_Hh3cIpaIfConfigIfIndex_Type = InterfaceIndex
_Hh3cIpaIfConfigIfIndex_Object = MibTableColumn
hh3cIpaIfConfigIfIndex = _Hh3cIpaIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 1),
    _Hh3cIpaIfConfigIfIndex_Type()
)
hh3cIpaIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaIfConfigIfIndex.setStatus("current")


class _Hh3cIpaIfConfigInEnable_Type(Integer32):
    """Custom type hh3cIpaIfConfigInEnable based on Integer32"""
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


_Hh3cIpaIfConfigInEnable_Type.__name__ = "Integer32"
_Hh3cIpaIfConfigInEnable_Object = MibTableColumn
hh3cIpaIfConfigInEnable = _Hh3cIpaIfConfigInEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 2),
    _Hh3cIpaIfConfigInEnable_Type()
)
hh3cIpaIfConfigInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaIfConfigInEnable.setStatus("current")


class _Hh3cIpaIfConfigOutEnable_Type(Integer32):
    """Custom type hh3cIpaIfConfigOutEnable based on Integer32"""
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


_Hh3cIpaIfConfigOutEnable_Type.__name__ = "Integer32"
_Hh3cIpaIfConfigOutEnable_Object = MibTableColumn
hh3cIpaIfConfigOutEnable = _Hh3cIpaIfConfigOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 3),
    _Hh3cIpaIfConfigOutEnable_Type()
)
hh3cIpaIfConfigOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaIfConfigOutEnable.setStatus("current")


class _Hh3cIpaIfConfigFWEnable_Type(Integer32):
    """Custom type hh3cIpaIfConfigFWEnable based on Integer32"""
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


_Hh3cIpaIfConfigFWEnable_Type.__name__ = "Integer32"
_Hh3cIpaIfConfigFWEnable_Object = MibTableColumn
hh3cIpaIfConfigFWEnable = _Hh3cIpaIfConfigFWEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 2, 1, 4),
    _Hh3cIpaIfConfigFWEnable_Type()
)
hh3cIpaIfConfigFWEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpaIfConfigFWEnable.setStatus("current")
_Hh3cIpaAccountListTable_Object = MibTable
hh3cIpaAccountListTable = _Hh3cIpaAccountListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3)
)
if mibBuilder.loadTexts:
    hh3cIpaAccountListTable.setStatus("current")
_Hh3cIpaAccountListEntry_Object = MibTableRow
hh3cIpaAccountListEntry = _Hh3cIpaAccountListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1)
)
hh3cIpaAccountListEntry.setIndexNames(
    (0, "HH3C-IPA-MIB", "hh3cIpaAccountListIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpaAccountListEntry.setStatus("current")


class _Hh3cIpaAccountListIndex_Type(Integer32):
    """Custom type hh3cIpaAccountListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpaAccountListIndex_Type.__name__ = "Integer32"
_Hh3cIpaAccountListIndex_Object = MibTableColumn
hh3cIpaAccountListIndex = _Hh3cIpaAccountListIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 1),
    _Hh3cIpaAccountListIndex_Type()
)
hh3cIpaAccountListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaAccountListIndex.setStatus("current")
_Hh3cIpaAccountListIpAddr_Type = IpAddress
_Hh3cIpaAccountListIpAddr_Object = MibTableColumn
hh3cIpaAccountListIpAddr = _Hh3cIpaAccountListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 2),
    _Hh3cIpaAccountListIpAddr_Type()
)
hh3cIpaAccountListIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpaAccountListIpAddr.setStatus("current")
_Hh3cIpaAccountListIpMask_Type = IpAddress
_Hh3cIpaAccountListIpMask_Object = MibTableColumn
hh3cIpaAccountListIpMask = _Hh3cIpaAccountListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 3),
    _Hh3cIpaAccountListIpMask_Type()
)
hh3cIpaAccountListIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpaAccountListIpMask.setStatus("current")
_Hh3cIpaAccountListRowStatus_Type = RowStatus
_Hh3cIpaAccountListRowStatus_Object = MibTableColumn
hh3cIpaAccountListRowStatus = _Hh3cIpaAccountListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 3, 1, 4),
    _Hh3cIpaAccountListRowStatus_Type()
)
hh3cIpaAccountListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpaAccountListRowStatus.setStatus("current")
_Hh3cIpaIntListTable_Object = MibTable
hh3cIpaIntListTable = _Hh3cIpaIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4)
)
if mibBuilder.loadTexts:
    hh3cIpaIntListTable.setStatus("current")
_Hh3cIpaIntListEntry_Object = MibTableRow
hh3cIpaIntListEntry = _Hh3cIpaIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1)
)
hh3cIpaIntListEntry.setIndexNames(
    (0, "HH3C-IPA-MIB", "hh3cIpaIntListIpSrc"),
    (0, "HH3C-IPA-MIB", "hh3cIpaIntListIpDst"),
    (0, "HH3C-IPA-MIB", "hh3cIpaIntListProtocol"),
)
if mibBuilder.loadTexts:
    hh3cIpaIntListEntry.setStatus("current")
_Hh3cIpaIntListIpSrc_Type = IpAddress
_Hh3cIpaIntListIpSrc_Object = MibTableColumn
hh3cIpaIntListIpSrc = _Hh3cIpaIntListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 1),
    _Hh3cIpaIntListIpSrc_Type()
)
hh3cIpaIntListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaIntListIpSrc.setStatus("current")
_Hh3cIpaIntListIpDst_Type = IpAddress
_Hh3cIpaIntListIpDst_Object = MibTableColumn
hh3cIpaIntListIpDst = _Hh3cIpaIntListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 2),
    _Hh3cIpaIntListIpDst_Type()
)
hh3cIpaIntListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaIntListIpDst.setStatus("current")


class _Hh3cIpaIntListProtocol_Type(Integer32):
    """Custom type hh3cIpaIntListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIpaIntListProtocol_Type.__name__ = "Integer32"
_Hh3cIpaIntListProtocol_Object = MibTableColumn
hh3cIpaIntListProtocol = _Hh3cIpaIntListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 3),
    _Hh3cIpaIntListProtocol_Type()
)
hh3cIpaIntListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaIntListProtocol.setStatus("current")
_Hh3cIpaIntListInPackets_Type = Counter32
_Hh3cIpaIntListInPackets_Object = MibTableColumn
hh3cIpaIntListInPackets = _Hh3cIpaIntListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 4),
    _Hh3cIpaIntListInPackets_Type()
)
hh3cIpaIntListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaIntListInPackets.setStatus("current")
_Hh3cIpaIntListInBytes_Type = Counter64
_Hh3cIpaIntListInBytes_Object = MibTableColumn
hh3cIpaIntListInBytes = _Hh3cIpaIntListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 5),
    _Hh3cIpaIntListInBytes_Type()
)
hh3cIpaIntListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaIntListInBytes.setStatus("current")
_Hh3cIpaIntListOutPackets_Type = Counter32
_Hh3cIpaIntListOutPackets_Object = MibTableColumn
hh3cIpaIntListOutPackets = _Hh3cIpaIntListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 6),
    _Hh3cIpaIntListOutPackets_Type()
)
hh3cIpaIntListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaIntListOutPackets.setStatus("current")
_Hh3cIpaIntListOutBytes_Type = Counter64
_Hh3cIpaIntListOutBytes_Object = MibTableColumn
hh3cIpaIntListOutBytes = _Hh3cIpaIntListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 4, 1, 7),
    _Hh3cIpaIntListOutBytes_Type()
)
hh3cIpaIntListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaIntListOutBytes.setStatus("current")
_Hh3cIpaExtListTable_Object = MibTable
hh3cIpaExtListTable = _Hh3cIpaExtListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5)
)
if mibBuilder.loadTexts:
    hh3cIpaExtListTable.setStatus("current")
_Hh3cIpaExtListEntry_Object = MibTableRow
hh3cIpaExtListEntry = _Hh3cIpaExtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1)
)
hh3cIpaExtListEntry.setIndexNames(
    (0, "HH3C-IPA-MIB", "hh3cIpaExtListIpSrc"),
    (0, "HH3C-IPA-MIB", "hh3cIpaExtListIpDst"),
    (0, "HH3C-IPA-MIB", "hh3cIpaExtListProtocol"),
)
if mibBuilder.loadTexts:
    hh3cIpaExtListEntry.setStatus("current")
_Hh3cIpaExtListIpSrc_Type = IpAddress
_Hh3cIpaExtListIpSrc_Object = MibTableColumn
hh3cIpaExtListIpSrc = _Hh3cIpaExtListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 1),
    _Hh3cIpaExtListIpSrc_Type()
)
hh3cIpaExtListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaExtListIpSrc.setStatus("current")
_Hh3cIpaExtListIpDst_Type = IpAddress
_Hh3cIpaExtListIpDst_Object = MibTableColumn
hh3cIpaExtListIpDst = _Hh3cIpaExtListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 2),
    _Hh3cIpaExtListIpDst_Type()
)
hh3cIpaExtListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaExtListIpDst.setStatus("current")


class _Hh3cIpaExtListProtocol_Type(Integer32):
    """Custom type hh3cIpaExtListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cIpaExtListProtocol_Type.__name__ = "Integer32"
_Hh3cIpaExtListProtocol_Object = MibTableColumn
hh3cIpaExtListProtocol = _Hh3cIpaExtListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 3),
    _Hh3cIpaExtListProtocol_Type()
)
hh3cIpaExtListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaExtListProtocol.setStatus("current")
_Hh3cIpaExtListInPackets_Type = Counter32
_Hh3cIpaExtListInPackets_Object = MibTableColumn
hh3cIpaExtListInPackets = _Hh3cIpaExtListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 4),
    _Hh3cIpaExtListInPackets_Type()
)
hh3cIpaExtListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaExtListInPackets.setStatus("current")
_Hh3cIpaExtListInBytes_Type = Counter64
_Hh3cIpaExtListInBytes_Object = MibTableColumn
hh3cIpaExtListInBytes = _Hh3cIpaExtListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 5),
    _Hh3cIpaExtListInBytes_Type()
)
hh3cIpaExtListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaExtListInBytes.setStatus("current")
_Hh3cIpaExtListOutPackets_Type = Counter32
_Hh3cIpaExtListOutPackets_Object = MibTableColumn
hh3cIpaExtListOutPackets = _Hh3cIpaExtListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 6),
    _Hh3cIpaExtListOutPackets_Type()
)
hh3cIpaExtListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaExtListOutPackets.setStatus("current")
_Hh3cIpaExtListOutBytes_Type = Counter64
_Hh3cIpaExtListOutBytes_Object = MibTableColumn
hh3cIpaExtListOutBytes = _Hh3cIpaExtListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 5, 1, 7),
    _Hh3cIpaExtListOutBytes_Type()
)
hh3cIpaExtListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaExtListOutBytes.setStatus("current")
_Hh3cIpaFWListTable_Object = MibTable
hh3cIpaFWListTable = _Hh3cIpaFWListTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6)
)
if mibBuilder.loadTexts:
    hh3cIpaFWListTable.setStatus("current")
_Hh3cIpaFWListEntry_Object = MibTableRow
hh3cIpaFWListEntry = _Hh3cIpaFWListEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1)
)
hh3cIpaFWListEntry.setIndexNames(
    (0, "HH3C-IPA-MIB", "hh3cIpaFWListIpSrc"),
    (0, "HH3C-IPA-MIB", "hh3cIpaFWListIpDst"),
)
if mibBuilder.loadTexts:
    hh3cIpaFWListEntry.setStatus("current")
_Hh3cIpaFWListIpSrc_Type = IpAddress
_Hh3cIpaFWListIpSrc_Object = MibTableColumn
hh3cIpaFWListIpSrc = _Hh3cIpaFWListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 1),
    _Hh3cIpaFWListIpSrc_Type()
)
hh3cIpaFWListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaFWListIpSrc.setStatus("current")
_Hh3cIpaFWListIpDst_Type = IpAddress
_Hh3cIpaFWListIpDst_Object = MibTableColumn
hh3cIpaFWListIpDst = _Hh3cIpaFWListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 2),
    _Hh3cIpaFWListIpDst_Type()
)
hh3cIpaFWListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpaFWListIpDst.setStatus("current")
_Hh3cIpaFWListInPackets_Type = Counter32
_Hh3cIpaFWListInPackets_Object = MibTableColumn
hh3cIpaFWListInPackets = _Hh3cIpaFWListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 3),
    _Hh3cIpaFWListInPackets_Type()
)
hh3cIpaFWListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaFWListInPackets.setStatus("current")
_Hh3cIpaFWListInBytes_Type = Counter64
_Hh3cIpaFWListInBytes_Object = MibTableColumn
hh3cIpaFWListInBytes = _Hh3cIpaFWListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 4),
    _Hh3cIpaFWListInBytes_Type()
)
hh3cIpaFWListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaFWListInBytes.setStatus("current")
_Hh3cIpaFWListOutPackets_Type = Counter32
_Hh3cIpaFWListOutPackets_Object = MibTableColumn
hh3cIpaFWListOutPackets = _Hh3cIpaFWListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 5),
    _Hh3cIpaFWListOutPackets_Type()
)
hh3cIpaFWListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaFWListOutPackets.setStatus("current")
_Hh3cIpaFWListOutBytes_Type = Counter64
_Hh3cIpaFWListOutBytes_Object = MibTableColumn
hh3cIpaFWListOutBytes = _Hh3cIpaFWListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 25, 6, 1, 6),
    _Hh3cIpaFWListOutBytes_Type()
)
hh3cIpaFWListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpaFWListOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IPA-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "hh3cIpa": hh3cIpa,
       "hh3cIpaGlobalStats": hh3cIpaGlobalStats,
       "hh3cIpaGlobalEnable": hh3cIpaGlobalEnable,
       "hh3cIpaTimeOutSeconds": hh3cIpaTimeOutSeconds,
       "hh3cIpaIntListMaxItemNum": hh3cIpaIntListMaxItemNum,
       "hh3cIpaExtListMaxItemNum": hh3cIpaExtListMaxItemNum,
       "hh3cIpaFWListMaxItemNum": hh3cIpaFWListMaxItemNum,
       "hh3cIpaAccountListMaxItemNum": hh3cIpaAccountListMaxItemNum,
       "hh3cIpaAccountListNextIndex": hh3cIpaAccountListNextIndex,
       "hh3cIpaListCleaningFlag": hh3cIpaListCleaningFlag,
       "hh3cIpaIfConfigTable": hh3cIpaIfConfigTable,
       "hh3cIpaIfConfigEntry": hh3cIpaIfConfigEntry,
       "hh3cIpaIfConfigIfIndex": hh3cIpaIfConfigIfIndex,
       "hh3cIpaIfConfigInEnable": hh3cIpaIfConfigInEnable,
       "hh3cIpaIfConfigOutEnable": hh3cIpaIfConfigOutEnable,
       "hh3cIpaIfConfigFWEnable": hh3cIpaIfConfigFWEnable,
       "hh3cIpaAccountListTable": hh3cIpaAccountListTable,
       "hh3cIpaAccountListEntry": hh3cIpaAccountListEntry,
       "hh3cIpaAccountListIndex": hh3cIpaAccountListIndex,
       "hh3cIpaAccountListIpAddr": hh3cIpaAccountListIpAddr,
       "hh3cIpaAccountListIpMask": hh3cIpaAccountListIpMask,
       "hh3cIpaAccountListRowStatus": hh3cIpaAccountListRowStatus,
       "hh3cIpaIntListTable": hh3cIpaIntListTable,
       "hh3cIpaIntListEntry": hh3cIpaIntListEntry,
       "hh3cIpaIntListIpSrc": hh3cIpaIntListIpSrc,
       "hh3cIpaIntListIpDst": hh3cIpaIntListIpDst,
       "hh3cIpaIntListProtocol": hh3cIpaIntListProtocol,
       "hh3cIpaIntListInPackets": hh3cIpaIntListInPackets,
       "hh3cIpaIntListInBytes": hh3cIpaIntListInBytes,
       "hh3cIpaIntListOutPackets": hh3cIpaIntListOutPackets,
       "hh3cIpaIntListOutBytes": hh3cIpaIntListOutBytes,
       "hh3cIpaExtListTable": hh3cIpaExtListTable,
       "hh3cIpaExtListEntry": hh3cIpaExtListEntry,
       "hh3cIpaExtListIpSrc": hh3cIpaExtListIpSrc,
       "hh3cIpaExtListIpDst": hh3cIpaExtListIpDst,
       "hh3cIpaExtListProtocol": hh3cIpaExtListProtocol,
       "hh3cIpaExtListInPackets": hh3cIpaExtListInPackets,
       "hh3cIpaExtListInBytes": hh3cIpaExtListInBytes,
       "hh3cIpaExtListOutPackets": hh3cIpaExtListOutPackets,
       "hh3cIpaExtListOutBytes": hh3cIpaExtListOutBytes,
       "hh3cIpaFWListTable": hh3cIpaFWListTable,
       "hh3cIpaFWListEntry": hh3cIpaFWListEntry,
       "hh3cIpaFWListIpSrc": hh3cIpaFWListIpSrc,
       "hh3cIpaFWListIpDst": hh3cIpaFWListIpDst,
       "hh3cIpaFWListInPackets": hh3cIpaFWListInPackets,
       "hh3cIpaFWListInBytes": hh3cIpaFWListInBytes,
       "hh3cIpaFWListOutPackets": hh3cIpaFWListOutPackets,
       "hh3cIpaFWListOutBytes": hh3cIpaFWListOutBytes}
)
