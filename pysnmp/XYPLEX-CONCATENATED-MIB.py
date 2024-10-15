# SNMP MIB module (XYPLEX-CONCATENATED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYPLEX-CONCATENATED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:46 2024
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
 experimental,
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
    "experimental",
    "iso",
    "mgmt")

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




class DateTime(OctetString):
    """Custom type DateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class AddressType(Integer32):
    """Custom type AddressType based on Integer32"""
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
        *(("ethernet", 5),
          ("ip", 4),
          ("local", 3),
          ("other", 2),
          ("unknown", 1))
    )





class AutonomousType(ObjectIdentifier):
    """Custom type AutonomousType based on ObjectIdentifier"""




class InstancePointer(ObjectIdentifier):
    """Custom type InstancePointer based on ObjectIdentifier"""



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
    (0, "XYPLEX-CONCATENATED-MIB", "ifIndex"),
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
    (0, "XYPLEX-CONCATENATED-MIB", "atIfIndex"),
    (0, "XYPLEX-CONCATENATED-MIB", "atNetAddress"),
)
if mibBuilder.loadTexts:
    atEntry.setStatus("deprecated")
_AtIfIndex_Type = Integer32
_AtIfIndex_Object = MibTableColumn
atIfIndex = _AtIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 3, 1, 1, 1),
    _AtIfIndex_Type()
)
atIfIndex.setMaxAccess("read-write")
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
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_IpForwarding_Type.__name__ = "Integer32"
_IpForwarding_Object = MibScalar
ipForwarding = _IpForwarding_Object(
    (1, 3, 6, 1, 2, 1, 4, 1),
    _IpForwarding_Type()
)
ipForwarding.setMaxAccess("read-write")
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
    (0, "XYPLEX-CONCATENATED-MIB", "ipAdEntAddr"),
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
    (0, "XYPLEX-CONCATENATED-MIB", "ipRouteDest"),
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
    (0, "XYPLEX-CONCATENATED-MIB", "ipNetToMediaIfIndex"),
    (0, "XYPLEX-CONCATENATED-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipNetToMediaEntry.setStatus("mandatory")
_IpNetToMediaIfIndex_Type = Integer32
_IpNetToMediaIfIndex_Object = MibTableColumn
ipNetToMediaIfIndex = _IpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 4, 22, 1, 1),
    _IpNetToMediaIfIndex_Type()
)
ipNetToMediaIfIndex.setMaxAccess("read-write")
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
    (0, "XYPLEX-CONCATENATED-MIB", "tcpConnLocalAddress"),
    (0, "XYPLEX-CONCATENATED-MIB", "tcpConnLocalPort"),
    (0, "XYPLEX-CONCATENATED-MIB", "tcpConnRemAddress"),
    (0, "XYPLEX-CONCATENATED-MIB", "tcpConnRemPort"),
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
    (0, "XYPLEX-CONCATENATED-MIB", "udpLocalAddress"),
    (0, "XYPLEX-CONCATENATED-MIB", "udpLocalPort"),
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
_Char_ObjectIdentity = ObjectIdentity
char = _Char_ObjectIdentity(
    (1, 3, 6, 1, 3, 19)
)
_CharNumber_Type = Integer32
_CharNumber_Object = MibScalar
charNumber = _CharNumber_Object(
    (1, 3, 6, 1, 3, 19, 1),
    _CharNumber_Type()
)
charNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charNumber.setStatus("mandatory")
_CharPortTable_Object = MibTable
charPortTable = _CharPortTable_Object(
    (1, 3, 6, 1, 3, 19, 2)
)
if mibBuilder.loadTexts:
    charPortTable.setStatus("mandatory")
_CharPortEntry_Object = MibTableRow
charPortEntry = _CharPortEntry_Object(
    (1, 3, 6, 1, 3, 19, 2, 1)
)
charPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "charPortIndex"),
)
if mibBuilder.loadTexts:
    charPortEntry.setStatus("mandatory")
_CharPortIndex_Type = Integer32
_CharPortIndex_Object = MibTableColumn
charPortIndex = _CharPortIndex_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 1),
    _CharPortIndex_Type()
)
charPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortIndex.setStatus("mandatory")


class _CharPortName_Type(DisplayString):
    """Custom type charPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CharPortName_Type.__name__ = "DisplayString"
_CharPortName_Object = MibTableColumn
charPortName = _CharPortName_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 2),
    _CharPortName_Type()
)
charPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortName.setStatus("mandatory")


class _CharPortType_Type(Integer32):
    """Custom type charPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("physical", 1),
          ("virtual", 2))
    )


_CharPortType_Type.__name__ = "Integer32"
_CharPortType_Object = MibTableColumn
charPortType = _CharPortType_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 3),
    _CharPortType_Type()
)
charPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortType.setStatus("mandatory")
_CharPortHardware_Type = AutonomousType
_CharPortHardware_Object = MibTableColumn
charPortHardware = _CharPortHardware_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 4),
    _CharPortHardware_Type()
)
charPortHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortHardware.setStatus("mandatory")


class _CharPortReset_Type(Integer32):
    """Custom type charPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_CharPortReset_Type.__name__ = "Integer32"
_CharPortReset_Object = MibTableColumn
charPortReset = _CharPortReset_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 5),
    _CharPortReset_Type()
)
charPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortReset.setStatus("mandatory")


class _CharPortAdminStatus_Type(Integer32):
    """Custom type charPortAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("maintenance", 4),
          ("off", 3))
    )


_CharPortAdminStatus_Type.__name__ = "Integer32"
_CharPortAdminStatus_Object = MibTableColumn
charPortAdminStatus = _CharPortAdminStatus_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 6),
    _CharPortAdminStatus_Type()
)
charPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminStatus.setStatus("mandatory")


class _CharPortOperStatus_Type(Integer32):
    """Custom type charPortOperStatus based on Integer32"""
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
        *(("absent", 4),
          ("active", 5),
          ("down", 2),
          ("maintenance", 3),
          ("up", 1))
    )


_CharPortOperStatus_Type.__name__ = "Integer32"
_CharPortOperStatus_Object = MibTableColumn
charPortOperStatus = _CharPortOperStatus_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 7),
    _CharPortOperStatus_Type()
)
charPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOperStatus.setStatus("mandatory")
_CharPortLastChange_Type = TimeTicks
_CharPortLastChange_Object = MibTableColumn
charPortLastChange = _CharPortLastChange_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 8),
    _CharPortLastChange_Type()
)
charPortLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortLastChange.setStatus("mandatory")


class _CharPortInFlowType_Type(Integer32):
    """Custom type charPortInFlowType based on Integer32"""
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
        *(("ctsRts", 4),
          ("dsrDtr", 5),
          ("hardware", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_CharPortInFlowType_Type.__name__ = "Integer32"
_CharPortInFlowType_Object = MibTableColumn
charPortInFlowType = _CharPortInFlowType_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 9),
    _CharPortInFlowType_Type()
)
charPortInFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortInFlowType.setStatus("mandatory")


class _CharPortOutFlowType_Type(Integer32):
    """Custom type charPortOutFlowType based on Integer32"""
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
        *(("ctsRts", 4),
          ("dsrDtr", 5),
          ("hardware", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_CharPortOutFlowType_Type.__name__ = "Integer32"
_CharPortOutFlowType_Object = MibTableColumn
charPortOutFlowType = _CharPortOutFlowType_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 10),
    _CharPortOutFlowType_Type()
)
charPortOutFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortOutFlowType.setStatus("mandatory")


class _CharPortInFlowState_Type(Integer32):
    """Custom type charPortInFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_CharPortInFlowState_Type.__name__ = "Integer32"
_CharPortInFlowState_Object = MibTableColumn
charPortInFlowState = _CharPortInFlowState_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 11),
    _CharPortInFlowState_Type()
)
charPortInFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInFlowState.setStatus("mandatory")


class _CharPortOutFlowState_Type(Integer32):
    """Custom type charPortOutFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_CharPortOutFlowState_Type.__name__ = "Integer32"
_CharPortOutFlowState_Object = MibTableColumn
charPortOutFlowState = _CharPortOutFlowState_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 12),
    _CharPortOutFlowState_Type()
)
charPortOutFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutFlowState.setStatus("mandatory")
_CharPortInCharacters_Type = Counter32
_CharPortInCharacters_Object = MibTableColumn
charPortInCharacters = _CharPortInCharacters_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 13),
    _CharPortInCharacters_Type()
)
charPortInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortInCharacters.setStatus("mandatory")
_CharPortOutCharacters_Type = Counter32
_CharPortOutCharacters_Object = MibTableColumn
charPortOutCharacters = _CharPortOutCharacters_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 14),
    _CharPortOutCharacters_Type()
)
charPortOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortOutCharacters.setStatus("mandatory")


class _CharPortAdminOrigin_Type(Integer32):
    """Custom type charPortAdminOrigin based on Integer32"""
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
        *(("dynamic", 1),
          ("local", 3),
          ("network", 2),
          ("none", 4))
    )


_CharPortAdminOrigin_Type.__name__ = "Integer32"
_CharPortAdminOrigin_Object = MibTableColumn
charPortAdminOrigin = _CharPortAdminOrigin_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 15),
    _CharPortAdminOrigin_Type()
)
charPortAdminOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortAdminOrigin.setStatus("mandatory")
_CharPortSessionMaximum_Type = Integer32
_CharPortSessionMaximum_Object = MibTableColumn
charPortSessionMaximum = _CharPortSessionMaximum_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 16),
    _CharPortSessionMaximum_Type()
)
charPortSessionMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charPortSessionMaximum.setStatus("mandatory")
_CharPortSessionNumber_Type = Gauge32
_CharPortSessionNumber_Object = MibTableColumn
charPortSessionNumber = _CharPortSessionNumber_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 17),
    _CharPortSessionNumber_Type()
)
charPortSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionNumber.setStatus("mandatory")
_CharPortSessionIndex_Type = Integer32
_CharPortSessionIndex_Object = MibTableColumn
charPortSessionIndex = _CharPortSessionIndex_Object(
    (1, 3, 6, 1, 3, 19, 2, 1, 18),
    _CharPortSessionIndex_Type()
)
charPortSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charPortSessionIndex.setStatus("mandatory")
_CharSessTable_Object = MibTable
charSessTable = _CharSessTable_Object(
    (1, 3, 6, 1, 3, 19, 3)
)
if mibBuilder.loadTexts:
    charSessTable.setStatus("mandatory")
_CharSessEntry_Object = MibTableRow
charSessEntry = _CharSessEntry_Object(
    (1, 3, 6, 1, 3, 19, 3, 1)
)
charSessEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "charSessPortIndex"),
    (0, "XYPLEX-CONCATENATED-MIB", "charSessIndex"),
)
if mibBuilder.loadTexts:
    charSessEntry.setStatus("mandatory")
_CharSessPortIndex_Type = Integer32
_CharSessPortIndex_Object = MibTableColumn
charSessPortIndex = _CharSessPortIndex_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 1),
    _CharSessPortIndex_Type()
)
charSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessPortIndex.setStatus("mandatory")
_CharSessIndex_Type = Integer32
_CharSessIndex_Object = MibTableColumn
charSessIndex = _CharSessIndex_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 2),
    _CharSessIndex_Type()
)
charSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessIndex.setStatus("mandatory")


class _CharSessKill_Type(Integer32):
    """Custom type charSessKill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_CharSessKill_Type.__name__ = "Integer32"
_CharSessKill_Object = MibTableColumn
charSessKill = _CharSessKill_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 3),
    _CharSessKill_Type()
)
charSessKill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    charSessKill.setStatus("mandatory")


class _CharSessState_Type(Integer32):
    """Custom type charSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("disconnecting", 3))
    )


_CharSessState_Type.__name__ = "Integer32"
_CharSessState_Object = MibTableColumn
charSessState = _CharSessState_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 4),
    _CharSessState_Type()
)
charSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessState.setStatus("mandatory")
_CharSessProtocol_Type = AutonomousType
_CharSessProtocol_Object = MibTableColumn
charSessProtocol = _CharSessProtocol_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 5),
    _CharSessProtocol_Type()
)
charSessProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessProtocol.setStatus("mandatory")


class _CharSessOperOrigin_Type(Integer32):
    """Custom type charSessOperOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("network", 2),
          ("unknown", 1))
    )


_CharSessOperOrigin_Type.__name__ = "Integer32"
_CharSessOperOrigin_Object = MibTableColumn
charSessOperOrigin = _CharSessOperOrigin_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 6),
    _CharSessOperOrigin_Type()
)
charSessOperOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOperOrigin.setStatus("mandatory")
_CharSessInCharacters_Type = Counter32
_CharSessInCharacters_Object = MibTableColumn
charSessInCharacters = _CharSessInCharacters_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 7),
    _CharSessInCharacters_Type()
)
charSessInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessInCharacters.setStatus("mandatory")
_CharSessOutCharacters_Type = Counter32
_CharSessOutCharacters_Object = MibTableColumn
charSessOutCharacters = _CharSessOutCharacters_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 8),
    _CharSessOutCharacters_Type()
)
charSessOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessOutCharacters.setStatus("mandatory")
_CharSessConnectionId_Type = InstancePointer
_CharSessConnectionId_Object = MibTableColumn
charSessConnectionId = _CharSessConnectionId_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 9),
    _CharSessConnectionId_Type()
)
charSessConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessConnectionId.setStatus("mandatory")
_CharSessStartTime_Type = TimeTicks
_CharSessStartTime_Object = MibTableColumn
charSessStartTime = _CharSessStartTime_Object(
    (1, 3, 6, 1, 3, 19, 3, 1, 10),
    _CharSessStartTime_Type()
)
charSessStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    charSessStartTime.setStatus("mandatory")
_WellKnownProtocols_ObjectIdentity = ObjectIdentity
wellKnownProtocols = _WellKnownProtocols_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4)
)
_ProtocolOther_ObjectIdentity = ObjectIdentity
protocolOther = _ProtocolOther_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 1)
)
_ProtocolTelnet_ObjectIdentity = ObjectIdentity
protocolTelnet = _ProtocolTelnet_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 2)
)
_ProtocolRlogin_ObjectIdentity = ObjectIdentity
protocolRlogin = _ProtocolRlogin_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 3)
)
_ProtocolLat_ObjectIdentity = ObjectIdentity
protocolLat = _ProtocolLat_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 4)
)
_ProtocolX29_ObjectIdentity = ObjectIdentity
protocolX29 = _ProtocolX29_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 5)
)
_ProtocolVtp_ObjectIdentity = ObjectIdentity
protocolVtp = _ProtocolVtp_ObjectIdentity(
    (1, 3, 6, 1, 3, 19, 4, 6)
)
_Rs232_ObjectIdentity = ObjectIdentity
rs232 = _Rs232_ObjectIdentity(
    (1, 3, 6, 1, 3, 20)
)
_Rs232Number_Type = Integer32
_Rs232Number_Object = MibScalar
rs232Number = _Rs232Number_Object(
    (1, 3, 6, 1, 3, 20, 1),
    _Rs232Number_Type()
)
rs232Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232Number.setStatus("mandatory")
_Rs232PortTable_Object = MibTable
rs232PortTable = _Rs232PortTable_Object(
    (1, 3, 6, 1, 3, 20, 2)
)
if mibBuilder.loadTexts:
    rs232PortTable.setStatus("mandatory")
_Rs232PortEntry_Object = MibTableRow
rs232PortEntry = _Rs232PortEntry_Object(
    (1, 3, 6, 1, 3, 20, 2, 1)
)
rs232PortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rs232PortIndex"),
)
if mibBuilder.loadTexts:
    rs232PortEntry.setStatus("mandatory")
_Rs232PortIndex_Type = Integer32
_Rs232PortIndex_Object = MibTableColumn
rs232PortIndex = _Rs232PortIndex_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 1),
    _Rs232PortIndex_Type()
)
rs232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortIndex.setStatus("mandatory")


class _Rs232PortType_Type(Integer32):
    """Custom type rs232PortType based on Integer32"""
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
        *(("other", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("v35", 5))
    )


_Rs232PortType_Type.__name__ = "Integer32"
_Rs232PortType_Object = MibTableColumn
rs232PortType = _Rs232PortType_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 2),
    _Rs232PortType_Type()
)
rs232PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortType.setStatus("mandatory")
_Rs232PortInSigNumber_Type = Integer32
_Rs232PortInSigNumber_Object = MibTableColumn
rs232PortInSigNumber = _Rs232PortInSigNumber_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 3),
    _Rs232PortInSigNumber_Type()
)
rs232PortInSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortInSigNumber.setStatus("mandatory")
_Rs232PortOutSigNumber_Type = Integer32
_Rs232PortOutSigNumber_Object = MibTableColumn
rs232PortOutSigNumber = _Rs232PortOutSigNumber_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 4),
    _Rs232PortOutSigNumber_Type()
)
rs232PortOutSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortOutSigNumber.setStatus("mandatory")
_Rs232PortInSpeed_Type = Integer32
_Rs232PortInSpeed_Object = MibTableColumn
rs232PortInSpeed = _Rs232PortInSpeed_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 5),
    _Rs232PortInSpeed_Type()
)
rs232PortInSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortInSpeed.setStatus("mandatory")
_Rs232PortOutSpeed_Type = Integer32
_Rs232PortOutSpeed_Object = MibTableColumn
rs232PortOutSpeed = _Rs232PortOutSpeed_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 6),
    _Rs232PortOutSpeed_Type()
)
rs232PortOutSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortOutSpeed.setStatus("mandatory")
_Rs232AsyncPortTable_Object = MibTable
rs232AsyncPortTable = _Rs232AsyncPortTable_Object(
    (1, 3, 6, 1, 3, 20, 3)
)
if mibBuilder.loadTexts:
    rs232AsyncPortTable.setStatus("mandatory")
_Rs232AsyncPortEntry_Object = MibTableRow
rs232AsyncPortEntry = _Rs232AsyncPortEntry_Object(
    (1, 3, 6, 1, 3, 20, 3, 1)
)
rs232AsyncPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rs232AsyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232AsyncPortEntry.setStatus("mandatory")
_Rs232AsyncPortIndex_Type = Integer32
_Rs232AsyncPortIndex_Object = MibTableColumn
rs232AsyncPortIndex = _Rs232AsyncPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 1),
    _Rs232AsyncPortIndex_Type()
)
rs232AsyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortIndex.setStatus("mandatory")


class _Rs232AsyncPortBits_Type(Integer32):
    """Custom type rs232AsyncPortBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_Rs232AsyncPortBits_Type.__name__ = "Integer32"
_Rs232AsyncPortBits_Object = MibTableColumn
rs232AsyncPortBits = _Rs232AsyncPortBits_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 2),
    _Rs232AsyncPortBits_Type()
)
rs232AsyncPortBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortBits.setStatus("mandatory")


class _Rs232AsyncPortStopBits_Type(Integer32):
    """Custom type rs232AsyncPortStopBits based on Integer32"""
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
        *(("dynamic", 4),
          ("one", 1),
          ("one-and-half", 3),
          ("two", 2))
    )


_Rs232AsyncPortStopBits_Type.__name__ = "Integer32"
_Rs232AsyncPortStopBits_Object = MibTableColumn
rs232AsyncPortStopBits = _Rs232AsyncPortStopBits_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 3),
    _Rs232AsyncPortStopBits_Type()
)
rs232AsyncPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortStopBits.setStatus("mandatory")


class _Rs232AsyncPortParity_Type(Integer32):
    """Custom type rs232AsyncPortParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_Rs232AsyncPortParity_Type.__name__ = "Integer32"
_Rs232AsyncPortParity_Object = MibTableColumn
rs232AsyncPortParity = _Rs232AsyncPortParity_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 4),
    _Rs232AsyncPortParity_Type()
)
rs232AsyncPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortParity.setStatus("mandatory")


class _Rs232AsyncPortAutobaud_Type(Integer32):
    """Custom type rs232AsyncPortAutobaud based on Integer32"""
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


_Rs232AsyncPortAutobaud_Type.__name__ = "Integer32"
_Rs232AsyncPortAutobaud_Object = MibTableColumn
rs232AsyncPortAutobaud = _Rs232AsyncPortAutobaud_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 5),
    _Rs232AsyncPortAutobaud_Type()
)
rs232AsyncPortAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortAutobaud.setStatus("mandatory")
_Rs232AsyncPortParityErrs_Type = Counter32
_Rs232AsyncPortParityErrs_Object = MibTableColumn
rs232AsyncPortParityErrs = _Rs232AsyncPortParityErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 6),
    _Rs232AsyncPortParityErrs_Type()
)
rs232AsyncPortParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortParityErrs.setStatus("mandatory")
_Rs232AsyncPortFramingErrs_Type = Counter32
_Rs232AsyncPortFramingErrs_Object = MibTableColumn
rs232AsyncPortFramingErrs = _Rs232AsyncPortFramingErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 7),
    _Rs232AsyncPortFramingErrs_Type()
)
rs232AsyncPortFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortFramingErrs.setStatus("mandatory")
_Rs232AsyncPortOverrunErrs_Type = Counter32
_Rs232AsyncPortOverrunErrs_Object = MibTableColumn
rs232AsyncPortOverrunErrs = _Rs232AsyncPortOverrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 8),
    _Rs232AsyncPortOverrunErrs_Type()
)
rs232AsyncPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortOverrunErrs.setStatus("mandatory")
_Rs232SyncPortTable_Object = MibTable
rs232SyncPortTable = _Rs232SyncPortTable_Object(
    (1, 3, 6, 1, 3, 20, 4)
)
if mibBuilder.loadTexts:
    rs232SyncPortTable.setStatus("mandatory")
_Rs232SyncPortEntry_Object = MibTableRow
rs232SyncPortEntry = _Rs232SyncPortEntry_Object(
    (1, 3, 6, 1, 3, 20, 4, 1)
)
rs232SyncPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rs232SyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232SyncPortEntry.setStatus("mandatory")
_Rs232SyncPortIndex_Type = Integer32
_Rs232SyncPortIndex_Object = MibTableColumn
rs232SyncPortIndex = _Rs232SyncPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 1),
    _Rs232SyncPortIndex_Type()
)
rs232SyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortIndex.setStatus("mandatory")


class _Rs232SyncPortClockSource_Type(Integer32):
    """Custom type rs232SyncPortClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("split", 3))
    )


_Rs232SyncPortClockSource_Type.__name__ = "Integer32"
_Rs232SyncPortClockSource_Object = MibTableColumn
rs232SyncPortClockSource = _Rs232SyncPortClockSource_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 2),
    _Rs232SyncPortClockSource_Type()
)
rs232SyncPortClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortClockSource.setStatus("mandatory")
_Rs232SyncPortFrameCheckErrs_Type = Counter32
_Rs232SyncPortFrameCheckErrs_Object = MibTableColumn
rs232SyncPortFrameCheckErrs = _Rs232SyncPortFrameCheckErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 3),
    _Rs232SyncPortFrameCheckErrs_Type()
)
rs232SyncPortFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortFrameCheckErrs.setStatus("mandatory")
_Rs232SyncPortTransmitUnderrunErrs_Type = Counter32
_Rs232SyncPortTransmitUnderrunErrs_Object = MibTableColumn
rs232SyncPortTransmitUnderrunErrs = _Rs232SyncPortTransmitUnderrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 4),
    _Rs232SyncPortTransmitUnderrunErrs_Type()
)
rs232SyncPortTransmitUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortTransmitUnderrunErrs.setStatus("mandatory")
_Rs232SyncPortReceiveOverrunErrs_Type = Counter32
_Rs232SyncPortReceiveOverrunErrs_Object = MibTableColumn
rs232SyncPortReceiveOverrunErrs = _Rs232SyncPortReceiveOverrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 5),
    _Rs232SyncPortReceiveOverrunErrs_Type()
)
rs232SyncPortReceiveOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortReceiveOverrunErrs.setStatus("mandatory")
_Rs232SyncPortInterruptedFrames_Type = Counter32
_Rs232SyncPortInterruptedFrames_Object = MibTableColumn
rs232SyncPortInterruptedFrames = _Rs232SyncPortInterruptedFrames_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 6),
    _Rs232SyncPortInterruptedFrames_Type()
)
rs232SyncPortInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortInterruptedFrames.setStatus("mandatory")
_Rs232SyncPortAbortedFrames_Type = Counter32
_Rs232SyncPortAbortedFrames_Object = MibTableColumn
rs232SyncPortAbortedFrames = _Rs232SyncPortAbortedFrames_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 7),
    _Rs232SyncPortAbortedFrames_Type()
)
rs232SyncPortAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortAbortedFrames.setStatus("mandatory")
_Rs232InSigTable_Object = MibTable
rs232InSigTable = _Rs232InSigTable_Object(
    (1, 3, 6, 1, 3, 20, 5)
)
if mibBuilder.loadTexts:
    rs232InSigTable.setStatus("mandatory")
_Rs232InSigEntry_Object = MibTableRow
rs232InSigEntry = _Rs232InSigEntry_Object(
    (1, 3, 6, 1, 3, 20, 5, 1)
)
rs232InSigEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rs232InSigPortIndex"),
    (0, "XYPLEX-CONCATENATED-MIB", "rs232InSigName"),
)
if mibBuilder.loadTexts:
    rs232InSigEntry.setStatus("mandatory")
_Rs232InSigPortIndex_Type = Integer32
_Rs232InSigPortIndex_Object = MibTableColumn
rs232InSigPortIndex = _Rs232InSigPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 1),
    _Rs232InSigPortIndex_Type()
)
rs232InSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigPortIndex.setStatus("mandatory")


class _Rs232InSigName_Type(Integer32):
    """Custom type rs232InSigName based on Integer32"""
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
        *(("cts", 2),
          ("dcd", 6),
          ("dsr", 3),
          ("dtr", 4),
          ("ri", 5),
          ("rts", 1),
          ("scts", 10),
          ("sdcd", 11),
          ("sq", 7),
          ("srs", 8),
          ("srts", 9))
    )


_Rs232InSigName_Type.__name__ = "Integer32"
_Rs232InSigName_Object = MibTableColumn
rs232InSigName = _Rs232InSigName_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 2),
    _Rs232InSigName_Type()
)
rs232InSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigName.setStatus("mandatory")


class _Rs232InSigState_Type(Integer32):
    """Custom type rs232InSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_Rs232InSigState_Type.__name__ = "Integer32"
_Rs232InSigState_Object = MibTableColumn
rs232InSigState = _Rs232InSigState_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 3),
    _Rs232InSigState_Type()
)
rs232InSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigState.setStatus("mandatory")
_Rs232InSigChanges_Type = Counter32
_Rs232InSigChanges_Object = MibTableColumn
rs232InSigChanges = _Rs232InSigChanges_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 4),
    _Rs232InSigChanges_Type()
)
rs232InSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigChanges.setStatus("mandatory")
_Rs232OutSigTable_Object = MibTable
rs232OutSigTable = _Rs232OutSigTable_Object(
    (1, 3, 6, 1, 3, 20, 6)
)
if mibBuilder.loadTexts:
    rs232OutSigTable.setStatus("mandatory")
_Rs232OutSigEntry_Object = MibTableRow
rs232OutSigEntry = _Rs232OutSigEntry_Object(
    (1, 3, 6, 1, 3, 20, 6, 1)
)
rs232OutSigEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rs232OutSigPortIndex"),
    (0, "XYPLEX-CONCATENATED-MIB", "rs232OutSigName"),
)
if mibBuilder.loadTexts:
    rs232OutSigEntry.setStatus("mandatory")
_Rs232OutSigPortIndex_Type = Integer32
_Rs232OutSigPortIndex_Object = MibTableColumn
rs232OutSigPortIndex = _Rs232OutSigPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 1),
    _Rs232OutSigPortIndex_Type()
)
rs232OutSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigPortIndex.setStatus("mandatory")


class _Rs232OutSigName_Type(Integer32):
    """Custom type rs232OutSigName based on Integer32"""
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
        *(("cts", 2),
          ("dcd", 6),
          ("dsr", 3),
          ("dtr", 4),
          ("ri", 5),
          ("rts", 1),
          ("scts", 10),
          ("sdcd", 11),
          ("sq", 7),
          ("srs", 8),
          ("srts", 9))
    )


_Rs232OutSigName_Type.__name__ = "Integer32"
_Rs232OutSigName_Object = MibTableColumn
rs232OutSigName = _Rs232OutSigName_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 2),
    _Rs232OutSigName_Type()
)
rs232OutSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigName.setStatus("mandatory")


class _Rs232OutSigState_Type(Integer32):
    """Custom type rs232OutSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_Rs232OutSigState_Type.__name__ = "Integer32"
_Rs232OutSigState_Object = MibTableColumn
rs232OutSigState = _Rs232OutSigState_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 3),
    _Rs232OutSigState_Type()
)
rs232OutSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigState.setStatus("mandatory")
_Rs232OutSigChanges_Type = Counter32
_Rs232OutSigChanges_Object = MibTableColumn
rs232OutSigChanges = _Rs232OutSigChanges_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 4),
    _Rs232OutSigChanges_Type()
)
rs232OutSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigChanges.setStatus("mandatory")
_Xyplex_ObjectIdentity = ObjectIdentity
xyplex = _Xyplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33)
)
_XSystem_ObjectIdentity = ObjectIdentity
xSystem = _XSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 1)
)


class _SysIdent_Type(DisplayString):
    """Custom type sysIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SysIdent_Type.__name__ = "DisplayString"
_SysIdent_Object = MibScalar
sysIdent = _SysIdent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 1),
    _SysIdent_Type()
)
sysIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIdent.setStatus("mandatory")


class _SysDefineMode_Type(Integer32):
    """Custom type sysDefineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operAndPerm", 2),
          ("permOnly", 1))
    )


_SysDefineMode_Type.__name__ = "Integer32"
_SysDefineMode_Object = MibScalar
sysDefineMode = _SysDefineMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 2),
    _SysDefineMode_Type()
)
sysDefineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDefineMode.setStatus("mandatory")
_SysDateTime_Type = DateTime
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 3),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("mandatory")


class _SysTimeZone_Type(OctetString):
    """Custom type sysTimeZone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysTimeZone_Type.__name__ = "OctetString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 4),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("mandatory")


class _SysLoadSoftware_Type(DisplayString):
    """Custom type sysLoadSoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SysLoadSoftware_Type.__name__ = "DisplayString"
_SysLoadSoftware_Object = MibScalar
sysLoadSoftware = _SysLoadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 5),
    _SysLoadSoftware_Type()
)
sysLoadSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoadSoftware.setStatus("mandatory")


class _SysDump_Type(Integer32):
    """Custom type sysDump based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_SysDump_Type.__name__ = "Integer32"
_SysDump_Object = MibScalar
sysDump = _SysDump_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 6),
    _SysDump_Type()
)
sysDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDump.setStatus("mandatory")


class _SysMaintenancePassword_Type(OctetString):
    """Custom type sysMaintenancePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_SysMaintenancePassword_Type.__name__ = "OctetString"
_SysMaintenancePassword_Object = MibScalar
sysMaintenancePassword = _SysMaintenancePassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 7),
    _SysMaintenancePassword_Type()
)
sysMaintenancePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaintenancePassword.setStatus("mandatory")


class _SysLocalName_Type(DisplayString):
    """Custom type sysLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SysLocalName_Type.__name__ = "DisplayString"
_SysLocalName_Object = MibScalar
sysLocalName = _SysLocalName_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 8),
    _SysLocalName_Type()
)
sysLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocalName.setStatus("mandatory")


class _SysSoftwareVersionType_Type(Integer32):
    """Custom type sysSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("production", 3),
          ("special", 4))
    )


_SysSoftwareVersionType_Type.__name__ = "Integer32"
_SysSoftwareVersionType_Object = MibScalar
sysSoftwareVersionType = _SysSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 9),
    _SysSoftwareVersionType_Type()
)
sysSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersionType.setStatus("mandatory")


class _SysSoftwareVersion_Type(OctetString):
    """Custom type sysSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SysSoftwareVersion_Type.__name__ = "OctetString"
_SysSoftwareVersion_Object = MibScalar
sysSoftwareVersion = _SysSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 10),
    _SysSoftwareVersion_Type()
)
sysSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSoftwareVersion.setStatus("mandatory")
_SysRomVersion_Type = Integer32
_SysRomVersion_Object = MibScalar
sysRomVersion = _SysRomVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 11),
    _SysRomVersion_Type()
)
sysRomVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysRomVersion.setStatus("mandatory")
_SysHardwareType_Type = Integer32
_SysHardwareType_Object = MibScalar
sysHardwareType = _SysHardwareType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 12),
    _SysHardwareType_Type()
)
sysHardwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareType.setStatus("mandatory")
_SysHardwareVersion_Type = Integer32
_SysHardwareVersion_Object = MibScalar
sysHardwareVersion = _SysHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 13),
    _SysHardwareVersion_Type()
)
sysHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHardwareVersion.setStatus("mandatory")


class _SysChassisType_Type(Integer32):
    """Custom type sysChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lanbusII", 3),
          ("mx45xx", 1),
          ("other", 2))
    )


_SysChassisType_Type.__name__ = "Integer32"
_SysChassisType_Object = MibScalar
sysChassisType = _SysChassisType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 14),
    _SysChassisType_Type()
)
sysChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisType.setStatus("mandatory")
_SysChassisVersion_Type = Integer32
_SysChassisVersion_Object = MibScalar
sysChassisVersion = _SysChassisVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 15),
    _SysChassisVersion_Type()
)
sysChassisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisVersion.setStatus("mandatory")


class _SysCrash_Type(Integer32):
    """Custom type sysCrash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysCrash_Type.__name__ = "Integer32"
_SysCrash_Object = MibScalar
sysCrash = _SysCrash_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 16),
    _SysCrash_Type()
)
sysCrash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCrash.setStatus("mandatory")


class _SysInitialize_Type(Integer32):
    """Custom type sysInitialize based on Integer32"""
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
        *(("cancel", 4),
          ("conditionalExecute", 2),
          ("ready", 1),
          ("unconditionalExecute", 3))
    )


_SysInitialize_Type.__name__ = "Integer32"
_SysInitialize_Object = MibScalar
sysInitialize = _SysInitialize_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 17),
    _SysInitialize_Type()
)
sysInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitialize.setStatus("mandatory")


