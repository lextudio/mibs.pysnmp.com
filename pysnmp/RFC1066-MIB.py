# SNMP MIB module (RFC1066-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1066-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:04 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_ObjectIdentity = ObjectIdentity
mib = _Mib_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_SysDescr_Type = OctetString
_SysDescr_Object = MibScalar
sysDescr = _SysDescr_Object(
    (1, 3, 6, 1, 2, 1, 1, 1),
    _SysDescr_Type()
)
sysDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDescr.setStatus("mandatory")
_SysObjectID_Type = ObjectIdentifier
_SysObjectID_Object = MibScalar
sysObjectID = _SysObjectID_Object(
    (1, 3, 6, 1, 2, 1, 1, 2),
    _SysObjectID_Type()
)
sysObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysObjectID.setStatus("mandatory")
_SysUpTime_Type = TimeTicks
_SysUpTime_Object = MibScalar
sysUpTime = _SysUpTime_Object(
    (1, 3, 6, 1, 2, 1, 1, 3),
    _SysUpTime_Type()
)
sysUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpTime.setStatus("mandatory")
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_IfNumber_Type = Integer32
_IfNumber_Object = MibScalar
ifNumber = _IfNumber_Object(
    (1, 3, 6, 1, 2, 1, 2, 1),
    _IfNumber_Type()
)
ifNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifNumber.setStatus("mandatory")
_IfTable_Object = MibTable
ifTable = _IfTable_Object(
    (1, 3, 6, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ifTable.setStatus("mandatory")
_IfEntry_Object = MibTableRow
ifEntry = _IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")
_IfDescr_Type = OctetString
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("mandatory")


class _IfType_Type(Integer32):
    """Custom type ifType based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("basicIsdn", 20),
          ("cept", 19),
          ("ddn-x25", 4),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("other", 1),
          ("primaryIsdn", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10MBit", 12),
          ("proteon-80MBit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("starLan", 11),
          ("t1-carrier", 18))
    )


_IfType_Type.__name__ = "Integer32"
_IfType_Object = MibTableColumn
ifType = _IfType_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 3),
    _IfType_Type()
)
ifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifType.setStatus("mandatory")
_IfMtu_Type = Integer32
_IfMtu_Object = MibTableColumn
ifMtu = _IfMtu_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 4),
    _IfMtu_Type()
)
ifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifMtu.setStatus("mandatory")
_IfSpeed_Type = Gauge32
_IfSpeed_Object = MibTableColumn
ifSpeed = _IfSpeed_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 5),
    _IfSpeed_Type()
)
ifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpeed.setStatus("mandatory")
_IfPhysAddress_Type = OctetString
_IfPhysAddress_Object = MibTableColumn
ifPhysAddress = _IfPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 6),
    _IfPhysAddress_Type()
)
ifPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysAddress.setStatus("mandatory")


class _IfAdminStatus_Type(Integer32):
    """Custom type ifAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_IfAdminStatus_Type.__name__ = "Integer32"
_IfAdminStatus_Object = MibTableColumn
ifAdminStatus = _IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 7),
    _IfAdminStatus_Type()
)
ifAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifAdminStatus.setStatus("mandatory")


