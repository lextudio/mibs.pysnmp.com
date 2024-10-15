# SNMP MIB module (ACC-UDPHELPER) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-UDPHELPER
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:08 2024
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

(DisplayString,
 IfIndex,
 RowStatus,
 SmdsAddress,
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
    "IfIndex",
    "RowStatus",
    "SmdsAddress",
    "accBRG")

(accTrapLogSeqNum,) = mibBuilder.importSymbols(
    "ACC-SYSTEM",
    "accTrapLogSeqNum")

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
 NotificationType,
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
    "NotificationType",
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

_AccUDPHelper_ObjectIdentity = ObjectIdentity
accUDPHelper = _AccUDPHelper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48)
)


class _AccUdpHelperStatus_Type(Integer32):
    """Custom type accUdpHelperStatus based on Integer32"""
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


_AccUdpHelperStatus_Type.__name__ = "Integer32"
_AccUdpHelperStatus_Object = MibScalar
accUdpHelperStatus = _AccUdpHelperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 1),
    _AccUdpHelperStatus_Type()
)
accUdpHelperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUdpHelperStatus.setStatus("mandatory")
_AccUdpHelperPortTable_Object = MibTable
accUdpHelperPortTable = _AccUdpHelperPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 2)
)
if mibBuilder.loadTexts:
    accUdpHelperPortTable.setStatus("mandatory")
_AccUdpHelperPortEntry_Object = MibTableRow
accUdpHelperPortEntry = _AccUdpHelperPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 2, 1)
)
accUdpHelperPortEntry.setIndexNames(
    (0, "ACC-UDPHELPER", "accUdpHelperPortNo"),
    (0, "ACC-UDPHELPER", "accUDPHelperIpAddr"),
)
if mibBuilder.loadTexts:
    accUdpHelperPortEntry.setStatus("mandatory")


class _AccUdpHelperPortNo_Type(Integer32):
    """Custom type accUdpHelperPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccUdpHelperPortNo_Type.__name__ = "Integer32"
_AccUdpHelperPortNo_Object = MibTableColumn
accUdpHelperPortNo = _AccUdpHelperPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 2, 1, 1),
    _AccUdpHelperPortNo_Type()
)
accUdpHelperPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUdpHelperPortNo.setStatus("mandatory")
_AccUDPHelperIpAddr_Type = IpAddress
_AccUDPHelperIpAddr_Object = MibTableColumn
accUDPHelperIpAddr = _AccUDPHelperIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 2, 1, 2),
    _AccUDPHelperIpAddr_Type()
)
accUDPHelperIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUDPHelperIpAddr.setStatus("mandatory")


class _AccUdpHelperTtlOverride_Type(Integer32):
    """Custom type accUdpHelperTtlOverride based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccUdpHelperTtlOverride_Type.__name__ = "Integer32"
_AccUdpHelperTtlOverride_Object = MibTableColumn
accUdpHelperTtlOverride = _AccUdpHelperTtlOverride_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 2, 1, 3),
    _AccUdpHelperTtlOverride_Type()
)
accUdpHelperTtlOverride.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUdpHelperTtlOverride.setStatus("mandatory")
_AccUdpHelperStatsTable_Object = MibTable
accUdpHelperStatsTable = _AccUdpHelperStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3)
)
if mibBuilder.loadTexts:
    accUdpHelperStatsTable.setStatus("mandatory")
_AccUdpHelperStatsEntry_Object = MibTableRow
accUdpHelperStatsEntry = _AccUdpHelperStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1)
)
accUdpHelperStatsEntry.setIndexNames(
    (0, "ACC-UDPHELPER", "accUdpHelperStPortNo"),
)
if mibBuilder.loadTexts:
    accUdpHelperStatsEntry.setStatus("mandatory")


class _AccUdpHelperStPortNo_Type(Integer32):
    """Custom type accUdpHelperStPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AccUdpHelperStPortNo_Type.__name__ = "Integer32"
_AccUdpHelperStPortNo_Object = MibTableColumn
accUdpHelperStPortNo = _AccUdpHelperStPortNo_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1, 1),
    _AccUdpHelperStPortNo_Type()
)
accUdpHelperStPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUdpHelperStPortNo.setStatus("mandatory")
_AccUDPHelperReceivedPkts_Type = Counter32
_AccUDPHelperReceivedPkts_Object = MibTableColumn
accUDPHelperReceivedPkts = _AccUDPHelperReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1, 2),
    _AccUDPHelperReceivedPkts_Type()
)
accUDPHelperReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUDPHelperReceivedPkts.setStatus("mandatory")
_AccUDPHelperForwardedPkts_Type = Counter32
_AccUDPHelperForwardedPkts_Object = MibTableColumn
accUDPHelperForwardedPkts = _AccUDPHelperForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1, 3),
    _AccUDPHelperForwardedPkts_Type()
)
accUDPHelperForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUDPHelperForwardedPkts.setStatus("mandatory")
_AccUDPHelperRebroadcastedPkts_Type = Counter32
_AccUDPHelperRebroadcastedPkts_Object = MibTableColumn
accUDPHelperRebroadcastedPkts = _AccUDPHelperRebroadcastedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1, 4),
    _AccUDPHelperRebroadcastedPkts_Type()
)
accUDPHelperRebroadcastedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUDPHelperRebroadcastedPkts.setStatus("mandatory")
_AccUDPHelperDiscardedPkts_Type = Counter32
_AccUDPHelperDiscardedPkts_Object = MibTableColumn
accUDPHelperDiscardedPkts = _AccUDPHelperDiscardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 3, 1, 5),
    _AccUDPHelperDiscardedPkts_Type()
)
accUDPHelperDiscardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUDPHelperDiscardedPkts.setStatus("mandatory")


class _AccUdpHelperPrAction_Type(Integer32):
    """Custom type accUdpHelperPrAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("add", 1),
          ("delete", 2))
    )


_AccUdpHelperPrAction_Type.__name__ = "Integer32"
_AccUdpHelperPrAction_Object = MibScalar
accUdpHelperPrAction = _AccUdpHelperPrAction_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 48, 4),
    _AccUdpHelperPrAction_Type()
)
accUdpHelperPrAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accUdpHelperPrAction.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-UDPHELPER",
    **{"accUDPHelper": accUDPHelper,
       "accUdpHelperStatus": accUdpHelperStatus,
       "accUdpHelperPortTable": accUdpHelperPortTable,
       "accUdpHelperPortEntry": accUdpHelperPortEntry,
       "accUdpHelperPortNo": accUdpHelperPortNo,
       "accUDPHelperIpAddr": accUDPHelperIpAddr,
       "accUdpHelperTtlOverride": accUdpHelperTtlOverride,
       "accUdpHelperStatsTable": accUdpHelperStatsTable,
       "accUdpHelperStatsEntry": accUdpHelperStatsEntry,
       "accUdpHelperStPortNo": accUdpHelperStPortNo,
       "accUDPHelperReceivedPkts": accUDPHelperReceivedPkts,
       "accUDPHelperForwardedPkts": accUDPHelperForwardedPkts,
       "accUDPHelperRebroadcastedPkts": accUDPHelperRebroadcastedPkts,
       "accUDPHelperDiscardedPkts": accUDPHelperDiscardedPkts,
       "accUdpHelperPrAction": accUdpHelperPrAction}
)