class _SysInitializeDelay_Type(Integer32):
    """Custom type sysInitializeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_SysInitializeDelay_Type.__name__ = "Integer32"
_SysInitializeDelay_Object = MibScalar
sysInitializeDelay = _SysInitializeDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 18),
    _SysInitializeDelay_Type()
)
sysInitializeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitializeDelay.setStatus("mandatory")


class _SysZeroAll_Type(Integer32):
    """Custom type sysZeroAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysZeroAll_Type.__name__ = "Integer32"
_SysZeroAll_Object = MibScalar
sysZeroAll = _SysZeroAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 19),
    _SysZeroAll_Type()
)
sysZeroAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysZeroAll.setStatus("mandatory")


class _SysZeroBase_Type(Integer32):
    """Custom type sysZeroBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_SysZeroBase_Type.__name__ = "Integer32"
_SysZeroBase_Object = MibScalar
sysZeroBase = _SysZeroBase_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 20),
    _SysZeroBase_Type()
)
sysZeroBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysZeroBase.setStatus("mandatory")
_SysZeroBaseTime_Type = TimeTicks
_SysZeroBaseTime_Object = MibScalar
sysZeroBaseTime = _SysZeroBaseTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 21),
    _SysZeroBaseTime_Type()
)
sysZeroBaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysZeroBaseTime.setStatus("mandatory")


class _SysLoaderName_Type(DisplayString):
    """Custom type sysLoaderName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_SysLoaderName_Type.__name__ = "DisplayString"
_SysLoaderName_Object = MibScalar
sysLoaderName = _SysLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 22),
    _SysLoaderName_Type()
)
sysLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderName.setStatus("mandatory")
_SysLoaderAddressType_Type = AddressType
_SysLoaderAddressType_Object = MibScalar
sysLoaderAddressType = _SysLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 23),
    _SysLoaderAddressType_Type()
)
sysLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderAddressType.setStatus("mandatory")
_SysLoaderAddress_Type = OctetString
_SysLoaderAddress_Object = MibScalar
sysLoaderAddress = _SysLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 24),
    _SysLoaderAddress_Type()
)
sysLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLoaderAddress.setStatus("mandatory")
_SysDumperAddressType_Type = AddressType
_SysDumperAddressType_Object = MibScalar
sysDumperAddressType = _SysDumperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 25),
    _SysDumperAddressType_Type()
)
sysDumperAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDumperAddressType.setStatus("mandatory")
_SysDumperAddress_Type = OctetString
_SysDumperAddress_Object = MibScalar
sysDumperAddress = _SysDumperAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 26),
    _SysDumperAddress_Type()
)
sysDumperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDumperAddress.setStatus("mandatory")
_SysResourceLacks_Type = Counter32
_SysResourceLacks_Object = MibScalar
sysResourceLacks = _SysResourceLacks_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 27),
    _SysResourceLacks_Type()
)
sysResourceLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceLacks.setStatus("mandatory")


class _SysChassisState_Type(Integer32):
    """Custom type sysChassisState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 3),
          ("noFault", 2),
          ("notApplicable", 1))
    )


_SysChassisState_Type.__name__ = "Integer32"
_SysChassisState_Object = MibScalar
sysChassisState = _SysChassisState_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 28),
    _SysChassisState_Type()
)
sysChassisState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisState.setStatus("mandatory")
_SysChassisFaultTransitions_Type = Counter32
_SysChassisFaultTransitions_Object = MibScalar
sysChassisFaultTransitions = _SysChassisFaultTransitions_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 29),
    _SysChassisFaultTransitions_Type()
)
sysChassisFaultTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysChassisFaultTransitions.setStatus("mandatory")
_SysResourceNumber_Type = Integer32
_SysResourceNumber_Object = MibScalar
sysResourceNumber = _SysResourceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 30),
    _SysResourceNumber_Type()
)
sysResourceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysResourceNumber.setStatus("mandatory")
_SysFeatureNumber_Type = Integer32
_SysFeatureNumber_Object = MibScalar
sysFeatureNumber = _SysFeatureNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 31),
    _SysFeatureNumber_Type()
)
sysFeatureNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFeatureNumber.setStatus("mandatory")
_ResTable_Object = MibTable
resTable = _ResTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32)
)
if mibBuilder.loadTexts:
    resTable.setStatus("mandatory")
_ResEntry_Object = MibTableRow
resEntry = _ResEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1)
)
resEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "resType"),
)
if mibBuilder.loadTexts:
    resEntry.setStatus("mandatory")


class _ResType_Type(Integer32):
    """Custom type resType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("cpuPercent", 1),
          ("freeMemory", 8),
          ("globalMemoryPercent", 9),
          ("ipFilterCache", 11),
          ("ipFilterTable", 15),
          ("ipPolicyTable", 14),
          ("ipRouteCache", 12),
          ("ipcMessage", 6),
          ("ipxRouteCache", 13),
          ("memoryPercent", 2),
          ("packetBuffer", 5),
          ("phivDecnetRouteCache", 10),
          ("process", 3),
          ("textPool", 7),
          ("timer", 4))
    )


_ResType_Type.__name__ = "Integer32"
_ResType_Object = MibTableColumn
resType = _ResType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 1),
    _ResType_Type()
)
resType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resType.setStatus("mandatory")
_ResCurrent_Type = Gauge32
_ResCurrent_Object = MibTableColumn
resCurrent = _ResCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 2),
    _ResCurrent_Type()
)
resCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resCurrent.setStatus("mandatory")
_ResWorst_Type = Gauge32
_ResWorst_Object = MibTableColumn
resWorst = _ResWorst_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 3),
    _ResWorst_Type()
)
resWorst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resWorst.setStatus("mandatory")
_ResAdminMaximum_Type = Integer32
_ResAdminMaximum_Object = MibTableColumn
resAdminMaximum = _ResAdminMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 4),
    _ResAdminMaximum_Type()
)
resAdminMaximum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resAdminMaximum.setStatus("mandatory")
_ResLacks_Type = Counter32
_ResLacks_Object = MibTableColumn
resLacks = _ResLacks_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 5),
    _ResLacks_Type()
)
resLacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resLacks.setStatus("mandatory")
_ResLackTime_Type = DateTime
_ResLackTime_Object = MibTableColumn
resLackTime = _ResLackTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 6),
    _ResLackTime_Type()
)
resLackTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resLackTime.setStatus("mandatory")
_ResOperMaximum_Type = Integer32
_ResOperMaximum_Object = MibTableColumn
resOperMaximum = _ResOperMaximum_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 32, 1, 7),
    _ResOperMaximum_Type()
)
resOperMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resOperMaximum.setStatus("mandatory")
_FeatTable_Object = MibTable
featTable = _FeatTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33)
)
if mibBuilder.loadTexts:
    featTable.setStatus("mandatory")
_FeatEntry_Object = MibTableRow
featEntry = _FeatEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1)
)
featEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "featType"),
)
if mibBuilder.loadTexts:
    featEntry.setStatus("mandatory")


class _FeatType_Type(Integer32):
    """Custom type featType based on Integer32"""
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
        *(("eventLog", 8),
          ("help", 1),
          ("internetSecurity", 9),
          ("kerberos", 12),
          ("lat", 7),
          ("menu", 5),
          ("multisessions", 6),
          ("rlogin", 14),
          ("scriptServer", 11),
          ("slip", 10),
          ("snmp", 2),
          ("telnet", 13),
          ("tn3270", 4),
          ("xremote", 3))
    )


_FeatType_Type.__name__ = "Integer32"
_FeatType_Object = MibTableColumn
featType = _FeatType_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1, 1),
    _FeatType_Type()
)
featType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    featType.setStatus("mandatory")


class _FeatStatus_Type(Integer32):
    """Custom type featStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FeatStatus_Type.__name__ = "Integer32"
_FeatStatus_Object = MibTableColumn
featStatus = _FeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 33, 1, 2),
    _FeatStatus_Type()
)
featStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    featStatus.setStatus("mandatory")
_BootControl_ObjectIdentity = ObjectIdentity
bootControl = _BootControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 1, 34)
)


class _BootControlLoadInternetFile_Type(DisplayString):
    """Custom type bootControlLoadInternetFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_BootControlLoadInternetFile_Type.__name__ = "DisplayString"
_BootControlLoadInternetFile_Object = MibScalar
bootControlLoadInternetFile = _BootControlLoadInternetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 1),
    _BootControlLoadInternetFile_Type()
)
bootControlLoadInternetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetFile.setStatus("mandatory")
_BootControlLoadInternetServer_Type = IpAddress
_BootControlLoadInternetServer_Object = MibScalar
bootControlLoadInternetServer = _BootControlLoadInternetServer_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 2),
    _BootControlLoadInternetServer_Type()
)
bootControlLoadInternetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetServer.setStatus("mandatory")
_BootControlLoadInternetGateway_Type = IpAddress
_BootControlLoadInternetGateway_Object = MibScalar
bootControlLoadInternetGateway = _BootControlLoadInternetGateway_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 3),
    _BootControlLoadInternetGateway_Type()
)
bootControlLoadInternetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadInternetGateway.setStatus("mandatory")


class _BootControlLoadBootpTftp_Type(Integer32):
    """Custom type bootControlLoadBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadBootpTftp_Type.__name__ = "Integer32"
_BootControlLoadBootpTftp_Object = MibScalar
bootControlLoadBootpTftp = _BootControlLoadBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 4),
    _BootControlLoadBootpTftp_Type()
)
bootControlLoadBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadBootpTftp.setStatus("mandatory")


class _BootControlLoadTftpDirect_Type(Integer32):
    """Custom type bootControlLoadTftpDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadTftpDirect_Type.__name__ = "Integer32"
_BootControlLoadTftpDirect_Object = MibScalar
bootControlLoadTftpDirect = _BootControlLoadTftpDirect_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 5),
    _BootControlLoadTftpDirect_Type()
)
bootControlLoadTftpDirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadTftpDirect.setStatus("mandatory")


class _BootControlLoadLocal_Type(Integer32):
    """Custom type bootControlLoadLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadLocal_Type.__name__ = "Integer32"
_BootControlLoadLocal_Object = MibScalar
bootControlLoadLocal = _BootControlLoadLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 6),
    _BootControlLoadLocal_Type()
)
bootControlLoadLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadLocal.setStatus("mandatory")


class _BootControlLoadMop_Type(Integer32):
    """Custom type bootControlLoadMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadMop_Type.__name__ = "Integer32"
_BootControlLoadMop_Object = MibScalar
bootControlLoadMop = _BootControlLoadMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 7),
    _BootControlLoadMop_Type()
)
bootControlLoadMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadMop.setStatus("mandatory")


class _BootControlLoadProprietary_Type(Integer32):
    """Custom type bootControlLoadProprietary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadProprietary_Type.__name__ = "Integer32"
_BootControlLoadProprietary_Object = MibScalar
bootControlLoadProprietary = _BootControlLoadProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 8),
    _BootControlLoadProprietary_Type()
)
bootControlLoadProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadProprietary.setStatus("mandatory")


class _BootControlLoadRarpTftp_Type(Integer32):
    """Custom type bootControlLoadRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlLoadRarpTftp_Type.__name__ = "Integer32"
_BootControlLoadRarpTftp_Object = MibScalar
bootControlLoadRarpTftp = _BootControlLoadRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 9),
    _BootControlLoadRarpTftp_Type()
)
bootControlLoadRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlLoadRarpTftp.setStatus("mandatory")


class _BootControlDumpBootpTftp_Type(Integer32):
    """Custom type bootControlDumpBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlDumpBootpTftp_Type.__name__ = "Integer32"
_BootControlDumpBootpTftp_Object = MibScalar
bootControlDumpBootpTftp = _BootControlDumpBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 10),
    _BootControlDumpBootpTftp_Type()
)
bootControlDumpBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpBootpTftp.setStatus("mandatory")


class _BootControlDumpLocal_Type(Integer32):
    """Custom type bootControlDumpLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlDumpLocal_Type.__name__ = "Integer32"
_BootControlDumpLocal_Object = MibScalar
bootControlDumpLocal = _BootControlDumpLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 11),
    _BootControlDumpLocal_Type()
)
bootControlDumpLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpLocal.setStatus("mandatory")


class _BootControlDumpMop_Type(Integer32):
    """Custom type bootControlDumpMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlDumpMop_Type.__name__ = "Integer32"
_BootControlDumpMop_Object = MibScalar
bootControlDumpMop = _BootControlDumpMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 12),
    _BootControlDumpMop_Type()
)
bootControlDumpMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpMop.setStatus("mandatory")


class _BootControlDumpProprietary_Type(Integer32):
    """Custom type bootControlDumpProprietary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlDumpProprietary_Type.__name__ = "Integer32"
_BootControlDumpProprietary_Object = MibScalar
bootControlDumpProprietary = _BootControlDumpProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 13),
    _BootControlDumpProprietary_Type()
)
bootControlDumpProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpProprietary.setStatus("mandatory")


class _BootControlDumpRarpTftp_Type(Integer32):
    """Custom type bootControlDumpRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlDumpRarpTftp_Type.__name__ = "Integer32"
_BootControlDumpRarpTftp_Object = MibScalar
bootControlDumpRarpTftp = _BootControlDumpRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 14),
    _BootControlDumpRarpTftp_Type()
)
bootControlDumpRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlDumpRarpTftp.setStatus("mandatory")


class _BootControlParamBootpTftp_Type(Integer32):
    """Custom type bootControlParamBootpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlParamBootpTftp_Type.__name__ = "Integer32"
_BootControlParamBootpTftp_Object = MibScalar
bootControlParamBootpTftp = _BootControlParamBootpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 15),
    _BootControlParamBootpTftp_Type()
)
bootControlParamBootpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamBootpTftp.setStatus("mandatory")


class _BootControlParamLocal_Type(Integer32):
    """Custom type bootControlParamLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlParamLocal_Type.__name__ = "Integer32"
_BootControlParamLocal_Object = MibScalar
bootControlParamLocal = _BootControlParamLocal_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 16),
    _BootControlParamLocal_Type()
)
bootControlParamLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamLocal.setStatus("mandatory")


class _BootControlParamMop_Type(Integer32):
    """Custom type bootControlParamMop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlParamMop_Type.__name__ = "Integer32"
_BootControlParamMop_Object = MibScalar
bootControlParamMop = _BootControlParamMop_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 17),
    _BootControlParamMop_Type()
)
bootControlParamMop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamMop.setStatus("mandatory")


class _BootControlParamProprietary_Type(Integer32):
    """Custom type bootControlParamProprietary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlParamProprietary_Type.__name__ = "Integer32"
_BootControlParamProprietary_Object = MibScalar
bootControlParamProprietary = _BootControlParamProprietary_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 18),
    _BootControlParamProprietary_Type()
)
bootControlParamProprietary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamProprietary.setStatus("mandatory")


class _BootControlParamRarpTftp_Type(Integer32):
    """Custom type bootControlParamRarpTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BootControlParamRarpTftp_Type.__name__ = "Integer32"
_BootControlParamRarpTftp_Object = MibScalar
bootControlParamRarpTftp = _BootControlParamRarpTftp_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 34, 19),
    _BootControlParamRarpTftp_Type()
)
bootControlParamRarpTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootControlParamRarpTftp.setStatus("mandatory")
_SysInstalledMemory_Type = Gauge32
_SysInstalledMemory_Object = MibScalar
sysInstalledMemory = _SysInstalledMemory_Object(
    (1, 3, 6, 1, 4, 1, 33, 1, 35),
    _SysInstalledMemory_Type()
)
sysInstalledMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysInstalledMemory.setStatus("mandatory")
_CharacterDep_ObjectIdentity = ObjectIdentity
characterDep = _CharacterDep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 2)
)
_Lat_ObjectIdentity = ObjectIdentity
lat = _Lat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 3)
)


class _LatAnnounceServices_Type(Integer32):
    """Custom type latAnnounceServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatAnnounceServices_Type.__name__ = "Integer32"
_LatAnnounceServices_Object = MibScalar
latAnnounceServices = _LatAnnounceServices_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 1),
    _LatAnnounceServices_Type()
)
latAnnounceServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latAnnounceServices.setStatus("mandatory")


class _LatCircuitTimer_Type(Integer32):
    """Custom type latCircuitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 200),
    )


_LatCircuitTimer_Type.__name__ = "Integer32"
_LatCircuitTimer_Object = MibScalar
latCircuitTimer = _LatCircuitTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 2),
    _LatCircuitTimer_Type()
)
latCircuitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latCircuitTimer.setStatus("mandatory")


class _LatIdentificationLengthLimit_Type(Integer32):
    """Custom type latIdentificationLengthLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_LatIdentificationLengthLimit_Type.__name__ = "Integer32"
_LatIdentificationLengthLimit_Object = MibScalar
latIdentificationLengthLimit = _LatIdentificationLengthLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 3),
    _LatIdentificationLengthLimit_Type()
)
latIdentificationLengthLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latIdentificationLengthLimit.setStatus("mandatory")


class _LatKeepaliveTimer_Type(Integer32):
    """Custom type latKeepaliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_LatKeepaliveTimer_Type.__name__ = "Integer32"
_LatKeepaliveTimer_Object = MibScalar
latKeepaliveTimer = _LatKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 4),
    _LatKeepaliveTimer_Type()
)
latKeepaliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latKeepaliveTimer.setStatus("mandatory")


class _LatMulticastTimer_Type(Integer32):
    """Custom type latMulticastTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_LatMulticastTimer_Type.__name__ = "Integer32"
_LatMulticastTimer_Object = MibScalar
latMulticastTimer = _LatMulticastTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 5),
    _LatMulticastTimer_Type()
)
latMulticastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latMulticastTimer.setStatus("mandatory")


class _LatNodeLimit_Type(Integer32):
    """Custom type latNodeLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_LatNodeLimit_Type.__name__ = "Integer32"
_LatNodeLimit_Object = MibScalar
latNodeLimit = _LatNodeLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 6),
    _LatNodeLimit_Type()
)
latNodeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeLimit.setStatus("mandatory")


class _LatNumber_Type(Integer32):
    """Custom type latNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_LatNumber_Type.__name__ = "Integer32"
_LatNumber_Object = MibScalar
latNumber = _LatNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 7),
    _LatNumber_Type()
)
latNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNumber.setStatus("mandatory")


class _LatRetransmitLimit_Type(Integer32):
    """Custom type latRetransmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 120),
    )


_LatRetransmitLimit_Type.__name__ = "Integer32"
_LatRetransmitLimit_Object = MibScalar
latRetransmitLimit = _LatRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 8),
    _LatRetransmitLimit_Type()
)
latRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latRetransmitLimit.setStatus("mandatory")


class _LatLocalServiceGroups_Type(OctetString):
    """Custom type latLocalServiceGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatLocalServiceGroups_Type.__name__ = "OctetString"
_LatLocalServiceGroups_Object = MibScalar
latLocalServiceGroups = _LatLocalServiceGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 9),
    _LatLocalServiceGroups_Type()
)
latLocalServiceGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latLocalServiceGroups.setStatus("mandatory")


class _LatGroupPurge_Type(Integer32):
    """Custom type latGroupPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatGroupPurge_Type.__name__ = "Integer32"
_LatGroupPurge_Object = MibScalar
latGroupPurge = _LatGroupPurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 10),
    _LatGroupPurge_Type()
)
latGroupPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latGroupPurge.setStatus("mandatory")


class _LatNodePurge_Type(Integer32):
    """Custom type latNodePurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatNodePurge_Type.__name__ = "Integer32"
_LatNodePurge_Object = MibScalar
latNodePurge = _LatNodePurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 11),
    _LatNodePurge_Type()
)
latNodePurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodePurge.setStatus("mandatory")
_LatNodesRejected_Type = Counter32
_LatNodesRejected_Object = MibScalar
latNodesRejected = _LatNodesRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 12),
    _LatNodesRejected_Type()
)
latNodesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodesRejected.setStatus("mandatory")
_LatInMessages_Type = Counter32
_LatInMessages_Object = MibScalar
latInMessages = _LatInMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 13),
    _LatInMessages_Type()
)
latInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInMessages.setStatus("mandatory")
_LatOutMessages_Type = Counter32
_LatOutMessages_Object = MibScalar
latOutMessages = _LatOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 14),
    _LatOutMessages_Type()
)
latOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latOutMessages.setStatus("mandatory")
_LatInSessionsAccepted_Type = Counter32
_LatInSessionsAccepted_Object = MibScalar
latInSessionsAccepted = _LatInSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 15),
    _LatInSessionsAccepted_Type()
)
latInSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInSessionsAccepted.setStatus("mandatory")
_LatInSessionsRejected_Type = Counter32
_LatInSessionsRejected_Object = MibScalar
latInSessionsRejected = _LatInSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 16),
    _LatInSessionsRejected_Type()
)
latInSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInSessionsRejected.setStatus("mandatory")
_LatAddressChange_Type = Counter32
_LatAddressChange_Object = MibScalar
latAddressChange = _LatAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 17),
    _LatAddressChange_Type()
)
latAddressChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latAddressChange.setStatus("mandatory")
_LatInDuplicates_Type = Counter32
_LatInDuplicates_Object = MibScalar
latInDuplicates = _LatInDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 18),
    _LatInDuplicates_Type()
)
latInDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInDuplicates.setStatus("mandatory")
_LatOutRetransmits_Type = Counter32
_LatOutRetransmits_Object = MibScalar
latOutRetransmits = _LatOutRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 19),
    _LatOutRetransmits_Type()
)
latOutRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latOutRetransmits.setStatus("mandatory")
_LatInBadMessages_Type = Counter32
_LatInBadMessages_Object = MibScalar
latInBadMessages = _LatInBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 20),
    _LatInBadMessages_Type()
)
latInBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadMessages.setStatus("mandatory")
_LatInBadSlots_Type = Counter32
_LatInBadSlots_Object = MibScalar
latInBadSlots = _LatInBadSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 21),
    _LatInBadSlots_Type()
)
latInBadSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadSlots.setStatus("mandatory")
_LatInBadMulticasts_Type = Counter32
_LatInBadMulticasts_Object = MibScalar
latInBadMulticasts = _LatInBadMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 22),
    _LatInBadMulticasts_Type()
)
latInBadMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latInBadMulticasts.setStatus("mandatory")
_LatPortTable_Object = MibTable
latPortTable = _LatPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23)
)
if mibBuilder.loadTexts:
    latPortTable.setStatus("mandatory")
_LatPortEntry_Object = MibTableRow
latPortEntry = _LatPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1)
)
latPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "latPortIndex"),
)
if mibBuilder.loadTexts:
    latPortEntry.setStatus("mandatory")
_LatPortIndex_Type = Integer32
_LatPortIndex_Object = MibTableColumn
latPortIndex = _LatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 1),
    _LatPortIndex_Type()
)
latPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latPortIndex.setStatus("mandatory")


class _LatPortAuthorizedGroups_Type(OctetString):
    """Custom type latPortAuthorizedGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatPortAuthorizedGroups_Type.__name__ = "OctetString"
_LatPortAuthorizedGroups_Object = MibTableColumn
latPortAuthorizedGroups = _LatPortAuthorizedGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 2),
    _LatPortAuthorizedGroups_Type()
)
latPortAuthorizedGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortAuthorizedGroups.setStatus("mandatory")


class _LatPortAutoPrompt_Type(Integer32):
    """Custom type latPortAutoPrompt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatPortAutoPrompt_Type.__name__ = "Integer32"
_LatPortAutoPrompt_Object = MibTableColumn
latPortAutoPrompt = _LatPortAutoPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 3),
    _LatPortAutoPrompt_Type()
)
latPortAutoPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortAutoPrompt.setStatus("mandatory")


class _LatPortCurrentGroups_Type(OctetString):
    """Custom type latPortCurrentGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatPortCurrentGroups_Type.__name__ = "OctetString"
_LatPortCurrentGroups_Object = MibTableColumn
latPortCurrentGroups = _LatPortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 4),
    _LatPortCurrentGroups_Type()
)
latPortCurrentGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortCurrentGroups.setStatus("mandatory")


class _LatPortRemoteModification_Type(Integer32):
    """Custom type latPortRemoteModification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatPortRemoteModification_Type.__name__ = "Integer32"
_LatPortRemoteModification_Object = MibTableColumn
latPortRemoteModification = _LatPortRemoteModification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 23, 1, 5),
    _LatPortRemoteModification_Type()
)
latPortRemoteModification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latPortRemoteModification.setStatus("mandatory")
_LatOfferedServiceTable_Object = MibTable
latOfferedServiceTable = _LatOfferedServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24)
)
if mibBuilder.loadTexts:
    latOfferedServiceTable.setStatus("mandatory")
_LatOfferedServiceEntry_Object = MibTableRow
latOfferedServiceEntry = _LatOfferedServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1)
)
latOfferedServiceEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "latOfferedServiceName"),
)
if mibBuilder.loadTexts:
    latOfferedServiceEntry.setStatus("mandatory")


class _LatOfferedServiceName_Type(DisplayString):
    """Custom type latOfferedServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatOfferedServiceName_Type.__name__ = "DisplayString"
_LatOfferedServiceName_Object = MibTableColumn
latOfferedServiceName = _LatOfferedServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 1),
    _LatOfferedServiceName_Type()
)
latOfferedServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceName.setStatus("mandatory")


class _LatOfferedServiceStatus_Type(Integer32):
    """Custom type latOfferedServiceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_LatOfferedServiceStatus_Type.__name__ = "Integer32"
_LatOfferedServiceStatus_Object = MibTableColumn
latOfferedServiceStatus = _LatOfferedServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 2),
    _LatOfferedServiceStatus_Type()
)
latOfferedServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceStatus.setStatus("mandatory")


class _LatOfferedServiceAllowConnections_Type(Integer32):
    """Custom type latOfferedServiceAllowConnections based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatOfferedServiceAllowConnections_Type.__name__ = "Integer32"
_LatOfferedServiceAllowConnections_Object = MibTableColumn
latOfferedServiceAllowConnections = _LatOfferedServiceAllowConnections_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 3),
    _LatOfferedServiceAllowConnections_Type()
)
latOfferedServiceAllowConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceAllowConnections.setStatus("mandatory")


class _LatOfferedServiceIdentification_Type(DisplayString):
    """Custom type latOfferedServiceIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatOfferedServiceIdentification_Type.__name__ = "DisplayString"
_LatOfferedServiceIdentification_Object = MibTableColumn
latOfferedServiceIdentification = _LatOfferedServiceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 4),
    _LatOfferedServiceIdentification_Type()
)
latOfferedServiceIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceIdentification.setStatus("mandatory")


class _LatOfferedServicePassword_Type(DisplayString):
    """Custom type latOfferedServicePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_LatOfferedServicePassword_Type.__name__ = "DisplayString"
_LatOfferedServicePassword_Object = MibTableColumn
latOfferedServicePassword = _LatOfferedServicePassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 5),
    _LatOfferedServicePassword_Type()
)
latOfferedServicePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServicePassword.setStatus("mandatory")
_LatOfferedServicePortMap_Type = OctetString
_LatOfferedServicePortMap_Object = MibTableColumn
latOfferedServicePortMap = _LatOfferedServicePortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 6),
    _LatOfferedServicePortMap_Type()
)
latOfferedServicePortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServicePortMap.setStatus("mandatory")


class _LatOfferedServiceQueuing_Type(Integer32):
    """Custom type latOfferedServiceQueuing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LatOfferedServiceQueuing_Type.__name__ = "Integer32"
_LatOfferedServiceQueuing_Object = MibTableColumn
latOfferedServiceQueuing = _LatOfferedServiceQueuing_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 24, 1, 7),
    _LatOfferedServiceQueuing_Type()
)
latOfferedServiceQueuing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latOfferedServiceQueuing.setStatus("mandatory")
_LatVisibleServiceTable_Object = MibTable
latVisibleServiceTable = _LatVisibleServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25)
)
if mibBuilder.loadTexts:
    latVisibleServiceTable.setStatus("mandatory")
_LatVisibleServiceEntry_Object = MibTableRow
latVisibleServiceEntry = _LatVisibleServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1)
)
latVisibleServiceEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "latVisibleServiceName"),
)
if mibBuilder.loadTexts:
    latVisibleServiceEntry.setStatus("mandatory")


class _LatVisibleServiceName_Type(DisplayString):
    """Custom type latVisibleServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatVisibleServiceName_Type.__name__ = "DisplayString"
_LatVisibleServiceName_Object = MibTableColumn
latVisibleServiceName = _LatVisibleServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 1),
    _LatVisibleServiceName_Type()
)
latVisibleServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceName.setStatus("mandatory")


class _LatVisibleServiceStatus_Type(Integer32):
    """Custom type latVisibleServiceStatus based on Integer32"""
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
        *(("available", 1),
          ("connected", 6),
          ("reachable", 5),
          ("unavailable", 2),
          ("unknown", 3),
          ("unreachable", 4))
    )


_LatVisibleServiceStatus_Type.__name__ = "Integer32"
_LatVisibleServiceStatus_Object = MibTableColumn
latVisibleServiceStatus = _LatVisibleServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 2),
    _LatVisibleServiceStatus_Type()
)
latVisibleServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceStatus.setStatus("mandatory")


class _LatVisibleServiceNode_Type(DisplayString):
    """Custom type latVisibleServiceNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatVisibleServiceNode_Type.__name__ = "DisplayString"
_LatVisibleServiceNode_Object = MibTableColumn
latVisibleServiceNode = _LatVisibleServiceNode_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 3),
    _LatVisibleServiceNode_Type()
)
latVisibleServiceNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceNode.setStatus("mandatory")
_LatVisibleServiceConnectedSessions_Type = Gauge32
_LatVisibleServiceConnectedSessions_Object = MibTableColumn
latVisibleServiceConnectedSessions = _LatVisibleServiceConnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 4),
    _LatVisibleServiceConnectedSessions_Type()
)
latVisibleServiceConnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceConnectedSessions.setStatus("mandatory")


class _LatVisibleServiceIdentification_Type(DisplayString):
    """Custom type latVisibleServiceIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatVisibleServiceIdentification_Type.__name__ = "DisplayString"
_LatVisibleServiceIdentification_Object = MibTableColumn
latVisibleServiceIdentification = _LatVisibleServiceIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 5),
    _LatVisibleServiceIdentification_Type()
)
latVisibleServiceIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceIdentification.setStatus("mandatory")
_LatVisibleServiceRating_Type = Gauge32
_LatVisibleServiceRating_Object = MibTableColumn
latVisibleServiceRating = _LatVisibleServiceRating_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 25, 1, 6),
    _LatVisibleServiceRating_Type()
)
latVisibleServiceRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latVisibleServiceRating.setStatus("mandatory")
_LatNodeTable_Object = MibTable
latNodeTable = _LatNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26)
)
if mibBuilder.loadTexts:
    latNodeTable.setStatus("mandatory")
_LatNodeEntry_Object = MibTableRow
latNodeEntry = _LatNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1)
)
latNodeEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "latNodeName"),
)
if mibBuilder.loadTexts:
    latNodeEntry.setStatus("mandatory")


class _LatNodeName_Type(DisplayString):
    """Custom type latNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LatNodeName_Type.__name__ = "DisplayString"
_LatNodeName_Object = MibTableColumn
latNodeName = _LatNodeName_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 1),
    _LatNodeName_Type()
)
latNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeName.setStatus("mandatory")


class _LatNodeStatus_Type(Integer32):
    """Custom type latNodeStatus based on Integer32"""
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
        *(("available", 1),
          ("connected", 6),
          ("reachable", 5),
          ("unavailable", 2),
          ("unknown", 3),
          ("unreachable", 4))
    )


_LatNodeStatus_Type.__name__ = "Integer32"
_LatNodeStatus_Object = MibTableColumn
latNodeStatus = _LatNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 2),
    _LatNodeStatus_Type()
)
latNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeStatus.setStatus("mandatory")
_LatNodeConnectedSessions_Type = Gauge32
_LatNodeConnectedSessions_Object = MibTableColumn
latNodeConnectedSessions = _LatNodeConnectedSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 3),
    _LatNodeConnectedSessions_Type()
)
latNodeConnectedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeConnectedSessions.setStatus("mandatory")


class _LatNodeAddress_Type(OctetString):
    """Custom type latNodeAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_LatNodeAddress_Type.__name__ = "OctetString"
_LatNodeAddress_Object = MibTableColumn
latNodeAddress = _LatNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 4),
    _LatNodeAddress_Type()
)
latNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeAddress.setStatus("mandatory")
_LatNodeDataLinkFrame_Type = Integer32
_LatNodeDataLinkFrame_Object = MibTableColumn
latNodeDataLinkFrame = _LatNodeDataLinkFrame_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 5),
    _LatNodeDataLinkFrame_Type()
)
latNodeDataLinkFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeDataLinkFrame.setStatus("mandatory")


class _LatNodeIdentification_Type(DisplayString):
    """Custom type latNodeIdentification based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_LatNodeIdentification_Type.__name__ = "DisplayString"
_LatNodeIdentification_Object = MibTableColumn
latNodeIdentification = _LatNodeIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 6),
    _LatNodeIdentification_Type()
)
latNodeIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeIdentification.setStatus("mandatory")


class _LatNodeGroups_Type(OctetString):
    """Custom type latNodeGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_LatNodeGroups_Type.__name__ = "OctetString"
_LatNodeGroups_Object = MibTableColumn
latNodeGroups = _LatNodeGroups_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 7),
    _LatNodeGroups_Type()
)
latNodeGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeGroups.setStatus("mandatory")
_LatNodeServiceNumber_Type = Gauge32
_LatNodeServiceNumber_Object = MibTableColumn
latNodeServiceNumber = _LatNodeServiceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 8),
    _LatNodeServiceNumber_Type()
)
latNodeServiceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeServiceNumber.setStatus("mandatory")


