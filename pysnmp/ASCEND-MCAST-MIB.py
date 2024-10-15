# SNMP MIB module (ASCEND-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:41:00 2024
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

(mCastGroup,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "mCastGroup")

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

_HeartBeatMulticastGroupAddress_Type = IpAddress
_HeartBeatMulticastGroupAddress_Object = MibScalar
heartBeatMulticastGroupAddress = _HeartBeatMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 14, 1),
    _HeartBeatMulticastGroupAddress_Type()
)
heartBeatMulticastGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeatMulticastGroupAddress.setStatus("mandatory")
_HeartBeatSourceAddress_Type = IpAddress
_HeartBeatSourceAddress_Object = MibScalar
heartBeatSourceAddress = _HeartBeatSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 14, 2),
    _HeartBeatSourceAddress_Type()
)
heartBeatSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeatSourceAddress.setStatus("mandatory")
_HeartBeatSlotTimeInterval_Type = Integer32
_HeartBeatSlotTimeInterval_Object = MibScalar
heartBeatSlotTimeInterval = _HeartBeatSlotTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 529, 14, 3),
    _HeartBeatSlotTimeInterval_Type()
)
heartBeatSlotTimeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeatSlotTimeInterval.setStatus("mandatory")
_HeartBeatSlotCount_Type = Integer32
_HeartBeatSlotCount_Object = MibScalar
heartBeatSlotCount = _HeartBeatSlotCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 14, 4),
    _HeartBeatSlotCount_Type()
)
heartBeatSlotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeatSlotCount.setStatus("mandatory")
_HeartBeatPacketCount_Type = Counter32
_HeartBeatPacketCount_Object = MibScalar
heartBeatPacketCount = _HeartBeatPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 14, 5),
    _HeartBeatPacketCount_Type()
)
heartBeatPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeatPacketCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MCAST-MIB",
    **{"heartBeatMulticastGroupAddress": heartBeatMulticastGroupAddress,
       "heartBeatSourceAddress": heartBeatSourceAddress,
       "heartBeatSlotTimeInterval": heartBeatSlotTimeInterval,
       "heartBeatSlotCount": heartBeatSlotCount,
       "heartBeatPacketCount": heartBeatPacketCount}
)
