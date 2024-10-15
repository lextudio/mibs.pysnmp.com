# SNMP MIB module (LIVINGSTON-SNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LIVINGSTON-SNMP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:18:29 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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
    (0, "LIVINGSTON-SNMP", "ifIndex"),
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
    (0, "LIVINGSTON-SNMP", "atIfIndex"),
    (0, "LIVINGSTON-SNMP", "atNetAddress"),
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
atNetAddress.setMaxAccess("read-only")
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
        *(("forwarding", 1),
          ("not-forwarding", 2))
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
ipDefaultTTL.setMaxAccess("read-only")
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
    (0, "LIVINGSTON-SNMP", "ipAdEntAddr"),
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


class _IpAdEntReasmMaxSize_Type(Integer32):
    """Custom type ipAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_IpAdEntReasmMaxSize_Object = MibTableColumn
ipAdEntReasmMaxSize = _IpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 4, 20, 1, 5),
    _IpAdEntReasmMaxSize_Type()
)
ipAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAdEntReasmMaxSize.setStatus("mandatory")
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
    (0, "LIVINGSTON-SNMP", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    ipRouteEntry.setStatus("mandatory")
_IpRouteDest_Type = IpAddress
_IpRouteDest_Object = MibTableColumn
ipRouteDest = _IpRouteDest_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 1),
    _IpRouteDest_Type()
)
ipRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteDest.setStatus("mandatory")
_IpRouteIfIndex_Type = Integer32
_IpRouteIfIndex_Object = MibTableColumn
ipRouteIfIndex = _IpRouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 2),
    _IpRouteIfIndex_Type()
)
ipRouteIfIndex.setMaxAccess("read-only")
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
ipRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteMetric2.setStatus("mandatory")
_IpRouteMetric3_Type = Integer32
_IpRouteMetric3_Object = MibTableColumn
ipRouteMetric3 = _IpRouteMetric3_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 5),
    _IpRouteMetric3_Type()
)
ipRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteMetric3.setStatus("mandatory")
_IpRouteMetric4_Type = Integer32
_IpRouteMetric4_Object = MibTableColumn
ipRouteMetric4 = _IpRouteMetric4_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 6),
    _IpRouteMetric4_Type()
)
ipRouteMetric4.setMaxAccess("read-only")
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
ipRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteAge.setStatus("mandatory")
_IpRouteMask_Type = IpAddress
_IpRouteMask_Object = MibTableColumn
ipRouteMask = _IpRouteMask_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 11),
    _IpRouteMask_Type()
)
ipRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRouteMask.setStatus("mandatory")
_IpRouteMetric5_Type = Integer32
_IpRouteMetric5_Object = MibTableColumn
ipRouteMetric5 = _IpRouteMetric5_Object(
    (1, 3, 6, 1, 2, 1, 4, 21, 1, 12),
    _IpRouteMetric5_Type()
)
ipRouteMetric5.setMaxAccess("read-only")
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
    (0, "LIVINGSTON-SNMP", "ipNetToMediaIfIndex"),
    (0, "LIVINGSTON-SNMP", "ipNetToMediaNetAddress"),
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
ipNetToMediaNetAddress.setMaxAccess("read-only")
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
tcpConnEntry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "tcpConnLocalAddress"),
    (0, "LIVINGSTON-SNMP", "tcpConnLocalPort"),
    (0, "LIVINGSTON-SNMP", "tcpConnRemAddress"),
    (0, "LIVINGSTON-SNMP", "tcpConnRemPort"),
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
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
tcpConnState.setMaxAccess("read-write")
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
_TcpInErrs_Type = Counter32
_TcpInErrs_Object = MibScalar
tcpInErrs = _TcpInErrs_Object(
    (1, 3, 6, 1, 2, 1, 6, 14),
    _TcpInErrs_Type()
)
tcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpInErrs.setStatus("mandatory")
_TcpOutRsts_Type = Counter32
_TcpOutRsts_Object = MibScalar
tcpOutRsts = _TcpOutRsts_Object(
    (1, 3, 6, 1, 2, 1, 6, 15),
    _TcpOutRsts_Type()
)
tcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpOutRsts.setStatus("mandatory")
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
    (0, "LIVINGSTON-SNMP", "udpLocalAddress"),
    (0, "LIVINGSTON-SNMP", "udpLocalPort"),
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
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Livingston_ObjectIdentity = ObjectIdentity
livingston = _Livingston_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 2)
)
_LivingstonPortMaster_ObjectIdentity = ObjectIdentity
livingstonPortMaster = _LivingstonPortMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 2, 1)
)
_LivingstonTraps_ObjectIdentity = ObjectIdentity
livingstonTraps = _LivingstonTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 2, 1, 1)
)
_LivingstonMib_ObjectIdentity = ObjectIdentity
livingstonMib = _LivingstonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3)
)
_LivingstonSystem_ObjectIdentity = ObjectIdentity
livingstonSystem = _LivingstonSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 1)
)


class _LivingstonTrapString_Type(DisplayString):
    """Custom type livingstonTrapString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_LivingstonTrapString_Type.__name__ = "DisplayString"
_LivingstonTrapString_Object = MibScalar
livingstonTrapString = _LivingstonTrapString_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 1, 1),
    _LivingstonTrapString_Type()
)
livingstonTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonTrapString.setStatus("mandatory")
_LivingstonInterfaces_ObjectIdentity = ObjectIdentity
livingstonInterfaces = _LivingstonInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 2)
)
_LivingstonSerial_ObjectIdentity = ObjectIdentity
livingstonSerial = _LivingstonSerial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1)
)
_LivingstonSerialTable_Object = MibTable
livingstonSerialTable = _LivingstonSerialTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    livingstonSerialTable.setStatus("mandatory")
_LivingstonSerialEntry_Object = MibTableRow
livingstonSerialEntry = _LivingstonSerialEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1)
)
livingstonSerialEntry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "livingstonSerialIndex"),
)
if mibBuilder.loadTexts:
    livingstonSerialEntry.setStatus("mandatory")
_LivingstonSerialIndex_Type = Integer32
_LivingstonSerialIndex_Object = MibTableColumn
livingstonSerialIndex = _LivingstonSerialIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 1),
    _LivingstonSerialIndex_Type()
)
livingstonSerialIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialIndex.setStatus("mandatory")