class _LatNodeZero_Type(Integer32):
    """Custom type latNodeZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_LatNodeZero_Type.__name__ = "Integer32"
_LatNodeZero_Object = MibTableColumn
latNodeZero = _LatNodeZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 9),
    _LatNodeZero_Type()
)
latNodeZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    latNodeZero.setStatus("mandatory")
_LatNodeZeroTime_Type = TimeTicks
_LatNodeZeroTime_Object = MibTableColumn
latNodeZeroTime = _LatNodeZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 10),
    _LatNodeZeroTime_Type()
)
latNodeZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeZeroTime.setStatus("mandatory")
_LatNodeInMessages_Type = Counter32
_LatNodeInMessages_Object = MibTableColumn
latNodeInMessages = _LatNodeInMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 11),
    _LatNodeInMessages_Type()
)
latNodeInMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInMessages.setStatus("mandatory")
_LatNodeOutMessages_Type = Counter32
_LatNodeOutMessages_Object = MibTableColumn
latNodeOutMessages = _LatNodeOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 12),
    _LatNodeOutMessages_Type()
)
latNodeOutMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutMessages.setStatus("mandatory")
_LatNodeInSlots_Type = Counter32
_LatNodeInSlots_Object = MibTableColumn
latNodeInSlots = _LatNodeInSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 13),
    _LatNodeInSlots_Type()
)
latNodeInSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSlots.setStatus("mandatory")
_LatNodeOutSlots_Type = Counter32
_LatNodeOutSlots_Object = MibTableColumn
latNodeOutSlots = _LatNodeOutSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 14),
    _LatNodeOutSlots_Type()
)
latNodeOutSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutSlots.setStatus("mandatory")
_LatNodeInBytes_Type = Counter32
_LatNodeInBytes_Object = MibTableColumn
latNodeInBytes = _LatNodeInBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 15),
    _LatNodeInBytes_Type()
)
latNodeInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBytes.setStatus("mandatory")
_LatNodeOutBytes_Type = Counter32
_LatNodeOutBytes_Object = MibTableColumn
latNodeOutBytes = _LatNodeOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 16),
    _LatNodeOutBytes_Type()
)
latNodeOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutBytes.setStatus("mandatory")
_LatNodeAddressChange_Type = Counter32
_LatNodeAddressChange_Object = MibTableColumn
latNodeAddressChange = _LatNodeAddressChange_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 17),
    _LatNodeAddressChange_Type()
)
latNodeAddressChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeAddressChange.setStatus("mandatory")
_LatNodeInDuplicates_Type = Counter32
_LatNodeInDuplicates_Object = MibTableColumn
latNodeInDuplicates = _LatNodeInDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 18),
    _LatNodeInDuplicates_Type()
)
latNodeInDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInDuplicates.setStatus("mandatory")
_LatNodeOutRetransmits_Type = Counter32
_LatNodeOutRetransmits_Object = MibTableColumn
latNodeOutRetransmits = _LatNodeOutRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 19),
    _LatNodeOutRetransmits_Type()
)
latNodeOutRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeOutRetransmits.setStatus("mandatory")
_LatNodeInBadMessages_Type = Counter32
_LatNodeInBadMessages_Object = MibTableColumn
latNodeInBadMessages = _LatNodeInBadMessages_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 20),
    _LatNodeInBadMessages_Type()
)
latNodeInBadMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBadMessages.setStatus("mandatory")
_LatNodeInBadSlots_Type = Counter32
_LatNodeInBadSlots_Object = MibTableColumn
latNodeInBadSlots = _LatNodeInBadSlots_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 21),
    _LatNodeInBadSlots_Type()
)
latNodeInBadSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInBadSlots.setStatus("mandatory")
_LatNodeInSessionsAccepted_Type = Counter32
_LatNodeInSessionsAccepted_Object = MibTableColumn
latNodeInSessionsAccepted = _LatNodeInSessionsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 22),
    _LatNodeInSessionsAccepted_Type()
)
latNodeInSessionsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSessionsAccepted.setStatus("mandatory")
_LatNodeInSessionsRejected_Type = Counter32
_LatNodeInSessionsRejected_Object = MibTableColumn
latNodeInSessionsRejected = _LatNodeInSessionsRejected_Object(
    (1, 3, 6, 1, 4, 1, 33, 3, 26, 1, 23),
    _LatNodeInSessionsRejected_Type()
)
latNodeInSessionsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latNodeInSessionsRejected.setStatus("mandatory")
_XInternetDep_ObjectIdentity = ObjectIdentity
xInternetDep = _XInternetDep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 4)
)
_BootServer_ObjectIdentity = ObjectIdentity
bootServer = _BootServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6)
)
_BsBasic_ObjectIdentity = ObjectIdentity
bsBasic = _BsBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 1)
)


class _BasicLogLimit_Type(Integer32):
    """Custom type basicLogLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BasicLogLimit_Type.__name__ = "Integer32"
_BasicLogLimit_Object = MibScalar
basicLogLimit = _BasicLogLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 1),
    _BasicLogLimit_Type()
)
basicLogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLogLimit.setStatus("mandatory")


class _BasicActiveLimit_Type(Integer32):
    """Custom type basicActiveLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_BasicActiveLimit_Type.__name__ = "Integer32"
_BasicActiveLimit_Object = MibScalar
basicActiveLimit = _BasicActiveLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 2),
    _BasicActiveLimit_Type()
)
basicActiveLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicActiveLimit.setStatus("mandatory")
_BasicActiveNumber_Type = Gauge32
_BasicActiveNumber_Object = MibScalar
basicActiveNumber = _BasicActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 3),
    _BasicActiveNumber_Type()
)
basicActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveNumber.setStatus("mandatory")
_BasicClientNumber_Type = Gauge32
_BasicClientNumber_Object = MibScalar
basicClientNumber = _BasicClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 4),
    _BasicClientNumber_Type()
)
basicClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicClientNumber.setStatus("mandatory")
_BasicOffersSent_Type = Counter32
_BasicOffersSent_Object = MibScalar
basicOffersSent = _BasicOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 5),
    _BasicOffersSent_Type()
)
basicOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicOffersSent.setStatus("mandatory")
_BasicEventTotal_Type = Gauge32
_BasicEventTotal_Object = MibScalar
basicEventTotal = _BasicEventTotal_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 6),
    _BasicEventTotal_Type()
)
basicEventTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicEventTotal.setStatus("mandatory")


class _BasicEventPurge_Type(Integer32):
    """Custom type basicEventPurge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicEventPurge_Type.__name__ = "Integer32"
_BasicEventPurge_Object = MibScalar
basicEventPurge = _BasicEventPurge_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 7),
    _BasicEventPurge_Type()
)
basicEventPurge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicEventPurge.setStatus("mandatory")
_ActiveTable_Object = MibTable
activeTable = _ActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8)
)
if mibBuilder.loadTexts:
    activeTable.setStatus("mandatory")
_ActiveEntry_Object = MibTableRow
activeEntry = _ActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1)
)
activeEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "activeIdentificationType"),
    (0, "XYPLEX-CONCATENATED-MIB", "activeIdentification"),
)
if mibBuilder.loadTexts:
    activeEntry.setStatus("mandatory")
_ActiveIdentificationType_Type = AddressType
_ActiveIdentificationType_Object = MibTableColumn
activeIdentificationType = _ActiveIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 1),
    _ActiveIdentificationType_Type()
)
activeIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeIdentificationType.setStatus("mandatory")


class _ActiveIdentification_Type(OctetString):
    """Custom type activeIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ActiveIdentification_Type.__name__ = "OctetString"
_ActiveIdentification_Object = MibTableColumn
activeIdentification = _ActiveIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 2),
    _ActiveIdentification_Type()
)
activeIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeIdentification.setStatus("mandatory")


class _ActiveFunction_Type(Integer32):
    """Custom type activeFunction based on Integer32"""
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
        *(("dump", 3),
          ("imageUpdate", 4),
          ("load", 2),
          ("parameterStore", 1))
    )


_ActiveFunction_Type.__name__ = "Integer32"
_ActiveFunction_Object = MibTableColumn
activeFunction = _ActiveFunction_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 3),
    _ActiveFunction_Type()
)
activeFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFunction.setStatus("mandatory")


class _ActiveSoftwareVersionType_Type(Integer32):
    """Custom type activeSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("notApplicable", 5),
          ("production", 3),
          ("special", 4))
    )


_ActiveSoftwareVersionType_Type.__name__ = "Integer32"
_ActiveSoftwareVersionType_Object = MibTableColumn
activeSoftwareVersionType = _ActiveSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 4),
    _ActiveSoftwareVersionType_Type()
)
activeSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeSoftwareVersionType.setStatus("mandatory")


class _ActiveSoftwareVersion_Type(OctetString):
    """Custom type activeSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ActiveSoftwareVersion_Type.__name__ = "OctetString"
_ActiveSoftwareVersion_Object = MibTableColumn
activeSoftwareVersion = _ActiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 5),
    _ActiveSoftwareVersion_Type()
)
activeSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeSoftwareVersion.setStatus("mandatory")
_ActiveParameterVersion_Type = Integer32
_ActiveParameterVersion_Object = MibTableColumn
activeParameterVersion = _ActiveParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 6),
    _ActiveParameterVersion_Type()
)
activeParameterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeParameterVersion.setStatus("mandatory")
_ActiveCurrentSequence_Type = Integer32
_ActiveCurrentSequence_Object = MibTableColumn
activeCurrentSequence = _ActiveCurrentSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 7),
    _ActiveCurrentSequence_Type()
)
activeCurrentSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeCurrentSequence.setStatus("mandatory")
_ActiveBytesRemaining_Type = Integer32
_ActiveBytesRemaining_Object = MibTableColumn
activeBytesRemaining = _ActiveBytesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 8),
    _ActiveBytesRemaining_Type()
)
activeBytesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeBytesRemaining.setStatus("mandatory")


class _ActiveFile_Type(DisplayString):
    """Custom type activeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ActiveFile_Type.__name__ = "DisplayString"
_ActiveFile_Object = MibTableColumn
activeFile = _ActiveFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 9),
    _ActiveFile_Type()
)
activeFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeFile.setStatus("mandatory")


class _ActiveStatus_Type(Integer32):
    """Custom type activeStatus based on Integer32"""
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
        *(("badFileData", 5),
          ("deviceWriteProtected", 6),
          ("fileSystemError", 11),
          ("fileTooLarge", 2),
          ("none", 1),
          ("notExecutableFile", 4),
          ("notImageFile", 3),
          ("operationTimeout", 7),
          ("protocolError", 10),
          ("remoteFileAccessViolation", 9),
          ("remoteFileNotFound", 8),
          ("success", 13),
          ("temporaryResourceConflict", 12))
    )


_ActiveStatus_Type.__name__ = "Integer32"
_ActiveStatus_Object = MibTableColumn
activeStatus = _ActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 10),
    _ActiveStatus_Type()
)
activeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeStatus.setStatus("mandatory")


class _ActiveState_Type(Integer32):
    """Custom type activeState based on Integer32"""
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
        *(("cleanup", 10),
          ("closeFile", 9),
          ("closePartner", 8),
          ("done", 11),
          ("error", 12),
          ("idle", 1),
          ("internal1", 2),
          ("internal2", 3),
          ("openFile", 5),
          ("openPartner", 4),
          ("receivePartner", 6),
          ("writeFile", 7))
    )


_ActiveState_Type.__name__ = "Integer32"
_ActiveState_Object = MibTableColumn
activeState = _ActiveState_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 8, 1, 11),
    _ActiveState_Type()
)
activeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeState.setStatus("mandatory")
_ClientTable_Object = MibTable
clientTable = _ClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9)
)
if mibBuilder.loadTexts:
    clientTable.setStatus("mandatory")
_ClientEntry_Object = MibTableRow
clientEntry = _ClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1)
)
clientEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "clientIdentificationType"),
    (0, "XYPLEX-CONCATENATED-MIB", "clientIdentification"),
)
if mibBuilder.loadTexts:
    clientEntry.setStatus("mandatory")
_ClientIdentificationType_Type = AddressType
_ClientIdentificationType_Object = MibTableColumn
clientIdentificationType = _ClientIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 1),
    _ClientIdentificationType_Type()
)
clientIdentificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIdentificationType.setStatus("mandatory")


class _ClientIdentification_Type(OctetString):
    """Custom type clientIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ClientIdentification_Type.__name__ = "OctetString"
_ClientIdentification_Object = MibTableColumn
clientIdentification = _ClientIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 2),
    _ClientIdentification_Type()
)
clientIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientIdentification.setStatus("mandatory")


class _ClientEntryStatus_Type(Integer32):
    """Custom type clientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ClientEntryStatus_Type.__name__ = "Integer32"
_ClientEntryStatus_Object = MibTableColumn
clientEntryStatus = _ClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 3),
    _ClientEntryStatus_Type()
)
clientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientEntryStatus.setStatus("mandatory")


class _ClientName_Type(DisplayString):
    """Custom type clientName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientName_Type.__name__ = "DisplayString"
_ClientName_Object = MibTableColumn
clientName = _ClientName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 4),
    _ClientName_Type()
)
clientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientName.setStatus("mandatory")


class _ClientLoadFile_Type(DisplayString):
    """Custom type clientLoadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientLoadFile_Type.__name__ = "DisplayString"
_ClientLoadFile_Object = MibTableColumn
clientLoadFile = _ClientLoadFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 5),
    _ClientLoadFile_Type()
)
clientLoadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLoadFile.setStatus("mandatory")


class _ClientDiagnosticFile_Type(DisplayString):
    """Custom type clientDiagnosticFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ClientDiagnosticFile_Type.__name__ = "DisplayString"
_ClientDiagnosticFile_Object = MibTableColumn
clientDiagnosticFile = _ClientDiagnosticFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 6),
    _ClientDiagnosticFile_Type()
)
clientDiagnosticFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDiagnosticFile.setStatus("mandatory")


class _ClientLoadService_Type(Integer32):
    """Custom type clientLoadService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientLoadService_Type.__name__ = "Integer32"
_ClientLoadService_Object = MibTableColumn
clientLoadService = _ClientLoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 7),
    _ClientLoadService_Type()
)
clientLoadService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientLoadService.setStatus("mandatory")


class _ClientDumpService_Type(Integer32):
    """Custom type clientDumpService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ClientDumpService_Type.__name__ = "Integer32"
_ClientDumpService_Object = MibTableColumn
clientDumpService = _ClientDumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 9, 1, 8),
    _ClientDumpService_Type()
)
clientDumpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clientDumpService.setStatus("mandatory")
_NamedTable_Object = MibTable
namedTable = _NamedTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10)
)
if mibBuilder.loadTexts:
    namedTable.setStatus("mandatory")
_NamedEntry_Object = MibTableRow
namedEntry = _NamedEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1)
)
namedEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "namedName"),
)
if mibBuilder.loadTexts:
    namedEntry.setStatus("mandatory")
_NamedIdentificationType_Type = AddressType
_NamedIdentificationType_Object = MibTableColumn
namedIdentificationType = _NamedIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 1),
    _NamedIdentificationType_Type()
)
namedIdentificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedIdentificationType.setStatus("mandatory")


class _NamedIdentification_Type(OctetString):
    """Custom type namedIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_NamedIdentification_Type.__name__ = "OctetString"
_NamedIdentification_Object = MibTableColumn
namedIdentification = _NamedIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 2),
    _NamedIdentification_Type()
)
namedIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedIdentification.setStatus("mandatory")


class _NamedEntryStatus_Type(Integer32):
    """Custom type namedEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NamedEntryStatus_Type.__name__ = "Integer32"
_NamedEntryStatus_Object = MibTableColumn
namedEntryStatus = _NamedEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 3),
    _NamedEntryStatus_Type()
)
namedEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedEntryStatus.setStatus("mandatory")


class _NamedName_Type(DisplayString):
    """Custom type namedName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedName_Type.__name__ = "DisplayString"
_NamedName_Object = MibTableColumn
namedName = _NamedName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 4),
    _NamedName_Type()
)
namedName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedName.setStatus("mandatory")


class _NamedLoadFile_Type(DisplayString):
    """Custom type namedLoadFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedLoadFile_Type.__name__ = "DisplayString"
_NamedLoadFile_Object = MibTableColumn
namedLoadFile = _NamedLoadFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 5),
    _NamedLoadFile_Type()
)
namedLoadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedLoadFile.setStatus("mandatory")


class _NamedDiagnosticFile_Type(DisplayString):
    """Custom type namedDiagnosticFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NamedDiagnosticFile_Type.__name__ = "DisplayString"
_NamedDiagnosticFile_Object = MibTableColumn
namedDiagnosticFile = _NamedDiagnosticFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 6),
    _NamedDiagnosticFile_Type()
)
namedDiagnosticFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedDiagnosticFile.setStatus("mandatory")


class _NamedLoadService_Type(Integer32):
    """Custom type namedLoadService based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NamedLoadService_Type.__name__ = "Integer32"
_NamedLoadService_Object = MibTableColumn
namedLoadService = _NamedLoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 7),
    _NamedLoadService_Type()
)
namedLoadService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedLoadService.setStatus("mandatory")


class _NamedDumpService_Type(Integer32):
    """Custom type namedDumpService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NamedDumpService_Type.__name__ = "Integer32"
_NamedDumpService_Object = MibTableColumn
namedDumpService = _NamedDumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 10, 1, 8),
    _NamedDumpService_Type()
)
namedDumpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    namedDumpService.setStatus("mandatory")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1)
)
eventEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")
_EventIndex_Type = Integer32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventText_Type(DisplayString):
    """Custom type eventText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_EventText_Type.__name__ = "DisplayString"
_EventText_Object = MibTableColumn
eventText = _EventText_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 11, 1, 2),
    _EventText_Type()
)
eventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventText.setStatus("mandatory")
_BasicDeviceNumber_Type = Integer32
_BasicDeviceNumber_Object = MibScalar
basicDeviceNumber = _BasicDeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 12),
    _BasicDeviceNumber_Type()
)
basicDeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicDeviceNumber.setStatus("mandatory")
_DeviceTable_Object = MibTable
deviceTable = _DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13)
)
if mibBuilder.loadTexts:
    deviceTable.setStatus("mandatory")
_DeviceEntry_Object = MibTableRow
deviceEntry = _DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1)
)
deviceEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "deviceIndex"),
)
if mibBuilder.loadTexts:
    deviceEntry.setStatus("mandatory")
_DeviceIndex_Type = Integer32
_DeviceIndex_Object = MibTableColumn
deviceIndex = _DeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 1),
    _DeviceIndex_Type()
)
deviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceIndex.setStatus("mandatory")


class _DeviceName_Type(DisplayString):
    """Custom type deviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DeviceName_Type.__name__ = "DisplayString"
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 2),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")


class _DeviceDescr_Type(DisplayString):
    """Custom type deviceDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DeviceDescr_Type.__name__ = "DisplayString"
_DeviceDescr_Object = MibTableColumn
deviceDescr = _DeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 3),
    _DeviceDescr_Type()
)
deviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDescr.setStatus("mandatory")


class _DeviceOperation_Type(Integer32):
    """Custom type deviceOperation based on Integer32"""
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
        *(("format", 3),
          ("idle", 4),
          ("read", 1),
          ("write", 2))
    )


_DeviceOperation_Type.__name__ = "Integer32"
_DeviceOperation_Object = MibTableColumn
deviceOperation = _DeviceOperation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 4),
    _DeviceOperation_Type()
)
deviceOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOperation.setStatus("mandatory")


class _DeviceFormat_Type(Integer32):
    """Custom type deviceFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("formatted", 2),
          ("unformatted", 1),
          ("unknown", 3))
    )


_DeviceFormat_Type.__name__ = "Integer32"
_DeviceFormat_Object = MibTableColumn
deviceFormat = _DeviceFormat_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 5),
    _DeviceFormat_Type()
)
deviceFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceFormat.setStatus("mandatory")


class _DeviceProtection_Type(Integer32):
    """Custom type deviceProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 3),
          ("write-enabled", 1),
          ("write-protected", 2))
    )


_DeviceProtection_Type.__name__ = "Integer32"
_DeviceProtection_Object = MibTableColumn
deviceProtection = _DeviceProtection_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 6),
    _DeviceProtection_Type()
)
deviceProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceProtection.setStatus("mandatory")


class _DeviceFormatMedium_Type(Integer32):
    """Custom type deviceFormatMedium based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_DeviceFormatMedium_Type.__name__ = "Integer32"
_DeviceFormatMedium_Object = MibTableColumn
deviceFormatMedium = _DeviceFormatMedium_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 7),
    _DeviceFormatMedium_Type()
)
deviceFormatMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceFormatMedium.setStatus("mandatory")


class _DeviceGetFile_Type(Integer32):
    """Custom type deviceGetFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_DeviceGetFile_Type.__name__ = "Integer32"
_DeviceGetFile_Object = MibTableColumn
deviceGetFile = _DeviceGetFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 8),
    _DeviceGetFile_Type()
)
deviceGetFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFile.setStatus("mandatory")
_DeviceGetFileHostIdentificationType_Type = AddressType
_DeviceGetFileHostIdentificationType_Object = MibTableColumn
deviceGetFileHostIdentificationType = _DeviceGetFileHostIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 9),
    _DeviceGetFileHostIdentificationType_Type()
)
deviceGetFileHostIdentificationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileHostIdentificationType.setStatus("mandatory")


class _DeviceGetFileHostIdentification_Type(OctetString):
    """Custom type deviceGetFileHostIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_DeviceGetFileHostIdentification_Type.__name__ = "OctetString"
_DeviceGetFileHostIdentification_Object = MibTableColumn
deviceGetFileHostIdentification = _DeviceGetFileHostIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 10),
    _DeviceGetFileHostIdentification_Type()
)
deviceGetFileHostIdentification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileHostIdentification.setStatus("mandatory")


class _DeviceGetFileName_Type(DisplayString):
    """Custom type deviceGetFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_DeviceGetFileName_Type.__name__ = "DisplayString"
_DeviceGetFileName_Object = MibTableColumn
deviceGetFileName = _DeviceGetFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 1, 13, 1, 11),
    _DeviceGetFileName_Type()
)
deviceGetFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceGetFileName.setStatus("mandatory")
_Dump_ObjectIdentity = ObjectIdentity
dump = _Dump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 2)
)


class _DumpService_Type(Integer32):
    """Custom type dumpService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DumpService_Type.__name__ = "Integer32"
_DumpService_Object = MibScalar
dumpService = _DumpService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 1),
    _DumpService_Type()
)
dumpService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpService.setStatus("mandatory")


class _DumpDrive_Type(Integer32):
    """Custom type dumpDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DumpDrive_Type.__name__ = "Integer32"
_DumpDrive_Object = MibScalar
dumpDrive = _DumpDrive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 2),
    _DumpDrive_Type()
)
dumpDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpDrive.setStatus("mandatory")


class _DumpMerit_Type(Integer32):
    """Custom type dumpMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DumpMerit_Type.__name__ = "Integer32"
_DumpMerit_Object = MibScalar
dumpMerit = _DumpMerit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 3),
    _DumpMerit_Type()
)
dumpMerit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpMerit.setStatus("mandatory")


class _DumpSize_Type(Integer32):
    """Custom type dumpSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("small", 1))
    )


_DumpSize_Type.__name__ = "Integer32"
_DumpSize_Object = MibScalar
dumpSize = _DumpSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 4),
    _DumpSize_Type()
)
dumpSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpSize.setStatus("mandatory")
_DumpCompleted_Type = Counter32
_DumpCompleted_Object = MibScalar
dumpCompleted = _DumpCompleted_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 5),
    _DumpCompleted_Type()
)
dumpCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpCompleted.setStatus("mandatory")
_DumpActive_Type = Gauge32
_DumpActive_Object = MibScalar
dumpActive = _DumpActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 6),
    _DumpActive_Type()
)
dumpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpActive.setStatus("mandatory")
_DumpFileNumber_Type = Gauge32
_DumpFileNumber_Object = MibScalar
dumpFileNumber = _DumpFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 7),
    _DumpFileNumber_Type()
)
dumpFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileNumber.setStatus("mandatory")
_DumpFileTable_Object = MibTable
dumpFileTable = _DumpFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8)
)
if mibBuilder.loadTexts:
    dumpFileTable.setStatus("mandatory")
_DumpFileEntry_Object = MibTableRow
dumpFileEntry = _DumpFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1)
)
dumpFileEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "dumpFileIdentificationType"),
    (0, "XYPLEX-CONCATENATED-MIB", "dumpFileIdentification"),
)
if mibBuilder.loadTexts:
    dumpFileEntry.setStatus("mandatory")
_DumpFileIdentificationType_Type = AddressType
_DumpFileIdentificationType_Object = MibTableColumn
dumpFileIdentificationType = _DumpFileIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 1),
    _DumpFileIdentificationType_Type()
)
dumpFileIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileIdentificationType.setStatus("mandatory")


class _DumpFileIdentification_Type(OctetString):
    """Custom type dumpFileIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_DumpFileIdentification_Type.__name__ = "OctetString"
_DumpFileIdentification_Object = MibTableColumn
dumpFileIdentification = _DumpFileIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 2),
    _DumpFileIdentification_Type()
)
dumpFileIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileIdentification.setStatus("mandatory")


class _DumpFileEntryStatus_Type(Integer32):
    """Custom type dumpFileEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_DumpFileEntryStatus_Type.__name__ = "Integer32"
_DumpFileEntryStatus_Object = MibTableColumn
dumpFileEntryStatus = _DumpFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 3),
    _DumpFileEntryStatus_Type()
)
dumpFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dumpFileEntryStatus.setStatus("mandatory")
_DumpFileCreation_Type = DateTime
_DumpFileCreation_Object = MibTableColumn
dumpFileCreation = _DumpFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 4),
    _DumpFileCreation_Type()
)
dumpFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileCreation.setStatus("mandatory")
_DumpFileSize_Type = Integer32
_DumpFileSize_Object = MibTableColumn
dumpFileSize = _DumpFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 2, 8, 1, 5),
    _DumpFileSize_Type()
)
dumpFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dumpFileSize.setStatus("mandatory")
_Load_ObjectIdentity = ObjectIdentity
load = _Load_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 3)
)


class _LoadService_Type(Integer32):
    """Custom type loadService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_LoadService_Type.__name__ = "Integer32"
_LoadService_Object = MibScalar
loadService = _LoadService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 1),
    _LoadService_Type()
)
loadService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadService.setStatus("mandatory")


class _LoadMerit_Type(Integer32):
    """Custom type loadMerit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_LoadMerit_Type.__name__ = "Integer32"
_LoadMerit_Object = MibScalar
loadMerit = _LoadMerit_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 2),
    _LoadMerit_Type()
)
loadMerit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loadMerit.setStatus("mandatory")
_LoadCompleted_Type = Counter32
_LoadCompleted_Object = MibScalar
loadCompleted = _LoadCompleted_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 3),
    _LoadCompleted_Type()
)
loadCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadCompleted.setStatus("mandatory")
_LoadActive_Type = Gauge32
_LoadActive_Object = MibScalar
loadActive = _LoadActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 4),
    _LoadActive_Type()
)
loadActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadActive.setStatus("mandatory")
_LoadFileNumber_Type = Gauge32
_LoadFileNumber_Object = MibScalar
loadFileNumber = _LoadFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 5),
    _LoadFileNumber_Type()
)
loadFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileNumber.setStatus("mandatory")
_LoadFileTable_Object = MibTable
loadFileTable = _LoadFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6)
)
if mibBuilder.loadTexts:
    loadFileTable.setStatus("mandatory")
_LoadFileEntry_Object = MibTableRow
loadFileEntry = _LoadFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1)
)
loadFileEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "loadFileName"),
)
if mibBuilder.loadTexts:
    loadFileEntry.setStatus("mandatory")


class _LoadFileName_Type(DisplayString):
    """Custom type loadFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_LoadFileName_Type.__name__ = "DisplayString"
_LoadFileName_Object = MibTableColumn
loadFileName = _LoadFileName_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 1),
    _LoadFileName_Type()
)
loadFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileName.setStatus("mandatory")
_LoadFileCreation_Type = DateTime
_LoadFileCreation_Object = MibTableColumn
loadFileCreation = _LoadFileCreation_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 2),
    _LoadFileCreation_Type()
)
loadFileCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileCreation.setStatus("mandatory")
_LoadFileSize_Type = Integer32
_LoadFileSize_Object = MibTableColumn
loadFileSize = _LoadFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 3),
    _LoadFileSize_Type()
)
loadFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSize.setStatus("mandatory")


class _LoadFileSoftwareVersionType_Type(Integer32):
    """Custom type loadFileSoftwareVersionType based on Integer32"""
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
        *(("alpha", 1),
          ("beta", 2),
          ("production", 3),
          ("special", 4))
    )


_LoadFileSoftwareVersionType_Type.__name__ = "Integer32"
_LoadFileSoftwareVersionType_Object = MibTableColumn
loadFileSoftwareVersionType = _LoadFileSoftwareVersionType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 4),
    _LoadFileSoftwareVersionType_Type()
)
loadFileSoftwareVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSoftwareVersionType.setStatus("mandatory")


class _LoadFileSoftwareVersion_Type(OctetString):
    """Custom type loadFileSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_LoadFileSoftwareVersion_Type.__name__ = "OctetString"
_LoadFileSoftwareVersion_Object = MibTableColumn
loadFileSoftwareVersion = _LoadFileSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 3, 6, 1, 5),
    _LoadFileSoftwareVersion_Type()
)
loadFileSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadFileSoftwareVersion.setStatus("mandatory")
_Param_ObjectIdentity = ObjectIdentity
param = _Param_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 6, 4)
)


class _ParamService_Type(Integer32):
    """Custom type paramService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamService_Type.__name__ = "Integer32"
_ParamService_Object = MibScalar
paramService = _ParamService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 1),
    _ParamService_Type()
)
paramService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramService.setStatus("mandatory")


class _ParamDefaultService_Type(Integer32):
    """Custom type paramDefaultService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamDefaultService_Type.__name__ = "Integer32"
_ParamDefaultService_Object = MibScalar
paramDefaultService = _ParamDefaultService_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 2),
    _ParamDefaultService_Type()
)
paramDefaultService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDefaultService.setStatus("mandatory")


class _ParamDrive_Type(Integer32):
    """Custom type paramDrive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ParamDrive_Type.__name__ = "Integer32"
_ParamDrive_Object = MibScalar
paramDrive = _ParamDrive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 3),
    _ParamDrive_Type()
)
paramDrive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramDrive.setStatus("mandatory")
_ParamActive_Type = Gauge32
_ParamActive_Object = MibScalar
paramActive = _ParamActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 4),
    _ParamActive_Type()
)
paramActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramActive.setStatus("mandatory")
_ParamStorageActive_Type = Gauge32
_ParamStorageActive_Object = MibScalar
paramStorageActive = _ParamStorageActive_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 5),
    _ParamStorageActive_Type()
)
paramStorageActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramStorageActive.setStatus("mandatory")
_ParamFileNumber_Type = Gauge32
_ParamFileNumber_Object = MibScalar
paramFileNumber = _ParamFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 6),
    _ParamFileNumber_Type()
)
paramFileNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileNumber.setStatus("mandatory")
_ParamFileTable_Object = MibTable
paramFileTable = _ParamFileTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7)
)
if mibBuilder.loadTexts:
    paramFileTable.setStatus("mandatory")
_ParamFileEntry_Object = MibTableRow
paramFileEntry = _ParamFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1)
)
paramFileEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "paramFileIdentificationType"),
    (0, "XYPLEX-CONCATENATED-MIB", "paramFileIdentification"),
)
if mibBuilder.loadTexts:
    paramFileEntry.setStatus("mandatory")
_ParamFileIdentificationType_Type = AddressType
_ParamFileIdentificationType_Object = MibTableColumn
paramFileIdentificationType = _ParamFileIdentificationType_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 1),
    _ParamFileIdentificationType_Type()
)
paramFileIdentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileIdentificationType.setStatus("mandatory")


class _ParamFileIdentification_Type(OctetString):
    """Custom type paramFileIdentification based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_ParamFileIdentification_Type.__name__ = "OctetString"
_ParamFileIdentification_Object = MibTableColumn
paramFileIdentification = _ParamFileIdentification_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 2),
    _ParamFileIdentification_Type()
)
paramFileIdentification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileIdentification.setStatus("mandatory")


class _ParamFileEntryStatus_Type(Integer32):
    """Custom type paramFileEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ParamFileEntryStatus_Type.__name__ = "Integer32"
_ParamFileEntryStatus_Object = MibTableColumn
paramFileEntryStatus = _ParamFileEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 3),
    _ParamFileEntryStatus_Type()
)
paramFileEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramFileEntryStatus.setStatus("mandatory")
_ParamFileWrite_Type = DateTime
_ParamFileWrite_Object = MibTableColumn
paramFileWrite = _ParamFileWrite_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 4),
    _ParamFileWrite_Type()
)
paramFileWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileWrite.setStatus("mandatory")
_ParamFileSize_Type = Integer32
_ParamFileSize_Object = MibTableColumn
paramFileSize = _ParamFileSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 5),
    _ParamFileSize_Type()
)
paramFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileSize.setStatus("mandatory")
_ParamFileParameterVersion_Type = Integer32
_ParamFileParameterVersion_Object = MibTableColumn
paramFileParameterVersion = _ParamFileParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 6, 4, 7, 1, 6),
    _ParamFileParameterVersion_Type()
)
paramFileParameterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramFileParameterVersion.setStatus("mandatory")
_ParamClient_ObjectIdentity = ObjectIdentity
paramClient = _ParamClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 7)
)
_ParamClientLoaderName_Type = DisplayString
_ParamClientLoaderName_Object = MibScalar
paramClientLoaderName = _ParamClientLoaderName_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 1),
    _ParamClientLoaderName_Type()
)
paramClientLoaderName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderName.setStatus("mandatory")
_ParamClientLoaderAddressType_Type = AddressType
_ParamClientLoaderAddressType_Object = MibScalar
paramClientLoaderAddressType = _ParamClientLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 2),
    _ParamClientLoaderAddressType_Type()
)
paramClientLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderAddressType.setStatus("mandatory")
_ParamClientLoaderAddress_Type = OctetString
_ParamClientLoaderAddress_Object = MibScalar
paramClientLoaderAddress = _ParamClientLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 3),
    _ParamClientLoaderAddress_Type()
)
paramClientLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientLoaderAddress.setStatus("mandatory")
_ParamClientParameterVersion_Type = Integer32
_ParamClientParameterVersion_Object = MibScalar
paramClientParameterVersion = _ParamClientParameterVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 4),
    _ParamClientParameterVersion_Type()
)
paramClientParameterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientParameterVersion.setStatus("mandatory")
_ParamClientUpdateTime_Type = DateTime
_ParamClientUpdateTime_Object = MibScalar
paramClientUpdateTime = _ParamClientUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 5),
    _ParamClientUpdateTime_Type()
)
paramClientUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientUpdateTime.setStatus("mandatory")


