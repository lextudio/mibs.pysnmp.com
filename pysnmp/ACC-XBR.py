# SNMP MIB module (ACC-XBR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ACC-XBR
# Produced by pysmi-1.5.4 at Mon Oct 14 20:33:12 2024
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

_AccXBr_ObjectIdentity = ObjectIdentity
accXBr = _AccXBr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34)
)
_AccXBridge_ObjectIdentity = ObjectIdentity
accXBridge = _AccXBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1)
)


class _AccXBridgeStatus_Type(Integer32):
    """Custom type accXBridgeStatus based on Integer32"""
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


_AccXBridgeStatus_Type.__name__ = "Integer32"
_AccXBridgeStatus_Object = MibScalar
accXBridgeStatus = _AccXBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1, 1),
    _AccXBridgeStatus_Type()
)
accXBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXBridgeStatus.setStatus("mandatory")
_AccXBridgeRingId_Type = Integer32
_AccXBridgeRingId_Object = MibScalar
accXBridgeRingId = _AccXBridgeRingId_Object(
    (1, 3, 6, 1, 4, 1, 5, 1, 1, 34, 1, 2),
    _AccXBridgeRingId_Type()
)
accXBridgeRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    accXBridgeRingId.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ACC-XBR",
    **{"accXBr": accXBr,
       "accXBridge": accXBridge,
       "accXBridgeStatus": accXBridgeStatus,
       "accXBridgeRingId": accXBridgeRingId}
)