class _IfOperStatus_Type(Integer32):
    """Custom type ifOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_IfOperStatus_Type.__name__ = "Integer32"
_IfOperStatus_Object = MibTableColumn
ifOperStatus = _IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 8),
    _IfOperStatus_Type()
)
ifOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOperStatus.setStatus("mandatory")
_IfLastChange_Type = TimeTicks
_IfLastChange_Object = MibTableColumn
ifLastChange = _IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 9),
    _IfLastChange_Type()
)
ifLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifLastChange.setStatus("mandatory")
_IfInOctets_Type = Counter32
_IfInOctets_Object = MibTableColumn
ifInOctets = _IfInOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 10),
    _IfInOctets_Type()
)
ifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInOctets.setStatus("mandatory")
_IfInUcastPkts_Type = Counter32
_IfInUcastPkts_Object = MibTableColumn
ifInUcastPkts = _IfInUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 11),
    _IfInUcastPkts_Type()
)
ifInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUcastPkts.setStatus("mandatory")
_IfInNUcastPkts_Type = Counter32
_IfInNUcastPkts_Object = MibTableColumn
ifInNUcastPkts = _IfInNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 12),
    _IfInNUcastPkts_Type()
)
ifInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInNUcastPkts.setStatus("mandatory")
_IfInDiscards_Type = Counter32
_IfInDiscards_Object = MibTableColumn
ifInDiscards = _IfInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 13),
    _IfInDiscards_Type()
)
ifInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInDiscards.setStatus("mandatory")
_IfInErrors_Type = Counter32
_IfInErrors_Object = MibTableColumn
ifInErrors = _IfInErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 14),
    _IfInErrors_Type()
)
ifInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInErrors.setStatus("mandatory")
_IfInUnknownProtos_Type = Counter32
_IfInUnknownProtos_Object = MibTableColumn
ifInUnknownProtos = _IfInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 15),
    _IfInUnknownProtos_Type()
)
ifInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifInUnknownProtos.setStatus("mandatory")
_IfOutOctets_Type = Counter32
_IfOutOctets_Object = MibTableColumn
ifOutOctets = _IfOutOctets_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 16),
    _IfOutOctets_Type()
)
ifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutOctets.setStatus("mandatory")
_IfOutUcastPkts_Type = Counter32
_IfOutUcastPkts_Object = MibTableColumn
ifOutUcastPkts = _IfOutUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 17),
    _IfOutUcastPkts_Type()
)
ifOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutUcastPkts.setStatus("mandatory")
_IfOutNUcastPkts_Type = Counter32
_IfOutNUcastPkts_Object = MibTableColumn
ifOutNUcastPkts = _IfOutNUcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 18),
    _IfOutNUcastPkts_Type()
)
ifOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutNUcastPkts.setStatus("mandatory")
_IfOutDiscards_Type = Counter32
_IfOutDiscards_Object = MibTableColumn
ifOutDiscards = _IfOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 19),
    _IfOutDiscards_Type()
)
ifOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutDiscards.setStatus("mandatory")
_IfOutErrors_Type = Counter32
_IfOutErrors_Object = MibTableColumn
ifOutErrors = _IfOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 20),
    _IfOutErrors_Type()
)
ifOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutErrors.setStatus("mandatory")
_IfOutQLen_Type = Gauge32
_IfOutQLen_Object = MibTableColumn
ifOutQLen = _IfOutQLen_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 21),
    _IfOutQLen_Type()
)
ifOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOutQLen.setStatus("mandatory")
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_AtTable_Object = MibTable
atTable = _AtTable_Object(
    (1, 3, 6, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atTable.setStatus("mandatory")
_AtEntry_Object = MibTableRow
atEntry = _AtEntry_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    atEntry.setStatus("mandatory")
_AtIfIndex_Type = Integer32
_AtIfIndex_Object = MibTableColumn
atIfIndex = _AtIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 1),
    _AtIfIndex_Type()
)
atIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atIfIndex.setStatus("mandatory")
_AtPhysAddress_Type = OctetString
_AtPhysAddress_Object = MibTableColumn
atPhysAddress = _AtPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 2),
    _AtPhysAddress_Type()
)
atPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atPhysAddress.setStatus("mandatory")
_AtNetAddress_Type = IpAddress
_AtNetAddress_Object = MibTableColumn
atNetAddress = _AtNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 3),
    _AtNetAddress_Type()
)
atNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetAddress.setStatus("mandatory")
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)


class _IpForwarding_Type(Integer32):
    """Custom type ipForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("gateway", 1),
          ("host", 2))
    )


_IpForwarding_Type.__name__ = "Integer32"
_IpForwarding_Object = MibScalar
ipForwarding = _IpForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 1),
    _IpForwarding_Type()
)
ipForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwarding.setStatus("mandatory")
_IpDefaultTTL_Type = Integer32
_IpDefaultTTL_Object = MibScalar
ipDefaultTTL = _IpDefaultTTL_Object(
    (1, 3, 6, 1, 2, 1, 4, 2),
    _IpDefaultTTL_Type()
)
ipDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultTTL.setStatus("mandatory")
_IpInReceives_Type = Counter32
_IpInReceives_Object = MibScalar
ipInReceives = _IpInReceives_Object(
    (1, 3, 6, 1, 2, 1, 4, 3),
    _IpInReceives_Type()
)
ipInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInReceives.setStatus("mandatory")
_IpInHdrErrors_Type = Counter32
_IpInHdrErrors_Object = MibScalar
ipInHdrErrors = _IpInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 4),
    _IpInHdrErrors_Type()
)
ipInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInHdrErrors.setStatus("mandatory")
_IpInAddrErrors_Type = Counter32
_IpInAddrErrors_Object = MibScalar
ipInAddrErrors = _IpInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 4, 5),
    _IpInAddrErrors_Type()
)
ipInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInAddrErrors.setStatus("mandatory")
_IpForwDatagrams_Type = Counter32
_IpForwDatagrams_Object = MibScalar
ipForwDatagrams = _IpForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 4, 6),
    _IpForwDatagrams_Type()
)
ipForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwDatagrams.setStatus("mandatory")
_IpInUnknownProtos_Type = Counter32
_IpInUnknownProtos_Object = MibScalar
ipInUnknownProtos = _IpInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 4, 7),
    _IpInUnknownProtos_Type()
)
ipInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInUnknownProtos.setStatus("mandatory")
_IpInDiscards_Type = Counter32
_IpInDiscards_Object = MibScalar
ipInDiscards = _IpInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 8),
    _IpInDiscards_Type()
)
ipInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDiscards.setStatus("mandatory")
_IpInDelivers_Type = Counter32
_IpInDelivers_Object = MibScalar
ipInDelivers = _IpInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 4, 9),
    _IpInDelivers_Type()
)
ipInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInDelivers.setStatus("mandatory")
_IpOutRequests_Type = Counter32
_IpOutRequests_Object = MibScalar
ipOutRequests = _IpOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 4, 10),
    _IpOutRequests_Type()
)
ipOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutRequests.setStatus("mandatory")
_IpOutDiscards_Type = Counter32
_IpOutDiscards_Object = MibScalar
ipOutDiscards = _IpOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 11),
    _IpOutDiscards_Type()
)
ipOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutDiscards.setStatus("mandatory")
_IpOutNoRoutes_Type = Counter32
_IpOutNoRoutes_Object = MibScalar
ipOutNoRoutes = _IpOutNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 4, 12),
    _IpOutNoRoutes_Type()
)
ipOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipOutNoRoutes.setStatus("mandatory")
_IpReasmTimeout_Type = Integer32
_IpReasmTimeout_Object = MibScalar
ipReasmTimeout = _IpReasmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 4, 13),
    _IpReasmTimeout_Type()
)
ipReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmTimeout.setStatus("mandatory")
_IpReasmReqds_Type = Counter32
_IpReasmReqds_Object = MibScalar
ipReasmReqds = _IpReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 4, 14),
    _IpReasmReqds_Type()
)
ipReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmReqds.setStatus("mandatory")
_IpReasmOKs_Type = Counter32
_IpReasmOKs_Object = MibScalar
ipReasmOKs = _IpReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 15),
    _IpReasmOKs_Type()
)
ipReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmOKs.setStatus("mandatory")
_IpReasmFails_Type = Counter32
_IpReasmFails_Object = MibScalar
ipReasmFails = _IpReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 16),
    _IpReasmFails_Type()
)
ipReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipReasmFails.setStatus("mandatory")
_IpFragOKs_Type = Counter32
_IpFragOKs_Object = MibScalar
ipFragOKs = _IpFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 4, 17),
    _IpFragOKs_Type()
)
ipFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragOKs.setStatus("mandatory")
_IpFragFails_Type = Counter32
_IpFragFails_Object = MibScalar
ipFragFails = _IpFragFails_Object(
    (1, 3, 6, 1, 2, 1, 4, 18),
    _IpFragFails_Type()
)
ipFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragFails.setStatus("mandatory")
_IpFragCreates_Type = Counter32
_IpFragCreates_Object = MibScalar
ipFragCreates = _IpFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 4, 19),
    _IpFragCreates_Type()
)
ipFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipFragCreates.setStatus("mandatory")
_IpAddrTable_Object = MibTable
ipAddrTable = _IpAddrTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 20)
)
if mibBuilder.loadTexts:
    ipAddrTable.setStatus("mandatory")