class _ParamClientServerCheck_Type(Integer32):
    """Custom type paramClientServerCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ParamClientServerCheck_Type.__name__ = "Integer32"
_ParamClientServerCheck_Object = MibScalar
paramClientServerCheck = _ParamClientServerCheck_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 6),
    _ParamClientServerCheck_Type()
)
paramClientServerCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientServerCheck.setStatus("mandatory")


class _ParamClientCheckInterval_Type(Integer32):
    """Custom type paramClientCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_ParamClientCheckInterval_Type.__name__ = "Integer32"
_ParamClientCheckInterval_Object = MibScalar
paramClientCheckInterval = _ParamClientCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 7),
    _ParamClientCheckInterval_Type()
)
paramClientCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientCheckInterval.setStatus("mandatory")


class _ParamClientCheckNow_Type(Integer32):
    """Custom type paramClientCheckNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_ParamClientCheckNow_Type.__name__ = "Integer32"
_ParamClientCheckNow_Object = MibScalar
paramClientCheckNow = _ParamClientCheckNow_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 8),
    _ParamClientCheckNow_Type()
)
paramClientCheckNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientCheckNow.setStatus("mandatory")


class _ParamClientServerLimit_Type(Integer32):
    """Custom type paramClientServerLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ParamClientServerLimit_Type.__name__ = "Integer32"
_ParamClientServerLimit_Object = MibScalar
paramClientServerLimit = _ParamClientServerLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 9),
    _ParamClientServerLimit_Type()
)
paramClientServerLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientServerLimit.setStatus("mandatory")


class _ParamClientRetransmitInterval_Type(Integer32):
    """Custom type paramClientRetransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ParamClientRetransmitInterval_Type.__name__ = "Integer32"
_ParamClientRetransmitInterval_Object = MibScalar
paramClientRetransmitInterval = _ParamClientRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 10),
    _ParamClientRetransmitInterval_Type()
)
paramClientRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientRetransmitInterval.setStatus("mandatory")


class _ParamClientRetransmitLimit_Type(Integer32):
    """Custom type paramClientRetransmitLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ParamClientRetransmitLimit_Type.__name__ = "Integer32"
_ParamClientRetransmitLimit_Object = MibScalar
paramClientRetransmitLimit = _ParamClientRetransmitLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 11),
    _ParamClientRetransmitLimit_Type()
)
paramClientRetransmitLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramClientRetransmitLimit.setStatus("mandatory")


class _ParamClientState_Type(Integer32):
    """Custom type paramClientState based on Integer32"""
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
        *(("hold", 11),
          ("idle", 2),
          ("internal1", 3),
          ("internal2", 4),
          ("internal3", 5),
          ("internal4", 6),
          ("internal5", 7),
          ("internal6", 8),
          ("internal7", 9),
          ("internal8", 10),
          ("other", 1),
          ("retry", 12))
    )


_ParamClientState_Type.__name__ = "Integer32"
_ParamClientState_Object = MibScalar
paramClientState = _ParamClientState_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 12),
    _ParamClientState_Type()
)
paramClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientState.setStatus("mandatory")
_ParamClientProtocolErrors_Type = Counter32
_ParamClientProtocolErrors_Object = MibScalar
paramClientProtocolErrors = _ParamClientProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 13),
    _ParamClientProtocolErrors_Type()
)
paramClientProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientProtocolErrors.setStatus("mandatory")
_ParamClientServerRejects_Type = Counter32
_ParamClientServerRejects_Object = MibScalar
paramClientServerRejects = _ParamClientServerRejects_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 14),
    _ParamClientServerRejects_Type()
)
paramClientServerRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientServerRejects.setStatus("mandatory")
_ParamClientServerNumber_Type = Integer32
_ParamClientServerNumber_Object = MibScalar
paramClientServerNumber = _ParamClientServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 15),
    _ParamClientServerNumber_Type()
)
paramClientServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramClientServerNumber.setStatus("mandatory")
_ParamServerTable_Object = MibTable
paramServerTable = _ParamServerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16)
)
if mibBuilder.loadTexts:
    paramServerTable.setStatus("mandatory")
_ParamServerEntry_Object = MibTableRow
paramServerEntry = _ParamServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1)
)
paramServerEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "paramServerName"),
)
if mibBuilder.loadTexts:
    paramServerEntry.setStatus("mandatory")


class _ParamServerName_Type(DisplayString):
    """Custom type paramServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ParamServerName_Type.__name__ = "DisplayString"
_ParamServerName_Object = MibTableColumn
paramServerName = _ParamServerName_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 1),
    _ParamServerName_Type()
)
paramServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerName.setStatus("mandatory")


class _ParamServerEntryStatus_Type(Integer32):
    """Custom type paramServerEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_ParamServerEntryStatus_Type.__name__ = "Integer32"
_ParamServerEntryStatus_Object = MibTableColumn
paramServerEntryStatus = _ParamServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 2),
    _ParamServerEntryStatus_Type()
)
paramServerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerEntryStatus.setStatus("mandatory")


class _ParamServerAddressType_Type(AddressType):
    """Custom type paramServerAddressType based on AddressType"""


_ParamServerAddressType_Object = MibTableColumn
paramServerAddressType = _ParamServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 3),
    _ParamServerAddressType_Type()
)
paramServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerAddressType.setStatus("mandatory")
_ParamServerAddress_Type = OctetString
_ParamServerAddress_Object = MibTableColumn
paramServerAddress = _ParamServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 4),
    _ParamServerAddress_Type()
)
paramServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    paramServerAddress.setStatus("mandatory")


class _ParamServerStoredVersion_Type(Integer32):
    """Custom type paramServerStoredVersion based on Integer32"""
    defaultValue = 0


_ParamServerStoredVersion_Object = MibTableColumn
paramServerStoredVersion = _ParamServerStoredVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 5),
    _ParamServerStoredVersion_Type()
)
paramServerStoredVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredVersion.setStatus("mandatory")


class _ParamServerStoredTime_Type(DateTime):
    """Custom type paramServerStoredTime based on DateTime"""
    defaultHexValue = "00"


_ParamServerStoredTime_Object = MibTableColumn
paramServerStoredTime = _ParamServerStoredTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 6),
    _ParamServerStoredTime_Type()
)
paramServerStoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredTime.setStatus("mandatory")


class _ParamServerStoredStatus_Type(Integer32):
    """Custom type paramServerStoredStatus based on Integer32"""
    defaultValue = 1

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
        *(("ahead", 3),
          ("behind", 4),
          ("current", 2),
          ("failed", 6),
          ("failing", 5),
          ("query", 7),
          ("unknown", 1))
    )


_ParamServerStoredStatus_Type.__name__ = "Integer32"
_ParamServerStoredStatus_Object = MibTableColumn
paramServerStoredStatus = _ParamServerStoredStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 7),
    _ParamServerStoredStatus_Type()
)
paramServerStoredStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredStatus.setStatus("mandatory")


class _ParamServerStoredFailure_Type(Integer32):
    """Custom type paramServerStoredFailure based on Integer32"""
    defaultValue = 2

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
        *(("close", 10),
          ("delete", 11),
          ("fileData", 13),
          ("none", 2),
          ("open", 4),
          ("other", 1),
          ("protocolIn", 8),
          ("protocolOut", 3),
          ("read", 5),
          ("rename", 12),
          ("resource", 7),
          ("response", 9),
          ("write", 6))
    )


_ParamServerStoredFailure_Type.__name__ = "Integer32"
_ParamServerStoredFailure_Object = MibTableColumn
paramServerStoredFailure = _ParamServerStoredFailure_Object(
    (1, 3, 6, 1, 4, 1, 33, 7, 16, 1, 8),
    _ParamServerStoredFailure_Type()
)
paramServerStoredFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    paramServerStoredFailure.setStatus("mandatory")
_XInternet_ObjectIdentity = ObjectIdentity
xInternet = _XInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10)
)
_XIp_ObjectIdentity = ObjectIdentity
xIp = _XIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 1)
)
_IpGatewayAddress1_Type = IpAddress
_IpGatewayAddress1_Object = MibScalar
ipGatewayAddress1 = _IpGatewayAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 1),
    _IpGatewayAddress1_Type()
)
ipGatewayAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress1.setStatus("mandatory")
_IpGatewayAddress2_Type = IpAddress
_IpGatewayAddress2_Object = MibScalar
ipGatewayAddress2 = _IpGatewayAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 2),
    _IpGatewayAddress2_Type()
)
ipGatewayAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGatewayAddress2.setStatus("mandatory")


class _IpAutoSubnetMask_Type(Integer32):
    """Custom type ipAutoSubnetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpAutoSubnetMask_Type.__name__ = "Integer32"
_IpAutoSubnetMask_Object = MibScalar
ipAutoSubnetMask = _IpAutoSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 3),
    _IpAutoSubnetMask_Type()
)
ipAutoSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAutoSubnetMask.setStatus("mandatory")


class _IpReassembly_Type(Integer32):
    """Custom type ipReassembly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_IpReassembly_Type.__name__ = "Integer32"
_IpReassembly_Object = MibScalar
ipReassembly = _IpReassembly_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 1, 4),
    _IpReassembly_Type()
)
ipReassembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipReassembly.setStatus("mandatory")
_XTcp_ObjectIdentity = ObjectIdentity
xTcp = _XTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 2)
)
_TcpPortTable_Object = MibTable
tcpPortTable = _TcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1)
)
if mibBuilder.loadTexts:
    tcpPortTable.setStatus("mandatory")
_TcpPortEntry_Object = MibTableRow
tcpPortEntry = _TcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1)
)
tcpPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tcpPortIndex"),
)
if mibBuilder.loadTexts:
    tcpPortEntry.setStatus("mandatory")
_TcpPortIndex_Type = Integer32
_TcpPortIndex_Object = MibTableColumn
tcpPortIndex = _TcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 1),
    _TcpPortIndex_Type()
)
tcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tcpPortIndex.setStatus("mandatory")


class _TcpPortConnectByAddress_Type(Integer32):
    """Custom type tcpPortConnectByAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TcpPortConnectByAddress_Type.__name__ = "Integer32"
_TcpPortConnectByAddress_Object = MibTableColumn
tcpPortConnectByAddress = _TcpPortConnectByAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 2),
    _TcpPortConnectByAddress_Type()
)
tcpPortConnectByAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortConnectByAddress.setStatus("mandatory")


class _TcpPortWindowSize_Type(Integer32):
    """Custom type tcpPortWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 8192),
    )


_TcpPortWindowSize_Type.__name__ = "Integer32"
_TcpPortWindowSize_Object = MibTableColumn
tcpPortWindowSize = _TcpPortWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 2, 1, 1, 3),
    _TcpPortWindowSize_Type()
)
tcpPortWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tcpPortWindowSize.setStatus("mandatory")
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 3)
)


class _SnmpAgentGetCommunity_Type(DisplayString):
    """Custom type snmpAgentGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentGetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentGetCommunity_Object = MibScalar
snmpAgentGetCommunity = _SnmpAgentGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 1),
    _SnmpAgentGetCommunity_Type()
)
snmpAgentGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentGetCommunity.setStatus("mandatory")


class _SnmpAgentSetCommunity_Type(DisplayString):
    """Custom type snmpAgentSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentSetCommunity_Type.__name__ = "DisplayString"
_SnmpAgentSetCommunity_Object = MibScalar
snmpAgentSetCommunity = _SnmpAgentSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 2),
    _SnmpAgentSetCommunity_Type()
)
snmpAgentSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentSetCommunity.setStatus("mandatory")


class _SnmpAgentTrapCommunity_Type(DisplayString):
    """Custom type snmpAgentTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpAgentTrapCommunity_Type.__name__ = "DisplayString"
_SnmpAgentTrapCommunity_Object = MibScalar
snmpAgentTrapCommunity = _SnmpAgentTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 3),
    _SnmpAgentTrapCommunity_Type()
)
snmpAgentTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentTrapCommunity.setStatus("mandatory")
_SnmpAgentGetClientNumber_Type = Integer32
_SnmpAgentGetClientNumber_Object = MibScalar
snmpAgentGetClientNumber = _SnmpAgentGetClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 4),
    _SnmpAgentGetClientNumber_Type()
)
snmpAgentGetClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentGetClientNumber.setStatus("mandatory")
_SnmpAgentSetClientNumber_Type = Integer32
_SnmpAgentSetClientNumber_Object = MibScalar
snmpAgentSetClientNumber = _SnmpAgentSetClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 5),
    _SnmpAgentSetClientNumber_Type()
)
snmpAgentSetClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentSetClientNumber.setStatus("mandatory")
_SnmpAgentTrapClientNumber_Type = Integer32
_SnmpAgentTrapClientNumber_Object = MibScalar
snmpAgentTrapClientNumber = _SnmpAgentTrapClientNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 6),
    _SnmpAgentTrapClientNumber_Type()
)
snmpAgentTrapClientNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentTrapClientNumber.setStatus("mandatory")
_GetClientTable_Object = MibTable
getClientTable = _GetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7)
)
if mibBuilder.loadTexts:
    getClientTable.setStatus("mandatory")
_GetClientEntry_Object = MibTableRow
getClientEntry = _GetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1)
)
getClientEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "getClientIndex"),
)
if mibBuilder.loadTexts:
    getClientEntry.setStatus("mandatory")
_GetClientIndex_Type = Integer32
_GetClientIndex_Object = MibTableColumn
getClientIndex = _GetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 1),
    _GetClientIndex_Type()
)
getClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    getClientIndex.setStatus("mandatory")


class _GetClientEntryStatus_Type(Integer32):
    """Custom type getClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_GetClientEntryStatus_Type.__name__ = "Integer32"
_GetClientEntryStatus_Object = MibTableColumn
getClientEntryStatus = _GetClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 2),
    _GetClientEntryStatus_Type()
)
getClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientEntryStatus.setStatus("mandatory")


class _GetClientAddressType_Type(AddressType):
    """Custom type getClientAddressType based on AddressType"""


_GetClientAddressType_Object = MibTableColumn
getClientAddressType = _GetClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 3),
    _GetClientAddressType_Type()
)
getClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientAddressType.setStatus("mandatory")
_GetClientAddress_Type = OctetString
_GetClientAddress_Object = MibTableColumn
getClientAddress = _GetClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 7, 1, 4),
    _GetClientAddress_Type()
)
getClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getClientAddress.setStatus("mandatory")
_SetClientTable_Object = MibTable
setClientTable = _SetClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8)
)
if mibBuilder.loadTexts:
    setClientTable.setStatus("mandatory")
_SetClientEntry_Object = MibTableRow
setClientEntry = _SetClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1)
)
setClientEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "setClientIndex"),
)
if mibBuilder.loadTexts:
    setClientEntry.setStatus("mandatory")
_SetClientIndex_Type = Integer32
_SetClientIndex_Object = MibTableColumn
setClientIndex = _SetClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 1),
    _SetClientIndex_Type()
)
setClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setClientIndex.setStatus("mandatory")


class _SetClientEntryStatus_Type(Integer32):
    """Custom type setClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_SetClientEntryStatus_Type.__name__ = "Integer32"
_SetClientEntryStatus_Object = MibTableColumn
setClientEntryStatus = _SetClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 2),
    _SetClientEntryStatus_Type()
)
setClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientEntryStatus.setStatus("mandatory")


class _SetClientAddressType_Type(AddressType):
    """Custom type setClientAddressType based on AddressType"""


_SetClientAddressType_Object = MibTableColumn
setClientAddressType = _SetClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 3),
    _SetClientAddressType_Type()
)
setClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientAddressType.setStatus("mandatory")
_SetClientAddress_Type = OctetString
_SetClientAddress_Object = MibTableColumn
setClientAddress = _SetClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 8, 1, 4),
    _SetClientAddress_Type()
)
setClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setClientAddress.setStatus("mandatory")
_TrapClientTable_Object = MibTable
trapClientTable = _TrapClientTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9)
)
if mibBuilder.loadTexts:
    trapClientTable.setStatus("mandatory")
_TrapClientEntry_Object = MibTableRow
trapClientEntry = _TrapClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1)
)
trapClientEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "trapClientIndex"),
)
if mibBuilder.loadTexts:
    trapClientEntry.setStatus("mandatory")
_TrapClientIndex_Type = Integer32
_TrapClientIndex_Object = MibTableColumn
trapClientIndex = _TrapClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 1),
    _TrapClientIndex_Type()
)
trapClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapClientIndex.setStatus("mandatory")


class _TrapClientEntryStatus_Type(Integer32):
    """Custom type trapClientEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_TrapClientEntryStatus_Type.__name__ = "Integer32"
_TrapClientEntryStatus_Object = MibTableColumn
trapClientEntryStatus = _TrapClientEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 2),
    _TrapClientEntryStatus_Type()
)
trapClientEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientEntryStatus.setStatus("mandatory")


class _TrapClientAddressType_Type(AddressType):
    """Custom type trapClientAddressType based on AddressType"""


_TrapClientAddressType_Object = MibTableColumn
trapClientAddressType = _TrapClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 3),
    _TrapClientAddressType_Type()
)
trapClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientAddressType.setStatus("mandatory")
_TrapClientAddress_Type = OctetString
_TrapClientAddress_Object = MibTableColumn
trapClientAddress = _TrapClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 3, 9, 1, 4),
    _TrapClientAddress_Type()
)
trapClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapClientAddress.setStatus("mandatory")
_DomainResolver_ObjectIdentity = ObjectIdentity
domainResolver = _DomainResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 4)
)


class _DomainResolverSuffix_Type(DisplayString):
    """Custom type domainResolverSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 115),
    )


_DomainResolverSuffix_Type.__name__ = "DisplayString"
_DomainResolverSuffix_Object = MibScalar
domainResolverSuffix = _DomainResolverSuffix_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 1),
    _DomainResolverSuffix_Type()
)
domainResolverSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverSuffix.setStatus("mandatory")
_DomainResolverAddress1_Type = IpAddress
_DomainResolverAddress1_Object = MibScalar
domainResolverAddress1 = _DomainResolverAddress1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 2),
    _DomainResolverAddress1_Type()
)
domainResolverAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverAddress1.setStatus("mandatory")
_DomainResolverAddress2_Type = IpAddress
_DomainResolverAddress2_Object = MibScalar
domainResolverAddress2 = _DomainResolverAddress2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 3),
    _DomainResolverAddress2_Type()
)
domainResolverAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverAddress2.setStatus("mandatory")


class _DomainResolverTtl_Type(Integer32):
    """Custom type domainResolverTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 168),
    )


_DomainResolverTtl_Type.__name__ = "Integer32"
_DomainResolverTtl_Object = MibScalar
domainResolverTtl = _DomainResolverTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 4),
    _DomainResolverTtl_Type()
)
domainResolverTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainResolverTtl.setStatus("mandatory")
_DomainResolverNameNumber_Type = Integer32
_DomainResolverNameNumber_Object = MibScalar
domainResolverNameNumber = _DomainResolverNameNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 5),
    _DomainResolverNameNumber_Type()
)
domainResolverNameNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainResolverNameNumber.setStatus("mandatory")
_NameTable_Object = MibTable
nameTable = _NameTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6)
)
if mibBuilder.loadTexts:
    nameTable.setStatus("mandatory")
_NameEntry_Object = MibTableRow
nameEntry = _NameEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1)
)
nameEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "nameName"),
    (0, "XYPLEX-CONCATENATED-MIB", "nameAddress"),
)
if mibBuilder.loadTexts:
    nameEntry.setStatus("mandatory")


class _NameName_Type(DisplayString):
    """Custom type nameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NameName_Type.__name__ = "DisplayString"
_NameName_Object = MibTableColumn
nameName = _NameName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 1),
    _NameName_Type()
)
nameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameName.setStatus("mandatory")
_NameAddress_Type = IpAddress
_NameAddress_Object = MibTableColumn
nameAddress = _NameAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 2),
    _NameAddress_Type()
)
nameAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameAddress.setStatus("mandatory")


class _NameStatus_Type(Integer32):
    """Custom type nameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NameStatus_Type.__name__ = "Integer32"
_NameStatus_Object = MibTableColumn
nameStatus = _NameStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 3),
    _NameStatus_Type()
)
nameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nameStatus.setStatus("mandatory")


class _NameSource_Type(Integer32):
    """Custom type nameSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manager", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_NameSource_Type.__name__ = "Integer32"
_NameSource_Object = MibTableColumn
nameSource = _NameSource_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 4),
    _NameSource_Type()
)
nameSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameSource.setStatus("mandatory")
_NameTtl_Type = Integer32
_NameTtl_Object = MibTableColumn
nameTtl = _NameTtl_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 4, 6, 1, 5),
    _NameTtl_Type()
)
nameTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nameTtl.setStatus("mandatory")
_Slip_ObjectIdentity = ObjectIdentity
slip = _Slip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 5)
)
_SlipTable_Object = MibTable
slipTable = _SlipTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1)
)
if mibBuilder.loadTexts:
    slipTable.setStatus("mandatory")
_SlipEntry_Object = MibTableRow
slipEntry = _SlipEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1)
)
slipEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "slipIndex"),
)
if mibBuilder.loadTexts:
    slipEntry.setStatus("mandatory")
_SlipIndex_Type = Integer32
_SlipIndex_Object = MibTableColumn
slipIndex = _SlipIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 1),
    _SlipIndex_Type()
)
slipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipIndex.setStatus("mandatory")


class _SlipState_Type(Integer32):
    """Custom type slipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_SlipState_Type.__name__ = "Integer32"
_SlipState_Object = MibTableColumn
slipState = _SlipState_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 2),
    _SlipState_Type()
)
slipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipState.setStatus("mandatory")
_SlipLocalAddress_Type = IpAddress
_SlipLocalAddress_Object = MibTableColumn
slipLocalAddress = _SlipLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 3),
    _SlipLocalAddress_Type()
)
slipLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipLocalAddress.setStatus("mandatory")
_SlipRemoteAddress_Type = IpAddress
_SlipRemoteAddress_Object = MibTableColumn
slipRemoteAddress = _SlipRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 4),
    _SlipRemoteAddress_Type()
)
slipRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipRemoteAddress.setStatus("mandatory")
_SlipMask_Type = IpAddress
_SlipMask_Object = MibTableColumn
slipMask = _SlipMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 5),
    _SlipMask_Type()
)
slipMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slipMask.setStatus("mandatory")
_SlipPortPacketsReceived_Type = Counter32
_SlipPortPacketsReceived_Object = MibTableColumn
slipPortPacketsReceived = _SlipPortPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 6),
    _SlipPortPacketsReceived_Type()
)
slipPortPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsReceived.setStatus("mandatory")
_SlipPortPacketsSent_Type = Counter32
_SlipPortPacketsSent_Object = MibTableColumn
slipPortPacketsSent = _SlipPortPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 7),
    _SlipPortPacketsSent_Type()
)
slipPortPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsSent.setStatus("mandatory")
_SlipPortPacketsDiscarded_Type = Counter32
_SlipPortPacketsDiscarded_Object = MibTableColumn
slipPortPacketsDiscarded = _SlipPortPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 8),
    _SlipPortPacketsDiscarded_Type()
)
slipPortPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketsDiscarded.setStatus("mandatory")
_SlipPortPacketLengthErrors_Type = Counter32
_SlipPortPacketLengthErrors_Object = MibTableColumn
slipPortPacketLengthErrors = _SlipPortPacketLengthErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 9),
    _SlipPortPacketLengthErrors_Type()
)
slipPortPacketLengthErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketLengthErrors.setStatus("mandatory")
_SlipPortPacketChecksumErrors_Type = Counter32
_SlipPortPacketChecksumErrors_Object = MibTableColumn
slipPortPacketChecksumErrors = _SlipPortPacketChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 10),
    _SlipPortPacketChecksumErrors_Type()
)
slipPortPacketChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipPortPacketChecksumErrors.setStatus("mandatory")
_SlipNetworkPacketsReceived_Type = Counter32
_SlipNetworkPacketsReceived_Object = MibTableColumn
slipNetworkPacketsReceived = _SlipNetworkPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 11),
    _SlipNetworkPacketsReceived_Type()
)
slipNetworkPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsReceived.setStatus("mandatory")
_SlipNetworkPacketsSent_Type = Counter32
_SlipNetworkPacketsSent_Object = MibTableColumn
slipNetworkPacketsSent = _SlipNetworkPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 12),
    _SlipNetworkPacketsSent_Type()
)
slipNetworkPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsSent.setStatus("mandatory")
_SlipNetworkPacketsDiscarded_Type = Counter32
_SlipNetworkPacketsDiscarded_Object = MibTableColumn
slipNetworkPacketsDiscarded = _SlipNetworkPacketsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 5, 1, 1, 13),
    _SlipNetworkPacketsDiscarded_Type()
)
slipNetworkPacketsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slipNetworkPacketsDiscarded.setStatus("mandatory")
_Telnet_ObjectIdentity = ObjectIdentity
telnet = _Telnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 6)
)
_TelnetPortTable_Object = MibTable
telnetPortTable = _TelnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1)
)
if mibBuilder.loadTexts:
    telnetPortTable.setStatus("mandatory")
_TelnetPortEntry_Object = MibTableRow
telnetPortEntry = _TelnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1)
)
telnetPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "telnetPortIndex"),
)
if mibBuilder.loadTexts:
    telnetPortEntry.setStatus("mandatory")
_TelnetPortIndex_Type = Integer32
_TelnetPortIndex_Object = MibTableColumn
telnetPortIndex = _TelnetPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 1),
    _TelnetPortIndex_Type()
)
telnetPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortIndex.setStatus("mandatory")


class _TelnetPortIncomingTcpPort_Type(Integer32):
    """Custom type telnetPortIncomingTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_TelnetPortIncomingTcpPort_Type.__name__ = "Integer32"
_TelnetPortIncomingTcpPort_Object = MibTableColumn
telnetPortIncomingTcpPort = _TelnetPortIncomingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 2),
    _TelnetPortIncomingTcpPort_Type()
)
telnetPortIncomingTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortIncomingTcpPort.setStatus("mandatory")
_TelnetPortOutgoingTcpPort_Type = Integer32
_TelnetPortOutgoingTcpPort_Object = MibTableColumn
telnetPortOutgoingTcpPort = _TelnetPortOutgoingTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 3),
    _TelnetPortOutgoingTcpPort_Type()
)
telnetPortOutgoingTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetPortOutgoingTcpPort.setStatus("mandatory")


class _TelnetPortNewlineTranslation_Type(Integer32):
    """Custom type telnetPortNewlineTranslation based on Integer32"""
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
        *(("cr", 2),
          ("crLf", 4),
          ("crNull", 3),
          ("none", 1))
    )


_TelnetPortNewlineTranslation_Type.__name__ = "Integer32"
_TelnetPortNewlineTranslation_Object = MibTableColumn
telnetPortNewlineTranslation = _TelnetPortNewlineTranslation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 4),
    _TelnetPortNewlineTranslation_Type()
)
telnetPortNewlineTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNewlineTranslation.setStatus("mandatory")


class _TelnetPortTerminalType_Type(DisplayString):
    """Custom type telnetPortTerminalType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_TelnetPortTerminalType_Type.__name__ = "DisplayString"
_TelnetPortTerminalType_Object = MibTableColumn
telnetPortTerminalType = _TelnetPortTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 5),
    _TelnetPortTerminalType_Type()
)
telnetPortTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortTerminalType.setStatus("mandatory")


class _TelnetPortEorReflection_Type(Integer32):
    """Custom type telnetPortEorReflection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TelnetPortEorReflection_Type.__name__ = "Integer32"
_TelnetPortEorReflection_Object = MibTableColumn
telnetPortEorReflection = _TelnetPortEorReflection_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 6),
    _TelnetPortEorReflection_Type()
)
telnetPortEorReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortEorReflection.setStatus("mandatory")


class _TelnetPortBinaryMode_Type(Integer32):
    """Custom type telnetPortBinaryMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 2),
          ("disabled", 3),
          ("flowControl", 1))
    )


_TelnetPortBinaryMode_Type.__name__ = "Integer32"
_TelnetPortBinaryMode_Object = MibTableColumn
telnetPortBinaryMode = _TelnetPortBinaryMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 1, 1, 7),
    _TelnetPortBinaryMode_Type()
)
telnetPortBinaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortBinaryMode.setStatus("mandatory")
_TelnetSerialPortTable_Object = MibTable
telnetSerialPortTable = _TelnetSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2)
)
if mibBuilder.loadTexts:
    telnetSerialPortTable.setStatus("mandatory")
_TelnetSerialPortEntry_Object = MibTableRow
telnetSerialPortEntry = _TelnetSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1)
)
telnetSerialPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "telnetSerialPortIndex"),
)
if mibBuilder.loadTexts:
    telnetSerialPortEntry.setStatus("mandatory")
_TelnetSerialPortIndex_Type = Integer32
_TelnetSerialPortIndex_Object = MibTableColumn
telnetSerialPortIndex = _TelnetSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 1),
    _TelnetSerialPortIndex_Type()
)
telnetSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telnetSerialPortIndex.setStatus("mandatory")


class _TelnetSerialPortOptionDisplay_Type(Integer32):
    """Custom type telnetSerialPortOptionDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TelnetSerialPortOptionDisplay_Type.__name__ = "Integer32"
_TelnetSerialPortOptionDisplay_Object = MibTableColumn
telnetSerialPortOptionDisplay = _TelnetSerialPortOptionDisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 2),
    _TelnetSerialPortOptionDisplay_Type()
)
telnetSerialPortOptionDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortOptionDisplay.setStatus("mandatory")


class _TelnetSerialPortCsiEscape_Type(Integer32):
    """Custom type telnetSerialPortCsiEscape based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TelnetSerialPortCsiEscape_Type.__name__ = "Integer32"
_TelnetSerialPortCsiEscape_Object = MibTableColumn
telnetSerialPortCsiEscape = _TelnetSerialPortCsiEscape_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 3),
    _TelnetSerialPortCsiEscape_Type()
)
telnetSerialPortCsiEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortCsiEscape.setStatus("mandatory")


class _TelnetSerialPortEchoMode_Type(Integer32):
    """Custom type telnetSerialPortEchoMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_TelnetSerialPortEchoMode_Type.__name__ = "Integer32"
_TelnetSerialPortEchoMode_Object = MibTableColumn
telnetSerialPortEchoMode = _TelnetSerialPortEchoMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 4),
    _TelnetSerialPortEchoMode_Type()
)
telnetSerialPortEchoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEchoMode.setStatus("mandatory")


class _TelnetSerialPortNewlineMode_Type(Integer32):
    """Custom type telnetSerialPortNewlineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crLf", 2),
          ("crNull", 1),
          ("verbatim", 3))
    )


_TelnetSerialPortNewlineMode_Type.__name__ = "Integer32"
_TelnetSerialPortNewlineMode_Object = MibTableColumn
telnetSerialPortNewlineMode = _TelnetSerialPortNewlineMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 5),
    _TelnetSerialPortNewlineMode_Type()
)
telnetSerialPortNewlineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortNewlineMode.setStatus("mandatory")


class _TelnetSerialPortTransmitMode_Type(Integer32):
    """Custom type telnetSerialPortTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("buffered", 2),
          ("immediate", 1),
          ("timed", 3))
    )


_TelnetSerialPortTransmitMode_Type.__name__ = "Integer32"
_TelnetSerialPortTransmitMode_Object = MibTableColumn
telnetSerialPortTransmitMode = _TelnetSerialPortTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 6),
    _TelnetSerialPortTransmitMode_Type()
)
telnetSerialPortTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortTransmitMode.setStatus("mandatory")


class _TelnetSerialPortTransmitCharacterTimes_Type(Integer32):
    """Custom type telnetSerialPortTransmitCharacterTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TelnetSerialPortTransmitCharacterTimes_Type.__name__ = "Integer32"
_TelnetSerialPortTransmitCharacterTimes_Object = MibTableColumn
telnetSerialPortTransmitCharacterTimes = _TelnetSerialPortTransmitCharacterTimes_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 7),
    _TelnetSerialPortTransmitCharacterTimes_Type()
)
telnetSerialPortTransmitCharacterTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortTransmitCharacterTimes.setStatus("mandatory")


class _TelnetSerialPortAbortOutputCharacter_Type(Integer32):
    """Custom type telnetSerialPortAbortOutputCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortAbortOutputCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortAbortOutputCharacter_Object = MibTableColumn
telnetSerialPortAbortOutputCharacter = _TelnetSerialPortAbortOutputCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 8),
    _TelnetSerialPortAbortOutputCharacter_Type()
)
telnetSerialPortAbortOutputCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortAbortOutputCharacter.setStatus("mandatory")


class _TelnetSerialPortAttentionCharacter_Type(Integer32):
    """Custom type telnetSerialPortAttentionCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortAttentionCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortAttentionCharacter_Object = MibTableColumn
telnetSerialPortAttentionCharacter = _TelnetSerialPortAttentionCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 9),
    _TelnetSerialPortAttentionCharacter_Type()
)
telnetSerialPortAttentionCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortAttentionCharacter.setStatus("mandatory")


class _TelnetSerialPortEraseKeyCharacter_Type(Integer32):
    """Custom type telnetSerialPortEraseKeyCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortEraseKeyCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortEraseKeyCharacter_Object = MibTableColumn
telnetSerialPortEraseKeyCharacter = _TelnetSerialPortEraseKeyCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 10),
    _TelnetSerialPortEraseKeyCharacter_Type()
)
telnetSerialPortEraseKeyCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEraseKeyCharacter.setStatus("mandatory")


class _TelnetSerialPortEraseLineCharacter_Type(Integer32):
    """Custom type telnetSerialPortEraseLineCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortEraseLineCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortEraseLineCharacter_Object = MibTableColumn
