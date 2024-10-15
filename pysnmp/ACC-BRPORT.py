# SNMP MIB module (ACC-BRPORT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-BRPORT
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:56 2024
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

_AccBrPort_ObjectIdentity = ObjectIdentity
accBrPort = _AccBrPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3)
)
_AccBrPortInfo_ObjectIdentity = ObjectIdentity
accBrPortInfo = _AccBrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1)
)
_AccBrPortStats_ObjectIdentity = ObjectIdentity
accBrPortStats = _AccBrPortStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1)
)
_AccBrPortInNUcastPkts_Type = Counter32
_AccBrPortInNUcastPkts_Object = MibScalar
accBrPortInNUcastPkts = _AccBrPortInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 1),
    _AccBrPortInNUcastPkts_Type()
)
accBrPortInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInNUcastPkts.setStatus("mandatory")
_AccBrPortInUcastPkts_Type = Counter32
_AccBrPortInUcastPkts_Object = MibScalar
accBrPortInUcastPkts = _AccBrPortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 2),
    _AccBrPortInUcastPkts_Type()
)
accBrPortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInUcastPkts.setStatus("mandatory")
_AccBrPortInDupPkts_Type = Counter32
_AccBrPortInDupPkts_Object = MibScalar
accBrPortInDupPkts = _AccBrPortInDupPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 3),
    _AccBrPortInDupPkts_Type()
)
accBrPortInDupPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInDupPkts.setStatus("mandatory")
_AccBrPortOutNUcastPkts_Type = Counter32
_AccBrPortOutNUcastPkts_Object = MibScalar
accBrPortOutNUcastPkts = _AccBrPortOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 4),
    _AccBrPortOutNUcastPkts_Type()
)
accBrPortOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutNUcastPkts.setStatus("mandatory")
_AccBrPortOutUcastPkts_Type = Counter32
_AccBrPortOutUcastPkts_Object = MibScalar
accBrPortOutUcastPkts = _AccBrPortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 5),
    _AccBrPortOutUcastPkts_Type()
)
accBrPortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutUcastPkts.setStatus("mandatory")
_AccBrPortStpInPkts_Type = Counter32
_AccBrPortStpInPkts_Object = MibScalar
accBrPortStpInPkts = _AccBrPortStpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 6),
    _AccBrPortStpInPkts_Type()
)
accBrPortStpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpInPkts.setStatus("mandatory")
_AccBrPortStpOutPkts_Type = Counter32
_AccBrPortStpOutPkts_Object = MibScalar
accBrPortStpOutPkts = _AccBrPortStpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 7),
    _AccBrPortStpOutPkts_Type()
)
accBrPortStpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpOutPkts.setStatus("mandatory")
_AccBrPortOutDelayDiscPkts_Type = Counter32
_AccBrPortOutDelayDiscPkts_Object = MibScalar
accBrPortOutDelayDiscPkts = _AccBrPortOutDelayDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 8),
    _AccBrPortOutDelayDiscPkts_Type()
)
accBrPortOutDelayDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutDelayDiscPkts.setStatus("mandatory")
_AccBrPortOutPrioDiscPkts_Type = Counter32
_AccBrPortOutPrioDiscPkts_Object = MibScalar
accBrPortOutPrioDiscPkts = _AccBrPortOutPrioDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 9),
    _AccBrPortOutPrioDiscPkts_Type()
)
accBrPortOutPrioDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutPrioDiscPkts.setStatus("mandatory")
_AccBrPortOutQLen_Type = Gauge32
_AccBrPortOutQLen_Object = MibScalar
accBrPortOutQLen = _AccBrPortOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 10),
    _AccBrPortOutQLen_Type()
)
accBrPortOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortOutQLen.setStatus("mandatory")
_AccBrPortInDiscPkts_Type = Counter32
_AccBrPortInDiscPkts_Object = MibScalar
accBrPortInDiscPkts = _AccBrPortInDiscPkts_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 1, 11),
    _AccBrPortInDiscPkts_Type()
)
accBrPortInDiscPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortInDiscPkts.setStatus("mandatory")


class _AccBrPortStpPriority_Type(Integer32):
    """Custom type accBrPortStpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AccBrPortStpPriority_Type.__name__ = "Integer32"
_AccBrPortStpPriority_Object = MibScalar
accBrPortStpPriority = _AccBrPortStpPriority_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 2),
    _AccBrPortStpPriority_Type()
)
accBrPortStpPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortStpPriority.setStatus("mandatory")
_AccBrPortId_Type = OctetString
_AccBrPortId_Object = MibScalar
accBrPortId = _AccBrPortId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 3),
    _AccBrPortId_Type()
)
accBrPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortId.setStatus("mandatory")


class _AccBrPortState_Type(Integer32):
    """Custom type accBrPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("disabled", 0),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )


_AccBrPortState_Type.__name__ = "Integer32"
_AccBrPortState_Object = MibScalar
accBrPortState = _AccBrPortState_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 5),
    _AccBrPortState_Type()
)
accBrPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortState.setStatus("mandatory")


class _AccBrPortStpPathCost_Type(Integer32):
    """Custom type accBrPortStpPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrPortStpPathCost_Type.__name__ = "Integer32"
_AccBrPortStpPathCost_Object = MibScalar
accBrPortStpPathCost = _AccBrPortStpPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 6),
    _AccBrPortStpPathCost_Type()
)
accBrPortStpPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortStpPathCost.setStatus("mandatory")
_AccBrPortStpDesRoot_Type = OctetString
_AccBrPortStpDesRoot_Object = MibScalar
accBrPortStpDesRoot = _AccBrPortStpDesRoot_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 7),
    _AccBrPortStpDesRoot_Type()
)
accBrPortStpDesRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesRoot.setStatus("mandatory")


class _AccBrPortStpDesCost_Type(Integer32):
    """Custom type accBrPortStpDesCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AccBrPortStpDesCost_Type.__name__ = "Integer32"
