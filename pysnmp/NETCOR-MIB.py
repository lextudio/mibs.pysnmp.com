# SNMP MIB module (NETCOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETCOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:43 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)


class _SysDescr_Type(DisplayString):
    """Custom type sysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysDescr_Type.__name__ = "DisplayString"
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


class _SysContact_Type(DisplayString):
    """Custom type sysContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysContact_Type.__name__ = "DisplayString"
_SysContact_Object = MibScalar
sysContact = _SysContact_Object(
    (1, 3, 6, 1, 2, 1, 1, 4),
    _SysContact_Type()
)
sysContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysContact.setStatus("mandatory")


class _SysName_Type(DisplayString):
    """Custom type sysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysName_Type.__name__ = "DisplayString"
_SysName_Object = MibScalar
sysName = _SysName_Object(
    (1, 3, 6, 1, 2, 1, 1, 5),
    _SysName_Type()
)
sysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysName.setStatus("mandatory")


class _SysLocation_Type(DisplayString):
    """Custom type sysLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysLocation_Type.__name__ = "DisplayString"
_SysLocation_Object = MibScalar
sysLocation = _SysLocation_Object(
    (1, 3, 6, 1, 2, 1, 1, 6),
    _SysLocation_Type()
)
sysLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocation.setStatus("mandatory")


class _SysServices_Type(Integer32):
    """Custom type sysServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SysServices_Type.__name__ = "Integer32"
_SysServices_Object = MibScalar
sysServices = _SysServices_Object(
    (1, 3, 6, 1, 2, 1, 1, 7),
    _SysServices_Type()
)
sysServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysServices.setStatus("mandatory")
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
ifEntry.setIndexNames(
    (0, "NETCOR-MIB", "ifIndex"),
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


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
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
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("basicISDN", 20),
          ("ddn-x25", 4),
          ("ds1", 18),
          ("ds3", 30),
          ("e1", 19),
          ("eon", 25),
          ("ethernet-3Mbit", 26),
          ("ethernet-csmacd", 6),
          ("fddi", 15),
          ("frame-relay", 32),
          ("hdh1822", 3),
          ("hyperchannel", 14),
          ("iso88023-csmacd", 7),
          ("iso88024-tokenBus", 8),
          ("iso88025-tokenRing", 9),
          ("iso88026-man", 10),
          ("lapb", 16),
          ("nsip", 27),
          ("other", 1),
          ("ppp", 23),
          ("primaryISDN", 21),
          ("propPointToPointSerial", 22),
          ("proteon-10Mbit", 12),
          ("proteon-80Mbit", 13),
          ("regular1822", 2),
          ("rfc877-x25", 5),
          ("sdlc", 17),
          ("sip", 31),
          ("slip", 28),
          ("softwareLoopback", 24),
          ("starLan", 11),
          ("ultra", 29))
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
_IfPhysAddress_Type = PhysAddress
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
_IfSpecific_Type = ObjectIdentifier
_IfSpecific_Object = MibTableColumn
ifSpecific = _IfSpecific_Object(
    (1, 3, 6, 1, 2, 1, 2, 2, 1, 22),
    _IfSpecific_Type()
)
ifSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifSpecific.setStatus("mandatory")
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_AtTable_Object = MibTable
atTable = _AtTable_Object(
    (1, 3, 6, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    atTable.setStatus("deprecated")
_AtEntry_Object = MibTableRow
atEntry = _AtEntry_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1)
)
atEntry.setIndexNames(
    (0, "NETCOR-MIB", "atIfIndex"),
    (0, "NETCOR-MIB", "atNetAddress"),
)
if mibBuilder.loadTexts:
    atEntry.setStatus("deprecated")
_AtIfIndex_Type = Integer32
_AtIfIndex_Object = MibTableColumn
atIfIndex = _AtIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 1),
    _AtIfIndex_Type()
)
atIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atIfIndex.setStatus("deprecated")
_AtPhysAddress_Type = PhysAddress
_AtPhysAddress_Object = MibTableColumn
atPhysAddress = _AtPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 2),
    _AtPhysAddress_Type()
)
atPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atPhysAddress.setStatus("deprecated")
_AtNetAddress_Type = IpAddress
_AtNetAddress_Object = MibTableColumn
atNetAddress = _AtNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 3),
    _AtNetAddress_Type()
)
atNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atNetAddress.setStatus("deprecated")
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
        *(("host", 2),
          ("hub", 1))
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
ipAddrEntry.setIndexNames(
    (0, "NETCOR-MIB", "ipAdEntAddr"),
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


class _IpAdEntReasmMaxSiz_Type(Integer32):
    """Custom type ipAdEntReasmMaxSiz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpAdEntReasmMaxSiz_Type.__name__ = "Integer32"