telnetSerialPortEraseLineCharacter = _TelnetSerialPortEraseLineCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 11),
    _TelnetSerialPortEraseLineCharacter_Type()
)
telnetSerialPortEraseLineCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortEraseLineCharacter.setStatus("mandatory")


class _TelnetSerialPortInterruptCharacter_Type(Integer32):
    """Custom type telnetSerialPortInterruptCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortInterruptCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortInterruptCharacter_Object = MibTableColumn
telnetSerialPortInterruptCharacter = _TelnetSerialPortInterruptCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 12),
    _TelnetSerialPortInterruptCharacter_Type()
)
telnetSerialPortInterruptCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortInterruptCharacter.setStatus("mandatory")


class _TelnetSerialPortQueryCharacter_Type(Integer32):
    """Custom type telnetSerialPortQueryCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortQueryCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortQueryCharacter_Object = MibTableColumn
telnetSerialPortQueryCharacter = _TelnetSerialPortQueryCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 13),
    _TelnetSerialPortQueryCharacter_Type()
)
telnetSerialPortQueryCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortQueryCharacter.setStatus("mandatory")


class _TelnetSerialPortSynchronizeCharacter_Type(Integer32):
    """Custom type telnetSerialPortSynchronizeCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TelnetSerialPortSynchronizeCharacter_Type.__name__ = "Integer32"
_TelnetSerialPortSynchronizeCharacter_Object = MibTableColumn
telnetSerialPortSynchronizeCharacter = _TelnetSerialPortSynchronizeCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 6, 2, 1, 14),
    _TelnetSerialPortSynchronizeCharacter_Type()
)
telnetSerialPortSynchronizeCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetSerialPortSynchronizeCharacter.setStatus("mandatory")
_Tn3270_ObjectIdentity = ObjectIdentity
tn3270 = _Tn3270_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 7)
)
_Tn3270DeviceNumber_Type = Integer32
_Tn3270DeviceNumber_Object = MibScalar
tn3270DeviceNumber = _Tn3270DeviceNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 1),
    _Tn3270DeviceNumber_Type()
)
tn3270DeviceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceNumber.setStatus("mandatory")
_Tn3270LanguageNumber_Type = Integer32
_Tn3270LanguageNumber_Object = MibScalar
tn3270LanguageNumber = _Tn3270LanguageNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 2),
    _Tn3270LanguageNumber_Type()
)
tn3270LanguageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270LanguageNumber.setStatus("mandatory")


class _Tn3270PortKeymapStatus_Type(Integer32):
    """Custom type tn3270PortKeymapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Tn3270PortKeymapStatus_Type.__name__ = "Integer32"
_Tn3270PortKeymapStatus_Object = MibScalar
tn3270PortKeymapStatus = _Tn3270PortKeymapStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 3),
    _Tn3270PortKeymapStatus_Type()
)
tn3270PortKeymapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortKeymapStatus.setStatus("mandatory")
_Tn3270DeviceTable_Object = MibTable
tn3270DeviceTable = _Tn3270DeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4)
)
if mibBuilder.loadTexts:
    tn3270DeviceTable.setStatus("mandatory")
_Tn3270DeviceEntry_Object = MibTableRow
tn3270DeviceEntry = _Tn3270DeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1)
)
tn3270DeviceEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270DeviceName"),
)
if mibBuilder.loadTexts:
    tn3270DeviceEntry.setStatus("mandatory")


class _Tn3270DeviceName_Type(DisplayString):
    """Custom type tn3270DeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270DeviceName_Type.__name__ = "DisplayString"
_Tn3270DeviceName_Object = MibTableColumn
tn3270DeviceName = _Tn3270DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 1),
    _Tn3270DeviceName_Type()
)
tn3270DeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270DeviceName.setStatus("mandatory")


class _Tn3270DeviceStatus_Type(Integer32):
    """Custom type tn3270DeviceStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270DeviceStatus_Type.__name__ = "Integer32"
_Tn3270DeviceStatus_Object = MibTableColumn
tn3270DeviceStatus = _Tn3270DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 2),
    _Tn3270DeviceStatus_Type()
)
tn3270DeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270DeviceStatus.setStatus("mandatory")


class _Tn3270DeviceType_Type(DisplayString):
    """Custom type tn3270DeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_Tn3270DeviceType_Type.__name__ = "DisplayString"
_Tn3270DeviceType_Object = MibTableColumn
tn3270DeviceType = _Tn3270DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 3),
    _Tn3270DeviceType_Type()
)
tn3270DeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270DeviceType.setStatus("mandatory")


class _Tn3270Device3278Model_Type(Integer32):
    """Custom type tn3270Device3278Model based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("model2", 1),
          ("model5", 2))
    )


_Tn3270Device3278Model_Type.__name__ = "Integer32"
_Tn3270Device3278Model_Object = MibTableColumn
tn3270Device3278Model = _Tn3270Device3278Model_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 4),
    _Tn3270Device3278Model_Type()
)
tn3270Device3278Model.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270Device3278Model.setStatus("mandatory")
_Tn3270DeviceKeyNumber_Type = Integer32
_Tn3270DeviceKeyNumber_Object = MibTableColumn
tn3270DeviceKeyNumber = _Tn3270DeviceKeyNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 5),
    _Tn3270DeviceKeyNumber_Type()
)
tn3270DeviceKeyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceKeyNumber.setStatus("mandatory")
_Tn3270DeviceScreenNumber_Type = Integer32
_Tn3270DeviceScreenNumber_Object = MibTableColumn
tn3270DeviceScreenNumber = _Tn3270DeviceScreenNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 4, 1, 6),
    _Tn3270DeviceScreenNumber_Type()
)
tn3270DeviceScreenNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270DeviceScreenNumber.setStatus("mandatory")
_Tn3270KeyTable_Object = MibTable
tn3270KeyTable = _Tn3270KeyTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5)
)
if mibBuilder.loadTexts:
    tn3270KeyTable.setStatus("mandatory")
_Tn3270KeyEntry_Object = MibTableRow
tn3270KeyEntry = _Tn3270KeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1)
)
tn3270KeyEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270KeyDeviceName"),
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270KeyName"),
)
if mibBuilder.loadTexts:
    tn3270KeyEntry.setStatus("mandatory")


class _Tn3270KeyDeviceName_Type(DisplayString):
    """Custom type tn3270KeyDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270KeyDeviceName_Type.__name__ = "DisplayString"
_Tn3270KeyDeviceName_Object = MibTableColumn
tn3270KeyDeviceName = _Tn3270KeyDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 1),
    _Tn3270KeyDeviceName_Type()
)
tn3270KeyDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270KeyDeviceName.setStatus("mandatory")


class _Tn3270KeyName_Type(Integer32):
    """Custom type tn3270KeyName based on Integer32"""
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
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70)
        )
    )
    namedValues = NamedValues(
        *(("backtab", 3),
          ("centsign", 15),
          ("clear", 68),
          ("cursordown", 7),
          ("cursorleft", 5),
          ("cursorright", 6),
          ("cursorsel", 69),
          ("cursorup", 4),
          ("delete", 9),
          ("duplicate", 16),
          ("enter", 67),
          ("eraseeof", 10),
          ("eraseinput", 11),
          ("fastleft", 21),
          ("fastright", 22),
          ("fieldmark", 17),
          ("flushinput", 13),
          ("home", 8),
          ("insert", 12),
          ("newline", 1),
          ("pa1", 63),
          ("pa2", 64),
          ("pa3", 65),
          ("pf1", 39),
          ("pf10", 48),
          ("pf11", 49),
          ("pf12", 50),
          ("pf13", 51),
          ("pf14", 52),
          ("pf15", 53),
          ("pf16", 54),
          ("pf17", 55),
          ("pf18", 56),
          ("pf19", 57),
          ("pf2", 40),
          ("pf20", 58),
          ("pf21", 59),
          ("pf22", 60),
          ("pf23", 61),
          ("pf24", 62),
          ("pf3", 41),
          ("pf4", 42),
          ("pf5", 43),
          ("pf6", 44),
          ("pf7", 45),
          ("pf8", 46),
          ("pf9", 47),
          ("print", 24),
          ("refresh", 14),
          ("reset", 20),
          ("scroll", 18),
          ("showkeys", 23),
          ("status", 19),
          ("sysreq", 66),
          ("tab", 2),
          ("test", 70))
    )


_Tn3270KeyName_Type.__name__ = "Integer32"
_Tn3270KeyName_Object = MibTableColumn
tn3270KeyName = _Tn3270KeyName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 2),
    _Tn3270KeyName_Type()
)
tn3270KeyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270KeyName.setStatus("mandatory")


class _Tn3270KeyStatus_Type(Integer32):
    """Custom type tn3270KeyStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270KeyStatus_Type.__name__ = "Integer32"
_Tn3270KeyStatus_Object = MibTableColumn
tn3270KeyStatus = _Tn3270KeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 3),
    _Tn3270KeyStatus_Type()
)
tn3270KeyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyStatus.setStatus("mandatory")


class _Tn3270KeyCharacterSequence_Type(OctetString):
    """Custom type tn3270KeyCharacterSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Tn3270KeyCharacterSequence_Type.__name__ = "OctetString"
_Tn3270KeyCharacterSequence_Object = MibTableColumn
tn3270KeyCharacterSequence = _Tn3270KeyCharacterSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 4),
    _Tn3270KeyCharacterSequence_Type()
)
tn3270KeyCharacterSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyCharacterSequence.setStatus("mandatory")


class _Tn3270KeyDescription_Type(DisplayString):
    """Custom type tn3270KeyDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_Tn3270KeyDescription_Type.__name__ = "DisplayString"
_Tn3270KeyDescription_Object = MibTableColumn
tn3270KeyDescription = _Tn3270KeyDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 5, 1, 5),
    _Tn3270KeyDescription_Type()
)
tn3270KeyDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270KeyDescription.setStatus("mandatory")
_Tn3270ScreenTable_Object = MibTable
tn3270ScreenTable = _Tn3270ScreenTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6)
)
if mibBuilder.loadTexts:
    tn3270ScreenTable.setStatus("mandatory")
_Tn3270ScreenEntry_Object = MibTableRow
tn3270ScreenEntry = _Tn3270ScreenEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1)
)
tn3270ScreenEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270ScreenDeviceName"),
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270ScreenActionName"),
)
if mibBuilder.loadTexts:
    tn3270ScreenEntry.setStatus("mandatory")


class _Tn3270ScreenDeviceName_Type(DisplayString):
    """Custom type tn3270ScreenDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270ScreenDeviceName_Type.__name__ = "DisplayString"
_Tn3270ScreenDeviceName_Object = MibTableColumn
tn3270ScreenDeviceName = _Tn3270ScreenDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 1),
    _Tn3270ScreenDeviceName_Type()
)
tn3270ScreenDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270ScreenDeviceName.setStatus("mandatory")


class _Tn3270ScreenActionName_Type(Integer32):
    """Custom type tn3270ScreenActionName based on Integer32"""
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
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33)
        )
    )
    namedValues = NamedValues(
        *(("base", 32),
          ("beep", 6),
          ("blinkoff", 11),
          ("blinkon", 10),
          ("boldoff", 9),
          ("boldon", 8),
          ("charset", 7),
          ("clearscr", 2),
          ("col132", 4),
          ("col80", 5),
          ("eraseeol", 1),
          ("movecursor", 3),
          ("reset1", 28),
          ("reset2", 29),
          ("reset3", 30),
          ("reset4", 31),
          ("reverseoff", 15),
          ("reverseon", 14),
          ("sgr", 33),
          ("status1", 26),
          ("status2", 27),
          ("underscoreoff", 13),
          ("underscoreon", 12))
    )


_Tn3270ScreenActionName_Type.__name__ = "Integer32"
_Tn3270ScreenActionName_Object = MibTableColumn
tn3270ScreenActionName = _Tn3270ScreenActionName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 2),
    _Tn3270ScreenActionName_Type()
)
tn3270ScreenActionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270ScreenActionName.setStatus("mandatory")


class _Tn3270ScreenStatus_Type(Integer32):
    """Custom type tn3270ScreenStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270ScreenStatus_Type.__name__ = "Integer32"
_Tn3270ScreenStatus_Object = MibTableColumn
tn3270ScreenStatus = _Tn3270ScreenStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 3),
    _Tn3270ScreenStatus_Type()
)
tn3270ScreenStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270ScreenStatus.setStatus("mandatory")


class _Tn3270ScreenCharacterSequence_Type(OctetString):
    """Custom type tn3270ScreenCharacterSequence based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_Tn3270ScreenCharacterSequence_Type.__name__ = "OctetString"
_Tn3270ScreenCharacterSequence_Object = MibTableColumn
tn3270ScreenCharacterSequence = _Tn3270ScreenCharacterSequence_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 6, 1, 4),
    _Tn3270ScreenCharacterSequence_Type()
)
tn3270ScreenCharacterSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270ScreenCharacterSequence.setStatus("mandatory")
_Tn3270LanguageTable_Object = MibTable
tn3270LanguageTable = _Tn3270LanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7)
)
if mibBuilder.loadTexts:
    tn3270LanguageTable.setStatus("mandatory")
_Tn3270LanguageEntry_Object = MibTableRow
tn3270LanguageEntry = _Tn3270LanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1)
)
tn3270LanguageEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270LanguageName"),
)
if mibBuilder.loadTexts:
    tn3270LanguageEntry.setStatus("mandatory")


class _Tn3270LanguageName_Type(DisplayString):
    """Custom type tn3270LanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270LanguageName_Type.__name__ = "DisplayString"
_Tn3270LanguageName_Object = MibTableColumn
tn3270LanguageName = _Tn3270LanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1, 1),
    _Tn3270LanguageName_Type()
)
tn3270LanguageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270LanguageName.setStatus("mandatory")


class _Tn3270LanguageStatus_Type(Integer32):
    """Custom type tn3270LanguageStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_Tn3270LanguageStatus_Type.__name__ = "Integer32"
_Tn3270LanguageStatus_Object = MibTableColumn
tn3270LanguageStatus = _Tn3270LanguageStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 7, 1, 2),
    _Tn3270LanguageStatus_Type()
)
tn3270LanguageStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270LanguageStatus.setStatus("mandatory")
_EToALanguageTable_Object = MibTable
eToALanguageTable = _EToALanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8)
)
if mibBuilder.loadTexts:
    eToALanguageTable.setStatus("mandatory")
_EToALanguageEntry_Object = MibTableRow
eToALanguageEntry = _EToALanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1)
)
eToALanguageEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "eToALanguageName"),
    (0, "XYPLEX-CONCATENATED-MIB", "eToAOffset"),
)
if mibBuilder.loadTexts:
    eToALanguageEntry.setStatus("mandatory")


class _EToALanguageName_Type(DisplayString):
    """Custom type eToALanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EToALanguageName_Type.__name__ = "DisplayString"
_EToALanguageName_Object = MibTableColumn
eToALanguageName = _EToALanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 1),
    _EToALanguageName_Type()
)
eToALanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eToALanguageName.setStatus("mandatory")


class _EToAOffset_Type(Integer32):
    """Custom type eToAOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(65, 256),
    )


_EToAOffset_Type.__name__ = "Integer32"
_EToAOffset_Object = MibTableColumn
eToAOffset = _EToAOffset_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 2),
    _EToAOffset_Type()
)
eToAOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eToAOffset.setStatus("mandatory")


class _EToAValue_Type(Integer32):
    """Custom type eToAValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 255),
    )


_EToAValue_Type.__name__ = "Integer32"
_EToAValue_Object = MibTableColumn
eToAValue = _EToAValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 8, 1, 3),
    _EToAValue_Type()
)
eToAValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eToAValue.setStatus("mandatory")
_AToELanguageTable_Object = MibTable
aToELanguageTable = _AToELanguageTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9)
)
if mibBuilder.loadTexts:
    aToELanguageTable.setStatus("mandatory")
_AToELanguageEntry_Object = MibTableRow
aToELanguageEntry = _AToELanguageEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1)
)
aToELanguageEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "aToELanguageName"),
    (0, "XYPLEX-CONCATENATED-MIB", "aToEOffset"),
)
if mibBuilder.loadTexts:
    aToELanguageEntry.setStatus("mandatory")


class _AToELanguageName_Type(DisplayString):
    """Custom type aToELanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AToELanguageName_Type.__name__ = "DisplayString"
_AToELanguageName_Object = MibTableColumn
aToELanguageName = _AToELanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 1),
    _AToELanguageName_Type()
)
aToELanguageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aToELanguageName.setStatus("mandatory")


class _AToEOffset_Type(Integer32):
    """Custom type aToEOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 256),
    )


_AToEOffset_Type.__name__ = "Integer32"
_AToEOffset_Object = MibTableColumn
aToEOffset = _AToEOffset_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 2),
    _AToEOffset_Type()
)
aToEOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aToEOffset.setStatus("mandatory")


class _AToEValue_Type(Integer32):
    """Custom type aToEValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 255),
    )


_AToEValue_Type.__name__ = "Integer32"
_AToEValue_Object = MibTableColumn
aToEValue = _AToEValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 9, 1, 3),
    _AToEValue_Type()
)
aToEValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aToEValue.setStatus("mandatory")
_Tn3270PortTable_Object = MibTable
tn3270PortTable = _Tn3270PortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10)
)
if mibBuilder.loadTexts:
    tn3270PortTable.setStatus("mandatory")
_Tn3270PortEntry_Object = MibTableRow
tn3270PortEntry = _Tn3270PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1)
)
tn3270PortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "tn3270PortIndex"),
)
if mibBuilder.loadTexts:
    tn3270PortEntry.setStatus("mandatory")
_Tn3270PortIndex_Type = Integer32
_Tn3270PortIndex_Object = MibTableColumn
tn3270PortIndex = _Tn3270PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 1),
    _Tn3270PortIndex_Type()
)
tn3270PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270PortIndex.setStatus("mandatory")


class _Tn3270PortDeviceName_Type(DisplayString):
    """Custom type tn3270PortDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270PortDeviceName_Type.__name__ = "DisplayString"
_Tn3270PortDeviceName_Object = MibTableColumn
tn3270PortDeviceName = _Tn3270PortDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 2),
    _Tn3270PortDeviceName_Type()
)
tn3270PortDeviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortDeviceName.setStatus("mandatory")


class _Tn3270PortLanguageName_Type(DisplayString):
    """Custom type tn3270PortLanguageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_Tn3270PortLanguageName_Type.__name__ = "DisplayString"
_Tn3270PortLanguageName_Object = MibTableColumn
tn3270PortLanguageName = _Tn3270PortLanguageName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 3),
    _Tn3270PortLanguageName_Type()
)
tn3270PortLanguageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortLanguageName.setStatus("mandatory")


class _Tn3270PortExtendedAttributes_Type(Integer32):
    """Custom type tn3270PortExtendedAttributes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Tn3270PortExtendedAttributes_Type.__name__ = "Integer32"
_Tn3270PortExtendedAttributes_Object = MibTableColumn
tn3270PortExtendedAttributes = _Tn3270PortExtendedAttributes_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 4),
    _Tn3270PortExtendedAttributes_Type()
)
tn3270PortExtendedAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortExtendedAttributes.setStatus("mandatory")


class _Tn3270PortEorNegotiation_Type(Integer32):
    """Custom type tn3270PortEorNegotiation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Tn3270PortEorNegotiation_Type.__name__ = "Integer32"
_Tn3270PortEorNegotiation_Object = MibTableColumn
tn3270PortEorNegotiation = _Tn3270PortEorNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 5),
    _Tn3270PortEorNegotiation_Type()
)
tn3270PortEorNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortEorNegotiation.setStatus("mandatory")


class _Tn3270PortErrorLock_Type(Integer32):
    """Custom type tn3270PortErrorLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Tn3270PortErrorLock_Type.__name__ = "Integer32"
_Tn3270PortErrorLock_Object = MibTableColumn
tn3270PortErrorLock = _Tn3270PortErrorLock_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 7, 10, 1, 6),
    _Tn3270PortErrorLock_Type()
)
tn3270PortErrorLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270PortErrorLock.setStatus("mandatory")
_Kerberos_ObjectIdentity = ObjectIdentity
kerberos = _Kerberos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 8)
)


class _KerbStatus_Type(Integer32):
    """Custom type kerbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("none", 1))
    )


_KerbStatus_Type.__name__ = "Integer32"
_KerbStatus_Object = MibScalar
kerbStatus = _KerbStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 1),
    _KerbStatus_Type()
)
kerbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbStatus.setStatus("mandatory")


class _KerbRealm_Type(DisplayString):
    """Custom type kerbRealm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_KerbRealm_Type.__name__ = "DisplayString"
_KerbRealm_Object = MibScalar
kerbRealm = _KerbRealm_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 2),
    _KerbRealm_Type()
)
kerbRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbRealm.setStatus("mandatory")


class _KerbQueryLimit_Type(Integer32):
    """Custom type kerbQueryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_KerbQueryLimit_Type.__name__ = "Integer32"
_KerbQueryLimit_Object = MibScalar
kerbQueryLimit = _KerbQueryLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 3),
    _KerbQueryLimit_Type()
)
kerbQueryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbQueryLimit.setStatus("mandatory")


class _KerbMasterName_Type(DisplayString):
    """Custom type kerbMasterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbMasterName_Type.__name__ = "DisplayString"
_KerbMasterName_Object = MibScalar
kerbMasterName = _KerbMasterName_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 4),
    _KerbMasterName_Type()
)
kerbMasterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbMasterName.setStatus("mandatory")


class _KerbServerName1_Type(DisplayString):
    """Custom type kerbServerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbServerName1_Type.__name__ = "DisplayString"
_KerbServerName1_Object = MibScalar
kerbServerName1 = _KerbServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 5),
    _KerbServerName1_Type()
)
kerbServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbServerName1.setStatus("mandatory")


class _KerbServerName2_Type(DisplayString):
    """Custom type kerbServerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_KerbServerName2_Type.__name__ = "DisplayString"
_KerbServerName2_Object = MibScalar
kerbServerName2 = _KerbServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 6),
    _KerbServerName2_Type()
)
kerbServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbServerName2.setStatus("mandatory")
_KerbInsecureLogins_Type = Counter32
_KerbInsecureLogins_Object = MibScalar
kerbInsecureLogins = _KerbInsecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 7),
    _KerbInsecureLogins_Type()
)
kerbInsecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbInsecureLogins.setStatus("mandatory")
_KerbSecureLogins_Type = Counter32
_KerbSecureLogins_Object = MibScalar
kerbSecureLogins = _KerbSecureLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 8),
    _KerbSecureLogins_Type()
)
kerbSecureLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbSecureLogins.setStatus("mandatory")
_KerbSecureLoginsFailed_Type = Counter32
_KerbSecureLoginsFailed_Object = MibScalar
kerbSecureLoginsFailed = _KerbSecureLoginsFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 9),
    _KerbSecureLoginsFailed_Type()
)
kerbSecureLoginsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbSecureLoginsFailed.setStatus("mandatory")
_KerbPasswordChangeFailed_Type = Counter32
_KerbPasswordChangeFailed_Object = MibScalar
kerbPasswordChangeFailed = _KerbPasswordChangeFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 10),
    _KerbPasswordChangeFailed_Type()
)
kerbPasswordChangeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbPasswordChangeFailed.setStatus("mandatory")
_KerbError_Type = Integer32
_KerbError_Object = MibScalar
kerbError = _KerbError_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 11),
    _KerbError_Type()
)
kerbError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbError.setStatus("mandatory")
_KerbErrorTime_Type = DateTime
_KerbErrorTime_Object = MibScalar
kerbErrorTime = _KerbErrorTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 12),
    _KerbErrorTime_Type()
)
kerbErrorTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbErrorTime.setStatus("mandatory")
_KerbMasterAccess_Type = Counter32
_KerbMasterAccess_Object = MibScalar
kerbMasterAccess = _KerbMasterAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 13),
    _KerbMasterAccess_Type()
)
kerbMasterAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbMasterAccess.setStatus("mandatory")
_KerbMasterAccessFailed_Type = Counter32
_KerbMasterAccessFailed_Object = MibScalar
kerbMasterAccessFailed = _KerbMasterAccessFailed_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 14),
    _KerbMasterAccessFailed_Type()
)
kerbMasterAccessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbMasterAccessFailed.setStatus("mandatory")
_KerbServerAccess1_Type = Counter32
_KerbServerAccess1_Object = MibScalar
kerbServerAccess1 = _KerbServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 15),
    _KerbServerAccess1_Type()
)
kerbServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccess1.setStatus("mandatory")
_KerbServerAccessFailed1_Type = Counter32
_KerbServerAccessFailed1_Object = MibScalar
kerbServerAccessFailed1 = _KerbServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 16),
    _KerbServerAccessFailed1_Type()
)
kerbServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccessFailed1.setStatus("mandatory")
_KerbServerAccess2_Type = Counter32
_KerbServerAccess2_Object = MibScalar
kerbServerAccess2 = _KerbServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 17),
    _KerbServerAccess2_Type()
)
kerbServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccess2.setStatus("mandatory")
_KerbServerAccessFailed2_Type = Counter32
_KerbServerAccessFailed2_Object = MibScalar
kerbServerAccessFailed2 = _KerbServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 18),
    _KerbServerAccessFailed2_Type()
)
kerbServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbServerAccessFailed2.setStatus("mandatory")
_KerbPortTable_Object = MibTable
kerbPortTable = _KerbPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19)
)
if mibBuilder.loadTexts:
    kerbPortTable.setStatus("mandatory")
_KerbPortEntry_Object = MibTableRow
kerbPortEntry = _KerbPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1)
)
kerbPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "kerbPortIndex"),
)
if mibBuilder.loadTexts:
    kerbPortEntry.setStatus("mandatory")
_KerbPortIndex_Type = Integer32
_KerbPortIndex_Object = MibTableColumn
kerbPortIndex = _KerbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1, 1),
    _KerbPortIndex_Type()
)
kerbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kerbPortIndex.setStatus("mandatory")


class _KerbPortStatus_Type(Integer32):
    """Custom type kerbPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("login", 2),
          ("none", 1))
    )


_KerbPortStatus_Type.__name__ = "Integer32"
_KerbPortStatus_Object = MibTableColumn
kerbPortStatus = _KerbPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 8, 19, 1, 2),
    _KerbPortStatus_Type()
)
kerbPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kerbPortStatus.setStatus("mandatory")
_PortSecurity_ObjectIdentity = ObjectIdentity
portSecurity = _PortSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 9)
)
_PsEntryNumber_Type = Integer32
_PsEntryNumber_Object = MibScalar
psEntryNumber = _PsEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 1),
    _PsEntryNumber_Type()
)
psEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryNumber.setStatus("mandatory")
_PsEntryNumberLimit_Type = Integer32
_PsEntryNumberLimit_Object = MibScalar
psEntryNumberLimit = _PsEntryNumberLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 2),
    _PsEntryNumberLimit_Type()
)
psEntryNumberLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryNumberLimit.setStatus("mandatory")
_PsEntryInvalidIndex_Type = Integer32
_PsEntryInvalidIndex_Object = MibScalar
psEntryInvalidIndex = _PsEntryInvalidIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 3),
    _PsEntryInvalidIndex_Type()
)
psEntryInvalidIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryInvalidIndex.setStatus("mandatory")
_PsPortTable_Object = MibTable
psPortTable = _PsPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4)
)
if mibBuilder.loadTexts:
    psPortTable.setStatus("mandatory")
_PsPortEntry_Object = MibTableRow
psPortEntry = _PsPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1)
)
psPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "psPortIndex"),
)
if mibBuilder.loadTexts:
    psPortEntry.setStatus("mandatory")
_PsPortIndex_Type = Integer32
_PsPortIndex_Object = MibTableColumn
psPortIndex = _PsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 1),
    _PsPortIndex_Type()
)
psPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psPortIndex.setStatus("mandatory")


class _PsPortDefaultInboundAccess_Type(Integer32):
    """Custom type psPortDefaultInboundAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsPortDefaultInboundAccess_Type.__name__ = "Integer32"
_PsPortDefaultInboundAccess_Object = MibTableColumn
psPortDefaultInboundAccess = _PsPortDefaultInboundAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 2),
    _PsPortDefaultInboundAccess_Type()
)
psPortDefaultInboundAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPortDefaultInboundAccess.setStatus("mandatory")


class _PsPortDefaultOutboundAccess_Type(Integer32):
    """Custom type psPortDefaultOutboundAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsPortDefaultOutboundAccess_Type.__name__ = "Integer32"
_PsPortDefaultOutboundAccess_Object = MibTableColumn
psPortDefaultOutboundAccess = _PsPortDefaultOutboundAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 4, 1, 3),
    _PsPortDefaultOutboundAccess_Type()
)
psPortDefaultOutboundAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psPortDefaultOutboundAccess.setStatus("mandatory")
_PsTable_Object = MibTable
psTable = _PsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5)
)
if mibBuilder.loadTexts:
    psTable.setStatus("mandatory")
_PsEntry_Object = MibTableRow
psEntry = _PsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1)
)
psEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "psEntryIndex"),
)
if mibBuilder.loadTexts:
    psEntry.setStatus("mandatory")
_PsEntryIndex_Type = Integer32
_PsEntryIndex_Object = MibTableColumn
psEntryIndex = _PsEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 1),
    _PsEntryIndex_Type()
)
psEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psEntryIndex.setStatus("mandatory")


class _PsEntryStatus_Type(Integer32):
    """Custom type psEntryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_PsEntryStatus_Type.__name__ = "Integer32"
_PsEntryStatus_Object = MibTableColumn
psEntryStatus = _PsEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 2),
    _PsEntryStatus_Type()
)
psEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryStatus.setStatus("mandatory")
_PsEntryAddress_Type = IpAddress
_PsEntryAddress_Object = MibTableColumn
psEntryAddress = _PsEntryAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 3),
    _PsEntryAddress_Type()
)
psEntryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryAddress.setStatus("mandatory")
_PsEntryMask_Type = IpAddress
_PsEntryMask_Object = MibTableColumn
psEntryMask = _PsEntryMask_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 4),
    _PsEntryMask_Type()
)
psEntryMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryMask.setStatus("mandatory")


class _PsEntryAccess_Type(Integer32):
    """Custom type psEntryAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_PsEntryAccess_Type.__name__ = "Integer32"
_PsEntryAccess_Object = MibTableColumn
psEntryAccess = _PsEntryAccess_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 5),
    _PsEntryAccess_Type()
)
psEntryAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryAccess.setStatus("mandatory")


class _PsEntryDirection_Type(Integer32):
    """Custom type psEntryDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_PsEntryDirection_Type.__name__ = "Integer32"
_PsEntryDirection_Object = MibTableColumn
psEntryDirection = _PsEntryDirection_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 6),
    _PsEntryDirection_Type()
)
psEntryDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryDirection.setStatus("mandatory")
_PsEntryPortMap_Type = OctetString
_PsEntryPortMap_Object = MibTableColumn
psEntryPortMap = _PsEntryPortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 9, 5, 1, 7),
    _PsEntryPortMap_Type()
)
psEntryPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psEntryPortMap.setStatus("mandatory")
_Xremote_ObjectIdentity = ObjectIdentity
xremote = _Xremote_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 10)
)


class _XremoteServerName1_Type(DisplayString):
    """Custom type xremoteServerName1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremoteServerName1_Type.__name__ = "DisplayString"
_XremoteServerName1_Object = MibScalar
xremoteServerName1 = _XremoteServerName1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 1),
    _XremoteServerName1_Type()
)
xremoteServerName1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremoteServerName1.setStatus("mandatory")


class _XremoteServerName2_Type(DisplayString):
    """Custom type xremoteServerName2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremoteServerName2_Type.__name__ = "DisplayString"
_XremoteServerName2_Object = MibScalar
xremoteServerName2 = _XremoteServerName2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 2),
    _XremoteServerName2_Type()
)
xremoteServerName2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremoteServerName2.setStatus("mandatory")
_XremoteServerAccess1_Type = Counter32
_XremoteServerAccess1_Object = MibScalar
xremoteServerAccess1 = _XremoteServerAccess1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 3),
    _XremoteServerAccess1_Type()
)
xremoteServerAccess1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccess1.setStatus("mandatory")
_XremoteServerAccessFailed1_Type = Counter32
_XremoteServerAccessFailed1_Object = MibScalar
xremoteServerAccessFailed1 = _XremoteServerAccessFailed1_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 4),
    _XremoteServerAccessFailed1_Type()
)
xremoteServerAccessFailed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccessFailed1.setStatus("mandatory")
_XremoteServerAccess2_Type = Counter32
_XremoteServerAccess2_Object = MibScalar
xremoteServerAccess2 = _XremoteServerAccess2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 5),
    _XremoteServerAccess2_Type()
)
xremoteServerAccess2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccess2.setStatus("mandatory")
_XremoteServerAccessFailed2_Type = Counter32
_XremoteServerAccessFailed2_Object = MibScalar
xremoteServerAccessFailed2 = _XremoteServerAccessFailed2_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 6),
    _XremoteServerAccessFailed2_Type()
)
xremoteServerAccessFailed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerAccessFailed2.setStatus("mandatory")
_XremoteSessions_Type = Gauge32
_XremoteSessions_Object = MibScalar
xremoteSessions = _XremoteSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 7),
    _XremoteSessions_Type()
)
xremoteSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteSessions.setStatus("mandatory")
_XremotePortTable_Object = MibTable
xremotePortTable = _XremotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8)
)
if mibBuilder.loadTexts:
    xremotePortTable.setStatus("mandatory")
_XremotePortEntry_Object = MibTableRow
xremotePortEntry = _XremotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1)
)
xremotePortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "psPortIndex"),
)
if mibBuilder.loadTexts:
    xremotePortEntry.setStatus("mandatory")
_XremotePortIndex_Type = Integer32
_XremotePortIndex_Object = MibTableColumn
xremotePortIndex = _XremotePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 1),
    _XremotePortIndex_Type()
)
xremotePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremotePortIndex.setStatus("mandatory")


