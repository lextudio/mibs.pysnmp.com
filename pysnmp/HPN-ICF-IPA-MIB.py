# SNMP MIB module (HPN-ICF-IPA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IPA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:36 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfIpa = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25)
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

_HpnicfIpaGlobalStats_ObjectIdentity = ObjectIdentity
hpnicfIpaGlobalStats = _HpnicfIpaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1)
)


class _HpnicfIpaGlobalEnable_Type(Integer32):
    """Custom type hpnicfIpaGlobalEnable based on Integer32"""
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


_HpnicfIpaGlobalEnable_Type.__name__ = "Integer32"
_HpnicfIpaGlobalEnable_Object = MibScalar
hpnicfIpaGlobalEnable = _HpnicfIpaGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 1),
    _HpnicfIpaGlobalEnable_Type()
)
hpnicfIpaGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaGlobalEnable.setStatus("current")


class _HpnicfIpaTimeOutSeconds_Type(Integer32):
    """Custom type hpnicfIpaTimeOutSeconds based on Integer32"""
    defaultValue = 43200


_HpnicfIpaTimeOutSeconds_Object = MibScalar
hpnicfIpaTimeOutSeconds = _HpnicfIpaTimeOutSeconds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 2),
    _HpnicfIpaTimeOutSeconds_Type()
)
hpnicfIpaTimeOutSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaTimeOutSeconds.setStatus("current")


class _HpnicfIpaIntListMaxItemNum_Type(Integer32):
    """Custom type hpnicfIpaIntListMaxItemNum based on Integer32"""
    defaultValue = 512


_HpnicfIpaIntListMaxItemNum_Object = MibScalar
hpnicfIpaIntListMaxItemNum = _HpnicfIpaIntListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 3),
    _HpnicfIpaIntListMaxItemNum_Type()
)
hpnicfIpaIntListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaIntListMaxItemNum.setStatus("current")


class _HpnicfIpaExtListMaxItemNum_Type(Integer32):
    """Custom type hpnicfIpaExtListMaxItemNum based on Integer32"""
    defaultValue = 0


_HpnicfIpaExtListMaxItemNum_Object = MibScalar
hpnicfIpaExtListMaxItemNum = _HpnicfIpaExtListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 4),
    _HpnicfIpaExtListMaxItemNum_Type()
)
hpnicfIpaExtListMaxItemNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaExtListMaxItemNum.setStatus("current")
_HpnicfIpaFWListMaxItemNum_Type = Integer32
_HpnicfIpaFWListMaxItemNum_Object = MibScalar
hpnicfIpaFWListMaxItemNum = _HpnicfIpaFWListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 5),
    _HpnicfIpaFWListMaxItemNum_Type()
)
hpnicfIpaFWListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaFWListMaxItemNum.setStatus("current")
_HpnicfIpaAccountListMaxItemNum_Type = Integer32
_HpnicfIpaAccountListMaxItemNum_Object = MibScalar
hpnicfIpaAccountListMaxItemNum = _HpnicfIpaAccountListMaxItemNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 6),
    _HpnicfIpaAccountListMaxItemNum_Type()
)
hpnicfIpaAccountListMaxItemNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListMaxItemNum.setStatus("current")
_HpnicfIpaAccountListNextIndex_Type = Integer32
_HpnicfIpaAccountListNextIndex_Object = MibScalar
hpnicfIpaAccountListNextIndex = _HpnicfIpaAccountListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 7),
    _HpnicfIpaAccountListNextIndex_Type()
)
hpnicfIpaAccountListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListNextIndex.setStatus("current")


class _HpnicfIpaListCleaningFlag_Type(Integer32):
    """Custom type hpnicfIpaListCleaningFlag based on Integer32"""
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


_HpnicfIpaListCleaningFlag_Type.__name__ = "Integer32"
_HpnicfIpaListCleaningFlag_Object = MibScalar
hpnicfIpaListCleaningFlag = _HpnicfIpaListCleaningFlag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 1, 8),
    _HpnicfIpaListCleaningFlag_Type()
)
hpnicfIpaListCleaningFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaListCleaningFlag.setStatus("current")
_HpnicfIpaIfConfigTable_Object = MibTable
hpnicfIpaIfConfigTable = _HpnicfIpaIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2)
)
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigTable.setStatus("current")
_HpnicfIpaIfConfigEntry_Object = MibTableRow
hpnicfIpaIfConfigEntry = _HpnicfIpaIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1)
)
hpnicfIpaIfConfigEntry.setIndexNames(
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigEntry.setStatus("current")
_HpnicfIpaIfConfigIfIndex_Type = InterfaceIndex
_HpnicfIpaIfConfigIfIndex_Object = MibTableColumn
hpnicfIpaIfConfigIfIndex = _HpnicfIpaIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 1),
    _HpnicfIpaIfConfigIfIndex_Type()
)
hpnicfIpaIfConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigIfIndex.setStatus("current")