class _LivingstonSerialPortName_Type(DisplayString):
    """Custom type livingstonSerialPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LivingstonSerialPortName_Type.__name__ = "DisplayString"
_LivingstonSerialPortName_Object = MibTableColumn
livingstonSerialPortName = _LivingstonSerialPortName_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 2),
    _LivingstonSerialPortName_Type()
)
livingstonSerialPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialPortName.setStatus("mandatory")


class _LivingstonSerialPhysType_Type(Integer32):
    """Custom type livingstonSerialPhysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("async", 2),
          ("isdn", 4),
          ("isdnSync", 7),
          ("isdnV120", 6),
          ("other", 1),
          ("sync", 3),
          ("trueDigital", 5))
    )


_LivingstonSerialPhysType_Type.__name__ = "Integer32"
_LivingstonSerialPhysType_Object = MibTableColumn
livingstonSerialPhysType = _LivingstonSerialPhysType_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 3),
    _LivingstonSerialPhysType_Type()
)
livingstonSerialPhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialPhysType.setStatus("mandatory")


class _LivingstonSerialUser_Type(DisplayString):
    """Custom type livingstonSerialUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LivingstonSerialUser_Type.__name__ = "DisplayString"
_LivingstonSerialUser_Object = MibTableColumn
livingstonSerialUser = _LivingstonSerialUser_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 4),
    _LivingstonSerialUser_Type()
)
livingstonSerialUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialUser.setStatus("mandatory")


class _LivingstonSerialSessionId_Type(DisplayString):
    """Custom type livingstonSerialSessionId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LivingstonSerialSessionId_Type.__name__ = "DisplayString"
_LivingstonSerialSessionId_Object = MibTableColumn
livingstonSerialSessionId = _LivingstonSerialSessionId_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 5),
    _LivingstonSerialSessionId_Type()
)
livingstonSerialSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialSessionId.setStatus("mandatory")


class _LivingstonSerialType_Type(Integer32):
    """Custom type livingstonSerialType based on Integer32"""
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
        *(("device", 3),
          ("login", 2),
          ("network", 1),
          ("twoway", 4))
    )


_LivingstonSerialType_Type.__name__ = "Integer32"
_LivingstonSerialType_Object = MibTableColumn
livingstonSerialType = _LivingstonSerialType_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 6),
    _LivingstonSerialType_Type()
)
livingstonSerialType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialType.setStatus("mandatory")


class _LivingstonSerialDirection_Type(Integer32):
    """Custom type livingstonSerialDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("inout", 3),
          ("out", 2))
    )


_LivingstonSerialDirection_Type.__name__ = "Integer32"
_LivingstonSerialDirection_Object = MibTableColumn
livingstonSerialDirection = _LivingstonSerialDirection_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 7),
    _LivingstonSerialDirection_Type()
)
livingstonSerialDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialDirection.setStatus("mandatory")


class _LivingstonSerialPortStatus_Type(Integer32):
    """Custom type livingstonSerialPortStatus based on Integer32"""
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
        *(("command", 5),
          ("connecting", 2),
          ("disconnecting", 4),
          ("established", 3),
          ("idle", 1),
          ("noservice", 6))
    )


_LivingstonSerialPortStatus_Type.__name__ = "Integer32"
_LivingstonSerialPortStatus_Object = MibTableColumn
livingstonSerialPortStatus = _LivingstonSerialPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 8),
    _LivingstonSerialPortStatus_Type()
)
livingstonSerialPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialPortStatus.setStatus("mandatory")
_LivingstonSerialStarted_Type = TimeTicks
_LivingstonSerialStarted_Object = MibTableColumn
livingstonSerialStarted = _LivingstonSerialStarted_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 9),
    _LivingstonSerialStarted_Type()
)
livingstonSerialStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialStarted.setStatus("mandatory")
_LivingstonSerialIdle_Type = TimeTicks
_LivingstonSerialIdle_Object = MibTableColumn
livingstonSerialIdle = _LivingstonSerialIdle_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 10),
    _LivingstonSerialIdle_Type()
)
livingstonSerialIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialIdle.setStatus("mandatory")
_LivingstonSerialInSpeed_Type = Gauge32
_LivingstonSerialInSpeed_Object = MibTableColumn
livingstonSerialInSpeed = _LivingstonSerialInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 11),
    _LivingstonSerialInSpeed_Type()
)
livingstonSerialInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialInSpeed.setStatus("mandatory")
_LivingstonSerialOutSpeed_Type = Gauge32
_LivingstonSerialOutSpeed_Object = MibTableColumn
livingstonSerialOutSpeed = _LivingstonSerialOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 12),
    _LivingstonSerialOutSpeed_Type()
)
livingstonSerialOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialOutSpeed.setStatus("mandatory")


class _LivingstonSerialModemName_Type(DisplayString):
    """Custom type livingstonSerialModemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LivingstonSerialModemName_Type.__name__ = "DisplayString"
_LivingstonSerialModemName_Object = MibTableColumn
livingstonSerialModemName = _LivingstonSerialModemName_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 13),
    _LivingstonSerialModemName_Type()
)
livingstonSerialModemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemName.setStatus("mandatory")
_LivingstonSerialIpAddress_Type = IpAddress
_LivingstonSerialIpAddress_Object = MibTableColumn
livingstonSerialIpAddress = _LivingstonSerialIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 14),
    _LivingstonSerialIpAddress_Type()
)
livingstonSerialIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialIpAddress.setStatus("mandatory")