class _XremotePortXremote_Type(Integer32):
    """Custom type xremotePortXremote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_XremotePortXremote_Type.__name__ = "Integer32"
_XremotePortXremote_Object = MibTableColumn
xremotePortXremote = _XremotePortXremote_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 2),
    _XremotePortXremote_Type()
)
xremotePortXremote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXremote.setStatus("mandatory")


class _XremotePortXdmQuery_Type(Integer32):
    """Custom type xremotePortXdmQuery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("indirect", 3),
          ("specific", 1))
    )


_XremotePortXdmQuery_Type.__name__ = "Integer32"
_XremotePortXdmQuery_Object = MibTableColumn
xremotePortXdmQuery = _XremotePortXdmQuery_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 3),
    _XremotePortXdmQuery_Type()
)
xremotePortXdmQuery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXdmQuery.setStatus("mandatory")


class _XremotePortXdmHost_Type(DisplayString):
    """Custom type xremotePortXdmHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_XremotePortXdmHost_Type.__name__ = "DisplayString"
_XremotePortXdmHost_Object = MibTableColumn
xremotePortXdmHost = _XremotePortXdmHost_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 8, 1, 4),
    _XremotePortXdmHost_Type()
)
xremotePortXdmHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xremotePortXdmHost.setStatus("mandatory")
_XremoteServerClients_Type = Gauge32
_XremoteServerClients_Object = MibScalar
xremoteServerClients = _XremoteServerClients_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 10, 9),
    _XremoteServerClients_Type()
)
xremoteServerClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xremoteServerClients.setStatus("mandatory")
_Rotary_ObjectIdentity = ObjectIdentity
rotary = _Rotary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 11)
)
_RotaryNumber_Type = Integer32
_RotaryNumber_Object = MibScalar
rotaryNumber = _RotaryNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 1),
    _RotaryNumber_Type()
)
rotaryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rotaryNumber.setStatus("mandatory")
_RotaryTable_Object = MibTable
rotaryTable = _RotaryTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2)
)
if mibBuilder.loadTexts:
    rotaryTable.setStatus("mandatory")
_RotaryEntry_Object = MibTableRow
rotaryEntry = _RotaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1)
)
rotaryEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "rotaryAddress"),
)
if mibBuilder.loadTexts:
    rotaryEntry.setStatus("mandatory")
_RotaryAddress_Type = IpAddress
_RotaryAddress_Object = MibTableColumn
rotaryAddress = _RotaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 1),
    _RotaryAddress_Type()
)
rotaryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rotaryAddress.setStatus("mandatory")


class _RotaryStatus_Type(Integer32):
    """Custom type rotaryStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_RotaryStatus_Type.__name__ = "Integer32"
_RotaryStatus_Object = MibTableColumn
rotaryStatus = _RotaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 2),
    _RotaryStatus_Type()
)
rotaryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rotaryStatus.setStatus("mandatory")
_RotaryPortMap_Type = OctetString
_RotaryPortMap_Object = MibTableColumn
rotaryPortMap = _RotaryPortMap_Object(
    (1, 3, 6, 1, 4, 1, 33, 10, 11, 2, 1, 3),
    _RotaryPortMap_Type()
)
rotaryPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rotaryPortMap.setStatus("mandatory")
_XEgp_ObjectIdentity = ObjectIdentity
xEgp = _XEgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 12)
)
_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 13)
)
_RouterIp_ObjectIdentity = ObjectIdentity
routerIp = _RouterIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 14)
)
_RouterUdp_ObjectIdentity = ObjectIdentity
routerUdp = _RouterUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 15)
)
_RouterPolicy_ObjectIdentity = ObjectIdentity
routerPolicy = _RouterPolicy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 10, 16)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 11)
)
_EtherTable_Object = MibTable
etherTable = _EtherTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1)
)
if mibBuilder.loadTexts:
    etherTable.setStatus("mandatory")
_EtherEntry_Object = MibTableRow
etherEntry = _EtherEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1)
)
etherEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "etherIndex"),
)
if mibBuilder.loadTexts:
    etherEntry.setStatus("mandatory")
_EtherIndex_Type = Integer32
_EtherIndex_Object = MibTableColumn
etherIndex = _EtherIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 1),
    _EtherIndex_Type()
)
etherIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherIndex.setStatus("mandatory")
_EtherAlignmentErrors_Type = Counter32
_EtherAlignmentErrors_Object = MibTableColumn
etherAlignmentErrors = _EtherAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 2),
    _EtherAlignmentErrors_Type()
)
etherAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherAlignmentErrors.setStatus("mandatory")
_EtherFCSErrors_Type = Counter32
_EtherFCSErrors_Object = MibTableColumn
etherFCSErrors = _EtherFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 1, 1, 3),
    _EtherFCSErrors_Type()
)
etherFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherFCSErrors.setStatus("mandatory")
_EtherTxTable_Object = MibTable
etherTxTable = _EtherTxTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2)
)
if mibBuilder.loadTexts:
    etherTxTable.setStatus("mandatory")
_EtherTxEntry_Object = MibTableRow
etherTxEntry = _EtherTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1)
)
etherTxEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "etherTxIndex"),
)
if mibBuilder.loadTexts:
    etherTxEntry.setStatus("mandatory")
_EtherTxIndex_Type = Integer32
_EtherTxIndex_Object = MibTableColumn
etherTxIndex = _EtherTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 1),
    _EtherTxIndex_Type()
)
etherTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxIndex.setStatus("mandatory")
_EtherTxSingleCollisionFrames_Type = Counter32
_EtherTxSingleCollisionFrames_Object = MibTableColumn
etherTxSingleCollisionFrames = _EtherTxSingleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 2),
    _EtherTxSingleCollisionFrames_Type()
)
etherTxSingleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxSingleCollisionFrames.setStatus("mandatory")
_EtherTxMultipleCollisionFrames_Type = Counter32
_EtherTxMultipleCollisionFrames_Object = MibTableColumn
etherTxMultipleCollisionFrames = _EtherTxMultipleCollisionFrames_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 2, 1, 3),
    _EtherTxMultipleCollisionFrames_Type()
)
etherTxMultipleCollisionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherTxMultipleCollisionFrames.setStatus("mandatory")
_EtherMulticastTable_Object = MibTable
etherMulticastTable = _EtherMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3)
)
if mibBuilder.loadTexts:
    etherMulticastTable.setStatus("mandatory")
_EtherMulticastEntry_Object = MibTableRow
etherMulticastEntry = _EtherMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1)
)
etherMulticastEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "etherMulticastIndex"),
)
if mibBuilder.loadTexts:
    etherMulticastEntry.setStatus("mandatory")
_EtherMulticastIndex_Type = Integer32
_EtherMulticastIndex_Object = MibTableColumn
etherMulticastIndex = _EtherMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 1),
    _EtherMulticastIndex_Type()
)
etherMulticastIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastIndex.setStatus("mandatory")
_EtherMulticastBytesIn_Type = Counter32
_EtherMulticastBytesIn_Object = MibTableColumn
etherMulticastBytesIn = _EtherMulticastBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 2),
    _EtherMulticastBytesIn_Type()
)
etherMulticastBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastBytesIn.setStatus("mandatory")
_EtherMulticastBytesOut_Type = Counter32
_EtherMulticastBytesOut_Object = MibTableColumn
etherMulticastBytesOut = _EtherMulticastBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 3, 1, 3),
    _EtherMulticastBytesOut_Type()
)
etherMulticastBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherMulticastBytesOut.setStatus("mandatory")
_EtherXTxTable_Object = MibTable
etherXTxTable = _EtherXTxTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4)
)
if mibBuilder.loadTexts:
    etherXTxTable.setStatus("mandatory")
_EtherXTxEntry_Object = MibTableRow
etherXTxEntry = _EtherXTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1)
)
etherXTxEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "etherXTxIndex"),
)
if mibBuilder.loadTexts:
    etherXTxEntry.setStatus("mandatory")
_EtherXTxIndex_Type = Integer32
_EtherXTxIndex_Object = MibTableColumn
etherXTxIndex = _EtherXTxIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 1),
    _EtherXTxIndex_Type()
)
etherXTxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherXTxIndex.setStatus("mandatory")
_EtherXTxExcessiveCollisions_Type = Counter32
_EtherXTxExcessiveCollisions_Object = MibTableColumn
etherXTxExcessiveCollisions = _EtherXTxExcessiveCollisions_Object(
    (1, 3, 6, 1, 4, 1, 33, 11, 4, 1, 2),
    _EtherXTxExcessiveCollisions_Type()
)
etherXTxExcessiveCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etherXTxExcessiveCollisions.setStatus("mandatory")
_BootClient_ObjectIdentity = ObjectIdentity
bootClient = _BootClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 12)
)


class _BootClientStatus_Type(DisplayString):
    """Custom type bootClientStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_BootClientStatus_Type.__name__ = "DisplayString"
_BootClientStatus_Object = MibScalar
bootClientStatus = _BootClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 12, 1),
    _BootClientStatus_Type()
)
bootClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootClientStatus.setStatus("mandatory")
_Character_ObjectIdentity = ObjectIdentity
character = _Character_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13)
)
_Basic_ObjectIdentity = ObjectIdentity
basic = _Basic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 1)
)


class _BasicBroadcast_Type(Integer32):
    """Custom type basicBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicBroadcast_Type.__name__ = "Integer32"
_BasicBroadcast_Object = MibScalar
basicBroadcast = _BasicBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 1),
    _BasicBroadcast_Type()
)
basicBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicBroadcast.setStatus("mandatory")


class _BasicErrorReport_Type(Integer32):
    """Custom type basicErrorReport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicErrorReport_Type.__name__ = "Integer32"
_BasicErrorReport_Object = MibScalar
basicErrorReport = _BasicErrorReport_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 2),
    _BasicErrorReport_Type()
)
basicErrorReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicErrorReport.setStatus("mandatory")


class _BasicLock_Type(Integer32):
    """Custom type basicLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicLock_Type.__name__ = "Integer32"
_BasicLock_Object = MibScalar
basicLock = _BasicLock_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 3),
    _BasicLock_Type()
)
basicLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLock.setStatus("mandatory")


class _BasicInactivityTimer_Type(Integer32):
    """Custom type basicInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_BasicInactivityTimer_Type.__name__ = "Integer32"
_BasicInactivityTimer_Object = MibScalar
basicInactivityTimer = _BasicInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 4),
    _BasicInactivityTimer_Type()
)
basicInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicInactivityTimer.setStatus("mandatory")


class _BasicPasswordRetryLimit_Type(Integer32):
    """Custom type basicPasswordRetryLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_BasicPasswordRetryLimit_Type.__name__ = "Integer32"
_BasicPasswordRetryLimit_Object = MibScalar
basicPasswordRetryLimit = _BasicPasswordRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 5),
    _BasicPasswordRetryLimit_Type()
)
basicPasswordRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPasswordRetryLimit.setStatus("mandatory")


class _BasicPrivilegedPassword_Type(DisplayString):
    """Custom type basicPrivilegedPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BasicPrivilegedPassword_Type.__name__ = "DisplayString"
_BasicPrivilegedPassword_Object = MibScalar
basicPrivilegedPassword = _BasicPrivilegedPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 6),
    _BasicPrivilegedPassword_Type()
)
basicPrivilegedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPrivilegedPassword.setStatus("mandatory")


class _BasicLoginPassword_Type(DisplayString):
    """Custom type basicLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BasicLoginPassword_Type.__name__ = "DisplayString"
_BasicLoginPassword_Object = MibScalar
basicLoginPassword = _BasicLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 7),
    _BasicLoginPassword_Type()
)
basicLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLoginPassword.setStatus("mandatory")


class _BasicLoginPrompt_Type(DisplayString):
    """Custom type basicLoginPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BasicLoginPrompt_Type.__name__ = "DisplayString"
_BasicLoginPrompt_Object = MibScalar
basicLoginPrompt = _BasicLoginPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 8),
    _BasicLoginPrompt_Type()
)
basicLoginPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicLoginPrompt.setStatus("mandatory")


class _BasicWelcome_Type(DisplayString):
    """Custom type basicWelcome based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_BasicWelcome_Type.__name__ = "DisplayString"
_BasicWelcome_Object = MibScalar
basicWelcome = _BasicWelcome_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 9),
    _BasicWelcome_Type()
)
basicWelcome.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicWelcome.setStatus("mandatory")
_BasicActivePorts_Type = Gauge32
_BasicActivePorts_Object = MibScalar
basicActivePorts = _BasicActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 10),
    _BasicActivePorts_Type()
)
basicActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActivePorts.setStatus("mandatory")
_BasicActivePortsHigh_Type = Gauge32
_BasicActivePortsHigh_Object = MibScalar
basicActivePortsHigh = _BasicActivePortsHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 11),
    _BasicActivePortsHigh_Type()
)
basicActivePortsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActivePortsHigh.setStatus("mandatory")
_BasicActiveUsers_Type = Gauge32
_BasicActiveUsers_Object = MibScalar
basicActiveUsers = _BasicActiveUsers_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 12),
    _BasicActiveUsers_Type()
)
basicActiveUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveUsers.setStatus("mandatory")
_BasicActiveUsersHigh_Type = Gauge32
_BasicActiveUsersHigh_Object = MibScalar
basicActiveUsersHigh = _BasicActiveUsersHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 13),
    _BasicActiveUsersHigh_Type()
)
basicActiveUsersHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicActiveUsersHigh.setStatus("mandatory")
_BasicSessions_Type = Gauge32
_BasicSessions_Object = MibScalar
basicSessions = _BasicSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 14),
    _BasicSessions_Type()
)
basicSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSessions.setStatus("mandatory")
_BasicSessionsHigh_Type = Gauge32
_BasicSessionsHigh_Object = MibScalar
basicSessionsHigh = _BasicSessionsHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 15),
    _BasicSessionsHigh_Type()
)
basicSessionsHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSessionsHigh.setStatus("mandatory")


class _BasicSessionsLimit_Type(Integer32):
    """Custom type basicSessionsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 64),
    )


_BasicSessionsLimit_Type.__name__ = "Integer32"
_BasicSessionsLimit_Object = MibScalar
basicSessionsLimit = _BasicSessionsLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 16),
    _BasicSessionsLimit_Type()
)
basicSessionsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSessionsLimit.setStatus("mandatory")
_BasicPortTable_Object = MibTable
basicPortTable = _BasicPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17)
)
if mibBuilder.loadTexts:
    basicPortTable.setStatus("mandatory")
_BasicPortEntry_Object = MibTableRow
basicPortEntry = _BasicPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1)
)
basicPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "basicPortIndex"),
)
if mibBuilder.loadTexts:
    basicPortEntry.setStatus("mandatory")
_BasicPortIndex_Type = Integer32
_BasicPortIndex_Object = MibTableColumn
basicPortIndex = _BasicPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 1),
    _BasicPortIndex_Type()
)
basicPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortIndex.setStatus("mandatory")


class _BasicPortDefaultDestAction_Type(Integer32):
    """Custom type basicPortDefaultDestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("preferred", 2))
    )


_BasicPortDefaultDestAction_Type.__name__ = "Integer32"
_BasicPortDefaultDestAction_Object = MibTableColumn
basicPortDefaultDestAction = _BasicPortDefaultDestAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 2),
    _BasicPortDefaultDestAction_Type()
)
basicPortDefaultDestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestAction.setStatus("mandatory")


class _BasicPortDefaultDestProtocol_Type(Integer32):
    """Custom type basicPortDefaultDestProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("lat", 1),
          ("telnet", 2))
    )


_BasicPortDefaultDestProtocol_Type.__name__ = "Integer32"
_BasicPortDefaultDestProtocol_Object = MibTableColumn
basicPortDefaultDestProtocol = _BasicPortDefaultDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 3),
    _BasicPortDefaultDestProtocol_Type()
)
basicPortDefaultDestProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestProtocol.setStatus("mandatory")


class _BasicPortDefaultDestName_Type(DisplayString):
    """Custom type basicPortDefaultDestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_BasicPortDefaultDestName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestName_Object = MibTableColumn
basicPortDefaultDestName = _BasicPortDefaultDestName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 4),
    _BasicPortDefaultDestName_Type()
)
basicPortDefaultDestName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestName.setStatus("mandatory")


class _BasicPortDefaultDestLATNodeName_Type(DisplayString):
    """Custom type basicPortDefaultDestLATNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultDestLATNodeName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestLATNodeName_Object = MibTableColumn
basicPortDefaultDestLATNodeName = _BasicPortDefaultDestLATNodeName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 5),
    _BasicPortDefaultDestLATNodeName_Type()
)
basicPortDefaultDestLATNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestLATNodeName.setStatus("mandatory")


class _BasicPortDefaultDestLATPortName_Type(DisplayString):
    """Custom type basicPortDefaultDestLATPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultDestLATPortName_Type.__name__ = "DisplayString"
_BasicPortDefaultDestLATPortName_Object = MibTableColumn
basicPortDefaultDestLATPortName = _BasicPortDefaultDestLATPortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 6),
    _BasicPortDefaultDestLATPortName_Type()
)
basicPortDefaultDestLATPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultDestLATPortName.setStatus("mandatory")


class _BasicPortAutoConnect_Type(Integer32):
    """Custom type basicPortAutoConnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAutoConnect_Type.__name__ = "Integer32"
_BasicPortAutoConnect_Object = MibTableColumn
basicPortAutoConnect = _BasicPortAutoConnect_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 7),
    _BasicPortAutoConnect_Type()
)
basicPortAutoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAutoConnect.setStatus("mandatory")


class _BasicPortAutoLogin_Type(Integer32):
    """Custom type basicPortAutoLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortAutoLogin_Type.__name__ = "Integer32"
_BasicPortAutoLogin_Object = MibTableColumn
basicPortAutoLogin = _BasicPortAutoLogin_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 8),
    _BasicPortAutoLogin_Type()
)
basicPortAutoLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortAutoLogin.setStatus("mandatory")


class _BasicPortBroadcast_Type(Integer32):
    """Custom type basicPortBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortBroadcast_Type.__name__ = "Integer32"
_BasicPortBroadcast_Object = MibTableColumn
basicPortBroadcast = _BasicPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 9),
    _BasicPortBroadcast_Type()
)
basicPortBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortBroadcast.setStatus("mandatory")


class _BasicPortConnectResume_Type(Integer32):
    """Custom type basicPortConnectResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortConnectResume_Type.__name__ = "Integer32"
_BasicPortConnectResume_Object = MibTableColumn
basicPortConnectResume = _BasicPortConnectResume_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 10),
    _BasicPortConnectResume_Type()
)
basicPortConnectResume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortConnectResume.setStatus("mandatory")


class _BasicPortDialup_Type(Integer32):
    """Custom type basicPortDialup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortDialup_Type.__name__ = "Integer32"
_BasicPortDialup_Object = MibTableColumn
basicPortDialup = _BasicPortDialup_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 11),
    _BasicPortDialup_Type()
)
basicPortDialup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDialup.setStatus("mandatory")


class _BasicPortIdleTimeout_Type(Integer32):
    """Custom type basicPortIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_BasicPortIdleTimeout_Type.__name__ = "Integer32"
_BasicPortIdleTimeout_Object = MibTableColumn
basicPortIdleTimeout = _BasicPortIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 12),
    _BasicPortIdleTimeout_Type()
)
basicPortIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortIdleTimeout.setStatus("mandatory")


class _BasicPortInactivityLogout_Type(Integer32):
    """Custom type basicPortInactivityLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortInactivityLogout_Type.__name__ = "Integer32"
_BasicPortInactivityLogout_Object = MibTableColumn
basicPortInactivityLogout = _BasicPortInactivityLogout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 13),
    _BasicPortInactivityLogout_Type()
)
basicPortInactivityLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortInactivityLogout.setStatus("mandatory")


class _BasicPortLossNotification_Type(Integer32):
    """Custom type basicPortLossNotification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortLossNotification_Type.__name__ = "Integer32"
_BasicPortLossNotification_Object = MibTableColumn
basicPortLossNotification = _BasicPortLossNotification_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 14),
    _BasicPortLossNotification_Type()
)
basicPortLossNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortLossNotification.setStatus("mandatory")


class _BasicPortMessageCodes_Type(Integer32):
    """Custom type basicPortMessageCodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortMessageCodes_Type.__name__ = "Integer32"
_BasicPortMessageCodes_Object = MibTableColumn
basicPortMessageCodes = _BasicPortMessageCodes_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 15),
    _BasicPortMessageCodes_Type()
)
basicPortMessageCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortMessageCodes.setStatus("mandatory")


class _BasicPortMultisessions_Type(Integer32):
    """Custom type basicPortMultisessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortMultisessions_Type.__name__ = "Integer32"
_BasicPortMultisessions_Object = MibTableColumn
basicPortMultisessions = _BasicPortMultisessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 16),
    _BasicPortMultisessions_Type()
)
basicPortMultisessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortMultisessions.setStatus("mandatory")


class _BasicPortDefaultUserName_Type(DisplayString):
    """Custom type basicPortDefaultUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortDefaultUserName_Type.__name__ = "DisplayString"
_BasicPortDefaultUserName_Object = MibTableColumn
basicPortDefaultUserName = _BasicPortDefaultUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 17),
    _BasicPortDefaultUserName_Type()
)
basicPortDefaultUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultUserName.setStatus("mandatory")


class _BasicPortVerification_Type(Integer32):
    """Custom type basicPortVerification based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicPortVerification_Type.__name__ = "Integer32"
_BasicPortVerification_Object = MibTableColumn
basicPortVerification = _BasicPortVerification_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 18),
    _BasicPortVerification_Type()
)
basicPortVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortVerification.setStatus("mandatory")


class _BasicPortDefaultProtocol_Type(Integer32):
    """Custom type basicPortDefaultProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("lat", 1),
          ("telnet", 2))
    )


_BasicPortDefaultProtocol_Type.__name__ = "Integer32"
_BasicPortDefaultProtocol_Object = MibTableColumn
basicPortDefaultProtocol = _BasicPortDefaultProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 19),
    _BasicPortDefaultProtocol_Type()
)
basicPortDefaultProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultProtocol.setStatus("mandatory")
_BasicPortLogins_Type = Counter32
_BasicPortLogins_Object = MibTableColumn
basicPortLogins = _BasicPortLogins_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 20),
    _BasicPortLogins_Type()
)
basicPortLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLogins.setStatus("mandatory")
_BasicPortRemoteSessions_Type = Counter32
_BasicPortRemoteSessions_Object = MibTableColumn
basicPortRemoteSessions = _BasicPortRemoteSessions_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 21),
    _BasicPortRemoteSessions_Type()
)
basicPortRemoteSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortRemoteSessions.setStatus("mandatory")
_BasicPortIdleTimeouts_Type = Counter32
_BasicPortIdleTimeouts_Object = MibTableColumn
basicPortIdleTimeouts = _BasicPortIdleTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 22),
    _BasicPortIdleTimeouts_Type()
)
basicPortIdleTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortIdleTimeouts.setStatus("mandatory")


class _BasicPortStatus_Type(Integer32):
    """Custom type basicPortStatus based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38)
        )
    )
    namedValues = NamedValues(
        *(("autobaud", 27),
          ("available", 28),
          ("cancelQueue", 26),
          ("checkConnect", 6),
          ("checkModem", 29),
          ("connectPassword", 23),
          ("connectWait", 16),
          ("connected", 8),
          ("connecting", 5),
          ("dialback1", 35),
          ("dialback2", 36),
          ("dialback3", 37),
          ("disconnect", 10),
          ("disconnecting", 9),
          ("executingCommand", 4),
          ("idle", 1),
          ("local", 2),
          ("locked", 12),
          ("login", 18),
          ("loginWait", 14),
          ("logout", 17),
          ("permanent", 13),
          ("reset", 20),
          ("retryConnect", 15),
          ("scriptLoad", 33),
          ("scriptRun", 34),
          ("scriptSearch", 32),
          ("signalWait", 31),
          ("slip", 30),
          ("suspended", 11),
          ("testServiceOut", 22),
          ("testServiceWait", 21),
          ("waitInput", 3),
          ("waitLogout", 24),
          ("waitOutput", 7),
          ("waitQueue", 25),
          ("waitSession", 19),
          ("xremote", 38))
    )


_BasicPortStatus_Type.__name__ = "Integer32"
_BasicPortStatus_Object = MibTableColumn
basicPortStatus = _BasicPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 23),
    _BasicPortStatus_Type()
)
basicPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortStatus.setStatus("mandatory")


class _BasicPortLastInCharacter_Type(Integer32):
    """Custom type basicPortLastInCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicPortLastInCharacter_Type.__name__ = "Integer32"
_BasicPortLastInCharacter_Object = MibTableColumn
basicPortLastInCharacter = _BasicPortLastInCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 24),
    _BasicPortLastInCharacter_Type()
)
basicPortLastInCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLastInCharacter.setStatus("mandatory")


class _BasicPortLastOutCharacter_Type(Integer32):
    """Custom type basicPortLastOutCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicPortLastOutCharacter_Type.__name__ = "Integer32"
_BasicPortLastOutCharacter_Object = MibTableColumn
basicPortLastOutCharacter = _BasicPortLastOutCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 25),
    _BasicPortLastOutCharacter_Type()
)
basicPortLastOutCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortLastOutCharacter.setStatus("mandatory")


class _BasicPortActiveUserName_Type(DisplayString):
    """Custom type basicPortActiveUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_BasicPortActiveUserName_Type.__name__ = "DisplayString"
_BasicPortActiveUserName_Object = MibTableColumn
basicPortActiveUserName = _BasicPortActiveUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 26),
    _BasicPortActiveUserName_Type()
)
basicPortActiveUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortActiveUserName.setStatus("mandatory")


class _BasicPortDefaultSessionMode_Type(Integer32):
    """Custom type basicPortDefaultSessionMode based on Integer32"""
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
        *(("binary", 2),
          ("binaryWithFlow", 3),
          ("interactive", 1),
          ("transparent", 4))
    )


_BasicPortDefaultSessionMode_Type.__name__ = "Integer32"
_BasicPortDefaultSessionMode_Object = MibTableColumn
basicPortDefaultSessionMode = _BasicPortDefaultSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 27),
    _BasicPortDefaultSessionMode_Type()
)
basicPortDefaultSessionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortDefaultSessionMode.setStatus("mandatory")


class _BasicPortZero_Type(Integer32):
    """Custom type basicPortZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_BasicPortZero_Type.__name__ = "Integer32"
_BasicPortZero_Object = MibTableColumn
basicPortZero = _BasicPortZero_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 28),
    _BasicPortZero_Type()
)
basicPortZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicPortZero.setStatus("mandatory")
_BasicPortZeroTime_Type = TimeTicks
_BasicPortZeroTime_Object = MibTableColumn
basicPortZeroTime = _BasicPortZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 17, 1, 29),
    _BasicPortZeroTime_Type()
)
basicPortZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicPortZeroTime.setStatus("mandatory")
_BasicSerialPortTable_Object = MibTable
basicSerialPortTable = _BasicSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18)
)
if mibBuilder.loadTexts:
    basicSerialPortTable.setStatus("mandatory")
_BasicSerialPortEntry_Object = MibTableRow
basicSerialPortEntry = _BasicSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1)
)
basicSerialPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "basicSerialPortIndex"),
)
if mibBuilder.loadTexts:
    basicSerialPortEntry.setStatus("mandatory")
_BasicSerialPortIndex_Type = Integer32
_BasicSerialPortIndex_Object = MibTableColumn
basicSerialPortIndex = _BasicSerialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 1),
    _BasicSerialPortIndex_Type()
)
basicSerialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basicSerialPortIndex.setStatus("mandatory")


class _BasicSerialPortBreak_Type(Integer32):
    """Custom type basicSerialPortBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("localSwitch", 2),
          ("sendRemote", 3))
    )


_BasicSerialPortBreak_Type.__name__ = "Integer32"
_BasicSerialPortBreak_Object = MibTableColumn
basicSerialPortBreak = _BasicSerialPortBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 2),
    _BasicSerialPortBreak_Type()
)
basicSerialPortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortBreak.setStatus("mandatory")


class _BasicSerialPortInterrupts_Type(Integer32):
    """Custom type basicSerialPortInterrupts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortInterrupts_Type.__name__ = "Integer32"
_BasicSerialPortInterrupts_Object = MibTableColumn
basicSerialPortInterrupts = _BasicSerialPortInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 3),
    _BasicSerialPortInterrupts_Type()
)
basicSerialPortInterrupts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortInterrupts.setStatus("mandatory")


class _BasicSerialPortNoLoss_Type(Integer32):
    """Custom type basicSerialPortNoLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortNoLoss_Type.__name__ = "Integer32"
_BasicSerialPortNoLoss_Object = MibTableColumn
basicSerialPortNoLoss = _BasicSerialPortNoLoss_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 4),
    _BasicSerialPortNoLoss_Type()
)
basicSerialPortNoLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortNoLoss.setStatus("mandatory")


class _BasicSerialPortPause_Type(Integer32):
    """Custom type basicSerialPortPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortPause_Type.__name__ = "Integer32"
_BasicSerialPortPause_Object = MibTableColumn
basicSerialPortPause = _BasicSerialPortPause_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 5),
    _BasicSerialPortPause_Type()
)
basicSerialPortPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPause.setStatus("mandatory")


class _BasicSerialPortPrompt_Type(DisplayString):
    """Custom type basicSerialPortPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BasicSerialPortPrompt_Type.__name__ = "DisplayString"
_BasicSerialPortPrompt_Object = MibTableColumn
basicSerialPortPrompt = _BasicSerialPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 6),
    _BasicSerialPortPrompt_Type()
)
basicSerialPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPrompt.setStatus("mandatory")


class _BasicSerialPortTerminalType_Type(Integer32):
    """Custom type basicSerialPortTerminalType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("hardcopy", 2),
          ("softcopy", 3))
    )


_BasicSerialPortTerminalType_Type.__name__ = "Integer32"
_BasicSerialPortTerminalType_Object = MibTableColumn
basicSerialPortTerminalType = _BasicSerialPortTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 7),
    _BasicSerialPortTerminalType_Type()
)
basicSerialPortTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortTerminalType.setStatus("mandatory")


class _BasicSerialPortTypeaheadLimit_Type(Integer32):
    """Custom type basicSerialPortTypeaheadLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(80, 16384),
    )


_BasicSerialPortTypeaheadLimit_Type.__name__ = "Integer32"
_BasicSerialPortTypeaheadLimit_Object = MibTableColumn
basicSerialPortTypeaheadLimit = _BasicSerialPortTypeaheadLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 8),
    _BasicSerialPortTypeaheadLimit_Type()
)
basicSerialPortTypeaheadLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortTypeaheadLimit.setStatus("mandatory")


class _BasicSerialPortBackwardSwitch_Type(Integer32):
    """Custom type basicSerialPortBackwardSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortBackwardSwitch_Type.__name__ = "Integer32"
_BasicSerialPortBackwardSwitch_Object = MibTableColumn
basicSerialPortBackwardSwitch = _BasicSerialPortBackwardSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 9),
    _BasicSerialPortBackwardSwitch_Type()
)
basicSerialPortBackwardSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortBackwardSwitch.setStatus("mandatory")


class _BasicSerialPortForwardSwitch_Type(Integer32):
    """Custom type basicSerialPortForwardSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortForwardSwitch_Type.__name__ = "Integer32"
_BasicSerialPortForwardSwitch_Object = MibTableColumn
basicSerialPortForwardSwitch = _BasicSerialPortForwardSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 10),
    _BasicSerialPortForwardSwitch_Type()
)
basicSerialPortForwardSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortForwardSwitch.setStatus("mandatory")


class _BasicSerialPortLocalSwitch_Type(Integer32):
    """Custom type basicSerialPortLocalSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLocalSwitch_Type.__name__ = "Integer32"
_BasicSerialPortLocalSwitch_Object = MibTableColumn
basicSerialPortLocalSwitch = _BasicSerialPortLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 11),
    _BasicSerialPortLocalSwitch_Type()
)
basicSerialPortLocalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLocalSwitch.setStatus("mandatory")


class _BasicSerialPortModemControl_Type(Integer32):
    """Custom type basicSerialPortModemControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortModemControl_Type.__name__ = "Integer32"
_BasicSerialPortModemControl_Object = MibTableColumn
basicSerialPortModemControl = _BasicSerialPortModemControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 12),
    _BasicSerialPortModemControl_Type()
)
basicSerialPortModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortModemControl.setStatus("mandatory")


class _BasicSerialPortSignalCheck_Type(Integer32):
    """Custom type basicSerialPortSignalCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortSignalCheck_Type.__name__ = "Integer32"
_BasicSerialPortSignalCheck_Object = MibTableColumn
basicSerialPortSignalCheck = _BasicSerialPortSignalCheck_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 13),
    _BasicSerialPortSignalCheck_Type()
)
basicSerialPortSignalCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortSignalCheck.setStatus("mandatory")


class _BasicSerialPortDSRLogout_Type(Integer32):
    """Custom type basicSerialPortDSRLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortDSRLogout_Type.__name__ = "Integer32"
_BasicSerialPortDSRLogout_Object = MibTableColumn
basicSerialPortDSRLogout = _BasicSerialPortDSRLogout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 14),
    _BasicSerialPortDSRLogout_Type()
)
basicSerialPortDSRLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDSRLogout.setStatus("mandatory")


class _BasicSerialPortDSRObserve_Type(Integer32):
    """Custom type basicSerialPortDSRObserve based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortDSRObserve_Type.__name__ = "Integer32"
_BasicSerialPortDSRObserve_Object = MibTableColumn
basicSerialPortDSRObserve = _BasicSerialPortDSRObserve_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 15),
    _BasicSerialPortDSRObserve_Type()
)
basicSerialPortDSRObserve.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDSRObserve.setStatus("mandatory")