class _HpnicfIpaIfConfigInEnable_Type(Integer32):
    """Custom type hpnicfIpaIfConfigInEnable based on Integer32"""
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


_HpnicfIpaIfConfigInEnable_Type.__name__ = "Integer32"
_HpnicfIpaIfConfigInEnable_Object = MibTableColumn
hpnicfIpaIfConfigInEnable = _HpnicfIpaIfConfigInEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 2),
    _HpnicfIpaIfConfigInEnable_Type()
)
hpnicfIpaIfConfigInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigInEnable.setStatus("current")


class _HpnicfIpaIfConfigOutEnable_Type(Integer32):
    """Custom type hpnicfIpaIfConfigOutEnable based on Integer32"""
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


_HpnicfIpaIfConfigOutEnable_Type.__name__ = "Integer32"
_HpnicfIpaIfConfigOutEnable_Object = MibTableColumn
hpnicfIpaIfConfigOutEnable = _HpnicfIpaIfConfigOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 3),
    _HpnicfIpaIfConfigOutEnable_Type()
)
hpnicfIpaIfConfigOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigOutEnable.setStatus("current")


class _HpnicfIpaIfConfigFWEnable_Type(Integer32):
    """Custom type hpnicfIpaIfConfigFWEnable based on Integer32"""
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


_HpnicfIpaIfConfigFWEnable_Type.__name__ = "Integer32"
_HpnicfIpaIfConfigFWEnable_Object = MibTableColumn
hpnicfIpaIfConfigFWEnable = _HpnicfIpaIfConfigFWEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 2, 1, 4),
    _HpnicfIpaIfConfigFWEnable_Type()
)
hpnicfIpaIfConfigFWEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpaIfConfigFWEnable.setStatus("current")
_HpnicfIpaAccountListTable_Object = MibTable
hpnicfIpaAccountListTable = _HpnicfIpaAccountListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3)
)
if mibBuilder.loadTexts:
    hpnicfIpaAccountListTable.setStatus("current")