_IpAddrEntry_Object = MibTableRow
ipAddrEntry = _IpAddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1)
)
if mibBuilder.loadTexts:
    ipAddrEntry.setStatus("mandatory")
_IpAdEntAddr_Type = IpAddress
_IpAdEntAddr_Object = MibTableColumn
ipAdEntAddr = _IpAdEntAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 1),
    _IpAdEntAddr_Type()
)
ipAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntAddr.setStatus("mandatory")
_IpAdEntIfIndex_Type = Integer32
_IpAdEntIfIndex_Object = MibTableColumn
ipAdEntIfIndex = _IpAdEntIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 2),
    _IpAdEntIfIndex_Type()
)
ipAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntIfIndex.setStatus("mandatory")
_IpAdEntNetMask_Type = IpAddress
_IpAdEntNetMask_Object = MibTableColumn
ipAdEntNetMask = _IpAdEntNetMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 3),
    _IpAdEntNetMask_Type()
)
ipAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntNetMask.setStatus("mandatory")
_IpAdEntBcastAddr_Type = Integer32
_IpAdEntBcastAddr_Object = MibTableColumn
ipAdEntBcastAddr = _IpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 4),
    _IpAdEntBcastAddr_Type()
)
ipAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntBcastAddr.setStatus("mandatory")
_IpRoutingTable_Object = MibTable
ipRoutingTable = _IpRoutingTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 21)
)
if mibBuilder.loadTexts:
    ipRoutingTable.setStatus("mandatory")
_IpRouteEntry_Object = MibTableRow
ipRouteEntry = _IpRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1)
)
if mibBuilder.loadTexts:
    ipRouteEntry.setStatus("mandatory")
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibTableColumn
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 1),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("mandatory")
_IpRouteIfIndex_Type = Integer32
_IpRouteIfIndex_Object = MibTableColumn
ipRouteIfIndex = _IpRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 2),
    _IpRouteIfIndex_Type()
)
ipRouteIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteIfIndex.setStatus("mandatory")
_IpRouteMetric1_Type = Integer32
_IpRouteMetric1_Object = MibTableColumn
ipRouteMetric1 = _IpRouteMetric1_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 3),
    _IpRouteMetric1_Type()
)
ipRouteMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric1.setStatus("mandatory")
_IpRouteMetric2_Type = Integer32
_IpRouteMetric2_Object = MibTableColumn
ipRouteMetric2 = _IpRouteMetric2_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 4),
    _IpRouteMetric2_Type()
)
ipRouteMetric2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric2.setStatus("mandatory")
_IpRouteMetric3_Type = Integer32
_IpRouteMetric3_Object = MibTableColumn
ipRouteMetric3 = _IpRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 5),
    _IpRouteMetric3_Type()
)
ipRouteMetric3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric3.setStatus("mandatory")
_IpRouteMetric4_Type = Integer32
_IpRouteMetric4_Object = MibTableColumn
ipRouteMetric4 = _IpRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 6),
    _IpRouteMetric4_Type()
)
ipRouteMetric4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric4.setStatus("mandatory")
_IpRouteNextHop_Type = IpAddress
_IpRouteNextHop_Object = MibTableColumn
ipRouteNextHop = _IpRouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 7),
    _IpRouteNextHop_Type()
)
ipRouteNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteNextHop.setStatus("mandatory")