class _BasicSerialPortDCDTimeout_Type(Integer32):
    """Custom type basicSerialPortDCDTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_BasicSerialPortDCDTimeout_Type.__name__ = "Integer32"
_BasicSerialPortDCDTimeout_Object = MibTableColumn
basicSerialPortDCDTimeout = _BasicSerialPortDCDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 16),
    _BasicSerialPortDCDTimeout_Type()
)
basicSerialPortDCDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDCDTimeout.setStatus("mandatory")


class _BasicSerialPortDTRAssert_Type(Integer32):
    """Custom type basicSerialPortDTRAssert based on Integer32"""
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
        *(("always", 1),
          ("onConnection", 3),
          ("onConnectionOrRing", 2),
          ("onRing", 4))
    )


_BasicSerialPortDTRAssert_Type.__name__ = "Integer32"
_BasicSerialPortDTRAssert_Object = MibTableColumn
basicSerialPortDTRAssert = _BasicSerialPortDTRAssert_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 17),
    _BasicSerialPortDTRAssert_Type()
)
basicSerialPortDTRAssert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortDTRAssert.setStatus("mandatory")


class _BasicSerialPortLimitedCommands_Type(Integer32):
    """Custom type basicSerialPortLimitedCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLimitedCommands_Type.__name__ = "Integer32"
_BasicSerialPortLimitedCommands_Object = MibTableColumn
basicSerialPortLimitedCommands = _BasicSerialPortLimitedCommands_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 18),
    _BasicSerialPortLimitedCommands_Type()
)
basicSerialPortLimitedCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLimitedCommands.setStatus("mandatory")


class _BasicSerialPortLimitedView_Type(Integer32):
    """Custom type basicSerialPortLimitedView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLimitedView_Type.__name__ = "Integer32"
_BasicSerialPortLimitedView_Object = MibTableColumn
basicSerialPortLimitedView = _BasicSerialPortLimitedView_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 19),
    _BasicSerialPortLimitedView_Type()
)
basicSerialPortLimitedView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLimitedView.setStatus("mandatory")


class _BasicSerialPortPassword_Type(Integer32):
    """Custom type basicSerialPortPassword based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortPassword_Type.__name__ = "Integer32"
_BasicSerialPortPassword_Object = MibTableColumn
basicSerialPortPassword = _BasicSerialPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 20),
    _BasicSerialPortPassword_Type()
)
basicSerialPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortPassword.setStatus("mandatory")


class _BasicSerialPortLineEditor_Type(Integer32):
    """Custom type basicSerialPortLineEditor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicSerialPortLineEditor_Type.__name__ = "Integer32"
_BasicSerialPortLineEditor_Object = MibTableColumn
basicSerialPortLineEditor = _BasicSerialPortLineEditor_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 21),
    _BasicSerialPortLineEditor_Type()
)
basicSerialPortLineEditor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditor.setStatus("mandatory")


class _BasicSerialPortLineEditorBackspace_Type(Integer32):
    """Custom type basicSerialPortLineEditorBackspace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorBackspace_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorBackspace_Object = MibTableColumn
basicSerialPortLineEditorBackspace = _BasicSerialPortLineEditorBackspace_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 22),
    _BasicSerialPortLineEditorBackspace_Type()
)
basicSerialPortLineEditorBackspace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorBackspace.setStatus("mandatory")


class _BasicSerialPortLineEditorBeginning_Type(Integer32):
    """Custom type basicSerialPortLineEditorBeginning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorBeginning_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorBeginning_Object = MibTableColumn
basicSerialPortLineEditorBeginning = _BasicSerialPortLineEditorBeginning_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 23),
    _BasicSerialPortLineEditorBeginning_Type()
)
basicSerialPortLineEditorBeginning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorBeginning.setStatus("mandatory")


class _BasicSerialPortLineEditorCancel_Type(Integer32):
    """Custom type basicSerialPortLineEditorCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorCancel_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorCancel_Object = MibTableColumn
basicSerialPortLineEditorCancel = _BasicSerialPortLineEditorCancel_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 24),
    _BasicSerialPortLineEditorCancel_Type()
)
basicSerialPortLineEditorCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorCancel.setStatus("mandatory")


class _BasicSerialPortLineEditorDeleteBeginning_Type(Integer32):
    """Custom type basicSerialPortLineEditorDeleteBeginning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorDeleteBeginning_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorDeleteBeginning_Object = MibTableColumn
basicSerialPortLineEditorDeleteBeginning = _BasicSerialPortLineEditorDeleteBeginning_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 25),
    _BasicSerialPortLineEditorDeleteBeginning_Type()
)
basicSerialPortLineEditorDeleteBeginning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorDeleteBeginning.setStatus("mandatory")


class _BasicSerialPortLineEditorDeleteLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorDeleteLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorDeleteLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorDeleteLine_Object = MibTableColumn
basicSerialPortLineEditorDeleteLine = _BasicSerialPortLineEditorDeleteLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 26),
    _BasicSerialPortLineEditorDeleteLine_Type()
)
basicSerialPortLineEditorDeleteLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorDeleteLine.setStatus("mandatory")


class _BasicSerialPortLineEditorEnd_Type(Integer32):
    """Custom type basicSerialPortLineEditorEnd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorEnd_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorEnd_Object = MibTableColumn
basicSerialPortLineEditorEnd = _BasicSerialPortLineEditorEnd_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 27),
    _BasicSerialPortLineEditorEnd_Type()
)
basicSerialPortLineEditorEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorEnd.setStatus("mandatory")


class _BasicSerialPortLineEditorForward_Type(Integer32):
    """Custom type basicSerialPortLineEditorForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorForward_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorForward_Object = MibTableColumn
basicSerialPortLineEditorForward = _BasicSerialPortLineEditorForward_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 28),
    _BasicSerialPortLineEditorForward_Type()
)
basicSerialPortLineEditorForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorForward.setStatus("mandatory")


class _BasicSerialPortLineEditorInsertToggle_Type(Integer32):
    """Custom type basicSerialPortLineEditorInsertToggle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorInsertToggle_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorInsertToggle_Object = MibTableColumn
basicSerialPortLineEditorInsertToggle = _BasicSerialPortLineEditorInsertToggle_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 29),
    _BasicSerialPortLineEditorInsertToggle_Type()
)
basicSerialPortLineEditorInsertToggle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorInsertToggle.setStatus("mandatory")


class _BasicSerialPortLineEditorNextLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorNextLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorNextLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorNextLine_Object = MibTableColumn
basicSerialPortLineEditorNextLine = _BasicSerialPortLineEditorNextLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 30),
    _BasicSerialPortLineEditorNextLine_Type()
)
basicSerialPortLineEditorNextLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorNextLine.setStatus("mandatory")


class _BasicSerialPortLineEditorPreviousLine_Type(Integer32):
    """Custom type basicSerialPortLineEditorPreviousLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorPreviousLine_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorPreviousLine_Object = MibTableColumn
basicSerialPortLineEditorPreviousLine = _BasicSerialPortLineEditorPreviousLine_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 31),
    _BasicSerialPortLineEditorPreviousLine_Type()
)
basicSerialPortLineEditorPreviousLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorPreviousLine.setStatus("mandatory")


class _BasicSerialPortLineEditorQuotingCharacter_Type(Integer32):
    """Custom type basicSerialPortLineEditorQuotingCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorQuotingCharacter_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorQuotingCharacter_Object = MibTableColumn
basicSerialPortLineEditorQuotingCharacter = _BasicSerialPortLineEditorQuotingCharacter_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 32),
    _BasicSerialPortLineEditorQuotingCharacter_Type()
)
basicSerialPortLineEditorQuotingCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorQuotingCharacter.setStatus("mandatory")


class _BasicSerialPortLineEditorRedisplay_Type(Integer32):
    """Custom type basicSerialPortLineEditorRedisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BasicSerialPortLineEditorRedisplay_Type.__name__ = "Integer32"
_BasicSerialPortLineEditorRedisplay_Object = MibTableColumn
basicSerialPortLineEditorRedisplay = _BasicSerialPortLineEditorRedisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 18, 1, 33),
    _BasicSerialPortLineEditorRedisplay_Type()
)
basicSerialPortLineEditorRedisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicSerialPortLineEditorRedisplay.setStatus("mandatory")


class _BasicConsoleLogoutDisconnect_Type(Integer32):
    """Custom type basicConsoleLogoutDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_BasicConsoleLogoutDisconnect_Type.__name__ = "Integer32"
_BasicConsoleLogoutDisconnect_Object = MibScalar
basicConsoleLogoutDisconnect = _BasicConsoleLogoutDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 1, 19),
    _BasicConsoleLogoutDisconnect_Type()
)
basicConsoleLogoutDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basicConsoleLogoutDisconnect.setStatus("mandatory")
_Queue_ObjectIdentity = ObjectIdentity
queue = _Queue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 2)
)


class _QueueLimit_Type(Integer32):
    """Custom type queueLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_QueueLimit_Type.__name__ = "Integer32"
_QueueLimit_Object = MibScalar
queueLimit = _QueueLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 1),
    _QueueLimit_Type()
)
queueLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueLimit.setStatus("mandatory")
_QueueHigh_Type = Gauge32
_QueueHigh_Object = MibScalar
queueHigh = _QueueHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 2),
    _QueueHigh_Type()
)
queueHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueHigh.setStatus("mandatory")
_QueueNumber_Type = Gauge32
_QueueNumber_Object = MibScalar
queueNumber = _QueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 3),
    _QueueNumber_Type()
)
queueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueNumber.setStatus("mandatory")
_QueueTable_Object = MibTable
queueTable = _QueueTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4)
)
if mibBuilder.loadTexts:
    queueTable.setStatus("mandatory")
_QueueEntry_Object = MibTableRow
queueEntry = _QueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1)
)
queueEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "queueJob"),
)
if mibBuilder.loadTexts:
    queueEntry.setStatus("mandatory")
_QueueJob_Type = Integer32
_QueueJob_Object = MibTableColumn
queueJob = _QueueJob_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 1),
    _QueueJob_Type()
)
queueJob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueJob.setStatus("mandatory")


class _QueueStatus_Type(Integer32):
    """Custom type queueStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_QueueStatus_Type.__name__ = "Integer32"
_QueueStatus_Object = MibTableColumn
queueStatus = _QueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 2),
    _QueueStatus_Type()
)
queueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queueStatus.setStatus("mandatory")


class _QueueSourceName_Type(DisplayString):
    """Custom type queueSourceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_QueueSourceName_Type.__name__ = "DisplayString"
_QueueSourceName_Object = MibTableColumn
queueSourceName = _QueueSourceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 3),
    _QueueSourceName_Type()
)
queueSourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueSourceName.setStatus("mandatory")


class _QueueServiceName_Type(DisplayString):
    """Custom type queueServiceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QueueServiceName_Type.__name__ = "DisplayString"
_QueueServiceName_Object = MibTableColumn
queueServiceName = _QueueServiceName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 4),
    _QueueServiceName_Type()
)
queueServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServiceName.setStatus("mandatory")
_QueueServicePortIndex_Type = Integer32
_QueueServicePortIndex_Object = MibTableColumn
queueServicePortIndex = _QueueServicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 5),
    _QueueServicePortIndex_Type()
)
queueServicePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServicePortIndex.setStatus("mandatory")


class _QueueServicePortName_Type(DisplayString):
    """Custom type queueServicePortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_QueueServicePortName_Type.__name__ = "DisplayString"
_QueueServicePortName_Object = MibTableColumn
queueServicePortName = _QueueServicePortName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 4, 1, 6),
    _QueueServicePortName_Type()
)
queueServicePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queueServicePortName.setStatus("mandatory")
_QueuePortTable_Object = MibTable
queuePortTable = _QueuePortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5)
)
if mibBuilder.loadTexts:
    queuePortTable.setStatus("mandatory")
_QueuePortEntry_Object = MibTableRow
queuePortEntry = _QueuePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1)
)
queuePortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "queuePortIndex"),
)
if mibBuilder.loadTexts:
    queuePortEntry.setStatus("mandatory")
_QueuePortIndex_Type = Integer32
_QueuePortIndex_Object = MibTableColumn
queuePortIndex = _QueuePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1, 1),
    _QueuePortIndex_Type()
)
queuePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    queuePortIndex.setStatus("mandatory")


class _QueuePortQueuing_Type(Integer32):
    """Custom type queuePortQueuing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_QueuePortQueuing_Type.__name__ = "Integer32"
_QueuePortQueuing_Object = MibTableColumn
queuePortQueuing = _QueuePortQueuing_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 2, 5, 1, 2),
    _QueuePortQueuing_Type()
)
queuePortQueuing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuePortQueuing.setStatus("mandatory")
_Menu_ObjectIdentity = ObjectIdentity
menu = _Menu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 3)
)
_MenuNumber_Type = Gauge32
_MenuNumber_Object = MibScalar
menuNumber = _MenuNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 1),
    _MenuNumber_Type()
)
menuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuNumber.setStatus("mandatory")


class _MenuContinuePrompt_Type(DisplayString):
    """Custom type menuContinuePrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MenuContinuePrompt_Type.__name__ = "DisplayString"
_MenuContinuePrompt_Object = MibScalar
menuContinuePrompt = _MenuContinuePrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 2),
    _MenuContinuePrompt_Type()
)
menuContinuePrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuContinuePrompt.setStatus("mandatory")


class _MenuSelectionPrompt_Type(DisplayString):
    """Custom type menuSelectionPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_MenuSelectionPrompt_Type.__name__ = "DisplayString"
_MenuSelectionPrompt_Object = MibScalar
menuSelectionPrompt = _MenuSelectionPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 3),
    _MenuSelectionPrompt_Type()
)
menuSelectionPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuSelectionPrompt.setStatus("mandatory")
_MenuTable_Object = MibTable
menuTable = _MenuTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4)
)
if mibBuilder.loadTexts:
    menuTable.setStatus("mandatory")
_MenuEntry_Object = MibTableRow
menuEntry = _MenuEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1)
)
menuEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "menuIndex"),
)
if mibBuilder.loadTexts:
    menuEntry.setStatus("mandatory")
_MenuIndex_Type = Integer32
_MenuIndex_Object = MibTableColumn
menuIndex = _MenuIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 1),
    _MenuIndex_Type()
)
menuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuIndex.setStatus("mandatory")


class _MenuStatus_Type(Integer32):
    """Custom type menuStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_MenuStatus_Type.__name__ = "Integer32"
_MenuStatus_Object = MibTableColumn
menuStatus = _MenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 2),
    _MenuStatus_Type()
)
menuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuStatus.setStatus("mandatory")


class _MenuText_Type(DisplayString):
    """Custom type menuText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_MenuText_Type.__name__ = "DisplayString"
_MenuText_Object = MibTableColumn
menuText = _MenuText_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 3),
    _MenuText_Type()
)
menuText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuText.setStatus("mandatory")


class _MenuCommand_Type(DisplayString):
    """Custom type menuCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MenuCommand_Type.__name__ = "DisplayString"
_MenuCommand_Object = MibTableColumn
menuCommand = _MenuCommand_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 4, 1, 4),
    _MenuCommand_Type()
)
menuCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuCommand.setStatus("mandatory")
_MenuPortTable_Object = MibTable
menuPortTable = _MenuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5)
)
if mibBuilder.loadTexts:
    menuPortTable.setStatus("mandatory")
_MenuPortEntry_Object = MibTableRow
menuPortEntry = _MenuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1)
)
menuPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "menuPortIndex"),
)
if mibBuilder.loadTexts:
    menuPortEntry.setStatus("mandatory")
_MenuPortIndex_Type = Integer32
_MenuPortIndex_Object = MibTableColumn
menuPortIndex = _MenuPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 1),
    _MenuPortIndex_Type()
)
menuPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    menuPortIndex.setStatus("mandatory")


class _MenuPortMenuStatus_Type(Integer32):
    """Custom type menuPortMenuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("privileged", 3))
    )


_MenuPortMenuStatus_Type.__name__ = "Integer32"
_MenuPortMenuStatus_Object = MibTableColumn
menuPortMenuStatus = _MenuPortMenuStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 3, 5, 1, 2),
    _MenuPortMenuStatus_Type()
)
menuPortMenuStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    menuPortMenuStatus.setStatus("mandatory")
_NetLogin_ObjectIdentity = ObjectIdentity
netLogin = _NetLogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 4)
)
_NetLoginNumber_Type = Integer32
_NetLoginNumber_Object = MibScalar
netLoginNumber = _NetLoginNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 1),
    _NetLoginNumber_Type()
)
netLoginNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginNumber.setStatus("mandatory")
_NetLoginServerTable_Object = MibTable
netLoginServerTable = _NetLoginServerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2)
)
if mibBuilder.loadTexts:
    netLoginServerTable.setStatus("mandatory")
_NetLoginServerEntry_Object = MibTableRow
netLoginServerEntry = _NetLoginServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1)
)
netLoginServerEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "netLoginServerName"),
)
if mibBuilder.loadTexts:
    netLoginServerEntry.setStatus("mandatory")


class _NetLoginServerName_Type(DisplayString):
    """Custom type netLoginServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_NetLoginServerName_Type.__name__ = "DisplayString"
_NetLoginServerName_Object = MibTableColumn
netLoginServerName = _NetLoginServerName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 1),
    _NetLoginServerName_Type()
)
netLoginServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerName.setStatus("mandatory")


class _NetLoginServerStatus_Type(Integer32):
    """Custom type netLoginServerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NetLoginServerStatus_Type.__name__ = "Integer32"
_NetLoginServerStatus_Object = MibTableColumn
netLoginServerStatus = _NetLoginServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 2),
    _NetLoginServerStatus_Type()
)
netLoginServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerStatus.setStatus("mandatory")


class _NetLoginServerPath_Type(DisplayString):
    """Custom type netLoginServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NetLoginServerPath_Type.__name__ = "DisplayString"
_NetLoginServerPath_Object = MibTableColumn
netLoginServerPath = _NetLoginServerPath_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 2, 1, 3),
    _NetLoginServerPath_Type()
)
netLoginServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginServerPath.setStatus("mandatory")
_NetLoginPortTable_Object = MibTable
netLoginPortTable = _NetLoginPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3)
)
if mibBuilder.loadTexts:
    netLoginPortTable.setStatus("mandatory")
_NetLoginPortEntry_Object = MibTableRow
netLoginPortEntry = _NetLoginPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1)
)
netLoginPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "netLoginPortIndex"),
)
if mibBuilder.loadTexts:
    netLoginPortEntry.setStatus("mandatory")
_NetLoginPortIndex_Type = Integer32
_NetLoginPortIndex_Object = MibTableColumn
netLoginPortIndex = _NetLoginPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 1),
    _NetLoginPortIndex_Type()
)
netLoginPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortIndex.setStatus("mandatory")


class _NetLoginPortScriptUse_Type(Integer32):
    """Custom type netLoginPortScriptUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("required", 3))
    )


_NetLoginPortScriptUse_Type.__name__ = "Integer32"
_NetLoginPortScriptUse_Object = MibTableColumn
netLoginPortScriptUse = _NetLoginPortScriptUse_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 2),
    _NetLoginPortScriptUse_Type()
)
netLoginPortScriptUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPortScriptUse.setStatus("mandatory")


class _NetLoginPortScriptEcho_Type(Integer32):
    """Custom type netLoginPortScriptEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_NetLoginPortScriptEcho_Type.__name__ = "Integer32"
_NetLoginPortScriptEcho_Object = MibTableColumn
netLoginPortScriptEcho = _NetLoginPortScriptEcho_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 3),
    _NetLoginPortScriptEcho_Type()
)
netLoginPortScriptEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netLoginPortScriptEcho.setStatus("mandatory")
_NetLoginPortLoaderAddressType_Type = AddressType
_NetLoginPortLoaderAddressType_Object = MibTableColumn
netLoginPortLoaderAddressType = _NetLoginPortLoaderAddressType_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 4),
    _NetLoginPortLoaderAddressType_Type()
)
netLoginPortLoaderAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderAddressType.setStatus("mandatory")
_NetLoginPortLoaderAddress_Type = OctetString
_NetLoginPortLoaderAddress_Object = MibTableColumn
netLoginPortLoaderAddress = _NetLoginPortLoaderAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 5),
    _NetLoginPortLoaderAddress_Type()
)
netLoginPortLoaderAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderAddress.setStatus("mandatory")
_NetLoginPortLoaderFile_Type = DisplayString
_NetLoginPortLoaderFile_Object = MibTableColumn
netLoginPortLoaderFile = _NetLoginPortLoaderFile_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 4, 3, 1, 6),
    _NetLoginPortLoaderFile_Type()
)
netLoginPortLoaderFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netLoginPortLoaderFile.setStatus("mandatory")
_Dial_ObjectIdentity = ObjectIdentity
dial = _Dial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 5)
)
_DialPortTable_Object = MibTable
dialPortTable = _DialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1)
)
if mibBuilder.loadTexts:
    dialPortTable.setStatus("mandatory")
_DialPortEntry_Object = MibTableRow
dialPortEntry = _DialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1)
)
dialPortEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "dialPortIndex"),
)
if mibBuilder.loadTexts:
    dialPortEntry.setStatus("mandatory")
_DialPortIndex_Type = Integer32
_DialPortIndex_Object = MibTableColumn
dialPortIndex = _DialPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 1),
    _DialPortIndex_Type()
)
dialPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialPortIndex.setStatus("mandatory")


class _DialPortDialback_Type(Integer32):
    """Custom type dialPortDialback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_DialPortDialback_Type.__name__ = "Integer32"
_DialPortDialback_Object = MibTableColumn
dialPortDialback = _DialPortDialback_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 2),
    _DialPortDialback_Type()
)
dialPortDialback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialback.setStatus("mandatory")


class _DialPortDialbackTimeout_Type(Integer32):
    """Custom type dialPortDialbackTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_DialPortDialbackTimeout_Type.__name__ = "Integer32"
_DialPortDialbackTimeout_Object = MibTableColumn
dialPortDialbackTimeout = _DialPortDialbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 5, 1, 1, 3),
    _DialPortDialbackTimeout_Type()
)
dialPortDialbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialPortDialbackTimeout.setStatus("mandatory")
_SessionLog_ObjectIdentity = ObjectIdentity
sessionLog = _SessionLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 13, 6)
)


class _SessionLogLimit_Type(Integer32):
    """Custom type sessionLogLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_SessionLogLimit_Type.__name__ = "Integer32"
_SessionLogLimit_Object = MibScalar
sessionLogLimit = _SessionLogLimit_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 1),
    _SessionLogLimit_Type()
)
sessionLogLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sessionLogLimit.setStatus("mandatory")
_SessionLogTable_Object = MibTable
sessionLogTable = _SessionLogTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2)
)
if mibBuilder.loadTexts:
    sessionLogTable.setStatus("mandatory")
_SessionLogEntry_Object = MibTableRow
sessionLogEntry = _SessionLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1)
)
sessionLogEntry.setIndexNames(
    (0, "XYPLEX-CONCATENATED-MIB", "sessionLogIndex"),
)
if mibBuilder.loadTexts:
    sessionLogEntry.setStatus("mandatory")
_SessionLogIndex_Type = Integer32
_SessionLogIndex_Object = MibTableColumn
sessionLogIndex = _SessionLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 1),
    _SessionLogIndex_Type()
)
sessionLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogIndex.setStatus("mandatory")


class _SessionLogConnectionID_Type(Integer32):
    """Custom type sessionLogConnectionID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SessionLogConnectionID_Type.__name__ = "Integer32"
_SessionLogConnectionID_Object = MibTableColumn
sessionLogConnectionID = _SessionLogConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 2),
    _SessionLogConnectionID_Type()
)
sessionLogConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogConnectionID.setStatus("mandatory")
_SessionLogPort_Type = Integer32
_SessionLogPort_Object = MibTableColumn
sessionLogPort = _SessionLogPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 3),
    _SessionLogPort_Type()
)
sessionLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogPort.setStatus("mandatory")


class _SessionLogEvent_Type(Integer32):
    """Custom type sessionLogEvent based on Integer32"""
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
        *(("connectLocal", 2),
          ("connectRemote", 3),
          ("disconnect", 4),
          ("login", 1))
    )


_SessionLogEvent_Type.__name__ = "Integer32"
_SessionLogEvent_Object = MibTableColumn
sessionLogEvent = _SessionLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 4),
    _SessionLogEvent_Type()
)
sessionLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogEvent.setStatus("mandatory")


class _SessionLogEventDetail_Type(Integer32):
    """Custom type sessionLogEventDetail based on Integer32"""
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
              32,
              33,
              34,
              35,
              36)
        )
    )
    namedValues = NamedValues(
        *(("accessDenied", 28),
          ("badCircuitTimer", 15),
          ("badMessageOrSlot", 17),
          ("badPassword", 22),
          ("badServiceClass", 16),
          ("domainTooLong", 32),
          ("duplicateQueueID", 6),
          ("internetConnectDisabled", 36),
          ("noImmeditatAccess", 27),
          ("noNodeResources", 12),
          ("noProgress", 19),
          ("noServiceResourced", 8),
          ("noSuchNode", 33),
          ("noSuchPort", 21),
          ("noSuchService", 24),
          ("noSuchServiceOnNode", 34),
          ("noUsers", 7),
          ("nodeUserdisconnect", 14),
          ("none", 1),
          ("notInQueue", 26),
          ("protocolBadCircuit", 2),
          ("protocolBadCredits", 3),
          ("protocolBadRange", 5),
          ("protocolBadReasonCode", 30),
          ("protocolBadSolicit", 29),
          ("protocolBadStartOrRun", 4),
          ("rejectService", 35),
          ("serverUserDisconnect", 11),
          ("serviceBusy", 23),
          ("serviceDisabled", 25),
          ("serviceNotOnPort", 20),
          ("serviceUnavailable", 10),
          ("serviceUserDisconnect", 9),
          ("systemShutdown", 13),
          ("timeout", 18),
          ("unsupportedTest", 31))
    )


_SessionLogEventDetail_Type.__name__ = "Integer32"
_SessionLogEventDetail_Object = MibTableColumn
sessionLogEventDetail = _SessionLogEventDetail_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 5),
    _SessionLogEventDetail_Type()
)
sessionLogEventDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogEventDetail.setStatus("mandatory")


class _SessionLogUserName_Type(DisplayString):
    """Custom type sessionLogUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionLogUserName_Type.__name__ = "DisplayString"
_SessionLogUserName_Object = MibTableColumn
sessionLogUserName = _SessionLogUserName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 6),
    _SessionLogUserName_Type()
)
sessionLogUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogUserName.setStatus("mandatory")


class _SessionLogRemoteName_Type(DisplayString):
    """Custom type sessionLogRemoteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SessionLogRemoteName_Type.__name__ = "DisplayString"
_SessionLogRemoteName_Object = MibTableColumn
sessionLogRemoteName = _SessionLogRemoteName_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 7),
    _SessionLogRemoteName_Type()
)
sessionLogRemoteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogRemoteName.setStatus("mandatory")
_SessionLogConnectTime_Type = DateTime
_SessionLogConnectTime_Object = MibTableColumn
sessionLogConnectTime = _SessionLogConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 8),
    _SessionLogConnectTime_Type()
)
sessionLogConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogConnectTime.setStatus("mandatory")
_SessionLogDisconnectTime_Type = DateTime
_SessionLogDisconnectTime_Object = MibTableColumn
sessionLogDisconnectTime = _SessionLogDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 9),
    _SessionLogDisconnectTime_Type()
)
sessionLogDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogDisconnectTime.setStatus("mandatory")
_SessionLogInCharacters_Type = Counter32
_SessionLogInCharacters_Object = MibTableColumn
sessionLogInCharacters = _SessionLogInCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 10),
    _SessionLogInCharacters_Type()
)
sessionLogInCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogInCharacters.setStatus("mandatory")
_SessionLogOutCharacters_Type = Counter32
_SessionLogOutCharacters_Object = MibTableColumn
sessionLogOutCharacters = _SessionLogOutCharacters_Object(
    (1, 3, 6, 1, 4, 1, 33, 13, 6, 2, 1, 11),
    _SessionLogOutCharacters_Type()
)
sessionLogOutCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sessionLogOutCharacters.setStatus("mandatory")
_Decnet_ObjectIdentity = ObjectIdentity
decnet = _Decnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14)
)
_Rcp_ObjectIdentity = ObjectIdentity
rcp = _Rcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 14, 1)
)


class _RcpRemoteAddress_Type(OctetString):
    """Custom type rcpRemoteAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_RcpRemoteAddress_Type.__name__ = "OctetString"
_RcpRemoteAddress_Object = MibScalar
rcpRemoteAddress = _RcpRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 14, 1, 1),
    _RcpRemoteAddress_Type()
)
rcpRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcpRemoteAddress.setStatus("mandatory")

# Managed Objects groups


# Notification objects

resourceLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 33, 1, 0, 1)
)
resourceLack.setObjects(
    ("XYPLEX-CONCATENATED-MIB", "resType")
)
if mibBuilder.loadTexts:
    resourceLack.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYPLEX-CONCATENATED-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "DateTime": DateTime,
       "AddressType": AddressType,
       "AutonomousType": AutonomousType,
       "InstancePointer": InstancePointer,
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
       "char": char,
       "charNumber": charNumber,
       "charPortTable": charPortTable,
       "charPortEntry": charPortEntry,
       "charPortIndex": charPortIndex,
       "charPortName": charPortName,
       "charPortType": charPortType,
       "charPortHardware": charPortHardware,
       "charPortReset": charPortReset,
       "charPortAdminStatus": charPortAdminStatus,
       "charPortOperStatus": charPortOperStatus,
       "charPortLastChange": charPortLastChange,
       "charPortInFlowType": charPortInFlowType,
       "charPortOutFlowType": charPortOutFlowType,
       "charPortInFlowState": charPortInFlowState,
       "charPortOutFlowState": charPortOutFlowState,
       "charPortInCharacters": charPortInCharacters,
       "charPortOutCharacters": charPortOutCharacters,
       "charPortAdminOrigin": charPortAdminOrigin,
       "charPortSessionMaximum": charPortSessionMaximum,
       "charPortSessionNumber": charPortSessionNumber,
       "charPortSessionIndex": charPortSessionIndex,
       "charSessTable": charSessTable,
       "charSessEntry": charSessEntry,
       "charSessPortIndex": charSessPortIndex,
       "charSessIndex": charSessIndex,
       "charSessKill": charSessKill,
       "charSessState": charSessState,
       "charSessProtocol": charSessProtocol,
       "charSessOperOrigin": charSessOperOrigin,
       "charSessInCharacters": charSessInCharacters,
       "charSessOutCharacters": charSessOutCharacters,
       "charSessConnectionId": charSessConnectionId,
       "charSessStartTime": charSessStartTime,
       "wellKnownProtocols": wellKnownProtocols,
       "protocolOther": protocolOther,
       "protocolTelnet": protocolTelnet,
       "protocolRlogin": protocolRlogin,
       "protocolLat": protocolLat,
       "protocolX29": protocolX29,
       "protocolVtp": protocolVtp,
       "rs232": rs232,
       "rs232Number": rs232Number,
       "rs232PortTable": rs232PortTable,
       "rs232PortEntry": rs232PortEntry,
       "rs232PortIndex": rs232PortIndex,
       "rs232PortType": rs232PortType,
       "rs232PortInSigNumber": rs232PortInSigNumber,
       "rs232PortOutSigNumber": rs232PortOutSigNumber,
       "rs232PortInSpeed": rs232PortInSpeed,
       "rs232PortOutSpeed": rs232PortOutSpeed,
       "rs232AsyncPortTable": rs232AsyncPortTable,
       "rs232AsyncPortEntry": rs232AsyncPortEntry,
       "rs232AsyncPortIndex": rs232AsyncPortIndex,
       "rs232AsyncPortBits": rs232AsyncPortBits,
       "rs232AsyncPortStopBits": rs232AsyncPortStopBits,
       "rs232AsyncPortParity": rs232AsyncPortParity,
       "rs232AsyncPortAutobaud": rs232AsyncPortAutobaud,
       "rs232AsyncPortParityErrs": rs232AsyncPortParityErrs,
       "rs232AsyncPortFramingErrs": rs232AsyncPortFramingErrs,
       "rs232AsyncPortOverrunErrs": rs232AsyncPortOverrunErrs,
       "rs232SyncPortTable": rs232SyncPortTable,
       "rs232SyncPortEntry": rs232SyncPortEntry,
       "rs232SyncPortIndex": rs232SyncPortIndex,
       "rs232SyncPortClockSource": rs232SyncPortClockSource,
       "rs232SyncPortFrameCheckErrs": rs232SyncPortFrameCheckErrs,
       "rs232SyncPortTransmitUnderrunErrs": rs232SyncPortTransmitUnderrunErrs,
       "rs232SyncPortReceiveOverrunErrs": rs232SyncPortReceiveOverrunErrs,
       "rs232SyncPortInterruptedFrames": rs232SyncPortInterruptedFrames,
       "rs232SyncPortAbortedFrames": rs232SyncPortAbortedFrames,
       "rs232InSigTable": rs232InSigTable,
       "rs232InSigEntry": rs232InSigEntry,
       "rs232InSigPortIndex": rs232InSigPortIndex,
       "rs232InSigName": rs232InSigName,
       "rs232InSigState": rs232InSigState,
       "rs232InSigChanges": rs232InSigChanges,
       "rs232OutSigTable": rs232OutSigTable,
       "rs232OutSigEntry": rs232OutSigEntry,
       "rs232OutSigPortIndex": rs232OutSigPortIndex,
       "rs232OutSigName": rs232OutSigName,
       "rs232OutSigState": rs232OutSigState,
       "rs232OutSigChanges": rs232OutSigChanges,
       "xyplex": xyplex,
       "xSystem": xSystem,
       "resourceLack": resourceLack,
       "sysIdent": sysIdent,
       "sysDefineMode": sysDefineMode,
       "sysDateTime": sysDateTime,
       "sysTimeZone": sysTimeZone,
       "sysLoadSoftware": sysLoadSoftware,
       "sysDump": sysDump,
       "sysMaintenancePassword": sysMaintenancePassword,
       "sysLocalName": sysLocalName,
       "sysSoftwareVersionType": sysSoftwareVersionType,
       "sysSoftwareVersion": sysSoftwareVersion,
       "sysRomVersion": sysRomVersion,
       "sysHardwareType": sysHardwareType,
       "sysHardwareVersion": sysHardwareVersion,
       "sysChassisType": sysChassisType,
       "sysChassisVersion": sysChassisVersion,
       "sysCrash": sysCrash,
       "sysInitialize": sysInitialize,
       "sysInitializeDelay": sysInitializeDelay,
       "sysZeroAll": sysZeroAll,
       "sysZeroBase": sysZeroBase,
       "sysZeroBaseTime": sysZeroBaseTime,
       "sysLoaderName": sysLoaderName,
       "sysLoaderAddressType": sysLoaderAddressType,
       "sysLoaderAddress": sysLoaderAddress,
       "sysDumperAddressType": sysDumperAddressType,
       "sysDumperAddress": sysDumperAddress,
       "sysResourceLacks": sysResourceLacks,
       "sysChassisState": sysChassisState,
       "sysChassisFaultTransitions": sysChassisFaultTransitions,
       "sysResourceNumber": sysResourceNumber,
       "sysFeatureNumber": sysFeatureNumber,
       "resTable": resTable,
       "resEntry": resEntry,
       "resType": resType,
       "resCurrent": resCurrent,
       "resWorst": resWorst,
       "resAdminMaximum": resAdminMaximum,
       "resLacks": resLacks,
       "resLackTime": resLackTime,
       "resOperMaximum": resOperMaximum,
       "featTable": featTable,
       "featEntry": featEntry,
       "featType": featType,
       "featStatus": featStatus,
       "bootControl": bootControl,
       "bootControlLoadInternetFile": bootControlLoadInternetFile,
       "bootControlLoadInternetServer": bootControlLoadInternetServer,
       "bootControlLoadInternetGateway": bootControlLoadInternetGateway,
       "bootControlLoadBootpTftp": bootControlLoadBootpTftp,
       "bootControlLoadTftpDirect": bootControlLoadTftpDirect,
       "bootControlLoadLocal": bootControlLoadLocal,
       "bootControlLoadMop": bootControlLoadMop,
       "bootControlLoadProprietary": bootControlLoadProprietary,
       "bootControlLoadRarpTftp": bootControlLoadRarpTftp,
       "bootControlDumpBootpTftp": bootControlDumpBootpTftp,
       "bootControlDumpLocal": bootControlDumpLocal,
       "bootControlDumpMop": bootControlDumpMop,
       "bootControlDumpProprietary": bootControlDumpProprietary,
       "bootControlDumpRarpTftp": bootControlDumpRarpTftp,
       "bootControlParamBootpTftp": bootControlParamBootpTftp,
       "bootControlParamLocal": bootControlParamLocal,
       "bootControlParamMop": bootControlParamMop,
       "bootControlParamProprietary": bootControlParamProprietary,
       "bootControlParamRarpTftp": bootControlParamRarpTftp,
       "sysInstalledMemory": sysInstalledMemory,
       "characterDep": characterDep,
       "lat": lat,
       "latAnnounceServices": latAnnounceServices,
       "latCircuitTimer": latCircuitTimer,
       "latIdentificationLengthLimit": latIdentificationLengthLimit,
       "latKeepaliveTimer": latKeepaliveTimer,
       "latMulticastTimer": latMulticastTimer,
       "latNodeLimit": latNodeLimit,
       "latNumber": latNumber,
       "latRetransmitLimit": latRetransmitLimit,
       "latLocalServiceGroups": latLocalServiceGroups,
       "latGroupPurge": latGroupPurge,
       "latNodePurge": latNodePurge,
       "latNodesRejected": latNodesRejected,
       "latInMessages": latInMessages,
       "latOutMessages": latOutMessages,
       "latInSessionsAccepted": latInSessionsAccepted,
       "latInSessionsRejected": latInSessionsRejected,
       "latAddressChange": latAddressChange,
       "latInDuplicates": latInDuplicates,
       "latOutRetransmits": latOutRetransmits,
       "latInBadMessages": latInBadMessages,
       "latInBadSlots": latInBadSlots,
       "latInBadMulticasts": latInBadMulticasts,
       "latPortTable": latPortTable,
       "latPortEntry": latPortEntry,
       "latPortIndex": latPortIndex,
       "latPortAuthorizedGroups": latPortAuthorizedGroups,
       "latPortAutoPrompt": latPortAutoPrompt,
       "latPortCurrentGroups": latPortCurrentGroups,
       "latPortRemoteModification": latPortRemoteModification,
       "latOfferedServiceTable": latOfferedServiceTable,
       "latOfferedServiceEntry": latOfferedServiceEntry,
       "latOfferedServiceName": latOfferedServiceName,
       "latOfferedServiceStatus": latOfferedServiceStatus,
       "latOfferedServiceAllowConnections": latOfferedServiceAllowConnections,
       "latOfferedServiceIdentification": latOfferedServiceIdentification,
       "latOfferedServicePassword": latOfferedServicePassword,
       "latOfferedServicePortMap": latOfferedServicePortMap,
       "latOfferedServiceQueuing": latOfferedServiceQueuing,
       "latVisibleServiceTable": latVisibleServiceTable,
       "latVisibleServiceEntry": latVisibleServiceEntry,
       "latVisibleServiceName": latVisibleServiceName,
       "latVisibleServiceStatus": latVisibleServiceStatus,
       "latVisibleServiceNode": latVisibleServiceNode,
       "latVisibleServiceConnectedSessions": latVisibleServiceConnectedSessions,
       "latVisibleServiceIdentification": latVisibleServiceIdentification,
       "latVisibleServiceRating": latVisibleServiceRating,
       "latNodeTable": latNodeTable,
       "latNodeEntry": latNodeEntry,
       "latNodeName": latNodeName,
       "latNodeStatus": latNodeStatus,
       "latNodeConnectedSessions": latNodeConnectedSessions,
       "latNodeAddress": latNodeAddress,
       "latNodeDataLinkFrame": latNodeDataLinkFrame,
       "latNodeIdentification": latNodeIdentification,
       "latNodeGroups": latNodeGroups,
       "latNodeServiceNumber": latNodeServiceNumber,
       "latNodeZero": latNodeZero,
       "latNodeZeroTime": latNodeZeroTime,
       "latNodeInMessages": latNodeInMessages,
       "latNodeOutMessages": latNodeOutMessages,
       "latNodeInSlots": latNodeInSlots,
       "latNodeOutSlots": latNodeOutSlots,
       "latNodeInBytes": latNodeInBytes,
       "latNodeOutBytes": latNodeOutBytes,
       "latNodeAddressChange": latNodeAddressChange,
       "latNodeInDuplicates": latNodeInDuplicates,
       "latNodeOutRetransmits": latNodeOutRetransmits,
       "latNodeInBadMessages": latNodeInBadMessages,
       "latNodeInBadSlots": latNodeInBadSlots,
       "latNodeInSessionsAccepted": latNodeInSessionsAccepted,
       "latNodeInSessionsRejected": latNodeInSessionsRejected,
       "xInternetDep": xInternetDep,
       "bootServer": bootServer,
       "bsBasic": bsBasic,
       "basicLogLimit": basicLogLimit,
       "basicActiveLimit": basicActiveLimit,
       "basicActiveNumber": basicActiveNumber,
       "basicClientNumber": basicClientNumber,
       "basicOffersSent": basicOffersSent,
       "basicEventTotal": basicEventTotal,
       "basicEventPurge": basicEventPurge,
       "activeTable": activeTable,
       "activeEntry": activeEntry,
       "activeIdentificationType": activeIdentificationType,
       "activeIdentification": activeIdentification,
       "activeFunction": activeFunction,
       "activeSoftwareVersionType": activeSoftwareVersionType,
       "activeSoftwareVersion": activeSoftwareVersion,
       "activeParameterVersion": activeParameterVersion,
       "activeCurrentSequence": activeCurrentSequence,
       "activeBytesRemaining": activeBytesRemaining,
       "activeFile": activeFile,
       "activeStatus": activeStatus,
       "activeState": activeState,
       "clientTable": clientTable,
       "clientEntry": clientEntry,
       "clientIdentificationType": clientIdentificationType,
       "clientIdentification": clientIdentification,
       "clientEntryStatus": clientEntryStatus,
       "clientName": clientName,
       "clientLoadFile": clientLoadFile,
       "clientDiagnosticFile": clientDiagnosticFile,
       "clientLoadService": clientLoadService,
       "clientDumpService": clientDumpService,
       "namedTable": namedTable,
       "namedEntry": namedEntry,
       "namedIdentificationType": namedIdentificationType,
       "namedIdentification": namedIdentification,
       "namedEntryStatus": namedEntryStatus,
       "namedName": namedName,
       "namedLoadFile": namedLoadFile,
       "namedDiagnosticFile": namedDiagnosticFile,
       "namedLoadService": namedLoadService,
       "namedDumpService": namedDumpService,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventText": eventText,
       "basicDeviceNumber": basicDeviceNumber,
       "deviceTable": deviceTable,
       "deviceEntry": deviceEntry,
       "deviceIndex": deviceIndex,
       "deviceName": deviceName,
       "deviceDescr": deviceDescr,
       "deviceOperation": deviceOperation,
       "deviceFormat": deviceFormat,
       "deviceProtection": deviceProtection,
       "deviceFormatMedium": deviceFormatMedium,
       "deviceGetFile": deviceGetFile,
       "deviceGetFileHostIdentificationType": deviceGetFileHostIdentificationType,
       "deviceGetFileHostIdentification": deviceGetFileHostIdentification,
       "deviceGetFileName": deviceGetFileName,
       "dump": dump,
       "dumpService": dumpService,
       "dumpDrive": dumpDrive,
       "dumpMerit": dumpMerit,
       "dumpSize": dumpSize,
       "dumpCompleted": dumpCompleted,
       "dumpActive": dumpActive,
       "dumpFileNumber": dumpFileNumber,
       "dumpFileTable": dumpFileTable,
       "dumpFileEntry": dumpFileEntry,
       "dumpFileIdentificationType": dumpFileIdentificationType,
       "dumpFileIdentification": dumpFileIdentification,
       "dumpFileEntryStatus": dumpFileEntryStatus,
       "dumpFileCreation": dumpFileCreation,
       "dumpFileSize": dumpFileSize,
       "load": load,
       "loadService": loadService,
       "loadMerit": loadMerit,
       "loadCompleted": loadCompleted,
       "loadActive": loadActive,
       "loadFileNumber": loadFileNumber,
       "loadFileTable": loadFileTable,
       "loadFileEntry": loadFileEntry,
       "loadFileName": loadFileName,
       "loadFileCreation": loadFileCreation,
       "loadFileSize": loadFileSize,
       "loadFileSoftwareVersionType": loadFileSoftwareVersionType,
       "loadFileSoftwareVersion": loadFileSoftwareVersion,
       "param": param,
       "paramService": paramService,
       "paramDefaultService": paramDefaultService,
       "paramDrive": paramDrive,
       "paramActive": paramActive,
       "paramStorageActive": paramStorageActive,
       "paramFileNumber": paramFileNumber,
       "paramFileTable": paramFileTable,
       "paramFileEntry": paramFileEntry,
       "paramFileIdentificationType": paramFileIdentificationType,
       "paramFileIdentification": paramFileIdentification,
       "paramFileEntryStatus": paramFileEntryStatus,
       "paramFileWrite": paramFileWrite,
       "paramFileSize": paramFileSize,
       "paramFileParameterVersion": paramFileParameterVersion,
       "paramClient": paramClient,
       "paramClientLoaderName": paramClientLoaderName,
       "paramClientLoaderAddressType": paramClientLoaderAddressType,
       "paramClientLoaderAddress": paramClientLoaderAddress,
       "paramClientParameterVersion": paramClientParameterVersion,
       "paramClientUpdateTime": paramClientUpdateTime,
       "paramClientServerCheck": paramClientServerCheck,
       "paramClientCheckInterval": paramClientCheckInterval,
       "paramClientCheckNow": paramClientCheckNow,
       "paramClientServerLimit": paramClientServerLimit,
       "paramClientRetransmitInterval": paramClientRetransmitInterval,
       "paramClientRetransmitLimit": paramClientRetransmitLimit,
       "paramClientState": paramClientState,
       "paramClientProtocolErrors": paramClientProtocolErrors,
       "paramClientServerRejects": paramClientServerRejects,
       "paramClientServerNumber": paramClientServerNumber,
       "paramServerTable": paramServerTable,
       "paramServerEntry": paramServerEntry,
       "paramServerName": paramServerName,
       "paramServerEntryStatus": paramServerEntryStatus,
       "paramServerAddressType": paramServerAddressType,
       "paramServerAddress": paramServerAddress,
       "paramServerStoredVersion": paramServerStoredVersion,
       "paramServerStoredTime": paramServerStoredTime,
       "paramServerStoredStatus": paramServerStoredStatus,
       "paramServerStoredFailure": paramServerStoredFailure,
       "xInternet": xInternet,
       "xIp": xIp,
       "ipGatewayAddress1": ipGatewayAddress1,
       "ipGatewayAddress2": ipGatewayAddress2,
       "ipAutoSubnetMask": ipAutoSubnetMask,
       "ipReassembly": ipReassembly,
       "xTcp": xTcp,
       "tcpPortTable": tcpPortTable,
       "tcpPortEntry": tcpPortEntry,
       "tcpPortIndex": tcpPortIndex,
       "tcpPortConnectByAddress": tcpPortConnectByAddress,
       "tcpPortWindowSize": tcpPortWindowSize,
       "snmpAgent": snmpAgent,
       "snmpAgentGetCommunity": snmpAgentGetCommunity,
       "snmpAgentSetCommunity": snmpAgentSetCommunity,
       "snmpAgentTrapCommunity": snmpAgentTrapCommunity,
       "snmpAgentGetClientNumber": snmpAgentGetClientNumber,
       "snmpAgentSetClientNumber": snmpAgentSetClientNumber,
       "snmpAgentTrapClientNumber": snmpAgentTrapClientNumber,
       "getClientTable": getClientTable,
       "getClientEntry": getClientEntry,
       "getClientIndex": getClientIndex,
       "getClientEntryStatus": getClientEntryStatus,
       "getClientAddressType": getClientAddressType,
       "getClientAddress": getClientAddress,
       "setClientTable": setClientTable,
       "setClientEntry": setClientEntry,
       "setClientIndex": setClientIndex,
       "setClientEntryStatus": setClientEntryStatus,
       "setClientAddressType": setClientAddressType,
       "setClientAddress": setClientAddress,
       "trapClientTable": trapClientTable,
       "trapClientEntry": trapClientEntry,
       "trapClientIndex": trapClientIndex,
       "trapClientEntryStatus": trapClientEntryStatus,
       "trapClientAddressType": trapClientAddressType,
       "trapClientAddress": trapClientAddress,
       "domainResolver": domainResolver,
       "domainResolverSuffix": domainResolverSuffix,
       "domainResolverAddress1": domainResolverAddress1,
       "domainResolverAddress2": domainResolverAddress2,
       "domainResolverTtl": domainResolverTtl,
       "domainResolverNameNumber": domainResolverNameNumber,
       "nameTable": nameTable,
       "nameEntry": nameEntry,
       "nameName": nameName,
       "nameAddress": nameAddress,
       "nameStatus": nameStatus,
       "nameSource": nameSource,
       "nameTtl": nameTtl,
       "slip": slip,
       "slipTable": slipTable,
       "slipEntry": slipEntry,
       "slipIndex": slipIndex,
       "slipState": slipState,
       "slipLocalAddress": slipLocalAddress,
       "slipRemoteAddress": slipRemoteAddress,
       "slipMask": slipMask,
       "slipPortPacketsReceived": slipPortPacketsReceived,
       "slipPortPacketsSent": slipPortPacketsSent,
       "slipPortPacketsDiscarded": slipPortPacketsDiscarded,
       "slipPortPacketLengthErrors": slipPortPacketLengthErrors,
       "slipPortPacketChecksumErrors": slipPortPacketChecksumErrors,
       "slipNetworkPacketsReceived": slipNetworkPacketsReceived,
       "slipNetworkPacketsSent": slipNetworkPacketsSent,
       "slipNetworkPacketsDiscarded": slipNetworkPacketsDiscarded,
       "telnet": telnet,
       "telnetPortTable": telnetPortTable,
       "telnetPortEntry": telnetPortEntry,
       "telnetPortIndex": telnetPortIndex,
       "telnetPortIncomingTcpPort": telnetPortIncomingTcpPort,
       "telnetPortOutgoingTcpPort": telnetPortOutgoingTcpPort,
       "telnetPortNewlineTranslation": telnetPortNewlineTranslation,
       "telnetPortTerminalType": telnetPortTerminalType,
       "telnetPortEorReflection": telnetPortEorReflection,
       "telnetPortBinaryMode": telnetPortBinaryMode,
       "telnetSerialPortTable": telnetSerialPortTable,
       "telnetSerialPortEntry": telnetSerialPortEntry,
       "telnetSerialPortIndex": telnetSerialPortIndex,
       "telnetSerialPortOptionDisplay": telnetSerialPortOptionDisplay,
       "telnetSerialPortCsiEscape": telnetSerialPortCsiEscape,
       "telnetSerialPortEchoMode": telnetSerialPortEchoMode,
       "telnetSerialPortNewlineMode": telnetSerialPortNewlineMode,
       "telnetSerialPortTransmitMode": telnetSerialPortTransmitMode,
       "telnetSerialPortTransmitCharacterTimes": telnetSerialPortTransmitCharacterTimes,
       "telnetSerialPortAbortOutputCharacter": telnetSerialPortAbortOutputCharacter,
       "telnetSerialPortAttentionCharacter": telnetSerialPortAttentionCharacter,
       "telnetSerialPortEraseKeyCharacter": telnetSerialPortEraseKeyCharacter,
       "telnetSerialPortEraseLineCharacter": telnetSerialPortEraseLineCharacter,
       "telnetSerialPortInterruptCharacter": telnetSerialPortInterruptCharacter,
       "telnetSerialPortQueryCharacter": telnetSerialPortQueryCharacter,
       "telnetSerialPortSynchronizeCharacter": telnetSerialPortSynchronizeCharacter,
       "tn3270": tn3270,
       "tn3270DeviceNumber": tn3270DeviceNumber,
       "tn3270LanguageNumber": tn3270LanguageNumber,
       "tn3270PortKeymapStatus": tn3270PortKeymapStatus,
       "tn3270DeviceTable": tn3270DeviceTable,
       "tn3270DeviceEntry": tn3270DeviceEntry,
       "tn3270DeviceName": tn3270DeviceName,
       "tn3270DeviceStatus": tn3270DeviceStatus,
       "tn3270DeviceType": tn3270DeviceType,
       "tn3270Device3278Model": tn3270Device3278Model,
       "tn3270DeviceKeyNumber": tn3270DeviceKeyNumber,
       "tn3270DeviceScreenNumber": tn3270DeviceScreenNumber,
       "tn3270KeyTable": tn3270KeyTable,
       "tn3270KeyEntry": tn3270KeyEntry,
       "tn3270KeyDeviceName": tn3270KeyDeviceName,
       "tn3270KeyName": tn3270KeyName,
       "tn3270KeyStatus": tn3270KeyStatus,
       "tn3270KeyCharacterSequence": tn3270KeyCharacterSequence,
       "tn3270KeyDescription": tn3270KeyDescription,
       "tn3270ScreenTable": tn3270ScreenTable,
       "tn3270ScreenEntry": tn3270ScreenEntry,
       "tn3270ScreenDeviceName": tn3270ScreenDeviceName,
       "tn3270ScreenActionName": tn3270ScreenActionName,
       "tn3270ScreenStatus": tn3270ScreenStatus,
       "tn3270ScreenCharacterSequence": tn3270ScreenCharacterSequence,
       "tn3270LanguageTable": tn3270LanguageTable,
       "tn3270LanguageEntry": tn3270LanguageEntry,
       "tn3270LanguageName": tn3270LanguageName,
       "tn3270LanguageStatus": tn3270LanguageStatus,
       "eToALanguageTable": eToALanguageTable,
       "eToALanguageEntry": eToALanguageEntry,
       "eToALanguageName": eToALanguageName,
       "eToAOffset": eToAOffset,
       "eToAValue": eToAValue,
       "aToELanguageTable": aToELanguageTable,
       "aToELanguageEntry": aToELanguageEntry,
       "aToELanguageName": aToELanguageName,
       "aToEOffset": aToEOffset,
       "aToEValue": aToEValue,
       "tn3270PortTable": tn3270PortTable,
       "tn3270PortEntry": tn3270PortEntry,
       "tn3270PortIndex": tn3270PortIndex,
       "tn3270PortDeviceName": tn3270PortDeviceName,
       "tn3270PortLanguageName": tn3270PortLanguageName,
       "tn3270PortExtendedAttributes": tn3270PortExtendedAttributes,
       "tn3270PortEorNegotiation": tn3270PortEorNegotiation,
       "tn3270PortErrorLock": tn3270PortErrorLock,
       "kerberos": kerberos,
       "kerbStatus": kerbStatus,
       "kerbRealm": kerbRealm,
       "kerbQueryLimit": kerbQueryLimit,
       "kerbMasterName": kerbMasterName,
       "kerbServerName1": kerbServerName1,
       "kerbServerName2": kerbServerName2,
       "kerbInsecureLogins": kerbInsecureLogins,
       "kerbSecureLogins": kerbSecureLogins,
       "kerbSecureLoginsFailed": kerbSecureLoginsFailed,
       "kerbPasswordChangeFailed": kerbPasswordChangeFailed,
       "kerbError": kerbError,
       "kerbErrorTime": kerbErrorTime,
       "kerbMasterAccess": kerbMasterAccess,
       "kerbMasterAccessFailed": kerbMasterAccessFailed,
       "kerbServerAccess1": kerbServerAccess1,
       "kerbServerAccessFailed1": kerbServerAccessFailed1,
       "kerbServerAccess2": kerbServerAccess2,
       "kerbServerAccessFailed2": kerbServerAccessFailed2,
       "kerbPortTable": kerbPortTable,
       "kerbPortEntry": kerbPortEntry,
       "kerbPortIndex": kerbPortIndex,
       "kerbPortStatus": kerbPortStatus,
       "portSecurity": portSecurity,
       "psEntryNumber": psEntryNumber,
       "psEntryNumberLimit": psEntryNumberLimit,
       "psEntryInvalidIndex": psEntryInvalidIndex,
       "psPortTable": psPortTable,
       "psPortEntry": psPortEntry,
       "psPortIndex": psPortIndex,
       "psPortDefaultInboundAccess": psPortDefaultInboundAccess,
       "psPortDefaultOutboundAccess": psPortDefaultOutboundAccess,
       "psTable": psTable,
       "psEntry": psEntry,
       "psEntryIndex": psEntryIndex,
       "psEntryStatus": psEntryStatus,
       "psEntryAddress": psEntryAddress,
       "psEntryMask": psEntryMask,
       "psEntryAccess": psEntryAccess,
       "psEntryDirection": psEntryDirection,
       "psEntryPortMap": psEntryPortMap,
       "xremote": xremote,
       "xremoteServerName1": xremoteServerName1,
       "xremoteServerName2": xremoteServerName2,
       "xremoteServerAccess1": xremoteServerAccess1,
       "xremoteServerAccessFailed1": xremoteServerAccessFailed1,
       "xremoteServerAccess2": xremoteServerAccess2,
       "xremoteServerAccessFailed2": xremoteServerAccessFailed2,
       "xremoteSessions": xremoteSessions,
       "xremotePortTable": xremotePortTable,
       "xremotePortEntry": xremotePortEntry,
       "xremotePortIndex": xremotePortIndex,
       "xremotePortXremote": xremotePortXremote,
       "xremotePortXdmQuery": xremotePortXdmQuery,
       "xremotePortXdmHost": xremotePortXdmHost,
       "xremoteServerClients": xremoteServerClients,
       "rotary": rotary,
       "rotaryNumber": rotaryNumber,
       "rotaryTable": rotaryTable,
       "rotaryEntry": rotaryEntry,
       "rotaryAddress": rotaryAddress,
       "rotaryStatus": rotaryStatus,
       "rotaryPortMap": rotaryPortMap,
       "xEgp": xEgp,
       "ospf": ospf,
       "routerIp": routerIp,
       "routerUdp": routerUdp,
       "routerPolicy": routerPolicy,
       "ethernet": ethernet,
       "etherTable": etherTable,
       "etherEntry": etherEntry,
       "etherIndex": etherIndex,
       "etherAlignmentErrors": etherAlignmentErrors,
       "etherFCSErrors": etherFCSErrors,
       "etherTxTable": etherTxTable,
       "etherTxEntry": etherTxEntry,
       "etherTxIndex": etherTxIndex,
       "etherTxSingleCollisionFrames": etherTxSingleCollisionFrames,
       "etherTxMultipleCollisionFrames": etherTxMultipleCollisionFrames,
       "etherMulticastTable": etherMulticastTable,
       "etherMulticastEntry": etherMulticastEntry,
       "etherMulticastIndex": etherMulticastIndex,
       "etherMulticastBytesIn": etherMulticastBytesIn,
       "etherMulticastBytesOut": etherMulticastBytesOut,
       "etherXTxTable": etherXTxTable,
       "etherXTxEntry": etherXTxEntry,
       "etherXTxIndex": etherXTxIndex,
       "etherXTxExcessiveCollisions": etherXTxExcessiveCollisions,
       "bootClient": bootClient,
       "bootClientStatus": bootClientStatus,
       "character": character,
       "basic": basic,
       "basicBroadcast": basicBroadcast,
       "basicErrorReport": basicErrorReport,
       "basicLock": basicLock,
       "basicInactivityTimer": basicInactivityTimer,
       "basicPasswordRetryLimit": basicPasswordRetryLimit,
       "basicPrivilegedPassword": basicPrivilegedPassword,
       "basicLoginPassword": basicLoginPassword,
       "basicLoginPrompt": basicLoginPrompt,
       "basicWelcome": basicWelcome,
       "basicActivePorts": basicActivePorts,
       "basicActivePortsHigh": basicActivePortsHigh,
       "basicActiveUsers": basicActiveUsers,
       "basicActiveUsersHigh": basicActiveUsersHigh,
       "basicSessions": basicSessions,
       "basicSessionsHigh": basicSessionsHigh,
       "basicSessionsLimit": basicSessionsLimit,
       "basicPortTable": basicPortTable,
       "basicPortEntry": basicPortEntry,
       "basicPortIndex": basicPortIndex,
       "basicPortDefaultDestAction": basicPortDefaultDestAction,
       "basicPortDefaultDestProtocol": basicPortDefaultDestProtocol,
       "basicPortDefaultDestName": basicPortDefaultDestName,
       "basicPortDefaultDestLATNodeName": basicPortDefaultDestLATNodeName,
       "basicPortDefaultDestLATPortName": basicPortDefaultDestLATPortName,
       "basicPortAutoConnect": basicPortAutoConnect,
       "basicPortAutoLogin": basicPortAutoLogin,
       "basicPortBroadcast": basicPortBroadcast,
       "basicPortConnectResume": basicPortConnectResume,
       "basicPortDialup": basicPortDialup,
       "basicPortIdleTimeout": basicPortIdleTimeout,
       "basicPortInactivityLogout": basicPortInactivityLogout,
       "basicPortLossNotification": basicPortLossNotification,
       "basicPortMessageCodes": basicPortMessageCodes,
       "basicPortMultisessions": basicPortMultisessions,
       "basicPortDefaultUserName": basicPortDefaultUserName,
       "basicPortVerification": basicPortVerification,
       "basicPortDefaultProtocol": basicPortDefaultProtocol,
       "basicPortLogins": basicPortLogins,
       "basicPortRemoteSessions": basicPortRemoteSessions,
       "basicPortIdleTimeouts": basicPortIdleTimeouts,
       "basicPortStatus": basicPortStatus,
       "basicPortLastInCharacter": basicPortLastInCharacter,
       "basicPortLastOutCharacter": basicPortLastOutCharacter,
       "basicPortActiveUserName": basicPortActiveUserName,
       "basicPortDefaultSessionMode": basicPortDefaultSessionMode,
       "basicPortZero": basicPortZero,
       "basicPortZeroTime": basicPortZeroTime,
       "basicSerialPortTable": basicSerialPortTable,
       "basicSerialPortEntry": basicSerialPortEntry,
       "basicSerialPortIndex": basicSerialPortIndex,
       "basicSerialPortBreak": basicSerialPortBreak,
       "basicSerialPortInterrupts": basicSerialPortInterrupts,
       "basicSerialPortNoLoss": basicSerialPortNoLoss,
       "basicSerialPortPause": basicSerialPortPause,
       "basicSerialPortPrompt": basicSerialPortPrompt,
       "basicSerialPortTerminalType": basicSerialPortTerminalType,
       "basicSerialPortTypeaheadLimit": basicSerialPortTypeaheadLimit,
       "basicSerialPortBackwardSwitch": basicSerialPortBackwardSwitch,
       "basicSerialPortForwardSwitch": basicSerialPortForwardSwitch,
       "basicSerialPortLocalSwitch": basicSerialPortLocalSwitch,
       "basicSerialPortModemControl": basicSerialPortModemControl,
       "basicSerialPortSignalCheck": basicSerialPortSignalCheck,
       "basicSerialPortDSRLogout": basicSerialPortDSRLogout,
       "basicSerialPortDSRObserve": basicSerialPortDSRObserve,
       "basicSerialPortDCDTimeout": basicSerialPortDCDTimeout,
       "basicSerialPortDTRAssert": basicSerialPortDTRAssert,
       "basicSerialPortLimitedCommands": basicSerialPortLimitedCommands,
       "basicSerialPortLimitedView": basicSerialPortLimitedView,
       "basicSerialPortPassword": basicSerialPortPassword,
       "basicSerialPortLineEditor": basicSerialPortLineEditor,
       "basicSerialPortLineEditorBackspace": basicSerialPortLineEditorBackspace,
       "basicSerialPortLineEditorBeginning": basicSerialPortLineEditorBeginning,
       "basicSerialPortLineEditorCancel": basicSerialPortLineEditorCancel,
       "basicSerialPortLineEditorDeleteBeginning": basicSerialPortLineEditorDeleteBeginning,
       "basicSerialPortLineEditorDeleteLine": basicSerialPortLineEditorDeleteLine,
       "basicSerialPortLineEditorEnd": basicSerialPortLineEditorEnd,
       "basicSerialPortLineEditorForward": basicSerialPortLineEditorForward,
       "basicSerialPortLineEditorInsertToggle": basicSerialPortLineEditorInsertToggle,
       "basicSerialPortLineEditorNextLine": basicSerialPortLineEditorNextLine,
       "basicSerialPortLineEditorPreviousLine": basicSerialPortLineEditorPreviousLine,
       "basicSerialPortLineEditorQuotingCharacter": basicSerialPortLineEditorQuotingCharacter,
       "basicSerialPortLineEditorRedisplay": basicSerialPortLineEditorRedisplay,
       "basicConsoleLogoutDisconnect": basicConsoleLogoutDisconnect,
       "queue": queue,
       "queueLimit": queueLimit,
       "queueHigh": queueHigh,
       "queueNumber": queueNumber,
       "queueTable": queueTable,
       "queueEntry": queueEntry,
       "queueJob": queueJob,
       "queueStatus": queueStatus,
       "queueSourceName": queueSourceName,
       "queueServiceName": queueServiceName,
       "queueServicePortIndex": queueServicePortIndex,
       "queueServicePortName": queueServicePortName,
       "queuePortTable": queuePortTable,
       "queuePortEntry": queuePortEntry,
       "queuePortIndex": queuePortIndex,
       "queuePortQueuing": queuePortQueuing,
       "menu": menu,
       "menuNumber": menuNumber,
       "menuContinuePrompt": menuContinuePrompt,
       "menuSelectionPrompt": menuSelectionPrompt,
       "menuTable": menuTable,
       "menuEntry": menuEntry,
       "menuIndex": menuIndex,
       "menuStatus": menuStatus,
       "menuText": menuText,
       "menuCommand": menuCommand,
       "menuPortTable": menuPortTable,
       "menuPortEntry": menuPortEntry,
       "menuPortIndex": menuPortIndex,
       "menuPortMenuStatus": menuPortMenuStatus,
       "netLogin": netLogin,
       "netLoginNumber": netLoginNumber,
       "netLoginServerTable": netLoginServerTable,
       "netLoginServerEntry": netLoginServerEntry,
       "netLoginServerName": netLoginServerName,
       "netLoginServerStatus": netLoginServerStatus,
       "netLoginServerPath": netLoginServerPath,
       "netLoginPortTable": netLoginPortTable,
       "netLoginPortEntry": netLoginPortEntry,
       "netLoginPortIndex": netLoginPortIndex,
       "netLoginPortScriptUse": netLoginPortScriptUse,
       "netLoginPortScriptEcho": netLoginPortScriptEcho,
       "netLoginPortLoaderAddressType": netLoginPortLoaderAddressType,
       "netLoginPortLoaderAddress": netLoginPortLoaderAddress,
       "netLoginPortLoaderFile": netLoginPortLoaderFile,
       "dial": dial,
       "dialPortTable": dialPortTable,
       "dialPortEntry": dialPortEntry,
       "dialPortIndex": dialPortIndex,
       "dialPortDialback": dialPortDialback,
       "dialPortDialbackTimeout": dialPortDialbackTimeout,
       "sessionLog": sessionLog,
       "sessionLogLimit": sessionLogLimit,
       "sessionLogTable": sessionLogTable,
       "sessionLogEntry": sessionLogEntry,
       "sessionLogIndex": sessionLogIndex,
       "sessionLogConnectionID": sessionLogConnectionID,
       "sessionLogPort": sessionLogPort,
       "sessionLogEvent": sessionLogEvent,
       "sessionLogEventDetail": sessionLogEventDetail,
       "sessionLogUserName": sessionLogUserName,
       "sessionLogRemoteName": sessionLogRemoteName,
       "sessionLogConnectTime": sessionLogConnectTime,
       "sessionLogDisconnectTime": sessionLogDisconnectTime,
       "sessionLogInCharacters": sessionLogInCharacters,
       "sessionLogOutCharacters": sessionLogOutCharacters,
       "decnet": decnet,
       "rcp": rcp,
       "rcpRemoteAddress": rcpRemoteAddress}
)