_IpAdEntReasmMaxSiz_Object = MibTableColumn
ipAdEntReasmMaxSiz = _IpAdEntReasmMaxSiz_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 5),
    _IpAdEntReasmMaxSiz_Type()
)
ipAdEntReasmMaxSiz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntReasmMaxSiz.setStatus("mandatory")
_IpRouteTable_Object = MibTable
ipRouteTable = _IpRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 21)
)
if mibBuilder.loadTexts:
    ipRouteTable.setStatus("mandatory")
_IpRouteEntry_Object = MibTableRow
ipRouteEntry = _IpRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1)
)
ipRouteEntry.setIndexNames(
    (0, "NETCOR-MIB", "ipRouteDest"),
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
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bbnSpfIgp", 12),
          ("bgp", 14),
          ("ciscoIgrp", 11),
          ("egp", 5),
          ("es-is", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("is-is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
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
_IpRouteMask_Type = IpAddress
_IpRouteMask_Object = MibTableColumn
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 11),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("mandatory")
_IpRouteMetric5_Type = Integer32
_IpRouteMetric5_Object = MibTableColumn
ipRouteMetric5 = _IpRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 12),
    _IpRouteMetric5_Type()
)
ipRouteMetric5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouteMetric5.setStatus("mandatory")
_IpRouteInfo_Type = ObjectIdentifier
_IpRouteInfo_Object = MibTableColumn
ipRouteInfo = _IpRouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 13),
    _IpRouteInfo_Type()
)
ipRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteInfo.setStatus("mandatory")
_IpNetToMediaTable_Object = MibTable
ipNetToMediaTable = _IpNetToMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 4, 22)
)
if mibBuilder.loadTexts:
    ipNetToMediaTable.setStatus("mandatory")
_IpNetToMediaEntry_Object = MibTableRow
ipNetToMediaEntry = _IpNetToMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1)
)
ipNetToMediaEntry.setIndexNames(
    (0, "NETCOR-MIB", "ipNetToMediaIfIndex"),
    (0, "NETCOR-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipNetToMediaEntry.setStatus("mandatory")
_IpNetToMediaIfIndex_Type = Integer32
_IpNetToMediaIfIndex_Object = MibTableColumn
ipNetToMediaIfIndex = _IpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 1),
    _IpNetToMediaIfIndex_Type()
)
ipNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetToMediaIfIndex.setStatus("mandatory")
_IpNetToMediaPhysAddress_Type = PhysAddress
_IpNetToMediaPhysAddress_Object = MibTableColumn
ipNetToMediaPhysAddress = _IpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 2),
    _IpNetToMediaPhysAddress_Type()
)
ipNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPhysAddress.setStatus("mandatory")
_IpNetToMediaNetAddress_Type = IpAddress
_IpNetToMediaNetAddress_Object = MibTableColumn
ipNetToMediaNetAddress = _IpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 3),
    _IpNetToMediaNetAddress_Type()
)
ipNetToMediaNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaNetAddress.setStatus("mandatory")


class _IpNetToMediaType_Type(Integer32):
    """Custom type ipNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_IpNetToMediaType_Type.__name__ = "Integer32"
_IpNetToMediaType_Object = MibTableColumn
ipNetToMediaType = _IpNetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 4),
    _IpNetToMediaType_Type()
)
ipNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaType.setStatus("mandatory")
_IpRoutingDiscards_Type = Counter32
_IpRoutingDiscards_Object = MibScalar
ipRoutingDiscards = _IpRoutingDiscards_Object(
    (1, 3, 6, 1, 2, 1, 4, 23),
    _IpRoutingDiscards_Type()
)
ipRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRoutingDiscards.setStatus("mandatory")
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
_UdpTable_Object = MibTable
udpTable = _UdpTable_Object(
    (1, 3, 6, 1, 2, 1, 7, 5)
)
if mibBuilder.loadTexts:
    udpTable.setStatus("mandatory")
_UdpEntry_Object = MibTableRow
udpEntry = _UdpEntry_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1)
)
udpEntry.setIndexNames(
    (0, "NETCOR-MIB", "udpLocalAddress"),
    (0, "NETCOR-MIB", "udpLocalPort"),
)
if mibBuilder.loadTexts:
    udpEntry.setStatus("mandatory")
_UdpLocalAddress_Type = IpAddress
_UdpLocalAddress_Object = MibTableColumn
udpLocalAddress = _UdpLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1, 1),
    _UdpLocalAddress_Type()
)
udpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLocalAddress.setStatus("mandatory")


class _UdpLocalPort_Type(Integer32):
    """Custom type udpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UdpLocalPort_Type.__name__ = "Integer32"
