# SNMP MIB module (ACC-SFT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-SFT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:57 2024
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

_AccSFT_ObjectIdentity = ObjectIdentity
accSFT = _AccSFT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47)
)
_AccSFTunTable_Object = MibTable
accSFTunTable = _AccSFTunTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1)
)
if mibBuilder.loadTexts:
    accSFTunTable.setStatus("mandatory")
_AccSFTunEntry_Object = MibTableRow
accSFTunEntry = _AccSFTunEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1)
)
accSFTunEntry.setIndexNames(
    (0, "ACC-SFT", "accSFTunIndex"),
)
if mibBuilder.loadTexts:
    accSFTunEntry.setStatus("mandatory")
_AccSFTunIndex_Type = Integer32
_AccSFTunIndex_Object = MibTableColumn
accSFTunIndex = _AccSFTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 1),
    _AccSFTunIndex_Type()
)
accSFTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSFTunIndex.setStatus("mandatory")


class _AccSFTunEntStatus_Type(Integer32):
    """Custom type accSFTunEntStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_AccSFTunEntStatus_Type.__name__ = "Integer32"
_AccSFTunEntStatus_Object = MibTableColumn
accSFTunEntStatus = _AccSFTunEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 2),
    _AccSFTunEntStatus_Type()
)
accSFTunEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSFTunEntStatus.setStatus("mandatory")
_AccSFTunIfIndex_Type = Integer32
_AccSFTunIfIndex_Object = MibTableColumn
accSFTunIfIndex = _AccSFTunIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 3),
    _AccSFTunIfIndex_Type()
)
accSFTunIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSFTunIfIndex.setStatus("mandatory")
_AccSFTunRemIPAddr_Type = IpAddress
_AccSFTunRemIPAddr_Object = MibTableColumn
accSFTunRemIPAddr = _AccSFTunRemIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 4),
    _AccSFTunRemIPAddr_Type()
)
accSFTunRemIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSFTunRemIPAddr.setStatus("mandatory")


class _AccSFTunUDPAddr_Type(Integer32):
    """Custom type accSFTunUDPAddr based on Integer32"""
    defaultValue = 2764

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 4000),
    )


_AccSFTunUDPAddr_Type.__name__ = "Integer32"
_AccSFTunUDPAddr_Object = MibTableColumn
accSFTunUDPAddr = _AccSFTunUDPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 5),
    _AccSFTunUDPAddr_Type()
)
accSFTunUDPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSFTunUDPAddr.setStatus("mandatory")


class _AccSFTunAdStat_Type(Integer32):
    """Custom type accSFTunAdStat based on Integer32"""
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


_AccSFTunAdStat_Type.__name__ = "Integer32"
_AccSFTunAdStat_Object = MibTableColumn
accSFTunAdStat = _AccSFTunAdStat_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 1, 1, 6),
    _AccSFTunAdStat_Type()
)
accSFTunAdStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accSFTunAdStat.setStatus("mandatory")
_AccSFTStatTable_Object = MibTable
accSFTStatTable = _AccSFTStatTable_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 2)
)
if mibBuilder.loadTexts:
    accSFTStatTable.setStatus("mandatory")
_AccSFTStatEntry_Object = MibTableRow
accSFTStatEntry = _AccSFTStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 2, 1)
)
accSFTStatEntry.setIndexNames(
    (0, "ACC-SFT", "accSFTunIndex"),
)
if mibBuilder.loadTexts:
    accSFTStatEntry.setStatus("mandatory")
_AccSFTunInPkts_Type = Counter32
_AccSFTunInPkts_Object = MibTableColumn
accSFTunInPkts = _AccSFTunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 2, 1, 1),
    _AccSFTunInPkts_Type()
)
accSFTunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSFTunInPkts.setStatus("mandatory")
_AccSFTunOutPkts_Type = Counter32
_AccSFTunOutPkts_Object = MibTableColumn
accSFTunOutPkts = _AccSFTunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 47, 2, 1, 2),
    _AccSFTunOutPkts_Type()
)
accSFTunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accSFTunOutPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-SFT",
    **{"accSFT": accSFT,
       "accSFTunTable": accSFTunTable,
       "accSFTunEntry": accSFTunEntry,
       "accSFTunIndex": accSFTunIndex,
       "accSFTunEntStatus": accSFTunEntStatus,
       "accSFTunIfIndex": accSFTunIfIndex,
       "accSFTunRemIPAddr": accSFTunRemIPAddr,
       "accSFTunUDPAddr": accSFTunUDPAddr,
       "accSFTunAdStat": accSFTunAdStat,
       "accSFTStatTable": accSFTStatTable,
       "accSFTStatEntry": accSFTStatEntry,
       "accSFTunInPkts": accSFTunInPkts,
       "accSFTunOutPkts": accSFTunOutPkts}
)