_HpnicfIpaAccountListEntry_Object = MibTableRow
hpnicfIpaAccountListEntry = _HpnicfIpaAccountListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1)
)
hpnicfIpaAccountListEntry.setIndexNames(
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaAccountListIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpaAccountListEntry.setStatus("current")


class _HpnicfIpaAccountListIndex_Type(Integer32):
    """Custom type hpnicfIpaAccountListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpaAccountListIndex_Type.__name__ = "Integer32"
_HpnicfIpaAccountListIndex_Object = MibTableColumn
hpnicfIpaAccountListIndex = _HpnicfIpaAccountListIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 1),
    _HpnicfIpaAccountListIndex_Type()
)
hpnicfIpaAccountListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListIndex.setStatus("current")
_HpnicfIpaAccountListIpAddr_Type = IpAddress
_HpnicfIpaAccountListIpAddr_Object = MibTableColumn
hpnicfIpaAccountListIpAddr = _HpnicfIpaAccountListIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 2),
    _HpnicfIpaAccountListIpAddr_Type()
)
hpnicfIpaAccountListIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListIpAddr.setStatus("current")
_HpnicfIpaAccountListIpMask_Type = IpAddress
_HpnicfIpaAccountListIpMask_Object = MibTableColumn
hpnicfIpaAccountListIpMask = _HpnicfIpaAccountListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 3),
    _HpnicfIpaAccountListIpMask_Type()
)
hpnicfIpaAccountListIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListIpMask.setStatus("current")
_HpnicfIpaAccountListRowStatus_Type = RowStatus
_HpnicfIpaAccountListRowStatus_Object = MibTableColumn
hpnicfIpaAccountListRowStatus = _HpnicfIpaAccountListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 3, 1, 4),
    _HpnicfIpaAccountListRowStatus_Type()
)
hpnicfIpaAccountListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpaAccountListRowStatus.setStatus("current")
_HpnicfIpaIntListTable_Object = MibTable
hpnicfIpaIntListTable = _HpnicfIpaIntListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4)
)
if mibBuilder.loadTexts:
    hpnicfIpaIntListTable.setStatus("current")
_HpnicfIpaIntListEntry_Object = MibTableRow
hpnicfIpaIntListEntry = _HpnicfIpaIntListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1)
)
hpnicfIpaIntListEntry.setIndexNames(
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListIpSrc"),
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListIpDst"),
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaIntListProtocol"),
)
if mibBuilder.loadTexts:
    hpnicfIpaIntListEntry.setStatus("current")
_HpnicfIpaIntListIpSrc_Type = IpAddress
_HpnicfIpaIntListIpSrc_Object = MibTableColumn
hpnicfIpaIntListIpSrc = _HpnicfIpaIntListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 1),
    _HpnicfIpaIntListIpSrc_Type()
)
hpnicfIpaIntListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaIntListIpSrc.setStatus("current")
_HpnicfIpaIntListIpDst_Type = IpAddress
_HpnicfIpaIntListIpDst_Object = MibTableColumn
hpnicfIpaIntListIpDst = _HpnicfIpaIntListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 2),
    _HpnicfIpaIntListIpDst_Type()
)
hpnicfIpaIntListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaIntListIpDst.setStatus("current")


class _HpnicfIpaIntListProtocol_Type(Integer32):
    """Custom type hpnicfIpaIntListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIpaIntListProtocol_Type.__name__ = "Integer32"
_HpnicfIpaIntListProtocol_Object = MibTableColumn
hpnicfIpaIntListProtocol = _HpnicfIpaIntListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 3),
    _HpnicfIpaIntListProtocol_Type()
)
hpnicfIpaIntListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaIntListProtocol.setStatus("current")
_HpnicfIpaIntListInPackets_Type = Counter32
_HpnicfIpaIntListInPackets_Object = MibTableColumn
hpnicfIpaIntListInPackets = _HpnicfIpaIntListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 4),
    _HpnicfIpaIntListInPackets_Type()
)
hpnicfIpaIntListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaIntListInPackets.setStatus("current")
_HpnicfIpaIntListInBytes_Type = Counter64
_HpnicfIpaIntListInBytes_Object = MibTableColumn
hpnicfIpaIntListInBytes = _HpnicfIpaIntListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 5),
    _HpnicfIpaIntListInBytes_Type()
)
hpnicfIpaIntListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaIntListInBytes.setStatus("current")
_HpnicfIpaIntListOutPackets_Type = Counter32
_HpnicfIpaIntListOutPackets_Object = MibTableColumn
hpnicfIpaIntListOutPackets = _HpnicfIpaIntListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 6),
    _HpnicfIpaIntListOutPackets_Type()
)
hpnicfIpaIntListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaIntListOutPackets.setStatus("current")
_HpnicfIpaIntListOutBytes_Type = Counter64
_HpnicfIpaIntListOutBytes_Object = MibTableColumn
hpnicfIpaIntListOutBytes = _HpnicfIpaIntListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 4, 1, 7),
    _HpnicfIpaIntListOutBytes_Type()
)
hpnicfIpaIntListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaIntListOutBytes.setStatus("current")
_HpnicfIpaExtListTable_Object = MibTable
hpnicfIpaExtListTable = _HpnicfIpaExtListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5)
)
if mibBuilder.loadTexts:
    hpnicfIpaExtListTable.setStatus("current")
_HpnicfIpaExtListEntry_Object = MibTableRow
hpnicfIpaExtListEntry = _HpnicfIpaExtListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1)
)
hpnicfIpaExtListEntry.setIndexNames(
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListIpSrc"),
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListIpDst"),
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaExtListProtocol"),
)
if mibBuilder.loadTexts:
    hpnicfIpaExtListEntry.setStatus("current")
_HpnicfIpaExtListIpSrc_Type = IpAddress
_HpnicfIpaExtListIpSrc_Object = MibTableColumn
hpnicfIpaExtListIpSrc = _HpnicfIpaExtListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 1),
    _HpnicfIpaExtListIpSrc_Type()
)
hpnicfIpaExtListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaExtListIpSrc.setStatus("current")
_HpnicfIpaExtListIpDst_Type = IpAddress
_HpnicfIpaExtListIpDst_Object = MibTableColumn
hpnicfIpaExtListIpDst = _HpnicfIpaExtListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 2),
    _HpnicfIpaExtListIpDst_Type()
)
hpnicfIpaExtListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaExtListIpDst.setStatus("current")