class _IpRouteType_Type(Integer32):
    """Custom type ipRouteType based on Integer32"""
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
        *(("direct", 3),
          ("invalid", 2),
          ("other", 1),
          ("remote", 4))
    )


_IpRouteType_Type.__name__ = "Integer32"
_IpRouteType_Object = MibTableColumn
ipRouteType = _IpRouteType_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 8),
    _IpRouteType_Type()
)
ipRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteType.setStatus("mandatory")


class _IpRouteProto_Type(Integer32):
    """Custom type ipRouteProto based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("oigp", 13),
          ("other", 1),
          ("rip", 8))
    )


_IpRouteProto_Type.__name__ = "Integer32"
_IpRouteProto_Object = MibTableColumn
ipRouteProto = _IpRouteProto_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 9),
    _IpRouteProto_Type()
)
ipRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteProto.setStatus("mandatory")
_IpRouteAge_Type = Integer32
_IpRouteAge_Object = MibTableColumn
ipRouteAge = _IpRouteAge_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 10),
    _IpRouteAge_Type()
)
ipRouteAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteAge.setStatus("mandatory")
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_IcmpInMsgs_Type = Counter32
_IcmpInMsgs_Object = MibScalar
icmpInMsgs = _IcmpInMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 1),
    _IcmpInMsgs_Type()
)
icmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInMsgs.setStatus("mandatory")
_IcmpInErrors_Type = Counter32
_IcmpInErrors_Object = MibScalar
icmpInErrors = _IcmpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 2),
    _IcmpInErrors_Type()
)
icmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInErrors.setStatus("mandatory")
_IcmpInDestUnreachs_Type = Counter32
_IcmpInDestUnreachs_Object = MibScalar
icmpInDestUnreachs = _IcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 5, 3),
    _IcmpInDestUnreachs_Type()
)
icmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInDestUnreachs.setStatus("mandatory")
_IcmpInTimeExcds_Type = Counter32
_IcmpInTimeExcds_Object = MibScalar
icmpInTimeExcds = _IcmpInTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 5, 4),
    _IcmpInTimeExcds_Type()
)
icmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimeExcds.setStatus("mandatory")
_IcmpInParmProbs_Type = Counter32
_IcmpInParmProbs_Object = MibScalar
icmpInParmProbs = _IcmpInParmProbs_Object(
    (1, 3, 6, 1, 2, 1, 5, 5),
    _IcmpInParmProbs_Type()
)
icmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInParmProbs.setStatus("mandatory")
_IcmpInSrcQuenchs_Type = Counter32
_IcmpInSrcQuenchs_Object = MibScalar
icmpInSrcQuenchs = _IcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 2, 1, 5, 6),
    _IcmpInSrcQuenchs_Type()
)
icmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInSrcQuenchs.setStatus("mandatory")
_IcmpInRedirects_Type = Counter32
_IcmpInRedirects_Object = MibScalar
icmpInRedirects = _IcmpInRedirects_Object(
    (1, 3, 6, 1, 2, 1, 5, 7),
    _IcmpInRedirects_Type()
)
icmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInRedirects.setStatus("mandatory")
_IcmpInEchos_Type = Counter32
_IcmpInEchos_Object = MibScalar
icmpInEchos = _IcmpInEchos_Object(
    (1, 3, 6, 1, 2, 1, 5, 8),
    _IcmpInEchos_Type()
)
icmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInEchos.setStatus("mandatory")
_IcmpInEchoReps_Type = Counter32
_IcmpInEchoReps_Object = MibScalar
icmpInEchoReps = _IcmpInEchoReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 9),
    _IcmpInEchoReps_Type()
)
icmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInEchoReps.setStatus("mandatory")
_IcmpInTimestamps_Type = Counter32
_IcmpInTimestamps_Object = MibScalar
icmpInTimestamps = _IcmpInTimestamps_Object(
    (1, 3, 6, 1, 2, 1, 5, 10),
    _IcmpInTimestamps_Type()
)
icmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimestamps.setStatus("mandatory")
_IcmpInTimestampReps_Type = Counter32
_IcmpInTimestampReps_Object = MibScalar
icmpInTimestampReps = _IcmpInTimestampReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 11),
    _IcmpInTimestampReps_Type()
)
icmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInTimestampReps.setStatus("mandatory")
_IcmpInAddrMasks_Type = Counter32
_IcmpInAddrMasks_Object = MibScalar
icmpInAddrMasks = _IcmpInAddrMasks_Object(
    (1, 3, 6, 1, 2, 1, 5, 12),
    _IcmpInAddrMasks_Type()
)
icmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInAddrMasks.setStatus("mandatory")
_IcmpInAddrMaskReps_Type = Counter32
_IcmpInAddrMaskReps_Object = MibScalar
icmpInAddrMaskReps = _IcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 13),
    _IcmpInAddrMaskReps_Type()
)
icmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpInAddrMaskReps.setStatus("mandatory")
_IcmpOutMsgs_Type = Counter32
_IcmpOutMsgs_Object = MibScalar
icmpOutMsgs = _IcmpOutMsgs_Object(
    (1, 3, 6, 1, 2, 1, 5, 14),
    _IcmpOutMsgs_Type()
)
icmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutMsgs.setStatus("mandatory")
_IcmpOutErrors_Type = Counter32
_IcmpOutErrors_Object = MibScalar
icmpOutErrors = _IcmpOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 5, 15),
    _IcmpOutErrors_Type()
)
icmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutErrors.setStatus("mandatory")
_IcmpOutDestUnreachs_Type = Counter32
_IcmpOutDestUnreachs_Object = MibScalar
icmpOutDestUnreachs = _IcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 5, 16),
    _IcmpOutDestUnreachs_Type()
)
icmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutDestUnreachs.setStatus("mandatory")
_IcmpOutTimeExcds_Type = Counter32
_IcmpOutTimeExcds_Object = MibScalar
icmpOutTimeExcds = _IcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 5, 17),
    _IcmpOutTimeExcds_Type()
)
icmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimeExcds.setStatus("mandatory")
_IcmpOutParmProbs_Type = Counter32
_IcmpOutParmProbs_Object = MibScalar
icmpOutParmProbs = _IcmpOutParmProbs_Object(
    (1, 3, 6, 1, 2, 1, 5, 18),
    _IcmpOutParmProbs_Type()
)
icmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutParmProbs.setStatus("mandatory")
_IcmpOutSrcQuenchs_Type = Counter32
_IcmpOutSrcQuenchs_Object = MibScalar
icmpOutSrcQuenchs = _IcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 2, 1, 5, 19),
    _IcmpOutSrcQuenchs_Type()
)
icmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutSrcQuenchs.setStatus("mandatory")
_IcmpOutRedirects_Type = Counter32
_IcmpOutRedirects_Object = MibScalar
icmpOutRedirects = _IcmpOutRedirects_Object(
    (1, 3, 6, 1, 2, 1, 5, 20),
    _IcmpOutRedirects_Type()
)
icmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutRedirects.setStatus("mandatory")
_IcmpOutEchos_Type = Counter32
_IcmpOutEchos_Object = MibScalar
icmpOutEchos = _IcmpOutEchos_Object(
    (1, 3, 6, 1, 2, 1, 5, 21),
    _IcmpOutEchos_Type()
)
icmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutEchos.setStatus("mandatory")
_IcmpOutEchoReps_Type = Counter32
_IcmpOutEchoReps_Object = MibScalar
icmpOutEchoReps = _IcmpOutEchoReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 22),
    _IcmpOutEchoReps_Type()
)
icmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutEchoReps.setStatus("mandatory")
_IcmpOutTimestamps_Type = Counter32
_IcmpOutTimestamps_Object = MibScalar
icmpOutTimestamps = _IcmpOutTimestamps_Object(
    (1, 3, 6, 1, 2, 1, 5, 23),
    _IcmpOutTimestamps_Type()
)
icmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimestamps.setStatus("mandatory")
_IcmpOutTimestampReps_Type = Counter32
_IcmpOutTimestampReps_Object = MibScalar
icmpOutTimestampReps = _IcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 24),
    _IcmpOutTimestampReps_Type()
)
icmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutTimestampReps.setStatus("mandatory")
_IcmpOutAddrMasks_Type = Counter32
_IcmpOutAddrMasks_Object = MibScalar
icmpOutAddrMasks = _IcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 2, 1, 5, 25),
    _IcmpOutAddrMasks_Type()
)
icmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutAddrMasks.setStatus("mandatory")
_IcmpOutAddrMaskReps_Type = Counter32
_IcmpOutAddrMaskReps_Object = MibScalar
icmpOutAddrMaskReps = _IcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 2, 1, 5, 26),
    _IcmpOutAddrMaskReps_Type()
)
icmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icmpOutAddrMaskReps.setStatus("mandatory")
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)


class _TcpRtoAlgorithm_Type(Integer32):
    """Custom type tcpRtoAlgorithm based on Integer32"""
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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_TcpRtoAlgorithm_Type.__name__ = "Integer32"
_TcpRtoAlgorithm_Object = MibScalar
tcpRtoAlgorithm = _TcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 2, 1, 6, 1),
    _TcpRtoAlgorithm_Type()
)
tcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoAlgorithm.setStatus("mandatory")
_TcpRtoMin_Type = Integer32
_TcpRtoMin_Object = MibScalar
tcpRtoMin = _TcpRtoMin_Object(
    (1, 3, 6, 1, 2, 1, 6, 2),
    _TcpRtoMin_Type()
)
tcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoMin.setStatus("mandatory")
_TcpRtoMax_Type = Integer32
_TcpRtoMax_Object = MibScalar
tcpRtoMax = _TcpRtoMax_Object(
    (1, 3, 6, 1, 2, 1, 6, 3),
    _TcpRtoMax_Type()
)
tcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRtoMax.setStatus("mandatory")
_TcpMaxConn_Type = Integer32
_TcpMaxConn_Object = MibScalar
tcpMaxConn = _TcpMaxConn_Object(
    (1, 3, 6, 1, 2, 1, 6, 4),
    _TcpMaxConn_Type()
)
tcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpMaxConn.setStatus("mandatory")
_TcpActiveOpens_Type = Counter32
_TcpActiveOpens_Object = MibScalar
tcpActiveOpens = _TcpActiveOpens_Object(
    (1, 3, 6, 1, 2, 1, 6, 5),
    _TcpActiveOpens_Type()
)
tcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpActiveOpens.setStatus("mandatory")
_TcpPassiveOpens_Type = Counter32
_TcpPassiveOpens_Object = MibScalar
tcpPassiveOpens = _TcpPassiveOpens_Object(
    (1, 3, 6, 1, 2, 1, 6, 6),
    _TcpPassiveOpens_Type()
)
tcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpPassiveOpens.setStatus("mandatory")
_TcpAttemptFails_Type = Counter32
_TcpAttemptFails_Object = MibScalar
tcpAttemptFails = _TcpAttemptFails_Object(
    (1, 3, 6, 1, 2, 1, 6, 7),
    _TcpAttemptFails_Type()
)
tcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpAttemptFails.setStatus("mandatory")
_TcpEstabResets_Type = Counter32
_TcpEstabResets_Object = MibScalar
tcpEstabResets = _TcpEstabResets_Object(
    (1, 3, 6, 1, 2, 1, 6, 8),
    _TcpEstabResets_Type()
)
tcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpEstabResets.setStatus("mandatory")
_TcpCurrEstab_Type = Gauge32
_TcpCurrEstab_Object = MibScalar
tcpCurrEstab = _TcpCurrEstab_Object(
    (1, 3, 6, 1, 2, 1, 6, 9),
    _TcpCurrEstab_Type()
)
tcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpCurrEstab.setStatus("mandatory")
_TcpInSegs_Type = Counter32
_TcpInSegs_Object = MibScalar
tcpInSegs = _TcpInSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 10),
    _TcpInSegs_Type()
)
tcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInSegs.setStatus("mandatory")
_TcpOutSegs_Type = Counter32
_TcpOutSegs_Object = MibScalar
tcpOutSegs = _TcpOutSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 11),
    _TcpOutSegs_Type()
)
tcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOutSegs.setStatus("mandatory")
_TcpRetransSegs_Type = Counter32
_TcpRetransSegs_Object = MibScalar
tcpRetransSegs = _TcpRetransSegs_Object(
    (1, 3, 6, 1, 2, 1, 6, 12),
    _TcpRetransSegs_Type()
)
tcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpRetransSegs.setStatus("mandatory")
_TcpConnTable_Object = MibTable
tcpConnTable = _TcpConnTable_Object(
    (1, 3, 6, 1, 2, 1, 6, 13)
)
if mibBuilder.loadTexts:
    tcpConnTable.setStatus("mandatory")
_TcpConnEntry_Object = MibTableRow
tcpConnEntry = _TcpConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1)
)
if mibBuilder.loadTexts:
    tcpConnEntry.setStatus("mandatory")


class _TcpConnState_Type(Integer32):
    """Custom type tcpConnState based on Integer32"""
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
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_TcpConnState_Type.__name__ = "Integer32"
_TcpConnState_Object = MibTableColumn
tcpConnState = _TcpConnState_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 1),
    _TcpConnState_Type()
)
tcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnState.setStatus("mandatory")
_TcpConnLocalAddress_Type = IpAddress
_TcpConnLocalAddress_Object = MibTableColumn
tcpConnLocalAddress = _TcpConnLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 2),
    _TcpConnLocalAddress_Type()
)
tcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnLocalAddress.setStatus("mandatory")


class _TcpConnLocalPort_Type(Integer32):
    """Custom type tcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpConnLocalPort_Type.__name__ = "Integer32"
