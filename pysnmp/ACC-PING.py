# SNMP MIB module (ACC-PING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-PING
# Produced by pysmi-1.5.4 at Mon Oct 14 20:32:44 2024
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

_AccPing_ObjectIdentity = ObjectIdentity
accPing = _AccPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30)
)
_AccPingDest_Type = IpAddress
_AccPingDest_Object = MibScalar
accPingDest = _AccPingDest_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 1),
    _AccPingDest_Type()
)
accPingDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDest.setStatus("mandatory")


class _AccPingReqCnt_Type(Integer32):
    """Custom type accPingReqCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AccPingReqCnt_Type.__name__ = "Integer32"
_AccPingReqCnt_Object = MibScalar
accPingReqCnt = _AccPingReqCnt_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 2),
    _AccPingReqCnt_Type()
)
accPingReqCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingReqCnt.setStatus("mandatory")


class _AccPingDataMin_Type(Integer32):
    """Custom type accPingDataMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_AccPingDataMin_Type.__name__ = "Integer32"
_AccPingDataMin_Object = MibScalar
accPingDataMin = _AccPingDataMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 3),
    _AccPingDataMin_Type()
)
accPingDataMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDataMin.setStatus("mandatory")


class _AccPingDataMax_Type(Integer32):
    """Custom type accPingDataMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 1500),
    )


_AccPingDataMax_Type.__name__ = "Integer32"
_AccPingDataMax_Object = MibScalar
accPingDataMax = _AccPingDataMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 4),
    _AccPingDataMax_Type()
)
accPingDataMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingDataMax.setStatus("mandatory")


class _AccPingTimeMin_Type(Integer32):
    """Custom type accPingTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AccPingTimeMin_Type.__name__ = "Integer32"
_AccPingTimeMin_Object = MibScalar
accPingTimeMin = _AccPingTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 5),
    _AccPingTimeMin_Type()
)
accPingTimeMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingTimeMin.setStatus("mandatory")


class _AccPingTimeMax_Type(Integer32):
    """Custom type accPingTimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AccPingTimeMax_Type.__name__ = "Integer32"
_AccPingTimeMax_Object = MibScalar
accPingTimeMax = _AccPingTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 6),
    _AccPingTimeMax_Type()
)
accPingTimeMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accPingTimeMax.setStatus("mandatory")
_AccPingSndPkts_Type = Counter32
_AccPingSndPkts_Object = MibScalar
accPingSndPkts = _AccPingSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 7),
    _AccPingSndPkts_Type()
)
accPingSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingSndPkts.setStatus("mandatory")
_AccPingSndBytes_Type = Counter32
_AccPingSndBytes_Object = MibScalar
accPingSndBytes = _AccPingSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 8),
    _AccPingSndBytes_Type()
)
accPingSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingSndBytes.setStatus("mandatory")
_AccPingRcvPkts_Type = Counter32
_AccPingRcvPkts_Object = MibScalar
accPingRcvPkts = _AccPingRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 9),
    _AccPingRcvPkts_Type()
)
accPingRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvPkts.setStatus("mandatory")
_AccPingRcvBytes_Type = Counter32
_AccPingRcvBytes_Object = MibScalar
accPingRcvBytes = _AccPingRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 10),
    _AccPingRcvBytes_Type()
)
accPingRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvBytes.setStatus("mandatory")
_AccPingRcvOKs_Type = Counter32
_AccPingRcvOKs_Object = MibScalar
accPingRcvOKs = _AccPingRcvOKs_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 11),
    _AccPingRcvOKs_Type()
)
accPingRcvOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvOKs.setStatus("mandatory")
_AccPingRcvBads_Type = Counter32
_AccPingRcvBads_Object = MibScalar
accPingRcvBads = _AccPingRcvBads_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 12),
    _AccPingRcvBads_Type()
)
accPingRcvBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingRcvBads.setStatus("mandatory")
_AccPingDelayMin_Type = Integer32
_AccPingDelayMin_Object = MibScalar
accPingDelayMin = _AccPingDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 13),
    _AccPingDelayMin_Type()
)
accPingDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayMin.setStatus("mandatory")
_AccPingDelayMax_Type = Integer32
_AccPingDelayMax_Object = MibScalar
accPingDelayMax = _AccPingDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 14),
    _AccPingDelayMax_Type()
)
accPingDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayMax.setStatus("mandatory")
_AccPingDelayAvg_Type = Integer32
_AccPingDelayAvg_Object = MibScalar
accPingDelayAvg = _AccPingDelayAvg_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 30, 15),
    _AccPingDelayAvg_Type()
)
accPingDelayAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accPingDelayAvg.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-PING",
    **{"accPing": accPing,
       "accPingDest": accPingDest,
       "accPingReqCnt": accPingReqCnt,
       "accPingDataMin": accPingDataMin,
       "accPingDataMax": accPingDataMax,
       "accPingTimeMin": accPingTimeMin,
       "accPingTimeMax": accPingTimeMax,
       "accPingSndPkts": accPingSndPkts,
       "accPingSndBytes": accPingSndBytes,
       "accPingRcvPkts": accPingRcvPkts,
       "accPingRcvBytes": accPingRcvBytes,
       "accPingRcvOKs": accPingRcvOKs,
       "accPingRcvBads": accPingRcvBads,
       "accPingDelayMin": accPingDelayMin,
       "accPingDelayMax": accPingDelayMax,
       "accPingDelayAvg": accPingDelayAvg}
)