class _LivingstonSerialifDescr_Type(DisplayString):
    """Custom type livingstonSerialifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LivingstonSerialifDescr_Type.__name__ = "DisplayString"
_LivingstonSerialifDescr_Object = MibTableColumn
livingstonSerialifDescr = _LivingstonSerialifDescr_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 15),
    _LivingstonSerialifDescr_Type()
)
livingstonSerialifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialifDescr.setStatus("mandatory")
_LivingstonSerialInOctets_Type = Counter32
_LivingstonSerialInOctets_Object = MibTableColumn
livingstonSerialInOctets = _LivingstonSerialInOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 16),
    _LivingstonSerialInOctets_Type()
)
livingstonSerialInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialInOctets.setStatus("mandatory")
_LivingstonSerialOutOctets_Type = Counter32
_LivingstonSerialOutOctets_Object = MibTableColumn
livingstonSerialOutOctets = _LivingstonSerialOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 17),
    _LivingstonSerialOutOctets_Type()
)
livingstonSerialOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialOutOctets.setStatus("mandatory")
_LivingstonSerialQOctets_Type = Counter32
_LivingstonSerialQOctets_Object = MibTableColumn
livingstonSerialQOctets = _LivingstonSerialQOctets_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 18),
    _LivingstonSerialQOctets_Type()
)
livingstonSerialQOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialQOctets.setStatus("mandatory")


class _LivingstonSerialModemStatus_Type(Integer32):
    """Custom type livingstonSerialModemStatus based on Integer32"""
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
        *(("active", 4),
          ("bound", 2),
          ("connecting", 3),
          ("none", 1),
          ("test", 5))
    )


_LivingstonSerialModemStatus_Type.__name__ = "Integer32"
_LivingstonSerialModemStatus_Object = MibTableColumn
livingstonSerialModemStatus = _LivingstonSerialModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 19),
    _LivingstonSerialModemStatus_Type()
)
livingstonSerialModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemStatus.setStatus("mandatory")


class _LivingstonSerialModemCompression_Type(Integer32):
    """Custom type livingstonSerialModemCompression based on Integer32"""
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
        *(("mnp5", 3),
          ("none", 1),
          ("stac", 4),
          ("v42bis", 2))
    )


_LivingstonSerialModemCompression_Type.__name__ = "Integer32"
_LivingstonSerialModemCompression_Object = MibTableColumn
livingstonSerialModemCompression = _LivingstonSerialModemCompression_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 20),
    _LivingstonSerialModemCompression_Type()
)
livingstonSerialModemCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemCompression.setStatus("mandatory")


class _LivingstonSerialModemProtocol_Type(Integer32):
    """Custom type livingstonSerialModemProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lapm", 2),
          ("mnp", 3),
          ("none", 1))
    )


_LivingstonSerialModemProtocol_Type.__name__ = "Integer32"
_LivingstonSerialModemProtocol_Object = MibTableColumn
livingstonSerialModemProtocol = _LivingstonSerialModemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 21),
    _LivingstonSerialModemProtocol_Type()
)
livingstonSerialModemProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemProtocol.setStatus("mandatory")
_LivingstonSerialModemRetrains_Type = Counter32
_LivingstonSerialModemRetrains_Object = MibTableColumn
livingstonSerialModemRetrains = _LivingstonSerialModemRetrains_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 22),
    _LivingstonSerialModemRetrains_Type()
)
livingstonSerialModemRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemRetrains.setStatus("mandatory")
_LivingstonSerialModemRenegotiates_Type = Counter32
_LivingstonSerialModemRenegotiates_Object = MibTableColumn
livingstonSerialModemRenegotiates = _LivingstonSerialModemRenegotiates_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 1, 1, 1, 23),
    _LivingstonSerialModemRenegotiates_Type()
)
livingstonSerialModemRenegotiates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonSerialModemRenegotiates.setStatus("mandatory")
_LivingstonT1E1_ObjectIdentity = ObjectIdentity
livingstonT1E1 = _LivingstonT1E1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2)
)
_LivingstonT1E1Table_Object = MibTable
livingstonT1E1Table = _LivingstonT1E1Table_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    livingstonT1E1Table.setStatus("mandatory")
_LivingstonT1E1Entry_Object = MibTableRow
livingstonT1E1Entry = _LivingstonT1E1Entry_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1)
)
livingstonT1E1Entry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "livingstonT1E1Index"),
)
if mibBuilder.loadTexts:
    livingstonT1E1Entry.setStatus("mandatory")
_LivingstonT1E1Index_Type = Integer32
_LivingstonT1E1Index_Object = MibTableColumn
livingstonT1E1Index = _LivingstonT1E1Index_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 1),
    _LivingstonT1E1Index_Type()
)
livingstonT1E1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1Index.setStatus("mandatory")


class _LivingstonT1E1PhysType_Type(Integer32):
    """Custom type livingstonT1E1PhysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("t1", 1))
    )


_LivingstonT1E1PhysType_Type.__name__ = "Integer32"
_LivingstonT1E1PhysType_Object = MibTableColumn
livingstonT1E1PhysType = _LivingstonT1E1PhysType_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 2),
    _LivingstonT1E1PhysType_Type()
)
livingstonT1E1PhysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1PhysType.setStatus("mandatory")


class _LivingstonT1E1Function_Type(Integer32):
    """Custom type livingstonT1E1Function based on Integer32"""
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
        *(("channelized", 2),
          ("clear", 3),
          ("fractional", 4),
          ("isdn", 1))
    )


_LivingstonT1E1Function_Type.__name__ = "Integer32"
_LivingstonT1E1Function_Object = MibTableColumn
livingstonT1E1Function = _LivingstonT1E1Function_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 3),
    _LivingstonT1E1Function_Type()
)
livingstonT1E1Function.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1Function.setStatus("mandatory")


class _LivingstonT1E1Status_Type(Integer32):
    """Custom type livingstonT1E1Status based on Integer32"""
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
          ("loopback", 3),
          ("up", 1))
    )


_LivingstonT1E1Status_Type.__name__ = "Integer32"
_LivingstonT1E1Status_Object = MibTableColumn
livingstonT1E1Status = _LivingstonT1E1Status_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 4),
    _LivingstonT1E1Status_Type()
)
livingstonT1E1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1Status.setStatus("mandatory")


class _LivingstonT1E1Framing_Type(Integer32):
    """Custom type livingstonT1E1Framing based on Integer32"""
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
        *(("crc4", 3),
          ("d4", 2),
          ("esf", 1),
          ("fas", 4))
    )


_LivingstonT1E1Framing_Type.__name__ = "Integer32"
_LivingstonT1E1Framing_Object = MibTableColumn
livingstonT1E1Framing = _LivingstonT1E1Framing_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 5),
    _LivingstonT1E1Framing_Type()
)
livingstonT1E1Framing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1Framing.setStatus("mandatory")


class _LivingstonT1E1Encoding_Type(Integer32):
    """Custom type livingstonT1E1Encoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_LivingstonT1E1Encoding_Type.__name__ = "Integer32"