_UdpLocalPort_Object = MibTableColumn
udpLocalPort = _UdpLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 7, 5, 1, 2),
    _UdpLocalPort_Type()
)
udpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    udpLocalPort.setStatus("mandatory")
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_SnmpInPkts_Type = Counter32
_SnmpInPkts_Object = MibScalar
snmpInPkts = _SnmpInPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 1),
    _SnmpInPkts_Type()
)
snmpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInPkts.setStatus("mandatory")
_SnmpOutPkts_Type = Counter32
_SnmpOutPkts_Object = MibScalar
snmpOutPkts = _SnmpOutPkts_Object(
    (1, 3, 6, 1, 2, 1, 11, 2),
    _SnmpOutPkts_Type()
)
snmpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutPkts.setStatus("mandatory")
_SnmpInBadVersions_Type = Counter32
_SnmpInBadVersions_Object = MibScalar
snmpInBadVersions = _SnmpInBadVersions_Object(
    (1, 3, 6, 1, 2, 1, 11, 3),
    _SnmpInBadVersions_Type()
)
snmpInBadVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadVersions.setStatus("mandatory")
_SnmpInBadCommunityNames_Type = Counter32
_SnmpInBadCommunityNames_Object = MibScalar
snmpInBadCommunityNames = _SnmpInBadCommunityNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 4),
    _SnmpInBadCommunityNames_Type()
)
snmpInBadCommunityNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityNames.setStatus("mandatory")
_SnmpInBadCommunityUses_Type = Counter32
_SnmpInBadCommunityUses_Object = MibScalar
snmpInBadCommunityUses = _SnmpInBadCommunityUses_Object(
    (1, 3, 6, 1, 2, 1, 11, 5),
    _SnmpInBadCommunityUses_Type()
)
snmpInBadCommunityUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadCommunityUses.setStatus("mandatory")
_SnmpInASNParseErrs_Type = Counter32
_SnmpInASNParseErrs_Object = MibScalar
snmpInASNParseErrs = _SnmpInASNParseErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 6),
    _SnmpInASNParseErrs_Type()
)
snmpInASNParseErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInASNParseErrs.setStatus("mandatory")
_SnmpInTooBigs_Type = Counter32
_SnmpInTooBigs_Object = MibScalar
snmpInTooBigs = _SnmpInTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 8),
    _SnmpInTooBigs_Type()
)
snmpInTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTooBigs.setStatus("mandatory")
_SnmpInNoSuchNames_Type = Counter32
_SnmpInNoSuchNames_Object = MibScalar
snmpInNoSuchNames = _SnmpInNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 9),
    _SnmpInNoSuchNames_Type()
)
snmpInNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInNoSuchNames.setStatus("mandatory")
_SnmpInBadValues_Type = Counter32
_SnmpInBadValues_Object = MibScalar
snmpInBadValues = _SnmpInBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 10),
    _SnmpInBadValues_Type()
)
snmpInBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInBadValues.setStatus("mandatory")
_SnmpInReadOnlys_Type = Counter32
_SnmpInReadOnlys_Object = MibScalar
snmpInReadOnlys = _SnmpInReadOnlys_Object(
    (1, 3, 6, 1, 2, 1, 11, 11),
    _SnmpInReadOnlys_Type()
)
snmpInReadOnlys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInReadOnlys.setStatus("mandatory")
_SnmpInGenErrs_Type = Counter32
_SnmpInGenErrs_Object = MibScalar
snmpInGenErrs = _SnmpInGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 12),
    _SnmpInGenErrs_Type()
)
snmpInGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGenErrs.setStatus("mandatory")
_SnmpInTotalReqVars_Type = Counter32
_SnmpInTotalReqVars_Object = MibScalar
snmpInTotalReqVars = _SnmpInTotalReqVars_Object(
    (1, 3, 6, 1, 2, 1, 11, 13),
    _SnmpInTotalReqVars_Type()
)
snmpInTotalReqVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTotalReqVars.setStatus("mandatory")
_SnmpInTotalSetVars_Type = Counter32
_SnmpInTotalSetVars_Object = MibScalar
snmpInTotalSetVars = _SnmpInTotalSetVars_Object(
    (1, 3, 6, 1, 2, 1, 11, 14),
    _SnmpInTotalSetVars_Type()
)
snmpInTotalSetVars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTotalSetVars.setStatus("mandatory")
_SnmpInGetRequests_Type = Counter32
_SnmpInGetRequests_Object = MibScalar
snmpInGetRequests = _SnmpInGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 15),
    _SnmpInGetRequests_Type()
)
snmpInGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetRequests.setStatus("mandatory")
_SnmpInGetNexts_Type = Counter32
_SnmpInGetNexts_Object = MibScalar
snmpInGetNexts = _SnmpInGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 16),
    _SnmpInGetNexts_Type()
)
snmpInGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetNexts.setStatus("mandatory")
_SnmpInSetRequests_Type = Counter32
_SnmpInSetRequests_Object = MibScalar
snmpInSetRequests = _SnmpInSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 17),
    _SnmpInSetRequests_Type()
)
snmpInSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInSetRequests.setStatus("mandatory")
_SnmpInGetResponses_Type = Counter32
_SnmpInGetResponses_Object = MibScalar
snmpInGetResponses = _SnmpInGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 18),
    _SnmpInGetResponses_Type()
)
snmpInGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInGetResponses.setStatus("mandatory")
_SnmpInTraps_Type = Counter32
_SnmpInTraps_Object = MibScalar
snmpInTraps = _SnmpInTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 19),
    _SnmpInTraps_Type()
)
snmpInTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpInTraps.setStatus("mandatory")
_SnmpOutTooBigs_Type = Counter32
_SnmpOutTooBigs_Object = MibScalar
snmpOutTooBigs = _SnmpOutTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 11, 20),
    _SnmpOutTooBigs_Type()
)
snmpOutTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTooBigs.setStatus("mandatory")
_SnmpOutNoSuchNames_Type = Counter32
_SnmpOutNoSuchNames_Object = MibScalar
snmpOutNoSuchNames = _SnmpOutNoSuchNames_Object(
    (1, 3, 6, 1, 2, 1, 11, 21),
    _SnmpOutNoSuchNames_Type()
)
snmpOutNoSuchNames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutNoSuchNames.setStatus("mandatory")
_SnmpOutBadValues_Type = Counter32
_SnmpOutBadValues_Object = MibScalar
snmpOutBadValues = _SnmpOutBadValues_Object(
    (1, 3, 6, 1, 2, 1, 11, 22),
    _SnmpOutBadValues_Type()
)
snmpOutBadValues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutBadValues.setStatus("mandatory")
_SnmpOutGenErrs_Type = Counter32
_SnmpOutGenErrs_Object = MibScalar
snmpOutGenErrs = _SnmpOutGenErrs_Object(
    (1, 3, 6, 1, 2, 1, 11, 24),
    _SnmpOutGenErrs_Type()
)
snmpOutGenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGenErrs.setStatus("mandatory")
_SnmpOutGetRequests_Type = Counter32
_SnmpOutGetRequests_Object = MibScalar
snmpOutGetRequests = _SnmpOutGetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 25),
    _SnmpOutGetRequests_Type()
)
snmpOutGetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetRequests.setStatus("mandatory")
_SnmpOutGetNexts_Type = Counter32
_SnmpOutGetNexts_Object = MibScalar
snmpOutGetNexts = _SnmpOutGetNexts_Object(
    (1, 3, 6, 1, 2, 1, 11, 26),
    _SnmpOutGetNexts_Type()
)
snmpOutGetNexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetNexts.setStatus("mandatory")
_SnmpOutSetRequests_Type = Counter32
_SnmpOutSetRequests_Object = MibScalar
snmpOutSetRequests = _SnmpOutSetRequests_Object(
    (1, 3, 6, 1, 2, 1, 11, 27),
    _SnmpOutSetRequests_Type()
)
snmpOutSetRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutSetRequests.setStatus("mandatory")
_SnmpOutGetResponses_Type = Counter32
_SnmpOutGetResponses_Object = MibScalar
snmpOutGetResponses = _SnmpOutGetResponses_Object(
    (1, 3, 6, 1, 2, 1, 11, 28),
    _SnmpOutGetResponses_Type()
)
snmpOutGetResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutGetResponses.setStatus("mandatory")
_SnmpOutTraps_Type = Counter32
_SnmpOutTraps_Object = MibScalar
snmpOutTraps = _SnmpOutTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 29),
    _SnmpOutTraps_Type()
)
snmpOutTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpOutTraps.setStatus("mandatory")