_AccBrPortStpDesCost_Object = MibScalar
accBrPortStpDesCost = _AccBrPortStpDesCost_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 8),
    _AccBrPortStpDesCost_Type()
)
accBrPortStpDesCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesCost.setStatus("mandatory")
_AccBrPortStpDesBridge_Type = OctetString
_AccBrPortStpDesBridge_Object = MibScalar
accBrPortStpDesBridge = _AccBrPortStpDesBridge_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 9),
    _AccBrPortStpDesBridge_Type()
)
accBrPortStpDesBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesBridge.setStatus("mandatory")
_AccBrPortStpDesPort_Type = OctetString
_AccBrPortStpDesPort_Object = MibScalar
accBrPortStpDesPort = _AccBrPortStpDesPort_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 10),
    _AccBrPortStpDesPort_Type()
)
accBrPortStpDesPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortStpDesPort.setStatus("mandatory")


class _AccBrPortAdminStatus_Type(Integer32):
    """Custom type accBrPortAdminStatus based on Integer32"""
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


_AccBrPortAdminStatus_Type.__name__ = "Integer32"
_AccBrPortAdminStatus_Object = MibScalar
accBrPortAdminStatus = _AccBrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 11),
    _AccBrPortAdminStatus_Type()
)
accBrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortAdminStatus.setStatus("mandatory")
_AccBrPortLine_Type = Integer32
_AccBrPortLine_Object = MibScalar
accBrPortLine = _AccBrPortLine_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 12),
    _AccBrPortLine_Type()
)
accBrPortLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortLine.setStatus("mandatory")


class _AccBrPortProtocol_Type(Integer32):
    """Custom type accBrPortProtocol based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dial", 10),
          ("enet", 1),
          ("fddi", 9),
          ("ffr", 4),
          ("lapb", 3),
          ("multilink", 11),
          ("other", 5),
          ("ppp", 8),
          ("smds", 7),
          ("token-ring", 6),
          ("x25", 2))
    )


_AccBrPortProtocol_Type.__name__ = "Integer32"
_AccBrPortProtocol_Object = MibScalar
accBrPortProtocol = _AccBrPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 13),
    _AccBrPortProtocol_Type()
)
accBrPortProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortProtocol.setStatus("mandatory")
_AccBrPortFrDlci_Type = Integer32
_AccBrPortFrDlci_Object = MibScalar
accBrPortFrDlci = _AccBrPortFrDlci_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 14),
    _AccBrPortFrDlci_Type()
)
accBrPortFrDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accBrPortFrDlci.setStatus("mandatory")
_AccBrPortIndex_Type = Integer32
_AccBrPortIndex_Object = MibScalar
accBrPortIndex = _AccBrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 15),
    _AccBrPortIndex_Type()
)
accBrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortIndex.setStatus("mandatory")


class _AccBrPortXBridgeStatus_Type(Integer32):
    """Custom type accBrPortXBridgeStatus based on Integer32"""
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


_AccBrPortXBridgeStatus_Type.__name__ = "Integer32"
_AccBrPortXBridgeStatus_Object = MibScalar
accBrPortXBridgeStatus = _AccBrPortXBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 3, 1, 16),
    _AccBrPortXBridgeStatus_Type()
)
accBrPortXBridgeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accBrPortXBridgeStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-BRPORT",
    **{"accBrPort": accBrPort,
       "accBrPortInfo": accBrPortInfo,
       "accBrPortStats": accBrPortStats,
       "accBrPortInNUcastPkts": accBrPortInNUcastPkts,
       "accBrPortInUcastPkts": accBrPortInUcastPkts,
       "accBrPortInDupPkts": accBrPortInDupPkts,
       "accBrPortOutNUcastPkts": accBrPortOutNUcastPkts,
       "accBrPortOutUcastPkts": accBrPortOutUcastPkts,
       "accBrPortStpInPkts": accBrPortStpInPkts,
       "accBrPortStpOutPkts": accBrPortStpOutPkts,
       "accBrPortOutDelayDiscPkts": accBrPortOutDelayDiscPkts,
       "accBrPortOutPrioDiscPkts": accBrPortOutPrioDiscPkts,
       "accBrPortOutQLen": accBrPortOutQLen,
       "accBrPortInDiscPkts": accBrPortInDiscPkts,
       "accBrPortStpPriority": accBrPortStpPriority,
       "accBrPortId": accBrPortId,
       "accBrPortState": accBrPortState,
       "accBrPortStpPathCost": accBrPortStpPathCost,
       "accBrPortStpDesRoot": accBrPortStpDesRoot,
       "accBrPortStpDesCost": accBrPortStpDesCost,
       "accBrPortStpDesBridge": accBrPortStpDesBridge,
       "accBrPortStpDesPort": accBrPortStpDesPort,
       "accBrPortAdminStatus": accBrPortAdminStatus,
       "accBrPortLine": accBrPortLine,
       "accBrPortProtocol": accBrPortProtocol,
       "accBrPortFrDlci": accBrPortFrDlci,
       "accBrPortIndex": accBrPortIndex,
       "accBrPortXBridgeStatus": accBrPortXBridgeStatus}
)