_LivingstonT1E1Encoding_Object = MibTableColumn
livingstonT1E1Encoding = _LivingstonT1E1Encoding_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 6),
    _LivingstonT1E1Encoding_Type()
)
livingstonT1E1Encoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1Encoding.setStatus("mandatory")


class _LivingstonT1E1PCM_Type(Integer32):
    """Custom type livingstonT1E1PCM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alaw", 2),
          ("ulaw", 1))
    )


_LivingstonT1E1PCM_Type.__name__ = "Integer32"
_LivingstonT1E1PCM_Object = MibTableColumn
livingstonT1E1PCM = _LivingstonT1E1PCM_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 7),
    _LivingstonT1E1PCM_Type()
)
livingstonT1E1PCM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1PCM.setStatus("mandatory")
_LivingstonT1E1ChangeTime_Type = TimeTicks
_LivingstonT1E1ChangeTime_Object = MibTableColumn
livingstonT1E1ChangeTime = _LivingstonT1E1ChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 8),
    _LivingstonT1E1ChangeTime_Type()
)
livingstonT1E1ChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1ChangeTime.setStatus("mandatory")
_LivingstonT1E1RecvLevel_Type = Gauge32
_LivingstonT1E1RecvLevel_Object = MibTableColumn
livingstonT1E1RecvLevel = _LivingstonT1E1RecvLevel_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 9),
    _LivingstonT1E1RecvLevel_Type()
)
livingstonT1E1RecvLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1RecvLevel.setStatus("mandatory")
_LivingstonT1E1BlueAlarms_Type = Counter32
_LivingstonT1E1BlueAlarms_Object = MibTableColumn
livingstonT1E1BlueAlarms = _LivingstonT1E1BlueAlarms_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 10),
    _LivingstonT1E1BlueAlarms_Type()
)
livingstonT1E1BlueAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1BlueAlarms.setStatus("mandatory")
_LivingstonT1E1YellowAlarms_Type = Counter32
_LivingstonT1E1YellowAlarms_Object = MibTableColumn
livingstonT1E1YellowAlarms = _LivingstonT1E1YellowAlarms_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 11),
    _LivingstonT1E1YellowAlarms_Type()
)
livingstonT1E1YellowAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1YellowAlarms.setStatus("mandatory")
_LivingstonT1E1CarrierLoss_Type = Counter32
_LivingstonT1E1CarrierLoss_Object = MibTableColumn
livingstonT1E1CarrierLoss = _LivingstonT1E1CarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 12),
    _LivingstonT1E1CarrierLoss_Type()
)
livingstonT1E1CarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1CarrierLoss.setStatus("mandatory")
_LivingstonT1E1SyncLoss_Type = Counter32
_LivingstonT1E1SyncLoss_Object = MibTableColumn
livingstonT1E1SyncLoss = _LivingstonT1E1SyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 13),
    _LivingstonT1E1SyncLoss_Type()
)
livingstonT1E1SyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1SyncLoss.setStatus("mandatory")
_LivingstonT1E1BipolarErrors_Type = Counter32
_LivingstonT1E1BipolarErrors_Object = MibTableColumn
livingstonT1E1BipolarErrors = _LivingstonT1E1BipolarErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 14),
    _LivingstonT1E1BipolarErrors_Type()
)
livingstonT1E1BipolarErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1BipolarErrors.setStatus("mandatory")
_LivingstonT1E1CRCErrors_Type = Counter32
_LivingstonT1E1CRCErrors_Object = MibTableColumn
livingstonT1E1CRCErrors = _LivingstonT1E1CRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 15),
    _LivingstonT1E1CRCErrors_Type()
)
livingstonT1E1CRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1CRCErrors.setStatus("mandatory")
_LivingstonT1E1SyncErrors_Type = Counter32
_LivingstonT1E1SyncErrors_Object = MibTableColumn
livingstonT1E1SyncErrors = _LivingstonT1E1SyncErrors_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 2, 1, 1, 16),
    _LivingstonT1E1SyncErrors_Type()
)
livingstonT1E1SyncErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonT1E1SyncErrors.setStatus("mandatory")
_LivingstonModem_ObjectIdentity = ObjectIdentity
livingstonModem = _LivingstonModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3)
)
_LivingstonModemTable_Object = MibTable
livingstonModemTable = _LivingstonModemTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    livingstonModemTable.setStatus("mandatory")
_LivingstonModemEntry_Object = MibTableRow
livingstonModemEntry = _LivingstonModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1)
)
livingstonModemEntry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "livingstonModemIndex"),
)
if mibBuilder.loadTexts:
    livingstonModemEntry.setStatus("mandatory")
_LivingstonModemIndex_Type = Integer32
_LivingstonModemIndex_Object = MibTableColumn
livingstonModemIndex = _LivingstonModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 1),
    _LivingstonModemIndex_Type()
)
livingstonModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemIndex.setStatus("mandatory")


class _LivingstonModemPortName_Type(DisplayString):
    """Custom type livingstonModemPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_LivingstonModemPortName_Type.__name__ = "DisplayString"
_LivingstonModemPortName_Object = MibTableColumn
livingstonModemPortName = _LivingstonModemPortName_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 2),
    _LivingstonModemPortName_Type()
)
livingstonModemPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemPortName.setStatus("mandatory")


