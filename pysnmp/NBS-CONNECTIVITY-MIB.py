# SNMP MIB module (NBS-CONNECTIVITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-CONNECTIVITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:46 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(nbsCmmcChassisIndex,
 nbsCmmcPortIndex,
 nbsCmmcSlotIndex) = mibBuilder.importSymbols(
    "NBS-CMMC-MIB",
    "nbsCmmcChassisIndex",
    "nbsCmmcPortIndex",
    "nbsCmmcSlotIndex")

(nbs,) = mibBuilder.importSymbols(
    "NBS-MIB",
    "nbs")

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

nbsConnectivityMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 238)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NbsConnectivityGrp_ObjectIdentity = ObjectIdentity
nbsConnectivityGrp = _NbsConnectivityGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 238, 1)
)
if mibBuilder.loadTexts:
    nbsConnectivityGrp.setStatus("current")
_NbsConnectivityTable_Object = MibTable
nbsConnectivityTable = _NbsConnectivityTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1)
)
if mibBuilder.loadTexts:
    nbsConnectivityTable.setStatus("current")
_NbsConnectivityEntry_Object = MibTableRow
nbsConnectivityEntry = _NbsConnectivityEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1)
)
nbsConnectivityEntry.setIndexNames(
    (0, "NBS-CONNECTIVITY-MIB", "nbsConnectivitySourceIfIndex"),
    (0, "NBS-CONNECTIVITY-MIB", "nbsConnectivityOrdinalIndex"),
)
if mibBuilder.loadTexts:
    nbsConnectivityEntry.setStatus("current")
_NbsConnectivitySourceIfIndex_Type = InterfaceIndex
_NbsConnectivitySourceIfIndex_Object = MibTableColumn
nbsConnectivitySourceIfIndex = _NbsConnectivitySourceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 10),
    _NbsConnectivitySourceIfIndex_Type()
)
nbsConnectivitySourceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsConnectivitySourceIfIndex.setStatus("current")


class _NbsConnectivityOrdinalIndex_Type(Integer32):
    """Custom type nbsConnectivityOrdinalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NbsConnectivityOrdinalIndex_Type.__name__ = "Integer32"
_NbsConnectivityOrdinalIndex_Object = MibTableColumn
nbsConnectivityOrdinalIndex = _NbsConnectivityOrdinalIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 11),
    _NbsConnectivityOrdinalIndex_Type()
)
nbsConnectivityOrdinalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbsConnectivityOrdinalIndex.setStatus("current")
_NbsConnectivityDestIfIndex_Type = InterfaceIndex
_NbsConnectivityDestIfIndex_Object = MibTableColumn
nbsConnectivityDestIfIndex = _NbsConnectivityDestIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 20),
    _NbsConnectivityDestIfIndex_Type()
)
nbsConnectivityDestIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestIfIndex.setStatus("current")
_NbsConnectivityDestIPAddress_Type = IpAddress
_NbsConnectivityDestIPAddress_Object = MibTableColumn
nbsConnectivityDestIPAddress = _NbsConnectivityDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 30),
    _NbsConnectivityDestIPAddress_Type()
)
nbsConnectivityDestIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestIPAddress.setStatus("deprecated")
_NbsConnectivityDestAddrType_Type = InetAddressType
_NbsConnectivityDestAddrType_Object = MibTableColumn
nbsConnectivityDestAddrType = _NbsConnectivityDestAddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 40),
    _NbsConnectivityDestAddrType_Type()
)
nbsConnectivityDestAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestAddrType.setStatus("current")
_NbsConnectivityDestAddr_Type = InetAddress
_NbsConnectivityDestAddr_Object = MibTableColumn
nbsConnectivityDestAddr = _NbsConnectivityDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 50),
    _NbsConnectivityDestAddr_Type()
)
nbsConnectivityDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestAddr.setStatus("current")


class _NbsConnectivityStatus_Type(Integer32):
    """Custom type nbsConnectivityStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("destBlocked", 6),
          ("down", 2),
          ("notSupported", 4),
          ("sourceBlocked", 5),
          ("unknown", 3),
          ("up", 1))
    )


_NbsConnectivityStatus_Type.__name__ = "Integer32"
_NbsConnectivityStatus_Object = MibTableColumn
nbsConnectivityStatus = _NbsConnectivityStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 60),
    _NbsConnectivityStatus_Type()
)
nbsConnectivityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityStatus.setStatus("current")
_NbsConnectivityDestV6AddrType_Type = InetAddressType
_NbsConnectivityDestV6AddrType_Object = MibTableColumn
nbsConnectivityDestV6AddrType = _NbsConnectivityDestV6AddrType_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 70),
    _NbsConnectivityDestV6AddrType_Type()
)
nbsConnectivityDestV6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestV6AddrType.setStatus("current")
_NbsConnectivityDestV6Addr_Type = InetAddress
_NbsConnectivityDestV6Addr_Object = MibTableColumn
nbsConnectivityDestV6Addr = _NbsConnectivityDestV6Addr_Object(
    (1, 3, 6, 1, 4, 1, 629, 238, 1, 1, 1, 80),
    _NbsConnectivityDestV6Addr_Type()
)
nbsConnectivityDestV6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsConnectivityDestV6Addr.setStatus("current")
_NbsConnectivityTraps_ObjectIdentity = ObjectIdentity
nbsConnectivityTraps = _NbsConnectivityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 238, 100)
)
if mibBuilder.loadTexts:
    nbsConnectivityTraps.setStatus("current")
_NbsConnectivityEvent_ObjectIdentity = ObjectIdentity
nbsConnectivityEvent = _NbsConnectivityEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 238, 100, 0)
)
if mibBuilder.loadTexts:
    nbsConnectivityEvent.setStatus("current")

# Managed Objects groups


# Notification objects

nbsConnectivityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 238, 100, 0, 10)
)
nbsConnectivityChanged.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddrType"),
        ("NBS-CONNECTIVITY-MIB", "nbsConnectivityDestAddr"),
        ("NBS-CONNECTIVITY-MIB", "nbsConnectivityStatus"))
)
if mibBuilder.loadTexts:
    nbsConnectivityChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-CONNECTIVITY-MIB",
    **{"nbsConnectivityMib": nbsConnectivityMib,
       "nbsConnectivityGrp": nbsConnectivityGrp,
       "nbsConnectivityTable": nbsConnectivityTable,
       "nbsConnectivityEntry": nbsConnectivityEntry,
       "nbsConnectivitySourceIfIndex": nbsConnectivitySourceIfIndex,
       "nbsConnectivityOrdinalIndex": nbsConnectivityOrdinalIndex,
       "nbsConnectivityDestIfIndex": nbsConnectivityDestIfIndex,
       "nbsConnectivityDestIPAddress": nbsConnectivityDestIPAddress,
       "nbsConnectivityDestAddrType": nbsConnectivityDestAddrType,
       "nbsConnectivityDestAddr": nbsConnectivityDestAddr,
       "nbsConnectivityStatus": nbsConnectivityStatus,
       "nbsConnectivityDestV6AddrType": nbsConnectivityDestV6AddrType,
       "nbsConnectivityDestV6Addr": nbsConnectivityDestV6Addr,
       "nbsConnectivityTraps": nbsConnectivityTraps,
       "nbsConnectivityEvent": nbsConnectivityEvent,
       "nbsConnectivityChanged": nbsConnectivityChanged}
)