_TcpConnLocalPort_Object = MibTableColumn
tcpConnLocalPort = _TcpConnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 3),
    _TcpConnLocalPort_Type()
)
tcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnLocalPort.setStatus("mandatory")
_TcpConnRemAddress_Type = IpAddress
_TcpConnRemAddress_Object = MibTableColumn
tcpConnRemAddress = _TcpConnRemAddress_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 4),
    _TcpConnRemAddress_Type()
)
tcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnRemAddress.setStatus("mandatory")


class _TcpConnRemPort_Type(Integer32):
    """Custom type tcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TcpConnRemPort_Type.__name__ = "Integer32"
_TcpConnRemPort_Object = MibTableColumn
tcpConnRemPort = _TcpConnRemPort_Object(
    (1, 3, 6, 1, 2, 1, 6, 13, 1, 5),
    _TcpConnRemPort_Type()
)
tcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpConnRemPort.setStatus("mandatory")
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_UdpInDatagrams_Type = Counter32
_UdpInDatagrams_Object = MibScalar
udpInDatagrams = _UdpInDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 1),
    _UdpInDatagrams_Type()
)
udpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInDatagrams.setStatus("mandatory")
_UdpNoPorts_Type = Counter32
_UdpNoPorts_Object = MibScalar
udpNoPorts = _UdpNoPorts_Object(
    (1, 3, 6, 1, 2, 1, 7, 2),
    _UdpNoPorts_Type()
)
udpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpNoPorts.setStatus("mandatory")
_UdpInErrors_Type = Counter32
_UdpInErrors_Object = MibScalar
udpInErrors = _UdpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 7, 3),
    _UdpInErrors_Type()
)
udpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpInErrors.setStatus("mandatory")
_UdpOutDatagrams_Type = Counter32
_UdpOutDatagrams_Object = MibScalar
udpOutDatagrams = _UdpOutDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 7, 4),
    _UdpOutDatagrams_Type()
)
udpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpOutDatagrams.setStatus("mandatory")
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_EgpInMsgs_Type = Counter32
_EgpInMsgs_Object = MibScalar
egpInMsgs = _EgpInMsgs_Object(
    (1, 3, 6, 1, 2, 1, 8, 1),
    _EgpInMsgs_Type()
)
egpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpInMsgs.setStatus("mandatory")
_EgpInErrors_Type = Counter32
_EgpInErrors_Object = MibScalar
egpInErrors = _EgpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 8, 2),
    _EgpInErrors_Type()
)
egpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpInErrors.setStatus("mandatory")
_EgpOutMsgs_Type = Counter32
_EgpOutMsgs_Object = MibScalar
egpOutMsgs = _EgpOutMsgs_Object(
    (1, 3, 6, 1, 2, 1, 8, 3),
    _EgpOutMsgs_Type()
)
egpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpOutMsgs.setStatus("mandatory")
_EgpOutErrors_Type = Counter32
_EgpOutErrors_Object = MibScalar
egpOutErrors = _EgpOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 8, 4),
    _EgpOutErrors_Type()
)
egpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpOutErrors.setStatus("mandatory")
_EgpNeighTable_Object = MibTable
egpNeighTable = _EgpNeighTable_Object(
    (1, 3, 6, 1, 2, 1, 8, 5)
)
if mibBuilder.loadTexts:
    egpNeighTable.setStatus("mandatory")
_EgpNeighEntry_Object = MibTableRow
egpNeighEntry = _EgpNeighEntry_Object(
    (1, 3, 6, 1, 2, 1, 8, 5, 1)
)
if mibBuilder.loadTexts:
    egpNeighEntry.setStatus("mandatory")


class _EgpNeighState_Type(Integer32):
    """Custom type egpNeighState based on Integer32"""
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
        *(("acquisition", 2),
          ("cease", 5),
          ("down", 3),
          ("idle", 1),
          ("up", 4))
    )


_EgpNeighState_Type.__name__ = "Integer32"
_EgpNeighState_Object = MibTableColumn
egpNeighState = _EgpNeighState_Object(
    (1, 3, 6, 1, 2, 1, 8, 5, 1, 1),
    _EgpNeighState_Type()
)
egpNeighState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpNeighState.setStatus("mandatory")
_EgpNeighAddr_Type = IpAddress
_EgpNeighAddr_Object = MibTableColumn
egpNeighAddr = _EgpNeighAddr_Object(
    (1, 3, 6, 1, 2, 1, 8, 5, 1, 2),
    _EgpNeighAddr_Type()
)
egpNeighAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    egpNeighAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1066-MIB",
    **{"mib": mib,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "interfaces": interfaces,
       "ifNumber": ifNumber,
       "ifTable": ifTable,
       "ifEntry": ifEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifType": ifType,
       "ifMtu": ifMtu,
       "ifSpeed": ifSpeed,
       "ifPhysAddress": ifPhysAddress,
       "ifAdminStatus": ifAdminStatus,
       "ifOperStatus": ifOperStatus,
       "ifLastChange": ifLastChange,
       "ifInOctets": ifInOctets,
       "ifInUcastPkts": ifInUcastPkts,
       "ifInNUcastPkts": ifInNUcastPkts,
       "ifInDiscards": ifInDiscards,
       "ifInErrors": ifInErrors,
       "ifInUnknownProtos": ifInUnknownProtos,
       "ifOutOctets": ifOutOctets,
       "ifOutUcastPkts": ifOutUcastPkts,
       "ifOutNUcastPkts": ifOutNUcastPkts,
       "ifOutDiscards": ifOutDiscards,
       "ifOutErrors": ifOutErrors,
       "ifOutQLen": ifOutQLen,
       "at": at,
       "atTable": atTable,
       "atEntry": atEntry,
       "atIfIndex": atIfIndex,
       "atPhysAddress": atPhysAddress,
       "atNetAddress": atNetAddress,
       "ip": ip,
       "ipForwarding": ipForwarding,
       "ipDefaultTTL": ipDefaultTTL,
       "ipInReceives": ipInReceives,
       "ipInHdrErrors": ipInHdrErrors,
       "ipInAddrErrors": ipInAddrErrors,
       "ipForwDatagrams": ipForwDatagrams,
       "ipInUnknownProtos": ipInUnknownProtos,
       "ipInDiscards": ipInDiscards,
       "ipInDelivers": ipInDelivers,
       "ipOutRequests": ipOutRequests,
       "ipOutDiscards": ipOutDiscards,
       "ipOutNoRoutes": ipOutNoRoutes,
       "ipReasmTimeout": ipReasmTimeout,
       "ipReasmReqds": ipReasmReqds,
       "ipReasmOKs": ipReasmOKs,
       "ipReasmFails": ipReasmFails,
       "ipFragOKs": ipFragOKs,
       "ipFragFails": ipFragFails,
       "ipFragCreates": ipFragCreates,
       "ipAddrTable": ipAddrTable,
       "ipAddrEntry": ipAddrEntry,
       "ipAdEntAddr": ipAdEntAddr,
       "ipAdEntIfIndex": ipAdEntIfIndex,
       "ipAdEntNetMask": ipAdEntNetMask,
       "ipAdEntBcastAddr": ipAdEntBcastAddr,
       "ipRoutingTable": ipRoutingTable,
       "ipRouteEntry": ipRouteEntry,
       "ipRouteDest": ipRouteDest,
       "ipRouteIfIndex": ipRouteIfIndex,
       "ipRouteMetric1": ipRouteMetric1,
       "ipRouteMetric2": ipRouteMetric2,
       "ipRouteMetric3": ipRouteMetric3,
       "ipRouteMetric4": ipRouteMetric4,
       "ipRouteNextHop": ipRouteNextHop,
       "ipRouteType": ipRouteType,
       "ipRouteProto": ipRouteProto,
       "ipRouteAge": ipRouteAge,
       "icmp": icmp,
       "icmpInMsgs": icmpInMsgs,
       "icmpInErrors": icmpInErrors,
       "icmpInDestUnreachs": icmpInDestUnreachs,
       "icmpInTimeExcds": icmpInTimeExcds,
       "icmpInParmProbs": icmpInParmProbs,
       "icmpInSrcQuenchs": icmpInSrcQuenchs,
       "icmpInRedirects": icmpInRedirects,
       "icmpInEchos": icmpInEchos,
       "icmpInEchoReps": icmpInEchoReps,
       "icmpInTimestamps": icmpInTimestamps,
       "icmpInTimestampReps": icmpInTimestampReps,
       "icmpInAddrMasks": icmpInAddrMasks,
       "icmpInAddrMaskReps": icmpInAddrMaskReps,
       "icmpOutMsgs": icmpOutMsgs,
       "icmpOutErrors": icmpOutErrors,
       "icmpOutDestUnreachs": icmpOutDestUnreachs,
       "icmpOutTimeExcds": icmpOutTimeExcds,
       "icmpOutParmProbs": icmpOutParmProbs,
       "icmpOutSrcQuenchs": icmpOutSrcQuenchs,
       "icmpOutRedirects": icmpOutRedirects,
       "icmpOutEchos": icmpOutEchos,
       "icmpOutEchoReps": icmpOutEchoReps,
       "icmpOutTimestamps": icmpOutTimestamps,
       "icmpOutTimestampReps": icmpOutTimestampReps,
       "icmpOutAddrMasks": icmpOutAddrMasks,
       "icmpOutAddrMaskReps": icmpOutAddrMaskReps,
       "tcp": tcp,
       "tcpRtoAlgorithm": tcpRtoAlgorithm,
       "tcpRtoMin": tcpRtoMin,
       "tcpRtoMax": tcpRtoMax,
       "tcpMaxConn": tcpMaxConn,
       "tcpActiveOpens": tcpActiveOpens,
       "tcpPassiveOpens": tcpPassiveOpens,
       "tcpAttemptFails": tcpAttemptFails,
       "tcpEstabResets": tcpEstabResets,
       "tcpCurrEstab": tcpCurrEstab,
       "tcpInSegs": tcpInSegs,
       "tcpOutSegs": tcpOutSegs,
       "tcpRetransSegs": tcpRetransSegs,
       "tcpConnTable": tcpConnTable,
       "tcpConnEntry": tcpConnEntry,
       "tcpConnState": tcpConnState,
       "tcpConnLocalAddress": tcpConnLocalAddress,
       "tcpConnLocalPort": tcpConnLocalPort,
       "tcpConnRemAddress": tcpConnRemAddress,
       "tcpConnRemPort": tcpConnRemPort,
       "udp": udp,
       "udpInDatagrams": udpInDatagrams,
       "udpNoPorts": udpNoPorts,
       "udpInErrors": udpInErrors,
       "udpOutDatagrams": udpOutDatagrams,
       "egp": egp,
       "egpInMsgs": egpInMsgs,
       "egpInErrors": egpInErrors,
       "egpOutMsgs": egpOutMsgs,
       "egpOutErrors": egpOutErrors,
       "egpNeighTable": egpNeighTable,
       "egpNeighEntry": egpNeighEntry,
       "egpNeighState": egpNeighState,
       "egpNeighAddr": egpNeighAddr}
)