class _HpnicfIpaExtListProtocol_Type(Integer32):
    """Custom type hpnicfIpaExtListProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfIpaExtListProtocol_Type.__name__ = "Integer32"
_HpnicfIpaExtListProtocol_Object = MibTableColumn
hpnicfIpaExtListProtocol = _HpnicfIpaExtListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 3),
    _HpnicfIpaExtListProtocol_Type()
)
hpnicfIpaExtListProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaExtListProtocol.setStatus("current")
_HpnicfIpaExtListInPackets_Type = Counter32
_HpnicfIpaExtListInPackets_Object = MibTableColumn
hpnicfIpaExtListInPackets = _HpnicfIpaExtListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 4),
    _HpnicfIpaExtListInPackets_Type()
)
hpnicfIpaExtListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaExtListInPackets.setStatus("current")
_HpnicfIpaExtListInBytes_Type = Counter64
_HpnicfIpaExtListInBytes_Object = MibTableColumn
hpnicfIpaExtListInBytes = _HpnicfIpaExtListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 5),
    _HpnicfIpaExtListInBytes_Type()
)
hpnicfIpaExtListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaExtListInBytes.setStatus("current")
_HpnicfIpaExtListOutPackets_Type = Counter32
_HpnicfIpaExtListOutPackets_Object = MibTableColumn
hpnicfIpaExtListOutPackets = _HpnicfIpaExtListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 6),
    _HpnicfIpaExtListOutPackets_Type()
)
hpnicfIpaExtListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaExtListOutPackets.setStatus("current")
_HpnicfIpaExtListOutBytes_Type = Counter64
_HpnicfIpaExtListOutBytes_Object = MibTableColumn
hpnicfIpaExtListOutBytes = _HpnicfIpaExtListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 5, 1, 7),
    _HpnicfIpaExtListOutBytes_Type()
)
hpnicfIpaExtListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaExtListOutBytes.setStatus("current")
_HpnicfIpaFWListTable_Object = MibTable
hpnicfIpaFWListTable = _HpnicfIpaFWListTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6)
)
if mibBuilder.loadTexts:
    hpnicfIpaFWListTable.setStatus("current")
_HpnicfIpaFWListEntry_Object = MibTableRow
hpnicfIpaFWListEntry = _HpnicfIpaFWListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1)
)
hpnicfIpaFWListEntry.setIndexNames(
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaFWListIpSrc"),
    (0, "HPN-ICF-IPA-MIB", "hpnicfIpaFWListIpDst"),
)
if mibBuilder.loadTexts:
    hpnicfIpaFWListEntry.setStatus("current")
_HpnicfIpaFWListIpSrc_Type = IpAddress
_HpnicfIpaFWListIpSrc_Object = MibTableColumn
hpnicfIpaFWListIpSrc = _HpnicfIpaFWListIpSrc_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 1),
    _HpnicfIpaFWListIpSrc_Type()
)
hpnicfIpaFWListIpSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaFWListIpSrc.setStatus("current")
_HpnicfIpaFWListIpDst_Type = IpAddress
_HpnicfIpaFWListIpDst_Object = MibTableColumn
hpnicfIpaFWListIpDst = _HpnicfIpaFWListIpDst_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 2),
    _HpnicfIpaFWListIpDst_Type()
)
hpnicfIpaFWListIpDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpaFWListIpDst.setStatus("current")
_HpnicfIpaFWListInPackets_Type = Counter32
_HpnicfIpaFWListInPackets_Object = MibTableColumn
hpnicfIpaFWListInPackets = _HpnicfIpaFWListInPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 3),
    _HpnicfIpaFWListInPackets_Type()
)
hpnicfIpaFWListInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaFWListInPackets.setStatus("current")
_HpnicfIpaFWListInBytes_Type = Counter64
_HpnicfIpaFWListInBytes_Object = MibTableColumn
hpnicfIpaFWListInBytes = _HpnicfIpaFWListInBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 4),
    _HpnicfIpaFWListInBytes_Type()
)
hpnicfIpaFWListInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaFWListInBytes.setStatus("current")
_HpnicfIpaFWListOutPackets_Type = Counter32
_HpnicfIpaFWListOutPackets_Object = MibTableColumn
hpnicfIpaFWListOutPackets = _HpnicfIpaFWListOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 5),
    _HpnicfIpaFWListOutPackets_Type()
)
hpnicfIpaFWListOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaFWListOutPackets.setStatus("current")
_HpnicfIpaFWListOutBytes_Type = Counter64
_HpnicfIpaFWListOutBytes_Object = MibTableColumn
hpnicfIpaFWListOutBytes = _HpnicfIpaFWListOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 25, 6, 1, 6),
    _HpnicfIpaFWListOutBytes_Type()
)
hpnicfIpaFWListOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpaFWListOutBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPA-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "hpnicfIpa": hpnicfIpa,
       "hpnicfIpaGlobalStats": hpnicfIpaGlobalStats,
       "hpnicfIpaGlobalEnable": hpnicfIpaGlobalEnable,
       "hpnicfIpaTimeOutSeconds": hpnicfIpaTimeOutSeconds,
       "hpnicfIpaIntListMaxItemNum": hpnicfIpaIntListMaxItemNum,
       "hpnicfIpaExtListMaxItemNum": hpnicfIpaExtListMaxItemNum,
       "hpnicfIpaFWListMaxItemNum": hpnicfIpaFWListMaxItemNum,
       "hpnicfIpaAccountListMaxItemNum": hpnicfIpaAccountListMaxItemNum,
       "hpnicfIpaAccountListNextIndex": hpnicfIpaAccountListNextIndex,
       "hpnicfIpaListCleaningFlag": hpnicfIpaListCleaningFlag,
       "hpnicfIpaIfConfigTable": hpnicfIpaIfConfigTable,
       "hpnicfIpaIfConfigEntry": hpnicfIpaIfConfigEntry,
       "hpnicfIpaIfConfigIfIndex": hpnicfIpaIfConfigIfIndex,
       "hpnicfIpaIfConfigInEnable": hpnicfIpaIfConfigInEnable,
       "hpnicfIpaIfConfigOutEnable": hpnicfIpaIfConfigOutEnable,
       "hpnicfIpaIfConfigFWEnable": hpnicfIpaIfConfigFWEnable,
       "hpnicfIpaAccountListTable": hpnicfIpaAccountListTable,
       "hpnicfIpaAccountListEntry": hpnicfIpaAccountListEntry,
       "hpnicfIpaAccountListIndex": hpnicfIpaAccountListIndex,
       "hpnicfIpaAccountListIpAddr": hpnicfIpaAccountListIpAddr,
       "hpnicfIpaAccountListIpMask": hpnicfIpaAccountListIpMask,
       "hpnicfIpaAccountListRowStatus": hpnicfIpaAccountListRowStatus,
       "hpnicfIpaIntListTable": hpnicfIpaIntListTable,
       "hpnicfIpaIntListEntry": hpnicfIpaIntListEntry,
       "hpnicfIpaIntListIpSrc": hpnicfIpaIntListIpSrc,
       "hpnicfIpaIntListIpDst": hpnicfIpaIntListIpDst,
       "hpnicfIpaIntListProtocol": hpnicfIpaIntListProtocol,
       "hpnicfIpaIntListInPackets": hpnicfIpaIntListInPackets,
       "hpnicfIpaIntListInBytes": hpnicfIpaIntListInBytes,
       "hpnicfIpaIntListOutPackets": hpnicfIpaIntListOutPackets,
       "hpnicfIpaIntListOutBytes": hpnicfIpaIntListOutBytes,
       "hpnicfIpaExtListTable": hpnicfIpaExtListTable,
       "hpnicfIpaExtListEntry": hpnicfIpaExtListEntry,
       "hpnicfIpaExtListIpSrc": hpnicfIpaExtListIpSrc,
       "hpnicfIpaExtListIpDst": hpnicfIpaExtListIpDst,
       "hpnicfIpaExtListProtocol": hpnicfIpaExtListProtocol,
       "hpnicfIpaExtListInPackets": hpnicfIpaExtListInPackets,
       "hpnicfIpaExtListInBytes": hpnicfIpaExtListInBytes,
       "hpnicfIpaExtListOutPackets": hpnicfIpaExtListOutPackets,
       "hpnicfIpaExtListOutBytes": hpnicfIpaExtListOutBytes,
       "hpnicfIpaFWListTable": hpnicfIpaFWListTable,
       "hpnicfIpaFWListEntry": hpnicfIpaFWListEntry,
       "hpnicfIpaFWListIpSrc": hpnicfIpaFWListIpSrc,
       "hpnicfIpaFWListIpDst": hpnicfIpaFWListIpDst,
       "hpnicfIpaFWListInPackets": hpnicfIpaFWListInPackets,
       "hpnicfIpaFWListInBytes": hpnicfIpaFWListInBytes,
       "hpnicfIpaFWListOutPackets": hpnicfIpaFWListOutPackets,
       "hpnicfIpaFWListOutBytes": hpnicfIpaFWListOutBytes}
)