class _SnmpEnableAuthenTraps_Type(Integer32):
    """Custom type snmpEnableAuthenTraps based on Integer32"""
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


_SnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_SnmpEnableAuthenTraps_Object = MibScalar
snmpEnableAuthenTraps = _SnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 2, 1, 11, 30),
    _SnmpEnableAuthenTraps_Type()
)
snmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpEnableAuthenTraps.setStatus("mandatory")
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Netcor_ObjectIdentity = ObjectIdentity
netcor = _Netcor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 329)
)
_Nc007_ObjectIdentity = ObjectIdentity
nc007 = _Nc007_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 329, 1)
)
_NetcorResetBox_Type = Integer32
_NetcorResetBox_Object = MibScalar
netcorResetBox = _NetcorResetBox_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 1),
    _NetcorResetBox_Type()
)
netcorResetBox.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorResetBox.setStatus("mandatory")
_NetcorDsLnkTst_Type = Integer32
_NetcorDsLnkTst_Object = MibScalar
netcorDsLnkTst = _NetcorDsLnkTst_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 2),
    _NetcorDsLnkTst_Type()
)
netcorDsLnkTst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorDsLnkTst.setStatus("mandatory")
_NetcorEnLnkTst_Type = Integer32
_NetcorEnLnkTst_Object = MibScalar
netcorEnLnkTst = _NetcorEnLnkTst_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 3),
    _NetcorEnLnkTst_Type()
)
netcorEnLnkTst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorEnLnkTst.setStatus("mandatory")
_NetcorLnkTstStat_Type = Integer32
_NetcorLnkTstStat_Object = MibScalar
netcorLnkTstStat = _NetcorLnkTstStat_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 4),
    _NetcorLnkTstStat_Type()
)
netcorLnkTstStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcorLnkTstStat.setStatus("mandatory")
_NetcorDsAutRxPolRev_Type = Integer32
_NetcorDsAutRxPolRev_Object = MibScalar
netcorDsAutRxPolRev = _NetcorDsAutRxPolRev_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 5),
    _NetcorDsAutRxPolRev_Type()
)
netcorDsAutRxPolRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorDsAutRxPolRev.setStatus("mandatory")
_NetcorEnAutRxPolRev_Type = Integer32
_NetcorEnAutRxPolRev_Object = MibScalar
netcorEnAutRxPolRev = _NetcorEnAutRxPolRev_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 6),
    _NetcorEnAutRxPolRev_Type()
)
netcorEnAutRxPolRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorEnAutRxPolRev.setStatus("mandatory")
_NetcorPolarityStat_Type = Integer32
_NetcorPolarityStat_Object = MibScalar
netcorPolarityStat = _NetcorPolarityStat_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 7),
    _NetcorPolarityStat_Type()
)
netcorPolarityStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcorPolarityStat.setStatus("mandatory")
_NetcorAltRecntAlg_Type = Integer32
_NetcorAltRecntAlg_Object = MibScalar
netcorAltRecntAlg = _NetcorAltRecntAlg_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 8),
    _NetcorAltRecntAlg_Type()
)
netcorAltRecntAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorAltRecntAlg.setStatus("mandatory")
_NetcorPartitionStat_Type = Integer32
_NetcorPartitionStat_Object = MibScalar
netcorPartitionStat = _NetcorPartitionStat_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 9),
    _NetcorPartitionStat_Type()
)
netcorPartitionStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netcorPartitionStat.setStatus("mandatory")
_NetcorPortDisable_Type = Integer32
_NetcorPortDisable_Object = MibScalar
netcorPortDisable = _NetcorPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 10),
    _NetcorPortDisable_Type()
)
netcorPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorPortDisable.setStatus("mandatory")
_NetcorPortEnable_Type = Integer32
_NetcorPortEnable_Object = MibScalar
netcorPortEnable = _NetcorPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 329, 1, 11),
    _NetcorPortEnable_Type()
)
netcorPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netcorPortEnable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETCOR-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "internet": internet,
       "mgmt": mgmt,
       "mib-2": mib_2,
       "system": system,
       "sysDescr": sysDescr,
       "sysObjectID": sysObjectID,
       "sysUpTime": sysUpTime,
       "sysContact": sysContact,
       "sysName": sysName,
       "sysLocation": sysLocation,
       "sysServices": sysServices,
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
       "ifSpecific": ifSpecific,
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
       "ipAdEntReasmMaxSiz": ipAdEntReasmMaxSiz,
       "ipRouteTable": ipRouteTable,
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
       "ipRouteMask": ipRouteMask,
       "ipRouteMetric5": ipRouteMetric5,
       "ipRouteInfo": ipRouteInfo,
       "ipNetToMediaTable": ipNetToMediaTable,
       "ipNetToMediaEntry": ipNetToMediaEntry,
       "ipNetToMediaIfIndex": ipNetToMediaIfIndex,
       "ipNetToMediaPhysAddress": ipNetToMediaPhysAddress,
       "ipNetToMediaNetAddress": ipNetToMediaNetAddress,
       "ipNetToMediaType": ipNetToMediaType,
       "ipRoutingDiscards": ipRoutingDiscards,
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
       "udp": udp,
       "udpInDatagrams": udpInDatagrams,
       "udpNoPorts": udpNoPorts,
       "udpInErrors": udpInErrors,
       "udpOutDatagrams": udpOutDatagrams,
       "udpTable": udpTable,
       "udpEntry": udpEntry,
       "udpLocalAddress": udpLocalAddress,
       "udpLocalPort": udpLocalPort,
       "egp": egp,
       "transmission": transmission,
       "snmp": snmp,
       "snmpInPkts": snmpInPkts,
       "snmpOutPkts": snmpOutPkts,
       "snmpInBadVersions": snmpInBadVersions,
       "snmpInBadCommunityNames": snmpInBadCommunityNames,
       "snmpInBadCommunityUses": snmpInBadCommunityUses,
       "snmpInASNParseErrs": snmpInASNParseErrs,
       "snmpInTooBigs": snmpInTooBigs,
       "snmpInNoSuchNames": snmpInNoSuchNames,
       "snmpInBadValues": snmpInBadValues,
       "snmpInReadOnlys": snmpInReadOnlys,
       "snmpInGenErrs": snmpInGenErrs,
       "snmpInTotalReqVars": snmpInTotalReqVars,
       "snmpInTotalSetVars": snmpInTotalSetVars,
       "snmpInGetRequests": snmpInGetRequests,
       "snmpInGetNexts": snmpInGetNexts,
       "snmpInSetRequests": snmpInSetRequests,
       "snmpInGetResponses": snmpInGetResponses,
       "snmpInTraps": snmpInTraps,
       "snmpOutTooBigs": snmpOutTooBigs,
       "snmpOutNoSuchNames": snmpOutNoSuchNames,
       "snmpOutBadValues": snmpOutBadValues,
       "snmpOutGenErrs": snmpOutGenErrs,
       "snmpOutGetRequests": snmpOutGetRequests,
       "snmpOutGetNexts": snmpOutGetNexts,
       "snmpOutSetRequests": snmpOutSetRequests,
       "snmpOutGetResponses": snmpOutGetResponses,
       "snmpOutTraps": snmpOutTraps,
       "snmpEnableAuthenTraps": snmpEnableAuthenTraps,
       "private": private,
       "enterprises": enterprises,
       "netcor": netcor,
       "nc007": nc007,
       "netcorResetBox": netcorResetBox,
       "netcorDsLnkTst": netcorDsLnkTst,
       "netcorEnLnkTst": netcorEnLnkTst,
       "netcorLnkTstStat": netcorLnkTstStat,
       "netcorDsAutRxPolRev": netcorDsAutRxPolRev,
       "netcorEnAutRxPolRev": netcorEnAutRxPolRev,
       "netcorPolarityStat": netcorPolarityStat,
       "netcorAltRecntAlg": netcorAltRecntAlg,
       "netcorPartitionStat": netcorPartitionStat,
       "netcorPortDisable": netcorPortDisable,
       "netcorPortEnable": netcorPortEnable}
)