class _LivingstonModemStatus_Type(Integer32):
    """Custom type livingstonModemStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("active", 4),
          ("admin", 9),
          ("bound", 2),
          ("connecting", 3),
          ("down", 6),
          ("halt", 8),
          ("none", 1),
          ("ready", 7),
          ("test", 5))
    )


_LivingstonModemStatus_Type.__name__ = "Integer32"
_LivingstonModemStatus_Object = MibTableColumn
livingstonModemStatus = _LivingstonModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 3),
    _LivingstonModemStatus_Type()
)
livingstonModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemStatus.setStatus("mandatory")


class _LivingstonModemProtocol_Type(Integer32):
    """Custom type livingstonModemProtocol based on Integer32"""
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
        *(("bufferd", 4),
          ("cellular", 6),
          ("direct", 5),
          ("lapm", 2),
          ("mnp", 3),
          ("none", 1))
    )


_LivingstonModemProtocol_Type.__name__ = "Integer32"
_LivingstonModemProtocol_Object = MibTableColumn
livingstonModemProtocol = _LivingstonModemProtocol_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 4),
    _LivingstonModemProtocol_Type()
)
livingstonModemProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemProtocol.setStatus("mandatory")


class _LivingstonModemCompression_Type(Integer32):
    """Custom type livingstonModemCompression based on Integer32"""
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
        *(("mnp5", 3),
          ("none", 1),
          ("stac", 4),
          ("v42bis", 2))
    )


_LivingstonModemCompression_Type.__name__ = "Integer32"
_LivingstonModemCompression_Object = MibTableColumn
livingstonModemCompression = _LivingstonModemCompression_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 5),
    _LivingstonModemCompression_Type()
)
livingstonModemCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemCompression.setStatus("mandatory")
_LivingstonModemInSpeed_Type = Gauge32
_LivingstonModemInSpeed_Object = MibTableColumn
livingstonModemInSpeed = _LivingstonModemInSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 6),
    _LivingstonModemInSpeed_Type()
)
livingstonModemInSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemInSpeed.setStatus("mandatory")
_LivingstonModemOutSpeed_Type = Gauge32
_LivingstonModemOutSpeed_Object = MibTableColumn
livingstonModemOutSpeed = _LivingstonModemOutSpeed_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 7),
    _LivingstonModemOutSpeed_Type()
)
livingstonModemOutSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemOutSpeed.setStatus("mandatory")
_LivingstonModemInByteCount_Type = Counter32
_LivingstonModemInByteCount_Object = MibTableColumn
livingstonModemInByteCount = _LivingstonModemInByteCount_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 8),
    _LivingstonModemInByteCount_Type()
)
livingstonModemInByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemInByteCount.setStatus("mandatory")
_LivingstonModemOutByteCount_Type = Counter32
_LivingstonModemOutByteCount_Object = MibTableColumn
livingstonModemOutByteCount = _LivingstonModemOutByteCount_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 9),
    _LivingstonModemOutByteCount_Type()
)
livingstonModemOutByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemOutByteCount.setStatus("mandatory")
_LivingstonModemRetrains_Type = Counter32
_LivingstonModemRetrains_Object = MibTableColumn
livingstonModemRetrains = _LivingstonModemRetrains_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 10),
    _LivingstonModemRetrains_Type()
)
livingstonModemRetrains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemRetrains.setStatus("mandatory")
_LivingstonModemRenegotiates_Type = Counter32
_LivingstonModemRenegotiates_Object = MibTableColumn
livingstonModemRenegotiates = _LivingstonModemRenegotiates_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 11),
    _LivingstonModemRenegotiates_Type()
)
livingstonModemRenegotiates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemRenegotiates.setStatus("mandatory")
_LivingstonModemCalls_Type = Counter32
_LivingstonModemCalls_Object = MibTableColumn
livingstonModemCalls = _LivingstonModemCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 12),
    _LivingstonModemCalls_Type()
)
livingstonModemCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemCalls.setStatus("mandatory")
_LivingstonModemDetects_Type = Counter32
_LivingstonModemDetects_Object = MibTableColumn
livingstonModemDetects = _LivingstonModemDetects_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 13),
    _LivingstonModemDetects_Type()
)
livingstonModemDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemDetects.setStatus("mandatory")
_LivingstonModemConnects_Type = Counter32
_LivingstonModemConnects_Object = MibTableColumn
livingstonModemConnects = _LivingstonModemConnects_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 2, 3, 1, 1, 14),
    _LivingstonModemConnects_Type()
)
livingstonModemConnects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonModemConnects.setStatus("mandatory")
_LivingstonAt_ObjectIdentity = ObjectIdentity
livingstonAt = _LivingstonAt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 3)
)
_LivingstonIp_ObjectIdentity = ObjectIdentity
livingstonIp = _LivingstonIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 4)
)
_LivingstonIcmp_ObjectIdentity = ObjectIdentity
livingstonIcmp = _LivingstonIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 5)
)
_LivingstonTcp_ObjectIdentity = ObjectIdentity
livingstonTcp = _LivingstonTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 6)
)
_LivingstonUdp_ObjectIdentity = ObjectIdentity
livingstonUdp = _LivingstonUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 7)
)
_LivingstonLocations_ObjectIdentity = ObjectIdentity
livingstonLocations = _LivingstonLocations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 12)
)
_LivingstonUsers_ObjectIdentity = ObjectIdentity
livingstonUsers = _LivingstonUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 13)
)
_LivingstonAcctMgmt_ObjectIdentity = ObjectIdentity
livingstonAcctMgmt = _LivingstonAcctMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 14)
)
_LivingstonPerfMgmt_ObjectIdentity = ObjectIdentity
livingstonPerfMgmt = _LivingstonPerfMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 15)
)
_LivingstonPMCallSummary_ObjectIdentity = ObjectIdentity
livingstonPMCallSummary = _LivingstonPMCallSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1)
)
_LivingstonPMBoardCallSummary_ObjectIdentity = ObjectIdentity
livingstonPMBoardCallSummary = _LivingstonPMBoardCallSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1)
)
_LivingstonPMBrdCallSummaryTable_Object = MibTable
livingstonPMBrdCallSummaryTable = _LivingstonPMBrdCallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    livingstonPMBrdCallSummaryTable.setStatus("mandatory")
_LivingstonPMBrdCallSumEntry_Object = MibTableRow
livingstonPMBrdCallSumEntry = _LivingstonPMBrdCallSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1)
)
livingstonPMBrdCallSumEntry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "livingstonPMBrdCallSumBoardId"),
)
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumEntry.setStatus("mandatory")
_LivingstonPMBrdCallSumBrdId_Type = Integer32
_LivingstonPMBrdCallSumBrdId_Object = MibTableColumn
livingstonPMBrdCallSumBrdId = _LivingstonPMBrdCallSumBrdId_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 1),
    _LivingstonPMBrdCallSumBrdId_Type()
)
livingstonPMBrdCallSumBrdId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumBrdId.setStatus("mandatory")
_LivingstonPMBrdCallSumCapacity_Type = Integer32
_LivingstonPMBrdCallSumCapacity_Object = MibTableColumn
livingstonPMBrdCallSumCapacity = _LivingstonPMBrdCallSumCapacity_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 2),
    _LivingstonPMBrdCallSumCapacity_Type()
)
livingstonPMBrdCallSumCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumCapacity.setStatus("mandatory")
_LivingstonPMBrdCallSumIsdnCalls_Type = Integer32
_LivingstonPMBrdCallSumIsdnCalls_Object = MibTableColumn
livingstonPMBrdCallSumIsdnCalls = _LivingstonPMBrdCallSumIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 3),
    _LivingstonPMBrdCallSumIsdnCalls_Type()
)
livingstonPMBrdCallSumIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumIsdnCalls.setStatus("mandatory")
_LivingstonPMBrdCallSumV90Calls_Type = Integer32
_LivingstonPMBrdCallSumV90Calls_Object = MibTableColumn
livingstonPMBrdCallSumV90Calls = _LivingstonPMBrdCallSumV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 4),
    _LivingstonPMBrdCallSumV90Calls_Type()
)
livingstonPMBrdCallSumV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumV90Calls.setStatus("mandatory")
_LivingstonPMBoardCallSumV34Calls_Type = Integer32
_LivingstonPMBoardCallSumV34Calls_Object = MibScalar
livingstonPMBoardCallSumV34Calls = _LivingstonPMBoardCallSumV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 5),
    _LivingstonPMBoardCallSumV34Calls_Type()
)
livingstonPMBoardCallSumV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBoardCallSumV34Calls.setStatus("mandatory")
_LivingstonPMBrdCallSumOtherCalls_Type = Integer32
_LivingstonPMBrdCallSumOtherCalls_Object = MibScalar
livingstonPMBrdCallSumOtherCalls = _LivingstonPMBrdCallSumOtherCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 1, 1, 1, 6),
    _LivingstonPMBrdCallSumOtherCalls_Type()
)
livingstonPMBrdCallSumOtherCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMBrdCallSumOtherCalls.setStatus("mandatory")
_LivingstonPMT1E1CallSummary_ObjectIdentity = ObjectIdentity
livingstonPMT1E1CallSummary = _LivingstonPMT1E1CallSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2)
)
_LivingstonPMT1E1CallSummaryTable_Object = MibTable
livingstonPMT1E1CallSummaryTable = _LivingstonPMT1E1CallSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSummaryTable.setStatus("mandatory")
_LivingstonPMT1E1CallSumEntry_Object = MibTableRow
livingstonPMT1E1CallSumEntry = _LivingstonPMT1E1CallSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1)
)
livingstonPMT1E1CallSumEntry.setIndexNames(
    (0, "LIVINGSTON-SNMP", "livingstonPMT1E1CallSumBrdId"),
    (0, "LIVINGSTON-SNMP", "livingstonPMT1E1CallSumIfId"),
)
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumEntry.setStatus("mandatory")
_LivingstonPMT1E1CallSumIfId_Type = Integer32
_LivingstonPMT1E1CallSumIfId_Object = MibTableColumn
livingstonPMT1E1CallSumIfId = _LivingstonPMT1E1CallSumIfId_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 1),
    _LivingstonPMT1E1CallSumIfId_Type()
)
livingstonPMT1E1CallSumIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumIfId.setStatus("mandatory")
_LivingstonPMT1E1CallSumCapacity_Type = Integer32
_LivingstonPMT1E1CallSumCapacity_Object = MibTableColumn
livingstonPMT1E1CallSumCapacity = _LivingstonPMT1E1CallSumCapacity_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 2),
    _LivingstonPMT1E1CallSumCapacity_Type()
)
livingstonPMT1E1CallSumCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumCapacity.setStatus("mandatory")
_LivingstonPMT1E1CallSumIsdnCalls_Type = Integer32
_LivingstonPMT1E1CallSumIsdnCalls_Object = MibTableColumn
livingstonPMT1E1CallSumIsdnCalls = _LivingstonPMT1E1CallSumIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 3),
    _LivingstonPMT1E1CallSumIsdnCalls_Type()
)
livingstonPMT1E1CallSumIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumIsdnCalls.setStatus("mandatory")
_LivingstonPMT1E1CallSumV90Calls_Type = Integer32
_LivingstonPMT1E1CallSumV90Calls_Object = MibTableColumn
livingstonPMT1E1CallSumV90Calls = _LivingstonPMT1E1CallSumV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 4),
    _LivingstonPMT1E1CallSumV90Calls_Type()
)
livingstonPMT1E1CallSumV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumV90Calls.setStatus("mandatory")
_LivingstonPMT1E1CallSumV34Calls_Type = Integer32
_LivingstonPMT1E1CallSumV34Calls_Object = MibTableColumn
livingstonPMT1E1CallSumV34Calls = _LivingstonPMT1E1CallSumV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 5),
    _LivingstonPMT1E1CallSumV34Calls_Type()
)
livingstonPMT1E1CallSumV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumV34Calls.setStatus("mandatory")
_LivingstonPMT1E1CallSumOtherCalls_Type = Integer32
_LivingstonPMT1E1CallSumOtherCalls_Object = MibScalar
livingstonPMT1E1CallSumOtherCalls = _LivingstonPMT1E1CallSumOtherCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 2, 1, 1, 6),
    _LivingstonPMT1E1CallSumOtherCalls_Type()
)
livingstonPMT1E1CallSumOtherCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMT1E1CallSumOtherCalls.setStatus("mandatory")
_LivingstonPMChasCallSummary_ObjectIdentity = ObjectIdentity
livingstonPMChasCallSummary = _LivingstonPMChasCallSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3)
)
_LivingstonPMChasCapacity_Type = Integer32
_LivingstonPMChasCapacity_Object = MibScalar
livingstonPMChasCapacity = _LivingstonPMChasCapacity_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 1),
    _LivingstonPMChasCapacity_Type()
)
livingstonPMChasCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasCapacity.setStatus("mandatory")
_LivingstonPMChasIsdnCalls_Type = Integer32
_LivingstonPMChasIsdnCalls_Object = MibScalar
livingstonPMChasIsdnCalls = _LivingstonPMChasIsdnCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 2),
    _LivingstonPMChasIsdnCalls_Type()
)
livingstonPMChasIsdnCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasIsdnCalls.setStatus("mandatory")
_LivingstonPMChasV90Calls_Type = Integer32
_LivingstonPMChasV90Calls_Object = MibScalar
livingstonPMChasV90Calls = _LivingstonPMChasV90Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 3),
    _LivingstonPMChasV90Calls_Type()
)
livingstonPMChasV90Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasV90Calls.setStatus("mandatory")
_LivingstonPMChasV34Calls_Type = Integer32
_LivingstonPMChasV34Calls_Object = MibScalar
livingstonPMChasV34Calls = _LivingstonPMChasV34Calls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 4),
    _LivingstonPMChasV34Calls_Type()
)
livingstonPMChasV34Calls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasV34Calls.setStatus("mandatory")
_LivingstonPMChasOtherCalls_Type = Integer32
_LivingstonPMChasOtherCalls_Object = MibScalar
livingstonPMChasOtherCalls = _LivingstonPMChasOtherCalls_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 5),
    _LivingstonPMChasOtherCalls_Type()
)
livingstonPMChasOtherCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasOtherCalls.setStatus("mandatory")
_LivingstonPMChasSessions_Type = Integer32
_LivingstonPMChasSessions_Object = MibScalar
livingstonPMChasSessions = _LivingstonPMChasSessions_Object(
    (1, 3, 6, 1, 4, 1, 307, 3, 15, 1, 3, 6),
    _LivingstonPMChasSessions_Type()
)
livingstonPMChasSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    livingstonPMChasSessions.setStatus("mandatory")

# Managed Objects groups


# Notification objects

livingstonPwrSupFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 3)
)
livingstonPwrSupFailTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonPwrSupFailTrap.setStatus(
        ""
    )

livingstonPwrSupRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 5)
)
livingstonPwrSupRestoredTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonPwrSupRestoredTrap.setStatus(
        ""
    )

livingstonFanFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 6)
)
livingstonFanFailTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonFanFailTrap.setStatus(
        ""
    )

livingstonFanRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 7)
)
livingstonFanRestoredTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonFanRestoredTrap.setStatus(
        ""
    )

livingstonBoardTempWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 8)
)
livingstonBoardTempWarnTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonBoardTempWarnTrap.setStatus(
        ""
    )

livingstonBoardTooHotTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 10)
)
livingstonBoardTooHotTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonBoardTooHotTrap.setStatus(
        ""
    )

livingstonModemFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 11)
)
livingstonModemFailTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonModemFailTrap.setStatus(
        ""
    )

livingstonT1E1LineDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 12)
)
livingstonT1E1LineDownTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonT1E1LineDownTrap.setStatus(
        ""
    )

livingstonBoardPwrOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 15)
)
livingstonBoardPwrOffTrap.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonBoardPwrOffTrap.setStatus(
        ""
    )

livingstonMCastHeartBeatFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 307, 0, 17)
)
livingstonMCastHeartBeatFail.setObjects(
    ("LIVINGSTON-SNMP", "livingstonTrapString")
)
if mibBuilder.loadTexts:
    livingstonMCastHeartBeatFail.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIVINGSTON-SNMP",
    **{"mib-2": mib_2,
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
       "ipAdEntReasmMaxSize": ipAdEntReasmMaxSize,
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
       "tcpInErrs": tcpInErrs,
       "tcpOutRsts": tcpOutRsts,
       "udp": udp,
       "udpInDatagrams": udpInDatagrams,
       "udpNoPorts": udpNoPorts,
       "udpInErrors": udpInErrors,
       "udpOutDatagrams": udpOutDatagrams,
       "udpTable": udpTable,
       "udpEntry": udpEntry,
       "udpLocalAddress": udpLocalAddress,
       "udpLocalPort": udpLocalPort,
       "transmission": transmission,
       "livingston": livingston,
       "livingstonPwrSupFailTrap": livingstonPwrSupFailTrap,
       "livingstonPwrSupRestoredTrap": livingstonPwrSupRestoredTrap,
       "livingstonFanFailTrap": livingstonFanFailTrap,
       "livingstonFanRestoredTrap": livingstonFanRestoredTrap,
       "livingstonBoardTempWarnTrap": livingstonBoardTempWarnTrap,
       "livingstonBoardTooHotTrap": livingstonBoardTooHotTrap,
       "livingstonModemFailTrap": livingstonModemFailTrap,
       "livingstonT1E1LineDownTrap": livingstonT1E1LineDownTrap,
       "livingstonBoardPwrOffTrap": livingstonBoardPwrOffTrap,
       "livingstonMCastHeartBeatFail": livingstonMCastHeartBeatFail,
       "products": products,
       "livingstonPortMaster": livingstonPortMaster,
       "livingstonTraps": livingstonTraps,
       "livingstonMib": livingstonMib,
       "livingstonSystem": livingstonSystem,
       "livingstonTrapString": livingstonTrapString,
       "livingstonInterfaces": livingstonInterfaces,
       "livingstonSerial": livingstonSerial,
       "livingstonSerialTable": livingstonSerialTable,
       "livingstonSerialEntry": livingstonSerialEntry,
       "livingstonSerialIndex": livingstonSerialIndex,
       "livingstonSerialPortName": livingstonSerialPortName,
       "livingstonSerialPhysType": livingstonSerialPhysType,
       "livingstonSerialUser": livingstonSerialUser,
       "livingstonSerialSessionId": livingstonSerialSessionId,
       "livingstonSerialType": livingstonSerialType,
       "livingstonSerialDirection": livingstonSerialDirection,
       "livingstonSerialPortStatus": livingstonSerialPortStatus,
       "livingstonSerialStarted": livingstonSerialStarted,
       "livingstonSerialIdle": livingstonSerialIdle,
       "livingstonSerialInSpeed": livingstonSerialInSpeed,
       "livingstonSerialOutSpeed": livingstonSerialOutSpeed,
       "livingstonSerialModemName": livingstonSerialModemName,
       "livingstonSerialIpAddress": livingstonSerialIpAddress,
       "livingstonSerialifDescr": livingstonSerialifDescr,
       "livingstonSerialInOctets": livingstonSerialInOctets,
       "livingstonSerialOutOctets": livingstonSerialOutOctets,
       "livingstonSerialQOctets": livingstonSerialQOctets,
       "livingstonSerialModemStatus": livingstonSerialModemStatus,
       "livingstonSerialModemCompression": livingstonSerialModemCompression,
       "livingstonSerialModemProtocol": livingstonSerialModemProtocol,
       "livingstonSerialModemRetrains": livingstonSerialModemRetrains,
       "livingstonSerialModemRenegotiates": livingstonSerialModemRenegotiates,
       "livingstonT1E1": livingstonT1E1,
       "livingstonT1E1Table": livingstonT1E1Table,
       "livingstonT1E1Entry": livingstonT1E1Entry,
       "livingstonT1E1Index": livingstonT1E1Index,
       "livingstonT1E1PhysType": livingstonT1E1PhysType,
       "livingstonT1E1Function": livingstonT1E1Function,
       "livingstonT1E1Status": livingstonT1E1Status,
       "livingstonT1E1Framing": livingstonT1E1Framing,
       "livingstonT1E1Encoding": livingstonT1E1Encoding,
       "livingstonT1E1PCM": livingstonT1E1PCM,
       "livingstonT1E1ChangeTime": livingstonT1E1ChangeTime,
       "livingstonT1E1RecvLevel": livingstonT1E1RecvLevel,
       "livingstonT1E1BlueAlarms": livingstonT1E1BlueAlarms,
       "livingstonT1E1YellowAlarms": livingstonT1E1YellowAlarms,
       "livingstonT1E1CarrierLoss": livingstonT1E1CarrierLoss,
       "livingstonT1E1SyncLoss": livingstonT1E1SyncLoss,
       "livingstonT1E1BipolarErrors": livingstonT1E1BipolarErrors,
       "livingstonT1E1CRCErrors": livingstonT1E1CRCErrors,
       "livingstonT1E1SyncErrors": livingstonT1E1SyncErrors,
       "livingstonModem": livingstonModem,
       "livingstonModemTable": livingstonModemTable,
       "livingstonModemEntry": livingstonModemEntry,
       "livingstonModemIndex": livingstonModemIndex,
       "livingstonModemPortName": livingstonModemPortName,
       "livingstonModemStatus": livingstonModemStatus,
       "livingstonModemProtocol": livingstonModemProtocol,
       "livingstonModemCompression": livingstonModemCompression,
       "livingstonModemInSpeed": livingstonModemInSpeed,
       "livingstonModemOutSpeed": livingstonModemOutSpeed,
       "livingstonModemInByteCount": livingstonModemInByteCount,
       "livingstonModemOutByteCount": livingstonModemOutByteCount,
       "livingstonModemRetrains": livingstonModemRetrains,
       "livingstonModemRenegotiates": livingstonModemRenegotiates,
       "livingstonModemCalls": livingstonModemCalls,
       "livingstonModemDetects": livingstonModemDetects,
       "livingstonModemConnects": livingstonModemConnects,
       "livingstonAt": livingstonAt,
       "livingstonIp": livingstonIp,
       "livingstonIcmp": livingstonIcmp,
       "livingstonTcp": livingstonTcp,
       "livingstonUdp": livingstonUdp,
       "livingstonLocations": livingstonLocations,
       "livingstonUsers": livingstonUsers,
       "livingstonAcctMgmt": livingstonAcctMgmt,
       "livingstonPerfMgmt": livingstonPerfMgmt,
       "livingstonPMCallSummary": livingstonPMCallSummary,
       "livingstonPMBoardCallSummary": livingstonPMBoardCallSummary,
       "livingstonPMBrdCallSummaryTable": livingstonPMBrdCallSummaryTable,
       "livingstonPMBrdCallSumEntry": livingstonPMBrdCallSumEntry,
       "livingstonPMBrdCallSumBrdId": livingstonPMBrdCallSumBrdId,
       "livingstonPMBrdCallSumCapacity": livingstonPMBrdCallSumCapacity,
       "livingstonPMBrdCallSumIsdnCalls": livingstonPMBrdCallSumIsdnCalls,
       "livingstonPMBrdCallSumV90Calls": livingstonPMBrdCallSumV90Calls,
       "livingstonPMBoardCallSumV34Calls": livingstonPMBoardCallSumV34Calls,
       "livingstonPMBrdCallSumOtherCalls": livingstonPMBrdCallSumOtherCalls,
       "livingstonPMT1E1CallSummary": livingstonPMT1E1CallSummary,
       "livingstonPMT1E1CallSummaryTable": livingstonPMT1E1CallSummaryTable,
       "livingstonPMT1E1CallSumEntry": livingstonPMT1E1CallSumEntry,
       "livingstonPMT1E1CallSumIfId": livingstonPMT1E1CallSumIfId,
       "livingstonPMT1E1CallSumCapacity": livingstonPMT1E1CallSumCapacity,
       "livingstonPMT1E1CallSumIsdnCalls": livingstonPMT1E1CallSumIsdnCalls,
       "livingstonPMT1E1CallSumV90Calls": livingstonPMT1E1CallSumV90Calls,
       "livingstonPMT1E1CallSumV34Calls": livingstonPMT1E1CallSumV34Calls,
       "livingstonPMT1E1CallSumOtherCalls": livingstonPMT1E1CallSumOtherCalls,
       "livingstonPMChasCallSummary": livingstonPMChasCallSummary,
       "livingstonPMChasCapacity": livingstonPMChasCapacity,
       "livingstonPMChasIsdnCalls": livingstonPMChasIsdnCalls,
       "livingstonPMChasV90Calls": livingstonPMChasV90Calls,
       "livingstonPMChasV34Calls": livingstonPMChasV34Calls,
       "livingstonPMChasOtherCalls": livingstonPMChasOtherCalls,
       "livingstonPMChasSessions": livingstonPMChasSessions}
)
