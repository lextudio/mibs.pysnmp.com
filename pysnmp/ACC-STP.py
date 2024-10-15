# SNMP MIB module (ACC-STP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-STP
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:02 2024
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
 accBRG) = mibBuilder.importSymbols(
    "ACC-MIB",
    "DisplayString",
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

_AccStp_ObjectIdentity = ObjectIdentity
accStp = _AccStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2)
)


class _AccStpPriority_Type(Integer32):
    """Custom type accStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccStpPriority_Type.__name__ = "Integer32"
_AccStpPriority_Object = MibScalar
accStpPriority = _AccStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 1),
    _AccStpPriority_Type()
)
accStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpPriority.setStatus("mandatory")
_AccStpId_Type = OctetString
_AccStpId_Object = MibScalar
accStpId = _AccStpId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 2),
    _AccStpId_Type()
)
accStpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpId.setStatus("mandatory")
_AccStpBrAddr_Type = OctetString
_AccStpBrAddr_Object = MibScalar
accStpBrAddr = _AccStpBrAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 3),
    _AccStpBrAddr_Type()
)
accStpBrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpBrAddr.setStatus("mandatory")


class _AccStpMode_Type(Integer32):
    """Custom type accStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_AccStpMode_Type.__name__ = "Integer32"
_AccStpMode_Object = MibScalar
accStpMode = _AccStpMode_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 4),
    _AccStpMode_Type()
)
accStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMode.setStatus("mandatory")
_AccStpFilterTime_Type = TimeTicks
_AccStpFilterTime_Object = MibScalar
accStpFilterTime = _AccStpFilterTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 5),
    _AccStpFilterTime_Type()
)
accStpFilterTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpFilterTime.setStatus("mandatory")
_AccStpMcastAddr_Type = OctetString
_AccStpMcastAddr_Object = MibScalar
accStpMcastAddr = _AccStpMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 6),
    _AccStpMcastAddr_Type()
)
accStpMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMcastAddr.setStatus("mandatory")


class _AccStpTopChangeDet_Type(Integer32):
    """Custom type accStpTopChangeDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AccStpTopChangeDet_Type.__name__ = "Integer32"
_AccStpTopChangeDet_Object = MibScalar
accStpTopChangeDet = _AccStpTopChangeDet_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 7),
    _AccStpTopChangeDet_Type()
)
accStpTopChangeDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeDet.setStatus("mandatory")


class _AccStpTopChange_Type(Integer32):
    """Custom type accStpTopChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AccStpTopChange_Type.__name__ = "Integer32"
_AccStpTopChange_Object = MibScalar
accStpTopChange = _AccStpTopChange_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 8),
    _AccStpTopChange_Type()
)
accStpTopChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChange.setStatus("mandatory")
_AccStpTopChangeTimer_Type = TimeTicks
_AccStpTopChangeTimer_Object = MibScalar
accStpTopChangeTimer = _AccStpTopChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 9),
    _AccStpTopChangeTimer_Type()
)
accStpTopChangeTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeTimer.setStatus("mandatory")
_AccStpDesRoot_Type = OctetString
_AccStpDesRoot_Object = MibScalar
accStpDesRoot = _AccStpDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 10),
    _AccStpDesRoot_Type()
)
accStpDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpDesRoot.setStatus("mandatory")
_AccStpRootPathCost_Type = Integer32
_AccStpRootPathCost_Object = MibScalar
accStpRootPathCost = _AccStpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 11),
    _AccStpRootPathCost_Type()
)
accStpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpRootPathCost.setStatus("mandatory")
_AccStpRootPort_Type = OctetString
_AccStpRootPort_Object = MibScalar
accStpRootPort = _AccStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 12),
    _AccStpRootPort_Type()
)
accStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpRootPort.setStatus("mandatory")


class _AccStpMaxAge_Type(Integer32):
    """Custom type accStpMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 3600),
    )


_AccStpMaxAge_Type.__name__ = "Integer32"
_AccStpMaxAge_Object = MibScalar
accStpMaxAge = _AccStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 13),
    _AccStpMaxAge_Type()
)
accStpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpMaxAge.setStatus("mandatory")


class _AccStpHelloTime_Type(Integer32):
    """Custom type accStpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1800),
    )


_AccStpHelloTime_Type.__name__ = "Integer32"
_AccStpHelloTime_Object = MibScalar
accStpHelloTime = _AccStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 14),
    _AccStpHelloTime_Type()
)
accStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpHelloTime.setStatus("mandatory")


class _AccStpForwardDelay_Type(Integer32):
    """Custom type accStpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_AccStpForwardDelay_Type.__name__ = "Integer32"
_AccStpForwardDelay_Object = MibScalar
accStpForwardDelay = _AccStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 15),
    _AccStpForwardDelay_Type()
)
accStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accStpForwardDelay.setStatus("mandatory")
_AccStpUpTime_Type = TimeTicks
_AccStpUpTime_Object = MibScalar
accStpUpTime = _AccStpUpTime_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 16),
    _AccStpUpTime_Type()
)
accStpUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpUpTime.setStatus("mandatory")
_AccStpTopChangeCnts_Type = Counter32
_AccStpTopChangeCnts_Object = MibScalar
accStpTopChangeCnts = _AccStpTopChangeCnts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 2, 17),
    _AccStpTopChangeCnts_Type()
)
accStpTopChangeCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accStpTopChangeCnts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-STP",
    **{"accStp": accStp,
       "accStpPriority": accStpPriority,
       "accStpId": accStpId,
       "accStpBrAddr": accStpBrAddr,
       "accStpMode": accStpMode,
       "accStpFilterTime": accStpFilterTime,
       "accStpMcastAddr": accStpMcastAddr,
       "accStpTopChangeDet": accStpTopChangeDet,
       "accStpTopChange": accStpTopChange,
       "accStpTopChangeTimer": accStpTopChangeTimer,
       "accStpDesRoot": accStpDesRoot,
       "accStpRootPathCost": accStpRootPathCost,
       "accStpRootPort": accStpRootPort,
       "accStpMaxAge": accStpMaxAge,
       "accStpHelloTime": accStpHelloTime,
       "accStpForwardDelay": accStpForwardDelay,
       "accStpUpTime": accStpUpTime,
       "accStpTopChangeCnts": accStpTopChangeCnts}
)
